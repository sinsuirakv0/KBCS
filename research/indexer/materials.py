import argparse
import json
import tarfile
from pathlib import Path

from indexer.store import LOCAL, configure_output, digest, write_json


def selected_files(include_binaries=False):
    # プロジェクト実体はバックアップZIPと重複するため保存を一本化する。
    for path in sorted((LOCAL / 'cache').rglob('*')):
        relative = path.relative_to(LOCAL)
        if path.is_file() and 'project' not in relative.parts and path.suffix not in ('.lock', '.partial'):
            yield path
    for directory in ('backups', 'apk'):
        for path in sorted((LOCAL / directory).rglob('*')):
            if not path.is_file():
                continue
            if directory == 'apk' and not include_binaries and path.suffix not in ('.json', '.xml', '.yml'):
                continue
            yield path
    for name in ('environment.json', 'mcp-tool-names.json', 'reference.json'):
        path = LOCAL / name
        if path.exists():
            yield path


def main():
    configure_output()
    parser = argparse.ArgumentParser(description='Pack local research materials for a private release')
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--include-binaries', action='store_true')
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    entries = []
    partial = output.with_suffix(output.suffix + '.partial')
    with tarfile.open(partial, 'w:gz', compresslevel=1) as archive:
        for path in selected_files(args.include_binaries):
            name = 'research/.local/' + path.relative_to(LOCAL).as_posix()
            entries.append({'path': name, 'bytes': path.stat().st_size, 'sha256': digest(path)})
            archive.add(path, arcname=name, recursive=False)
    partial.replace(output)
    manifest = output.with_name(output.name + '.manifest.json')
    write_json(manifest, {'archive': output.name, 'sha256': digest(output),
                         'bytes': output.stat().st_size, 'include_binaries': args.include_binaries,
                         'project_storage': 'backup-project.zip; duplicate live project excluded',
                         'files': entries})
    print(json.dumps({'archive': str(output), 'bytes': output.stat().st_size,
                      'files': len(entries), 'manifest': str(manifest)}))


if __name__ == '__main__':
    main()
