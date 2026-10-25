import {readBattleJson,battleItems} from './battle-support.js';
import {catalog} from './simulation-profile.js';
import {loadStageScene,paintStageScene} from './src/features/stages/native-media.js';
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
 const atlas=await readBattleJson('/images/native-battle/manifest.json',{signal});
 if(atlas.version!==snapshot.version)throw Error('戦闘UI素材とDBの版が異なります');
 if(atlas.buildId!==snapshot.buildId){
  const sources=Object.values(atlas.atlases).flatMap(value=>Object.entries(value.sources)),paths=[...new Set(sources.map(([path])=>path))];
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
 const audioUrls=new Map();
 const dispose=()=>{for(const url of audioUrls.values())URL.revokeObjectURL(url);audioUrls.clear();};
 signal.addEventListener('abort',dispose,{once:true});
 try{for(const track of snapshot.stage.musicTracks||[]){
  signal.throwIfAborted();if(audioUrls.has(track.id))continue;
  const response=await fetch('/api/stage-audio/'+track.id,{signal});
  if(!response.ok){const error=await response.json();throw Error(error.error||'BGM '+track.id+' を読み込めません');}
  const blob=await response.blob();signal.throwIfAborted();audioUrls.set(track.id,URL.createObjectURL(blob));report('BGM',audioUrls.size,snapshot.stage.musicTracks.length);
 }}catch(error){dispose();signal.removeEventListener('abort',dispose);throw error;}
 return {atlas,forms,images,audioUrls,dispose:()=>{signal.removeEventListener('abort',dispose);dispose();},...values};
}
export async function startBattleScreen(root,canvas,scene,snapshot,resources,onReturn){
 let background=document.createElement('canvas'),sceneBuffer=document.createElement('canvas'),screenWidth=960,camera=scene.layout,cameraVersion=0,drawnVersion=-1,drawnFrame=-1,drawnRows=0;
 const context=canvas.getContext('2d'),message=root.querySelector('[data-battle-message]'),menu=root.querySelector('[data-battle-menu]');
 message.textContent='';
 const labels=resources.forms.map(v=>v?.name||'空き枠');
 let state={frame:0,intro:12,rows:2,page:0,page_frame:0,page_direction:1,paused:0,money:resources.money,worker:resources.worker,cannon:0,holding:-1,hold_frames:0,pointer_down:0,pointer_x:0,pointer_y:0,guard:0,pending_control:-1,items_on:resources.config.items,request_slot:-1,request_cannon:0,ui_frame:0,speed_mode:(resources.config.items&1)?1:0,wallet_flash:0,description_item:-1,description_wait:0,start_x:0,start_y:0,gesture:0,page_step:1,request_action:0,bgm_level:3,se_level:3,vibration_on:0,info_mode:0,info_slot:0,saved_rows:2,hud_frame:0};
 let view,stopped=false,raf=0,busy=false,lastTime=0,accumulator=0,pointer={phase:0,x:0,y:0},control=0,error=false;
 const requestController=new AbortController();
 const track=snapshot.stage.musicTracks?.[0],audio=track?new Audio(resources.audioUrls.get(track.id)):null;
 let audioStarted=false;if(audio)audio.loop=track.loop!==false;
 function resize(){
  const box=canvas.parentElement.getBoundingClientRect(),width=Math.max(960,Math.min(3840,Math.round(box.width/Math.max(1,box.height)*640)));
  if(width===screenWidth&&canvas.width===width)return;
  screenWidth=width;resources.config.viewport_width=width;canvas.width=width;canvas.height=640;canvas.style.width='min(100cqw,'+(width/640*100)+'cqh)';++cameraVersion;
 }
 async function drawScene(){
  if(drawnVersion===cameraVersion&&drawnRows===state.rows&&(!scene.animated||drawnFrame===state.frame))return;
  const version=cameraVersion,rows=state.rows,frame=state.frame,width=screenWidth;
  const next=await loadStageScene(snapshot.stage,{frame,center:camera.center,zoom:camera.zoom,showEnemy:true,showPlayer:true,showEffects:true,viewportWidth:width,battleRows:rows});
  if(stopped)return;
  if(sceneBuffer.width!==width||sceneBuffer.height!==640){sceneBuffer.width=width;sceneBuffer.height=640;}await paintStageScene(sceneBuffer,next);
  if(stopped)return;[background,sceneBuffer]=[sceneBuffer,background];scene=next;drawnVersion=version;drawnFrame=frame;drawnRows=rows;
  // 操作中の新しい要求は古い描画応答で上書きしない。
  if(version===cameraVersion)camera=next.layout;
 }
 async function update(ticks){
  const input={ticks,...pointer,control};if(ticks)pointer.phase=0;control=0;
  const next=await readBattleJson('/api/battle-screen',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({config:resources.config,state,input}),signal:requestController.signal});
  if(stopped)return;state=next.state;view=next.layout;
  // 実個体生成の成否をまだ確認できないため、残高・再生産待機を確定しない。
  if(state.request_slot>=0)message.textContent=labels[state.request_slot]+'：出撃要求（個体生成は未接続）';
  if(state.request_cannon)message.textContent='にゃんこ砲：発射要求（攻撃処理は未接続）';
  menu.hidden=!state.paused;
  if(audio){if(state.intro>=24&&!audioStarted&&state.bgm_level){audioStarted=true;audio.play().catch(()=>{});}audio.muted=!state.bgm_level;audio.volume=[0,.25,.5,1][state.bgm_level]*(state.paused?.5:1);}
  if(state.request_action===301)window.open('https://kbc-rakv0.pages.dev/information/appli/battlecats/help/index.html','_blank','noopener');
  if(state.request_action===302){stop();onReturn();return;}
  root.querySelector('[data-battle-clock]').textContent=state.frame+'F';
  root.querySelector('[data-battle-rows]').textContent=state.rows===2?'スロット：2段':'スロット：1段';
  for(const button of root.querySelectorAll('[data-battle-page]'))button.hidden=state.rows===2;
  await drawScene();
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
 function number(value,base,right,y,gap=-1,scale=1){
  const digits=String(Math.max(0,Math.trunc(value))).split('').map(Number),rects=resources.atlas.atlases.img001_ja.rects;
  const width=digits.reduce((sum,v)=>sum+rects[base+v][2]*scale+gap,0)-gap;
  let x=right-width;for(const digit of digits){const cut=rects[base+digit];sprite('img001_ja',base+digit,x,y,cut[2]*scale,cut[3]*scale);x+=cut[2]*scale+gap;}return right-width;
 }
 function paint(){
  if(!view)return;
  context.fillStyle='#000';context.fillRect(0,0,screenWidth,640);if(background.width)context.drawImage(background,0,0);
  const moneyBase=view.money_base,moneyRight=screenWidth-34,capX=number(view.wallet_max/100,moneyBase,moneyRight,10),slashX=capX-29;
  sprite('img001_ja',moneyBase+10,slashX,10);number(state.money/100,moneyBase,slashX-1,10);sprite('img001_ja',moneyBase+11,moneyRight,10);
  // 005d0508は後ろのページを先に描き、選択ページを重ねる。
  function slots(){
  const order=view.order;
  for(const index of order){const [x,y,w,h]=view.slots[index],form=resources.forms[index];
   if(!form){sprite('uni',0,x,y,w,h);if(view.modes[index]===2){context.fillStyle='rgba(0,0,0,.392)';context.fillRect(x,y,w,h);}continue;}
   const image=resources.images.get(form.icon);context.drawImage(image,9,21,110,85,x,y,w,h);
   if(resources.config.blocked[index]||resources.config.costs[index]*100>state.money||view.modes[index]===2){context.fillStyle='rgba(0,0,0,.392)';context.fillRect(x,y,w,h);}
   const disabled=resources.config.blocked[index]||resources.config.costs[index]*100>state.money,base=disabled?46:35;
   const [labelX,labelY]=view.labels[index];number(resources.config.costs[index],base,labelX+94,labelY+62,-3);sprite('img001_ja',disabled?56:45,labelX+94,labelY+62,22,26);
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
 function cameraArea(event){const {y}=coordinates(event);return y>=134&&y<(state.rows===2?449:543);}
 const gestures=initializeSceneGestures(canvas,()=>state.intro>=24&&!state.paused?{...camera,viewport_width:screenWidth,maximum:1}:null,value=>{camera={...camera,...value};++cameraVersion;},{acceptPointer:event=>{if(!cameraArea(event))return false;pointer={...pointer,phase:3};cameraPointers.add(event.pointerId);return true;},acceptWheel:cameraArea});
 function input(event){if(cameraPointers.has(event.pointerId)){if(event.type==='pointerup'||event.type==='pointercancel')cameraPointers.delete(event.pointerId);return;}if(state.intro<24)return;event.preventDefault();const phase={pointerdown:1,pointerup:2,pointercancel:3,pointermove:4}[event.type];if(phase===4&&!state.pointer_down&&pointer.phase!==1)return;pointer={...coordinates(event),phase};if(phase===1)canvas.setPointerCapture(event.pointerId);}
 for(const type of ['pointerdown','pointerup','pointercancel','pointermove'])canvas.addEventListener(type,input);
 function wheel(event){if(state.paused||state.rows!==1||state.intro<24||!event.deltaY)return;const point=coordinates(event);if(point.y<543||point.x<159+(screenWidth-960)/2||point.x>801+(screenWidth-960)/2)return;event.preventDefault();control=event.deltaY>0?9:8;}
 canvas.addEventListener('wheel',wheel,{passive:false});
 const observer=new ResizeObserver(resize);
 function command(event){const button=event.target.closest('[data-battle-control]');if(!button)return;const value=button.dataset.battleControl;if(value==='return'){stop();onReturn();return;}control=Number(value);}
 root.addEventListener('click',command);
 function key(event){if(event.key==='Escape'){event.preventDefault();control=state.paused?1:2;}}
 window.addEventListener('keydown',key);
 function visibility(){if(document.hidden)control=2;}
 document.addEventListener('visibilitychange',visibility);
 async function animate(now){
  if(stopped)return;
  if(lastTime&&!document.hidden)accumulator+=(now-lastTime)*30/1000;lastTime=now;
  if(!busy&&(Math.floor(accumulator)>0||control||drawnVersion!==cameraVersion)){
   busy=true;const ticks=control?0:Math.min(30,Math.floor(accumulator));accumulator-=ticks;
   try{await update(ticks);paint();}catch(e){if(!stopped){error=true;message.textContent=e.message;menu.hidden=false;}}finally{busy=false;}
  }
  if(!error&&!stopped)raf=requestAnimationFrame(animate);
 }
 function stop(){stopped=true;cancelAnimationFrame(raf);requestController.abort();observer.disconnect();gestures.dispose();cameraPointers.clear();canvas.removeEventListener('wheel',wheel);if(audio){audio.pause();audio.removeAttribute('src');}resources.dispose();for(const type of ['pointerdown','pointerup','pointercancel','pointermove'])canvas.removeEventListener(type,input);root.removeEventListener('click',command);window.removeEventListener('keydown',key);document.removeEventListener('visibilitychange',visibility);}
 try{resize();observer.observe(canvas.parentElement);await update(0);state.cannon=view.cannon_initial;await update(0);paint();raf=requestAnimationFrame(animate);}catch(error){stop();throw error;}
 return {stop};
}
