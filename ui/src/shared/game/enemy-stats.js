import {inheritSimulationSettings} from "../../../simulation-profile.js";
export const defaultEnemySettings={health:100,attack:100,alien:600,starred:1500,god1:100,god2:100,god3:100,seconds:true,strengthen:false,critical:false,savage:false,accountingLevel:30,accountingTreasure:300};
import {accountingMultiplier} from './game-settings.js';
const bounded=(value,fallback,min,max)=>value==null||value===''||!Number.isFinite(Number(value))?fallback:Math.max(min,Math.min(max,Number(value)));
export function readEnemySettings(params,defaults=defaultEnemySettings) {
  const base=Object.fromEntries(Object.entries(defaultEnemySettings).map(([key,fallback])=>[key,params.has('setup')?fallback:defaults[key]??fallback]));
  return inheritSimulationSettings({...base,health:bounded(params.get('health'),base.health,0,1000000),attack:bounded(params.get('attack'),base.attack,0,1000000),alien:bounded(params.get('alien'),base.alien,0,600),starred:bounded(params.get('starred'),base.starred,0,1500),...Object.fromEntries(['god1','god2','god3'].map(key=>[key,bounded(params.get(key),base[key],0,100)])),accountingLevel:Math.trunc(bounded(params.get('accountingLevel'),base.accountingLevel,1,30)),accountingTreasure:Math.trunc(bounded(params.get('accountingTreasure'),base.accountingTreasure,0,300)),seconds:params.has('time')?params.get('time')!=='frames':base.seconds,...Object.fromEntries(['strengthen','critical','savage'].map(key=>[key,params.has(key)?params.get(key)==='true':base[key]]))},defaults);
}
export function writeEnemySettings(params,settings) {
  params.set('setup','1');
  for(const [key,value] of Object.entries(defaultEnemySettings)) {
    if(settings[key]===value)continue;
    if(key==='seconds')params.set('time','frames');else params.set(key,String(settings[key]));
  }
  return params;
}
export function enemyDetailUrl(enemy) {
  return '/pages/tunit-detail/?id='+enemy.id;
}

// ステージ倍率とクリスタル補正を反映し、連続攻撃は一撃ずつ四捨五入する。
export function calculateEnemyStats(enemy,settings=defaultEnemySettings) {
  const options={...defaultEnemySettings,...settings};
  const crystal=enemy.star===1?16-options.starred/100:enemy.star>1?11-options['god'+(enemy.star-1)]/10:enemy.attributes.includes('alien')?7-options.alien/100:1;
  const hp=Math.round(enemy.hp*options.health/100*crystal);
  const strengthen=options.strengthen?enemy.abilities.find(ability=>ability.key==='strengthen'):null;
  const savage=options.savage?enemy.abilities.find(ability=>ability.key==='savage'):null;
  const critical=options.critical&&enemy.abilities.some(ability=>ability.key==='critical');
  const attacks=enemy.attacks.map((value,index)=>{
    let damage=Math.round(value*options.attack/100*crystal);
    if(strengthen)damage+=Math.floor(damage*(strengthen.power-100)/100);
    if(savage&&enemy.abilityHits[index])damage+=Math.floor(damage*(savage.power-100)/100);
    if(critical&&enemy.abilityHits[index])damage*=2;
    return damage;
  });
  const attack=attacks.reduce((total,value)=>total+value,0);
  const shield=enemy.abilities.find(ability=>ability.key==='aku-shield');
  return {hp,attack,attacks,crystal,dps:enemy.attackCycle>0?Math.floor(attack*30/enemy.attackCycle):null,range:enemy.range,speed:enemy.speed,knockbacks:enemy.knockbacks,
    drop:Math.floor(enemy.drop*accountingMultiplier(options)),dropWithoutTreasure:Math.floor(enemy.drop*accountingMultiplier(options,false)),attackCycle:enemy.attackCycle,foreswing:enemy.foreswings[0],backswing:enemy.backswing,
    shield:shield?Math.round(shield.hp*options.health/100*crystal):0,barrier:enemy.abilities.find(ability=>ability.key==='enemy-barrier')?.hp||0};
}
