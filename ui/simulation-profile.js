import catalog from './settings-catalog.js';
export {catalog};
const bounded=(value,min,max,fallback)=>value==null||value===''||!Number.isFinite(Number(value))?fallback:Math.max(min,Math.min(max,Math.trunc(Number(value))));
const id=(campaign,chapter,group)=>campaign+'-'+chapter+'-'+group;

export function normalizeSimulationProfile(value={}){
  return {schemaVersion:1,catalogVersion:catalog.version,
    cannon:Object.fromEntries(['base','decoration'].map(part=>[part,{id:bounded(value.cannon?.[part]?.id,0,7,0),level:bounded(value.cannon?.[part]?.level,0,20,20)}])),
    treasures:Object.fromEntries(catalog.treasures.map(item=>[item.id,bounded(value.treasures?.[item.id],0,100,100)])),
    facilities:Object.fromEntries(catalog.facilities.map(item=>[item.id,{level:bounded(value.facilities?.[item.id]?.level,1,item.maxLevel,item.maxLevel),plus:bounded(value.facilities?.[item.id]?.plus,0,item.maxPlus,item.maxPlus)}]))};
}

export function migrateSimulationProfile(legacy={}){
  const profile=normalizeSimulationProfile({cannon:{base:{id:legacy.cannonBase,level:legacy.cannonBaseLevel},decoration:{id:legacy.cannonDecoration,level:legacy.cannonDecorationLevel}}});
  // 旧合計値は1章から順に配分し、合計と既存の最大設定を保つ。
  const distribute=(campaign,groups,total)=>{
    let remaining=bounded(total,0,groups.length*300,groups.length*300);
    for(let chapter=1;chapter<=3;chapter++)for(const group of groups){const value=Math.min(100,remaining);profile.treasures[id(campaign,chapter,group)]=value;remaining-=value;}
  };
  for(const [key,group] of [['healthTreasure',6],['attackTreasure',7],['researchTreasure',2],['accountingTreasure',5]])distribute(0,[group],legacy[key]);
  for(const group of [5,6,7,8])distribute(1,[group],legacy.fruit);
  for(const group of [5,6,7])distribute(2,[group],legacy.fruit);
  distribute(1,[0,1],legacy.alien);distribute(2,[0,1,2,3,4],legacy.starred);
  for(let chapter=1;chapter<=3;chapter++){
    for(const [key,campaign,group] of [['studyJapan',0,3],['studySpace',2,9],['god',2,10]])profile.treasures[id(campaign,chapter,group)]=bounded(legacy[key+chapter],0,100,100);
  }
  for(const key of ['research','accounting','study'])if(legacy[key+'Level']!=null){const level=bounded(legacy[key+'Level'],1,30,30);profile.facilities[key]={level:Math.min(20,level),plus:Math.max(0,level-20)};}
  return profile;
}

export function deriveSimulationSettings(value){
  const profile=normalizeSimulationProfile(value);
  const percent=(campaign,group)=>[1,2,3].reduce((total,chapter)=>total+profile.treasures[id(campaign,chapter,group)],0);
  // 章別に原本の最大加算値を掛けて整数化してから合算する。
  const effect=(campaign,group)=>catalog.treasures.filter(item=>item.campaign===campaign&&item.group===group).reduce((total,item)=>total+Math.floor(item.maximumEffect*profile.treasures[item.id]/100),0);
  const facility=key=>profile.facilities[key].level+profile.facilities[key].plus;
  return {profileActive:true,cannonBase:profile.cannon.base.id,cannonBaseLevel:profile.cannon.base.level,cannonDecoration:profile.cannon.decoration.id,cannonDecorationLevel:profile.cannon.decoration.level,healthTreasure:percent(0,6),attackTreasure:percent(0,7),healthTreasureBonus:effect(0,6),attackTreasureBonus:effect(0,7),
    fruitByTarget:{red:percent(1,6),floating:percent(1,7),black:percent(1,5),angel:percent(1,8),metal:percent(2,5),zombie:percent(2,6),alien:percent(2,7)},
    researchLevel:facility('research'),researchTreasure:percent(0,2),researchReductionOverride:(facility('research')-1)*6+effect(0,2),
    accountingLevel:facility('accounting'),accountingTreasure:percent(0,5),accountingTreasureBonus:effect(0,5)/100,studyLevel:facility('study'),studyTreasureBonus:effect(0,3)+effect(2,9),
    alien:percent(1,0)+percent(1,1),starred:[0,1,2,3,4].reduce((total,group)=>total+percent(2,group),0),
    ...Object.fromEntries([1,2,3].flatMap(chapter=>[['studyJapan'+chapter,profile.treasures[id(0,chapter,3)]],['studySpace'+chapter,profile.treasures[id(2,chapter,9)]],['god'+chapter,profile.treasures[id(2,chapter,10)]]]))};
}

export const profileSettingKeys=Object.keys(deriveSimulationSettings(normalizeSimulationProfile()));
export function inheritSimulationSettings(target,defaults){
  if(defaults.profileActive)for(const key of profileSettingKeys)if(defaults[key]!=null)target[key]=defaults[key];
  return target;
}
