import {calculateUnitStats} from './src/shared/game/unit-stats.js';
import {applyUnitTalents} from './talent-effects.js';
export {applyUnitTalents};

// 表示ステータスに必要な成長・お宝・本能だけを適用する。
export function calculateTalentStats(unit,original,growth,settings,options={},calculateBase=calculateUnitStats){
  const base=calculateBase(unit,original,growth,settings);
  const improved=applyUnitTalents(unit,original,options.talentLevels||{},base.level,options.talents!==false);
  const stats=calculateBase(unit,improved.form,growth,settings);
  const percent=(value,rate)=>Math.floor(value*(100+rate)/100+1e-9);
  stats.hp=improved.healthRates.reduce(percent,stats.hp);
  stats.attacks=stats.attacks.map(value=>improved.attackRates.reduce(percent,value));
  stats.attack=stats.attacks.reduce((total,value)=>total+value,0);
  stats.dps=stats.attackCycle>0?stats.attack*30/stats.attackCycle:null;
  return {...improved,stats};
}
