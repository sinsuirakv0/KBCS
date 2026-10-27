"""006ddfb8上部の実描画をC++命令へ照合。probeは所有状態を制御した描画専用fixture。"""
import argparse,ctypes as c,itertools,json,math,os,sqlite3,struct,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path,required=True);p.add_argument('--probe',type=Path,required=True);a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
class TopNative(Native):
 def hook(self,cpu,address,size,data):
  if address in self.helpers or address in self.terminals:return super().hook(cpu,address,size,data)
  if any(start<=address<self.ends[start] for start in self.actual):return
  return super().hook(cpu,address,size,data)
n=TopNative();g=0x40000000;n.cpu.mem_map(g,0x500000);n.cpu.mem_map(n.memory+0x10000,0x20000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 n.ends.update({int(x,16):int(x,16)+size for x,size in db.execute("select address,size from functions where address not like 'EXTERNAL:%'")})
n.actual=[0x44626c,0x448034,0x448040,0x448048]
class Cut(c.Structure):_fields_=[(k,c.c_int32) for k in ['x','y','width','height']]
class Command(c.Structure):_fields_=[(k,c.c_int32) for k in ['texture','layer','count','blend']]+[('opacity',c.c_double),('points',c.c_double*16),('cut',c.c_int32*4),('colors',c.c_int32*6)]
class Display(c.Structure):_fields_=[(k,c.c_int32) for k in ['phase','frame','origin','value','scale']]
dll_dir=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()));probe=c.CDLL(str(a.probe.resolve()))
probe.top_probe.argtypes=[c.POINTER(c.c_int32),c.POINTER(Cut),c.c_int32,c.POINTER(Cut),c.c_int32,c.POINTER(Command),c.POINTER(c.c_int32)]
lib.kbcs_core_battle_score_display.argtypes=[c.c_int32,c.POINTER(Display)]
m=json.loads((ROOT/'ui/images/native-battle/manifest.json').read_text(encoding='utf-8-sig'));base=m['atlases']['img001_ja']['rects']
with sqlite3.connect('C:/Users/ABC/AppData/Local/KBCS/official/jp-9bf0ddccfec99076e741e8a25bf198035d407e5f77cb1ca7373f89c8e46e06b9.sqlite') as db:
 lines=db.execute("select bytes from source_file where path='ImageData/FeverEffect.imgcut'").fetchone()[0].decode('utf-8-sig').splitlines();fever=[[int(x) for x in l.split(',')[:4]] for l in lines[4:4+int(lines[3])]]
arrays=[(Cut*len(rows))(*(Cut(*row) for row in rows)) for rows in [base,fever]]
sp=n.stack+0x8000;texture=n.memory+0x10000
for offset,value in [(0x320,9000),(0x16598,9001)]:n.cpu.mem_write(texture+offset,struct.pack('<Q',value))
for i,arr in enumerate(arrays):n.cpu.mem_write(n.memory+0x4000+i*0x2000,bytes(arr))
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))
def integer(i):return c.c_int32(reg(i)).value
def f(i):return struct.unpack('<f',struct.pack('<I',n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_S'+str(i)))))[0]
def put(offset,value):n.cpu.mem_write(g+offset,struct.pack('<i',value))
def pointer(offset,value):n.cpu.mem_write(sp+offset,struct.pack('<Q',value))
def run(start,end):
 n.entry=0x6ddfb8;n.terminals={end};n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,sp);n.cpu.reg_write(n.reg.UC_ARM64_REG_X29,sp+0x400);n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop);n.cpu.emu_start(start,n.stop+4,count=50000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==end
records=[]
# 表示補間は任意の加算値・phase・カウンタで原本の分岐を実行する。
for phase,frame,score,origin in itertools.product(range(3),range(6),[0,1,17,100000],[0,101]):
 if phase==1 and frame>3:continue
 n.cpu.mem_write(g+0x3310,bytes(20));put(0x3310,phase);put(0x3314,frame);put(0x331c,origin);put(0x32ec,score);n.cpu.reg_write(n.reg.UC_ARM64_REG_X24,g)
 run(0x6e11fc,0x6e1604);state=Display(phase,frame,origin,0,0);assert not lib.kbcs_core_battle_score_display(score,c.byref(state));expected=[struct.unpack('<i',n.cpu.mem_read(g+x,4))[0] for x in [0x3310,0x3314,0x331c,0x3318,0x3320]];assert list(bytes(state))==list(struct.pack('<5i',*expected)),(phase,frame,score,origin,expected,list(bytes(state)))
counts={'animation':0};counts['animation']=3*6*4*2-2*4*2
cases=[(w,k,m,t,v,s,e,0,0,0) for w in [960,1280] for k in [1,3] for m in [0,4] for t in [0,1,899,900,901,5400] for v,s in [(0,100),(12345,136)] for e in ([0,1] if k==3 else [0])]
cases += [(w,3,0,900,12345,100,1,gauge,wait,frame) for w in [960,1280] for gauge,wait,frame in [(0,300,0),(294,150,3),(150,1,6),(150,0,0)]]
for width,kind,mode,remaining,score,scale,enabled,gauge,wait,visual_frame in cases:
 n.cpu.mem_write(g,bytes(0x500000));put(0x3318,score);put(0x3320,scale);put(0x32ec,score)
 pointer(0xa8,texture+0x16000);pointer(0x180,texture);pointer(0x188,g+0x32f7dc);pointer(0x168,g+0x32e9fc);pointer(0x170,g+0x32f7e0);pointer(0x1b0,g);pointer(0x190,g)
 for i in range(31):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),0)
 for i,v in {20:texture,21:g+0x32e9fc,24:g,26:0x1234,27:0x2b2000}.items():n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),v)
 actual=[];color=[255,255,255]
 def add(tex,cut,x,y,w,h):
  if w and h:actual.append([tex,list(cut),[x,y,x,y+h,x+w,y+h,x+w,y],color.copy()])
 def cut():return n.memory+0x4000+(0x2000 if reg(0)==9001 else 0)+integer(1)*16
 def source():
  sx,sy,sw,sh=[integer(i) for i in range(2,6)];add(int(reg(1)==9001),[sx,sy,sw,sh],f(0),f(1),f(2),f(3));return 0
 def piece():
  loc=n.cpu.reg_read(n.reg.UC_ARM64_REG_SP);sw=struct.unpack('<i',n.cpu.mem_read(loc,4))[0];sh=struct.unpack('<i',n.cpu.mem_read(loc+8,4))[0];add(int(reg(1)==9001),[integer(6),integer(7),sw,sh],integer(2),integer(3),integer(4),integer(5));return 0
 def sprite():
  rows=fever if reg(1)==9001 else base;v=rows[integer(4)];add(int(reg(1)==9001),v,integer(2),integer(3),v[2],v[3]);return 0
 def scaled():
  rows=fever if reg(1)==9001 else base;v=rows[integer(6)];add(int(reg(1)==9001),v,integer(2),integer(3),integer(4),integer(5));return 0
 def float_scaled():
  rows=fever if reg(1)==9001 else base;v=rows[integer(2)];add(int(reg(1)==9001),v,f(0),f(1),f(2),f(3));return 0
 def power():n.cpu.reg_write(n.reg.UC_ARM64_REG_S0,struct.unpack('<I',struct.pack('<f',math.pow(f(0),f(1))))[0]);return 0
 def tint():color[:]=[integer(i) for i in [1,2,3]];return 0
 def ratio():n.cpu.reg_write(n.reg.UC_ARM64_REG_D0,struct.unpack('<Q',struct.pack('<d',wait/300))[0]);return 0
 n.helpers={0x7cf950:0,0x5e1400:int(kind==1),0xa0b03c:int(kind==3),0x81f580:g,0x449aec:width,0x467074:cut,0x445f48:source,0x445e30:piece,0x4460b0:sprite,0x446d2c:scaled,0x447378:float_scaled,0x44ab6c:power,0x44ab84:lambda:len(str(integer(0))),0x5bc058:mode,0x5bbba0:remaining,0x444c88:tint,0xa0b818:score,0x6440f0:enabled,0x644238:int(wait>0),0x64556c:gauge,0x6455fc:visual_frame,0x645504:ratio,0xa0d078:1,0xa0d06c:remaining}
 # 補間自体は上で照合済み。ここでは同じ解決済み表示値から描画する。
 run(0x6e1604 if kind==1 else 0x6e123c,0x6e1b9c)
 out=(Command*64)();written=c.c_int32();values=(c.c_int32*10)(width,kind,remaining,mode,score,scale,gauge,wait,enabled,visual_frame)
 assert not probe.top_probe(values,arrays[0],len(base),arrays[1],len(fever),out,c.byref(written))
 expected=[[cmd.texture,list(cmd.cut),list(cmd.points)[:8],list(cmd.colors)[:3]] for cmd in out[:written.value]]
 actual.sort(key=lambda v:(v[0],v[1],v[2]));expected.sort(key=lambda v:(v[0],v[1],v[2]));
 assert len(actual)==len(expected),(width,kind,mode,remaining,score,scale,len(actual),len(expected),[(v[1],v[2][:2]) for v in actual],[(v[1],v[2][:2]) for v in expected])
 for i,(left,right) in enumerate(zip(actual,expected)):
  assert left[:2]==right[:2] and left[3]==right[3] and all(abs(x-y)<.0001 for x,y in zip(left[2],right[2])),(width,kind,mode,remaining,score,scale,i,left,right)
 records.append({'width':width,'kind':kind,'mode':mode,'remaining':remaining,'score':score,'scale':scale,'fever':enabled,'wait':wait,'gauge':gauge,'commands':written.value})
counts['drawing']=len(records);report={'version':'15.7.2','nativeSha256':SHA,'counts':counts,'records':records,'controlled':['resolved score/mode/remaining/fever and texture cuts','GPU draw capture, viewport and singleton','powf and digit count'],'limits':['draw fixture sets private owner display state; separate replay verifies actual Session connection','Android GPU pixels are not compared']};(ROOT/'research/.local/battle-top-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig');print(json.dumps(counts))
