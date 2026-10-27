"""通常死亡の時計・残存効果による保留・枠解放を原本の両陣営で照合する。"""
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
class Input(c.Structure):_fields_=[(name,c.c_int32) for name in ['blocked','body_frames','soul_frames','production_slot','cannon_base','cannon_remaining']]
class Result(c.Structure):_fields_=[(name,c.c_int32) for name in ['handled','removed','death_notice','reset_production','production_slot','cannon_remaining']]
class RetirementNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=RetirementNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44abfc,0x44abe4] for pc in range(a,a+sizes[a],4)}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_last_error.restype=c.c_int64
lib.kbcs_core_actor_retire.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.c_int32,c.POINTER(Input),c.POINTER(Result)]
def sparse(pool):return [[(s*51+j)*251+i,v] for s,team in enumerate(pool) for j,actor in enumerate(team) for i,v in enumerate(actor.words) if v]
records=[];count=0
cases=[(side,mode,frame,body,soul,blocked,0,0) for side,mode,frame,body,soul,blocked in itertools.product([0,1],[0,1],[0,1,5,9,10],[-1,0,1,5,10],[-1,0,7],[0,1])]
cases += [(side,1,10,1,-1,0,peer,rate) for side,peer,rate in itertools.product([0,1],[0,1,2,4,21],[0,17,1000,2000])]
for side,mode,frame,body,soul,blocked,peer,rate in cases:
 pool=Pool();word=pool[side][1].words
 for i,v in {0:2,1:4,2:frame,27:4,28:5,29:6,127:soul,129:int(body!=-1),213:count%2-1,237:rate}.items():word[i]=v
 if peer:
  pool[side][2].words[0]=2 if peer!=2 else 3;pool[side][2].words[1]=peer
 environment=Environment();environment.unit_modes[side]=mode
 input=Input(blocked,body,7,3,[0,100,10001][count%3],[0,1,1000][count%3]);pool[side][0].words[12]=input.cannon_remaining
 before=sparse(pool);sp=n.stack+0x8000;fp=sp+0x200;actor=game+0x84080+side*0xc804+0x3ec;castle=game+0x84080+side*0xc804;flags=n.memory+0x5000
 n.cpu.mem_write(game+0x84080,bytes(pool));n.cpu.mem_write(sp-0x400,bytes(0x800));n.cpu.mem_write(flags,struct.pack('<21i',*[1]*21));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678))
 n.cpu.mem_write(sp+0xb0,struct.pack('<Q',n.memory));n.cpu.mem_write(sp+0xd0,struct.pack('<Q',flags));n.cpu.mem_write(fp-0x80,struct.pack('<Q',castle));n.cpu.mem_write(sp+0x6c,struct.pack('<i',1-blocked))
 notices=[]
 def notice():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)==side and n.cpu.reg_read(n.reg.UC_ARM64_REG_W2)==1
  notices.append(1);return 0
 def model():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)==side and n.cpu.reg_read(n.reg.UC_ARM64_REG_W2)==3 and n.cpu.reg_read(n.reg.UC_ARM64_REG_W3)==8
  return n.memory+0x6000
 def soul_model():
  key=n.cpu.reg_read(n.reg.UC_ARM64_REG_X1)
  assert struct.unpack('<i',n.cpu.mem_read(key,4))[0]==soul+1000
  return n.memory+0x6100
 def length():
  address=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)
  assert address in [n.memory+0x6000,n.memory+0x6128]
  return body if address==n.memory+0x6000 else input.soul_frames
 n.helpers={0x81f580:game,0x5bc1dc:input.production_slot,0x5c2710:mode,0x6fce54:notice,0x5bde34:model,0x65c134:soul_model,0x44beb4:length,0xa93074:input.cannon_base}
 if mode:
  n.entry=0x6eb464;n.terminals={0x6eb6a4};entry=0x6ebb0c
  registers=[('W20',side),('X23',1),('X22',game),('X24',n.memory),('X19',actor),('W25',1-blocked)]
 else:
  n.entry=0x6eccf4;n.terminals={0x6ece44};entry=0x6ed5e0
  registers=[('W19',side),('X26',1),('X22',game),('X28',actor)]
 n.ends[n.entry]=n.entry+sizes[n.entry]
 for register,value in [('SP',sp),('X29',fp),*registers]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 try:n.cpu.emu_start(entry,n.stop+4,count=100000)
 except Exception as error:raise RuntimeError((count,(side,mode,frame,body,soul,blocked,peer,rate),hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)))) from error
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'retirement budget'
 assert struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]==0x12345678
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)));output=Result()
 code=lib.kbcs_core_actor_retire(pool,c.byref(environment),side,1,c.byref(input),c.byref(output))
 assert code==0,(count,code,hex(lib.kbcs_core_actor_last_error()))
 # 城砲残りはHUD所有状態への出力として分離したため、同じ場所へ投影して全個体を比較する。
 actual=bytearray(bytes(pool));struct.pack_into('<i',actual,side*0xc804+48,output.cannon_remaining)
 assert output.handled==1 and actual==expected,{'case':(count,side,mode,frame,body,soul,blocked,peer,rate),'diff':[(i,a,b) for i,(a,b) in enumerate(zip(struct.unpack('<25602i',actual),struct.unpack('<25602i',expected))) if a!=b][:10]}
 reset=struct.unpack('<i',n.cpu.mem_read(flags+input.production_slot*4,4))[0]==0
 assert output.death_notice==int(bool(notices)) and output.removed==int(word[0]==0) and output.reset_production==int(reset) and output.production_slot==(input.production_slot if reset else -1)
 count+=1
 if count%47==0 or (rate>0 and peer in [1,4]):records.append({'side':side,'mode':mode,'before':before,'after':sparse(pool),'input':{k:getattr(input,k) for k,_ in Input._fields_},'output':{k:getattr(output,k) for k,_ in Result._fields_}})
print(json.dumps({'retirementCases':count,'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entries':['006ebb0c','006ed5e0'],'terminals':['006eb6a4','006ece44'],'records':records,'cases':count,'controlled':['singleton and decoded unit mode','body motion kind 8 length and soul ID+1000 length lookup','production slot and cannon base getter','precomputed remaining attack-effect guard','native death notification capture','castle cooldown write projected into explicit output'],'limits':['action 4 only, action 21 death surge emission and effect ownership scan are separate']}
(ROOT/'research/.local/actor-retirement-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-retirement-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
