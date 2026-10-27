"""烈波・反射待ち・爆波を原本順で連続実行し、履歴・命中引数・RNG・寿命を比較する。"""
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
parser.add_argument('--assets',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,Assets,ROOT,SHA
assets=Assets(args.assets);parameters_text=assets.text('Data/param.tsv')
source_parameters={key:int(value) for line in parameters_text.splitlines() if '\t' in line for key,value in [line.split('\t',1)] if key.startswith(('battle_demon_summon_','battle_explosion_'))}
class Actor(c.Structure):_fields_=[('words',c.c_int32*251)]
Pool=(Actor*51)*2
class Environment(c.Structure):
 _fields_=[('unit_modes',c.c_int32*2),*[(name,c.c_int32) for name in ['stage_width','castle_slot','castle_x','castle_scale','castle_offset','stage_kind','zombie','chapter_rate','crown','hp_percent','attack_percent']],('crystal_max',c.c_int32*5),('crystal',c.c_int32*5),('treasures',c.c_int32*32),('combos',c.c_int32*32),('orb_stage',c.c_int32),('talents_disabled',c.c_int32),('parameters',c.c_int32*2),('spawned',c.c_int32*2),('spawn_row',c.c_int32*14),('special_castle',c.c_int32)]
class Hit(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','target','hit','kind','parameter','rate']]+[('flags',c.c_int32*12)]
class SecondaryHit(c.Structure):_fields_=[('hit',Hit),('attack_type',c.c_int32)]
class Surge(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','frame','x','level','hit']]+[('flags',c.c_uint8*12),('parameter',c.c_int32),('mini',c.c_uint8),('reserved',c.c_uint8*3),('kind',c.c_int32)]
class Explosion(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','frame','x','hit']]+[('flags',c.c_uint8*12),('parameter',c.c_int32)]
class Area(c.Structure):_fields_=[('surge_present',c.c_int32),('explosion_present',c.c_int32),('surge',Surge),('explosion',Explosion)]
class Reflection(c.Structure):_fields_=[(name,c.c_int32) for name in ['side','slot','state','frame','x','level','offset','span']]+[('mini',c.c_uint8),('reserved',c.c_uint8*3)]
class Rules(c.Structure):_fields_=[('summon_sound_frame',c.c_int32),('summon_frame',c.c_int32),('summon_motion',c.c_int32*2),('explosion_frames',c.c_int32*4),('explosion_widths',c.c_int32*3),('explosion_damage',c.c_int32*3)]
class History(c.Structure):_fields_=[('cycles',c.c_int32*51),('present',c.c_uint8*51)]
class ExplosionHistory(c.Structure):_fields_=[('hits',(c.c_uint8*5)*51)]
class Counts(c.Structure):_fields_=[(name,c.c_int32) for name in ['surges','reflections','explosions','events']]
class Event(c.Structure):_fields_=[('kind',c.c_int32),('value',c.c_int32)]
Sink=c.CFUNCTYPE(c.c_uint32,c.c_void_p,c.POINTER(Actor*51),c.POINTER(c.c_uint32),c.POINTER(SecondaryHit),c.POINTER(c.c_int32))
class SecondaryNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
  if address in self.allowed:return
  return super().hook(cpu,address,size,data)
n=SecondaryNative();game=0x40000000;heap=0x50000000;n.cpu.mem_map(game,0x800000);n.cpu.mem_map(heap,0x400000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
roots=[0x5d3af8,0x5d4158,0x5d4988,0x6eaef0,0x6eb364,0x419064,0x44ab70,0x44abfc,0x44abe4,0x44a8d8,0x44a8e8]
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],*roots] for pc in range(a,a+sizes[a],4)}
for got,target in zip(range(0xc1b580,0xc1b5a8,8),range(0xc23e68,0xc23e7c,4)):n.cpu.mem_write(got,struct.pack('<Q',target))
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()))
lib.kbcs_core_actor_areas_create.argtypes=[c.POINTER(c.c_void_p)];lib.kbcs_core_actor_areas_destroy.argtypes=[c.c_void_p]
lib.kbcs_core_actor_areas_append.argtypes=[c.c_void_p,c.POINTER(Area)];lib.kbcs_core_actor_areas_counts.argtypes=[c.c_void_p,c.POINTER(Counts)]
lib.kbcs_core_actor_areas_surge.argtypes=[c.c_void_p,c.c_int32,c.POINTER(Surge),c.POINTER(History)]
lib.kbcs_core_actor_areas_reflection.argtypes=[c.c_void_p,c.c_int32,c.POINTER(Reflection)]
lib.kbcs_core_actor_areas_explosion.argtypes=[c.c_void_p,c.c_int32,c.POINTER(Explosion),c.POINTER(ExplosionHistory)]
lib.kbcs_core_actor_areas_event.argtypes=[c.c_void_p,c.c_int32,c.POINTER(Event)]
lib.kbcs_core_actor_areas_step.argtypes=[c.c_void_p,c.c_int32,c.POINTER(Actor*51),c.POINTER(Environment),c.POINTER(Rules),c.POINTER(c.c_uint32),Sink,c.c_void_p]
def sparse(pool):return [[(s*51+j)*251+i,v] for s,team in enumerate(pool) for j,actor in enumerate(team) for i,v in enumerate(actor.words) if v]
def fields(value):return {name:list(getattr(value,name)) if isinstance(getattr(value,name),c.Array) else getattr(value,name) for name,_ in value._fields_}
def advance(value):
 value^=(value<<13)&0xffffffff;value^=value>>17;value^=(value<<15)&0xffffffff;return value
def i32(value):return c.c_int32(value).value
def pointer(address):return struct.unpack('<Q',n.cpu.mem_read(address,8))[0]
def integer(address):return struct.unpack('<i',n.cpu.mem_read(address,4))[0]
def native_list(offset):
 begin,end=struct.unpack('<QQ',n.cpu.mem_read(game+offset,16));return [pointer(at) for at in range(begin,end,8)]
def tree(root,explosion=False):
 if not root:return []
 return tree(pointer(root),explosion)+[[integer(root+28),list(n.cpu.mem_read(root+32,5)) if explosion else integer(root+32)]]+tree(pointer(root+8),explosion)
def snapshot(native,handle,pool,seed,events):
 result={'surges':[],'reflections':[],'explosions':[],'events':events,'seed':seed,'pool':sparse(pool)}
 if native:
  for at in native_list(0x340320):result['surges'].append({'record':fields(Surge.from_buffer_copy(n.cpu.mem_read(at,48))),'history':tree(pointer(at+56))})
  for at in native_list(0x340338):result['reflections'].append(fields(Reflection.from_buffer_copy(n.cpu.mem_read(at,36))))
  for at in native_list(0x340350):result['explosions'].append({'record':fields(Explosion.from_buffer_copy(n.cpu.mem_read(at,36))),'history':tree(pointer(at+48),True)})
 else:
  counts=Counts();assert lib.kbcs_core_actor_areas_counts(handle,c.byref(counts))==0
  for i in range(counts.surges):
   record=Surge();history=History();assert lib.kbcs_core_actor_areas_surge(handle,i,c.byref(record),c.byref(history))==0
   result['surges'].append({'record':fields(record),'history':[[j,history.cycles[j]] for j in range(51) if history.present[j]]})
  for i in range(counts.reflections):
   record=Reflection();assert lib.kbcs_core_actor_areas_reflection(handle,i,c.byref(record))==0;result['reflections'].append(fields(record))
  for i in range(counts.explosions):
   record=Explosion();history=ExplosionHistory();assert lib.kbcs_core_actor_areas_explosion(handle,i,c.byref(record),c.byref(history))==0
   result['explosions'].append({'record':fields(record),'history':[[j,list(history.hits[j])] for j in range(51) if any(history.hits[j])]})
  result['events']=[]
  for i in range(counts.events):
   event=Event();assert lib.kbcs_core_actor_areas_event(handle,i,c.byref(event))==0;result['events'].append(fields(event))
 return result
records=[];case_count=0;updates=0;hit_count=0
for side,kind,mini,scenario,applied in itertools.product([0,1],range(3),[0,1],range(4),[0,1]):
 mode=(kind+scenario)%4;rules=Rules()
 original=(source_parameters['battle_demon_summon_se_frame'],source_parameters['battle_demon_summon_frame'],[81,81],*[ [source_parameters['battle_explosion_'+key+str(i+1)] for i in range(length)] for key,length in [('frame',4),('width',3),('damage',3)] ])
 rule_values=[original,(0,1,[1,2],[1,2,1,2],[801,501,401],[99,71,41]),(1,2,[2,2],[0,1,0,0],[800,500,400],[101,69,39]),(0,3,[5,4],[1,3,1,1],[-800,0,-400],[100,70,40])][mode]
 rules.summon_sound_frame,rules.summon_frame=rule_values[:2];rules.summon_motion[:]=rule_values[2];rules.explosion_frames[:]=rule_values[3];rules.explosion_widths[:]=rule_values[4];rules.explosion_damage[:]=rule_values[5]
 frames=140 if mode==0 else 34;pool=Pool();environment=Environment();environment.unit_modes[:]=[1,0]
 for team in range(2):
  for slot in range(0,12):
   word=pool[team][slot].words
   for i,value in {0:2 if slot else 1,1:[0,1,2,3,4,11,13,14,15,16,21,0][slot],3:10000+[-750,-500,-250,0,250,500,750,999,1000,-1000,1500][slot%11],7:100,8:100,14:0 if scenario%2==0 else 120,174:100,175:[-200,0,700,999][scenario],176:[0,1,-1,400][scenario],177:1,187:500,188:[-1,0,1,100][scenario],189:2,198:scenario%2,211:mini,212:int(slot in [1,2,3,5,7,8,10,11]),218:17+team*12,228:61,233:1-mini,238:37,239:int(slot%2==0)}.items():word[i]=value
   for j,field in enumerate([56,49,50,52,68,163,135,132,147,171,183,246]):word[field]=[0,1,50,100][(slot+j)%4]
   word[123]=word[124]=word[125]=1
 initial_pool=sparse(pool);n.cpu.mem_write(game+0x84080,bytes(pool));seed=c.c_uint32(0x12345678);n.cpu.mem_write(0xc24d18,struct.pack('<I',seed.value))
 n.cpu.mem_write(game+0x38fb8c,bytes(48));n.cpu.mem_write(0xc249b8,bytes(8));allocated=heap+0x10000
 def allocate(size=None):
  global allocated
  if size is None:size=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)
  assert size<0x10000;out=allocated;allocated+=(size+15)//16*16;assert allocated<heap+0x400000;n.cpu.mem_write(out,bytes([0x6b])*size);return out
 def copy():
  target=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);source=n.cpu.reg_read(n.reg.UC_ARM64_REG_X1);size=n.cpu.reg_read(n.reg.UC_ARM64_REG_X2)
  if size:n.cpu.mem_write(target,bytes(n.cpu.mem_read(source,size)))
  return target
 def string(address):
  first=n.cpu.mem_read(address,1)[0]
  if first&1:return bytes(n.cpu.mem_read(pointer(address+16),pointer(address+8))).decode()
  return bytes(n.cpu.mem_read(address+1,first>>1)).decode()
 def to_string():
  address=n.cpu.reg_read(n.reg.UC_ARM64_REG_X8);value=str(i32(n.cpu.reg_read(n.reg.UC_ARM64_REG_X0))).encode();n.cpu.mem_write(address,bytes([len(value)<<1])+value+b'\0'+bytes(22-len(value)));return address
 def insert():
  address=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);prefix=n.cpu.reg_read(n.reg.UC_ARM64_REG_X2);value=bytearray()
  while n.cpu.mem_read(prefix+len(value),1)[0]:value+=n.cpu.mem_read(prefix+len(value),1)
  value+=string(address).encode();storage=allocate(len(value)+1);n.cpu.mem_write(storage,bytes(value)+b'\0');n.cpu.mem_write(address,struct.pack('<QQQ',1,len(value),storage));return address
 parameters={'battle_demon_summon_frame':rules.summon_frame,'battle_demon_summon_se_frame':rules.summon_sound_frame}
 for index in range(3):parameters['battle_explosion_width'+str(index+1)]=rules.explosion_widths[index];parameters['battle_explosion_damage'+str(index+1)]=rules.explosion_damage[index]
 for index in range(4):parameters['battle_explosion_frame'+str(index+1)]=rules.explosion_frames[index]
 def parameter():
  key=string(n.cpu.reg_read(n.reg.UC_ARM64_REG_X1));assert key in parameters,key;return parameters[key]
 def unit_mode():
  team=(n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)-game-0x2678)//0x1f0;assert team in [0,1];return environment.unit_modes[team]
 def sound():native_events.append({'kind':0,'value':n.cpu.reg_read(n.reg.UC_ARM64_REG_X1)});return 0
 def shake():native_events.append({'kind':1,'value':n.cpu.reg_read(n.reg.UC_ARM64_REG_X1)});return 0
 def mutation(team,target,read,write,random,put_random):
  if scenario%2:
   write(team,target,8,read(team,target,8)-1);put_random(advance(random))
  if scenario==2:write(team,2,1,14)
 def native_hit(team):
  raw=[n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i))) for i in range(8)];sp=n.cpu.reg_read(n.reg.UC_ARM64_REG_SP);raw+=list(struct.unpack('<11Q',n.cpu.mem_read(sp,88)))
  flags=[0]*12
  # boolのスタック引数はSTRB。上位byteの前回値をフラグに含めない。
  for index,param in [(0,7),(5,8),(1,9),(2,10),(3,11),(4,12),(6,13),(8,14),(7,15),(10,17)]:flags[index]=int(raw[param-1]&255!=0)
  if team:flags[9]=int(raw[15]&255!=0);flags[11]=int(raw[17]&255!=0)
  else:assert raw[15]&255==0
  event={'hit':{'side':team,'slot':raw[2],'target':raw[3],'hit':i32(raw[4]),'kind':raw[5],'parameter':0 if team else i32(raw[17]),'rate':i32(raw[18]),'flags':flags},'attack_type':raw[1]}
  native_hits.append(event);value=struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]
  mutation(1-team,raw[3],lambda t,s,w:integer(game+0x84080+t*0xc804+s*0x3ec+w*4),lambda t,s,w,v:n.cpu.mem_write(game+0x84080+t*0xc804+s*0x3ec+w*4,struct.pack('<i',i32(v))),value,lambda v:n.cpu.mem_write(0xc24d18,struct.pack('<I',v)))
  return applied
 @Sink
 def emit(user,actors,random,event,result):
  value=event.contents;cpp_hits.append({'hit':fields(value.hit),'attack_type':value.attack_type})
  mutation(1-value.hit.side,value.hit.target,lambda t,s,w:actors[t][s].words[w],lambda t,s,w,v:actors[t][s].words.__setitem__(w,i32(v)),random[0],lambda v:random.__setitem__(0,v));result[0]=applied;return 0
 n.helpers={0x81f580:game,0x5c2710:unit_mode,0x457e1c:0,0x459f04:sound,0x459efc:sound,0x5c1404:shake,0xbdaf40:allocate,0xbdaf60:0,0xbdb0b0:copy,0xbdb000:to_string,0xbdb010:insert,0x9019f4:parameter,0x44beb4:lambda:rules.summon_motion[(n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)-0x29d8)//0x38],0x59d12c:0,0x5d9598:0,0x6e4aec:lambda:native_hit(0),0x6e79bc:lambda:native_hit(1)}
 for offset in [0x340320,0x340338,0x340350]:n.cpu.mem_write(game+offset,bytes(24))
 handle=c.c_void_p();assert lib.kbcs_core_actor_areas_create(c.byref(handle))==0;initial=[]
 for index in range(2 if scenario==3 else 1):
  area=Area(surge_present=1,explosion_present=1);area.surge=Surge(side=side,slot=1,frame=[0,13,14,34][scenario]+index*20,x=10000,level=[0,1,2,3][scenario],hit=index,parameter=91,mini=mini,kind=kind)
  area.explosion=Explosion(side=side,slot=1,frame=index*9,x=10000,hit=index,parameter=92)
  area.surge.flags[:]=area.explosion.flags[:]=[int((j+scenario)%3==0) for j in range(12)]
  initial.append({'surge':fields(area.surge),'explosion':fields(area.explosion)});assert lib.kbcs_core_actor_areas_append(handle,c.byref(area))==0
  for offset,record,size,tree_offset in [(0x340320,area.surge,72,48),(0x340350,area.explosion,64,40)]:
   address=allocate(size);raw=bytes(record)+bytes(size-c.sizeof(record));n.cpu.mem_write(address,raw);n.cpu.mem_write(address+tree_offset,struct.pack('<Q',address+tree_offset+8))
   old=native_list(offset);data=allocate((len(old)+1)*8);n.cpu.mem_write(data,struct.pack('<'+'Q'*(len(old)+1),*old,address));n.cpu.mem_write(game+offset,struct.pack('<QQQ',data,data+(len(old)+1)*8,data+(len(old)+1)*8))
 checkpoints=[]
 for frame in range(frames):
  for phase,entry in enumerate([0x5d3af8,0x5d4158,0x5d4988]):
   native_events=[];native_hits=[];cpp_hits=[];n.entry=entry;n.ends[entry]=entry+sizes[entry];n.terminals={n.stop};n.cpu.mem_write(n.stack+0x5000,bytes(0x5000));n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,n.stack+0x9000);n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop);n.cpu.reg_write(n.reg.UC_ARM64_REG_X0,game)
   try:n.cpu.emu_start(entry,n.stop+4,count=2000000)
   except Exception as error:raise RuntimeError((case_count,frame,phase,hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)))) from error
   code=lib.kbcs_core_actor_areas_step(handle,phase,pool,c.byref(environment),c.byref(rules),c.byref(seed),emit,None);assert code==0,(case_count,frame,phase,code)
   expected_pool=Pool.from_buffer_copy(n.cpu.mem_read(game+0x84080,c.sizeof(pool)));expected_seed=struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]
   expected=snapshot(True,handle,expected_pool,expected_seed,native_events);actual=snapshot(False,handle,pool,seed.value,[])
   if expected!=actual or native_hits!=cpp_hits:
    details={'case':case_count,'side':side,'kind':kind,'mini':mini,'scenario':scenario,'mode':mode,'frame':frame,'phase':phase,'expected':expected,'actual':actual,'nativeHits':native_hits,'cppHits':cpp_hits}
    (ROOT/'research/.local/actor-secondary-diff.json').write_text(json.dumps(details,indent=2),encoding='utf-8-sig');raise AssertionError({k:v for k,v in details.items() if k not in ['expected','actual']})
   updates+=1;hit_count+=len(cpp_hits)
   if case_count%9==0 and (frame in [0,1,2,14,15,34,49,50,51,81,139] or frame==frames-1):
    # 個体全域の比較は毎phase実施。代表fixtureでは初期値からの差分だけを保存する。
    sample=dict(expected);after_pool=dict(sample.pop('pool'));before_pool=dict(initial_pool)
    sample['poolChanges']=[[i,after_pool.get(i,0)] for i in sorted(after_pool.keys()|before_pool.keys()) if after_pool.get(i,0)!=before_pool.get(i,0)]
    checkpoints.append({'frame':frame,'phase':phase,'state':sample,'hits':native_hits})
 lib.kbcs_core_actor_areas_destroy(handle)
 if checkpoints:records.append({'side':side,'kind':kind,'mini':mini,'scenario':scenario,'applied':applied,'frames':frames,'pool':initial_pool,'initial':initial,'rules':fields(rules),'checkpoints':checkpoints})
 case_count+=1
 if case_count%8==0:print(json.dumps({'cases':case_count,'phaseUpdates':updates,'hits':hit_count}),flush=True)
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'parameterSource':{'logicalPath':'Data/param.tsv',**assets.sources['Data/param.tsv']},'cases':case_count,'phaseUpdates':updates,'hits':hit_count,'records':records,'controlled':['singleton/unit modes','successful heap allocation/deletion/memcpy and string conversion/insert','param.tsv getter and reflection model lengths explicitly supplied','SE and shake captured','006e4aec/006e79bc ABI capture, applied return and optional HP/action/RNG mutation','tree cleanup frees omitted after removal; live tree search/insert/rebalance use original instructions'],'limits':['secondary state progression only; actual hit bodies and whole battle dispatch not executed','normalization of native pointer lists/history trees into typed records and target-indexed history','cancellation state writer and owner retirement guards are not part of these functions']}
(ROOT/'research/.local/actor-secondary-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-secondary-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
print(json.dumps({'secondaryCases':case_count,'phaseUpdates':updates,'hits':hit_count,'published':len(records)}))
