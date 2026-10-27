"""SEの終了ゲート・オプションcallback・命中音の乱数消費を同版ARM64で検査する。"""
import argparse,ctypes as c,itertools,json,os,sqlite3,struct,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path,required=True)
a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
class AudioNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.terminals or address in self.helpers:return super().hook(cpu,address,size,data)
  if any(start<=address<self.ends[start] for start in self.actual):return
  return super().hook(cpu,address,size,data)
n=AudioNative();g=0x40000000;n.cpu.mem_map(g,0x500000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 n.ends.update({int(address,16):int(address,16)+size for address,size in db.execute("select address,size from functions where address not like 'EXTERNAL:%'")})
n.actual=[0x44a8d8,0x44a8e8]
dll_dir=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()));lib.kbcs_core_random_bounded.argtypes=[c.POINTER(c.c_uint32),c.c_int32,c.POINTER(c.c_int32)]
records=[];sounds=[];level=3
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))
def sound():sounds.append(reg(1));return 0
for mode in [0,1,2,4,7]:
 sounds.clear();n.helpers={0x5bc058:mode,0x459170:sound};n.call(0x459f04,0,44)
 assert sounds==([44] if not mode else []);records.append({'wrapperMode':mode,'sounds':sounds.copy()})
for callback in [0x8fef58,0x8ff0d8,0x8ff260,0x8ff388,0x8ffb80]:
 for event,current in itertools.product([0,1,2,3],range(4)):
  sounds.clear();level=current;n.terminals=set();n.cpu.mem_write(n.memory+0x100,struct.pack('<Q',n.memory+0x300));n.cpu.mem_write(n.memory+0x200,struct.pack('<i',event))
  def volume():
   global level
   level=reg(1);return 0
  n.helpers={0x81f580:g,0x883cc0:0,0x9e97b8:0,0x9e97a0:0,0x457e1c:0,0x459efc:sound,0x45a1f0:0,0x45a1f8:0,0x8f93f0:current,0x9e9a80:0,0x8fbce8:lambda:reg(0),0x45a208:volume,0x45a244:volume}
  n.call(callback,n.memory+0x400,n.memory+0x100,n.memory+0x200)
  assert sounds==([10] if event==0 else [11] if event==3 else [])
  assert level==((current+1)%4 if callback in [0x8ff260,0x8ff388] and event==3 else current)
  records.append({'callback':f'{callback:08x}','event':event,'level':current,'after':level,'sounds':sounds.copy()})
for mode,kind,initial in itertools.product([0,1,2,4,7],range(3),[1,1572,0xffffffff]):
 sounds.clear();n.cpu.mem_write(0xc24d18,struct.pack('<I',initial));n.helpers={0x5bc058:mode,0x457e1c:0,0x459efc:sound};n.entry=0x6d6d04;n.terminals={0x6db500,0x6db624}
 n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,n.stack+0x8000);n.cpu.reg_write(n.reg.UC_ARM64_REG_W19,kind)
 n.cpu.emu_start(0x6db4f8,n.stop+4,count=10000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals
 seed=c.c_uint32(initial);choice=c.c_int32(0)
 if not mode and kind==1:assert not lib.kbcs_core_random_bounded(c.byref(seed),2,c.byref(choice))
 expected=[] if mode or not kind else [22 if kind==2 else 20+choice.value]
 assert sounds==expected and struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]==seed.value
 records.append({'mode':mode,'impact':kind,'seedBefore':initial,'seedAfter':seed.value,'sounds':sounds.copy()})
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(a.library.read_bytes()),'cases':len(records),'records':records,'controlled':['sound device, sprite output, singleton, resolved volume getter','fragment entry registers and game mode getter'],'limits':['native callback / impact fragment plus shared C++ RNG; full input sequences are covered separately by battle-audio.cpp','Android audio device and voice priority are not executed']}
(ROOT/'research/.local/battle-audio-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig');print(json.dumps({'cases':len(records),'result':'equal'}))
