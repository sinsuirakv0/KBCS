// SEの選択・終了後の抑止はC++で確定する。音源の取得で戦闘時計を止めない。
export function createBattleSounds(errors,settings=[]){
 const context=new AudioContext(),gain=context.createGain(),buffers=new Map(),voices=new Map(),controller=new AbortController();
 gain.connect(context.destination);let closed=false,sequence=Promise.resolve(),generation=0,finished=false,muted=false,paused=false;
 async function buffer(id){
  if(!buffers.has(id))buffers.set(id,(async()=>{
   const response=await fetch('/api/stage-audio/'+id,{signal:controller.signal});
   if(!response.ok){const result=await response.json();throw Error(result.error||'SE '+id);}
   const data=await context.decodeAudioData(await response.arrayBuffer());errors.delete('SE '+id);return data;
  })().catch(error=>{if(error.name!=='AbortError'&&!closed)errors.set('SE '+id,error.message);return null;}));
  return buffers.get(id);
 }
 return {
  preload(ids){let next=0;return Promise.all(Array.from({length:Math.min(4,ids.length)},async()=>{while(!closed&&next<ids.length)await buffer(ids[next++]);}));},
  update(events,level,speed=1,hostPaused=false,ended=false){
   if(closed)return;
   gain.gain.value=[0,.25,.5,1][level];
   // 未デコードの古い通知が、終了音やミュート解除の後へ遅れて混入するのを防ぐ。
   // 00459bb4(-1)はBGMだけを停止するため、既に鳴っているSEは終了時に切らない。
   if((ended&&!finished)||(!level&&!muted)||(hostPaused&&!paused)){++generation;sequence=Promise.resolve();}
   finished=ended;muted=!level;paused=hostPaused;
   if(paused||muted||!events.length)return;
   context.resume().catch(()=>{});
   const token=generation,origin=context.currentTime,first=events[0].frame;
   // 取得は並行、発音は通知順。同じ音源の再生は00459170と同じく一つのプレイヤーへ戻す。
   const pending=Promise.all(events.map(event=>buffer(event.id)));
   sequence=sequence.then(async()=>{
    const decoded=await pending;if(closed||token!==generation)return;
    for(let i=0;i<events.length;++i){
     const event=events[i],data=decoded[i];if(!data)continue;
     const when=Math.max(context.currentTime,origin+(event.frame-first)/(30*speed));
     const previous=voices.get(event.id);if(previous)previous.stop(when);
     const source=context.createBufferSource();source.buffer=data;source.loop=!!settings[event.id]?.loop;
     source.connect(gain);voices.set(event.id,source);
     source.onended=()=>{if(voices.get(event.id)===source)voices.delete(event.id);source.disconnect();};
     source.start(when);
    }
   }).catch(error=>{if(!closed)errors.set('SE',error.message);});
  },
  stop(){if(closed)return;closed=true;++generation;controller.abort();for(const source of voices.values())source.stop();voices.clear();buffers.clear();context.close().catch(()=>{});},
 };
}
