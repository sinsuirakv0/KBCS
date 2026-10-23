"""クリア時間スコアと最高記録をまたぐ報酬要求を現版ARM64で照合する。"""
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
native=Native();native.ends[0x5dd634]=0x5dddd0
game=0x40000000;native.cpu.mem_map(game,0x800000)

def write(address,value,wide=False):native.cpu.mem_write(address,struct.pack('<Q' if wide else '<I',value&((1<<(64 if wide else 32))-1)))

def score(elapsed):
    return 10000-elapsed if elapsed<=9000 else 1000-(elapsed-9000)//10 if elapsed<19000 else 0

def execute(elapsed,best,thresholds,grant_result=0,save_id=17,stage_index=0):
    base=game+0x38b168;stage=base+stage_index*0xbc;stack=native.stack+0x8000;kind=native.memory+0x3000
    saved=game+0x3b7680+save_id*0xf0+stage_index*0x10+2*4
    native.cpu.mem_write(game+0x334018,bytes(0x100));native.cpu.mem_write(game+0x3c32c8,bytes(0x100))
    write(game+0x83dfc,stage_index);write(game+0x83e74,elapsed);write(game+0x83e54,0);write(game+0x83e58,0)
    write(game+0x3c3334,save_id);write(game+0x39797c,2);write(saved,best);write(kind,3)
    mask=0x01020304;write(stage+0xb8,mask)
    for index in range(10):write(stage+0x40+index*12,(thresholds[index] if index<len(thresholds) else -1)^mask)
    vector=native.memory+0x5000
    for offset,value in [(0x60,vector),(0x68,vector),(0x70,vector+0x100)]:write(game+0x334018+offset,value,True)
    for offset,value in [(0x58,base),(0xc8,stage_index),(0xa8,game+0x3c32c8),(0xd0,kind),(0xe8,game+0x83dfc),(0xf0,game+0x334018),(0xf8,game)]:write(stack+offset,value,True)
    for name,value in [('SP',stack),('X29',stack+0x280),('X11',game+0x83dfc),('X9',saved),('X19',game+0x3c32c8),('X25',stage),('X20',0)]:
        native.cpu.reg_write(getattr(native.reg,'UC_ARM64_REG_'+name),value)
    calls=[];allocations=[]
    def grant():
        values=[native.cpu.reg_read(getattr(native.reg,'UC_ARM64_REG_X'+str(i))) for i in range(3)]
        assert values[0]==game and values[2]==1
        assert struct.unpack('<i',native.cpu.mem_read(saved,4))[0]==best
        calls.append(values[1]);return grant_result
    def allocate():
        assert native.cpu.reg_read(native.reg.UC_ARM64_REG_X0)==16
        pointer=native.memory+0x6000+len(allocations)*0x20;allocations.append(pointer);return pointer
    native.helpers={0x6e34b0:grant,0xbdaf40:allocate,0x7f96d8:0}
    native.terminals={0x5ddd8c};native.entry=0x5dd634
    native.cpu.emu_start(native.entry,native.stop,count=50000)
    assert native.cpu.reg_read(native.reg.UC_ARM64_REG_PC)==0x5ddd8c
    actual=struct.unpack('<i',native.cpu.mem_read(game+0x83e54,4))[0]
    record=struct.unpack('<i',native.cpu.mem_read(saved,4))[0]
    improved=struct.unpack('<i',native.cpu.mem_read(game+0x83e58,4))[0]
    expected=score(elapsed);indices=[i for i,t in enumerate(thresholds) if best<t<=expected]
    assert actual==expected and record==max(best,expected) and improved==int(expected>best),(elapsed,best,actual,record)
    assert calls==[17+i*3 for i in indices],(thresholds,calls,indices)
    end=struct.unpack('<Q',native.cpu.mem_read(game+0x334080,8))[0]
    rows=[]
    for pointer in range(vector,end,24):
        data=struct.unpack('<Q',native.cpu.mem_read(pointer,8))[0]
        rows.append(list(struct.unpack('<4i',native.cpu.mem_read(data,16))))
    assert rows==([] if grant_result==1 else [[0,column,1,grant_result] for column in calls]),rows
    return {'input':{'elapsed':elapsed,'best':best,'count':len(thresholds),'thresholds':thresholds+[0]*(10-len(thresholds))},
            'score':actual,'best':record,'improved':improved,'rewardMask':sum(1<<i for i in indices),
            'grantColumns':calls,'grantResult':grant_result,'resultRows':rows}

vectors=[]
for elapsed in [0,1,8999,9000,9001,9009,9010,18999,19000,19001,2147483647]:
    for best in [0,1000,10000]:vectors.append(execute(elapsed,best,[8500,1000,999,1,0]))
witness_path=ROOT/'research/.local/stages-1572-band1000.json';witness=read_json(witness_path)
assert witness['sha256']==SHA and witness['version']=='15.7.2' and witness['architecture']=='arm64-v8a'
headers={m['id']:m['headers'][0]['cells'] for m in witness['maps']}
actual=[];profiles=[];disabled=[]
for stage in witness['stages']:
    if stage.get('orphan'):continue
    cells=stage['rewards']['cells']
    if len(cells)<=15 or cells[15]!=1:continue
    save_id=headers[stage['map']][2]
    if save_id<0 or save_id>=200:
        disabled.append({'map':stage['map'],'stage':stage['stage'],'saveId':save_id});continue
    thresholds=[]
    for column in range(16,46,3):
        if column>=len(cells) or cells[column]==-1:break
        thresholds.append(cells[column] or 0)
    assert 1<=len(thresholds)<=10
    profiles.append({'map':stage['map'],'stage':stage['stage'],'saveId':save_id,'thresholds':thresholds})
    for target in sorted(set(thresholds)):
        elapsed=10000-target if target>=1000 else 9000+(1000-target)*10
        for best in [max(0,target-1),target]:
            for grant_result in [0,1]:
                actual.append({'map':stage['map'],'stage':stage['stage'],**execute(elapsed,best,thresholds,grant_result,save_id,stage['stage'])})
# 保存先なしの通常イベントはスコア計算へ進まず、既存値にも触らない。
write(game+0x3c3334,-1);write(game+0x83e54,37);write(game+0x83e58,41)
native.cpu.reg_write(native.reg.UC_ARM64_REG_X19,game+0x3c32c8)
native.helpers={};native.entry=0x5dd5f4;native.terminals={0x5ddd8c}
native.cpu.emu_start(native.entry,native.stop,count=100)
assert native.cpu.reg_read(native.reg.UC_ARM64_REG_PC)==0x5ddd8c
assert struct.unpack('<ii',native.cpu.mem_read(game+0x83e54,8))==(37,41)
timers=[]
for elapsed in [0,1,29998,29999,30000,2147483647]:
    for phase in [0,1,2,3]:
        write(game+0x83e74,elapsed);stack=native.stack+0x8000
        write(stack+0x60,game+0x83dfc,True)
        native.cpu.reg_write(native.reg.UC_ARM64_REG_SP,stack)
        native.helpers={0x5bc058:phase};native.entry=0x6d81d4;native.terminals={0x6d81f8}
        native.cpu.emu_start(native.entry,native.stop,count=100)
        assert native.cpu.reg_read(native.reg.UC_ARM64_REG_PC)==0x6d81f8
        result=struct.unpack('<i',native.cpu.mem_read(game+0x83e74,4))[0]
        assert result==(min(30000,elapsed+1) if phase==0 else elapsed)
        timers.append({'elapsed':elapsed,'phase':phase,'result':result})
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,
        'scope':'005dd634 through 005ddd8c, resolved normal-mode saved-score pointer; actual score, threshold iteration, saved best and result rows; controlled grant, allocation and analytics; not actual inventory grant',
        'evidence':{a:digest((native.cache/'code'/(a+'.c')).read_bytes()) for a in ['005d996c','006d6d04','005bc058','0081c6a0']},
        'stageWitnessSha256':digest(witness_path.read_bytes()),'vectors':vectors,'profiles':profiles,'stages':actual,'disabled':disabled,'timers':timers}
(ROOT/'research/.local/stage-score-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    fixture={k:v for k,v in report.items() if k not in ['profiles','stages']}
    # 実原本の最大10枠も小さいfixtureへ残す。
    fixture['vectors']=vectors+[next(v for v in actual if v['input']['count']==10)]
    (ROOT/'native/kbcs-core/tests/score-vectors.json').write_text(json.dumps(fixture,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'vectors':len(vectors),'profiles':len(profiles),'actualCases':len(actual),'disabled':len(disabled)}))
