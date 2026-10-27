"""ステージのキャラ報酬を15.7.2 ARM64の入手ハンドラーと照合する。"""
import argparse,ctypes as c,itertools,json,os,sqlite3,struct,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path)
a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
n=Native();g=0x40000000;n.cpu.mem_map(g,0x800000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 n.ends[0x6e34b0]=0x6e34b0+db.execute('SELECT size FROM functions WHERE address=?',('006e34b0',)).fetchone()[0]
def put(address,value):n.cpu.mem_write(address,struct.pack('<i',value))
def get(address):return struct.unpack('<i',n.cpu.mem_read(address,4))[0]
n.cpu.mem_write(0xc1b5e0,struct.pack('<Q',0xc27d14));put(0xc27d14,1079);put(0xc27d10,1188)
class Input(c.Structure):_fields_=[(key,c.c_int32) for key in ['kind','seen','plus','limit','third','fourth']]
class Output(c.Structure):_fields_=[(key,c.c_int32) for key in ['result','seen','plus','third','fourth']]
if a.library:
 runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
 lib=c.CDLL(str(a.library.resolve()));lib.kbcs_core_character_reward.argtypes=[c.POINTER(Input),c.POINTER(Output)]
cases=[]
for kind,seen,plus,score in itertools.product(range(4),[0,1],[0,9,10],[0,1]):
 n.cpu.mem_write(g,bytes(0x500000));unit=1;gift=3;item=[1005,1100,19001,19002][kind];limit=10
 put(g+0x38b168+6*4,item);put(g+0x38b168+7*4,1)
 flag=g+0x3969f4+gift*4
 put(flag,seen);put(g+0x4b0ac+unit*0x100,limit)
 put(g+0x4b0bc+unit*0x100,19001);put(g+0x4b0c0+unit*0x100,19002)
 third=seen if kind==2 else 0;fourth=seen if kind==3 else 0
 put(g+0x3b0fa8+unit*4,third);put(g+0x3b1d70+unit*4,fourth)
 mutable=[plus]
 def add():mutable[0]+=n.cpu.reg_read(n.reg.UC_ARM64_REG_X1);return 0
 n.helpers={0x6f2f8c:-1,0x6fe6f8:gift,0x6fe890:unit,0xacf804:lambda:mutable[0],0xacf940:add,0x5dfeb0:limit,0x81f580:g,0x7f96d8:0,0x5c022c:0,0x5e0000:item}
 result=n.call(0x6e34b0,g,6,score)
 expected=(result,get(flag),mutable[0],get(g+0x3b0fa8+unit*4),get(g+0x3b1d70+unit*4))
 i=Input(kind,seen,plus,limit,third,fourth)
 if a.library:
  o=Output();assert lib.kbcs_core_character_reward(c.byref(i),c.byref(o))==0
  actual=tuple(getattr(o,key) for key,_ in Output._fields_);assert actual==expected,(kind,seen,plus,score,actual,expected)
 cases.append({'input':dict((key,getattr(i,key)) for key,_ in Input._fields_),'score':score,'expected':expected})
report={'version':'15.7.2','nativeSha256':SHA,'cases':len(cases),'result':'equal' if a.library else 'native-recorded','controlled':['item lookup -1','drop_chara id/save/unit lookup','unitbuy limit','decoded stage reward getter','notification and radar getters'],'actual':['006e34b0 character ownership/evolution/result branches'],'vectors':cases}
if a.library:report['librarySha256']=digest(a.library.read_bytes())
(ROOT/'research/.local/character-reward-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig')
print(json.dumps({key:value for key,value in report.items() if key!='vectors'},ensure_ascii=False))
if not a.library:print(sorted(set((v['input']['kind'],v['input']['seen'],v['expected'][0]) for v in cases)))
