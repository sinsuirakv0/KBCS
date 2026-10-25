import {readEnemySettings,writeEnemySettings} from '/native-enemy-statistics.js';
import {calculateEnemyStats,prepareEnemyStatistics} from '/native-enemy-statistics.js';
import {readPageParams,writePageParams,clearPageParams,bindDetailNavigation} from "/native-state.js";
import {loadEnemyDatabase} from '../../shared/game/enemies.js';
import {defaultEnemySettings} from '../../shared/game/enemy-stats.js';
import {escapeHtml} from '../../shared/game/database-view.js';
import {saveElementImage} from '../../shared/browser/capture.js';
import {matchesEnemyQuery} from './model.js';
import {enemySheetHtml,enemyConditionControls,enemyComparisonHtml,enemyRadarHtml} from './view.js';
import {readGameSettings,initializeGameSettings} from '../../shared/browser/game-settings.js';
import {compactState} from '../../shared/game/share-state.js';

const element=id=>document.getElementById(id),params=readPageParams("enemy-detail");
let database,enemy,peer,settings=readEnemySettings(params,readGameSettings()),same=params.get('same')!=='false'&&settings.health===settings.attack;
let comparison={enabled:false,id:null,same:true,settings:readEnemySettings(new URLSearchParams(),readGameSettings())};
try {
  const value=JSON.parse(params.get('compare')||'null');
  if(value&&Number.isInteger(value.id)&&value.id>=0)comparison={enabled:value.enabled!==false,id:value.id,same:value.same!==false,settings:readEnemySettings(new URLSearchParams(value.settings||{}),readGameSettings())};
}catch{}

function selectTab(tab) {
  for(const name of ['settings','results']) {
    element('enemy-tab-'+name).setAttribute('aria-selected',name===tab?'true':'false');
    element(name==='settings'?'enemy-settings':'enemy-comparison-results').hidden=name!==tab;
  }
}
function saveState() {
  const query=writeEnemySettings(new URLSearchParams({id:String(enemy.id)}),settings);
  if(!same)query.set('same','false');
  if(comparison.enabled&&comparison.id!=null) {
    const peer=compactState({id:comparison.id,same:comparison.same},{same:true});
    if(!comparison.same)peer.settings=compactState(comparison.settings,defaultEnemySettings);
    query.set('compare',JSON.stringify(peer));
  }
  writePageParams("enemy-detail",query);
}
function renderPeerOptions() {
  const query=element('enemy-compare-query').value;
  const candidates=database.enemies.filter(item=>matchesEnemyQuery(item,query)||item.id===comparison.id);
  element('enemy-compare-id').innerHTML='<option value="">敵を選択</option>'+candidates.map(item=>'<option value="'+item.id+'"'+(item.id===comparison.id?' selected':'')+'>'+item.id+' '+escapeHtml(item.name)+'</option>').join('');
}
function renderPeerControls() {
  peer=database.enemies.find(item=>item.id===comparison.id);
  element('enemy-peer-condition-controls').innerHTML=peer?enemyConditionControls(peer,comparison.settings,'enemy-peer-'):'';
  for(const key of ['health','attack'])element('enemy-compare-'+key).value=comparison.settings[key];
}
function readConditions(container,target) {
  for(const input of container.querySelectorAll('[data-enemy-condition]')) {
    const key=input.dataset.enemyCondition;
    target[key]=input.type==='checkbox'?input.checked:Math.max(Number(input.min),Math.min(Number(input.max),Number(input.value)||0));
  }
}
function renderResults() {
  const stats=calculateEnemyStats(enemy,settings),entries=[{enemy,settings,stats}];
  if(comparison.enabled&&peer) {
    const options={...(comparison.same?settings:comparison.settings),seconds:settings.seconds};
    entries.push({enemy:peer,settings:options,stats:calculateEnemyStats(peer,options)});
  }
  element('enemy-comparison-output').innerHTML='<p>'+entries.map(({enemy},index)=>'<span style="color:var(--color-'+(index?'accent':'primary')+')">'+escapeHtml(enemy.name)+'</span>').join(' / ')+'</p>'+enemyRadarHtml(entries)+enemyComparisonHtml(database,entries,settings.seconds)+'<p class="db-meta">DPSは通常攻撃の合計を使用。波動・烈波・毒撃などの追加ダメージは含みません。</p>';
}
let revision=0;
async function render() {
  const current=++revision;try{await prepareEnemyStatistics([{enemy,settings},...(comparison.enabled&&peer?[{enemy:peer,settings:comparison.same?settings:comparison.settings}]:[])]);if(current!==revision)return;}catch(error){if(current===revision)element('enemy-sheet-output').textContent=error.message;return;}
  element('enemy-sheet-output').innerHTML=enemySheetHtml(database,enemy,calculateEnemyStats(enemy,settings),settings);
  element('enemy-compare-controls').hidden=!comparison.enabled;element('enemy-compare-conditions').hidden=comparison.same;
  renderResults();saveState();
}
function update(event) {
  const target=event?.target;
  same=element('enemy-same').checked;
  const bound=id=>Math.max(0,Math.min(1000000,Number(element(id).value)||0));
  settings.health=bound('enemy-health');settings.attack=bound('enemy-attack');
  if(same&&target?.id==='enemy-health') {settings.attack=settings.health;element('enemy-attack').value=settings.attack;}
  else if(same) {settings.health=settings.attack;element('enemy-health').value=settings.health;}
  settings.seconds=element('enemy-time').value==='seconds';
  readConditions(element('enemy-condition-controls'),settings);
  comparison.enabled=element('enemy-compare-enabled').checked;comparison.same=element('enemy-compare-same').checked;
  for(const key of ['health','attack'])comparison.settings[key]=bound('enemy-compare-'+key);
  readConditions(element('enemy-peer-condition-controls'),comparison.settings);
  render();
}
function initialize() {
  const id=params.get('id')??'0';
  if(!/^\d+$/.test(id))throw Error('敵IDを確認してください。');
  enemy=database.enemies.find(item=>item.id===Number(id));
  if(!enemy)throw Error('ID '+id+'の敵は収録されていません。');
  if(comparison.id!=null&&!database.enemies.some(item=>item.id===comparison.id))comparison={...comparison,id:null,enabled:false};
  element('enemy-title').textContent=enemy.name+' 敵詳細';document.title=enemy.name+' | KBC';
  element('enemy-version').textContent='JP データv'+database.gameVersion;
  for(const key of ['health','attack'])element('enemy-'+key).value=settings[key];
  element('enemy-time').value=settings.seconds?'seconds':'frames';element('enemy-same').checked=same;
  element('enemy-compare-enabled').checked=comparison.enabled;element('enemy-compare-same').checked=comparison.same;
  element('enemy-condition-controls').innerHTML=enemyConditionControls(enemy,settings,'enemy-current-');
  renderPeerOptions();renderPeerControls();
  element('enemy-status').hidden=true;element('enemy-content').hidden=false;render();
}
initializeGameSettings(element('enemy-version').parentElement,()=>settings,values=>{
  Object.assign(settings,readEnemySettings(new URLSearchParams(),{...settings,...values}));
  if(!enemy)return;
  element('enemy-time').value=settings.seconds?'seconds':'frames';
  element('enemy-condition-controls').innerHTML=enemyConditionControls(enemy,settings,'enemy-current-');render();
});
let inputTimer;
element('workspace-body').addEventListener('input',event=>{
  if(event.target.id==='enemy-compare-query'||event.target.closest('.simulation-settings'))return;
  clearTimeout(inputTimer);inputTimer=setTimeout(()=>update(event),150);
});
element('workspace-body').addEventListener('change',event=>{
  if(event.target.id==='enemy-compare-query'||event.target.closest('.simulation-settings'))return;
  clearTimeout(inputTimer);
  if(event.target.id==='enemy-compare-id') {
    comparison.id=event.target.value===''?null:Number(event.target.value);renderPeerControls();
  }
  update(event);
});
element('enemy-compare-query').addEventListener('input',renderPeerOptions);
for(const name of ['settings','results'])element('enemy-tab-'+name).addEventListener('click',()=>selectTab(name));
element('workspace-body').addEventListener('click',async event=>{
  const tab=event.target.closest('[data-enemy-tab]');if(tab)selectTab(tab.dataset.enemyTab);
  const button=event.target.closest('[data-capture]');if(!button)return;
  button.disabled=true;const status=element('enemy-capture-status');status.textContent='画像を作成しています。';
  try{await saveElementImage(element(button.dataset.capture),'KBC-enemy-'+enemy.id+'-'+(button.dataset.capture==='enemy-sheet-output'?'detail':'compare'));status.textContent='画像を保存しました。';}catch(error){status.textContent=error.message;}finally{button.disabled=false;}
});
document.addEventListener('error',event=>{if(event.target.matches?.('[data-enemy-image]')){event.target.hidden=true;event.target.parentElement.title='画像未収録';}},true);
async function load(){element('enemy-retry').hidden=true;try{database=await loadEnemyDatabase();initialize();}catch(error){element('enemy-status').textContent=error.message;element('enemy-status').hidden=false;element('enemy-retry').hidden=false;}}
element('enemy-retry').addEventListener('click',load);load();

bindDetailNavigation('enemy-detail','/pages/tunit-detail/',target=>writeEnemySettings(new URLSearchParams(),!comparison.same&&Number(target.searchParams.get('id'))===comparison.id?comparison.settings:settings));

window.addEventListener('kbcs:simulation-change',event=>{Object.assign(settings,event.detail);Object.assign(comparison.settings,event.detail);if(enemy){element('enemy-condition-controls').innerHTML=enemyConditionControls(enemy,settings,'enemy-current-');renderPeerControls();render();}});
