"""005d5afc→005d63f8の連続時計と描画要求を同版ARM64で照合する。"""
import argparse,ctypes,json,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--python-libs',type=Path,required=True);parser.add_argument('--library',type=Path,required=True);parser.add_argument('--publish',action='store_true');args=parser.parse_args();sys.path.insert(0,str(args.python_libs))
from stages import Native,SHA
n=Native();g=0x40000000;n.cpu.mem_map(g,0x500000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for a,size in db.execute("SELECT address,size FROM functions WHERE address IN ('005d5afc','005d63f8')"):n.ends[int(a,16)]=int(a,16)+size
reg=lambda i:n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))
put=lambda p,v:n.cpu.mem_write(p,struct.pack('<Q',v))
def string():n.cpu.mem_write(reg(8),bytes(24));return 0
def font():n.cpu.mem_write(reg(8),struct.pack('<QQ',1,0));return 0
def pending():return n.cpu.mem_read(reg(0)+0x34,1)[0]
def done():n.cpu.mem_write(reg(0)+0x34,bytes([reg(1)]));return 0
calls=[];color=[255]*4
signed=lambda v:ctypes.c_int32(v).value
def tint():
 global color
 color=[reg(i) for i in range(1,5)];return 0
def band():calls.append(['band',*[signed(reg(i)) for i in range(1,5)],color]);return 0
def sprite():calls.append(['sprite',*[signed(reg(i)) for i in range(2,5)]]);return 0
def text():calls.append(['text',*[signed(reg(i)) for i in range(2,5)],color]);return 0
n.helpers={0x896c68:pending,0x896c70:done,0x449aec:1188,0x829328:0,0x88ebc4:string,0x45ba04:font,0xbdaf60:0,0x444988:1,0x444c18:0,0x444c54:tint,0x44507c:band,0x4460b0:sprite,0x44592c:text}
n.cpu.mem_write(0xc24f78,b'\x01')
class Layout(ctypes.Structure):_fields_=[('index',ctypes.c_int32),('age',ctypes.c_int32),('blink',ctypes.c_int32),('band',ctypes.c_int32*4),('text_x',ctypes.c_int32),('text_y',ctypes.c_int32*3),('skip',ctypes.c_int32*2)]
lib=ctypes.CDLL(str(args.library.resolve()));lib.kbcs_core_combo_intro.argtypes=[ctypes.c_int32,ctypes.c_int32,ctypes.c_int32,ctypes.POINTER(ctypes.c_int32),ctypes.POINTER(Layout)]
fixtures=[]
for groups in [[-1],[0],[-1,0,-1],[0,-1,1]]:
 n.cpu.mem_write(g,bytes(0x500000));vec=0x20001000;records=0x20002000
 for i,group in enumerate(groups):
  p=records+i*128;n.cpu.mem_write(p,bytes(128));n.cpu.mem_write(p+0x34,b'\x01');n.cpu.mem_write(p+0x10,struct.pack('<i',group));n.cpu.mem_write(p+0x3c,struct.pack('<5i',*range(5)));put(vec+i*16,p);put(vec+i*16+8,0)
 put(g+0x448e70,vec);put(g+0x448e78,vec+len(groups)*16)
 n.cpu.mem_write(g+0x449300,struct.pack('<4i',30,120,192,6));p=0x20000080;put(p+0x410,1)
 for frame in range(1,30+len(groups)*120+3):
  n.call(0x5d5afc,g);calls=[];n.call(0x5d63f8,g,p)
  out=Layout();assert lib.kbcs_core_combo_intro(frame,1188,len(groups),(ctypes.c_int32*len(groups))(*groups),ctypes.byref(out))==0
  native_index=next((i for i in range(len(groups)) if n.cpu.mem_read(records+i*128+0x34,1)[0]),-1)
  age=struct.unpack('<i',n.cpu.mem_read(g+0x449314,4))[0]
  if not age:assert out.index==-1,(groups,frame,age,out.index);continue
  assert out.index==native_index and out.age==age,(groups,frame,native_index,age,out.index,out.age)
  assert calls[0]==['band',*list(out.band),[40,40,77,255]],(groups,frame,calls,list(out.band))
  if age>=6:
   assert calls[1]==['sprite',*list(out.skip),8],(groups,frame,calls,list(out.skip))
   texts=[c for c in calls if c[0]=='text'];expected_colors=[[255]*4,[255,255,0,255] if out.blink<2 else [255,0,255,255]]+([[255]*4] if groups[out.index]!=-1 else [])
   assert texts==[['text',out.text_x,out.text_y[i],1,expected_colors[i]] for i in range(len(texts))],(groups,frame,calls)
  if frame in [29,30,34,35,40,148,149,150,154,155,269,270]:fixtures.append({'frame':frame,'groups':groups,'layout':{'index':out.index,'age':out.age,'blink':out.blink,'band':list(out.band),'text_x':out.text_x,'text_y':list(out.text_y),'skip':list(out.skip)}})
print(json.dumps({'frames':sum(30+len(g)*120+2 for g in [[-1],[0],[-1,0,-1],[0,-1,1]]),'result':'一致'},ensure_ascii=True))
if args.publish:Path('native/kbcs-core/tests/combo-intro-vectors.json').write_text(json.dumps({'nativeSha256':SHA,'cases':fixtures},ensure_ascii=False,indent=2),encoding='utf-8-sig')
