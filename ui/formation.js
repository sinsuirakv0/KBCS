import {formationLayout,insertMember,stepFloating} from './formation-layout.js';
import {loadUnitDatabase} from './src/shared/game/units.js';
import {createFormationMember,resolveFormationMember,formationDisplayName,formationListForm} from './formation-model.js';
import {formationIconHtml,blockedBadgeSvg} from './formation-view.js';
import {formationStageContext,stageDeployment,battleFormation,deploymentReason} from './battle-support.js';
import {escapeHtml as escape} from './src/shared/game/database-view.js';
import {readSimulationProfile} from './simulation-store.js';
import {readGameSettings} from './src/shared/browser/game-settings.js';
import {createSimulationSettings} from './simulation-settings.js';

const node=id=>document.getElementById(id),clone=value=>structuredClone(value);
const names=['にゃんこ砲','スロウ砲','鉄壁砲','かみなり砲','水鉄砲','エンジェル砲','キャノンブレイク砲','呪い砲'];
const status=node('formation-status'),screen=node('formation-screen');status.textContent='読み込み中';
let database,manifest,equipment=[],entry,count=0,index=0,selected=0,changed=false,saving=Promise.resolve(),timer,busy=false,dragged=null;
const units=new Map();
let floating=null,suppressClick=false,stageContext=null,deployment=null,deployVersion=0,deployTimer;
const shifts=Array.from({length:10},()=>({x:0,y:0}));
async function request(path,body){
  const response=await fetch(path,body?{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}:{});
  if(!response.ok)throw new Error(await response.text());return response.json();
}
function blank(){return {format:'kbcs-formation',schemaVersion:1,region:'jp',gameVersion:database.gameVersion,name:'編成'+(count+1),slotName:'編成'+(count+1),slots:Array(10).fill(null),cannon:{id:0,level:30,developmentLevel:30},profile:clone(readSimulationProfile(readGameSettings()))};}
function spriteRect(atlas,rect,x,y,width,height,extra=''){
  const [sx,sy,w,h]=rect,sheet=manifest.atlases[atlas];
  return '<svg x="'+x+'" y="'+y+'" width="'+(width??w)+'" height="'+(height??h)+'" viewBox="'+[sx,sy,w,h].join(' ')+'" preserveAspectRatio="none" '+extra+'><image href="/images/native-formation/'+atlas+'.png" width="'+sheet.width+'" height="'+sheet.height+'"/></svg>';
}
const sprite=(atlas,cut,...args)=>spriteRect(atlas,manifest.atlases[atlas].rects[cut],...args);
// 00446784と同じ中央伸縮。四隅と縁は原本の画素幅を保つ。
function panel(outer,inner,x,y,width,height){
  const a=manifest.atlases.img029_ja.rects[outer],b=manifest.atlases.img029_ja.rects[inner];
  const sw=[b[0]-a[0],b[2],a[0]+a[2]-b[0]-b[2]],sh=[b[1]-a[1],b[3],a[1]+a[3]-b[1]-b[3]],dw=[sw[0],width-sw[0]-sw[2],sw[2]],dh=[sh[0],height-sh[0]-sh[2],sh[2]];
  let result='',sy=a[1],dy=y;
  for(let row=0;row<3;row++){let sx=a[0],dx=x;for(let column=0;column<3;column++){result+=spriteRect('img029_ja',[sx,sy,sw[column],sh[row]],dx,dy,dw[column],dh[row]);sx+=sw[column];dx+=dw[column];}sy+=sh[row];dy+=dh[row];}return result;
}
function digits(text,atlas,first,x,y,height,gap=0){
  let result='';for(const character of String(text)){const cut=first===12?(Number(character)===0?21:11+Number(character)):first+Number(character),rect=manifest.atlases[atlas].rects[cut],width=rect[2]*height/rect[3];result+=sprite(atlas,cut,x,y,width,height);x+=width+gap;}return result;
}
function actionSvg(label,action,content){
  const layout=formationLayout();
  const [x,y,w,h]={menu:[layout.badgeX,61,147,36],previous:[layout.leftX,134,62,97],next:[layout.rightX,134,62,97],cannon:[layout.width-65,80,66,51],clear:[-7,220,80,80]}[action];
  return content+'<rect role="button" tabindex="0" aria-label="'+escape(label)+'" data-action="'+action+'" x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="transparent"/>';
}
function draw(){
  const doc=entry.document,layout=formationLayout();
  let body='<rect width="1188" height="278" fill="#d4b15f"/>'+sprite('img008_ja',0,0,0,1188,55)+sprite('img008_ja',3,8,3,297,46)+'<path d="M0 55H1188V79H0Z" fill="#ffe290"/><path d="M0 79H1188" stroke="#706241"/>';
  // 原本の子スプライトは親中心+51、中心揃え。11件以上の保存番号はPC用文字表示。
  const badgeNumber=index<=10?sprite('img029_ja',43+index,layout.badgeX+124-Math.trunc(25/2),67,25,24):'<text x="'+(layout.badgeX+124)+'" y="89" text-anchor="middle" fill="white" stroke="black" stroke-width="2" paint-order="stroke" font-size="'+Math.min(24,44/String(index).length)+'" font-weight="bold">'+index+'</text>';
  body+=actionSvg('出陣スロットの操作','menu',sprite('img029_ja',5,layout.badgeX,61,147,36)+badgeNumber);
  // 00a71320 / 00a82394: 名前欄はcut120/121、中央揃え、原本param.tsvの余白。
  const parameters=manifest.parameters.values,nameWidth=147-2*parameters.slot_name_margin_left;
  if(doc.slotName)body+=panel(120,121,layout.badgeX,parameters.slot_bg_y,147,27)+'<text data-slot-name x="'+(layout.badgeX+73)+'" y="'+(parameters.slot_bg_y+parameters.slot_name_margin_top)+'" text-anchor="middle" dominant-baseline="text-before-edge" fill="white" font-size="'+parameters.slot_font_size+'">'+escape(doc.slotName)+'</text>';
  body+=actionSvg('前の編成','previous',sprite('img006_ja',8,layout.leftX,134,62,97));
  body+=actionSvg('次の編成','next','<g transform="translate('+(2*layout.rightX+62)+' 0) scale(-1 1)">'+sprite('img006_ja',8,layout.rightX,134,62,97)+'</g>');
  body+=sprite('img029_ja',7,layout.pageX,110+manifest.parameters.values.slot_page_y_offset)+sprite('img029_ja',8,layout.pageX,205+manifest.parameters.values.slot_page_y_offset);
  body+='<rect x="290" y="160" width="696" height="4" fill="#9b8247"/><rect x="290" y="255" width="696" height="4" fill="#9b8247"/>';
  // 00a82394は占有状態に関係なく、番号付きの10枠を先に描く。
  for(const [slot,{x,y}] of layout.slots.entries()){
    const rect=manifest.atlases.img029_ja.rects[64+slot];
    body+='<rect x="'+(x+2)+'" y="'+(y+2)+'" width="111" height="85" fill="#54472a"/><rect x="'+x+'" y="'+y+'" width="111" height="85" fill="#9b8247"/>'+sprite('img029_ja',64+slot,x+55-Math.trunc(rect[2]/2),y+42-Math.trunc(rect[3]/2),rect[2],rect[3]);
  }
  let floatingBody='';
  for(let slot=0;slot<10;slot++){
    const {x,y}=layout.slots[slot],member=doc.slots[slot],unit=member&&units.get(member.unitId),effective=unit&&resolveFormationMember(unit,member),form=unit?.forms.find(form=>form.index===effective.form);
    let contents='';
    if(form){
      // 0063fa4c / 00a8b028: 元画像の自然寸法を保ち、uni.imgcutの110×85を切り抜く。
      contents+='<svg x="'+x+'" y="'+y+'" width="110" height="85" viewBox="'+manifest.unitIcon.rect.join(' ')+'" preserveAspectRatio="none"><image href="'+escape(database.imageBase+form.icon)+'"/></svg>';
      // 005d1bb4 → 00448048。通常編成のcut60〜70、文字間隔-3、右寄せと円の予約幅22。
      const price=String(Math.floor(form.cost*1.5));
      contents+=digits(price,'img023_ja',60,x+88-price.length*15,y+61,26,-3)+sprite('img023_ja',70,x+91,y+61,22,26);
    }
    if(form&&deployment?.slots[slot].reasons)contents+=blockedBadgeSvg(manifest,x,y);
    if(selected===slot&&form&&floating?.slot!==slot)contents+=panel(9,25,x,y,110,85);
    if(floating?.slot===slot){
      const width=110+Math.trunc(floating.growth*110/100),height=85+Math.trunc(floating.growth*85/100);
      const left=x+floating.x-Math.trunc(floating.growth*110/200),top=y+floating.y-Math.trunc(floating.growth*85/200);
      floatingBody='<g pointer-events="none" opacity="'+((255-floating.alpha)/255)+'" transform="translate('+left+' '+top+') scale('+(width/110)+' '+(height/85)+') translate('+(-x)+' '+(-y)+')">'+contents+'</g>';
    }else body+='<g transform="translate('+shifts[slot].x+' '+shifts[slot].y+')">'+contents+'</g>';
    body+='<rect role="button" tabindex="0" data-slot="'+slot+'" aria-label="枠'+(slot+1)+' '+escape(form?.name??'空き')+'" aria-pressed="'+(selected===slot)+'" x="'+x+'" y="'+y+'" width="110" height="85" fill="transparent"/>';

  }
  body+=actionSvg('城砲を変更','cannon',panel(101,102,layout.width-172,59,271,27)+'<text x="'+(layout.width-86)+'" y="79" text-anchor="middle" fill="white" font-size="18" font-weight="bold">'+names[doc.cannon.id]+'</text>'+sprite('img029_ja',100,layout.width-55,90,46,36));
  body+=actionSvg('編成中のキャラをすべて外す','clear',sprite('img029_ja',132,13,230,40,40))+floatingBody;
  document.title=formationDisplayName(doc,index)+' | KBCS';screen.innerHTML='<svg class="formation-native" viewBox="0 0 1188 278" aria-label="キャラクター編成">'+body+'</svg>';
  const nameLabel=screen.querySelector('[data-slot-name]');
  if(nameLabel&&nameLabel.getComputedTextLength()>nameWidth){nameLabel.setAttribute('textLength',nameWidth);nameLabel.setAttribute('lengthAdjust','spacingAndGlyphs');}
  node('formation-position').textContent=index+' / '+count;node('formation-name').value=formationDisplayName(doc,index);
  if(entry.id){const route=new URLSearchParams(location.search);route.set('id',entry.id);history.replaceState(null,'','/pages/formation/?'+route);}
}
function mark(){clearTimeout(deployTimer);deployTimer=setTimeout(updateRestrictions,180);changed=true;status.textContent='保存待ち';clearTimeout(timer);timer=setTimeout(()=>save().catch(showError),350);}
function showError(error){status.textContent=error.message;status.dataset.error='true';}
async function save(){
  clearTimeout(timer);
  // 保存を直列化し、前の応答で編集途中のドキュメントを上書きしない。
  saving=saving.catch(()=>{}).then(async()=>{
    if(!changed)return;
    const current=entry,snapshot=clone(current.document);changed=false;status.textContent='保存中';
    try{const result=await request('/api/formations',{id:current.id??null,revision:current.revision??null,document:snapshot});current.id=result.entry.id;current.revision=result.entry.revision;count=result.count;index=result.index;status.textContent=changed?'保存待ち':'保存済み';delete status.dataset.error;try{localStorage.setItem('kbcs:formation-update',Date.now()+':'+current.id+':'+current.revision);}catch{}}
    catch(error){changed=true;throw error;}
  });return saving;
}
async function exclusive(task){
  if(busy||dragged||floating)return;busy=true;
  const controls=document.querySelectorAll('#formation-screen,.formation-toolbar,.formation-library,#formation-member,#formation-profile');
  for(const control of controls)control.inert=true;
  try{await save();await task();}catch(error){showError(error);}finally{busy=false;for(const control of controls)control.inert=false;}
}
async function updateRestrictions(){
  if(!entry||!stageContext)return;
  const version=++deployVersion;
  try{
    const value=await stageDeployment(database,stageContext.map,stageContext.stage,stageContext.crown,battleFormation(database,entry.document));
    if(version!==deployVersion)return;deployment=value;draw();
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
  const member=entry.document.slots[selected],unit=member&&units.get(member.unitId),host=node('formation-member');
  if(!unit){host.innerHTML='<h2>枠'+(selected+1)+'</h2>';return;}
  const effective=resolveFormationMember(unit,member),advancedLocked=unit.rarity===4&&member.level<60,capacity=unit.orbSlots;
  const talents=unit.talents.length?'<details><summary>本能・超本能</summary>'+unit.talents.map(talent=>'<label>'+escape((talent.limit?'超本能：':'')+talent.name)+'<select '+(advancedLocked&&talent.limit?'disabled':'')+' data-talent="'+talent.index+'">'+Array.from({length:talent.maxLevel+1},(_,level)=>'<option value="'+level+'" '+(level===(member.talents[talent.index]??0)?'selected':'')+'>'+level+'</option>').join('')+'</select></label>').join('')+'</details>':'';
  const orbs=capacity?'<details><summary>本能玉 '+Math.min(member.orbs.length,capacity)+' / '+capacity+'</summary>'+orbRows(member)+'<button data-orb-add '+(member.orbs.length>=capacity?'disabled':'')+'>玉を追加</button>'+(member.orbs.length>capacity?'<button data-orb-trim>上限を超えた設定を外す</button>':'')+'</details>':'';
  host.innerHTML='<h2>'+escape(unit.forms.find(form=>form.index===effective.form)?.name??'未収録キャラ')+'</h2><label>形態<select data-member="form">'+unit.forms.map(form=>'<option value="'+form.index+'" '+(form.index===effective.form?'selected':'')+' '+(advancedLocked&&form.index===3?'disabled':'')+'>'+escape(form.name)+'</option>').join('')+'</select></label>'+((advancedLocked&&(unit.forms.some(form=>form.index===3)||unit.talents.some(talent=>talent.limit)))?'<p class="formation-level-lock">超本能・第4形態はLv60から有効</p>':'')+'<div class="formation-levels"><label>Lv<input type="number" min="1" max="'+unit.maxLevel+'" value="'+member.level+'" data-member="level"></label><label>＋<input type="number" min="0" max="'+(unit.plusLevel??0)+'" value="'+member.plus+'" data-member="plus"></label></div><button data-remove>枠から外す</button>'+talents+orbs+'<div class="formation-move"><button data-move="-1">◀ 枠移動</button><button data-move="1">枠移動 ▶</button></div>';
}
function render(){draw();renderMember();renderSettings();updateRestrictions();}
function filter(){
  const query=node('formation-search').value.normalize('NFKC').toLowerCase(),choice=node('formation-display-form').value;
  const found=database.units.filter(unit=>!unit.isSpirit&&(String(unit.id)===query||[...unit.aliases,...unit.forms.map(form=>form.name)].join(' ').normalize('NFKC').toLowerCase().includes(query)));
  node('formation-results').innerHTML=found.slice(0,90).map(unit=>{const form=formationListForm(unit,choice);return '<button data-unit="'+unit.id+'" aria-label="'+escape(form.name)+'">'+formationIconHtml(database,form,manifest)+'<span>'+escape(form.name)+'</span></button>';}).join('')+(found.length>90?'<p>検索して絞り込む</p>':'');
}

function action(name){
  if(busy||dragged||floating)return;
  if(name==='clear'){if(entry.document.slots.some(Boolean)){entry.document.slots.fill(null);selected=0;mark();draw();renderMember();}}
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
function animateFormation(){
  if(!entry)return;
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
  [database,manifest]=await Promise.all([loadUnitDatabase(),request('/images/native-formation/manifest.json')]);
  await Promise.all(Object.entries(manifest.atlases).map(async([name,atlas])=>{const image=new Image();image.src='/images/native-formation/'+name+'.png';await image.decode();atlas.width=image.naturalWidth;atlas.height=image.naturalHeight;}));
  for(const unit of database.units)units.set(unit.id,unit);
  const requested=new URLSearchParams(location.search).get('id');
  const result=await request('/api/formations'+(requested?'?current='+encodeURIComponent(requested):''));entry=result.entry;count=result.count;index=result.index;
  if(!entry){entry={document:blank()};changed=true;await save();}
  node('formation-cannon').innerHTML=names.map((name,id)=>'<option value="'+id+'">'+name+'</option>').join('');
  stageContext=await formationStageContext(new URLSearchParams(location.search));
  if(stageContext){if(stageContext.buildId!==database.buildId)throw Error('DBが更新されました。再読み込みしてください');const host=node('formation-context');host.hidden=false;const params=new URLSearchParams({map:stageContext.map.key,stage:stageContext.stage.index,crown:stageContext.crown});host.innerHTML='<a href="/pages/stage-sortie/?'+params+'">'+escape(stageContext.stage.name)+' / '+stageContext.crown+'冠の出撃準備に戻る</a>'; }
  try{node('formation-display-form').value=sessionStorage.getItem('kbcs:formation:display-form')||'max';}catch{}
  render();filter();status.textContent='保存済み';request('/api/formation-equipment').then(result=>{equipment=result.items;renderMember();}).catch(showError);
  screen.addEventListener('click',event=>{if(suppressClick)return;const slot=event.target.closest('[data-slot]');if(slot){selected=Number(slot.dataset.slot);draw();renderMember();}else{const target=event.target.closest('[data-action]');if(target)action(target.dataset.action);}});
  screen.addEventListener('keydown',event=>{if(['Enter',' '].includes(event.key)){event.preventDefault();event.target.dispatchEvent(new MouseEvent('click',{bubbles:true}));}});
  screen.addEventListener('pointerdown',event=>{
    const target=event.target.closest('[data-slot]');if(!target||event.button!==0||busy||floating)return;
    const slot=Number(target.dataset.slot);if(!entry.document.slots[slot])return;
    const pointer=pointerPosition(event),base=formationLayout().slots[slot];
    dragged={slot,pointer,grab:{x:pointer.x-base.x,y:pointer.y-base.y},ticks:0,pointerId:event.pointerId,snapshot:clone(entry.document.slots)};
    screen.setPointerCapture(event.pointerId);
    selected=slot;draw();renderMember();
  });
  screen.addEventListener('pointermove',event=>{if(dragged&&dragged.pointerId===event.pointerId)dragged.pointer=pointerPosition(event);});
  screen.addEventListener('pointerup',event=>{if(dragged&&dragged.pointerId===event.pointerId){dragged.pointer=pointerPosition(event);finishDrag();}});
  screen.addEventListener('pointercancel',()=>finishDrag(true));
  screen.addEventListener('lostpointercapture',()=>finishDrag(true));
  window.addEventListener('blur',()=>finishDrag(true));
  setInterval(animateFormation,1000/30);
  node('formation-search').addEventListener('input',filter);
  node('formation-display-form').addEventListener('change',event=>{try{sessionStorage.setItem('kbcs:formation:display-form',event.target.value);}catch{}filter();});
  node('formation-results').addEventListener('click',event=>{const button=event.target.closest('[data-unit]');if(!button||busy||dragged||floating)return;const id=Number(button.dataset.unit),slots=entry.document.slots,existing=slots.findIndex(member=>member?.unitId===id);if(existing>=0)[slots[selected],slots[existing]]=[slots[existing],slots[selected]];else slots[selected]=createFormationMember(units.get(id));mark();draw();renderMember();});
  node('formation-member').addEventListener('change',event=>{const target=event.target,member=entry.document.slots[selected];if(!member||!target.checkValidity())return;if(target.dataset.member)member[target.dataset.member]=Number(target.value);if(target.dataset.talent)member.talents[target.dataset.talent]=Number(target.value);if(target.dataset.orb!==undefined)member.orbs[Number(target.dataset.orb)]=target.value?Number(target.value):null;mark();draw();if(target.dataset.member==='form'||target.dataset.member==='level')renderMember();});
  node('formation-member').addEventListener('click',event=>{const button=event.target.closest('button'),member=entry.document.slots[selected];if(!button||!member||dragged||floating)return;if(button.hasAttribute('data-orb-add')){if(member.orbs.length<units.get(member.unitId).orbSlots){member.orbs.push(null);mark();renderMember();}return;}if(button.hasAttribute('data-orb-trim')){member.orbs=member.orbs.slice(0,units.get(member.unitId).orbSlots);mark();renderMember();return;}if(button.dataset.orbRemove!==undefined){member.orbs.splice(Number(button.dataset.orbRemove),1);mark();renderMember();return;}if(button.dataset.move){const next=(selected+Number(button.dataset.move)+10)%10;insertMember(entry.document.slots,selected,next);selected=next;mark();draw();renderMember();return;}if(event.target.closest('[data-remove]')){entry.document.slots[selected]=null;mark();draw();renderMember();}});
  node('formation-name').addEventListener('change',event=>{const name=event.target.value.trim();if(name){entry.document.name=name;entry.document.slotName=name;mark();draw();}else event.target.value=entry.document.name;});
  node('formation-new').addEventListener('click',()=>exclusive(async()=>{entry={document:blank()};changed=true;await save();render();}));
  for(const [id,key] of [['formation-cannon','id'],['formation-cannon-level','level'],['formation-development-level','developmentLevel']])node(id).addEventListener('change',event=>{if(event.target.checkValidity()){entry.document.cannon[key]=Number(event.target.value);mark();draw();}});
  node('formation-rename').addEventListener('click',()=>{const name=node('formation-slot-name').value.trim();if(!name)return;entry.document.slotName=name;entry.document.name=name;mark();draw();node('formation-menu').close();});
  node('formation-import').addEventListener('click',()=>action('import'));
  node('formation-export').addEventListener('click',()=>exclusive(async()=>{const url=URL.createObjectURL(new Blob([JSON.stringify(entry.document,null,2)],{type:'application/json'})),link=document.createElement('a');link.href=url;link.download=formationDisplayName(entry.document,index).replace(/[<>:"/\\|?*]/g,'_')+'.kbcs.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);node('formation-menu').close();}));
  node('formation-file').addEventListener('change',event=>exclusive(async()=>{const file=event.target.files[0];event.target.value='';if(!file)return;if(file.size>1_000_000)throw new Error('編成ファイルが大きすぎます');const document=JSON.parse(await file.text()),result=await request('/api/formations',{id:entry.id,revision:entry.revision,document});entry=result.entry;count=result.count;index=result.index;changed=false;render();node('formation-menu').close();status.textContent='読込・保存済み';}));
  window.addEventListener('beforeunload',event=>{if(changed){event.preventDefault();event.returnValue='';}});
}catch(error){showError(error);}
