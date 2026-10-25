"""同版ARM64の出現処理を連続実行し、候補確定後の再検査と乱数消費を照合する。"""
import argparse,json,sqlite3,struct,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,ROOT,SHA,digest

class Continuous(Native):
    def hook(self,cpu,address,size,data):
        if not getattr(self,'recording',False):return super().hook(cpu,address,size,data)
        if address==0x44a8d8:self.bounds.append(cpu.reg_read(self.reg.UC_ARM64_REG_W0))
        if address==0x9f1e64:
            self.generated.append(cpu.reg_read(self.reg.UC_ARM64_REG_X7))
            self.saved={r:cpu.reg_read(r) for r in [self.reg.UC_ARM64_REG_SP,self.reg.UC_ARM64_REG_LR,*[getattr(self.reg,'UC_ARM64_REG_X'+str(i)) for i in range(19,30)]]}
        if address==0xaa0aa4:
            # 枠探索・レイヤー抽選は実命令。その先の個体能力構築だけを成功へ置き換える。
            for r,value in self.saved.items():cpu.reg_write(r,value)
            cpu.reg_write(self.reg.UC_ARM64_REG_X0,1)
            cpu.reg_write(self.reg.UC_ARM64_REG_PC,self.saved[self.reg.UC_ARM64_REG_LR]);return
        if 0x44a8d8<=address<0x44aa50 or 0x9f1e64<=address<self.actor_end:return
        super().hook(cpu,address,size,data)

n=Continuous()
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
    n.actor_end=0x9f1e64+db.execute("SELECT size FROM functions WHERE address='009f1e64'").fetchone()[0]
game=0x40000000;n.cpu.mem_map(game,0x400000)
vectors=[]
for name,finite,castle,after,free in [('finite-zero',1,100,0,1),('castle-held-zero',0,90,1,1),('allocation-failure',1,100,0,0)]:
    row=[2,finite,0,0,0,castle,0,9,0,100,0,0,after,0]
    n.recording=False
    n.schedule({'rows':[row],'states':[[0,0,0]],'spawnResult':-1})
    n.cpu.mem_write(n.memory+0x4000,bytes(12))
    n.cpu.mem_write(game+0x84048,struct.pack('<i',0));n.cpu.mem_write(game+0x9ee50,bytes(8))
    n.cpu.mem_write(0xc24d18,struct.pack('<I',0x12345678))
    n.helpers.pop(0x44a8d8);n.helpers.pop(0x9f1e64)
    n.helpers.update({a:0 for a in [0xa9400c,0xa9478c,0x5bbc10,0xa9486c,0xa94e34,0xa94ec0,0xa9bb38,0xa9d498,0xa94f4c,0xa94fe0,0xa95220]})
    n.helpers[0xa93f08]=lambda: int(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)!=free)
    n.recording=True
    steps=[]
    for frame in range(3):
        n.generated=[];n.bounds=[]
        n.call(0x6ef2b0,game)
        steps.append({'frame':frame,'states':[list(struct.unpack('<3i',n.cpu.mem_read(n.memory+0x4000,12)))],'globalWait':struct.unpack('<i',n.cpu.mem_read(game+0x84048,4))[0],'bounds':n.bounds,'state':struct.unpack('<I',n.cpu.mem_read(0xc24d18,4))[0],'generated':n.generated.copy(),'seen':struct.unpack('<i',n.cpu.mem_read(game+0xda58,4))[0]})
    vectors.append({'name':name,'row':row,'seed':0x12345678,'success':free!=0,'steps':steps})
report={'version':'15.7.2','sha256':SHA,'scope':'006ef2b0 repeated updates, actual 009f1e64 allocation/layer path and 0044a8d8 RNG; constructor after first stat getter controlled as success; not full battle','evidence':{a:digest((n.cache/'code'/(a+'.c')).read_bytes()) for a in ['006ef2b0','009f1e64','0044a8d8','0044a8e8']},'vectors':vectors}
(ROOT/'research/.local/stage-continuous-1572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8-sig')
if args.publish:(ROOT/'native/kbcs-core/tests/stage-continuous-vectors.json').write_text(json.dumps(report,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps(vectors,indent=2))
