from pathlib import Path
import sys,json,hashlib,struct
import argparse
parser=argparse.ArgumentParser(description='15.7.2 ARM64の局所実行による計算照合')
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--assets',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args()
sys.path.insert(0,str(args.python_libs.resolve()))
root=Path(__file__).resolve().parents[2]
reference=json.loads((root/'research/.local/reference.json').read_text(encoding='utf-8-sig'))
cache=Path(reference['cache'])
identity=json.loads((cache/'identity.json').read_text(encoding='utf-8-sig'))
assert identity['version']=='15.7.2' and identity['architecture']=='arm64-v8a'
assert reference['sha256']==identity['sha256']
from unicorn import Uc,UC_ARCH_ARM64,UC_MODE_ARM,UC_HOOK_CODE
from unicorn.arm64_const import *
from elftools.elf.elffile import ELFFile
binary=Path(identity['binary'])
sha=hashlib.sha256(binary.read_bytes()).hexdigest();assert sha=='6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea'
with binary.open('rb') as f:
 elf=ELFFile(f);assert elf['e_machine']=='EM_AARCH64';segments=[(s['p_vaddr']+0x100000,s.data(),s['p_memsz']) for s in elf.iter_segments() if s['p_type']=='PT_LOAD']
image=bytearray((max(a+n for a,d,n in segments)+4095)//4096*4096)
for a,d,n in segments:image[a:a+len(d)]=d
regs=[UC_ARM64_REG_X0,UC_ARM64_REG_X1,UC_ARM64_REG_X2,UC_ARM64_REG_X3,UC_ARM64_REG_X4,UC_ARM64_REG_X5,UC_ARM64_REG_X6,UC_ARM64_REG_X7]
def execute(kind,base,level,treasure,combo,talent,extra,rates):
 u=Uc(UC_ARCH_ARM64,UC_MODE_ARM);u.mem_map(0,len(image));u.mem_write(0,bytes(image))
 game=0x20000000;stack=0x30000000;stop=0x60000000
 u.mem_map(game,0x800000);u.mem_map(stack,0x10000);u.mem_map(stop,4096)
 for offset in [0,12,59*4,60*4]:u.mem_write(game+2*0x770+0x9ee88+offset,struct.pack('<I',base))
 for i,value in enumerate(rates):u.mem_write(game+0x44fcc4+i*4,struct.pack('<I',value))
 entry=0xa9e9fc if kind=='health' else 0xa9fb88
 trace=[]
 def ret(value):u.reg_write(UC_ARM64_REG_X0,value);u.reg_write(UC_ARM64_REG_PC,u.reg_read(UC_ARM64_REG_LR))
 def hook(uc,address,size,data):
  trace.append(hex(address));trace[:]=trace[-8:]
  if address==stop:u.emu_stop()
  elif address==0x81f580:ret(game)
  elif address==0x5c2710:ret(1)
  elif address==0xa5b084:ret(treasure)
  elif address==0x88f9e4:ret(combo)
  elif address==0xa9f0e0:ret(extra if u.reg_read(UC_ARM64_REG_X3) in [70,71] else talent)
  elif not entry<=address<(0xa9f0e0 if kind=='health' else 0xaa02d0):raise RuntimeError('Unhandled '+hex(address)+' '+str(trace))
 u.hook_add(UC_HOOK_CODE,hook)
 for reg,value in zip(regs,[0,0,0,level,0,0,0,0]):u.reg_write(reg,value)
 u.reg_write(UC_ARM64_REG_SP,stack+0x8000);u.reg_write(UC_ARM64_REG_LR,stop);u.emu_start(entry,stop+4,count=150000)
 return u.reg_read(UC_ARM64_REG_X0)&0xffffffff


def hit(case):
 u=Uc(UC_ARCH_ARM64,UC_MODE_ARM);u.mem_map(0,len(image));u.mem_write(0,bytes(image))
 game=0x20000000;stack=0x30000000;stop=0x60000000;arena=0x40000000
 u.mem_map(game,0x800000);u.mem_map(stack,0x10000);u.mem_map(stop,4096);u.mem_map(arena,0x10000)
 result=None;calls=[];trace=[];allocated=arena;checkpoints={}
 unit_points={0x6e4d84:[0],0x6e4db0:[0],0x6e4dc8:[1],0x6e4eb8:[2],0x6e4f10:[3],0x6e4f6c:[4],0x6e4fc8:[5],0x6e5910:[6],0x6e5a38:[7],0x6e5b78:[8],0x6e5bf4:[9],0x6e5c70:[10],0x6e5cd4:[11],0x6e5dc0:[12],0x6e5ea0:[13],0x6e5ef4:[14],0x6e508c:[15,16,17,18],0x6e50b0:[19]}
 if case.get('castle'):unit_points[0x6e4ff0]=[6,7,8,9,10,11,12,13,14]
 enemy_points={0x6e7c74:[0],0x6e7c9c:[0],0x6e7cb8:[1],0x6e7d78:[2,3],0x6e7dd4:[4],0x6e7e30:[5],0x6e895c:[6],0x6e8ab8:[7],0x6e8cf8:[8],0x6e8da8:[9],0x6e8e58:[10],0x6e8edc:[11],0x6e8fa8:[12],0x6e9074:[13],0x6e90d4:[14],0x6e80cc:[15],0x6e812c:[16],0x6e8590:[17],0x6e8600:[18],0x6e862c:[19]}
 def ret(value=0):u.reg_write(UC_ARM64_REG_X0,value&0xffffffffffffffff);u.reg_write(UC_ARM64_REG_PC,u.reg_read(UC_ARM64_REG_LR))
 def hook(uc,address,size,data):
  nonlocal result,allocated
  if address==stop:u.emu_stop();return
  for index in (enemy_points if case.get('incoming') else unit_points).get(address,[]):checkpoints[str(index)]=u.reg_read(UC_ARM64_REG_X23 if case.get('incoming') or address==0x6e50b0 else UC_ARM64_REG_X24)
  if (0x6e79bc<=address<0x6e92bc if case.get('incoming') else 0x6e4aec<=address<0x6e60f0):return
  args=[u.reg_read(r)&0xffffffff for r in regs];calls.append((hex(address),args[:5]))
  values={0xa94678:1,0x81f580:game,0x5bbc10:1 if case.get('castle') else 0xffffffff,0x5bce20:2,0xa95a68:case.get('attack',13),0xa958b0:1 if case.get('strengthen',0) else 100,0xa95824:case.get('maxHp',100),0xa9876c:case.get('poison',0),0xa9e20c:case.get('poisonResistance',0),0xa9b8a8:case.get('poisonImmune',0),0xa998cc:50 if case.get('strengthen',0) else 0,0xa99958:case.get('strengthen',0),0xa9c3bc:int(case.get('weaken',100)<100),0xa9c49c:1,0xa9c528:case.get('weaken',100),0xa9a9b0:case.get('savage',0),0xa99c24:case.get('strong',0),0xa99de4:case.get('massive',0),0xa99fa4:case.get('extreme',0),0xa99d04:case.get('resistant',0),0xa99ec4:case.get('superResistant',0),0xa9a2cc:case.get('witch',0),0xa97068:case.get('witch',0),0xa9a3ac:case.get('eva',0),0xa970d8:case.get('eva',0),0xa9a48c:case.get('colossus',0),0xa976b8:case.get('colossus',0),0xa9a56c:160,0xa9a6dc:70,0xa96a38:int(case.get('baseReduction',0)>0),0xa9e068:case.get('resistance',0),0xa9e298:case.get('resistance',0),0xa9e324:case.get('resistance',0),0xa9b024:case.get('immune',0),0xa9b93c:case.get('immune',0),0xa9b9d0:case.get('immune',0),0xa999e4:2 if case.get('killStrengthen') else 0,0xa978ec:case.get('villain',0),0xa9aa88:case.get('behemoth',0),0xa97774:case.get('behemoth',0),0xa9ad10:case.get('sage',0),0xa97830:case.get('sage',0),0xa96cd8:case.get('metal',0),0xa5b1b4:case.get('fruit',300),0xa9fb88:case.get('raw',8)}
  if address==0x44abe4:ret(max(args[0],args[1]));return
  if address==0x63a050:ret(case.get('baseReduction',0) if args[1]==100 else case.get('decorationReduction',0) if args[1] in [0xc9,0xcb] else case.get('decoration',0) if args[1]==0xcd else 0);return
  if address in allocations:
   pointer=allocated;allocated+=0x100;ret(pointer);return
  if address==0x41b298:
   text=bytearray();pointer=u.reg_read(UC_ARM64_REG_X1)
   while u.mem_read(pointer+len(text),1)!=b'\0':text.extend(u.mem_read(pointer+len(text),1))
   dest=u.reg_read(UC_ARM64_REG_X0)
   if len(text)<=22:u.mem_write(dest,bytes([len(text)*2])+bytes(text)+b'\0')
   else:
    pointer=allocated;allocated+=0x100;u.mem_write(pointer,bytes(text)+b'\0');u.mem_write(dest,struct.pack('<QQQ',0x101,len(text),pointer))
   ret(dest);return
  if address==0x9019f4:
   pointer=u.reg_read(UC_ARM64_REG_X1);first=u.mem_read(pointer,1)[0]
   if first&1:length=struct.unpack('<Q',u.mem_read(pointer+8,8))[0];pointer=struct.unpack('<Q',u.mem_read(pointer+16,8))[0]
   else:length=first//2;pointer+=1
   name=bytes(u.mem_read(pointer,length)).decode('ascii',errors='replace');ret(case.get('waveRate',parameters.get(name,args[2])) if name=='battle_wave_s_st' else parameters.get(name,args[2]));return
  if address==0xa962a8:ret(int(case.get('incoming') or args[0]==0));return
  if address==0xa9a158:ret(case.get('castleBreaker',0));return
  if address==0x88f9e4:ret(case.get('combos',{}).get(str(args[1]),0));return
  if address==0x66398c:ret(case.get('killStrengthen',0));return
  if address==0x663c44:ret(case.get('orbs',{}).get(str(args[2]),0));return
  if address==0xa9bbac:result=args[2];checkpoints['20']=result;u.emu_stop();return
  ret(values.get(address,0))
 u.hook_add(UC_HOOK_CODE,hook)
 sp=stack+0x8000
 # param_1..8はレジスタ、param_9..19は8バイト間隔のスタック。
 for reg,value in zip(regs,[game,case.get('incomingType',0),1,1,0,case.get('attackKind',0),case.get('critical',0),int(case.get('savage',0)>0)]):u.reg_write(reg,value)
 u.mem_write(sp,b'\0'*88);u.mem_write(sp+56,struct.pack('<Q',int(case.get('poison',0)>0)));u.mem_write(sp+80,struct.pack('<Q',case.get('attackScale',100)))
 u.reg_write(UC_ARM64_REG_SP,sp);u.reg_write(UC_ARM64_REG_LR,stop)
 u.emu_start(0x6e79bc if case.get('incoming') else 0x6e4aec,stop+4,count=200000)
 if result is None:raise RuntimeError('No damage '+str(calls[-12:]))
 return result,calls,checkpoints
allocations={int(row.split('\t')[0],16) for row in (cache/'catalog.tsv').read_text(encoding='utf-8-sig').splitlines() if 'operator.new' in row}
assets=args.assets.resolve()
current=json.loads((assets/'metadata/jp/current.json').read_text(encoding='utf-8-sig'))
assert current['status']=='verified' and current['versionName']==identity['version']
generated=assets/current['generatedPath'];manifest_bytes=(generated/'manifest.json').read_bytes()
assert hashlib.sha256(manifest_bytes).hexdigest()==current['manifestSha256']
manifest=json.loads(manifest_bytes);index_bytes=(generated/'indexes/assets.json').read_bytes();index_ref=manifest['artifacts']['indexes/assets.json']
assert len(index_bytes)==index_ref['size'] and hashlib.sha256(index_bytes).hexdigest()==index_ref['sha256']
index=json.loads(index_bytes)
for header in [manifest['header'],index['header']]:assert all(header[key]==current[key] for key in ['schemaVersion','datasetId','buildId','sourceRegion','versionCode','versionName'])
param=index['files']['Data/param.tsv'];content=(assets/param['path']).read_bytes()
assert len(content)==param['size'] and hashlib.sha256(content).hexdigest()==param['sha256']
cannon_sources={}
for name in ['Data/CC_BaseParts_growth.csv','Data/CC_DecoParts_growth.csv']:
 entry=index['files'][name];data=(assets/entry['path']).read_bytes()
 assert len(data)==entry['size'] and hashlib.sha256(data).hexdigest()==entry['sha256']
 curves=[list(map(int,line.split(',')))[2:] for line in data.decode('utf-8-sig').splitlines()[1:] if line.strip()]
 assert curves==[[20,75,1500,0]]*7
 cannon_sources[name]=entry
parameters={key:int(value) for line in content.decode('utf-8-sig').splitlines() if '\t' in line for key,value in [line.split('\t',1)] if value.lstrip('-').isdigit()}
assert parameters['battle_metal_killer_hp_type']==1
cases=[{'attack':13},{'attack':13,'critical':1,'strengthen':17,'weaken':57,'savage':43,'strong':1,'fruit':147,'combos':{'14':15}},{'attack':13,'strong':1,'massive':1,'extreme':1,'fruit':147},{'attack':13,'metal':1,'orbs':{'0':500}},{'attack':13,'critical':1,'metal':1,'orbs':{'0':500}}]
cases += [{'attack':103,'incoming':1,'strong':1,'resistant':1,'superResistant':1,'fruit':147},{'attack':103,'incoming':1,'witch':1,'eva':1,'colossus':1},{'attack':103,'critical':1,'incoming':1,'strong':1,'fruit':147,'metal':1},{'attack':103,'incoming':1,'strong':1,'fruit':147,'metal':1}]
for special in ['witch','eva','colossus','behemoth','sage']:
 for incoming in [0,1]:
  cases.append({'attack':103,'incoming':incoming,special:1})
  cases.append({'attack':103,'incoming':incoming,special:1,'critical':1,'strengthen':17,'weaken':57,'savage':43,'strong':1,'fruit':147,'combos':{'14':15,'22':100,'23':100}})
for incoming in [0,1]:cases.append({'attack':10007,'incoming':incoming,'witch':1,'eva':1,'colossus':1,'behemoth':1,'sage':1,'strong':1,'fruit':147,'combos':{'14':15,'22':100,'23':100}})
cases += [{'attack':0,'incoming':1,'maxHp':101,'poison':20},{'attack':0,'incoming':1,'maxHp':101,'poison':20,'poisonResistance':50,'decoration':3333},{'attack':0,'incoming':1,'maxHp':3,'poison':20,'poisonResistance':99},{'attack':0,'incoming':1,'maxHp':101,'poison':20,'poisonImmune':1}]
cases += [{'attack':103,'villain':1,'combos':{'25':2500}},{'attack':103,'incoming':1,'villain':1,'combos':{'25':2500}},{'attack':103,'critical':1,'strengthen':17,'killStrengthen':13,'weaken':57,'savage':43,'strong':1,'fruit':147},{'attack':10007,'witch':1,'eva':1,'colossus':1,'behemoth':1,'sage':1,'villain':1,'combos':{'22':100,'23':100,'25':2500}}]
cases += [{'attack':103,'incoming':1,'baseReduction':1500},{'attack':103,'incoming':1,'incomingType':1,'strong':1,'fruit':147,'combos':{'14':15},'resistance':17,'orbs':{'1':8},'baseReduction':1333,'decorationReduction':1333},{'attack':103,'incoming':1,'incomingType':1,'resistance':17,'orbs':{'1':8},'baseReduction':1333,'decorationReduction':1333,'metal':1},{'attack':103,'incoming':1,'incomingType':1,'immune':1,'baseReduction':1500,'decorationReduction':1500}]
results=[]
cases += [{'attack':103,'castle':1,'castleBreaker':1,'critical':critical,'savage':savage} for critical in [0,1] for savage in [0,43]]
cases += [{'attack':103,'strong':1,'massive':1,'fruit':147,'combos':{'14':15,'15':17},'orbs':{'0':13}}]
cases += [{'attack':10007,'incoming':1,'strong':1,'resistant':1,'fruit':147,'combos':{'14':15,'16':17}}]
cases += [{'attack':10007,'incoming':1,'witch':1,'eva':1,'combos':{'22':value,'23':value}} for value in [0,99,100]]
for case in cases:
 value,calls,checkpoints=hit(case);results.append({'input':case,'damage':value,'calls':calls,'checkpoints':checkpoints})
preparations=[]
for incoming in [0,1]:
 for kind in [0,1,2]:
  for attack,scale,wave in [(103,97,17),(1,99,20),(10007,121,39)]:
   value,_,_=hit({'attack':attack,'incoming':incoming,'attackKind':kind,'attackScale':scale,'waveRate':wave})
   preparations.append({'input':{'attack':attack,'kind':kind,'percent':scale,'wavePercent':wave},'incoming':incoming,'result':value})
(root/'research/.local/hit-1572.json').write_text(json.dumps({'version':'15.7.2','architecture':'arm64-v8a','sha256':sha,'entry':'006e4aec','scope':'Native ARM64 direct-hit instructions; controlled helper returns, flags and actor data; not full game','vectors':results},indent=2),encoding='utf-8-sig')





def percentage_health(hp,rates):
 u=Uc(UC_ARCH_ARM64,UC_MODE_ARM);u.mem_map(0,len(image));u.mem_write(0,bytes(image));memory=0x20000000;u.mem_map(memory,0x10000)
 u.mem_write(memory+0x28,struct.pack('<QQ',memory+0x100,memory+0x100+len(rates)*4))
 u.mem_write(memory+0x100,struct.pack('<'+'I'*len(rates),*rates));u.reg_write(UC_ARM64_REG_X25,memory);u.reg_write(UC_ARM64_REG_X21,hp);u.reg_write(UC_ARM64_REG_X28,1)
 damages=[]
 def hook(uc,address,size,data):
  if address==0x6d9768:u.emu_stop()
  elif address==0x44abe4:
   value=u.reg_read(UC_ARM64_REG_X0)&0xffffffff;u.reg_write(UC_ARM64_REG_X0,max(value,1));u.reg_write(UC_ARM64_REG_PC,u.reg_read(UC_ARM64_REG_LR))
  elif address==0xa9bbac:damages.append(u.reg_read(UC_ARM64_REG_X2)&0xffffffff);u.reg_write(UC_ARM64_REG_PC,u.reg_read(UC_ARM64_REG_LR))
 u.hook_add(UC_HOOK_CODE,hook);u.emu_start(0x6d970c,0x6d976c,count=2000)
 return damages,u.reg_read(UC_ARM64_REG_X21)&0xffffffff
percentage=[]
for hp,rates in [(101,[20,20]),(3,[20,20]),(1,[20,20]),(101,[100,20]),(100003,[1,17,33])]:
 damage,remaining=percentage_health(hp,rates);percentage.append({'hp':hp,'percentages':rates,'damage':damage,'remainingBasis':remaining})

(root/'research/.local/percentage-1572.json').write_text(json.dumps({'version':'15.7.2','architecture':'arm64-v8a','sha256':sha,'instructions':'006d970c-006d9764','parameter':{'key':'battle_metal_killer_hp_type','value':parameters['battle_metal_killer_hp_type']},'scope':'Native ARM64 queue loop with controlled current HP, rates and helper max; current-HP selector separately read in pseudocode and verified asset','vectors':percentage},indent=2),encoding='utf-8-sig')


def cannon_curve(level):
 u=Uc(UC_ARCH_ARM64,UC_MODE_ARM);u.mem_map(0,len(image));u.mem_write(0,bytes(image));memory=0x20000000;stop=0x60000000;stack=0x30000000
 u.mem_map(memory,0x10000);u.mem_map(stack,0x10000);u.mem_map(stop,4096)
 u.mem_write(memory+0x18,struct.pack('<Q',memory+0x100));u.mem_write(memory+0x120,struct.pack('<I',100));u.mem_write(memory+0x128,struct.pack('<QQQ',memory+0x200,memory+0x214,memory+0x214))
 u.mem_write(memory+0x200,struct.pack('<IIIII',0,0,20,75,1500))
 for reg,value in zip(regs,[memory,100,level]):u.reg_write(reg,value)
 u.reg_write(UC_ARM64_REG_SP,stack+0x8000);u.reg_write(UC_ARM64_REG_LR,stop)
 def hook(uc,address,size,data):
  if address==stop:u.emu_stop()
  elif not 0x63a050<=address<0x63a770:raise RuntimeError('Unexpected curve helper '+hex(address))
 u.hook_add(UC_HOOK_CODE,hook);u.emu_start(0x63a050,stop+4,count=20000)
 return u.reg_read(UC_ARM64_REG_X0)&0xffffffff
curve=[cannon_curve(level) for level in range(1,21)];assert curve==list(range(75,1501,75));print('Native curve: 20 levels matched')
(root/'research/.local/cannon-1572.json').write_text(json.dumps({'version':'15.7.2','architecture':'arm64-v8a','sha256':sha,'function':'0063a050','curve':{'endLevel':20,'start':75,'end':1500,'easing':0},'values':curve},indent=2),encoding='utf-8-sig')

growth_vectors=[]
for kind in ['health','attack']:
 for base,level,treasure,combo,talent,extra in [(8,30,150,0,0,0),(16,30,150,0,0,0),(27,17,68,5,7,7),(13,22,150,15,20,17),(103,41,0,30,17,0),(17,1,150,10,10,0),(103,200,147,15,20,17)]:
  result=execute(kind,base,level,treasure,combo,talent,extra,[20]*20)
  expected=(base*(100+(level-1)*20)+50)//100;expected+=expected*treasure//100
  for rate in [combo,talent,extra]:expected=expected*(100+rate)//100
  assert result==expected
  growth_vectors.append({'kind':kind,'base':base,'growth':100+(level-1)*20,'level':level,'treasure':treasure,'combo':combo,'talent':talent,'extra':extra,'result':result})
for kind in ['health','attack']:
 for level in [10,11,20,21,199,200]:
  rates=[20,10,30,5]*5;growth=100+sum(rates[current//10] for current in range(1,level))
  result=execute(kind,13,level,67,15,20,17,rates)
  expected=(13*growth+50)//100;expected+=expected*67//100
  for rate in [15,20,17]:expected=expected*(100+rate)//100
  assert result==expected
  growth_vectors.append({'kind':kind,'base':13,'growth':growth,'level':level,'treasure':67,'combo':15,'talent':20,'extra':17,'rates':rates,'result':result})

# 章ごとの50×完成率/100を整数化してから合算する現在版の処理。
def treasure_bonus(chapters):
 u=Uc(UC_ARCH_ARM64,UC_MODE_ARM);u.mem_map(0,len(image));u.mem_write(0,bytes(image));game=0x20000000;table=0x21000000;stack=0x30000000;stop=0x60000000
 for address,length in [(game,0x800000),(table,0x10000),(stack,0x10000),(stop,4096)]:u.mem_map(address,length)
 for chapter,value in enumerate(chapters):
  row=table+0x100+chapter*0x30
  u.mem_write(table+chapter*0x18,struct.pack('<QQQ',row,row+0x30,row+0x30));u.mem_write(row+0x24,struct.pack('<II',9,50));u.mem_write(game+0x83e90+chapter*0x2c,struct.pack('<I',value))
 def hook(uc,address,size,data):
  if address==stop:u.emu_stop()
  elif address==0x81f580:u.reg_write(UC_ARM64_REG_X0,game);u.reg_write(UC_ARM64_REG_PC,u.reg_read(UC_ARM64_REG_LR))
  elif not 0xa5b084<=address<0xa5b1b4:raise RuntimeError('Unexpected treasure helper '+hex(address))
 u.hook_add(UC_HOOK_CODE,hook);u.reg_write(UC_ARM64_REG_X0,table);u.reg_write(UC_ARM64_REG_X1,9);u.reg_write(UC_ARM64_REG_SP,stack+0x8000);u.reg_write(UC_ARM64_REG_LR,stop);u.emu_start(0xa5b084,stop+4,count=20000)
 return u.reg_read(UC_ARM64_REG_X0)&0xffffffff
treasures=[{'chapters':values,'bonus':treasure_bonus(values)} for values in [[0,0,0],[100,100,100],[45,45,45],[100,35,0],[99,99,99]]]
assert [row['bonus'] for row in treasures]==[0,150,66,67,147]
(root/'research/.local/growth-1572.json').write_text(json.dumps({'version':'15.7.2','architecture':'arm64-v8a','sha256':sha,'functions':['00a9e9fc','00a9fb88'],'vectors':growth_vectors},indent=2),encoding='utf-8-sig')

# 小さい照合ベクトルだけを追跡対象へ保存する。完全な呼出記録は.localに残す。
if args.publish:
 source=json.loads((root/'research/.local/hit-1572.json').read_text(encoding='utf-8-sig'));vectors=[];poison=[]
 flags={'strong':1,'massive':2,'extreme':4,'resistant':8,'superResistant':16,'witch':32,'eva':64,'colossus':128,'behemoth':256,'sage':512,'villain':1024}
 for row in source['vectors']:
  case=row['input'];incoming=case.get('incoming',0);combos=case.get('combos',{});orbs=case.get('orbs',{})
  if case.get('poison'):
   poison.append({'input':{'maxHp':case['maxHp'],'percent':case['poison'],'resistance':case.get('poisonResistance',0),'decorationReduction':case.get('decoration',0),'immune':case.get('poisonImmune',0)},'damage':row['damage']});continue
  hit_input={'attack':case['attack'],'rawAttack':case.get('raw',8),'critical':case.get('critical',0),'strengthen':case.get('strengthen',0),'killStrengthen':case.get('killStrengthen',0),'weaken':case.get('weaken',100),'savage':case.get('savage',0),'abilities':sum(flag for key,flag in flags.items() if case.get(key)),'fruit':case.get('fruit',300),'metal':case.get('metal',0),'strongCombo':combos.get('14',0),'massiveCombo':combos.get('15',0),'resistantCombo':combos.get('16',0),'witchCombo':combos.get('22',0),'evaCombo':combos.get('23',0),'villainRate':combos.get('25',0),'attackOrb':orbs.get('0',0),'defenseOrb':orbs.get('1',0),'behemothRate':parameters['battle_super_beast_hunter_df' if incoming else 'battle_super_beast_hunter'],'sageRate':parameters['battle_super_sage_hunter_damage2' if incoming else 'battle_super_sage_hunter_damage1'],'resistance':case.get('resistance',0),'baseReduction':case.get('baseReduction',0),'decorationReduction':case.get('decorationReduction',0),'immune':case.get('immune',0),'castle':case.get('castle',0),'castleBreaker':case.get('castleBreaker',0)}
  vectors.append({'input':hit_input,'incoming':incoming,'damage':row['damage'],'checkpoints':row['checkpoints']})
 percentage=json.loads((root/'research/.local/percentage-1572.json').read_text(encoding='utf-8-sig'))
 cannon=json.loads((root/'research/.local/cannon-1572.json').read_text(encoding='utf-8-sig'))
 fixture={key:value for key,value in source.items() if key!='vectors'}|{'preparations':preparations,'parameterSource':param,'cannonSources':cannon_sources,'manifestSha256':current['manifestSha256'],'growth':growth_vectors,'treasures':treasures,'vectors':vectors,'poison':poison,'metalKiller':percentage,'cannon':cannon}
 (root/'native/kbcs-core/tests/native-vectors.json').write_text(json.dumps(fixture,ensure_ascii=False,indent=2),encoding='utf-8-sig')
print(f'Native verification: {len(growth_vectors)} base, {len(results)} hit/poison, {len(percentage["vectors"]) if isinstance(percentage,dict) else len(percentage)} metal queues, 20 curve levels, 5 treasure groups')
