import {readPageParams,writePageParams,clearPageParams,bindDetailNavigation} from "/native-state.js";
import {loadStageDatabase} from '../../shared/game/stages.js';
import {loadEnemyDatabase} from '../../shared/game/enemies.js';
import {enemyImageHtml} from '../../shared/game/enemy-view.js';
import {escapeHtml,formatNumber,iconChoiceHtml,bindIconHints} from '../../shared/game/database-view.js';
import {enemyDetailUrl} from '../../shared/game/enemy-stats.js';
import {readGameSettings,initializeGameSettings} from '../../shared/browser/game-settings.js';
import {initializeRewardPicker} from './rewards.js';
import {createPagination} from '../../shared/browser/pagination.js';
import {stageGimmicks,stageRanges,selectStageMaps,stageMapUrl,selectStageSeries} from './model.js';

const element=id=>document.getElementById(id),params=readPageParams("stage-search"),defaults=readGameSettings();
const selectionMode=params.get('play')==='1';
if(selectionMode){document.title='既存ステージを選択 | KBCS';const tab=document.querySelector('.workspace-tab');if(tab)tab.textContent='既存ステージを選択';}
const state={crown:Math.max(0,Math.min(4,Number(params.get("crown"))||0)),...Object.fromEntries(['query','series','enemy','reward','background','music'].map(key=>[key,params.get(key==='query'?'q':key)||''])),attributes:(params.get('attributes')||'').split(',').filter(Boolean),gimmicks:(params.get('gimmicks')||'').split(',').filter(Boolean),enemyMode:params.get('enemyMode')==='any'?'any':'all',attributeMode:params.get('attributeMode')==='all'?'all':'any',excludeEnemies:params.get('excludeEnemies')==='true',attributesOnly:params.get('attributesOnly')==='true',ranges:Object.fromEntries(stageRanges.map(([key])=>[key,[params.get(key+'Min')||'',params.get(key+'Max')||'']])),sort:['id','name','map','count',...stageRanges.map(([key])=>key)].includes(params.get('sort'))?params.get('sort'):'id',direction:params.get('direction')==='desc'?'desc':'asc'};
let database,enemyDatabase,rows=[],page=Math.max(1,Math.trunc(Number(params.get('page')))||1);
const pagination=[element('stage-pagination-top'),element('stage-pagination')].map(root=>createPagination(root,value=>{page=value;render();saveState();}));
const labels=new Map(stageGimmicks),columns=[['id','ID'],['name','マップ'],['count','ステージ数'],['enemies','出現する敵'],['energy','統率力'],['difficulty','難易度'],['flags','ギミック']];

function saveState(){
  const query=new URLSearchParams();
  for(const key of ['query','series','enemy','reward','background','music'])if(state[key])query.set(key==='query'?'q':key,state[key]);
  for(const key of ['attributes','gimmicks'])if(state[key].length)query.set(key,state[key].join(','));
  for(const [key,fallback]of [['enemyMode','all'],['attributeMode','any'],['sort','id'],['direction','asc']])if(state[key]!==fallback)query.set(key,state[key]);
  for(const key of ['excludeEnemies','attributesOnly'])if(state[key])query.set(key,'true');
  for(const [key,bounds]of Object.entries(state.ranges))for(const [index,suffix]of ['Min','Max'].entries())if(bounds[index]!=='')query.set(key+suffix,bounds[index]);
  if(page>1)query.set('page',page);query.set('size',element('stage-page-size').value);query.set('showEnemies',String(element('stage-show-enemies').checked));
  if(state.crown)query.set('crown',state.crown);
  writePageParams("stage-search",query);
}
function render(){
  const size=Number(element('stage-page-size').value),pages=Math.max(1,Math.ceil(rows.length/size));page=Math.min(page,pages);
  for(const item of pagination)item.update(page,pages);
  element('stage-count').textContent=rows.length.toLocaleString('ja-JP')+'マップ / '+rows.reduce((count,entry)=>count+entry.stages.length,0)+'ステージ';element('stage-empty').hidden=!!rows.length;
  element('stage-table').querySelector('thead').innerHTML='<tr>'+columns.map(([key,label])=>'<th'+(key==='enemies'?' class="stage-enemies-column"':'')+(key===state.sort?' aria-sort="'+(state.direction==='asc'?'ascending':'descending')+'"':'')+'>'+(['enemies','flags'].includes(key)?label:'<button type="button" data-sort="'+key+'">'+label+(state.sort===key?(state.direction==='asc'?' ▲':' ▼'):'')+'</button>')+'</th>').join('')+'</tr>';
  element('stage-table').querySelector('tbody').innerHTML=rows.slice((page-1)*size,page*size).map(entry=>{
    const {map,stages,enemies,flags}=entry,url=stageMapUrl(map,state.crown||1).replace('/stage-detail/',selectionMode?'/stage-sortie/':'/stage-detail/');
    const icons=enemies.slice(0,12).map(id=>{const enemy=enemyDatabase.enemies[id];return enemy?'<a href="'+escapeHtml(enemyDetailUrl(enemy))+'" title="'+escapeHtml(enemy.name)+'（ID '+id+'）" aria-label="'+escapeHtml(enemy.name)+'の詳細">'+enemyImageHtml(enemyDatabase,enemy,24)+'</a>':'<span title="敵ID '+id+'">#'+id+'</span>';}).join('');
    const range=(values,star=false)=>values.length?[...new Set(values)].map(value=>star?'★'+value:formatNumber(value)).join('〜'):'—';
    return '<tr><td title="ゲーム内マップID '+map.nativeId+'">'+map.nativeId+'<small class="db-meta">'+map.key+'</small></td><td class="stage-names"><a href="'+url+'">'+escapeHtml(map.name)+'</a></td><td title="条件に一致したステージ / マップ内の全ステージ">'+(stages.length===map.stages.length?stages.length:stages.length+' / '+map.stages.length)+'</td><td class="stage-enemies-column"><div class="stage-enemy-icons">'+icons+(enemies.length>12?'<a href="'+url+'">+'+(enemies.length-12)+'</a>':'')+'</div></td><td>'+range(entry.energy)+'</td><td>'+range(entry.difficulty,true)+'</td><td class="stage-tags">'+flags.map(key=>'<span>'+labels.get(key)+'</span>').join('')+'</td></tr>';
  }).join('');
}
function readControls(){
  state.crown=Number(element('stage-crown-filter').value);
  for(const key of ['query','series','enemy','reward','background','music'])state[key]=element('stage-'+key).value;
  for(const key of ['attributes','gimmicks'])state[key]=[...element('stage-'+key).querySelectorAll('input:checked')].map(input=>input.value);
  for(const [id,key]of [['enemy-mode','enemyMode'],['attribute-mode','attributeMode']])state[key]=element('stage-'+id).querySelector('input:checked').value;
  for(const [id,key]of [['exclude-enemies','excludeEnemies'],['attributes-only','attributesOnly']])state[key]=element('stage-'+id).checked;
  for(const [key]of stageRanges)state.ranges[key]=['min','max'].map(suffix=>element('stage-'+key+'-'+suffix).value);
}
function update(commit=true){readControls();page=1;rows=selectStageMaps(database,enemyDatabase,state);render();if(commit)saveState();}
function initialize(){
  element('stage-crown-filter').value=state.crown;
  element('stage-series').innerHTML='<option value="">すべて</option>'+selectStageSeries(database).map(series=>'<option value="'+series.id+'">'+escapeHtml(series.id+' '+series.label)+'</option>').join('');
  state.series=database.series.some(series=>series.id===state.series)?state.series:'';
  const attributes=[...enemyDatabase.attributes,...enemyDatabase.species];
  state.attributes=state.attributes.filter(key=>attributes.some(item=>item.key===key));state.gimmicks=state.gimmicks.filter(key=>labels.has(key));
  element('stage-attributes').innerHTML=attributes.map(item=>iconChoiceHtml(enemyDatabase,{...item,checked:state.attributes.includes(item.key)})).join('');
  element('stage-gimmicks').innerHTML=stageGimmicks.filter(([key])=>database.stages.some(stage=>stage.flags.includes(key))).map(([key,label])=>'<label class="db-chip"><input type="checkbox" value="'+key+'"'+(state.gimmicks.includes(key)?' checked':'')+'><span>'+label+'</span></label>').join('');
  element('stage-enemy-options').innerHTML=enemyDatabase.enemies.map(enemy=>'<option value="'+escapeHtml(enemy.name)+'">ID '+enemy.id+'</option>').join('');
  element('stage-ranges').innerHTML=stageRanges.map(([key,label])=>'<label>'+label+'<input id="stage-'+key+'-min" type="number" min="0" step="any" aria-label="'+label+'の下限"><span>〜</span><input id="stage-'+key+'-max" type="number" min="0" step="any" aria-label="'+label+'の上限"></label>').join('');
  for(const key of ['query','series','enemy','reward','background','music'])element('stage-'+key).value=state[key];
  for(const [id,key]of [['enemy-mode','enemyMode'],['attribute-mode','attributeMode']])for(const input of element('stage-'+id).querySelectorAll('input'))input.checked=input.value===state[key];
  for(const [id,key]of [['exclude-enemies','excludeEnemies'],['attributes-only','attributesOnly']])element('stage-'+id).checked=state[key];
  for(const [key,bounds]of Object.entries(state.ranges))for(const [index,suffix]of ['min','max'].entries())element('stage-'+key+'-'+suffix).value=bounds[index];
  if(state.gimmicks.length||state.reward||state.background||state.music||state.excludeEnemies||state.attributesOnly||Object.values(state.ranges).some(values=>values.some(value=>value!=='')))element('stage-filters').querySelector('details').open=true;
  initializeRewardPicker(element('stage-reward-picker'),database);
  bindIconHints(element('stage-filters'),element('stage-icon-hint'));
  element('stage-version').textContent='JP データv'+database.gameVersion;element('stage-status').hidden=true;element('stage-filters').hidden=false;element('stage-results').hidden=false;
  rows=selectStageMaps(database,enemyDatabase,state);render();saveState();
}
initializeGameSettings(element('stage-version').parentElement,()=>defaults,values=>{Object.assign(defaults,values);element('stage-page-size').value=values.pageSize;if(database){page=1;render();saveState();}});
element('stage-page-size').value=[25,50,100].includes(Number(params.get('size')))?params.get('size'):defaults.pageSize;
element('stage-page-size').addEventListener('change',()=>{page=1;render();saveState();});
element('stage-show-enemies').checked=params.get('showEnemies')==='true';element('stage-table').classList.toggle('hide-stage-enemies',!element('stage-show-enemies').checked);
element('stage-show-enemies').addEventListener('change',event=>{element('stage-table').classList.toggle('hide-stage-enemies',!event.target.checked);saveState();});
element('stage-filters').addEventListener('submit',event=>{event.preventDefault();if(database)saveState();});
element('stage-filters').addEventListener('input',event=>{if(database)update(!event.target.matches('input[type=search],input[type=text],input[type=number]'));});
element('stage-filters').addEventListener('change',()=>{if(database)saveState();});
element('stage-filters').addEventListener('keyup',event=>{if(event.key==='Enter'&&!event.isComposing&&event.target.matches('input[type=search],input[type=text],input[type=number]')&&database)saveState();});
element('stage-reset').addEventListener('click',()=>{clearPageParams('stage-search');location.href='/pages/stage-search/'+(selectionMode?'?play=1':'');});
element('stage-table').addEventListener('click',event=>{const button=event.target.closest('[data-sort]');if(!button)return;state.direction=state.sort===button.dataset.sort&&state.direction==='asc'?'desc':'asc';state.sort=button.dataset.sort;update();});
async function load(){element('stage-retry').hidden=true;try{[database,enemyDatabase]=await Promise.all([loadStageDatabase(),loadEnemyDatabase()]);initialize();}catch(error){element('stage-status').textContent=error.message;element('stage-status').hidden=false;element('stage-retry').hidden=false;}}
element('stage-retry').addEventListener('click',load);load();
