"""スニャイパーの照準/射撃/弾と到達命中を同版ARM64へ局所照合する。"""
import argparse,ctypes as c,itertools,json,os,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--library',type=Path,required=True)
parser.add_argument('--hit-only',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs))
from stages import Native,ROOT,SHA,digest
class SniperNative(Native):
 def hook(self,cpu,address,size,data):
  if any(a<=address<self.ends[a] for a in self.actual):return
  super().hook(cpu,address,size,data)
n=SniperNative();g=0x40000000;n.cpu.mem_map(g,0x500000)
actual=['0044aa9c','0044aad4','0044ab0c','00a94484','00a94678','00a9bbac','00a9cc4c','00a9cc8c','00a9b790','00a9b81c','00a9cd6c','00a96cd8']
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for a,size in db.execute('SELECT address,size FROM functions WHERE address IN ('+','.join('?' for _ in actual+['005ce564','005ced48'])+')',actual+['005ce564','005ced48']):n.ends[int(a,16)]=int(a,16)+size
n.actual=[int(a,16) for a in actual]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));math=c.CDLL('ucrtbase.dll')
for name,kind,count in [('sin',c.c_double,1),('cos',c.c_double,1),('atan2f',c.c_float,2)]:
 fn=getattr(math,name);fn.argtypes=[kind]*count;fn.restype=kind
class Bullet(c.Structure):_fields_=[(k,c.c_int32) for k in ['active','x','y','target','angle','speed']]
class State(c.Structure):_fields_=[('angle',c.c_float),('desired',c.c_float)]+[(k,c.c_int32) for k in ['target','wait','firing','frame','gun_recoil','body_bump']]+[('bullets',Bullet*50),('impacts',(c.c_int32*6)*50),('smoke_active',c.c_int32),('smoke',(c.c_int32*5)*4)]
class Input(c.Structure):_fields_=[(k,c.c_int32) for k in ['enabled','camera','height']]+[('phase',c.c_float)]
Actors=((c.c_int32*251)*51)*2
lib.kbcs_core_actor_sniper_step.argtypes=[c.POINTER(State),c.POINTER(Input),c.POINTER(Actors),c.c_void_p,c.POINTER(c.c_int32)]
lib.kbcs_core_actor_sniper_hit.argtypes=[c.POINTER(State),c.POINTER(Actors),c.c_void_p,c.c_int32,c.POINTER(c.c_uint32),c.POINTER(c.c_int32)]
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))&0xffffffff
def put(offset,value):n.cpu.mem_write(g+offset,struct.pack('<i',value))
def get(offset):return struct.unpack('<i',n.cpu.mem_read(g+offset,4))[0]
def floating(i,double=False):return struct.unpack('<d' if double else '<f',struct.pack('<Q' if double else '<I',n.cpu.reg_read(getattr(n.reg,('UC_ARM64_REG_D' if double else 'UC_ARM64_REG_S')+str(i)))))[0]
def result_float(value,double=False):n.cpu.reg_write(n.reg.UC_ARM64_REG_D0 if double else n.reg.UC_ARM64_REG_S0,struct.unpack('<Q' if double else '<I',struct.pack('<d' if double else '<f',value))[0]);return 0
def trig(name):return result_float(getattr(math,name)(floating(0,True)),True)
helpers={0x81f580:g,0x5c2710:0,0xbdb490:lambda:trig('sin'),0xbdb4a0:lambda:trig('cos'),0xbdb4c0:lambda:result_float(math.atan2f(floating(0),floating(1))),0x5bc058:0,0x449bac:640,0x5bbbc8:0}
fields={'angle':0x32e0a8,'desired':0x32e0ac,'target':0x32e0a0,'wait':0x32e4cc,'firing':0x32e4d0,'frame':0x32e4d4,'gun_recoil':0x32e4d8,'body_bump':0x32e080}
def write_state(s):
 for key,offset in fields.items():
  if key in ['angle','desired']:n.cpu.mem_write(g+offset,struct.pack('<f',getattr(s,key)))
  else:put(offset,getattr(s,key))
 put(0x32e9dc,s.smoke_active);n.cpu.mem_write(g+0x32e4dc,bytes(s.smoke))
 for i,b in enumerate(s.bullets):
  for key,offset in [('x',0x32e0b0),('y',0x32e178),('target',0x32e240),('angle',0x32e404),('speed',0x32e33c)]:put(offset+i*4,getattr(b,key))
  n.cpu.mem_write(g+0x32e308+i,bytes([b.active]));n.cpu.mem_write(g+0x32e52c+i*24,bytes(s.impacts[i]))
def read_state():
 s=State()
 for key,offset in fields.items():setattr(s,key,struct.unpack('<f',n.cpu.mem_read(g+offset,4))[0] if key in ['angle','desired'] else get(offset))
 for i,b in enumerate(s.bullets):
  for key,offset in [('x',0x32e0b0),('y',0x32e178),('target',0x32e240),('angle',0x32e404),('speed',0x32e33c)]:setattr(b,key,get(offset+i*4))
  b.active=n.cpu.mem_read(g+0x32e308+i,1)[0];s.impacts[i][:]=struct.unpack('<6i',n.cpu.mem_read(g+0x32e52c+i*24,24))
 s.smoke_active=get(0x32e9dc);c.memmove(c.addressof(s.smoke),bytes(n.cpu.mem_read(g+0x32e4dc,80)),80)
 return s
def mismatch(a,b):
 for k,_ in State._fields_:
  va,vb=getattr(a,k),getattr(b,k)
  if k not in ['bullets','impacts','smoke'] and va!=vb:return k,va,vb
 return 'arrays'
environment=(c.c_int32*128)();environment[0]=1;environment[2]=20000;environment[3]=-1
steps=0;shots=0
for scenario in range(0 if args.hit_only else 6):
 n.cpu.mem_write(g,bytes(0x500000));s=State();write_state(s);actors=Actors();actors[0][0][0]=1;actors[0][0][3]=16800;actors[0][0][4]=4400;actors[0][0][7]=236000
 if scenario==5:
  for b in s.bullets:b.active=1;b.x=10000000;b.speed=1500;b.target=1
  write_state(s)
 phase=c.c_float(0)
 for tick in range(620):
  phase.value+=6;enabled=not(scenario==4 and 310<=tick<350);camera=[0,4890,11001][scenario%3]
  for i in range(1,4):
   actors[1][i][0]=2+i;actors[1][i][1]=[0,2,0][i-1];actors[1][i][3]=3200+i*800+(tick%30 if scenario==2 else 0);actors[1][i][4]=4400;actors[1][i][5]=i%2
  if scenario==1:actors[1][3][3]=actors[1][2][3]
  if scenario==3 and 305<=tick<320:
   for i in range(1,4):actors[1][i][0]=0
  n.cpu.mem_write(g+0x84080,bytes(actors));put(0x83e10,camera);n.cpu.mem_write(g+0x32e0a4,struct.pack('<f',phase.value))
  n.helpers={**helpers,0x5c022c:int(enabled),0x5bbc10:-1,0xa92ea0:actors[0][0][3],0xa92eb4:4400}
  n.call(0x5ce564,g)
  fired=c.c_int32();value=Input(enabled,camera,640,phase.value)
  assert lib.kbcs_core_actor_sniper_step(c.byref(s),c.byref(value),c.byref(actors),environment,c.byref(fired))==0
  expected=read_state();assert bytes(s)==bytes(expected),(scenario,tick,mismatch(s,expected))
  steps+=1;shots+=fired.value>=0
if not args.hit_only:assert shots>0,'実弾の生成を通過していません'
hit_cases=0
for action,x,remaining,chance,metal,count,initial_seed in itertools.product([0,3,11,14,16],[3000,3001],[0,3],[0,33,100],[0,1],[1,2],[0x12345678,7]):
 n.cpu.mem_write(g,bytes(0x500000));actors=Actors();actors[0][0][0]=1;actors[0][0][7]=236000
 target=actors[1][1];target[0]=2;target[1]=action;target[3]=3000;target[4]=4400;target[7]=target[8]=10001;target[43]=metal;target[165]=chance;target[167]=remaining;target[168]=59
 n.cpu.mem_write(g+0x84080,bytes(actors));s=State()
 for i in range(count):s.bullets[i]=Bullet(1,x,0,1,0,1500)
 write_state(s);native_seed=initial_seed
 def random():
  global native_seed
  bound=reg(0);native_seed^=(native_seed<<13)&0xffffffff;native_seed^=native_seed>>17;native_seed^=(native_seed<<15)&0xffffffff;native_seed&=0xffffffff;return native_seed%bound
 def name():n.cpu.mem_write(n.cpu.reg_read(n.reg.UC_ARM64_REG_X8),bytes(24));return 0
 n.helpers={**helpers,0x44a8d8:random,0xa9327c:11800,0xa94074:name}
 n.call(0x5ced48,g,1,1,0)
 seed=c.c_uint32(initial_seed);hits=c.c_int32()
 assert lib.kbcs_core_actor_sniper_hit(c.byref(s),c.byref(actors),environment,1,c.byref(seed),c.byref(hits))==0
 expected=read_state();assert bytes(s)==bytes(expected),('hit',action,x,remaining,chance,metal,count,mismatch(s,expected))
 assert bytes(actors)==bytes(n.cpu.mem_read(g+0x84080,c.sizeof(actors))),('hit actors',action,x,remaining,chance,metal,count)
 assert seed.value==native_seed,('hit RNG',seed.value,native_seed)
 hit_cases+=1
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(args.library.read_bytes()),'stepUpdates':steps,'shots':shots,'hitCases':hit_cases,'controlled':['item/game mode/camera/castle getters','system libm calls use UCRT on both sides','RNG getter, debug name, castle damage getter'],'limits':['Android libm versus UCRT is not verified']}
if args.hit_only:
 previous=json.loads((ROOT/'research/.local/actor-sniper-1572.json').read_text(encoding='utf-8-sig'))
 if previous['librarySha256']==report['librarySha256']:
  for key in ['stepUpdates','shots']:report[key]=previous[key]
(ROOT/'research/.local/actor-sniper-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig')
print(json.dumps(report))
