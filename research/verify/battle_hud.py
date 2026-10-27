"""実DBの再生結果を005d18a4の実命令へ渡し、再生産ゲージの色と矩形を照合する。"""
import argparse,json,re,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--replay',type=Path,required=True)
args=parser.parse_args();sys.path.insert(0,str(args.python_libs))
from stages import Native,ROOT,SHA
n=Native();g=0x40000000;n.cpu.mem_map(g,0x500000)
# ELFのGOT relocation。表自体は同じ原本の.dataから読む。
n.cpu.mem_write(0xc1b5b8,struct.pack('<Q',0xc23f98))
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 row=db.execute("SELECT size FROM functions WHERE address='005d18a4'").fetchone();n.ends[0x5d18a4]=0x5d18a4+row[0]
 allocations={int(a,16):n.memory+0x2000 if 'new' in name else 0 for a,name in db.execute("SELECT address,name FROM functions WHERE name LIKE 'operator.new%' OR name LIKE 'operator.delete%'")}
def reg(i):return n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))
def signed(value):return struct.unpack('<i',struct.pack('<I',value&0xffffffff))[0]
def put(offset,value):n.cpu.mem_write(g+offset,struct.pack('<i',value))
records=[];seen=set()
for response in json.loads(args.replay.read_text(encoding='utf-8-sig')):
 state=response['state'];layout=response['layout'];runtime=response['runtime']
 for slot,gauge in enumerate(runtime['hud']['gauges']):
  if not gauge[2]:continue
  maximum=runtime['maximum'][slot];wait=runtime['wait'][slot]
  signature=(slot,state['rows'],wait,maximum)
  if not maximum or signature in seen:continue
  seen.add(signature);n.cpu.mem_write(g,bytes(0x500000));put(0x2820+slot*4,1)
  n.cpu.mem_write(g+0x1405,bytes([state['rows']==2]));color=[];rectangles=[]
  put(0x32f804,gauge[1]-(606-(95 if state['rows']==2 and slot<5 else 0)))
  expected_x=gauge[0];shift=expected_x-[165,295,425,555,685,177,307,437,567,697][slot%5 if state['rows']==2 else slot]
  width=960+shift*2
  def paint():color[:]=[signed(reg(i)) for i in range(1,5)];return 0
  def rectangle():rectangles.append({'color':color.copy(),'rect':[signed(reg(i)) for i in range(1,5)]});return 0
  n.helpers={**allocations,0x58c05c:maximum,0x5c2d18:wait,0x5c2e40:maximum,0x9019f4:95,0x444c54:paint,0x44507c:rectangle,0x449aec:width}
  n.call(0x5d18a4,g,n.memory,slot)
  x,y,_,cyan,red=gauge
  expected=[{'color':[0,0,0,255],'rect':[x,y,97,14]},{'color':[255,0,0,255],'rect':[x+2,y+2,red,10]},{'color':[0,255,255,255],'rect':[x+2,y+2,cyan,10]}]
  assert rectangles==expected,(signature,rectangles,expected)
  records.append({'slot':slot,'wait':wait,'maximum':maximum,'rows':state['rows'],'rectangles':rectangles})
assert records,'再生産中の記録がありません'
report={'version':'15.7.2','nativeSha256':SHA,'cases':len(records),'entry':'005d18a4','controlled':['recharge/remaining/maximum getters','parameter lookup','allocator','viewport','draw calls'],'records':records}
(ROOT/'research/.local/battle-hud-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig')
print(json.dumps({'cases':len(records),'result':'equal'}))
