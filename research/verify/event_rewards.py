"""1000番台の候補数決定・通常比較・重み選択を現版命令へ照合する。"""
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
native=Native();native.ends[0x5dbae4]=0x5de000

def reward_type(identifier):
    return 2 if 10000<=identifier<20000 else 3 if 20000<=identifier<30000 else 1 if 1000<=identifier<10000 else 0


def execute(case,map_id=17,stage_index=0):
    stage,state,kind,group,aux=[native.memory+offset for offset in [0x1000,0x2000,0x3000,0x4000,0x5000]]
    stack=native.stack+0x8000
    for pointer in [stage,state,kind,group,aux]:native.cpu.mem_write(pointer,bytes(0x800))
    mask=0x01020304
    native.cpu.mem_write(stage+0xb8,struct.pack('<I',mask))
    cells=case['cells']
    for column in range(5,39):
        value=cells[column] if column<len(cells) and cells[column] is not None else -1
        native.cpu.mem_write(stage+column*4,struct.pack('<I',(value^mask)&0xffffffff))
    native.cpu.mem_write(kind,struct.pack('<i',3));native.cpu.mem_write(group,struct.pack('<i',map_id))
    for offset,pointer in [(0xf0,state),(0xa0,aux),(0xd0,kind),(0xd8,state+0x3cc),(0xc8,stage_index),(0xc0,map_id)]:
        native.cpu.mem_write(stack+offset,struct.pack('<Q',pointer&0xffffffffffffffff))
    native.cpu.mem_write(stack+0xbc,bytes(4))
    for name,value in [('SP',stack),('X19',group),('X25',stage)]:
        native.cpu.reg_write(getattr(native.reg,'UC_ARM64_REG_'+name),value)
    bounds=[];records=[]
    def random():
        bound=native.cpu.reg_read(native.reg.UC_ARM64_REG_W0)
        value=case['roll'] if case['roll']>=0 else bound-1
        assert 0<=value<bound,(case,bound)
        bounds.append(bound);return value
    def acquired():
        values=[native.cpu.reg_read(getattr(native.reg,'UC_ARM64_REG_W'+str(i))) for i in range(5)]
        assert values==[map_id,stage_index,2,cells[8],0],values
        return case['acquired']
    def record():
        values=[native.cpu.reg_read(getattr(native.reg,'UC_ARM64_REG_W'+str(i))) for i in range(6)]
        assert values==[map_id,stage_index,2,cells[8],1,0],values
        records.append(values);return 0
    def getter():return cells[native.cpu.reg_read(native.reg.UC_ARM64_REG_W1)]&0xffffffff
    native.helpers={0x44a8d8:random,0x5c022c:case['radar'],0x7d04f0:reward_type(cells[6]),0x7cfcd8:2,0x7d03e0:cells[6],0x6fea2c:case['acquired'],
                    0xa092a0:acquired,0xa0956c:record,0x5e0000:getter}
    native.entry=0x5dbae4;native.terminals={0x5dd500,0x5dd52c,0x5dbe5c}
    native.cpu.emu_start(native.entry,native.stop,count=20000)
    pc=native.cpu.reg_read(native.reg.UC_ARM64_REG_PC);assert pc in native.terminals,hex(pc)
    source=struct.unpack('<i',native.cpu.mem_read(group+0x70,4))[0]
    winner=-1 if pc==0x5dd52c else (0 if source==0 else (source-1)//3)
    count=native.cpu.reg_read(native.reg.UC_ARM64_REG_W21) if cells[8] in [-3,-4] else struct.unpack('<i',native.cpu.mem_read(stack+0x60,4))[0]
    return {'winner':winner,'consumed':len(bounds),'bounds':bounds,'count':count,
            'markAcquired':int(bool(records)),'radarBlocked':native.cpu.mem_read(aux+0x6ec,1)[0]}


def compare(case,result):
    cells=case['cells'];mode=cells[8]
    if mode in [-3,-4]:
        weights=[]
        for column in [5,*range(9,39,3)]:
            if column>=len(cells) or cells[column]==-1:break
            weights.append(cells[column])
        # 11枠を使い切ると元関数は候補数を0へ戻す。正常APIは終端ありの1..10枠だけ扱う。
        count=0 if len(weights)==11 else len(weights)
        total=sum(weights);roll=case['roll'] if case['roll']>=0 else total-1
        expected=-1;running=0
        for index,weight in enumerate(weights[:count]):
            running+=weight
            if roll<running:expected=index;break
        assert result['winner']==expected and result['bounds']==[total] and result['count']==count,(case,result)
        return {'weights':weights,'total':total,'roll':roll,'winner':expected}
    count=1 if mode<0 or len(cells)<=9 or cells[9]<0 else 2 if len(cells)<=12 or cells[12]<0 else 3
    chances=[cells[i] for i in [5,9,12][:count]];roll=99 if case['roll']==-1 else case['roll']
    expected=-1;consumed=0;blocked=0
    for index,chance in enumerate(chances):
        consumed+=1
        if not case['radar'] and roll>=chance:continue
        if index==0 and mode in [1,2] and case.get('saveId',17)!=-1 and case['acquired']:
            if case['radar']:blocked=1;break
            continue
        expected=index;break
    assert result['winner']==expected and result['count']==count and result['consumed']==consumed,(case,result)
    assert result['markAcquired']==int(expected==0 and mode in [1,2] and case.get('saveId',17)!=-1) and result['radarBlocked']==blocked,(case,result)
    return {'context':{'mode':mode,'saveId':case.get('saveId',17),'acquired':case['acquired'],'radar':case['radar'],
                       'chances':[(cells[i] if i<len(cells) and cells[i] is not None else -1) for i in [5,9,12]],'rolls':[roll]*3},
            'input':{'count':count,'mode':0 if mode in [1,2] and case.get('saveId',17)==-1 else mode,'acquired':case['acquired'],'radar':case['radar'],
                     'chances':chances+[0]*(3-count),'rolls':[roll]*3},
            'winner':expected,'consumed':consumed,'markAcquired':result['markAcquired'],'radarBlocked':blocked}

witness_path=ROOT/'research/.local/stages-1572-band1000.json';witness=read_json(witness_path)
assert witness['sha256']==SHA
headers={m['id']:m['headers'][0]['cells'] for m in witness['maps']}
actual=[];vectors=[];weighted=[];skipped=[]
for stage in witness['stages']:
    if stage.get('orphan'):continue
    cells=stage['rewards']['cells']
    # 報酬なしを通常比較の候補へ変えない。
    if cells[5]==-1:skipped.append([stage['map'],stage['stage']]);continue
    for acquired in [0,1]:
        for radar in [0,1]:
            for roll in [0,-1]:
                save_id=headers[stage['map']][1]
                save_id=-1 if save_id>399 else save_id
                case={'cells':cells,'acquired':acquired,'radar':radar,'roll':roll,'saveId':save_id}
                result=execute(case,save_id,stage['stage']);expected=compare(case,result)
                actual.append({'map':stage['map'],'stage':stage['stage'],'mode':cells[8],'saveId':save_id,'rewardType':reward_type(cells[6]),**result})
                target=weighted if cells[8] in [-3,-4] else vectors
                if expected not in target:target.append(expected)
# 境界値と0重みを実命令でも確認する。
for weights in [[0,2,0,3],[1],[1]*10,[1]*11]:
    cells=[0]*9;cells[5:9]=[weights[0],6,1,-4]
    for weight in weights[1:]:cells.extend([weight,6,1])
    cells.extend([-1,-1,-1])
    for roll in range(sum(weights)):
        case={'cells':cells,'acquired':0,'radar':0,'roll':roll}
        expected=compare(case,execute(case))
        if expected not in weighted:weighted.append(expected)
# 原本に先頭分類3がない場合も、所有済み分岐の入口を制御して確認する。
ownership_cases=[]
for identifier in [6,1018,10010,20001]:
    for mode in [1,2]:
        for acquired in [0,1]:
            for radar in [0,1]:
                for roll in [49,50,99]:
                    case={'cells':[0,0,0,0,0,50,identifier,1,mode,100,6,1,-1],
                          'acquired':acquired,'radar':radar,'roll':roll}
                    result=execute(case);compare(case,result)
                    ownership_cases.append({'id':identifier,'mode':mode,'acquired':acquired,'radar':radar,'roll':roll,**result})
# mode2だけ冠ごとの1バイトを使い、それ以外は0冠へ集約する。
game=0x40000000;native.cpu.mem_map(game,0x800000)
native.helpers={0x81f580:game};native.terminals=set()
acquisition=[]
for mode in [1,2]:
    for crown in range(4):
        address=game+0x3b2b68+17*0x30+2*4
        initial=bytes([3,5,7,11]);native.cpu.mem_write(address,initial)
        value=native.call(0xa092a0,17,2,crown,mode,0)
        slot=crown if mode==2 else 0
        assert value==initial[slot]
        native.call(0xa0956c,17,2,crown,mode,1,0)
        result=bytes(native.cpu.mem_read(address,4));expected=bytearray(initial);expected[slot]=1
        assert result==bytes(expected)
        acquisition.append({'mode':mode,'crown':crown,'slot':slot,'value':value,'after':list(result)})
classifications=[]
for identifier in sorted({stage['rewards']['cells'][6] for stage in witness['stages'] if not stage.get('orphan')} | {-1,0,999,1000,9999,10000,19999,20000,29999,30000}):
    pointer=game+0x38b168;mask=0x01020304
    native.cpu.mem_write(pointer+0xb8,struct.pack('<I',mask))
    native.cpu.mem_write(pointer+0x18,struct.pack('<I',(identifier^mask)&0xffffffff))
    category=native.call(0x7d04f0,0,0)
    assert category==reward_type(identifier)
    classifications.append({'id':identifier,'type':category})
header_normalizations=[]
for kind,column,entry,stop,offset,limit in [('acquisition',1,0x9a46e8,0x9a4708,0,399),('score',2,0x9a485c,0x9a487c,0x6c,199)]:
    for raw in sorted({header[column] for header in headers.values()}|{-1,0,limit,limit+1,2147483647}):
        stack=native.stack+0x8000;destination=native.memory+0x8000
        native.cpu.mem_write(stack+0x18,struct.pack('<Q',destination))
        native.cpu.reg_write(native.reg.UC_ARM64_REG_SP,stack)
        native.helpers={0x464a64:raw&0xffffffff};native.entry=entry;native.terminals={stop}
        native.cpu.emu_start(entry,native.stop,count=100)
        assert native.cpu.reg_read(native.reg.UC_ARM64_REG_PC)==stop
        resolved=struct.unpack('<i',native.cpu.mem_read(destination+offset,4))[0]
        assert resolved==(raw if raw<=limit else -1)
        header_normalizations.append({'kind':kind,'raw':raw,'resolved':resolved})
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,
        'scope':'Header acquisition-save ID resolved from MapStageData; 005dbae4 candidate count and mode dispatch through sequential selection/record or weighted selection before acquisition; normal flag, mode3, original first-item classification, crown2; controlled RNG/radar, saved acquisition or item ownership helpers; not grant or full result screen',
        'evidence':{a:digest((native.cache/'code'/(a+'.c')).read_bytes()) for a in ['005d996c','00a092a0','00a0956c','00a09734','007d04f0','006fea2c','009a3a30']},
        'stageWitnessSha256':digest(witness_path.read_bytes()),'vectors':vectors,'weighted':weighted,'stages':actual,'noReward':skipped,'acquisition':acquisition,'classifications':classifications,'ownershipCases':ownership_cases,'headerNormalizations':header_normalizations}
(ROOT/'research/.local/event-rewards-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    fixture={k:v for k,v in report.items() if k not in ['stages','noReward','ownershipCases']}
    selected={}
    for vector in vectors:
        value=vector['input']
        key=(value['mode'],value['count'],value['acquired'],value['radar'],vector['winner'],vector['consumed'],vector['context']['mode'],vector['context']['saveId']!=-1)
        selected.setdefault(key,vector)
    fixture['vectors']=list(selected.values())
    (ROOT/'native/kbcs-core/tests/event-reward-vectors.json').write_text(json.dumps(fixture,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'stageCases':len(actual),'noReward':len(skipped),'vectors':len(vectors),'weighted':len(weighted)}))
