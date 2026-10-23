"""日本編の章倍率が出現行倍率を使わない経路を、同版ARM64で確認する。"""
import argparse,json,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--python-libs',type=Path,required=True);args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA,digest,read_json
from elftools.elf.elffile import ELFFile
n=Native();game=0x40000000;n.cpu.mem_map(game,0x800000);n.ends.update({0xa9e9fc:0xa9f0e0,0xa9fb88:0xaa02d0})
identity=read_json(n.cache/'identity.json');address=None
with Path(identity['binary']).open('rb') as stream:
 for section in ELFFile(stream).iter_sections():
  if hasattr(section,'iter_relocations'):
   for relocation in section.iter_relocations():
    if relocation['r_offset']+0x100000==0xc1b770:address=relocation['r_addend']+0x100000
assert address is not None
n.cpu.mem_write(0xc1b770,struct.pack('<Q',address))
coefficients=list(struct.unpack('<3i',n.cpu.mem_read(address,12)));assert coefficients==[0,5,30]
rows=n.memory+0x2000;n.cpu.mem_write(game+0x9ee70,struct.pack('<Q',rows));n.cpu.mem_write(rows,bytes(56))
vectors=[]
for chapter in range(3):
 for base in [1,101,1001]:
  n.cpu.mem_write(game+0x32f934,struct.pack('<i',chapter))
  for function,column in [(0xa9e9fc,0),(0xa9fb88,3)]:
   pointer=game+0x239da8+2*0x1c4;n.cpu.mem_write(pointer,bytes(0x1c4));n.cpu.mem_write(pointer+column*4,struct.pack('<i',base))
   n.helpers={0x81f580:game,0x5c2710:0}
   actual=n.call(function,1,0,0,1,0,0,0,0)
   rate=(coefficients[chapter]+10)*10;expected=(base*rate+50)//100
   assert actual==expected,(chapter,base,function,actual,expected)
   vectors.append(dict(chapter=chapter,base=base,rate=rate,function=f'{function:08x}',result=actual))
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,'scope':'日本編mode0..2・ゾンビなし・通常敵・体力と第1攻撃。GOTの該当1件を同じSOのrela addendで復元。原本の出現行倍率は0にして不使用を確認。','tableAddress':hex(address),'coefficients':coefficients,'evidence':{a:digest((n.cache/'code'/(a+'.c')).read_bytes()) for a in ['00a9e9fc','00a9fb88']},'vectors':vectors}
(ROOT/'research/.local/chapter-enemies-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8-sig');print(json.dumps({'cases':len(vectors),'rates':[100,150,400]}))
