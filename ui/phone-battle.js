import {createBattleDetails} from './battle-details.js';
import {createBattleInspector,prepareInspectorAssets} from './battle-inspector.js';
import {createBattleMonitor} from './battle-monitor.js';
import {createBattleResults} from './battle-results.js';
import {createBattleStageStats} from './battle-stage-stats.js';
import {battleFpsLimits} from './battle-view.js';
import {prepareBattleImages,readBattleJson} from './battle-support.js';
import {editableKeyTarget,readBattleKeys} from './keyboard.js';
import {phoneConnection} from './phone-connection.js';

const json=body=>({method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
export const sendPhoneControl=value=>readBattleJson('/api/phone/control',json(value));

// PCは同じ戦闘の一覧と操作盤だけを動かす。
export function startPhoneBattle(id,{snapshot,textures,inspectionAssets},database,enemies,onEnd){
 const root=document.getElementById('battle-details'),controls=document.getElementById('battle-controls');
 const actions=controls.querySelector('.battle-actions'),cheats=controls.querySelector('#battle-cheats');
 const fps=controls.querySelector('[data-battle-fps]'),speed=controls.querySelector('[data-battle-speed]');
 const message=document.createElement('span');message.setAttribute('role','status');root.querySelector('.battle-status-line').prepend(message);
 const controller=new AbortController(),{signal}=controller,images=new Map();
 const stage=createBattleStageStats(root,snapshot),results=createBattleResults(controls,{drawing:false});
 const phoneTab=root.querySelector('#battle-tab-phone');phoneTab.hidden=false;
 let timer,inspector,frame=0,remote={},clockOffset=0,clockSample,force=true;
 const request=()=>{force=true;};
 const details=createBattleDetails(root,{profiles:[]},images,request);
 const monitor=createBattleMonitor(root,()=>({images:{bytes:0,pending:0},fpsLimit:30,lag:0,...remote,frame,
  firstPaint:remote.firstPaint+clockOffset,lastPaint:remote.lastPaint+clockOffset}),{phone:true});
 const restricted=[...controls.querySelectorAll('[data-debug=large],[data-debug=fullscreen],[data-recording],[data-battle-aspect]')];
 for(const node of restricted)node.hidden=true;
 for(const node of controls.querySelectorAll('button'))node.disabled=false;
 fps.innerHTML=battleFpsLimits.map(value=>'<option value="'+value+'">'+value+' FPS</option>').join('');fps.value=30;
 speed.innerHTML='<option value="0">アイテムに従う</option>'+[.1,.2,.25,.5,.75,...Array.from({length:20},(_,i)=>i+1)].map(value=>'<option value="'+value+'">'+value+'倍</option>').join('');
 cheats.hidden=true;for(const node of cheats.querySelectorAll('input'))node.checked=false;
 const disconnect=document.createElement('button');disconnect.type='button';disconnect.textContent='スマホ接続を終了';actions.append(disconnect);
 disconnect.onclick=()=>phoneConnection('DELETE').then(()=>onEnd(true)).catch(fail);
 function fail(error){if(!signal.aborted)message.textContent=error.message;}
 function send(value){void sendPhoneControl({id,...value}).catch(fail);}
 controls.addEventListener('click',event=>{
  const button=event.target.closest('[data-debug]'),action=button?.dataset.debug;
  if(action==='cheats'){cheats.hidden=!cheats.hidden;button.setAttribute('aria-expanded',String(!cheats.hidden));return;}
  if(action==='report'){
   const url=URL.createObjectURL(new Blob([JSON.stringify(monitor.snapshot(),null,2)],{type:'application/json'}));
   const link=document.createElement('a');link.href=url;link.download='kbcs-android-diagnostics.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);return;
  }
  if(['toggle','step','ten','menu','rows','page','camera','return'].includes(action))send({type:'action',action});
 },{signal});
 controls.addEventListener('change',event=>{
  const {target}=event;
  if(target===fps||target===speed)send({type:'setting',name:target===fps?'fps':'speed',value:Number(target.value)});
  else if(cheats.contains(target))send({type:'setting',name:'cheats',value:[...cheats.querySelectorAll('input:checked')].reduce((mask,box)=>mask|Number(box.dataset.cheat),0)});
 },{signal});
 const bindings=new Map(Object.entries(readBattleKeys()).map(([action,code])=>[code,action])),held=new Set();
 window.addEventListener('keydown',event=>{
  const action=bindings.get(event.code);
  if(!action||event.repeat||event.ctrlKey||event.metaKey||event.altKey||event.isComposing||editableKeyTarget(event.target)||document.querySelector('dialog:modal'))return;
  event.preventDefault();event.stopPropagation();
  if(action.startsWith('camera'))held.add(action);
  send({type:'key',phase:'down',action});
 },{signal,capture:true});
 window.addEventListener('keyup',event=>{
  const action=bindings.get(event.code);if(held.delete(action))send({type:'key',phase:'up',action});
 },{signal});
 window.addEventListener('blur',()=>{for(const action of held)send({type:'key',phase:'up',action});held.clear();},{signal});

 const poses=[inspectionAssets.bone,...inspectionAssets.profiles.flatMap(profile=>[profile.idle,profile.kb,profile.soul])];
 prepareBattleImages(poses.map(pose=>textures[pose?.texture]),images,signal).then(()=>prepareInspectorAssets(inspectionAssets,textures,images,database,signal)).then(assets=>{
  if(signal.aborted)return;
  details.setAssets(assets);
  inspector=createBattleInspector(document.getElementById('battle-actor-list'),document.getElementById('battle-actor-detail'),assets,database,enemies,request,actor=>details.select(actor));
 }).catch(fail);

 async function poll(){
  try{
   const inspection=inspector?.query(performance.now(),force);force=false;
   const sample=await readBattleJson('/api/phone/inspect?'+new URLSearchParams({session:id}),{...json({inspection,focusActor:details?.focus()}),signal});
   if(signal.aborted)return;
   if(!sample){onEnd();return;}
   if(sample.error)message.textContent=sample.error;
   const {state,runtime,pose,phoneStats}=sample;frame=state.frame;
   if(phoneStats?.clock!==clockSample){clockSample=phoneStats?.clock;clockOffset=performance.now()-(clockSample??0);}
   remote={...phoneStats,coreMs:sample.coreMs,computeMs:sample.sceneMs};
   const finished=!!runtime.result.mode;
   controls.querySelector('[data-debug=toggle]').textContent=remote.playbackPaused||state.paused?'再開':'一時停止';
   controls.querySelector('[data-debug=rows]').textContent=state.rows===2?'2段':'1段';
   for(const action of ['menu','rows','page','step','ten'])controls.querySelector('[data-debug='+action+']').disabled=finished||state.intro<24||action==='page'&&state.rows===2;
   stage.update(state,runtime);results.update(runtime);
   inspector?.update(runtime.inspection,frame);
   details?.update(runtime.focusedActor,frame,pose?[0,pose.length]:null,pose?{commands:pose,textures}:null);
  }catch(error){fail(error);}
  if(!signal.aborted)timer=setTimeout(poll,90);
 }
 poll();
 return {stop(){
  controller.abort();clearTimeout(timer);monitor.stop();stage.stop();results.stop();inspector?.stop();details?.stop();disconnect.remove();message.remove();
  phoneTab.hidden=true;root.querySelector('#battle-detail-phone').hidden=true;
  for(const node of restricted)node.hidden=false;
  for(const node of controls.querySelectorAll('[data-debug]'))node.disabled=false;
 }};
}
