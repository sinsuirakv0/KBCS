"""戦闘用の二種類のモーション長を0044beb4/0044bf2cへ直接比較する。"""
import argparse
import ctypes as c
import itertools
import json
import os
from pathlib import Path
import struct
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs',type=Path,required=True)
parser.add_argument('--assets',type=Path,required=True)
parser.add_argument('--library',type=Path,required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args();sys.path.insert(0,str(args.python_libs.resolve()))
from stages import Native,Assets,ROOT,SHA
class Track(c.Structure):_fields_=[(k,c.c_int32) for k in ['part','property','loop','first','count']]
class Key(c.Structure):_fields_=[(k,c.c_int32) for k in ['frame','value','easing','power']]
assets=Assets(args.assets);native=Native()
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(args.library.resolve()));lib.kbcs_core_motion_lengths.argtypes=[c.POINTER(Track),c.c_int32,c.POINTER(Key),c.c_int32,c.POINTER(c.c_int32)]
def compare(tracks):
 values=(Track*len(tracks))();keys=[]
 for i,(repeat,frames) in enumerate(tracks):
  values[i]=Track(loop=repeat,first=len(keys),count=len(frames));keys.extend(Key(frame=f) for f in frames)
  data=native.memory+0x4000+values[i].first*16
  native.cpu.mem_write(native.memory+0x1000+i*40,struct.pack('<iiiiQ',0,0,repeat,len(frames),data)+bytes(16))
  if frames:native.cpu.mem_write(data,b''.join(struct.pack('<iiii',f,0,0,0) for f in frames))
 native.cpu.mem_write(native.memory,struct.pack('<QQQI',native.memory+0x1000,0,0,len(tracks)))
 expected=[native.call(0x44beb4,native.memory),native.call(0x44bf2c,native.memory)]
 out=(c.c_int32*2)();assert lib.kbcs_core_motion_lengths(values,len(values),(Key*len(keys))(*keys),len(keys),out)==0
 assert list(out)==expected,(tracks,expected,list(out))
 return expected
records=[]
for repeat,first,last,count in itertools.product([-1,0,1,2,3],[-1,0,3],[0,9,99],[0,1,2]):
 frames=[] if not count else [last] if count==1 else [first,last]
 records.append({'repeat':repeat,'frames':frames,'lengths':compare([(repeat,frames)])})
models=json.loads((ROOT/'research/.local/battle-clock-models.json').read_text(encoding='utf-8-sig'));clocks={}
for offset,path in models.items():
 lines=assets.text(path).splitlines();cursor=3;tracks=[]
 for i in range(int(lines[2])):
  header=[int(v) for v in lines[cursor].split(',')[:5]];cursor+=1;count=int(lines[cursor]);cursor+=1
  frames=[int(lines[cursor+j].split(',')[0]) for j in range(count)];cursor+=count
  tracks.append((header[2],frames))
 clocks[offset]={'path':path,'lengths':compare(tracks),'source':assets.sources[path]}
report={'version':'15.7.2','sha256':SHA,'cases':len(records),'records':records,'clocks':clocks}
(ROOT/'research/.local/actor-motion-lengths-1572.json').write_text(json.dumps(report,indent=2),encoding='utf-8-sig')
if args.publish:
 path=ROOT/'crates/kbcs-data/resources/battle-inputs.json';data=json.loads(path.read_text(encoding='utf-8-sig'));data['clocks']=clocks
 data.setdefault('clockSource',{}).update({'function':'009f560c','loader':'0044ba98','lengths':['0044beb4','0044bf2c']})
 path.write_text(json.dumps(data,separators=(',',':')),encoding='utf-8-sig')
print(json.dumps({'syntheticCases':len(records),'actualClocks':clocks}))
