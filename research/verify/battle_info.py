"""006a4e9cの属性・特性の配置を同版ARM64の描画要求へ照合する。"""
import sys,struct,json,sqlite3,argparse,ctypes,random
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--python-libs',type=Path,required=True);parser.add_argument('--library',type=Path,required=True);parser.add_argument('--publish',action='store_true');parser.add_argument('--orbs-only',action='store_true');args=parser.parse_args();sys.path.insert(0,str(args.python_libs));sys.path.insert(0,'research/verify');from stages import Native
m=json.loads(Path('ui/images/native-combo/manifest.json').read_text(encoding='utf-8-sig'))
n=Native();g=0x40000000;n.cpu.mem_map(g,0x500000);arena=0x20003000
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:n.ends[0x6a4e9c]=0x6a4e9c+db.execute("SELECT size FROM functions WHERE address='006a4e9c'").fetchone()[0]
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))
def put(p,v):n.cpu.mem_write(p,struct.pack('<Q',v))
def tree(header,values):
 global arena
 nodes=[arena+i*0x30 for i in range(len(values))];arena+=len(values)*0x30
 def build(lo,hi,parent):
  if lo>=hi:return 0
  k=(lo+hi)//2;addr=nodes[k];left=build(lo,k,addr);right=build(k+1,hi,addr)
  n.cpu.mem_write(addr,struct.pack('<QQQii',left,right,parent,0,k)+struct.pack('<i',values[k])+bytes(12));return addr
 root=build(0,len(values),header+8);n.cpu.mem_write(header,struct.pack('<3Q',nodes[0] if nodes else header+8,root,len(values)))
def empty():
 p=reg(8);n.cpu.mem_write(p,struct.pack('<3Q',p+8,0,0));return 0
calls=[];opacity=255;color=[255]*4
def alpha():
 global opacity
 opacity=reg(1);return 0
def tint():
 global color
 color=[reg(i) for i in range(1,5)];return 0
def draw():
 def signed(v):return struct.unpack('<i',struct.pack('<I',v&0xffffffff))[0]
 calls.append([signed(reg(4)),signed(reg(2)),signed(reg(3)),opacity,*color[:3]]);return 0
n.helpers={0x444988:1,0x81f580:g,0x821cb4:100,0x66141c:0,0x6a0128:empty,0x6a4d58:0,0x650740:0,0x4460b0:draw,0x445d04:alpha,0x444c88:tint}
for kind,offset in [('abilities',0x3c5380),('attributes',0x3c5398)]:
 vec=arena;arena+=len(m[kind])*24;refs=[]
 for row in m[kind]:
  p=arena;raw=struct.pack('<'+'i'*(len(row)-1),*row[1:]);arena+=(len(raw)+15)&-16;n.cpu.mem_write(p,raw);refs.append(struct.pack('<3Q',p,p+len(raw),p+len(raw)))
 n.cpu.mem_write(vec,b''.join(refs));put(g+offset,vec)
vec=arena;arena+=64;n.cpu.mem_write(vec,struct.pack('<10i',*sorted(range(10),key=lambda i:m['attributes'][i][1])));put(g+0x3c53b0,vec);put(g+0x3c53b8,vec+40)
class Input(ctypes.Structure):
 _fields_=[('center',ctypes.c_int32),('y',ctypes.c_int32),('form',ctypes.c_int32),('attributes',ctypes.c_int32*10),('abilities',ctypes.c_int32*88),('talents',ctypes.c_int32*88),('new_attributes',ctypes.c_int32*10),('orbs',ctypes.c_int32)]
class Layout(ctypes.Structure):
 _fields_=[('count',ctypes.c_int32),('sprites',(ctypes.c_int32*4)*192),('orb_count',ctypes.c_int32),('orbs',(ctypes.c_int32*2)*8)]
lib=ctypes.CDLL(str(args.library.resolve()));lib.kbcs_core_unit_info.argtypes=[ctypes.POINTER(Input),ctypes.POINTER(Layout)]
randomizer=random.Random(20261101);cases=[];base_arena=arena
samples=[([],[]),([],[22]),([],[0]),([0],[7]),([0,1],[0,7,11,22]),([],[15,18,19,20,21,22]),(list(range(10)),[22])]
samples += [(randomizer.sample(range(10),randomizer.randrange(11)),randomizer.sample([i for i,row in enumerate(m['abilities']) if row[5]<999],randomizer.randrange(20))) for _ in range(160)]
samples=[(a,b,0,{},{}) for a,b in samples]+[(a,b,2,{m['abilities'][i][3]:5+(j%2)*5 for j,i in enumerate(b) if m['abilities'][i][3]}, {i:1 for i in a[:2]}) for a,b in samples[:7]]
if args.orbs_only:samples=[]
for attrs,abilities,form,talents,added in samples:
 arena=base_arena
 outer=arena;arena+=64;n.cpu.mem_write(outer,bytes(64));put(g+0x239d60,outer);put(g+0x239d68,outer);put(g+0x239d70,1)
 tree(outer+0x28,[talents.get(i,0) for i in range(128)])
 def new_attributes():tree(reg(8),[added.get(i,0) for i in range(16)]);return 0
 n.helpers.update({0x6a0128:new_attributes,0xaa7314:10})
 tree(g+0x431d08,[int(i in attrs) for i in range(16)]);tree(g+0x431d20,[int(i in abilities) for i in range(88)]);p=0x20000100;put(p,111)
 calls=[];opacity=255;color=[255]*4;n.entry=0x6a4e9c
 for i,v in enumerate([0,form,p,p,p,p,p,594]):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),v)
 n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,n.stack+0x8000);n.cpu.mem_write(n.stack+0x8000,struct.pack('<Q',159));n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop);n.cpu.emu_start(n.entry,n.stop+4,count=1000000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==n.stop
 value=Input(594,159,form,(ctypes.c_int32*10)(*[int(i in attrs) for i in range(10)]),(ctypes.c_int32*88)(*[int(i in abilities) for i in range(88)]),(ctypes.c_int32*88)(*[0 if not row[3] or not talents.get(row[3],0) else 2 if talents[row[3]]==10 else 1 for row in m['abilities']]),(ctypes.c_int32*10)(*[added.get(i,0) for i in range(10)]),0);out=Layout()
 assert lib.kbcs_core_unit_info(ctypes.byref(value),ctypes.byref(out))==0
 expected=[[cut,x,y,red] for cut,x,y,opacity,red,green,blue in calls];actual=[list(v) for v in out.sprites[:out.count]]
 assert actual==expected,(attrs,abilities,expected,actual)
 if len(cases)<12 or form==2:cases.append({'form':form,'talents':list(value.talents),'new_attributes':list(value.new_attributes),'attributes':list(value.attributes),'abilities':list(value.abilities),'sprites':expected})
# 本能玉の親はSpriteNode。最初の生成要求で止め、親の中心とラベルまで照合する。
class FirstOrb(Exception):pass
orb_calls=[]
def first_orb():
 orb_calls.append([reg(i) for i in range(4)]);raise FirstOrb()
n.helpers.update({0x661498:0,0x9e97c4:first_orb})
for full in [False,True]:
 for count in [1,2,8]:
  arena=base_arena;outer=arena;arena+=64;n.cpu.mem_write(outer,bytes(64));put(g+0x239d60,outer);put(g+0x239d68,outer);put(g+0x239d70,1);tree(outer+0x28,[0]*128);tree(g+0x431d08,[int(full and i==0) for i in range(16)]);tree(g+0x431d20,[int(full and i==7) for i in range(88)])
  n.helpers.update({0x66141c:count,0x6a0128:empty});calls=[];orb_calls=[];opacity=255;color=[255]*4;n.entry=0x6a4e9c
  for i,v in enumerate([0,2,p,p,p,p,p,594]):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),v)
  n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,n.stack+0x8000);n.cpu.mem_write(n.stack+0x8000,struct.pack('<Q',159));n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop)
  try:n.cpu.emu_start(n.entry,n.stop+4,count=1000000)
  except FirstOrb:pass
  value=Input(594,159,2,(ctypes.c_int32*10)(*[int(full and i==0) for i in range(10)]),(ctypes.c_int32*88)(*[int(full and i==7) for i in range(88)]),(ctypes.c_int32*88)(),(ctypes.c_int32*10)(),count);out=Layout();assert lib.kbcs_core_unit_info(ctypes.byref(value),ctypes.byref(out))==0
  expected=[[cut,x,y,red] for cut,x,y,opacity,red,green,blue in calls];actual=[list(v) for v in out.sprites[:out.count] if v[0]!=291]
  assert actual==expected,(full,count,actual,expected)
  x,y=out.orbs[0];assert orb_calls==[[p,x+23,y+23,291]],(full,count,orb_calls,x,y)
print(json.dumps({'cases':len(samples),'orbFrames':6,'result':'一致'},ensure_ascii=True))
if args.publish:
 from stages import SHA
 Path('native/kbcs-core/tests/battle-info-vectors.json').write_text(json.dumps({'nativeSha256':SHA,'cases':cases},ensure_ascii=False,indent=2),encoding='utf-8-sig')
