"""敵KBの移動・終了と、蘇生・撃破数・報酬の分岐を同版ARM64へ照合する。"""
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
class Environment(c.Structure):
    _fields_=[('unit_modes',c.c_int32*2),*[(name,c.c_int32) for name in ['stage_width','castle_slot','castle_x','castle_scale','castle_offset','stage_kind','zombie','chapter_rate','crown','hp_percent','attack_percent']],
              ('crystal_max',c.c_int32*5),('crystal',c.c_int32*5),('treasures',c.c_int32*32),('combos',c.c_int32*32),('orb_stage',c.c_int32),('talents_disabled',c.c_int32),('parameters',c.c_int32*2),('spawned',c.c_int32*2),('spawn_row',c.c_int32*14),('special_castle',c.c_int32)]
INPUTS=['boundary','quiet','game_mode','money_base','accounting_level','score_enabled','notifications','money_disabled','recording','timer','limit','score','cohort_present']
class Death(c.Structure):_fields_=[*[(name,c.c_int32) for name in INPUTS],('cohort_count',c.c_int32),('cohort',c.POINTER(c.c_int32))]
class Result(c.Structure):
    _fields_=[('score_display',c.c_uint64),*[(name,c.c_int32) for name in ['handled','money','selected_bonus_slot','bonus_visual_slot','erase_cohort','cohort_serial','score','score_updated','record_requested']],('record_values',c.c_int32*2),('sound',c.c_int32)]
class DeathNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=DeathNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed={pc for a in [*[int(v,16) for v in manifest['functions'] if int(v,16) in sizes],0x44abfc,0x44abe4,0xa956f8,0xa957d0,0xa9e5e0] for pc in range(a,a+sizes[a],4)}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_actor_last_error.restype=c.c_int64
lib.kbcs_core_actor_enemy_knockback.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.c_int32,c.POINTER(Death),c.POINTER(Result)]
n.cpu.mem_write(0xc1b630,struct.pack('<Q',0xc23fc4));n.entry=0x6eccf4;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={0x6ece44}
def sparse(pool):return [[(s*51+j)*251+i,v] for s,team in enumerate(pool) for j,actor in enumerate(team) for i,v in enumerate(actor.words) if v]
cases=[]
for side,frame,position,hp,resume in itertools.product([0,1],[0,22,23],[199,200,201],[0,1],[0,1,2]):
    cases.append(dict(side=side,frame=frame,position=position,hp=hp,resume=resume))
for side,zombie,revives,killed,wait,percent in itertools.product([0,1],[0,1],[-1,0,1,2],[0,1],[0,17],[0,33,100]):
    cases.append(dict(side=side,zombie=zombie,revives=revives,killed=killed,wait=wait,percent=percent))
for side,shield,current,percent in itertools.product([0,1],[0,1,100],[0,1],[0,33,100]):
    cases.append(dict(side=side,hp=1,shield=shield,current=current,regen=percent))
for side,score,notifications,disabled,recording,mode,cohort in itertools.product([0,1],[0,1],[0,1],[0,1],[0,1],[0,4,7],range(4)):
    cases.append(dict(side=side,score_enabled=score,notifications=notifications,money_disabled=disabled,recording=recording,game_mode=mode,cohort=cohort))
records=[]
for index,case in enumerate(cases):
 side=case['side'];pool=Pool();word=pool[side][1].words
 for i,v in {0:2,1:3,2:case.get('frame',23),3:case.get('position',200),4:4480,7:101,8:case.get('hp',0),10:17,47:case.get('zombie',0),61:7,62:9,63:[0,1,2][index%3],66:11,67:12,75:13,76:14,77:15,103:case.get('revives',0),104:case.get('percent',33),105:case.get('wait',17),114:case.get('killed',0),115:index%2,118:case.get('resume',0),113:123,184:case.get('shield',0),185:case.get('regen',33),190:case.get('current',0),192:2,194:1,196:4,240:88}.items():word[i]=v
 # 同じ生成通番・空き枠・同率の候補も原本どおり走査する。
 for slot,serial,bonus in [(1,11,10),(2,22,30),(3,11,30),(4,0,100)]:
  peer=pool[1-side][slot].words;peer[0]=2 if slot!=4 else 0;peer[240]=serial;peer[241]=7;peer[243]=bonus
 cohort=[[],[11],[22,11,22],[0]][case.get('cohort',index%4)]
 ids=(c.c_int32*len(cohort))(*cohort)
 input=Death(boundary=200,quiet=index%2,game_mode=case.get('game_mode',0),money_base=[0,100,12345,90000000,-100][index%5],accounting_level=[0,20,30][index%3],
  score_enabled=case.get('score_enabled',1),notifications=case.get('notifications',1),money_disabled=case.get('money_disabled',0),recording=case.get('recording',1),
  timer=[0,1800,3601][index%3],limit=[0,1800][index%2],score=[0,999999998,-100][index%3],cohort_present=int(index%5!=0),cohort_count=len(ids),cohort=ids)
 environment=Environment();environment.treasures[5]=[0,100,300][index%3];environment.combos[12]=[0,10,17][index%3]
 before=sparse(pool);actor=game+0x84080+side*0xc804+0x3ec;sp=n.stack+0x8000;fp=sp+0x200;table=game+0x2678+side*0x1f0
 n.cpu.mem_write(game+0x84080,bytes(pool));n.cpu.mem_write(game+0x32e9,bytes([input.quiet]));n.cpu.mem_write(game+0x32ec,struct.pack('<ii',input.score,input.timer));n.cpu.mem_write(game+0x3310,bytes(8));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678))
 n.cpu.mem_write(game+0x239da8+2*0x1c4+0x18,struct.pack('<i',input.money_base));n.cpu.mem_write(sp-0x400,bytes(0x800))
 for offset,value in [(0xb0,n.memory),(0x70,game+0x2678),(0x78,game+0x239da8)]:n.cpu.mem_write(sp+offset,struct.pack('<Q',value))
 node=n.memory+0x1000;vector=n.memory+0x2000;values=n.memory+0x3000
 n.cpu.mem_write(node,bytes(64));n.cpu.mem_write(node+32,struct.pack('<i',88));n.cpu.mem_write(table+0x1e0,struct.pack('<Q',node if input.cohort_present else 0))
 if cohort:n.cpu.mem_write(values,struct.pack('<'+'i'*len(cohort),*cohort))
 n.cpu.mem_write(vector,struct.pack('<QQQ',values,values+len(cohort)*4,values+len(cohort)*4))
 sounds=[];money=[];erased=[];recorded=[];visual=[]
 def sound():sounds.append(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1));return 0
 def reward():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_X0)==game+0x2678
  money.append(c.c_int32(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)).value);return 0
 def erase():
  erased.append(struct.unpack('<i',n.cpu.mem_read(n.cpu.reg_read(n.reg.UC_ARM64_REG_X1),4))[0]);return 0
 def record():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)==1 and n.cpu.reg_read(n.reg.UC_ARM64_REG_W2)==1 and n.cpu.reg_read(n.reg.UC_ARM64_REG_W4)==2
  recorded.append(list(struct.unpack('<ii',n.cpu.mem_read(n.cpu.reg_read(n.reg.UC_ARM64_REG_X3),8))));return 0
 def bonus_visual():visual.append(struct.unpack('<i',n.cpu.mem_read(n.cpu.reg_read(n.reg.UC_ARM64_REG_X1),4))[0]);return 0
 def boundary():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)==side and n.cpu.reg_read(n.reg.UC_ARM64_REG_W2)==1
  n.cpu.mem_write(actor+120,struct.pack('<i',input.boundary));return 0
 def accounting():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_W0)==8
  return input.accounting_level
 def treasure():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)==5
  return environment.treasures[5]
 def combo():
  assert n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)==12
  return environment.combos[12]
 n.helpers={0x81f580:game,0x5bc1dc:1,0x5c2710:0,0xa9490c:boundary,0x457e1c:0,0x459efc:sound,0x459f04:sound,0x5bc058:input.game_mode,
  0x5e1400:input.score_enabled,0x5bbba0:input.limit,0x58b674:accounting,0xa5b084:treasure,0x88f9e4:combo,0x9d49e4:input.notifications,
  0x7cf950:0,0x6440f0:input.money_disabled,0xa0b03c:input.recording,0xa0cfec:record,0x5c2990:reward,0x6ee50c:vector,0x6ef68c:erase,0x6b5d40:bonus_visual,0x41b298:0,0xbdaf60:0}
 for register,value in [('SP',sp),('X29',fp),('W19',side),('X26',1),('X22',game),('X28',actor),('X20',table),('W24',1-side),('D8',1)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
 try:n.cpu.emu_start(0x6ed43c,n.stop+4,count=200000)
 except Exception as error:raise RuntimeError((index,case,hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)))) from error
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'enemy death budget'
 assert struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]==0x12345678
 expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)));output=Result()
 code=lib.kbcs_core_actor_enemy_knockback(pool,c.byref(environment),side,1,c.byref(input),c.byref(output))
 assert code==0,(index,case,code,hex(lib.kbcs_core_actor_last_error()))
 assert output.handled==1 and bytes(pool)==expected,{'case':(index,case),'diff':[(i,a,b) for i,(a,b) in enumerate(zip(struct.unpack('<25602i',bytes(pool)),struct.unpack('<25602i',expected))) if a!=b][:10]}
 score,=struct.unpack('<i',n.cpu.mem_read(game+0x32ec,4));display,=struct.unpack('<Q',n.cpu.mem_read(game+0x3310,8))
 selected=struct.unpack('<i',n.cpu.mem_read(sp+0xc8,4))[0] if word[1]==4 else -1
 assert output.selected_bonus_slot==selected and output.score_updated==int(bool(display)),(index,case,'selection',output.selected_bonus_slot,selected)
 assert (output.sound,output.money,output.erase_cohort,output.cohort_serial,output.score,output.score_display,output.record_requested,list(output.record_values),output.bonus_visual_slot)==(
  sounds[0] if sounds else -1,money[0] if money else 0,int(bool(erased)),erased[0] if erased else -1,score,display,int(bool(recorded)),recorded[0] if recorded else [0,0],visual[0] if visual else -1),(index,case,'events',sounds,money,erased,recorded,visual)
 if index%23==0 or (case.get('revives')==1 and case.get('killed')==0 and case.get('percent')==0):
  records.append({'side':side,'before':before,'after':sparse(pool),'treasures':list(environment.treasures),'combos':list(environment.combos),'cohort':cohort,'input':{k:getattr(input,k) for k in INPUTS},'output':{k:list(getattr(output,k)) if k=='record_values' else getattr(output,k) for k,_ in Result._fields_}})
print(json.dumps({'enemyKnockbackCases':len(cases),'published':len(records)}))
result={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entry':'006ed43c','terminal':'006ece44','records':records,'cases':len(cases),'controlled':['singleton and unit mode/slot lookup','decoded accounting/treasure/combo/scoring inputs','model boundary resolver','native map value lookup/erase with supplied ordered contributor IDs','sound/money/record/bonus display output capture','stack frame locals, register table pointer, enemy data table and D8=SO constant 1','GOT c1b630 relative relocation'],'limits':['enemy action 3 only; recorder/wallet encryption and whole-frame setup outside kernel']}
(ROOT/'research/.local/actor-enemy-death-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-enemy-death-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
