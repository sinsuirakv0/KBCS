"""15.7.2の演出時計・固定プール・呪い素材名を実命令と所有C++へ比較する。全main/GPU照合ではない。"""
import argparse
import ctypes as c
import itertools
import json
import os
from pathlib import Path
import sqlite3
import struct
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--library',type=Path,required=True)
parser.add_argument('--allow-known-differences',action='store_true')
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA,digest

class Actor(c.Structure):_fields_=[('words',c.c_int32*251)]
class Visual(c.Structure):_fields_=[(name,c.c_int32) for name in ['kind','side','slot','phase','frame','x','y','layer']]+[('root',c.c_int32*2)]
class EffectNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
  if address in self.allowed:return
  return super().hook(cpu,address,size,data)

n=EffectNative();game=0x40000000;texture=game+0x500000;n.cpu.mem_map(game,0x800000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
actual=[0xa9c81c,0xa9c93c,0xa9c8b0,0xa9c864,0xa9cfb8,0xa9d0d0,0xa9d044,0xa9cff8,0xa9474c,0x5bb4dc]
n.allowed={pc for a in actual for pc in range(a,a+sizes[a],4)}
n.ends.update({a:a+sizes[a] for a in [0x6d6d04,0x6ddfb8,0x9f560c,0x5ccda8,0x5ccf40,0x5cd0b0,0x5cd248,0x5cd3e0,0x5cd614,0x5cd848,0x5cda6c]})
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()))
lib.kbcs_audit_owner_clock.argtypes=[c.POINTER(Actor),c.POINTER(c.c_int32),c.c_int32,c.POINTER(Actor),c.POINTER(c.c_uint32)]
lib.kbcs_audit_effect_pool.argtypes=[c.c_int32,c.POINTER(c.c_int32),c.POINTER(Visual),c.c_int32,c.c_int32,c.POINTER(Visual)]

def reg(index):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(index)))
def setreg(name,value):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+name),value)
def run_fragment(start,end):
 n.terminals={end};n.cpu.emu_start(start,n.stop+4,count=100000)
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==end,'fragment budget'

# モデルの準備だけを制御し、文字列構築のADRP/LDR/STRは本物を実行する。
names={}
def capture_name():
 address=reg(1);tag=n.cpu.mem_read(address,1)[0];assert not tag&1
 names[hex(reg(0)-texture)]='ImageData/'+bytes(n.cpu.mem_read(address+1,tag//2)).decode('ascii');return 0
n.entry=0x9f560c;n.helpers={0x44ba98:capture_name,0x44c80c:0,0x44c86c:0,0x44c1dc:0}
setreg('SP',n.stack+0x8000);setreg('X29',n.stack+0x9000);setreg('X19',texture)
n.cpu.mem_write(n.stack+0x8128,struct.pack('<Q',texture))
run_fragment(0x9fa2bc,0x9fa3b8)
assert names=={'0x2dc8':'ImageData/skill_curse.maanim','0x2e00':'ImageData/skill_curse_e.maanim'},names
resource=json.loads((ROOT/'crates/kbcs-data/resources/battle-inputs.json').read_text(encoding='utf-8-sig'))
binding_differences=[{'phase':key,'native':path,'cppInput':resource['clocks'][key]['path']} for key,path in names.items() if path!=resource['clocks'][key]['path']]

def native_clock(before,lengths,ticks):
 n.entry=0x6d6d04;n.helpers={0x81f580:game,0x44beb4:lambda:dict(zip([0x2328,0x2478,0x24b0,0x24e8],lengths))[reg(0)-texture]}
 address=game+0x84080+0xc804+0x3ec;n.cpu.mem_write(address,bytes(before))
 setreg('SP',n.stack+0x8000);n.cpu.mem_write(n.stack+0x8190,struct.pack('<Q',texture));n.cpu.mem_write(n.stack+0x81a8,struct.pack('<Q',texture+0x2478))
 for _ in range(ticks):
  setreg('W27',1);setreg('W28',1);run_fragment(0x6d951c,0x6d95dc)
 return Actor.from_buffer_copy(n.cpu.mem_read(address,c.sizeof(Actor)))

clock_fields=[133,134,192,193];owner_cases=0;owner_differences=[];owner_trace=[];clock_vectors=[]
for raw,barrier,shield,age,ticks,lengths in itertools.product([0,2],[0,1],range(4),[0,13,25],[1,2,30],[(26,14,14,18),(-1,0,1,-1)]):
 before=Actor()
 for index,value in {0:raw,1:17,3:9000,4:4400,7:1000,8:1000,9:1,133:barrier,134:age,192:shield,193:age}.items():before.words[index]=value
 expected=native_clock(before,lengths,ticks);out=Actor();seed=c.c_uint32()
 code=lib.kbcs_audit_owner_clock(c.byref(before),(c.c_int32*4)(*lengths),ticks,c.byref(out),c.byref(seed));assert code==0,('owner',code)
 assert seed.value==0x12345678,'visual clock changed RNG'
 a=[expected.words[i] for i in clock_fields];b=[out.words[i] for i in clock_fields]
 row={'logicalFrame':ticks,'side':1,'slot':1,'raw':raw,'action':17,'hp':1000,'lengths':lengths,'before':[before.words[i] for i in clock_fields],'native':a,'cpp':b,'seed':seed.value}
 if a!=b:owner_differences.append(row)
 if raw==2 and barrier==1 and shield==1 and age==0 and lengths[0]==26:owner_trace.append(row)
 if raw==2 and ticks==1:clock_vectors.append({'before':row['before'],'lengths':lengths,'after':a})
 owner_cases+=1

pool_cases=0;pool_differences=[]
for kind,ticks in itertools.product(range(4),[0,1,2,25,40]):
 count=30 if kind else 200;record_size=28 if kind>=2 else 16;lengths=(25,31)
 phases=[(0x10e8,0x10e8),(0x2248,0x2248),(0x2360,0x2398),(0x2520,0x2558)][kind]
 start=[0x9d8f0,0x9e570,0x9e750,0x9ea98][kind];entry=[0x5ccda8,0x5ccf40,0x5cd0b0,0x5cd248][kind]
 data=bytearray(count*record_size);values=(Visual*count)();after=(Visual*count)()
 for i,value in enumerate(values):
  value.kind=6;value.phase=phases[i%2] if i%3 else 0;value.frame=i%25;value.x=100+i;value.y=200+i
  at=i*record_size;data[at]=int(value.phase!=0);struct.pack_into('<iii',data,at+4,value.x,value.y,value.frame)
  if kind>=2:data[at+24]=i%2
 n.cpu.mem_write(game+start,bytes(data));n.helpers={0x457e1c:0,0x459f04:0,0x44bf2c:lambda:dict(zip(phases,lengths if kind>=2 else (25,25)))[reg(0)-texture]};n.terminals=set()
 for _ in range(ticks):n.call(entry,game,texture)
 assert lib.kbcs_audit_effect_pool(kind,(c.c_int32*2)(*lengths),values,count,ticks,after)==0
 result=bytes(n.cpu.mem_read(game+start,len(data)))
 for i,value in enumerate(after):
  at=i*record_size;expected=[bool(result[at]),*struct.unpack_from('<iii',result,at+4)];got=[bool(value.phase),value.x,value.y,value.frame]
  if expected!=got:pool_differences.append({'kind':kind,'poolSlot':i,'logicalFrame':ticks,'native':expected,'cpp':got})
 pool_cases+=1

transient_cases=0
if hasattr(lib,'kbcs_audit_transient_pool'):
 lib.kbcs_audit_transient_pool.argtypes=[c.c_int32,c.c_int32,c.POINTER(Visual),c.c_int32,c.c_int32,c.POINTER(Visual),c.POINTER(c.c_int32)]
 for phase,header,entry in [(0x35b8,0x9ede0,0x5cd3e0),(0x3628,0x9edf8,0x5cd614),(0x16480,0x9ee10,0x5cd848),(0x16560,0x9ee28,0x5cda6c)]:
  for ticks,length in itertools.product([0,1,2,25,40],[26,-1]):
   pointers=n.memory+0x5000;records=n.memory+0x6000;values=(Visual*8)();after=(Visual*8)();remaining=c.c_int32()
   n.cpu.mem_write(game+header,struct.pack('<QQQ',pointers,pointers+64,pointers+64))
   for i,value in enumerate(values):
    value.kind=6;value.phase=phase;value.x=100+i;value.y=200+i;value.frame=[0,24,25,26][i%4]
    n.cpu.mem_write(pointers+i*8,struct.pack('<Q',records+i*16));n.cpu.mem_write(records+i*16,struct.pack('<iii',value.x,value.y,value.frame))
   n.helpers={0x457e1c:0,0x459f04:0,0xbdaf60:0,0x44beb4:lambda:length};n.terminals=set()
   for _ in range(ticks):n.call(entry,game,texture)
   end=struct.unpack('<Q',n.cpu.mem_read(game+header+8,8))[0];expected=[]
   for address in range(pointers,end,8):
    record=struct.unpack('<Q',n.cpu.mem_read(address,8))[0];expected.append(list(struct.unpack('<iii',n.cpu.mem_read(record,12))))
   assert lib.kbcs_audit_transient_pool(phase,length,values,8,ticks,after,c.byref(remaining))==0
   assert [[v.x,v.y,v.frame] for v in after[:remaining.value]]==expected,('transient',phase,ticks,length)
   transient_cases+=1

death_draw=[];display_cases=0
if hasattr(lib,'kbcs_audit_actor_visuals'):
 lib.kbcs_audit_actor_visuals.argtypes=[c.c_int32,c.POINTER(Actor),c.POINTER(Visual),c.POINTER(c.c_int32)]
 for side,action in itertools.product([0,1],[2,4,14,21]):
  actor=Actor();values=(Visual*32)();count=c.c_int32()
  for i,v in {0:2,1:action,2:7,3:12345,4:-201,5:2,7:1000,8:1000,133:1,134:5}.items():actor.words[i]=v
  assert lib.kbcs_audit_actor_visuals(side,c.byref(actor),values,c.byref(count))==0
  if action==4:assert count.value==0
  elif action in [2,14]:assert count.value==1 and values[0].kind==7 and values[0].phase==0x2328
  else:
   assert count.value==1 and values[0].kind==10
   n.entry=0x6ddfb8;node=game+0x600000;base=game+0x84080
   n.cpu.mem_write(base+side*0xc804+0x3ec,bytes(actor))
   pose=[];draw=[]
   def pose_capture():pose.append([reg(1)-texture,reg(2)&0xffffffff]);return 0
   def draw_capture():draw.append([c.c_int32(reg(2)).value,c.c_int32(reg(3)).value]);return 0
   n.helpers={0x81f580:game,0x44d1dc:pose_capture,0x448e7c:draw_capture,0x449aec:960}
   sp=n.stack+0x8000
   setreg('D9',struct.unpack('<Q',struct.pack('<d',0.5))[0])
   for key,value in [('SP',sp),('W20',20 if side else 40),('X21',node),('W25',0xc804),('W27',1),('W23',side)]:setreg(key,value)
   for offset,value in [(0x130,game+0x83e00),(0x138,base),(0x190,game),(0x100,base+side*0xc804),(0xf0,texture+0x26a8),(0xe8,texture+0x27f8),(0x160,0)]:n.cpu.mem_write(sp+offset,struct.pack('<Q',value))
   run_fragment(0x6de8e4,0x6de9d0)
   value=values[0];assert pose==[[value.phase,value.frame]] and draw==[[value.x,value.y]],(side,pose,draw)
   death_draw.append({'side':side,'action':action,'phase':hex(value.phase),'frame':value.frame,'x':value.x,'y':value.y})
  display_cases+=1

report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(args.library.read_bytes()),'nativeNames':names,'bindingDifferences':binding_differences,'ownerClockCases':owner_cases,'ownerClockDifferences':len(owner_differences),'firstOwnerDifference':owner_differences[:1],'ownerTrace':owner_trace,'poolCases':pool_cases,'poolDifferences':len(pool_differences),'firstPoolDifference':pool_differences[:1],'transientCases':transient_cases,'displayCases':display_cases,'nativeDeathDraw':death_draw,
 'controlled':['BattleTextureContext lengths and model preparation','fixture owner action17/game mode4/no attacks','singleton, sound device'],
 'limits':['full main and GPU pixels are not compared','transient generation and all character sequences are not covered by this probe']}
path=ROOT/'research/.local'/('effect-state-'+args.library.stem+'.json');path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=True))
if not args.allow_known_differences:assert not binding_differences and not owner_differences and not pool_differences,'effect state mismatch'
if args.publish:
 assert not binding_differences and not owner_differences and not pool_differences
 fixture={'version':'15.7.2','sha256':SHA,'entry':'006d951c','terminal':'006d95dc','fields':clock_fields,'bindings':names,'records':clock_vectors}
 (ROOT/'native/kbcs-core/tests/effect-state-vectors.json').write_text(json.dumps(fixture,separators=(',',':')),encoding='utf-8-sig')
