"""JP15.7.2のスワイプ・財布点滅・オプション枠を制御して局所実行する。"""
import argparse,json,math,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
args=parser.parse_args();sys.path.insert(0,str(args.python_libs))
from stages import Native,SHA,ROOT
n=Native();g=0x40000000;n.cpu.mem_map(g,0x500000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for address,size in db.execute("SELECT address,size FROM functions WHERE address IN ('009f4228','005c8a6c','005d0044','008fb5f4','008f9e20','005d1f2c','005d2408')"):
  n.ends[int(address,16)]=int(address,16)+size
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))
def signed(v):return struct.unpack('<i',struct.pack('<I',v&0xffffffff))[0]
def put(offset,value):n.cpu.mem_write(g+offset,struct.pack('<i',value))
swipes=[]
for dx,dy in [(0,-24),(0,-25),(0,24),(0,25),(30,25),(25,25),(-25,25),(0,0)]:
 n.cpu.mem_write(g,bytes(0x500000));put(0x343c,10000);put(0x83e6c,100);n.cpu.mem_write(g+0x332e12,b'\1')
 n.helpers={0x80d8e0:0,0x827b94:1,0x8292ec:500+dx,0x8292f4:570+dy,0x8292fc:500,0x829304:570,0x82930c:500,0x44ab0c:lambda:0}
 # atan2の整数角度を原本ヘルパーと同じ向きで与える。
 angle=int(math.degrees(math.atan2(dy,dx))%360) if dx or dy else 0
 # ヘルパーの浮動小数戻り値もS0へ渡す。
 def atan():n.cpu.reg_write(n.reg.UC_ARM64_REG_S0,struct.unpack('<I',struct.pack('<f',float(angle)))[0]);return 0
 n.helpers[0x44ab0c]=atan
 n.call(0x9f4228,g)
 swipes.append({'delta':[dx,dy],'active':n.cpu.mem_read(g+0x32e9fc,1)[0],'direction':struct.unpack('<i',n.cpu.mem_read(g+0x32e9f8,4))[0]})
camera=[]
for rows in [1,2]:
 n.cpu.mem_write(g,bytes(0x500000));put(0x343c,10000);put(0x34a4,520 if rows==1 else 505);n.cpu.mem_write(g+0x1405,bytes([rows==2]))
 def parameter():
  p=reg(1);raw=n.cpu.mem_read(p,24);name=raw[1:1+(raw[0]>>1)].decode('ascii',errors='ignore') if not raw[0]&1 else n.cpu.mem_read(struct.unpack('<Q',raw[16:24])[0],24).split(b'\0')[0].decode('ascii')
  return {'battle_zoom_slot_y':500,'battle_slot_2lines_y':-15,'battle_slot_2lines_line':95}[name]
 n.helpers={0x9019f4:parameter,0x417f20:0,0x4184d0:0}
 # 文字列の一時確保だけを制御する。
 alloc=n.memory+0x2000
 with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
  for address,name in db.execute("SELECT address,name FROM functions WHERE name LIKE 'operator.new%' OR name LIKE 'operator.delete%'"):n.helpers[int(address,16)]=alloc if 'new' in name else 0
 offset=n.call(0x5c8a6c,g);camera.append({'rows':rows,'offset':offset})
pause=[]
for wide in [960,1280]:
 n.cpu.mem_write(g,bytes(0x500000));put(0x4a640,2)
 n.helpers={0x81f580:g,0x449aec:wide,0x467074:0}
 # 最初のテクスチャ問合せ直前まで実コンストラクタを進める。
 n.terminals={0x467074}
 try:n.call(0x8f9e20,n.memory,n.memory+0x100)
 except AssertionError:assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==0x467074
 n.terminals=set();rectangles=[]
 def sprite():rectangles.append([signed(reg(6)),*[signed(reg(i)) for i in range(2,6)]]);return 0
 def natural():rectangles.append([signed(reg(4)),signed(reg(2)),signed(reg(3)),0,0]);return 0
 n.helpers={0x444988:0,0x469e20:0,0x46ad74:0,0x444c54:0,0x81f580:g,0x449aec:wide,0x449bac:640,0x44507c:0,0x446d2c:sprite,0x4460b0:natural,0x8847e4:0,0x883bb8:0}
 n.call(0x8fb5f4,n.memory);pause.append({'width':wide,'window':list(struct.unpack('<8i',n.cpu.mem_read(n.memory+0x10,32))),'sprites':rectangles})
money=[]
for timer in range(15):
 n.cpu.mem_write(g,bytes(0x500000));put(0x83e60,timer);bases=[]
 def digits():
  bases.append(signed(reg(2)));n.cpu.mem_write(reg(8),bytes(12));return 0
 n.helpers={0x444988:0,0x449c84:0,0x444bb0:0,0x449aec:960,0x5c27f4:100000,0x5c2720:12300,0x448034:digits,0x446d2c:0}
 n.call(0x5d0044,g,n.memory+0x200);money.append({'timer':timer,'base':bases[0]})
ready=[]
for flash in [0,1]:
 n.cpu.mem_write(g,bytes(0x500000));put(0x32f9b8,flash);put(0x32fc3c,814);put(0x32fc40,510);cuts=[]
 def natural():cuts.append([signed(reg(4)),signed(reg(2)),signed(reg(3))]);return 0
 n.helpers={0xa08564:1,0x444988:0,0xa930e0:0,0x449aec:960,0x449c84:0,0x449d44:0,0x4460b0:natural}
 n.call(0x5d1f2c,g,n.memory+0x200);ready.append({'flash':flash,'cuts':cuts})
n.cpu.mem_write(g,bytes(0x500000));put(0x32fc4c,-48);put(0x32fc50,519);cuts=[]
n.helpers={0xa08564:1,0x444988:0,0x5c2a5c:7,0x449c34:0,0x449d44:0,0x4460b0:natural}
n.call(0x5d2408,g,n.memory+0x200)
out={'version':'15.7.2','abi':'arm64-v8a','nativeSha256':SHA,'swipes':swipes,'camera':camera,'pause':pause,'money':money,'ready':ready,'walletMax':cuts,'volumeBgm':list(struct.unpack('<4i',n.cpu.mem_read(0x2b14a0,16))),'volumeSe':list(struct.unpack('<4i',n.cpu.mem_read(0x2b1bf0,16)))}
(ROOT/'native/kbcs-core/tests/battle-controls-vectors.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8-sig')
print(json.dumps({'swipes':len(swipes),'camera':camera,'pauseWidths':[row['width'] for row in pause],'money':len(money),'ready':ready,'walletMax':cuts,'volumeBgm':out['volumeBgm'],'volumeSe':out['volumeSe']}))
