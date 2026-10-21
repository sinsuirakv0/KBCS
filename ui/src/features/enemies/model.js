import {calculateEnemyStats} from '../../shared/game/enemy-stats.js';
export const rangeFields=[['hp','体力'],['attack','攻撃力'],['dps','DPS'],['range','射程'],['speed','速度'],['knockbacks','KB'],['drop','お金'],['attackCycle','攻撃頻度F'],['foreswing','攻撃発生F']];
const normalize=value=>String(value).normalize('NFKC').toLocaleLowerCase('ja').replace(/\s+/g,' ').trim();
export function matchesEnemyQuery(enemy,query) {
  const text=normalize(query??'');if(!text)return true;
  if(/^\d+(?:\s*[-,、]\s*\d+)*$/.test(text))return text.split(/[,、]/).some(token=>{
    const [start,end=start]=token.split('-').map(Number);return enemy.id>=Math.min(start,end)&&enemy.id<=Math.max(start,end);
  });
  const name=normalize(enemy.name+(enemy.attributes.includes('base')?' 敵城':''));
  return text.split(' ').every(word=>name.includes(word)||String(enemy.id)===word);
}
function matchesKeys(values,selected=[],mode='all'){return !selected.length||(mode==='any'?selected.some(key=>values.includes(key)):selected.every(key=>values.includes(key)));}
export function selectEnemyRows(database,state) {
  return database.enemies.filter(enemy=> {
    if(!matchesEnemyQuery(enemy,state.query))return false;
    if(!matchesKeys([...enemy.attributes,...enemy.species],state.attributes,state.attributeMode))return false;
    if(state.attackType&&enemy.attackType!==state.attackType)return false;
    const abilityMatch=matchesKeys(enemy.abilities.map(ability=>ability.key),state.abilities,state.abilityMode);
    return !state.abilities?.length||(state.negate?!abilityMatch:abilityMatch);
  }).map(enemy=>({enemy,stats:calculateEnemyStats(enemy,state)})).filter(({stats})=>rangeFields.every(([key])=>{
    const [min='',max='']=state.ranges?.[key]||[];
    return (min===''||stats[key]!=null&&stats[key]>=Number(min))&&(max===''||stats[key]!=null&&stats[key]<=Number(max));
  })).sort((left,right)=>{
    const key=state.sort||'id';
    const a=key==='name'?left.enemy.name:key==='id'?left.enemy.id:left.stats[key];
    const b=key==='name'?right.enemy.name:key==='id'?right.enemy.id:right.stats[key];
    if(a==null||b==null)return a==null?(b==null?0:1):-1;
    const order=typeof a==='string'?a.localeCompare(b,'ja'):a-b;
    return (state.direction==='desc'?-order:order)||left.enemy.id-right.enemy.id;
  });
}
