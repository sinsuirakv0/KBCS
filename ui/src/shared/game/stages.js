const url="/api/stages";
let pending;
async function readJson(url){const response=await fetch(url);if(!response.ok)throw Error('ステージデータを読み込めませんでした。');return response.json();}
export function loadStageDatabase(){
  if(!pending)pending=readJson(url).then(value=>{if(value.schemaVersion!==1||!value.maps?.length||!value.stages?.length)throw Error('ステージデータの形式が不正です。');return value;}).catch(error=>{pending=null;throw error;});
  return pending;
}
export async function loadStageDetail(database,id){
  const stage=database.stages.find(stage=>stage.id===id);
  if(!stage)throw Error('ステージIDが見つかりません。');
  return stage;
}
export async function loadStageMap(database,key){return database.stages.filter(stage=>stage.map===key);}
