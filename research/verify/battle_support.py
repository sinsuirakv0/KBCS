"""15.7.2 ARM64の城体力と、到達済みスニャイパー弾の局所照合。"""
import argparse,json,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--assets',type=Path,required=True)
args=parser.parse_args();sys.path.insert(0,str(args.python_libs))
from stages import Native,Assets,ROOT,SHA
native=Native();game=0x40000000;native.cpu.mem_map(game,0x500000)
with sqlite3.connect((native.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    for address,size in db.execute("SELECT address,size FROM functions WHERE address IN ('0063c560','0058b7d4','005ced48','00a9327c','00a5b084','009e505c','00aa0568')"):
        native.ends[int(address,16)]=int(address,16)+size
assets=Assets(args.assets);rows=[row['cells'] for row in assets.numeric('Data/CC_Castle_growth.csv')]
table=native.memory+0x1000
native.cpu.mem_write(table,b''.join(struct.pack('<4i',*row) for row in rows))
native.cpu.mem_write(native.memory+0x18,struct.pack('<QQ',table,table+16*len(rows)))
growth=[]
for level in [1,2,10,11,20,21,30]:
    native.helpers={};actual=native.call(0x63c560,native.memory,level)
    assert actual==(level-1)*4000;growth.append({'level':level,'result':actual})
castles=[]
for facility,development,treasure,combo in [(1,1,0,0),(4,1,0,0),(5,10,21000,0),(8,20,12345,10),(9,30,21000,0),(20,1,21000,0),(30,30,42000,0),(30,30,42000,20)]:
    native.helpers={0x58b674:facility-1,0x81f580:game,0x8cfcf0:0,0x63c560:(development-1)*4000,0xa5b084:treasure,0x88f9e4:combo}
    actual=native.call(0x58b7d4)
    castles.append({'input':{'facilityLevel':facility,'developmentLevel':development,'treasureBonus':treasure,'comboPercent':combo},'maximum':actual,'sniper':actual//20})
snipers=[]
for maximum,metal,active,chance,roll in [(215000,0,0,0,0),(215019,0,0,0,99),(215000,1,0,0,0),(215000,0,1,0,0),(215000,0,0,50,49),(215000,0,0,50,50)]:
    native.cpu.mem_write(game+0x32e0b0,bytes(0x1000))
    native.cpu.mem_write(game+0x32e0b0+400,struct.pack('<i',1))
    native.cpu.mem_write(game+0x32e308,b'\1')
    native.cpu.mem_write(game+0x8408c+0xc804+0x3ec,struct.pack('<i',100))
    native.cpu.mem_write(game+0x840dc+0xc804+0x3ec,bytes(4))
    damage=[];bounds=[];dodged=[]
    def random():
        bound=native.cpu.reg_read(native.reg.UC_ARM64_REG_X0);bounds.append(bound)
        return roll if len(bounds)==1 else 0
    def hit():
        damage.append(native.cpu.reg_read(native.reg.UC_ARM64_REG_X2));return 0
    def text():
        native.cpu.mem_write(native.cpu.reg_read(native.reg.UC_ARM64_REG_X0),bytes(24));return 0
    def dodge():dodged.append(True);return 0
    native.helpers={0xa94484:1,0xa94678:1,0xa9cc4c:active,0xa9b790:chance,0xa9b81c:30,0xa9cc8c:dodge,0xa9cd6c:0,0xa94074:text,0xa96cd8:metal,0xa9bbac:hit,0xa9327c:maximum//20,0x44a8d8:random}
    native.call(0x5ced48,game,1,1,0)
    knocked=struct.unpack('<i',native.cpu.mem_read(game+0x840dc+0xc804+0x3ec,4))[0]
    snipers.append({'input':{'castleMaximum':maximum,'metal':metal,'dodgeActive':active,'dodgeChance':chance,'roll':roll},'output':{'damage':damage[0] if damage else 0,'knockback':knocked,'randomConsumed':len(bounds),'dodged':int(bool(dodged))},'randomBounds':bounds})
# 00a5b084自体も実行し、日本編だけを渡す入力テストに閉じない。
treasures=[]
vectors=native.memory+0x3000
native.cpu.mem_write(vectors,bytes(24*10))
for chapter in [0,1,2,4,5,6]:
    data=native.memory+0x4000+chapter*0x300
    native.cpu.mem_write(data,b''.join(struct.pack('<12i',*([0]*9+[999,0,0])) for _ in range(11)))
    native.cpu.mem_write(vectors+24*chapter,struct.pack('<QQQ',data,data+11*48,data+11*48))
    group=4 if chapter<3 else 2
    native.cpu.mem_write(data+48*group+0x24,struct.pack('<ii',0,7000))
for percentages in [[100]*6,[100,100,100,0,0,0],[0,0,0,100,100,100],[33,0,0,1,0,0]]:
    for chapter,percent in zip([0,1,2,4,5,6],percentages):
        group=4 if chapter<3 else 2
        native.cpu.mem_write(game+0x83e90+chapter*0x2c+group*4,struct.pack('<i',percent))
    native.helpers={0x81f580:game}
    actual=native.call(0xa5b084,vectors,0)
    assert actual==sum(p*7000//100 for p in percentages)
    treasures.append({'percentages':percentages,'result':actual})

# 009e505cの選択済み制限ノード。個体数・資金などの動的判定は含めない。
deployments=[]
manager,node,group_node=native.memory+0x7000,native.memory+0x8000,native.memory+0x8100
for rarity,slot,cost,mask,slots,minimum,maximum,group_type,in_group,phase in [
    *[(rarity,0,75,6,0,0,0,-1,0,1) for rarity in range(6)],
    (1,4,75,0,1,0,0,-1,0,1),(1,5,75,0,1,0,0,-1,0,1),
    (1,0,500,0,0,500,1000,-1,0,1),(1,0,499,0,0,500,1000,-1,0,1),
    (1,0,1001,0,0,500,1000,-1,0,1),(1,0,750,0,0,1000,500,-1,0,1),
    (1,0,500,0,0,1000,500,-1,0,1),(1,0,1000,0,0,1000,500,-1,0,1),
    *[(1,0,75,0,0,0,0,group_type,member,phase) for group_type,member,phase in [(0,0,1),(0,1,1),(1,0,1),(1,0,0),(2,1,1),(2,0,1)]]]:
    native.cpu.mem_write(game+0x32ff0c,struct.pack('<i',3))
    native.cpu.mem_write(game+0x39781c,bytes(4));native.cpu.mem_write(game+0xc428,bytes(4))
    native.cpu.mem_write(game+0xc400,struct.pack('<10i',*([2]*10)))
    native.cpu.mem_write(manager,bytes(0x60));native.cpu.mem_write(node,bytes(0x60));native.cpu.mem_write(group_node,bytes(0x60))
    native.cpu.mem_write(manager+8,struct.pack('<Q',node))
    native.cpu.mem_write(node+0x24,struct.pack('<6i',mask,0,slots,minimum,maximum,0))
    if group_type>=0:
        native.cpu.mem_write(manager+0x20,struct.pack('<Q',group_node))
        values=native.memory+0x8200
        native.cpu.mem_write(values,struct.pack('<i',0 if in_group else 999))
        native.cpu.mem_write(group_node+0x28,struct.pack('<QQ',values,values+4))
        native.cpu.mem_write(group_node+0x58,struct.pack('<i',group_type))
    native.helpers={0x81f580:game,0x9e4ef8:0,0x63eaf8:0,0x63e4a8:rarity,0x5c2710:1,0xaa0568:cost*100,0x644304:0}
    actual=native.call(0x9e505c,manager,slot,phase)
    deployments.append({'input':dict(rarity=rarity,slot=slot,cost=cost,mask=mask,slots=slots,minimum=minimum,maximum=maximum,group_type=group_type,in_group=in_group,phase=phase,rarity_limit=-1,preceding=0),'allowed':bool(actual)})

costs=[]
for raw,reduction,chapter,multiplier,fixed,rate in [(75,0,0,0,-1,100),(75,0,1,0,-1,100),(75,0,2,0,-1,100),(101,10,1,0,-1,100),(101,200,1,0,-1,100),(101,10,1,125,-1,50),(101,10,1,0,500,50)]:
    native.cpu.mem_write(game+0x9fd80,struct.pack('<i',raw*100));native.cpu.mem_write(game+0x38fad8,struct.pack('<i',chapter))
    vector=native.memory+0x9000;values=native.memory+0x9100
    native.cpu.mem_write(values,struct.pack('<6i',*([rate]*6)))
    native.cpu.mem_write(vector,struct.pack('<QQQ',values,values+24,values+24))
    fixed_vector=native.memory+0x9200;fixed_values=native.memory+0x9300
    native.cpu.mem_write(fixed_values,struct.pack('<i',max(0,fixed)))
    native.cpu.mem_write(fixed_vector,struct.pack('<QQQ',fixed_values,fixed_values+4,fixed_values+4))
    def rules():
        kind=native.cpu.reg_read(native.reg.UC_ARM64_REG_X2)
        return fixed_vector if kind==4 and fixed>=0 else vector if kind==5 else 0
    native.helpers={0x81f580:game,0x644304:rules,0x5c2710:1,0xa9f0e0:reduction,0x7cf950:0,0x7cf370:multiplier,0x63e4a8:0}
    # maxの符号付き比較だけをスタブへ分離する。
    def clamp():
        value=native.cpu.reg_read(native.reg.UC_ARM64_REG_X0)&0xffffffff
        return max(0,value-0x100000000 if value&0x80000000 else value)
    native.helpers[0x44abe4]=clamp
    actual=native.call(0xaa0568,0,0,1,0xffffffff)
    costs.append({'input':dict(raw=raw,reduction=reduction,chapter=chapter,multiplier=multiplier,fixed=fixed,rarity_rate=rate),'cost':actual//100})

report={'version' :'15.7.2','abi':'arm64-v8a','sha256':SHA,'sources':assets.sources,'growth':growth,'castles':castles,'snipers':snipers,'treasures':treasures,'deployments':deployments,'costs':costs}
path=ROOT/'native/kbcs-core/tests/battle-support-vectors.json';path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8-sig')
print(json.dumps({'castleCases':len(castles),'sniperCases':len(snipers),'growth':len(growth),'treasures':len(treasures),'deployments':len(deployments),'costs':len(costs),'randomBounds':[case['randomBounds'] for case in snipers]}))
