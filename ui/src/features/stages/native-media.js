import {NativeWebGLRenderer} from '../motion/native-webgl-renderer.js';
import {escapeHtml as esc} from '../../shared/game/database-view.js';
import {saveCanvasImage} from '../../shared/browser/capture.js';
import {initializeSceneGestures} from './scene-controls.js';

const imagePromises=new Map(),decoded=new Map(),gradients=new Map(),renderers=new Set();let renderer,pending=0,imageHits=0,imageMisses=0;
const castlePath=stage=>stage.enemyCastle==null&&stage.castle!=null?'Image/'+['ec','wc','sc','rc'][stage.castleSet??3]+String(stage.castle).padStart(3,'0')+'.png':null;
async function image(path){
  if(!imagePromises.has(path)){
    ++pending;++imageMisses;
    const value=new Image();value.src='/api/asset/'+path;
    imagePromises.set(path,value.decode().then(()=>{
      decoded.set(path,value);
      while(decoded.size>24||[...decoded.values()].reduce((sum,v)=>sum+v.naturalWidth*v.naturalHeight*4,0)>64*1024*1024){
        const [key,old]=decoded.entries().next().value;decoded.delete(key);imagePromises.delete(key);for(const renderer of renderers)renderer.releaseTexture(old);
      }
      return value;
    }).catch(error=>{imagePromises.delete(path);throw error;}).finally(()=>--pending));
  }else ++imageHits;
  return imagePromises.get(path);
}
function gradient(colors){
  const key=colors.join(',');if(!gradients.has(key)){
    const canvas=document.createElement('canvas');canvas.width=1;canvas.height=256;
    const context=canvas.getContext('2d'),paint=context.createLinearGradient(0,0,0,256);
    paint.addColorStop(0,'rgb('+colors.slice(0,3).join(',')+')');paint.addColorStop(1,'rgb('+colors.slice(3).join(',')+')');
    context.fillStyle=paint;context.fillRect(0,0,1,256);gradients.set(key,canvas);
  }return gradients.get(key);
}
// UIは受け取った描画命令をGPUへ送る。姿勢・カメラ・背景の式は持たない。
async function raster(canvas,result,direct,supplied){
  const paths=[...new Set(result.commands.filter(c=>c.texture>=0).map(c=>result.textures[c.texture]).filter(Boolean))];
  const loaded=new Map(await Promise.all(paths.map(async path=>{try{const cached=supplied?.get(path);if(cached)++imageHits;return [path,cached||await image(path)];}catch{return [path,null];}})));
  if(!direct&&(!renderer||renderer.gl.isContextLost())){if(renderer)renderers.delete(renderer);renderer=new NativeWebGLRenderer(document.createElement('canvas'));renderers.add(renderer);}
  const active=direct||renderer;
  if(active.gl.isContextLost())return false;
  if(active.canvas.width!==canvas.width)active.canvas.width=canvas.width;if(active.canvas.height!==canvas.height)active.canvas.height=canvas.height;
  active.beginFrame(result.layout.viewport_width||960,640,[0,0,0,1]);
  let batchTexture=null,batch=[];
  const flush=()=>{if(batch.length)active.drawPackets(batchTexture,batch);batch=[];};
  for(const command of result.commands){
    const positions=command.points.subarray?command.points.subarray(0,command.count*2):command.points.slice(0,command.count*2);
    if(command.texture===-2){flush();batchTexture=null;active.drawColorGeometry(positions,[...Array.from(command.colors.slice(0,3),v=>v/255),command.opacity],active.gl.TRIANGLE_FAN,command.blend);continue;}
    const texture=command.texture===-1?gradient(command.colors):loaded.get(result.textures[command.texture]);if(!texture)continue;
    const width=texture.naturalWidth||texture.width,height=texture.naturalHeight||texture.height;
    const [x,y,rawWidth,rawHeight]=command.cut,w=command.texture===-1||rawWidth<0?width:rawWidth,h=command.texture===-1||rawHeight<0?height:rawHeight;
    if(texture!==batchTexture||batch.length>=16000){flush();batchTexture=texture;}
    const tint=command.texture>=0&&command.colors[3]===1?Array.from(command.colors.slice(0,3),v=>v/255):null;
    batch.push({tint,tintKey:tint?.join(),blendMode:command.blend,opacity:command.opacity,positions,uvs:[x/width,y/height,x/width,(y+h)/height,(x+w)/width,(y+h)/height,(x+w)/width,y/height]});
  }
  flush();
  if(!direct){const context=canvas.getContext('2d');context.clearRect(0,0,canvas.width,canvas.height);context.drawImage(active.canvas,0,0);}
  for(const [path,texture]of loaded)if(texture&&!decoded.has(path)&&!supplied?.has(path))active.releaseTexture(texture);
  return true;
}
async function frame(stage,view,signal){
  const response=await fetch('/api/stage-scene',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(stageSceneInput(stage,view)),signal});
  const value=await response.json();if(!response.ok)throw Error(value.error||'背景を読み込めませんでした。');return value;
}
// 出撃準備でも同じC++描画命令とGPU転送を使う。
export function stageSceneInput(stage,view){return {background:stage.background,width:stage.width,castle:stage.castle,castleSet:stage.castleSet??3,enemyCastle:stage.enemyCastle,...view};}
export {frame as loadStageScene,raster as paintStageScene};
export function stageMediaStats(supplied){return {pending,hits:imageHits,misses:imageMisses,bytes:[...new Set([...decoded.values(),...(supplied?.values()||[])])].reduce((sum,v)=>sum+v.naturalWidth*v.naturalHeight*4,0)};}
// 戦闘は専用WebGL面へ直接描き、2D面にはHUDだけを重ねる。
export function createStagePainter(canvas,onRestore,supplied){
  let active=new NativeWebGLRenderer(canvas,{preserveDrawingBuffer:false,trackTextures:true}),disposed=false;
  renderers.add(active);
  const lost=event=>event.preventDefault();
  const restored=()=>{renderers.delete(active);active=new NativeWebGLRenderer(canvas,{preserveDrawingBuffer:false,trackTextures:true});renderers.add(active);onRestore();};
  canvas.addEventListener('webglcontextlost',lost);canvas.addEventListener('webglcontextrestored',restored);
  return {paint:async result=>{if(disposed||active.gl.isContextLost())return false;return raster(canvas,result,active,supplied);},dispose:()=>{disposed=true;renderers.delete(active);active.dispose();canvas.removeEventListener('webglcontextlost',lost);canvas.removeEventListener('webglcontextrestored',restored);}};
}
const audioTime=value=>Number.isFinite(value)?Math.floor(value/60)+':'+String(Math.floor(value%60)).padStart(2,'0'):'—';
export function stageMediaHtml(database,stage,enemies){
  const actor=enemies.enemies[stage.enemyCastle],path=actor?.icon||castlePath(stage),available=stage.background!=null&&stage.width>0;
  return '<div class="stage-media" data-media-stage="'+stage.id+'"><div class="stage-media-background"><button type="button" data-background-open aria-label="'+esc(stage.name)+'の背景を拡大"'+(available?'':' disabled')+'><canvas width="384" height="256" role="img" aria-label="背景 '+stage.background+'"></canvas></button><small>背景 '+(stage.background??'—')+'</small></div><div class="stage-media-castle">'+(path?'<img src="/api/asset/'+esc(path)+'" alt="'+esc(actor?.name||'敵城')+'" loading="lazy">':'—')+'<small>'+(actor?'敵ID '+actor.id:stage.castle==null?'—':['ec','wc','sc','rc'][stage.castleSet??3]+String(stage.castle).padStart(3,'0'))+'</small></div><div class="stage-music">'+(stage.musicTracks||[]).map(track=>{
    const item=database.musicCatalog?.tracks?.[track.id],name='BGM '+track.id+(item?.name?' '+item.name:'');
    return '<div class="stage-track"><button type="button" data-track-play aria-label="'+esc(name)+'を再生"'+(item?'':' disabled')+'>▶</button><span>'+esc(name)+'<small>'+(track.threshold==null?'開始時':'敵城'+track.threshold+'%以下')+(item?'':' / 音源未収録')+'</small></span>'+(item?'<input type="range" data-track-seek min="0" max="100" step="0.1" value="0" disabled aria-label="再生位置"><output data-track-time>0:00 / —</output><audio preload="none" hidden src="/api/stage-audio/'+track.id+'"></audio>':'')+'</div>';
  }).join('')+'</div></div>';
}
export function initializeStageMedia(root,resolveStage){
  let dialog,camera,activeStage,request=0,animation=0,lastTime=0,currentFrame=0,focus=0,clearGestures;
  const previews=new WeakMap();
  async function thumbnail(canvas){
    if(!previews.has(canvas)){
      const stage=resolveStage(canvas.closest('[data-media-stage]').dataset.mediaStage);
      previews.set(canvas,frame(stage,{frame:0,showEnemy:false,showPlayer:false,showEffects:false}).then(async data=>{if(canvas.isConnected)await raster(canvas,data);}).catch(error=>{if(canvas.isConnected)canvas.replaceWith(document.createTextNode(error.message));}));
    }return previews.get(canvas);
  }
  const observer=new IntersectionObserver(entries=>{for(const entry of entries)if(entry.isIntersecting){thumbnail(entry.target);observer.unobserve(entry.target);}},{rootMargin:'180px'});
  function stopAudio(){for(const audio of root.querySelectorAll('audio'))audio.pause();}
  async function draw(){
    if(!dialog?.open||!activeStage)return;const version=++request;
    try{
      const result=await frame(activeStage,{frame:Math.floor(currentFrame),center:Number(dialog.querySelector('[name="offset"]').value),zoom:Number(dialog.querySelector('[name="zoom"]').value)/100,focus,showEnemy:dialog.querySelector('[name="castle"]').checked,showPlayer:dialog.querySelector('[name="player"]').checked,showEffects:dialog.querySelector('[name="effects"]').checked});
      if(version!==request||!dialog.open)return;await raster(dialog.querySelector('canvas'),result);if(version!==request||!dialog.open)return;
      camera=result.layout;const offset=dialog.querySelector('[name="offset"]'),zoom=dialog.querySelector('[name="zoom"]');offset.max=camera.width;offset.value=camera.center;zoom.min=camera.minimum*100;zoom.value=camera.zoom*100;
      dialog.querySelector('[data-zoom]').textContent=(camera.zoom*100).toFixed(1)+'%';dialog.querySelector('[data-save]').disabled=false;
      dialog.querySelector('[name="motion"]').disabled=!result.animated;
      dialog.querySelector('[data-status]').textContent=(result.missing.length?'未収録: '+result.missing.join(', ')+' / ':'')+(result.issues?'一部は静止モデル / ':'')+Math.floor(currentFrame)+'F';
    }catch(error){if(version===request&&dialog.open){dialog.querySelector('[data-status]').textContent=error.message;dialog.querySelector('[name="motion"]').checked=false;}}
  }
  async function animate(now){
    animation=0;if(!dialog?.open||!dialog.querySelector('[name="motion"]').checked||document.hidden)return;
    if(lastTime)currentFrame+=Math.min(now-lastTime,1000)*30/1000;lastTime=now;await draw();
    if(dialog.open&&dialog.querySelector('[name="motion"]').checked)animation=requestAnimationFrame(animate);
  }
  async function open(stage){
    if(!dialog){
      dialog=document.createElement('dialog');dialog.className='db-dialog stage-background-dialog';dialog.innerHTML='<div class="db-toolbar"><h2></h2><button type="button" data-close>閉じる</button></div><canvas width="1440" height="960" aria-label="ステージ背景と城"></canvas><div class="db-toolbar"><button type="button" data-camera="1">敵城へ</button><button type="button" data-camera="3">全体</button><button type="button" data-camera="2">自城へ</button><label>横位置<input name="offset" type="range" min="0" max="100000" value="0" step="any"></label><label>拡大率<input name="zoom" type="range" min="0.1" max="200" value="100" step="any"><output data-zoom>100%</output></label><label><input name="castle" type="checkbox" checked>敵城</label><label><input name="player" type="checkbox" checked>自城</label><label><input name="effects" type="checkbox" checked>演出</label><label><input name="motion" type="checkbox">動きを再生</label><button type="button" data-save disabled>画像保存</button></div><output data-status role="status"></output>';
      document.body.append(dialog);dialog.querySelector('[data-close]').onclick=()=>dialog.close();
      clearGestures=initializeSceneGestures(dialog.querySelector('canvas'),()=>camera?{...camera,minimum:camera.minimum}:null,view=>{focus=0;dialog.querySelector('[name="offset"]').value=view.center;dialog.querySelector('[name="zoom"]').value=view.zoom*100;draw();});
      dialog.addEventListener('close',()=>{request++;cancelAnimationFrame(animation);activeStage=null;camera=null;clearGestures();});
      dialog.addEventListener('input',event=>{if(event.target.name==='motion'){cancelAnimationFrame(animation);lastTime=0;if(event.target.checked)animation=requestAnimationFrame(animate);else draw();}else{focus=0;draw();}});
      dialog.addEventListener('click',event=>{const button=event.target.closest('[data-camera]');if(button){focus=Number(button.dataset.camera);draw();}});
      dialog.querySelector('[data-save]').onclick=async()=>{try{await saveCanvasImage(dialog.querySelector('canvas'),'stage-'+activeStage.id+'-background');}catch(error){dialog.querySelector('[data-status]').textContent=error.message;}};
    }
    stopAudio();activeStage=stage;currentFrame=0;lastTime=0;focus=0;camera=null;
    dialog.querySelector('h2').textContent=stage.name+' / 背景 '+stage.background;dialog.querySelector('[data-status]').textContent='読み込み中';dialog.querySelector('[data-save]').disabled=true;
    dialog.querySelector('[name="offset"]').value=stage.width;dialog.querySelector('[name="zoom"]').value=100;
    dialog.querySelector('[name="motion"]').checked=false;dialog.querySelector('[name="effects"]').checked=true;dialog.showModal();await draw();
  }
  root.addEventListener('click',async event=>{
    const background=event.target.closest('[data-background-open]');if(background){open(resolveStage(background.closest('[data-media-stage]').dataset.mediaStage));return;}
    const button=event.target.closest('[data-track-play]');if(!button)return;const audio=button.closest('.stage-track').querySelector('audio');if(!audio)return;
    if(!audio.paused)audio.pause();else{stopAudio();try{button.textContent='…';await audio.play();}catch{button.textContent='!';button.title='音源を取得・再生できませんでした。';}}
  });
  root.addEventListener('input',event=>{if(event.target.matches('[data-track-seek]')){const audio=event.target.closest('.stage-track').querySelector('audio');if(Number.isFinite(audio.duration))audio.currentTime=Number(event.target.value)/100*audio.duration;}});
  return {
    clear(){stopAudio();observer.disconnect();if(dialog?.open)dialog.close();},
    refresh(){
      for(const canvas of root.querySelectorAll('[data-media-stage] canvas'))observer.observe(canvas);
      for(const audio of root.querySelectorAll('audio')){
        const track=audio.closest('.stage-track'),button=track.querySelector('[data-track-play]'),seek=track.querySelector('[data-track-seek]');
        audio.onplay=()=>button.textContent='Ⅱ';audio.onpause=audio.onended=()=>button.textContent='▶';
        audio.onerror=()=>{button.textContent='!';button.title='音源を取得・再生できませんでした。';};
        const progress=()=>{seek.value=audio.duration?audio.currentTime/audio.duration*100:0;track.querySelector('[data-track-time]').textContent=audioTime(audio.currentTime)+' / '+audioTime(audio.duration);};
        audio.onloadedmetadata=()=>{seek.disabled=!Number.isFinite(audio.duration);progress();};audio.ontimeupdate=progress;
      }
    },
    prepareCapture:target=>Promise.all([...target.querySelectorAll('[data-media-stage] canvas')].map(thumbnail)),
  };
}
