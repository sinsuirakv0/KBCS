"""検証済みJP15.7.2原本から戦闘HUDの矩形・出典を同期する。"""
import argparse,csv,io,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'research/verify'))
from stages import Assets,SHA,digest
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('assets',type=Path)
args=parser.parse_args();assets=Assets(args.assets)
output={'version':'15.7.2','buildId':assets.current['buildId'],'nativeSha256':SHA,'atlases':{}}
destination=root/'ui/images/native-battle'
destination.mkdir(parents=True,exist_ok=True)
for stem in ['img001_ja','img002_ja','mapicon','uni','img100_ja','img015','img004_ja','img004_DOJO_ja','img101','img101_nekoDojo','img005_1','img006_ja','img031_ja']:
    key='ImageData/'+stem+'.imgcut';lines=assets.text(key).splitlines()
    rects=[[int(cell) for cell in line.split(',')[:4]] for line in lines[4:4+int(lines[3])]]
    image=('Unit/' if stem=='uni' else 'Image/')+stem+'.png';entry=assets.files[image]
    source=(assets.root/entry['path']).resolve();source.relative_to(assets.root)
    data=source.read_bytes()
    assert len(data)==entry['size'] and digest(data)==entry['sha256'],image
    (destination/(stem+'.png')).write_bytes(data)
    output['atlases'][stem]={'image':image,'url':'/images/native-battle/'+stem+'.png','rects':rects,'sources':{path:assets.files[path] for path in [key,image]}}
items=list(csv.reader(io.StringIO(assets.text('res/GatyaitemName.csv'))))[:6]
output['items']=[{'name':row[0],'lines':[cell for cell in row[1:] if cell and cell!='＠']} for row in items]
normal=next(line.split('\t',1)[1] for line in assets.text('res/localizable.tsv').splitlines() if line.startswith('speedup_message\t'))
output['normalSpeedLines']=re.sub(r'<(?!br>)[^>]*>','',normal).split('<br>')
output['localizationSource']=assets.files['res/localizable.tsv']
output['itemSource']=assets.files['res/GatyaitemName.csv']
(destination/'manifest.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8-sig')
