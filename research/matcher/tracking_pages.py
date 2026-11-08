import html
import json
import os
import tempfile
from collections import defaultdict
from itertools import islice
from pathlib import Path

from indexer.reference import fenced, reference_path
from indexer.store import digest, read_json, write_json
from indexer.upstream import tracking_sources
from matcher.comparison_pages import COMPARISON_LINK, DIRECTIONS, catalog_path, disconnect, overlay
from matcher.structure import reader


PAGE_SIZE = 100
GROUPS = {'structure_or_reference_change': '構造・参照差',
          'register_sensitive': 'レジスタ割当差を含む候補', 'reference_sensitive': '参照アドレスに依存する差',
          'machine_only_observed': '機械語差のみを観測',
          'machine_cfg_equal': '命令バイト・CFG形状の一致', 'no_difference_in_scope': '検査範囲で差分なし',
          'unavailable': '未検証・解析不能'}
PRIORITY = """EXISTS (SELECT 1 FROM json_each(l.evidence,'$.changes') AS item
    WHERE item.value IN ('operation_sequence','operation_order','branch_condition_or_target','call',
                         'control_flow_count','memory_write_count','memory_read_count','comparison'))"""


def groups():
    yield 'logic_change_candidate', 'priority', 'ロジック変更候補（優先確認）', f'AND {PRIORITY}'
    yield 'logic_change_candidate', 'operands', '定数・オペランドの変更候補', f'AND NOT {PRIORITY}'
    yield from ((status, status, heading, '') for status, heading in GROUPS.items())


def link(target, page):
    return Path(os.path.relpath(target, page.parent)).as_posix()


def write_page(path, lines):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8-sig', newline='\n')


def label(text):
    return html.escape(str(text)).replace('|', '&#124;').replace('[', '&#91;').replace(']', '&#93;').replace('\n', ' ')


def render(database, repository, destination, asset_url, reference_url=None):
    if destination.exists():
        existing = read_json(destination / 'manifest.json')
        if existing['database_sha256'] != digest(database) or not (destination / 'README.md').is_file():
            raise ValueError('Published tracking directory belongs to a different or incomplete result')
        return read_json(destination / 'summary.json')
    destination.parent.mkdir(parents=True, exist_ok=True)
    # 同じ深さの一時ディレクトリで、版資料への相対リンクを保ったまま生成する。
    with tempfile.TemporaryDirectory(prefix='.tracking-', dir=destination.parent) as temporary:
        staged = Path(temporary)
        result = render_pages(database, repository, staged, asset_url, reference_url)
        staged.rename(destination)
    return result


def render_pages(database, repository, destination, asset_url, reference_url):
    with reader(database) as db:
        result = json.loads(db.execute("SELECT value FROM metadata WHERE key='result'").fetchone()[0])
        if result['complete'] is not True or result['format'] != 2:
            raise ValueError('A completed v2 tracking database is required')
        versions = dict(db.execute('SELECT id,version FROM datasets'))
        nodes = {(i, a): (name, repository / ref) for i, a, name, ref in db.execute(
            'SELECT dataset,address,name,reference FROM nodes')}
        for _, target in nodes.values():
            if not target.is_file():
                raise ValueError(f'Tracking link target is missing: {target}')
        outgoing, incoming = defaultdict(set), defaultdict(set)
        for dataset, owner, callee in db.execute('SELECT dataset,owner,callee FROM xrefs WHERE callee IS NOT NULL'):
            if (dataset, callee) in nodes:
                outgoing[dataset, owner].add(callee)
                incoming[dataset, callee].add(owner)

        def node(number, address, page, *, named=False):
            if address is None:
                return '—'
            name, target = nodes[number, address]
            url = reference_url + target.relative_to(repository).as_posix() if reference_url else link(target, page)
            return f'[`{address}`]({url})' + (f' {label(name[:140])}' if named else '')

        def call_context(number, address, page):
            rows = []
            for heading, graph in (('呼出元', incoming), ('呼出先', outgoing)):
                functions = sorted(graph[number, address])
                rows.append(f'{heading} {len(functions)}件 ' + ' '.join(node(number, a, page) for a in functions[:5]))
            return ' · '.join(rows)

        def paged(index, title, slug, heading, rows, body):
            rows = iter(rows)
            number = 1
            while chunk := list(islice(rows, PAGE_SIZE)):
                page = index.parent / f'{slug}-{number:04d}.md'
                lines = [f'# {title} · {heading} ({number})', '', '[一覧の目次](README.md)', '']
                for row in chunk:
                    lines.extend(body(row, page))
                write_page(page, lines)
                yield f'- [{heading} {number}]({page.name}) · {len(chunk)}件'
                number += 1

        root = destination / 'README.md'
        indices = ['# ネイティブ関数のバージョン間追跡', '',
                   f'[追跡SQLite]({asset_url}) · [集計と出典](summary.json)', '',
                   f'SQLite SHA-256 `{digest(database)}`', '',
                   '関係は根拠付きの推定です。変更候補は検査範囲と合わせて読みます。',
                   '構造とP-codeの一致だけで実行時の挙動は確定しません。', '', '## 連続版の比較', '']
        for pair, i, j, summary in db.execute("SELECT pair,older,newer,summary FROM pairs WHERE role='adjacent' ORDER BY older"):
            title = f"v{versions[i]} → v{versions[j]}"
            page = destination / pair / 'README.md'
            indices.append(f'- [{title}]({link(page, root)})')
            pair_index = [f'# {title}', '', '[追跡の目次](../README.md)', '', '## 処理・構造の差と対応根拠', '']
            for status, slug, heading, condition in groups():
                rows = db.execute(f"""SELECT l.old,l.new,l.evidence,r.reason,
                        EXISTS (SELECT 1 FROM conflict_edges c WHERE c.pair=l.pair AND c.old=l.old AND c.new=l.new)
                    FROM logic l JOIN relations r ON l.pair=r.pair AND l.old=r.old AND l.new=r.new
                    WHERE l.pair=? AND l.status=? AND r.verdict='accepted' {condition} ORDER BY l.old""", (pair, status))

                def pair_row(row, detail):
                    a, b, raw, reason, conflict = row
                    record = json.loads(raw)
                    tags = ', '.join(record.get('changes', ()))
                    extra = [f"`{record['scope']}`", *(f"`{value}`" for value in record.get('warnings', ())),
                             *([f"`{record['structural_candidate']}`"] if 'structural_candidate' in record else []),
                             *(['`reordered`'] if record.get('order_changed') else []),
                             *(['**経路矛盾あり**'] if conflict else [])]
                    lines = [f'### {node(i, a, detail)} → {node(j, b, detail, named=True)}', '',
                             f'根拠 `{reason}` · ' + ' · '.join(extra), '',
                             f'- 旧版 {call_context(i, a, detail)}', f'- 新版 {call_context(j, b, detail)}', '']
                    if tags:
                        lines.extend([f'変更の種類 {tags}', ''])
                    sample = []
                    for change in record.get('details', ())[:3]:
                        sample.extend('- ' + label(site) + ' ' + json.dumps(op, ensure_ascii=False)
                                      for site, op in change['old'][:4])
                        sample.extend('+ ' + label(site) + ' ' + json.dumps(op, ensure_ascii=False)
                                      for site, op in change['new'][:4])
                    if sample:
                        lines.extend([fenced('\n'.join(sample), 'diff'), ''])
                    return lines

                pair_index.extend(paged(page, title, slug, heading, rows, pair_row))
            pair_index.extend(['', '## 競合・未確定と再調査の優先順', '',
                               '分割・統合・インライン化候補を先に並べています。詳細根拠と全参照はSQLiteで調べられます。', ''])
            reviews = db.execute("""SELECT side,address,kind,targets,evidence FROM review WHERE pair=?
                ORDER BY CASE WHEN kind IN ('split_candidate','merge_candidate','inline_candidate','outline_candidate')
                              THEN 0 WHEN kind='competing_candidates' THEN 1 ELSE 2 END,side,address""", (pair,))

            def review_row(row, detail):
                side, address, kind, targets, raw = row
                first, second = (i, j) if side == 0 else (j, i)
                target_links = ' '.join(node(second, a, detail) for a in json.loads(targets))
                return [f'### v{versions[first]} {node(first, address, detail, named=True)}', '',
                        f'`{kind}` {target_links}', '', call_context(first, address, detail), '',
                        fenced(json.dumps(json.loads(raw), ensure_ascii=False, indent=2), 'json')]

            pair_index.extend(paged(page, title, 'review', '追加調査', reviews, review_row))
            pair_index.extend(['', '## 集計・検証', '', fenced(json.dumps(json.loads(summary), ensure_ascii=False, indent=2), 'json')])
            write_page(page, pair_index)
        indices.extend(['', '## 3版経路の検証', '',
                        '直接経路は検証に用います。一致した経路も共通の解析器に依存します。', '',
                        fenced(json.dumps(result['cycles'], ensure_ascii=False, indent=2), 'json')])
        rows = db.execute("""SELECT older,middle,newer,old,middle_address,via,direct,state,temporal
            FROM cycles WHERE state IN ('conflict','gap_candidate') OR temporal!='' ORDER BY state,older,old""")
        cycle_index = destination / 'cycles/README.md'

        def cycle_row(row, detail):
            i, j, k, a, b, via, direct, state, temporal = row
            return [f'- `{state}` {temporal} · {node(i, a, detail)} → {node(j, b, detail)} → {node(k, via, detail)}'
                    f' · 直接経路 {node(k, direct, detail)}']

        write_page(cycle_index, ['# 3版経路の矛盾・再登場・一時変化候補', '', '[追跡の目次](../README.md)', '',
            *paged(cycle_index, '3版経路', 'review', '確認候補', rows, cycle_row)])
        indices.extend(['', f'[矛盾・再登場・一時変化候補]({link(cycle_index, root)})'])
        write_page(root, indices)
        write_json(destination / 'summary.json', result)
        write_json(destination / 'manifest.json', {'format': 2, 'run': result['run'], 'database_sha256': digest(database)})
    return result


def retire_legacy(reference, identities):
    # v2の全リンク先が揃った後、旧形式が管理していた差分とリンクだけを外す。
    paths = {reference / reference_path(identity) for identity in identities}
    for source in sorted(paths):
        for direction in DIRECTIONS:
            catalog = catalog_path(source, direction)
            if catalog.is_file() and reference / reference_path(read_json(catalog)['peer']) in paths:
                disconnect(reference, source, direction)
        if catalog_path(source, 'previous').is_file():
            continue
        (source / 'comparison.md').unlink(missing_ok=True)
        readme = source / 'README.md'
        before = readme.read_bytes()
        after = before.replace(('\n' + COMPARISON_LINK + '\n').encode(), b'')
        if before != after:
            readme.write_bytes(after)


def attach(repository, destination, result):
    reference = repository / 'research/reference'
    for source in result['sources']:
        identity = source['identity']
        manifest = read_json(reference / reference_path(identity) / 'manifest.json')
        if (manifest['source_database_sha256'], manifest['analysis_revision']) != (
                source['cache_sha256'], identity['analysis_revision']):
            raise ValueError('Published version changed during tracking')
    identities = [source['identity'] for source in result['sources']]
    retire_legacy(reference, identities)
    for i, source in enumerate(result['sources']):
        directory = reference / reference_path(source['identity'])
        page = directory / 'README.md'
        overlay(page, 'tracking', f'[バージョン間の関数追跡]({link(destination / "README.md", page)})', '## アドレス索引\n')
        manifest = read_json(directory / 'manifest.json')
        manifest.update(comparison_state='complete' if i else manifest.get('comparison_state', 'no_baseline'),
                        tracking_format=2, tracking_run=result['run'],
                        tracking_page=(destination / 'README.md').relative_to(repository).as_posix(),
                        tracking_sources=tracking_sources(identities[:i + 1]))
        write_json(directory / 'manifest.json', manifest)
    root = repository / 'research/comparisons'
    write_page(root / 'README.md', ['# ネイティブ関数の追跡資料', '', *(
        f'- [{path.parent.relative_to(root).as_posix()}]({link(path, root / "README.md")})'
        for path in sorted(root.glob('*/*/README.md')))])
