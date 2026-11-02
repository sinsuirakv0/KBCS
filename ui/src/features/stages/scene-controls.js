// 画面上の操作点の世界座標を保ち、パンと拡大を同時に扱う。
export function sceneGestureView(view,previous,current,rectangle){
  const zoom=Math.max(view.minimum,Math.min(view.maximum??2,view.zoom*(previous.distance&&current.distance?current.distance/previous.distance:1)));
  const offset=point=>(point-rectangle.left-rectangle.width/2)*(view.viewport_width||960)/rectangle.width;
  return {zoom,center:view.center+offset(previous.x)/view.zoom-offset(current.x)/zoom};
}
// PCキーも既存カメラの倍率・中心と同じ制限で解決する。戦闘時計は進めない。
export function sceneKeyboardView(view,action){
 const width=view.viewport_width||960;
 if(action==='cameraLeft'||action==='cameraRight')return {zoom:view.zoom,center:view.center+(action==='cameraLeft'?-1:1)*width/(10*view.zoom)};
 const ratio=Math.exp(action==='cameraIn'?.15:-.15);
 return sceneGestureView(view,{x:width/2,distance:1},{x:width/2,distance:ratio},{left:0,width});
}
// PCの連続操作。OSのキーリピートやRPCの応答間隔を移動量へ使わない。
export function createSceneMotion(){
 const held=new Set();let wheel=null;
 const clamp=(value,lo,hi)=>Math.max(lo,Math.min(hi,value));
 return {
  key(action,down){if(down)held.add(action);else held.delete(action);},
  zoom(view,target,x,rectangle){wheel={zoom:clamp((wheel?.zoom??view.zoom)*target.zoom/view.zoom,view.minimum,view.maximum??2),x,rectangle,remaining:.12};},
  clear(){held.clear();wheel=null;},
  step(view,seconds){
   if(!view||seconds<=0)return null;
   const dt=Math.min(seconds,.1),width=view.viewport_width||960;
   let next={zoom:view.zoom,center:view.center};
   const direction=Number(held.has('cameraRight'))-Number(held.has('cameraLeft'));
   const zooming=Number(held.has('cameraIn'))-Number(held.has('cameraOut'));
   if(direction)next.center+=direction*width*.6*dt/view.zoom;
   if(zooming){next.zoom=clamp(view.zoom+zooming*.6*dt,view.minimum,view.maximum??2);wheel=null;}
   else if(wheel){const used=Math.min(dt,wheel.remaining),zoom=view.zoom+(wheel.zoom-view.zoom)*used/wheel.remaining;next=sceneGestureView({...view,...next},{x:wheel.x,distance:view.zoom},{x:wheel.x,distance:zoom},wheel.rectangle);wheel.remaining-=used;if(wheel.remaining<=1e-6)wheel=null;}
   if(view.width){const half=width*.5/next.zoom;next.center=view.width<=half*2?view.width/2:clamp(next.center,half,view.width-half);}
   return next.zoom===view.zoom&&next.center===view.center?null:next;
  },
 };
}
export function initializeSceneGestures(canvas,readView,applyView,options={}){
  const pointers=new Map();let previous;
  function measure(){const values=[...pointers.values()];if(!values.length)return null;return values.length===1?{x:values[0].x,distance:0}:{x:(values[0].x+values[1].x)/2,distance:Math.hypot(values[0].x-values[1].x,values[0].y-values[1].y)};}
  function start(event){
    if(event.button!==0||!readView()||options.acceptPointer&&!options.acceptPointer(event))return;
    event.preventDefault();pointers.set(event.pointerId,{x:event.clientX,y:event.clientY});previous=measure();canvas.setPointerCapture(event.pointerId);
  }
  function move(event){
    if(!pointers.has(event.pointerId))return;
    pointers.set(event.pointerId,{x:event.clientX,y:event.clientY});const current=measure(),view=readView();
    if(previous&&view)applyView(sceneGestureView(view,previous,current,canvas.getBoundingClientRect()));previous=current;
  }
  const end=event=>{pointers.delete(event.pointerId);previous=measure();};
  for(const name of ['pointerup','pointercancel','lostpointercapture'])canvas.addEventListener(name,end);
  function wheel(event){
    const view=readView();if(!view||options.acceptWheel&&!options.acceptWheel(event))return;event.preventDefault();
    const delta=event.deltaY*(event.deltaMode===1?16:event.deltaMode===2?canvas.clientHeight:1);
    const rectangle=canvas.getBoundingClientRect(),target=sceneGestureView(view,{x:event.clientX,distance:1},{x:event.clientX,distance:Math.exp(-delta*.0015)},rectangle);
    if(options.wheelTarget)options.wheelTarget(view,target,event.clientX,rectangle);else applyView(target);
  }
  canvas.addEventListener('pointerdown',start);
  canvas.addEventListener('pointermove',move);
  canvas.addEventListener('wheel',wheel,{passive:false});
  const reset=()=>{pointers.clear();previous=null;};
  reset.dispose=()=>{reset();canvas.removeEventListener('pointerdown',start);canvas.removeEventListener('pointermove',move);canvas.removeEventListener('wheel',wheel);for(const name of ['pointerup','pointercancel','lostpointercapture'])canvas.removeEventListener(name,end);};
  return reset;
}
