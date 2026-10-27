"""攻撃待機・接触・潜行開始の両陣営走査を同版ARM64へ照合する。"""
import argparse
import ctypes as c
import hashlib
import itertools
import json
import os
import random
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
class IntentNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=IntentNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44abfc,0x44abe4] for pc in range(a,a+sizes[a],4)}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_last_error.restype=c.c_int64
lib.kbcs_core_actor_intent.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.POINTER(c.c_int32)]
def sparse(pool):return [[(s*51+j)*251+i,v] for s,team in enumerate(pool) for j,actor in enumerate(team) for i,v in enumerate(actor.words) if v]
n.entry=0x6d6d04;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={0x6d8510}
records=[];count=0;generator=random.Random(1572)
cases=[(side,action,timer,contact,zombie,burrows) for side,action,timer,contact,zombie,burrows in itertools.product([0,1],[0,1,12],[-1,0,1,2],[0,1,2],[0,1],[-1,0,1])]
for side,action,timer,contact,zombie,burrows in cases:
 pool=Pool();environment=Environment();environment.unit_modes[:]=[1,0];environment.castle_slot=-1
 for team in range(2):
  castle=pool[team][0].words;castle[0]=1;castle[3]=2000 if team==0 else 0;castle[7]=castle[8]=1000
 word=pool[side][1].words
 for i,v in {0:2,1:action,2:7,3:1000,7:100,8:100,10:[0,17][count%2],13:100,47:zombie,97:burrows,115:count%2,117:timer,118:count%3}.items():word[i]=v
 if contact==1:
  target=pool[1-side][1].words
  for i,v in {0:2,1:4,3:1050 if side else 950,7:100,8:100}.items():target[i]=v
 elif contact==2:pool[1-side][0].words[3]=1050 if side else 950
 if count%3==0:
  # 地中から城へ接触したときのbreakが、後続枠を飛ばす条件も照合する。
  peer=pool[side][2].words
  for i,v in {0:2,1:0,3:1000,7:100,8:100,117:1,115:1}.items():peer[i]=v
 guard=pool[1][count%2].words;guard[64]=int(count%5==0);guard[65]=int(count%7==0)
 if count%11==0:
  pool[0][3].words[0]=2;pool[0][3].words[1]=7
 if count%13==0:environment.unit_modes[:]=[generator.randrange(2),generator.randrange(2)]
 before=sparse(pool);n.cpu.mem_write(game+0x84080,bytes(pool));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678))
 def unit_mode():
  address=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);team=(address-game-0x2678)//0x1f0
  assert team in [0,1];return environment.unit_modes[team]
 n.helpers={0x81f580:game,0x5c2710:unit_mode,0x5bbbc8:0,0x5bbc10:-1}
 sp=n.stack+0x8000
 for register,value in [('SP',sp),('X29',sp+0x400),('X27',game),('W24',1)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 try:n.cpu.emu_start(0x6d823c,n.stop+4,count=1000000)
 except Exception as error:raise RuntimeError((count,(side,action,timer,contact,zombie,burrows),hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)))) from error
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'intent budget'
 assert struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]==0x12345678
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)));blocked=n.cpu.reg_read(n.reg.UC_ARM64_REG_W24);output=c.c_int32()
 code=lib.kbcs_core_actor_intent(pool,c.byref(environment),c.byref(output))
 assert code==0,(count,code,hex(lib.kbcs_core_actor_last_error()))
 assert bytes(pool)==expected and output.value==blocked,{'case':(count,side,action,timer,contact,zombie,burrows),'blocked':(output.value,blocked),'diff':[(i,a,b) for i,(a,b) in enumerate(zip(struct.unpack('<25602i',bytes(pool)),struct.unpack('<25602i',expected))) if a!=b][:10]}
 count+=1
 if count%31==0:records.append({'before':before,'after':sparse(pool),'unit_modes':list(environment.unit_modes),'blocked':blocked})
print(json.dumps({'intentCases':count,'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entry':'006d823c','terminal':'006d8510','records':records,'cases':count,'controlled':['singleton game address','decoded per-side unit modes','ordinary castle selection','entry W24 initialized by preceding enemy update call site'],'limits':['post-action intent selection only; attack clock and hit invocation follow separately']}
(ROOT/'research/.local/actor-intent-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-intent-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
