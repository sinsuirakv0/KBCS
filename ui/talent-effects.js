// 本能適用と戦闘補正を分け、整数化する段階を一か所で管理する。
const integer = value => Math.floor(value + 1e-9);
const percent = (value, rate) => integer(value * (100 + rate) / 100);
const clamp = (value, min, max) => Math.max(min, Math.min(max, Number(value) || 0));

export function applyUnitTalents(unit, original, levels, level, enabled = true) {
  const form = structuredClone(original);
  const healthRates=[],attackRates=[];
  const applied = [], locked = [];
  for (const talent of unit.talents) {
    const selected = enabled ? clamp(levels[talent.index], 0, talent.maxLevel) : 0;
    if (form.index >= 2 && talent.effect.kind === 'target') form.targets = form.targets.filter(key => key !== talent.effect.key);
    if (!selected) continue;
    if (form.index < 2 || (talent.limit && level < 60)) { locked.push(talent.name); continue; }
    const values = talent.values[Math.trunc(selected)-1];
    if (!values) continue;
    applied.push(talent.index);
    for (const key of talent.targets) if (!form.targets.includes(key)) form.targets.push(key);
    const effect = talent.effect;
    if (effect.kind === 'target') { if (!form.targets.includes(effect.key)) form.targets.push(effect.key); continue; }
    if (effect.kind === 'stat') {
      const value = values[0];
      if (effect.key === 'healthPercent') healthRates.push({id:talent.id,value});
      else if (effect.key === 'attackPercent') attackRates.push({id:talent.id,value});
      else if (effect.key === 'cost' || effect.key === 'respawn') form[effect.key] = Math.max(0, form[effect.key] - value);
      else if (effect.key === 'intervalPercent') form.attackInterval = integer(form.attackInterval * (100 - value) / 100);
      else if (effect.key === 'alternateRespawnPercent') form.abilities.push({key:'alternate-respawn',label:'2回生産ごと再生産短縮',percent:value});
      else form[effect.key] += value;
      continue;
    }
    if (effect.kind !== 'ability') continue;
    let ability = form.abilities.find(value => value.key === effect.key);
    if (!ability) { ability = {key:effect.key,label:effect.label}; form.abilities.push(ability); }
    for (const [index, field] of effect.fields.entries()) {
      const value = values[index];
      if (field === 'immune') { ability.resistance = 100; ability.label = effect.label; }
      else if (field === 'resistance') { ability.resistance = Math.min(100,(ability.resistance || 0)+value); ability.label = ability.resistance===100 ? effect.label.replace('耐性','無効') : effect.label; }
      else if (field === 'healthReduction') { if (value>0) ability.health = 100 - ((ability.health || 0)+value); }
      else if (field === 'strengthenPercent' || field === 'savagePercent') ability.power = (ability.power || 100) + value;
      else if (field === 'weakenPercent') ability.percent = (ability.percent ?? 100) - value;
      else if (field === 'surgeStart') ability.range = [value/4,value/4];
      else if (field === 'surgeWidth') ability.range[1] += value/4;
      else if (field === 'blastStart') ability.range = [value/4,value/4];
      else if (field === 'blastWidth') ability.range[1] += value/4;
      else if (field === 'miniPercent') ability.percent = value || 20;
      else ability[field] = (ability[field] || 0) + value;
    }
    if (ability.probability != null) ability.probability = Math.min(100,ability.probability);
  }
  if (form.attackCycle != null) form.attackCycle = Math.max(Math.max(...form.foreswings)+form.attackInterval*2-1,Math.max(...form.foreswings)+form.backswing);
  return {form,healthRates:healthRates.sort((a,b)=>a.id-b.id).map(entry=>entry.value),attackRates:attackRates.sort((a,b)=>a.id-b.id).map(entry=>entry.value),applied,locked};
}

