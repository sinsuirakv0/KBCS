import {loadUnitDatabase} from './src/shared/game/units.js';
import {readUnitSettings,unitDetailUrl} from './src/shared/game/unit-stats.js';
import {createNativeStatistics} from './native-calculation.js';
import {createDamageCalculator} from './damage-calculator.js';
import {createUnitGrowth} from './src/features/units/growth.js';
import {comparisonHtml} from './src/features/units/view.js';
import {createComboBuilder} from './src/features/units/combo-builder.js';
import {isStatCombo} from './src/features/units/combo-model.js';
import {saveElementImage} from './src/shared/browser/capture.js';
import {readGameSettings} from './src/shared/browser/game-settings.js';
import {readPageParams,writePageParams,bindDetailNavigation} from './native-state.js';
import {escapeHtml,formatNumber,formatTime,propertyIconHtml,imageHtml,rarityIconHtml,abilitiesHtml,handleUnitImages} from './src/features/units/view.js';

const element=id=>document.getElementById(id),params=readPageParams('unit-detail');
const settings=readUnitSettings(params,readGameSettings());
let database,unit,nativeStatistics,calculateTalentStats;
let renderVersion=0;
let damageCalculator;
let talentLevels={};
let growthPanel,growthForm,comboBuilder;
const restore=key=>{try{const value=JSON.parse(params.get(key)||'{}');return value&&typeof value==='object'?value:{};}catch{return {};}};
const restored={...restore('calc'),...restore('display')};
const displaySettings=()=>element('table-treasure').checked?settings:{...settings,healthTreasure:0,attackTreasure:0,healthTreasureBonus:0,attackTreasureBonus:0,fruitByTarget:{},researchTreasure:0,researchReductionOverride:(settings.researchLevel-1)*6};
const cells=(label,value)=>'<th scope="row">'+label+'</th><td class="unit-value">'+escapeHtml(value)+'</td>';
const information=(label,html,extra=false)=>'<tr'+(extra?' class="unit-extra"':'')+'><th scope="row">'+label+'</th><td colspan="5" class="unit-information">'+html+'</td></tr>';

function progressionHtml(value){
  const lines=[],description=value.description.trim();
  if(/^[？?]+$/.test(description))lines.push('<li>図鑑では非表示</li>');
  else if(description&&!/^Lv\d+で進化$/.test(description)&&!/^合計Lv\d+到達後\n必要数のXP、(?:マタタビ|獣石)を使用で進化$/.test(description))lines.push('<li class="unit-description">'+escapeHtml(description)+'</li>');
  const materials=[...(value.level>0?['合計Lv'+value.level]:[]),...(value.xp>0?['XP '+formatNumber(value.xp)]:[]),...(value.materials||[]).map(item=>'<span class="unit-material" title="'+escapeHtml(item.name)+'">'+(item.icon?'<img src="'+escapeHtml(database.imageBase+item.icon)+'" alt="'+escapeHtml(item.name)+'" loading="lazy">':escapeHtml(item.name))+'×'+item.count+'</span>')];
  if(materials.length)lines.push('<li>'+materials.join(' / ')+'</li>');
  if(value.stages.length)lines.push('<li>'+(value.stages.length>1?'対象ステージ（いずれか）：':'対象ステージ：')+'<ul>'+value.stages.map(stage=>{
    const label=escapeHtml((stage.series?stage.series+' / ':'')+stage.mapName+'「'+stage.stageName+'」の報酬');
    return '<li>'+(stage.map>=0&&stage.map<1000?'<a href="/pages/stage-detail/?map=N'+String(stage.map).padStart(3,'0')+'&stage='+stage.stage+'">'+label+'</a>':label)+'</li>';
  }).join('')+'</ul></li>');
  return lines.length?'<ul class="unit-progression">'+lines.join('')+'</ul>':'条件の記載なし';
}

function sheet(form){
  const profile=calculateTalentStats(unit,form,database.growth[unit.growth],displaySettings(),{talents:element('detail-apply-talents').checked,talentLevels});
  form=profile.form;
  const stats=profile.stats,time=value=>formatTime(value,settings.seconds);
  const traits=new Set(['omni','long-range','multi-hit']);
  const abilities=abilitiesHtml(database,form.abilities.filter(ability=>!traits.has(ability.key)),settings.seconds);
  const evolution=unit.evolution.find(value=>value.form===form.index);
  return '<table class="unit-sheet" id="unit-sheet-'+form.code+'"><colgroup><col><col><col><col><col><col></colgroup><tbody>'+
    '<tr><th class="unit-id">'+String(unit.id).padStart(3,'0')+'-'+(form.index+1)+'</th><th colspan="3" class="unit-form-name"><h2>'+escapeHtml(form.name)+'</h2></th><td colspan="2">'+rarityIconHtml(database,unit)+(unit.isSpirit?'・精霊':'')+'</td></tr>'+
    '<tr><td colspan="2" rowspan="3" class="unit-portrait">'+imageHtml(database,form,56,43)+'</td>'+cells('体力',formatNumber(stats.hp))+cells('KB',formatNumber(stats.knockbacks))+'</tr>'+
    '<tr>'+cells('攻撃力',formatNumber(stats.attack))+cells('速度',formatNumber(stats.speed))+'</tr>'+
    '<tr>'+cells('DPS',formatNumber(stats.dps))+cells('射程',formatNumber(stats.range))+'</tr>'+
    '<tr>'+cells('コスト',formatNumber(stats.cost))+cells('攻撃頻度',time(stats.attackCycle))+cells('攻撃発生',time(stats.foreswing))+'</tr>'+
    '<tr>'+cells('再生産',time(stats.respawn))+cells('待機時間',time(stats.attackCycle==null?null:stats.attackCycle-form.foreswings.at(-1)))+cells('攻撃後',time(stats.backswing))+'</tr>'+
    (form.targets.length?information('対象',form.targets.map(key=>propertyIconHtml(database,key,database.targets.find(target=>target.key===key)?.label||key)).join(' ')):'')+
    information('攻撃特性','<ul class="unit-abilities"><li>'+propertyIconHtml(database,form.attackType==='範囲'?'area':'single',form.attackType)+'</li>'+abilitiesHtml(database,form.abilities.filter(ability=>traits.has(ability.key)),settings.seconds)+(stats.attacks.length>1?'<li>連続攻撃 '+stats.attacks.length+'回</li>':'')+'</ul>')+
    information('特性',abilities?'<ul class="unit-abilities">'+abilities+'</ul>':'なし')+
    (form.ranges.length?information('攻撃範囲',escapeHtml(form.ranges.map(range=>range.join('〜')).join(' / '))):'')+
    (stats.attacks.length>1?information('連続攻撃',stats.attacks.map((attack,index)=>escapeHtml(formatNumber(attack)+'（発生 '+time(form.foreswings[index])+'）')).join(' / ')):'')+
    information('説明','<span class="unit-description">'+escapeHtml(form.description)+'</span>',true)+
    (form.index===0?information('入手条件',progressionHtml(unit.acquisition),true):'')+
    (evolution?information('進化条件',progressionHtml(evolution),true):'')+
    information('表示','<button type="button" data-capture="unit-sheet-'+form.code+'">画像保存</button>')+
    (form.index===unit.forms.at(-1).index&&unit.talents.length?information('本能','<div id="unit-talent-host"></div>'):'')+'</tbody></table>';
}

function talentFields(){
  element('unit-calc-talents').innerHTML=unit.talents.map(talent=>{
    const icon=database.propertyAtlas.icons[talent.effect.key]?propertyIconHtml(database,talent.effect.key,talent.name,18,false):'';
    return '<div class="unit-talent-entry"><div class="unit-talent-heading"><label>'+icon+'<strong>'+(talent.limit?'超本能：':'')+escapeHtml(talent.name)+'</strong><select data-talent="'+talent.index+'" aria-label="'+escapeHtml((talent.limit?'超本能：':'')+talent.name)+'のレベル">'+Array.from({length:talent.maxLevel+1},(_,level)=>'<option value="'+level+'"'+(level===talentLevels[talent.index]?' selected':'')+'>'+(level?'Lv'+level:'なし')+'</option>').join('')+'</select></label><span class="db-meta" data-talent-status="'+talent.index+'"></span></div><small data-talent-detail>'+escapeHtml(talent.description)+'</small><small data-np-cost>NP ('+talent.costs.join(',')+') / 最大 '+talent.costs.reduce((total,value)=>total+value,0)+' / 設定 <span data-talent-np="'+talent.index+'">0</span></small></div>';
  }).join('');
}

function updateTalents(){
  const enabled=element('detail-apply-talents').checked;
  const profile=calculateTalentStats(unit,unit.forms.at(-1),database.growth[unit.growth],displaySettings(),{talents:enabled,talentLevels});
  let selectedNp=0,appliedNp=0;
  for(const talent of unit.talents){
    const level=talentLevels[talent.index],applied=profile.applied.includes(talent.index);
    const cost=talent.costs.slice(0,level).reduce((total,value)=>total+value,0);
    selectedNp+=cost;if(applied)appliedNp+=cost;
    element('unit-calc-talents').querySelector('[data-talent-status="'+talent.index+'"]').textContent=applied?'反映中':!enabled?'反映OFF':!level?'なし':talent.limit&&profile.stats.level<60?'Lv60以上':'第3形態以上';
    element('unit-calc-talents').querySelector('[data-talent-np="'+talent.index+'"]').textContent=cost;
    const select=element('unit-calc-talents').querySelector('[data-talent="'+talent.index+'"]');
    select.disabled=!enabled;
    select.title=talent.description;
  }
  element('unit-talent-total').textContent='設定Lvの合計NP：'+selectedNp+'（表に適用中：'+appliedNp+'）';
}

async function render(){
  const version=++renderVersion;
  settings.level=Math.max(1,Math.min(200,unit.maxLevel+unit.plusLevel||1,Math.trunc(Number(element('detail-level').value)||1)));
  element('detail-level').value=settings.level;
  element('detail-level').dispatchEvent(new Event('kbcs:level-sync'));
  settings.seconds=element('detail-time').value==='seconds';
  try {
    const prepared=await nativeStatistics.prepare(displaySettings(),{talents:element('detail-apply-talents').checked,talentLevels,combos:comboBuilder?.state().combos});
    if(version!==renderVersion)return;
    calculateTalentStats=prepared.calculate;
    element('unit-detail-status').hidden=true;
  } catch(error) {
    if(version!==renderVersion)return;
    element('unit-detail-status').hidden=false;element('unit-detail-status').textContent=error.message;return;
  }
  element('unit-talent-staging').append(element('unit-talent-controls'));
  element('unit-form-sheets').innerHTML=unit.forms.slice().reverse().map(sheet).join('');
  element('unit-talent-host')?.append(element('unit-talent-controls'));
  element('unit-form-sheets').classList.toggle('is-expanded',element('detail-expanded').checked);
  updateTalents();
  element('unit-form-comparison').innerHTML=comparisonHtml(database,unit.forms.map(form=>({unit,form,stats:calculateTalentStats(unit,form,database.growth[unit.growth],displaySettings(),{talents:element('detail-apply-talents').checked,talentLevels}).stats})),settings);
  growthPanel?.update();
  damageCalculator?.update();
  const stored=new URLSearchParams({...settings,setup:'1'});
  const team=comboBuilder?.state();
  stored.set('calc',JSON.stringify({talents:element('detail-apply-talents').checked,talentLevels,treasureEnabled:element('table-treasure').checked,...(team?{selectedCombos:team.selectedCombos,comboForms:team.comboForms}:{})}));
  writePageParams('unit-detail',stored);
}

function raiseTalentLevel(){
  if(unit.talents.some(talent=>talent.limit&&talentLevels[talent.index]>0))element('detail-level').value=Math.max(60,Number(element('detail-level').value));
}

try{
  database=await loadUnitDatabase();unit=database.units.find(unit=>unit.id===Number(params.get('id')||0));if(!unit)throw Error('キャラが見つかりません');
  const selected=unit.forms.find(form=>form.code===params.get('form'))||unit.forms.at(-1);
  growthForm=selected;
  nativeStatistics=createNativeStatistics(unit,database.growth[unit.growth],database.gameVersion);
  element('unit-title').textContent=selected.name;document.title=selected.name+' | KBCS';
  element('unit-detail-version').textContent='JP データv'+database.gameVersion;
  element('detail-level').max=unit.maxLevel+unit.plusLevel||1;element('detail-level').value=settings.level;
  element('detail-time').value=settings.seconds?'seconds':'frames';
  element('table-treasure').checked=restored.treasureEnabled!==false;
  element('detail-apply-talents').checked=restored.talents!==false;
  talentLevels=Object.fromEntries(unit.talents.map(talent=>[talent.index,Math.max(0,Math.min(talent.maxLevel,Math.trunc(Number(restored.talentLevels?.[talent.index]??talent.maxLevel)||0)))]));
  talentFields();
  element('unit-summary').textContent='上限Lv'+unit.maxLevel+'+'+unit.plusLevel;
  element('unit-form-tabs').innerHTML=unit.forms.map(form=>'<a href="#unit-sheet-'+form.code+'" data-form="'+form.index+'"'+(form.index===selected.index?' aria-current="true"':'')+'>'+imageHtml(database,form,32,25)+'<span>'+escapeHtml(form.name)+'<small>第'+(form.index+1)+'形態</small></span></a>').join('');
  element('unit-form-tabs').addEventListener('click',event=>{const link=event.target.closest('[data-form]');if(link){for(const item of element('unit-form-tabs').children)item.removeAttribute('aria-current');link.setAttribute('aria-current','true');growthForm=unit.forms[Number(link.dataset.form)];growthPanel?.update();}});
  const combos=unit.combos.map(id=>database.combos.find(combo=>combo.id===id)).filter(Boolean);
  element('unit-combo-section').hidden=!combos.length;
  element('unit-combo-summary').textContent='にゃんコンボ（'+combos.length+'）';
  element('unit-combo-list').innerHTML=combos.map(combo=>'<li><strong>'+escapeHtml(combo.name)+'</strong> / '+escapeHtml(combo.effect)+(isStatCombo(combo)?' <button type="button" data-build-combo="'+combo.id+'">編成に追加</button>':'')+'<div class="unit-combo-members">'+combo.members.map(member=>{
    const peer=database.units.find(value=>value.id===member.id),form=peer?.forms[member.form];
    return form?'<a href="'+escapeHtml(unitDetailUrl(peer,form,settings))+'" title="'+escapeHtml(form.name)+'">'+imageHtml(database,form,40,31)+'<span>'+escapeHtml(form.name)+'・第'+(member.form+1)+'以上</span></a>':'<span>ID '+member.id+'・第'+(member.form+1)+'以上</span>';
  }).join('')+'</div></li>').join('');
  comboBuilder=createComboBuilder(database,params.get('calc'),()=>{if(comboBuilder)render();},'unit-team');
  element('unit-combo-list').addEventListener('click',event=>{const button=event.target.closest('[data-build-combo]');if(button){comboBuilder.add(Number(button.dataset.buildCombo));element('unit-team-builder').open=true;element('unit-team-builder').scrollIntoView({block:'start'});}});
  growthPanel=createUnitGrowth(()=>{
    const options={talents:element('detail-apply-talents').checked,talentLevels,combos:comboBuilder?.state().combos};
    return {unit,form:growthForm,settings:displaySettings(),options,level:settings.level,superTalents:unit.talents.some(talent=>talent.limit&&talentLevels[talent.index]>0),buildRows:()=>Array.from({length:Math.max(1,Math.min(200,unit.maxLevel+unit.plusLevel||1))},(_,index)=>{
      const stats=calculateTalentStats(unit,growthForm,database.growth[unit.growth],{...displaySettings(),level:index+1},options).stats;
      return {level:index+1,hp:stats.hp,attack:stats.attack};
    })};
  });
  element('unit-detail-status').hidden=true;element('unit-detail-content').hidden=false;await render();
  damageCalculator=createDamageCalculator(database,unit,()=>({form:growthForm,settings:displaySettings(),combos:comboBuilder?.state().combos,calculate:form=>calculateTalentStats(unit,form,database.growth[unit.growth],displaySettings(),{talents:element('detail-apply-talents').checked,talentLevels})}));
  document.addEventListener('input',event=>{if(event.target.form===element('unit-detail-settings'))render();});
  element('unit-detail-settings').addEventListener('submit',event=>event.preventDefault());
  element('unit-talent-controls').addEventListener('input',event=>{
    if(event.target.id==='unit-show-np'){element('unit-talent-controls').classList.toggle('show-details',event.target.checked);return;}
    if(event.target.dataset.talent!=null){talentLevels[event.target.dataset.talent]=Number(event.target.value);if(unit.talents[Number(event.target.dataset.talent)].limit&&Number(event.target.value)>0)raiseTalentLevel();}
    if(event.target.id==='detail-apply-talents'&&event.target.checked)raiseTalentLevel();
    const focused=document.activeElement;
    render();focused?.focus({preventScroll:true});
  });
  for(const [id,maximum] of [['unit-calc-talents-max',true],['unit-calc-talents-zero',false]])element(id).addEventListener('click',()=>{
    element('detail-apply-talents').checked=true;
    for(const talent of unit.talents){talentLevels[talent.index]=maximum?talent.maxLevel:0;element('unit-calc-talents').querySelector('[data-talent="'+talent.index+'"]').value=talentLevels[talent.index];}
    if(maximum)raiseTalentLevel();render();
  });
  element('unit-source-panel').addEventListener('toggle',async()=>{
    if(!element('unit-source-panel').open||element('source-text').textContent)return;
    try{const response=await fetch('/api/source?id='+unit.id);const source=await response.json();if(!response.ok)throw Error(source.error);element('source-metadata').textContent=source.metadata.version+' / '+source.original+' / SHA-256 '+source.sha256;element('source-text').textContent=source.text;}
    catch(error){element('source-text').textContent=error.message;}
  });
}catch(error){element('unit-detail-status').textContent=error.message;}
handleUnitImages();
window.addEventListener('kbcs:simulation-change',event=>{Object.assign(settings,event.detail);if(unit)render();});
bindDetailNavigation('unit-detail','/pages/unit-detail/',()=>new URLSearchParams({...settings,setup:'1'}));
document.addEventListener('click',async event=>{
  const button=event.target.closest('[data-capture]');if(!button||button.disabled)return;
  button.disabled=true;const status=element('unit-capture-status');status.textContent='画像を作成しています。';
  try{await saveElementImage(element(button.dataset.capture),'KBCS-unit-'+unit.id+'-'+button.dataset.capture);status.textContent='画像を保存しました。';}
  catch(error){status.textContent=error.message;}
  finally{button.disabled=false;}
});
