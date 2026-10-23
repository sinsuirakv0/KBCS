"""EX候補・直接EXの優先順と、同じ実乱数状態の消費を現版ARM64で照合する。"""
import argparse
import csv
import io
import json
from pathlib import Path
import sqlite3
import struct
import sys
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--assets',type=Path,required=True)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,Assets,ROOT,SHA,digest,read_json
class ExNative(Native):
    def hook(self,cpu,address,size,data):
        if hasattr(self,'returns'):
            if self.returns and address==self.returns[-1]:
                self.rolls.append(cpu.reg_read(self.reg.UC_ARM64_REG_W0));self.returns.pop()
            if address==0x44a8d8:
                self.bounds.append(cpu.reg_read(self.reg.UC_ARM64_REG_W0));self.returns.append(cpu.reg_read(self.reg.UC_ARM64_REG_LR))
            if address==0x5e1d20:
                value=cpu.reg_read(self.reg.UC_ARM64_REG_W0);self.group=value if value<0x80000000 else value-0x100000000
        if hasattr(self,'allowed') and address not in self.helpers and address not in self.terminals and address!=self.stop:
            if 0x44a8d8<=address<0x44aa50 or any(a<=address<b for a,b in self.allowed):return
        super().hook(cpu,address,size,data)
native=ExNative();game=0x40000000;native.cpu.mem_map(game,0x800000)
addresses=['006562ac','0065644c','007cd560']
with sqlite3.connect((native.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    native.allowed=[(int(a,16),int(a,16)+size) for a,size in db.execute('SELECT address,size FROM functions WHERE address IN ('+','.join('?' for _ in addresses)+')',addresses)]
native.allowed.append((0x5e1cfc,0x5e23e0))
assets=Assets(args.assets)
def csv_numbers(path):return [list(map(int,row)) for row in csv.reader(io.StringIO(assets.text(path))) if row and row[0].strip().isdigit()]
groups=csv_numbers('Data/EX_group.csv');lottery=csv_numbers('Data/EX_lottery.csv')
group_rows={(row[1],row[2]):row for row in groups}
assert len(group_rows)==len(groups)
def write(address,value,wide=False):native.cpu.mem_write(address,struct.pack('<Q' if wide else '<I',value&((1<<(64 if wide else 32))-1)))
manager=game+0x12b0;table=native.memory+0x4000
for index,row in enumerate(lottery):
    assert len(row)==2 and 4000<=row[0]<5000
    pointer=native.memory+0x5000+index*8;write(table+index*8,pointer,True)
    native.cpu.mem_write(pointer,struct.pack('<ii',*row))
write(manager+0x18,table,True);write(manager+0x20,table+len(lottery)*8,True)

def execute(map_id,stage_index,settings,seed,group_row=None):
    row=group_row if group_row is not None else group_rows.get((map_id,stage_index))
    root,metadata,ids,thresholds=[native.memory+v for v in [0x1000,0x2000,0x3000,0x3100]]
    native.cpu.mem_write(root,bytes(0x80));native.cpu.mem_write(metadata,bytes(0x80))
    write(manager+8,root if row is not None else 0,True)
    choices=[]
    if row is not None:
        write(root+0x20,map_id*100+stage_index);write(root+0x28,metadata,True)
        for index,column in enumerate(range(3,len(row)-1,2)):
            group,threshold=row[column:column+2]
            write(ids+index*4,group);write(thresholds+index*4,threshold)
            target=lottery[group] if group>=0 else [-1,-1]
            choices.append({'group':group,'threshold':threshold,'mapIndex':target[0]-4000 if group>=0 else -1,'stage':target[1]})
        for offset,value in [(8,ids),(0x10,ids+len(choices)*4),(0x20,thresholds),(0x28,thresholds+len(choices)*4)]:write(metadata+offset,value,True)
    chance,map_index,minimum,maximum=settings
    native.cpu.mem_write(game+0x473498,struct.pack('<4i',*settings));native.cpu.mem_write(game+0x40a510,bytes(0x20));write(0xc24d18,seed)
    for name,value in [('SP',native.stack+0x8000),('X19',game),('X27',game+0x40a510),('X28',game+0x473498)]:native.cpu.reg_write(getattr(native.reg,'UC_ARM64_REG_'+name),value)
    native.helpers={0x7cf950:map_id,0x7cfaa0:stage_index};native.entry=0x5e1cfc;native.terminals={0x5e2120,0x5e23dc}
    native.bounds=[];native.rolls=[];native.returns=[];native.group=-1
    native.cpu.emu_start(native.entry,native.stop,count=50000)
    pc=native.cpu.reg_read(native.reg.UC_ARM64_REG_PC);assert pc in native.terminals
    assert len(native.bounds)==len(native.rolls) and not native.returns
    group_roll=native.rolls[0] if row is not None else -1
    selected=next((c for c in choices if group_roll<c['threshold']),None)
    group=selected['group'] if selected else -1;assert native.group==group
    primary=native.rolls[int(row is not None)];direct=primary<chance
    source=1 if direct else 2 if group>=0 else 0
    expected_bounds=([100] if row is not None else [])+[100]+([maximum-minimum+1] if direct else [])
    assert native.bounds==expected_bounds
    if source:
        result_map=struct.unpack('<i',native.cpu.mem_read(game+0x40a514,4))[0];result_stage=struct.unpack('<i',native.cpu.mem_read(game+0x40a51c,4))[0]
        assert result_map==(map_index if direct else selected['mapIndex'])
        assert result_stage==(minimum+native.rolls[-1] if direct else selected['stage'])
    else:result_map=result_stage=-1
    state=struct.unpack('<I',native.cpu.mem_read(0xc24d18,4))[0]
    return {'input':{'chance':chance,'mapIndex':map_index,'minimum':minimum,'maximum':maximum,'groupPresent':int(row is not None)},
            'choices':choices,'seed':seed,'stateAfter':state,'group':group,'source':source,'mapIndex':result_map,'stage':result_stage,
            'consumed':len(native.bounds),'bounds':native.bounds+[0]*(3-len(native.bounds)),'rolls':native.rolls+[0]*(3-len(native.rolls))}

witness_path=ROOT/'research/.local/stages-1572-band1000.json';witness=read_json(witness_path);assert witness['sha256']==SHA
actual=[];vectors=[];seeds=[1,2,3,0x12345678,0xffffffff,0x80000000]
for stage in witness['stages']:
    if stage.get('orphan'):continue
    settings=stage['settings']['cells'][2:6];assert all(v is not None for v in settings)
    for seed in seeds:
        value=execute(stage['map'],stage['stage'],settings,seed)
        actual.append({'map':stage['map'],'stageIndex':stage['stage'],**value})
# 全EX_groupを選択器だけへ通す。他番台の戦闘全体の検証とは区別する。
selectors=[]
for row in groups:
    for seed in [1,0x12345678]:selectors.append(execute(row[1],row[2],[0,0,0,0],seed))
for chance in [0,1,100]:
    for seed in seeds:
        vectors.append(execute(1000,0,[chance,0,2,2],seed,[100,1000,0,0,50,1,100]))
vectors.append(execute(1000,0,[0,0,0,0],1,[100,1000,0]))
selected={}
for value in actual:
    key=(value['input']['groupPresent'],value['source'],tuple(value['bounds']),value['group'])
    selected.setdefault(key,value)
vectors.extend(selected.values())
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,'build':assets.current,
        'scope':'005e1cfc through EX target flags before UI; real 006562ac/0065644c and 0044a8d8 RNG, supplied parsed EX tables and current stage getters; not result-screen timing or EX initialization',
        'evidence':{a:digest((native.cache/'code'/(a+'.c')).read_bytes()) for a in ['005e1a5c','00655a44',*addresses,'0044a8d8','0044a8e8']},
        'sources':assets.sources,'stageWitnessSha256':digest(witness_path.read_bytes()),'vectors':vectors,'stages':actual,'selectors':selectors}
(ROOT/'research/.local/ex-transition-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    fixture={k:v for k,v in report.items() if k not in ['stages','selectors','sources','build']}
    (ROOT/'native/kbcs-core/tests/ex-vectors.json').write_text(json.dumps(fixture,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'stageCases':len(actual),'groupCases':len(selectors),'vectors':len(vectors)}))
