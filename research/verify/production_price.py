"""特殊ルール11の生産価格を005be130の実命令へ比較する。"""
import argparse,ctypes as c,itertools,json,os,sqlite3,struct,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path,required=True);a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
n=Native();g=0x40000000;n.cpu.mem_map(g,0x500000)
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:n.ends[0x5be130]=0x5be130+db.execute("SELECT size FROM functions WHERE address='005be130'").fetchone()[0]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()))
class Price(c.Structure):_fields_=[(k,c.c_int32) for k in ['base','last_cost','count']]+[('rule',c.c_int32*3)]
lib.kbcs_core_production_price.argtypes=[c.POINTER(Price),c.POINTER(c.c_int32)]
class RuleError(Exception):pass
def invalid_rule():raise RuleError()
cases=0;invalid=0
for rule,base,last in itertools.product([[],[0,0],[0,99],[0,200,99999],[1,10],[1,99,99999],[1,200,1],[2]],[0,1,9999,15000,109900,9999900],[0,9999,22000,9999900]):
 i=Price(base,last,len(rule));i.rule[:]=(rule+[0,0,0])[:3];out=c.c_int32(-9)
 # 27a8は直近価格。生産済み回数ではなく価格の非0を検査する。
 n.cpu.mem_write(g+0x27a8,struct.pack('<i',last))
 node=n.memory+0x1000;values=n.memory+0x2000;n.cpu.mem_write(node,struct.pack('<QQ',values,values+len(rule)*4));n.cpu.mem_write(values,struct.pack('<3i',*i.rule))
 n.helpers={0x81f580:g,0x5c2710:1,0x7cf950:0,0x644304:node if rule else 0,0x5bc280:42,0xaa0568:base,0x47c518:invalid_rule}
 try:expected=n.call(0x5be130,0,0)
 except RuleError:expected=None
 code=lib.kbcs_core_production_price(c.byref(i),c.byref(out))
 if expected is None:assert code==1 and out.value==-9,(rule,base,last,code,out.value);invalid+=1
 else:assert code==0 and out.value==expected,(rule,base,last,code,out.value,expected);cases+=1
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(a.library.read_bytes()),'entry':'005be130','cases':cases,'invalidRules':invalid,'controlled':['profile base cost and special-rule lookup','singleton/mode/profile getters'],'result':'equal'}
(ROOT/'research/.local/production-price-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig');print(json.dumps(report))
