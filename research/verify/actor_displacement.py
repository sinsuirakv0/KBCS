"""敵のふっとばし距離と終了時の状態を、果実・コンボ・軽減の境界で照合する。"""
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
class DisplacementNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=DisplacementNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44abfc,0x6ee5d8,0xa9490c] for pc in range(a,a+sizes[a],4)}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_last_error.restype=c.c_int64
lib.kbcs_core_actor_enemy_displacement.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.c_int32,c.c_int32,c.POINTER(c.c_int32)]
n.cpu.mem_write(0xc1b680,struct.pack('<Q',0xc24024));n.entry=0x6eccf4;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={0x6ece44}
records=[];count=0
profiles=[[0]*7,[10,20,30,40,50,60,70],[600,150,300,0,900,10,20],[-1,-2,-3,-4,-5,-6,-7]]
for side,action,frame,position,mask,profile,combo,reduction in itertools.product([0,1],[5,6],[0,10,11],[199,200,201],[0,1,5,127],range(4),[0,17],[0,17,100]):
 pool=Pool();word=pool[side][1].words
 for i,v in {0:2,1:action,2:frame,3:position,4:4480,7:100,8:100,10:17,115:count%2,217:reduction}.items():word[i]=v
 for bit,field in enumerate([17,41,42,45,43,47,46]):word[field]=int(bool(mask&(1<<bit)))
 word[64]=count%3;pool[1][0].words[3]=3200
 environment=Environment();environment.unit_modes[:]=[0,0];environment.stage_width=20000;environment.castle_x=3200;environment.castle_scale=[75,100,127][count%3];environment.castle_offset=13;environment.combos[17]=combo
 if side==1 and word[64]:word[3]+=3200-int(environment.castle_scale*1180/100)+int(environment.castle_scale*13/10)+int(environment.castle_scale*127/10)
 before=list(word);n.cpu.mem_write(game+0x9ee48,struct.pack('<i',environment.stage_width))
 for key,value in zip([12,14,13,15,19,20,21],profiles[profile]):environment.treasures[key]=value
 n.cpu.mem_write(game+0x84080,bytes(pool));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678))
 sp=n.stack+0x8000;actor=game+0x84080+side*0xc804+0x3ec;n.cpu.mem_write(sp-0x400,bytes(0x800));n.cpu.mem_write(sp+0xb0,struct.pack('<Q',n.memory))
 heap=n.memory+0x8000
 def allocate():
  global heap
  size=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);out=heap;heap+=(size+15)//16*16
  assert heap<n.memory+0x10000;n.cpu.mem_write(out,bytes(size));return out
 def copy():
  out=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);src=n.cpu.reg_read(n.reg.UC_ARM64_REG_X1);size=n.cpu.reg_read(n.reg.UC_ARM64_REG_X2)
  if size:n.cpu.mem_write(out,bytes(n.cpu.mem_read(src,size)))
  return out
 def treasure():return environment.treasures[n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)]
 def point():n.cpu.mem_write(n.cpu.reg_read(n.reg.UC_ARM64_REG_X4),struct.pack('<ii',990 if side==0 else 20,0));return 0
 def castle():n.cpu.reg_write(n.reg.UC_ARM64_REG_W1,environment.castle_scale);return environment.castle_offset
 n.helpers={0x81f580:game,0x5bc1dc:1,0x5c2710:0,0xa5b084:treasure,0x88f9e4:combo,
  0xbdaf40:allocate,0xbdaf60:0,0xbdb0b0:copy,0x41b298:0,0xa94074:0,
  0x5bddf8:n.memory,0x44d254:n.memory,0x44b8d4:0,0x44b8dc:0,0x44b8e4:0,0x44b854:point,0x5bbfb0:0,0x656de0:castle}
 for register,value in [('SP',sp),('X29',sp+0x200),('W19',side),('X26',1),('X22',game),('X28',actor)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 try:n.cpu.emu_start(0x6ed8d4,n.stop+4,count=100000)
 except Exception as error:raise RuntimeError((count,side,action,frame,hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)))) from error
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'enemy displacement budget'
 assert struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]==0x12345678
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)));handled=c.c_int32()
 code=lib.kbcs_core_actor_enemy_displacement(pool,c.byref(environment),side,1,200,c.byref(handled))
 assert code==0,(side,action,frame,position,mask,profile,combo,reduction,code,hex(lib.kbcs_core_actor_last_error()))
 assert handled.value==1 and bytes(pool)==expected,{'case':(side,action,frame,position,mask,profile,combo,reduction),'diff':[(i,a,b) for i,(a,b) in enumerate(zip(struct.unpack('<25602i',bytes(pool)),struct.unpack('<25602i',expected))) if a!=b][:10]}
 count+=1
 if count%79==0:records.append({'side':side,'castle_scale':environment.castle_scale,'castle_offset':environment.castle_offset,'before':before,'after':list(word),'treasures':list(environment.treasures),'combos':list(environment.combos)})
print(json.dumps({'enemyDisplacementCases':count,'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entry':'006ed8d4','terminal':'006ece44','records':records,'cases':count,'controlled':['singleton game address','unit mode/slot lookup','decoded fruit/combo inputs','model point resolver (990/20), original 00a9490c including boss correction','string construction and name lookup','heap allocation/deallocation/memcpy for native vector'],'limits':['enemy actions 5/6 only, not action 3 death/revive']}
(ROOT/'research/.local/actor-displacement-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-displacement-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
