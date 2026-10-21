import {inheritSimulationSettings} from "../../../simulation-profile.js";
export const rarityNames = ["基本", "EX", "レア", "激レア", "超激レア", "伝説レア"];
export const formCodes = ["f", "c", "s", "u"];

import {researchSettings,researchReduction,cannonSettings,cannonSettingKeys} from './game-settings.js';
export const defaultUnitSettings = { level: 30, healthTreasure: 300, attackTreasure: 300, fruit:300,chapter: 2, research: "max", researchLevel:30,researchTreasure:300,seconds: true,...cannonSettings({}) };

export function getTalentRequiredLevel(unit,levels) {
  return unit.talents.some(talent=>talent.limit&&Number(levels[talent.index])>0)?60:0;
}

export function calculateUnitStats(unit, form, growth, settings = defaultUnitSettings) {
  const level = Math.max(1, Math.min(200, unit.maxLevel + unit.plusLevel || 1, Math.trunc(Number(settings.level) || 1)));
  // ネイティブの成長値の四捨五入を先に行い、お宝の段階で切り捨てる。
  const scale = (base, treasure, bonus=Number(treasure)/2) => {const grown=Math.floor((base*growth[level]+50)/100);return grown+Math.floor(grown*bonus/100);};
  const attacks = form.attacks.map(value => scale(value, settings.attackTreasure,settings.attackTreasureBonus));
  const attack = attacks.reduce((total, value) => total + value, 0);
  const reduction=researchReduction(settings);
  return {
    level, hp: scale(form.hp, settings.healthTreasure,settings.healthTreasureBonus), attack, attacks,
    dps: form.attackCycle > 0 ? attack * 30 / form.attackCycle : null,
    cost: unit.isSpirit ? null : Math.floor(form.cost * [1, 1, 1.5, 2][Number(settings.chapter)]),
    respawn: unit.isSpirit ? null : Math.trunc(Math.max(60, form.respawn - reduction)),researchReduction:reduction,
    range: form.range, speed: form.speed, knockbacks: form.knockbacks, attackCycle: form.attackCycle,
    foreswing: form.foreswings[0], backswing: form.backswing,
  };
}

export function unitDetailUrl(unit,form) {
  return "/pages/unit-detail/?"+new URLSearchParams({id:String(unit.id),form:form.code});
}

export function readUnitSettings(params,defaults=defaultUnitSettings) {
  const value = Object.fromEntries(Object.entries(defaultUnitSettings).map(([key,fallback])=>[key,params.has('setup')?fallback:defaults[key]??fallback]));
  if(params.has('research'))Object.assign(value,params.get('research')==='none'?{researchLevel:1,researchTreasure:0}:{researchLevel:30,researchTreasure:300});
  for (const [key, max] of [["level", 200], ["healthTreasure", 300], ["attackTreasure", 300], ["fruit",300],["chapter", 3]]) {
    if (params.has(key)) value[key] = Math.max(key === "level" || key === "chapter" ? 1 : 0, Math.min(max, Number(params.get(key)) || 0));
  }
  for(const [key,min,max] of [['researchLevel',1,30],['researchTreasure',0,300]])if(params.has(key))value[key]=Math.max(min,Math.min(max,Math.trunc(Number(params.get(key))||min)));
  Object.assign(value,researchSettings({...value,research:'custom'}),cannonSettings({...value,...Object.fromEntries(cannonSettingKeys.filter(key=>params.has(key)).map(key=>[key,params.get(key)]))}));
  if(params.has('seconds'))value.seconds=params.get('seconds')!=='false';
  return inheritSimulationSettings(value,defaults);
}
