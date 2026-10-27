"""ニャンピュータ006ee6c8を同版ARM64と比較する（判断・保持・RNG・操作要求）。"""
import argparse,ctypes as c,json,os,random,sqlite3,struct,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path,required=True)
a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
class ComputerNative(Native):
 def hook(self,cpu,address,size,data):
  if any(start<=address<self.ends[start] for start in self.actual):return
  super().hook(cpu,address,size,data)
n=ComputerNative();g=0x40000000;n.cpu.mem_map(g,0x500000)
n.actual=[0x44a8d8,0x44a8e8,0x5bf658,0x5bf6c8,0xa92ec8,0xa92f5c,0xa93f08]
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for start in [0x6ee6c8]+n.actual:
  row=db.execute('SELECT size FROM functions WHERE address=?',(f'{start:08x}',)).fetchone();n.ends[start]=start+row[0]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()))
class Input(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['enabled','mode','worker','money','wallet','upgrade_cost','worker_level','page','page_frame','page_direction','page_step','full','cannon_wait','cannon_action','cannon_range','castle_x','camera']]+[(k,c.c_int32*10) for k in ['raw','cost','eligible','wait','summoned']]
class State(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['action','selected','pending_raw','cannon_state','cannon_wait']]+[(k,c.c_int32*10) for k in ['candidates','choices']]
class Output(c.Structure):_fields_=[(k,c.c_int32) for k in ['deploy','upgrade','fire','page_start','page_step']]
Actors=(c.c_int32*251)*51
lib.kbcs_core_battle_computer.argtypes=[c.POINTER(Input),c.POINTER(State),c.POINTER(Actors),c.POINTER(c.c_uint32),c.POINTER(Output)]
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))&0xffffffff
def put(offset,value):n.cpu.mem_write(g+offset,struct.pack('<i',value))
def get(offset):return struct.unpack('<i',n.cpu.mem_read(g+offset,4))[0]
fields={'action':0x32ff9c,'selected':0x32ffa4,'pending_raw':0x32fffc,'cannon_state':0x330004,'cannon_wait':0x33000c,'candidates':0x32ffac,'choices':0x33001c}
def write_state(s):
 for k,off in fields.items():
  if k in ['candidates','choices']:n.cpu.mem_write(g+off,bytes(getattr(s,k)))
  else:put(off,getattr(s,k))
def read_state():
 s=State()
 for k,off in fields.items():
  if k in ['candidates','choices']:getattr(s,k)[:]=struct.unpack('<10i',n.cpu.mem_read(g+off,40))
  else:setattr(s,k,get(off))
 return s
rng=random.Random(1572006);cases=[];operations=set();updates=0
for case in range(640):
 n.cpu.mem_write(g,bytes(0x500000));i=Input();s=State();opponents=Actors()
 i.enabled=int(case%17!=0);i.mode=[0,0,0,1,2][case%5];i.worker=case%8;i.worker_level=[0,6,7,29][case%4]
 i.wallet=[15000,1656000,60000][case%3];i.upgrade_cost=(4000+i.worker_level*1000 if i.worker_level<7 else -2000+i.worker_level*2000)*(i.worker+1)
 i.money=[0,i.upgrade_cost-1,i.upgrade_cost,i.wallet][case%4];i.page=case%2;i.page_frame=case%6;i.page_direction=(case//2)%2;i.page_step=[1,-1][case%2]
 i.full=int(case%19==0);i.cannon_wait=0 if case%3 else 15;i.cannon_action=0 if case%7 else 1;i.cannon_range=[0,1,3,6][case%4];i.castle_x=16800+case%10;i.camera=[0,4893,11001][case%3]
 s.action=case%4;s.selected=case%10;s.pending_raw=-1;s.cannon_state=case%5;s.cannon_wait=[0,1,2,149][case%4]
 for slot in range(10):
  i.raw[slot]=slot+2 if rng.randrange(4) else -1;i.cost[slot]=rng.choice([1,15000,100000,2000000]);i.eligible[slot]=int(rng.randrange(4)!=0);i.wait[slot]=rng.choice([0,0,1,60]);i.summoned[slot]=int(rng.randrange(10)==0)
  s.candidates[slot]=slot if rng.randrange(2) else -1;s.choices[slot]=slot
 for slot in range(1,51):
  if rng.randrange(5)==0:opponents[slot][0]=2+slot;opponents[slot][1]=rng.choice([0,2,4,14]);opponents[slot][3]=rng.choice([1000,7000,10000,15070,15071,18000])+case%10
 if i.full:
  for slot in range(1,51):put(0x84080+slot*1004,2)
 for frame in range(4):
  n.cpu.mem_write(g+0x90884,bytes(opponents));put(0x8408c,i.castle_x);put(0x83e10,i.camera);put(0x84098,i.cannon_range);put(0x840a4,i.cannon_action);put(0x840b0,i.cannon_wait)
  put(0x2971f0,i.mode);n.cpu.mem_write(g+0x32ff98,bytes([i.enabled]));put(0x32e9e0,i.page);put(0x32e9f8,i.page_direction);put(0x32e07c,i.page_step);n.cpu.mem_write(g+0x32e9fc,bytes([bool(i.page_frame)]));write_state(s)
  events=[]
  def event(kind,slot=-1):events.append((kind,slot));return 0
  def cost():return i.cost[reg(1)] if reg(1)<10 else 0
  def raw():return i.raw[reg(1)] if reg(1)<10 else -1
  n.helpers={0x9e57b8:0,0x5bcdec:lambda:int(raw()!=-1),0x5bc910:lambda:i.eligible[reg(1)],0x9e583c:0,0x5bf81c:lambda:i.summoned[reg(1)],0x5c2d18:lambda:i.wait[reg(1)],0x5c2a5c:i.worker,0x5c27f4:i.wallet,0x5c2720:i.money,0x5be130:cost,0x5c2b4c:i.worker_level,0x5bc280:raw,0x5c2aa0:i.upgrade_cost,0x5c2990:lambda:event('money'),0x5c2ca8:lambda:event('upgrade'),0x457e1c:0,0x459efc:0,0x5d8f58:lambda:event('fire'),0x9f4a74:lambda:event('deploy',reg(2)),0x81f580:g}
  seed=rng.randrange(1,0xffffffff);n.cpu.mem_write(0xc24d18,struct.pack('<I',seed));native_seed=c.c_uint32(seed)
  n.call(0x6ee6c8,g,0);expected=read_state();out=Output()
  code=lib.kbcs_core_battle_computer(c.byref(i),c.byref(s),c.byref(opponents),c.byref(native_seed),c.byref(out));assert code==0,(case,frame,code)
  assert bytes(s)==bytes(expected),(case,frame,'computer state',list(struct.unpack('<25i',bytes(s))),list(struct.unpack('<25i',bytes(expected))))
  assert native_seed.value==struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0],(case,frame,'rng')
  expected_events=[('upgrade' if k=='upgrade' else k,slot) for k,slot in events if k!='money']
  got=([('upgrade',-1)] if out.upgrade else [])+([('fire',-1)] if out.fire else [])+([('deploy',out.deploy)] if out.deploy>=0 else [])
  assert got==expected_events,(case,frame,got,expected_events)
  assert out.page_start==int(not i.page_frame and n.cpu.mem_read(g+0x32e9fc,1)[0]!=0),(case,frame,'page start')
  assert out.page_step==get(0x32e07c),(case,frame,'page step')
  operations.update(k for k,_ in got);updates+=1
assert operations=={'upgrade','fire','deploy'},operations
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(a.library.read_bytes()),'entry':'006ee6c8','cases':640,'updates':updates,'operations':sorted(operations),'controlled':['deployment eligibility and price/recharge/profile getters','wallet getters/setters','deployment/cannon calls and audio','009e57b8 census'],'actual':['candidate and retained action branches','cannon two-stage random decision and range helpers','page requests','Xorshift32 consumption'],'result':'equal'}
(ROOT/'research/.local/battle-computer-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig');print(json.dumps(report,ensure_ascii=False))
