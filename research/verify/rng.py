"""現版の非0シードの乱数列と、個体生成のレイヤー抽選入口を照合する。"""
import argparse
import json
from pathlib import Path
import sqlite3
import struct
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA,digest

class RandomNative(Native):
    def hook(self,cpu,address,size,data):
        if self.entry==0x6ef2b0 and address==0x44a8d8:
            bound=cpu.reg_read(self.reg.UC_ARM64_REG_W0)
            self.bounds.append(bound if bound<0x80000000 else bound-0x100000000)
        if 0x44a8d8<=address<0x44aa50:return
        super().hook(cpu,address,size,data)

native=RandomNative()
with sqlite3.connect((native.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    native.ends.update({int(a,16):int(a,16)+s for a,s in db.execute("SELECT address,size FROM functions WHERE address='009f1e64'")})

def next_state(state):
    state^=(state<<13)&0xffffffff;state^=state>>17;state^=(state<<15)&0xffffffff
    return state

vectors=[]
for seed in [1,0xffffffff,0x80000000,0x12345678]:
    state=seed;steps=[]
    for bound in [0,-1,-2147483648,1,1,2,25,100,65535,2147483647,1]:
        native.cpu.mem_write(native.memory+0x2000,struct.pack('<I',state))
        actual=native.call(0x44a8e8,native.memory+0x2000,bound)
        saved=struct.unpack('<I',native.cpu.mem_read(native.memory+0x2000,4))[0]
        expected=next_state(state) if bound>0 else state
        assert (saved,actual)==(expected,expected%bound if bound>0 else 0)
        steps.append({'bound':bound,'state':saved,'value':actual});state=saved
    vectors.append({'seed':seed,'steps':steps})

game=0x40000000;native.cpu.mem_map(game,0x400000)
actors=[]
for raw,free,minimum,maximum in [(2,1,0,0),(2,50,3,9),(2,1,9,3),(2,0,0,9),(-1,1,0,9)]:
    seed=0x12345678;native.cpu.mem_write(0xc24d18,struct.pack('<I',seed));slots=[]
    def occupied():
        slot=native.cpu.reg_read(native.reg.UC_ARM64_REG_W1);slots.append(slot)
        return int(slot!=free)
    native.helpers={address:0 for address in [0xa9400c,0xa9478c,0x5bbc10,0xa9486c,0xa94e34,
                   0xa94ec0,0xa9bb38,0xa9d498,0xa94f4c,0xa94fe0,0xa95220]}
    native.helpers[0xa93f08]=occupied;native.terminals={0xaa0aa4}
    native.entry=0x9f1e64
    for index,value in enumerate([game,1,raw,0,minimum,maximum,0,0]):
        native.cpu.reg_write(getattr(native.reg,'UC_ARM64_REG_X'+str(index)),value&0xffffffffffffffff)
    native.cpu.reg_write(native.reg.UC_ARM64_REG_SP,native.stack+0x8000)
    native.cpu.reg_write(native.reg.UC_ARM64_REG_LR,native.stop)
    native.cpu.emu_start(native.entry,native.stop+4,count=20000)
    pc=native.cpu.reg_read(native.reg.UC_ARM64_REG_PC);assert pc in [native.stop,0xaa0aa4]
    state=struct.unpack('<I',native.cpu.mem_read(0xc24d18,4))[0]
    expected=next_state(seed) if pc==0xaa0aa4 else seed
    assert state==expected
    layer=None
    if pc==0xaa0aa4:
        layer=struct.unpack('<i',native.cpu.mem_read(game+0x84094+0xc804+free*0x3ec,4))[0]
        assert layer==minimum+state%(max(0,maximum-minimum)+1)
    actors.append({'rawEnemy':raw,'freeSlot':free,'minimum':minimum,'maximum':maximum,'visitedSlots':slots,'state':state,'layer':layer})
schedulers=[]
row=[2,0,0,0,0,100,0,9,0,100,0,0,0,0]
for success in [False,True]:
    native.bounds=[];seed=0x12345678;native.cpu.mem_write(0xc24d18,struct.pack('<I',seed))
    result=native.schedule({'rows':[row],'states':[[0,0,0]],'spawnResult':0 if success else -1})
    state=struct.unpack('<I',native.cpu.mem_read(0xc24d18,4))[0]
    seen=struct.unpack('<i',native.cpu.mem_read(game+0xda58,4))[0]
    assert seen==int(success)
    assert native.bounds==([5,1] if success else [])
    assert state==(next_state(next_state(seed)) if success else seed)
    schedulers.append({'success':success,'bounds':native.bounds,'state':state,'seen':seen,'result':result})
# 実原本にある逆転した再出現区間は、非正のboundで0を返し状態を進めない。
inverted=[]
for row in [[8,1,960,600,300,100,1,2,0,100,0,0,0,0],[291,0,800,2200,2100,100,4,6,0,300,0,0,0,0]]:
    native.bounds=[];seed=0x12345678;native.cpu.mem_write(0xc24d18,struct.pack('<I',seed))
    result=native.schedule({'rows':[row],'states':[[0,0,0]]})
    state=struct.unpack('<I',native.cpu.mem_read(0xc24d18,4))[0]
    assert native.bounds==[5,row[4]-row[3]+1]
    assert state==next_state(seed) and result['states']==[[row[3],1,0]]
    inverted.append({'row':row,'seed':seed,'state':state,'bounds':native.bounds,'result':result})
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,
        'scope':'0044a8e8 nonzero seed, signed bounds including nonpositive no-op; 009f1e64 allocation scan through first stat getter, setters controlled; not full actor construction or zero-seed OS initialization',
        'evidence':{a:digest((native.cache/'code'/(a+'.c')).read_bytes()) for a in ['0044a8d8','0044a8e8','009f1e64','006ef2b0']},
        'vectors':vectors,'actors':actors,'schedulers':schedulers,'inverted':inverted}
(ROOT/'research/.local/random-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    (ROOT/'native/kbcs-core/tests/random-vectors.json').write_text(json.dumps(report,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'randomSteps':sum(len(v['steps']) for v in vectors),'actorEntrances':len(actors),'schedulers':len(schedulers),'invertedIntervals':len(inverted)}))
