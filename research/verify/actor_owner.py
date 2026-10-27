"""死亡時の効果所有者走査を、行動関数内の実命令区間へ照合する。"""
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
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA
class Actor(c.Structure):_fields_=[('words',c.c_int32*251)]
Pool=(Actor*51)*2
class Hit(c.Structure):_fields_=[('words',c.c_int32*19)]
class Wave(c.Structure):_fields_=[(key,c.c_int32) for key in ['side','slot','state','frame','x','level','hit']]+[('flags',c.c_uint8*12),('parameter',c.c_int32),('mini',c.c_uint8),('reserved',c.c_uint8*3)]
class Waves(c.Structure):_fields_=[('records',Wave*200),('hits',(c.c_uint8*200)*51)]
class Surge(c.Structure):_fields_=[(key,c.c_int32) for key in ['side','slot','frame','x','level','hit']]+[('flags',c.c_uint8*12),('parameter',c.c_int32),('mini',c.c_uint8),('reserved',c.c_uint8*3),('kind',c.c_int32)]
class Explosion(c.Structure):_fields_=[(key,c.c_int32) for key in ['side','slot','frame','x','hit']]+[('flags',c.c_uint8*12),('parameter',c.c_int32)]
class Area(c.Structure):_fields_=[('surge_present',c.c_int32),('explosion_present',c.c_int32),('surge',Surge),('explosion',Explosion)]
class Reflection(c.Structure):_fields_=[('words',c.c_int32*9)]
class Counts(c.Structure):_fields_=[(key,c.c_int32) for key in ['surges','reflections','explosions','events']]
Sink=c.CFUNCTYPE(c.c_uint32,c.c_void_p,c.POINTER(Actor*51),c.POINTER(c.c_uint32),c.c_void_p,c.POINTER(c.c_int32))
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()))
lib.kbcs_core_actor_areas_create.argtypes=[c.POINTER(c.c_void_p)];lib.kbcs_core_actor_areas_destroy.argtypes=[c.c_void_p]
lib.kbcs_core_actor_areas_append.argtypes=[c.c_void_p,c.POINTER(Area)];lib.kbcs_core_actor_areas_counts.argtypes=[c.c_void_p,c.POINTER(Counts)]
lib.kbcs_core_actor_areas_surge.argtypes=[c.c_void_p,c.c_int32,c.POINTER(Surge),c.c_void_p]
lib.kbcs_core_actor_areas_reflection.argtypes=[c.c_void_p,c.c_int32,c.POINTER(Reflection)]
lib.kbcs_core_actor_areas_explosion.argtypes=[c.c_void_p,c.c_int32,c.POINTER(Explosion),c.c_void_p]
lib.kbcs_core_actor_areas_retirement_blocked.argtypes=[c.c_void_p,c.POINTER(Waves),c.c_int32,c.c_int32,c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_core_actor_areas_step.argtypes=[c.c_void_p,c.c_int32,c.POINTER(Actor*51),c.c_void_p,c.c_void_p,c.POINTER(c.c_uint32),Sink,c.c_void_p]
n=Native();game=0x40000000;n.cpu.mem_map(game,0x800000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address IN ('006eb464','006eccf4')")}
@Sink
def applied(user,actors,seed,event,out):out[0]=1;return 0
records=[];count=0
for side,unit_route,mask,wave_state,mismatch in itertools.product([0,1],[0,1],range(16),range(4),[0,1]):
 handle=c.c_void_p();assert lib.kbcs_core_actor_areas_create(c.byref(handle))==0
 if mask&2:
  pool=Pool();word=pool[side][1].words;word[0]=2;word[1]=0;word[3]=10000+(250 if side else -250);word[212]=1
  incoming=Area(surge_present=1);incoming.surge=Surge(side=1-side,slot=2,frame=14,x=10000,level=1)
  assert lib.kbcs_core_actor_areas_append(handle,c.byref(incoming))==0
  # この走査区間は環境値を参照しない。構造体の108語は0、unit_modesだけ[1,0]。
  environment=(c.c_int32*108)(1,0);rules=(c.c_int32*14)();seed=c.c_uint32(0x12345678)
  assert lib.kbcs_core_actor_areas_step(handle,0,pool,environment,rules,c.byref(seed),applied,None)==0
  counts=Counts();lib.kbcs_core_actor_areas_counts(handle,c.byref(counts));assert counts.reflections==1
 area=Area(surge_present=int(bool(mask&1)),explosion_present=int(bool(mask&4)));area.surge=Surge(side=side^mismatch,slot=1,level=1);area.explosion=Explosion(side=side,slot=1)
 assert lib.kbcs_core_actor_areas_append(handle,c.byref(area))==0
 waves=Waves()
 if mask&8:waves.records[199 if mismatch else 0]=Wave(side=7,slot=1+mismatch,state=wave_state)
 n.cpu.mem_write(game+0x33b81c,bytes(waves.records))
 counts=Counts();assert lib.kbcs_core_actor_areas_counts(handle,c.byref(counts))==0
 for kind,(offset,number,record_type,method) in enumerate([(0x340320,counts.surges,Surge,lib.kbcs_core_actor_areas_surge),(0x340338,counts.reflections,Reflection,lib.kbcs_core_actor_areas_reflection),(0x340350,counts.explosions,Explosion,lib.kbcs_core_actor_areas_explosion)]):
  table=n.memory+0x1000+kind*0x1000;pointers=[]
  for i in range(number):
   record=record_type();code=method(handle,i,c.byref(record)) if kind==1 else method(handle,i,c.byref(record),None);assert code==0
   address=table+0x100+i*0x100;n.cpu.mem_write(address,bytes(record));pointers.append(address)
  if pointers:n.cpu.mem_write(table,struct.pack('<'+'Q'*number,*pointers))
  n.cpu.mem_write(game+offset,struct.pack('<QQQ',table,table+number*8,table+number*8))
 sp=n.stack+0x8000;fp=sp+0x200;n.cpu.mem_write(sp-0x100,bytes(0x400));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678));n.helpers={}
 if unit_route:
  n.entry=0x6eb464;n.terminals={0x6ebb0c};start=0x6eb978
  n.cpu.mem_write(fp-0x88,struct.pack('<Q',game+0x33b824));registers=[('W20',side),('X23',1),('X28',game+0x340320)]
 else:
  n.entry=0x6eccf4;n.terminals={0x6ed5e0};start=0x6ed4ec
  n.cpu.mem_write(sp+0x90,struct.pack('<QQ',game+0x33b824,game+0x340320));registers=[('W19',side),('X26',1)]
 n.ends[n.entry]=n.entry+sizes[n.entry]
 for register,value in [('SP',sp),('X29',fp),*registers]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 n.cpu.emu_start(start,n.stop+4,count=10000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals
 free=n.cpu.reg_read(n.reg.UC_ARM64_REG_W25) if unit_route else struct.unpack('<i',n.cpu.mem_read(sp+0x6c,4))[0]
 out=c.c_int32(-1);assert lib.kbcs_core_actor_areas_retirement_blocked(handle,c.byref(waves),side,1,unit_route,c.byref(out))==0
 assert out.value==1-free,(side,unit_route,mask,wave_state,mismatch,out.value,free)
 assert struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]==0x12345678
 lib.kbcs_core_actor_areas_destroy(handle);count+=1
 if count%61==0 or (mask in [2,4] and wave_state==0 and mismatch==0):records.append({'side':side,'unit_route':unit_route,'mask':mask,'wave_state':wave_state,'mismatch':mismatch,'blocked':out.value})
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'cases':count,'entries':['006eb978','006ed4ec'],'terminals':['006ebb0c','006ed5e0'],'records':records,'controlled':['local entry registers/stack and effect pointer lists','same supplied typed records normalized to native pointer lists','existing action conditions resolved before ownership scan'],'limits':['ownership guard only; full retirement/action dispatcher not executed']}
(ROOT/'research/.local/actor-owner-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-owner-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
print(json.dumps({'ownerGuardCases':count,'published':len(records)}))
