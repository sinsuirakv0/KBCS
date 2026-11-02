"""JP15.7.2のコンボ図鑑・キャラ情報で使用する原画と定義を同期する。"""
import argparse
import csv
import io
import json
from pathlib import Path
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / 'research/verify'))
from stages import Assets, SHA, digest

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('assets', type=Path)
parser.add_argument('--apk', type=Path, default=root / 'research/.local/apk/150702/app.apk')
args = parser.parse_args()
assets = Assets(args.assets)
destination = root / 'ui/images/native-combo'
destination.mkdir(parents=True, exist_ok=True)
result = {'version': '15.7.2', 'nativeSha256': SHA, 'atlases': {}, 'sources': {}}


def data(key):
    entry = assets.files[key]
    path = (assets.root / entry['path']).resolve()
    path.relative_to(assets.root)
    value = path.read_bytes()
    assert len(value) == entry['size'] and digest(value) == entry['sha256'], key
    result['sources'][key] = entry
    return value


for stem in ['img005_1', 'img006_ja', 'img008_ja', 'img024_ja', 'img015', 'img016', 'img029_ja', 'img034', 'img050_02', 'img102', 'equipment_attribute', 'equipment_effect', 'equipment_grade', 'equipment_shadow']:
    image = 'Image/' + stem + '.png'
    cut = 'ImageData/' + stem + '.imgcut'
    raw = data(image)
    (destination / (stem + '.png')).write_bytes(raw)
    lines = data(cut).decode('utf-8-sig').splitlines()
    rects = [[int(v) for v in line.split(',')[:4]] for line in lines[4:4 + int(lines[3])]]
    result['atlases'][stem] = {'url': '/images/native-combo/' + stem + '.png', 'rects': rects}
filter_rows = list(csv.reader(io.StringIO(data('Data/ComboFiltering.tsv').decode('utf-8-sig')), delimiter='\t'))[1:]
result['filters'] = [{'id': int(row[0]), 'types': [int(v) for v in row[1:]]} for row in filter_rows]
result['filterLabels'] = {}
for kind in [value for row in result['filters'] for value in row['types']]:
    name = f'Combo_name_{kind:03}.png'
    (destination / name).write_bytes(data('Map/' + name))
    result['filterLabels'][str(kind)] = '/images/native-combo/' + name
localization = dict(line.split('\t', 1) for line in data('res/localizable.tsv').decode('utf-8-sig').splitlines() if '\t' in line)
result['texts'] = {key: value for key, value in localization.items() if key.startswith('nyancombo_')}
definitions=list(csv.reader(io.StringIO(data('Data/Gatyaitembuy.csv').decode('utf-8-sig'))))[1:]
result['currencies']={'xp':int(definitions[6][3]),'catfood':int(definitions[22][3])}
verified=json.loads((args.apk.parent/'verified.json').read_text(encoding='utf-8-sig'))
assert verified['version']['versionCode']==1507021
assert digest(args.apk.read_bytes())==verified['version']['mergedApkSha256']
with zipfile.ZipFile(args.apk) as archive:
    cancel=archive.read('assets/cancel.png')
(destination/'cancel.png').write_bytes(cancel)
result['sources']['assets/cancel.png']={'apkSha256':verified['version']['mergedApkSha256'],'sha256':digest(cancel)}
for key, path in [('attributes', 'Data/nyankoPictureBookData_Attribute.csv'), ('abilities', 'Data/nyankoPictureBookData_EffectAbility.csv')]:
    result[key] = [[int(v) for v in row] for row in csv.reader(io.StringIO(data(path).decode('utf-8-sig')))]
icons = json.loads((root / 'crates/kbcs-data/resources/property-icons.json').read_text(encoding='utf-8-sig'))
icons['delay-immune'] = 391
result['abilityKeys'] = [[key for key, cut in icons.items() if cut == row[5]] for row in result['abilities']]
constants = json.loads((root / 'native/kbcs-core/resources/interface.json').read_text(encoding='utf-8-sig'))
assert constants['nativeSha256'] == SHA
result['orbColors'] = constants['orbColors']
definition = '// JP15.7.2、00abb824で読み込む表示順・分類・原画cut。sync-combo-ui.pyで同期。\n'
definition += 'static constexpr int infoAbilities[][3]={\n' + ',\n'.join(' {' + ','.join(map(str, [row[1], row[2], row[5]])) + '}' for row in result['abilities']) + '\n};\n'
(root / 'native/kbcs-core/src/interface_data.inc').write_text(definition, encoding='utf-8-sig')
(destination / 'manifest.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8-sig')
