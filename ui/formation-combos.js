import {escapeHtml as esc} from './src/shared/game/database-view.js';
import {normalizeUnitQuery} from './src/features/units/model.js';
import {createFormationMember,resolveFormationMember} from './formation-model.js';
import {createNativeSprites} from './native-sprites.js';
import {nativeFont,loadNativeFonts} from './native-font.js';

const plain=value=>String(value??'').replace(/<br>/g,'\n').replace(/<[^>]*>/g,'');
export function activeFormationCombos(database,slots){
 const team=new Map(slots.slice(0,5).filter(Boolean).map(member=>[member.unitId,member.form]));
 return database.combos.filter(combo=>combo.members.every(member=>team.has(member.id)&&team.get(member.id)>=member.form)).sort((a,b)=>a.members.length-b.members.length);
}
// 00895118の10枠更新。既存キャラの個別設定を複製して、保存は既存の編成APIへ戻す。
export function applyComboPlan(database,slots,plan){
 const existing=new Map(slots.filter(Boolean).map(member=>[member.unitId,member]));
 return plan.slots.map(id=>id<0?null:structuredClone(existing.get(id)||createFormationMember(database.units.find(unit=>unit.id===id))));
}
export async function createFormationCombos(database,getDocument,onApply,request){
 const [manifest,layout,inventory]=await Promise.all([request('/images/native-combo/manifest.json'),request('/api/combo-layout?width=1188'),request('/api/inventory'),loadNativeFonts()]);
 const W=1188,margin=(W-960)/2,{sprite,panel,slice}=createNativeSprites(manifest),units=new Map(database.units.map(unit=>[unit.id,unit]));
 const combos=[...database.combos].sort((a,b)=>a.members.length-b.members.length),definitions=combos.map(combo=>({units:Array.from({length:5},(_,i)=>combo.members[i]?.id??-1),forms:Array.from({length:5},(_,i)=>combo.members[i]?.form??0)}));
 const dialog=document.createElement('dialog');dialog.className='native-combo-dialog';dialog.setAttribute('aria-label','にゃんコンボ図鑑');document.body.append(dialog);
 const search=document.createElement('input');search.type='search';search.placeholder='コンボ名・キャラ名・ID';search.setAttribute('aria-label',search.placeholder);search.className='native-combo-query';
 const status=document.createElement('span');status.className='native-combo-status';status.setAttribute('role','status');
 const canvas=document.createElement('div');canvas.className='native-combo-canvas';dialog.append(search,status,canvas);
 const guide=document.createElement('div');guide.className='native-combo-guide';guide.hidden=true;
 guide.innerHTML='<iframe title="にゃんコンボについて" sandbox="allow-same-origin" referrerpolicy="no-referrer"></iframe><button type="button" aria-label="説明を閉じる"><img src="/images/native-combo/cancel.png" alt=""></button>';
 canvas.append(guide);guide.querySelector('button').addEventListener('click',()=>{help=false;render();});
 const counts=new Map(inventory.items.map(item=>[item.id,item.displayCount]));
 const measure=document.createElement('canvas').getContext('2d');measure.font=nativeFont(20);
 const patternOpacity=()=> (140+Math.trunc(Math.fround(Math.fround(Math.cos(flash*Math.PI/180))*115)))/255;
 let notice='',lastTap=null,suppressClick=false,popupPhase=5,selectedUnit=null;
 let page=0,selection=-1,unitFilter=null,types=new Set(),pendingTypes=new Set(),filter=false,scroll=0,query='',confirm=null,help=false,locked=false,selectedEffect=null,flash=0,interval;
 const seenKey='kbcs:combo-seen',seen=new Set();try{for(const id of JSON.parse(localStorage.getItem(seenKey)||'[]'))if(Number.isInteger(id))seen.add(id);}catch{}
 let fresh=new Set(combos.filter(combo=>!seen.has(combo.id)).map(combo=>combo.id));
 const saveSeen=()=>{try{localStorage.setItem(seenKey,JSON.stringify([...seen]));}catch{}};
 const effectiveSlots=()=>getDocument().slots.map(member=>member&&resolveFormationMember(units.get(member.unitId),member));
 function filtered(){const words=normalizeUnitQuery(query).split(/\s+/).filter(Boolean),selectedTypes=[...types].filter(type=>type!==100);return combos.filter(combo=>(!selectedTypes.length||selectedTypes.includes(combo.type))&&(!types.has(100)||fresh.has(combo.id))&&(unitFilter==null||combo.members.some(member=>member.id===unitFilter))&&words.every(word=>normalizeUnitQuery([combo.name,combo.effect,...combo.members.flatMap(member=>[String(member.id),...(units.get(member.id)?.forms||[]).map(form=>form.name)])].join(' ')).includes(word)));}
 function text(value,x,y,size=20,color='white',extra=''){return '<text x="'+x+'" y="'+y+'" text-anchor="middle" dominant-baseline="text-before-edge" font-size="'+size+'" fill="'+color+'" '+extra+'>'+esc(plain(value))+'</text>';}
 function hit(action,x,y,w,h,label,extra=''){return '<rect data-combo-action="'+action+'" x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="transparent" role="button" tabindex="0" aria-label="'+esc(label)+'" '+extra+'/>';}
 function center(atlas,index,x,y,scale=1){const [, ,w,h]=manifest.atlases[atlas].rects[index];return sprite(atlas,index,x-w*scale/2,y-h*scale/2,w*scale,h*scale);}
 function icon(id,form,x,y,w=88,h=68){const unit=units.get(id),value=unit?.forms.find(value=>value.index===form);return sprite('img029_ja',33,x,y)+(value?.icon?'<svg x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" viewBox="9 21 110 85"><image href="'+esc(database.imageBase+value.icon)+'"/></svg>':'');}
 // 00a6c1f0/00a6c358→00448048。持ち物の表示数だけを読み、ここでは増減しない。
 function currency(kind,y){
  const top=kind==='xp',left=W-manifest.atlases.img024_ja.rects[11][2];
  let html=top?sprite('img024_ja',11,left,0)+sprite('img024_ja',10,left-100,17)+sprite('img006_ja',23,left-37,8,62,36):'<g transform="translate(0 1225) scale(1 -1)">'+sprite('img024_ja',11,left,585)+'</g>'+sprite('img006_ja',21,left+18,588,55,42)+sprite('img006_ja',24,left+10,617,76,25);
  const digits=String(Math.min(2147483647,counts.get(manifest.currencies[kind])||0));let x=W-6-[...digits].reduce((w,n)=>w+manifest.atlases.img024_ja.rects[Number(n)][2],0)+(digits.length-1);
  for(const n of digits){html+=sprite('img024_ja',Number(n),x,y);x+=manifest.atlases.img024_ja.rects[Number(n)][2]-1;}
  return html;
 }
 function list(){
  const values=filtered(),pages=Math.max(1,Math.ceil(values.length/4));page=Math.min(page,pages-1);
  const active=new Set(activeFormationCombos(database,effectiveSlots()).map(combo=>combo.id));
  let html='<defs><filter id="combo-bg" color-interpolation-filters="sRGB"><feComponentTransfer><feFuncR type="linear" slope="'+(82/255)+'"/><feFuncG type="linear" slope="'+(203/255)+'"/><feFuncB type="linear" slope="'+(156/255)+'"/></feComponentTransfer></filter><filter id="combo-pattern" color-interpolation-filters="sRGB"><feComponentTransfer><feFuncR type="linear" slope="'+(115/255)+'"/><feFuncG type="linear" slope="'+(211/255)+'"/><feFuncB type="linear" slope="'+(156/255)+'"/></feComponentTransfer></filter><filter id="combo-flash" color-interpolation-filters="sRGB"><feComponentTransfer><feFuncR data-flash-r type="linear" slope="1"/><feFuncG data-flash-g type="linear" slope="1"/><feFuncB data-flash-b type="linear" slope="1"/></feComponentTransfer></filter></defs><g filter="url(#combo-bg)">'+sprite('img015',76,-40,0,W+80,640)+'</g><g data-combo-pattern filter="url(#combo-pattern)" opacity="'+(patternOpacity())+'">'+sprite('img016',0,0,0,W,W*manifest.atlases.img016.rects[0][3]/manifest.atlases.img016.rects[0][2])+'</g>';
  html+=sprite('img008_ja',0,0,0,W,55)+sprite('img050_02',3,8,3);
  html+='<g transform="translate(0 1225) scale(1 -1)">'+sprite('img008_ja',0,0,585,W,55)+'</g>';
  html+=center('img015',123,W/2-376,99)+center('img015',57,W/2-376,99)+hit('filter',W/2-440,72,129,55,'コンボ絞り込み');
  html+=panel('img029_ja',34,75,W/2+55,88,386,32);
  const name=selectedUnit?selectedUnit.rarity+selectedUnit.name:manifest.texts.nyancombo_txt1,compressed=measure.measureText(plain(name)).width>308;
  html+='<text x="'+(W/2+245)+'" y="92" text-anchor="middle" dominant-baseline="text-before-edge" font-size="20" fill="white"'+(compressed?' textLength="308" lengthAdjust="spacingAndGlyphs"':'')+'>'+(selectedUnit?'<tspan fill="#ffd400">'+esc(selectedUnit.rarity)+'</tspan>'+esc(selectedUnit.name):esc(name))+'</text>';
  html+=center('img015',280,W/2+79,104)+(unitFilter==null?'':center('img015',279,W/2+79,104))+hit('unit-filter',W/2+55,80,48,48,'表示中のキャラを含むコンボに絞る','aria-pressed="'+(unitFilter!=null)+'"');
  for(const [row,combo] of values.slice(page*4,page*4+4).entries()){
   const r=layout.rows[Number(combo.group!==-1)][row],[x,y,w,h]=r.panel;
   html+=panel('img029_ja',31,32,x,y,w,h);
   if(active.has(combo.id)||locked&&selection===combo.id)html+='<g filter="url(#combo-flash)">'+panel('img029_ja',41,74,x,y,w,h,2)+'</g>';
   html+=text(combo.name,...r.name,30)+text(combo.effect,...r.effect,20)+(combo.group!==-1?text(combo.groupName,...r.group,20):'');
   html+=hit('combo:'+combo.id,x,y,380,h,combo.name+'：ダブルタップで自動セット');
   for(let i=0;i<5;++i){const member=combo.members[i],[ix,iy,iw,ih]=r.icons[i];html+=icon(member?.id,member?.form,ix,iy,iw,ih);if(member)html+=hit('unit:'+combo.id+':'+i,ix,iy,iw,ih,units.get(member.id)?.forms.find(form=>form.index===member.form)?.name||'キャラ');}
   if(selectedUnit?.combo===combo.id){const [ix,iy,iw,ih]=r.icons[selectedUnit.index];for(let frame=0;frame<2;++frame)html+='<g data-combo-highlight="'+frame+'"'+(frame===Math.floor(flash/2)%2?'':' display="none"')+'>'+panel('img029_ja',9+frame,25+frame,ix,iy,iw,ih)+'</g>';}
   if(fresh.has(combo.id))html+='<image href="'+manifest.atlases.img034.url+'" x="'+(x-13)+'" y="'+(y-27)+'" width="64" height="64"/>';
   seen.add(combo.id);
  }
  saveSeen();
  for(const [key,y] of [['nyancombo_txt10',534],['nyancombo_txt11',554]]){html+=text(manifest.texts[key],W/2+1,y+1,19,'#404040')+text(manifest.texts[key],W/2,y,19);}
  if(page>0)html+='<g data-combo-arrow="left" opacity=".447">'+sprite('img006_ja',8,Math.trunc(24+Math.sin(flash*Math.PI/6)*10),255)+'</g>'+hit('previous',4,220,95,150,'前のページ');
  if(page+1<pages)html+='<g data-combo-arrow="right" opacity=".447" transform="translate('+W+' 0) scale(-1 1)">'+sprite('img006_ja',8,Math.trunc(24+Math.sin(flash*Math.PI/6)*10),255)+'</g>'+hit('next',W-99,220,95,150,'次のページ');
  html+=center('img006_ja',9,51,588)+center('img006_ja',3,50,588)+hit('back',4,541,95,95,'編成へ戻る');
  html+=currency('xp',6)+currency('catfood',592);
  html+=center('img029_ja',28,213,618)+hit('help',115,604,197,28,'にゃんコンボとは？');
  status.textContent=notice||((page+1)+' / '+pages+'　'+values.length+'件');
  return html;
 }
 function filterPanel(){
  let content='',y=105;
  for(const group of manifest.filters){
   for(const [i,type]of group.types.entries()){
    const x=margin+224+(i%3)*211,top=y+Math.floor(i/3)*65;
    content+=center('img015',pendingTypes.has(type)?0:1,x+105,top+27)+'<image href="'+manifest.filterLabels[type]+'" x="'+(x+28.5)+'" y="'+(top+8)+'" width="153" height="38" preserveAspectRatio="xMidYMid meet"/>';
    content+=hit('type:'+type,x,top,211,54,plain(database.comboEffects[type]?.label||'NEW'), 'aria-pressed="'+pendingTypes.has(type)+'"');
   }
   const last=Math.floor((group.types.length-1)/3)*65;
   content+=sprite('img015',282+group.id,margin+75,y+(last+54)/2-19);
   const lineY=y+last+62;content+=sprite('img015',27,margin+76,lineY)+sprite('img015',28,margin+82,lineY,796,6)+sprite('img015',29,margin+878,lineY);y+=last+76;
  }
  scroll=Math.max(0,Math.min(scroll,Math.max(0,y-560)));
  let html='<rect width="1188" height="640" fill="#000" opacity=".7"/>';
  for(const [cut,x,top,w,h]of [[26,64,91,842,474],[22,64,21,842,88],[24,64,545,842,90],[25,30,91,39,474],[21,30,21,39,88],[23,30,545,39,90]])html+=sprite('img015',cut,margin+x,top,w,h);
  html+='<g transform="translate('+(2*(margin+930))+' 0) scale(-1 1)">';for(const [cut,top,h]of [[25,91,474],[21,21,88],[23,545,90]])html+=sprite('img015',cut,margin+930,top,39,h);html+='</g>';
  html+=sprite('img015',30,margin+393,35)+'<defs><clipPath id="combo-filter-clip"><rect x="'+margin+'" y="93" width="960" height="455"/></clipPath></defs><g clip-path="url(#combo-filter-clip)"><g transform="translate(0 '+(-scroll)+')">'+content+'</g></g>';
  html+=center('img015',125,margin+482,591,1.33)+center('img015',124,margin+482,591)+hit('filter-apply',margin+317,559,330,64,'絞り込みを適用');
  html+=center('img015',123,margin+838,591,1.33)+center('img015',34,margin+838,591)+hit('filter-clear',margin+765,559,146,64,'絞り込みをクリア');
  html+=center('img015',126,margin+910,44)+hit('filter-close',margin+876,10,68,68,'絞り込みを閉じる');
  return html;
 }
 function confirmation(){
  const [x,y,w,h]=layout.popup[4].window,cut=manifest.atlases.img005_1.rects[0],padding=manifest.atlases.img005_1.rects[8];
  let html='<rect width="1188" height="640" fill="#000" opacity="'+(178/255)+'"/>';
  if(popupPhase<5){const [left,top,width,height]=layout.popup[popupPhase].window;return html+(width?slice('img005_1',cut,[padding[0],padding[1],cut[2]-padding[0]*2,cut[3]-padding[1]*2],left,top,width,height,2.7):'');}
  html+=slice('img005_1',cut,[padding[0],padding[1],cut[2]-padding[0]*2,cut[3]-padding[1]*2],x,y,w,h,2.7);
  html+=text(manifest.texts.nyancombo_overwrite_popup_title,W/2,y+25,28)+sprite('img029_ja',110,W/2-300,y+99)+sprite('img029_ja',111,W/2-300,y+209)+sprite('img029_ja',112,W/2-10,y+159);
  for(let i=0;i<5;++i){for(const [slots,top]of [[getDocument().slots,y+82],[confirm.document.slots,y+192]]){const member=slots[i];html+=icon(member?.unitId,member&&resolveFormationMember(units.get(member.unitId),member).form,W/2-210+i*103,top);if(member&&selectedEffect?.members.some(value=>value.id===member.unitId)){for(let frame=0;frame<2;++frame)html+='<g data-combo-highlight="'+frame+'"'+(frame===Math.floor(flash/2)%2?'':' display="none"')+'>'+panel('img029_ja',9+frame,25+frame,W/2-210+i*103,top,88,68)+'</g>';}}}
  // 008920f8→0088e208: 新規(黄)、維持(白)、解除(灰)をまとめ、先頭4件を左に置く。
  const before=new Set(confirm.before.map(combo=>combo.id)),after=new Set(confirm.after.map(combo=>combo.id));
  const first=list=>list.sort((a,b)=>Number(b.id===confirm.combo.id)-Number(a.id===confirm.combo.id));
  const changes=[...first(confirm.after.filter(combo=>!before.has(combo.id))).map(combo=>[combo,'#ff0']),...first(confirm.before.filter(combo=>after.has(combo.id))).map(combo=>[combo,'#fff'])];
  if(!after.has(confirm.combo.id))changes.push([confirm.combo,'#808080']);
  changes.push(...confirm.before.filter(combo=>!after.has(combo.id)&&combo.id!==confirm.combo.id).map(combo=>[combo,'#808080']));
  for(const [i,[combo,color]]of changes.entries()){
   const left=W/2+(i<4?-255:45),top=y+278+(i%4)*23;
   html+='<text x="'+left+'" y="'+top+'" dominant-baseline="text-before-edge" font-size="20" fill="'+color+'"'+(selectedEffect?.id===combo.id?' data-combo-text-flash="1"':'')+'>'+esc(combo.name)+'</text>'+hit('effect:'+combo.id,left,top,245,23,combo.name+'の効果');
  }
  html+=panel('img029_ja',101,102,W/2-176,y+h-52,353,29)+text(selectedEffect?.effect||manifest.texts.nyancombo_overwrite_popup_description,W/2,y+h-40,20);
  const a=manifest.atlases.img005_1.rects[1],origin=manifest.atlases.img005_1.rects[0],p=manifest.atlases.img005_1.rects[7],px=p[0]-origin[0],py=p[1]-origin[1];html+=slice('img005_1',a,[px,py,a[2]-px*2,a[3]-py*2],W/2-84,y+h+8,168,72)+center('img005_1',6,W/2,y+h+44)+hit('confirm',W/2-84,y+h+8,168,72,'コンボをセット');
  html+=sprite('img005_1',11,x+w-36,y-36,72,72)+hit('cancel',x+w-36,y-36,72,72,'セットせず閉じる');
  return html;
 }
 function render(){
  let body=list();if(filter)body+=filterPanel();if(confirm)body+=confirmation();
  canvas.querySelector('svg')?.remove();canvas.insertAdjacentHTML('afterbegin','<svg viewBox="0 0 1188 640" role="group" aria-label="にゃんコンボ図鑑">'+body+'</svg>');guide.hidden=!help;const frame=guide.querySelector('iframe');if(help&&!frame.src)frame.src='https://ponosgames.com/information/appli/battlecats/combo/index.html';search.disabled=filter||!!confirm||locked||help;
 }
 async function preview(id){
  if(locked)return;locked=true;status.textContent='編成を確認中';
  try{await new Promise(resolve=>setTimeout(resolve,14*1000/30));const document=getDocument(),effective=effectiveSlots(),selected=combos.findIndex(combo=>combo.id===id),plan=await request('/api/combo-plan',{combos:definitions,selection:{team:effective.map(member=>member?.unitId??-1),forms:effective.map(member=>member?.form??0),locked:Array(10).fill(0),selected}});const next={...document,slots:applyComboPlan(database,document.slots,plan)};confirm={combo:combos[selected],document:next,before:activeFormationCombos(database,effective),after:activeFormationCombos(database,next.slots.map(member=>member&&resolveFormationMember(units.get(member.unitId),member)))};selectedEffect=null;popupPhase=0;}finally{locked=false;render();}
 }
 async function action(value,doubled=false){
  if(locked||help||confirm&&popupPhase<5)return;notice='';const [command,id,part]=value.split(':');
  if(command==='combo'){selection=Number(id);if(doubled)await preview(selection);else render();}
  else if(command==='unit'){
   const combo=combos.find(combo=>combo.id===Number(id)),index=Number(part),member=combo.members[index],unit=units.get(member.id);
   selectedUnit={combo:combo.id,index,id:member.id,rarity:plain(manifest.texts['nyancombo_txt'+(unit?.rarity+2)]),name:(unit?.forms.find(form=>form.index===member.form)?.name||manifest.texts.nyancombo_txt9)};render();
  }
  else if(command==='unit-filter'){unitFilter=unitFilter==null?selectedUnit?.id??null:null;page=0;render();}
  else if(command==='filter'){pendingTypes=new Set(types);filter=true;scroll=0;render();}
  else if(command==='type'){const type=Number(id);if(pendingTypes.has(type))pendingTypes.delete(type);else pendingTypes.add(type);render();}
  else if(command==='filter-clear'){pendingTypes.clear();render();}
  else if(command==='filter-close'){filter=false;render();}
  else if(command==='filter-apply'){types=new Set(pendingTypes);fresh=new Set(combos.filter(combo=>!seen.has(combo.id)).map(combo=>combo.id));filter=false;page=0;render();}
  else if(command==='next'||command==='previous'){page+=command==='next'?1:-1;render();}
  else if(command==='cancel'){confirm=null;render();}
  else if(command==='effect'){selectedEffect=combos.find(combo=>combo.id===Number(id));render();}
  else if(command==='confirm'){const current=confirm;locked=true;try{await onApply(current.document.slots);confirm=null;if(!activeFormationCombos(database,effectiveSlots()).some(combo=>combo.id===current.combo.id))notice=plain(manifest.texts.nyancombo_autoset3.replace('%@',current.combo.name));}finally{locked=false;render();}}
  else if(command==='help'){help=true;render();}
  else if(command==='help-close'){help=false;render();}
  else if(command==='back')dialog.close();
 }
 const report=error=>{status.textContent=error.message;};
 canvas.addEventListener('click',event=>{
  if(suppressClick){suppressClick=false;return;}const target=event.target.closest('[data-combo-action]');if(!target)return;
  const value=target.dataset.comboAction,point=canvas.getBoundingClientRect(),x=(event.clientX-point.left)*W/point.width;
  // 008920f8: 同じ行、8F以内、横座標±24。DOMを再描画しても二度押しを失わない。
  const doubled=value.startsWith('combo:')&&lastTap?.value===value&&flash-lastTap.frame<8&&Math.abs(x-lastTap.x)<=24;
  lastTap=doubled?null:{value,frame:flash,x};action(value,doubled).catch(report);
 });
 canvas.addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){const target=event.target.closest('[data-combo-action]');if(target){event.preventDefault();action(target.dataset.comboAction,event.key==='Enter'&&target.dataset.comboAction.startsWith('combo:')).catch(report);}}});
 canvas.addEventListener('wheel',event=>{if(filter&&!help){event.preventDefault();scroll+=event.deltaY*640/canvas.getBoundingClientRect().height;render();}},{passive:false});
 let pointer;
 canvas.addEventListener('pointerdown',event=>{if(help)return;pointer={x:event.clientX,y:event.clientY,id:event.pointerId,scroll,moved:false};});
 canvas.addEventListener('pointermove',event=>{
  if(help||!pointer||pointer.id!==event.pointerId)return;const dx=event.clientX-pointer.x,dy=event.clientY-pointer.y;
  if(Math.hypot(dx,dy)>6)pointer.moved=true;
  if(filter&&pointer.moved){event.preventDefault();scroll=pointer.scroll-dy*640/canvas.getBoundingClientRect().height;render();}
 });
 canvas.addEventListener('pointerup',event=>{
  if(help||!pointer||pointer.id!==event.pointerId)return;const dx=event.clientX-pointer.x,dy=event.clientY-pointer.y;suppressClick=pointer.moved;pointer=null;
  if(Math.abs(dx)>70&&Math.abs(dx)>Math.abs(dy)&&!filter&&!confirm){page=Math.max(0,page+(dx<0?1:-1));render();}
 });
 canvas.addEventListener('pointercancel',()=>{pointer=null;});
 search.addEventListener('input',()=>{query=search.value;page=0;render();});
 dialog.addEventListener('cancel',event=>{if(confirm||filter||help){event.preventDefault();confirm=null;filter=false;help=false;render();}});
 dialog.addEventListener('close',()=>clearInterval(interval));
 const button=document.createElement('button');button.className='formation-combo-book';button.type='button';button.setAttribute('aria-label','にゃんコンボ図鑑');button.innerHTML='<svg viewBox="0 580 1188 64">'+sprite('img029_ja',30,W-586,590,279,52)+'</svg>';
 button.addEventListener('click',()=>{fresh=new Set(combos.filter(combo=>!seen.has(combo.id)).map(combo=>combo.id));render();dialog.showModal();clearInterval(interval);interval=setInterval(()=>{++flash;for(const arrow of canvas.querySelectorAll('[data-combo-arrow]'))arrow.querySelector('svg')?.setAttribute('x',Math.trunc(24+Math.sin(flash*Math.PI/6)*10));if(confirm&&popupPhase<5){++popupPhase;render();}canvas.querySelector('[data-combo-pattern]')?.setAttribute('opacity',patternOpacity());const color=flash%4<2?[244,15,255]:[255,241,15];for(const highlight of canvas.querySelectorAll('[data-combo-highlight]'))highlight.setAttribute('display',Number(highlight.dataset.comboHighlight)===Math.floor(flash/2)%2?'inline':'none');for(const text of canvas.querySelectorAll('[data-combo-text-flash]'))text.setAttribute('fill','rgb('+color.join(',')+')');for(const [i,key]of ['r','g','b'].entries())canvas.querySelector('[data-flash-'+key+']')?.setAttribute('slope',color[i]/255);},1000/30);});
 return button;
}
