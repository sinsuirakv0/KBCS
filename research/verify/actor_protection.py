"""006d97dc..006d9da0のバリア・盾確定をARM64と比較する。描画プールは別責務。"""
import argparse
import ctypes as c
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
class Protection(c.Structure):
    _fields_=[('shield_hit',c.c_int32),('sound_count',c.c_int32),('sounds',c.c_int32*2),('visual_count',c.c_int32),('visuals',(c.c_int32*4)*2)]
class ProtectionNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=ProtectionNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44abe4,0x5bb5b8,0x5bb5d0] for pc in range(a,a+sizes[a],4)}
n.entry=0x6d6d04;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={0x6d9510,0x6d9da0}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_protect.argtypes=[c.POINTER(Actor*51),c.c_int32,c.c_int32,c.POINTER(Protection)]
records=[];count=0
for side in [0,1]:
 for barrier in [0,100]:
  for barrier_flag in [0,1,2]:
   for shield in [0,49,50,100]:
    for shield_flag in [0,1,2]:
     for damage in [0,49,50,51,100,101]:
      pool=Pool();word=pool[side][1].words
      for i in range(251):word[i]=(i*17+3)%13
      for i,v in {0:2,3:12345,4:-200,19:damage,130:barrier,131:barrier_flag,162:1,184:100,190:shield,192:shield_flag,194:0}.items():word[i]=v
      before=list(word)
      n.cpu.mem_write(game,bytes(0x500000));n.cpu.mem_write(game+0x84080,bytes(pool))
      tree=n.memory+0x4000;node=n.memory+0x5000;sp=n.stack+0x8000
      n.cpu.mem_write(tree,struct.pack('<QQQ',tree+8,0,0));n.cpu.mem_write(node,bytes(40))
      n.cpu.mem_write(sp-0x100,bytes(0x400))
      for offset,value in [(0x1e8,tree+8),(0x140,game+0x9e750),(0x1e0,game+0x9ea98),(0x1f0,game+0x84080),(0x1d8,game+0x84080+side*0xc804)]:n.cpu.mem_write(sp+offset,struct.pack('<Q',value))
      sounds=[]
      def sound():sounds.append(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1));return 0
      n.helpers={0x81f580:game,0x457e1c:0,0x459f04:sound,0xbdaf40:node,0x419064:0}
      for register,value in [('SP',sp),('X23',tree),('W27',side),('W28',1)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
      n.cpu.emu_start(0x6d97dc,n.stop+4,count=100000)
      assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'protection budget'
      expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)))
      output=Protection();assert lib.kbcs_core_actor_protect(pool,side,1,c.byref(output))==0
      assert bytes(pool)==expected,{'input':before,'differences':[(i,a,b) for i,(a,b) in enumerate(zip(bytes(pool),expected)) if a!=b][:20]}
      assert list(output.sounds)[:output.sound_count]==sounds
      assert output.shield_hit==int(n.cpu.mem_read(node+32,1)[0]!=0)
      visuals=[]
      for kind,address in [(0,game+0x9e750),(1,game+0x9ea98)]:
       if n.cpu.mem_read(address,1)[0]&1:
        x,y=struct.unpack('<ii',n.cpu.mem_read(address+4,8));visuals.append([kind,x,y,n.cpu.mem_read(address+24,1)[0]])
      assert [list(v) for v in output.visuals][:output.visual_count]==visuals
      count+=1
      if count%17==0 or (barrier and shield and damage==101):
       records.append({'side':side,'before':before,'after':list(word),'shield_hit':output.shield_hit,'sounds':sounds,'visuals':visuals})
print(json.dumps({'protectionCases':count,'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'entry':'006d97dc','terminals':['006d9510','006d9da0'],'records':records,'cases':count,'controlled':['singleton game address','sound manager and sound emission capture','operator_new and empty shield-hit tree rebalance']}
(ROOT/'research/.local/actor-protection-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-protection-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
