import {calculateTalentStats} from './talents.js';
import {calculateUnitStats} from './src/shared/game/unit-stats.js';
import {calculateNative} from './native-calculation.js';
import {applyUnitTalents} from './talent-effects.js';
let savedKey,pending;
export function prepareUnitSearch(database,settings){
  const key=JSON.stringify([settings.level,settings.healthTreasureBonus??settings.healthTreasure/2,settings.attackTreasureBonus??settings.attackTreasure/2,settings.applyTalents]);
  if(key===savedKey)return pending;savedKey=key;
  pending=(async()=>{
    const inputs=[],rows=new Map();
    for(const unit of database.units){const level=Math.max(1,Math.min(200,unit.maxLevel+unit.plusLevel||1,Math.trunc(settings.level)||1)),levels=Object.fromEntries(unit.talents.map(t=>[t.index,t.maxLevel]));
      for(const form of unit.forms){const improved=applyUnitTalents(unit,form,levels,level,!!settings.applyTalents);
        const append=(base,treasure,rates)=>{const index=inputs.length;inputs.push({base,growth:database.growth[unit.growth][level],treasure:Math.trunc(treasure),combo:0,talent:rates[0]||0,extra:rates[1]||0});return index;};
        rows.set(unit.id+':'+form.code,{hp:append(improved.form.hp,settings.healthTreasureBonus??settings.healthTreasure/2,improved.healthRates),attacks:improved.form.attacks.map(v=>append(v,settings.attackTreasureBonus??settings.attackTreasure/2,improved.attackRates))});
      }
    }
    const values=[];for(let offset=0;offset<inputs.length;offset+=4000)values.push(...(await calculateNative({stats:inputs.slice(offset,offset+4000)})).stats);
    return new Map([...rows].map(([id,row])=>[id,{hp:values[row.hp],attacks:row.attacks.map(i=>values[i])}]));
  })().catch(error=>{if(savedKey===key)savedKey=null;throw error;});return pending;
}

export function unitSearchProfile(database,unit,form,settings,nativeProfiles) {
  const levels=Object.fromEntries(unit.talents.map(talent=>[talent.index,talent.maxLevel]));
  const profile=settings.applyTalents?calculateTalentStats(unit,form,database.growth[unit.growth],settings,{talents:true,talentLevels:levels},calculateUnitStats):{form,stats:calculateUnitStats(unit,form,database.growth[unit.growth],settings)};
  const native=nativeProfiles.get(unit.id+':'+form.code);if(!native)throw Error('ネイティブのキャラステータスを準備中です。');profile.stats={...profile.stats,...native,attack:native.attacks.reduce((a,b)=>a+b,0)};profile.stats.dps=profile.stats.attackCycle>0?profile.stats.attack*30/profile.stats.attackCycle:null;
  if(!settings.includeTalents)return profile;
  const potential=applyUnitTalents(unit,form,levels,60,true).form;
  // 検索用の属性・特性だけ補い、表示ステータスと詳細へ渡す本能ON/OFFは変えない。
  return {...profile,form:{...profile.form,targets:potential.targets,abilities:potential.abilities}};
}
