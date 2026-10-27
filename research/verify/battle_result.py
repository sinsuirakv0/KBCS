"""勝敗の入口・終了時の個体処理・道場時計・出撃制限を15.7.2 ARM64と照合する。"""
import argparse,ctypes as c,itertools,json,os,random,sqlite3,struct,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path,required=True)
a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
from battle_abi import Rules,Result,PointRules
class ResultNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.terminals or address in self.helpers:return super().hook(cpu,address,size,data)
  if any(start<=address<self.ends[start] for start in self.actual):return
  super().hook(cpu,address,size,data)
n=ResultNative();g=0x40000000;n.cpu.mem_map(g,0x500000);n.actual=[0x44a8d8,0x44a8e8]
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for start in [0x9e583c,0x9d4e1c,0x6d6d04,0x5e02b0,0x5d996c]+n.actual:
  n.ends[start]=start+db.execute('SELECT size FROM functions WHERE address=?',(f'{start:08x}',)).fetchone()[0]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()))
assert lib.kbcs_core_abi_version()==4,"ABI4のライブラリが必要"
class Limit(c.Structure):_fields_=[(k,c.c_int32) for k in ['fixed_money','money','cost','rarity_limit','active','total_limit','total']]
Actors=((c.c_int32*251)*51)*2
lib.kbcs_core_battle_limit.argtypes=[c.POINTER(Limit),c.POINTER(c.c_int32)]
lib.kbcs_core_battle_bonus.argtypes=[c.POINTER(Rules),c.c_int32,c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_core_battle_result_step.argtypes=[c.POINTER(Rules),c.POINTER(Result),c.c_int32,c.c_int32,c.c_int32,c.POINTER(Actors),c.POINTER(c.c_uint32)]
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))&0xffffffff
def put(offset,value):n.cpu.mem_write(g+offset,struct.pack('<i',value))
def get(offset):return struct.unpack('<i',n.cpu.mem_read(g+offset,4))[0]
def pointer(address,value):n.cpu.mem_write(address,struct.pack('<Q',value))
def fragment(entry,end,start,registers=None):
 n.entry=entry;n.terminals={end};sp=n.stack+0x8000
 for i in range(31):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),0)
 for i,value in (registers or {}).items():n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),value)
 n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,sp);n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop)
 n.cpu.emu_start(start,n.stop+4,count=200000)
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==end,hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC))
counts={};rng=random.Random(1572027)
# 009d4e1c: 実マップで未定義の効果は0、定義済みの効果は対象数で整数除算。
for points,count in itertools.product([0,1000,1500,2000,2500,3000],[0,1,2,3,7,2147483647]):
 node=n.memory+0x4000;values=n.memory+0x4100;pointer(node,values);pointer(node+8,values+4);n.cpu.mem_write(values,struct.pack('<i',points))
 n.helpers={0x9d4b78:node if points else 0};n.terminals=set();expected=n.call(0x9d4e1c,g,14,count)
 rules=Rules();rules.bonus[14]=points;out=c.c_int32(-1)
 assert lib.kbcs_core_battle_bonus(c.byref(rules),14,count,c.byref(out))==0
 assert out.value==expected,(points,count,out.value,expected)
counts['score_bonus']=36
# 現版ScoreBonusMapの全12マップ。未定義種別を0にし、同じ定義をC++へ渡す。
with sqlite3.connect('C:/Users/ABC/AppData/Local/KBCS/official/jp-9bf0ddccfec99076e741e8a25bf198035d407e5f77cb1ca7373f89c8e46e06b9.sqlite') as db:
 bonus_maps=json.loads(db.execute("SELECT bytes FROM source_file WHERE path='Data/ScoreBonusMap.json'").fetchone()[0].decode('utf-8-sig'))['MapID']
map_count=0
for map_id,definition in bonus_maps.items():
 rules=Rules();types={int(k):v['Parameters'][0] for k,v in definition['BonusType'].items()}
 for key,value in types.items():rules.bonus[key]=value
 for kind,count in itertools.product(range(20),[0,1,2,3,50]):
  points=types.get(kind,0);node=n.memory+0x4000;values=n.memory+0x4100;pointer(node,values);pointer(node+8,values+4);n.cpu.mem_write(values,struct.pack('<i',points))
  n.helpers={0x9d4b78:lambda:node if reg(1) in types else 0};n.terminals=set();expected=n.call(0x9d4e1c,g,kind,count);out=c.c_int32(-1)
  assert not lib.kbcs_core_battle_bonus(c.byref(rules),kind,count,c.byref(out));assert out.value==expected,(map_id,kind,count,out.value,expected);map_count+=1
counts['score_bonus_maps']=map_count
# 009e583cの配列は解決済み、取得順と早期returnは実命令。
cases=list(itertools.product([0,1],[99,100,101],[0,1,3],[0,1,3],[-1,0,2],[0,1,2]))
for fixed,money,limit,active,total_limit,total in cases:
 n.cpu.mem_write(g,bytes(0x1000));i=Limit(fixed,money,100,limit,active,total_limit,total)
 ptrs={3:n.memory+0x1000,7:n.memory+0x1100};values={3:n.memory+0x2000,7:n.memory+0x2100}
 for kind,value in [(3,limit),(7,total_limit)]:pointer(ptrs[kind],values[kind]);pointer(ptrs[kind]+8,values[kind]+4);n.cpu.mem_write(values[kind],struct.pack('<i',value))
 def rule():return 1 if reg(2)==0 and fixed else ptrs[3] if reg(2)==3 else ptrs[7] if reg(2)==7 and total_limit>=0 else 0
 put(0x30,active);put(0x48,total)
 n.helpers={0x81f580:g,0x7cf950:0,0x644304:rule,0x5bce08:0,0x63e4a8:0,0x5c2720:money,0x5be130:100};n.terminals=set()
 expected=n.call(0x9e583c,g,0);out=c.c_int32(-1)
 assert lib.kbcs_core_battle_limit(c.byref(i),c.byref(out))==0
 assert bool(out.value)==bool(expected),(list(bytes(i)),out.value,expected)
counts['limits']=len(cases)
# 006db46cの城0境界と同時破壊優先。報酬/セーブ関数は呼出だけ捕捉する。
sp=n.stack+0x8000
for mode,ally,enemy in itertools.product([0,1,2,4],[0,1,100],[0,1,100]):
 n.cpu.mem_write(g,bytes(0xa0000));pool=Actors();pool[0][0][8]=ally;pool[1][0][8]=enemy
 n.cpu.mem_write(g+0x84080,bytes(pool));calls=[]
 pointer(sp+0x50,g+0x90890);pointer(sp+0x110,g+0x83e60);pointer(sp+0x60,g+0x83dfc);pointer(sp+0xb8,g+0x1000)
 def victory():calls.append(1);return 0
 def defeat():calls.append(2);return 0
 def repair():put(0x840a0,1);return 0
 n.helpers={0x5bc058:mode,0x5d996c:victory,0x5e02b0:defeat,0x5e144c:0,0xa958b0:ally,0xa958f0:repair}
 fragment(0x6d6d04,0x6db4f8,0x6db46c,{27:g})
 rules=Rules(total_limit=-1);s=Result(mode=mode);seed=c.c_uint32(1)
 assert lib.kbcs_core_battle_result_step(c.byref(rules),c.byref(s),1,19,-1,c.byref(pool),c.byref(seed))==0
 assert (s.mode!=mode)==bool(calls),(mode,ally,enemy,s.mode,calls)
 if calls:assert s.mode==calls[0]
 assert pool[0][0][8]==get(0x840a0)
counts['judgement']=36
# 005e0668..074c: 敗北時の全枠処理。5回のRNGと全251wordを比較。
for case in range(48):
 pool=Actors();pool[1][0][8]=100
 for j in range(1,51):
  for word in range(251):pool[0][j][word]=rng.randrange(500)
  pool[0][j][0]=rng.choice([0,1,j+2]);pool[0][j][1]=rng.choice([0,2,3,4,7,14,21])
 n.cpu.mem_write(g+0x84080,bytes(pool));seed=c.c_uint32(rng.randrange(1,0xffffffff));n.cpu.mem_write(0xc24d18,bytes(seed));n.helpers={}
 fragment(0x5e02b0,0x5e074c,0x5e0668,{19:g})
 rules=Rules(score_type=case%2,total_limit=-1);s=Result()
 assert lib.kbcs_core_battle_result_step(c.byref(rules),c.byref(s),1,19,-1,c.byref(pool),c.byref(seed))==0
 assert bytes(pool)==bytes(n.cpu.mem_read(g+0x84080,c.sizeof(pool))),case
 assert seed.value==struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0],case
counts['defeat_actors_rng']=48
# 005da11c..036c: 特殊城を除外した敵死亡と、魂なし特殊城の行動17。
for special,soul in itertools.product([-1,1,25,50],[0,1]):
 pool=Actors();pool[0][0][8]=100
 for j in range(1,51):pool[1][j][0]=rng.choice([0,2,3]);pool[1][j][1]=rng.choice([0,2,4,17]);pool[1][j][8]=321
 if special>0:pool[1][special][111]=soul
 n.cpu.mem_write(g+0x84080,bytes(pool));head=n.memory+0x3000;node=n.memory+0x3100
 n.cpu.mem_write(head,bytes(64));n.cpu.mem_write(node,bytes(64));pointer(head+8,node);n.cpu.mem_write(node+0x20,struct.pack('<i',1))
 pointer(sp+0xf8,g);pointer(sp+0xd8,head)
 def action():put(0x90884+reg(1)*1004+4,reg(2));return 0
 n.helpers={0x5bbc10:special,0xa93fc8:0,0xa9b39c:soul,0xa94274:action}
 fragment(0x5d996c,0x5da36c,0x5da11c)
 rules=Rules(total_limit=-1);s=Result();seed=c.c_uint32(1)
 assert lib.kbcs_core_battle_result_step(c.byref(rules),c.byref(s),1,19,special,c.byref(pool),c.byref(seed))==0
 assert bytes(pool)==bytes(n.cpu.mem_read(g+0x84080,c.sizeof(pool))),(special,soul)
counts['victory_actors']=8
# 時間判定の入口と締切分岐、その後の経過カウンター。保存ハンドラーは別責務。
cases=list(itertools.product([0,4],[0,5398,5399,5400,2147483647],[0,29998,29999,30000]))
for mode,timer,elapsed in cases:
 put(0x32f0,timer);put(0x83e74,elapsed)
 n.helpers={0x5bc058:mode,0x5e1400:1,0x5bbba0:5400,0xa0b03c:0}
 n.entry=0x6d6d04;n.terminals={0x6d7ef4,0x6d81a8};n.cpu.reg_write(n.reg.UC_ARM64_REG_X27,g);n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,sp)
 n.cpu.emu_start(0x6d7e48,n.stop+4,count=1000);pc=n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)
 expected_mode=4 if pc==0x6d7ef4 else mode
 pointer(sp+0x58,g+0x1000);pointer(sp+0x60,g+0x83dfc);n.helpers[0x5bc058]=expected_mode
 fragment(0x6d6d04,0x6d81f8,0x6d81a8,{27:g})
 rules=Rules(score_type=1,time_limit=5400,total_limit=-1);s=Result(mode,timer,elapsed);pool=Actors();seed=c.c_uint32(1)
 assert lib.kbcs_core_battle_result_step(c.byref(rules),c.byref(s),0,19,-1,c.byref(pool),c.byref(seed))==0
 assert (s.mode,s.timer,s.elapsed)==(expected_mode,get(0x32f0),get(0x83e74)),(mode,timer,elapsed,tuple((s.mode,s.timer,s.elapsed)))
counts['dojo_clock']=len(cases)
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(a.library.read_bytes()),'cases':counts,'result':'equal','controlled':['resolved rule vectors/rarity/wallet getters','victory/defeat/timeout save and reward handlers','enemy seen tree already exists'],'actual':['009e583c limit branches','006db46c castle priority','005e0668 defeat actor writes and Xorshift32','005da11c victory actor loop','006d7e48 timer threshold and 006d81a8 elapsed saturation']}
(ROOT/'research/.local/battle-result-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig');print(json.dumps(report,ensure_ascii=False))
