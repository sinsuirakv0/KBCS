import {comboAvailable,partialCalculation,battlePrecisionReasons} from './effect-support.js';
import {nativeFont} from './native-font.js';
import {prepareNativeText} from './native-text.js';
import {readBattleKeys,defaultBattleKeys,battleKeyAction,editableKeyTarget} from './keyboard.js';
import {createSessionId} from './src/shared/browser/session-id.js';
import {battleAspects,battleViewportWidth,phoneCanvasSize,phoneHudInsets,phoneHudPoint,battleCameraView,battlePlaybackRate,battleFpsLimits,battlePresentationClock,accumulateBattleTicks} from './battle-view.js';
import {audioBlobUrl} from './src/shared/browser/audio-preview.js';
import {createBattleResults} from './battle-results.js';
import {createBattleSounds} from './battle-audio.js';
import {readBattleJson,battleItems,prepareBattleImages} from './battle-support.js';
import {catalog} from './simulation-profile.js';
import {stageSceneInput,createStagePainter,stageMediaStats} from './src/features/stages/native-media.js';
import {createBattleMonitor} from './battle-monitor.js';
import {createBattleFrameClient} from './battle-frame.js';
import {initializeSceneGestures,createSceneMotion} from './src/features/stages/scene-controls.js';
import {sortieFixedMoney} from './sortie-view.js';
import {prepareBattleInfo,drawBattleInfo,drawBattleSlotOrbs} from './battle-info.js';
import {prepareInspectorAssets,createBattleInspector} from './battle-inspector.js';
import {createBattleDisplay} from './battle-display.js';
import {createBattleDetails} from './battle-details.js';
import {createBattleStageStats} from './battle-stage-stats.js';

export function battleScreenConfiguration(database,snapshot){
 const {formation,map,items,deployment}=snapshot,profile=formation.profile;
 const facility=id=>{const v=profile.facilities[id];return v.level+v.plus-1;};
 const treasure=type=>catalog.treasures.filter(v=>v.effectType===type&&!v.effectFlag).reduce((sum,v)=>sum+Math.trunc(v.maximumEffect*profile.treasures[v.id]/100),0);
 const team=new Map(formation.slots.slice(0,5).filter(Boolean).map(v=>[v.unitId,v.form]));
 const combo=type=>database.combos.filter(v=>v.type===type&&comboAvailable(v,formation.slots)&&v.members.every(m=>team.has(m.id)&&team.get(m.id)>=m.form)).reduce((sum,v)=>sum+database.comboEffects[type].values[v.grade],0);
 const rule=(map.rules||[]).find(v=>v.id===0),fixed=sortieFixedMoney(map,snapshot.fixedMoney),mask=battleItems.reduce((bits,v,index)=>bits|(items[v.key]?1<<index:0),0);
 const speed=mask&1&&snapshot.speed===3?3:2;
 return {config:{worker_level:facility('worker'),wallet_level:facility('wallet'),attack_level:facility('cannonAttack'),charge_level:facility('cannonCharge'),chapter:['EOC','EOCZ'].includes(map.series)?map.number:3,income_treasure:treasure(3),wallet_treasure:treasure(4),charge_treasure:treasure(1),speed_treasure:treasure(17),income_combo:combo(8),wallet_combo:combo(9),charge_combo:combo(7),charge_start_combo:combo(3),items:mask|1,speed,fixed_money:rule?fixed*100:-1,costs:deployment.slots.map(v=>v.cost),present:formation.slots.map(v=>Number(!!v)),blocked:deployment.slots.map(v=>v.reasons)},itemsOn:mask,speedMode:mask&1?speed-1:0,worker:items.rich||rule?7:Math.min(7,combo(4)),money:rule?fixed*100:combo(5)*100};
}
export async function prepareBattleScreen(database,snapshot,assets,signal,report,enemies,{phone=false,onFailure}={}){
 const [atlas,options,textDiagnostics]=await Promise.all([readBattleJson('/images/native-battle/manifest.json',{signal}),readBattleJson('/api/battle-options',{signal}),prepareNativeText()]);
 let presentationDifferences=[];
 if(atlas.buildId!==snapshot.buildId||atlas.version!==snapshot.version){
  const sources=Object.values(atlas.atlases).flatMap(value=>Object.entries(value.sources)),paths=[...new Set([...sources.map(([path])=>path),atlas.soundSource.path])];
  const hashes=await readBattleJson('/api/asset-hashes',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(paths),signal});
  if(hashes[atlas.soundSource.path]!==atlas.soundSource.sha256)throw Error('戦闘音声の設定とDBの原本が異なります');
  presentationDifferences=[...new Map(sources)].flatMap(([path,source])=>hashes[path]===source.sha256?[]:[{path,missing:hashes[path]==null}]);
 }
 const forms=snapshot.formation.slots.map(member=>member&&database.units.find(v=>v.id===member.unitId)?.forms.find(v=>v.index===member.form));
 const atlasUrls=new Map(Object.values(atlas.atlases).map(v=>[v.image,v.url]));
 const mediaVersion=phone?'?'+new URLSearchParams({build:snapshot.buildId}):'';
 const paths=[...new Set([...Object.values(atlas.atlases).map(v=>v.image),...forms.filter(Boolean).map(v=>v.icon)])];
 let count=0;
 const images=new Map();
 for(const path of paths){signal.throwIfAborted();const url=atlasUrls.get(path);const image=(url?null:assets.images.get(path))||new Image();if(!image.src)image.src=url||'/api/asset/'+path+mediaVersion;try{await image.decode();}catch{throw Error('戦闘UI画像を読み込めません：'+path);}signal.throwIfAborted();images.set(path,image);report('戦闘UI',++count,paths.length);}
 const values=battleScreenConfiguration(database,snapshot);
 const info=await prepareBattleInfo(database,snapshot,signal);
 // 一覧の状態アイコンも幕が開く前にデコードする。
 const statusImages=phone?[]:await Promise.all([...new Set([database.imageBase+database.propertyAtlas.path,enemies.imageBase+enemies.propertyAtlas.path,'/icons/enemies/revive.png','/icons/enemies/burrow.png'])].map(async url=>{const image=new Image();image.src=url;await image.decode();signal.throwIfAborted();return image;}));
 const audioUrls=new Map(),audioErrors=new Map(),audioController=new AbortController();
 const dispose=()=>{audioController.abort();for(const url of audioUrls.values())URL.revokeObjectURL(url);audioUrls.clear();};
 signal.addEventListener('abort',dispose,{once:true});
 async function loadAudio(track){
  if(audioUrls.has(track.id))return;
  audioUrls.set(track.id,await audioBlobUrl('/api/stage-audio/'+track.id+mediaVersion,audioController.signal));
 }
 const tracks=snapshot.stage.musicTracks||[];
 try{if(!phone&&tracks[0]){await loadAudio(tracks[0]);report('開始BGM',1,1);}}
 catch(error){dispose();signal.removeEventListener('abort',dispose);throw error;}
 // 後の曲の取得は開始を待たせない。将来の切替入口は読込完了を確認する。
 const optionalAudio=tracks=>Promise.all(tracks.map(async track=>{try{await loadAudio(track);}catch(error){if(error.name!=='AbortError')audioErrors.set(track.id,error.message);}}));
 if(!phone)void optionalAudio(tracks.slice(1));
 return {phone,database,enemies,statusImages,atlas,options,forms,info,images,sceneImages:assets.images,audioUrls,audioErrors,presentationDifferences,textDiagnostics,
  preloadMusic:ids=>optionalAudio([...new Set([...tracks.map(track=>track.id),...ids])].filter(id=>id>=0).map(id=>({id}))),
  mediaVersion,report,onFailure,dispose:()=>{signal.removeEventListener('abort',dispose);dispose();},...values};
}

export async function startBattleScreen(root,canvas,scene,snapshot,resources,onReturn,recording,signal,largeAtStart=false){
 const {phone}=resources;
 let screenWidth=960,camera=scene.layout,cameraVersion=0,drawnVersion=-1,drawnRows=0;
 const backgroundCanvas=root.querySelector('[data-battle-background]'),controls=document.getElementById('battle-controls'),session=createSessionId();
 const detailsRoot=document.getElementById('battle-details'),presentation=battlePresentationClock();
 const largeHint=root.querySelector('[data-battle-large-hint]');let large=false,largeHintTimer;
 const fps=controls.querySelector('[data-battle-fps]');
 fps.innerHTML=battleFpsLimits.map(value=>'<option value="'+value+'">'+value+' FPS</option>').join('');
 try{fps.value=presentation.set(localStorage.getItem('kbcs:battle-fps'));}catch{fps.value=30;}
 const aspect=controls.querySelector('[data-battle-aspect]');aspect.innerHTML=battleAspects.map(([value,label])=>'<option value="'+value+'">'+label+'</option>').join('');
 try{aspect.value=localStorage.getItem('kbcs:battle-aspect')||'20:9';}catch{}if(!aspect.value)aspect.value='20:9';
 let painter;try{painter=createStagePainter(backgroundCanvas,()=>++cameraVersion,resources.sceneImages,{preloadedOnly:phone});}catch(error){resources.dispose();throw error;}
 let playbackPaused=false,stepQueue=0,paints=0,activeMs=0,activePaints=0,lastActivePaint,cheats=0,settingsVersion=0,appliedSettings=-1;
 const speed=controls.querySelector('[data-battle-speed]'),cheatPanel=controls.querySelector('#battle-cheats');
 speed.innerHTML='<option value="0">アイテムに従う</option>'+[.1,.2,.25,.5,.75,...Array.from({length:20},(_,i)=>i+1)].map(value=>'<option value="'+value+'">'+value+'倍</option>').join('');
 cheatPanel.hidden=true;for(const input of cheatPanel.querySelectorAll('input'))input.checked=false;
 controls.querySelector('[data-debug=cheats]').setAttribute('aria-expanded','false');
 function changeSettings(event){
  if(event.target===fps){
   fps.value=presentation.set(fps.value);
   try{localStorage.setItem('kbcs:battle-fps',fps.value);}catch{}
   clearTimeout(presentationTimer);presentationTimer=0;++cameraVersion;return;
  }
  if(event.target!==speed&&!cheatPanel.contains(event.target))return;
  cheats=[...cheatPanel.querySelectorAll('input:checked')].reduce((flags,input)=>flags|Number(input.dataset.cheat),0);++settingsVersion;accumulator=0;lastTime=0;
 }
 controls.addEventListener('change',changeSettings);
 const timing={coreMs:0,apiMs:0,computeMs:0,drawMs:0},frames=createBattleFrameClient({compress:!phone});
 const bandCanvas=document.createElement('canvas');
 const context=canvas.getContext('2d'),message=root.querySelector('[data-battle-message]'),menu=root.querySelector('[data-battle-menu]');
 const messageHome=message.parentElement;
 if(!phone)detailsRoot.querySelector('.battle-status-line').prepend(message);
 message.textContent='';
 const notices=document.createElement('div');notices.className='battle-precision-notices';
 const precisionWarning=document.createElement('div');precisionWarning.hidden=true;
 notices.append(precisionWarning);message.after(notices);
 const differences=resources.presentationDifferences;
 if(differences.length){
  const details=document.createElement('details'),summary=document.createElement('summary'),list=document.createElement('ul');
  summary.textContent='JPデータ v'+snapshot.version+' の戦闘UI素材 '+differences.length+'件が参照版と一致しないため、v'+resources.atlas.version+' の素材で表示しています。';
  for(const {path,missing} of differences){const item=document.createElement('li');item.textContent=path+'（'+(missing?'DBに未収録':'内容が異なる')+'）';list.append(item);}
  details.append(summary,list);notices.append(details);
 }
 const keyBindings=readBattleKeys();
 let state={frame:0,intro:12,rows:2,page:0,page_frame:0,page_direction:1,paused:0,money:resources.money,worker:resources.worker,cannon:0,holding:-1,hold_frames:0,hold_wait:0,pointer_down:0,pointer_x:0,pointer_y:0,guard:0,pending_control:-1,items_on:resources.itemsOn,request_slot:-1,request_cannon:0,ui_frame:0,speed_mode:resources.speedMode,wallet_flash:0,description_item:-1,description_wait:0,start_x:0,start_y:0,gesture:0,page_step:1,request_action:0,bgm_level:3,se_level:3,vibration_on:0,info_mode:0,info_slot:0,saved_rows:2,hud_frame:0};
 let runtime={wait:Array(10).fill(0),maximum:Array(10).fill(0)},sessionCreated=false,skipCombos=false,returnPending=false,inspector,details,inspectionDirty=false;
 Object.assign(state,{rows:resources.options.rows,saved_rows:resources.options.rows,bgm_level:resources.options.bgmLevel,se_level:resources.options.seLevel});
 let savedOptions=JSON.stringify(resources.options),saveOptions=Promise.resolve();
 function persistOptions(){
  const body=JSON.stringify({bgmLevel:state.bgm_level,seLevel:state.se_level,rows:state.info_mode?state.saved_rows:state.rows});
  if(body===savedOptions)return;savedOptions=body;
  saveOptions=saveOptions.then(()=>readBattleJson('/api/battle-options',{method:'PUT',headers:{'Content-Type':'application/json'},body,keepalive:true})).catch(error=>{savedOptions='';if(!stopped)message.textContent='設定保存: '+error.message;});
 }
 const stageStats=createBattleStageStats(detailsRoot,snapshot);
 let keySerial=0;
 let view,stopped=false,raf=0,busy=false,pendingScene,presenting=false,presentationTimer=0,updateTimer=0,returnAfterPaint=0,lastTime=0,lastCameraTime=0,firstPaint,lastPaint,accumulator=0,pointer={phase:0,x:0,y:0},control=0,error=false,failure=null;
 const requestController=new AbortController();
 let audio=null,audioId=-1;
 let audioStarted=false;
 function music(){
  const id=runtime.music?.id??-1;
  if(id!==audioId){if(audio){audio.pause();audio.removeAttribute('src');sounds.setMusic(null);}audio=null;audioStarted=false;audioId=id;}
  if(id>=0&&!audio&&resources.audioUrls.has(id)){audio=new Audio(resources.audioUrls.get(id));audio.loop=resources.atlas.sounds[id]?.loop??true;sounds.setMusic(audio);}
  if(!audio)return;audio.muted=!state.bgm_level;audio.volume=[0,.25,.5,1][state.bgm_level];
  if(playbackPaused||runtime.result.mode)audio.pause();else if(audio.paused&&!audio.ended&&state.bgm_level){audioStarted=true;audio.play().catch(()=>{});}
 }
 const sounds=createBattleSounds(resources.audioErrors,resources.atlas.sounds,{preloadedOnly:phone,version:resources.mediaVersion}),tints=new Map();
 const pixel8TextPreview=!phone&&new URLSearchParams(globalThis.location?.search).get('text-preview')==='pixel8';
 const results=createBattleResults(controls,{summary:!phone,pixel8TextPreview});
 let leftInset=0,rightInset=0;
 if(!phone)sounds.preload([8,9,10,11,15,19,20,21,22,23,24,25,26,27,28,29,36,37,42,44,45,50,57,59,60,61,65,70,71,72,73,74,83,84,85,86,90,105,106,110,111,112,124,137,138,139,159,162,167,168,169,188,189,194]);
 function tinted(image,cut,color,key){
  if(!tints.has(key)){const surface=document.createElement('canvas');surface.width=cut[2];surface.height=cut[3];const paint=surface.getContext('2d');paint.drawImage(image,...cut,0,0,cut[2],cut[3]);paint.globalCompositeOperation='multiply';paint.fillStyle='rgb('+color.join(',')+')';paint.fillRect(0,0,surface.width,surface.height);paint.globalCompositeOperation='destination-in';paint.drawImage(image,...cut,0,0,cut[2],cut[3]);tints.set(key,surface);}return tints.get(key);
 }
 function resize(){
  const choice=large?'auto':aspect.value;
  const box=canvas.parentElement.getBoundingClientRect(),width=battleViewportWidth(choice,box.width,box.height);
  if(phone){
   const safe=window.top.getComputedStyle(window.top.document.documentElement);
   const [left,right]=phoneHudInsets(width,box,parseFloat(safe.getPropertyValue('--phone-safe-left'))||0,parseFloat(safe.getPropertyValue('--phone-safe-right'))||0);
   if(left!==leftInset||right!==rightInset){leftInset=left;rightInset=right;++cameraVersion;}
  }
  document.dispatchEvent(new CustomEvent('kbcs:battle-view',{detail:{ratio:choice==='auto'?null:width/640}}));
  const [pixels,height]=phone?phoneCanvasSize(width,box,window.devicePixelRatio||1):[width,640];
  if(width===screenWidth&&canvas.width===pixels&&canvas.height===height&&backgroundCanvas.width===pixels&&backgroundCanvas.height===height)return;
  screenWidth=width;resources.config.viewport_width=width;
  for(const surface of [canvas,backgroundCanvas]){
   surface.width=pixels;surface.height=height;surface.style.width='min(100cqw,'+(width/640*100)+'cqh)';
  }
  context.setTransform(pixels/width,0,0,height/640,0,0);
  ++cameraVersion;
 }
 function setLargeBattle(enabled){
  large=enabled;document.body.classList.toggle('battle-large',enabled);
  if(sessionCreated)showLargeHint();
  resize();canvas.focus({preventScroll:true});
 }
 function showLargeHint(){
  clearTimeout(largeHintTimer);largeHint.hidden=!large||phone;
  if(large&&!phone)largeHintTimer=setTimeout(()=>{largeHint.hidden=true;},5000);
 }
 async function drawScene(next,version){
  if(!next||stopped)return;timing.computeMs=next.computeMs;
  const drawing=performance.now();if(!await painter.paint(next))return;timing.drawMs=performance.now()-drawing;
  if(stopped)return;scene=next;drawnVersion=version;drawnRows=state.rows;
  // 操作中の新しい要求は古い描画応答で上書きしない。
  if(version===cameraVersion)camera=next.layout;
  return true;
 }
 async function present(){
  const scheduledAt=performance.now();
  const next=pendingScene;pendingScene=null;
  timing.displayWaitMs=next?scheduledAt-next.received:0;
  const drawn=next&&await drawScene(next.scene,next.version);
  if(stopped)return;
  const hudStart=performance.now();paint();if(drawn)recording?.frame(backgroundCanvas,canvas);
  lastPaint=performance.now();timing.hudMs=lastPaint-hudStart;firstPaint??=lastPaint;presentation.presented(scheduledAt);
  if(!playbackPaused&&!state.paused&&!document.hidden&&state.intro>=24&&!state.battle_mode){
   if(lastActivePaint!=null){activeMs+=lastPaint-lastActivePaint;++activePaints;}
   lastActivePaint=lastPaint;
  }else lastActivePaint=undefined;
  if(next)details?.update(next.actor,next.frame,next.range,next.scene);
 }
 function queuePresentation(){
  if(!pendingScene||presenting||presentationTimer||stopped||error||document.hidden)return;
  const delay=presentation.delay(performance.now());
  if(delay>0){presentationTimer=setTimeout(()=>{presentationTimer=0;queuePresentation();},Math.ceil(delay));return;}
  presenting=true;
  present().then(()=>{if(returnPending)returnAfterPaint=2;}).catch(fail).finally(()=>{
   presenting=false;
   // 次のブラウザー描画通知を待たず、既に経過したtickだけ送る。
   scheduleUpdate();
  });
 }
 let phoneTextures,lastPhoneStats=-Infinity;
 function phoneStats(){
  const now=performance.now();if(!phone||now-lastPhoneStats<250)return undefined;lastPhoneStats=now;
  return {...timing,...frames.stats(),clock:now,paints,firstPaint,lastPaint,activeMs,activePaints,fpsLimit:Number(fps.value),lag:accumulator,images:stageMediaStats(resources.sceneImages),playbackPaused};
 }
 async function update(ticks,stepping=false){
  inspectionDirty=false;
  const immediate=playbackPaused&&!state.paused&&!!(cheats&4);
  const input=stepping?{ticks,phase:0,x:0,y:0,control:10}:{ticks,...pointer,control};
  if(ticks||immediate)pointer.phase=0;control=0;
  const version=cameraVersion,sentSettings=settingsVersion,sentKeys=keySerial;
  const sceneInput=stageSceneInput(snapshot.stage,{center:camera.center,zoom:camera.zoom,showEnemy:true,showPlayer:true,showEffects:true,session});
  const {value:next,timing:measured}=await frames.load({session,input,cheats,skipCombos,compact:true,inspection:inspector?.query(performance.now(),stepping||immediate),focusActor:details?.focus(),phoneStats:phoneStats(),scene:{...sceneInput,viewportWidth:screenWidth,safeLeft:leftInset}},requestController.signal);
  if(phone&&next.scene&&!next.scene.textures.length)next.scene.textures=phoneTextures;
  Object.assign(timing,measured);timing.coreMs=next.coreMs;
  if(stopped)return;appliedSettings=sentSettings;
  accrueClock(performance.now());
  // 0tickキーの後に届いた同一Fの古い描画応答で、押下状態を巻き戻さない。
  if(sentKeys===keySerial||next.state.ui_frame>state.ui_frame||next.state.frame>state.frame){state=next.state;view=next.layout;}runtime=next.runtime;
  if(runtime.precision?.status==='partial'&&precisionWarning.hidden){
   const heading=document.createElement('p'),list=document.createElement('ul');heading.textContent=partialCalculation;
   for(const reason of battlePrecisionReasons(runtime.precision.issues,{dataVersion:snapshot.version,calculationVersion:catalog.version,rules:snapshot.map.rules,combos:resources.database.combos})){
    const item=document.createElement('li');item.textContent=reason;list.append(item);
   }
   precisionWarning.append(heading,list);precisionWarning.hidden=false;
  }
  persistOptions();
  results.update(runtime,screenWidth,resources.atlas);
  inspector?.update(runtime.inspection,state.frame);
  sounds.update(runtime.sounds||[],state.se_level,state.speed_mode+1,playbackPaused&&!stepping,!!runtime.result.mode);
  const result=runtime.result,finished=!!result.mode;
  if(!phone)stageStats.update(state,runtime);
  if(state.request_slot>=0)message.textContent='';
  if(state.request_cannon)message.textContent='にゃんこ砲を発射';
  menu.hidden=!state.paused;
  music();
  if(state.request_action===301)window.open('https://kbc-rakv0.pages.dev/information/appli/battlecats/help/index.html','_blank','noopener');
  if(state.request_action===302){if(runtime.result?.mode)returnPending=true;else{stop();onReturn();return;}}
  for(const button of controls.querySelectorAll('button'))button.disabled=false;
  controls.querySelector('[data-debug=toggle]').textContent=playbackPaused||state.paused?'再開':'一時停止';
  controls.querySelector('[data-debug=rows]').textContent=state.rows===2?'2段':'1段';
  controls.querySelector('[data-debug=page]').disabled=state.rows===2||finished;
  for(const key of ['menu','rows'])controls.querySelector('[data-debug='+key+']').disabled=finished;
  for(const button of controls.querySelectorAll('[data-debug=step],[data-debug=ten]'))button.disabled=state.intro<24;
  if(playbackPaused&&!state.paused){state.pointer_down=0;state.holding=-1;state.hold_frames=0;pointer.phase=0;if(!stepping)accumulator=0;}
  pendingScene={scene:next.scene,version,actor:runtime.focusedActor,range:runtime.focusedDrawRange,frame:next.state.frame,received:performance.now()};
 }
 function sprite(name,index,x,y,width,height){
  const atlas=resources.atlas.atlases[name],cut=atlas.rects[index];if(!cut)throw Error(name+' cut '+index+' がありません');
  const w=width??cut[2],h=height??cut[3];
  if(w<0||h<0){context.save();context.translate(x,y);context.scale(w<0?-1:1,h<0?-1:1);context.drawImage(resources.images.get(atlas.image),...cut,0,0,Math.abs(w),Math.abs(h));context.restore();}
  else context.drawImage(resources.images.get(atlas.image),...cut,x,y,w,h);
 }
 function nineSlice(name,index,centerIndex,x,y,width,height){
  const atlas=resources.atlas.atlases[name],border=atlas.rects[index],center=atlas.rects[centerIndex],image=resources.images.get(atlas.image);
  const left=center[0]-border[0],top=center[1]-border[1],right=border[2]-left-center[2],bottom=border[3]-top-center[3];
  const sx=[border[0],center[0],center[0]+center[2]],sy=[border[1],center[1],center[1]+center[3]],sw=[left,center[2],right],sh=[top,center[3],bottom];
  const dx=[x,x+left,x+width-right],dy=[y,y+top,y+height-bottom],dw=[left,width-left-right,right],dh=[top,height-top-bottom,bottom];
  for(let row=0;row<3;++row)for(let column=0;column<3;++column)context.drawImage(image,sx[column],sy[row],sw[column],sh[row],dx[column],dy[row],dw[column],dh[row]);
 }
 function number(value,base,right,y,gap=-1,scale=1,leftAligned=false){
  const digits=String(Math.max(0,Math.trunc(value))).split('').map(Number),rects=resources.atlas.atlases.img001_ja.rects;
  const width=digits.reduce((sum,v)=>sum+rects[base+v][2]*scale+gap,0)-gap;
  const start=leftAligned?right:right-width;let x=start;for(const digit of digits){const cut=rects[base+digit];sprite('img001_ja',base+digit,x,y,cut[2]*scale,cut[3]*scale);x+=cut[2]*scale+gap;}return start;
 }
 function paint(){
  if(!view)return;
  ++paints;context.clearRect(0,0,screenWidth,640);
  if(runtime.result?.mode&&runtime.ending.phase){results.paint(context,screenWidth,sprite,number,resources.atlas,resources.images);paintFade();return;}
  // 005d0044 / 005d0a68 / 005d1f2c / 005d2408 / 006e21c0。背景と同じ終了時計を使う。
  const slide=runtime.endingHudSlide??0,moneyY=10-slide;
  const rightEdge=screenWidth-rightInset;
  const moneyBase=view.money_base,moneyRight=rightEdge-34,capX=number(view.wallet_max/100,moneyBase,moneyRight,moneyY),slashX=capX-29;
  sprite('img001_ja',moneyBase+10,slashX,moneyY);number(state.money/100,moneyBase,slashX-1,moneyY);sprite('img001_ja',moneyBase+11,moneyRight,moneyY);
  // 005d0508は後ろのページを先に描き、選択ページを重ねる。
  function slots(){
  const order=view.order;
  for(const index of order){
   if(view.modes[index]===0)continue;
   const [x,y,w,h]=view.slots[index],form=resources.forms[index];
   if(!form){sprite('uni',0,x,y,w,h);if(view.modes[index]===2){context.fillStyle='rgba(0,0,0,.392)';context.fillRect(x,y,w,h);}continue;}
   const summon=runtime.hud.summons[index],image=resources.images.get(form.icon);
   const restricted=!summon[0]&&(runtime.deployment.blocked[index]&(0x7f|0x100))!==0;
   const tint=summon[0]&&summon[1]?'summon-ready':summon[0]||restricted?'slot-locked':null;
   if(tint)context.drawImage(tinted(image,[9,21,110,85],tint==='summon-ready'?[157,215,255]:[135,100,100],form.icon+'-'+tint),x,y,w,h);
   else context.drawImage(image,9,21,110,85,x,y,w,h);
   const cost=runtime.costs[index],disabled=!tint&&(state.battle_mode||(!(cheats&1)&&cost>state.money)||runtime.wait[index]>0),base=disabled?46:35;
   if(disabled||(!tint&&view.modes[index]===2)){context.fillStyle='rgba(0,0,0,.392)';context.fillRect(x,y,w,h);}
   if(summon[0]&&summon[1]){const cut=resources.atlas.atlases.img002_ja.rects[53],[sx,sy]=view.labels[index];context.drawImage(tinted(resources.images.get(resources.atlas.atlases.img002_ja.image),cut,[summon[4],summon[4],summon[4]],'summon-'+summon[4]),sx+Math.trunc((110-cut[2])/2),sy+Math.trunc((85-cut[3])/2));}
   const gauge=runtime.hud.gauges[index];
   if(gauge[2]){
    const [gx,gy,,cyan,red]=gauge;context.fillStyle='#000';context.fillRect(gx,gy,97,14);
    context.fillStyle='#f00';context.fillRect(gx+2,gy+2,red,10);context.fillStyle='#0ff';context.fillRect(gx+2,gy+2,cyan,10);
   }else if(!summon[0]&&(!restricted||resources.config.fixed_money>=0&&view.modes[index]!==2)){const [labelX,labelY]=view.labels[index];number(Math.trunc(cost/100),base,labelX+94,labelY+62,-3);sprite('img001_ja',disabled?56:45,labelX+94,labelY+62,22,26);}
   if(index<5&&!state.info_mode&&view.modes[index]===1&&!skipCombos&&runtime.comboIntro?.layout.blink<2&&runtime.comboIntro.combo?.members.some(member=>member.id===snapshot.formation.slots[index]?.unitId))sprite('img002_ja',44,x-8,y-8,w+16,h+16);
   if(view.modes[index]===1){
    const [labelX,labelY]=view.labels[index];
    drawBattleSlotOrbs(context,resources.info,runtime.hud.orbIcons?.[index],labelX,labelY);
   }
  }
  }
  context.save();context.translate(0,slide);
  slots();
  context.save();context.translate(leftInset,0);
  const canUpgrade=state.worker<7&&state.money>=view.upgrade_cost;
  sprite('img002_ja',view.wallet_base,-48,519);
  if(state.worker===7){sprite('img001_ja',81,4,611);sprite('img001_ja',13,4,510);sprite('img001_ja',22,73,510);}
  else {const base=canUpgrade?35:46,digits=String(Math.trunc(view.upgrade_cost/100)),right=4+[...digits].reduce((sum,v)=>sum+resources.atlas.atlases.img001_ja.rects[base+Number(v)][2]-3,3);number(view.upgrade_cost/100,base,right,611,-3);sprite('img001_ja',canUpgrade?45:56,right,611,22,26);sprite('img001_ja',canUpgrade?13:24,4,510);sprite('img001_ja',(canUpgrade?15:26)+state.worker,73,510);}
  context.restore();
  if(view.cannon_base>=0)sprite('img002_ja',view.cannon_base,rightEdge-146,510);
  for(let i=0;i<view.cannon_bands;++i)sprite('img002_ja',11+i,rightEdge-146,i===9?510:628-i*12);if(view.cannon_label>=0)sprite('img002_ja',view.cannon_label,rightEdge-129,581);
  context.restore();
  const [pauseX,pauseY,pauseW,pauseH]=view.pause_icon;
  sprite('img002_ja',2,leftInset+pauseX-slide,pauseY,pauseW,pauseH);
  const hud=runtime.hud,scale=hud.scale,hpCuts=resources.atlas.atlases.img001_ja.rects;
  for(let side=0;side<2;++side){
   const [anchor,y]=hud.anchors[side],[hp,maximum,unknown]=hud.health[side];
   // 0070af68〜0070b028。特殊敵城の基準は斜線の位置でなく、分母の桁数を加える前の左端。
   const x=side&&hud.specialEnemyCastle?anchor+(unknown?7*hpCuts[108][2]:String(maximum).length*hpCuts[57][2])*scale:anchor;
   if(unknown){const cut=hpCuts[108];for(let i=0;i<7;++i){sprite('img001_ja',108,x-(7-i)*cut[2]*scale,y,cut[2]*scale,cut[3]*scale);sprite('img001_ja',108,x+(18+i*cut[2])*scale,y,cut[2]*scale,cut[3]*scale);}}
   else{number(hp,57,x,y,0,scale);number(maximum,57,x+18*scale,y,0,scale,true);}
   sprite('img001_ja',67,x,y,18*scale,18*scale);
  }
  for(const [cut,x,y,w,h] of view.item_icons)if(w)sprite('mapicon',cut,x-rightInset,y-slide,w,h);
  const [warning,warningX,warningY]=hud.warning;
  if(warning){
   context.font=nativeFont(30);context.textAlign='center';context.textBaseline='top';context.fillStyle='#000';
   const text=resources.atlas.deploymentWarnings[warning-1];
   for(let y=-2;y<=2;++y)for(let x=-2;x<=2;++x)context.fillText(text,warningX+x,warningY+y);
   context.fillStyle='#ff0';context.fillText(text,warningX,warningY);context.textBaseline='alphabetic';
  }
  if(view.description_box[2]){
   context.save();context.translate(-rightInset,0);
   context.fillStyle='rgba(255,255,255,'+(216/255)+')';context.fillRect(...view.description_box);context.beginPath();const points=view.description_arrow;context.moveTo(points[0],points[1]);context.lineTo(points[2],points[3]);context.lineTo(points[4],points[5]);context.closePath();context.fill();
   const item=resources.atlas.items[state.description_item],lines=state.description_item===0&&resources.config.speed===2?resources.atlas.normalSpeedLines:[item.name,...item.lines];context.font=nativeFont(30);context.textAlign='center';context.textBaseline='top';
   for(let i=0;i<lines.length;++i){context.fillStyle=i===0&&state.description_item===0&&resources.config.speed===3?'#f0f':'#000';context.fillText(lines[i],screenWidth-363,145+i*36,690);}context.textBaseline='alphabetic';
   context.restore();
  }
  const intro=runtime.comboIntro;
  if(intro?.combo&&!skipCombos){
   // 乗算をHUDにも適用し、透明な部分は背景側の同じ帯を見せる。
   const [x,y,w,h]=intro.layout.band;if(bandCanvas.width!==w||bandCanvas.height!==h){bandCanvas.width=w;bandCanvas.height=h;}
   const band=bandCanvas.getContext('2d'),sx=canvas.width/screenWidth,sy=canvas.height/640;
   const sample=()=>band.drawImage(canvas,x*sx,y*sy,w*sx,h*sy,0,0,w,h);
   band.globalCompositeOperation='source-over';band.clearRect(0,0,w,h);sample();band.globalCompositeOperation='multiply';band.fillStyle='rgb(40,40,77)';band.fillRect(0,0,w,h);band.globalCompositeOperation='destination-in';sample();context.clearRect(x,y,w,h);context.drawImage(bandCanvas,x,y);
  }
  if(intro?.combo&&intro.layout.age>=6&&!skipCombos){
   const {layout,combo}=intro;context.textAlign='center';context.textBaseline='top';
   context.fillStyle='#fff';context.font=nativeFont(40);context.fillText(combo.name,layout.text_x,layout.text_y[0]);
   context.fillStyle=layout.blink<2?'#ff0':'#f0f';context.font=nativeFont(26);context.fillText(combo.effect,layout.text_x,layout.text_y[1]);
   if(combo.group!==-1){context.fillStyle='#fff';context.fillText(combo.groupName,layout.text_x,layout.text_y[2]);}context.textBaseline='alphabetic';
   sprite('img004_ja',8,...layout.skip);
  }
  if(state.paused&&!state.info_mode){context.fillStyle='rgba(0,0,0,'+(178/255)+')';context.fillRect(0,0,screenWidth,640);for(let i=0;i<view.menu_count;++i){const [atlas,index,x,y,w,h]=view.menu_sprites[i];if(atlas&&index===339)nineSlice('img015',339,340,x,y,w,h);else sprite(atlas?'img015':'img100_ja',index,x,y,w,h);}}
  if(state.info_mode){
   context.fillStyle='rgba(0,0,0,'+(178/255)+')';context.fillRect(0,0,screenWidth,640);slots();
  }
  if(view.info_box[2]){
   nineSlice('img002_ja',48,49,...view.info_box);
   if(state.info_mode||state.hold_frames>=16){
    const slot=state.info_mode?state.info_slot:state.holding,form=resources.forms[slot];context.fillStyle='#fff';context.textAlign='center';context.textBaseline='top';context.font=nativeFont(30);context.fillText(form?.name||'',screenWidth/2,106,920);
    context.textBaseline='alphabetic';
    drawBattleInfo(context,resources,snapshot.formation.slots[slot],slot,screenWidth/2,sprite,tinted);
   }
  }
  if(state.info_mode){
   const [x,y,w,h]=view.slots[state.info_slot],blink=Math.floor(state.ui_frame/2)%2;nineSlice('img015',345+blink*2,346+blink*2,x-1,y-1,112,87);
   nineSlice('img015',341,342,screenWidth/2-461,566,128,63);sprite('img015',344,screenWidth/2-453,580,112,34);
  }
  paintFade();
 }
 function paintFade(){context.fillStyle='#000';for(let i=0;i<view.fade_count;++i){const points=view.fade[i];context.beginPath();for(let p=0;p<view.fade_sizes[i];++p){if(!p)context.moveTo(points[0],points[1]);else context.lineTo(points[p*2],points[p*2+1]);}context.closePath();context.fill();}}
 function coordinates(event){const box=canvas.getBoundingClientRect();return {x:Math.trunc((event.clientX-box.left)*screenWidth/box.width),y:Math.trunc((event.clientY-box.top)*640/box.height)};}
 function inputPoint(event){const point=coordinates(event);return phone&&!state.paused&&!runtime.result?.mode?phoneHudPoint(point,screenWidth,{left:leftInset,right:rightInset},view?.item_icons.filter(item=>item[3]).length??0):point;}
 const cameraPointers=new Set();
 const cameraMotion=createSceneMotion();
 function comboArea(event){const intro=runtime.comboIntro;if(!intro?.combo||intro.layout.age<6||skipCombos)return false;const {x,y}=coordinates(event),[left,top]=intro.layout.skip,[,,w,h]=resources.atlas.atlases.img004_ja.rects[8];return x>=left&&x<=left+w&&y>=top&&y<=top+h;}
 function cameraArea(event){
  if(comboArea(event))return false;
  const {x,y}=coordinates(event);
  const inside=rect=>rect?.[2]>0&&x>=rect[0]&&x<=rect[0]+rect[2]&&y>=rect[1]&&y<=rect[1]+rect[3];
  if(runtime.result?.mode){
   const ending=runtime.ending;
   return ending.phase!==5&&ending.phase!==8&&!inside(runtime.continuePrompt?.layout.panel)&&!inside(runtime.defeatHint?.layout.panel)&&!inside(runtime.endingMap)&&!(ending.ready&&inside(ending.button));
  }
  return y>=134&&y<(state.rows===2?449:543)&&!view?.slots.some(([sx,sy,w,h])=>x>=sx&&x<=sx+w&&y>=sy-1&&y<=sy+h+2);
 }
 const cameraView=()=>battleCameraView(state,runtime,camera,screenWidth);
 const gestures=initializeSceneGestures(canvas,cameraView,value=>{cameraMotion.clear();camera={...camera,...value};++cameraVersion;},{acceptPointer:event=>{if(!cameraArea(event))return false;pointer={...pointer,phase:3};cameraPointers.add(event.pointerId);return true;},acceptWheel:cameraArea,wheelTarget:(...args)=>cameraMotion.zoom(...args)});
 let resultPress;
 function input(event){if(!state.paused&&comboArea(event)){event.preventDefault();if(event.type==='pointerdown')pointer.phase=3;if(event.type==='pointerup'){pointer.phase=3;skipCombos=true;++settingsVersion;}return;}const ended=!!runtime.result?.mode;if(cameraPointers.has(event.pointerId)){if(event.type==='pointerup'||event.type==='pointercancel')cameraPointers.delete(event.pointerId);return;}if(ended&&!runtime.receipt&&!runtime.continuePrompt&&runtime.ending.phase!==5)return;if(state.intro<24||playbackPaused&&!state.paused&&!(cheats&4))return;event.preventDefault();const phase={pointerdown:1,pointerup:2,pointercancel:3,pointermove:4}[event.type];if(phase===4&&!state.pointer_down&&pointer.phase!==1)return;const point=inputPoint(event);pointer={...point,phase:phase===4?4:0};if(phase===1)canvas.setPointerCapture(event.pointerId);if(phase===4)return;
  const command={control:11,phase,...point};
  if(ended&&phase===1){resultPress=sendInput(command);return;}
  if(ended&&resultPress){const pressed=resultPress;resultPress=undefined;pressed.then(()=>{if(!stopped&&!error)sendInput(command);});return;}
  sendInput(command);
 }
 for(const type of ['pointerdown','pointerup','pointercancel','pointermove'])canvas.addEventListener(type,input);
 function wheel(event){if(runtime.result?.mode||state.paused||state.rows!==1||state.intro<24||!event.deltaY)return;const point=coordinates(event);if(point.y<543||point.x<159+(screenWidth-960)/2||point.x>801+(screenWidth-960)/2)return;event.preventDefault();control=event.deltaY>0?9:8;}
 canvas.addEventListener('wheel',wheel,{passive:false});
 function changeAspect(){try{localStorage.setItem('kbcs:battle-aspect',aspect.value);}catch{}resize();}
 aspect.addEventListener('change',changeAspect);
 const observer=new ResizeObserver(resize);
 const enemyPanel=document.getElementById('battle-actor-list'),allyPanel=document.getElementById('battle-actor-detail');
 const display=createBattleDisplay({controls,details:detailsRoot,enemies:enemyPanel,allies:allyPanel,setLarge:setLargeBattle,key,keyup,blur:()=>cameraMotion.clear(),recording});
 const monitor=phone?null:createBattleMonitor(detailsRoot,()=>({...timing,...frames.stats(),frame:state.frame,paints,firstPaint,lastPaint,activeMs,activePaints,cheats,speed:Number(speed.value),fpsLimit:Number(fps.value),lag:accumulator*(state.speed_mode?state.speed_mode+1:1)+stepQueue,images:stageMediaStats(resources.sceneImages)}));
 function command(event){
  const button=event.target.closest('[data-debug],[data-battle-control]');if(!button)return;
  const action=button.dataset.debug;
  if(action==='cheats'){cheatPanel.hidden=!cheatPanel.hidden;button.setAttribute('aria-expanded',String(!cheatPanel.hidden));}
  else if(action==='toggle'){playbackPaused=!(playbackPaused||state.paused);accumulator=0;lastTime=0;lastActivePaint=undefined;if(playbackPaused&&!state.paused){state.pointer_down=0;state.holding=-1;state.hold_frames=0;pointer.phase=0;}if(state.paused&&!playbackPaused)control=1;button.textContent=playbackPaused?'再開':'一時停止';sounds.update([],state.se_level,1,playbackPaused,!!runtime.result.mode);if(audio){if(playbackPaused)audio.pause();else if(audioStarted&&!audio.ended&&!runtime.result.mode)audio.play().catch(()=>{});}}
  else if(action==='step'||action==='ten'){playbackPaused=true;stepQueue+=action==='step'?1:10;accumulator=0;if(state.paused)control=1;}
  else if(action==='menu')control=2;
  else if(action==='rows')control=3;
  else if(action==='page')control=4;
  else if(action==='camera'){camera={...camera,center:snapshot.stage.width,zoom:1};++cameraVersion;}
  else if(action==='large')setLargeBattle(true);
  else if(action==='fullscreen')display.request();
  else if(action==='report'&&monitor){const blob=new Blob([JSON.stringify({gameVersion:snapshot.version,buildId:snapshot.buildId,abi:5,error:failure,textRendering:{...resources.textDiagnostics,notificationRenderer:pixel8TextPreview?'pixel8-canvas-preview':'browser-legacy'},...monitor.snapshot()},null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download='kbcs-diagnostics.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
  else if(action==='return'||button.dataset.battleControl==='return'){stop();onReturn();return;}
  else if(!action)control=Number(button.dataset.battleControl);
 }
 controls.addEventListener('click',command);
 detailsRoot.addEventListener('click',command);
 root.addEventListener('click',command);
 function remote(event){
  const value=event.detail;if(value.id&&value.id!==session)return;
  if(value.type==='observe'){inspectionDirty=true;scheduleUpdate();return;}
  if(value.type==='action'){inspectionDirty=true;lastPhoneStats=-Infinity;}
  if(value.type==='action')controls.querySelector('[data-debug='+CSS.escape(value.action)+']')?.click();
  if(value.type==='setting'){
   const node=controls.querySelector('[data-battle-'+CSS.escape(value.name)+']');
   if(value.name==='cheats'){for(const box of cheatPanel.querySelectorAll('input'))box.checked=!!(Number(value.value)&Number(box.dataset.cheat));cheatPanel.lastElementChild?.querySelector('input')?.dispatchEvent(new Event('change',{bubbles:true}));}
   else if(node){node.value=value.value;node.dispatchEvent(new Event('change',{bubbles:true}));}
  }
  const code=defaultBattleKeys[value.action];
  if(value.type==='key'&&code){
   const input=new KeyboardEvent(value.phase==='up'?'keyup':'keydown',{code,cancelable:true});
   if(value.phase==='up')keyup(input,value.action);else key(input,value.action);
  }
  scheduleUpdate();
 }
 if(phone)document.addEventListener('kbcs:phone-control',remote);
function fail(e){if(!stopped&&!error){error=true;resources.onFailure?.(e.message);failure={frame:state.frame,message:e.message};message.textContent='戦闘停止: '+e.message;message.title=message.textContent;message.setAttribute('role','alert');const shelf=detailsRoot.closest('details');if(shelf)shelf.open=true;if(audio)audio.pause();for(const button of controls.querySelectorAll('button'))button.disabled=!['report','return'].includes(button.dataset.debug);}}
 function sendInput(input){
  const serial=++keySerial;
  return readBattleJson('/api/battle-session/input',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({session,cheats,...input}),signal:requestController.signal}).then(next=>{
   if(stopped)return;
   if(state.battle_mode&&!next.state.battle_mode)return;
   sounds.update(next.sounds,state.se_level,state.speed_mode+1,playbackPaused,!!runtime.result?.mode);
   if(serial===keySerial&&next.state.ui_frame>=state.ui_frame&&next.state.frame>=state.frame){state=next.state;view=next.layout;++cameraVersion;inspector?.refresh();persistOptions();menu.hidden=!state.paused;}
  }).catch(fail);
 }
 function restoreBattleFocus(event){
  if(document.querySelector('dialog:modal')||editableKeyTarget(event.target))return;
  const target=event.type==='change'?event.target.closest?.('select'):event.detail>0&&event.target.closest?.('button,[role="button"],summary,input[type="checkbox"],input[type="radio"]');
  if(target)canvas.focus({preventScroll:true});
 }
 document.addEventListener('click',restoreBattleFocus);
 document.addEventListener('change',restoreBattleFocus);
 function key(event,remoteAction){
  if(event.isComposing||event.ctrlKey||event.altKey||event.metaKey||editableKeyTarget(event.target)||document.querySelector('dialog:modal'))return;
  if(large&&!phone&&event.code==='Escape'){event.preventDefault();event.stopPropagation();if(!event.repeat)display.leave();return;}
  // 2段で切替操作が無効でも、Spaceでフォーカス中の段数ボタンを押さない。
  const bindings=remoteAction?{[remoteAction]:event.code}:keyBindings;
  if(event.code===bindings.page){event.preventDefault();event.stopPropagation();}
  const action=battleKeyAction(event.code,bindings,state);
  if(action?.camera){const view=cameraView();if(!view||error||stopped)return;event.preventDefault();event.stopPropagation();if(action.camera==='cameraReset'){cameraMotion.clear();camera={...camera,center:snapshot.stage.width,zoom:1};++cameraVersion;}else cameraMotion.key(action.camera,true);return;}
  if(event.repeat||state.intro<24||runtime.result?.mode||error||stopped||state.page_frame)return;
  if(state.paused&&event.code!==bindings.options)return;
  if(!action)return;
  if(playbackPaused&&!state.paused&&action.target!==100&&(!(cheats&4)||!Number.isInteger(action.target)||action.target>=10))return;
  event.preventDefault();event.stopPropagation();
  const input=playbackPaused&&action.target===100?2:action.control??1000+action.target;
  sendInput({control:input});
 }
 window.addEventListener('keydown',key,true);
 function keyup(event,remoteAction){const action=battleKeyAction(event.code,remoteAction?{[remoteAction]:event.code}:keyBindings,state);if(action?.camera)cameraMotion.key(action.camera,false);}
 const blur=()=>cameraMotion.clear();
 window.addEventListener('keyup',keyup);window.addEventListener('blur',blur);
 function visibility(){lastTime=lastCameraTime=0;lastActivePaint=undefined;presentation.reset();if(document.hidden){cameraMotion.clear();control=2;}}
 document.addEventListener('visibilitychange',visibility);
 function clockRate(){return state.intro>=24&&!state.paused&&!state.battle_mode?battlePlaybackRate(Number(speed.value),state.speed_mode):1;}
 function accrueClock(now){
  if(document.hidden)return;
  if(lastTime&&(!playbackPaused||state.paused)){
   accumulator=accumulateBattleTicks(accumulator,now-lastTime,clockRate(),fps.value);
  }
  lastTime=now;
 }
 function scheduleUpdate(){
  if(stopped||error||document.hidden)return;
  accrueClock(performance.now());
  if(returnAfterPaint||returnPending||busy||(!phone&&presenting)||pendingScene)return;
  if(Math.floor(accumulator)>0||control||stepQueue||inspectionDirty||drawnVersion!==cameraVersion||appliedSettings!==settingsVersion||playbackPaused&&(cheats&4)&&pointer.phase===2){
   clearTimeout(updateTimer);updateTimer=0;
   busy=true;const stepping=!control&&stepQueue>0,ticks=control?0:stepping?Math.min(30,stepQueue):Math.min(playbackPaused?1:30,Math.floor(accumulator));if(stepping)stepQueue-=ticks;else accumulator-=ticks;
   update(ticks,stepping).catch(fail).finally(()=>{busy=false;queuePresentation();});
  }else if(!updateTimer&&(!playbackPaused||state.paused)){
   // 次の論理Fが貯まる時刻に起こし、requestAnimationFrameだけを待つ数msの遅れを減らす。
   updateTimer=setTimeout(()=>{updateTimer=0;scheduleUpdate();},Math.ceil((1-accumulator)*1000/(30*clockRate())));
  }
 }
 function animate(now){
  if(stopped)return;
  // 暗転を提示した描画機会を1回通してから準備画面へ戻る。
  if(returnAfterPaint&&!--returnAfterPaint){stop();onReturn();return;}
  if(lastCameraTime&&!document.hidden){
   const moved=cameraMotion.step(cameraView(),(now-lastCameraTime)/1000);if(moved){camera={...camera,...moved};++cameraVersion;}
  }lastCameraTime=now;
  queuePresentation();scheduleUpdate();
  if(!error&&!stopped)raf=requestAnimationFrame(animate);
 }
 window.addEventListener('pagehide',stop);
 function stop(){
  if(stopped)return;stopped=true;
  display.stop();
  inspector?.stop();inspector=null;details?.stop();pendingScene=null;
  document.body.classList.remove('battle-large');largeHint.hidden=true;clearTimeout(largeHintTimer);
  detailsRoot.removeEventListener('click',command);results.stop();window.removeEventListener('pagehide',stop);
  signal?.removeEventListener('abort',stop);recording?.detach();if(sessionCreated)fetch('/api/battle-session?'+new URLSearchParams({session}),{method:'DELETE',keepalive:true}).catch(()=>{});
  stageStats.stop();notices.remove();message.removeAttribute('title');message.setAttribute('role','status');messageHome.append(message);
  cancelAnimationFrame(raf);clearTimeout(presentationTimer);clearTimeout(updateTimer);requestController.abort();observer.disconnect();
  aspect.removeEventListener('change',changeAspect);controls.removeEventListener('change',changeSettings);painter.dispose();monitor?.stop();controls.removeEventListener('click',command);
  gestures.dispose();sounds.stop();tints.clear();cameraPointers.clear();canvas.removeEventListener('wheel',wheel);if(audio){audio.pause();audio.removeAttribute('src');}resources.dispose();
  for(const type of ['pointerdown','pointerup','pointercancel','pointermove'])canvas.removeEventListener(type,input);
  root.removeEventListener('click',command);window.removeEventListener('keydown',key,true);window.removeEventListener('keyup',keyup);window.removeEventListener('blur',blur);cameraMotion.clear();
  document.removeEventListener('visibilitychange',visibility);document.removeEventListener('click',restoreBattleFocus);document.removeEventListener('change',restoreBattleFocus);
  document.removeEventListener('kbcs:phone-control',remote);
 }
 signal?.addEventListener('abort',stop,{once:true});
 try{signal?.throwIfAborted();if(largeAtStart)setLargeBattle(true);else resize();observer.observe(canvas.parentElement);
  const sceneInput={...stageSceneInput(snapshot.stage,{center:camera.center,zoom:camera.zoom,showEnemy:true,showPlayer:true,showEffects:true,session}),viewportWidth:screenWidth};
  const started=await readBattleJson('/api/battle-session',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({snapshot,config:resources.config,state,scene:sceneInput}),signal:requestController.signal});sessionCreated=true;
  phoneTextures=started.textures;
  const preparation=[prepareBattleImages(started.textures,resources.sceneImages,requestController.signal,phone?resources.report:undefined,resources.mediaVersion)];
  if(phone){
   const ids=resources.atlas.sounds.flatMap((sound,id)=>sound.bgm?[]:[id]);
   preparation.push(sounds.preload([...new Set([...ids,...started.audio.se])],resources.report),resources.preloadMusic(started.audio.music));
  }
  await Promise.all(preparation);
  requestController.signal.throwIfAborted();
  const prepared=phone?null:await prepareInspectorAssets(started.inspectionAssets,started.textures,resources.sceneImages,resources.database,requestController.signal);
  // 最初の出現時にGPU転送が集中しないよう、暗転中の転送量に上限を設ける。
  const textures=phone?started.textures:started.inspectionAssets.profiles.flatMap(profile=>[profile.idle,profile.kb,profile.soul].map(pose=>started.textures[pose?.texture]));
  timing.warmTextureBytes=painter.warmTextures(textures,32*1024*1024);
  const requestInspection=()=>{inspectionDirty=true;};
  if(prepared){
   details=createBattleDetails(detailsRoot,prepared,resources.sceneImages,requestInspection);
   inspector=createBattleInspector(enemyPanel,allyPanel,prepared,resources.database,resources.enemies,requestInspection,id=>details.select(id));
  }
  recording?.attach({name:snapshot.map.key+'-'+(snapshot.stage.index+1),size:()=>[screenWidth,640],audio:()=>sounds.recordAudio(),redraw:requestInspection,button:controls.querySelector('[data-recording]')});
  await update(0);await present();if(large)showLargeHint();raf=requestAnimationFrame(animate);}catch(error){stop();throw error;}
 return {stop};
}
