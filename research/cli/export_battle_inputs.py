"""版固定のparam/本能玉属性と、BattleTextureContextの確認済みモーション参照を出力する。"""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/verify'))
from stages import Assets,SHA

def recent_inline_name(before,heap,declarations):
    # local_f0の短い文字列が、直前のヒープ文字列を置き換える経路も読む。
    tags=list(re.finditer(r'local_f0\._0_1_ = (0x[0-9a-f]+|\d+);',before))
    if not tags or tags[-1].start()<max(heap,before.rfind('FUN_00469f7c(&local_f0,')) or int(tags[-1][1],0)&1:return None
    data=bytearray(24);written=set()
    for line in before[tags[-1].start():].splitlines():
        field=re.search(r'local_f0\._(\d+)_(\d+)_ = (0x[0-9a-f]+|\d+);',line)
        stack=re.search(r'(uStack|bStack|abStack)_([0-9a-f]+)(?:\[(\d+)\])? = (0x[0-9a-f]+|\d+);',line)
        if field:at,size,value=int(field[1]),int(field[2]),int(field[3],0)
        elif stack:
            kind,offset,index,value=stack.groups();at=0xf0-int(offset,16)+(int(index) if index else 0)
            size=1 if index else declarations.get(kind+'_'+offset,1);value=int(value,0)
        else:continue
        if 0<=at and at+size<=24:
            data[at:at+size]=value.to_bytes(size,'little');written.update(range(at,at+size))
    length=data[0]//2
    assert length<=22 and set(range(length+1))<=written,'incomplete inline filename'
    return data[1:length+1].decode('ascii')

assets=Assets(Path(sys.argv[1]))
reference=json.loads((ROOT/'research/.local/reference.json').read_text(encoding='utf-8-sig'))
identity=json.loads((Path(reference['cache'])/'identity.json').read_text(encoding='utf-8-sig'))
assert identity['version']=='15.7.2' and identity['architecture']=='arm64-v8a' and identity['sha256']==SHA
source=(Path(reference['cache'])/'code/009f560c.c').read_text(encoding='utf-8-sig')
parameters={}
for line in assets.text('Data/param.tsv').splitlines():
    if '\t' not in line:continue
    key,value=line.split('\t',1)
    try:parameters[key]=int(value)
    except ValueError:continue
cannon={'status':[r['cells'] for r in assets.numeric('Data/CC_AllParts_status.csv')], 'growth':[r['cells'] for r in assets.numeric('Data/CC_AllParts_growth.csv')]}
attributes=assets.text('Data/equipment_attribute.csv')
masks=[sum(1<<i for i,v in enumerate(line.split(',')) if v.strip()=='1') for line in attributes.splitlines()[1:] if line.strip()]
declarations={name:int(kind[-1]) if kind.startswith('undefined') else 1 for kind,name in re.findall(r'\b(undefined[1248]|byte|char) ((?:local|uStack|bStack)_[0-9a-f]+);',source)}
models={}
for offset in [0x1988,0x1a68,0x1de8,0x2168,0x2248,0x30d8,0x3148,0x27f8,0x2830,0x29d8,0x2a10,0x10e8,0x1040,0x1528,0x1b48,0x16e8,0x1d08,0x1608,0x1c28,0x17c8,0x18a8,0x1ec8,0x1fa8,0x2088,0x2dc8,0x2e00,0x35b8,0x35f0,0x3628,0x16480,0x16560]:
    end=source.index('FUN_0044ba98(param_1 + '+hex(offset//8))
    before=source[:end]
    head=list(re.finditer(r'  local_1e0 = (0x[0-9a-f]+);',before))[-1]
    heap=before.rfind('  pcVar56 = operator_new(')
    data=bytearray(100)
    if heap>head.start():
        block=before[heap:]
        for match in re.finditer(r'\*\(undefined8 \*\)(?:\(pcVar56 \+ (0x[0-9a-f]+|\d+)\)|pcVar56) = (0x[0-9a-f]+);',block):
            at=int(match[1],0) if match[1] else 0
            data[at:at+8]=int(match[2],0).to_bytes(8,'little')
        name=data.split(b'\0')[0].decode('ascii')
    else:
        for name,at,value in re.findall(r'  ((?:local|uStack|bStack)_([0-9a-f]+)) = (0x[0-9a-f]+|\d+);',before[head.start():]):
            at=0x1e0-int(at,16)
            if 0<=at<24:
                size=declarations.get(name,1);data[at:at+size]=int(value,0).to_bytes(size,'little')
        name=data[1:1+data[0]//2].decode('ascii')
    name=recent_inline_name(before,heap,declarations) or name
    assert name.endswith('.maanim'),(hex(offset),name)
    path='ImageData/'+name
    assert path in assets.files,path
    models[hex(offset)]=path
# 009f560cの書式文字列ループ。配列先頭と0x38刻み、suffix順を原本から固定する。
for base,prefix,suffixes in [(0x2328,'skill_barrier_e',['','_destruction','_breaker']),
                             (0x2478,'skill_demonshield',['00','01','_revive','_destruction','_breaker'])]:
    for index,suffix in enumerate(suffixes):
        path='ImageData/'+prefix+suffix+'.maanim'
        assert path in assets.files,path
        models[hex(base+index*0x38)]=path
(ROOT/'research/.local/battle-clock-models.json').write_text(json.dumps(models,indent=2),encoding='utf-8-sig')
target=ROOT/'crates/kbcs-data/resources/battle-inputs.json'
previous=json.loads(target.read_text(encoding='utf-8-sig')) if target.exists() else {}
output={'version':'15.7.2','versionCode':1507021,'parameters':parameters,'equipmentMasks':masks,'sources':assets.sources,'cannon':cannon,
        'clockSource':{'function':'009f560c','sha256':hashlib.sha256(source.encode()).hexdigest(),'loader':'0044ba98','lengths':['0044beb4','0044bf2c']},
        'clocks':{k:v for k,v in previous.get('clocks',{}).items() if models.get(k)==v['path']}}
target.write_text(json.dumps(output,separators=(',',':')),encoding='utf-8-sig')
print(json.dumps({'parameters':len(parameters),'masks':len(masks),'models':models}))
