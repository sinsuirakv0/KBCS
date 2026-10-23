"""重み選択後の履歴・付与要求・結果行を現版ARM64で照合する。"""
import argparse
import json
from pathlib import Path
import struct
import sys
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA,digest
native=Native();native.ends[0x5dbe5c]=0x5dd600
game=0x40000000;native.cpu.mem_map(game,0x800000)
def write(address,value,wide=False):native.cpu.mem_write(address,struct.pack('<Q' if wide else '<I',value&((1<<(64 if wide else 32))-1)))

def execute(mode,seen,radar,winner,grant_result):
    stage=game+0x38b168;group=game+0x3c32c8;state=game+0x334018
    root,child,vector,aux=[native.memory+o for o in [0x1000,0x2000,0x5000,0x7000]]
    for pointer in [root,child,vector,aux,state,group]:native.cpu.mem_write(pointer,bytes(0x100))
    write(game+0x3c32d8,root,True);write(root+0x20,1000);write(root+0x28,child,True);write(root+0x30,child,True)
    write(child+0x1c,0);native.cpu.mem_write(child+0x20,bytes([seen]))
    native.helpers={0x81f580:game};native.terminals=set()
    assert native.call(0xa09734,1000,0)==seen
    mask=0x01020304;write(stage+0xb8,mask);write(stage+0x20,mode^mask)
    source=0 if winner==0 else winner*3+1;write(group+0x70,source)
    for offset,value in [(0x60,vector),(0x68,vector),(0x70,vector+0x100)]:write(state+offset,value,True)
    stack=native.stack+0x8000
    for offset,value in [(0xa0,aux),(0xc0,1000),(0xc8,0),(0xf0,state),(0xf8,game)]:write(stack+offset,value,True)
    for name,value in [('SP',stack),('X29',stack+0x280),('X19',group),('X25',stage)]:
        native.cpu.reg_write(getattr(native.reg,'UC_ARM64_REG_'+name),value)
    calls=[];allocated=[]
    def grant():
        args=[native.cpu.reg_read(getattr(native.reg,'UC_ARM64_REG_X'+str(i))) for i in range(3)]
        assert args==[game,source+6,0]
        # 初回履歴が付与より前に書かれる。付与が1でも戻さない。
        assert native.cpu.mem_read(child+0x20,1)[0]==(1 if mode==-3 else seen)
        calls.append(args[1]);return grant_result
    def allocate():
        assert native.cpu.reg_read(native.reg.UC_ARM64_REG_X0)==16
        pointer=native.memory+0x6000+len(allocated)*0x20;allocated.append(pointer);return pointer
    native.helpers={0xa09734:seen,0x6e34b0:grant,0xbdaf40:allocate,0x5c022c:radar}
    native.entry=0x5dbe5c;native.terminals={0x5dd52c}
    native.cpu.emu_start(native.entry,native.stop,count=20000)
    assert native.cpu.reg_read(native.reg.UC_ARM64_REG_PC)==0x5dd52c
    expected_grant=mode==-4 or not seen
    blocked=native.cpu.mem_read(aux+0x6ec,1)[0]
    assert calls==([source+6] if expected_grant else [])
    assert blocked==int(mode==-3 and seen and radar)
    after=native.cpu.mem_read(child+0x20,1)[0];assert after==(1 if mode==-3 else seen)
    end=struct.unpack('<Q',native.cpu.mem_read(state+0x68,8))[0];rows=[]
    for pointer in range(vector,end,24):
        data=struct.unpack('<Q',native.cpu.mem_read(pointer,8))[0]
        rows.append(list(struct.unpack('<4i',native.cpu.mem_read(data,16))))
    assert rows==([[0,source+6,0,grant_result]] if expected_grant else [])
    return {'input':{'mode':mode,'seen':seen,'radar':radar,'winner':winner},
            'grantColumn':source+6 if expected_grant else -1,'markHistory':int(mode==-3 and not seen),
            'radarBlocked':blocked,'grantResult':grant_result,'resultRows':rows,'historyAfter':after}

vectors=[execute(mode,seen,radar,winner,result) for mode in [-3,-4] for seen in [0,1]
         for radar in [0,1] for winner in [0,1,9] for result in [0,1]]
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,
        'scope':'005dbe5c through 005dd52c, existing map/stage tree nodes, history getter separately executed; controlled grant, allocation, radar and history lookup; actual history write ordering and result rows, not node insertion or inventory grant',
        'evidence':{a:digest((native.cache/'code'/(a+'.c')).read_bytes()) for a in ['005d996c','00a09734']},'vectors':vectors}
(ROOT/'research/.local/reward-finish-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    (ROOT/'native/kbcs-core/tests/reward-finish-vectors.json').write_text(json.dumps(report,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'vectors':len(vectors)}))
