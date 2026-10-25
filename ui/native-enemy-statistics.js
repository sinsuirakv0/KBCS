import {calculateNative} from './native-calculation.js';
import {calculateEnemyStats as presentation,defaultEnemySettings,readEnemySettings as readSettings,writeEnemySettings as writeSettings} from './src/shared/game/enemy-stats.js';
const cache=new Map();
const options=settings=>({...defaultEnemySettings,...settings});
const key=(enemy,settings)=>JSON.stringify([enemy.id,...['health','attack','nativeCrown','alien','starred','god1','god2','god3','strengthen','critical','savage'].map(k=>options(settings)[k])]);
export function stageEnemySettings(spawn,map,crown,settings){return {...settings,health:spawn.health,attack:spawn.attack,nativeCrown:map.stars[crown-1]??100};}
export async function prepareEnemyStatistics(entries){
  const missing=new Map(entries.filter(({enemy,settings})=>enemy&&!cache.has(key(enemy,settings))).map(entry=>[key(entry.enemy,entry.settings),entry]));
  const inputs=[],rows=[];
  for(const [id,{enemy,settings}]of missing){
    const s=options(settings),maximum=enemy.star===1?1500:enemy.star>1?1000:enemy.attributes.includes('alien')?600:0;
    const treasure=maximum===1500?s.starred:enemy.star>1?s['god'+(enemy.star-1)]*10:maximum?s.alien:0;
    const append=(base,rate,castleAttack=0)=>{const index=inputs.length;inputs.push({base,rowPercent:Math.trunc(rate),crownPercent:Math.trunc(s.nativeCrown??100),crystalMax:maximum,crystalTreasure:Math.trunc(treasure),castleAttack});return index;};
    const hp=append(enemy.hp,s.health),attacks=enemy.attacks.map(value=>append(value,s.attack,Number(enemy.attributes.includes('base'))));
    rows.push({id,enemy,s,hp,attacks});
  }
  const values=[];
  for(let offset=0;offset<inputs.length;offset+=4000)values.push(...(await calculateNative({enemyStats:inputs.slice(offset,offset+4000)})).enemyStats);
  const hits=[],targets=[];
  for(const row of rows){
    row.result={hp:values[row.hp].stages[2],attacks:row.attacks.map(index=>values[index].stages[2]),nativeStages:{hp:values[row.hp].stages,attacks:row.attacks.map(index=>values[index].stages)}};
    const strengthen=row.s.strengthen?row.enemy.abilities.find(a=>a.key==='strengthen'):null;
    for(const [index,attack]of row.result.attacks.entries()){
      const savage=row.s.savage&&row.enemy.abilityHits[index]?row.enemy.abilities.find(a=>a.key==='savage'):null;
      const critical=row.s.critical&&row.enemy.abilityHits[index]&&row.enemy.abilities.some(a=>a.key==='critical');
      if(!strengthen&&!savage&&!critical)continue;
      targets.push([row,index]);hits.push({hit:{attack,rawAttack:attack,strengthen:strengthen?strengthen.power-100:0,savage:savage?savage.power-100:0},criticalChance:critical?100:0,savageChance:savage?100:0,forceCritical:!!critical,forceSavage:!!savage});
    }
  }
  for(let offset=0;offset<hits.length;offset+=64){const result=await calculateNative({enemyDamage:hits.slice(offset,offset+64)});for(const [i,value]of result.enemyDamage.entries()){const [row,index]=targets[offset+i];row.result.attacks[index]=value.selected.damage;}}
  if(cache.size>20000)cache.clear();
  for(const row of rows)cache.set(row.id,row.result);
}
export function calculateEnemyStats(enemy,settings=defaultEnemySettings){
  const native=cache.get(key(enemy,settings));if(!native)throw Error('ネイティブの敵ステータスを準備中です。');
  // 元JSは表示用の時間・コスト等だけに使用。HP/攻撃はC++応答以外を採用しない。
  const display=presentation(enemy,{...settings,health:options(settings).health*(settings.nativeCrown??100)/100}),attack=native.attacks.reduce((sum,n)=>sum+n,0);
  return {...display,...native,attack,dps:enemy.attackCycle>0?Math.floor(attack*30/enemy.attackCycle):null};
}

export function readEnemySettings(params,defaults){return {...readSettings(params,defaults),nativeCrown:Math.max(0,Math.min(1000000,Number(params.get('nativeCrown')??defaults?.nativeCrown??100)))};}
export function writeEnemySettings(params,settings){writeSettings(params,settings);if(settings.nativeCrown!=null&&settings.nativeCrown!==100)params.set('nativeCrown',settings.nativeCrown);return params;}
