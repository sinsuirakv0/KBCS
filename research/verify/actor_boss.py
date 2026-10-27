"""ボス衝撃波の走査と2F連続更新を、006d6d04の実命令へ照合する。"""
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
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA
class Actor(c.Structure):_fields_=[('words',c.c_int32*251)]
Pool=(Actor*51)*2
class Environment(c.Structure):
    _fields_=[('unit_modes',c.c_int32*2),*[(name,c.c_int32) for name in ['stage_width','castle_slot','castle_x','castle_scale','castle_offset','stage_kind','zombie','chapter_rate','crown','hp_percent','attack_percent']],
              ('crystal_max',c.c_int32*5),('crystal',c.c_int32*5),('treasures',c.c_int32*32),('combos',c.c_int32*32),('orb_stage',c.c_int32),('talents_disabled',c.c_int32),('parameters',c.c_int32*2),('spawned',c.c_int32*2),('spawn_row',c.c_int32*14),('special_castle',c.c_int32)]
class BossNative(Native):
    def hook(self,cpu,address,size,data):
        if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
        if address in self.allowed:return
        return super().hook(cpu,address,size,data)
n=BossNative();game=0x40000000;n.cpu.mem_map(game,0x800000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    sizes={int(a,16):size for a,size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
functions=[0xa94bf0,0xa95100,0xa9518c,0xa95140,0xa9502c,0xa94678,0xa94484,0xa9b4c4,0xa94274,0xa9478c]
n.allowed={pc for a in functions for pc in range(a,a+sizes[a],4)}
n.entry=0x6d6d04;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={0x6d9454}
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()))
lib.kbcs_core_actor_boss.argtypes=[c.POINTER(Actor*51),c.POINTER(Environment),c.c_int32,c.POINTER(c.c_int32),c.POINTER(c.c_int32)]
count=0
for mode,bosses,flag,counter,length in itertools.product([0,1],[0,1,2],[1,2],[0,1,31,32],[0,1,32]):
    pool=Pool();env=Environment();env.unit_modes[:]=[1,mode]
    for slot in range(1,51):
        w=pool[0][slot].words;w[0]=2 if slot%3 else 0;w[1]=(slot-1)%22;w[2]=9;w[116]=int(slot%4==0)
    for slot in range(bosses):pool[1][slot].words[64]=flag;pool[1][slot].words[65]=counter
    for tick in range(2):
        sounds=[];shakes=[]
        def sound():sounds.append(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1));return 0
        def shake():shakes.append(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1));return 0
        n.helpers={0x81f580:game,0x5c2710:mode,0x44bf2c:length,0x457e1c:0,0x459efc:sound,0x5c1404:shake}
        n.cpu.mem_write(game+0x84080,bytes(pool));sp=n.stack+0x8000
        n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,sp);n.cpu.reg_write(n.reg.UC_ARM64_REG_X27,game)
        n.cpu.emu_start(0x6d9334,n.stop+4,count=500000)
        assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'boss budget'
        expected=bytes(n.cpu.mem_read(game+0x84080,c.sizeof(pool)))
        actual_sounds=c.c_int32();actual_shakes=c.c_int32()
        assert lib.kbcs_core_actor_boss(pool,c.byref(env),length,c.byref(actual_sounds),c.byref(actual_shakes))==0
        assert bytes(pool)==expected,(mode,bosses,flag,counter,length,tick)
        assert sounds==[45]*actual_sounds.value and shakes==[1]*actual_shakes.value
        count+=1
# 城メタデータはX0=[offsetX,offsetY]、X1=[scale,...]の複合戻り値。
lib.kbcs_core_boss_effect_anchor.argtypes=[c.c_int32]*5+[c.POINTER(c.c_int32)]
n.entry=0x6ddfb8;n.ends[n.entry]=n.entry+sizes[n.entry];n.terminals={0x6e0588};anchors=0
for x,y,scale,offset_x,offset_y in itertools.product([3200,4800],[4400,5011],[50,100,127],[-13,0,17],[-7,0,12]):
    def metadata():
        n.cpu.reg_write(n.reg.UC_ARM64_REG_X1,scale)
        return (offset_x&0xffffffff)|((offset_y&0xffffffff)<<32)
    n.helpers={0xa92ea0:x,0xa92eb4:y,0x5bbfb0:0,0x656de0:metadata}
    sp=n.stack+0x8000;n.cpu.mem_write(sp+0x130,struct.pack('<Q',n.memory));n.cpu.mem_write(n.memory+0x10,bytes(4))
    for reg,value in [('SP',sp),('X25',game),('X21',game)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+reg),value)
    n.cpu.emu_start(0x6e042c,n.stop+4,count=5000)
    assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals,'boss anchor budget'
    base=struct.unpack('<ii',n.cpu.mem_read(game+0xde4,8));expected=[base[0]+64,base[1]+224];out=(c.c_int32*2)()
    assert lib.kbcs_core_boss_effect_anchor(x,y,scale,offset_x,offset_y,out)==0
    assert list(out)==expected,((x,y,scale,offset_x,offset_y),list(out),expected)
    anchors+=1
report={'version':'15.7.2','sha256':SHA,'librarySha256':hashlib.sha256(args.library.read_bytes()).hexdigest(),'entry':'006d9334','terminal':'006d9454','updates':count,'anchorCases':anchors,'anchorEntry':'006e042c','anchorTerminal':'006e0588',
        'controlled':['singleton','unit-mode flag','boss animation plain length','SE45 and vibration request capture'],
        'limits':['boss fragment only; preceding attacks and full battle main are outside this comparison']}
(ROOT/'research/.local/actor-boss-1572.json').write_text(json.dumps(report,indent=2),encoding='utf-8-sig')
print(json.dumps(report))
