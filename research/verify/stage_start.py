"""現版ARM64の出現待機初期化と敵城行の先行消費を照合する。"""
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

class StartNative(Native):
    def hook(self,cpu,address,size,data):
        if self.entry in [0x9ee368,0x9f0a60] and (0xa06c30<=address<0xa06ce4 or 0xa06dc8<=address<0xa06ddc):return
        super().hook(cpu,address,size,data)

native=StartNative();game=0x40000000;native.cpu.mem_map(game,0x400000)
def execute(case):
    rows=case['rows'];stack=native.stack+0x8000;frame=native.stack+0x9000
    definitions=native.memory+0x1000;states=game+0x200000;flags=native.memory+0x8000
    native.cpu.mem_write(stack,bytes(0x200));native.cpu.mem_write(states,bytes([0xcc])*max(12,len(rows)*12))
    for index,row in enumerate(rows):native.cpu.mem_write(definitions+index*56,struct.pack('<14i',*row))
    native.cpu.mem_write(game+0x9ee50,struct.pack('<ii',case['minimum'],case['maximum']))
    native.cpu.mem_write(game+0x9ee70,struct.pack('<QQ',definitions,definitions+len(rows)*56))
    native.cpu.mem_write(game+0x84050,struct.pack('<QQQ',states,states+len(rows)*12,states+max(12,len(rows)*12)))
    for offset,value in [(0x58,game+0x83dfc),(0x68,game+0x9ede0),(0xa8,flags),(0x100,game)]:
        native.cpu.mem_write(stack+offset,struct.pack('<Q',value))
    for name,value in [('SP',stack),('X29',frame),('X19',game+0x9ede0)]:native.cpu.reg_write(getattr(native.reg,'UC_ARM64_REG_'+name),value)
    calls=[]
    def random():
        bound=native.cpu.reg_read(native.reg.UC_ARM64_REG_W0);assert bound==case['maximum']-case['minimum']+1
        calls.append([bound,case['roll']]);return case['roll']
    native.entry=0x9ee368;native.terminals={0x9ee520};native.helpers={0x44a8d8:random}
    native.cpu.emu_start(native.entry,native.stop,count=100000)
    assert native.cpu.reg_read(native.reg.UC_ARM64_REG_PC)==0x9ee520
    spawned=[]
    def spawn():
        spawned.append(native.cpu.reg_read(native.reg.UC_ARM64_REG_W7));return case.get('spawnResult',0)
    native.cpu.mem_write(flags+0xb0,struct.pack('<i',case.get('modeFlag',0)))
    native.entry=0x9f0a60;native.terminals={0x9f0b58}
    native.helpers={0x5bbbc8:int(case.get('castleRaw',0)>0),0x5bbbf0:case.get('castleRaw',0),0x9f1e64:spawn}
    native.cpu.emu_start(native.entry,native.stop,count=100000)
    assert native.cpu.reg_read(native.reg.UC_ARM64_REG_PC)==0x9f0b58
    native.terminals=set()
    return {'states':[list(struct.unpack('<3i',native.cpu.mem_read(states+index*12,12))) for index in range(len(rows))],
            'globalWait':struct.unpack('<i',native.cpu.mem_read(game+0x84048,4))[0],'castleRows':spawned,'calls':calls}

row=[2,0,-14,6,18,100,0,9,0,100,0,0,0,0]
other=row.copy();other[2]=9
cases=[dict(rows=[],minimum=3,maximum=7,roll=4),
       dict(rows=[row,other],minimum=3,maximum=7,roll=0),
       dict(rows=[row,other],minimum=3,maximum=7,roll=4,castleRaw=2),
       dict(rows=[row,other],minimum=3,maximum=7,roll=0,castleRaw=5),
       dict(rows=[row,other],minimum=3,maximum=7,roll=0,castleRaw=2,modeFlag=1),
       dict(rows=[row,other],minimum=3,maximum=7,roll=0,castleRaw=2,spawnResult=-1)]
vectors=[]
for case in cases:vectors.append({'input':case,'result':execute(case)})
witness=json.loads((ROOT/'research/.local/stages-1572-band0.json').read_text(encoding='utf-8-sig'))
actual=[]
for stage in witness['stages']:
    case={'rows':[row['loaded'] for row in stage['spawns']],'minimum':stage['header']['cells'][2],
          'maximum':stage['header']['cells'][3],'roll':0,'castleRaw':stage['header']['cells'][6] or 0}
    result=execute(case);expected=[[row[2],0,0] for row in case['rows']]
    candidates=[index for index,row in enumerate(case['rows']) if case['castleRaw']>0 and row[0]==case['castleRaw']]
    if candidates:expected[candidates[0]]=[1,1,0]
    assert result['states']==expected and result['castleRows']==candidates[:1]
    actual.append({'map':stage['map'],'stage':stage['stage'],'result':result})
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,
        'scope':'009eadc8 fragments 009ee368..009ee520 and 009f0a60..009f0b58; preallocated vectors, controlled RNG, mode flag, castle getter and actor construction; not full battle initialization',
        'evidence':{address:digest((native.cache/'code'/(address+'.c')).read_bytes()) for address in ['009eadc8','00a06c68','00a06dc8']},
        'vectors':vectors,'stages':actual}
(ROOT/'research/.local/stage-start-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    fixture={key:value for key,value in report.items() if key!='stages'}
    (ROOT/'native/kbcs-core/tests/stage-start-vectors.json').write_text(json.dumps(fixture,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'stageStarts':len(actual),'boundaryCases':len(vectors),'castleStarts':sum(bool(stage['result']['castleRows']) for stage in actual)}))
