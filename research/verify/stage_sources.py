"""0..39000番台のIDと戦闘用ファイル選択を現版命令で照合する。"""
import argparse,json,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA,digest
native=Native();game=0x40000000;native.cpu.mem_map(game,0x800000)
with sqlite3.connect((native.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for address in ['0099fe4c','007cf4b0']:
  native.ends[int(address,16)]=int(address,16)+db.execute('SELECT size FROM functions WHERE address=?',(address,)).fetchone()[0]

def write(offset,value):native.cpu.mem_write(game+offset,struct.pack('<i',value))
def register(index):return native.cpu.reg_read(getattr(native.reg,'UC_ARM64_REG_X'+str(index)))
def string():
 pointer=register(0);source=register(1);value=bytes(native.cpu.mem_read(source,100)).split(b'\0')[0]
 if len(value)<23:native.cpu.mem_write(pointer,bytes([len(value)*2])+value+b'\0')
 else:
  native.cpu.mem_write(native.memory+0x800,value+b'\0')
  native.cpu.mem_write(pointer,struct.pack('<QQQ',1,len(value),native.memory+0x800))
 return pointer

def source(context):
 native.cpu.mem_write(native.stack,bytes(0x10000))
 for offset,value in [(0x32f934,context['mode']),(0x38b164,context['kind']),(0x340368,context['index']),
                      (0x40a514,context['exIndex']),(0x40a51c,context['exStage']),
                      (0x389910+context['stage']*4,context['questReference'])]:write(offset,value)
 for offset,key in [(0x334048,'zombie'),(0x334056,'invasion'),(0x334057,'invasionZombie')]:native.cpu.mem_write(game+offset,bytes([context[key]]))
 result=[]
 def capture():
  pointer=register(0);data=bytes(native.cpu.mem_read(pointer,24))
  if data[0]&1:
   _,length,pointer=struct.unpack('<QQQ',data);template=bytes(native.cpu.mem_read(pointer,length)).decode('ascii')
  else:template=data[1:1+(data[0]>>1)].decode('ascii')
  count=template.count('%')
  values=[register(i)&0xffffffff for i in range(2,2+count)]
  result.append({'template':template,'arguments':values,'file':template%tuple(values)})
  native.cpu.emu_stop();return 0
 native.helpers={0x464f48:0,0x4618e8:0,0x470ac0:1,0x7cd110:lambda:register(0),0x41b298:string,
                 0x424bb4:capture,0x4253b4:capture,0x7cf4b0:context['kind'],0x71b5b4:context['labyrinthTemplate']}
 native.entry=0x99fe4c
 for name,value in [('X0',game),('X1',context['stage']),('X2',context['battle']),('SP',native.stack+0x8000),('LR',native.stop)]:native.cpu.reg_write(getattr(native.reg,'UC_ARM64_REG_'+name),value)
 try:native.cpu.emu_start(native.entry,native.stop+4,count=10000)
 except Exception as error:raise RuntimeError((context,hex(native.cpu.reg_read(native.reg.UC_ARM64_REG_PC)))) from error
 assert len(result)==1,context
 return {'context':context,**result[0]}

bases={0:0,1:1000,2:2000,-2:3000,-3:3003,-7:3006,-8:4000,-5:5000,3:6000,-4:7000,4:11000,-6:12000,-9:13000,-10:14000,-11:16000,-12:20000,-13:21000,-14:22000,-15:23000,-16:24000,-17:25000,-18:27000,-19:30000,-20:31000,-21:33000,-22:34000,-23:36000,-24:37000,-25:38000,-26:39000}
mapping=[];mapping_all=[]
for identifier in range(40000):
 kind=native.call(0x7cd2ac,identifier);index=native.call(0x7cd560,identifier)
 expected=next((k for k,b in bases.items() if b<=identifier<b+(3 if k in [-2,-3,-7] else 1000)),-1)
 assert kind==expected,(identifier,kind,expected)
 if kind!=-1:assert native.call(0x7cd120,kind,index)==identifier
 mapping_all.append({'id':identifier,'kind':kind,'index':index})
 if identifier%1000 in [0,999] or 2998<=identifier<=3010:mapping.append({'id':identifier,'kind':kind,'index':index})
contexts=[]
for kind in [0,1,2,3,4,-4,-6,-8,-9,-10,-11,-16,-17,-18,-19,-20,-21,-22,-23,-24,-26]:
 for battle in ([1] if kind in [4,-11] else [0,1]):
  for index,stage in [(0,0),(2,5),(999,99)]:
   contexts.append(dict(mode=99 if kind==-8 and battle else 3,kind=kind,index=index,stage=stage,battle=battle,zombie=0,invasion=0,invasionZombie=0,questReference=1203,labyrinthTemplate=17,exIndex=index,exStage=stage))
for kind,offset in [(-2,0),(-3,4),(-7,7),(-12,0),(-13,4),(-14,7),(-15,7),(-25,7)]:
 for chapter in range(3):
  contexts.append(dict(mode=offset+chapter,kind=kind,index=chapter,stage=12,battle=1,zombie=int(kind in [-12,-13,-14]),invasion=int(kind==-15),invasionZombie=int(kind==-25),questReference=0,labyrinthTemplate=0,exIndex=0,exStage=0))
vectors=[source(context) for context in contexts]
# 現在種別の分岐を、外部状態getterだけ制御して実行する。
current=[]
for mode in [0,1,2,3,4,5,6,7,8,9,10,99]:
 for zombie,invasion,invasion_z in [(0,0,0),(1,0,0),(1,1,1),(0,0,1)]:
  for ignore in [0,1]:
   write(0x32f934,mode);write(0x38b164,-26)
   native.helpers={0x81f580:game,0x7cf658:zombie,0x7cf830:invasion,0x7cf8c0:invasion_z,0x78aefc:0,0x78af80:0}
   value=native.call(0x7cf4b0,ignore)
   current.append(dict(mode=mode,selectedKind=-26,zombie=zombie,invasion=invasion,invasionZombie=invasion_z,ignore=ignore,exOverride=0,exMarker=300,kind=value))
for selected in [-27,-26,-1,0,4,5]:
 for marker in [299,300,301]:
  for override in [0,1]:
   for ignore in [0,1]:
    write(0x32f934,3);write(0x38b164,selected)
    native.helpers={0x81f580:game,0x78aefc:override,0x78af80:0,0x821cb4:marker}
    value=native.call(0x7cf4b0,ignore)
    current.append(dict(mode=3,selectedKind=selected,zombie=0,invasion=0,invasionZombie=0,ignore=ignore,exOverride=override,exMarker=marker,kind=value))
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,
 'scope':'All 40000 nonnegative IDs; native source-choice prefix stops at formatting boundary, CSV/format allocation not executed; current-kind external state getters controlled; quest/template selection values supplied',
 'evidence':{a:digest((native.cache/'code'/(a+'.c')).read_bytes()) for a in ['007cd120','007cd2ac','007cd560','007cf4b0','0099fe4c','0071b5b4']},
 'mappingAll':mapping_all,'mapping':mapping,'vectors':vectors,'current':current,'idCases':40000}
(ROOT/'research/.local/stage-sources-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/stage-source-vectors.json').write_text(json.dumps({k:v for k,v in report.items() if k!='mappingAll'},separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'idCases':40000,'mappingVectors':len(mapping),'sources':len(vectors),'current':len(current)}))
