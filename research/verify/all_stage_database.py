"""全番台SQLiteを、同版原本とARM64共通読込の保存済み証跡へ全件照合する。"""
import argparse,csv,hashlib,json,re,sqlite3
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--data-dir',type=Path,required=True)
parser.add_argument('--assets',type=Path,required=True)
args=parser.parse_args()
from stages import ROOT,SHA,Assets,read_json,digest
assets=Assets(args.assets);witness=read_json(ROOT/'research/.local/stage-bands-1572.json');assert witness['sha256']==SHA
pointer=read_json(args.data_dir/'current.json');path=args.data_dir/'official'/pointer['regions']['jp']
db=sqlite3.connect(path.resolve().as_uri()+'?mode=ro',uri=True)
assert db.execute('pragma user_version').fetchone()[0]==8
assert db.execute('pragma integrity_check').fetchone()[0]=='ok'
assert not db.execute('pragma foreign_key_check').fetchall()
metadata=dict(db.execute('select key,value from metadata'));assert metadata['version']=='15.7.2' and metadata['importer_version'] in ['9','10']
assert metadata['build_id']==assets.current['buildId']
actual={p for (p,) in db.execute('select path from stage_definition')};assert actual==set(witness['definitions'])
spawns=0;headers=0
for name,expected in witness['definitions'].items():
 saved=db.execute('select settings_raw,header_raw,header_count,numeric_terminator from stage_definition where region="jp" and path=?',(name,)).fetchone()
 header=expected['headers'];skip=len(header)
 assert saved[2]==skip and saved[3]==expected['numericTerminator'],name
 assert json.loads(saved[0])==(header[0]['raw'] if skip==2 else [])
 assert json.loads(saved[1])==header[skip-1]['raw'];headers+=1
 raw_lines=assets.text(name).splitlines()
 actual=db.execute('select source_row,raw_cells,enemy_raw,count,first_raw,interval_min_raw,interval_max_raw,castle,layer_min,layer_max,boss,hp_percent,score,attack_percent,after_castle,kills from stage_definition_spawn where region="jp" and definition_path=? order by position',(name,)).fetchall()
 assert len(actual)==len(expected['spawns']),name
 for row,original in zip(actual,expected['spawns']):
  assert row[0]==original['line']
  raw=next(csv.reader([raw_lines[row[0]-1].split('//',1)[0].strip()]))
  assert json.loads(row[1])==raw,(name,row[0],'raw')
  loaded=list(row[2:]);loaded[2]*=2;loaded[3]*=2;loaded[4]*=2
  assert loaded==original['native'],(name,row[0],loaded,original['native'])
  spawns+=1
for name,source in witness['sources'].items():
 saved=db.execute('select sha256,bytes from source_file where path=?',(name,)).fetchone();assert saved is not None,name
 assert saved[0]==source['sha256']==digest(saved[1]),name
 assert assets.files[name]['sha256']==saved[0],name
# 一覧メタと定義の型付き列を元の物理行へ戻して照合する。
source_lines={}
for row in db.execute('select s.map_id,s.stage_index,s.metadata_row,s.rewards_raw,s.energy,s.xp_raw,s.width,s.castle_hp,s.spawn_min,s.spawn_max,s.background,s.max_enemies,s.castle_raw,s.time_raw,s.boss_guard,s.no_continue,e.metadata_path,e.definition_path,e.listed from stage s join stage_entry e using(region,map_id,stage_index)'):
 map_id,index,line,raw,energy,xp,*tail=row;physical=tail[:10];name,definition_path,listed=tail[10:]
 if listed:
  if name not in source_lines:source_lines[name]=assets.text(name).splitlines()
  original=next(csv.reader([source_lines[name][line-1].split('//',1)[0].strip()]))
  assert json.loads(raw)==original,(map_id,index,'metadata')
  assert [energy,xp]==[int(v) if v.strip() else None for v in original[:2]],(map_id,index,'energy/xp')
 else:assert line==0 and energy is None and xp is None and json.loads(raw)==[]
 if definition_path:
  definition=witness['definitions'][definition_path];definition_headers=definition['headers'];header=definition_headers[-1]['raw']
  numeric=lambda value:int(value.strip()) if value.strip() and value!='.' else 0
  expected=[numeric(v) for v in header[:9]]
  expected.append(numeric(definition_headers[0]['raw'][1]) if len(definition_headers)==2 else 0)
  assert physical==expected,(map_id,index,'physics',physical,expected)
 else:assert all(value is None for value in physical),(map_id,index,'unresolved')
# 一覧外定義とテンプレートを失っていないこと、クエストに架空の固定定義を付けないこと。
assert db.execute("select count(*) from stage_entry where listed=0 and map_id in (1268,1325,13038)").fetchone()[0]==7
assert db.execute("select count(*) from stage_definition where path like 'Data/stageL%'").fetchone()[0]==113
assert db.execute('select count(*) from stage_entry where map_id in (16000,33000) and definition_path is not null').fetchone()[0]==0
assert db.execute('select count(*) from stage_variant v left join stage_definition d on d.region=v.region and d.path=v.definition_path where d.path is null').fetchone()[0]==0
# 数値終端が架空ステージへ混入しない。元の不正セルは原文を保持する。
assert db.execute('select count(*) from stage where energy<0').fetchone()[0]==0
assert db.execute("select json_extract(raw_cells,'$[10]') from stage_definition_spawn where definition_path='Data/stageRS111_00.csv' and source_row=12").fetchone()[0]=='.'
assert db.execute('select count(*) from stage_reward where item_id<0 or amount<=0').fetchone()[0]==0
assert db.execute('select count(*) from stage_reward where kind not in (\'normal\',\'weight\',\'score\',\'clear\')').fetchone()[0]==0
# 各面の原本セルから報酬型と元列を独立に再構成し、全保存行を比較する。
clear_path='Data/MapStageDataClearCountReward.json'
clear=json.loads(assets.text(clear_path)).get('MapID',{}) if clear_path in assets.files else {}
reward_count=0
for map_id,index,raw_cells,mode,score_id in db.execute('select s.map_id,s.stage_index,s.rewards_raw,m.mode,m.score_id from stage s join stage_map m on m.id=s.map_id and m.region=s.region'):
 raw=json.loads(raw_cells);values=[int(v.strip()) if v.strip() else None for v in raw]
 get=lambda c,default=0:values[c] if c<len(values) and values[c] is not None else default
 expected=[];reward_mode=get(8)
 if reward_mode in [-3,-4]:
  columns=[]
  for column in [5,*range(9,39,3)]:
   if get(column,-1)<0:break
   columns.append(column)
 else:
  count=1 if reward_mode<0 or get(9,-1)<0 else 2 if get(12,-1)<0 else 3
  columns=[5,9,12][:count]
 def add(column,kind):
  if column+2<len(values) and all(values[column+i] is not None for i in range(3)) and get(column)>=0 and get(column+1)>=0 and get(column+2)>0:
   expected.append((get(column),get(column+1),get(column+2),column,kind))
 for column in columns:add(column,'weight' if reward_mode in [-3,-4] else 'normal')
 if (score_id is not None or 4<=mode<=6) and get(15)==1:
  for column in range(16,46,3):
   if get(column,-1)<0:break
   add(column,'score')
 for i,reward in enumerate(clear.get(str(map_id),{}).get(str(index),{}).get('data',[])):
  if reward['DropItemID']>=0 and reward['Quantity']>0:expected.append((i+1,reward['DropItemID'],reward['Quantity'],-1,'clear'))
 actual=db.execute('select comparison,item_id,amount,source_column,kind from stage_reward where region="jp" and map_id=? and stage_index=? order by position',(map_id,index)).fetchall()
 assert actual==expected,(map_id,index,'reward',actual,expected)
 reward_count+=len(actual)
# 固定編成の全presetを元bytesとともに保存し、章スコアも落とさない。
fixed=list(csv.reader(assets.text('Data/fixed_formation.csv').splitlines()))
presets={'Data/'+row[3] for row in fixed[1:] if len(row)>3 and row[3].endswith('.preset')}
assert len(presets)==10
for name in presets:
 saved=db.execute('select a.content,s.bytes from stage_attachment a join source_file s on s.path=a.path where a.path=?',(name,)).fetchone()
 assert saved is not None and json.loads(saved[0])==json.loads(saved[1]),name
 assert digest(saved[1])==assets.files[name]['sha256'],name
assert db.execute("select count(distinct r.map_id||'-'||r.stage_index) from stage_reward r join stage_map m on m.id=r.map_id where r.kind='score' and m.mode between 4 and 6").fetchone()[0]==144
# スコア旗だけでは有効にならず、専用保存番号を必要とする。
assert db.execute('select count(*) from stage_reward r join stage_map m on m.region=r.region and m.id=r.map_id where r.kind=\'score\' and m.score_id is null and m.mode not between 4 and 6').fetchone()[0]==0
# 本能玉報酬の名前・3層画像を再構築できる全原本も保持する。
equipment_sources=['Data/equipmentlist.json','Data/equipmentgrade.csv','res/equipment_explonation.tsv']+[f'{folder}/equipment_{kind}.{extension}' for kind in ['attribute','effect','grade'] for folder,extension in [('Image','png'),('ImageData','imgcut')]]
for name in equipment_sources:
 saved=db.execute('select sha256,bytes from source_file where path=?',(name,)).fetchone()
 assert saved is not None and digest(saved[1])==saved[0]==assets.files[name]['sha256'],name
report={'database':str(path),'version':'15.7.2','schema':8,'importer':int(metadata['importer_version']),'nativeSha256':SHA,'maps':db.execute('select count(*) from stage_map').fetchone()[0],'stages':db.execute('select count(*) from stage').fetchone()[0],'definitions':headers,'spawns':spawns,'sources':len(witness['sources']),'rewardRowsCompared':reward_count,'variants':db.execute('select count(*) from stage_variant').fetchone()[0],'series':db.execute('select series,count(*) from stage_map group by series order by min(id)').fetchall(),'rewards':db.execute('select kind,count(*) from stage_reward group by kind').fetchall(),'witnessSha256':digest((ROOT/'research/.local/stage-bands-1572.json').read_bytes())}
(ROOT/('research/.local/all-stage-database-'+('0.1.16' if metadata['importer_version']=='10' else '0.1.15')+'.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
