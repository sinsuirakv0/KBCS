"""スコア旗確認後の章/通常モードの保存先選択を現版命令で照合する。"""
import sys,struct,json,argparse
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument("--python-libs",type=Path,required=True);args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA
n=Native();game=0x40000000;n.cpu.mem_map(game,0x800000);stack=n.stack+0x8000;modeptr=n.memory+0x3000
for offset,pointer in [(0xd0,modeptr),(0xe8,game+0x83dfc),(0xf8,game)]:n.cpu.mem_write(stack+offset,struct.pack('<Q',pointer))
result=[]
for mode in [0,3,4,5,6,7,99]:
 for save in [-1,17]:
  n.cpu.mem_write(modeptr,struct.pack('<i',mode));n.cpu.mem_write(game+0x3c3334,struct.pack('<i',save));n.cpu.mem_write(game+0x83dfc,struct.pack('<i',2));n.cpu.mem_write(game+0x39797c,struct.pack('<i',1))
  n.entry=0x5dd5b8;n.helpers={};n.terminals={0x5dd634,0x5ddd8c}
  for register,value in [('SP',stack),('X19',game+0x3c32c8),('X11',game+0x83dfc)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
  n.cpu.emu_start(n.entry,n.stop,count=200)
  pc=n.cpu.reg_read(n.reg.UC_ARM64_REG_PC);active=pc==0x5dd634
  assert pc in n.terminals
  assert active==(mode in [4,5,6] or save!=-1),(mode,save,hex(pc))
  saved=n.cpu.reg_read(n.reg.UC_ARM64_REG_X9)
  if active:assert saved==game+0x3c3720+(mode-4)*0xcc+8 if mode in [4,5,6] else saved==game+0x3b7680+save*0xf0+2*0x10+4
  result.append(dict(mode=mode,saveId=save,active=active,pointer=hex(saved) if active else None))
(ROOT/'research/.local/chapter-score-gate-1572.json').write_text(json.dumps({'sha256':SHA,'scope':'005dd5b8から有効スコア区間/skipまで。スコア旗確認後の保存先選択。','vectors':result},ensure_ascii=False,indent=2)+'\n',encoding='utf-8-sig')
print(json.dumps(result))
