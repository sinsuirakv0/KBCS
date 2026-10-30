import {createNativeStatistics} from './native-calculation.js';
import {resolveFormationMember} from './formation-model.js';
import {deriveSimulationSettings} from './simulation-profile.js';
import {readUnitSettings} from './src/shared/game/unit-stats.js';
import {unitSheetHtml} from './src/features/units/sheet.js';

export function createFormationDetails(database){
 const units=new Map(database.units.map(unit=>[unit.id,unit]));
 let revision=0,currentUnit,statistics;
 return async(host,member,profile,cost)=>{
  const current=++revision;if(!host||!member)return;
  const unit=units.get(member.unitId);if(!unit)return;
  const effective=resolveFormationMember(unit,member),form=unit.forms.find(form=>form.index===effective.form);
  const settings={...readUnitSettings(new URLSearchParams(),deriveSimulationSettings(profile)),level:effective.level+effective.plus};
  const options={talents:true,talentLevels:effective.talents};
  if(currentUnit!==unit){currentUnit=unit;statistics=createNativeStatistics(unit,database.growth[unit.growth],database.calculationVersion??database.gameVersion);}
  try{
   const prepared=await statistics.prepare(settings,options);if(current!==revision||!host.isConnected)return;
   const result=prepared.calculate(unit,form,database.growth[unit.growth],settings,options);
   result.stats.cost=cost??null;
   host.innerHTML=unitSheetHtml(database,unit,result,settings);
  }catch(error){if(current===revision&&host.isConnected)host.textContent=error.message;}
 };
}
