"""保存済み背景を同じC++描画経路で一括評価する（GPU画像一致の試験ではない）。"""
import argparse, json, sqlite3, subprocess, tempfile, time
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--exe',type=Path,required=True)
parser.add_argument('--data-dir',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
pointer=json.loads((args.data_dir/'current.json').read_text(encoding='utf-8-sig'))
path=args.data_dir/'official'/pointer['regions']['jp']
with sqlite3.connect(path.resolve().as_uri()+'?mode=ro',uri=True) as database:
 raw=database.execute("select bytes from source_file where path='Data/bg.csv'").fetchone()[0].decode('utf-8-sig')
 ids=[int(line.split(',')[0]) for line in raw.splitlines() if len(line.split('//')[0].split(','))>=15 and line.split(',')[0].strip().isdigit()]
 inputs=[dict(background=id,width=10000,castle=6,castleSet=3,frame=frame) for id in ids for frame in [0,31,300,7]]
 for actor in [0,42,574]:
  inputs.append(dict(background=0,width=10000,castleSet=3,enemyCastle=actor,frame=31))
start=time.monotonic()
with tempfile.TemporaryDirectory(prefix='kbcs-scene-') as temporary:
 source=Path(temporary)/'input.json';source.write_text(json.dumps(inputs),encoding='utf-8')
 result=subprocess.run([str(args.exe.resolve()),'scene','--data-dir',str(args.data_dir),'--input',str(source),'--summary'],capture_output=True,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0),timeout=300)
 if result.returncode:raise RuntimeError(result.stderr.decode('utf-8','replace'))
 rows=[json.loads(line) for line in result.stdout.decode('utf-8-sig').splitlines()]
 assert len(rows)==len(inputs)
 assert all(row['core']=='C++' and row['commands']>0 for row in rows)
 report=dict(database=str(path),backgrounds=len(ids),conditions=len(rows),seconds=round(time.monotonic()-start,3),missing=[row for row in rows if row['missing']],staticModels=[row for row in rows if row['issues']])
 args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig')
 print(json.dumps({key:len(value) if isinstance(value,list) else value for key,value in report.items()},ensure_ascii=False))
