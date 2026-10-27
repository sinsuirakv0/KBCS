"""直接命中→波動→烈波→爆波を2回連続実行し、同版ARM64の状態とRNGへ照合する。"""
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
class Wave(c.Structure):
 _fields_=[(name,c.c_int32) for name in ['side','slot','state','frame','x','level','hit']]+[('flags',c.c_uint8*12),('parameter',c.c_int32),('mini',c.c_uint8),('reserved',c.c_uint8*3)]
class Waves(c.Structure):_fields_=[('records',Wave*200),('hits',(c.c_uint8*200)*51)]
class Selection(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','hit','count']]+[('targets',c.c_int32*51)]
class Hit(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','target','hit','kind','parameter','rate']]+[('flags',c.c_int32*12)]
class Emission(c.Structure):_fields_=[('flags',c.c_int32*12),('parameter',c.c_int32)]
class Surge(c.Structure):
 _fields_=[(name,c.c_int32) for name in ['side','slot','frame','x','level','hit']]+[('flags',c.c_uint8*12),('parameter',c.c_int32),('mini',c.c_uint8),('reserved',c.c_uint8*3),('kind',c.c_int32)]
class Explosion(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','frame','x','hit']]+[('flags',c.c_uint8*12),('parameter',c.c_int32)]
class Area(c.Structure):_fields_=[('surge_present',c.c_int32),('explosion_present',c.c_int32),('surge',Surge),('explosion',Explosion)]
Sink=c.CFUNCTYPE(c.c_uint32,c.c_void_p,c.POINTER(Actor*51),c.POINTER(c.c_uint32),c.POINTER(Hit),c.POINTER(c.c_int32))
class EmissionNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
  if address in self.allowed:return
  return super().hook(cpu,address,size,data)
n=EmissionNative();game=0x40000000;heap=0x50000000
n.cpu.mem_map(game,0x800000);n.cpu.mem_map(heap,0x100000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44ab70,0x44abfc,0x44abe4,0x44a8d8,0x44a8e8] for pc in range(a,a+sizes[a],4)}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_last_error.restype=c.c_int64
lib.kbcs_core_actor_emit_direct.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.POINTER(Selection),c.POINTER(c.c_uint32),Sink,c.c_void_p,c.POINTER(Emission)]
lib.kbcs_core_actor_emit_wave.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.POINTER(Selection),c.POINTER(Emission),c.POINTER(Waves),c.POINTER(c.c_uint32),c.POINTER(c.c_int32)]
lib.kbcs_core_actor_emit_area.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.POINTER(Selection),c.POINTER(Emission),c.POINTER(c.c_uint32),c.POINTER(Area)]
def sparse(pool):return [[(s*51+j)*251+i,v] for s,team in enumerate(pool) for j,actor in enumerate(team) for i,v in enumerate(actor.words) if v]
def advance(value):
 value^=(value<<13)&0xffffffff;value^=value>>17;value^=(value<<15)&0xffffffff;return value
def fields(value):return {name:list(getattr(value,name)) if isinstance(getattr(value,name),c.Array) else getattr(value,name) for name,_ in value._fields_}
records=[];count=0;steps=0
for side,hit,enabled,chances,span,capacity_mode in itertools.product([0,1],range(3),[0,1],[(-1,100),(0,100),(1,50),(50,1),(100,-1),(100,100),(100,0)],[-2147483648,-2147483647,-2,-1,0,1,2,2147483647],range(3)):
 pool=Pool();environment=Environment();environment.unit_modes[:]=[1,0];source=pool[side][1].words
 for i,v in {0:2,1:2,3:[10000,2147483647,-2147483648][count%3],7:100,8:100,84:10*(count%2),198:count%2,218:[0,17,-1][count%3],39:[0,100,50][count%3],40:7,182:count%3,174:chances[0],175:[300,-700,2147483647][count%3],176:span,177:[0,1,7,-1][count%4],211:[-1,0,1,2][count%4],224:chances[1],225:[700,-300,-2147483648][count%3],226:-span if span!=-2147483648 else span}.items():source[i]=v
 for field in [56,49,50,52,68,163,135,132,147,171,183,246]:source[field]=[0,1,50,100][(count+field)%4]
 for field in [123,124,125]:source[field]=enabled
 for target in [1,2]:pool[1-side][target].words[0]=2;pool[1-side][target].words[1]=14 if target==1 else 0
 selection=Selection(side=side,slot=1,hit=hit,count=2);selection.targets[:2]=[1,2]
 waves=Waves();c.memset(c.byref(waves),0x6b,c.sizeof(waves))
 for i,wave in enumerate(waves.records):wave.side=int(count%3==0 or i<199);wave.state=0
 n.cpu.mem_write(game+0x33b81c,bytes(waves.records));n.cpu.mem_write(game+0x38fbc0,bytes(waves.hits))
 n.cpu.mem_write(game+0x84080,bytes(pool));initial_seed=[0x12345678,1,0xffffffff][count%3]
 n.cpu.mem_write(0xc24d18,struct.pack('<I',initial_seed));seed=c.c_uint32(initial_seed)
 n.cpu.mem_write(game+0x38fb8c,bytes(48));allocated=heap+0x4000;original=[];cpp_records=[[],[]]
 for index,offset in enumerate([0x340320,0x340350]):
  begin=heap+index*0x1000;size=72 if index==0 else 64;old=heap+0x2000+index*0x100
  n.cpu.mem_write(old,bytes([0x4b+index])*size);original.append((old,bytes(n.cpu.mem_read(old,size))))
  present=int(capacity_mode!=0);capacity=[0,1,8][capacity_mode]
  n.cpu.mem_write(begin,struct.pack('<Q',old));n.cpu.mem_write(game+offset,struct.pack('<QQQ',begin if capacity else 0,begin+present*8 if capacity else 0,begin+capacity*8 if capacity else 0))
 vector=n.memory+0x2000;data=n.memory+0x3000;n.cpu.mem_write(vector,struct.pack('<QQQ',data,data+8,data+8));n.cpu.mem_write(data,struct.pack('<ii',1,2))
 def allocate():
  global allocated
  size=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);assert size<0x1000
  result=allocated;allocated+=(size+15)//16*16;n.cpu.mem_write(result,bytes([0x6b])*size);return result
 def copy():
  target=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);source=n.cpu.reg_read(n.reg.UC_ARM64_REG_X1);size=n.cpu.reg_read(n.reg.UC_ARM64_REG_X2)
  if size:n.cpu.mem_write(target,bytes(n.cpu.mem_read(source,size)))
  return target
 def unit_mode():
  team=(n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)-game-0x2678)//0x1f0;assert team in [0,1];return environment.unit_modes[team]
 def native_hit():
  if count%2:
   address=game+0x84080+side*0xc804+0x3ec
   for word in [3,218]:
    value=struct.unpack('<i',n.cpu.mem_read(address+word*4,4))[0];n.cpu.mem_write(address+word*4,struct.pack('<i',c.c_int32(value+1).value))
   value=struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0];n.cpu.mem_write(0xc24d18,struct.pack('<I',advance(value)))
  return count%2
 @Sink
 def emit(user,actors,random,event,result):
  if count%2:
   words=actors[side][1].words;words[3]=c.c_int32(words[3]+1).value;words[218]=c.c_int32(words[218]+1).value;random[0]=advance(random[0])
  result[0]=count%2;return 0
 n.helpers={0x81f580:game,0x5c2710:unit_mode,0xa94074:0,0x4253b4:0,0xbdaf60:0,0xbdaf40:allocate,0xbdb0b0:copy,0x6e4aec:native_hit,0x6e79bc:native_hit}
 n.entry=0x6ea1c0 if side else 0x6e92bc;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={n.stop}
 for step in range(2):
  before=sparse(pool);n.cpu.mem_write(n.stack+0x6000,bytes(0x4000))
  for i,value in enumerate([game,1,vector,hit,0,0,0,0]):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),value)
  n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,n.stack+0x8000);n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop)
  try:n.cpu.emu_start(n.entry,n.stop+4,count=500000)
  except Exception as error:raise RuntimeError((count,step,side,hit,enabled,chances,span,capacity_mode,hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)))) from error
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==n.stop
  output=Emission();code=lib.kbcs_core_actor_emit_direct(pool,c.byref(environment),c.byref(selection),c.byref(seed),emit,None,c.byref(output));assert code==0,(count,code)
  wave_slot=c.c_int32();code=lib.kbcs_core_actor_emit_wave(pool,c.byref(environment),c.byref(selection),c.byref(output),c.byref(waves),c.byref(seed),c.byref(wave_slot));assert code==0,(count,code)
  area_seed=seed.value;after=sparse(pool);area=Area();c.memset(c.byref(area),0x6b,c.sizeof(area))
  code=lib.kbcs_core_actor_emit_area(pool,c.byref(environment),c.byref(selection),c.byref(output),c.byref(seed),c.byref(area));assert code==0,(count,code,hex(lib.kbcs_core_actor_last_error()))
  expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)));expected_seed=struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]
  assert bytes(pool)==expected and seed.value==expected_seed,{'case':count,'step':step,'seed':(seed.value,expected_seed),'poolEqual':bytes(pool)==expected}
  assert bytes(waves.records)==n.cpu.mem_read(game+0x33b81c,c.sizeof(waves.records)) and bytes(waves.hits)==n.cpu.mem_read(game+0x38fbc0,c.sizeof(waves.hits)),count
  for index,(present,record,offset) in enumerate([(area.surge_present,area.surge,0x340320),(area.explosion_present,area.explosion,0x340350)]):
   assert present in [0,1]
   if present:cpp_records[index].append(bytes(record))
   else:assert not any(bytes(record))
   begin,end,capacity=struct.unpack('<QQQ',n.cpu.mem_read(game+offset,24));initial=int(capacity_mode!=0)
   assert (end-begin)//8==initial+len(cpp_records[index]) and capacity>=end,(count,index)
   for j,payload in enumerate(cpp_records[index]):
    pointer=struct.unpack('<Q',n.cpu.mem_read(begin+(initial+j)*8,8))[0]
    expected_record=payload+ (b'' if index==0 else bytes(4))+struct.pack('<Q',pointer+(56 if index==0 else 48))+bytes(16)
    raw=bytes(n.cpu.mem_read(pointer,72 if index==0 else 64));assert raw==expected_record,{'case':count,'step':step,'record':index,'actual':list(raw),'expected':list(expected_record)}
   if initial:assert struct.unpack('<Q',n.cpu.mem_read(begin,8))[0]==original[index][0]
   assert bytes(n.cpu.mem_read(original[index][0],len(original[index][1])))==original[index][1]
  steps+=1
  if count%73==0 or (enabled and chances==(100,100) and span in [-1,0,1] and capacity_mode==1):
   records.append({'side':side,'hit':hit,'step':step,'before':before,'after':after,'area_seed':area_seed,'seed':expected_seed,'emission':fields(output),'area':{**fields(area),'surge':fields(area.surge),'explosion':fields(area.explosion)}})
 count+=1
 if count%500==0:print(json.dumps({'cases':count,'steps':steps}),flush=True)
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entries':['006e92bc','006ea1c0'],'cases':count,'steps':steps,'records':records,'controlled':['singleton game address and decoded unit modes','debug name/string construction/destruction','successful allocator/delete/memcpy; empty, growth and spare vector capacity','006e4aec/006e79bc applied return plus optional source/RNG mutation'],'limits':['full emission function only; actual hit bodies, secondary effect lifetime/hits and full battle dispatch not executed','native raw pointers/vector capacity normalized to typed emission records; allocation failure not exercised']}
(ROOT/'research/.local/actor-area-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-area-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
print(json.dumps({'areaEmissionCases':count,'consecutiveSteps':steps,'published':len(records)}))
