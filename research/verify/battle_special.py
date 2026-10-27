"""追加生産・条件付き本能玉・イベントPt/フィーバーを同版ARM64へ照合する。"""
import argparse,ctypes as c,itertools,json,os,random,sqlite3,struct,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path,required=True)
a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
from battle_abi import Rules,Result,PointRules
class SpecialNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
  if any(start<=address<self.ends[start] for start in self.actual):return
  super().hook(cpu,address,size,data)
n=SpecialNative();g=0x40000000;n.cpu.mem_map(g,0x500000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for start in [0x6d6d04,0x9f4a74,0xaa0568,0x5c2f88,0xa0cfec,0xa0cdf4,0xa0d874,0xa0cdbc,0xa0d078,0xa0cde0,0x88f9e4,0x9e4e14,0x645288,0x645444,0x64556c]:
  n.ends[start]=start+db.execute('SELECT size FROM functions WHERE address=?',(f'{start:08x}',)).fetchone()[0]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()))
assert lib.kbcs_core_abi_version()==4,"ABI4のライブラリが必要"
class Spawn(c.Structure):_fields_=[(k,c.c_int32) for k in ['side','raw','level_index','layer_min','layer_max','form','row']]
class Production(c.Structure):_fields_=[('money',c.c_int32)]+[(k,c.c_int32*10) for k in ['wait','maximum','produced','last_cost']]+[('total',c.c_int32)]
class Extra(c.Structure):_fields_=[('slot',c.c_int32),('wait',c.c_int32)]
class Points(c.Structure):_fields_=[(k,c.c_int32) for k in ['score','origin','wait','frame','phase','ending','gauge']]
class PointInput(c.Structure):_fields_=[('event',c.c_int32),('count',c.c_int32),('values',c.c_int32*2),('timer',c.c_int32),('limit',c.c_int32)]
Constructor=c.CFUNCTYPE(c.c_int32,c.c_void_p,c.POINTER(Spawn),c.POINTER(c.c_uint32))
lib.kbcs_core_production_condition.argtypes=[c.c_int32,c.c_int32,c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_core_production_extra_plan.argtypes=[c.POINTER(c.c_int32),c.c_int32,c.c_int32,c.POINTER(Extra),c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_core_production_extra_tick.argtypes=[c.POINTER(Extra),c.POINTER(c.c_int32),c.POINTER(Production),c.POINTER(Spawn),c.POINTER(c.c_uint32),Constructor,c.c_void_p]
lib.kbcs_core_battle_point_add.argtypes=[c.POINTER(PointRules),c.POINTER(Points),c.POINTER(PointInput)]
lib.kbcs_core_battle_point_fever.argtypes=[c.POINTER(PointRules),c.POINTER(Points),c.POINTER(c.c_int32)]
lib.kbcs_core_battle_point_display.argtypes=[c.POINTER(PointRules),c.POINTER(Points)]
lib.kbcs_core_battle_point_render.argtypes=[c.POINTER(PointRules),c.POINTER(Points)]
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))&0xffffffff
def signed(v):return c.c_int32(v).value
def put(address,value):n.cpu.mem_write(address,struct.pack('<i',value))
def pointer(address,value):n.cpu.mem_write(address,struct.pack('<Q',value))
def get(address):return struct.unpack('<i',n.cpu.mem_read(address,4))[0]
sp=n.stack+0x8000
def fragment(function,start,end,registers):
 n.entry=function;n.terminals={end};n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,sp)
 for i in range(31):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),0)
 for i,value in registers.items():n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),value&0xffffffffffffffff)
 n.cpu.emu_start(start,n.stop+4,count=200000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==end
counts={};cases=list(itertools.product([-1,0,1,2,7,2147483647],[0,1],[0,1,2,3]))
for produced,kind,period in cases:
 n.actual=[];n.cpu.mem_write(sp-0x100,bytes(0x300));put(g+0x108,produced);n.helpers={0x81f580:g,0x9019f4:period}
 fragment(0x5c2f88,0x5c307c,0x5c3168,{22:g,21:0,23:kind,25:0,29:sp+0x100})
 expected=reg(20);out=c.c_int32(-1);assert lib.kbcs_core_production_condition(produced,kind,period,c.byref(out))==0
 assert out.value==expected,(produced,kind,period,out.value,expected)
counts['production_condition']=len(cases)
# 通常生産の実入口でルール8を読み、予約追加と通常費用/生産数の継続を確認。
queue=n.memory+0x4000;rule_node=n.memory+0x6000;rule_values=n.memory+0x6100
for mask,rarity,amount,interval in itertools.product([2,16,63],[0,1,4,5],[0,1,2],[0,1,60]):
 n.cpu.mem_write(g,bytes(0x400000));pointer(g+0x2768,queue);pointer(g+0x2770,queue);pointer(g+0x2778,queue+128)
 rule=(c.c_int32*3)(mask,amount,interval);pointer(rule_node,rule_values);pointer(rule_node+8,rule_values+12);n.cpu.mem_write(rule_values,bytes(rule))
 economy=g+0x2678;slot=2;money=[100000];n.actual=[];n.terminals=set()
 def deduct():money[0]+=signed(reg(1));return 0
 n.helpers={0x5bc910:1,0x5bcdec:1,0x5be130:7500,0x5bf81c:0,0x5c2d18:0,0x5c2720:lambda:money[0],0x9e583c:0,
  0x5bbbf0:2,0x6505d0:1,0xacf894:29,0xacf804:7,0x44abfc:lambda:min(reg(0),reg(1)),0x44abe4:lambda:max(signed(reg(0)),signed(reg(1))),
  0x8cfcf0:0,0x5bce08:40,0x5bc280:42,0x5bce20:2,0x9f1e64:1,0x7cf950:0,
  0x644304:lambda:rule_node if reg(2)==8 else 0,0x63e4a8:rarity,0x47c518:0,0xa9e594:0,0xa0b03c:0,0xaa3f20:-1,
  0x5c2990:deduct,0x58c05c:181,0x5c2f88:0,0x5c2d60:0,0x457e1c:0,0x459efc:0,0xa60594:0}
 n.call(0x9f4a74,g,0,slot,1)
 length=(struct.unpack('<Q',n.cpu.mem_read(g+0x2770,8))[0]-queue)//8
 out=(Extra*4)();size=c.c_int32(-1)
 assert lib.kbcs_core_production_extra_plan(rule,rarity,slot,out,4,c.byref(size))==0
 assert size.value==length and bytes(out)[:length*8]==bytes(n.cpu.mem_read(queue,length*8)),(mask,rarity,amount,interval)
 assert get(economy+0x108+slot*4)==1 and money[0]==92500,(mask,rarity,amount,interval,money[0])
counts['extra_plan']=216
# 実生成は捕捉し、生産数を1減らして呼ぶ時点・後ろからの順序・失敗時消費を検証。
rng=random.Random(157208);queue=n.memory+0x4000
for case in range(80):
 n.cpu.mem_write(g,bytes(0xa0000));records=[Extra(rng.randrange(10),rng.choice([-1,0,0,1,2,60])) for _ in range(case%12)]
 production=Production(money=123456,total=29);production.produced[:]=[rng.randrange(1,100) for _ in range(10)]
 native_calls=[];calls=[];slots=(Spawn*10)(*[Spawn(0,slot+2,36,1,4,2,0) for slot in range(10)])
 pointer(g+0x2768,queue);pointer(g+0x2770,queue+len(records)*8);pointer(g+0x2778,queue+128)
 n.cpu.mem_write(queue,b''.join(bytes(x) for x in records));n.cpu.mem_write(g+0x2780,bytes(production.produced))
 for off,value in [(0x1b0,g),(0xa8,g+0x47ba4),(0xa0,g+0x2780),(0x98,g+0x9ee88)]:pointer(sp+off,value)
 for slot in range(10):
  put(g+0x9ee88+(slot+2)*0x770+2*0x1dc+0x38,1);put(g+0x9ee88+(slot+2)*0x770+2*0x1dc+0x3c,4)
 def create():
  native_calls.append(([reg(i) for i in range(1,8)],get(g+0x2780+(reg(2)-2)*4)));return -1 if case%3==0 else 1
 def move():n.cpu.mem_write(n.cpu.reg_read(n.reg.UC_ARM64_REG_X0),bytes(n.cpu.mem_read(n.cpu.reg_read(n.reg.UC_ARM64_REG_X1),reg(2))));return n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)
 n.actual=[];n.helpers={0x5bce08:lambda:reg(1),0xacf9cc:36,0x5bc280:lambda:reg(1)+2,0x5bce20:2,0x9f1e64:create,0xbdaff0:move}
 fragment(0x6d6d04,0x6d7c38,0x6d7dc4,{27:g})
 length=(struct.unpack('<Q',n.cpu.mem_read(g+0x2770,8))[0]-queue)//8
 expected=bytes(n.cpu.mem_read(queue,length*8));array=(Extra*max(1,len(records)))(*records);size=c.c_int32(len(records));seed=c.c_uint32(1)
 @Constructor
 def construct(user,request,random):
  v=request.contents;calls.append(([getattr(v,k) for k,_ in Spawn._fields_],production.produced[v.raw-2]));return -1 if case%3==0 else 1
 assert lib.kbcs_core_production_extra_tick(array,c.byref(size),c.byref(production),slots,c.byref(seed),construct,None)==0
 assert size.value==length and bytes(array)[:length*8]==expected and calls==native_calls,(case,calls,native_calls)
 assert bytes(production.produced)==bytes(n.cpu.mem_read(g+0x2780,40)) and production.total==29 and production.money==123456
counts['extra_queue']=80
# 00aa0568を全入口から実行。固定価格の早期returnと修飾ごとの整数化。
class Cost(c.Structure):_fields_=[(k,c.c_int32) for k in ['enabled','raw','talent','chapter','multiplier','fixed','rarity_rate','orb_rate','orb_enabled','combo_count']]+[('combos',c.c_int32*32)]
lib.kbcs_core_production_cost.argtypes=[c.POINTER(Cost),c.POINTER(c.c_int32)]
fixed_node=n.memory+0x6000;rarity_node=n.memory+0x6020;fixed_values=n.memory+0x6100;rarity_values=n.memory+0x6140;combo_values=n.memory+0x6200
pointer(fixed_node,fixed_values);pointer(fixed_node+8,fixed_values+4);pointer(rarity_node,rarity_values);pointer(rarity_node+8,rarity_values+24)
price_cases=list(itertools.product([7500,91100,123450],[0,100],[0,1,2],[0,133],[-1,321],[50,100,133],[-1,0,20],[[],[20],[5,10]]))
for raw,talent,chapter,multiplier,fixed,rarity,orb,combos in price_cases:
 put(g+0x9fd80+2*0x770+2*0x1dc,raw);put(g+0x38fad8,chapter);put(fixed_values,fixed)
 n.cpu.mem_write(rarity_values,struct.pack('<6i',*[rarity]*6));n.cpu.mem_write(combo_values,struct.pack('<'+'i'*len(combos),*combos))
 def combo_vector():
  dest=n.cpu.reg_read(n.reg.UC_ARM64_REG_X8);pointer(dest,combo_values);pointer(dest+8,combo_values+4*len(combos));pointer(dest+16,combo_values+128);return 0
 n.actual=[];n.terminals=set();n.helpers={0x81f580:g,0x7cf950:0,0x644304:lambda:fixed_node if reg(2)==4 and fixed>=0 else rarity_node if reg(2)==5 else 0,
  0x5c2710:1,0xa9f0e0:talent,0x44abe4:lambda:max(signed(reg(0)),signed(reg(1))),0x7cf370:multiplier,
  0x5c2f30:int(orb>=0),0x66398c:max(0,orb),0x88faec:combo_vector,0xbdaf60:0,0x63e4a8:2}
 expected=n.call(0xaa0568,2,2,1,2)
 value=Cost(enabled=1,raw=raw,talent=talent,chapter=chapter,multiplier=multiplier,fixed=fixed,rarity_rate=rarity,orb_rate=max(0,orb),orb_enabled=int(orb>=0),combo_count=len(combos))
 value.combos[:len(combos)]=combos;out=c.c_int32(-1)
 assert lib.kbcs_core_production_cost(c.byref(value),c.byref(out))==0
 assert out.value==expected,(raw,talent,chapter,multiplier,fixed,rarity,orb,combos,out.value,expected)
counts['production_cost']=len(price_cases)
# 原本のPtテーブルは右だけの正しい探索木を用意し、実getterの端点も通す。
rules=PointRules(rate=7,tier_count=5,fever_count=10);tiers=[(2000,15),(4500,17),(5500,25),(7000,30),(10000,0)]
for i,value in enumerate(tiers):rules.tiers[i][:]=value
rules.fever[:]=[0,25000,600,6,0,0,0,0,0,0]
stage=n.memory+0x1000;rate=n.memory+0x2000;heap=n.memory+0x3000
pointer(stage+0x68,rate);put(stage,0);put(rate+8,7);pointer(rate+0x10,rate+0x100);pointer(rate+0x18,rate+0x100)
for i,(threshold,value) in enumerate(tiers):
 node=rate+0x100+i*0x40;n.cpu.mem_write(node,bytes(64));pointer(node+8,node+0x40 if i<4 else 0);pointer(node+16,node-0x40 if i else rate+0x18);put(node+28,threshold);put(node+32,value)
def memcpy():n.cpu.mem_write(n.cpu.reg_read(n.reg.UC_ARM64_REG_X0),bytes(n.cpu.mem_read(n.cpu.reg_read(n.reg.UC_ARM64_REG_X1),reg(2))));return n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)
point_cases=[]
for event,count,values in [(0,1,[v,0]) for v in [0,1,1999,2000,2001,4500,4501,5500,5501,7000,7001,10000,10001]]+[(1,2,[12345,917]),(1,2,[0,0]),(1,2,[2147483647,1]),(0,2,[100,5])]:
 for timer,limit in [(0,5400),(5399,5400),(5400,5400),(5401,5400),(0,-1),(0,0)]:
  for score in [0,999999998]:point_cases.append((event,count,values,timer,limit,score))
for event,count,values,timer,limit,score in point_cases:
 state=Points(score=score);input=PointInput(event,count,(c.c_int32*2)(*values),timer,limit)
 n.actual=[0xa0cdf4,0xa0d874];put(g+0x80,timer);put(g+0x84,limit);put(g+0x88,score)
 n.cpu.mem_write(n.memory+0x5000,bytes(input.values));n.helpers={0xa0e40c:stage,0xa0e088:0,0xa0e194:rate,0xa0d86c:7,0xbdaf40:heap,0xbdaf60:0,0xbdb0b0:memcpy};n.terminals=set()
 n.call(0xa0cfec,g,event,0,n.memory+0x5000,count)
 assert lib.kbcs_core_battle_point_add(c.byref(rules),c.byref(state),c.byref(input))==0
 assert state.score==get(g+0x88),(event,values,timer,limit,score,state.score,get(g+0x88))
counts['point_add']=len(point_cases)
node=n.memory+0x6000;values=n.memory+0x6100;pointer(node,values);pointer(node+8,values+40);n.cpu.mem_write(values,bytes(rules.fever));offsets=[0x68,0x6c,0x70,0x74,0x78,0x7c]
for case in range(80):
 state=Points(score=rng.choice([0,24999,25000,25001,51000,2147473647,-2147473648]),origin=rng.choice([0,10000,2147473647,-2147473648]),wait=rng.choice([0,1,2,5,6,599,600]),frame=3,phase=0,ending=case%2,gauge=rng.choice([-1,0,100,294,2147483647,-2147483648]))
 for step in range(10):
  expected_fields=[state.origin,state.wait,state.frame,state.phase,state.ending,state.gauge]
  for off,value in zip(offsets,expected_fields):put(g+off,value)
  events=[];n.actual=[];n.helpers={0x7cf950:0,0x644304:node,0x6453ac:lambda:events.append('refresh') or 0,0x457e1c:0,0x459efc:lambda:events.append(reg(1)) or 0};n.terminals=set()
  n.call(0x645288,g,state.score);changed=c.c_int32(9)
  assert lib.kbcs_core_battle_point_fever(c.byref(rules),c.byref(state),c.byref(changed))==0
  assert [state.origin,state.wait,state.frame,state.phase,state.ending,state.gauge]==[get(g+off) for off in offsets],(case,step,'fever')
  assert bool(changed.value)==('refresh' in events) and (changed.value==1)==(194 in events)
  n.helpers={0x7cf950:0,0x644304:node,0x81f580:g,0x821cb4:300};n.call(0x645444,g)
  assert lib.kbcs_core_battle_point_display(c.byref(rules),c.byref(state))==0
  assert [state.origin,state.wait,state.frame,state.phase,state.ending,state.gauge]==[get(g+off) for off in offsets],(case,step,'display')
  n.call(0x64556c,g,state.score);assert lib.kbcs_core_battle_point_render(c.byref(rules),c.byref(state))==0
  assert state.gauge==get(g+0x7c),(case,step,'render')
  state.score+=rng.randrange(1000)
counts['fever_updates']=800
# PRの実時計/終了分岐。結果保存は捕捉し、期限前後と経過Fを比較する。
Actors=((c.c_int32*251)*51)*2
lib.kbcs_core_battle_result_step.argtypes=[c.POINTER(Rules),c.POINTER(Result),c.c_int32,c.c_int32,c.c_int32,c.POINTER(Actors),c.POINTER(c.c_uint32)]
ctx=g+0x1000;cases=list(itertools.product([0,1,7],[0,5398,5399,5400],[-1,5400],[0,29999,30000]))
for mode,timer,limit,elapsed in cases:
 put(ctx+0x80,timer);put(ctx+0x84,limit);put(g+0x83e74,elapsed);pointer(g+0x7e8,ctx)
 actual_mode=[mode];n.actual=[0xa0cdbc,0xa0d078,0xa0cde0]
 def victory():actual_mode[0]=1;return 0
 n.helpers={0x5bc058:lambda:actual_mode[0],0xa0b03c:1,0x5d996c:victory,0x5e144c:0}
 pointer(sp+0x60,g+0x83dfc);pointer(sp+0xb8,g+0x2000)
 # fragmentの引数は開始/終了。期限判定から経過時計の入口までを通す。
 fragment(0x6d6d04,0x6d7e6c,0x6d81a8,{27:g})
 pointer(sp+0x58,g+0x3000);pointer(sp+0x60,g+0x83dfc)
 fragment(0x6d6d04,0x6d81a8,0x6d81f8,{27:g})
 state=Result(mode,timer,elapsed);pool=Actors();seed=c.c_uint32(1);rules=Rules(native_kind=-26,score_type=3,time_limit=limit,total_limit=-1)
 assert lib.kbcs_core_battle_result_step(c.byref(rules),c.byref(state),0,17,-1,c.byref(pool),c.byref(seed))==0
 assert (state.mode,state.timer,state.elapsed)==(actual_mode[0],get(ctx+0x80),get(g+0x83e74)),(mode,timer,limit,elapsed,state.mode,state.timer,state.elapsed)
counts['point_clock']=len(cases)
# 008900xxのgroup列と同じ解決済みレコードを作り、実getterの対象内/外を保存。
combo_context=n.memory+0x1000;records=n.memory+0x2000;effects=n.memory+0x3000;group=g+0x343270;group_node=n.memory+0x7000;members=n.memory+0x7100
units=[831,832,833,834,835,836,857,858];kinds=[(25,2500),(11,50),(26,1),(27,20),(2,30)]
pointer(group+0x20,group_node);n.cpu.mem_write(group_node,bytes(0x60));put(group_node+0x20,10);put(group_node+0x58,3)
pointer(group_node+0x28,members);pointer(group_node+0x30,members+len(units)*4);n.cpu.mem_write(members,struct.pack('<8i',*units))
pointer(combo_context,records);pointer(combo_context+8,records+len(kinds)*16);pointer(combo_context+0x1b8,effects)
for i,(kind,value) in enumerate(kinds):
 obj=n.memory+0x4000+i*0x80;values=n.memory+0x5000+kind*8;pointer(records+i*16,obj);pointer(records+i*16+8,0);n.cpu.mem_write(obj,bytes(0x80))
 put(obj+0x10,10);put(obj+0x18,kind);put(obj+0x24,0);put(obj+0x30,1);n.cpu.mem_write(obj+0x65,b'\x01');pointer(effects+kind*24,values);put(values,value)
def find_member():
 address=n.cpu.reg_read(n.reg.UC_ARM64_REG_X0);target=reg(1)
 for i in range(reg(2)):
  if get(address+i*4)==target:return address+i*4
 return 0
n.actual=[0x9e4e14];n.helpers={0x81f580:g,0xbdb500:find_member};n.terminals=set();targeted=[]
for unit in units+[94]:
 values=[0]*32
 for kind,value in kinds:values[kind]=n.call(0x88f9e4,combo_context,kind,unit)
 targeted.append({'unit_id':unit,'values':values})
assert not any(targeted[-1]['values'])
(ROOT/'research/.local/battle-special-combo-oracle.json').write_text(json.dumps(targeted),encoding='utf-8-sig')
counts['native_target_getters']=len(targeted)*len(kinds)
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(a.library.read_bytes()),'cases':counts,'result':'equal','controlled':['profile/constructor/level getters and preallocated queue','PointStageSettings lookup and vector allocation','Fever rule lookup/audio/velocity refresh'],'actual':['00aa0568 full price branch/rounding; modifier getters controlled','0088f9e4/009e4e14 group lookup; records controlled','006d7e6c PR timer/controller branch; result handler controlled','005c307c condition arithmetic','006d7c38 reverse queue and produced restoration','00a0cfec/cdf4 point rounding and 00a0d874 tier lookup','00645288 fever gauge/start/end and 00645444 display phase']}
(ROOT/'research/.local/battle-special-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig');print(json.dumps(report,ensure_ascii=False))
