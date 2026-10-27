"""直接命中から波動生成までの連続したRNG・200枠・命中履歴を同版ARM64へ照合する。"""
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
class DirectNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=DirectNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44abfc,0x44abe4,0x44a8d8,0x44a8e8] for pc in range(a,a+sizes[a],4)}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_last_error.restype=c.c_int64
class Motion(c.Structure):_fields_=[('encoded',c.c_int32*8),('plain',c.c_int32*8),('soul_frames',c.c_int32)]
class Wave(c.Structure):
 _fields_=[(name,c.c_int32) for name in ['side','slot','state','frame','x','level','hit']]+[('flags',c.c_uint8*12),('parameter',c.c_int32),('mini',c.c_uint8),('reserved',c.c_uint8*3)]
class Waves(c.Structure):_fields_=[('records',Wave*200),('hits',(c.c_uint8*200)*51)]
class Selection(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','hit','count']]+[('targets',c.c_int32*51)]
class Hit(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','target','hit','kind','parameter','rate']]+[('flags',c.c_int32*12)]
class Emission(c.Structure):_fields_=[('flags',c.c_int32*12),('parameter',c.c_int32)]
Sink=c.CFUNCTYPE(c.c_uint32,c.c_void_p,c.POINTER(Actor*51),c.POINTER(c.c_uint32),c.POINTER(Hit),c.POINTER(c.c_int32))
lib.kbcs_core_actor_emit_direct.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.POINTER(Selection),c.POINTER(c.c_uint32),Sink,c.c_void_p,c.POINTER(Emission)]
lib.kbcs_core_actor_emit_wave.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.POINTER(Selection),c.POINTER(Emission),c.POINTER(Waves),c.POINTER(c.c_uint32),c.POINTER(c.c_int32)]
def sparse(pool):return [[(s*51+j)*251+i,v] for s,team in enumerate(pool) for j,actor in enumerate(team) for i,v in enumerate(actor.words) if v]
def advance(value):
 value^=(value<<13)&0xffffffff;value^=value>>17;value^=(value<<15)&0xffffffff;return value
records=[];count=0
for side,hit,enabled,chance,occupied,kind in itertools.product([0,1],range(3),[0,1],[-1,0,1,50,100],[0,1,199,200],[0,1,2]):
 probability=[0,1,50,100][count%4];targets=[1,2];applied=count%2;mutation=count%3
 pool=Pool();environment=Environment();environment.unit_modes[:]=[1,0]
 source=pool[side][1].words
 for i,v in {0:2,1:2,7:100,8:100,84:10*(count%2),198:int(count%3==0),218:[0,17,-1][count%3]}.items():source[i]=v
 for field in [56,49,50,52,68,163,135,132,147,171,183,246]:source[field]=probability
 for field in [123,124,125]:source[field]=enabled
 source[3]=10000;source[39]=chance;source[40]=7;source[182]=kind
 for target in range(3):
  word=pool[1-side][target].words
  for i,v in {0:2 if target else 1,1:14 if target%2 else 0,7:100,8:100,96:9}.items():word[i]=v
 selection=Selection(side=side,slot=1,hit=hit,count=len(targets));selection.targets[:len(targets)]=targets
 waves=Waves();c.memset(c.byref(waves),0x6b,c.sizeof(waves))
 for i,wave in enumerate(waves.records):wave.side=int(i<occupied and i%2==0);wave.state=int(i<occupied and i%2==1)
 wave_before=bytes(waves);n.cpu.mem_write(game+0x33b81c,bytes(waves.records));n.cpu.mem_write(game+0x38fbc0,bytes(waves.hits))
 initial_parameter=0 if side else source[218]
 before=sparse(pool);n.cpu.mem_write(game+0x84080,bytes(pool));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678));n.cpu.mem_write(game+0x38fb8c,struct.pack('<12i',*[123]*12))
 vector=n.memory+0x2000;data=n.memory+0x3000
 n.cpu.mem_write(vector,struct.pack('<QQQ',data,data+len(targets)*4,data+len(targets)*4))
 if targets:n.cpu.mem_write(data,struct.pack('<'+'i'*len(targets),*targets))
 n.cpu.mem_write(n.stack+0x6000,bytes(0x4000));native_events=[];cpp_events=[]
 def unit_mode():
  address=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);team=(address-game-0x2678)//0x1f0
  assert team in [0,1];return environment.unit_modes[team]
 def native_hit():
  raw=[n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i))) for i in range(8)]
  sp=n.cpu.reg_read(n.reg.UC_ARM64_REG_SP);raw+=list(struct.unpack('<11Q',n.cpu.mem_read(sp,88)))
  assert raw[1]==0 and raw[2]==1 and raw[4]==hit and raw[5]==0 and raw[18]==100
  target=raw[3];flags=[0]*12
  for index,parameter in [(0,7),(5,8),(1,9),(2,10),(3,11),(4,12),(6,13),(8,14),(7,15),(10,17)]:flags[index]=int(raw[parameter-1]!=0)
  if side:flags[9]=int(raw[15]!=0);flags[11]=int(raw[17]!=0)
  else:assert raw[15]==0
  parameter=0 if side else c.c_int32(raw[17]).value
  state=struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]
  native_events.append({'side':side,'slot':1,'target':target,'hit':hit,'kind':0,'parameter':parameter,'rate':100,'flags':flags,'seed':state})
  address=game+0x84080+side*0xc804+0x3ec
  if mutation==1:n.cpu.mem_write(game+0x84080+(1-side)*0xc804+target*0x3ec+4,struct.pack('<i',14))
  if mutation==2:
   value=struct.unpack('<i',n.cpu.mem_read(address+218*4,4))[0];n.cpu.mem_write(address+218*4,struct.pack('<i',value+1));value=struct.unpack('<i',n.cpu.mem_read(address+12,4))[0];n.cpu.mem_write(address+12,struct.pack('<i',value+5))
   value=struct.unpack('<i',n.cpu.mem_read(address+84*4,4))[0];n.cpu.mem_write(address+84*4,struct.pack('<i',0 if value else 10));n.cpu.mem_write(0xc24d18,struct.pack('<I',advance(state)))
  return applied
 n.helpers={0x81f580:game,0x5c2710:unit_mode,0xa94074:0,0x4253b4:0,0xbdaf60:0,0x6e4aec:native_hit,0x6e79bc:native_hit}
 n.entry=0x6ea1c0 if side else 0x6e92bc;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={n.stop,0x6ea62c if side else 0x6e9768}
 for i,value in enumerate([game,1,vector,hit,0,0,0,0]):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),value)
 n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,n.stack+0x8000);n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop)
 try:n.cpu.emu_start(n.entry,n.stop+4,count=500000)
 except Exception as error:raise RuntimeError((count,side,hit,enabled,chance,occupied,kind,hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)))) from error
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,(count,side,hit,enabled,chance,occupied,kind,hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)))
 expected_waves=bytes(n.cpu.mem_read(game+0x33b81c,c.sizeof(waves.records)))+bytes(n.cpu.mem_read(game+0x38fbc0,c.sizeof(waves.hits)))
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)));expected_seed=struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0];flags=list(struct.unpack('<12i',n.cpu.mem_read(game+0x38fb8c,48)))
 @Sink
 def emit(user,actors,seed,call,result):
  event=call.contents
  cpp_events.append({**{k:getattr(event,k) for k,_ in Hit._fields_ if k!='flags'},'flags':list(event.flags),'seed':seed[0]})
  if mutation==1:actors[1-side][event.target].words[1]=14
  if mutation==2:
   words=actors[side][1].words;words[218]+=1;words[3]+=5;words[84]=0 if words[84] else 10;seed[0]=advance(seed[0])
  result[0]=applied;return 0
 seed=c.c_uint32(0x12345678);output=Emission()
 code=lib.kbcs_core_actor_emit_direct(pool,c.byref(environment),c.byref(selection),c.byref(seed),emit,None,c.byref(output))
 assert code==0,(count,code,hex(lib.kbcs_core_actor_last_error()))
 direct_seed=seed.value;spawned=c.c_int32()
 code=lib.kbcs_core_actor_emit_wave(pool,c.byref(environment),c.byref(selection),c.byref(output),c.byref(waves),c.byref(seed),c.byref(spawned))
 assert code==0 and bytes(waves)==expected_waves,{'case':(count,side,hit,enabled,chance,occupied,kind),'code':code,'waveDiff':[(i,a,b) for i,(a,b) in enumerate(zip(bytes(waves),expected_waves)) if a!=b][:20]}
 expected_slot=occupied if occupied<200 and bytes(waves)!=wave_before else -1
 assert spawned.value==expected_slot
 assert bytes(pool)==expected and seed.value==expected_seed and native_events==cpp_events and list(output.flags)==flags,{'case':(count,side,hit,enabled,probability,targets,applied,mutation),'seed':(seed.value,expected_seed),'events':(cpp_events,native_events),'flags':(list(output.flags),flags),'diff':[(i,a,b) for i,(a,b) in enumerate(zip(struct.unpack('<25602i',bytes(pool)),struct.unpack('<25602i',expected))) if a!=b][:10]}
 assert output.parameter==initial_parameter
 count+=1
 if count%37==0:records.append({'side':side,'hit':hit,'targets':targets,'before':before,'after':sparse(pool),'applied':applied,'mutation':mutation,'events':native_events,'seed':expected_seed,'output':{'flags':list(output.flags),'parameter':output.parameter},'chance':chance,'kind':kind,'occupied':occupied,'direct_seed':direct_seed,'spawned':spawned.value,'wave':list(bytes(waves.records[spawned.value])) if spawned.value>=0 else []})
print(json.dumps({'waveEmissionCases':count,'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entries':['006e92bc','006ea1c0'],'terminals':['006e9768','006ea62c','function return when disabled'],'records':records,'cases':count,'controlled':['singleton game address','wave records and 51x200 hit marks supplied with stale data and partial busy fields','decoded per-side unit modes','debug name/string formatting and destruction','006e4aec/006e79bc captured arguments and controlled applied result, target/source/RNG mutation'],'limits':['through wave generation; actual hit gates/damage, wave lifetime/hits and surge/explosion suffix not executed']}
(ROOT/'research/.local/actor-wave-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-wave-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
