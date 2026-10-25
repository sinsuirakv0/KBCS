"""JP15.7.2 ARM64の暗転頂点・矩形境界・HUD経済式を局所実行する。"""
import argparse,json,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--assets',type=Path,required=True)
args=parser.parse_args();sys.path.insert(0,str(args.python_libs))
from stages import Native,Assets,SHA,ROOT
n=Native();assets=Assets(args.assets);g=0x40000000;n.cpu.mem_map(g,0x500000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for address,size in db.execute("SELECT address,size FROM functions WHERE address IN ('006994e8','005d026c','009a6f44','005c27f4','005c2b54','005c2aa0','0058b8ec')"):
  n.ends[int(address,16)]=int(address,16)+size

def reg(index):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(index)))
def integer(value):return struct.unpack('<i',struct.pack('<I',value&0xffffffff))[0]
fade=[]
for frame in range(24):
 n.cpu.mem_write(g+0x32e038,struct.pack('<ii',1,frame));polygons=[]
 def rect():
  x,y,w,h=[integer(reg(i)) for i in range(1,5)];polygons.append([x,y,x,y+h,x+w,y+h,x+w,y]);return 0
 def triangle():
  xs=struct.unpack('<3i',n.cpu.mem_read(reg(1),12));ys=struct.unpack('<3i',n.cpu.mem_read(reg(2),12));polygons.append([v for pair in zip(xs,ys) for v in pair]);return 0
 n.helpers={0x444c24:0,0x444c54:0,0x449aec:960,0x449bac:640,0x828da0:1,0x828de8:0,0x44507c:rect,0x445124:triangle}
 n.call(0x6994e8,g,0,1);fade.append({'frame':frame,'polygons':polygons})

hits=[]
for x,y in [(159,448),(269,536),(270,536),(269,537),(158,448),(159,447),(200,500)]:
 n.helpers={0x8292ec:x,0x8292f4:y};value=n.call(0x9a6f44,g,159,448,110,88);hits.append({'point':[x,y],'inside':value})

economy=[]
for level,worker,combo in [(0,0,0),(6,1,0),(7,2,10),(29,0,0),(29,7,0),(29,7,20)]:
 n.cpu.mem_write(n.memory+0xc,struct.pack('<II',worker,0))
 n.helpers={0x81f580:g,0x7cf950:0,0x644304:0,0x58b674:level,0xa5b084:300000,0x88f9e4:combo}
 cap=n.call(0x5c27f4,n.memory)
 n.helpers[0xa5b084]=300;rate=n.call(0x5c2b54,n.memory)
 cost=n.call(0x5c2aa0,n.memory)
 economy.append({'level':level,'worker':worker,'combo':combo,'walletMax':cap,'income':rate,'upgrade':cost})

charges=[]
for attack,charge,chapter,speed,treasure,combo in [(0,0,0,0,0,0),(29,29,3,1500,450,0),(29,29,3,1500,450,20),(9,29,2,0,450,0)]:
 n.cpu.mem_write(g+0x32f934,struct.pack('<i',chapter))
 def facility():return attack if reg(0)==1 else charge
 def effect():return speed if reg(1)==17 else treasure
 n.helpers={0x81f580:g,0x58b674:facility,0xa5b084:effect,0x88f9e4:combo}
 value=n.call(0x58b8ec);charges.append({'attack':attack,'charge':charge,'chapter':chapter,'speed':speed,'treasure':treasure,'combo':combo,'maximum':value})

pages=[]
for page in [0,1]:
 for direction in [0,1]:
  n.cpu.mem_write(g+0x32e9e0,struct.pack('<6i',page,0,0,0,0,0));n.cpu.mem_write(g+0x32e9fc,b'\1');n.cpu.mem_write(g+0x32e07c,struct.pack('<i',1))
  values=[]
  for _ in range(6):
   n.helpers={};n.call(0x5d026c,g,direction);values.append(list(struct.unpack('<6i',n.cpu.mem_read(g+0x32e9e0,24))))
  pages.append({'page':page,'direction':direction,'states':values})

out={'version':'15.7.2','abi':'arm64-v8a','nativeSha256':SHA,'paramSource':assets.files['Data/param.tsv'],'fade':fade,'hits':hits,'economy':economy,'charges':charges,'pages':pages}
path=ROOT/'native/kbcs-core/tests/battle-screen-vectors.json';path.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8-sig')
print(json.dumps({'fade':len(fade),'hits':len(hits),'economy':len(economy),'charges':len(charges),'pageSteps':len(pages)*6}))
