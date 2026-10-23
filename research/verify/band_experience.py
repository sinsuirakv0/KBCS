"""各内部種別と章・EXのXP入口を同版ARM64へ通し、共通補正と取得元を確認する。"""
import argparse,json,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA,digest,read_json
native=Native();game=0x40000000;native.cpu.mem_map(game,0x800000);native.ends[0x58bad0]=0x58bf80

def write(offset,value):native.cpu.mem_write(game+offset,struct.pack('<I',value&0xffffffff))
def minimum():return min(native.cpu.reg_read(native.reg.UC_ARM64_REG_W0),native.cpu.reg_read(native.reg.UC_ARM64_REG_W1))
def execute(mode,kind,stage,base,clears,study,treasure,combo,okame):
 write(0x32f934,mode);write(0x83dfc,stage)
 write(0x38b220+stage*0xbc,base^0x01020304);write(0x38b16c+stage*0xbc,0x01020304)
 write(0xcb34+mode*0xd0,0);write(0xca68+mode*0xd0+stage*4,clears)
 calls=[]
 def repeat():calls.append('legend');return clears
 def bounded():calls.append('minimum');return minimum()
 native.helpers={0x81f580:game,0x7cd100:kind,0xa08564:repeat,0x44abfc:bounded,0x58b674:study-1,0xa5b084:treasure,0x88f9e4:combo,0x5c022c:okame}
 actual=native.call(0x58bad0)
 legend=mode==3 and kind in [0,-9,-22]
 initial=base*9 if legend else base if mode in [3,99] else (stage*6000+20000)//10
 repeated=initial-initial*min(clears,4)//5 if legend else initial if mode in [3,99] else initial-initial*min(clears,13)//14
 studied=repeated*(100+(study-1)*5+treasure)//100;combined=studied*(100+combo)//100
 expected=combined*15//10 if okame else combined
 assert actual==expected,(mode,kind,stage,base,clears,actual,expected,calls)
 assert ('legend' in calls)==legend
 assert ('minimum' in calls)==(mode!=99 and (mode!=3 or legend))
 return {'input':dict(mode=mode,kind=kind,stage=stage,base=base,clears=clears,studyLevel=study,treasure=treasure,combo=combo,okame=okame),'stages':[initial,repeated,studied,combined,actual],'calls':calls}
vectors=[]
for kind in list(range(-26,0))+list(range(5)):
 for clears in [0,1,4,5]:vectors.append(execute(3,kind,0,3041,clears,17,97,10,1))
for mode in [0,1,2,4,5,6,7,8,9,99]:
 for stage in [0,1,47]:
  for clears in [0,1,12,13,14,100]:vectors.append(execute(mode,-2,stage,3041,clears,17,97,10,1))
path=ROOT/'research/.local/stage-bands-1572.json';witness=read_json(path);assert witness['sha256']==SHA
actual=[]
for band in witness['bands']:
 if band['series']=='RE':continue
 for entry in band['maps']:
  for stage in entry['stages']:
   base=stage['metadata']['cells'][1]
   if base is None or base<0:continue
   for clears,study,treasure,combo,okame in [(0,1,0,0,0),(4,30,225,15,1)]:
    actual.append(dict(map=entry['id'],stage=stage['stage'],**execute(3,entry['kind'],stage['stage'],base,clears,study,treasure,combo,okame)))
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,'scope':'XP入口の内部種別/画面mode/章clear状態を制御、取得元と減衰helper呼出を検査。章の実保存先選択や報酬付与全体とは別。EX表は通常報酬表として読まない。',
 'evidence':{'0058bad0':digest((native.cache/'code/0058bad0.c').read_bytes())},'stageWitnessSha256':digest(path.read_bytes()),'vectors':vectors,'actual':actual}
(ROOT/'research/.local/band-experience-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/band-experience-vectors.json').write_text(json.dumps({k:v for k,v in report.items() if k!='actual'},separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'vectors':len(vectors),'actual':len(actual)}))
