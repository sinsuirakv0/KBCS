import {nativePackets} from './native-pose.js';
import {createEffectSequence} from './effect-sequence.js';
import {parseImgCut,parseMaModel,parseMaAnim,evaluateMotion} from './motion-engine.js';
import {NativeWebGLRenderer} from './native-webgl-renderer.js';
import {escapeHtml} from '../../shared/game/database-view.js';

const el=id=>document.getElementById('motion-'+id),esc=escapeHtml;
const params=new URLSearchParams(location.search),formCodes=['f','c','s','u'];
const state={kind:params.has('enemy')?'enemy':document.querySelector('[data-motion-kind]').dataset.motionKind,id:document.querySelector('[data-motion-kind]').dataset.motionKind==='effect'?(params.get('id')||'skill_wave_attack'):Number(params.get('enemy')??params.get('id')??0),form:Math.max(0,formCodes.indexOf(params.get('form')||'f')),motion:'02',frame:0,playing:false,zoom:1,panX:0,panY:0,selected:0,resource:'body',hidden:new Set(),solo:false,tab:'parts',screen:[],poses:new Map(),timeline:[]};
const choiceCache=new Map(),manifestCache=new Map(),projectCache=new Map();
let drawVersion=0,fitVersion=0;
let effectSequence=null,manifest,resources=new Map(),renderer,loading=0,lastTime=0,inspectorTime=0,sourceFile=null;
const propertyNames=['親','ID','画像','Z順','X','Y','ピボットX','ピボットY','XY拡縮','X拡縮','Y拡縮','回転','不透明度','X反転','Y反転'];
const clipNames={'00':'移動','01':'待機','02':'攻撃','03':'KB','04':'潜行開始','05':'地中移動','06':'潜行終了','_soul':'専用の魂','soul':'魂','sequence':'KB → 魂'};
const api=async(path,options)=>{const response=await fetch(path,options),value=await response.json();if(!response.ok)throw Error(value.error||'読込に失敗しました');return value;};
const selectedResource=()=>resources.get(state.resource)||resources.get('body');
function report(text,error=false){el('status').textContent=text;el('status').hidden=!text;el('status').classList.toggle('error',error);el('message').textContent=error?text:'';}
function characters(){return choiceCache.get(state.kind)?.entries||[];}
async function loadChoices(kind){
  if(!choiceCache.has(kind))choiceCache.set(kind,await api(kind==='effect'?'/api/motion-effects':'/api/motion-choices?kind='+kind));
}
async function loadManifest(path){
  if(manifestCache.has(path))return manifestCache.get(path);
  const value=await api(path);if(manifestCache.size>=16)manifestCache.delete(manifestCache.keys().next().value);manifestCache.set(path,value);return value;
}
function updateChoices(){
  const query=el('query').value.normalize('NFKC').toLowerCase();
  el('category').hidden=state.kind!=='effect';
  const category=el('category').value;
  const entries=characters().filter(item=>state.kind!=='effect'||category==='all'||item.category===category||item.side===category).filter(item=>String(item.id).includes(query)||(item.name||item.forms?.[0]?.name||'').toLowerCase().includes(query));
  el('character').innerHTML=entries.map(item=>'<option value="'+item.id+'"'+(item.id===state.id?' selected':'')+(item.issue?' disabled':'')+'>'+String(item.id).padStart(3,'0')+' '+esc(item.name||item.forms?.[0]?.name||'')+(item.issue?' / 対応未確認':'')+'</option>').join('');
}
function updateForms(){
  const unit=state.kind==='unit'?characters().find(unit=>unit.id===state.id):null;
  el('forms').innerHTML=unit?unit.forms.map(form=>'<button data-form="'+form.index+'" aria-pressed="'+(form.index===state.form)+'" title="'+esc(form.name)+'">第'+(form.index+1)+'形態</button>').join(''):'';
}
async function project(resource,files){
  const paths=[resource.image,resource.cut,resource.model,...resource.animations.map(clip=>clip.path)];
  const nativeRequest={kind:state.kind,id:state.id,form:state.form};
  const key=JSON.stringify([nativeRequest,resource,...paths.map(path=>files.get(path)?.sha256)]);
  if(projectCache.has(key)){const cached=projectCache.get(key);projectCache.delete(key);projectCache.set(key,cached);return cached;}
  const text=path=>files.get(path)?.text||'';
  const image=new Image();image.src='/api/asset/'+resource.image;await image.decode();
  const motions=Object.fromEntries(resource.animations.map(clip=>[clip.key,parseMaAnim(text(clip.path))]));
  if(!Object.keys(motions).length)motions['static']={tracks:[],maxFrame:0,frameCount:1};
  const result={...resource,nativeRequest,image,imgcut:parseImgCut(text(resource.cut)),model:parseMaModel(text(resource.model)),motions};
  for(const motion of Object.values(motions))for(const track of motion.tracks)if(track.partIndex<0||track.partIndex>=result.model.parts.length)throw Error('存在しないパーツ参照: '+resource.stem);
  // デコード済み画像と解析結果を小さい範囲で再利用する。GPUのtextureは切替時に解放する。
  const cost=result.image.naturalWidth*result.image.naturalHeight*4+paths.reduce((sum,path)=>sum+(files.get(path)?.size||0),0);
  result.cacheCost=cost;
  while(projectCache.size&&(projectCache.size>=8||[...projectCache.values()].reduce((sum,p)=>sum+p.cacheCost,0)+cost>32*1024*1024))projectCache.delete(projectCache.keys().next().value);
  if(cost<=32*1024*1024)projectCache.set(key,result);
  return result;
}
async function loadCharacter(){
  const version=++loading;effectSequence=null;state.playing=false;syncPlay();resources.forEach(p=>renderer?.releaseTexture(p.image));resources=new Map();manifest=null;state.screen=[];state.poses.clear();draw();report('素材を読み込んでいます。');
  el('source').hidden=true;el('export-cut').disabled=true;el('parts').replaceChildren();el('files').replaceChildren();el('cuts').replaceChildren();el('part-detail').textContent='読込中';el('clip').replaceChildren();
  try{
    const path='/api/motion?'+new URLSearchParams({kind:state.kind,id:state.id,form:state.form});
    const [value]=await Promise.all([loadManifest(path),loadChoices(state.kind)]);if(version!==loading)return;
    updateChoices();updateForms();
    const files=new Map(value.files.map(file=>[file.path,file]));
    const projects=await Promise.all([project(value.body,files),value.soul?project(value.soul,files):null]);
    if(version!==loading)return;
    manifest=value;resources=new Map(projects.filter(Boolean).map(p=>[p.key,p]));
    state.frame=0;state.selected=0;state.resource='body';state.hidden.clear();state.solo=false;
    const body=resources.get('body');state.selected=body.model.parts.find(part=>part.id>=0&&part.imageIndex>=0)?.index??0;if(!body.motions[state.motion])state.motion=body.motions['02']?'02':Object.keys(body.motions)[0];
    const soul=resources.get('soul'),soulFrames=soul?Math.max(0,...Object.values(soul.motions).map(m=>m.frameCount)):0;
    const specialFrames=value.character.deathMotion?body.motions._soul?.frameCount||0:0;
    state.timeline=state.kind==='effect'?[]:(await api('/api/motion-timeline',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({soulFrames,specialFrames})})).frames;
    if(version!==loading)return;
    if(state.kind==='effect')updateEffectSequence();
    el('title').textContent=value.character.name;document.title=value.character.name+' モーション | KBCS';
    el('resource').innerHTML=[...resources.values()].map(p=>'<option value="'+p.key+'">'+(p.key==='body'?(state.kind==='effect'?'素材':'本体'):'共通の魂')+' / '+p.stem+'</option>').join('');
    el('clip').innerHTML=(value.body.animations.length?value.body.animations:[{key:'static',name:'静止モデル'}]).map(m=>'<option value="'+m.key+'">'+esc(m.name)+'</option>').join('')+(soul?'<option value="soul">共通の魂</option>':'')+(body.motions['03']?'<option value="sequence">KB → 魂</option>':'')+(effectSequence?'<option value="effect-sequence">一連の演出</option>':'');
    if(effectSequence)state.motion='effect-sequence';
    el('effect-level-control').hidden=!effectSequence||effectSequence.kind==='explosion';
    el('clip').value=state.motion;el('solo').setAttribute('aria-pressed','false');
    renderFiles();renderParts();renderCuts();setClip(state.motion);fit();report('');
    history.replaceState(null,'','/pages/'+state.kind+'-motion/?'+new URLSearchParams({id:state.id,...(state.kind==='unit'?{form:formCodes[state.form]}:{})}));
    el('message').textContent=value.files.length+'ファイル / '+body.model.parts.length+'パーツ / '+body.imgcut.cuts.length+'分割画像';
  }catch(error){if(version===loading){report(error.message,true);el('title').textContent='モーション';}}
}
function updateEffectSequence(){const body=resources.get('body');effectSequence=createEffectSequence(manifest.character.stem,body.animations.map(clip=>({frames:body.motions[clip.key].frameCount})),manifest.sequenceConfig||{},Number(el('effect-level').value));}
function frameCount(){if(state.motion==='effect-sequence')return effectSequence?.duration||1;if(!manifest)return 1;if(state.motion==='sequence')return state.timeline.length;const p=state.motion==='soul'?resources.get('soul'):resources.get('body');return p?.motions[state.motion]?.frameCount||1;}
function setClip(key){const desired=key==='soul'?'soul':'body';if(state.resource!==desired){state.resource=desired;state.selected=resources.get(desired)?.model.parts.find(part=>part.id>=0&&part.imageIndex>=0)?.index??0;el('resource').value=desired;renderParts();renderCuts();}state.motion=key;state.frame=0;el('clip').value=key;el('scrub').max=frameCount()-1;el('frame').max=frameCount()-1;el('length').textContent='/ '+(frameCount()-1)+'F';renderTracks();syncFrame();draw();}
function syncFrame(){const frame=Math.floor(state.frame);el('frame').value=frame;el('scrub').value=frame;}
function syncPlay(){el('play').textContent=state.playing?'Ⅱ':'▶';el('play').setAttribute('aria-label',state.playing?'一時停止':'再生');}
function setFrame(value){state.frame=Math.max(0,Math.min(frameCount()-1,Number(value)||0));state.playing=false;syncPlay();syncFrame();draw();inspect();}
function renderFiles(){
  el('files').innerHTML=manifest.files.map((file,index)=>'<button class="motion-file-row" data-file="'+index+'">'+esc(file.path.split('/').at(-1))+'<small>'+esc(file.role)+' / '+file.size.toLocaleString()+' B</small></button>').join('');
}
function renderParts(){
  const p=selectedResource();if(!p)return;
  const query=el('part-query').value.toLowerCase();
  el('parts').innerHTML=p.model.parts.filter(part=>String(part.index).includes(query)||part.name.toLowerCase().includes(query)).map(part=>{
    let depth=0,parent=part.parent,seen=new Set([part.index]);while(parent>=0&&!seen.has(parent)){seen.add(parent);depth++;parent=p.model.parts[parent]?.parent??-1;}
    return '<div class="motion-part-row" data-row="'+part.index+'" aria-current="'+(state.selected===part.index)+'" style="padding-left:'+Math.min(6,depth)*9+'px"><input type="checkbox" data-part-visible="'+part.index+'" aria-label="パーツ '+part.index+' を表示"'+(!state.hidden.has(p.key+':'+part.index)?' checked':'')+'><button data-part="'+part.index+'" title="'+esc(part.name)+'">'+part.index+' '+esc(part.name||'パーツ '+part.index)+'</button><small>画像 '+part.imageIndex+'</small></div>';
  }).join('');
  el('configs').innerHTML=p.model.configs.map((config,index)=>'<div class="motion-track">'+index+' '+esc(config.name)+'<br>'+config.values.join(', ')+'</div>').join('')||'設定なし';
  renderTracks();inspect();
}
function renderCuts(){
  const p=selectedResource();if(!p)return;el('export-cut').disabled=true;
  el('cuts').innerHTML=p.imgcut.cuts.map(cut=>{const scale=Math.min(1,64/Math.max(1,cut.width,cut.height));return '<button class="motion-cut" data-cut="'+cut.index+'" aria-pressed="false" title="'+esc(cut.name)+'"><span><i class="motion-cut-image" style="width:'+cut.width*scale+'px;height:'+cut.height*scale+'px"><img src="/api/asset/'+p.image.src.split('/api/asset/')[1]+'" alt="" loading="lazy" style="width:'+p.image.naturalWidth*scale+'px;height:'+p.image.naturalHeight*scale+'px;left:'+(-cut.x*scale)+'px;top:'+(-cut.y*scale)+'px"></i></span><small>cut-'+String(cut.index).padStart(3,'0')+'.png</small><small>'+cut.width+'×'+cut.height+'</small></button>';}).join('');
}
function partIndices(index){const p=selectedResource(),result=new Set([index]);if(el('descendants').checked)for(let changed=true;changed;){changed=false;for(const part of p.model.parts)if(result.has(part.parent)&&!result.has(part.index)){result.add(part.index);changed=true;}}return result;}
function choosePart(index,resource=state.resource){const changed=resource!==state.resource;state.resource=resource;state.selected=index;el('resource').value=resource;renderParts();if(changed)renderCuts();draw();}
function inspect(){
  const p=selectedResource();if(!p)return;
  const base=p.model.parts[state.selected],instance=frameInstances().find(v=>v.p===p);
  const part=instance?evaluateMotion(p,instance.key,instance.frame,{loop:false,facing:el('flip').getAttribute('aria-pressed')==='true'?-1:1}).find(v=>v.index===state.selected)||base:base;if(!part)return;
  const rows=[['番号',base.index],['名前',base.name||'—'],['親',part.parent],['画像',part.imageIndex],['Z順',part.zIndex],['座標',part.x+', '+part.y],['ピボット',part.pivotX+', '+part.pivotY],['拡縮',part.scaleX+', '+part.scaleY],['角度',part.angle+' / '+p.model.angleUnit],['不透明度',part.opacity+' / '+p.model.opacityUnit],['合成',['通常','加算','乗算','スクリーン'][part.glow]||part.glow],['表示設定',state.hidden.has(p.key+':'+part.index)?'非表示':'表示'],['画面',state.screen.some(packet=>packet.resource===p.key&&packet.partIndex===part.index)?'描画中':'非描画']];
  el('part-detail').innerHTML='<table class="motion-property-table"><tbody>'+rows.map(([key,value])=>'<tr><th>'+key+'</th><td>'+esc(value)+'</td></tr>').join('')+'</tbody></table>';
}
function renderTracks(){
  const p=selectedResource();if(!p)return;
  const key=state.motion==='sequence'?'03':state.motion==='effect-sequence'?p.animations[0]?.key:state.motion;
  const motion=p.motions[key]||Object.values(p.motions)[0];
  const tracks=motion?.tracks.filter(track=>track.partIndex===state.selected)||[];
  el('tracks').innerHTML=tracks.map(track=>'<div class="motion-track">'+esc(propertyNames[track.property]||track.property)+' / '+track.keys.length+'キー / 反復 '+track.loop+'<div>'+track.keys.map(key=>'<button data-key-frame="'+(key.frame-track.offset)+'" title="補間 '+key.easing+' / 強度 '+key.easingPower+'">'+(key.frame-track.offset)+'F: '+key.value+'</button>').join('')+'</div></div>').join('')||'このモーションにキーなし';
  const keys=[...new Set(tracks.flatMap(track=>track.keys.map(key=>key.frame-track.offset)))].filter(frame=>frame>=0&&frame<frameCount());
  el('key-strip').innerHTML=keys.map(frame=>'<button class="motion-key-marker" data-key-frame="'+frame+'" style="left:'+frame/Math.max(1,frameCount()-1)*100+'%" title="'+frame+'F" aria-label="'+frame+'フレームへ"></button>').join('');
}
function showFile(index){
  sourceFile=manifest.files[index];if(!sourceFile)return;
  el('source').hidden=false;el('source-name').textContent=sourceFile.path;el('file-proof').textContent='SHA-256 '+sourceFile.sha256+'\n'+sourceFile.original+'\n'+sourceFile.sourceKind;
  el('source-text').hidden=!sourceFile.text;el('source-text').textContent=sourceFile.text||'';
  el('source-image').hidden=!sourceFile.path.endsWith('.png');if(!el('source-image').hidden)el('source-image').src='/api/asset/'+sourceFile.path;draw();
}
function download(url,name){const a=document.createElement('a');a.href=url;a.download=name;a.click();}
function saveCut(index){const p=selectedResource(),cut=p.imgcut.cuts[index],canvas=document.createElement('canvas');canvas.width=cut.width;canvas.height=cut.height;canvas.getContext('2d').drawImage(p.image,cut.x,cut.y,cut.width,cut.height,0,0,cut.width,cut.height);download(canvas.toDataURL('image/png'),p.stem+'-cut-'+String(index).padStart(3,'0')+'.png');}
function frameInstances(){
  const body=resources.get('body'),soul=resources.get('soul');if(!body)return [];
  if(state.motion==='effect-sequence'&&effectSequence)return effectSequence.instances(Math.floor(state.frame)).map(instance=>({p:body,key:body.animations[instance.motion].key,frame:instance.frame,x:instance.x,y:0}));
  if(state.motion==='sequence'){
    const offset=state.timeline[Math.floor(state.frame)];if(!offset)return [];
    if(offset.phase===0)return [{p:body,key:'03',frame:offset.frame,x:offset.x,y:offset.y}];
    if(offset.phase===1)return [manifest.character.deathMotion&&body.motions._soul&&offset.frame<body.motions._soul.frameCount?{p:body,key:'_soul',frame:offset.frame,x:offset.x,y:0}:null,soul&&offset.frame<soul.motions.soul.frameCount?{p:soul,key:'soul',frame:offset.frame,x:offset.x,y:-97}:null].filter(Boolean);
    return [];
  }
  const p=state.motion==='soul'?soul:body;
  return p?.motions[state.motion]?[{p,key:state.motion,frame:state.frame,x:0,y:state.motion==='soul'?-97:0}]:[];
}
function renderProject(instance,values){
  const {p,x,y}=instance,stage=el('stage'),originX=stage.clientWidth*.5+state.panX+x*state.zoom,originY=stage.clientHeight*.72+state.panY+y*state.zoom;
  const selected=partIndices(state.selected);
  const packets=values.filter(packet=>!state.hidden.has(p.key+':'+packet.partIndex)&&(!state.solo||p.key===state.resource&&selected.has(packet.partIndex))).map(packet=>({...packet,positions:packet.positions.map((value,index)=>(index%2?originY:originX)+value*state.zoom)}));
  renderer.drawPackets(p.image,packets);state.screen.push(...packets.map(packet=>({...packet,resource:p.key})));
}
async function draw(){
  const version=++drawVersion;
  if(!renderer)return;
  const stage=el('stage'),width=stage.clientWidth,height=stage.clientHeight;if(!width||!height)return;
  const ratio=Math.min(2,devicePixelRatio||1),canvas=el('canvas'),overlay=el('overlay');
  for(const target of [canvas,overlay])if(target.width!==Math.round(width*ratio)||target.height!==Math.round(height*ratio)){target.width=Math.round(width*ratio);target.height=Math.round(height*ratio);}
  const instances=frameInstances();let poses;
  try{poses=await Promise.all(instances.map(instance=>nativePackets(instance.p,instance.key,instance.frame,el('flip').getAttribute('aria-pressed')==='true'?-1:1)));}
  catch(error){if(version===drawVersion)report(error.message,true);return;}
  if(version!==drawVersion)return;
  renderer.beginFrame(width,height,[.047,.079,.133,1]);state.screen=[];
  if(el('grid').checked){const positions=[];const step=50*state.zoom;for(let x=(width*.5+state.panX)%step;x<width;x+=step)positions.push(x,0,x,height);for(let y=(height*.72+state.panY)%step;y<height;y+=step)positions.push(0,y,width,y);renderer.drawColorGeometry(positions,[.2,.29,.4,.35],renderer.gl.LINES);renderer.drawColorGeometry([0,height*.72+state.panY,width,height*.72+state.panY],[.43,.55,.69,.7],renderer.gl.LINES);}
  instances.forEach((instance,index)=>renderProject(instance,poses[index]));
  const body=resources.get('body');if(body){
    const offset=state.motion==='sequence'?state.timeline[Math.floor(state.frame)]:null;
    const label=state.motion==='effect-sequence'?'一連の演出':state.motion==='sequence'?(offset?.phase===0?'KB':offset?.phase===1?'魂':'退場'):clipNames[state.motion]||body.animations.find(clip=>clip.key===state.motion)?.name||'静止モデル';
    el('phase').textContent=label+' / '+Math.floor(state.frame)+'F / '+state.screen.length+'パーツ描画';
  }
  const ctx=overlay.getContext('2d');ctx.setTransform(ratio,0,0,ratio,0,0);ctx.clearRect(0,0,width,height);
  if(!el('selection-outline').checked)return;
  for(const packet of state.screen.filter(p=>p.resource===state.resource&&p.partIndex===state.selected)){ctx.strokeStyle='#ffbf48';ctx.lineWidth=1.5;ctx.beginPath();for(let i=0;i<4;i++)ctx[i?'lineTo':'moveTo'](packet.positions[i*2],packet.positions[i*2+1]);ctx.closePath();ctx.stroke();}
}
async function fit(){
  const version=loading,fitRequest=++fitVersion;
  const p=state.motion==='soul'?resources.get('soul'):resources.get('body');if(!p)return;
  const key=p.motions[state.motion]?state.motion:Object.keys(p.motions)[0];
  let packets;
  try{
    packets=await nativePackets(p,key,state.frame);
    if(state.motion==='effect-sequence'&&effectSequence){
      const samples=[];for(let frame=0;frame<effectSequence.duration;frame++)for(const instance of effectSequence.instances(frame)){const values=await nativePackets(p,p.animations[instance.motion].key,instance.frame);samples.push(...values.map(packet=>({...packet,positions:packet.positions.map((value,index)=>value+(index%2?0:instance.x))})));}packets=samples;
    }
    if(state.motion==='sequence'){
      packets=[];for(const frame of [0,11,23]){const step=state.timeline[frame],values=await nativePackets(p,'03',frame);packets.push(...values.map(packet=>({...packet,positions:packet.positions.map((value,index)=>value+(index%2?step.y:step.x))})));}
      const soul=resources.get('soul');if(soul){const values=await nativePackets(soul,'soul',0);packets.push(...values.map(packet=>({...packet,positions:packet.positions.map((value,index)=>value+(index%2?-97:138))})));}
    }
  }catch(error){if(version===loading)report(error.message,true);return;}
  if(version!==loading||fitRequest!==fitVersion)return;const points=packets.flatMap(p=>p.positions);if(!points.length)return;
  let minX=Infinity,maxX=-Infinity,minY=Infinity,maxY=-Infinity;for(let i=0;i<points.length;i+=2){minX=Math.min(minX,points[i]);maxX=Math.max(maxX,points[i]);minY=Math.min(minY,points[i+1]);maxY=Math.max(maxY,points[i+1]);}
  state.zoom=Math.max(.1,Math.min(5,el('stage').clientWidth*.65/Math.max(1,maxX-minX),el('stage').clientHeight*.65/Math.max(1,maxY-minY)));
  state.panX=-(minX+maxX)*state.zoom/2;state.panY=el('stage').clientHeight*(-.18)-(minY+maxY)*state.zoom/2;
  el('zoom').value=Math.round(state.zoom*100);el('zoom-label').textContent=Math.round(state.zoom*100)+'%';draw();
}
function toggleVisibility(index,visible){for(const id of partIndices(index)){const key=state.resource+':'+id;if(visible)state.hidden.delete(key);else state.hidden.add(key);}renderParts();draw();}
async function tick(time){const elapsed=lastTime?Math.min(.1,(time-lastTime)/1000):0;lastTime=time;if(state.playing&&manifest){state.frame+=elapsed*30*Number(el('speed').value);const count=frameCount();if(state.frame>=count){if(el('loop').checked)state.frame%=count;else{state.frame=count-1;state.playing=false;syncPlay();}}syncFrame();await draw();if(time-inspectorTime>150){inspect();inspectorTime=time;}}requestAnimationFrame(tick);}

el('export-cut').onclick=()=>saveCut(state.cut);
el('kind').value=state.kind;
el('kind').addEventListener('change',()=>{state.kind=el('kind').value;state.id=state.kind==='effect'?'skill_wave_attack':0;state.form=0;el('category').value='all';el('query').value='';loadCharacter();});
el('query').addEventListener('input',updateChoices);
el('category').addEventListener('change',updateChoices);
el('effect-level').addEventListener('input',()=>{if(!manifest)return;el('effect-level').value=Math.max(1,Math.min(20,Math.trunc(Number(el('effect-level').value))||1));updateEffectSequence();setClip('effect-sequence');fit();});
el('character').addEventListener('change',()=>{state.id=state.kind==='effect'?el('character').value:Number(el('character').value);state.form=0;loadCharacter();});
el('forms').addEventListener('click',event=>{const button=event.target.closest('[data-form]');if(button){state.form=Number(button.dataset.form);loadCharacter();}});
el('clip').addEventListener('change',()=>{state.playing=false;syncPlay();setClip(el('clip').value);fit();});
el('resource').addEventListener('change',()=>{state.resource=el('resource').value;state.selected=0;renderParts();renderCuts();draw();});
el('part-query').addEventListener('input',renderParts);
el('parts').addEventListener('click',event=>{const part=event.target.closest('[data-part]');if(part)choosePart(Number(part.dataset.part));});
el('parts').addEventListener('change',event=>{if(event.target.matches('[data-part-visible]'))toggleVisibility(Number(event.target.dataset.partVisible),event.target.checked);});
el('all-visible').addEventListener('click',()=>{state.hidden.clear();state.solo=false;el('solo').setAttribute('aria-pressed','false');renderParts();draw();});
el('part-reset').addEventListener('click',()=>{toggleVisibility(state.selected,true);state.solo=false;el('solo').setAttribute('aria-pressed','false');draw();});
el('solo').addEventListener('click',()=>{state.solo=!state.solo;el('solo').setAttribute('aria-pressed',String(state.solo));draw();});
el('files').addEventListener('click',event=>{const file=event.target.closest('[data-file]');if(file)showFile(Number(file.dataset.file));});
el('cuts').addEventListener('click',event=>{const cut=event.target.closest('[data-cut]');if(!cut)return;const index=Number(cut.dataset.cut),p=selectedResource(),part=p.model.parts.find(part=>part.imageIndex===index);if(part)choosePart(part.index);for(const button of el('cuts').querySelectorAll('[data-cut]'))button.setAttribute('aria-pressed',String(Number(button.dataset.cut)===index));state.cut=index;el('export-cut').disabled=false;el('message').textContent=p.stem+' / cut-'+String(index).padStart(3,'0')+'.png';});
for(const button of document.querySelectorAll('[data-explorer]'))button.addEventListener('click',()=>{state.tab=button.dataset.explorer;for(const tab of document.querySelectorAll('[data-explorer]'))tab.setAttribute('aria-selected',String(tab===button));for(const [name,id] of [['parts','part-panel'],['files','file-panel'],['cuts','cut-panel']])el(id).hidden=state.tab!==name;});
for(const root of [el('tracks'),el('key-strip')])root.addEventListener('click',event=>{const button=event.target.closest('[data-key-frame]');if(button)setFrame(button.dataset.keyFrame);});
el('source-close').onclick=()=>{el('source').hidden=true;draw();};el('download').onclick=()=>{if(sourceFile)download('/api/asset/'+sourceFile.path,sourceFile.path.split('/').at(-1));};
el('play').onclick=()=>{if(manifest){state.playing=!state.playing;syncPlay();}};el('rewind').onclick=()=>setFrame(0);el('prev').onclick=()=>setFrame(Math.floor(state.frame)-1);el('next').onclick=()=>setFrame(Math.floor(state.frame)+1);
el('frame').oninput=()=>setFrame(el('frame').value);el('scrub').oninput=()=>setFrame(el('scrub').value);el('fit').onclick=fit;
el('zoom').oninput=()=>{state.zoom=Number(el('zoom').value)/100;el('zoom-label').textContent=el('zoom').value+'%';draw();};el('flip').onclick=()=>{el('flip').setAttribute('aria-pressed',String(el('flip').getAttribute('aria-pressed')!=='true'));draw();};el('grid').onchange=draw;el('interpolate').onchange=draw;
el('save').onclick=async()=>{await draw();download(el('canvas').toDataURL('image/png'),(manifest?.character.stem||'motion')+'-'+state.motion+'-'+Math.floor(state.frame)+'.png');};
el('selection-outline').onchange=draw;
// ネイティブの整数フレームで再生する。補間は表示仕様が確定してから追加する。
el('interpolate').checked=false;el('interpolate').disabled=true;el('interpolate').parentElement.hidden=true;
let drag=null;
el('stage').addEventListener('pointerdown',event=>{if(event.button!==0)return;el('stage').focus();drag={x:event.clientX,y:event.clientY,panX:state.panX,panY:state.panY};el('stage').setPointerCapture(event.pointerId);});
el('stage').addEventListener('pointermove',event=>{if(!drag)return;state.panX=drag.panX+event.clientX-drag.x;state.panY=drag.panY+event.clientY-drag.y;draw();});
el('stage').addEventListener('pointerup',event=>{if(!drag)return;const distance=Math.hypot(event.clientX-drag.x,event.clientY-drag.y);drag=null;if(distance>4)return;const rect=el('stage').getBoundingClientRect(),x=event.clientX-rect.x,y=event.clientY-rect.y;const packet=[...state.screen].reverse().find(packet=>{const v=packet.positions,signs=[0,1,2,3].map(i=>{const j=(i+1)%4;return (v[j*2]-v[i*2])*(y-v[i*2+1])-(v[j*2+1]-v[i*2+1])*(x-v[i*2]);});return signs.every(value=>value>=0)||signs.every(value=>value<=0);});if(packet)choosePart(packet.partIndex,packet.resource);});
el('stage').addEventListener('pointercancel',()=>{drag=null;});
el('stage').addEventListener('wheel',event=>{event.preventDefault();state.zoom=Math.min(5,Math.max(.1,state.zoom*Math.exp(-event.deltaY*.001)));el('zoom').value=Math.round(state.zoom*100);el('zoom-label').textContent=Math.round(state.zoom*100)+'%';draw();},{passive:false});
el('stage').addEventListener('keydown',event=>{if(!manifest)return;const seek=event.shiftKey?10:1;if(event.code==='Space'){event.preventDefault();state.playing=!state.playing;syncPlay();}else if(event.key==='ArrowLeft'||event.key==='ArrowRight'){event.preventDefault();setFrame(Math.floor(state.frame)+(event.key==='ArrowLeft'?-seek:seek));}else if(event.key==='Home'){event.preventDefault();setFrame(0);}else if(event.key==='End'){event.preventDefault();setFrame(frameCount()-1);}else if(event.key.toLowerCase()==='f')fit();else if(event.key.toLowerCase()==='h')toggleVisibility(state.selected,state.hidden.has(state.resource+':'+state.selected));});
new ResizeObserver(draw).observe(el('stage'));
try{renderer=new NativeWebGLRenderer(el('canvas'));await loadCharacter();requestAnimationFrame(tick);}catch(error){report(error.message,true);}
