import {prepareUnitSearch} from '/native-unit-search.js';
import {readPageParams,writePageParams,clearPageParams,bindDetailNavigation} from "/native-state.js";
import { loadUnitDatabase } from "../../shared/game/units.js";
import { defaultUnitSettings, readUnitSettings, rarityNames, unitDetailUrl } from "../../shared/game/unit-stats.js";
import { selectUnitRows } from "./model.js";
import { escapeHtml, formatNumber, formatTime, imageHtml, comparisonHtml, rarityName, handleUnitImages,propertyIconHtml,abilityIconHtml } from "./view.js";
import {applyUnitTalents,calculateTalentStats} from "/talents.js";
import {calculateUnitStats} from '../../shared/game/unit-stats.js';
import {abilityGroups,getAbilityGroup,getResistanceOptions,unitKinds,rangeFields} from './filters.js';
import {iconChoiceHtml,bindIconHints,rarityIconHtml} from './view.js';
import {readGameSettings,initializeGameSettings} from '../../shared/browser/game-settings.js';
import {researchSettings} from '../../shared/game/game-settings.js';
import {createPagination} from '../../shared/browser/pagination.js';

const element = id => document.getElementById(id);
const rangeKeys = rangeFields.map(([key])=>key);
const selected = new Map();
let database, rows = [], page = 1, queued = false;
const talentLevels=new Map();
let nativeProfiles=new Map(),nativeRevision=0;
const pagination=createPagination(element('unit-prev').parentElement,value=>{page=value;render();});
const params = readPageParams("unit-search");
const state = {
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

function chips(options, selectedValues,kind='') {
  return options.map(({key,label})=>iconChoiceHtml(database,{key:kind==='rarity'?'rarity-'+key:key,label,value:key,checked:selectedValues.includes(key),attributes:kind==='ability'?' data-ability="'+escapeHtml(key)+'"':''})).join('');
}

function initializeControls() {
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

function saveState() {
  const query = new URLSearchParams({setup:'1'});
  for (const [key, value] of Object.entries(state)) {
    if (key === "ranges") { for (const [metric, bounds] of Object.entries(value)) for (const [index, direction] of ["Min", "Max"].entries()) if (bounds[index] !== "") query.set(metric + direction, bounds[index]); }
    else if (key === "query") { if (value) query.set("q", value); }
    else if (key === "rarities") { if (value.length) query.set("rarity", value.join(",")); }
    else if(key==='research')continue;
    else if (Array.isArray(value)) { if (value.length) query.set(key, value.join(",")); }
    else if (key in defaultUnitSettings) { if (value !== defaultUnitSettings[key]) query.set(key, String(value)); }
    else if(['spirits','unnamed'].includes(key)){if(!value)query.set(key,'false');}
    else if(key==='kind'){if(value!=='all')query.set(key,value);}
    else if(key==='includeTalentResistance'){if(!value)query.set(key,'false');}
    else if (value && !["form", "sort", "direction", "targetMode", "abilityMode"].includes(key)) query.set(key, String(value));
    else if ((key === "form" && value !== "last") || (key === "sort" && value !== "id") || (key === "direction" && value !== "asc") || (key === "targetMode" && value !== "any") || (key === "abilityMode" && value !== "all")) query.set(key, value);
  }
  writePageParams("unit-search",query);
}

function updateSelection() {
  element("unit-open-compare").textContent = "比較（" + selected.size + "/4）";
  element("unit-open-compare").disabled = selected.size < 2;
  element("unit-clear-compare").hidden = selected.size === 0;
}
function getSearchProfile(unit,form,settings=state) {
  const levels=talentLevels.get(unit.id);
  const profile=settings.applyTalents?calculateTalentStats(unit,form,database.growth[unit.growth],settings,{talents:true,talentLevels:levels},calculateUnitStats):{form,stats:calculateUnitStats(unit,form,database.growth[unit.growth],settings)};
  const native=nativeProfiles.get(unit.id+':'+form.code);if(!native)throw Error('ネイティブのキャラステータスを準備中です。');profile.stats={...profile.stats,...native,attack:native.attacks.reduce((a,b)=>a+b,0)};profile.stats.dps=profile.stats.attackCycle>0?profile.stats.attack*30/profile.stats.attackCycle:null;
  if(!settings.includeTalents)return profile;
  const potential=applyUnitTalents(unit,form,levels,60,true).form;
  // 検索用の属性・特性だけ補い、表示ステータスと詳細へ渡す本能ON/OFFは変えない。
  return {...profile,form:{...profile.form,targets:potential.targets,abilities:potential.abilities}};
}
function searchDetailUrl(unit,form) {return unitDetailUrl(unit,form);}
bindDetailNavigation('unit-detail','/pages/unit-detail/',()=>{
  const params=new URLSearchParams({setup:'1'});
  for(const key of Object.keys(defaultUnitSettings))params.set(key,String(state[key]));
  params.set('calc',JSON.stringify({talents:state.applyTalents}));
  return params;
});

function propertiesHtml(form) {
  return '<td class="unit-properties-column"><span class="unit-property-list">'+form.targets.map(key=>propertyIconHtml(database,key,database.targets.find(value=>value.key===key)?.label||key,14)).join('')+'</span></td><td class="unit-properties-column"><span class="unit-property-list">'+form.abilities.map(ability=>abilityIconHtml(database,ability,state.seconds,14)).join('')+'</span></td>';
}

async function render() {
  if (!database) return;
  const revision=++nativeRevision;try{const values=await prepareUnitSearch(database,{...state});if(revision!==nativeRevision)return;nativeProfiles=values;}catch(error){if(revision===nativeRevision){element('unit-message').textContent=error.message;element('unit-message').hidden=false;}return;}
  rows = selectUnitRows(database, state,getSearchProfile);
  element('unit-include-talent-resistance').closest('label').hidden=state.includeTalents;
  const pageSize = Number(element("unit-page-size").value);
  const pageCount = Math.max(1, Math.ceil(rows.length / pageSize));
  page = Math.min(page, pageCount);
  const visible = rows.slice((page - 1) * pageSize, page * pageSize);
  element("unit-results").innerHTML = visible.map(row => '<tr data-key="' + row.key + '"><td><input type="checkbox" data-compare="' + row.key + '" aria-label="' + escapeHtml(row.form.name) + 'を比較"' + (selected.has(row.key) ? " checked" : "") + '></td><td>' + String(row.unit.id).padStart(3, "0") + '</td><td class="db-icon">' + imageHtml(database, row.form) + '</td><td class="db-name"><a href="' + escapeHtml(searchDetailUrl(row.unit,row.form)) + '" title="' + escapeHtml(row.unit.forms.map(form => form.name).join(" / ")) + '">' + escapeHtml(row.form.name) + '</a>'+(row.unit.kind!=='normal'?'<span class="db-meta"> '+unitKinds[row.unit.kind]+'</span>':'')+'</td><td>' + rarityIconHtml(database,row.unit) + '</td>'+propertiesHtml(row.form)+'<td>' + formatNumber(row.stats.hp) + '</td><td>' + formatNumber(row.stats.attack) + '</td><td>' + formatNumber(row.stats.dps) + '</td><td>' + formatNumber(row.stats.range) + '</td><td>' + formatNumber(row.stats.cost) + '</td><td>' + formatNumber(row.stats.speed) + '</td><td>' + formatTime(row.stats.respawn, state.seconds) + '</td></tr>').join("");
  const unitCount = new Set(rows.map(row => row.unit.id)).size;
  element("unit-result-count").textContent = unitCount + "キャラ / " + rows.length + "形態";
  pagination.update(page,pageCount);
  element("unit-export").disabled = rows.length === 0;
  const conditionCount = Number(Boolean(state.exclude)) + Number(Boolean(state.attackType)) + Number(Boolean(state.talentMode)) + Number(state.minForms>0)+Number(state.guaranteed)+Number(state.exactTargets)+Number(state.negateAbilities)+Object.values(state.ranges).filter(bounds => bounds.some(value => value !== "")).length;
  element("unit-filter-summary").textContent = "詳細検索・計算条件" + (conditionCount ? "（" + conditionCount + "）" : "");
  const labels=[...(state.exclude?['除外名：'+state.exclude]:[]),...(state.negateAbilities?['選んだ特性・効果を除外']:[]),...(state.exactTargets?['選択属性のみ']:[]),...rangeFields.filter(([key])=>state.ranges[key].some(value=>value!=='')).map(([key,label])=>label+' '+(state.ranges[key][0]||'下限なし')+'〜'+(state.ranges[key][1]||'上限なし'))];
  element('unit-active-filters').textContent=labels.join(' / ');element('unit-active-filters').hidden=!labels.length;
  element('unit-search-calculation-note').textContent=(state.includeTalents?'属性・特性は本能・超本能の追加分も検索。':'')+'体力のお宝'+state.healthTreasure+'%・攻撃のお宝'+state.attackTreasure+'%・研究力Lv'+state.researchLevel+'（お宝'+state.researchTreasure+'%）を反映。'+(state.applyTalents?'第3形態以上の本能を最大Lvで反映。超本能は検索Lv60以上。':'本能は未適用。')+'特性倍率・本能玉・コンボは未適用。数値条件の時間はF（30F＝1秒）。';
  element('unit-table').querySelector('caption').textContent='キャラ検索の結果。'+element('unit-search-calculation-note').textContent;
  element('unit-table').classList.toggle('hide-properties',!element('unit-show-properties').checked);
  element("unit-message").hidden = rows.length > 0;
  element("unit-message").textContent = rows.length ? "" : "見つかりませんでした。名前を短くするか、条件をクリアしてください。";
  for (const header of document.querySelectorAll("[data-column]")) {
    const current = header.dataset.column === state.sort;
    header.setAttribute("aria-sort", current ? state.direction === "asc" ? "ascending" : "descending" : "none");
    const button = header.querySelector("button"); button.textContent = button.textContent.replace(/ [↑↓]$/, "") + (current ? state.direction === "asc" ? " ↑" : " ↓" : "");
  }
  saveState(); updateSelection();
}

function requestRender() {
  if (!database) { state.query = element("unit-query").value; state.exclude = element("unit-exclude").value; return; }
  if (queued) return;
  queued = true;
  requestAnimationFrame(() => { queued = false; readControls(); page = 1; render(); });
}

element("unit-search-form").addEventListener("submit", event => { event.preventDefault(); requestRender(); });
document.addEventListener("input",event=>{if(event.target.form===element("unit-search-form"))requestRender();});
document.addEventListener("change",event=>{if(event.target.form===element("unit-search-form"))requestRender();});
initializeGameSettings(element('unit-search-form').querySelector('.db-toolbar'),()=>state,values=>{
  Object.assign(state,readUnitSettings(new URLSearchParams(),{...state,...values}),researchSettings(values));
  element('unit-page-size').value=values.pageSize;
  if(database){initializeControls();page=1;render();}
});
element("unit-reset").addEventListener("click", () => {
  Object.assign(state, { query: "", exclude: "", form: "last", rarities: [], targets: [], abilities: [], targetMode: "any", abilityMode: "all", spirits:true,unnamed:true,kind:'all',talentMode:'',minForms:0,includeTalents:false,applyTalents:false,exactTargets:false,negateAbilities:false,guaranteed:false,fullImmunity:false,includeTalentResistance:true,attackType: "", sort: "id", direction: "asc", ranges: Object.fromEntries(rangeKeys.map(key => [key, ["", ""]])) });
  element("unit-query").value = ""; element("unit-exclude").value = "";
  if (database) { initializeControls(); page = 1; render(); }
});
element("unit-table").addEventListener("click", event => {
  const sort = event.target.closest("[data-sort]");
  if (sort) { state.direction = state.sort === sort.dataset.sort && state.direction === "asc" ? "desc" : "asc"; state.sort = sort.dataset.sort; page = 1; render(); }
});
element("unit-table").addEventListener("change", event => {
  const key = event.target.dataset.compare;
  if (!key) return;
  if (event.target.checked) {
    if (selected.size === 4) { event.target.checked = false; element("unit-message").textContent = "比較は4形態までです。"; element("unit-message").hidden = false; return; }
    selected.set(key, rows.find(row => row.key === key));
  } else selected.delete(key);
  updateSelection();
});
element('unit-page-size').value=readGameSettings().pageSize;
element("unit-page-size").addEventListener("change", () => { page = 1; render(); });
element('unit-show-properties').addEventListener('change',render);
element("unit-clear-compare").addEventListener("click", () => { selected.clear(); render(); });
element("unit-open-compare").addEventListener("click", () => { element("unit-compare-table").innerHTML = comparisonHtml(database, [...selected.values()].map(row=>({...row,...getSearchProfile(row.unit,row.unit.forms.find(form=>form.code===row.form.code)),detailUrl:searchDetailUrl(row.unit,row.form)})), state); element("unit-compare-dialog").showModal(); });
element("unit-close-compare").addEventListener("click", () => element("unit-compare-dialog").close());
element("unit-export").addEventListener("click", () => {
  const values = [["ID", "キャラ名", "形態", "レアリティ", "合計Lv", "体力", "攻撃力", "DPS", "射程", "コスト", "速度", "再生産F"], ...rows.map(row => [row.unit.id, row.form.name, row.form.index + 1, rarityName(row.unit), row.stats.level, row.stats.hp, row.stats.attack, row.stats.dps == null ? "" : Math.round(row.stats.dps), row.stats.range, row.stats.cost, row.stats.speed, row.stats.respawn])];
  const csv = values.map(row => row.map(value => '"' + String(typeof value === "string" && /^[=+@-]/.test(value) ? "'" + value : value ?? "").replaceAll('"', '""') + '"').join(",")).join("\r\n");
  const url = URL.createObjectURL(new Blob(["\uFEFF" + csv], { type: "text/csv;charset=utf-8" }));
  const link = document.createElement("a"); link.href = url; link.download = "kbc-units-v" + database.gameVersion + ".csv"; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
});
document.addEventListener("keydown", event => { if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") { event.preventDefault(); element("unit-query").focus(); element("unit-query").select(); } });
handleUnitImages();
bindIconHints(element('unit-search-form'),element('unit-filter-hint'));

async function start() {
  try {
    database = await loadUnitDatabase();
    for(const unit of database.units)talentLevels.set(unit.id,Object.fromEntries(unit.talents.map(talent=>[talent.index,talent.maxLevel])));
    initializeControls();
    if(state.exclude||state.talentMode||state.minForms||state.guaranteed||state.exactTargets||state.negateAbilities||Object.values(state.ranges).some(bounds=>bounds.some(value=>value!=='')))element('unit-filter-panel').open=true;
    element("unit-data-version").textContent = "JP データv" + database.gameVersion;
    element("unit-retry").hidden = true;
    render();
  } catch (error) {
    element("unit-result-count").textContent = "取得失敗";
    element("unit-message").textContent = error.message; element("unit-message").hidden = false; element("unit-retry").hidden = false;
  }
}
element("unit-retry").addEventListener("click", start);
element("unit-query").value = state.query; element("unit-exclude").value = state.exclude;
start();

window.addEventListener('kbcs:simulation-change',event=>{Object.assign(state,event.detail);if(database){initializeControls();page=1;render();}});
