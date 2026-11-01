"""009f560cのワープ素材対応と00448fa0の変形頂点を同版ARM64へ照合する。"""
import argparse,ctypes as c,json,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--python-libs',type=Path,required=True);parser.add_argument('--assets',type=Path,required=True);parser.add_argument('--library',type=Path);parser.add_argument('--publish',action='store_true');args=parser.parse_args();sys.path.insert(0,str(args.python_libs))
from stages import Native,Assets,ROOT,SHA
n=Native();assets=Assets(args.assets);texture=0x40000000;n.cpu.mem_map(texture,0x10000);cursor=0x20008000;names={}
reg=lambda i:n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))
setreg=lambda name,value:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+name),value)
def alloc(length):
 global cursor
 p=cursor;cursor+=(length+15)&-16;assert cursor<0x20010000;return p
def string(p):
 tag=n.cpu.mem_read(p,1)[0]
 if tag&1:length,p=struct.unpack('<QQ',n.cpu.mem_read(p+8,16))
 else:length=tag//2;p+=1
 return bytes(n.cpu.mem_read(p,length)).decode('ascii')
def store(p,value):
 raw=value.encode('ascii')
 if len(raw)<23:n.cpu.mem_write(p,bytes([len(raw)*2])+raw+bytes(23-len(raw)))
 else:q=alloc(len(raw)+1);n.cpu.mem_write(q,raw+b'\0');n.cpu.mem_write(p,struct.pack('<3Q',(len(raw)+8)&-8|1,len(raw),q))
def format_string():store(reg(8),string(reg(0)).replace('%@',string(reg(1))));return 0
def capture():names[hex(reg(0)-texture)]='ImageData/'+string(reg(1));return 0
n.entry=0x9f560c;n.ends[n.entry]=0xa02000;n.helpers={0xbdaf40:lambda:alloc(reg(0)),0xbdaf60:0,0x44c1dc:0,0x46ff30:format_string,0x44ba98:capture}
setreg('SP',n.stack+0x8000);setreg('X29',n.stack+0x9000);setreg('X19',texture)
n.cpu.mem_write(n.stack+0x8128,struct.pack('<Q',texture));n.cpu.mem_write(n.stack+0x8040,struct.pack('<Q',texture+0x2b98));n.cpu.mem_write(n.stack+0x8110,struct.pack('<QQ',33,24))
n.terminals={0x9fb594};n.cpu.emu_start(0x9fb38c,n.stop+4,count=10000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==0x9fb594
assert names=={'0x2b98':'ImageData/skill_warp_entrance.maanim','0x2bd0':'ImageData/skill_warp_exit.maanim','0x2c08':'ImageData/skill_warp_chara_entrance.maanim','0x2c40':'ImageData/skill_warp_chara_exit.maanim'},names
clocks={}
for offset,path in names.items():
 lines=assets.text(path).splitlines();pos=3;tracks=[]
 for _ in range(int(lines[2])):
  header=list(map(int,lines[pos].split(',')[:5]));count=int(lines[pos+1]);frames=[int(lines[pos+2+i].split(',')[0]) for i in range(count)];pos+=2+count;tracks.append((header[2],frames))
 n.terminals=set();n.helpers={};n.cpu.mem_write(n.memory,struct.pack('<QQQI',n.memory+0x1000,0,0,len(tracks)))
 at=n.memory+0x3000
 for i,(repeat,frames) in enumerate(tracks):
  n.cpu.mem_write(n.memory+0x1000+i*40,struct.pack('<iiiiQ',0,0,repeat,len(frames),at)+bytes(16));n.cpu.mem_write(at,b''.join(struct.pack('<4i',f,0,0,0) for f in frames));at+=len(frames)*16
 lengths=[n.call(0x44beb4,n.memory),n.call(0x44bf2c,n.memory)];clocks[offset]={'path':path,'lengths':lengths,'source':assets.sources[path]}
if args.publish:
 p=ROOT/'crates/kbcs-data/resources/battle-inputs.json';v=json.loads(p.read_text(encoding='utf-8-sig'));v['clocks'].update(clocks);p.write_text(json.dumps(v,ensure_ascii=False,separators=(',',':')),encoding='utf-8-sig')
print(json.dumps({'bindings':names,'lengths':{k:v['lengths'] for k,v in clocks.items()}},ensure_ascii=True))

if args.library:
 import random
 class Warp(c.Structure):_fields_=[('scale',c.c_float),('y',c.c_int32),('alpha',c.c_int32)]
 class Packet(c.Structure):_fields_=[('part',c.c_int32),('cut',c.c_int32),('blend',c.c_int32),('opacity',c.c_double),('points',c.c_int32*8)]
 lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_warp_packets.argtypes=[c.POINTER(Warp),c.POINTER(c.c_int32),c.POINTER(c.c_int32),c.POINTER(Packet),c.c_int32,c.POINTER(Packet)]
 with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:n.ends[0x448fa0]=0x448fa0+db.execute("SELECT size FROM functions WHERE address='00448fa0'").fetchone()[0]
 ctx,gl,model,node,order,textures=map(lambda v:n.memory+v,[0x8000,0x8100,0x8200,0x8300,0x8500,0x8600]);calls=[]
 n.cpu.mem_write(ctx,struct.pack('<Q',gl));n.cpu.mem_write(ctx+0x40,struct.pack('<4i',255,255,255,255));n.cpu.mem_write(model+0x10,struct.pack('<3Q',textures,node,node+0xb0));n.cpu.mem_write(model+0x30,struct.pack('<Q',order));n.cpu.mem_write(model+0x68,struct.pack('<i',1000));n.cpu.mem_write(textures,struct.pack('<Q',1));n.cpu.mem_write(order,bytes(4))
 def draw():
  sp=n.cpu.reg_read(n.reg.UC_ARM64_REG_SP)
  calls.append([c.c_int32(reg(i)).value for i in range(2,8)]+[c.c_int32(v).value for v in struct.unpack('<2Q',n.cpu.mem_read(sp,16))]);return 0
 n.terminals=set();n.helpers={0x447dc8:draw};rng=random.Random(20261102);vectors=[]
 for index in range(100):
  scale=rng.choice([0.,.1,.3,.963,1.,1.02,2.26]);y=rng.choice([-350,-73,0,20]);alpha=rng.choice([0,32,127,255]);raw_alpha=rng.choice([0,500,1000]);base_alpha=raw_alpha*255//1000
  anchor=[rng.randrange(-500,500) for _ in range(4)];origin=[rng.randrange(-10000,10000),rng.randrange(-2000,2000)];points=[rng.randrange(-1000,1000) for _ in range(8)];warp=Warp(scale,y,alpha);packet=Packet(0,0,0,base_alpha/255,(c.c_int32*8)(*points));out=Packet()
  n.cpu.mem_write(node,bytes(0xb0));n.cpu.mem_write(node+0x80,struct.pack('<i',raw_alpha));n.cpu.mem_write(node+0x90,struct.pack('<8i',*points));n.cpu.mem_write(n.stack+0x8000,bytes(8));setreg('S0',struct.unpack('<I',struct.pack('<f',scale))[0]);calls=[]
  n.call(0x448fa0,ctx,model,origin[0]-anchor[0],origin[1]-anchor[3]+y,anchor[2],anchor[3],alpha,0)
  assert lib.kbcs_core_warp_packets(c.byref(warp),(c.c_int32*4)(*anchor),(c.c_int32*2)(*origin),c.byref(packet),1,c.byref(out))==0
  expected_alpha=base_alpha*alpha//255
  assert out.opacity==expected_alpha/255
  assert calls==([list(out.points)] if expected_alpha else []),(index,scale,anchor,origin,points,calls,list(out.points))
  if index<12:vectors.append({'warp':{'scale':warp.scale,'y':y,'alpha':alpha},'anchor':anchor,'origin':origin,'baseAlpha':base_alpha,'points':points,'output':list(out.points),'alpha':expected_alpha})
 print(json.dumps({'drawCases':100,'result':'一致'},ensure_ascii=True))
 if args.publish:(ROOT/'native/kbcs-core/tests/warp-vectors.json').write_text(json.dumps({'nativeSha256':SHA,'bindings':names,'cases':vectors,'control':{'cut':assets.text('ImageData/skill001.imgcut'),'model':assets.text('ImageData/skill_warp_chara.mamodel'),'entrance':assets.text('ImageData/skill_warp_chara_entrance.maanim'),'exit':assets.text('ImageData/skill_warp_chara_exit.maanim')}},ensure_ascii=False,indent=2),encoding='utf-8-sig')
