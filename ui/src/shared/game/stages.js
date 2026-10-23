const url='/api/stages';
let pending;
const maps=new Map();
async function readJson(path){const response=await fetch(path);if(!response.ok){const value=await response.json().catch(()=>({}));throw Error(value.error||'ステージデータを読み込めませんでした。');}return response.json();}
export function loadStageDatabase(){
  if(!pending)pending=readJson(url).then(value=>{if(value.schemaVersion!==2||!value.maps?.length||!value.stages?.length)throw Error('ステージデータの形式が不正です。');return value;}).catch(error=>{pending=null;throw error;});
  return pending;
}
export async function loadStageDetail(database,id){
  const stage=database.stages.find(stage=>stage.id===id);if(!stage)throw Error('ステージIDが見つかりません。');
  return (await loadStageMap(database,stage.map)).find(value=>value.id===id);
}
export async function loadStageMap(database,key){
  if(!maps.has(key))maps.set(key,readJson(url+'?'+new URLSearchParams({map:key})).then(value=>{if(value.schemaVersion!==2||value.buildId!==database.buildId||value.revision!==database.revision)throw Error('DBが更新されています。ページを再読み込みしてください。');return value.stages;}).catch(error=>{maps.delete(key);throw error;}));
  return maps.get(key);
}
export async function loadStageVariant(map,index,source){return readJson('/api/stage-variant?'+new URLSearchParams({map,stage:index,source}));}
