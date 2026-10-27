"""006da994..006dac68のHP・再生産遅延・生き残りをARM64と比較する。"""
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
class Health(c.Structure):_fields_=[(name,c.c_int32) for name in ['deployment_slot','cooldown','preserve_enemy_castle']]
class Result(c.Structure):_fields_=[(name,c.c_int32) for name in ['previous_hp','delay_slot','delay_frames','delay_x','delay_y','sound']]
class HealthNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=HealthNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44a8d8,0x44a8e8,0x5bb5dc] for pc in range(a,a+sizes[a],4)}
n.entry=0x6d6d04;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={0x6dac68}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_health.argtypes=[c.POINTER(Actor*51),c.c_int32,c.c_int32,c.POINTER(Health),c.POINTER(c.c_uint32),c.POINTER(Result)]
records=[];count=0
cases=[(side,slot,hp,damage,chance,used,immune,0,0,0) for side,slot,hp,damage,chance,used,immune in itertools.product([0,1],[0,1],[0,1,100],[0,99,100,101],[0,1,50,99,100],[0,1],[0,1])]
cases += [(side,slot,100,100,70,0,0,delay,cooldown,deployment) for side,slot,delay,cooldown,deployment in itertools.product([0,1],[0,1],[0,1,100],[-1,0,1],[0,9,20])]
for side,slot,hp,damage,chance,used,immune,delay,cooldown,deployment in cases:
 pool=Pool();word=pool[side][slot].words
 for i,v in {0:2,3:12345,4:-200,7:100,8:hp,19:damage,73:chance,77:used,111:immune,248:delay}.items():word[i]=v
 before=list(word);input=Health(deployment,cooldown,count%2)
 n.cpu.mem_write(game,bytes(0x500000));n.cpu.mem_write(game+0x84080,bytes(pool))
 n.cpu.mem_write(game+0x39a228,bytes([input.preserve_enemy_castle]));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678))
 sp=n.stack+0x8000;actor=game+0x84080+side*0xc804+slot*0x3ec;vector=n.memory+0x4000;storage=n.memory+0x6000;visual=n.memory+0x7000
 n.cpu.mem_write(vector,bytes(0x500));n.cpu.mem_write(vector+0x398,struct.pack('<QQ',storage,storage+0x100))
 n.cpu.mem_write(visual,bytes(12));n.cpu.mem_write(sp,bytes(0x500))
 for offset,value in [(0x1f0,game+0x84080),(0x1d8,game+0x84080+side*0xc804),(0x1e0,vector)]:n.cpu.mem_write(sp+offset,struct.pack('<Q',value))
 n.cpu.mem_write(sp+0x1d0,struct.pack('<I',int(side==0 or slot!=0)))
 sounds=[]
 def sound():sounds.append(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1));return 0
 n.helpers={0x81f580:game,0x457e1c:0,0x459efc:sound,0xbdaf40:visual,0x5bc1dc:deployment,0x5c2d18:cooldown}
 for register,value in [('SP',sp),('X19',actor),('X27',game),('W26',side),('W28',slot),('W24',int(side==0))]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 n.cpu.emu_start(0x6da994,n.stop+4,count=100000)
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'health budget'
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)))
 output=Result();seed=c.c_uint32(0x12345678);assert lib.kbcs_core_actor_health(pool,side,slot,c.byref(input),c.byref(seed),c.byref(output))==0
 assert bytes(pool)==expected,{'case':cases[count],'differences':[(i,a,b) for i,(a,b) in enumerate(zip(bytes(pool),expected)) if a!=b][:20]}
 assert seed.value==struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0],cases[count]
 assert output.sound==(sounds[0] if sounds else -1)
 assert output.previous_hp==hp
 expected_delay=side==0 and delay>0 and cooldown>0
 assert output.delay_slot==(deployment if expected_delay else -1)
 if expected_delay:
  assert output.delay_frames==struct.unpack('<i',n.cpu.mem_read(sp+0x360+deployment*4,4))[0]
  assert [output.delay_x,output.delay_y]==list(struct.unpack('<ii',n.cpu.mem_read(visual,8)))
 count+=1
 if count%31==0 or (expected_delay and deployment==20):
  records.append({'side':side,'slot':slot,'before':before,'after':list(word),'input':{k:getattr(input,k) for k,_ in Health._fields_},'output':{k:getattr(output,k) for k,_ in Result._fields_},'seed':seed.value})
print(json.dumps({'healthCases':count,'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entry':'006da994','terminal':'006dac68','records':records,'cases':count,'controlled':['singleton game address','deployment lookup/cooldown decoded value','sound emission capture','preallocated visual vector and operator_new']}
(ROOT/'research/.local/actor-health-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-health-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
