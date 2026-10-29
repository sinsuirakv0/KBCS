// HTTP Rangeに依存しないBlob音源。試聴と戦闘開始で同じ読み込みを使う。
export async function audioBlobUrl(source,signal){
 const response=await fetch(source,{signal});
 if(!response.ok)throw Error('BGMを読み込めません（'+response.status+'）');
 const blob=await response.blob();signal?.throwIfAborted();return URL.createObjectURL(blob);
}
export function createAudioPreview(audio,button,seek,time,stopOthers){
 const controller=new AbortController(),source=audio.dataset.source;
 let pending,url,intent=false,generation=0,disposed=false,scrubbing=false;
 const format=value=>Number.isFinite(value)?Math.floor(value/60)+':'+String(Math.floor(value%60)).padStart(2,'0'):'—';
 function progress(){
  if(!scrubbing)seek.value=Number.isFinite(audio.duration)&&audio.duration>0?audio.currentTime/audio.duration*100:0;
  time.textContent=format(audio.currentTime)+' / '+format(audio.duration);
 }
 function pause(){intent=false;++generation;audio.pause();button.textContent='▶';}
 async function load(){
  if(!pending)pending=audioBlobUrl(source,controller.signal).then(value=>{
   if(disposed){URL.revokeObjectURL(value);throw new DOMException('停止済み','AbortError');}
   url=value;audio.src=url;audio.load();
  }).catch(error=>{pending=null;throw error;});
  return pending;
 }
 async function toggle(){
  if(intent||!audio.paused){pause();return;}
  stopOthers();intent=true;const turn=++generation;button.textContent='…';
  try{await load();if(disposed||turn!==generation)return;await audio.play();}
  catch(error){if(disposed||turn!==generation)return;intent=false;button.textContent='!';button.title=error.message;}
 }
 function seekToValue(){
  if(!Number.isFinite(audio.duration)||audio.duration<=0)return;
  audio.currentTime=Math.max(0,Math.min(100,Number(seek.value)))/100*audio.duration;
 }
 const begin=()=>{scrubbing=true;};
 const input=()=>{scrubbing=true;seekToValue();};
 const commit=()=>{seekToValue();scrubbing=false;progress();};
 seek.addEventListener('pointerdown',begin);seek.addEventListener('input',input);seek.addEventListener('change',commit);
 seek.addEventListener('pointerup',commit);seek.addEventListener('pointercancel',commit);seek.addEventListener('blur',commit);
 audio.onplay=()=>button.textContent='Ⅱ';audio.onpause=()=>button.textContent='▶';audio.onended=()=>{intent=false;button.textContent='▶';};
 audio.onloadedmetadata=()=>{seek.disabled=!Number.isFinite(audio.duration)||audio.duration<=0;progress();};audio.ontimeupdate=progress;
 audio.onerror=()=>{intent=false;button.textContent='!';button.title='音源を再生できませんでした';};
 return {toggle,pause,dispose(){
  disposed=true;pause();controller.abort();audio.removeAttribute('src');if(url)URL.revokeObjectURL(url);
  for(const [type,fn]of [['pointerdown',begin],['input',input],['change',commit],['pointerup',commit],['pointercancel',commit],['blur',commit]])seek.removeEventListener(type,fn);
  audio.onplay=audio.onpause=audio.onended=audio.onloadedmetadata=audio.ontimeupdate=audio.onerror=null;
 }};
}
