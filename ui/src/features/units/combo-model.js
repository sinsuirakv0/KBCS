import { normalizeUnitQuery } from './model.js';

export const statComboTypes=[['attack',0],['health',1],['speed',2],['research',11],['strong',14],['massive',15],['resistant',16],['knockback',17],['slow',18],['stop',19],['weaken',20],['strengthen',21],['critical',24],['witch-killer',22],['eva-killer',23],['villain',25]];
const typeKeys=new Map(statComboTypes.map(([key,type])=>[type,key]));
export const isStatCombo=combo=>typeKeys.has(combo.type);

export function buildComboTeam(database, selected, forms={}) {
  const team=new Map();
  for(const id of new Set(selected)) {
    const combo=database.combos.find(combo=>combo.id===id&&isStatCombo(combo));
    if(!combo)continue;
    for(const member of combo.members) team.set(member.id,Math.max(team.get(member.id)??0,member.form));
  }
  return [...team].map(([id,minimum])=> {
    const unit=database.units.find(unit=>unit.id===id), maximum=unit.forms.length-1;
    const form=Math.max(minimum,Math.min(maximum,Math.trunc(Number(forms[id])||0)));
    return {id,form,minimum};
  }).sort((a,b)=>a.id-b.id);
}
export function getActiveCombos(database, team) {
  const forms=new Map(team.map(member=>[member.id,member.form]));
  return database.combos.filter(combo=>isStatCombo(combo)&&combo.members.every(member=>forms.has(member.id)&&forms.get(member.id)>=member.form));
}
export function getComboEffects(database, active) {
  const effects=Object.fromEntries(statComboTypes.map(([key])=>[key,0]));
  for(const combo of active) {
    const amount=database.comboEffects[combo.type]?.values[combo.grade];
    if(!Number.isFinite(amount))throw Error('コンボの効果量が未収録です：'+combo.name);
    effects[typeKeys.get(combo.type)]+=amount;
  }
  return effects;
}
export function filterCombos(database, combos, query, type, team, fitOnly) {
  const words=normalizeUnitQuery(query).split(/\s+/).filter(Boolean);
  const known=new Map(database.units.map(unit=>[unit.id,unit]));
  return combos.filter(combo=> {
    if(type!==''&&combo.type!==Number(type))return false;
    const text=normalizeUnitQuery([combo.name,combo.effect,...combo.members.flatMap(member=>[String(member.id),...known.get(member.id).forms.map(form=>form.name)])].join(' '));
    if(!words.every(word=>/^\d+$/.test(word)?combo.members.some(member=>member.id===Number(word)):text.includes(word)))return false;
    return !fitOnly||new Set([...team.map(member=>member.id),...combo.members.map(member=>member.id)]).size<=5;
  });
}
