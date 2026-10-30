import {insertMember,stepFloating} from './formation-layout.js';
import {createFormationReorder,createFormationGhost} from './formation-reorder.js';
import {addFormationMember,moveTrayMember,swapTrayMember} from './formation-tray.js';
import {createFormationSearch} from './formation-search.js';
import {createFormationDetails} from './formation-details.js';
import {loadUnitDatabase} from './src/shared/game/units.js';
import {createFormationMember,resolveFormationMember,formationDisplayName,formationAdvancedUnlocked} from './formation-model.js';
import {createFormationView,fitFormationName} from './formation-view.js';
import {formationStageContext,stageDeployment,battleFormation} from './battle-support.js';
import {escapeHtml as escape} from './src/shared/game/database-view.js';
import {readSimulationProfile} from './simulation-store.js';
import {readGameSettings} from './src/shared/browser/game-settings.js';
import {createSimulationSettings} from './simulation-settings.js';

const node=id=>document.getElementById(id),clone=value=>structuredClone(value);
const names=['にゃんこ砲','スロウ砲','鉄壁砲','かみなり砲','水鉄砲','エンジェル砲','キャノンブレイク砲','呪い砲'];
const status=node('formation-status'),screen=node('formation-screen');status.textContent='読み込み中';
let paintFormation,renderDetails,database,manifest,equipment=[],entry,count=0,index=0,selected=0,changed=false,saving=Promise.resolve(),timer,busy=false,reorder;
const units=new Map();
let stageContext=null,deployment=null,deployVersion=0,deployTimer;
let tray=Array(5).fill(null),trayEntry=null,selectedTray=-1,trayDrag=null,trayDeployment=null,suppressTrayClick=false;
const trayHost=document.createElement('section');trayHost.className='formation-tray';
const trayArea=document.createElement('div');trayArea.className='formation-tray-area';
const trash=document.createElement('button');trash.id='formation-trash';trash.type='button';trash.title='ドラッグして編成から外す';trash.setAttribute('aria-label',trash.title);
trash.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M9 6V3h6v3M6 6l1 15h10l1-15M10 10v7m4-7v7"/></svg><span>ゴミ箱</span>';
trayArea.append(trayHost,trash);screen.after(trayArea);
const memberPanels=new Map();
const activeMember=()=>selectedTray>=0?tray[selectedTray]:entry.document.slots[selected];
function storeTray(){try{sessionStorage.setItem('kbcs:formation-tray:'+entry.id,JSON.stringify(tray));}catch{}}
function loadTray(){
 if(trayEntry===entry.id)return;trayEntry=entry.id;selectedTray=-1;tray=Array(5).fill(null);
 try{const saved=JSON.parse(sessionStorage.getItem('kbcs:formation-tray:'+entry.id));if(Array.isArray(saved))for(let i=0;i<5;++i){const value=saved[i];if(value&&units.has(value.unitId)&&Array.isArray(value.orbs)&&value.talents&&Number.isInteger(value.level)&&Number.isInteger(value.form))tray[i]=value;}}catch{}
}
async function request(path,body){
  const response=await fetch(path,body?{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}:{});
  if(!response.ok)throw new Error(await response.text());return response.json();
}
function blank(){return {format:'kbcs-formation',schemaVersion:1,region:'jp',gameVersion:database.gameVersion,name:'編成'+(count+1),slotName:'編成'+(count+1),slots:Array(10).fill(null),cannon:{id:0,level:30,developmentLevel:30},profile:clone(readSimulationProfile(readGameSettings()))};}
function draw(){
  loadTray();const doc=entry.document;
  trayHost.innerHTML='<div class="formation-tray-label">一時枠<button type="button" data-tray-clear>空にする</button></div>'+paintFormation({...doc,slots:[...tray,...Array(5).fill(null)]},{tray:true,selected:selectedTray,deployment:trayDeployment,hiddenSlot:trayDrag?.ghost?trayDrag.index:-1});
  screen.innerHTML=paintFormation(doc,{index,selected:selectedTray<0?selected:-1,deployment,...reorder?.view});fitFormationName(screen,manifest);reorder?.renderFloating();
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
    if(reorder?.active||trayDrag){timer=setTimeout(()=>save().catch(showError),100);return;}
    const current=entry,snapshot=clone(current.document);snapshot.gameVersion=database.gameVersion;changed=false;status.textContent='保存中';
    try{const result=await request('/api/formations',{id:current.id??null,revision:current.revision??null,document:snapshot});current.id=result.entry.id;current.revision=result.entry.revision;current.document.gameVersion=snapshot.gameVersion;count=result.count;index=result.index;status.textContent=changed?'保存待ち':'保存済み';delete status.dataset.error;try{localStorage.setItem('kbcs:formation-update',Date.now()+':'+current.id+':'+current.revision);}catch{}}
    catch(error){changed=true;throw error;}
  });return saving;
}
async function exclusive(task){
  if(busy||reorder?.active||trayDrag)return;busy=true;
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
    if(version!==deployVersion)return;deployment=value;trayDeployment=pending;draw();renderMemberSheet();
  }catch(error){if(version===deployVersion)showError(error);}
}

function renderSettings(){
  node('formation-settings').replaceChildren();createSimulationSettings(node('formation-settings'),{profile:entry.document.profile,onChange:()=>{mark();renderMemberSheet();}});
  node('formation-cannon').value=entry.document.cannon.id;node('formation-cannon-level').value=entry.document.cannon.level;
  node('formation-development-level').value=entry.document.cannon.developmentLevel??30;
}
function orbRows(member){
  return member.orbs.slice(0,units.get(member.unitId).orbSlots).map((id,index)=>'<label>玉'+(index+1)+'<select data-orb="'+index+'"><option value="">なし</option>'+equipment.map(item=>'<option value="'+item.id+'" '+(item.id===id?'selected':'')+'>'+escape(item.name)+'</option>').join('')+(id&&!equipment.some(item=>item.id===id)?'<option value="'+id+'" selected>未収録 ID '+id+'</option>':'')+'</select><button data-orb-remove="'+index+'" aria-label="玉'+(index+1)+'を外す">×</button></label>').join('');
}
function renderMember(){
  const member=activeMember(),unit=member&&units.get(member.unitId),host=node('formation-member');
  if(host.dataset.unitId)memberPanels.set(host.dataset.unitId,[...host.querySelectorAll('details[data-member-panel][open]')].map(panel=>panel.dataset.memberPanel));
  host.dataset.unitId=unit?String(unit.id):'';
  if(!unit){host.innerHTML='<h2>枠'+(selected+1)+'</h2>';return;}
  const effective=resolveFormationMember(unit,member),advancedLocked=!formationAdvancedUnlocked(unit,member),capacity=unit.orbSlots;
  const talents=unit.talents.length?'<details data-member-panel="talents"><summary>本能・超本能</summary>'+unit.talents.map(talent=>'<label>'+escape((talent.limit?'超本能：':'')+talent.name)+'<select '+(advancedLocked&&talent.limit?'disabled':'')+' data-talent="'+talent.index+'">'+Array.from({length:talent.maxLevel+1},(_,level)=>'<option value="'+level+'" '+(level===(member.talents[talent.index]??0)?'selected':'')+'>'+level+'</option>').join('')+'</select></label>').join('')+'</details>':'';
  const orbs=capacity?'<details data-member-panel="orbs"><summary>本能玉 '+Math.min(member.orbs.length,capacity)+' / '+capacity+'</summary>'+orbRows(member)+'<button data-orb-add '+(member.orbs.length>=capacity?'disabled':'')+'>玉を追加</button>'+(member.orbs.length>capacity?'<button data-orb-trim>上限を超えた設定を外す</button>':'')+'</details>':'';
  host.innerHTML='<h2>'+escape(unit.forms.find(form=>form.index===effective.form)?.name??'未収録キャラ')+'</h2><label>形態<select data-member="form">'+unit.forms.map(form=>'<option value="'+form.index+'" '+(form.index===effective.form?'selected':'')+' '+(advancedLocked&&form.index===3?'disabled':'')+'>'+escape(form.name)+'</option>').join('')+'</select></label>'+((advancedLocked&&(unit.forms.some(form=>form.index===3)||unit.talents.some(talent=>talent.limit)))?'<p class="formation-level-lock">超本能・第4形態は合計Lv60から有効</p>':'')+'<div class="formation-levels"><label>Lv<input type="number" min="1" max="'+unit.maxLevel+'" value="'+member.level+'" data-member="level"></label><label>＋<input type="number" min="0" max="'+(unit.plusLevel??0)+'" value="'+member.plus+'" data-member="plus"></label></div><button data-remove>枠から外す</button>'+talents+orbs+(selectedTray>=0?'<button data-tray-move '+(entry.document.slots.every(Boolean)?'disabled':'')+'>編成へ移す</button>':'<div class="formation-move"><button data-move="-1">◀ 枠移動</button><button data-move="1">枠移動 ▶</button></div>');
  for(const panel of host.querySelectorAll('details[data-member-panel]'))panel.open=(memberPanels.get(String(unit.id))||[]).includes(panel.dataset.memberPanel);
  host.insertAdjacentHTML('beforeend','<div class="formation-member-sheet" data-member-sheet></div>');renderMemberSheet();
}

function render(){deployment=null;trayDeployment=null;++deployVersion;draw();renderMember();renderSettings();updateRestrictions();}
function renderMemberSheet(){
 const cost=(selectedTray>=0?trayDeployment?.slots[selectedTray]:deployment?.slots[selected])?.cost;
 renderDetails?.(node('formation-member').querySelector('[data-member-sheet]'),activeMember(),entry.document.profile,cost);
}

function addUnit(id){
  if(busy||reorder?.active||trayDrag||reorder?.suppressClick)return;
  const result=addFormationMember(entry.document.slots,tray,createFormationMember(units.get(id)));
  if(!result){status.textContent='一時枠がいっぱいです';return;}
  selectedTray=result.group==='tray'?result.index:-1;if(selectedTray<0)selected=result.index;
  if(result.changed){if(result.group==='slots')mark();else{storeTray();updateRestrictions();}}draw();renderMember();
}

function action(name){
  if(busy||reorder?.active||trayDrag)return;
  if(name==='clear'){if(entry.document.slots.some(Boolean)){entry.document.slots.fill(null);selected=0;selectedTray=-1;mark();draw();renderMember();}}
  else if(name==='menu'){node('formation-slot-name').value=formationDisplayName(entry.document,index);node('formation-menu').showModal();}
  else if(name==='previous'||name==='next')exclusive(async()=>{const result=await request('/api/formations?current='+entry.id+'&direction='+(name==='next'?1:-1));entry=result.entry;count=result.count;index=result.index;render();});
  else if(name==='import')node('formation-file').click();
  else if(name==='cannon'){node('formation-profile').firstElementChild.open=true;node('formation-cannon').focus();}
}
function dropTarget(event){
 const target=event&&document.elementFromPoint(event.clientX,event.clientY);
 if(target?.closest('#formation-trash,#formation-results'))return {group:'remove'};
 const slot=target?.closest('[data-slot]');
 if(slot&&trayHost.contains(slot))return {group:'tray',index:Number(slot.dataset.slot)};
 if(slot&&screen.contains(slot))return {group:'slots',index:Number(slot.dataset.slot)};
 return null;
}
function startTrayDrag(event){
 const target=event.target.closest('[data-slot]');if(!target||event.button!==0||busy||reorder?.active)return;
 const index=Number(target.dataset.slot);if(!tray[index])return;
 event.preventDefault();trayDrag={index,pointerId:event.pointerId,x:event.clientX,y:event.clientY,ticks:0,growth:0,alpha:0,held:true,ghost:null};
 trayHost.setPointerCapture(event.pointerId);
}
function paintTrayDrag(){
 const value=trayDrag;if(!value)return;
 if(!value.ghost){value.ghost=createFormationGhost(paintFormation,entry.document,tray[value.index],trayDeployment?.slots[value.index]);draw();}
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
  const target=dropTarget(event);
  if(target?.group==='slots'&&swapTrayMember(entry.document.slots,tray,value.index,target.index)){selected=target.index;selectedTray=-1;mark();renderMember();}
  else if(target?.group==='tray'){
   [tray[value.index],tray[target.index]]=[tray[target.index],tray[value.index]];selectedTray=target.index;storeTray();updateRestrictions();renderMember();
  }else if(target?.group==='remove'){tray[value.index]=null;selectedTray=-1;storeTray();updateRestrictions();renderMember();}
  draw();
 }
 if(trayHost.hasPointerCapture(value.pointerId))trayHost.releasePointerCapture(value.pointerId);
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
  renderDetails=createFormationDetails(database);
  createFormationSearch(database,manifest,addUnit,showError);
  reorder=createFormationReorder(screen,{
    getDocument:()=>entry.document,getDeployment:()=>deployment,paint:paintFormation,canStart:()=>!busy&&!trayDrag,
    onSelect:(slot,refresh=true)=>{selectedTray=-1;selected=slot;if(refresh)renderMember();},onDraw:draw,
    onCommit:()=>{mark();renderMember();},onDrop:(event,slot)=>{
      const target=dropTarget(event);
      if(target?.group==='tray'&&swapTrayMember(entry.document.slots,tray,target.index,slot)){selectedTray=target.index;return true;}
      if(target?.group==='remove'){entry.document.slots[slot]=null;return true;}
      return false;
    }
  });
  render();status.textContent='保存済み';request('/api/formation-equipment').then(result=>{equipment=result.items;renderMember();}).catch(showError);
  screen.addEventListener('click',event=>{if(reorder.suppressClick||reorder.active)return;const slot=event.target.closest('[data-slot]');if(slot){selectedTray=-1;selected=Number(slot.dataset.slot);draw();renderMember();}else{const target=event.target.closest('[data-action]');if(target)action(target.dataset.action);}});
  screen.addEventListener('keydown',event=>{if(['Enter',' '].includes(event.key)){event.preventDefault();event.target.dispatchEvent(new MouseEvent('click',{bubbles:true}));}});
  setInterval(()=>{if(trayDrag&&++trayDrag.ticks>=5)paintTrayDrag();},1000/30);
  trayHost.addEventListener('click',event=>{
    if(suppressTrayClick||busy||reorder?.active)return;
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
  node('formation-member').addEventListener('change',event=>{const target=event.target,member=activeMember();if(!member||!target.checkValidity())return;if(target.dataset.member)member[target.dataset.member]=Number(target.value);if(target.dataset.talent)member.talents[target.dataset.talent]=Number(target.value);if(target.dataset.orb!==undefined)member.orbs[Number(target.dataset.orb)]=target.value?Number(target.value):null;markMember();draw();renderMember();});
  node('formation-member').addEventListener('click',event=>{const button=event.target.closest('button'),member=activeMember();if(!button||!member||reorder?.active)return;if(button.hasAttribute('data-tray-move')){const moved=moveTrayMember(entry.document.slots,tray,selectedTray);if(moved>=0){selected=moved;selectedTray=-1;mark();draw();renderMember();}return;}if(button.hasAttribute('data-orb-add')){if(member.orbs.length<units.get(member.unitId).orbSlots){member.orbs.push(null);markMember();renderMember();}return;}if(button.hasAttribute('data-orb-trim')){member.orbs=member.orbs.slice(0,units.get(member.unitId).orbSlots);markMember();renderMember();return;}if(button.dataset.orbRemove!==undefined){member.orbs.splice(Number(button.dataset.orbRemove),1);markMember();renderMember();return;}if(button.dataset.move){const next=(selected+Number(button.dataset.move)+10)%10;insertMember(entry.document.slots,selected,next);selected=next;mark();draw();renderMember();return;}if(event.target.closest('[data-remove]')){if(selectedTray>=0){tray[selectedTray]=null;selectedTray=-1;storeTray();}else{entry.document.slots[selected]=null;mark();}draw();renderMember();}});
  node('formation-name').addEventListener('change',event=>{const name=event.target.value.trim();if(name){entry.document.name=name;entry.document.slotName=name;mark();draw();}else event.target.value=entry.document.name;});
  node('formation-new').addEventListener('click',()=>exclusive(async()=>{entry={document:blank()};changed=true;await save();render();}));
  for(const [id,key] of [['formation-cannon','id'],['formation-cannon-level','level'],['formation-development-level','developmentLevel']])node(id).addEventListener('change',event=>{if(event.target.checkValidity()){entry.document.cannon[key]=Number(event.target.value);mark();draw();}});
  node('formation-rename').addEventListener('click',()=>{const name=node('formation-slot-name').value.trim();if(!name)return;entry.document.slotName=name;entry.document.name=name;mark();draw();node('formation-menu').close();});
  node('formation-import').addEventListener('click',()=>action('import'));
  node('formation-export').addEventListener('click',()=>exclusive(async()=>{const url=URL.createObjectURL(new Blob([JSON.stringify(entry.document,null,2)],{type:'application/json'})),link=document.createElement('a');link.href=url;link.download=formationDisplayName(entry.document,index).replace(/[<>:"/\\|?*]/g,'_')+'.kbcs.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);node('formation-menu').close();}));
  node('formation-file').addEventListener('change',event=>exclusive(async()=>{const file=event.target.files[0];event.target.value='';if(!file)return;if(file.size>1_000_000)throw new Error('編成ファイルが大きすぎます');const document=JSON.parse(await file.text()),result=await request('/api/formations',{id:entry.id,revision:entry.revision,document});entry=result.entry;count=result.count;index=result.index;changed=false;render();node('formation-menu').close();status.textContent='読込・保存済み';}));
  window.addEventListener('beforeunload',event=>{if(changed){event.preventDefault();event.returnValue='';}});
}catch(error){showError(error);}
