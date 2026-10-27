"""城HP閾値→次Fのボス出現・衝撃波・城破壊を原本の順に連続照合する。"""
import argparse,ctypes as c,itertools,json,os,sqlite3,struct,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path,required=True)
a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
from battle_abi import Rules,Result
class ContinuousNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.terminals or address in self.helpers:return super().hook(cpu,address,size,data)
  if any(start<=address<self.ends[start] for start in self.actual):return
  return super().hook(cpu,address,size,data)
n=ContinuousNative();g=0x40000000;n.cpu.mem_map(g,0x800000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 n.ends.update({int(address,16):int(address,16)+size for address,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")})
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
n.actual=[int(value,16) for value in manifest['functions'] if int(value,16) in n.ends]+[0x44a8d8,0x44a8e8,0x5bb5dc,0xa94bf0,0xa95100,0xa9518c,0xa95140,0xa9502c,0xa94678,0xa94484,0xa9b4c4,0xa94274,0xa9478c,0xa06c60,0xa06c80,0xa06ca0]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()))
class Actor(c.Structure):_fields_=[('words',c.c_int32*251)]
Pool=(Actor*51)*2
class Environment(c.Structure):
 _fields_=[('unit_modes',c.c_int32*2)]+[(k,c.c_int32) for k in ['stage_width','castle_slot','castle_x','castle_scale','castle_offset','stage_kind','zombie','chapter_rate','crown','hp_percent','attack_percent']]+[('crystal_max',c.c_int32*5),('crystal',c.c_int32*5),('treasures',c.c_int32*32),('combos',c.c_int32*32),('orb_stage',c.c_int32),('talents_disabled',c.c_int32),('part_curse',c.c_int32)]
class Context(c.Structure):_fields_=[(k,c.c_int32) for k in ['global_wait','kill_delta','active_enemies','max_enemies','castle_hp','castle_max_hp','castle_damage','damage_condition','paused','global_min','global_max']]
class State(c.Structure):_fields_=[(k,c.c_int32) for k in ['wait','spawned','kills']]
class Row(c.Structure):_fields_=[('cells',c.c_int32*14)]
class Health(c.Structure):_fields_=[(k,c.c_int32) for k in ['deployment_slot','cooldown','preserve_enemy_castle']]
class HealthResult(c.Structure):_fields_=[(k,c.c_int32) for k in ['previous_hp','delay_slot','delay_frames','delay_x','delay_y','sound']]
lib.kbcs_core_stage_tick.argtypes=[c.POINTER(Row),c.POINTER(State),c.c_int32,c.POINTER(Context),c.POINTER(c.c_int32)]
lib.kbcs_core_stage_commit.argtypes=[c.POINTER(Row),c.POINTER(State),c.c_int32,c.POINTER(Context),c.c_int32,c.c_int32,c.c_int32]
lib.kbcs_core_stage_castle_guard.argtypes=[c.POINTER(Row),c.POINTER(State),c.c_int32,c.POINTER(Context),c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_core_actor_boss.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.POINTER(c.c_int32),c.POINTER(c.c_int32)]
lib.kbcs_core_actor_health.argtypes=[c.POINTER(Actor*51),c.c_int32,c.c_int32,c.POINTER(Health),c.POINTER(c.c_uint32),c.POINTER(HealthResult)]
lib.kbcs_core_battle_result_step.argtypes=[c.POINTER(Rules),c.POINTER(Result),c.c_int32,c.c_int32,c.c_int32,c.POINTER(Actor*51),c.POINTER(c.c_uint32)]
sp=n.stack+0x8000
def pointer(address,value):n.cpu.mem_write(address,struct.pack('<Q',value))
def fragment(start,end,registers):
 n.entry=0x6d6d04;n.terminals={end}
 for i in range(31):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),0)
 for key,value in registers.items():n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+key),value)
 n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,sp);n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop)
 n.cpu.emu_start(start,n.stop+4,count=200000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==end
records=[]
for last_damage,immune in itertools.product([0,1],[0,1]):
 pool=Pool();pool[0][0].words[8]=100;pool[1][0].words[7]=pool[1][0].words[8]=100;pool[1][0].words[0]=2
 for key,value in {0:2,1:2,7:100,8:100,116:immune}.items():pool[0][1].words[key]=value
 row_values=[2,1,0,10,10,50,1,0,1,100,0,0,0,0];row=Row((c.c_int32*14)(*row_values));state=State(1,0,0);context=Context(0,0,0,50,100,100,0,0,0,3,7)
 env=Environment();env.unit_modes[0]=1;result=Result();seed=c.c_uint32(1572)
 for frame,damage in enumerate([100,last_damage],1):
  context.castle_hp=pool[1][0].words[8]
  scheduled=n.schedule({'rows':[row_values],'states':[[state.wait,state.spawned,state.kills]],'castleHp':context.castle_hp,'castlePresent':True,'globalWait':context.global_wait})
  candidate=c.c_int32();assert lib.kbcs_core_stage_tick(c.byref(row),c.byref(state),1,c.byref(context),c.byref(candidate))==0
  assert scheduled['spawnedRows']==([0] if candidate.value==0 else [])
  if candidate.value==0:
   assert lib.kbcs_core_stage_commit(c.byref(row),c.byref(state),1,c.byref(context),0,0,0)==0
   for key,value in {0:2,1:2,7:100,8:100,64:1}.items():pool[1][1].words[key]=value
  assert [state.wait,state.spawned,state.kills]==scheduled['states'][0] and context.global_wait==scheduled['globalWait']
  pool[1][0].words[19]=damage;n.cpu.mem_write(g+0x84080,bytes(pool))
  sounds=[]
  def sound():sounds.append(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1));return 0
  n.helpers={0x81f580:g,0x5c2710:0,0x44bf2c:32,0x457e1c:0,0x459efc:sound,0x5c1404:0}
  fragment(0x6d9334,0x6d9454,{'X27':g})
  sound_count=c.c_int32();shake=c.c_int32();assert lib.kbcs_core_actor_boss(pool,c.byref(env),32,c.byref(sound_count),c.byref(shake))==0
  assert bytes(pool)==bytes(n.cpu.mem_read(g+0x84080,c.sizeof(pool)))
  assert sounds==[45]*sound_count.value
  # 前回の試験で欠落していた、ボス出現前の致死攻撃をHP1へ止める入口。
  n.cpu.mem_write(g+0x39a228,bytes(1));pointer(sp+0x1e0,g+0x9ea98);pointer(sp+0x110,g+0x83e60)
  n.helpers={0x5bbbc8:0,0xa958b0:context.castle_hp,0xa9baf8:damage}
  fragment(0x6d9e44,0x6d9fc0,{'X9':g+0x9ea98,'X26':g+0x90890,'X27':g})
  preserve=c.c_int32();assert lib.kbcs_core_stage_castle_guard(c.byref(row),c.byref(state),1,c.byref(context),damage,c.byref(preserve))==0
  assert preserve.value==n.cpu.mem_read(g+0x39a228,1)[0]
  vector=n.memory+0x4000;storage=n.memory+0x6000;visual=n.memory+0x7000
  n.cpu.mem_write(vector,bytes(0x500));pointer(vector+0x398,storage);pointer(vector+0x3a0,storage+0x100)
  for offset,value in [(0x1f0,g+0x84080),(0x1d8,g+0x90884),(0x1e0,vector)]:pointer(sp+offset,value)
  n.cpu.mem_write(sp+0x1d0,bytes(4));n.cpu.mem_write(0xc24d18,bytes(seed));n.helpers={0x81f580:g,0x457e1c:0,0x459efc:sound,0xbdaf40:visual,0x5bc1dc:0,0x5c2d18:0}
  fragment(0x6da994,0x6dac68,{'X19':g+0x90884,'X27':g,'W26':1,'W28':0,'W24':0})
  output=HealthResult();health=Health(0,0,preserve.value);assert lib.kbcs_core_actor_health(pool,1,0,c.byref(health),c.byref(seed),c.byref(output))==0
  assert bytes(pool)==bytes(n.cpu.mem_read(g+0x84080,c.sizeof(pool)))
  pointer(sp+0x50,g+0x90890);pointer(sp+0x110,g+0x83e60);pointer(sp+0x60,g+0x83dfc);pointer(sp+0xb8,g+0x1000)
  judged=[]
  def victory():judged.append(1);return 0
  n.helpers={0x5bc058:0,0x5d996c:victory,0x5e02b0:2,0x5e144c:0,0xa958b0:100,0xa958f0:0}
  fragment(0x6db46c,0x6db4f8,{'X27':g})
  rules=Rules(total_limit=-1);assert lib.kbcs_core_battle_result_step(c.byref(rules),c.byref(result),1,frame,-1,pool,c.byref(seed))==0
  assert result.mode==(judged[0] if judged else 0)
  assert pool[0][1].words[1]==(7 if frame==2 and not immune else 2)
  assert seed.value==1572
  records.append({'frame':frame,'damage':damage,'immune':immune,'castleHp':pool[1][0].words[8],'allyAction':pool[0][1].words[1],'mode':result.mode,'spawned':state.spawned})
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(a.library.read_bytes()),'result':'equal','records':records,'actual':['006ef2b0','006d9334..006d9454','006d9e44..006d9fc0','006da994..006dac68','006db46c..006db4f8'],'controlled':['successful enemy constructor; resolved boss fields','first attack is lethal, follow-up damage 0/1 supplied before shockwave','victory handler captured; its actor writes independently covered in battle_result.py','stage interval random returns zero'],'limits':['sequential native fragments, not the complete appUpdate instruction stream']}
(ROOT/'research/.local/battle-one-frame-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig');print(json.dumps(report,ensure_ascii=False))
