const url="/api/enemies";
const baseIcon="/icons/enemies/base.png";
const burrowIcon="/icons/enemies/burrow.png";
const reviveIcon="/icons/enemies/revive.png";
let pending;
export function loadEnemyDatabase() {
  if(!pending)pending=fetch(url).then(async response=>{
    if(!response.ok)throw Error('敵データを読み込めませんでした。');
    const value=await response.json();
    if(value.schemaVersion!==1||!value.enemies?.length)throw Error('敵データの形式を確認できません。');
    return {...value,propertyImages:{base:baseIcon,burrow:burrowIcon,revive:reviveIcon}};
  }).catch(error=>{pending=null;throw error;});
  return pending;
}
