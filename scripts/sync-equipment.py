"""採用元を検証し、編成用のキャラ別本能玉スロット定義を更新する。"""
import argparse
import json
import sys
from pathlib import Path

root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'research/verify'))
from stages import Assets

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('assets',type=Path)
args=parser.parse_args()
assets=Assets(args.assets)
entries={str(row['cells'][0]):{'count':row['cells'][1],'conditions':row['cells'][2:]} for row in assets.numeric('Data/equipmentslot.csv')}
assert all(0<entry['count']<=2 for entry in entries.values())
value={'version':assets.current['versionName'],'versionCode':assets.current['versionCode'],'buildId':assets.current['buildId'],'source':assets.sources['Data/equipmentslot.csv'],'native':['00660ab4','0066141c'],'entries':entries}
output=root/'crates/kbcs-data/resources/unit-equipment-slots.json'
output.write_text(json.dumps(value,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
print(f'Equipment slots: {len(entries)} verified units')
