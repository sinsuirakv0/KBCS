const element=id=>document.getElementById(id);
const icons={left:'M3 3h18v18H3zM9 3v18',right:'M3 3h18v18H3zM15 3v18',bottom:'M3 3h18v18H3zM3 15h18',close:'m6 6 12 12M6 18 18 6'};
const icon=name=>'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="'+icons[name]+'"/></svg>';
const create=(tag,className,html='')=>{const node=document.createElement(tag);node.className=className;node.innerHTML=html;return node;};
const move=(selector,target)=>{const node=typeof selector==='string'?document.querySelector(selector):selector;if(node)target.append(node);return node;};

import {createSimulationSettings} from './simulation-settings.js';
import {openSiteSettings} from './src/shared/browser/game-settings.js';
import {createLevelControl} from './src/shared/browser/level-control.js';

export function initializeWorkspace(){
  const shell=document.querySelector('.site-shell'),main=element('main');
  if(!shell||!main)return;
  const header=shell.querySelector('.site-header');
  const navigation=header.querySelector('.site-nav');
  navigation.innerHTML='<a href="/">ホーム</a><button type="button" data-page-back aria-label="戻る" title="戻る">←</button><button type="button" data-page-forward aria-label="次へ" title="次へ">→</button><button type="button" data-page-reload aria-label="ページを再読み込み" title="ページを再読み込み">↻</button>';
  navigation.querySelector('[data-page-back]').addEventListener('click',()=>history.back());
  navigation.querySelector('[data-page-forward]').addEventListener('click',()=>history.forward());
  navigation.querySelector('[data-page-reload]').addEventListener('click',()=>location.reload());
  const page=location.pathname.split('/').filter(Boolean).at(-1)||'home';
  const titles={'inventory':'持ち物','stage-sortie':'出撃準備','formation':'キャラクター編成','stage-play':'ステージ Play','unit-motion':'キャラモーション','enemy-motion':'敵モーション','effect-motion':'その他モーション','unit-search':'キャラ検索','unit-detail':'キャラ詳細','tunit-search':'敵検索','tunit-detail':'敵詳細','stage-search':'ステージ検索','stage-detail':'ステージ詳細',home:'ホーム'};
  const title=titles[page]||main.querySelector('h1')?.textContent||'KBCS';
  let saved={};
  try{saved=JSON.parse(localStorage.getItem('kbcs:workspace')||'{}')||{};}catch{}
  const boundedWidth=(value,fallback)=>Math.max(200,Math.min(440,Number(value)||fallback));
  const state={left:saved.left!==false,right:saved.right!==false,leftWidth:boundedWidth(saved.leftWidth,272),rightWidth:boundedWidth(saved.rightWidth,236)};
  if(innerWidth<800&&state.left&&state.right)state.right=false;
  const store=()=>{try{localStorage.setItem('kbcs:workspace',JSON.stringify(state));}catch{}};
  shell.classList.add('workspace');
  const body=create('div','workspace-body');body.id='workspace-body';
  const editor=create('section','workspace-editor');editor.setAttribute('aria-label',title);
  const viewbar=create('div','workspace-viewbar','<span class="workspace-tab">'+title+'</span>');
  editor.append(viewbar,main);
  const left=createPanel('left',page.endsWith('search')?'絞り込み':'このページ');
  const right=createPanel('right','計算・表示');
  const separators=['left','right'].map(side=>{
    const separator=create('div','workspace-separator workspace-separator-'+side);
    separator.tabIndex=0;separator.setAttribute('role','separator');separator.setAttribute('aria-orientation','vertical');
    separator.setAttribute('aria-label',(side==='left'?'左':'右')+'パネルの幅');
    separator.setAttribute('aria-controls','workspace-'+side);
    return separator;
  });
  body.append(left.panel,separators[0],editor,separators[1],right.panel);shell.append(body);
  const bottom=create('details','workspace-bottom','<summary><span>情報</span><span id="workspace-status" role="status"></span><span id="workspace-version"></span></summary><div class="workspace-information"></div>');
  const information=bottom.querySelector('.workspace-information');shell.append(bottom);
  const controls=create('div','workspace-controls');
  for(const side of ['left','right','bottom']){
    const button=create('button','workspace-toggle',icon(side));button.type='button';button.dataset.workspaceToggle=side;
    button.setAttribute('aria-controls',side==='bottom'?'workspace-information':'workspace-'+side);
    controls.append(button);
    button.addEventListener('click',()=>{if(side==='bottom'){bottom.open=!bottom.open;}else{state[side]=!state[side];if(innerWidth<800&&state[side])state[side==='left'?'right':'left']=false;store();}apply();});
  }
  information.id='workspace-information';header.append(controls);
  const settingsGroup=create('div','workspace-settings');right.content.append(settingsGroup);

  // 要素は複製せず移動し、元WebのIDと状態をそのまま利用する。
  if(page==='unit-search'){
    main.classList.add('workspace-search');
    const form=move('#unit-search-form',left.content);
    // 形態・種類は検索側、Lv・時間・本能反映は計算側へ配置する。
    for(const id of ['unit-level','unit-time','unit-apply-talents'])moveLabel(id,settingsGroup);
    const calculation=move(element('unit-health-treasure')?.closest('details'),settingsGroup);if(calculation)calculation.hidden=true;
    const display=create('div','workspace-settings');right.content.append(sectionHeading('一覧の表示'),display);
    for(const id of ['unit-page-size','unit-show-properties'])moveLabel(id,display);
    associateForm(settingsGroup,form.id);
    const note=element('unit-search-calculation-note')?.closest('details');if(note)information.append(note);
    move('#unit-active-filters',information);
  }else if(page==='tunit-search'){
    main.classList.add('workspace-search');
    const form=move('#enemy-filters',left.content);
    const conditions=element('enemy-health')?.closest('fieldset');if(conditions)settingsGroup.append(conditions);
    const display=create('div','workspace-settings');right.content.append(sectionHeading('一覧の表示'),display);
    for(const id of ['enemy-page-size','enemy-show-properties'])moveLabel(id,display);
    associateForm(settingsGroup,form.id);
  }else if(page==='stage-search'){
    main.classList.add('workspace-search');
    move('#stage-filters',left.content);
    for(const id of ['stage-page-size','stage-show-enemies'])moveLabel(id,settingsGroup);
  }else if(page==='formation'){
    left.panel.querySelector('h2').textContent='キャラ一覧';
    right.panel.querySelector('h2').textContent='キャラ・城砲設定';
    move('.formation-library',left.content);move('#formation-member',right.content);move('#formation-profile',right.content);
    right.content.classList.add('formation-options');
  }else if(page==='stage-sortie'){
    move('#sortie-stage-navigation',left.content);move('#sortie-details',right.content);move('#battle-controls',viewbar);
    right.panel.querySelector('h2').textContent='ステージ詳細';
    let previous;
    document.addEventListener('kbcs:battle-mode',event=>{
      const active=event.detail;body.classList.toggle('workspace-battle',active);
      if(active){previous={left:state.left,right:state.right};state.left=false;state.right=false;}
      else if(previous){Object.assign(state,previous);previous=null;}
      left.panel.querySelector('h2').textContent=active?'シミュレーター':'このページ';
      right.panel.querySelector('h2').textContent=active?'シミュレーター':'ステージ詳細';
      for(const panel of [left.panel,right.panel]){const label=panel.querySelector('h2').textContent;panel.setAttribute('aria-label',label);panel.querySelector('.workspace-close').setAttribute('aria-label',label+'を閉じる');}
      viewbar.querySelector('.workspace-tab').textContent=active?'戦闘':'出撃準備';element('battle-controls').hidden=!active;for(const button of element('battle-controls').querySelectorAll('button'))button.disabled=active;viewbar.classList.toggle('battle-viewbar',active);
      apply();
    });
  }else if(page==='stage-detail'){
    move('#stage-navigation',left.content);
    move('#stage-detail-controls',settingsGroup);
    move('#stage-message',information);
  }else if(page==='unit-motion'||page==='enemy-motion'||page==='effect-motion'){
    left.panel.querySelector('h2').textContent='モーション';
    right.panel.querySelector('h2').textContent='パーツ詳細';
    move('#motion-explorer',left.content);move('#motion-inspector',right.content);
    move('#motion-message',information);
    main.classList.add('workspace-motion');
  }else if(page==='unit-detail'){
    move('#unit-form-tabs',left.content);
    const outline=create('nav','workspace-outline');outline.setAttribute('aria-label','キャラ詳細の項目');left.content.append(outline);
    for(const [id,label] of [['unit-growth-panel','成長'],['unit-form-comparison-panel','形態比較'],['unit-combo-section','にゃんコンボ'],['unit-team-builder','コンボ編成'],['unit-source-panel','元データ']])addOutline(outline,id,label);
    move('#unit-detail-settings',settingsGroup);
    const level=element('detail-level'),label=level.closest('label');
    const levelbar=create('div','workspace-levelbar','<span>Lv</span>');
    level.setAttribute('form','unit-detail-settings');levelbar.append(level);label.remove();
    viewbar.append(levelbar);
    const control=createLevelControl(level,'キャラLv');
    for(const [index,button] of [...level.closest('.db-level-control').querySelectorAll('button')].entries())button.textContent=['−10','−1','＋1','＋10'][index];
    levelbar.append(element('unit-summary'));
    level.addEventListener('kbcs:level-sync',()=>control.sync());
    new MutationObserver(()=>control.sync()).observe(level,{attributes:true,attributeFilter:['max','min','disabled']});
    move('#unit-capture-status',information);
  }else if(page==='tunit-detail'){
    const outline=create('nav','workspace-outline');outline.setAttribute('aria-label','敵詳細の項目');left.content.append(outline);
    addOutline(outline,'enemy-sheet-output','ステータス');addOutline(outline,'enemy-comparison','条件・比較');
    move('#enemy-content > .db-toolbar',settingsGroup);
    const conditions=element('enemy-condition-controls')?.closest('fieldset');if(conditions)settingsGroup.append(conditions);
    move('#enemy-capture-status',information);
  }
  for(const panel of [left.panel,right.panel]){const label=panel.querySelector('h2').textContent;panel.setAttribute('aria-label',label);panel.querySelector('.workspace-close').setAttribute('aria-label',label+'を閉じる');}
  const profileEditor=page.endsWith('-motion')||['formation','stage-play','stage-sortie','inventory'].includes(page)?null:createSimulationSettings(right.content);
  window.addEventListener('kbcs:open-simulation-settings',()=>{state.right=true;if(innerWidth<800)state.left=false;store();apply();profileEditor?.open();});
  if(!settingsGroup.childElementCount)settingsGroup.remove();
  if(!left.content.childElementCount){
    const outline=create('nav','workspace-outline');outline.setAttribute('aria-label','このページの項目');left.content.append(outline);
    for(const [index,target]of [...main.querySelectorAll('h1,h2,details>summary')].entries()){
      const anchor=target.tagName==='SUMMARY'?target.parentElement:target;
      if(!anchor.id)anchor.id='workspace-section-'+index;addOutline(outline,anchor.id,target.textContent);
    }
  }
  const displayButton=create('button','workspace-display-settings','表示設定');displayButton.type='button';displayButton.addEventListener('click',()=>openSiteSettings());right.content.append(displayButton);
  const available={left:true,right:true};

  function apply(){
    for(const [side,panel] of [['left',left.panel],['right',right.panel]]){
      const shown=available[side]&&state[side];panel.hidden=!shown;
      shell.style.setProperty('--workspace-'+side,shown?state[side+'Width']+'px':'0px');
      shell.style.setProperty('--workspace-'+side+'-handle',shown?'5px':'0px');
      const separator=separators[side==='left'?0:1];separator.hidden=!shown;
      separator.setAttribute('aria-valuemin','200');separator.setAttribute('aria-valuemax','440');separator.setAttribute('aria-valuenow',String(state[side+'Width']));
      const button=controls.querySelector('[data-workspace-toggle="'+side+'"]');button.disabled=!available[side];button.setAttribute('aria-expanded',String(shown));
      button.title=(side==='left'?'左パネル':'右パネル')+'を'+(shown?'閉じる':'開く');button.setAttribute('aria-label',button.title);
    }
    const button=controls.querySelector('[data-workspace-toggle="bottom"]');button.setAttribute('aria-expanded',String(bottom.open));button.title='情報パネルを'+(bottom.open?'閉じる':'開く');button.setAttribute('aria-label',button.title);
  }
  bottom.addEventListener('toggle',apply);
  for(const separator of separators){
    const side=separator.classList.contains('workspace-separator-left')?'left':'right';
    const resize=width=>{
      const other=side==='left'?'right':'left';
      const maximum=body.clientWidth-(state[other]&&available[other]?state[other+'Width']+5:0)-330;
      state[side+'Width']=Math.round(Math.max(200,Math.min(440,maximum,width)));apply();
    };
    separator.addEventListener('pointerdown',event=>{
      if(event.button!==0)return;
      const start=event.clientX,width=state[side+'Width'],scale=Number(getComputedStyle(shell).zoom)||1;
      separator.setPointerCapture(event.pointerId);
      const drag=event=>resize(width+(event.clientX-start)*(side==='left'?1:-1)/scale);
      const stop=()=>{separator.removeEventListener('pointermove',drag);store();};
      separator.addEventListener('pointermove',drag);separator.addEventListener('lostpointercapture',stop,{once:true});
    });
    separator.addEventListener('keydown',event=>{if(!['ArrowLeft','ArrowRight'].includes(event.key))return;event.preventDefault();resize(state[side+'Width']+(event.key==='ArrowRight'?10:-10)*(side==='left'?1:-1));store();});
  }
  const updateStatus=()=>{
    const count=element('unit-result-count')||element('enemy-count')||element('unit-summary')||element('stage-count')||element('stage-visible-count')||element('data-state');
    const version=element('unit-data-version')||element('unit-detail-version')||element('enemy-version')||element('stage-version');
    element('workspace-status').textContent=count?.textContent||document.title.replace(/ \| KBCS?$/,'');
    element('workspace-version').textContent=version?.textContent||'';
    const ready=page==='unit-search'?!element('unit-export').disabled:page==='tunit-search'?!element('enemy-filters').hidden:page==='unit-detail'?!element('unit-detail-content').hidden:page==='tunit-detail'?!element('enemy-content').hidden:true;
    left.content.inert=!ready;right.content.inert=!ready;
    const current=page.endsWith('detail')?document.title.replace(/ \| KBCS?$/,''):title;
    viewbar.firstElementChild.textContent=current;
  };
  const observer=new MutationObserver(updateStatus);
  for(const id of ['unit-result-count','unit-data-version','unit-detail-version','unit-summary','enemy-count','enemy-version','stage-count','stage-visible-count','stage-version','data-state','unit-export','enemy-filters','unit-detail-content','enemy-content']){
    const node=element(id);if(node)observer.observe(node,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['hidden','disabled']});
  }
  observer.observe(document.querySelector('title'),{childList:true});updateStatus();apply();
}

function createPanel(side,title){
  const panel=create('aside','workspace-panel workspace-'+side);panel.id='workspace-'+side;panel.setAttribute('aria-label',title);
  const heading=create('div','workspace-panel-heading','<h2>'+title+'</h2>');
  const close=create('button','workspace-close',icon('close'));close.type='button';close.setAttribute('aria-label',title+'を閉じる');
  close.addEventListener('click',()=>document.querySelector('[data-workspace-toggle="'+side+'"]').click());
  heading.append(close);const content=create('div','workspace-panel-content');panel.append(heading,content);
  return {panel,content};
}
function moveLabel(id,target){const label=element(id)?.closest('label');if(label)target.append(label);}
function associateForm(container,id){for(const control of container.querySelectorAll('input,select,textarea'))control.setAttribute('form',id);}
function sectionHeading(title){return create('h3','workspace-section-heading',title);}
function addOutline(container,id,label){
  const target=element(id);if(!target)return;
  const link=create('a','',label);link.href='#'+id;
  if(target.hidden){link.hidden=true;new MutationObserver(()=>{link.hidden=target.hidden;}).observe(target,{attributes:true,attributeFilter:['hidden']});}
  link.addEventListener('click',()=>{if(target.tagName==='DETAILS')target.open=true;});container.append(link);
}
