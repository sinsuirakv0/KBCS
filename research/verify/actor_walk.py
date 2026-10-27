"""味方歩行・敵歩行/潜行/蘇生待機の更新区間をARM64と比較する。前後の命中/開始判定は分離。"""
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
class WalkNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=WalkNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44abfc] for pc in range(a,a+sizes[a],4)}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_walk.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.c_int32,c.POINTER(c.c_int32)]
records=[];count=0
cases=[(side,mode,0,0,stop,slow,speed,distance,0,0,0) for side,mode,stop,slow,speed,distance in itertools.product([0,1],[0,1],[0,1],[0,1],[0,1,17],[None,499,500,501])]
cases += [(side,0,action,frame,stop,slow,17,None,offset,remaining,1) for side,action,frame,stop,slow,offset,remaining in itertools.product([0,1],[11,12,13,14,15,16],[0,25,26,29,30,39,40],[0,1],[0,1],[-1,0,1],[0,1,2])]
for side,mode,action,frame,stop,slow,speed,distance,offset,remaining,buried in cases:
 pool=Pool();word=pool[side][1].words
 for i,v in {0:2,1:action,2:frame,3:10000+offset,7:100,8:100,10:speed,13:500,61:stop,62:slow,98:10000,106:0,205:remaining}.items():word[i]=v
 if distance is not None:
  target=pool[1-side][1].words;target[0]=2;target[8]=100;target[3]=10000+(-distance if side==0 else distance)
 initial=list(word);environment=Environment();environment.unit_modes[side]=mode;environment.castle_slot=0
 n.cpu.mem_write(game+0x84080,bytes(pool));sp=n.stack+0x8000
 def unit_mode():return environment.unit_modes[(n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)-game-0x2678)//0x1f0]
 n.helpers={0x81f580:game,0x5bc1dc:1,0x5c2710:unit_mode,0x5bbbc8:0,0x5bbc10:0}
 if mode:
  entry=0x6eb8c0;n.entry=0x6eb464;n.terminals={0x6eb6a4};registers=[('W20',side),('X23',1),('X22',game),('X24',n.memory)]
 else:
  entry=0x6ecfec;n.entry=0x6eccf4;n.terminals={0x6ece44};registers=[('W19',side),('X26',1),('X22',game),('X28',game+0x84080+side*0xc804+0x3ec)]
  n.cpu.mem_write(sp+0xb0,struct.pack('<Q',n.memory))
 n.ends[n.entry]=n.entry+sizes[n.entry];n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,sp)
 for register,value in registers:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 n.cpu.emu_start(entry,n.stop+4,count=100000)
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'walk budget'
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)));handled=c.c_int32()
 assert lib.kbcs_core_actor_walk(pool,c.byref(environment),side,1,c.byref(handled))==0
 assert handled.value==1 and bytes(pool)==expected,{'case':cases[count],'diff':[(i,a,b) for i,(a,b) in enumerate(zip(struct.unpack('<25602i',bytes(pool)),struct.unpack('<25602i',expected))) if a!=b][:10]}
 count+=1
 if count%97==0 or (action in [11,12,13,14,15,16] and word[1]!=action and frame in [29,39] and not offset and remaining==1):
  records.append({'side':side,'mode':mode,'before':initial,'after':list(word),'distance':distance})
print(json.dumps({'walkCases':count,'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entries':['006eb8c0','006ecfec'],'records':records,'cases':count,'controlled':['singleton game address','unit mode, special castle, model slot lookup'],'limits':['movement block after begin and sniper/shock hit processing','burrow start/revive scheduling not included']}
(ROOT/'research/.local/actor-walk-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-walk-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
