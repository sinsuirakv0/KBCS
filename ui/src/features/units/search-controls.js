import {readUnitSettings,rarityNames} from '../../shared/game/unit-stats.js';
import {readGameSettings} from '../../shared/browser/game-settings.js';
import {researchSettings} from '../../shared/game/game-settings.js';
import {abilityGroups,getAbilityGroup,getResistanceOptions,unitKinds,rangeFields} from './filters.js';
import {iconChoiceHtml,escapeHtml,bindIconHints} from './view.js';
const element=id=>document.getElementById(id),rangeKeys=rangeFields.map(([key])=>key);

// キャラデータと編成は、同じ検索フォーム・条件の読取を使う。
export function mountUnitSearchForm(host){
 let form=element('unit-search-form');
 if(!form){host.insertAdjacentHTML('beforeend',unitSearchFormHtml);form=element('unit-search-form');}
 else if(!form.childElementCount)form.innerHTML=unitSearchFormHtml.slice(unitSearchFormHtml.indexOf('>')+1,unitSearchFormHtml.lastIndexOf('</form>'));
 return form;
}
export function createUnitSearchState(params=new URLSearchParams()){
return {
  ...readUnitSettings(params,readGameSettings()), query: params.get("q") || "", exclude: params.get("exclude") || "",
  form: ["last", "all", "f", "c", "s", "u"].includes(params.get("form")) ? params.get("form") : "last",
  rarities: (params.get("rarity") || "").split(",").filter(Boolean).map(Number).filter(value => value >= 0 && value <= 5),
  targets: (params.get("targets") || "").split(",").filter(Boolean), abilities: (params.get("abilities") || "").split(",").filter(Boolean),
  targetMode: params.get("targetMode") === "all" ? "all" : "any", abilityMode: params.get("abilityMode") === "any" ? "any" : "all",
  spirits: params.get("spirits") !== "false", unnamed: params.get("unnamed") !== "false",
  kind:Object.hasOwn(unitKinds,params.get('kind'))?params.get('kind'):'all',
  talentMode:['normal','super','none'].includes(params.get('talentMode'))?params.get('talentMode'):params.get('talents')==='true'?'normal':'',
  applyTalents:params.get('applyTalents')==='true',exactTargets:params.get('exactTargets')==='true',negateAbilities:params.get('negateAbilities')==='true',guaranteed:params.get('guaranteed')==='true',fullImmunity:params.get('fullImmunity')==='true',
  includeTalentResistance:params.get('includeTalentResistance')!=='false',includeTalents:params.get('includeTalents')==='true',
  minForms:[2,3,4].includes(Number(params.get('minForms')))?Number(params.get('minForms')):0,
  attackType: ["単体", "範囲"].includes(params.get("attackType")) ? params.get("attackType") : "",
  ranges: Object.fromEntries(rangeKeys.map(key => [key, [params.get(key + "Min") || "", params.get(key + "Max") || ""]])),
  sort: ["id", "name", "rarity", ...rangeKeys, "dps"].includes(params.get("sort")) ? params.get("sort") : "id",
  direction: params.get("direction") === "desc" ? "desc" : "asc",
};

}
export function createUnitFilterControls(getDatabase,state){
function chips(options, selectedValues,kind='') {
  const database=getDatabase();
  return options.map(({key,label})=>iconChoiceHtml(database,{key:kind==='rarity'?'rarity-'+key:key,label,value:key,checked:selectedValues.includes(key),attributes:kind==='ability'?' data-ability="'+escapeHtml(key)+'"':''})).join('');
}

function initializeControls() {
  const database=getDatabase();
  element('unit-filter-hint').textContent='';
  element("unit-rarity").innerHTML = chips(rarityNames.map((label, key) => ({ key, label })), state.rarities,'rarity');
  state.targets = state.targets.filter(key => database.targets.some(target => target.key === key));
  const resistanceOptions=getResistanceOptions(database);
  state.abilities = state.abilities.filter(key => [...database.abilities,...resistanceOptions].some(ability => ability.key === key));
  element("unit-targets").innerHTML = chips(database.targets, state.targets,'target');
  const groupChips=key=>chips(database.abilities.filter(ability=>getAbilityGroup(ability.key)===key).map(ability=>({...ability,label:ability.label.replace('無効・耐性','無効')})),state.abilities,'ability');
  element('unit-traits').innerHTML=groupChips('traits');
  element("unit-abilities").innerHTML = abilityGroups.filter(group=>group.key!=='traits').map(group=>'<div class="unit-filter-row"><span class="unit-filter-label">'+({attacks:'攻撃',immunities:'無効'}[group.key]||group.label)+'</span><fieldset class="db-filter-group" aria-label="'+group.label+'">'+groupChips(group.key)+'</fieldset></div>').join('');
  element('unit-abilities').insertAdjacentHTML('beforeend','<div class="unit-filter-row"><span class="unit-filter-label">耐性</span><div><fieldset class="db-filter-group" aria-label="耐性">'+chips(resistanceOptions,state.abilities,'ability')+'</fieldset><label class="unit-resistance-talents" title="数値への本能反映とは別に、第3形態以上で本能から獲得できる耐性も探します。"><input id="unit-include-talent-resistance" type="checkbox"'+(state.includeTalentResistance?' checked':'')+'>本能の耐性だけ含む</label></div></div>');
  element("unit-ranges").innerHTML = rangeFields.map(([key,label]) => '<div class="unit-range"><span>' + label + '</span><input type="number" min="0" step="any" id="range-' + key + '-min" aria-label="' + label + 'の下限"><span>〜</span><input type="number" min="0" step="any" id="range-' + key + '-max" aria-label="' + label + 'の上限"></div>').join("");
  const controls = { "unit-query": state.query, "unit-exclude": state.exclude, "unit-form": state.form, "unit-level": state.level, "unit-time": state.seconds ? "seconds" : "frames", "unit-attack-type": state.attackType, "unit-health-treasure": state.healthTreasure, "unit-attack-treasure": state.attackTreasure, "unit-chapter": state.chapter, "unit-research-level": state.researchLevel,"unit-research-treasure":state.researchTreasure,'unit-kind':state.kind,'unit-talent-mode':state.talentMode,'unit-min-forms':state.minForms };
  for (const [id, value] of Object.entries(controls)) element(id).value = value;
  for(const [id,key] of [['unit-include-talents','includeTalents'],['unit-apply-talents','applyTalents'],['unit-exact-targets','exactTargets'],['unit-negate-abilities','negateAbilities'],['unit-guaranteed','guaranteed']])element(id).checked=state[key];
  for(const [id,key] of [['unit-target-mode','targetMode'],['unit-ability-mode','abilityMode']])for(const input of element(id).querySelectorAll('input'))input.checked=input.value===state[key];
  for (const key of rangeKeys) for (const [index, direction] of ["min", "max"].entries()) element("range-" + key + "-" + direction).value = state.ranges[key][index];
}

function readControls() {
  const checked = id => [...element(id).querySelectorAll("input:checked")].map(input => input.value);
  state.query = element("unit-query").value; state.exclude = element("unit-exclude").value;
  state.rarities = checked("unit-rarity").map(Number); state.targets = checked("unit-targets"); state.abilities = [...document.querySelectorAll('[data-ability]:checked')].map(input=>input.value);
  state.form = element("unit-form").value; state.targetMode = element("unit-target-mode").querySelector('input:checked').value; state.abilityMode = element("unit-ability-mode").querySelector('input:checked').value; state.attackType = element("unit-attack-type").value;
  state.kind=element('unit-kind').value;state.talentMode=element('unit-talent-mode').value;state.minForms=Number(element('unit-min-forms').value);
  for(const [id,key] of [['unit-include-talents','includeTalents'],['unit-apply-talents','applyTalents'],['unit-exact-targets','exactTargets'],['unit-negate-abilities','negateAbilities'],['unit-guaranteed','guaranteed'],['unit-include-talent-resistance','includeTalentResistance']])state[key]=element(id).checked;
  for (const [id, key, min, max] of [["unit-level", "level", 1, 200], ["unit-health-treasure", "healthTreasure", 0, 300], ["unit-attack-treasure", "attackTreasure", 0, 300]]) state[key] = Math.max(min, Math.min(max, Number(element(id).value) || min));
  state.chapter = Number(element("unit-chapter").value); Object.assign(state,researchSettings({researchLevel:element('unit-research-level').value,researchTreasure:element('unit-research-treasure').value})); state.seconds = element("unit-time").value === "seconds";
  for (const key of rangeKeys) state.ranges[key] = [element("range-" + key + "-min").value, element("range-" + key + "-max").value];
}

 bindIconHints(element('unit-search-form'),element('unit-filter-hint'));
 return {initializeControls,readControls};
}
export const unitSearchFormHtml='<form id="unit-search-form" role="search" aria-label="キャラ検索">\n        <div class="db-toolbar"><input id="unit-query" type="search" aria-label="名前・ID" placeholder="名前・ID" autocomplete="off"><button type="button" id="unit-reset">クリア</button></div>\n        <div class="unit-filter-row"><span class="unit-filter-label">レア度</span><fieldset id="unit-rarity" class="db-filter-group" aria-label="レアリティ"></fieldset></div>\n        <div class="db-toolbar">\n          <label>形態<select id="unit-form"><option value="last">最終形態</option><option value="all">全形態</option><option value="f">第1</option><option value="c">第2</option><option value="s">第3</option><option value="u">第4</option></select></label>\n          <label>合計Lv<input id="unit-level" type="number" min="1" max="200" value="30"></label>\n          <label>単位<select id="unit-time"><option value="seconds">秒</option><option value="frames">F</option></select></label>\n          <label>種類<select id="unit-kind"><option value="all">すべて</option><option value="normal">通常</option><option value="overseas">海外</option><option value="spirit">精霊</option><option value="retired">削除済み</option><option value="other">その他</option></select></label>\n          <label><input id="unit-apply-talents" type="checkbox">数値に本能を最大Lvで反映</label>\n        </div>\n        <div class="db-toolbar"><label title="第3形態以上で取得できる通常本能・超本能の属性と特性を最大Lvで探します。検索Lvや数値への本能反映とは別です。"><input id="unit-include-talents" type="checkbox">本能で追加される属性・特性も検索</label><span class="db-meta">超本能も含む・数値反映とは別</span></div>\n        <div class="unit-match-toolbar">\n          <fieldset id="unit-target-mode" class="unit-match-mode"><legend>属性</legend><label class="db-chip" title="選んだ属性のいずれかを持つ"><input type="radio" name="targetMode" value="any" checked><span>OR</span></label><label class="db-chip" title="選んだ属性をすべて持つ"><input type="radio" name="targetMode" value="all"><span>AND</span></label></fieldset>\n          <fieldset id="unit-ability-mode" class="unit-match-mode"><legend>特性・効果</legend><label class="db-chip" title="選んだ特性・効果・無効・耐性・能力をすべて持つ"><input type="radio" name="abilityMode" value="all" checked><span>AND</span></label><label class="db-chip" title="選んだ特性・効果・無効・耐性・能力のいずれかを持つ"><input type="radio" name="abilityMode" value="any"><span>OR</span></label></fieldset>\n        </div>\n        <div class="unit-filter-row"><span class="unit-filter-label">属性</span><fieldset id="unit-targets" class="db-filter-group" aria-label="対象属性"></fieldset></div>\n        <div class="unit-filter-row"><span class="unit-filter-label">特性</span><fieldset id="unit-traits" class="db-filter-group" aria-label="特性"></fieldset></div>\n        <div id="unit-abilities"></div>\n        <output id="unit-filter-hint" class="unit-filter-hint db-meta" aria-live="polite"></output>\n        <details id="unit-filter-panel" class="unit-related"><summary id="unit-filter-summary">詳細検索・計算条件</summary>\n          <div class="db-toolbar"><label><input id="unit-exact-targets" type="checkbox">選択属性以外を持たない</label><label><input id="unit-negate-abilities" type="checkbox">選択した特性・効果を除外</label></div>\n          <div class="db-toolbar"><label>除外名<input id="unit-exclude" type="search" placeholder="除外する名前"></label><label>攻撃<select id="unit-attack-type"><option value="">すべて</option><option>単体</option><option>範囲</option></select></label><label>本能<select id="unit-talent-mode"><option value="">指定なし</option><option value="normal">本能あり</option><option value="super">超本能あり</option><option value="none">本能なし</option></select></label><label>実装形態<select id="unit-min-forms"><option value="0">指定なし</option><option value="2">第2以上</option><option value="3">第3以上</option><option value="4">第4あり</option></select></label></div>\n          <div class="db-toolbar"><label><input id="unit-guaranteed" type="checkbox">選んだ効果・能力の発動率100%</label></div>\n          <details open><summary>数値条件</summary>\n          <div class="unit-ranges" id="unit-ranges"></div>\n          </details>\n          <details><summary>計算条件</summary><div class="db-toolbar"><label>体力のお宝 %<input id="unit-health-treasure" type="number" min="0" max="300" value="300"></label><label>攻撃のお宝 %<input id="unit-attack-treasure" type="number" min="0" max="300" value="300"></label><label>コスト<select id="unit-chapter"><option value="1">日本編1章</option><option value="2" selected>2章・未来・宇宙</option><option value="3">日本編3章</option></select></label><label>研究力 Lv<input id="unit-research-level" type="number" min="1" max="30" value="30"></label><label>研究力のお宝 %<input id="unit-research-treasure" type="number" min="0" max="300" value="300"></label></div></details>\n        </details>\n      </form>';
