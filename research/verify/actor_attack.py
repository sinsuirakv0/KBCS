"""攻撃段の発生・対象列挙・単体抽選と同期呼出順を同版ARM64へ照合する。"""
import argparse
import ctypes as c
import hashlib
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
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA
class Actor(c.Structure):_fields_=[('words',c.c_int32*251)]
Pool=(Actor*51)*2
class Environment(c.Structure):
    _fields_=[('unit_modes',c.c_int32*2),*[(name,c.c_int32) for name in ['stage_width','castle_slot','castle_x','castle_scale','castle_offset','stage_kind','zombie','chapter_rate','crown','hp_percent','attack_percent']],
              ('crystal_max',c.c_int32*5),('crystal',c.c_int32*5),('treasures',c.c_int32*32),('combos',c.c_int32*32),('orb_stage',c.c_int32),('talents_disabled',c.c_int32),('parameters',c.c_int32*2),('spawned',c.c_int32*2),('spawn_row',c.c_int32*14),('special_castle',c.c_int32)]
class AttackNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=AttackNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44abfc,0x44abe4,0x44a8d8,0x44a8e8] for pc in range(a,a+sizes[a],4)}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_last_error.restype=c.c_int64
class Motion(c.Structure):_fields_=[('encoded',c.c_int32*8),('plain',c.c_int32*8),('soul_frames',c.c_int32)]
class Selection(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','hit','count']]+[('targets',c.c_int32*51)]
class Result(c.Structure):_fields_=[('handled',c.c_int32),('emitted',c.c_int32)]
Sink=c.CFUNCTYPE(c.c_uint32,c.c_void_p,c.POINTER(Actor*51),c.POINTER(c.c_uint32),c.POINTER(Selection))
lib.kbcs_core_actor_attack.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.c_int32,c.POINTER(Motion),c.POINTER(c.c_uint32),Sink,c.c_void_p,c.POINTER(Result)]
def sparse(pool):return [[(s*51+j)*251+i,v] for s,team in enumerate(pool) for j,actor in enumerate(team) for i,v in enumerate(actor.words) if v]
def advance(value):
 value^=(value<<13)&0xffffffff;value^=value>>17;value^=(value<<15)&0xffffffff;return value
n.entry=0x6d6d04;n.ends[n.entry]=n.entry+sizes[n.entry]
patterns=[[],[1],[1,5],[1,5,9],[1,1,1],[5,1,9],[0,1,1],[1,0,1]]
cases=[(side,frame,pattern,length,stopped,number%8,number%2,number%2,0) for number,(side,frame,pattern,length,stopped) in enumerate(itertools.product([0,1],[-1,0,1,4,5,8,11],range(len(patterns)),[0,1,6,12,-1],[0,1]))]
cases += [(side,0,pattern,12,0,targets,only,area,callback) for side,pattern,targets,only,area,callback in itertools.product([0,1],[1,3,4],range(8),[0,1],[0,1],range(4))]
records=[];count=0
for side,frame,pattern,length,stopped,targets,only,area,callback in cases:
 pool=Pool();environment=Environment();environment.unit_modes[:]=[1,0];environment.castle_slot=2 if targets==6 else -1;environment.special_castle=int(targets==6)
 for team in range(2):
  castle=pool[team][0].words;castle[0]=1;castle[3]=20000 if team==0 else 0;castle[7]=castle[8]=1000
 word=pool[side][1].words
 for i,v in {0:2,1:2,2:frame,3:10000,7:100,8:100,10:17,13:1000,15:area,16:count%2,12:37,18:17,22:37,57:only,61:stopped,115:count%3,118:count%3}.items():word[i]=v
 for i,v in zip([21,121,122],patterns[pattern]):word[i]=v
 positions={0:[],1:[50],2:[100,100,100],3:[200,50,100,50,100],4:[1001,1001],5:[50,75,100],6:[50,75,100],7:[50]*50}[targets]
 for slot,distance in enumerate(positions,1):
  target=pool[1-side][slot].words
  for i,v in {0:2,1:0,3:10000+distance if side else 10000-distance,7:100,8:100,14:0 if targets in [2,3] else [0,10,-10][slot%3],17:int(slot%2==0)}.items():target[i]=v
 if targets==5:
  pool[1-side][2].words[1]=12;pool[1-side][3].words[8]=0
 if targets in [2,3,6,7]:
  distance=100 if targets==2 else 50
  pool[1-side][0].words[3]=10000+distance if side else 10000-distance
 motion=Motion();motion.encoded[:]=[length]*8;motion.plain[:]=[8]*8
 before=sparse(pool);n.cpu.mem_write(game+0x84080,bytes(pool));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678));n.cpu.mem_write(game+0x38fb8c,bytes([0x2a]*48))
 sp=n.stack+0x8000;n.cpu.mem_write(sp-0x100,bytes(0x1000))
 for offset,value in {0x190:n.memory,0x1c8:game+0x292938,0x50:game+0x90890,0x28:game+0x90c7c,0xd8:game+0x840b8,0x68:game+0x292944,0x78:game+0x29293c,0x88:game+0x38fb8c,0x1b0:game}.items():n.cpu.mem_write(sp+offset,struct.pack('<Q',value))
 heap=n.memory+0x8000;native_events=[];cpp_events=[]
 def allocate():
  global heap
  size=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);out=heap;heap+=(size+15)//16*16
  assert heap<n.memory+0x10000;n.cpu.mem_write(out,bytes(size));return out
 def copy():
  out=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);src=n.cpu.reg_read(n.reg.UC_ARM64_REG_X1);size=n.cpu.reg_read(n.reg.UC_ARM64_REG_X2)
  if size:n.cpu.mem_write(out,bytes(n.cpu.mem_read(src,size)))
  return out
 def unit_mode():
  address=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);team=(address-game-0x2678)//0x1f0
  assert team in [0,1];return environment.unit_modes[team]
 def model():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)==side and n.cpu.reg_read(n.reg.UC_ARM64_REG_W2)==1 and n.cpu.reg_read(n.reg.UC_ARM64_REG_W3)==2
  return n.memory+0x1000
 def encoded():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)==n.memory+0x1000;return length
 def plain():
  assert side==0 and length==-1 and n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)==n.memory+0x1000;return 8
 def native_emit():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)==1
  vector=n.cpu.reg_read(n.reg.UC_ARM64_REG_X2);start,end=struct.unpack('<QQ',n.cpu.mem_read(vector,16));size=(end-start)//4;assert 0<size<=51
  selected=list(struct.unpack('<'+'i'*size,n.cpu.mem_read(start,size*4)));hit=n.cpu.reg_read(n.reg.UC_ARM64_REG_W3)
  current=Actor.from_buffer_copy(bytes(n.cpu.mem_read(game+0x84080+side*0xc804+0x3ec,c.sizeof(Actor))));state=struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]
  native_events.append({'side':side,'slot':1,'hit':hit,'targets':selected,'frame':current.words[2],'wait':current.words[18],'attacks':current.words[115],'seed':state})
  if callback==1:n.cpu.mem_write(game+0x84080+side*0xc804+0x3ec+8,bytes(4))
  if callback==2:n.cpu.mem_write(game+0x84080+side*0xc804+0x3ec+121*4,bytes(8))
  if callback==3:n.cpu.mem_write(0xc24d18,struct.pack('<I',advance(state)))
  return 0
 n.helpers={0x81f580:game,0x5c2710:unit_mode,0x5bbbc8:environment.special_castle,0x5bbc10:environment.castle_slot,0x5bc1dc:1,0x5bde34:model,0x44beb4:encoded,0x44bf2c:plain,
  0xbdaf40:allocate,0xbdaf60:0,0xbdb0b0:copy,0x6e92bc:native_emit,0x6ea1c0:native_emit}
 n.terminals={0x6d854c} if side==0 else {0x6d8cb4}
 for register,value in [('SP',sp),('X29',sp+0x600),('X27',game),('X21',1),('W24',0)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 try:n.cpu.emu_start(0x6d8584 if side==0 else 0x6d8cf8,n.stop+4,count=2000000)
 except Exception as error:raise RuntimeError((count,(side,frame,pattern,length,stopped,targets,only,area,callback),hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)))) from error
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'attack budget'
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)));expected_seed=struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]
 @Sink
 def emit(user,actors,seed,selection):
  event=selection.contents;current=actors[side][1].words
  cpp_events.append({'side':event.side,'slot':event.slot,'hit':event.hit,'targets':list(event.targets)[:event.count],'frame':current[2],'wait':current[18],'attacks':current[115],'seed':seed[0]})
  if callback==1:current[2]=0
  if callback==2:current[121]=current[122]=0
  if callback==3:seed[0]=advance(seed[0])
  return 0
 seed=c.c_uint32(0x12345678);output=Result()
 code=lib.kbcs_core_actor_attack(pool,c.byref(environment),side,1,c.byref(motion),c.byref(seed),emit,None,c.byref(output))
 assert code==0,(count,code,hex(lib.kbcs_core_actor_last_error()))
 assert bytes(pool)==expected and seed.value==expected_seed and native_events==cpp_events,{'case':(count,side,frame,pattern,length,stopped,targets,only,area,callback),'seed':(seed.value,expected_seed),'events':(cpp_events,native_events),'diff':[(i,a,b) for i,(a,b) in enumerate(zip(struct.unpack('<25602i',bytes(pool)),struct.unpack('<25602i',expected))) if a!=b][:10]}
 assert output.handled==int(not stopped) and output.emitted==len(native_events)
 count+=1
 if count%47==0 or (pattern==4 and targets==3 and callback==3):records.append({'side':side,'before':before,'after':sparse(pool),'length':length,'castle_slot':environment.castle_slot,'special_castle':environment.special_castle,'callback':callback,'events':native_events,'seed':expected_seed,'handled':output.handled,'emitted':output.emitted})
print(json.dumps({'attackCases':count,'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entries':['006d8584','006d8cf8'],'terminals':['006d854c','006d8cb4'],'records':records,'cases':count,'controlled':['singleton game address','decoded per-side unit modes and castle selector','model slot and attack encoded/plain length','stack pointers to native candidate table, metrics, proc flags and actor tables','heap malloc/delete/memcpy','006e92bc/006ea1c0 emission captured and optional frame/hit-count/RNG changes'],'limits':['attack phase 2 through target selection only; full emission/hit effects remain outside callback oracle']}
(ROOT/'research/.local/actor-attack-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-attack-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
