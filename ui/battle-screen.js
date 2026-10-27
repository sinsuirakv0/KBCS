import {createBattleResults} from './battle-results.js';
import {createBattleSounds} from './battle-audio.js';
import {readBattleJson,battleItems} from './battle-support.js';
import {catalog} from './simulation-profile.js';
import {stageSceneInput,createStagePainter,stageMediaStats} from './src/features/stages/native-media.js';
import {createBattleMonitor} from './battle-monitor.js';
import {createBattleFrameClient} from './battle-frame.js';
import {initializeSceneGestures} from './src/features/stages/scene-controls.js';

function configuration(database,snapshot){
 const {formation,map,items,deployment}=snapshot,profile=formation.profile;
 const facility=id=>{const v=profile.facilities[id];return v.level+v.plus-1;};
 const treasure=type=>catalog.treasures.filter(v=>v.effectType===type&&!v.effectFlag).reduce((sum,v)=>sum+Math.trunc(v.maximumEffect*profile.treasures[v.id]/100),0);
 const team=new Map(formation.slots.slice(0,5).filter(Boolean).map(v=>[v.unitId,v.form]));
 const combo=type=>database.combos.filter(v=>v.type===type&&v.members.every(m=>team.has(m.id)&&team.get(m.id)>=m.form)).reduce((sum,v)=>sum+database.comboEffects[type].values[v.grade],0);
 const rule=(map.rules||[]).find(v=>v.id===0),mask=battleItems.reduce((bits,v,index)=>bits|(items[v.key]?1<<index:0),0);
 return {config:{worker_level:facility('worker'),wallet_level:facility('wallet'),attack_level:facility('cannonAttack'),charge_level:facility('cannonCharge'),chapter:['EOC','EOCZ'].includes(map.series)?map.number:3,income_treasure:treasure(3),wallet_treasure:treasure(4),charge_treasure:treasure(1),speed_treasure:treasure(17),income_combo:combo(8),wallet_combo:combo(9),charge_combo:combo(7),charge_start_combo:combo(3),items:mask,speed:snapshot.speed===2?2:3,fixed_money:rule?rule.parameters[0]*100:-1,costs:deployment.slots.map(v=>v.cost),present:formation.slots.map(v=>Number(!!v)),blocked:deployment.slots.map(v=>v.reasons)},worker:items.rich||rule?7:Math.min(7,combo(4)),money:rule?rule.parameters[0]*100:combo(5)*100};
}
export async function prepareBattleScreen(database,snapshot,assets,signal,report){
 const [atlas,options]=await Promise.all([readBattleJson('/images/native-battle/manifest.json',{signal}),readBattleJson('/api/battle-options',{signal})]);
 if(atlas.version!==snapshot.version)throw Error('戦闘UI素材とDBの版が異なります');
 if(atlas.buildId!==snapshot.buildId){
  const sources=Object.values(atlas.atlases).flatMap(value=>Object.entries(value.sources)).concat([[atlas.soundSource.path,atlas.soundSource]]),paths=[...new Set(sources.map(([path])=>path))];
  const hashes=await readBattleJson('/api/asset-hashes',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(paths),signal});
  if(sources.some(([path,source])=>hashes[path]!==source.sha256))throw Error('戦闘UI素材とDBの原本が異なります');
 }
 const forms=snapshot.formation.slots.map(member=>member&&database.units.find(v=>v.id===member.unitId)?.forms.find(v=>v.index===member.form));
 const atlasUrls=new Map(Object.values(atlas.atlases).map(v=>[v.image,v.url]));
 const paths=[...new Set([...Object.values(atlas.atlases).map(v=>v.image),...forms.filter(Boolean).map(v=>v.icon)])];
 let count=0;
 const images=new Map();
 for(const path of paths){signal.throwIfAborted();const image=assets.images.get(path)||new Image();if(!image.src)image.src=atlasUrls.get(path)||'/api/asset/'+path;try{await image.decode();}catch{throw Error('戦闘UI画像を読み込めません：'+path);}signal.throwIfAborted();images.set(path,image);report('戦闘UI',++count,paths.length);}
 const values=configuration(database,snapshot);values.config.description_lines=forms.map(form=>Math.min(3,Array.isArray(form?.description)?form.description.filter(Boolean).length:form?.description?String(form.description).split('\n').filter(Boolean).length:0));
 const audioUrls=new Map(),audioErrors=new Map(),audioController=new AbortController();
 const dispose=()=>{audioController.abort();for(const url of audioUrls.values())URL.revokeObjectURL(url);audioUrls.clear();};
 signal.addEventListener('abort',dispose,{once:true});
 async function loadAudio(track){
  if(audioUrls.has(track.id))return;
  const response=await fetch('/api/stage-audio/'+track.id,{signal:audioController.signal});
  if(!response.ok){const error=await response.json();throw Error(error.error||'BGM '+track.id+' を読み込めません');}
  const blob=await response.blob();audioController.signal.throwIfAborted();audioUrls.set(track.id,URL.createObjectURL(blob));
 }
 const tracks=snapshot.stage.musicTracks||[];
 try{if(tracks[0]){await loadAudio(tracks[0]);report('開始BGM',1,1);}}
 catch(error){dispose();signal.removeEventListener('abort',dispose);throw error;}
 // 後の曲の取得は開始を待たせない。将来の切替入口は読込完了を確認する。
 Promise.all(tracks.slice(1).map(async track=>{try{await loadAudio(track);}catch(error){if(error.name!=='AbortError')audioErrors.set(track.id,error.message);}}));
 return {atlas,options,forms,images,sceneImages:assets.images,audioUrls,audioErrors,dispose:()=>{signal.removeEventListener('abort',dispose);dispose();},...values};
}
export async function startBattleScreen(root,canvas,scene,snapshot,resources,onReturn){
 let screenWidth=960,camera=scene.layout,cameraVersion=0,drawnVersion=-1,drawnRows=0;
 const backgroundCanvas=root.querySelector('[data-battle-background]'),controls=document.getElementById('battle-controls'),session=crypto.randomUUID();
 let painter;try{painter=createStagePainter(backgroundCanvas,()=>++cameraVersion,resources.sceneImages);}catch(error){resources.dispose();throw error;}
 let playbackPaused=false,stepQueue=0,paints=0;
 const timing={coreMs:0,apiMs:0,computeMs:0,drawMs:0},frames=createBattleFrameClient();
 const context=canvas.getContext('2d'),message=root.querySelector('[data-battle-message]'),menu=root.querySelector('[data-battle-menu]');
 const messageHome=message.parentElement;controls.querySelector('.battle-stats').prepend(message);
 message.textContent='';
 const labels=resources.forms.map(v=>v?.name||'空き枠');
 let state={frame:0,intro:12,rows:2,page:0,page_frame:0,page_direction:1,paused:0,money:resources.money,worker:resources.worker,cannon:0,holding:-1,hold_frames:0,pointer_down:0,pointer_x:0,pointer_y:0,guard:0,pending_control:-1,items_on:resources.config.items,request_slot:-1,request_cannon:0,ui_frame:0,speed_mode:(resources.config.items&1)?1:0,wallet_flash:0,description_item:-1,description_wait:0,start_x:0,start_y:0,gesture:0,page_step:1,request_action:0,bgm_level:3,se_level:3,vibration_on:0,info_mode:0,info_slot:0,saved_rows:2,hud_frame:0};
 let runtime={wait:Array(10).fill(0),maximum:Array(10).fill(0)},sessionCreated=false;
 Object.assign(state,{rows:resources.options.rows,saved_rows:resources.options.rows,bgm_level:resources.options.bgmLevel,se_level:resources.options.seLevel});
 let savedOptions=JSON.stringify(resources.options),saveOptions=Promise.resolve();
 function persistOptions(){
  const body=JSON.stringify({bgmLevel:state.bgm_level,seLevel:state.se_level,rows:state.info_mode?state.saved_rows:state.rows});
  if(body===savedOptions)return;savedOptions=body;
  saveOptions=saveOptions.then(()=>readBattleJson('/api/battle-options',{method:'PUT',headers:{'Content-Type':'application/json'},body,keepalive:true})).catch(error=>{savedOptions='';if(!stopped)message.textContent='設定保存: '+error.message;});
 }
 const actorsInfo=document.createElement('span');actorsInfo.className='battle-actor-info';controls.querySelector('.battle-stats').append(actorsInfo);
 const resultInfo=document.createElement('output');resultInfo.setAttribute('aria-live','polite');controls.querySelector('.battle-actions').append(resultInfo);
 const limitInfo=document.createElement('span');controls.querySelector('.battle-stats').append(limitInfo);
 let view,stopped=false,raf=0,busy=false,lastTime=0,accumulator=0,pointer={phase:0,x:0,y:0},control=0,error=false,failure=null;
 const requestController=new AbortController();
 let audio=null,audioId=-1;
 let audioStarted=false;
 function music(){
  const id=runtime.music?.id??-1;
  if(id!==audioId){if(audio){audio.pause();audio.removeAttribute('src');}audio=null;audioStarted=false;audioId=id;}
  if(id>=0&&!audio&&resources.audioUrls.has(id)){audio=new Audio(resources.audioUrls.get(id));audio.loop=resources.atlas.sounds[id]?.loop??true;}
  if(!audio)return;audio.muted=!state.bgm_level;audio.volume=[0,.25,.5,1][state.bgm_level];
  if(playbackPaused||runtime.result.mode)audio.pause();else if(audio.paused&&!audio.ended&&state.bgm_level){audioStarted=true;audio.play().catch(()=>{});}
 }
 const sounds=createBattleSounds(resources.audioErrors,resources.atlas.sounds),tints=new Map();
 const results=createBattleResults(controls);
 sounds.preload([8,9,10,11,15,19,20,21,22,23,24,25,26,27,28,29,37,44,45,50,57,59,60,61,65,70,71,72,73,74,84,85,86,90,105,106,110,111,112,124,137,138,139,159,162,167,168,169,188,189,194]);
 function tinted(image,cut,color,key){
  if(!tints.has(key)){const surface=document.createElement('canvas');surface.width=cut[2];surface.height=cut[3];const paint=surface.getContext('2d');paint.drawImage(image,...cut,0,0,cut[2],cut[3]);paint.globalCompositeOperation='multiply';paint.fillStyle='rgb('+color.join(',')+')';paint.fillRect(0,0,surface.width,surface.height);paint.globalCompositeOperation='destination-in';paint.drawImage(image,...cut,0,0,cut[2],cut[3]);tints.set(key,surface);}return tints.get(key);
 }
 function resize(){
  const box=canvas.parentElement.getBoundingClientRect(),width=Math.max(960,Math.min(3840,Math.round(box.width/Math.max(1,box.height)*640)));
  if(width===screenWidth&&canvas.width===width&&backgroundCanvas.width===width)return;
  screenWidth=width;resources.config.viewport_width=width;canvas.width=width;canvas.height=640;canvas.style.width='min(100cqw,'+(width/640*100)+'cqh)';backgroundCanvas.width=width;backgroundCanvas.height=640;backgroundCanvas.style.width=canvas.style.width;++cameraVersion;
 }
 async function drawScene(next,version){
  if(!next||stopped)return;timing.computeMs=next.computeMs;
  const drawing=performance.now();if(!await painter.paint(next))return;timing.drawMs=performance.now()-drawing;
  if(stopped)return;scene=next;drawnVersion=version;drawnRows=state.rows;
  // 操作中の新しい要求は古い描画応答で上書きしない。
  if(version===cameraVersion)camera=next.layout;
 }
 async function update(ticks,stepping=false){
  const input=stepping?{ticks,phase:0,x:0,y:0,control:10}:{ticks,...pointer,control};if(ticks)pointer.phase=0;control=0;
  const version=cameraVersion;
  const sceneInput=stageSceneInput(snapshot.stage,{center:camera.center,zoom:camera.zoom,showEnemy:true,showPlayer:true,showEffects:true,session});
  const {value:next,timing:measured}=await frames.load({session,input,scene:{...sceneInput,viewportWidth:screenWidth}},requestController.signal);
  Object.assign(timing,measured);timing.coreMs=next.coreMs;
  if(stopped)return;state=next.state;view=next.layout;runtime=next.runtime;
  persistOptions();
  results.update(runtime);
  sounds.update(runtime.sounds||[],state.se_level,state.speed_mode+1,playbackPaused&&!stepping,!!runtime.result.mode);
  actorsInfo.textContent='味方 '+runtime.units+' / 敵 '+runtime.enemies+'　城 '+runtime.castleHp.map(value=>value.toLocaleString()).join(' / ');
  const result=runtime.result,rules=runtime.rules,finished=!!result.mode;
  resultInfo.textContent=[result.reason===3?(result.mode===1?'時間終了（勝利）':'時間終了'):result.mode===1?'勝利':result.reason===2?'敗北':'',rules.scoreType===1||rules.scoreType===3||rules.scoreType===2&&finished||rules.nativeKind===-6&&finished?(rules.scoreType===3?'Pt ':'Score ')+result.score.toLocaleString():'',(rules.scoreType===1||rules.scoreType===3)?'残り '+(Math.max(0,rules.timeLimit-result.timer)/30).toFixed(2)+'秒':''].filter(Boolean).join('　');
  limitInfo.textContent=[!finished&&runtime.points.wait>0?'フィーバー '+(runtime.points.wait/30).toFixed(1)+'秒':'',runtime.extras.length?'追加生産 待機 '+runtime.extras.length:'',rules.totalLimit>=0?'総生産 '+runtime.deployment.total+' / '+rules.totalLimit:'',...rules.rarityLimits.flatMap((limit,i)=>limit>0?['同時 '+['基本','EX','レア','激レア','超激レア','伝説レア'][i]+' '+runtime.deployment.active[i]+' / '+limit]:[])].join('　');
  if(state.request_slot>=0)message.textContent='';
  if(state.request_cannon)message.textContent='にゃんこ砲を発射';
  menu.hidden=!state.paused;
  music();
  if(state.request_action===301)window.open('https://kbc-rakv0.pages.dev/information/appli/battlecats/help/index.html','_blank','noopener');
  if(state.request_action===302){stop();onReturn();return;}
  for(const button of controls.querySelectorAll('button'))button.disabled=false;
  controls.querySelector('[data-battle-clock]').textContent=state.frame+'F / '+(state.frame/30).toFixed(2)+'秒';
  controls.querySelector('[data-debug=toggle]').textContent=playbackPaused||state.paused?'再開':'一時停止';
  controls.querySelector('[data-debug=rows]').textContent=state.rows===2?'2段':'1段';
  controls.querySelector('[data-debug=page]').disabled=state.rows===2||finished;
  for(const key of ['menu','rows','camera'])controls.querySelector('[data-debug='+key+']').disabled=finished;
  for(const button of controls.querySelectorAll('[data-debug=step],[data-debug=ten]'))button.disabled=state.intro<24;
  if(playbackPaused&&!state.paused){state.pointer_down=0;state.holding=-1;state.hold_frames=0;pointer.phase=0;if(!stepping)accumulator=0;}
  await drawScene(next.scene,version);
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
  if(runtime.result?.mode&&runtime.ending.phase){results.paint(context,screenWidth,sprite,number,resources.atlas,resources.images);return;}
  const moneyBase=view.money_base,moneyRight=screenWidth-34,capX=number(view.wallet_max/100,moneyBase,moneyRight,10),slashX=capX-29;
  sprite('img001_ja',moneyBase+10,slashX,10);number(state.money/100,moneyBase,slashX-1,10);sprite('img001_ja',moneyBase+11,moneyRight,10);
  // 005d0508は後ろのページを先に描き、選択ページを重ねる。
  function slots(){
  const order=view.order;
  for(const index of order){const [x,y,w,h]=view.slots[index],form=resources.forms[index];
   if(!form){sprite('uni',0,x,y,w,h);if(view.modes[index]===2){context.fillStyle='rgba(0,0,0,.392)';context.fillRect(x,y,w,h);}continue;}
   const summon=runtime.hud.summons[index],image=resources.images.get(form.icon);if(summon[0]&&summon[1])context.drawImage(tinted(image,[9,21,110,85],[157,215,255],form.icon),x,y,w,h);else context.drawImage(image,9,21,110,85,x,y,w,h);
   const cost=runtime.costs[index],disabled=state.battle_mode||runtime.deployment.blocked[index]||(summon[0]?!summon[1]:cost>state.money||runtime.wait[index]>0),base=disabled?46:35;
   if(disabled||view.modes[index]===2){context.fillStyle='rgba(0,0,0,.392)';context.fillRect(x,y,w,h);}
   if(summon[0]&&summon[1]){const cut=resources.atlas.atlases.img002_ja.rects[53],[sx,sy]=view.labels[index];context.drawImage(tinted(resources.images.get(resources.atlas.atlases.img002_ja.image),cut,[summon[4],summon[4],summon[4]],'summon-'+summon[4]),sx+Math.trunc((110-cut[2])/2),sy+Math.trunc((85-cut[3])/2));}
   const gauge=runtime.hud.gauges[index];
   if(gauge[2]){
    const [gx,gy,,cyan,red]=gauge;context.fillStyle='#000';context.fillRect(gx,gy,97,14);
    context.fillStyle='#f00';context.fillRect(gx+2,gy+2,red,10);context.fillStyle='#0ff';context.fillRect(gx+2,gy+2,cyan,10);
   }else if(!summon[0]){const [labelX,labelY]=view.labels[index];number(Math.trunc(cost/100),base,labelX+94,labelY+62,-3);sprite('img001_ja',disabled?56:45,labelX+94,labelY+62,22,26);}
  }
  }
  slots();
  const canUpgrade=state.worker<7&&state.money>=view.upgrade_cost;
  sprite('img002_ja',view.wallet_base,-48,519);
  if(state.worker===7){sprite('img001_ja',81,4,611);sprite('img001_ja',13,4,510);sprite('img001_ja',22,73,510);}
  else {const base=canUpgrade?35:46,digits=String(Math.trunc(view.upgrade_cost/100)),right=4+[...digits].reduce((sum,v)=>sum+resources.atlas.atlases.img001_ja.rects[base+Number(v)][2]-3,3);number(view.upgrade_cost/100,base,right,611,-3);sprite('img001_ja',canUpgrade?45:56,right,611,22,26);sprite('img001_ja',canUpgrade?13:24,4,510);sprite('img001_ja',(canUpgrade?15:26)+state.worker,73,510);}
  if(view.cannon_base>=0)sprite('img002_ja',view.cannon_base,screenWidth-146,510);
  for(let i=0;i<view.cannon_bands;++i)sprite('img002_ja',11+i,screenWidth-146,i===9?510:628-i*12);if(view.cannon_label>=0)sprite('img002_ja',view.cannon_label,screenWidth-129,581);
  sprite('img002_ja',2,...view.pause_icon);
  const hud=runtime.hud,scale=hud.scale;
  for(let side=0;side<2;++side){
   const [x,y]=hud.anchors[side],[hp,maximum,unknown]=hud.health[side];
   if(unknown){const cut=resources.atlas.atlases.img001_ja.rects[108];for(let i=0;i<7;++i){sprite('img001_ja',108,x-(7-i)*cut[2]*scale,y,cut[2]*scale,cut[3]*scale);sprite('img001_ja',108,x+(18+i*cut[2])*scale,y,cut[2]*scale,cut[3]*scale);}}
   else{number(hp,57,x,y,0,scale);number(maximum,57,x+18*scale,y,0,scale,true);}
   sprite('img001_ja',67,x,y,18*scale,18*scale);
  }
  for(const icon of view.item_icons)if(icon[3])sprite('mapicon',...icon);
  if(view.description_box[2]){
   context.fillStyle='rgba(255,255,255,'+(216/255)+')';context.fillRect(...view.description_box);context.beginPath();const points=view.description_arrow;context.moveTo(points[0],points[1]);context.lineTo(points[2],points[3]);context.lineTo(points[4],points[5]);context.closePath();context.fill();
   const item=resources.atlas.items[state.description_item],lines=state.description_item===0&&resources.config.speed===2?resources.atlas.normalSpeedLines:[item.name,...item.lines];context.font='30px sans-serif';context.textAlign='center';context.textBaseline='top';
   for(let i=0;i<lines.length;++i){context.fillStyle=i===0&&state.description_item===0&&resources.config.speed===3?'#f0f':'#000';context.fillText(lines[i],screenWidth-363,145+i*36,690);}context.textBaseline='alphabetic';
  }
  if(state.paused&&!state.info_mode){context.fillStyle='rgba(0,0,0,'+(178/255)+')';context.fillRect(0,0,screenWidth,640);for(let i=0;i<view.menu_count;++i){const [atlas,index,x,y,w,h]=view.menu_sprites[i];if(atlas&&index===339)nineSlice('img015',339,340,x,y,w,h);else sprite(atlas?'img015':'img100_ja',index,x,y,w,h);}}
  if(state.info_mode){
   context.fillStyle='rgba(0,0,0,'+(178/255)+')';context.fillRect(0,0,screenWidth,640);slots();
   nineSlice('img002_ja',48,49,...view.info_box);
   const form=resources.forms[state.info_slot];context.fillStyle='#fff';context.textAlign='center';context.textBaseline='top';context.font='30px sans-serif';context.fillText(form?.name||'',screenWidth/2,106,920);
   const lines=Array.isArray(form?.description)?form.description:String(form?.description||'').split('\n');for(let i=0;i<Math.min(3,lines.length);++i)context.fillText(lines[i],screenWidth/2,263+i*39,920);context.textBaseline='alphabetic';
   const [x,y,w,h]=view.slots[state.info_slot],blink=Math.floor(state.ui_frame/2)%2;nineSlice('img015',345+blink*2,346+blink*2,x-1,y-1,112,87);
   nineSlice('img015',341,342,screenWidth/2-461,566,128,63);sprite('img015',344,screenWidth/2-453,580,112,34);
  }
  if(state.holding>=0&&state.hold_frames>=14){const text=labels[state.holding];context.fillStyle='rgba(0,0,0,.9)';context.fillRect(200,305,560,52);context.fillStyle='#fff';context.font='24px sans-serif';context.textAlign='center';context.fillText(text,480,340,530);}
  context.fillStyle='#000';for(let i=0;i<view.fade_count;++i){const points=view.fade[i];context.beginPath();for(let p=0;p<view.fade_sizes[i];++p){if(!p)context.moveTo(points[0],points[1]);else context.lineTo(points[p*2],points[p*2+1]);}context.closePath();context.fill();}
 }
 function coordinates(event){const box=canvas.getBoundingClientRect();return {x:Math.trunc((event.clientX-box.left)*screenWidth/box.width),y:Math.trunc((event.clientY-box.top)*640/box.height)};}
 const cameraPointers=new Set();
 function cameraArea(event){const {x,y}=coordinates(event);return y>=134&&y<(state.rows===2?449:543)&&!view?.slots.some(([sx,sy,w,h])=>x>=sx&&x<=sx+w&&y>=sy-1&&y<=sy+h+2);}
 const gestures=initializeSceneGestures(canvas,()=>state.intro>=24&&!state.paused&&!runtime.result?.mode?{...camera,viewport_width:screenWidth,maximum:1}:null,value=>{camera={...camera,...value};++cameraVersion;},{acceptPointer:event=>{if(!cameraArea(event))return false;pointer={...pointer,phase:3};cameraPointers.add(event.pointerId);return true;},acceptWheel:cameraArea});
 function input(event){if(runtime.result?.mode&&!runtime.receipt)return;if(cameraPointers.has(event.pointerId)){if(event.type==='pointerup'||event.type==='pointercancel')cameraPointers.delete(event.pointerId);return;}if(state.intro<24||playbackPaused&&!state.paused)return;event.preventDefault();const phase={pointerdown:1,pointerup:2,pointercancel:3,pointermove:4}[event.type];if(phase===4&&!state.pointer_down&&pointer.phase!==1)return;pointer={...coordinates(event),phase};if(phase===1)canvas.setPointerCapture(event.pointerId);}
 for(const type of ['pointerdown','pointerup','pointercancel','pointermove'])canvas.addEventListener(type,input);
 function wheel(event){if(runtime.result?.mode||state.paused||state.rows!==1||state.intro<24||!event.deltaY)return;const point=coordinates(event);if(point.y<543||point.x<159+(screenWidth-960)/2||point.x>801+(screenWidth-960)/2)return;event.preventDefault();control=event.deltaY>0?9:8;}
 canvas.addEventListener('wheel',wheel,{passive:false});
 const observer=new ResizeObserver(resize);
 const monitor=createBattleMonitor(controls,()=>({...timing,...frames.stats(),frame:state.frame,paints,lag:accumulator*(state.speed_mode?state.speed_mode+1:1)+stepQueue,images:stageMediaStats(resources.sceneImages)}));
 function command(event){
  const button=event.target.closest('[data-debug],[data-battle-control]');if(!button)return;
  const action=button.dataset.debug;
  if(action==='toggle'){playbackPaused=!(playbackPaused||state.paused);accumulator=0;lastTime=0;if(playbackPaused&&!state.paused){state.pointer_down=0;state.holding=-1;state.hold_frames=0;pointer.phase=0;}if(state.paused&&!playbackPaused)control=1;button.textContent=playbackPaused?'再開':'一時停止';sounds.update([],state.se_level,1,playbackPaused,!!runtime.result.mode);if(audio){if(playbackPaused)audio.pause();else if(audioStarted&&!audio.ended&&!runtime.result.mode)audio.play().catch(()=>{});}}
  else if(action==='step'||action==='ten'){playbackPaused=true;stepQueue+=action==='step'?1:10;accumulator=0;if(state.paused)control=1;}
  else if(action==='menu')control=2;
  else if(action==='rows')control=3;
  else if(action==='page')control=4;
  else if(action==='camera'){camera={...camera,center:snapshot.stage.width,zoom:1};++cameraVersion;}
  else if(action==='report'){const blob=new Blob([JSON.stringify({version:'0.1.34',gameVersion:snapshot.version,buildId:snapshot.buildId,abi:4,error:failure,...monitor.snapshot()},null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download='kbcs-diagnostics.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
  else if(action==='return'||button.dataset.battleControl==='return'){stop();onReturn();return;}
  else if(!action)control=Number(button.dataset.battleControl);
 }
 controls.addEventListener('click',command);
 root.addEventListener('click',command);
 function key(event){if(event.key==='Escape'){event.preventDefault();control=state.paused?1:2;}}
 window.addEventListener('keydown',key);
 function visibility(){if(document.hidden)control=2;}
 document.addEventListener('visibilitychange',visibility);
 async function animate(now){
  if(stopped)return;
  if(lastTime&&!document.hidden&&(!playbackPaused||state.paused))accumulator+=(now-lastTime)*30/1000;lastTime=now;
  if(!busy&&(Math.floor(accumulator)>0||control||stepQueue||drawnVersion!==cameraVersion)){
   busy=true;const stepping=!control&&stepQueue>0,ticks=control?0:stepping?Math.min(30,stepQueue):Math.min(playbackPaused?1:30,Math.floor(accumulator));if(stepping)stepQueue-=ticks;else accumulator-=ticks;
   try{await update(ticks,stepping);paint();}catch(e){if(!stopped){error=true;failure={frame:state.frame,message:e.message};message.textContent='戦闘停止: '+e.message;message.title=message.textContent;message.setAttribute('role','alert');if(audio)audio.pause();for(const button of controls.querySelectorAll('button'))button.disabled=!['report','return'].includes(button.dataset.debug);}}finally{busy=false;}
  }
  if(!error&&!stopped)raf=requestAnimationFrame(animate);
 }
 window.addEventListener('pagehide',stop);
 function stop(){if(stopped)return;results.stop();window.removeEventListener('pagehide',stop);stopped=true;if(sessionCreated)fetch('/api/battle-session?'+new URLSearchParams({session}),{method:'DELETE',keepalive:true}).catch(()=>{});actorsInfo.remove();resultInfo.remove();limitInfo.remove();messageHome.append(message);cancelAnimationFrame(raf);requestController.abort();observer.disconnect();painter.dispose();monitor.stop();controls.removeEventListener('click',command);gestures.dispose();sounds.stop();tints.clear();cameraPointers.clear();canvas.removeEventListener('wheel',wheel);if(audio){audio.pause();audio.removeAttribute('src');}resources.dispose();for(const type of ['pointerdown','pointerup','pointercancel','pointermove'])canvas.removeEventListener(type,input);root.removeEventListener('click',command);window.removeEventListener('keydown',key);document.removeEventListener('visibilitychange',visibility);}
 try{resize();observer.observe(canvas.parentElement);
  const sceneInput={...stageSceneInput(snapshot.stage,{center:camera.center,zoom:camera.zoom,showEnemy:true,showPlayer:true,showEffects:true,session}),viewportWidth:screenWidth};
  const started=await readBattleJson('/api/battle-session',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({snapshot,config:resources.config,state,scene:sceneInput}),signal:requestController.signal});sessionCreated=true;
  await Promise.all([...new Set(started.textures)].filter(path=>path&&!resources.sceneImages.has(path)).map(async path=>{const image=new Image();image.src='/api/asset/'+path;try{await image.decode();}catch{throw Error('戦闘画像を読み込めません: '+path);}requestController.signal.throwIfAborted();resources.sceneImages.set(path,image);}));
  await update(0);paint();raf=requestAnimationFrame(animate);}catch(error){stop();throw error;}
 return {stop};
}
