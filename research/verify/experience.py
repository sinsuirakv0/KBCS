"""現版ARM64の0番台XP計算と章別お宝の整数化を局所実行する。"""
import argparse
import json
from pathlib import Path
import struct
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args()
sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native, ROOT, SHA, digest

native=Native()
game=0x40000000
native.cpu.mem_map(game,0x800000)
native.ends[0x58bad0]=0x58bf80
native.ends[0xa5b084]=0xa5b1cc
def write(offset,value): native.cpu.mem_write(game+offset,struct.pack('<I',value))
def minimum():
    return min(native.cpu.reg_read(native.reg.UC_ARM64_REG_X0)&0xffffffff,
               native.cpu.reg_read(native.reg.UC_ARM64_REG_X1)&0xffffffff)

# 章別に切り捨てて合算する処理も同版の汎用集計関数へ通す。
treasures=[]
for values in [[0]*6,[100]*6,[45]*6,[99]*6,[1,3,5,7,9,11]]:
    native.cpu.mem_write(native.memory,bytes(0x1000))
    for index,(chapter,maximum) in enumerate([(0,50),(1,50),(2,50),(6,25),(7,25),(8,25)]):
        row=native.memory+0x200+index*0x30
        native.cpu.mem_write(native.memory+chapter*0x18,struct.pack('<QQQ',row,row+0x30,row+0x30))
        native.cpu.mem_write(row+0x24,struct.pack('<II',6,maximum))
        write(0x83e90+chapter*0x2c,values[index])
    native.helpers={0x81f580:game}
    actual=native.call(0xa5b084,native.memory,6)
    expected=sum(value*maximum//100 for value,maximum in zip(values,[50]*3+[25]*3))
    assert actual==expected,(values,actual,expected)
    treasures.append({'chapters':values,'result':actual})

vectors=[]
for base,clears,study,treasure,combo,okame in [
    (3040,0,30,225,0,0),(3041,1,17,97,10,1),(3041,4,1,0,0,0),
    (3041,5,30,225,15,1),(1,3,2,1,5,1),(0,0,1,0,0,0),
    (12345,2,20,134,25,0),(12345,3,30,225,30,1),
]:
    write(0x32f934,3);write(0x83dfc,0)
    write(0x38b220,base^0x01020304);write(0x38b16c,0x01020304)
    native.helpers={0x81f580:game,0x7cd100:0,0xa08564:clears,0x44abfc:minimum,
                    0x58b674:study-1,0xa5b084:treasure,0x88f9e4:combo,0x5c022c:okame}
    actual=native.call(0x58bad0)
    initial=base*9
    repeated=initial-initial*min(clears,4)//5
    studied=repeated*(100+(study-1)*5+treasure)//100
    combined=studied*(100+combo)//100
    expected=combined*15//10 if okame else combined
    assert actual==expected,(base,clears,actual,expected)
    vectors.append({'input':{'base':base,'clears':clears,'studyLevel':study,'treasure':treasure,'combo':combo,'okame':okame},
                    'result':actual,'stages':[initial,repeated,studied,combined,actual]})
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,
        'scope':'Band 0 XP arithmetic; controlled game state, kind, clear count, study, treasure, combo and item helpers; not reward acquisition',
        'evidence':{address:digest((native.cache/'code'/(address+'.c')).read_bytes()) for address in ['0058bad0','00a5b084']},
        'treasures':treasures,'vectors':vectors}
(ROOT/'research/.local/experience-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    (ROOT/'native/kbcs-core/tests/experience-vectors.json').write_text(json.dumps(report,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'experienceCases':len(vectors),'treasureCases':len(treasures)}))
