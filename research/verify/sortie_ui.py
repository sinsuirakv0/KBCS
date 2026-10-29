"""007acf88の出陣ボタン2部品を、解決済みviewport/押下値で実行する。"""
import argparse,json,struct,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--python-libs',type=Path,required=True);a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA
n=Native();n.ends[0x7acf88]=0x7bced8;sp=n.stack+0x8000;context=n.memory+0x1000;state=n.memory+0x2000;table=n.memory+0x3000
n.cpu.mem_write(sp+0x98,struct.pack('<Q',state));n.cpu.mem_write(context+0x138,struct.pack('<Q',9000));n.cpu.mem_write(0xc1b5b0,struct.pack('<Q',table));n.cpu.mem_write(state+0xe0,bytes(4))
cases=[(width,press)for width in [960,1188,1422,1920] for press in [0,2,4,8,-1,-3]]
uri=(ROOT/'ui/sortie-view.js').as_uri();script=f'import {{sortieLaunchLayout}} from {json.dumps(uri)};process.stdout.write(JSON.stringify({json.dumps(cases)}.map(([w,p])=>sortieLaunchLayout(w,p))));'
expected=json.loads(subprocess.check_output(['node','--input-type=module','-e',script],text=True,encoding='utf-8'));records=[]
for (width,press),want in zip(cases,expected):
 actual=[];n.cpu.mem_write(table,struct.pack('<i',press))
 for i,value in {0:width,19:context,21:0,23:9000,28:1234}.items():n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_X'+str(i)),value)
 def capture():
  values=[n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_X'+str(i)))&0xffffffff for i in range(2,7)];values=[v if v<2**31 else v-2**32 for v in values];actual.append([values[4],*values[:4]]);return 0
 n.entry=0x7acf88;n.helpers={0x446d2c:capture,0x449aec:width};n.terminals={0x7b3d2c};n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,sp);n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop)
 n.cpu.emu_start(0x7b3c98,n.stop+4,count=2000);assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==0x7b3d2c;assert actual==want,(width,press,actual,want);records.append({'width':width,'press':press,'sprites':actual})
report={'version':'15.7.2','nativeSha256':SHA,'cases':len(records),'records':records,'controlled':['viewport getter/texture pointer/press-table value','graphics callback; native arithmetic executed'],'limits':['local drawing fragment; full stage selection/input dispatch/GPU pixels not compared']};(ROOT/'research/.local/sortie-ui-1572.json').write_text(json.dumps(report,indent=2),encoding='utf-8-sig');print('native sortie button',len(records),'conditions passed')
