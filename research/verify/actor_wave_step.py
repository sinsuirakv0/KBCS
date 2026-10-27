"""波動の生成時計・区間・遮断・命中を連続ARM64実行へ比較する。"""
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
 _fields_=[('unit_modes',c.c_int32*2),*[(name,c.c_int32) for name in ['stage_width','castle_slot','castle_x','castle_scale','castle_offset','stage_kind','zombie','chapter_rate','crown','hp_percent','attack_percent']],('crystal_max',c.c_int32*5),('crystal',c.c_int32*5),('treasures',c.c_int32*32),('combos',c.c_int32*32),('orb_stage',c.c_int32),('talents_disabled',c.c_int32),('parameters',c.c_int32*2),('spawned',c.c_int32*2),('spawn_row',c.c_int32*14),('special_castle',c.c_int32)]
class Direct(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','target','hit','kind','parameter','rate']]+[('flags',c.c_int32*12)]
class Hit(c.Structure):_fields_=[('hit',Direct),('attack_type',c.c_int32)]
class Wave(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','state','frame','x','level','hit']]+[('flags',c.c_uint8*12),('parameter',c.c_int32),('mini',c.c_uint8),('reserved',c.c_uint8*3)]
class Waves(c.Structure):_fields_=[('records',Wave*200),('hits',(c.c_uint8*200)*51)]
class Segment(c.Structure):_fields_=[('frame',c.c_int32),('x',c.c_int32)]
class Segments(c.Structure):_fields_=[('records',(Segment*6)*200)]
class Rules(c.Structure):_fields_=[('small_interval',c.c_int32),('small_start',c.c_int32),('small_end',c.c_int32),('motion_frames',c.c_int32*2),('game_mode',c.c_int32)]
Sink=c.CFUNCTYPE(c.c_uint32,c.c_void_p,c.POINTER(Actor*51),c.POINTER(c.c_uint32),c.POINTER(Hit),c.POINTER(c.c_int32))
class WaveNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
  if address in self.allowed:return
  return super().hook(cpu,address,size,data)
 def value(self,index):return self.cpu.reg_read(getattr(self.reg,'UC_ARM64_REG_X'+str(index)))
 def call(self,entry,*values):
  self.entry=entry;self.cpu.reg_write(self.reg.UC_ARM64_REG_SP,self.stack+0x8000);self.cpu.reg_write(self.reg.UC_ARM64_REG_LR,self.stop)
  for i,value in enumerate(values):self.cpu.reg_write(getattr(self.reg,'UC_ARM64_REG_X'+str(i)),value)
  self.cpu.emu_start(entry,self.stop+4,count=2000000)
  assert self.cpu.reg_read(self.reg.UC_ARM64_REG_PC)==self.stop,'wave budget'
n=WaveNative();game,heap=0x40000000,0x50000000;n.cpu.mem_map(game,0x800000);n.cpu.mem_map(heap,0x100000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
roots=[0x5d287c,0x5d2c18,0x6eab4c,0x6ead1c,0xaaf04c,0x419064]
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions']],*roots] if a in sizes for pc in range(a,a+sizes[a],4)}
n.cpu.mem_write(0xc1b578,struct.pack('<Q',0xc24400))
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()))
lib.kbcs_core_actor_waves_step.argtypes=[c.c_int32,c.POINTER(Waves),c.POINTER(Segments),c.POINTER(Actor*51),c.POINTER(Environment),c.POINTER(Rules),c.POINTER(c.c_uint32),Sink,c.c_void_p,c.POINTER(c.c_int32)]
lib.kbcs_core_actor_last_error.restype=c.c_int64
def pod(value):
 if isinstance(value,c.Structure):return {k:pod(getattr(value,k)) for k,*_ in value._fields_}
 if isinstance(value,c.Array):return [pod(v) for v in value]
 return value
def sparse(pool):return [[i,v] for i,v in enumerate(struct.unpack('<25602i',bytes(pool))) if v]
records=[];updates=hits=0
for case,(side,mini,stopper,applied) in enumerate(itertools.product([0,1],[0,1],[0,1,2,3],[0,1])):
 waves,segments,pool,environment=Waves(),Segments(),Pool(),Environment();environment.unit_modes[:]=[1,0];environment.castle_slot=50
 rules=Rules(small_interval=4,small_start=3,small_end=7,motion_frames=(c.c_int32*2)(18,19))
 wave=waves.records[0];wave.side=wave.state=side+1;wave.slot=1;wave.x=12000;wave.level=6;wave.hit=1;wave.parameter=17;wave.mini=mini;wave.flags[:]=[i%2 for i in range(12)]
 pool[side][1].words[0]=2
 for target,delta in enumerate([-700,-350,-1,0,350,700,1050,1400,1750],1):
  w=pool[1-side][target].words;w[0]=2;w[3]=wave.x+(delta if side else -delta);w[14]=13
  if stopper and target in ([3] if stopper==1 else [3,7] if stopper==2 else [1,9]):w[87]=1
 initial={'applied':applied,'pool':sparse(pool),'wave':pod(wave),'rules':pod(rules),'steps':[]}
 n.cpu.mem_write(game,bytes(0x400000));n.cpu.mem_write(game+0x84080,bytes(pool));n.cpu.mem_write(game+0x33b81c,bytes(waves.records));n.cpu.mem_write(game+0x33dd9c,bytes(segments));n.cpu.mem_write(game+0x38fbc0,bytes(waves.hits));n.cpu.mem_write(0xc249b8,struct.pack('<Q',n.memory));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678))
 seed=c.c_uint32(0x12345678);native_calls=[];cpp_calls=[];sounds=[];next_heap=heap
 def allocate():
  global next_heap
  at=next_heap;next_heap+=(n.value(0)+15)&~15;assert next_heap<heap+0x100000;n.cpu.mem_write(at,bytes(next_heap-at));return at
 def copy_memory():n.cpu.mem_write(n.value(0),bytes(n.cpu.mem_read(n.value(1),n.value(2))));return n.value(0)
 def sound():sounds.append(n.value(1));return 0
 def parameter():
  address=n.value(1);head=n.cpu.mem_read(address,24);at=struct.unpack_from('<Q',head,16)[0] if head[0]&1 else address+1
  key=bytes(n.cpu.mem_read(at,100)).split(b'\0')[0].decode('ascii');return {'battle_wave_s_inter':rules.small_interval,'battle_wave_s_frame1':rules.small_start,'battle_wave_s_frame2':rules.small_end}[key]
 def native_hit():
  values=[n.value(i) for i in range(8)]+list(struct.unpack('<11Q',n.cpu.mem_read(n.cpu.reg_read(n.reg.UC_ARM64_REG_SP),88)))
  call=Hit();call.attack_type=values[1];call.hit=Direct(side=side,slot=values[2],target=values[3],hit=values[4],kind=values[5],parameter=0 if side else values[17],rate=values[18])
  for index,arg in [(0,6),(5,7),(1,8),(2,9),(3,10),(4,11),(6,12),(8,13),(7,14),(10,16)]:call.hit.flags[index]=values[arg]&1
  if side:call.hit.flags[9]=values[15]&1;call.hit.flags[11]=values[17]&1
  native_calls.append(pod(call));return applied
 n.helpers={0x81f580:game,0x5c2710:lambda:environment.unit_modes[(n.value(0)-game-0x2678)//0x1f0],0x5bc058:0,0x5bbc10:50,0xbdb6c0:n.memory,0x44beb4:lambda:rules.motion_frames[int(n.value(0)-n.memory==0x3148)],0x9019f4:parameter,0x457e1c:0,0x459efc:sound,0xbdaf40:allocate,0xbdaf60:0,0xbdb0b0:copy_memory,0x5d9534:0,0x59d12c:0,0xa94074:0,0x6e4aec:native_hit,0x6e79bc:native_hit}
 @Sink
 def hit(user,actors,random,call,result):cpp_calls.append(pod(call.contents));result[0]=applied;return 0
 for frame in range(75):
  for phase in [0,1]:
   native_calls.clear();cpp_calls.clear();sounds.clear()
   n.call(0x5d287c if phase==0 else 0x5d2c18,game)
   output=c.c_int32(-1);code=lib.kbcs_core_actor_waves_step(phase,c.byref(waves),c.byref(segments),pool,c.byref(environment),c.byref(rules),c.byref(seed),hit,None,c.byref(output))
   expected_pool=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)))
   comparisons={'waves':(bytes(waves.records),bytes(n.cpu.mem_read(game+0x33b81c,9600))),'segments':(bytes(segments),bytes(n.cpu.mem_read(game+0x33dd9c,c.sizeof(segments)))),'history':(bytes(waves.hits),bytes(n.cpu.mem_read(game+0x38fbc0,10200))),'pool':(bytes(pool),expected_pool)}
   diff={name:[(i,a,b) for i,(a,b) in enumerate(zip(*pair)) if a!=b][:12] for name,pair in comparisons.items() if pair[0]!=pair[1]}
   assert not code and not diff and native_calls==cpp_calls,(case,frame,phase,code,hex(lib.kbcs_core_actor_last_error()),diff,native_calls,cpp_calls)
   assert output.value==len(sounds) and all(v==26 for v in sounds)
   assert seed.value==struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]
   updates+=1;hits+=len(cpp_calls)
   if case%7==0 and (frame<25 or cpp_calls):
    initial['steps'].append({'frame':frame,'phase':phase,'wave':pod(waves.records[0]),'segments':pod(segments.records[0]),'history':[waves.hits[j][0] for j in range(51)],'pool':sparse(pool),'calls':cpp_calls.copy(),'sounds':output.value})
 if initial['steps']:records.append(initial)
print(json.dumps({'cases':case+1,'updates':updates,'hits':hits}))
report={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'cases':case+1,'updates':updates,'hits':hits,'records':records,'controlled':['motion lengths and small-wave parameter values','sound capture','allocator/memcpy/tree cleanup','hit bodies return controlled applied'],'entries':['005d287c','005d2c18','006eab4c','006ead1c']}
(ROOT/'research/.local/actor-wave-step-1572.json').write_text(json.dumps(report,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-wave-step-vectors.json').write_text(json.dumps(report,separators=(',',':')),encoding='utf-8-sig')
