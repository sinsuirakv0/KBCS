"""出現予定による城HP保持旗の計算を006d9e44..006d9fc0と比較する。"""
import argparse,ctypes as c,json,os,random,sqlite3,struct,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path,required=True)
a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
class GuardNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
  if any(start<=address<self.ends[start] for start in self.actual):return
  return super().hook(cpu,address,size,data)
n=GuardNative();g=0x40000000;n.cpu.mem_map(g,0x800000);n.actual=[0xa06c60,0xa06c80,0xa06ca0]
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for address in [0x6d6d04,*n.actual]:n.ends[address]=address+db.execute('SELECT size FROM functions WHERE address=?',(f'{address:08x}',)).fetchone()[0]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()))
class Row(c.Structure):_fields_=[('cells',c.c_int32*14)]
class State(c.Structure):_fields_=[(k,c.c_int32) for k in ['wait','spawned','kills']]
class Context(c.Structure):_fields_=[(k,c.c_int32) for k in ['global_wait','kill_delta','active_enemies','max_enemies','castle_hp','castle_max_hp','castle_damage','damage_condition','paused','global_min','global_max']]
lib.kbcs_core_stage_castle_guard.argtypes=[c.POINTER(Row),c.POINTER(State),c.c_int32,c.POINTER(Context),c.c_int32,c.POINTER(c.c_int32)]
def pointer(address,value):n.cpu.mem_write(address,struct.pack('<Q',value))
def put(address,value):n.cpu.mem_write(address,struct.pack('<i',value))
rows=n.memory+0x5000;states=n.memory+0x4000;sp=n.stack+0x8000;rng=random.Random(1572028);count=0
for case in range(1024):
 size=case%4;data=(Row*size)();status=(State*size)();hp=rng.choice([0,1,2,100,2147483647]);maximum=rng.choice([100,2147483647]);pending=rng.choice([-1,0,1,99,100,2147483647]);damage=rng.choice([0,49,50,100]);mode=case%2;before=case//2%2
 for row,state in zip(data,status):
  row.cells[1]=rng.choice([0,1,2]);row.cells[5]=rng.choice([0,50,100,2147483647]);row.cells[8]=rng.choice([0,1,2]);state.spawned=rng.choice([0,1,2]);state.wait=rng.choice([-1,0,1,100]);state.kills=rng.choice([0,1,100]);row.cells[13]=100
 n.cpu.mem_write(rows,bytes(data));n.cpu.mem_write(states,bytes(status));pointer(g+0x9ee70,rows);pointer(g+0x9ee78,rows+c.sizeof(data));pointer(g+0x84050,states)
 put(g+0x908a0,maximum);put(g+0x908a4,hp);put(g+0x239e6c,mode);n.cpu.mem_write(g+0x39a228,bytes([before]))
 for offset,value in [(0x1e0,g+0x9ea98),(0x110,g+0x83e60),(0xb0,g+0x239da8)]:pointer(sp+offset,value)
 n.helpers={0x5bbbc8:mode,0x5bbbf0:0,0x5bbc10:1,0xa951e0:damage,0xa958b0:hp,0xa9baf8:pending};n.entry=0x6d6d04;n.terminals={0x6d9fc0}
 for register,value in [('SP',sp),('X9',g+0x9ea98),('X26',g+0x90890),('X27',g)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 n.cpu.emu_start(0x6d9e44,n.stop+4,count=10000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==0x6d9fc0
 expected=n.cpu.mem_read(g+0x39a228,1)[0];context=Context(castle_hp=hp,castle_max_hp=maximum,castle_damage=damage,damage_condition=mode);actual=c.c_int32(before)
 assert lib.kbcs_core_stage_castle_guard(data,status,size,c.byref(context),pending,c.byref(actual))==0
 assert actual.value==expected,(case,hp,maximum,pending,mode,damage,actual.value,expected);count+=1
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(a.library.read_bytes()),'cases':count,'result':'equal','actual':['006d9e44..006d9fc0 and row getters'],'controlled':['castle presence/CSV damage-condition flag','resolved castle HP/pending damage/cumulative damage getters'],'boundaries':['HP 0/1/2','count 0/1/2 and spawned limit','boss 0/1/2','32-bit multiply/subtract wrap','sticky flag','wait and kills intentionally ignored']}
(ROOT/'research/.local/stage-castle-guard-1572.json').write_text(json.dumps(report,indent=2),encoding='utf-8-sig');print(json.dumps(report))
