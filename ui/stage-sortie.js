import {loadStageDatabase,loadStageVariant} from './src/shared/game/stages.js';
import {loadEnemyDatabase} from './src/shared/game/enemies.js';
import {loadUnitDatabase} from './src/shared/game/units.js';
import {enemyImageHtml} from './src/shared/game/enemy-view.js';
import {escapeHtml as esc,formatNumber,formatTime} from './src/shared/game/database-view.js';
import {resolveStageRoute,applicableLimits} from './src/features/stages/model.js';
import {loadStageScene,stageMediaHtml,initializeStageMedia} from './src/features/stages/native-media.js';
import {prepareBattleScreen,startBattleScreen} from './battle-screen.js';
import {formationIconHtml} from './formation-view.js';
import {formationDisplayName} from './formation-model.js';
import {stageRulesHtml,stageFormationHtml} from './src/features/stages/view.js';
import {battleItems,readBattleJson,battleFormation,castleHealth,prepareBattleAssets,effectiveStageLimit,stageDeployment,deploymentReason} from './battle-support.js';

const node=id=>document.getElementById('sortie-'+id),route=new URLSearchParams(location.search);
let artwork,deployment,deployVersion=0,battle;
let database,enemies,units,map,stages=[],stage,entry,health,choiceVersion=0,controller,loadedAssets,prepared;
let saved={};try{saved=JSON.parse(sessionStorage.getItem('kbcs:sortie')||'{}');}catch{}
let crown=Math.max(1,Number(route.get('crown'))||1),items={...saved.items},speed=saved.speed===2?2:3;
const known=new Map();
const stageMedia=initializeStageMedia(node('media'),id=>stages.find(value=>value.id===id));
function status(message,error=false){node('message').textContent=message;node('message').classList.toggle('sortie-status-error',error);}
function store(){try{sessionStorage.setItem('kbcs:sortie',JSON.stringify({formation:entry?.id,items,speed}));}catch{}}
function ready(){node('launch').disabled=!!controller||!entry||!health||!deployment||!stage||!!(stage.variants?.length&&!stage.patternSource)||!(stage.width>0)||stage.background==null;}
function drawFormation(){
  if(!entry){node('formation-preview').innerHTML='<a href="/pages/formation/">編成を作成</a>';return;}
  const document=battleFormation(units,entry.document);
  node('formation-edit').href='/pages/formation/?'+new URLSearchParams({id:entry.id,map:map.key,stage:stage.index,crown});
  node('formation-preview').innerHTML=document.slots.map((member,index)=>{
    const form=member&&known.get(member.unitId)?.forms.find(form=>form.index===member.form);
    return form?formationIconHtml(units,form,artwork,deploymentReason(deployment?.slots[index].reasons||0)):'<span class="sortie-slot-empty">'+(index+1)+'</span>';
  }).join('');
}
async function refreshDeployment(){
  if(!entry||!stage||!artwork)return;
  const version=++deployVersion;deployment=null;ready();
  try{
    const value=await stageDeployment(units,map,stage,crown,battleFormation(units,entry.document));
    if(version!==deployVersion)return;deployment=value;drawFormation();
    const count=value.slots.filter(slot=>slot.reasons).length;
    node('restricted').textContent=count?count+'枠が出撃不可':'';
  }catch(error){if(version===deployVersion)status(error.message,true);}finally{if(version===deployVersion)ready();}
}
async function refreshFormationList(preferred=entry?.id){
  const list=await readBattleJson('/api/formations?list=1');
  node('formation').innerHTML=list.entries.map((value,index)=>'<option value="'+value.id+'">'+esc(formationDisplayName(value,index+1))+'</option>').join('');
  const id=list.entries.some(value=>value.id===preferred)?preferred:list.entries[0]?.id;
  await chooseFormation(id);
}
async function chooseFormation(id){
  const version=++choiceVersion;health=null;deployment=null;ready();status('編成を読み込み中');
  try{
    const result=await readBattleJson('/api/formations'+(id?'?current='+encodeURIComponent(id):''));
    if(version!==choiceVersion)return;entry=result.entry;
    if(entry&&entry.document.gameVersion!==units.gameVersion)throw Error('編成とDBの版が異なります。編成を確認してください');
    drawFormation();
    if(entry){node('formation').value=entry.id;const value=await castleHealth(units,battleFormation(units,entry.document));if(version!==choiceVersion)return;health=value;node('health-breakdown').innerHTML=[['施設',value.facility],['城開発',value.development],['お宝',value.beforeCombo-value.facility-value.development],['コンボ加算',value.maximum-value.beforeCombo]].map(([name,amount])=>'<dt>'+name+'</dt><dd>'+formatNumber(amount)+'</dd>').join('');node('castle-health').textContent=formatNumber(value.maximum);node('sniper-damage').textContent=formatNumber(value.sniper);store();status('');await refreshDeployment();}
    else status('使用する編成を作成してください');
  }catch(error){status(error.message,true);}finally{if(version===choiceVersion)ready();}
}
function renderStage(){
  node('title').textContent=stage.name;document.title=stage.name+' 出撃準備 | KBCS';node('map').textContent=map.name;
  node('stages').innerHTML=stages.map(value=>'<button type="button" data-stage="'+value.index+'" aria-current="'+(value.index===stage.index)+'">'+(value.index+1)+'. '+esc(value.name)+'</button>').join('');
  node('crowns').innerHTML=map.stars.map((_,index)=>'<button type="button" data-crown="'+(index+1)+'" aria-pressed="'+(crown===index+1)+'"><img src="/icons/stages/crown-'+(index<crown?'on':'off')+'.png" alt="" width="25" height="24">'+(index+1)+'</button>').join('');
  node('crown-rate').textContent=formatNumber(map.stars[crown-1])+'%';
  node('pattern').innerHTML=stage.variants?.length?'<label>'+esc(stage.patternLabel||'出現パターン')+'<select data-pattern><option value="" disabled '+(!stage.patternSource?'selected':'')+'>選択してください</option>'+stage.variants.map(value=>'<option value="'+esc(value.source)+'" '+(value.source===stage.patternSource?'selected':'')+'>'+esc(value.name)+'</option>').join('')+'</select></label>':'';
  const ids=[...new Set([...(stage.enemies||[]),...stage.spawns.map(spawn=>spawn.enemy)])];
  node('enemies').innerHTML=ids.map(id=>{const enemy=enemies.enemies.find(enemy=>enemy.id===id);return '<div class="sortie-enemy">'+(enemy?enemyImageHtml(enemies,enemy,36):'')+'<span>'+esc(enemy?.name??'敵ID '+id)+'</span></div>';}).join('')||'<span>出現情報なし</span>';
  const limit=effectiveStageLimit(map,stage,crown),hasLimit=Object.keys(limit).length>0;
  node('limit-summary').textContent=hasLimit||map.rules.length||stage.formation?'出撃制限・特殊条件あり':'';
  node('limits').innerHTML=stageRulesHtml(database,stage,map,crown,units,true,{selectedLimits:hasLimit?[limit]:[],showOtherCrowns:false})+stageFormationHtml(stage,units);
  const enemyCastle=enemies.enemies.find(enemy=>enemy.id===stage.enemyCastle);
  node('stage-facts').innerHTML=[['統率力',stage.energy],['敵最大数',stage.maxEnemies],['ステージ幅',stage.width],['難易度',stage.difficulty==null?'—':'★'+stage.difficulty],['敵城',stage.timeLimit?'スコア制':stage.enemyCastle!=null?(enemyCastle?.name??'敵ID '+stage.enemyCastle):stage.castleHealth],['コンテニュー',stage.noContinue?'不可':'可'],['制限時間',stage.timeLimit?formatTime(stage.timeLimit,true):'なし']].map(([label,value])=>'<dt>'+label+'</dt><dd>'+esc(typeof value==='number'?formatNumber(value):value??'—')+'</dd>').join('');
  stageMedia.clear();node('media').innerHTML=stageMediaHtml(database,stage,enemies);stageMedia.refresh();
  node('database-link').href='/pages/stage-detail/?'+new URLSearchParams({map:map.key,stage:stage.index,crown});
  history.replaceState(null,'','/pages/stage-sortie/?'+new URLSearchParams({map:map.key,stage:stage.index,crown}));drawFormation();refreshDeployment();ready();
}
function report(label,current,total){node('loading-status').textContent=label+' '+current+' / '+total;node('progress').max=Math.max(1,total);node('progress').value=current;}
async function depart(){
  if(node('launch').disabled)return;
  const active=new AbortController();controller=active;ready();node('initial').hidden=false;node('setup').hidden=true;document.dispatchEvent(new CustomEvent('kbcs:battle-mode',{detail:true}));node('blackout').hidden=false;node('loading-status').textContent='ステージを準備中';
  try{
    // 出撃時点の保存版を固定し、編集タブで変更された設定を黙って使わない。
    const latest=await readBattleJson('/api/formations?current='+entry.id,{signal:active.signal});
    if(latest.entry?.revision!==entry.revision){await chooseFormation(entry.id);throw Error('編成が更新されました。設定を確認してから出撃してください');}
    const formation=battleFormation(units,entry.document),currentHealth=await castleHealth(units,formation);
    const snapshot={schemaVersion:1,version:database.gameVersion,buildId:database.buildId,stage:structuredClone(stage),map:structuredClone(map),crown,formationId:entry.id,formationRevision:entry.revision,formation,items:structuredClone(items),speed:items.speedup?speed:1,seed:0x12345678,limits:applicableLimits(map,stage,crown),castle:currentHealth,deployment:structuredClone(deployment),frame:0};
    snapshot.stage.musicTracks=(stage.musicTracks||[]).map(track=>({...track,loop:database.musicCatalog?.tracks?.[track.id]?.loop!==false}));
    const scene=await loadStageScene(stage,{frame:0,showEnemy:true,showPlayer:true,showEffects:true});
    if(scene.missing?.length)throw Error('ステージ素材が未収録です：'+scene.missing.join(', '));
    loadedAssets=await prepareBattleAssets(stage,formation,scene,report,active.signal);
    const screen=await prepareBattleScreen(units,snapshot,loadedAssets,active.signal,report);active.signal.throwIfAborted();
    prepared=snapshot;node('initial').hidden=false;node('setup').hidden=true;stageMedia.clear();
    battle=await startBattleScreen(node('initial'),node('canvas'),scene,snapshot,screen,returnToPreparation);active.signal.throwIfAborted();status('');
  }catch(error){returnToPreparation();if(error.name!=='AbortError')status(error.message,true);}
  finally{if(controller===active){controller=null;node('blackout').hidden=true;ready();}}
}
node('launch').addEventListener('click',depart);
node('cancel').addEventListener('click',()=>{controller?.abort();node('blackout').hidden=true;});
function returnToPreparation(){battle?.stop();battle=null;prepared=null;loadedAssets=null;node('initial').hidden=true;node('setup').hidden=false;document.dispatchEvent(new CustomEvent('kbcs:battle-mode',{detail:false}));stageMedia.refresh();}
node('formation').addEventListener('change',event=>chooseFormation(event.target.value));
node('stages').addEventListener('click',event=>{const target=event.target.closest('[data-stage]');if(target){stage=stages.find(value=>value.index===Number(target.dataset.stage));renderStage();}});
node('crowns').addEventListener('click',event=>{const target=event.target.closest('[data-crown]');if(target){crown=Number(target.dataset.crown);renderStage();}});
node('pattern').addEventListener('change',async event=>{const index=stage.index;node('launch').disabled=true;try{const value=await loadStageVariant(map.key,index,event.target.value);stages=stages.map(stage=>stage.index===index?value:stage);if(stage.index===index){stage=value;renderStage();status('');}}catch(error){status(error.message,true);}finally{ready();}});
node('items').addEventListener('change',event=>{const key=event.target.dataset.item;if(key){items[key]=event.target.checked;node('speed').disabled=!items.speedup;store();}});
node('speed').addEventListener('change',event=>{speed=Number(event.target.value);store();});
async function load(){
  try{
    [database,enemies,units,artwork]=await Promise.all([loadStageDatabase(),loadEnemyDatabase(),loadUnitDatabase(),readBattleJson('/images/native-formation/manifest.json')]);
    if(database.buildId!==units.buildId)throw Error('DBが更新されました。画面を再読み込みしてください');
    for(const unit of units.units)known.set(unit.id,unit);
    const routeResult=resolveStageRoute(database,route),detail=await readBattleJson('/api/stages?'+new URLSearchParams({map:routeResult.map.key}));
    if(detail.buildId!==database.buildId||detail.revision!==database.revision)throw Error('DBが更新されました。画面を再読み込みしてください');
    map=detail.maps.find(value=>value.key===routeResult.map.key);stages=detail.stages;stage=stages.find(value=>value.id===routeResult.selected)||stages[0];crown=Math.min(map.stars.length,crown);

    node('items').innerHTML=battleItems.map(item=>{const image=database.rewards[item.id]?.icon;return '<label><input type="checkbox" data-item="'+item.key+'" '+(items[item.key]?'checked':'')+'>'+(image?'<img src="'+esc(database.imageBase+image)+'" alt="">':'')+'<span>'+item.name+'</span></label>';}).join('');
    node('speed').value=speed;node('speed').disabled=!items.speedup;renderStage();node('status').hidden=true;node('content').hidden=false;
    await refreshFormationList(saved.formation);
  }catch(error){node('status').textContent=error.message;}
}
let refreshTime=0;
function refreshSavedFormation(){if(!map||!units||controller||Date.now()-refreshTime<300)return;refreshTime=Date.now();refreshFormationList().catch(error=>status(error.message,true));}
window.addEventListener('pageshow',event=>{if(event.persisted)refreshSavedFormation();});
window.addEventListener('focus',refreshSavedFormation);
window.addEventListener('storage',event=>{if(event.key==='kbcs:formation-update')refreshSavedFormation();});
load();
