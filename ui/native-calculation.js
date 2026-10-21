import catalog from './settings-catalog.js';
import {applyUnitTalents} from './talent-effects.js';
import {calculateUnitStats} from './src/shared/game/unit-stats.js';

export async function calculateNative(payload){
  const response=await fetch('/api/calculate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
  const result=await response.json();
  if(!response.ok)throw Error(result.error||'計算できませんでした。');
  if(result.ruleset!==catalog.versionCode)throw Error('この版の計算コアは未対応です。');
  if(result.abi!==2)throw Error('計算コアの版が一致しません。');
  return result;
}

export function createNativeStatistics(unit,growth,gameVersion=catalog.version){
  let key,pending;
  return {prepare(settings,options){
    if(gameVersion!==catalog.version)throw Error('DBとお宝・施設の定義の版が一致しません。');
    const next=JSON.stringify([settings.healthTreasureBonus??settings.healthTreasure/2,settings.attackTreasureBonus??settings.attackTreasure/2,options.talents,options.talentLevels,options.combos?.health||0,options.combos?.attack||0]);
    if(next!==key){
      key=next;
      const inputs=[],rows=new Map();
      for(const form of unit.forms)for(let level=1;level<=Math.min(200,unit.maxLevel+unit.plusLevel||1);level++){
        const improved=applyUnitTalents(unit,form,options.talentLevels,level,options.talents!==false);
        const append=(base,treasure,combo,rates)=>{const index=inputs.length;inputs.push({base,growth:growth[level],treasure:Math.trunc(treasure),combo,talent:rates[0]||0,extra:rates[1]||0});return index;};
        const hp=append(improved.form.hp,settings.healthTreasureBonus??settings.healthTreasure/2,options.combos?.health||0,improved.healthRates);
        const attacks=improved.form.attacks.map(value=>append(value,settings.attackTreasureBonus??settings.attackTreasure/2,options.combos?.attack||0,improved.attackRates));
        rows.set(form.code+':'+level,{hp,attacks});
      }
      pending=calculateNative({stats:inputs}).then(result=>({calculate(currentUnit,form,currentGrowth,currentSettings,currentOptions={}){
        const base=calculateUnitStats(currentUnit,form,currentGrowth,currentSettings);
        const improved=applyUnitTalents(currentUnit,form,currentOptions.talentLevels||{},base.level,currentOptions.talents!==false);
        const stats=calculateUnitStats(currentUnit,improved.form,currentGrowth,currentSettings),row=rows.get(form.code+':'+base.level);
        stats.hp=result.stats[row.hp];stats.attacks=row.attacks.map(index=>result.stats[index]);
        stats.attack=stats.attacks.reduce((sum,value)=>sum+value,0);
        stats.dps=stats.attackCycle>0?stats.attack*30/stats.attackCycle:null;
        return {...improved,stats};
      }})).catch(error=>{if(key===next)key=null;throw error;});
    }
    return pending;
  }};
}
