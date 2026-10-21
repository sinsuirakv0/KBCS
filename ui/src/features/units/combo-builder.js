import { statComboTypes, isStatCombo, buildComboTeam, getActiveCombos, getComboEffects, filterCombos } from './combo-model.js';
import { escapeHtml, imageHtml } from './view.js';
export function createComboBuilder(database, saved, onChange, prefix='unit-combo') {
  const element=id=>document.getElementById(id.replace('unit-combo',prefix));
  if(!element('unit-combo-effect'))element('unit-combo-builder').innerHTML='<summary id="'+prefix+'-builder-summary">にゃんコンボ</summary><p class="db-meta">共有キャラは1枠。上位形態で下位形態の条件も満たします。</p><div class="db-toolbar"><input id="'+prefix+'-query" type="search" aria-label="コンボを絞り込み" placeholder="コンボ名・キャラ名・ID"><select id="'+prefix+'-effect" aria-label="コンボの効果"></select><label><input id="'+prefix+'-fit" type="checkbox">追加できるものだけ</label><button id="'+prefix+'-clear" type="button">解除</button><span id="'+prefix+'-count" class="db-meta"></span></div><div id="'+prefix+'-team" class="unit-combo-team"></div><div id="'+prefix+'-selected"></div><details><summary id="'+prefix+'-active-summary">同時発動</summary><ul id="'+prefix+'-active" class="unit-related-list"></ul></details><div id="'+prefix+'-options" class="unit-combo-options"></div><p id="'+prefix+'-message" class="db-meta" role="status"></p>';
  const available=database.combos.filter(isStatCombo), units=new Map(database.units.map(unit=>[unit.id,unit]));
  let restored={};try{if(saved&&saved.length<10000)restored=JSON.parse(saved)||{};}catch{}
  let selected=[],forms=restored.comboForms||{},team=[],active=[];
  for(const id of Array.isArray(restored.selectedCombos)?restored.selectedCombos:[]) {
    if(available.some(combo=>combo.id===id)&&buildComboTeam(database,[...selected,id],forms).length<=5)selected.push(id);
  }
  selected=[...new Set(selected)];
  element('unit-combo-effect').innerHTML='<option value="">すべての効果</option>'+statComboTypes.filter(([,type])=>available.some(combo=>combo.type===type)).map(([,type])=>'<option value="'+type+'">'+escapeHtml(database.comboEffects[type].label.replace('キャラクターの',''))+'</option>').join('');
  function membersHtml(combo) {
    return '<div class="unit-combo-members">'+combo.members.map(member=> {
      const unit=units.get(member.id),form=unit.forms[member.form],label=form.name+'：第'+(member.form+1)+'形態以上';
      return '<span title="'+escapeHtml(label)+'" aria-label="'+escapeHtml(label)+'">'+imageHtml(database,form,32,25)+'<small>第'+(member.form+1)+'以上</small></span>';
    }).join('')+'</div>';
  }
  function renderOptions() {
    const matches=filterCombos(database,available,element('unit-combo-query').value,element('unit-combo-effect').value,team,element('unit-combo-fit').checked).filter(combo=>!selected.includes(combo.id));
    const count=matches.length;
    element('unit-combo-count').textContent=team.length+' / 5キャラ・候補'+count+'件';
    element('unit-combo-options').innerHTML=matches.map(combo=> {
      const count=new Set([...team.map(member=>member.id),...combo.members.map(member=>member.id)]).size;
      return '<article class="unit-combo-option"><div><strong>'+escapeHtml(combo.name)+'</strong><span class="db-meta"> '+escapeHtml(combo.effect)+'</span>'+membersHtml(combo)+'</div><button type="button" data-add-combo="'+combo.id+'"'+(count>5?' disabled title="'+count+'キャラ必要"':'')+'>'+ (count>5?count+'体必要':'追加')+'</button></article>';
    }).join('')||'<p class="db-meta">該当するコンボはありません。</p>';
  }
  function update() {
    team=buildComboTeam(database,selected,forms);active=getActiveCombos(database,team);
    element('unit-combo-team').innerHTML=team.map(member=> {
      const unit=units.get(member.id),form=unit.forms[member.form];
      return '<label class="unit-combo-slot" title="'+escapeHtml(form.name)+'">'+imageHtml(database,form,40,31)+'<select data-combo-form="'+member.id+'" aria-label="'+escapeHtml(unit.forms[0].name)+'の形態">'+unit.forms.map((form,index)=>index<member.minimum?'':'<option value="'+index+'"'+(index===member.form?' selected':'')+'>第'+(index+1)+'形態</option>').join('')+'</select></label>';
    }).join('')||'<span class="db-meta">コンボを追加すると必要なキャラが並びます。</span>';
    element('unit-combo-selected').innerHTML=selected.map(id=> {
      const combo=available.find(combo=>combo.id===id);
      return '<div class="unit-combo-picked"><span>'+escapeHtml(combo.name)+' <small>'+escapeHtml(combo.effect)+'</small></span><button type="button" data-remove-combo="'+id+'" aria-label="'+escapeHtml(combo.name)+'を外す">外す</button></div>';
    }).join('');
    element('unit-combo-active-summary').textContent='同時発動（'+active.length+'）';
    element('unit-combo-active').innerHTML=active.map(combo=>'<li>'+escapeHtml(combo.name)+' <small>'+escapeHtml(combo.effect)+(selected.includes(combo.id)?'':'・自動発動')+'</small></li>').join('')||'<li class="db-meta">なし</li>';
    element('unit-combo-builder-summary').innerHTML='にゃんコンボ <span class="unit-condition-summary">'+team.map(member=>imageHtml(database,units.get(member.id).forms[member.form],24,19)).join(' ')+'</span> <span class="db-meta">'+team.length+'/5体・'+active.length+'発動</span>';
    renderOptions();onChange();
  }
  function add(id) {
    if(selected.includes(id))return;
    if(!available.some(combo=>combo.id===id))return;
    if(buildComboTeam(database,[...selected,id],forms).length>5){element('unit-combo-message').textContent='5キャラを超える組み合わせです。';return;}
    selected.push(id);element('unit-combo-message').textContent='';update();
  }
  element('unit-combo-options').addEventListener('click',event=> {
    const button=event.target.closest('[data-add-combo]');if(!button)return;
    const id=Number(button.dataset.addCombo);
    add(id);
  });
  element('unit-combo-selected').addEventListener('click',event=> {const button=event.target.closest('[data-remove-combo]');if(button){selected=selected.filter(id=>id!==Number(button.dataset.removeCombo));update();}});
  element('unit-combo-team').addEventListener('change',event=>{if(event.target.dataset.comboForm){forms[event.target.dataset.comboForm]=Number(event.target.value);update();}});
  for(const id of ['unit-combo-query','unit-combo-effect','unit-combo-fit'])element(id).addEventListener('input',renderOptions);
  element('unit-combo-clear').addEventListener('click',()=>{selected=[];forms={};update();});
  update();
  return {add,set(values){forms=values.comboForms||{};selected=[];for(const id of values.selectedCombos||[])if(!selected.includes(id)&&available.some(combo=>combo.id===id)&&buildComboTeam(database,[...selected,id],forms).length<=5)selected.push(id);update();},state(){return {selectedCombos:[...selected],comboForms:Object.fromEntries(team.map(member=>[member.id,member.form])),combos:getComboEffects(database,active)};}};
}
