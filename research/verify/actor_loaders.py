"""CSVのセル取得だけを制御し、個体定義の既定値と単位変換を実命令で照合する。"""
import argparse
import ctypes as c
import json
import os
from pathlib import Path
import sqlite3
import struct
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--library',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA

runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()))
lib.kbcs_core_actor_load.argtypes=[c.POINTER(c.c_int32),c.c_int32,c.c_int32,c.POINTER(c.c_int32)]
n=Native();game=0x40000000;n.cpu.mem_map(game,0x800000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    n.ends.update({int(a,16):int(a,16)+size for a,size in db.execute("SELECT address,size FROM functions WHERE address IN ('009a67f4','009a6c68')")})
n.terminals={0x465780}
records=[]
for unit in [1,0]:
    rows=[list(range(1,120)),list(range(10)),list(range(119)),[0]*67] if unit else [list(range(1,114)),[],list(range(7))]+[[] for _ in range(801)]
    position=-1;current_column=-1
    def next_row():
        global position
        position+=1
        return int(position<len(rows))
    def count():return len(rows[position])
    def integer():
        global current_column
        current_column=n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)
        return rows[position][current_column]
    # 味方は整数の再フォーマット結果が一致しなかった列から後を読まない。
    def canonical():return int(not (unit and position==2 and current_column==7))
    n.helpers={0x464f48:0,0xab1128:1,0x464a44:next_row,0x465680:count,0x464a64:integer,
               0x464b8c:0,0x4253b4:0,0x470ac0:canonical}
    n.cpu.mem_write(game,bytes(0x500000));n.cpu.mem_write(n.stack+0x6000,bytes(0x2000))
    n.entry=0x9a67f4 if unit else 0x9a6c68
    for i in range(8):n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),game if i==0 else 0)
    n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,n.stack+0x8000);n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop)
    n.cpu.emu_start(n.entry,n.stop+4,count=15000000)
    assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==0x465780,'CSV loader instruction budget'
    for index,row in enumerate(rows):
        prefix=row[:7] if unit and index==2 else row
        values=(c.c_int32*len(prefix))(*prefix);loaded=(c.c_int32*119)()
        assert lib.kbcs_core_actor_load(values,len(prefix),unit,loaded)==0
        address=game+(0x9ee88+2*0x770+index*0x1dc if unit else 0x239da8+index*0x1c4)
        expected=list(struct.unpack('<'+('119' if unit else '113')+'i',n.cpu.mem_read(address,(119 if unit else 113)*4)))
        assert list(loaded)[:len(expected)]==expected,(unit,index,[(i,a,b) for i,(a,b) in enumerate(zip(loaded,expected)) if a!=b])
        if unit or index in [0,1,2,803]:records.append(dict(unit=unit,raw=prefix,loaded=expected+([] if unit else [0]*6)))
    print(json.dumps({'unit':unit,'rows':len(rows)}),flush=True)
result={'version':'15.7.2','sha256':SHA,'records':records,'controlled':['CSV cells/count/next/format equality','stop before stream destruction']}
(ROOT/'research/.local/actor-loaders-1572.json').write_text(json.dumps(result,indent=2),encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/actor-loader-vectors.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8-sig')
