"""006dac8c..006db1acのKB・ふっとばし・ワープ遷移をARM64と比較する。"""
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
class Reaction(c.Structure):_fields_=[('previous_hp',c.c_int32),('death_visual_available',c.c_int32)]
class Result(c.Structure):_fields_=[('sound_count',c.c_int32),('sounds',c.c_int32*2),('death_visual',c.c_int32),('death_x',c.c_int32),('death_y',c.c_int32)]
class ReactionNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=ReactionNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44a8d8,0x44a8e8,0x5bb5a0] for pc in range(a,a+sizes[a],4)}
n.entry=0x6d6d04;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={0x6db1ac,0x6db1b4}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_react.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.c_int32,c.POINTER(Reaction),c.POINTER(c.c_uint32),c.POINTER(Result)]
records=[];count=0
cases=[(side,maximum,kb,hp,before,0,0,0,0,0,0,0) for side,maximum,kb,hp,before in itertools.product([0,1],[1,100,10001],[0,1,3],[0,1,33,34,99,100],[1,34,100])]
cases += [(side,100,3,hp,100,action,flags,mode,available,special,1,int(flags==4)) for side,hp,action,flags,mode,available,special in itertools.product([0,1],[0,50],[0,4,21],[0,1,2,3,4],[0,1],[0,1],[0,1])]
for side,maximum,kb,hp,before,action,flags,mode,available,special,trait,survive in cases:
 pool=Pool();word=pool[side][1].words
 for i,v in {0:2,1:action,2:17,3:12345,4:-200,7:maximum,8:hp,9:kb,19:1,23:int(flags in [1,3]),60:int(flags in [2,3]),63:1,77:survive,107:trait,139:int(flags==4)}.items():word[i]=v
 initial=list(word);environment=Environment();environment.unit_modes[0]=1-mode;environment.unit_modes[1]=mode;environment.special_castle=special;environment.castle_slot=1
 input=Reaction(before,available);sp=n.stack+0x8000;actor=game+0x84080+side*0xc804+0x3ec;visual=game+0x9e570
 n.cpu.mem_write(game,bytes(0x500000));n.cpu.mem_write(game+0x84080,bytes(pool));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678));n.cpu.mem_write(sp,bytes(0x500))
 if not available:
  for i in range(30):n.cpu.mem_write(visual+i*16,bytes([1]))
 for offset,value in [(0x1f0,game+0x84080),(0x80,visual)]:n.cpu.mem_write(sp+offset,struct.pack('<Q',value))
 sounds=[]
 def sound():sounds.append(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1));return 0
 def unit_mode():return environment.unit_modes[(n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)-game-0x2678)//0x1f0]
 n.helpers={0x81f580:game,0x457e1c:0,0x459f04:sound,0x5c2710:unit_mode,0x5bbbc8:special,0x5bbc10:1}
 for register,value in [('SP',sp),('X19',actor),('W21',before),('W26',side),('W28',1),('W24',int(side==0))]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 n.cpu.emu_start(0x6dac8c,n.stop+4,count=100000)
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'reaction budget'
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)))
 output=Result();seed=c.c_uint32(0x12345678);assert lib.kbcs_core_actor_react(pool,c.byref(environment),side,1,c.byref(input),c.byref(seed),c.byref(output))==0
 assert bytes(pool)==expected,{'case':cases[count],'differences':[(i,a,b) for i,(a,b) in enumerate(zip(bytes(pool),expected)) if a!=b][:20]}
 assert seed.value==struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0],cases[count]
 assert list(output.sounds)[:output.sound_count]==sounds
 expected_visual=available and bool(n.cpu.mem_read(visual,1)[0]&1)
 assert output.death_visual==expected_visual
 if expected_visual:assert [output.death_x,output.death_y]==list(struct.unpack('<ii',n.cpu.mem_read(visual+4,8)))
 count+=1
 if count%43==0 or output.death_visual:
  records.append({'side':side,'before':initial,'after':list(word),'modes':list(environment.unit_modes),'special_castle':special,'input':{'previous_hp':before,'death_visual_available':available},'output':{'sound_count':output.sound_count,'sounds':list(output.sounds),'death_visual':output.death_visual,'death_x':output.death_x,'death_y':output.death_y},'seed':seed.value})
print(json.dumps({'reactionCases':count,'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entry':'006dac8c','terminals':['006db1ac','006db1b4'],'records':records,'cases':count,'controlled':['singleton game address','unit mode and special castle getters','sound emission capture']}
(ROOT/'research/.local/actor-reaction-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-reaction-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
