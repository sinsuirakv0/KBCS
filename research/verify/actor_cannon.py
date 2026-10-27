"""にゃんこ砲の命中・発射・行動時計を15.7.2 ARM64へ局所照合する。"""
import argparse,ast,ctypes as c,itertools,json,os,re,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True);parser.add_argument('--library',type=Path,required=True)
args=parser.parse_args();sys.path.insert(0,str(args.python_libs))
from stages import Native,ROOT,SHA,digest
# 命中の既存FFI宣言を共用し、テスト実行部分は読み込まない。
classes={'Actor','Environment','Effects','HitContext','Clock','Damage','Events'}
tree=ast.parse((ROOT/'research/verify/actor_hit.py').read_text(encoding='utf-8-sig'))
exec(compile(ast.Module(body=[node for node in tree.body if isinstance(node,ast.ClassDef) and node.name in classes],type_ignores=[]),'actor_hit.py','exec'))
Actors=(Actor*51)*2
class Rules(c.Structure):_fields_=[('encoded',c.c_int32*4),('attack_rate',c.c_int32)]
class State(c.Structure):_fields_=[('segments',((c.c_int32*3)*15)*2)]
class CannonNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
  if any(a<=address<self.ends[a] for a in self.actual):return
  super().hook(cpu,address,size,data)
n=CannonNative();game=0x40000000;heap=0x50000000;n.cpu.mem_map(game,0x800000);n.cpu.mem_map(heap,0x100000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
actual=set(manifest['functions'])|{'00a93034','006eb464','005d8f58','00a94678','00a956f8','0044abe4','0044abfc','0044a8d8','0044a8e8'}
actual.update(re.findall(r'FUN_(00a9[0-9a-f]{4})', (n.cache/'code/005d8f58.c').read_text(encoding='utf-8')))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for address,size in db.execute('SELECT address,size FROM functions WHERE address NOT LIKE \'EXTERNAL:%\''):
  if address in actual:n.ends[int(address,16)]=int(address,16)+size
n.actual=[int(v,16) for v in actual if int(v,16) in n.ends]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_last_error.restype=c.c_int64
hit_args=[c.POINTER(State),c.POINTER(Actors),c.POINTER(Environment),c.POINTER(HitContext),c.POINTER(Clock),c.POINTER(Damage),c.POINTER(Rules),c.c_int32]
lib.kbcs_core_actor_cannon_hit.argtypes=hit_args+[c.c_int32,c.c_int32,c.POINTER(c.c_uint32),c.POINTER(Events)]
lib.kbcs_core_actor_cannon_step.argtypes=hit_args+[c.POINTER(c.c_uint32),c.POINTER(Events)]
lib.kbcs_core_actor_cannon_action.argtypes=[c.POINTER(State),c.POINTER(Actors),c.POINTER(Rules),c.c_int32]
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))
def put(offset,value):n.cpu.mem_write(game+offset,struct.pack('<i',value))
def string():n.cpu.mem_write(reg(8),bytes(24));return 0
def allocate():
 global next_heap
 value=next_heap;next_heap+=(reg(0)+15)&~15;n.cpu.mem_write(value,bytes(reg(0)));return value
def random():
 global native_seed
 bound=reg(0)&0xffffffff;native_seed^=(native_seed<<13)&0xffffffff;native_seed^=native_seed>>17;native_seed^=(native_seed<<15)&0xffffffff;native_seed&=0xffffffff;return native_seed%bound
def reset(actors,state):
 global next_heap,native_seed
 n.cpu.mem_write(game,bytes(0x800000));n.cpu.mem_write(game+0x84080,bytes(actors));n.cpu.mem_write(game+0x9d788,bytes(state));next_heap=heap;native_seed=0x12345678
 n.cpu.mem_write(0xc1b578,struct.pack('<Q',0xc24400))
 n.helpers={0x81f580:game,0x5c2710:lambda:1 if reg(0)==game+0x2678 else 0,0x5bbc10:-1,0x5bbbc8:0,0x5bc058:0,
  0x59f80c:0,0x457e1c:0,0x459efc:0,0x459bb4:0,0x44beb4:lambda:rules.encoded[{0x2d38:0,0x2d70:1,0x2da8:2,0x30d8:3}[reg(0)-game if reg(0)>=game else reg(0)]],
  0x44a8d8:random,0x419064:0,0xbdaf40:allocate,0xbdaf60:0,0xbdb160:string,0xa94074:string,0x41b298:lambda:n.cpu.mem_write(reg(0),bytes(24)) or 0,0x5d75d4:heap,
  0x7cf950:0,0x644304:0,0xa5b1b4:0,0xa5b084:0,0x88f9e4:0,0x5bc198:1,0x9d49e4:1,0xa960ac:1,0x9d4e1c:0,0x9019f4:0,0x63c178:0,0x63c480:0,0x68c330:0,0x8cfcf0:0,0x63a050:0}
 for field,offset in [(0x9ee48,20000)]:put(field,offset)
 def notify():return 0
 n.helpers[0x9d4e1c]=notify

def compare(actors,state,label):
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(actors)))
 if bytes(actors)!=expected:
  a=struct.unpack('<25602i',bytes(actors));b=struct.unpack('<25602i',expected);diff=[(i//12801,(i%12801)//251,i%251,x,y) for i,(x,y) in enumerate(zip(a,b)) if x!=y];raise AssertionError((label,diff[:8]))
 assert bytes(state)==bytes(n.cpu.mem_read(game+0x9d788,c.sizeof(state))),(label,'segments')
rules=Rules((c.c_int32*4)(27,31,22,13),100);env=Environment();env.unit_modes[:]=[1,0];env.stage_width=20000;env.castle_slot=-1
context=HitContext();context.effects.target_count=1;context.effects.scenario_level=1
clock=Clock();damage=Damage();hits=0
for kind,condition,action in itertools.product(range(8),['plain','metal','zombie','dodge','wave-ignore','wave-stop','barrier','effects','curse'],[0,12,14]):
 actors=Actors();state=State();events=Events();castle=actors[0][0].words;target=actors[1][1].words
 for k,v in {0:1,3:16800,4:4400,6:12,7:236000,8:236000,13:7,17:kind,20:4550,21:1000,22:1,27:250,28:1,30:150,31:200}.items():castle[k]=v
 for k,v in {0:2,1:action,3:7000,4:4400,7:10001,8:5001,22:0,126:-1,168:59}.items():target[k]=v
 if condition=='metal':target[43]=1
 if condition=='zombie':target[46]=1
 if condition=='dodge':target[165]=100
 if condition=='wave-ignore':target[85]=1;castle[5]=1
 if condition=='wave-stop':target[86]=1;castle[5]=1
 if condition=='barrier':target[117]=10001
 if condition=='effects':castle[61]=100;castle[62]=30;castle[64]=100;castle[65]=31;castle[78]=100;castle[79]=32
 if condition=='curse':target[153]=39
 reset(actors,state);n.call(0x5d6c3c,game,0,1,7)
 seed=c.c_uint32(0x12345678)
 code=lib.kbcs_core_actor_cannon_hit(c.byref(state),c.byref(actors),c.byref(env),c.byref(context),c.byref(clock),c.byref(damage),c.byref(rules),0,1,7,c.byref(seed),c.byref(events))
 assert code==0,('hit error',kind,condition,action,code,hex(lib.kbcs_core_actor_last_error()))
 compare(actors,state,('hit',kind,condition,action));assert seed.value==native_seed,('RNG',kind,condition,action,seed.value,native_seed);hits+=1
steps=0
for kind,side,remaining in itertools.product([0,5],[0,1],[4,5,8,9,13,31]):
 actors=Actors();state=State();events=Events();castle=actors[side][0].words
 for k,v in {0:1,3:16800 if not side else 3200,4:4400,6:12,7:236000,8:236000,13:7,17:kind,20:4550}.items():castle[k]=v
 for slot in [1,2,3]:
  target=actors[1-side][slot].words
  for k,v in {0:2+slot,3:7000+slot*1000,4:4400,7:10001,8:5001,126:-1,168:59}.items():target[k]=v
 state.segments[side][0][:]=[remaining,20000 if not side else 0,7]
 reset(actors,state);n.call(0x5d6740,game,side)
 seed=c.c_uint32(0x12345678)
 code=lib.kbcs_core_actor_cannon_step(c.byref(state),c.byref(actors),c.byref(env),c.byref(context),c.byref(clock),c.byref(damage),c.byref(rules),side,c.byref(seed),c.byref(events));assert code==0,('step error',kind,side,remaining,hex(lib.kbcs_core_actor_last_error()))
 compare(actors,state,('step',kind,side,remaining));assert seed.value==native_seed;steps+=1
updates=0
for side,pair,frame,pool_full in itertools.product([0,1],[(kind,action) for kind,actions in enumerate([[0,1,2],[3],[6],[4,5],[7,8],[9,10],[11],[12]]) for action in actions],[0,3,4,5,10,16,17,22,27,31,32,33,48],[0,1]):
 kind,action=pair
 actors=Actors();state=State();w=actors[side][0].words
 for k,v in {0:1,3:16800 if side==0 else 3200,4:4400,6:12,7:236000,8:236000,9:action,10:frame,13:7,17:kind}.items():w[k]=v
 if pool_full:
  for segment in state.segments[side]:segment[0]=20
 reset(actors,state);n.call(0x6eb464,game,0,side)
 code=lib.kbcs_core_actor_cannon_action(c.byref(state),c.byref(actors),c.byref(rules),side);assert code==0
 compare(actors,state,('action',side,kind,action,frame,pool_full));updates+=1
class Spawn(c.Structure):_fields_=[(k,c.c_int32) for k in ['side','raw','level_index','layer_min','layer_max','form','row']]
class Fire(c.Structure):_fields_=[(k,c.c_int32) for k in ['fired','slot','sound']]
Constructor=c.CFUNCTYPE(c.c_int32,c.c_void_p,c.POINTER(Spawn),c.POINTER(c.c_uint32))
lib.kbcs_core_actor_cannon_fire.argtypes=[c.POINTER(Actors),c.POINTER(Environment),c.POINTER(Spawn),c.POINTER(c.c_uint32),Constructor,c.c_void_p,c.POINTER(Fire)]
fire_cases=0
for kind,remaining,action,available,raw in itertools.product(range(8),[0,1],[0,1],[0,1],[2,341]):
 actors=Actors();state=State();castle=actors[0][0].words
 for k,v in {0:1,3:16800,4:4400,7:236000,8:236000,9:action,11:1500,12:remaining,13:7,17:kind,21:362,22:180,26:339,27:20}.items():castle[k]=v
 for side in [0,1]:
  for slot in range(1,3):
   for k,v in {0:raw,1:0,3:5000+slot*1000,7:100,8:100}.items():actors[side][slot].words[k]=v
 reset(actors,state);sounds=[]
 def create_native():
  global native_seed
  if not available:return 0xffffffff
  n.cpu.mem_write(game+0x84080+3*0x3ec,struct.pack('<251i',*([341]+[0]*6+[100,100]+[0]*242)))
  random_bound=1;native_seed^=(native_seed<<13)&0xffffffff;native_seed^=native_seed>>17;native_seed^=(native_seed<<15)&0xffffffff;native_seed&=0xffffffff;return 3
 n.helpers.update({0x5bc280:341,0x5bce08:339,0xacf9cc:0,0x5bce20:0,0x9f1e64:create_native,0x459efc:lambda:sounds.append(reg(1)) or 0})
 native_args=[]
 # 原本はrawのレイヤー列を読み、同じ順に構築callbackへ渡す。
 put(0x9ee88+341*0x770+0x38,2);put(0x9ee88+341*0x770+0x3c,3)
 n.call(0x5d8f58,game,1)
 seed=c.c_uint32(0x12345678);iron=Spawn(0,341,0,2,3,0,0);out=Fire()
 @Constructor
 def create_cpp(user,request,random_state):
  if not available:return -1
  assert bytes(request.contents)==bytes(iron)
  w=actors[0][3].words;w[0]=341;w[7]=w[8]=100
  v=random_state[0];v^=(v<<13)&0xffffffff;v^=v>>17;v^=(v<<15)&0xffffffff;random_state[0]=v&0xffffffff;return 3
 code=lib.kbcs_core_actor_cannon_fire(c.byref(actors),c.byref(env),c.byref(iron),c.byref(seed),create_cpp,None,c.byref(out));assert code==0
 compare(actors,state,('fire',kind,remaining,action,available,raw));assert seed.value==native_seed
 assert bool(out.fired)==(19 in sounds);assert out.sound in sounds if out.sound>=0 else True
 fire_cases+=1
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(args.library.read_bytes()),'hitCases':hits,'actionCases':updates,'fireCases':fire_cases,'contactSteps':steps,'limits':['制御されたステージ補正/モデル長/表示用文字列とコンテナ','所有戦闘の全フレーム/音声/GPU画素の一致ではない']}
(ROOT/'research/.local/actor-cannon-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig');print(json.dumps(report))
