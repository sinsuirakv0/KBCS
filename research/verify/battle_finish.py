"""骨素材・敗北ヒント候補・終了暗転をJP15.7.2 ARM64へ照合する。GPU画素比較ではない。"""
import argparse, csv, ctypes as c, io, itertools, json, os, sqlite3, struct, sys
from pathlib import Path

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--assets',type=Path,required=True)
p.add_argument('--library',type=Path,required=True);p.add_argument('--publish',action='store_true')
p.add_argument('--quick',action='store_true')
a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,Assets,ROOT,SHA

class FinishNative(Native):
 def call(self,entry,*args):
  if entry!=0x701164:return super().call(entry,*args)
  self.entry=entry
  for i in range(8):self.cpu.reg_write(getattr(self.reg,f'UC_ARM64_REG_X{i}'),args[i] if i<len(args) else 0)
  self.cpu.reg_write(self.reg.UC_ARM64_REG_X8,args[0])
  self.cpu.reg_write(self.reg.UC_ARM64_REG_SP,self.stack+0x8000);self.cpu.reg_write(self.reg.UC_ARM64_REG_LR,self.stop)
  self.cpu.emu_start(entry,self.stop+4,count=2000000)
  assert self.cpu.reg_read(self.reg.UC_ARM64_REG_PC)==self.stop,'hint instruction budget'
 def hook(self,cpu,address,size,data):
  if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
  if address in self.allowed:return
  return super().hook(cpu,address,size,data)

n=FinishNative();n.allowed=set();assets=Assets(a.assets);game=0x40000000;texture=game+0x500000
n.cpu.mem_map(game,0x800000);heap=0x51000000;n.cpu.mem_map(heap,0x100000);cursor=heap
reg=lambda i:n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))
def put(offset,value):n.cpu.mem_write(game+offset,struct.pack('<i',value))
def alloc(length):
 global cursor
 out=cursor;cursor+=(length+15)&-16;assert cursor<heap+0x100000;return out
def string(address):
 tag=n.cpu.mem_read(address,1)[0]
 if tag&1:length,address=struct.unpack('<QQ',n.cpu.mem_read(address+8,16))
 else:length=tag//2;address+=1
 return bytes(n.cpu.mem_read(address,length)).decode('utf-8')
names={}
def capture():names[hex(reg(0)-texture)]='ImageData/'+string(reg(1));return 0
n.entry=0x9f560c;n.ends[n.entry]=0xa02000
n.helpers={0xbdaf40:lambda:alloc(reg(0)),0xbdaf60:0,0x44c80c:0,0x44ba98:capture}
n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,n.stack+0x8000);n.cpu.reg_write(n.reg.UC_ARM64_REG_X29,n.stack+0x9000)
n.cpu.mem_write(n.stack+0x8128,struct.pack('<Q',texture));n.terminals={0x9f8ff0}
n.cpu.emu_start(0x9f8ed4,n.stop+4,count=10000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==0x9f8ff0
assert names=={'0x1258':'ImageData/set_enemy001_zombie_down.maanim','0x1290':'ImageData/set_enemy001_zombie_revive.maanim','0x12c8':'ImageData/set_enemy001_zombie_back.maanim'},names
# GOT c1b5f8の相対再配置先はc244c8。原本の拡大率を直接確認する。
assert struct.unpack('<5i',n.cpu.mem_read(0xc244c8,20))==(0,50,80,90,100)
clocks={}
for offset,path in names.items():
 lines=assets.text(path).splitlines();pos=3;tracks=[]
 for _ in range(int(lines[2])):
  header=list(map(int,lines[pos].split(',')[:5]));count=int(lines[pos+1]);tracks.append((header[2],[int(lines[pos+2+i].split(',')[0]) for i in range(count)]));pos+=2+count
 n.helpers={};n.terminals=set();n.cpu.mem_write(n.memory,struct.pack('<QQQI',n.memory+0x1000,0,0,len(tracks)));at=n.memory+0x3000
 for i,(repeat,frames) in enumerate(tracks):
  n.cpu.mem_write(n.memory+0x1000+i*40,struct.pack('<iiiiQ',0,0,repeat,len(frames),at)+bytes(16));n.cpu.mem_write(at,b''.join(struct.pack('<4i',f,0,0,0) for f in frames));at+=len(frames)*16
 clocks[offset]={'path':path,'lengths':[n.call(0x44beb4,n.memory),n.call(0x44bf2c,n.memory)],'source':assets.sources[path]}
if a.publish:
 path=ROOT/'crates/kbcs-data/resources/battle-inputs.json';data=json.loads(path.read_text(encoding='utf-8-sig'));data['clocks'].update(clocks);path.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf-8-sig')

runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()))
class HintContext(c.Structure):_fields_=[(k,c.c_int32) for k in ['mode','map_id','stage','crown','special','progress','cosmos']]
lib.kbcs_core_battle_hint_candidates.argtypes=[c.POINTER(HintContext),c.POINTER(c.c_int32),c.c_int32,c.POINTER(c.c_int32),c.c_int32,c.c_int32,c.POINTER(c.c_int32),c.POINTER(c.c_int32)]
groups=[int(row[0]) for row in csv.reader(io.StringIO(assets.text('res/Lose_ja.csv'))) if row]
settings=[list(map(int,row)) for row in csv.reader(io.StringIO(assets.text('Data/LoseTextSetting.csv'))) if row]
columns=max(map(len,settings));cells=(c.c_int32*(len(settings)*columns))(*(v for row in settings for v in row+[-1]*(columns-len(row))))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for address in [0x701164,0x7013b8,0x70195c,0x6994e8,0x6ddfb8]:
  size=db.execute('SELECT size FROM functions WHERE address=?',(f'{address:08x}',)).fetchone()[0];n.ends[address]=address+size;n.allowed.update(range(address,address+size,4))
source=game+0x600000;rows=source+0x2000;stride=(columns*4+15)&-16;types=rows+stride*len(settings)+0x1000
for i,row in enumerate(settings):
 address=rows+i*stride;n.cpu.mem_write(address,struct.pack('<'+'i'*len(row),*row));n.cpu.mem_write(source+i*24,struct.pack('<QQQ',address,address+len(row)*4,address+len(row)*4))
n.cpu.mem_write(types,struct.pack('<'+'i'*len(groups),*groups));n.cpu.mem_write(game+0x328b00,struct.pack('<QQ',source,source+len(settings)*24));n.cpu.mem_write(game+0x328ae8,struct.pack('<QQ',types,types+len(groups)*4))
def copy_vector():n.cpu.mem_write(reg(0),struct.pack('<QQQ',reg(1),reg(2),reg(2)));return 0
def memcpy():n.cpu.mem_write(reg(0),bytes(n.cpu.mem_read(reg(1),reg(2))));return reg(0)
# バッファ確保/解放とvectorのコピーだけを制御し、候補の分岐・優先順は原本を実行する。
from capstone import Cs,CS_ARCH_ARM64,CS_MODE_ARM
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 functions=dict(db.execute('SELECT address,name FROM functions'))
copies={}
for address in [0x701164,0x7013b8]:
 for instruction in Cs(CS_ARCH_ARM64,CS_MODE_ARM).disasm(n.cpu.mem_read(address,n.ends[address]-address),address):
  if instruction.mnemonic=='bl':
   target=int(instruction.op_str[1:],16)
   if 'memcpy' in functions.get(f'{target:08x}',''):copies[target]=memcpy
cases=0
contexts=list(itertools.product([0,9,99] if a.quick else [0,1,2,3,4,5,6,7,8,9,99],[0],[1],[1],[0,1]))
if not a.quick:contexts.extend((3,crown,1,1,0) for crown in range(1,5))
for mode,crown,progress,cosmos,special in contexts:
 cursor=heap;context=HintContext(mode,33033,2,crown,special,progress,cosmos)
 put(0x32f934,mode);put(0x39797c,crown);put(0x83dfc,context.stage);n.cpu.mem_write(game+0x334048,bytes([progress]));n.cpu.mem_write(game+0x334056,bytes([cosmos]))
 n.helpers={0x81f580:game,0x65054c:special,0x7cf950:context.map_id,0x44dabc:copy_vector,0xbdaf40:lambda:alloc(reg(0)),0xbdaf60:0,**copies};n.terminals=set();n.call(0x701164,n.memory)
 begin,end=struct.unpack('<QQ',n.cpu.mem_read(n.memory,16));expected=list(struct.unpack('<'+'i'*((end-begin)//4),n.cpu.mem_read(begin,end-begin))) if end>begin else []
 output=(c.c_int32*len(groups))();count=c.c_int32();assert lib.kbcs_core_battle_hint_candidates(c.byref(context),(c.c_int32*len(groups))(*groups),len(groups),cells,len(settings),columns,output,c.byref(count))==0
 assert list(output[:count.value])==expected,([getattr(context,k) for k,_ in HintContext._fields_],expected,list(output[:count.value]));cases+=1
class Actor(c.Structure):_fields_=[('words',c.c_int32*251)]
class Visual(c.Structure):_fields_=[(k,c.c_int32) for k in ['kind','side','slot','phase','frame','x','y','layer']]+[('root',c.c_int32*2)]
lib.kbcs_audit_actor_visuals.argtypes=[c.c_int32,c.POINTER(Actor),c.POINTER(Visual),c.POINTER(c.c_int32)]
bone_cases=0
for action,counter,frame in itertools.product([3,6,14,15,16,19],[0,1,30],[0,7,39]):
 actor=Actor();actor.words[0]=2;actor.words[1]=action;actor.words[2]=frame;actor.words[3]=15000;actor.words[4]=4400;actor.words[5]=2;actor.words[205]=counter
 output=(Visual*32)();count=c.c_int32();assert lib.kbcs_audit_actor_visuals(1,c.byref(actor),output,c.byref(count))==0
 primary=[v for v in output[:count.value] if v.kind==12];revive=[v for v in output[:count.value] if v.kind==13]
 assert bool(primary)==(counter>0 and action not in [15,19]);assert bool(revive)==(action in [15,16])
 for entry,start,end in [(primary,0x6df35c,0x6dfec0),(revive,0x6df5ec,0x6df65c)]:
  if not entry:continue
  scratch=game+0x700000;sp=n.stack+0x8000;captured=[]
  def model():captured.append([reg(1)-texture,c.c_int32(reg(2)).value]);return 0
  def draw():captured[-1].extend([c.c_int32(reg(2)).value,c.c_int32(reg(3)).value]);return 0
  n.helpers={0xa94234:action,0xa9474c:frame,0x449aec:960,0x44d1dc:model,0x448e7c:draw};n.entry=0x6ddfb8;n.terminals={end}
  n.cpu.mem_write(scratch+0xde4,struct.pack('<ii',1500,448));put(0x3400,0)
  for offset,value in [(0x80,texture+0x12c8),(0xc0,texture+0x1258),(0x108,texture+0x11b0),(0x190,game),(0x168,scratch)]:n.cpu.mem_write(sp+offset,struct.pack('<Q',value))
  for name,value in [('SP',sp),('W0',action),('W28',1),('W27',1),('X25',1),('X20',texture),('X21',scratch)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+name),value)
  n.cpu.emu_start(start,n.stop+4,count=1000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==end
  assert captured==[[v.phase,v.frame,v.x,v.y] for v in entry],(action,counter,frame,captured)
 bone_cases+=1

lib.kbcs_audit_return_wipe.argtypes=[c.c_int32,c.c_int32,c.POINTER(c.c_int32),c.POINTER(c.c_int32),c.POINTER(c.c_int32)]
for mode,ticks in itertools.product([1,2,4,7],[1,5,11,12,30]):
 action,fade,frame=c.c_int32(),c.c_int32(),c.c_int32()
 assert lib.kbcs_audit_return_wipe(mode,ticks,c.byref(action),c.byref(fade),c.byref(frame))==0
 assert (action.value==302)==(ticks>=12);assert bool(fade.value)==(ticks>=12);assert frame.value==min(11,ticks-1),(mode,ticks,frame.value)
fixture_rows=[[0]+[1]*26+[0,-1],[1]+[0]*26+[1,1002,-1],[2]+[1]*26+[2,77,-1],[3]+[1]*26+[1,1002,-1]]
fixture_groups=[0,1,0,3,2,0];fixture=[]
for i,row in enumerate(fixture_rows):
 address=rows+i*stride;n.cpu.mem_write(address,struct.pack('<'+'i'*len(row),*row));n.cpu.mem_write(source+i*24,struct.pack('<QQQ',address,address+len(row)*4,address+len(row)*4))
n.cpu.mem_write(types,struct.pack('<6i',*fixture_groups));n.cpu.mem_write(game+0x328b00,struct.pack('<QQ',source,source+len(fixture_rows)*24));n.cpu.mem_write(game+0x328ae8,struct.pack('<QQ',types,types+len(fixture_groups)*4))
for map_id,stage in [(10,2),(10,3),(77,0)]:
 cursor=heap;put(0x32f934,99);put(0x83dfc,stage)
 n.helpers={0x81f580:game,0x65054c:0,0x7cf950:map_id,0x44dabc:copy_vector,0xbdaf40:lambda:alloc(reg(0)),0xbdaf60:0,**copies};n.terminals=set();n.call(0x701164,n.memory)
 begin,end=struct.unpack('<QQ',n.cpu.mem_read(n.memory,16));expected=list(struct.unpack('<'+'i'*((end-begin)//4),n.cpu.mem_read(begin,end-begin)))
 fixture.append({'context':[99,map_id,stage,0,0,1,1],'indices':expected})
if a.publish:(ROOT/'native/kbcs-core/tests/battle-hint-vectors.json').write_text(json.dumps({'version':'15.7.2','sha256':SHA,'groups':fixture_groups,'settings':fixture_rows,'cases':fixture},separators=(',',':')),encoding='utf-8-sig')
report={'version':'15.7.2','sha256':SHA,'boneBindings':names,'boneLengths':{k:v['lengths'] for k,v in clocks.items()},'hintCases':cases,'boneDrawCases':bone_cases,'returnCases':20}
(ROOT/'research/.local/battle-finish-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8-sig');print(json.dumps(report))
