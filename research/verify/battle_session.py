"""GUIを操作せず、実DBの戦闘セッションをまとめ更新と1F更新で照合する。原本全戦闘の証明ではない。"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import time

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--executable',type=Path,required=True)
parser.add_argument('--input',type=Path,required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parents[2]
source=json.loads(args.input.read_text(encoding='utf-8-sig'))


def run(data,name):
    path=root/'research/.local'/f'{args.input.stem}-{name}.json'
    path.write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8-sig')
    started=time.perf_counter()
    result=subprocess.run([str(args.executable.resolve()),'battle-replay','--input',str(path)],capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr.decode('utf-8',errors='replace'))
    return json.loads(result.stdout),time.perf_counter()-started


batch=copy.deepcopy(source)
for request in batch['requests']:request['debug']=True
# phaseは表示tickの最初だけに渡す。押しっぱなし/5tickガード/コマ送りも同じ順番を維持する。
single=copy.deepcopy(batch);single['requests']=[];ends=[]
for request in batch['requests']:
    ticks=request['input']['ticks']
    if ticks<=1:
        single['requests'].append(copy.deepcopy(request))
    else:
        for i in range(ticks):
            value=copy.deepcopy(request);value['input']['ticks']=1
            if i:
                value['input']['phase']=0
                if value['input']['control']!=10:value['input']['control']=0
            single['requests'].append(value)
    ends.append(len(single['requests'])-1)
first,batch_seconds=run(batch,'batch');second,single_seconds=run(single,'single')
assert len(first)==len(ends)
for index,end in enumerate(ends):
    for key in ['state','runtime','layout']:
        a,b=first[index][key],second[end][key]
        # request_*は当該HTTP batch中の通知。永続状態と混同しない。
        if key=='state':
            a={k:v for k,v in a.items() if not k.startswith('request_')}
            b={k:v for k,v in b.items() if not k.startswith('request_')}
        if key=='runtime':
            beginning=0 if index==0 else ends[index-1]+1
            assert a.get('sounds',[])==[event for v in second[beginning:end+1] for event in v['runtime'].get('sounds',[])],(index,'sound order')
            a={k:v for k,v in a.items() if k!='sounds'};b={k:v for k,v in b.items() if k!='sounds'}
        assert a==b,(index,end,key)
last=first[-1]
report={'input':str(args.input),'executableSha256':hashlib.sha256(args.executable.read_bytes()).hexdigest(),
        'responses':len(first),'singleResponses':len(second),'finalFrame':last['state']['frame'],
        'visualKinds':sorted({effect['kind'] for v in first for effect in v['runtime'].get('visuals',[])}),
        'maxUnits':max(v['runtime']['units'] for v in first),'maxEnemies':max(v['runtime']['enemies'] for v in first),
        'batchSeconds':batch_seconds,'singleSeconds':single_seconds,'result':'equal',
        'limits':['実DB/入力経路とbatch境界の比較。ARM64の全フレーム照合ではない','命中局所の原本比較はactor-hit-1572.json']}
path=root/'research/.local'/f'{args.input.stem}-session-report.json';path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=True))
