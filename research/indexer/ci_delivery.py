import re
import shutil
import tempfile
from pathlib import Path

from indexer.ci import public_only, publish_worktree, reference_worktree, restore
from indexer.reference import export_cache, reference_path, replace_reference
from indexer.store import LOCAL, digest, read_json, write_json
from matcher.comparison_pages import COMPARISON_LINK, DIRECTIONS, carry_links, disconnect, overlay
from matcher.tracking_pages import link


def checkpoint_key(tag):
    match = re.fullmatch(r'native-analysis-(\d+\.\d+\.\d+)-([A-Za-z0-9_-]+)-([a-f0-9]{16})', tag)
    if not match:
        raise ValueError('Invalid native analysis Release tag')
    return match.groups()


def restore_completed(tag, root):
    version, architecture, revision = checkpoint_key(tag)
    restore(root, tag, revision)
    state = root / 'ci-status.json'
    if not state.is_file() or read_json(state).get('complete') is not True:
        raise ValueError('A completed checkpoint is required')
    data = read_json(root / 'ci-plan.json')['input']
    identity = read_json(root / 'identity.json')
    expected = (version, architecture, revision, data['librarySha256'], data['versionCode'], data['library'])
    actual = tuple(identity[key] for key in ('version', 'architecture', 'analysis_revision', 'sha256', 'version_code', 'library'))
    if actual != expected or (data['versionName'], data['architecture']) != (version, architecture):
        raise ValueError('Completed checkpoint identity differs from its Release tag')
    return data, identity


def same_reference(manifest, expected):
    return all(manifest.get(key) == value for key, value in expected.items())


def link_comparison(source):
    readme = source / 'README.md'
    link_line = COMPARISON_LINK
    if link_line not in readme.read_text(encoding='utf-8-sig'):
        with readme.open('a', encoding='utf-8') as output:
            output.write('\n' + link_line + '\n')


def publish_materials(tag, publish):
    public_only()
    LOCAL.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='ci-materials-', dir=LOCAL) as directory:
        root = Path(directory) / 'cache'
        data, identity = restore_completed(tag, root)
        source, report = export_cache(root, Path(directory) / 'reference')
        report.update(source_archive_sha256=data['archiveSha256'], source_version_code=data['versionCode'],
                      comparison_state='pending')
        write_json(source / 'manifest.json', report)
        if publish:
            revision = identity['analysis_revision']
            work = reference_worktree(revision + '-materials')
            reference = work / 'research/reference'
            manifest = reference / reference_path(identity) / 'manifest.json'
            expected = {key: report[key] for key in ('source_database_sha256', 'analysis_revision', 'source_archive_sha256', 'source_version_code')}
            previous = read_json(manifest) if manifest.is_file() else None
            if previous and same_reference(previous, expected):
                comparison = manifest.with_name('comparison.md')
                if previous.get('tracking_format') == 2:
                    keys = ('comparison_state', 'tracking_format', 'tracking_policy', 'tracking_run', 'tracking_page', 'tracking_sources')
                    report.update({key: previous[key] for key in keys if key in previous})
                    if report.get('tracking_page'):
                        target = work / report['tracking_page']
                        overlay(source / 'README.md', 'tracking',
                                f'[バージョン間の関数追跡]({link(target, manifest.with_name("README.md"))})',
                                '## アドレス索引\n')
                elif previous.get('comparison_state') == 'complete' and comparison.is_file():
                    shutil.copyfile(comparison, source / comparison.name)
                    link_comparison(source)
                    report['comparison_state'] = 'complete'
                elif previous.get('comparison_state') == 'no_baseline':
                    report['comparison_state'] = 'no_baseline'
                carry_links(manifest.parent, source)
                write_json(source / 'manifest.json', report)
            else:
                for replaced in manifest.parent.parent.glob('*/manifest.json'):
                    for direction in DIRECTIONS:
                        disconnect(reference, replaced.parent, direction, replacing=True)
            replace_reference(source, reference)
            publish_worktree(work, f'Publish native references {revision}')


def publish_comparison(tag, publish):
    from indexer.ci_tracking import publish_tracking
    publish_tracking(tag, publish)
