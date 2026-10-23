"""現版ARM64の敵HP・各攻撃のステージ倍率、冠、クリスタル補正を照合する。"""
import argparse
import json
from pathlib import Path
import struct
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--assets',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,Assets,ROOT,SHA,digest,read_json

class EnemyNative(Native):
    def hook(self,cpu,address,size,data):
        if address in range(0xa06cb0,0xa06ce4):return
        super().hook(cpu,address,size,data)

native=EnemyNative();game=0x40000000;native.cpu.mem_map(game,0x800000)
native.ends.update({0xa9e9fc:0xa9f0e0,0xa9fb88:0xaa02d0})
columns=list(struct.unpack('<3i',native.cpu.mem_read(0x2f48dc,12)))
assert columns==[3,55,56],columns

def write(offset,value):native.cpu.mem_write(game+offset,struct.pack('<i',value))

def execute(case):
    kind=case['kind'];hit=case.get('hit',0);star=case.get('star',0)
    base=game+0x239da8+2*0x1c4
    for column in [0,3,55,56,18,69]:native.cpu.mem_write(base+column*4,bytes(4))
    native.cpu.mem_write(base+(0 if kind=='health' else columns[hit])*4,struct.pack('<i',case['base']))
    native.cpu.mem_write(base+18*4,struct.pack('<i',case.get('alien',0)))
    native.cpu.mem_write(base+69*4,struct.pack('<i',star))
    write(0x32f934,3);write(0x334048,0)
    row=native.memory+0x2000
    native.cpu.mem_write(game+0x9ee70,struct.pack('<Q',row))
    values=[0]*14;values[9]=case['healthRate'];values[11]=case['attackRate']
    native.cpu.mem_write(row,struct.pack('<14i',*values))
    treasure_calls=[]
    def treasure(maximum):
        effect=native.cpu.reg_read(native.reg.UC_ARM64_REG_W1)
        treasure_calls.append([maximum,effect])
        assert effect=={0:16,1:18,2:22,3:23,4:24}[star]
        return case['crystalMax'] if maximum else case['crystalTreasure']
    native.helpers={0x81f580:game,0x5c2710:0,0x7cf950:0,0x7cfcd8:0,
                    0x7cebc8:case['crown'],0xa5b2d8:lambda:treasure(True),0xa5b084:lambda:treasure(False)}
    actual=native.call(0xa9e9fc if kind=='health' else 0xa9fb88,1,0,0,1,0,hit,0,case.get('castleAttack',0))
    rate=case['healthRate'] if kind=='health' or not case['attackRate'] else case['attackRate']
    rounded=(case['base']*rate+50)//100
    crowned=rounded*(100 if kind=='attack' and case.get('castleAttack') else case['crown'])//100
    expected=crowned+crowned*(case['crystalMax']-case['crystalTreasure'])//100
    assert actual==expected,(case,actual,expected)
    return {'input':{'base':case['base'],'rowPercent':rate,'crownPercent':case['crown'],
                     'crystalMax':case['crystalMax'],'crystalTreasure':case['crystalTreasure'],
                     'castleAttack':case.get('castleAttack',0) if kind=='attack' else 0},
            'stages':[rounded,crowned,actual],'treasureCalls':treasure_calls}

vectors=[]
for base,rate,crown,star,alien,maximum,treasure,castle,attack in [
    (1,149,150,0,0,0,0,0,0),(1,150,150,0,0,0,0,0,0),
    (101,125,170,0,0,0,0,0,0),(101,125,170,0,0,0,0,1,75),
    (101,0,150,0,0,0,0,0,0),(101,1,150,0,0,0,0,0,0),
    (101,125,170,0,1,600,397,0,0),(101,125,170,1,1,1500,999,0,0),
    (101,125,170,2,1,1000,333,0,0),(101,125,170,3,1,1000,1000,0,0),
    (101,125,170,4,1,1000,0,1,0),(103,97,170,0,1,600,599,0,199),
]:
    for kind,hit in [('health',0),('attack',0),('attack',1),('attack',2)]:
        case=dict(kind=kind,hit=hit,base=base,healthRate=rate,attackRate=attack,crown=crown,
                  star=star,alien=alien,crystalMax=maximum,crystalTreasure=treasure,castleAttack=castle)
        vectors.append({'case':case,**execute(case)})

assets=Assets(args.assets);enemies=assets.numeric('Data/t_unit.csv')
# 元CSVは2予約行を含む。既存読込の行対応を変更しない。
rows=[entry['cells'] for entry in enemies]
witness=read_json(ROOT/'research/.local/stages-1572-band0.json')
crowns={entry['id']:entry['nativeCrowns'] for entry in witness['maps']}
seen=set();actual=[];covered=0
for stage in witness['stages']:
    for spawn in stage['spawns']:
        row=spawn['loaded'];raw=rows[row[0]];star=raw[69] or 0;alien=raw[18] or 0
        maximum=1500 if star==1 else 1000 if star>1 else 600 if alien else 0
        castle=row[0]==stage['header']['cells'][6]
        for crown in crowns[stage['map']]:
            covered+=1;key=(row[0],row[9],row[11],crown,castle)
            if key in seen:continue
            seen.add(key)
            for kind,hit in [('health',0),('attack',0),('attack',1),('attack',2)]:
                case=dict(kind=kind,hit=hit,base=raw[0 if kind=='health' else columns[hit]] or 0,
                          healthRate=row[9],attackRate=row[11],crown=crown,star=star,alien=alien,
                          crystalMax=maximum,crystalTreasure=maximum,castleAttack=int(castle))
                actual.append({'enemyRaw':row[0],**execute(case)})
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,
        'scope':'Full enemy branches of 00a9e9fc/00a9fb88; kind=3, controlled game singleton, faction flag, crown and crystal aggregate helpers; not actor construction or battle simulation',
        'evidence':{address:digest((native.cache/'code'/(address+'.c')).read_bytes()) for address in ['00a9e9fc','00a9fb88','00a06cb0','00a06cb8','009f1e64']},
        'sources':assets.sources,'vectors':vectors,'coveredRowsAndCrowns':covered,'profiles':actual}
(ROOT/'research/.local/enemy-stats-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    fixture={key:value for key,value in report.items() if key not in ['sources','profiles']}
    (ROOT/'native/kbcs-core/tests/enemy-stat-vectors.json').write_text(json.dumps(fixture,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'boundaries':len(vectors),'rowCrowns':covered,'nativeProfiles':len(actual)}))
