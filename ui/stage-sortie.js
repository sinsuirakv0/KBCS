import {loadStageDatabase,loadStageVariant} from './src/shared/game/stages.js';
import {loadEnemyDatabase} from './src/shared/game/enemies.js';
import {loadUnitDatabase} from './src/shared/game/units.js';
import {escapeHtml as esc,formatNumber} from './src/shared/game/database-view.js';
import {resolveStageRoute,applicableLimits} from './src/features/stages/model.js';
import {loadStageScene} from './src/features/stages/native-media.js';
import {prepareBattleScreen,startBattleScreen} from './battle-screen.js';
import {createBattleRecording} from './battle-recording.js';
import {createFormationView,fitFormationName} from './formation-view.js';
import {createFormationReorder} from './formation-reorder.js';
import {readSortiePreferences,sortieItemsHtml,toggleSortieItem,sortieLaunchHtml,sortieFixedMoney,sortieEnemyLinksHtml} from './sortie-view.js';
import {formationDisplayName} from './formation-model.js';
import {readBattleJson,battleFormation,castleHealth,prepareBattleAssets,effectiveStageLimit,stageDeployment} from './battle-support.js';
import {enterPhoneFullscreen,phoneConnection} from './phone-connection.js';
import {loadStageSearchIndex} from './search-index.js';
import {sendPhoneControl,startPhoneBattle} from './phone-battle.js';

const node=id=>document.getElementById('sortie-'+id),route=new URLSearchParams(location.search);
const largeStart=node('large-start');
const phone=route.get('phone')==='1',desktop=typeof window.ipc?.postMessage==='function';
const phonePolling=new AbortController();
let phoneLinked=false,phoneLoading=false,phoneMirror,phoneTimer,phoneDisconnect;
function stopPhonePolling(){phonePolling.abort();clearTimeout(phoneTimer);phoneMirror?.stop();}
window.addEventListener('pagehide',stopPhonePolling,{once:true});
if(phone)node('enemies').inert=true;
let artwork,battleArtwork,paintFormation,formationIndex=1,deployment,deployVersion=0,battle;
let database,enemies,units,map,stages=[],stage,entry,health,choiceVersion=0,controller,loadedAssets,prepared;
let reorder,formationSaving=false,formationSelected=-1;
if(phone)window.addEventListener('kbcs:phone-leave',()=>{
 stopPhonePolling();controller?.abort();
 battle?.stop();
});
let saved={items:{},speed:2};try{saved=readSortiePreferences(localStorage,sessionStorage);}catch{}
largeStart.checked=saved.large===true;
let crown=Math.max(1,Number(route.get('crown'))||1),items={...saved.items},speed=saved.speed;
let sidebar,sidebarRequest,sidebarDatabase;
const variantRequests=new Map();
node('enemies').addEventListener('error',event=>{
  const icon=event.target.closest?.('.enemy-icon');
  if(icon){icon.nextElementSibling.hidden=false;icon.remove();}
},true);
function status(message,error=false){node('message').textContent=message;node('message').classList.toggle('sortie-status-error',error);}
function store(){saved={...saved,formation:entry?.id??saved.formation,items,speed};try{for(const storage of [localStorage,sessionStorage])storage.setItem('kbcs:sortie',JSON.stringify(saved));}catch{}}
largeStart.onchange=()=>{saved.large=largeStart.checked;store();};
const moneyControls=document.createElement('label');moneyControls.className='sortie-fixed-money';moneyControls.hidden=true;
moneyControls.innerHTML='所持金<input type="number" min="0" max="10000000" step="1" aria-label="お小遣い制ステージの所持金">円<button type="button">ステージ初期値</button>';
node('items').before(moneyControls);
const moneyInput=moneyControls.querySelector('input');
moneyInput.addEventListener('change',()=>{try{const value=sortieFixedMoney(map,moneyInput.valueAsNumber);saved.fixedMoney={...saved.fixedMoney,[map.key]:value};moneyInput.setCustomValidity('');store();}catch(error){moneyInput.setCustomValidity(error.message);moneyInput.reportValidity();}});
moneyControls.querySelector('button').onclick=()=>{if(saved.fixedMoney)delete saved.fixedMoney[map.key];moneyInput.value=sortieFixedMoney(map);moneyInput.setCustomValidity('');store();};
function ready(){node('launch').disabled=!!controller||phoneLoading||!!phoneMirror||formationSaving||!!reorder?.active||!entry||!health||!deployment||!stage||variantRequests.has(stage.index)||!!(stage.variants?.length&&!stage.patternSource)||!(stage.width>0)||stage.background==null;}
function drawFormation(){
  if(!entry){node('formation-preview').innerHTML=phone?'PCで編成を作成してください':'<a href="/pages/formation/">編成を作成</a>';return;}
  const document=battleFormation(units,entry.document);
  node('formation-edit').href='/pages/formation/?'+new URLSearchParams({id:entry.id,map:map.key,stage:stage.index,crown});
  node('formation-preview').innerHTML=paintFormation(document,{index:formationIndex,selected:formationSelected,deployment,preview:true,...reorder?.view});fitFormationName(node('formation-preview'),artwork);reorder?.renderFloating();ready();
}
async function refreshFormationStats(version){
  const current=entry,value=await castleHealth(units,battleFormation(units,current.document));
  if(version!==choiceVersion||entry!==current)return;
  health=value;node('health-breakdown').innerHTML=[['施設',value.facility],['城開発',value.development],['お宝',value.beforeCombo-value.facility-value.development],['コンボ加算',value.maximum-value.beforeCombo]].map(([name,amount])=>'<tr><th scope="row">'+name+'</th><td class="data-align-right">'+formatNumber(amount)+'</td></tr>').join('');node('castle-health').textContent=formatNumber(value.maximum);node('sniper-damage').textContent=formatNumber(value.sniper);store();status('');await refreshDeployment();
}
async function saveFormationOrder(before){
  const current=entry,version=++choiceVersion;formationSaving=true;health=null;deployment=null;++deployVersion;
  node('formation').disabled=true;node('formation-edit').inert=true;drawFormation();status('編成を保存中');
  try{
    const result=await readBattleJson('/api/formations',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:current.id,revision:current.revision,document:structuredClone(current.document)})});
    current.revision=result.entry.revision;
    try{localStorage.setItem('kbcs:formation-update',Date.now()+':'+current.id+':'+current.revision);}catch{}
    await refreshFormationStats(version);
  }catch(error){
    // 競合や応答切断時は保存済みの版を取り直し、未保存の並びで出撃しない。
    try{const latest=await readBattleJson('/api/formations?current='+current.id);entry=latest.entry;}catch{current.document.slots=before;}
    reorder.cancel();
    try{if(entry)await refreshFormationStats(version);}catch{}
    drawFormation();status(error.message,true);
  }finally{formationSaving=false;node('formation').disabled=false;node('formation-edit').inert=false;ready();}
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
async function refreshFormationList(preferred=entry?.id??saved.formation){
  preferred=Number(preferred);
  const list=await readBattleJson('/api/formations?list=1');
  if(formationSaving||reorder?.active)return;
  node('formation').innerHTML=list.entries.map((value,index)=>'<option value="'+value.id+'">'+esc(formationDisplayName(value,index+1))+'</option>').join('');
  const id=list.entries.some(value=>value.id===preferred)?preferred:list.entries[0]?.id;
  await chooseFormation(id);
}
async function chooseFormation(id){
  if(formationSaving)return;reorder?.cancel();formationSelected=-1;
  const version=++choiceVersion;++deployVersion;health=null;deployment=null;ready();status('編成を読み込み中');
  try{
    const result=await readBattleJson('/api/formations'+(id?'?current='+encodeURIComponent(id):''));
    if(version!==choiceVersion)return;entry=result.entry;formationIndex=result.index;
    drawFormation();
    if(entry){node('formation').value=entry.id;await refreshFormationStats(version);}
    else status('使用する編成を作成してください');
  }catch(error){status(error.message,true);}finally{if(version===choiceVersion)ready();}
}
function showSidebarMessage(message){node('details-message').textContent=message;}
function refreshStageDetails(){
  if(phone||!stage||!node('initial').hidden)return;
  if(!sidebar){
    if(!sidebarRequest)sidebarRequest=import('./sortie-stage-detail.js').then(({mountSortieStageDetail})=>
      mountSortieStageDetail(node('details'),{onCrown:selectCrown,onPattern:selectPattern,onMessage:showSidebarMessage})
    ).then(details=>{sidebar=details;refreshStageDetails();})
      .catch(error=>{showSidebarMessage(error.message);node('details').setAttribute('aria-busy','false');})
      .finally(()=>{sidebarRequest=null;});
    return;
  }
  showSidebarMessage('');
  node('details').setAttribute('aria-busy','false');
  void sidebar.render({database:sidebarDatabase,map,stage,stages,crown,units,enemies})
    .catch(error=>showSidebarMessage(error.message));
}
function renderStage(){
  const fixed=sortieFixedMoney(map,saved.fixedMoney?.[map.key]);moneyControls.hidden=fixed===null;moneyInput.value=fixed??'';moneyInput.setCustomValidity('');
  node('title').textContent=stage.name;document.title=stage.name+' 出撃準備 | KBCS';node('map').textContent=map.key+'-'+stage.index+' '+map.name;
  node('stages').innerHTML=stages.map(value=>'<button type="button" data-stage="'+value.index+'" aria-current="'+(value.index===stage.index)+'">'+(value.index+1)+'. '+esc(value.name)+'</button>').join('');
  node('crowns').innerHTML=map.stars.map((_,index)=>'<button type="button" data-crown="'+(index+1)+'" aria-label="'+(index+1)+'冠" title="'+(index+1)+'冠" aria-pressed="'+(crown===index+1)+'"><img src="/icons/stages/crown-'+(index<crown?'on':'off')+'.png" alt="" width="25" height="24"></button>').join('');
  const continueStatus=stage.width==null?'未収録':stage.noContinue?'不可':'可';
  node('crown-rate').textContent='倍率'+formatNumber(map.stars[crown-1])+'%';
  node('continue-status').textContent='コンテニュー'+continueStatus;
  node('pattern').innerHTML=stage.variants?.length?'<label>'+esc(stage.patternLabel||'出現パターン')+'<select data-pattern><option value="" disabled '+(!stage.patternSource?'selected':'')+'>選択してください</option>'+stage.variants.map(value=>'<option value="'+esc(value.source)+'" '+(value.source===stage.patternSource?'selected':'')+'>'+esc(value.name)+'</option>').join('')+'</select></label>':'';
  node('enemies').innerHTML=sortieEnemyLinksHtml(stage,map,crown,enemies);
  const limit=effectiveStageLimit(map,stage,crown),hasLimit=Object.keys(limit).length>0;
  node('limit-summary').textContent=hasLimit||map.rules.length||stage.formation?'出撃制限・特殊条件あり':'';
  refreshStageDetails();
  node('database-link').href='/pages/stage-detail/?'+new URLSearchParams({map:map.key,stage:stage.index,crown});
  const nextRoute=new URLSearchParams({map:map.key,stage:stage.index,crown});
  if(phone)nextRoute.set('phone','1');
  else if(route.get('text-preview')==='pixel8')nextRoute.set('text-preview','pixel8');
  history.replaceState(null,'','/pages/stage-sortie/?'+nextRoute);drawFormation();refreshDeployment();ready();
}
function report(label,current,total){node('loading-status').textContent=label+' '+current+' / '+total;node('progress').max=Math.max(1,total);node('progress').value=current;}
let recording;
function battleMode(active){
  if(active)sidebar?.clear();
  document.dispatchEvent(new CustomEvent('kbcs:battle-mode',{detail:active}));
  if(!active)refreshStageDetails();
}
async function sortieSnapshot(signal){
  // 出撃時点の保存版を固定し、編集タブで変更された設定を黙って使わない。
  const latest=await readBattleJson('/api/formations?current='+entry.id,{signal});
  if(latest.entry?.revision!==entry.revision){await chooseFormation(entry.id);throw Error('編成が更新されました。設定を確認してから出撃してください');}
  const formation=battleFormation(units,entry.document),currentHealth=await castleHealth(units,formation);
  const seed=new Uint32Array(1);while(!seed[0])crypto.getRandomValues(seed);
  const snapshot={schemaVersion:1,version:database.gameVersion,buildId:database.buildId,stage:structuredClone(stage),map:structuredClone(map),crown,formationId:entry.id,formationRevision:entry.revision,formation,fixedMoney:sortieFixedMoney(map,saved.fixedMoney?.[map.key]),items:structuredClone(items),speed:items.speedup?speed:1,seed:seed[0],limits:applicableLimits(map,stage,crown),castle:currentHealth,deployment:structuredClone(deployment),frame:0};
  snapshot.stage.musicTracks=(stage.musicTracks||[]).map(track=>({...track,loop:database.musicCatalog?.tracks?.[track.id]?.loop!==false}));
  return snapshot;
}
function phoneFailure(message){
 return readBattleJson('/api/phone/failure',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(message)}).catch(()=>{});
}
async function depart(assigned){
  if(controller||battle||phoneMirror||(!assigned&&(node('launch').disabled||!moneyInput.reportValidity())))return;
  if(phone&&!assigned)void enterPhoneFullscreen();
  const active=new AbortController();controller=active;ready();
  let entering=false;
  try{
    if(phoneLinked&&(await phoneConnection()).paired){
      const snapshot=await sortieSnapshot(active.signal);active.signal.throwIfAborted();
      await sendPhoneControl({type:'launch',snapshot});phoneLoading=true;status('スマホで戦闘素材を準備しています…');return;
    }
    entering=true;node('initial').hidden=false;node('setup').hidden=true;battleMode(true);node('blackout').hidden=false;node('load-info').hidden=false;report('ステージを準備中',0,1);
    if(phone)window.top.document.documentElement.classList.add('phone-playing');
    const snapshot=assigned??await sortieSnapshot(active.signal);
    if(snapshot.buildId!==database.buildId)throw Error('DBが更新されました。出撃準備を開き直してください');
    const scene=await loadStageScene(snapshot.stage,{frame:0,showEnemy:true,showPlayer:true,showEffects:true},active.signal);
    if(scene.missing?.length)throw Error('ステージ素材が未収録です：'+scene.missing.join(', '));
    loadedAssets=phone?{images:new Map()}:await prepareBattleAssets(snapshot.stage,snapshot.formation,scene,report,active.signal);
    const screen=await prepareBattleScreen(units,snapshot,loadedAssets,active.signal,report,enemies,{phone,onFailure:phone?phoneFailure:undefined});active.signal.throwIfAborted();
    prepared=snapshot;
    battle=await startBattleScreen(node('initial'),node('canvas'),scene,snapshot,screen,returnToPreparation,recording,active.signal,phone||largeStart.checked);active.signal.throwIfAborted();status('');
  }catch(error){
    if(entering)returnToPreparation();
    if(phone&&!phonePolling.signal.aborted)void phoneFailure(error.name==='AbortError'?'スマホで出撃を取り消しました':error.message);
    if(error.name!=='AbortError')status(error.message,true);
  }finally{if(controller===active){controller=null;node('blackout').hidden=true;node('load-info').hidden=true;ready();}}
}
node('launch').addEventListener('click',()=>depart());
node('cancel').addEventListener('click',()=>controller?.abort());
function returnToPreparation(){
 battle?.stop();battle=null;phoneMirror?.stop();phoneMirror=null;phoneLoading=false;
 if(phone)window.top.document.documentElement.classList.remove('phone-playing');
 document.body.classList.remove('phone-battle-monitor');prepared=null;loadedAssets=null;node('initial').hidden=true;node('setup').hidden=false;battleMode(false);ready();
}
node('formation').addEventListener('change',event=>chooseFormation(event.target.value));
node('stages').addEventListener('click',event=>{const target=event.target.closest('[data-stage]');if(target){stage=stages.find(value=>value.index===Number(target.dataset.stage));renderStage();}});
function selectCrown(value){crown=value;renderStage();}
async function selectPattern(target,source){
  const index=target.index,request=loadStageVariant(map.key,index,source);
  variantRequests.set(index,request);ready();
  try{
    const variant=await request;
    if(variantRequests.get(index)!==request)return;
    const value={...target,...variant};
    stages=stages.map(item=>item.index===index?value:item);
    if(stage.index===index){stage=value;renderStage();status('');}
  }catch(error){
    if(variantRequests.get(index)===request)throw error;
  }finally{
    if(variantRequests.get(index)===request){variantRequests.delete(index);ready();}
  }
}
node('crowns').addEventListener('click',event=>{const target=event.target.closest('[data-crown]');if(target)selectCrown(Number(target.dataset.crown));});
node('pattern').addEventListener('change',async event=>{
  const select=event.target,previous=stage;
  select.disabled=true;
  try{await selectPattern(previous,select.value);}
  catch(error){select.value=previous.patternSource??'';status(error.message,true);}
  finally{select.disabled=false;}
});
node('formation-preview').addEventListener('click',event=>{
 if(formationSaving||reorder?.active||reorder?.suppressClick)return;
 const target=event.target.closest('[data-action],[data-slot]');if(!target)return;
 const action=target.dataset.action;
 if(action==='previous'||action==='next'){
  const select=node('formation'),count=select.options.length;
  if(count)chooseFormation(Number(select.options[(select.selectedIndex+(action==='next'?1:-1)+count)%count].value));
 }else if(action==='menu'){node('formation').focus();try{node('formation').showPicker?.();}catch{}}
 else if(target.dataset.slot!=null){formationSelected=Number(target.dataset.slot);drawFormation();}
});
node('formation-preview').addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){const button=event.target.closest('[role=button]');if(button){event.preventDefault();button.dispatchEvent(new MouseEvent('click',{bubbles:true}));}}});
node('items').addEventListener('click',event=>{const button=event.target.closest('[data-item]'),key=button?.dataset.item;if(key){const focused=document.activeElement===button;speed=toggleSortieItem(items,speed,key);node('items').innerHTML=sortieItemsHtml(battleArtwork,items,speed);if(focused)node('items').querySelector('[data-item="'+key+'"]').focus({preventScroll:true});store();}});
async function load(){
  try{
    if(!phone&&!recording)recording=createBattleRecording();
    const readMap=key=>readBattleJson('/api/stages?'+new URLSearchParams({map:key}));
    const detailRequest=phone&&route.get('map')?readMap(route.get('map')):null;
    let detail;
    [database,enemies,units,artwork,battleArtwork,detail]=await Promise.all([(phone?loadStageSearchIndex:loadStageDatabase)(),loadEnemyDatabase(),loadUnitDatabase(),readBattleJson('/images/native-formation/manifest.json'),readBattleJson('/images/native-battle/manifest.json'),detailRequest]);
    if(database.buildId!==units.buildId)throw Error('DBが更新されました。画面を再読み込みしてください');
    const routeResult=resolveStageRoute(database,route);
    detail??=await readMap(routeResult.map.key);
    if(detail.buildId!==database.buildId||detail.revision!==database.revision)throw Error('DBが更新されました。画面を再読み込みしてください');
    if(phone)database={...database,musicCatalog:detail.musicCatalog};
    else sidebarDatabase={...database,musicCatalog:detail.musicCatalog,
      rewards:detail.rewardCatalogVersion===1?{...database.rewards,...detail.rewards}:database.rewards};
    map=detail.maps.find(value=>value.key===routeResult.map.key);stages=detail.stages;stage=stages.find(value=>value.id===routeResult.selected)||stages[0];crown=Math.min(map.stars.length,crown);

    paintFormation=createFormationView(units,artwork);
    reorder=createFormationReorder(node('formation-preview'),{
      getDocument:()=>entry?.document,getDeployment:()=>deployment,paint:paintFormation,allowRemove:false,
      canStart:()=>!!(entry&&health&&deployment&&!controller&&!formationSaving),
      onSelect:slot=>{formationSelected=slot;},onDraw:drawFormation,onCommit:saveFormationOrder
    });
    node('items').innerHTML=sortieItemsHtml(battleArtwork,items,speed);node('launch').innerHTML=sortieLaunchHtml(battleArtwork);
    renderStage();node('status').hidden=true;node('content').hidden=false;
    node('options').inert=false;
    await refreshFormationList(saved.formation);
  }catch(error){node('status').textContent=error.message;}
  finally{node('content').setAttribute('aria-busy','false');}
}
let refreshTime=0;
function refreshSavedFormation(){if(!map||!units||controller||battle||phoneMirror||formationSaving||reorder?.active||Date.now()-refreshTime<300)return;refreshTime=Date.now();refreshFormationList().catch(error=>status(error.message,true));}
window.addEventListener('pageshow',event=>{if(event.persisted)refreshSavedFormation();});
window.addEventListener('focus',refreshSavedFormation);
window.addEventListener('kbcs:simulation-change',refreshStageDetails);
window.addEventListener('storage',event=>{
  if(event.key==='kbcs:database-display:stages'||event.key===null)refreshStageDetails();
});
window.addEventListener('storage',event=>{if(event.key==='kbcs:formation-update')refreshSavedFormation();});
async function listenToPc(){
 if(phonePolling.signal.aborted)return;
 let delay=0;
 try{
  const commands=await readBattleJson('/api/phone/commands',{signal:phonePolling.signal});
  for(const command of commands){
   if(command.type==='launch'){
    if(controller||battle)void phoneFailure('スマホで出撃準備中、または戦闘中です');
    else void depart(command.snapshot);
   }else document.dispatchEvent(new CustomEvent('kbcs:phone-control',{detail:command}));
  }
 }catch{delay=250;}
 if(!phonePolling.signal.aborted)phoneTimer=setTimeout(listenToPc,delay);
}
function phoneBattleEnded(disconnected=false){
 if(disconnected){phoneLinked=false;phoneDisconnect?.remove();}
 returnToPreparation();status('');void pollPhoneBattle();
}
async function pollPhoneBattle(){
 if(phonePolling.signal.aborted||phoneMirror||!phoneLinked)return;
 try{
  const value=await readBattleJson('/api/phone/battle',{signal:phonePolling.signal});
  if(phonePolling.signal.aborted)return;
  if(value.id&&value.start&&units&&!battle&&!controller){
   document.body.classList.add('phone-battle-monitor');node('initial').hidden=false;node('setup').hidden=true;battleMode(true);
   phoneMirror=startPhoneBattle(value.id,value.start,units,enemies,phoneBattleEnded);return;
  }
  if(value.loading!==phoneLoading||value.error&&node('message').textContent!==value.error){
   phoneLoading=value.loading;status(value.error||(phoneLoading?'スマホで戦闘素材を準備しています…':''),!!value.error);ready();
  }
 }catch(error){if(!phonePolling.signal.aborted)status(error.message,true);}
 if(!phonePolling.signal.aborted)phoneTimer=setTimeout(pollPhoneBattle,240);
}
async function openSortie(){
 const validate=desktop&&!phone?phoneConnection().catch(()=>null):null;
 await load();
 if(phone&&map)void listenToPc();
 if((await validate)?.active){
  phoneLinked=true;
  phoneDisconnect=document.createElement('button');phoneDisconnect.textContent='スマホ接続を終了';phoneDisconnect.type='button';node('launch').after(phoneDisconnect);
  phoneDisconnect.onclick=async()=>{try{await phoneConnection('DELETE');phoneBattleEnded(true);}catch(error){status(error.message,true);}};
  void pollPhoneBattle();
 }
}
openSortie();
