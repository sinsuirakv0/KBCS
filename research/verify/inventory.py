"""原本アイテム定義と通常所持数の加算・変換・上限を現版命令で照合する。"""
import argparse
import csv
import io
import json
from pathlib import Path
import sqlite3
import struct
import sys
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--assets',type=Path,required=True)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,Assets,ROOT,SHA,digest
class InventoryNative(Native):
    def hook(self,cpu,address,size,data):
        if hasattr(self,'allowed') and address not in self.helpers and address not in self.terminals and address!=self.stop:
            if any(begin<=address<end for begin,end in self.allowed):return
        super().hook(cpu,address,size,data)
native=InventoryNative();game=0x40000000;native.cpu.mem_map(game,0x800000)
addresses=['006f23b4','006f1e2c','006f3154','00adbf54','00adbf88','006f18c4','006e34b0','006f2f8c','007dcdc4','007dc944','007dcb94']
with sqlite3.connect((native.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    native.allowed=[(int(a,16),int(a,16)+size) for a,size in db.execute('SELECT address,size FROM functions WHERE address IN ('+','.join('?' for _ in addresses)+')',addresses)]
assets=Assets(args.assets)
rows=[r for r in csv.reader(io.StringIO(assets.text('Data/Gatyaitembuy.csv'))) if r and r[0].strip().isdigit()]
assert len(rows)==275
rows=[[int(v) for v in row[:12]] for row in rows]
def write(address,value,wide=False):native.cpu.mem_write(address,struct.pack('<Q' if wide else '<I',value&((1<<(64 if wide else 32))-1)))
def encode():
    # 数値を難読化するOS乱数キーだけ0にする。ゲーム抽選の0044a8d8は置換しない。
    pointer=native.cpu.reg_read(native.reg.UC_ARM64_REG_X0);native.cpu.mem_write(pointer+4,bytes(4));return 0
for index,row in enumerate(rows):
    pointer=game+0x392460+index*0x40
    native.helpers={0x464a44:0,0x464a64:lambda:row[native.cpu.reg_read(native.reg.UC_ARM64_REG_W1)],
                    0x5c3468:encode,native.stop+0x100:12}
    native.cpu.mem_write(native.memory,struct.pack('<Q',native.memory+0x100))
    write(native.memory+0x128,native.stop+0x100,True)
    native.call(0x6f53b8,pointer,native.memory)
    actual=list(struct.unpack('<16i',native.cpu.mem_read(pointer,64)))
    expected=[row[0],0,row[2],0,row[3],0,row[4],0,*row[5:12],int(row[1]!=0)]
    assert actual==expected,(index,actual,expected)

# 可変長ストックの実行時領域を用意し、カテゴリ4の実getter/setterも通す。
stock=native.memory+0x9000
stock_count=max(row[7] for row in rows if row[6]==4)+1
write(game+0x40a528,stock,True);write(game+0x40a530,stock+stock_count*8,True)

def storage(index):
    row=rows[index];category,slot=row[6:8]
    bases={1:(0x3346f4,4),3:(0x4a5b0,8),5:(0x448a2c,8),6:(0x448a5c,8),7:(0x448a74,8),
           8:(0x34a8,8),10:(0x3660,8),11:(0x10ac,4),12:(0x3670,8),13:(0x1b0,4)}
    if category==4:return stock+slot*8+4,9999,4
    if index in [105,157,207,247]:
        base,limit,width={105:(0x1eea,9999,2),157:(0x2668,9999,8),207:(0x478,999999,4),247:(0x6f0,999999,4)}[index]
        return game+base,limit,width
    if category in bases:
        base,width=bases[category];return game+base+slot*width,9999,width
    if index in [6,7,20]:return game+{6:0xc3b8,7:0xc3c0,20:0x3346e4}[index],99999999 if index==6 else 9999,8
    return None

def target(index):
    visited=[]
    while rows[index][8]!=-1:
        assert index not in visited;visited.append(index);index=rows[index][8]
        assert 0<=index<len(rows)
    return index,visited

supported=[];unsupported=[];definitions=[]
for index,row in enumerate(rows):
    end,chain=target(index);slot=storage(end)
    definitions.append({'redirect':row[8],'factor':row[4],'limit':storage(index)[1] if storage(index) else -1})
    (supported if slot else unsupported).append(index)

vectors=[];actual=[]
for index in supported:
    end,chain=target(index);pointer,limit,width=storage(end)
    for current in [0,limit-1,limit]:
        for amount in [0,1,3]:
            native.cpu.mem_write(pointer,bytes(width));write(pointer,current)
            native.helpers={0x81f580:game,0x5c3468:encode}
            assert native.call(0x6f1e2c,index)==current,(index,'getter')
            native.call(0x6f23b4,index,amount,0)
            value=struct.unpack('<h' if width==2 else '<i',native.cpu.mem_read(pointer,2 if width==2 else 4))[0]
            assert native.call(0x6f1e2c,index)==value
            total=current+amount*(rows[index][4] if chain else 1)
            for intermediate in chain[1:]:total*=rows[intermediate][4]
            expected=min(total,limit)
            assert value==expected,(index,current,amount,value,expected)
            entry={'index':index,'target':end,'current':current,'amount':amount,'total':value,'limit':limit,'chain':chain}
            actual.append(entry)
            if index in [0,6,7,10,80,85,140,187,20,105,157,207,247]:vectors.append(entry)
# 多段変換では既存所持数を含む合計も後続の倍率を通る。
nested=[]
for current in [0,50]:
    pointer=game+0xc3b8;native.cpu.mem_write(pointer,bytes(8));write(pointer,current)
    for index,destination,factor in [(0,1,2),(1,6,3)]:
        write(game+0x392460+index*0x40+0x2c,destination)
        write(game+0x392460+index*0x40+0x18,factor)
        write(game+0x392460+index*0x40+0x1c,0)
    native.helpers={0x81f580:game,0x5c3468:encode}
    native.call(0x6f23b4,0,5,0)
    value=struct.unpack('<i',native.cpu.mem_read(pointer,4))[0]
    assert value==(current+5*2)*3
    nested.append({'current':current,'amount':5,'total':value})
for index in [0,1]:
    row=rows[index];write(game+0x392460+index*0x40+0x2c,row[8]);write(game+0x392460+index*0x40+0x18,row[4])
# 報酬CSVのIDから検索し、実際の付与入口を通す。ID−1の定義は報酬扱いしない。
grants=[];lookup={}
for index,row in enumerate(rows):lookup.setdefault(row[3],index)
for identifier,index in sorted(lookup.items()):
    if identifier<0 or index not in supported:continue
    end,chain=target(index);pointer,limit,width=storage(end)
    for current in [0,limit-1]:
        amount=3;native.cpu.mem_write(pointer,bytes(width));write(pointer,current)
        write(game+0x83dfc,0);mask=0x01020304;stage=game+0x38b168
        write(stage+0xb8,mask);write(stage+6*4,identifier^mask);write(stage+7*4,amount^mask)
        native.helpers={0x81f580:game,0x5c3468:encode}
        native.entry=0x6e34b0
        for name,value in [('X0',game),('X1',6),('X2',0),('SP',native.stack+0x8000),('LR',native.stop)]:
            native.cpu.reg_write(getattr(native.reg,'UC_ARM64_REG_'+name),value)
        native.cpu.emu_start(native.entry,native.stop+4,count=100000)
        assert native.cpu.reg_read(native.reg.UC_ARM64_REG_PC)==native.stop
        status=native.cpu.reg_read(native.reg.UC_ARM64_REG_W0);assert status==0
        value=struct.unpack('<h' if width==2 else '<i',native.cpu.mem_read(pointer,2 if width==2 else 4))[0]
        expected=min(current+amount*(rows[index][4] if chain else 1),limit)
        assert value==expected,(identifier,index,current,value,expected)
        grants.append({'rewardId':identifier,'index':index,'current':current,'amount':amount,'total':value,'status':status})
report={'version':'15.7.2','architecture':'arm64-v8a','sha256':SHA,'build':assets.current,
        'scope':'Native definition reader all275; numeric add/get/set with real redirect and limit branches for supported categories; only OS numeric-obfuscation key fixed to zero; no account save or special currency/unlock handlers',
        'evidence':{a:digest((native.cache/'code'/(a+'.c')).read_bytes()) for a in [*addresses,'006f53b8','005c3468']},
        'sources':assets.sources,'rows':rows,'definitions':definitions,'supported':supported,'unsupported':unsupported,
        'vectors':vectors,'actual':actual,'grants':grants,'nested':nested}
(ROOT/'research/.local/inventory-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:
    fixture={k:v for k,v in report.items() if k not in ['actual','rows','sources','build','grants']}
    (ROOT/'native/kbcs-core/tests/inventory-vectors.json').write_text(json.dumps(fixture,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'definitions':len(rows),'supported':len(supported),'unsupported':len(unsupported),'cases':len(actual),'vectors':len(vectors),'grantCases':len(grants)}))
