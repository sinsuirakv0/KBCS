// 原本の姿勢評価は共通C++へ渡す。ここではGPU用のUVだけを対応付ける。
export async function nativePackets(project,clip,frame,facing=1){
  frame=Math.max(0,Math.floor(frame));
  const first=Math.floor(frame/16)*16,key=clip+':'+facing+':'+first;
  const cache=project.nativePoses??=new Map();
  if(!cache.has(key)){
    if(cache.size>=Math.max(1,Math.min(8,Math.floor(8192/Math.max(1,project.model.parts.length*16)))))cache.delete(cache.keys().next().value);
    const frames=Array.from({length:Math.min(16,1000001-first)},(_,i)=>first+i);
    cache.set(key,fetch('/api/motion-pose',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({...project.nativeRequest,resource:project.key,clip,frames,facing})}).then(async response=>{const value=await response.json();if(!response.ok)throw Error(value.error||'姿勢を読み込めませんでした。');return value.frames;}).catch(error=>{cache.delete(key);throw error;}));
  }
  const values=await cache.get(key),width=project.image.naturalWidth,height=project.image.naturalHeight;
  return values[frame].map(packet=>{
    const cut=project.imgcut.cuts[packet.cut];
    return {partIndex:packet.part,blendMode:packet.blend,opacity:packet.opacity,positions:packet.points,uvs:[cut.x/width,cut.y/height,cut.x/width,(cut.y+cut.height)/height,(cut.x+cut.width)/width,(cut.y+cut.height)/height,(cut.x+cut.width)/width,cut.y/height]};
  });
}
