// 編成へ新しく追加するキャラの初期値。保存済み・読込済みの設定には適用しない。
export function createFormationMember(unit){
  const maximum=unit.rarity<=2;
  const level=maximum?unit.maxLevel:Math.min(unit.maxLevel,unit.rarity===4?60:50);
  return {unitId:unit.id,form:Math.max(...unit.forms.map(form=>form.index)),level,plus:maximum?unit.plusLevel:0,talents:Object.fromEntries(unit.talents.map(talent=>[talent.index,talent.maxLevel])),orbs:[]};
}

// 設定値と実際に使う値を分け、Lvを戻した際も第四形態・本能Lvを保持する。
export function resolveFormationMember(unit,member){
  const advancedUnlocked=formationAdvancedUnlocked(unit,member);
  const requested=!advancedUnlocked&&member.form===3?2:member.form,form=formationListForm(unit,requested).index;
  return {...member,orbs:member.orbs.slice(0,unit.orbSlots??0),form,talents:Object.fromEntries(unit.talents.map(talent=>[talent.index,!advancedUnlocked&&talent.limit?0:member.talents[talent.index]??0]))};
}

export function formationDisplayName(document,index){
  return document.slotName?.trim()||(document.name&&document.name!=='新しい編成'?document.name:'編成'+(index??''));
}
export function formationListForm(unit,choice='max'){
  const forms=unit.forms.filter(form=>choice==='max'||form.index<=Number(choice));
  return forms.reduce((latest,form)=>!latest||form.index>latest.index?form:latest,null)||unit.forms[0];
}

// ユーザー指定の合計Lv（＋値を含む）で解放する。
export function formationAdvancedUnlocked(unit,member){return unit.rarity!==4||Number(member.level)+Number(member.plus??0)>=60;}
