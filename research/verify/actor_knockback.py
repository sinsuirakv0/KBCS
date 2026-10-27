"""味方のKB/ふっとばし・死亡移行をARM64と比較する。敵の蘇生経路とは分離。"""
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
class KnockbackNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=KnockbackNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44abfc,0x44abe4,0xa9490c] for pc in range(a,a+sizes[a],4)}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_last_error.restype=c.c_int64
class Knockback(c.Structure):_fields_=[(name,c.c_int32) for name in ['boundary','cost','quiet','game_mode']]
class Result(c.Structure):_fields_=[(name,c.c_int32) for name in ['handled','refund','sound']]
lib.kbcs_core_actor_unit_knockback.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.c_int32,c.POINTER(Knockback),c.POINTER(Result)]
n.cpu.mem_write(0xc1b630,struct.pack('<Q',0xc23fc4));n.cpu.mem_write(0xc1b680,struct.pack('<Q',0xc24024))
n.entry=0x6eb464;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={0x6eb6a4}
records=[];count=0
cases=[(side,action,frame,position,hp,0,0,0,0,0) for side,action,frame,position,hp in itertools.product([0,1],[3,5,6,7],[0,1,10,11,22,23,46,47],[199,200,201],[0,1])]
cases += [(side,action,frame,200,0,mode,rate,override,quiet,game_mode) for side,action,frame,mode,rate,override,quiet,game_mode in itertools.product([0,1],[3,5,6,7],[11,23,47],[0,2],[0,25],[0,600],[0,1],[0,4])]
for side,action,frame,position,hp,mode,rate,override,quiet,game_mode in cases:
 pool=Pool();word=pool[side][1].words
 for i,v in {0:2,1:action,2:frame,3:position,4:4480,7:100,8:hp,10:17,61:7,62:9,75:1,115:count%2,118:mode,156:[0,31,100][count%3],217:[0,17,70][count%3],231:rate,242:override}.items():word[i]=v
 word[64]=count%3;pool[1][0].words[3]=3200
 before=list(word);environment=Environment();environment.unit_modes[:]=[1,1];environment.stage_width=20000;environment.castle_x=3200;environment.castle_scale=[75,100,127][count%3];environment.castle_offset=13
 n.cpu.mem_write(game+0x9ee48,struct.pack('<i',environment.stage_width))
 input=Knockback(200,400,quiet,game_mode);sp=n.stack+0x8000;fp=sp+0x200;actor=game+0x84080+side*0xc804+0x3ec
 n.cpu.mem_write(game+0x84080,bytes(pool));n.cpu.mem_write(game+0x32e9,bytes([quiet]))
 n.cpu.mem_write(sp,bytes(0x400));n.cpu.mem_write(fp-0xb4,struct.pack('<i',60 if side==0 else -60));n.cpu.mem_write(sp+0xb4,struct.pack('<i',20 if side==0 else -20));n.cpu.mem_write(sp+0xc8,struct.pack('<Q',game+side*0x1f0))
 sounds=[];refunds=[]
 def sound():sounds.append(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1));return 0
 def refund():refunds.append(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1));return 0
 def unit_mode():return environment.unit_modes[(n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)-game-0x2678)//0x1f0]
 def point():n.cpu.mem_write(n.cpu.reg_read(n.reg.UC_ARM64_REG_X4),struct.pack('<ii',990 if side==0 else 20,0));return 0
 def castle():n.cpu.reg_write(n.reg.UC_ARM64_REG_W1,environment.castle_scale);return environment.castle_offset
 n.helpers={0x81f580:game,0x5bc1dc:1,0x5c2710:unit_mode,0x457e1c:0,0x459efc:sound,0x5bc058:game_mode,0x5be130:input.cost,0x5c2990:refund,
            0x5bddf8:n.memory,0x44d254:n.memory,0x44b8d4:0,0x44b8dc:0,0x44b8e4:0,0x44b854:point,0x5bbfb0:0,0x656de0:castle}
 for register,value in [('SP',sp),('X29',fp),('W20',side),('X23',1),('X22',game),('X24',n.memory),('X19',actor)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 n.cpu.emu_start(0x6eb7e0,n.stop+4,count=100000)
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'unit knockback budget'
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)));output=Result()
 code=lib.kbcs_core_actor_unit_knockback(pool,c.byref(environment),side,1,c.byref(input),c.byref(output))
 assert code==0,(cases[count],code,hex(lib.kbcs_core_actor_last_error()))
 assert output.handled==1 and bytes(pool)==expected,{'case':cases[count],'diff':[(i,a,b) for i,(a,b) in enumerate(zip(struct.unpack('<25602i',bytes(pool)),struct.unpack('<25602i',expected))) if a!=b][:10]}
 assert output.sound==(sounds[0] if sounds else -1) and output.refund==(refunds[0] if refunds else 0),(cases[count],output.sound,sounds,output.refund,refunds)
 count+=1
 if count%41==0 or (refunds and not quiet and not override and mode==0):
  records.append({'side':side,'environment':{'unit_modes':list(environment.unit_modes),'castle_x':environment.castle_x,'castle_scale':environment.castle_scale,'castle_offset':environment.castle_offset},'before':before,'after':list(word),'input':{k:getattr(input,k) for k,_ in Knockback._fields_},'output':{k:getattr(output,k) for k,_ in Result._fields_}})
print(json.dumps({'unitKnockbackCases':count,'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entry':'006eb7e0','terminal':'006eb6a4','records':records,'cases':count,'controlled':['singleton game address','unit mode/current cost/slot lookup','model point resolver (990/20), original 00a9490c executed including boss correction','sound and money emission capture','GOT relative relocation c1b630/c1b680'], 'limits':['unit mode only','death money returned as request, wallet encryption outside kernel']}
(ROOT/'research/.local/actor-knockback-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-knockback-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
