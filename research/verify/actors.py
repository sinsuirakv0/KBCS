"""個体初期化の全フィールドを15.7.2 ARM64とC++へ同時投入して比較する。"""
import argparse
import ctypes as c
import json
import os
from pathlib import Path
import sqlite3
import struct
import sys
from copy import deepcopy

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--library',type=Path,required=True)
parser.add_argument('--assets',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
parser.add_argument('--all-assets',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,Assets,ROOT,SHA,digest

class Definition(c.Structure):
    _fields_=[('cells',c.c_int32*119),('count',c.c_int32),('growth',c.c_int32*20),
              ('talents',(c.c_int32*4)*73),('talent_active',c.c_int32*73),('talent_min_level',c.c_int32*73),
              ('added_targets',c.c_int32),('orb_enabled',c.c_int32),('orbs',(c.c_int32*4)*32),('orb_present',c.c_int32*32),
              ('speed_rule',c.c_int32),('speed_value',c.c_int32)]
class Environment(c.Structure):
    _fields_=[('unit_modes',c.c_int32*2),*[(name,c.c_int32) for name in ['stage_width','castle_slot','castle_x','castle_scale','castle_offset','stage_kind','zombie','chapter_rate','crown','hp_percent','attack_percent']],
              ('crystal_max',c.c_int32*5),('crystal',c.c_int32*5),('treasures',c.c_int32*32),('combos',c.c_int32*32),
              ('orb_stage',c.c_int32),('talents_disabled',c.c_int32),('parameters',c.c_int32*2),('spawned',c.c_int32*2),('spawn_row',c.c_int32*14),('special_castle',c.c_int32)]
class Request(c.Structure):
    _fields_=[(name,c.c_int32) for name in ['side','raw','level_index','layer_min','layer_max','form','row']]
class Actor(c.Structure):
    _fields_=[('words',c.c_int32*251)]
Pool=(Actor*51)*2
class EffectContext(c.Structure):
    _fields_=[('fruit',c.c_int32),('base_reductions',c.c_int32*4),('sage',c.c_int32*11),('notifications',c.c_int32),('target_count',c.c_int32),('scenario_level',c.c_int32)]
class EffectEvents(c.Structure):
    _fields_=[('count',c.c_int32),('events',(c.c_int32*2)*16)]
class Clock(c.Structure):
    _fields_=[('encoded',c.c_int32*4),('plain',c.c_int32*4),('forms',(c.c_int32*51)*2),('kill_orb',c.c_int32*51),('kill_threshold',c.c_int32)]
class Motion(c.Structure):
    _fields_=[('encoded',c.c_int32*8),('plain',c.c_int32*8),('soul_frames',c.c_int32)]
class StageRow(c.Structure):
    _fields_=[('cells',c.c_int32*14)]
class StageState(c.Structure):
    _fields_=[('wait',c.c_int32),('spawned',c.c_int32),('kills',c.c_int32)]
class DamageContext(c.Structure):
    _fields_=[('guard_enabled',c.c_int32),('notice',c.c_int32*2),('rows',c.POINTER(StageRow)),('states',c.POINTER(StageState)),('count',c.c_int32)]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()))
lib.kbcs_core_actor_initialize.argtypes=[c.POINTER(Definition),c.POINTER(Environment),c.POINTER(Actor*51),c.POINTER(Request),c.POINTER(c.c_uint32),c.POINTER(c.c_int32)]
lib.kbcs_core_actor_load.argtypes=[c.POINTER(c.c_int32),c.c_int32,c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_core_actor_last_error.restype=c.c_int64
lib.kbcs_core_actor_roll.argtypes=[c.POINTER(Actor*51),c.c_int32,c.c_int32,c.c_int32,c.POINTER(c.c_uint32),c.POINTER(c.c_int32)]
lib.kbcs_core_actor_contact.argtypes=[c.POINTER(Actor*51),c.c_int32,c.c_int32,c.c_int32,c.c_int32,c.c_int32,c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_core_actor_effects.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.POINTER(EffectContext),c.c_int32,c.c_int32,c.c_int32,c.POINTER(c.c_int32),c.POINTER(c.c_uint32),c.POINTER(EffectEvents)]
lib.kbcs_core_actor_clock.argtypes=[c.POINTER(Actor*51),c.POINTER(Clock)]
lib.kbcs_core_actor_matches.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.c_int32,c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_core_actor_motion.argtypes=[c.POINTER(Actor*51),c.c_int32,c.c_int32,c.POINTER(Motion)]
lib.kbcs_core_actor_begin.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.c_int32]
lib.kbcs_core_actor_transition.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.c_int32,c.POINTER(Motion),c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_core_actor_resume.argtypes=[c.POINTER(Actor*51),c.c_int32,c.c_int32]
lib.kbcs_core_actor_damage.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.POINTER(DamageContext),c.c_int32,c.c_int32,c.c_int32]
manifest=json.loads((ROOT/'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))

class ActorNative(Native):
    def call(self,entry,*args):
        self.entry=entry
        for index in range(8):self.cpu.reg_write(getattr(self.reg,'UC_ARM64_REG_X'+str(index)),(args[index] if index<len(args) else 0)&0xffffffffffffffff)
        self.cpu.reg_write(self.reg.UC_ARM64_REG_SP,self.stack+0x8000)
        for index,value in enumerate(args[8:]):self.cpu.mem_write(self.stack+0x8000+index*8,struct.pack('<Q',value&0xffffffffffffffff))
        self.cpu.reg_write(self.reg.UC_ARM64_REG_LR,self.stop)
        self.cpu.emu_start(entry,self.stop+4,count=500000)
        assert self.cpu.reg_read(self.reg.UC_ARM64_REG_PC)==self.stop,'instruction budget'
        return signed(self.value(0))
    def hook(self,cpu,address,size,data):
        self.coverage.add(address)
        self.trace.append(address);self.trace[:]=self.trace[-12:]
        if address==0xa95738:self.last_argument=self.value(2)
        if address in self.helpers:return super().hook(cpu,address,size,data)
        if address in self.allowed_pc:return
        try:return super().hook(cpu,address,size,data)
        except RuntimeError as error:raise RuntimeError(str(error)+' trace='+str([hex(v) for v in self.trace]))
    def value(self,index):return self.cpu.reg_read(getattr(self.reg,'UC_ARM64_REG_X'+str(index)))&0xffffffff

n=ActorNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
    names=db.execute("SELECT address,name FROM functions WHERE address NOT LIKE 'EXTERNAL:%'").fetchall()
allowed={int(a,16) for a in manifest['functions'] if int(a,16) in sizes}|{0x5c2710,0xa9e9fc,0xa9fb88,0xa9f9fc,0xaa68ec,0xa06cb0,0xa06cb8,0xa92ea0,0xa9482c,0x44a8d8,0x44a8e8}
n.allowed=[(a,a+sizes[a]) for a in allowed]
n.allowed_pc={pc for a,b in n.allowed for pc in range(a,b,4)}
n.ends.update({a:a+sizes[a] for a in allowed})
# 章倍率表のGOT参照だけを同版のrela addendから復元する。
from elftools.elf.elffile import ELFFile
identity=json.loads((n.cache/'identity.json').read_text(encoding='utf-8-sig'))
with Path(identity['binary']).open('rb') as stream:
    for section in ELFFile(stream).iter_sections():
        if hasattr(section,'iter_relocations'):
            for relocation in section.iter_relocations():
                if relocation['r_offset']+0x100000==0xc1b770:n.cpu.mem_write(0xc1b770,struct.pack('<Q',relocation['r_addend']+0x100000))

def signed(v):return v-0x100000000 if v&0x80000000 else v

def execute(definition,environment,request,pool,entry=0x9f1e64,argument=1):
    n.cpu.mem_write(game,bytes(0x500000));n.cpu.mem_write(game+0x84080,bytes(pool))
    raw=request.raw;form=request.form;side=request.side
    for index in range(2):n.cpu.mem_write(game+0x2678+index*0x1f0,struct.pack('<i',environment.unit_modes[index]))
    base=game+(0x9ee88+raw*0x770+form*0x1dc if environment.unit_modes[side] else 0x239da8+raw*0x1c4)
    n.cpu.mem_write(base,bytes(definition.cells))
    n.cpu.mem_write(game+0x44fcc4+(raw-2)*0x50,bytes(definition.growth))
    n.cpu.mem_write(game+0x32f934,struct.pack('<i',environment.stage_kind))
    n.cpu.mem_write(game+0x334048,bytes([environment.zombie]))
    n.cpu.mem_write(game+0x9ee48,struct.pack('<i',environment.stage_width))
    n.cpu.mem_write(game+0x9ee60,struct.pack('<i',environment.special_castle))
    n.cpu.mem_write(game+0x284c,struct.pack('<i',environment.spawned[0]));n.cpu.mem_write(game+0x2a3c,struct.pack('<i',environment.spawned[1]))
    n.cpu.mem_write(game+0x9ee70,struct.pack('<Q',n.memory+0x2000))
    row=list(environment.spawn_row);row[9]=environment.hp_percent;row[11]=environment.attack_percent
    n.cpu.mem_write(n.memory+0x2000+request.row*0x38,struct.pack('<14i',*row))
    n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678))
    n.cpu.mem_write(n.memory+0x7000,struct.pack('<QQ',n.memory+0x7020,n.memory+0x7030))
    n.cpu.mem_write(n.memory+0x7020,struct.pack('<4i',definition.speed_rule,definition.speed_value,definition.speed_rule,definition.speed_value))
    def active(effect):return environment.unit_modes[side] and form>=2 and not environment.talents_disabled and definition.talent_active[effect] and request.level_index+1>=definition.talent_min_level[effect]
    def talent():
        effect=n.value(3);parameter=n.value(4)
        return definition.talents[effect][parameter] if active(effect) else 0
    def castle_setting():n.cpu.reg_write(n.reg.UC_ARM64_REG_W1,environment.castle_scale);return environment.castle_offset
    heap=n.memory+0x8000
    def allocate():
        nonlocal heap
        out=heap;heap+=(n.value(0)+15)//16*16;return out
    crystals={16:0,18:1,22:2,23:3,24:4}
    n.helpers={0x81f580:game,0x5bbc10:environment.castle_slot,0x5bbbc8:int(environment.special_castle>0),
               0x5c2ec0:int(side==0 and form>=2 and definition.orb_enabled),
               0x66398c:lambda:definition.orbs[n.value(2)][n.value(3)],0x663af4:lambda:definition.orbs[n.value(2)][n.value(3)],
               0x66367c:lambda:definition.orb_present[n.value(2)],
               0xa9f0e0:talent,0xaa2c2c:lambda:int(active(n.value(3))),
               0xaa4fb0:lambda:int(form>=2 and not environment.talents_disabled and definition.added_targets&n.value(3)!=0),
               0x88f9e4:lambda:environment.combos[n.value(1)],
               0xa5b084:lambda:environment.crystal[crystals[n.value(1)]] if n.value(1) in crystals else environment.treasures[n.value(1)],
               0xa5b2d8:lambda:environment.crystal_max[crystals[n.value(1)]],
               0x7cf4b0:0 if environment.orb_stage==9 else -9 if environment.orb_stage==16 else 1,
               0x78aefc:0,0x78af80:0,0x7bd9d0:0,
               0x7cf950:0,0x7cfcd8:0,0x7cebc8:environment.crown,
               0x644304:lambda:n.memory+0x7000 if definition.speed_rule and n.value(2)==10 else 0,
               0x44abe4:lambda:max(signed(n.value(0)),signed(n.value(1))),
               0x656de0:castle_setting,0x5bbfb0:0,
               0x457e1c:0,0x459efc:0,0x9019f4:lambda:environment.parameters[0 if n.value(2)==600 else 1]}
    for address,name in names:
        if 'operator.new' in name:n.helpers[int(address,16)]=allocate
        if 'operator.delete' in name:n.helpers[int(address,16)]=0
    n.trace=[];n.last_argument=None
    if entry==0x9f1e64:
        value=n.call(entry,game,side,raw,request.level_index,request.layer_min,request.layer_max,form,request.row)
        result=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(Pool)))
        state=struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]
        counters=struct.unpack('<i',n.cpu.mem_read(game+0x284c,4))[0],struct.unpack('<i',n.cpu.mem_read(game+0x2a3c,4))[0]
        return value,result,state,n.last_argument,counters
    value=n.call(entry,side,raw-2,form,argument)
    return value

assets=Assets(args.assets)
def make(unit,row,raw=2,form=2):
    d=Definition();d.count=min(len(row),119 if unit else 113)
    values=(c.c_int32*len(row))(*row)
    assert lib.kbcs_core_actor_load(values,len(row),int(unit),d.cells)==0
    for i in range(20):d.growth[i]=20 if i<3 else 10
    e=Environment();e.unit_modes[:]=[1,0];e.stage_width=24000;e.castle_slot=-1;e.castle_x=3200;e.castle_scale=127
    e.stage_kind=3;e.crown=100;e.hp_percent=e.attack_percent=100;e.parameters[:]=[600,4000]
    e.spawn_row[9]=100
    r=Request(0 if unit else 1,raw,29,0,9,form,0)
    pool=Pool();pool[1][0].words[3]=3200
    return d,e,r,pool

unitrows=assets.numeric('Data/unit001.csv')
enemyrows=assets.numeric('Data/t_unit.csv')
cases=[]
for unit,row,name in [(True,unitrows[2]['cells'],'cat'),(False,enemyrows[2]['cells'],'dog')]:
    values=[v or 0 for v in row]
    d,e,r,pool=make(unit,values)
    cases.append((name,d,e,r,pool))

# 各列の単独設定、全本能、玉の上書き、形態・Lv境界、特殊な敵城と枠探索。
for column in range(10,119):
    d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']])
    d.cells[column]=1
    cases.append(('unit-column-'+str(column),d,e,r,pool))
for column in range(10,113):
    d,e,r,pool=make(False,[v or 0 for v in enemyrows[2]['cells']])
    d.cells[column]=1
    cases.append(('enemy-column-'+str(column),d,e,r,pool))
for form,level in [(0,59),(1,59),(2,58),(2,59),(3,59)]:
    d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']],form=form)
    r.level_index=level
    for effect in range(73):
        d.talent_active[effect]=1
        d.talent_min_level[effect]=60 if effect>=70 else 0
        d.talents[effect][:]=[13,17,23,29]
    d.added_targets=0xfff
    cases.append(('talents-'+str(form)+'-'+str(level),d,e,r,pool))
for probability in [0,50,100]:
    d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']])
    d.orb_enabled=1
    for effect in range(32):d.orbs[effect][:]=[probability,probability,probability,probability];d.orb_present[effect]=1
    cases.append(('orbs-'+str(probability),d,e,r,pool))
for boss in [0,1,2]:
    d,e,r,pool=make(False,[v or 0 for v in enemyrows[2]['cells']])
    e.castle_slot=1;e.spawn_row[8]=boss;e.spawn_row[12]=7;e.castle_offset=13;e.castle_scale=90
    cases.append(('castle-'+str(boss),d,e,r,pool))
for star in range(5):
    d,e,r,pool=make(False,[v or 0 for v in enemyrows[2]['cells']])
    d.cells[18]=1;d.cells[69]=star;d.cells[87]=101
    e.hp_percent=125;e.attack_percent=0;e.crown=170
    e.crystal_max[:]=[600,1500,1000,1000,1000];e.crystal[:]=[397,999,333,1000,0]
    cases.append(('crystal-'+str(star),d,e,r,pool))
for chapter in range(3):
    d,e,r,pool=make(False,[v or 0 for v in enemyrows[2]['cells']])
    e.stage_kind=chapter;e.chapter_rate=[0,5,30][chapter];d.cells[87]=101
    cases.append(('chapter-'+str(chapter),d,e,r,pool))
for free in [0,50]:
    d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']])
    for i in range(1,51):pool[0][i].words[0]=0 if i==free else 2
    cases.append(('free-'+str(free),d,e,r,pool))
d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);r.raw=-1
cases.append(('invalid-raw',d,e,r,pool))

for serial in [1,17,2147483646]:
    d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);e.spawned[0]=serial
    cases.append(('serial-'+str(serial),d,e,r,pool))
for rule,value in [(1,0),(1,17),(2,31),(2,200)]:
    d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);d.speed_rule=rule;d.speed_value=value
    # 00a9f9fcの特殊ルールgetterも同じ指定で実命令に渡す。
    cases.append(('speed-'+str(rule)+'-'+str(value),d,e,r,pool))
for stage in [9,16]:
    d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);e.orb_stage=stage;d.orbs[stage][:]=[13,27,0,0]
    cases.append(('stage-orbs-'+str(stage),d,e,r,pool))
for disabled in [0,1]:
    d,e,r,pool=deepcopy(next(v[1:] for v in cases if v[0]=='talents-3-59'));e.talents_disabled=disabled
    cases.append(('talents-disabled-'+str(disabled),d,e,r,pool))
d,e,r,pool=make(True,[0]*119);pool[0][1].words[:]=[12345]*251;pool[0][1].words[0]=0
cases.append(('reuse-zero-hp',d,e,r,pool))
if args.all_assets:
    import re
    for path in sorted(assets.files):
        if re.fullmatch(r'Data/unit\d+\.csv',path):
            for form,row in enumerate(assets.numeric(path)[:4]):
                d,e,r,pool=make(True,[v or 0 for v in row['cells']],form=form)
                cases.append((path+'#'+str(form),d,e,r,pool))
    for index,row in enumerate(enemyrows[2:]):
        d,e,r,pool=make(False,[v or 0 for v in row['cells']])
        cases.append(('enemy-'+str(index),d,e,r,pool))

def pod(value):
    if isinstance(value,c.Array):return [pod(v) for v in value]
    if isinstance(value,c.Structure):return {name:pod(getattr(value,name)) for name,_ in value._fields_}
    return value

records=[]
n.coverage=set()
published=[]
for name,d,e,r,pool in cases:
    before=(pod(d),pod(e),pod(r),[[[i,w] for i,w in enumerate(a.words) if w] for side in pool for a in side])
    native=execute(d,e,r,pool)
    out=c.c_int32(-99);seed=c.c_uint32(0x12345678)
    code=lib.kbcs_core_actor_initialize(c.byref(d),c.byref(e),pool,c.byref(r),c.byref(seed),c.byref(out))
    assert code==0,(name,'C++ error',code,hex(lib.kbcs_core_actor_last_error()))
    differences=[(i,a,b) for i,(a,b) in enumerate(zip(struct.unpack('<'+str(c.sizeof(Pool)//4)+'i',native[1]),struct.unpack('<'+str(c.sizeof(Pool)//4)+'i',bytes(pool)))) if a!=b]
    assert not differences,(name,'fields',differences[:30],native[3])
    assert (out.value,seed.value)==(native[0],native[2]),(name,out.value,seed.value,native[0],native[2])
    assert tuple(e.spawned)==native[4],(name,'generation serial')
    records.append({'name':name,'slot':out.value,'seed':seed.value,'words':list(pool[r.side][out.value].words) if out.value>0 else None})
    if len(records)%250==0:print(json.dumps({'checked':len(records),'total':len(cases)}),flush=True)
    if name in ['cat','dog','talents-2-59','orbs-100','castle-2','crystal-2','serial-17','reuse-zero-hp','free-0','invalid-raw']:
        published.append(dict(name=name,definition=before[0],environment=before[1],request=before[2],pool=before[3],output=records[-1],spawned=list(e.spawned)))
print(json.dumps({'cases':len(records),'wordsPerCase':251,'names':[v['name'] for v in records][-20:]}))
actions=[]
for hit in range(3):
    for enabled in [0,1]:
        for probability in [0,1,50,99,100]:
            d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']])
            record=pool[0][1].words
            # 006e9c88の12確率getterの領域と、段別の効果フラグ。
            for word in [56,49,50,52,68,163,135,132,147,171,183,246]:record[word]=probability
            for word in [123,124,125]:record[word]=enabled
            execute(d,e,r,pool)
            n.cpu.mem_write(game+0x84080,bytes(pool));n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678))
            n.cpu.mem_write(game+0x38fb8c,struct.pack('<12i',*([123]*12)))
            n.call(0x6e9c88,game,0,1,hit)
            expected=list(struct.unpack('<12i',n.cpu.mem_read(game+0x38fb8c,48)))
            state=struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0]
            seed=c.c_uint32(0x12345678);flags=(c.c_int32*12)(*([123]*12))
            assert lib.kbcs_core_actor_roll(pool,0,1,hit,c.byref(seed),flags)==0
            assert (list(flags),seed.value)==(expected,state),(hit,enabled,probability,list(flags),expected)
            actions.append(dict(kind='roll',side=0,hit=hit,enabled=enabled,probability=probability,seed=state,flags=expected))
for side in [0,1]:
    for action in [0,1,2,3,4,11,13,14,15,16]:
        for distance in [-501,-500,-499,0,499,500,501]:
            d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);r.side=side
            a=pool[side][1].words;b=pool[1-side][1].words
            a[0]=b[0]=2;a[1]=2;b[1]=action;a[3]=10000;b[3]=10000+distance
            a[13]=500;b[14]=200;b[15]=-100
            execute(d,e,r,pool)
            n.cpu.mem_write(game+0x84080,bytes(pool))
            expected=n.call(0x6dda04,game,side,1,1,0)
            output=c.c_int32(-99)
            assert lib.kbcs_core_actor_contact(pool,side,1,1,0,-1,0,c.byref(output))==0
            assert output.value==expected,(side,action,distance,output.value,expected)
            actions.append(dict(kind='contact',side=side,action=action,distance=distance,output=expected))
print(json.dumps({'actions':len(actions)}))
for hit in range(3):
    for distance in [-601,-200,0,199,200,600,601]:
        for target in [0,1]:
            d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']])
            a=pool[0][1].words;b=pool[1][target].words
            a[0]=b[0]=2;a[1]=b[1]=2;a[3]=10000;b[3]=10000+distance;a[13]=500
            for word,value in [(84,200),(85,400),(199,-200),(200,200),(201,600),(202,-600),(203,20),(204,30)]:a[word]=value
            execute(d,e,r,pool);n.cpu.mem_write(game+0x84080,bytes(pool))
            expected=n.call(0x6dda04,game,0,1,target,hit);out=c.c_int32()
            assert lib.kbcs_core_actor_contact(pool,0,1,target,hit,-1,0,c.byref(out))==0
            assert out.value==expected,('far',hit,distance,target,out.value,expected)
            actions.append(dict(kind='far',hit=hit,distance=distance,target=target,output=expected))
for side in [0,1]:
    for field in [16,41,42,43,44,45,46,47,109,144,146,194]:
        for cursed in [0,1,2,3]:
            for target_traits in [0,1]:
                d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);r.side=side
                a=pool[side][1].words;b=pool[1-side][1].words;a[field]=1
                a[150]=cursed&1;a[151]=int(bool(cursed&2))
                for word in [17,41,42,43,44,45,46,47,109,144,146,194]:b[word]=target_traits
                execute(d,e,r,pool);n.cpu.mem_write(game+0x84080,bytes(pool))
                expected=n.call(0xa962a8,side,1,1);out=c.c_int32()
                assert lib.kbcs_core_actor_matches(pool,c.byref(e),side,1,1,c.byref(out))==0
                assert out.value==expected,('matches',side,field,cursed,target_traits,out.value,expected)
                actions.append(dict(kind='matches',side=side,field=field,cursed=cursed,target_traits=target_traits,output=expected))
print(json.dumps({'contactAndMatches':len(actions)}))
immune_words=[88,89,90,91,143,149,249]
effect_conditions=['plain','immune','resist-99','resist-100','sage','hunter','both-sage','decoration','combo','fruit','notifications','warp-equal','warp-reverse']
for side in [0,1]:
    for flags_value in [0,1,2,4,8,16,32,64,127]:
        for condition in effect_conditions:
            d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);r.side=side
            a=pool[side][1].words;b=pool[1-side][1].words
            a[0]=b[0]=2;a[1]=b[1]=2
            for word,value in [(51,101),(53,103),(69,107),(70,20),(136,47),(137,21),(138,101),(148,109),(247,113)]:a[word]=value
            if condition=='warp-equal':a[137]=a[138]=21
            if condition=='warp-reverse':a[137]=101;a[138]=21
            context=EffectContext();context.target_count=3;context.scenario_level=1;context.sage[:]=[50,51,52,53,54,55,56,57,70,58,59]
            if condition=='immune':
                for word in immune_words:b[word]=1
            if condition.startswith('resist-'):
                for word in [153,154,155,159]:b[word]=int(condition.split('-')[1])
            if condition in ['sage','both-sage']:a[215]=b[215]=1
            if condition in ['hunter','both-sage']:a[216]=b[216]=1
            if condition=='decoration':context.base_reductions[:]=[1111,2222,3333,4444]
            if condition=='combo':e.combos[17]=13;e.combos[18]=17;e.combos[19]=19
            if condition=='fruit':context.fruit=173
            if condition=='notifications':context.notifications=1
            flags=[int(bool(flags_value&(1<<i))) for i in range(7)]
            before=bytes(pool);execute(d,e,r,pool);n.cpu.mem_write(game+0x84080,before);n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678))
            n.cpu.mem_write(game+0x4dc,struct.pack('<i',-1))
            events=[]
            def notify():events.append([signed(n.value(1)),signed(n.value(2))]);return len(events)
            def parameter():
                address=n.value(1);head=n.cpu.mem_read(address,24)
                data=struct.unpack_from('<Q',head,16)[0] if head[0]&1 else address+1
                key=bytes(n.cpu.mem_read(data,100)).split(b'\0')[0].decode('ascii')
                return context.sage[manifest['effectParameters'].index(key)]
            n.helpers.update({0x63c178:0,0x68c330:context.scenario_level-1,0x8cfcf0:0,0x63c480:0,
                              0x63a050:lambda:context.base_reductions[(n.value(1)-200)//2],0xa5b1b4:context.fruit,
                              0x5bc198:context.notifications,0x9d49e4:context.notifications,0xa960ac:context.target_count,
                              0x9d4e1c:notify,0x9019f4:parameter})
            n.call(0x6e62f8,game,side,1,1,0,*flags)
            expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(Pool)))
            seed=c.c_uint32(0x12345678);output=EffectEvents();code=lib.kbcs_core_actor_effects(pool,c.byref(e),c.byref(context),side,1,1,(c.c_int32*7)(*flags),c.byref(seed),c.byref(output))
            assert code==0,(side,flags_value,condition,code,hex(lib.kbcs_core_actor_last_error()))
            diff=[(i,x,y) for i,(x,y) in enumerate(zip(struct.unpack('<25602i',expected),struct.unpack('<25602i',bytes(pool)))) if x!=y]
            assert not diff,(side,flags_value,condition,diff[:20])
            assert [list(v) for v in output.events[:output.count]]==events
            assert seed.value==struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0],(side,flags_value,condition,'RNG')
            if condition in ['plain','immune','both-sage','decoration','notifications','warp-equal','warp-reverse'] and flags_value in [1,2,4,8,16,32,64,127]:
                def sparse(data):return [[i,v] for i,v in enumerate(struct.unpack('<25602i',data)) if v]
                actions.append(dict(kind='effects',side=side,flags=flags,context=pod(context),environment=pod(e),before=sparse(before),after=sparse(expected),seed=seed.value,events=events))
print(json.dumps({'effectCases':2*9*len(effect_conditions),'allActions':len(actions)}))
clocks=[]
for timer in [0,1,2,5]:
    for fallback in [0,1]:
        d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);clock=Clock()
        clock.encoded[:]=[-1 if fallback else 3,4,5,6];clock.plain[:]=[4,5,6,7];clock.kill_threshold=15
        for side in [0,1]:
            record=pool[side][1].words;record[0]=2;record[7]=101;record[8]=37;record[71]=37;record[241]=15
            for word in [167,210,234,61,62,75,150]:record[word]=timer
            for word in [77,93,95,102,63]:record[word]=1
            for word,value in zip([81,82,83,152,170],[1,2,3,4,5]):record[word]=value
            clock.forms[side][1]=2;clock.kill_orb[1]=1
        before=bytes(pool);execute(d,e,r,pool);n.cpu.mem_write(game+0x84080,before)
        offsets=[0x1de8,0x1988,0x1a68,0x2168]
        n.helpers.update({0x44beb4:lambda:clock.encoded[offsets.index(n.value(0)-0x2000a000)],
                          0x44bf2c:lambda:clock.plain[offsets.index(n.value(0)-0x2000a000)],
                          0x5bc1dc:lambda:n.value(1),0x5bce20:lambda:clock.forms[n.value(0)][n.value(1)],
                          0x66367c:lambda:clock.kill_orb[1],0x9019f4:clock.kill_threshold})
        steps=[]
        for frame in range(6):
            n.call(0x5ce03c,game,0x2000a000)
            expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(Pool)))
            code=lib.kbcs_core_actor_clock(pool,c.byref(clock))
            assert code==0,('clock',timer,fallback,frame,code,hex(lib.kbcs_core_actor_last_error()))
            diff=[(i,x,y) for i,(x,y) in enumerate(zip(struct.unpack('<25602i',expected),struct.unpack('<25602i',bytes(pool)))) if x!=y]
            assert not diff,('clock',timer,fallback,frame,diff[:20])
            steps.append([[i,v] for i,v in enumerate(struct.unpack('<25602i',expected)) if v])
        clocks.append(dict(timer=timer,fallback=fallback,clock=pod(clock),before=[[i,v] for i,v in enumerate(struct.unpack('<25602i',before)) if v],steps=steps))
print(json.dumps({'clocks':len(clocks),'steps':6*len(clocks)}))
motions=[];resumes=[];transitions=[]
for side in [0,1]:
    d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);execute(d,e,r,pool)
    motion=Motion();motion.plain[:]=[8]*8;motion.soul_frames=9
    model=n.memory+0xe000;soul=n.memory+0xe100
    n.helpers.update({0x5bc1dc:1,0x5bde34:lambda:model+n.value(3)*8,
                      0x44beb4:lambda:motion.soul_frames if n.value(0)==soul+0x28 else motion.encoded[(n.value(0)-model)//8],
                      0x44bf2c:lambda:motion.plain[(n.value(0)-model)//8],0x65c134:soul})
    for action in range(22):
        for frame in [0,1,4,23,47,2147483647]:
            for length in [5,-1,0]:
                for special in [0,1]:
                    pool=Pool();record=pool[side][1].words;record[0]=2;record[1]=action;record[2]=frame;record[126]=3 if special else -1;record[128]=special
                    motion.encoded[:]=[length]*8;n.cpu.mem_write(game+0x84080,bytes(pool))
                    n.call(0x9f4688,game,n.memory,side,1)
                    expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(Pool)))
                    code=lib.kbcs_core_actor_motion(pool,side,1,c.byref(motion))
                    assert code==0,('motion',side,action,frame,length,special,code)
                    assert bytes(pool)==expected,('motion',side,action,frame,length,special,record[2],struct.unpack_from('<i',expected,(side*51+1)*1004+8)[0])
                    motions.append(dict(side=side,action=action,frame=frame,length=length,special=special,output=record[2]))
        for speed in [0,1]:
            for mode in [0,1,2]:
                pool=Pool();record=pool[side][1].words;record[0]=2;record[1]=action;record[2]=17;record[10]=speed;record[118]=mode
                n.cpu.mem_write(game+0x84080,bytes(pool));n.call(0x6ec9f4,0,side,1)
                expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(Pool)))
                assert lib.kbcs_core_actor_resume(pool,side,1)==0
                assert bytes(pool)==expected,('resume',side,action,speed,mode)
                resumes.append(dict(side=side,action=action,speed=speed,mode=mode,output=[record[1],record[2],record[10]]))
    for action in [0,10,18,19,20]:
        for frame in [0,4,19,20,29,30]:
            for remaining in [0,1]:
                for position in [199,200,201]:
                    for mode in [0,1]:
                        pool=Pool();record=pool[side][1].words
                        for word,value in {0:2,1:action,2:frame,3:position,30:123,126:-1,139:remaining,142:123}.items():record[word]=value
                        before=list(record);motion.encoded[:]=[5]*8;e.unit_modes[side]=mode
                        n.cpu.mem_write(game+0x84080,bytes(pool));sounds=[]
                        def boundary():
                            assert n.value(1)==side and n.value(2)==1,('boundary arguments',side,n.value(1),n.value(2))
                            n.cpu.mem_write(game+0x840f8+side*0xc804+0x3ec,struct.pack('<i',200));return 0
                        def sound():sounds.append(n.value(1));return 0
                        n.helpers.update({0xa9490c:boundary,0x459f04:sound,0x5c2710:lambda:e.unit_modes[(n.value(0)-game-0x2678)//0x1f0]})
                        n.call(0x6ecae4,game,n.memory,side,1)
                        expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(Pool)));output=c.c_int32()
                        code=lib.kbcs_core_actor_transition(pool,c.byref(e),side,1,c.byref(motion),200,c.byref(output))
                        assert code==0 and bytes(pool)==expected,('transition',side,action,frame,remaining,position,mode,code)
                        assert output.value==(sounds[0] if sounds else -1)
                        transitions.append(dict(side=side,mode=mode,before=before,after=list(record),sound=output.value))
print(json.dumps({'motions':len(motions),'resumes':len(resumes)}))
print(json.dumps({'transitions':len(transitions)}))
begins=[]
for side in [0,1]:
    for mode in [0,1,2,3]:
        for slot in [0,1]:
            for raw in [0,1,2]:
                for value in [-1,0,1,3]:
                    pool=Pool();record=pool[side][slot].words;record[:]=[value]*251;record[0]=raw;before=list(record)
                    environment=Environment();environment.unit_modes[side]=mode
                    n.cpu.mem_write(game+0x84080,bytes(pool));sp=n.stack+0x8000;fp=n.stack+0x7000
                    if mode&1:
                        entry=0x6eb6b0;n.entry=0x6eb464;n.terminals={0x6eb7a0 if slot==0 else 0x6eb7d8,0x6eb6a4}
                        n.cpu.mem_write(fp-0x78,struct.pack('<Q',game+0x84080))
                        registers=[('W20',side),('X23',slot),('W26',side),('X29',fp)]
                    else:
                        entry=0x6ece50;n.entry=0x6eccf4;n.terminals={0x6ecf64 if slot==0 else 0x6ecf90,0x6ece44}
                        n.cpu.mem_write(sp+0xb8,struct.pack('<QQ',game+0x84080,side));registers=[('W19',side),('X26',slot)]
                    n.ends[n.entry]=n.entry+sizes[n.entry]
                    n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,sp)
                    for register,argument in registers:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),argument)
                    n.cpu.emu_start(entry,n.stop+4,count=100000)
                    assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'begin budget'
                    expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(Pool)))
                    assert lib.kbcs_core_actor_begin(pool,c.byref(environment),side,slot)==0
                    assert bytes(pool)==expected,('begin',side,mode,slot,raw,value)
                    begins.append(dict(side=side,mode=mode,slot=slot,before=before,after=list(record)))
n.terminals=set()
print(json.dumps({'begins':len(begins)}))
damages=[]
for side in [0,1]:
    for amounts in [[0],[99],[100],[101],[60,60],[2147483647,1]]:
        for barrier_flag in [0,1,2]:
            d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);record=pool[side][1].words
            record[0]=2;record[130]=100;record[131]=barrier_flag
            before=bytes(pool);execute(d,e,r,pool);n.cpu.mem_write(game+0x84080,before)
            context=DamageContext();output=[]
            for amount in amounts:
                n.call(0xa9bbac,side,1,amount)
                expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(Pool)))
                assert lib.kbcs_core_actor_damage(pool,c.byref(e),c.byref(context),side,1,amount)==0
                assert bytes(pool)==expected,('damage',side,amounts,barrier_flag)
                output.append([record[19],record[112],record[130],record[131],record[162]])
            damages.append(dict(kind='barrier',side=side,amounts=amounts,barrier_flag=barrier_flag,output=output))
for special in [0,1]:
    for condition in ['disabled','no-rows','unspawned','spawned','unlimited','threshold-below','threshold-equal','threshold-above','boss-alive','boss-soul','notice-active']:
        d,e,r,pool=make(True,[v or 0 for v in unitrows[2]['cells']]);e.special_castle=special;e.castle_slot=2
        slot=2 if special else 0;record=pool[1][slot].words;record[0]=2;record[7]=record[8]=100
        pool[1][0].words[7]=pool[1][0].words[8]=100
        rows=(StageRow*1)();states=(StageState*1)();rows[0].cells[1]=1;rows[0].cells[5]=100;rows[0].cells[8]=1
        context=DamageContext();context.rows=rows;context.states=states;context.count=1;context.guard_enabled=int(condition!='disabled')
        if condition=='no-rows':context.count=0
        if condition=='spawned':states[0].spawned=1
        if condition=='unlimited':rows[0].cells[1]=0
        if condition.startswith('threshold-'):
            rows[0].cells[5]=50;pool[1][0].words[8]={'threshold-below':49,'threshold-equal':50,'threshold-above':51}[condition]
        if condition.startswith('boss-'):
            context.count=0;pool[1][3].words[0]=2;pool[1][3].words[64]=1;pool[1][3].words[1]=4 if condition=='boss-soul' else 0
        if condition=='notice-active':context.notice[:]=[1,7]
        before=bytes(pool);initial_notice=list(context.notice);execute(d,e,r,pool);n.cpu.mem_write(game+0x84080,before)
        n.cpu.mem_write(game+0x9ee68,struct.pack('<i',context.guard_enabled))
        n.cpu.mem_write(game+0x9ee78,struct.pack('<Q',n.memory+0x2000+context.count*56))
        n.cpu.mem_write(n.memory+0x2000,bytes(rows));n.cpu.mem_write(n.memory+0x6000,bytes(states))
        n.cpu.mem_write(game+0x84050,struct.pack('<Q',n.memory+0x6000));n.cpu.mem_write(game+0x898,bytes(context.notice))
        n.call(0xa9bbac,1,slot,101)
        expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(Pool)));notice=list(struct.unpack('<2i',n.cpu.mem_read(game+0x898,8)))
        code=lib.kbcs_core_actor_damage(pool,c.byref(e),c.byref(context),1,slot,101)
        assert code==0,('castle',special,condition,code,hex(lib.kbcs_core_actor_last_error()))
        assert bytes(pool)==expected and list(context.notice)==notice,('castle',special,condition,list(context.notice),notice)
        damages.append(dict(kind='castle',special=special,condition=condition,before=[[i,v] for i,v in enumerate(struct.unpack('<25602i',before)) if v],rows=[list(rows[0].cells)][:context.count],states=[pod(states[0])][:context.count],guard=context.guard_enabled,initial_notice=initial_notice,notice=notice,output=[record[19],record[112],record[131],record[162]]))
print(json.dumps({'damages':len(damages)}))
report={'version':'15.7.2','sha256':SHA,'records':records,'actions':actions,'clocks':clocks,'motions':motions,'resumes':resumes,'damages':damages,'transitions':transitions,'begins':begins,'executedInstructions':sorted(n.coverage)}
(ROOT/'research/.local/actors-1572.json').write_text(json.dumps(report,indent=2),encoding='utf-8-sig')
if args.publish:
    (ROOT/'native/kbcs-core/tests/actor-vectors.json').write_text(json.dumps({'version':'15.7.2','sha256':SHA,'cases':published,'actions':actions,'clocks':clocks,'motions':motions,'resumes':resumes,'damages':damages,'transitions':transitions[::11],'begins':begins[::7]},ensure_ascii=False,separators=(',',':')),encoding='utf-8-sig')
