"""1000番台S系列を全件棚卸しし、分類・出現行読込・冠の共通部分を照合する。"""
import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import re
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--assets',type=Path,required=True)
parser.add_argument('--python-libs',type=Path,required=True)
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Assets,Native,ROOT,SHA,digest

assets=Assets(args.assets);native=Native()
metadata={int(m[1]):name for name in assets.files if (m:=re.fullmatch(r'Data/MapStageDataS_(\d+)\.csv',name))}
definitions={(int(m[1]),int(m[2])):name for name in assets.files if (m:=re.fullmatch(r'Data/stageRS(\d+)_(\d+)\.csv',name))}
options={row['cells'][0]:row for row in assets.numeric('Data/Map_option.csv',19) if 1000<=row['cells'][0]<2000}
limits=[row for row in assets.numeric('Data/Stage_option.csv',9) if 1000<=row['cells'][0]<2000]
maps=[];stages=[];used=set();modes=Counter();features=Counter();rows_count=0;crowns_count=0
conversions=[]

def definition_rows(path):
    result=[]
    for line,text in enumerate(assets.text(path).splitlines(),1):
        cells=next(csv.reader([text.split('//',1)[0]])) if text.strip() else []
        if not cells or not re.fullmatch(r'-?\d+',cells[0].strip()):continue
        values=[]
        for column,cell in enumerate(cells):
            if cell.strip()=='.':
                # 本家のセル取得はstrtol(文字列, end, 10)。原文と変換を別に保持する。
                native.cpu.mem_write(native.memory+0x130,(native.stop+0x100).to_bytes(8,'little'))
                native.cpu.mem_write(native.memory+0x300,(native.memory+0x400).to_bytes(8,'little'))
                native.cpu.mem_write(native.memory+0x400,b'.\0')
                def strtol():
                    assert native.cpu.reg_read(native.reg.UC_ARM64_REG_X0)==native.memory+0x400
                    assert native.cpu.reg_read(native.reg.UC_ARM64_REG_X2)==10
                    return 0
                native.helpers={native.stop+0x100:native.memory+0x300,0xbdb640:strtol}
                value=native.call(0x464a64,native.memory,column)
                native.helpers={};assert value==0
                conversions.append({'path':path,'line':line,'column':column,'raw':cell,'value':value,
                                    'scope':'Native getter through strtol delegation; no-digit conversion controlled as 0, Bionic libc not executed'})
                values.append(value)
            else:values.append(int(cell) if cell.strip() else None)
        result.append({'line':line,'cells':values,'raw':cells})
    return result
for index,path in sorted(metadata.items()):
    identifier=1000+index
    assert native.call(0x7cd120,1,index)==identifier
    assert native.call(0x7cd2ac,identifier)==1 and native.call(0x7cd560,identifier)==index
    rows=assets.numeric(path);assert len(rows)>=2
    option=options[identifier];values=option['cells'];assert 1<=values[1]<=4
    actual=native.crowns(identifier,values[3:7])[:values[1]]
    assert all(value>0 for value in actual)
    crowns_count+=len(actual)
    maps.append({'id':identifier,'index':index,'path':path,'headers':rows[:2],'options':option,
                 'nativeCrowns':actual,'limits':[row for row in limits if row['cells'][0]==identifier]})
    for number,rewards in enumerate(rows[2:]):
        key=(index,number);assert key in definitions,key
        used.add(key);mode=rewards['cells'][8] if len(rewards['cells'])>8 else None;modes[mode]+=1
        stages.append({'map':identifier,'index':index,'stage':number,'rewardMode':mode,'rewards':rewards,'path':definitions[key]})

# メタ情報に現れない原本2件も削除せず、孤立定義として区別して調べる。
for key,path in sorted(definitions.items()):
    rows=definition_rows(path);assert len(rows)>=3,path
    loaded=[];terminated=False
    for row in rows[2:]:
        decoded=native.spawn(row['cells']);rows_count+=1
        if not native.call(0xa06c30,native.memory+0x200):terminated=True;break
        assert native.call(0xa06c48,native.memory+0x200)==decoded[0]-2
        assert native.call(0xa06cb8,native.memory+0x200)==(decoded[11] or decoded[9])
        loaded.append({**row,'native':decoded})
        for name,active in [('negativeFirst',decoded[2]<0),('explicitAttack',decoded[11]!=0),
                            ('castleWait',decoded[12]!=0),('killGate',decoded[13]!=0),
                            ('extraColumns',len(row['cells'])>14)]:features[name]+=int(active)
    entry=next((stage for stage in stages if (stage['index'],stage['stage'])==key),None)
    # 0099fe4cは行取得の成否も判定するため、数値0の終端を必須にしない。
    # コメント/空行を含むCSVパーサー全体の実行とは区別して記録する。
    definition={'settings':rows[0],'header':rows[1],'spawns':loaded,'numericTerminator':terminated}
    if entry is not None:entry.update(definition)
    else:stages.append({'map':1000+key[0],'index':key[0],'stage':key[1],'path':path,'orphan':True,**definition})
assert len(used)==sum(not stage.get('orphan') for stage in stages)
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,'build':assets.current,
        'scope':'Band1000 S/RS inventory; full source hashes, native ID mapping, crown getter and common 14-cell reader; not full stage loading, reward modes or battle execution',
        'evidence':{a:digest((native.cache/'code'/(a+'.c')).read_bytes()) for a in ['0099fe4c','009a3a30','007cd120','007cd2ac','007cd560','007cebc8','00a06ae4','00a06cb8']},
        'maps':maps,'stages':stages,'sources':assets.sources,'rewardModes':dict(modes),
        'features':dict(features),'decodedRowsIncludingTerminators':rows_count,'activeCrowns':crowns_count,
        'conversions':conversions,
        'withoutNumericTerminator':[stage['path'] for stage in stages if not stage['numericTerminator']],
        'orphans':[{'map':1000+i,'stage':j,'path':definitions[(i,j)]} for i,j in sorted(definitions.keys()-used)]}
(ROOT/'research/.local/stages-1572-band1000.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8-sig')
print(json.dumps({'maps':len(maps),'metadataStages':len(used),'definitions':len(stages),'activeCrowns':crowns_count,
                  'decodedRows':rows_count,'rewardModes':dict(modes),'features':dict(features),'orphans':report['orphans'],
                  'withoutNumericTerminator':len(report['withoutNumericTerminator'])},ensure_ascii=True))
