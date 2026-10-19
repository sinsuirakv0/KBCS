import argparse
import csv
import json
import shutil
import subprocess
import sys
import time
import zipfile
from contextlib import closing
from pathlib import Path

from indexer.run import headless, locked
from indexer.store import LOCAL, configure_output, connect, digest, import_index, read_json, sync_results, write_json


def recover_failed(root, config):
    # 構文木を省く標準設定と、推論・分割を抑える設定を有限回だけ試す。
    checkpoint = root / 'recovery-summary.json'
    attempts = read_json(checkpoint) if checkpoint.exists() else []
    for style in ('decompile', 'conservative', 'minimal'):
        if any(attempt['style'] == style for attempt in attempts):
            continue
        sync_results(root)
        with closing(connect(root / 'cache.sqlite')) as db:
            failed = db.execute("SELECT count(*) FROM functions WHERE external=0 AND status='failed'").fetchone()[0]
        if not failed:
            break
        path = root / f'recovery-{style}.json'
        write_json(path, config | {'decompiler_style': style})
        subprocess.run([sys.executable, '-m', 'indexer.run', '--config', str(path),
                        'decompile', '--cache', str(root), '--all', '--retry-failed'], check=True)
        attempts.append({'style': style, 'requested': failed})
        write_json(checkpoint, attempts)
    return attempts


def build_reference(root):
    # 大きな疑似コードを連結せず、索引と関数別ファイルを参照資料にする。
    sync_results(root)
    identity = read_json(root / 'identity.json')
    with closing(connect(root / 'cache.sqlite')) as db:
        with db:
            db.execute("UPDATE functions SET status='external' WHERE external=1")
            db.execute("UPDATE functions SET confidence='low' WHERE status='cached' AND error LIKE 'Recovered with %'")
        with (root / 'catalog.tsv').open('w', encoding='utf-8-sig', newline='') as stream:
            writer = csv.writer(stream, delimiter='\t')
            writer.writerow(('address', 'name', 'bytes', 'external', 'thunk', 'status', 'confidence', 'file', 'error'))
            writer.writerows(db.execute('SELECT address,name,size,external,thunk,status,confidence,file,error FROM functions ORDER BY address'))
        with (root / 'external-functions.tsv').open('w', encoding='utf-8-sig', newline='') as stream:
            writer = csv.writer(stream, delimiter='\t')
            writer.writerow(('address', 'name'))
            writer.writerows(db.execute('SELECT address,name FROM functions WHERE external=1 ORDER BY name'))
        counts = dict(db.execute('SELECT status,count(*) FROM functions WHERE external=0 GROUP BY status'))
        external = db.execute('SELECT count(*) FROM functions WHERE external=1').fetchone()[0]
        low_confidence = db.execute("SELECT count(*) FROM functions WHERE confidence='low'").fetchone()[0]
        missing = [dict(row) for row in db.execute("SELECT address,name,status,error,file FROM functions WHERE external=0 AND status!='cached'")]
    for path in (root / 'code').glob('*.c'):
        if not path.stat().st_size:
            raise ValueError(f'Empty pseudocode: {path}')
    report = {'cache': str(root), 'version': identity['version'], 'architecture': identity['architecture'],
              'sha256': identity['sha256'], 'internal': counts, 'external': external,
              'low_confidence_recovered': low_confidence, 'unresolved': missing,
              'code_files': sum(1 for _ in (root / 'code').glob('*.c')),
              'code_bytes': sum(p.stat().st_size for p in (root / 'code').glob('*.c'))}
    if report['code_files'] != counts.get('cached', 0):
        raise ValueError('Pseudocode file count does not match the index')
    write_json(root / 'reference-summary.json', report)
    guide = f'''# ネイティブコード参考資料

対象: {identity['version']} / {identity['architecture']} / {identity.get('library', 'libnative-lib.so')}

SO SHA-256: `{identity['sha256']}`

内部関数: 保存済み{counts.get('cached', 0)}、失敗{counts.get('failed', 0)}、未処理{counts.get('pending', 0)}。外部関数: {external}。

- [全関数索引](catalog.tsv): アドレス・関数名・サイズ・状態・ファイルパス。
- [疑似コード](code/): アドレス別のCファイル。
- [外部関数](external-functions.tsv): 実装が対象SOに含まれない関数。
- [集計と未解決一覧](reference-summary.json): 失敗理由とアセンブリのパス。
- `cache.sqlite`: 関数・文字列・参照・呼出関係の検索索引。
- `backup-project.zip`: 自動解析完了後のGhidraプロジェクト。

リポジトリのルートから `python research/cli/cache.py stats`、`find <名前>`、`strings <文字列>`、`code <アドレス>`、`callers <アドレス>`、`callees <アドレス>` を実行できます。Ghidraの起動は不要です。
失敗した関数は `failures` で調べ、`assembly <アドレス>` で命令一覧を参照できます。

疑似コードはGhidraによる復元で、型・名前・処理の意味は未確認です。アドレスはこの解析状態のGhidraアドレスを使います。元のSOと版・SHA-256を対応させて参照してください。
'''
    (root / 'README.md').write_text(guide, encoding='utf-8-sig')
    return report


def main():
    configure_output()
    parser = argparse.ArgumentParser(description='Complete analysis and cache every internal function in a separate revision')
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--cache', required=True, type=Path)
    args = parser.parse_args()
    source = args.cache.resolve()
    root = source.with_name(source.name + '-complete')
    root.mkdir(exist_ok=True)
    config = read_json(args.config) | {'analysis_timeout_seconds': 0, 'batch_timeout_seconds': 0, 'timeout_seconds': 0}
    identity = read_json(source / 'identity.json')
    config['program'] = identity.get('library', config['program'])
    write_json(root / 'config.json', config)
    with locked(root / 'complete.lock'):
        start_file = root / 'workflow-start.json'
        if not start_file.exists():
            previous = read_json(root / 'progress.json') if (root / 'progress.json').exists() else {}
            write_json(start_file, {'started_unix': previous.get('started_unix', time.time())})
        tick = read_json(start_file)['started_unix']
        if not (root / 'project').exists():
            size = sum(p.stat().st_size for p in (source / 'project').rglob('*') if p.is_file())
            if shutil.disk_usage(root).free < size * 3 + 512 * 1024**2:
                raise RuntimeError('Insufficient disk space for project copy and backup')
            shutil.copytree(source / 'project', root / 'project')
        if not (root / 'analysis-complete.json').exists():
            write_json(root / 'progress.json', {'stage': 'analysis', 'started_unix': tick})
            with locked(root / 'writer.lock'):
                metrics = headless(config, root, Path(identity['snapshot']), 'index', 0, analyze_existing=True)
                with (root / 'index.jsonl').open(encoding='utf-8-sig') as stream:
                    header = json.loads(stream.readline())
                if header['analysis_timed_out']:
                    raise RuntimeError('Analysis did not complete')
                backup = root / 'backup-project.zip'
                temporary = backup.with_suffix('.partial')
                with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_STORED) as archive:
                    for path in (root / 'project').rglob('*'):
                        if path.is_file():
                            archive.write(path, path.relative_to(root / 'project'))
                temporary.replace(backup)
                identity = identity | {'snapshot': str(backup), 'snapshot_sha256': digest(backup),
                                       'analysis_timed_out': False, 'previous_cache': str(source),
                                       'revision': 'complete', 'snapshot_format': 'project_zip'}
                metrics['functions'] = import_index(root, identity)
                write_json(root / 'identity.json', identity)
                write_json(root / 'analysis-complete.json', metrics)
        write_json(root / 'progress.json', {'stage': 'decompile', 'started_unix': tick})
        subprocess.run([sys.executable, '-m', 'indexer.run', '--config', str(root / 'config.json'),
                        'decompile', '--cache', str(root), '--all'], check=True)
        recover_failed(root, config)
        report = build_reference(root)
        if report['internal'].get('pending', 0):
            raise RuntimeError('Pending internal functions remain')
        report['workflow_seconds'] = time.time()-tick
        write_json(root / 'progress.json', {'stage': 'complete', **report})
        write_json(LOCAL / 'reference.json', {'cache': str(root), 'version': identity['version'],
                   'architecture': identity['architecture'], 'sha256': identity['sha256']})
        print(json.dumps({key: value for key, value in report.items() if key != 'unresolved'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
