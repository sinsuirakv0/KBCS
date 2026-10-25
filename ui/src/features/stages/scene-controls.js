// 画面上の操作点の世界座標を保ち、パンと拡大を同時に扱う。
export function sceneGestureView(view,previous,current,rectangle){
  const zoom=Math.max(view.minimum,Math.min(view.maximum??2,view.zoom*(previous.distance&&current.distance?current.distance/previous.distance:1)));
  const offset=point=>(point-rectangle.left-rectangle.width/2)*(view.viewport_width||960)/rectangle.width;
  return {zoom,center:view.center+offset(previous.x)/view.zoom-offset(current.x)/zoom};
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
    applyView(sceneGestureView(view,{x:event.clientX,distance:1},{x:event.clientX,distance:Math.exp(-delta*.0015)},canvas.getBoundingClientRect()));
  }
  canvas.addEventListener('pointerdown',start);
  canvas.addEventListener('pointermove',move);
  canvas.addEventListener('wheel',wheel,{passive:false});
  const reset=()=>{pointers.clear();previous=null;};
  reset.dispose=()=>{reset();canvas.removeEventListener('pointerdown',start);canvas.removeEventListener('pointermove',move);canvas.removeEventListener('wheel',wheel);for(const name of ['pointerup','pointercancel','lostpointercapture'])canvas.removeEventListener(name,end);};
  return reset;
}
