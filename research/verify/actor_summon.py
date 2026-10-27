"""009f4a74の精霊入口を制御した個体構築でC++と比較する。全戦闘の照合ではない。"""
import argparse,ctypes as c,itertools,json,os,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--library',type=Path,required=True)
args=parser.parse_args();sys.path.insert(0,str(args.python_libs))
from stages import Native,ROOT,SHA,digest
class SummonNative(Native):
 def hook(self,cpu,address,size,data):
  if any(a<=address<self.ends[a] for a in self.actual):return
  super().hook(cpu,address,size,data)
n=SummonNative();g=0x40000000;n.cpu.mem_map(g,0x500000)
setters=['00a991a0','00a9486c','00a95338','00a95ebc','00a9b7d0','00a9b85c','00a9b50c','00a94274']
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for a,size in db.execute('SELECT address,size FROM functions WHERE address IN ('+','.join('?' for _ in setters+['009f4a74'])+')',setters+['009f4a74']):n.ends[int(a,16)]=int(a,16)+size
n.actual=[int(a,16) for a in setters]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()))
class Spawn(c.Structure):_fields_=[(k,c.c_int32) for k in ['side','raw','level_index','layer_min','layer_max','form','row']]
class State(c.Structure):_fields_=[(k,c.c_int32*10) for k in ['active','wait','used']]
class Input(c.Structure):_fields_=[('child',Spawn),('slot',c.c_int32),('parent_raw',c.c_int32),('position',c.c_int32)]
class Output(c.Structure):_fields_=[(k,c.c_int32) for k in ['count','last_slot','sound','failure_sound','completion_sound']]
Actors=((c.c_int32*251)*51)*2
Constructor=c.CFUNCTYPE(c.c_int32,c.c_void_p,c.POINTER(Spawn),c.POINTER(c.c_uint32))
lib.kbcs_core_actor_summon.argtypes=[c.POINTER(Input),c.POINTER(State),c.POINTER(Actors),c.c_void_p,c.POINTER(c.c_uint32),Constructor,c.c_void_p,c.POINTER(Output)]
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))&0xffffffff
def write(offset,value):n.cpu.mem_write(g+offset,struct.pack('<i',value))
def random(seed):
 seed^=(seed<<13)&0xffffffff;seed^=seed>>17;seed^=(seed<<15)&0xffffffff;return seed&0xffffffff
records=[]
for wait,used,count,action,position,fail in itertools.product([0,1],[0,1],[0,1,2],[0,4,21],[-150,150],[0,1,2]):
 before=Actors();before[0][0][0]=1
 for i in range(1,count+1):before[0][i][0]=42;before[0][i][1]=action;before[0][i][3]=[0,3000,19800][i]
 n.cpu.mem_write(g,bytes(0x500000));n.cpu.mem_write(g+0x84080,bytes(before));write(0x9ee48,20000);write(0x270c+2*4,wait);n.cpu.mem_write(g+0x275c+2,bytes([used]))
 actors=Actors.from_buffer_copy(bytes(before));state=State();state.active[2]=1;state.wait[2]=wait;state.used[2]=used
 environment=(c.c_int32*128)();environment[2]=20000;seed=c.c_uint32(0x12345678);native_seed=seed.value
 native_calls=[];native_sounds=[];cpp_calls=[]
 def create_native():
  global native_seed
  native_calls.append([reg(i) for i in range(1,8)])
  if fail and len(native_calls)==fail:return -1
  native_seed=random(native_seed);slot=10+len(native_calls);values=[0]*251;values[0]=72;values[3]=16800;values[13]=450
  n.cpu.mem_write(g+0x84080+slot*1004,struct.pack('<251i',*values));return slot
 @Constructor
 def create_cpp(_,request,random_state):
  p=request.contents;cpp_calls.append([getattr(p,k) for k,_ in Spawn._fields_])
  if fail and len(cpp_calls)==fail:return -1
  random_state[0]=random(random_state[0]);slot=10+len(cpp_calls);actors[0][slot][0]=72;actors[0][slot][3]=16800;actors[0][slot][13]=450;return slot
 n.helpers={0x81f580:g,0x5bc910:1,0x5bcdec:1,0x5be130:7500,0x5bf81c:1,0x5c2d18:1000,0x5c2720:0,0x9e583c:0,
  0x5bbbf0:2,0x6505d0:1,0xacf894:29,0xacf804:7,0x44abfc:lambda:min(reg(0),reg(1)),
  0x5bf8e8:int(not used and count>0 and action!=4),0x5bce08:lambda:70 if reg(1)>10 else 40,
  0x5bc280:lambda:72 if reg(1)>10 else 42,0x5bce20:lambda:0 if reg(1)>10 else 2,0x63e7a8:20,
  0xa93f08:lambda:struct.unpack('<i',n.cpu.mem_read(g+0x84080+reg(1)*1004,4))[0],
  0xa93fc8:lambda:struct.unpack('<i',n.cpu.mem_read(g+0x84080+reg(1)*1004,4))[0]-2,
  0xa9482c:lambda:struct.unpack('<i',n.cpu.mem_read(g+0x8408c+reg(1)*1004,4))[0],
  0xa95cb8:450,0x9f1e64:create_native,0x9019f4:position,0x457e1c:0,0xa60594:0,
  0x459efc:lambda:native_sounds.append(reg(1)) or 0}
 n.call(0x9f4a74,g,0,2,1)
 out=Output();request=Input(Spawn(0,72,19,0,0,0,0),2,42,position)
 assert lib.kbcs_core_actor_summon(c.byref(request),c.byref(state),c.byref(actors),environment,c.byref(seed),create_cpp,None,c.byref(out))==0
 assert bytes(actors)==bytes(n.cpu.mem_read(g+0x84080,c.sizeof(actors))),(wait,used,count,action,position,fail,'actors')
 assert cpp_calls==native_calls,(cpp_calls,native_calls)
 assert state.used[2]==n.cpu.mem_read(g+0x275c+2,1)[0] and seed.value==native_seed
 sounds=[v for v in [out.sound,out.failure_sound,out.completion_sound] if v>=0]
 assert sounds==native_sounds,(wait,used,count,action,position,fail,sounds,native_sounds)
 records.append({'wait':wait,'used':used,'parents':count,'action':action,'position':position,'fail':fail,'created':out.count,'sounds':sounds})
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(args.library.read_bytes()),'cases':len(records),'controlled':['profile and eligibility getters','individual construction and level clamp','parameter lookup','sound and achievement sink'],'records':records}
(ROOT/'research/.local/actor-summon-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig')
print(json.dumps({'cases':len(records),'result':'equal'}))
