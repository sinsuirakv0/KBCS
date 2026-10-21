import {readPageParams,writePageParams,clearPageParams,bindDetailNavigation} from "/native-state.js";
import {loadEnemyDatabase} from '../../shared/game/enemies.js';
import {readEnemySettings,writeEnemySettings,enemyDetailUrl} from '../../shared/game/enemy-stats.js';
import {escapeHtml,formatNumber,formatTime,iconChoiceHtml,bindIconHints} from '../../shared/game/database-view.js';
import {rangeFields,selectEnemyRows} from './model.js';
import {enemyImageHtml,enemyAttributesHtml,enemyAbilitiesHtml} from './view.js';
import {readGameSettings,initializeGameSettings} from '../../shared/browser/game-settings.js';
import {createPagination} from '../../shared/browser/pagination.js';
const element=id=>document.getElementById(id),params=readPageParams("enemy-search");
const state={...readEnemySettings(params,readGameSettings()),query:params.get('q')||'',attributes:(params.get('attributes')||'').split(',').filter(Boolean),abilities:(params.get('abilities')||'').split(',').filter(Boolean),attributeMode:params.get('attributeMode')==='all'?'all':'any',abilityMode:params.get('abilityMode')==='any'?'any':'all',attackType:['単体','範囲'].includes(params.get('attackType'))?params.get('attackType'):'',negate:params.get('negate')==='true',ranges:Object.fromEntries(rangeFields.map(([key])=>[key,[params.get(key+'Min')||'',params.get(key+'Max')||'']])),sort:['id','name',...rangeFields.map(([key])=>key)].includes(params.get('sort'))?params.get('sort'):'id',direction:params.get('direction')==='desc'?'desc':'asc'};
let database,rows=[],page=1;
const pagination=createPagination(element('enemy-prev').parentElement,value=>{page=value;renderRows();});
const columns=[['id','ID'],['icon',''],['name','名前'],['attributes','属性・種族'],['abilities','特性'],['hp','体力'],['attack','攻撃力'],['dps','DPS'],['range','射程'],['knockbacks','KB'],['speed','速度'],['drop','お金'],['attackCycle','攻撃頻度'],['foreswing','攻撃発生']];
function saveState() {
  const query=writeEnemySettings(new URLSearchParams(),state);
  if(state.query)query.set('q',state.query);
  for(const key of ['attributes','abilities'])if(state[key].length)query.set(key,state[key].join(','));
  for(const [key,fallback] of [['attributeMode','any'],['abilityMode','all'],['sort','id'],['direction','asc']])if(state[key]!==fallback)query.set(key,state[key]);
  for(const key of ['attackType','negate'])if(state[key])query.set(key,state[key]);
  for(const [key,bounds] of Object.entries(state.ranges))for(const [index,name] of ['Min','Max'].entries())if(bounds[index]!=='')query.set(key+name,bounds[index]);
  writePageParams("enemy-search",query);
}
function renderRows() {
  const size=Number(element('enemy-page-size').value),pages=Math.max(1,Math.ceil(rows.length/size));page=Math.min(page,pages);
  element('enemy-count').textContent=rows.length+'体';element('enemy-empty').hidden=!!rows.length;
  pagination.update(page,pages);
  element('enemy-table').querySelector('thead').innerHTML='<tr>'+columns.map(([key,label])=>'<th'+(key==='attributes'?' class="enemy-attributes-column"':key==='abilities'?' class="unit-properties-column"':'')+(key===state.sort?' aria-sort="'+(state.direction==='asc'?'ascending':'descending')+'"':'')+'>'+(['icon','attributes','abilities'].includes(key)?label:'<button type="button" data-sort="'+key+'">'+label+(key===state.sort?(state.direction==='asc'?' ▲':' ▼'):'')+'</button>')+'</th>').join('')+'</tr>';
  element('enemy-table').querySelector('tbody').innerHTML=rows.slice((page-1)*size,page*size).map(({enemy,stats})=>{
    const url=escapeHtml(enemyDetailUrl(enemy,state));
    return '<tr><td>'+enemy.id+'</td><td class="db-icon"><a href="'+url+'" aria-label="'+escapeHtml(enemy.name)+'の詳細">'+enemyImageHtml(database,enemy)+'</a></td><td class="db-name"><a href="'+url+'">'+escapeHtml(enemy.name)+'</a></td><td class="enemy-attributes-column"><div class="enemy-properties">'+enemyAttributesHtml(database,enemy)+'</div></td><td class="unit-properties-column"><div class="enemy-properties">'+enemyAbilitiesHtml(database,enemy,state,stats,true)+'</div></td>'+columns.slice(5).map(([key])=>'<td>'+(['attackCycle','foreswing'].includes(key)?formatTime(stats[key],state.seconds):formatNumber(stats[key]))+'</td>').join('')+'</tr>';
  }).join('');
}
function readControls() {
  const checked=id=>[...element(id).querySelectorAll('input:checked')].map(input=>input.value);
  state.query=element('enemy-query').value;state.attributes=[...checked('enemy-attributes'),...checked('enemy-species')];
  state.abilities=checked('enemy-abilities');state.attributeMode=element('enemy-attribute-mode').querySelector('input:checked').value;state.abilityMode=element('enemy-ability-mode').querySelector('input:checked').value;
  state.attackType=element('enemy-attack-type').value;state.negate=element('enemy-negate').checked;
  for(const [key,max] of [['health',1000000],['attack',1000000],['alien',600],['starred',1500]])state[key]=Math.max(0,Math.min(max,Number(element('enemy-'+key).value)||0));
  state.seconds=element('enemy-time').value==='seconds';
  for(const [key] of rangeFields)state.ranges[key]=['min','max'].map(direction=>element('enemy-'+key+'-'+direction).value);
}
function update(){readControls();page=1;rows=selectEnemyRows(database,state);saveState();renderRows();}
function initialize() {
  const chips=options=>options.map(({key,label})=>iconChoiceHtml(database,{key,label,checked:(state.attributes.includes(key)||state.abilities.includes(key))})).join('');
  state.attributes=state.attributes.filter(key=>[...database.attributes,...database.species].some(item=>item.key===key));state.abilities=state.abilities.filter(key=>database.abilities.some(item=>item.key===key));
  element('enemy-attributes').innerHTML=chips(database.attributes);element('enemy-species').innerHTML=chips(database.species);
  const groups=[['効果',['knockback','stop','slow','weaken','curse','warp','toxic','dodge','delay']],['攻撃',['long-range','omni','multi-hit']],['無効',database.abilities.filter(item=>item.key.endsWith('-immune')).map(item=>item.key)]];
  const grouped=new Set(groups.flatMap(([,keys])=>keys));groups.push(['能力',database.abilities.filter(item=>!grouped.has(item.key)).map(item=>item.key)]);
  element('enemy-abilities').innerHTML=groups.map(([label,keys])=>'<div class="unit-filter-row"><span class="unit-filter-label">'+label+'</span><fieldset class="db-filter-group" aria-label="'+label+'">'+chips(database.abilities.filter(item=>keys.includes(item.key)))+'</fieldset></div>').join('');
  element('enemy-ranges').innerHTML=rangeFields.map(([key,label])=>'<div class="unit-range"><span>'+label+'</span><input id="enemy-'+key+'-min" type="number" min="0" step="any" aria-label="'+label+'の下限"><span>〜</span><input id="enemy-'+key+'-max" type="number" min="0" step="any" aria-label="'+label+'の上限"></div>').join('');
  for(const [id,value] of [['query',state.query],['attack-type',state.attackType],['health',state.health],['attack',state.attack],['alien',state.alien],['starred',state.starred],['time',state.seconds?'seconds':'frames']])element('enemy-'+id).value=value;
  element('enemy-negate').checked=state.negate;
  for(const [id,key] of [['attribute-mode','attributeMode'],['ability-mode','abilityMode']])for(const input of element('enemy-'+id).querySelectorAll('input'))input.checked=input.value===state[key];
  for(const [key,bounds] of Object.entries(state.ranges))for(const [index,direction] of ['min','max'].entries())element('enemy-'+key+'-'+direction).value=bounds[index];
  element('enemy-version').textContent='JP データv'+database.gameVersion;element('enemy-status').hidden=true;element('enemy-filters').hidden=false;element('enemy-results').hidden=false;
  bindIconHints(element('enemy-filters'),element('enemy-filter-hint'));update();
}
initializeGameSettings(element('enemy-query').parentElement,()=>state,values=>{
  Object.assign(state,readEnemySettings(new URLSearchParams(),{...state,...values}));
  for(const key of ['alien','starred'])element('enemy-'+key).value=state[key];
  element('enemy-page-size').value=values.pageSize;element('enemy-time').value=state.seconds?'seconds':'frames';
  if(database)update();
});
element('enemy-filters').addEventListener('submit',event=>event.preventDefault());
document.addEventListener('input',event=>{if(event.target.form===element('enemy-filters'))update();});
document.addEventListener('change',event=>{if(event.target.form===element('enemy-filters'))update();});
element('enemy-reset').addEventListener('click',()=>{clearPageParams('enemy-search');location.href='/pages/tunit-search/';});
element('enemy-page-size').value=readGameSettings().pageSize;
element('enemy-page-size').addEventListener('change',()=>{page=1;renderRows();});
element('enemy-show-properties').addEventListener('change',event=>element('enemy-table-wrap').classList.toggle('hide-properties',!event.target.checked));
element('enemy-table').addEventListener('click',event=>{const button=event.target.closest('[data-sort]');if(!button)return;state.direction=state.sort===button.dataset.sort&&state.direction==='asc'?'desc':'asc';state.sort=button.dataset.sort;update();});
document.addEventListener('error',event=>{if(event.target.matches?.('[data-enemy-image]')){event.target.hidden=true;event.target.parentElement.title='画像未収録';}},true);
async function load(){element('enemy-retry').hidden=true;try{database=await loadEnemyDatabase();initialize();}catch(error){element('enemy-status').textContent=error.message;element('enemy-retry').hidden=false;}}
element('enemy-retry').addEventListener('click',load);load();

bindDetailNavigation('enemy-detail','/pages/tunit-detail/',()=>writeEnemySettings(new URLSearchParams(),state));

window.addEventListener('kbcs:simulation-change',event=>{Object.assign(state,event.detail);for(const key of ['alien','starred'])element('enemy-'+key).value=state[key];if(database)update();});
