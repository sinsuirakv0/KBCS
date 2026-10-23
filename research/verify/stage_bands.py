"""39000番台までの全系列を原本のまま棚卸しし、共通出現行を現版命令で照合する。"""
import argparse,csv,json,re,sys
from collections import Counter
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--assets',type=Path,required=True)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Assets,Native,ROOT,SHA,digest
assets=Assets(args.assets);native=Native()
series={'N':(0,'RN'),'S':(1000,'RS'),'C':(2000,'RC'),'RE':(4000,'EX'),'T':(6000,'RT'),'V':(7000,'RV'),'R':(11000,'RR'),'M':(12000,'RM'),'NA':(13000,'RNA'),'B':(14000,'RB'),'D':(16000,None),'A':(24000,'RA'),'H':(25000,'RH'),'CA':(27000,'RCA'),'DM':(30000,'DM'),'Q':(31000,'RQ'),'L':(33000,'L'),'ND':(34000,'RND'),'SR':(36000,'RSR'),'G':(37000,'G'),'PR':(39000,'RPR')}
conversions=[]
def numeric(path):
 result=[]
 for line,text in enumerate(assets.text(path).splitlines(),1):
  text=text.split('//',1)[0].strip()
  if not text:continue
  raw=next(csv.reader([text]))
  if not re.fullmatch(r'-?\d+',raw[0].strip()):continue
  values=[]
  for column,cell in enumerate(raw):
   cell=cell.strip()
   if not cell:values.append(None);continue
   if re.fullmatch(r'-?\d+',cell):values.append(int(cell));continue
   # strtol委譲の入力を保持する。Bionic libc実行の証明とは区別する。
   match=re.match(r'[+-]?\d+',cell);value=int(match[0]) if match else 0
   values.append(value);conversions.append(dict(path=path,line=line,column=column,raw=cell,value=value))
  result.append(dict(line=line,cells=values,raw=raw))
 return result
options={r['cells'][0]:r for r in assets.numeric('Data/Map_option.csv',19)}
limits=assets.numeric('Data/Stage_option.csv',9)
definitions={};decoded={};total=0
for path in sorted(assets.files):
 match=re.fullmatch(r'Data/stage((?:R[A-Z]+|EX|DM|L|G)\d+_\d+|Z\d+_\d+|W\d+_\d+|Space\d+(?:_Invasion(?:_Z)?)?_\d+|\d+)\.csv',path)
 if not match:continue
 rows=numeric(path);chapter=bool(re.fullmatch(r'Data/stage(?:\d+|W\d+_\d+|Space\d+_\d+)\.csv',path))
 skip=1 if chapter else 2
 assert len(rows)>=skip,path
 active=[];terminated=False
 for row in rows[skip:]:
  cells=row['cells'];key=tuple(value or 0 for value in cells)
  if key not in decoded:decoded[key]=native.spawn(cells)
  actual=decoded[key];total+=1
  if not actual[0]:terminated=True;break
  active.append(dict(line=row['line'],cells=cells,native=actual))
 definitions[path]=dict(headers=rows[:skip],spawns=active,numericTerminator=terminated)
print(json.dumps({'phase':'definitions','files':len(definitions),'rows':total,'uniqueRows':len(decoded)}),flush=True)
bands=[];used=set()
for label,(base,prefix) in series.items():
 maps=[];missing=[];modes=Counter()
 for path in sorted(assets.files):
  match=re.fullmatch(r'Data/MapStageData'+label+r'_(\d+)\.csv',path)
  if not match:continue
  index=int(match[1]);identifier=base+index;rows=numeric(path)
  kind=native.call(0x7cd2ac,identifier);assert kind!=-1
  assert native.call(0x7cd120,kind,index)==identifier
  option=options.get(identifier);crowns=None
  if option:
   crowns=native.crowns(identifier,option['cells'][3:7])
  stages=[]
  for stage,row in enumerate(rows[2:]):
   target=f'Data/stage{prefix}{index:03}_{stage:02}.csv' if prefix else None
   present=target in definitions
   if present:used.add(target)
   elif target:missing.append(dict(map=identifier,stage=stage,path=target))
   if label!='RE' and len(row['cells'])>8:modes[row['cells'][8]]+=1
   stages.append(dict(stage=stage,metadata=row,path=target,present=present))
  maps.append(dict(id=identifier,index=index,path=path,kind=kind,headers=rows[:2],option=option,nativeCrowns=crowns,stages=stages,limits=[r for r in limits if r['cells'][0]==identifier]))
 files={p:v for p,v in definitions.items() if prefix and re.fullmatch(r'Data/stage'+prefix+r'\d+_\d+\.csv',p)}
 bands.append(dict(base=base,series=label,maps=maps,definitionFiles=list(files),definitions=len(files),spawnRows=sum(len(v['spawns']) for v in files.values()),missing=missing,orphans=[p for p in files if p not in used],rewardModes=dict(modes),withoutNumericTerminator=sum(not v['numericTerminator'] for v in files.values())))
used.update(p for p in definitions if re.fullmatch(r'Data/stageL\d+_\d+\.csv',p))
# 章/ゾンビ/襲来は通常MapStageDataと型が異なるため、専用群として保持する。
chapter_files={}
for base,pattern in [(3000,r'Data/stage\d+\.csv'),(3003,r'Data/stageW\d+_\d+\.csv'),(3006,r'Data/stageSpace\d+_\d+\.csv'),(20000,r'Data/stageZ0[0-2]_\d+\.csv'),(21000,r'Data/stageZ0[4-6]_\d+\.csv'),(22000,r'Data/stageZ0[7-9]_\d+\.csv'),(23000,r'Data/stageSpace\d+_Invasion_\d+\.csv'),(38000,r'Data/stageSpace\d+_Invasion_Z_\d+\.csv')]:
 files=[p for p in definitions if re.fullmatch(pattern,p)];chapter_files[str(base)]=files;used.update(files)
metadata={p:numeric(p) for p in assets.files if re.fullmatch(r'Data/stageNormal.*\.csv',p)}
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,'build':assets.current,
 'scope':'All supplied static MapStageData/stage definitions through band39000; native ID/crown/common spawn reader only, not battle/reward/availability validation for every band; quest/template metadata relations remain explicit',
 'evidence':{a:digest((native.cache/'code'/(a+'.c')).read_bytes()) for a in ['007cd120','007cd2ac','007cd560','007cebc8','00a06ae4','0099fe4c','009a3a30']},
 'bands':bands,'chapterFiles':chapter_files,'chapterMetadata':metadata,'definitions':definitions,'conversions':conversions,'sources':assets.sources,
 'decodedRowsIncludingTerminators':total,'uniqueDecodedRows':len(decoded),'unassignedDefinitions':sorted(set(definitions)-used)}
if args.publish:
 selected={}
 for path,definition in definitions.items():
  prefix=re.sub(r'\d.*','',path)
  for row in definition['spawns']:
   v=row['native'];key=(prefix,min(len(row['cells']),14),v[2]<0,v[11]!=0,v[12]!=0,v[13]!=0)
   selected.setdefault(key,dict(path=path,**row))
 fixture={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,'evidence':report['evidence'],'vectors':list(selected.values())}
 (ROOT/'native/kbcs-core/tests/band-row-vectors.json').write_text(json.dumps(fixture,separators=(',',':'))+'\n',encoding='utf-8')
(ROOT/'research/.local/stage-bands-1572.json').write_text(json.dumps(report,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8-sig')
print(json.dumps({'bands':[dict(base=b['base'],series=b['series'],maps=len(b['maps']),stages=sum(len(m['stages']) for m in b['maps']),definitions=b['definitions'],spawnRows=b['spawnRows'],missing=len(b['missing']),orphans=len(b['orphans'])) for b in bands],'chapterFiles':{k:len(v) for k,v in chapter_files.items()},'conversions':len(conversions),'unassigned':report['unassignedDefinitions']}),flush=True)
