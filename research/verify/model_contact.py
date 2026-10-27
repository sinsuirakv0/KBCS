"""0044c884/0044af4c/0044b854の根部品と逆順キーを実命令へ照合する。"""
import argparse,ctypes as c,itertools,json,os,re,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True);parser.add_argument('--library',type=Path,required=True);parser.add_argument('--assets',type=Path,required=True)
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,Assets,ROOT,SHA,digest
class Input(c.Structure):_fields_=[('units',c.c_int32*3),*[(name,c.c_int32)for name in ['frame','loop','anchor','facing']],('config',c.c_int32*6),('root_override',c.c_int32),('root',c.c_double*5)]
class Part(c.Structure):_fields_=[('cells',c.c_int32*13)]
class Track(c.Structure):_fields_=[('part',c.c_int32),('property',c.c_int32),('loop',c.c_int32),('first',c.c_int32),('count',c.c_int32)]
class Key(c.Structure):_fields_=[('frame',c.c_int32),('value',c.c_int32),('easing',c.c_int32),('power',c.c_int32)]
class PointNative(Native):
 def hook(self,cpu,address,size,data):
  if any(a<=address<self.ends[a]for a in self.actual):return
  super().hook(cpu,address,size,data)
n=PointNative();actual=['0044c884','0044af4c','0044b854','00444908','00444778','00444840','0044aa9c','0044aad4','004448a8']
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True)as db:
 for address,size in db.execute('SELECT address,size FROM functions WHERE address IN ('+','.join('?'for _ in actual)+')',actual):n.ends[int(address,16)]=int(address,16)+size
n.actual=list(map(lambda s:int(s,16),actual))
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin')if os.name=='nt'else None
math=c.CDLL('ucrtbase.dll')
for name in ['sin','cos','pow']:
 fn=getattr(math,name);fn.argtypes=[c.c_double]*(2 if name=='pow' else 1);fn.restype=c.c_double
def floating(index):return struct.unpack('<d',struct.pack('<Q',n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_D'+str(index)))))[0]
def calculated(name):
 value=getattr(math,name)(*[floating(i)for i in range(2 if name=='pow' else 1)]);n.cpu.reg_write(n.reg.UC_ARM64_REG_D0,struct.unpack('<Q',struct.pack('<d',value))[0]);return 0
n.helpers={0xbdb490:lambda:calculated('sin'),0xbdb4a0:lambda:calculated('cos'),0xbdb4f0:lambda:calculated('pow')}
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_model_contact.argtypes=[c.POINTER(Input),c.POINTER(Part),c.c_int32,c.POINTER(c.c_int32)]
lib.kbcs_core_pose_contact.argtypes=[c.POINTER(Input),c.POINTER(Part),c.c_int32,c.POINTER(Track),c.c_int32,c.POINTER(Key),c.c_int32,c.POINTER(c.c_int32)]
native_part=n.memory;model=n.memory+0x1000;point=n.memory+0x2000;animation=n.memory+0x3000;native_track=n.memory+0x4000;native_keys=n.memory+0x5000
# 実レイアウト: 3c/40は基礎位置、44/48は位置加算、4c/50は基礎原点、54/58は原点加算。
def reset(part,units):
 n.cpu.mem_write(native_part,bytes(0xb0));n.cpu.mem_write(model,bytes(0x80));n.cpu.mem_write(model+0x18,struct.pack('<2Q',native_part,native_part+0xb0));n.cpu.mem_write(model+0x60,struct.pack('<3i',*units))
 v=list(part.cells)
 for offset,value in {0x1c:-1,0x24:-1,0x3c:v[4],0x40:v[5],0x4c:v[6],0x50:v[7],0x5c:v[8],0x64:units[0],0x68:v[9],0x70:units[0],0x74:0,0x7c:v[11],0x84:units[2]}.items():n.cpu.mem_write(native_part+offset,struct.pack('<i',value))
def native_point(config):
 n.call(0x44af4c,native_part,model);n.call(0x44b854,native_part,model,config[2],config[3],point);return list(struct.unpack('<2i',n.cpu.mem_read(point,8)))
records=[]
for x,y,sx,sy in itertools.product([-177,-1,0,99],[-123,0,98],[-200,0,77,123,320],[-200,0,77,123,320]):
 part=Part((c.c_int32*13)(-1,-1,0,0,x,y,41,-7,sx,sy,0,255,0));value=Input(units=(c.c_int32*3)(100,360,255),facing=1,config=(c.c_int32*6)(0,0,31,52,0,0));out=(c.c_int32*2)();reset(part,value.units);expected=native_point(value.config)
 assert lib.kbcs_core_model_contact(c.byref(value),c.byref(part),1,out)==0
 assert list(out)==expected,(x,y,sx,sy,list(out),expected);records.append([x,y,sx,sy,*expected])
assets=Assets(args.assets);roots=[]
def values(s,count):return [int(re.match(r'[+-]?\d+',v.strip()).group())for v in s.split(',')[:count]]
for stem in ['559_s','115_e']:
 lines=assets.text('ImageData/'+stem+'.mamodel').splitlines();size=int(lines[2]);part=Part((c.c_int32*13)(*values(lines[3],13)));units=values(lines[size+3],3);config=values(lines[size+5],6);value=Input(units=(c.c_int32*3)(*units),facing=1,config=(c.c_int32*6)(*config));out=(c.c_int32*2)();reset(part,units);expected=native_point(config)
 assert lib.kbcs_core_model_contact(c.byref(value),c.byref(part),1,out)==0 and list(out)==expected,(stem,list(out),expected);roots.append({'stem':stem,'point':expected})
# カイの攻撃track93は47Fの次に46Fがある。補間自体を位置trackへ投影し値を取り出す。
lines=assets.text('ImageData/106_s02.maanim').splitlines();pos=3
for index in range(94):
 header=values(lines[pos],3);size=int(lines[pos+1]);raw=[values(s,4)for s in lines[pos+2:pos+2+size]];pos+=2+size
assert any(b[0]<a[0]for a,b in zip(raw,raw[1:]))
keys=(Key*len(raw))(*[Key(*v)for v in raw]);track=Track(0,4,header[2],0,len(raw));part=Part((c.c_int32*13)(-1,-1,0,0,164,477,0,0,100,100,0,255,0));value=Input(units=(c.c_int32*3)(100,360,255),facing=1);out=(c.c_int32*2)();key_cases=0
for frame in range(145):
 reset(part,value.units);n.cpu.mem_write(animation,struct.pack('<Q16xI',native_track,1));n.cpu.mem_write(native_track,struct.pack('<4iQ16x',0,4,header[2],len(raw),native_keys));n.cpu.mem_write(native_keys,bytes(keys));n.call(0x44c884,model,animation,frame,0,1,2);expected=native_point(value.config);value.frame=frame
 assert lib.kbcs_core_pose_contact(c.byref(value),c.byref(part),1,c.byref(track),1,keys,len(keys),out)==0
 assert list(out)==expected,('key',frame,list(out),expected);key_cases+=1
report={'version':'15.7.2','sha256':SHA,'librarySha256':digest(args.library.read_bytes()),'cases':len(records),'roots':roots,'keyCases':key_cases,'limits':['根部品の原点と原本の逆順キー。全階層/全パケット/GPU画素は別照合']}
(ROOT/'research/.local/model-contact-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig');print(json.dumps(report,ensure_ascii=True))
