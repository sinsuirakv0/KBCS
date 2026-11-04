"""砲の射程部品と敗北文字の移動を15.7.2 ARM64の実命令へ照合する。画面操作は行わない。"""
import argparse, ast, ctypes as c, itertools, json, math, os, sqlite3, struct, sys
from pathlib import Path

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path,required=True)
a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
from elftools.elf.elffile import ELFFile

class PresentationNative(Native):
 def call(self,address,*args):
  self.entry=address
  for i in range(8):self.cpu.reg_write(getattr(self.reg,f'UC_ARM64_REG_X{i}'),args[i] if i<len(args) else 0)
  self.cpu.reg_write(self.reg.UC_ARM64_REG_SP,self.stack+0x8000);self.cpu.reg_write(self.reg.UC_ARM64_REG_LR,self.stop)
  self.cpu.emu_start(address,self.stop+4,count=10000)
  assert self.cpu.reg_read(self.reg.UC_ARM64_REG_PC) in {self.stop,*self.terminals},'instruction budget'
  return self.cpu.reg_read(self.reg.UC_ARM64_REG_X0)
 def hook(self,cpu,address,size,data):
  if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
  if any(start<=address<end for start,end in self.actual):return
  super().hook(cpu,address,size,data)

n=PresentationNative();n.actual=[];game=0x40000000;texture=game+0x500000
n.cpu.mem_map(game,0x800000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for address in [0x6ddfb8,0x5eb040,0x5ecde0,0x5bf658,0xa9394c,0xa92ec8]:
  size=db.execute('SELECT size FROM functions WHERE address=?',(f'{address:08x}',)).fetchone()[0]
  n.ends[address]=address+size;n.actual.append((address,address+size))
identity=json.loads((n.cache/'identity.json').read_text(encoding='utf-8-sig'))
with Path(identity['binary']).open('rb') as stream:
 elf=ELFFile(stream)
 for reloc in elf.get_section_by_name('.rela.dyn').iter_relocations():
  address=reloc['r_offset']+0x100000
  if address in [0xc1b578,0xc1b608]:n.cpu.mem_write(address,struct.pack('<Q',reloc['r_addend']+0x100000))

reg=lambda i:n.cpu.reg_read(getattr(n.reg,f'UC_ARM64_REG_X{i}'))
def put(offset,value):n.cpu.mem_write(game+offset,struct.pack('<i',value))
def get(offset):return struct.unpack('<i',n.cpu.mem_read(game+offset,4))[0]
def register(name,value):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+name),value)

runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()));assert lib.kbcs_core_abi_version()==5
class Actor(c.Structure):_fields_=[('words',c.c_int32*251)]
class Cut(c.Structure):_fields_=[(name,c.c_int32) for name in ['x','y','width','height']]
class Layout(c.Structure):_fields_=[(name,c.c_double) for name in ['width','center','zoom','minimum','top','bottom']]+[('enemy',c.c_double*4)]+[(name,c.c_double) for name in ['player_x','viewport_width','y_origin','y_offset']]
class Paint(c.Structure):_fields_=[('cuts',c.POINTER(Cut)*2),('counts',c.c_int32*2),('textures',c.c_int32*2)]
class Command(c.Structure):_fields_=[(name,c.c_int32) for name in ['texture','layer','count','blend']]+[('opacity',c.c_double),('points',c.c_double*16),('cut',c.c_int32*4),('colors',c.c_int32*6)]
classes={'Popup','Ending'}
tree=ast.parse((ROOT/'research/verify/battle_ending.py').read_text(encoding='utf-8-sig'))
exec(compile(ast.Module(body=[node for node in tree.body if isinstance(node,ast.ClassDef) and node.name in classes],type_ignores=[]),'battle_ending.py','exec'))
class Hint(c.Structure):_fields_=[('id',c.c_int32),('panel',c.c_int32*4),('text_y',c.c_int32),('ready',c.c_int32)]
lib.kbcs_core_actor_cannon_range_draw.argtypes=[c.POINTER(Actor),c.c_int32,c.c_int32,c.c_int32,c.POINTER(Layout),c.POINTER(Paint),c.POINTER(Command),c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_audit_defeat.argtypes=[c.c_int32,c.POINTER(Ending),c.POINTER(Hint)]
# 原本から同期済みの切り抜き。画像部品番号は本家のdrawから採る。
atlas=json.loads((ROOT/'ui/images/native-battle/manifest.json').read_text(encoding='utf-8-sig'))
assert atlas['version']=='15.7.2' and atlas['nativeSha256']==SHA
cuts=(Cut*2)(*(Cut(*rect) for rect in atlas['atlases']['img002_ja']['rects'][:2]));paint=Paint((c.POINTER(Cut)*2)(cuts,None),(c.c_int32*2)(2,0),(c.c_int32*2)(7,-1))
range_cases=0
for side,camera,position,span,frame,viewport,enabled,wait in itertools.product([0,1],[0,9371],[3200,20000],[3,12],[0,1,2,5,6,59],[960,1281],[0,1],[0,1]):
 actor=Actor();actor.words[3]=position;actor.words[6]=span;actor.words[29]=enabled;actor.words[12]=wait
 n.cpu.mem_write(game+0x84080+side*0xc804,bytes(actor));put(0x83e10,camera);put(0x32f9bc,frame)
 sp=n.stack+0x8000
 for offset,value in [(0x138,game+0x84080),(0x70,game+0x2678),(0x190,game),(0x130,game+0x83e00),(0x180,texture),(0x160,n.memory),(0x170,0)]:n.cpu.mem_write(sp+offset,struct.pack('<Q',value))
 n.cpu.mem_write(texture+0x3d0,struct.pack('<Q',7))
 for name,value in [('SP',sp),('X21',game+0x32e9fc),('X22',side),('X23',struct.unpack('<Q',n.cpu.mem_read(0xc1b578,8))[0]),('W8',int(not side)),('W25',side),('W27',92),('D9',struct.unpack('<Q',struct.pack('<d',.5))[0]),('S10',struct.unpack('<I',struct.pack('<f',11))[0])]:register(name,value)
 calls=[];alpha=255;flip=0
 def draw():calls.append((reg(4),c.c_int32(reg(2)).value,c.c_int32(reg(3)).value,alpha,flip));return 0
 def opacity():
  global alpha
  alpha=reg(1);return 0
 def facing():
  global flip
  flip=reg(1);return 0
 def sine():register('S0',struct.unpack('<I',struct.pack('<f',math.sin(struct.unpack('<f',struct.pack('<I',n.cpu.reg_read(n.reg.UC_ARM64_REG_S0)))[0]*math.pi/180)))[0]);return 0
 n.entry=0x6ddfb8;n.terminals={0x6dff9c,0x6dff88};n.helpers={0x81f580:game,0x5c2710:1,0x449aec:viewport,0x4460b0:draw,0x445d04:opacity,0x445d88:facing,0x44aa9c:sine}
 n.cpu.emu_start(0x6dffb0,n.stop+4,count=5000)
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals
 layout=Layout();layout.zoom=1;layout.viewport_width=viewport;commands=(Command*4)();count=c.c_int32()
 assert lib.kbcs_core_actor_cannon_range_draw(c.byref(actor),side,camera,frame,c.byref(layout),c.byref(paint),commands,4,c.byref(count))==0
 actual=[]
 for i,v in enumerate(commands[:count.value]):actual.append((i,int(min(v.points[0],v.points[6])),int(v.points[1]),round(v.opacity*255),int(v.points[0]>v.points[6])))
 assert calls==actual,(side,camera,position,span,frame,viewport,enabled,wait,calls,actual)
 range_cases+=1

# 005eb040: コンティニュー可能な枝の文字移動を実行。KBCSは中間の課金画面を省いてヒントへ進む。
n.cpu.mem_write(game,bytes(0x800000));n.cpu.mem_write(game,struct.pack('<Q',n.memory));n.cpu.mem_write(n.memory+0x38,struct.pack('<Q',n.stop+0x100))
put(0xc3c8,1);put(0x83e48,-1)
n.helpers={0x9f4228:0,0x5bc00c:0,0x5e0048:0,0x9bd60c:0,0x7cf950:0,0x7cfaa0:0,0x6562ac:-1,0xa08564:1,0x94b6e8:0,0x81f580:game,n.stop+0x100:0};n.terminals={0x5eb8dc}
defeat_cases=0
for tick in range(1,160):
 n.call(0x5eb040,game);phase=get(0x83e38);clock=get(0x83e3c);offset=get(0x32e068)
 out=Ending();hint=Hint();assert lib.kbcs_audit_defeat(tick,c.byref(out),c.byref(hint))==0
 assert (out.phase,out.frame,out.panel)==((4,0,offset) if phase==3 else (phase,clock,offset)),(tick,phase,clock,offset,out.phase,out.frame,out.panel)
 if phase:
  # 原本の描画命令からタイトルの座標・部品を採取する。ヒントの表示前に停止する。
  helpers=n.helpers;terminals=n.terminals;capture=[];n.helpers={0x449aec:960,0x449bac:760,0x445044:0,0x444c18:0,0x444c54:0,0x44507c:0};n.terminals={0x4460b0};n.call(0x5ecde0,game,texture,n.memory)
  capture=[c.c_int32(reg(i)).value for i in [2,3,4]]
  assert capture==list(out.title),(tick,capture,list(out.title))
  n.helpers=helpers;n.terminals=terminals
 assert (hint.id<0)==(out.phase!=4)
 defeat_cases+=1
 if phase==3:break
else:raise AssertionError('defeat slide not completed')
assert out.panel==-100 and out.title[1]==142 and hint.panel[2]==0
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(a.library.read_bytes()),'rangeCases':range_cases,'defeatFrames':defeat_cases,'result':'equal','limits':['controlled renderer, sine library and window getters','continue UI is intentionally skipped after the native title movement; no account, ads or purchase processing','GPU pixels and real audio playback are not compared']}
(ROOT/'research/.local/cannon-presentation-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig')
print(json.dumps(report))
