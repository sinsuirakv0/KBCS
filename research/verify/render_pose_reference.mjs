// 既存評価器との回帰資料。リポジトリのルートから実行する。
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {parseImgCut,parseMaModel,parseMaAnim,buildNativeDrawPackets} from '../../ui/src/features/motion/motion-engine.js';
const root=process.argv[2]||'D:/KBC/KBC-rakv0-assets',current=JSON.parse(await readFile(root+'/metadata/jp/current.json','utf8'));
const index=JSON.parse(await readFile(root+'/'+current.generatedPath+'/indexes/assets.json','utf8'));
async function text(path){const descriptor=index.files[path];if(!descriptor)throw Error(path);const data=await readFile(root+'/'+descriptor.path);if(createHash('sha256').update(data).digest('hex')!==descriptor.sha256)throw Error('sha');return data.toString('utf8');}
const inputs=[['000_f','000_f02'],['042_s','042_s02'],['644_e','644_e02']];
for(const path of Object.keys(index.files)){if(/^ImageData\/bg\d+_\d+\.mamodel$/.test(path)){const stem=path.slice(10,-8);if(index.files['ImageData/'+stem+'.maanim']){inputs.push([stem,stem]);break;}}}
const cases=[];
for(const [stem,animation]of inputs){
 const cutStem=stem.startsWith('bg')?stem.split('_')[0]:stem;
 const input={cut:await text('ImageData/'+cutStem+'.imgcut'),model:await text('ImageData/'+stem+'.mamodel'),animation:await text('ImageData/'+animation+'.maanim')};
 const imgcut=parseImgCut(input.cut),model=parseMaModel(input.model),motion=parseMaAnim(input.animation),project={imgcut,model,motions:{main:motion},image:{width:4096,height:4096}};
 const vectors=[];
 for(const frame of [0,1,15,30,61,300])for(const loop of [false,true])for(const facing of [1,-1]){
  const value=buildNativeDrawPackets(project,'main',frame,{loop,facing,useModelAnchor:true});
  vectors.push({frame,loop,facing,packets:value.packets.map(p=>({part:p.partIndex,cut:value.parts.find(part=>part.index===p.partIndex).imageIndex,blend:p.blendMode,opacity:p.opacity,points:p.positions}))});
 }
 cases.push({stem,input,vectors});
}
await writeFile('native/kbcs-core/tests/pose-vectors.json',JSON.stringify({version:current.versionName,buildId:current.buildId,reference:'Existing integer evaluator with limited ARM validation; not a fresh complete native rendering comparison',cases}));
console.log(cases.map(c=>[c.stem,c.vectors.length]));
