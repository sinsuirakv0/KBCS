"""15.7.2 ARM64の開発素材抽選と素材ID対応を局所実行する。"""
import argparse
import csv
import io
import json
from pathlib import Path
import struct
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--assets',type=Path,required=True)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args()
sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native, Assets, ROOT, SHA, digest

native=Native();assets=Assets(args.assets)
game=0x40000000;native.cpu.mem_map(game,0x800000)
items=[row for row in csv.reader(io.StringIO(assets.text('Data/Gatyaitembuy.csv'))) if row and row[0].strip().isdigit()]
for index,row in enumerate(items):
    native.cpu.mem_write(game+0x392484+index*0x40,struct.pack('<ii',int(row[6]),int(row[7])))
native.helpers={0x81f580:game}
ids=[native.call(0x6f308c,7,slot) for slot in range(16)]
assert ids==[85,86,87,88,89,90,91,140,*range(187,195)]

def execute(case):
    stack,frame=native.stack+0x8000,native.stack+0x9000
    weights=native.memory+0x2000;count=native.memory+0x3000;multiplier=count+4
    native.cpu.mem_write(stack,bytes(0x200));native.cpu.mem_write(frame-0x60,bytes(64))
    native.cpu.mem_write(count,struct.pack('<ff',case['count'],case['multiplier']))
    native.cpu.mem_write(weights,struct.pack('<'+'i'*len(case['weights']),*case['weights']))
    for offset,value in [(0x70,multiplier),(0x88,count),(0xa8,weights),(0xb0,weights+4*len(case['weights']))]:
        native.cpu.mem_write(stack+offset,struct.pack('<Q',value))
    native.cpu.mem_write(stack+0xa0,struct.pack('<i',case['miss']))
    for name,value in [('SP',stack),('X29',frame),('W20',0),('W21',0),('W28',1)]:
        native.cpu.reg_write(getattr(native.reg,'UC_ARM64_REG_'+name),value)
    consumed=[]
    def random():
        bound=native.cpu.reg_read(native.reg.UC_ARM64_REG_W0)
        value=case['rolls'][len(consumed)]
        assert 0<=value<bound
        consumed.append([bound,value]);return value
    native.entry=0x7df270;native.terminals={0x7df3a4};native.helpers={0x44a8d8:random}
    native.cpu.emu_start(native.entry,native.stop,count=100000)
    assert native.cpu.reg_read(native.reg.UC_ARM64_REG_PC)==0x7df3a4
    result={'draws':native.cpu.reg_read(native.reg.UC_ARM64_REG_W20),
            'counts':list(struct.unpack('<16i',native.cpu.mem_read(frame-0x60,64))),'calls':consumed}
    native.terminals=set();return result

cases=[{'count':3,'multiplier':.75,'weights':[13,0,13,13,0,0,0,0],'miss':60,'rolls':rolls}
       for rolls in [[59,59],[60,0,99,12],[60,13,99,25],[60,26,99,38]]]
cases += [dict(count=1,multiplier=.49,weights=[1]*16,miss=0,rolls=[]),
          dict(count=3,multiplier=.5,weights=[1]*16,miss=0,rolls=[0,0,99,15]),
          dict(count=1,multiplier=1,weights=[1,0,2],miss=100,rolls=[99])]
vectors=[{'input':case,**execute(case)} for case in cases]
profiles=[]
for line,text in enumerate(assets.text('Data/DropItem.csv').splitlines(),1):
    cells=next(csv.reader([text])) if text.strip() else []
    if not cells or not cells[0].isdigit() or not 0<=int(cells[0])<49:continue
    values=[float(cell) if cell.strip() else 0 for cell in cells]
    for crown in range(4):
        for stage in range(8):
            case={'count':values[5+stage],'multiplier':values[1+crown],
                  'weights':[int(value) for value in values[14:]],'miss':100,'rolls':[0]*64}
            actual=execute(case)
            product=struct.unpack('<f',struct.pack('<f',case['count']*case['multiplier']))[0]
            assert actual['draws']==int(product+.5)
    profiles.append({'id':int(cells[0]),'line':line,'raw':cells})
assert len(profiles)==49
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,
        'scope':'Material count rounding and two-stage sampler 007df270..007df3a4; RNG controlled; item lookup 006f308c with source table fields',
        'evidence':{address:digest((native.cache/'code'/(address+'.c')).read_bytes()) for address in ['007de628','007df104','006f308c','006f53b8']},
        'sources':assets.sources,'itemIds':ids,'profiles':profiles,'vectors':vectors}
(ROOT/'research/.local/materials-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    fixture={key:value for key,value in report.items() if key not in ['profiles','sources']}
    (ROOT/'native/kbcs-core/tests/material-vectors.json').write_text(json.dumps(fixture,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'profiles':len(profiles),'countCases':len(profiles)*32,'samplerCases':len(vectors),'itemIds':ids}))
