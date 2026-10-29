import {formationLayout,insertMember,stepFloating} from './formation-layout.js';
import {addFormationMember,moveTrayMember,swapTrayMember} from './formation-tray.js';
import {loadUnitDatabase} from './src/shared/game/units.js';
import {createFormationMember,resolveFormationMember,formationDisplayName,formationListForm} from './formation-model.js';
import {formationIconHtml,createFormationView,fitFormationName} from './formation-view.js';
import {formationStageContext,stageDeployment,battleFormation} from './battle-support.js';
import {escapeHtml as escape} from './src/shared/game/database-view.js';
import {readSimulationProfile} from './simulation-store.js';
import {readGameSettings} from './src/shared/browser/game-settings.js';
import {createSimulationSettings} from './simulation-settings.js';

const node=id=>document.getElementById(id),clone=value=>structuredClone(value);
const names=['にゃんこ砲','スロウ砲','鉄壁砲','かみなり砲','水鉄砲','エンジェル砲','キャノンブレイク砲','呪い砲'];
const status=node('formation-status'),screen=node('formation-screen');status.textContent='読み込み中';
let paintFormation,database,manifest,equipment=[],entry,count=0,index=0,selected=0,changed=false,saving=Promise.resolve(),timer,busy=false,dragged=null;
const units=new Map();
let floating=null,suppressClick=false,stageContext=null,deployment=null,deployVersion=0,deployTimer;
let tray=Array(5).fill(null),trayEntry=null,selectedTray=-1,trayDrag=null,trayDeployment=null,suppressTrayClick=false;
const trayHost=document.createElement('section');trayHost.className='formation-tray';trayHost.hidden=true;screen.after(trayHost);
const activeMember=()=>selectedTray>=0?tray[selectedTray]:entry.document.slots[selected];
function storeTray(){try{sessionStorage.setItem('kbcs:formation-tray:'+entry.id,JSON.stringify(tray));}catch{}}
function loadTray(){
 if(trayEntry===entry.id)return;trayEntry=entry.id;selectedTray=-1;tray=Array(5).fill(null);
 try{const saved=JSON.parse(sessionStorage.getItem('kbcs:formation-tray:'+entry.id));if(Array.isArray(saved))for(let i=0;i<5;++i){const value=saved[i];if(value&&units.has(value.unitId)&&Array.isArray(value.orbs)&&value.talents&&Number.isInteger(value.level)&&Number.isInteger(value.form))tray[i]=value;}}catch{}
}
const shifts=Array.from({length:10},()=>({x:0,y:0}));
async function request(path,body){
  const response=await fetch(path,body?{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}:{});
  if(!response.ok)throw new Error(await response.text());return response.json();
}
function blank(){return {format:'kbcs-formation',schemaVersion:1,region:'jp',gameVersion:database.gameVersion,name:'編成'+(count+1),slotName:'編成'+(count+1),slots:Array(10).fill(null),cannon:{id:0,level:30,developmentLevel:30},profile:clone(readSimulationProfile(readGameSettings()))};}
function draw(){
  loadTray();const doc=entry.document;
  trayHost.hidden=!doc.slots.every(Boolean)&&!tray.some(Boolean);
  trayHost.innerHTML='<div class="formation-tray-label">一時枠<button type="button" data-tray-clear>空にする</button></div>'+paintFormation({...doc,slots:[...tray,...Array(5).fill(null)]},{tray:true,selected:selectedTray,deployment:trayDeployment,hiddenSlot:trayDrag?.ghost?trayDrag.index:-1});
  screen.innerHTML=paintFormation(doc,{index,selected:selectedTray<0?selected:-1,floating,shifts,deployment});fitFormationName(screen,manifest);
  document.title=formationDisplayName(doc,index)+' | KBCS';
  node('formation-position').textContent=index+' / '+count;node('formation-name').value=formationDisplayName(doc,index);
  if(entry.id){const route=new URLSearchParams(location.search);route.set('id',entry.id);history.replaceState(null,'','/pages/formation/?'+route);}
}
function mark(){deployment=null;trayDeployment=null;++deployVersion;storeTray();clearTimeout(deployTimer);deployTimer=setTimeout(updateRestrictions,180);changed=true;status.textContent='保存待ち';clearTimeout(timer);timer=setTimeout(()=>save().catch(showError),350);}
function markMember(){if(selectedTray>=0){trayDeployment=null;++deployVersion;storeTray();clearTimeout(deployTimer);deployTimer=setTimeout(updateRestrictions,180);}else mark();}
function showError(error){status.textContent=error.message;status.dataset.error='true';}
async function save(){
  clearTimeout(timer);
  // 保存を直列化し、前の応答で編集途中のドキュメントを上書きしない。
  saving=saving.catch(()=>{}).then(async()=>{
    if(!changed)return;
    const current=entry,snapshot=clone(current.document);snapshot.gameVersion=database.gameVersion;changed=false;status.textContent='保存中';
    try{const result=await request('/api/formations',{id:current.id??null,revision:current.revision??null,document:snapshot});current.id=result.entry.id;current.revision=result.entry.revision;current.document.gameVersion=snapshot.gameVersion;count=result.count;index=result.index;status.textContent=changed?'保存待ち':'保存済み';delete status.dataset.error;try{localStorage.setItem('kbcs:formation-update',Date.now()+':'+current.id+':'+current.revision);}catch{}}
    catch(error){changed=true;throw error;}
  });return saving;
}
async function exclusive(task){
  if(busy||dragged||floating)return;busy=true;
  const controls=document.querySelectorAll('#formation-screen,.formation-tray,.formation-toolbar,.formation-library,#formation-member,#formation-profile');
  for(const control of controls)control.inert=true;
  try{await save();await task();}catch(error){showError(error);}finally{busy=false;for(const control of controls)control.inert=false;}
}
async function updateRestrictions(){
  if(!entry)return;
  const version=++deployVersion;
  try{
    const calculate=document=>stageDeployment(database,stageContext?.map,stageContext?.stage,stageContext?.crown,battleFormation(database,document));
    const [value,pending]=await Promise.all([calculate(entry.document),tray.some(Boolean)?calculate({...entry.document,slots:[...tray,...Array(5).fill(null)]}):null]);
    if(version!==deployVersion)return;deployment=value;trayDeployment=pending;draw();
  }catch(error){if(version===deployVersion)showError(error);}
}

function renderSettings(){
  node('formation-settings').replaceChildren();createSimulationSettings(node('formation-settings'),{profile:entry.document.profile,onChange:mark});
  node('formation-cannon').value=entry.document.cannon.id;node('formation-cannon-level').value=entry.document.cannon.level;
  node('formation-development-level').value=entry.document.cannon.developmentLevel??30;
}
function orbRows(member){
  return member.orbs.slice(0,units.get(member.unitId).orbSlots).map((id,index)=>'<label>玉'+(index+1)+'<select data-orb="'+index+'"><option value="">なし</option>'+equipment.map(item=>'<option value="'+item.id+'" '+(item.id===id?'selected':'')+'>'+escape(item.name)+'</option>').join('')+(id&&!equipment.some(item=>item.id===id)?'<option value="'+id+'" selected>未収録 ID '+id+'</option>':'')+'</select><button data-orb-remove="'+index+'" aria-label="玉'+(index+1)+'を外す">×</button></label>').join('');
}
function renderMember(){
  const member=activeMember(),unit=member&&units.get(member.unitId),host=node('formation-member');
  if(!unit){host.innerHTML='<h2>枠'+(selected+1)+'</h2>';return;}
  const effective=resolveFormationMember(unit,member),advancedLocked=unit.rarity===4&&member.level<60,capacity=unit.orbSlots;
  const talents=unit.talents.length?'<details><summary>本能・超本能</summary>'+unit.talents.map(talent=>'<label>'+escape((talent.limit?'超本能：':'')+talent.name)+'<select '+(advancedLocked&&talent.limit?'disabled':'')+' data-talent="'+talent.index+'">'+Array.from({length:talent.maxLevel+1},(_,level)=>'<option value="'+level+'" '+(level===(member.talents[talent.index]??0)?'selected':'')+'>'+level+'</option>').join('')+'</select></label>').join('')+'</details>':'';
  const orbs=capacity?'<details><summary>本能玉 '+Math.min(member.orbs.length,capacity)+' / '+capacity+'</summary>'+orbRows(member)+'<button data-orb-add '+(member.orbs.length>=capacity?'disabled':'')+'>玉を追加</button>'+(member.orbs.length>capacity?'<button data-orb-trim>上限を超えた設定を外す</button>':'')+'</details>':'';
  host.innerHTML='<h2>'+escape(unit.forms.find(form=>form.index===effective.form)?.name??'未収録キャラ')+'</h2><label>形態<select data-member="form">'+unit.forms.map(form=>'<option value="'+form.index+'" '+(form.index===effective.form?'selected':'')+' '+(advancedLocked&&form.index===3?'disabled':'')+'>'+escape(form.name)+'</option>').join('')+'</select></label>'+((advancedLocked&&(unit.forms.some(form=>form.index===3)||unit.talents.some(talent=>talent.limit)))?'<p class="formation-level-lock">超本能・第4形態はLv60から有効</p>':'')+'<div class="formation-levels"><label>Lv<input type="number" min="1" max="'+unit.maxLevel+'" value="'+member.level+'" data-member="level"></label><label>＋<input type="number" min="0" max="'+(unit.plusLevel??0)+'" value="'+member.plus+'" data-member="plus"></label></div><button data-remove>枠から外す</button>'+talents+orbs+(selectedTray>=0?'<button data-tray-move '+(entry.document.slots.every(Boolean)?'disabled':'')+'>編成へ移す</button>':'<div class="formation-move"><button data-move="-1">◀ 枠移動</button><button data-move="1">枠移動 ▶</button></div>');
}
function render(){deployment=null;trayDeployment=null;++deployVersion;draw();renderMember();renderSettings();updateRestrictions();}
function filter(){
  const query=node('formation-search').value.normalize('NFKC').toLowerCase(),choice=node('formation-display-form').value;
  const found=database.units.filter(unit=>!unit.isSpirit&&(String(unit.id)===query||[...unit.aliases,...unit.forms.map(form=>form.name)].join(' ').normalize('NFKC').toLowerCase().includes(query)));
  node('formation-results').innerHTML=found.slice(0,90).map(unit=>{const form=formationListForm(unit,choice);return '<button data-unit="'+unit.id+'" aria-label="'+escape(form.name)+'">'+formationIconHtml(database,form,manifest)+'<span>'+escape(form.name)+'</span></button>';}).join('')+(found.length>90?'<p>検索して絞り込む</p>':'');
}

function action(name){
  if(busy||dragged||floating)return;
  if(name==='clear'){if(entry.document.slots.some(Boolean)){entry.document.slots.fill(null);selected=0;selectedTray=-1;mark();draw();renderMember();}}
  else if(name==='menu'){node('formation-slot-name').value=formationDisplayName(entry.document,index);node('formation-menu').showModal();}
  else if(name==='previous'||name==='next')exclusive(async()=>{const result=await request('/api/formations?current='+entry.id+'&direction='+(name==='next'?1:-1));entry=result.entry;count=result.count;index=result.index;render();});
  else if(name==='import')node('formation-file').click();
  else if(name==='cannon'){node('formation-profile').firstElementChild.open=true;node('formation-cannon').focus();}
}
function pointerPosition(event){
  const rect=screen.querySelector('svg').getBoundingClientRect(),layout=formationLayout();
  return {x:Math.trunc((event.clientX-rect.left)*layout.width/rect.width),y:Math.trunc((event.clientY-rect.top)*layout.height/rect.height)};
}
function finishDrag(cancel=false){
  if(!dragged)return;
  const captured=dragged;dragged=null;
  if(floating?.held){
    const base=formationLayout().slots[floating.slot];floating.x=captured.pointer.x-captured.grab.x-base.x;floating.y=captured.pointer.y-captured.grab.y-base.y;
    floating.held=false;suppressClick=true;
    if(cancel){entry.document.slots=captured.snapshot;floating=null;for(const shift of shifts){shift.x=0;shift.y=0;}}
    else{floating.remove=captured.pointer.y<80||captured.pointer.y>280;mark();}
    renderMember();draw();
    setTimeout(()=>{suppressClick=false;},0);
  }
  if(screen.hasPointerCapture(captured.pointerId))screen.releasePointerCapture(captured.pointerId);
}
function startTrayDrag(event){
 const target=event.target.closest('[data-slot]');if(!target||event.button!==0||busy||dragged||floating)return;
 const index=Number(target.dataset.slot);if(!tray[index])return;
 event.preventDefault();trayDrag={index,pointerId:event.pointerId,x:event.clientX,y:event.clientY,ticks:0,growth:0,alpha:0,held:true,ghost:null};
 trayHost.setPointerCapture(event.pointerId);
}
function paintTrayDrag(){
 const value=trayDrag;if(!value)return;
 if(!value.ghost){const ghost=document.createElement('div');ghost.className='formation-drag-preview';ghost.innerHTML=paintFormation({...entry.document,slots:[tray[value.index],...Array(9).fill(null)]},{ghost:true,deployment:trayDeployment?{slots:[trayDeployment.slots[value.index]]}:null});document.body.append(ghost);value.ghost=ghost;draw();}
 stepFloating(value);
 const scale=screen.getBoundingClientRect().width/1188,width=(110+Math.trunc(value.growth*110/100))*scale,height=(85+Math.trunc(value.growth*85/100))*scale;
 Object.assign(value.ghost.style,{left:(value.x-width/2)+'px',top:(value.y-height/2)+'px',width:width+'px',height:height+'px',opacity:(255-value.alpha)/255});
}
function moveTrayDrag(event){if(trayDrag&&trayDrag.pointerId===event.pointerId){trayDrag.x=event.clientX;trayDrag.y=event.clientY;}}
function finishTrayDrag(event){
 if(!trayDrag||event&&event.pointerId!==trayDrag.pointerId)return;
 const value=trayDrag;trayDrag=null;value.ghost?.remove();
 if(value.ticks>=5){
  suppressTrayClick=true;setTimeout(()=>{suppressTrayClick=false;},0);
  if(event){const point=pointerPosition(event),target=formationLayout().slots.findIndex(slot=>point.x>=slot.x&&point.x<slot.x+110&&point.y>=slot.y&&point.y<slot.y+85);
   if(swapTrayMember(entry.document.slots,tray,value.index,target)){selected=target;selectedTray=-1;mark();renderMember();}}
  draw();
 }
 if(trayHost.hasPointerCapture(value.pointerId))trayHost.releasePointerCapture(value.pointerId);
}
function animateFormation(){
  if(!entry)return;
  if(trayDrag){++trayDrag.ticks;if(trayDrag.ticks>=5)paintTrayDrag();}
  const layout=formationLayout();let dirty=false;
  for(const shift of shifts){if(shift.x||shift.y){shift.x=Math.trunc(shift.x/2);shift.y=Math.trunc(shift.y/2);dirty=true;}}
  if(dragged){
    if(!floating){const base=layout.slots[dragged.slot],point=dragged.pointer;if(point.x<base.x||point.x>=base.x+114||point.y<base.y-2||point.y>=base.y+86){finishDrag(true);return;}}
    dragged.ticks++;
    if(dragged.ticks>=5&&!floating){
      selected=dragged.slot;floating={slot:selected,held:true,growth:0,alpha:0,x:0,y:0};renderMember();
    }
    if(floating?.held){
      const target=layout.slots.findIndex((slot,i)=>entry.document.slots[i]&&dragged.pointer.x>=slot.x&&dragged.pointer.x<slot.x+114&&dragged.pointer.y>=slot.y-2&&dragged.pointer.y<slot.y+86);
      if(target>=0&&target!==floating.slot){
        const from=floating.slot,direction=target>from?1:-1;
        for(let i=from;i!==target;i+=direction){const next=i+direction;shifts[i].x=layout.slots[next].x+shifts[next].x-layout.slots[i].x;shifts[i].y=layout.slots[next].y+shifts[next].y-layout.slots[i].y;}
        shifts[target].x=0;shifts[target].y=0;insertMember(entry.document.slots,from,target);floating.slot=target;selected=target;
      }
      const base=layout.slots[floating.slot];
      floating.x=dragged.pointer.x-dragged.grab.x-base.x;floating.y=dragged.pointer.y-dragged.grab.y-base.y;
    }
  }
  if(floating){
    if(floating.remove){floating.growth=Math.max(-100,floating.growth-20);if(floating.growth===-100){entry.document.slots[floating.slot]=null;floating=null;mark();renderMember();}}
    else stepFloating(floating);
    if(floating&&!floating.held&&!floating.remove&&floating.x===0&&floating.y===0)floating=null;
    dirty=true;
  }
  if(dirty)draw();
}
try{
  selected=Math.max(0,Math.min(9,Number(new URLSearchParams(location.search).get('slot'))||0));
  [database,manifest]=await Promise.all([loadUnitDatabase(),request('/images/native-formation/manifest.json')]);
  await Promise.all(Object.entries(manifest.atlases).map(async([name,atlas])=>{const image=new Image();image.src='/images/native-formation/'+name+'.png';await image.decode();atlas.width=image.naturalWidth;atlas.height=image.naturalHeight;}));
  for(const unit of database.units)units.set(unit.id,unit);
  const requested=new URLSearchParams(location.search).get('id');
  paintFormation=createFormationView(database,manifest);
  const result=await request('/api/formations'+(requested?'?current='+encodeURIComponent(requested):''));entry=result.entry;count=result.count;index=result.index;
  if(!entry){entry={document:blank()};changed=true;await save();}
  node('formation-cannon').innerHTML=names.map((name,id)=>'<option value="'+id+'">'+name+'</option>').join('');
  stageContext=await formationStageContext(new URLSearchParams(location.search));
  if(stageContext){if(stageContext.buildId!==database.buildId)throw Error('DBが更新されました。再読み込みしてください');const host=node('formation-context');host.hidden=false;const params=new URLSearchParams({map:stageContext.map.key,stage:stageContext.stage.index,crown:stageContext.crown});host.innerHTML='<a href="/pages/stage-sortie/?'+params+'">'+escape(stageContext.stage.name)+' / '+stageContext.crown+'冠の出撃準備に戻る</a>'; }
  try{node('formation-display-form').value=sessionStorage.getItem('kbcs:formation:display-form')||'max';}catch{}
  render();filter();status.textContent='保存済み';request('/api/formation-equipment').then(result=>{equipment=result.items;renderMember();}).catch(showError);
  screen.addEventListener('click',event=>{if(suppressClick)return;const slot=event.target.closest('[data-slot]');if(slot){selectedTray=-1;selected=Number(slot.dataset.slot);draw();renderMember();}else{const target=event.target.closest('[data-action]');if(target)action(target.dataset.action);}});
  screen.addEventListener('keydown',event=>{if(['Enter',' '].includes(event.key)){event.preventDefault();event.target.dispatchEvent(new MouseEvent('click',{bubbles:true}));}});
  screen.addEventListener('pointerdown',event=>{
    const target=event.target.closest('[data-slot]');if(!target||event.button!==0||busy||floating)return;
    const slot=Number(target.dataset.slot);if(!entry.document.slots[slot])return;
    const pointer=pointerPosition(event),base=formationLayout().slots[slot];
    dragged={slot,pointer,grab:{x:pointer.x-base.x,y:pointer.y-base.y},ticks:0,pointerId:event.pointerId,snapshot:clone(entry.document.slots)};
    screen.setPointerCapture(event.pointerId);
    selectedTray=-1;selected=slot;draw();renderMember();
  });
  screen.addEventListener('pointermove',event=>{if(dragged&&dragged.pointerId===event.pointerId)dragged.pointer=pointerPosition(event);});
  screen.addEventListener('pointerup',event=>{if(dragged&&dragged.pointerId===event.pointerId){dragged.pointer=pointerPosition(event);finishDrag();}});
  screen.addEventListener('pointercancel',()=>finishDrag(true));
  screen.addEventListener('lostpointercapture',()=>finishDrag(true));
  window.addEventListener('blur',()=>finishDrag(true));
  setInterval(animateFormation,1000/30);
  node('formation-search').addEventListener('input',filter);
  node('formation-display-form').addEventListener('change',event=>{try{sessionStorage.setItem('kbcs:formation:display-form',event.target.value);}catch{}filter();});
  trayHost.addEventListener('click',event=>{
    if(suppressTrayClick||busy||dragged||floating)return;
    if(event.target.closest('[data-tray-clear]')){tray.fill(null);selectedTray=-1;storeTray();draw();renderMember();return;}
    const target=event.target.closest('[data-slot]');if(!target)return;const index=Number(target.dataset.slot);if(!tray[index])return;
    const moved=moveTrayMember(entry.document.slots,tray,index);
    if(moved>=0){selected=moved;selectedTray=-1;mark();}else selectedTray=index;
    storeTray();draw();renderMember();
  });
  trayHost.addEventListener('pointerdown',startTrayDrag);
  trayHost.addEventListener('pointermove',moveTrayDrag);
  trayHost.addEventListener('pointerup',finishTrayDrag);
  trayHost.addEventListener('pointercancel',()=>finishTrayDrag(null));
  trayHost.addEventListener('lostpointercapture',()=>finishTrayDrag(null));
  window.addEventListener('blur',()=>finishTrayDrag(null));
  trayHost.addEventListener('keydown',event=>{if(['Enter',' '].includes(event.key)&&event.target.hasAttribute('data-slot')){event.preventDefault();event.target.dispatchEvent(new MouseEvent('click',{bubbles:true}));}});
  node('formation-results').addEventListener('click',event=>{
    const button=event.target.closest('[data-unit]');if(!button||busy||dragged||floating)return;
    const result=addFormationMember(entry.document.slots,tray,createFormationMember(units.get(Number(button.dataset.unit))));
    if(!result){status.textContent='一時枠がいっぱいです';return;}
    selectedTray=result.group==='tray'?result.index:-1;if(selectedTray<0)selected=result.index;
    if(result.changed){if(result.group==='slots')mark();else{storeTray();updateRestrictions();}}draw();renderMember();
  });
  node('formation-member').addEventListener('change',event=>{const target=event.target,member=activeMember();if(!member||!target.checkValidity())return;if(target.dataset.member)member[target.dataset.member]=Number(target.value);if(target.dataset.talent)member.talents[target.dataset.talent]=Number(target.value);if(target.dataset.orb!==undefined)member.orbs[Number(target.dataset.orb)]=target.value?Number(target.value):null;markMember();draw();if(target.dataset.member==='form'||target.dataset.member==='level')renderMember();});
  node('formation-member').addEventListener('click',event=>{const button=event.target.closest('button'),member=activeMember();if(!button||!member||dragged||floating)return;if(button.hasAttribute('data-tray-move')){const moved=moveTrayMember(entry.document.slots,tray,selectedTray);if(moved>=0){selected=moved;selectedTray=-1;mark();draw();renderMember();}return;}if(button.hasAttribute('data-orb-add')){if(member.orbs.length<units.get(member.unitId).orbSlots){member.orbs.push(null);markMember();renderMember();}return;}if(button.hasAttribute('data-orb-trim')){member.orbs=member.orbs.slice(0,units.get(member.unitId).orbSlots);markMember();renderMember();return;}if(button.dataset.orbRemove!==undefined){member.orbs.splice(Number(button.dataset.orbRemove),1);markMember();renderMember();return;}if(button.dataset.move){const next=(selected+Number(button.dataset.move)+10)%10;insertMember(entry.document.slots,selected,next);selected=next;mark();draw();renderMember();return;}if(event.target.closest('[data-remove]')){if(selectedTray>=0){tray[selectedTray]=null;selectedTray=-1;storeTray();}else{entry.document.slots[selected]=null;mark();}draw();renderMember();}});
  node('formation-name').addEventListener('change',event=>{const name=event.target.value.trim();if(name){entry.document.name=name;entry.document.slotName=name;mark();draw();}else event.target.value=entry.document.name;});
  node('formation-new').addEventListener('click',()=>exclusive(async()=>{entry={document:blank()};changed=true;await save();render();}));
  for(const [id,key] of [['formation-cannon','id'],['formation-cannon-level','level'],['formation-development-level','developmentLevel']])node(id).addEventListener('change',event=>{if(event.target.checkValidity()){entry.document.cannon[key]=Number(event.target.value);mark();draw();}});
  node('formation-rename').addEventListener('click',()=>{const name=node('formation-slot-name').value.trim();if(!name)return;entry.document.slotName=name;entry.document.name=name;mark();draw();node('formation-menu').close();});
  node('formation-import').addEventListener('click',()=>action('import'));
  node('formation-export').addEventListener('click',()=>exclusive(async()=>{const url=URL.createObjectURL(new Blob([JSON.stringify(entry.document,null,2)],{type:'application/json'})),link=document.createElement('a');link.href=url;link.download=formationDisplayName(entry.document,index).replace(/[<>:"/\\|?*]/g,'_')+'.kbcs.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);node('formation-menu').close();}));
  node('formation-file').addEventListener('change',event=>exclusive(async()=>{const file=event.target.files[0];event.target.value='';if(!file)return;if(file.size>1_000_000)throw new Error('編成ファイルが大きすぎます');const document=JSON.parse(await file.text()),result=await request('/api/formations',{id:entry.id,revision:entry.revision,document});entry=result.entry;count=result.count;index=result.index;changed=false;render();node('formation-menu').close();status.textContent='読込・保存済み';}));
  window.addEventListener('beforeunload',event=>{if(changed){event.preventDefault();event.returnValue='';}});
}catch(error){showError(error);}
