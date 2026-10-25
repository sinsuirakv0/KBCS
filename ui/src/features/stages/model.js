export const stageGimmicks=[['restriction','出撃制限'],['formation','固定編成'],['ex','連戦・EX'],['specialRule','特殊ルール'],['pointRule','イベントPt'],['levelSeal','Lv封印'],['noContinue','コンテ不可'],['bossGuard','城バリア'],['timeLimit','時間制限'],['splitMultiplier','体力・攻撃の倍率差'],['kills','味方の撃破数条件'],['afterCastle','城連動後の待機'],['enemyCastle','敵キャラの城'],['musicChange','BGM切替'],['animatedBackground','背景が動く'],['abyss','アビス'],['randomPattern','抽選ステージ'],['missing','敵データ未収録'],['unlisted','一覧外']];
export const stageRanges=[['energy','統率力'],['difficulty','難易度'],['width','ステージ幅']];
export function normalizeStageQuery(value){return String(value).normalize('NFKC').toLowerCase().replace(/[ァ-ヶ]/g,char=>String.fromCharCode(char.charCodeAt(0)-0x60)).trim();}
export const queryTerms=value=>normalizeStageQuery(value).split(/[\s,、]+/).filter(Boolean);
export function selectStageSeries(database){
  const firstId=series=>Math.min(...database.maps.filter(map=>map.series===series.id).map(map=>map.nativeId));
  return [...database.series].sort((a,b)=>firstId(a)-firstId(b));
}
export function selectStageRewards(database,kind='',query=''){
  const terms=queryTerms(query);
  return Object.values(database.rewards).filter(item=>(!kind||(kind==='unit'?item.unit!=null&&!item.evolution:kind==='evolution'?item.evolution:item.unit==null))&&terms.every(term=>normalizeStageQuery(item.name+' '+item.id+(item.unit!=null?' '+item.unit:'')).includes(term))).sort((a,b)=>a.id-b.id);
}
const matches=(selected,values,all)=>!selected.length||(all?selected.every(value=>values.includes(value)):selected.some(value=>values.includes(value)));
export function stageMapUrl(map,crown=1){return '/pages/stage-detail/?'+new URLSearchParams({map:typeof map==='string'?map:map.key,...(crown>1?{crown:String(crown)}:{})});}
export function stageDetailUrl(stage,crown=1){const url=new URL(stageMapUrl(stage.map||stage.id.replace(/-\d+$/,''),crown),'https://kbc.invalid');url.searchParams.set('stage',stage.index??Number(stage.id.match(/-(\d+)$/)?.[1]));return url.pathname+url.search;}
export function resolveStageRoute(database,params){
  const legacy=database.stages.find(stage=>stage.id===params.get('id'));
  const key=params.get('map')||legacy?.map||(!params.has('id')?'N000':null),map=database.maps.find(map=>map.key===key);
  if(!map)throw Error('マップIDが見つかりません。');
  const choice=params.get('stage');
  const selected=choice==null||choice===''||choice==='all'?null:database.stages.find(stage=>stage.map===map.key&&String(stage.index)===choice);
  if(choice&&choice!=='all'&&!selected)throw Error('このマップのステージが見つかりません。');
  return {map,selected:selected?.id||'',legacy:legacy?.id||null};
}

export function selectStageRows(database,enemyDatabase,state){
  const maps=new Map(database.maps.map(map=>[map.key,map])),enemies=new Map(enemyDatabase.enemies.map(enemy=>[enemy.id,enemy]));
  const terms=queryTerms(state.query),enemyTerms=queryTerms(state.enemy),rewardTerms=queryTerms(state.reward),numbers=value=>queryTerms(value).map(Number).filter(Number.isFinite);
  const background=numbers(state.background),music=numbers(state.music),series=new Map(database.series.map(series=>[series.id,series.label]));
  const rows=database.stages.filter(stage=>{
    const map=maps.get(stage.map);
    if(state.series&&state.series!==map.series)return false;
    if(state.crown>map.stars.length)return false;
    const name=normalizeStageQuery([stage.name,map.name,stage.id,map.key,series.get(map.series)].join(' '));
    if(!terms.every(term=>/^\d+$/.test(term)?map.nativeId===Number(term):/^\d+-\d+$/.test(term)?map.nativeId===Number(term.split('-')[0])&&stage.index===Number(term.split('-')[1]):name.includes(term.replace('_','-'))))return false;
    if(!matches(state.gimmicks,stage.flags,true))return false;
    if(state.excludeEnemies&&enemyTerms.length&&(stage.patterns||[stage]).some(pattern=>{
      const found=enemyTerms.map(term=>pattern.enemies.some(id=>/^\d+$/.test(term)?id===Number(term):normalizeStageQuery((enemies.get(id)?.name||'')+' '+(enemies.get(id)?.aliases||[]).join(' ')).includes(term)));
      return state.enemyMode==='any'?found.some(Boolean):found.every(Boolean);
    }))return false;
    if(!((stage.patterns||[stage]).some(pattern=>{
    const present=pattern.enemies.map(id=>enemies.get(id)).filter(Boolean);
    if(enemyTerms.length&&!state.excludeEnemies){
      const found=enemyTerms.map(term=>present.some(enemy=>/^\d+$/.test(term)?enemy.id===Number(term):normalizeStageQuery(enemy.name+' '+(enemy.aliases||[]).join(' ')).includes(term)));
      const matched=state.enemyMode==='any'?found.some(Boolean):found.every(Boolean);
      if(!matched)return false;
    }
    const attributes=[...new Set(present.flatMap(enemy=>[...enemy.attributes,...enemy.species]))];
    if(!matches(state.attributes,attributes,state.attributeMode==='all'))return false;
    if(state.attributesOnly&&state.attributes.length&&attributes.some(key=>!state.attributes.includes(key)))return false;
    const flags=state.crown?[...pattern.flags.filter(flag=>flag!=='restriction'),...(applicableLimits(map,stage,state.crown).length?['restriction']:[])]:pattern.flags;
    if(!matches(state.gimmicks,flags,true))return false;
    if(background.length&&!background.includes(pattern.background))return false;
    const width=state.ranges.width||[];if(width.some((value,index)=>value!==''&&value!=null&&(pattern.width==null||(index===0?pattern.width<Number(value):pattern.width>Number(value)))))return false;
    return true;
    })))return false;
    if(rewardTerms.length&&!rewardTerms.every(term=>stage.rewards.some(id=>/^\d+$/.test(term)?id===Number(term):normalizeStageQuery(database.rewards[id]?.name||'').includes(term))))return false;
    if(music.length&&!stage.music.some(id=>music.includes(id)))return false;
    for(const [key]of stageRanges.filter(([key])=>key!=='width'))for(const [index,value]of (state.ranges[key]||[]).entries())if(value!==''&&value!=null&&(stage[key]==null||(index===0?stage[key]<Number(value):stage[key]>Number(value))))return false;
    return true;
  }).map(stage=>{const map=maps.get(stage.map);return {stage:state.crown?{...stage,flags:[...stage.flags.filter(flag=>flag!=='restriction'),...(applicableLimits(map,stage,state.crown).length?['restriction']:[])]}:stage,map};});
  if(state.sort==='id')return state.direction==='desc'?rows.reverse():rows;
  const direction=state.direction==='desc'?-1:1;
  return rows.sort((a,b)=>{
    const x=state.sort==='name'?a.stage.name:state.sort==='map'?a.map.name:a.stage[state.sort];
    const y=state.sort==='name'?b.stage.name:state.sort==='map'?b.map.name:b.stage[state.sort];
    return x==null?(y==null?0:1):y==null?-1:direction*(typeof x==='string'?x.localeCompare(y,'ja'):x-y);
  });
}

export function applicableLimits(map,stage,crown){return map.limits.filter(limit=>(limit.crown<0||limit.crown===crown-1)&&(limit.stage<0||limit.stage===stage.index));}
export function effectiveSpawn(spawn,map,crown=1){const factor=(map.stars[crown-1]??map.stars[0]??100)/100,scale=value=>Math.round(value*factor*1e6)/1e6;return {...spawn,health:scale(spawn.health),attack:scale(spawn.attack)};}

// ステージ単位で条件を判定してからマップへまとめ、別ステージを跨ぐAND一致を防ぐ。
export function selectStageMaps(database,enemyDatabase,state){
  const groups=new Map();
  for(const {stage,map}of selectStageRows(database,enemyDatabase,{...state,sort:'id',direction:'asc'})){
    if(!groups.has(map.key))groups.set(map.key,{map,stages:[]});groups.get(map.key).stages.push(stage);
  }
  const rows=[...groups.values()].map(entry=>{
    const range=key=>{const values=entry.stages.map(stage=>stage[key]).filter(Number.isFinite);return values.length?[Math.min(...values),Math.max(...values)]:[];};
    return {...entry,enemies:[...new Set(entry.stages.flatMap(stage=>stage.enemies))],flags:[...new Set(entry.stages.flatMap(stage=>stage.flags))],energy:range('energy'),difficulty:range('difficulty'),width:range('width')};
  });
  const direction=state.direction==='desc'?-1:1;
  return rows.sort((a,b)=>{
    const value=entry=>state.sort==='id'?entry.map.nativeId:['name','map'].includes(state.sort)?entry.map.name:state.sort==='count'?entry.map.stages.length:entry[state.sort]?.[0];
    const x=value(a),y=value(b);return x==null?(y==null?0:1):y==null?-1:direction*(typeof x==='string'?x.localeCompare(y,'ja'):x-y);
  });
}

export function stagePlayUrl(stage,crown=1){
  const url=new URL(stageDetailUrl(stage,crown),'https://kbc.invalid');url.pathname='/pages/stage-play/';
  if(stage.patternId)url.searchParams.set('pattern',stage.patternId);
  return url.pathname+url.search;
}
