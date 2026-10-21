"""保存済み現版照合結果とSQLiteの0番台全件を比較する。"""
import argparse
import json
from pathlib import Path
import sqlite3
import struct

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--data-dir',type=Path,required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parents[2]
witness=json.loads((root/'research/.local/stages-1572-band0.json').read_text(encoding='utf-8-sig'))
pointer=json.loads((args.data_dir/'current.json').read_text(encoding='utf-8-sig'))
path=args.data_dir/'official'/pointer['regions']['jp']
db=sqlite3.connect(path.as_uri()+'?mode=ro',uri=True)
schema=db.execute('pragma user_version').fetchone()[0]
assert schema in [6,7]
metadata=dict(db.execute('select key,value from metadata'))
assert metadata['version']==witness['version']
assert metadata['build_id']==witness['build']['buildId']
assert db.execute('select count(*) from stage_map').fetchone()[0]==len(witness['maps'])
assert db.execute('select count(*) from stage').fetchone()[0]==len(witness['stages'])
count=0
for stage in witness['stages']:
    rows=db.execute('select source_row,raw_cells,enemy_raw,count,first_raw,interval_min_raw,interval_max_raw,castle,layer_min,layer_max,boss,hp_percent,score,attack_percent,after_castle,kills from stage_spawn where map_id=? and stage_index=? order by position',(stage['map'],stage['stage'])).fetchall()
    assert len(rows)==len(stage['spawns'])
    for saved,expected in zip(rows,stage['spawns']):
        line,cells,*values=saved
        for column in [2,3,4]:values[column]*=2
        assert line==expected['line'] and values==expected['loaded'],(stage['map'],stage['stage'],line)
        original=[int(cell) if cell.strip() else None for cell in json.loads(cells)]
        assert original==expected['cells']
        count+=1
    stored=db.execute('select settings_raw,header_raw,rewards_raw,metadata_row from stage where map_id=? and stage_index=?',(stage['map'],stage['stage'])).fetchone()
    for cells,expected in zip(stored[:3],[stage['settings'],stage['header'],stage['rewards']]):
        assert [int(cell) if cell.strip() else None for cell in json.loads(cells)]==expected['cells']
    assert stored[3]==stage['rewards']['line']
for entry in witness['maps']:
    actual=[row[0] for row in db.execute('select multiplier from stage_crown where map_id=? order by crown',(entry['id'],))]
    assert actual==entry['nativeCrowns']
for name,source in witness['sources'].items():
    assert db.execute('select sha256 from source_file where path=?',(name,)).fetchone()[0]==source['sha256'],name
assert db.execute("select count(*) from progression_stage where source_path like 'Data/MapStageDataPR_%' and map_id/1000 != 39").fetchone()[0]==0
report={'maps':len(witness['maps']),'stages':len(witness['stages']),'spawns':count,'crowns':sum(len(row['nativeCrowns']) for row in witness['maps']),'sources':len(witness['sources']),'database':str(path)}
if schema==7:
    materials=json.loads((root/'research/.local/materials-1572.json').read_text(encoding='utf-8-sig'))
    f32=lambda value:struct.unpack('<f',struct.pack('<f',float(value)))[0]
    for profile in materials['profiles']:
        saved=db.execute('select source_row,raw_cells,miss from stage_material_profile where map_id=?',(profile['id'],)).fetchone()
        assert saved[0]==profile['line'] and json.loads(saved[1])==profile['raw'] and saved[2]==int(profile['raw'][13])
        actual=[r[0] for r in db.execute('select multiplier from stage_material_crown where map_id=? order by crown',(profile['id'],))]
        assert actual==list(map(f32,profile['raw'][1:5]))
        actual=[r[0] for r in db.execute('select count from stage_material_count where map_id=? order by stage_index',(profile['id'],))]
        assert actual==list(map(f32,profile['raw'][5:13]))
        actual=db.execute('select slot,item_id,weight from stage_material_weight where map_id=? order by slot',(profile['id'],)).fetchall()
        assert actual==[(slot,materials['itemIds'][slot],int(value)) for slot,value in enumerate(profile['raw'][14:])]
    for name,source in materials['sources'].items():
        assert db.execute('select sha256 from source_file where path=?',(name,)).fetchone()[0]==source['sha256']
    report['materials']={table:db.execute('select count(*) from '+table).fetchone()[0] for table in ['stage_material_profile','stage_material_crown','stage_material_count','stage_material_weight']}
version='0.1.8' if schema==7 else '0.1.7'
(root/('research/.local/stage-database-'+version+'.json')).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
print(json.dumps(report))
