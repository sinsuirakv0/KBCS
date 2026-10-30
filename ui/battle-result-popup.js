import {readBattleJson} from './battle-support.js';

// 005e53dcの原本文面を、00884eccと同じ文字runへ分ける。HTMLとして実行しない。
function lines(markup){
 const rows=[[]];let color='rgb(255,255,255)',flash=false;
 for(const token of markup.split(/(<br>|<color=\d+,\d+,\d+>|<\/color>|<flash>|<\/flash>)/g)){
  if(token==='<br>')rows.push([]);
  else if(token.startsWith('<color='))color='rgb('+token.slice(7,-1)+')';
  else if(token==='</color>')color='rgb(255,255,255)';
  else if(token==='<flash>')flash=true;
  else if(token==='</flash>')flash=false;
  else if(token)rows.at(-1).push({text:token,color,flash});
 }
 return rows;
}
export function createResultPopup(reportError){
 const measure=document.createElement('canvas').getContext('2d');measure.font='30px sans-serif';
 function texture(run,flashColor){
  const metrics=measure.measureText(run.text),w=Math.ceil(metrics.width),ascent=Math.ceil(metrics.fontBoundingBoxAscent),h=Math.ceil(metrics.fontBoundingBoxAscent+metrics.fontBoundingBoxDescent);
  const canvas=document.createElement('canvas');canvas.width=Math.max(1,w);canvas.height=Math.max(1,h);const ink=canvas.getContext('2d');ink.font=measure.font;ink.textBaseline='alphabetic';ink.fillStyle=run.flash?flashColor:run.color;ink.fillText(run.text,0,ascent);return {canvas,w,h};
 }
 let key='',prepared,closed=false;
 return {
  prepare(messages,width,atlas){
   const next=JSON.stringify([messages,width]);if(next===key)return;key=next;prepared=null;
   const entries=messages.map(message=>{
    const rows=lines(message),textures=['rgb(255,255,0)','rgb(255,0,255)'].map(color=>rows.map(row=>row.map(run=>texture(run,color)))),widths=textures[0].map(row=>row.reduce((sum,run)=>sum+run.w,0));
    return {rows,widths,textures};
   });
   // 通知ごとの要求を並列に増やさず、Serviceの64件/16KiB以内でまとめる。
   const cut=atlas.atlases.img005_1.rects,input=entries.flatMap(entry=>Array.from({length:5},(_,scaleFrame)=>({viewport:width,count:entry.rows.length,widths:Array.from({length:8},(_,i)=>entry.widths[i]||0),scaleFrame,cut:cut[0],padding:cut[8].slice(0,2)})));
   return (async()=>{
    const layouts=[];
    for(let offset=0;offset<input.length;offset+=50)layouts.push(...await readBattleJson('/api/battle-popup',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(input.slice(offset,offset+50))}));
    return entries.map((entry,index)=>({...entry,layouts:layouts.slice(index*5,index*5+5)}));
   })().then(value=>{if(!closed&&key===next)prepared=value;}).catch(error=>{if(!closed&&key===next)reportError(error.message);});
  },
  paint(context,popup,width,atlas,images){
   const entry=prepared?.[popup.index];if(!entry)return;
   const layout=entry.layouts[popup.scaleFrame],image=images.get(atlas.atlases.img005_1.image);
   if(popup.scaleFrame)for(const part of layout.parts){
    const [x,y,w,h,sx,sy,sw,sh]=part;
    // 原本の幅0のUVは同じ画素を面へ伸ばす。Canvasの空描画とは区別する。
    if(w&&h)context.drawImage(image,sx,sy,Math.max(1,sw),Math.max(1,sh),x,y,w,h);
   }
   if(popup.phase!==1&&popup.phase!==2)return;
   context.save();context.font='30px sans-serif';context.textBaseline='top';
   for(let index=0;index<entry.rows.length;++index){
    const scale=layout.textScale[index],textures=entry.textures[popup.flash%4<2?0:1][index];let offset=0;
    for(const texture of textures){context.drawImage(texture.canvas,Math.trunc(layout.textX[index]+offset*scale),layout.textY+index*36-Math.trunc(texture.h/2),Math.trunc(texture.w*scale),texture.h);offset+=texture.w;}
   }
   context.restore();
  },
  stop(){closed=true;prepared=null;},
 };
}
