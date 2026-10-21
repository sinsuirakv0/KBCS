import { calculateUnitStats } from "../../shared/game/unit-stats.js";

export function normalizeUnitQuery(value) {
  return String(value || "").normalize("NFKC").toLowerCase().replace(/[ァ-ヶ]/g, character => String.fromCharCode(character.charCodeAt(0) - 96)).trim();
}

export function selectUnitRows(database, state,calculateProfile) {
  const words = normalizeUnitQuery(state.query).split(/[\s,、]+/).filter(Boolean);
  const ids = words.length && words.every(word => /^\d+$/.test(word)) ? new Set(words.map(Number)) : null;
  const excludes = normalizeUnitQuery(state.exclude).split(/\s+/).filter(Boolean);
  const matchesGroup = (available, selected, mode) => !selected.length || (mode === "all" ? selected.every(key => available.includes(key)) : selected.some(key => available.includes(key)));
  const rows = [];
  for (const unit of database.units) {
    if (!state.spirits && unit.isSpirit) continue;
    if (!state.unnamed && unit.forms.every(form => /^\d+[_-]\d+$/.test(form.name))) continue;
    if (state.rarities.length && !state.rarities.includes(unit.rarity)) continue;
    if (state.talents && !unit.talents.length) continue;
    if(state.kind&&state.kind!=='all'&&unit.kind!==state.kind)continue;
    if(state.talentMode==='normal'&&!unit.talents.length||state.talentMode==='super'&&!unit.talents.some(talent=>talent.limit)||state.talentMode==='none'&&unit.talents.length)continue;
    if(state.minForms&&unit.forms.length<state.minForms)continue;
    const text = normalizeUnitQuery([...unit.aliases, ...unit.forms.map(form => form.name)].join(" "));
    if (ids ? !ids.has(unit.id) : words.some(word => /^\d+$/.test(word) ? Number(word) !== unit.id : !text.includes(word))) continue;
    if (excludes.some(word => text.includes(word))) continue;
    const forms = state.form === "last" ? unit.forms.slice(-1) : state.form === "all" ? unit.forms : unit.forms.filter(form => form.code === state.form);
    for (const original of forms) {
      const profile=(state.applyTalents||state.includeTalents)&&calculateProfile?calculateProfile(unit,original,state):null;
      const form=profile?.form||original;
      if (!matchesGroup(form.targets, state.targets, state.targetMode)) continue;
      if(state.exactTargets&&form.targets.some(key=>!state.targets.includes(key)))continue;
      const available=form.abilities.filter(ability=>(!state.guaranteed||ability.probability==null||ability.probability>=100)&&(!state.fullImmunity||!ability.key.endsWith('-immune')||ability.resistance>=100)).map(ability=>ability.key.endsWith('-immune')&&ability.resistance<100?ability.key.replace(/-immune$/,'-resist'):ability.key);
      // 本能の耐性を探す条件は、表示する数値への本能反映と分ける。
      if(state.includeTalentResistance&&form.index>=2)for(const talent of unit.talents){const resistance=talent.values.at(-1)[0];if(talent.effect.kind==='ability'&&talent.effect.key?.endsWith('-immune')&&resistance>0&&resistance<100)available.push(talent.effect.key.replace(/-immune$/,'-resist'));}
      if(state.abilities.length&&matchesGroup(available,state.abilities,state.abilityMode)===Boolean(state.negateAbilities))continue;
      if (state.attackType && form.attackType !== state.attackType) continue;
      const stats = {...(profile?.stats||calculateUnitStats(unit, form, database.growth[unit.growth], state)),maxLevel:unit.maxLevel+unit.plusLevel,targetCount:form.targets.length};
      if (Object.entries(state.ranges).some(([key, [min, max]]) => ((min !== "" || max !== "") && stats[key] == null) || (min !== "" && stats[key] < Number(min)) || (max !== "" && stats[key] > Number(max)))) continue;
      rows.push({ unit, form, stats, key: unit.id + ":" + form.code });
    }
  }
  const collator = new Intl.Collator("ja", { numeric: true });
  rows.sort((a, b) => {
    const value = row => state.sort === "id" ? row.unit.id : state.sort === "rarity" ? row.unit.rarity : state.sort === "name" ? row.form.name : row.stats[state.sort];
    const left = value(a), right = value(b);
    if (left === null) return right === null ? 0 : 1;
    if (right === null) return -1;
    const order = typeof left === "string" ? collator.compare(left, right) : left - right;
    return order * (state.direction === "desc" ? -1 : 1) || a.unit.id - b.unit.id || a.form.index - b.form.index;
  });
  return rows;
}
