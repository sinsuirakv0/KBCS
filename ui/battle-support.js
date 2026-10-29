import {catalog,normalizeSimulationProfile} from './simulation-profile.js';
import {resolveFormationMember} from './formation-model.js';

export const battleItems=[{id:0,key:'speedup',name:'スピードアップ'},{id:1,key:'radar',name:'トレジャーレーダー'},{id:2,key:'rich',name:'ネコボン'},{id:3,key:'computer',name:'ニャンピュータ'},{id:4,key:'okame',name:'おかめはちもく'},{id:5,key:'sniper',name:'スニャイパー'}];
export async function readBattleJson(path,options){
  const response=await fetch(path,options),value=await response.json();
  if(!response.ok)throw Error(value.error||'読み込みに失敗しました');return value;
}
export function battleFormation(database,document){
  const known=new Map(database.units.map(unit=>[unit.id,unit]));
  return {...structuredClone(document),gameVersion:database.gameVersion,slots:document.slots.map(member=>{
    if(!member)return null;const unit=known.get(member.unitId);if(!unit)throw Error('キャラID '+member.unitId+' が現在のDBにありません');
    const effective=resolveFormationMember(unit,member);if(!unit.forms.some(form=>form.index===effective.form))throw Error('キャラの形態が未収録です');return structuredClone(effective);
  }),profile:normalizeSimulationProfile(document.profile)};
}
export function castleHealthInput(database,document){
  if((database.calculationVersion??database.gameVersion)!==catalog.version)throw Error('城体力計算とDBの対応版が異なります');
  const profile=normalizeSimulationProfile(document.profile),facility=profile.facilities.castle;
  const treasureBonus=catalog.treasures.filter(item=>item.effectType===0&&!item.effectFlag).reduce((sum,item)=>sum+Math.trunc(item.maximumEffect*profile.treasures[item.id]/100),0);
  const team=new Map(document.slots.slice(0,5).filter(Boolean).map(member=>[member.unitId,member.form]));
  const comboPercent=database.combos.filter(combo=>combo.type===10&&combo.members.every(member=>team.has(member.id)&&team.get(member.id)>=member.form)).reduce((sum,combo)=>sum+database.comboEffects[10].values[combo.grade],0);
  return {facilityLevel:facility.level+facility.plus,developmentLevel:document.cannon.developmentLevel??30,treasureBonus,comboPercent};
}
export async function castleHealth(database,document){
  return readBattleJson('/api/battle-support',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(castleHealthInput(database,document))});
}

// 暗転中に、選択したステージと編成の原本画像を重複なくデコードする。
export async function prepareBattleAssets(stage,formation,scene,report,signal){
  const actors=[...new Set([...(stage.enemies||[]),...stage.spawns.map(spawn=>spawn.enemy),stage.enemyCastle].filter(id=>Number.isInteger(id)&&id>=0))].map(id=>({kind:'enemy',id}));
  actors.push(...formation.slots.filter(Boolean).map(member=>({kind:'unit',id:member.unitId,form:member.form})));
  const manifests=[];let completed=0;
  async function workers(values,run){let index=0;await Promise.all(Array.from({length:Math.min(4,values.length)},async()=>{while(index<values.length){signal.throwIfAborted();const value=values[index++];await run(value);}}));}
  await workers(actors,async actor=>{manifests.push(await readBattleJson('/api/motion?'+new URLSearchParams(actor),{signal}));report('キャラ素材',++completed,actors.length);});
  const paths=new Set(scene.textures.filter(Boolean));
  for(const manifest of manifests)for(const resource of [manifest.body,manifest.soul])if(resource?.image)paths.add(resource.image);
  const images=new Map();completed=0;
  await workers([...paths],async path=>{const image=new Image();image.src='/api/asset/'+path;try{await image.decode();}catch{throw Error('画像を読み込めません：'+path);}signal.throwIfAborted();images.set(path,image);report('画像',++completed,paths.size);});
  return {manifests,images};
}

// 009e4474は対象の冠・面へ展開して後の行で上書きする。
export function effectiveStageLimit(map,stage,crown){
  return map.limits.filter(limit=>(limit.crown<0||limit.crown===crown-1)&&(limit.stage<0||limit.stage===stage.index)).at(-1)||{};
}
export function deploymentReason(bits){return [[1,'レア度制限'],[2,'編成1ページ目のみ'],[4,'生産コスト制限'],[8,'キャラ指定制限'],[16,'レア度別の編成数制限']].filter(([mask])=>bits&mask).map(([,text])=>text).join('・');}
export async function stageDeployment(database,map,stage,crown,document){
  const limit=effectiveStageLimit(map,stage,crown),known=new Map(database.units.map(unit=>[unit.id,unit])),rules=new Map((map.rules||[]).map(rule=>[rule.id,rule.parameters]));
  const costs=document.slots.map(member=>{
    if(!member)return {raw:0,reduction:0,chapter:1,multiplier:0,fixed:-1,rarity_rate:100};
    const unit=known.get(member.unitId),form=unit.forms.find(form=>form.index===member.form);
    const reduction=form.index<2?0:unit.talents.filter(talent=>talent.effect.key==='cost').reduce((sum,talent)=>sum+(talent.values[(member.talents[talent.index]||0)-1]?.[0]||0),0);
    return {raw:form.cost,reduction,chapter:['EOC','EOCZ'].includes(map.series)?map.number:1,multiplier:0,fixed:rules.get(4)?.[0]??-1,rarity_rate:rules.get(5)?.[unit.rarity]??100};
  });
  const checks=[],positions=[],counts=Array(6).fill(0);
  for(const [slot,member]of document.slots.entries()){
    if(!member)continue;const unit=known.get(member.unitId),group=limit.group;
    const check={rarity:unit.rarity,slot,cost:0,mask:limit.rarities||0,slots:limit.slots||0,minimum:limit.minCost||0,maximum:limit.maxCost||0,group_type:group?.type??-1,in_group:Number(group?.units.includes(member.unitId)||false),phase:1,rarity_limit:rules.get(2)?.[unit.rarity]??-1,preceding:counts[unit.rarity]++};
    positions.push(slot);checks.push(check,{...check,phase:0});
  }
  const value=await readBattleJson('/api/deployment',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({costs,checks})});
  const result=document.slots.map(()=>({reasons:0,formationReasons:0,cost:0}));
  for(const [index,slot]of positions.entries())result[slot]={reasons:value.checks[index*2]|value.checks[index*2+1],formationReasons:value.checks[index*2],cost:value.costs[slot]};
  return {slots:result,maxUnits:limit.maxUnits||0,limit};
}
export async function formationStageContext(params){
  if(!params.has('map'))return null;
  const detail=await readBattleJson('/api/stages?'+new URLSearchParams({map:params.get('map')})),map=detail.maps.find(map=>map.key===params.get('map')),stage=detail.stages.find(stage=>stage.index===(Number(params.get('stage'))||0));
  if(!map||!stage)throw Error('出撃準備のステージが見つかりません');
  return {map,stage,crown:Math.max(1,Math.min(map.stars.length,Number(params.get('crown'))||1)),buildId:detail.buildId};
}
