import {formationLayout,insertMember,stepFloating} from './formation-layout.js';

// PCのペイン境界で切れない浮遊画像。切抜き・金額は通常枠と同じviewを使う。
export function createFormationGhost(paint,document,member,cost){
 const ghost=window.document.createElement('div');ghost.className='formation-drag-preview';ghost.setAttribute('aria-hidden','true');
 ghost.innerHTML=paint({...document,slots:[member,...Array(9).fill(null)]},{ghost:true,deployment:cost?{slots:[cost]}:null});
 window.document.body.append(ghost);return ghost;
}

// 00a7888c/00a82394の5tick長押し、隣接送り、拡大/透明度/整数減衰を編集と準備で共用する。
export function createFormationReorder(screen,{getDocument,getDeployment,paint,canStart=()=>true,onSelect=()=>{},onDraw,onCommit,onDrop=()=>false,allowRemove=true}){
 const layout=formationLayout(),shifts=layout.slots.map(()=>({x:0,y:0}));
 let dragged=null,floating=null,ghost=null,suppressClick=false;
 function point(event){
  const rect=screen.querySelector('svg').getBoundingClientRect();
  return {x:Math.trunc((event.clientX-rect.left)*layout.width/rect.width),y:Math.trunc((event.clientY-rect.top)*layout.height/rect.height)};
 }
 function clear(){floating=null;ghost?.remove();ghost=null;}
 function resetShifts(){for(const shift of shifts){shift.x=0;shift.y=0;}}
 function finish(cancel=false,event=null){
  if(!dragged)return;
  const captured=dragged;dragged=null;
  if(floating?.held){
   const base=layout.slots[floating.slot];floating.x=captured.pointer.x-captured.grab.x-base.x;floating.y=captured.pointer.y-captured.grab.y-base.y;floating.held=false;
   suppressClick=true;setTimeout(()=>{suppressClick=false;},0);
   if(cancel){getDocument().slots=captured.snapshot;clear();resetShifts();onSelect(captured.slot);}
   else{
    const handled=onDrop(event,floating.slot);
    if(handled)clear();
    else floating.remove=allowRemove&&(captured.pointer.y<80||captured.pointer.y>280);
    if(!floating?.remove&&(handled||captured.snapshot.some((member,i)=>member!==getDocument().slots[i])))onCommit(captured.snapshot);
   }
   onDraw();
  }
  if(screen.hasPointerCapture(captured.pointerId))screen.releasePointerCapture(captured.pointerId);
 }
 function renderFloating(){
  if(!floating){ghost?.remove();ghost=null;return;}
  if(!ghost)ghost=createFormationGhost(paint,getDocument(),getDocument().slots[floating.slot],floating.cost);
  const rect=screen.querySelector('svg').getBoundingClientRect(),scale=rect.width/layout.width,base=layout.slots[floating.slot];
  const width=110+Math.trunc(floating.growth*110/100),height=85+Math.trunc(floating.growth*85/100);
  Object.assign(ghost.style,{left:(rect.left+(base.x+floating.x-Math.trunc(floating.growth*110/200))*scale)+'px',top:(rect.top+(base.y+floating.y-Math.trunc(floating.growth*85/200))*scale)+'px',width:width*scale+'px',height:height*scale+'px',opacity:(255-floating.alpha)/255});
 }
 function tick(){
  if(!getDocument())return;let dirty=false;
  for(const shift of shifts)if(shift.x||shift.y){shift.x=Math.trunc(shift.x/2);shift.y=Math.trunc(shift.y/2);dirty=true;}
  if(dragged){
   if(!floating){const base=layout.slots[dragged.slot],p=dragged.pointer;if(p.x<base.x||p.x>=base.x+114||p.y<base.y-2||p.y>=base.y+86){finish(true);return;}}
   if(++dragged.ticks>=5&&!floating){floating={slot:dragged.slot,held:true,growth:0,alpha:0,x:0,y:0,cost:dragged.cost};onSelect(dragged.slot);}
   if(floating?.held){
    const slots=getDocument().slots,p=dragged.pointer,target=layout.slots.findIndex((slot,i)=>slots[i]&&p.x>=slot.x&&p.x<slot.x+114&&p.y>=slot.y-2&&p.y<slot.y+86);
    if(target>=0&&target!==floating.slot){
     const from=floating.slot,direction=target>from?1:-1;
     for(let i=from;i!==target;i+=direction){const next=i+direction;shifts[i].x=layout.slots[next].x+shifts[next].x-layout.slots[i].x;shifts[i].y=layout.slots[next].y+shifts[next].y-layout.slots[i].y;}
     shifts[target].x=0;shifts[target].y=0;insertMember(slots,from,target);floating.slot=target;onSelect(target,false);
    }
    const base=layout.slots[floating.slot];floating.x=p.x-dragged.grab.x-base.x;floating.y=p.y-dragged.grab.y-base.y;
   }
  }
  if(floating){
   if(floating.remove){floating.growth=Math.max(-100,floating.growth-20);if(floating.growth===-100){getDocument().slots[floating.slot]=null;clear();onCommit();}}
   else stepFloating(floating);
   if(floating&&!floating.held&&!floating.remove&&floating.x===0&&floating.y===0)clear();
   dirty=true;
  }
  if(dirty)onDraw();
 }
 screen.addEventListener('pointerdown',event=>{
  const target=event.target.closest('[data-slot]');if(!target||event.button!==0||dragged||floating||!canStart())return;
  const slot=Number(target.dataset.slot),doc=getDocument();if(!doc?.slots[slot])return;
  const pointer=point(event),base=layout.slots[slot];
  dragged={slot,pointer,grab:{x:pointer.x-base.x,y:pointer.y-base.y},ticks:0,pointerId:event.pointerId,snapshot:doc.slots.slice(),cost:getDeployment()?.slots[slot]};
  screen.setPointerCapture(event.pointerId);onSelect(slot);onDraw();
 });
 screen.addEventListener('pointermove',event=>{if(dragged?.pointerId===event.pointerId)dragged.pointer=point(event);});
 screen.addEventListener('pointerup',event=>{if(dragged?.pointerId===event.pointerId){dragged.pointer=point(event);finish(false,event);}});
 screen.addEventListener('pointercancel',()=>finish(true));screen.addEventListener('lostpointercapture',()=>finish(true));
 function cancel(){if(!dragged&&!floating&&!shifts.some(value=>value.x||value.y))return;finish(true);clear();resetShifts();onDraw();}
 window.addEventListener('blur',cancel);window.addEventListener('pagehide',cancel);
 setInterval(tick,1000/30);
 return {get active(){return !!(dragged||floating);},get suppressClick(){return suppressClick;},get view(){return {shifts,hiddenSlot:floating?.slot??-1};},renderFloating,cancel};
}
