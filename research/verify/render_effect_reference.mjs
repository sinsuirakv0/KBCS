// 既存評価器との回帰資料。リポジトリのルートから実行する。
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {parseMaAnim} from '../../ui/src/features/motion/motion-engine.js';
import {pathToFileURL} from 'node:url';
const lab=process.argv[3]||'D:/KBC/KBC-rakv0-lab';
const {createEffectSystem}=await import(pathToFileURL(lab+'/stage-db/scene-effects.js'));
const {createClassicEffects}=await import(pathToFileURL(lab+'/stage-db/scene-classic.js'));
const root=process.argv[2]||'D:/KBC/KBC-rakv0-assets',current=JSON.parse(await readFile(root+'/metadata/jp/current.json','utf8'));
const index=JSON.parse(await readFile(root+'/'+current.generatedPath+'/indexes/assets.json','utf8'));
async function text(path){const d=index.files[path];if(!d)return '';const bytes=await readFile(root+'/'+d.path);if(createHash('sha256').update(bytes).digest('hex')!==d.sha256)throw Error(path);return bytes.toString('utf8').replace(/^\uFEFF/,'');}
const rows=(await text('Data/bg.csv')).split(/\r?\n/).map(line=>line.split('//')[0].split(',').map(Number)).filter(r=>r.length>14&&Number.isInteger(r[0]));
const names=['star','snow','bubble','balloon','shine','splash','rain','rock','fall','wind'];
const cases=[];
for(const background of [2,33,110,1079]){
 let id=background,data;const seen=new Set();
 while(true){if(seen.has(id))throw Error('cycle');seen.add(id);data=JSON.parse((await text('Data/bg'+String(id).padStart(3,'0')+'.json'))||'{}');if(data.id!=null){id=data.id;continue;}break;}
 const cut=rows.find(r=>r[0]===id)[13],segments=[],lengths=[],counts=[];
 for(const raw of data.data||[]){
  const models=raw.model?.values??(raw.model?.value!=null?[raw.model.value]:[]);
  const files=raw.file?[raw.file.anime]:models.map(value=>'bg'+String(cut).padStart(2,'0')+'_'+String(value).padStart(2,'0')+'.maanim');
  const assets=[];
  for(const file of files){let length=0;if(!file.endsWith('.mamodel')){const path=['ImageData/','Image/','Number/'].map(prefix=>prefix+file).find(p=>index.files[p]);if(!path)throw Error(file);length=Math.max(0,...parseMaAnim(await text(path)).tracks.map(track=>track.lastFrame));}assets.push({id:lengths.length,length});lengths.push(length);}
  segments.push({parameters:raw,assets});counts.push(assets.length);
 }
 const width=10000,worldWidth=width*.4,minimum=Math.min(1,960/worldWidth),world={width:worldWidth,zoomPercent:minimum*100,margin:960/minimum-worldWidth,top:Math.ceil(40*minimum-20)+480-Math.trunc(500/minimum),bottom:520+Math.trunc(120/minimum)};
 const classic=[2,33].includes(background)?background:-1,vectors=[];
 for(const frame of [0,1,7,31,300,7]){
  let state=0x12345678;const random=()=>{state^=state<<13;state^=state>>>17;state^=state<<15;return (state>>>0)/4294967296;};
  const system=createEffectSystem(segments,world,random),weather=createClassicEffects(classic,world,random);
  for(let i=0;i<frame;i++){system.update();weather.update();}
  const all=system.particles.filter(p=>p.wait<=0).map(p=>({asset:p.asset.id,front:Number(p.front),kind:0,variant:0,x:p.x,y:p.y,frame:p.frame,scale:p.scale,sx:p.sx,sy:p.sy,angle:p.angle,alpha:p.alpha,spacing:p.spacing?.value||0,spacing_min:p.spacing?.min||0,spacing_max:p.spacing?.max||0,color:[0,0,0]}));
  for(const front of [false,true])for(const p of weather.commands(front))all.push({asset:-1,front:Number(front),kind:names.indexOf(p.kind)+1,variant:p.variant,x:p.x,y:p.y,frame:0,scale:p.size,sx:1,sy:1,angle:p.angle,alpha:p.opacity*255,spacing:0,spacing_min:0,spacing_max:0,color:p.color||[255,255,255]});
  const indices=[...new Set([0,1,2,7,15,29,30,Math.floor(all.length/2),all.length-2,all.length-1].filter(i=>i>=0&&i<all.length))].sort((a,b)=>a-b);
  vectors.push({frame,count:all.length,samples:indices.map(index=>({index,value:all[index]}))});
 }
 cases.push({background,width,classic,parameters:segments.map(s=>s.parameters),lengths,counts,vectors});
}
await writeFile('native/kbcs-core/tests/scene-effect-vectors.json',JSON.stringify({version:current.versionName,reference:'Existing scene interpretation with limited ARM v15.7.1 checks; explicit Xorshift32 seed, not the original full RNG sequence',cases}));
console.log(cases.map(c=>[c.background,c.lengths.length,c.vectors[0].count]));
