"""0番台の通常報酬比較と取得済み分岐を現版命令へ照合する。"""
import argparse
import json
from pathlib import Path
import struct
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA,digest,read_json

native=Native();native.ends[0x5dbfd4]=0x5de000

def execute(case,map_id=17,stage_index=5):
    stage,state,kind,group,aux=[native.memory+offset for offset in [0x1000,0x2000,0x3000,0x4000,0x5000]]
    stack=native.stack+0x8000
    for pointer in [stage,state,kind,group,aux]:native.cpu.mem_write(pointer,bytes(0x800))
    mask=0x01020304
    native.cpu.mem_write(stage+0xb8,struct.pack('<I',mask))
    native.cpu.mem_write(stage+0x20,struct.pack('<I',(case['mode']^mask)&0xffffffff))
    for offset,chance in zip([0x14,0x24,0x30],case['chances']):
        native.cpu.mem_write(stage+offset,struct.pack('<I',chance^mask))
    native.cpu.mem_write(kind,struct.pack('<i',3));native.cpu.mem_write(group,struct.pack('<i',map_id))
    for offset,pointer in [(0xf0,state),(0xa0,aux),(0xd0,kind),(0xd8,state+0x3cc),(0xc8,stage_index),(0x50,stage+0x16)]:
        native.cpu.mem_write(stack+offset,struct.pack('<Q',pointer))
    native.cpu.mem_write(stack+0xbc,bytes(4));native.cpu.mem_write(stack+0x60,struct.pack('<i',case['count']))
    for name,value in [('SP',stack),('X19',group),('X21',stage+0x14),('X23',stage+0x15),('X25',stage),('X28',stage+0x17)]:
        native.cpu.reg_write(getattr(native.reg,'UC_ARM64_REG_'+name),value)
    consumed=[];records=[]
    def random():
        bound=native.cpu.reg_read(native.reg.UC_ARM64_REG_W0);assert bound==100
        value=case['rolls'][len(consumed)];consumed.append(value);return value
    def record():
        records.append([native.cpu.reg_read(getattr(native.reg,'UC_ARM64_REG_W'+str(index))) for index in range(6)])
        assert records[-1]==[map_id,stage_index,2,case['mode'],1,0]
        return 0
    def acquired():
        values=[native.cpu.reg_read(getattr(native.reg,'UC_ARM64_REG_W'+str(index))) for index in range(5)]
        assert values==[map_id,stage_index,2,case['mode'],0]
        return case['acquired']
    native.helpers={0x44a8d8:random,0x5c022c:case['radar'],0x7d04f0:0,0x7cfcd8:2,
                    0xa092a0:acquired,0xa0956c:record,0x5e0000:case['mode']&0xffffffff}
    native.entry=0x5dbfd4;native.terminals={0x5dd500,0x5dd52c}
    native.cpu.emu_start(native.entry,native.stop,count=20000)
    pc=native.cpu.reg_read(native.reg.UC_ARM64_REG_PC);assert pc in native.terminals
    winner=-1 if pc==0x5dd52c else 0 if records else native.cpu.reg_read(native.reg.UC_ARM64_REG_W27)
    expected=-1
    for index in range(case['count']):
        if not case['radar'] and case['rolls'][index]>=case['chances'][index]:continue
        if index==0 and case['mode']==1 and case['acquired']:
            if case['radar']:break
            continue
        expected=index;break
    assert winner==expected,(case,winner,expected)
    return {'winner':winner,'consumed':len(consumed),'markAcquired':int(bool(records)),
            'radarBlocked':native.cpu.mem_read(aux+0x6ec,1)[0]}

vectors=[]
for mode in [-1,1]:
    for acquired in [0,1]:
        for radar in [0,1]:
            for chances,rolls,count in [([30,85,9],[29,99,99],3),([30,85,9],[30,84,99],3),
                                       ([30,85,9],[99,85,8],3),([30,85,9],[99,99,9],3),
                                       ([100,0,0],[99,0,0],1),([0,100,0],[0,99,0],2)]:
                case=dict(mode=mode,acquired=acquired,radar=radar,chances=chances,rolls=rolls,count=count)
                vectors.append({'input':case,**execute(case)})
witness=read_json(ROOT/'research/.local/stages-1572-band0.json')
actual=[]
for stage in witness['stages']:
    cells=stage['rewards']['cells'];assert cells[8] in [-1,1] and cells[5]<1000
    chances=[cells[column] or 0 for column in [5,*range(9,len(cells)-3,3)]]
    assert 1<=len(chances)<=3
    for acquired in [0,1]:
        for radar in [0,1]:
            for roll in [0,99]:
                case=dict(mode=cells[8],acquired=acquired,radar=radar,chances=chances+[0]*(3-len(chances)),rolls=[roll]*3,count=len(chances))
                actual.append({'map':stage['map'],'stage':stage['stage'],'input':case,**execute(case,stage['map'],stage['stage'])})
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,
        'scope':'005dbfd4..005dd500/005dd52c ordinary sequential reward path; kind=3, normal flag, crown=2, special reward type=0; controlled RNG, radar, acquisition getters/setter with supplied map/stage; not inventory grant or full result screen',
        'evidence':{address:digest((native.cache/'code'/(address+'.c')).read_bytes()) for address in ['005d996c','00a092a0','00a0956c','007d04f0']},
        'stageWitnessSha256':digest((ROOT/'research/.local/stages-1572-band0.json').read_bytes()),
        'vectors':vectors,'stages':actual}
(ROOT/'research/.local/rewards-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    fixture={key:value for key,value in report.items() if key!='stages'}
    (ROOT/'native/kbcs-core/tests/reward-vectors.json').write_text(json.dumps(fixture,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'vectors':len(vectors),'stageCases':len(actual)}))
