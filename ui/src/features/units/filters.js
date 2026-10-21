export const abilityGroups=[
  {key:'traits',label:'特性',keys:['strong','resistant','super-resistant','massive','extreme','target-only','colossus','behemoth','sage']},
  {key:'effects',label:'効果',keys:['weaken','stop','slow','knockback','curse','dodge']},
  {key:'attacks',label:'攻撃形式',keys:['long-range','omni','multi-hit']},
  {key:'immunities',label:'無効',keys:[]},
  {key:'abilities',label:'能力',keys:[]},
];
export function getAbilityGroup(key) {
  return abilityGroups.find(group=>group.keys.includes(key))?.key||(key.endsWith('-immune')?'immunities':'abilities');
}
export function getResistanceOptions(database) {
  return database.abilities.filter(ability=>ability.key.endsWith('-immune')).map(ability=>({key:ability.key.replace(/-immune$/,'-resist'),label:ability.label.replace(/無効(?:・耐性)?$/,'耐性')}));
}
export const unitKinds={normal:'通常',overseas:'海外',spirit:'精霊',retired:'削除済み',other:'その他'};
export const rangeFields=[['hp','体力'],['attack','攻撃力'],['dps','DPS'],['range','射程'],['cost','コスト'],['speed','速度'],['knockbacks','KB'],['respawn','再生産F'],['attackCycle','攻撃頻度F'],['foreswing','攻撃発生F'],['maxLevel','上限合計Lv'],['targetCount','対象属性数']];
