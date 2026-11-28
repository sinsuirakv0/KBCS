import {battleFrameSamples,decodeBattleFrame} from './battle-frame.js';
import {readBattleJson} from './battle-support.js';

const post=(body,signal)=>({method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body),signal});

export function createPhoneRuntime(session, signal) {
 const worker=new Worker('/phone-runtime-worker.js',{type:'module'});
 const requests=new Map(),samples=battleFrameSamples();
 let requestId=0,inFlight=false,stopped=false,queryDirty=false,lastSent=-Infinity,query,settlementMs=0,retryRewardAt=0;
 function stop(error=new DOMException('戦闘を終了しました','AbortError')){
  if(stopped)return;stopped=true;worker.terminate();
  for(const {reject} of requests.values())reject(error);
  requests.clear();
 }
 signal.addEventListener('abort',()=>stop(),{once:true});
 worker.onmessage=({data:{id,value,error}})=>{
  const request=requests.get(id);if(!request)return;
  requests.delete(id);
  if(error)request.reject(Error(error));else request.resolve(value);
 };
 worker.onerror=event=>stop(Error(event.message||'スマホの戦闘を起動できません'));
 const call=(operation,payload,transfer=[])=>new Promise((resolve,reject)=>{
  if(stopped){reject(new DOMException('戦闘を終了しました','AbortError'));return;}
  const id=++requestId;requests.set(id,{resolve,reject});worker.postMessage({id,operation,payload},transfer);
 });
 const path=name=>'/api/phone/'+name+'?'+new URLSearchParams({session});
 async function settle(request){
  const started=performance.now();
  for(let attempt=0;attempt<3;++attempt){
   try{
    const deadline=AbortSignal.any([signal,AbortSignal.timeout(3000)]);
    const result=await readBattleJson(path('settle'),post(request,deadline));
    await call(3,result);
    settlementMs=performance.now()-started;
    if(request.kind==='reward'&&!result.receipt)retryRewardAt=performance.now()+2000;
    return;
   }catch(error){if(signal.aborted||attempt===2)throw error;}
  }
 }
 return {
  start(buffer){return call(0,buffer,[buffer]);},
  input(payload){return call(2,payload);},
  popupLayouts(payload){return call(4,payload);},
  observe(value){query={inspection:value?.inspection??query?.inspection,focusActor:value?.focusActor??null};queryDirty=true;},
  async load(request){
   const now=performance.now(),sample=!inFlight&&(queryDirty||now-lastSent>=200);
   const observation=sample?query:undefined;const started=performance.now();
   const buffer=await call(1,{request,observation}),received=performance.now(),value=decodeBattleFrame(buffer);
   const decoded=performance.now(),apiMs=decoded-started;
   samples.record(apiMs);
   const settlement=value.runtime.settlement;
   if(settlement&&(settlement.kind!=='reward'||decoded>=retryRewardAt))await settle(settlement);
   return {value,sample,observation,timing:{localWasm:true,apiMs,serverMs:value.serverMs,encodeMs:value.encodeMs,decodeMs:decoded-received,
    computeMs:value.scene?.computeMs,workerWaitMs:Math.max(0,received-started-value.serverMs),settlementMs}};
  },
  publish({value,sample,observation},stats) {
   if(!sample||inFlight||stopped)return;
   lastSent=performance.now();
   if(query===observation&&query){query={focusActor:query.focusActor};queryDirty=false;}
   const {state,runtime,scene,coreMs}=value;
   const pose=runtime.focusedDrawRange?scene.commands.slice(...runtime.focusedDrawRange).map(({points,cut,colors,...command})=>({
    ...command,points:Array.from(points),cut:Array.from(cut),colors:Array.from(colors),
   })):null;
   const {units,enemies,rules,result,points,extras,deployment,inspection,focusedActor,receipt,receiptError,continueNotice,continuePrompt,ex}=runtime;
   const {scoreType,nativeKind,timeLimit,totalLimit,rarityLimits}=rules;
   const data={state:{frame:state.frame,paused:state.paused,rows:state.rows,intro:state.intro,money:state.money},
    runtime:{units,enemies,rules:{scoreType,nativeKind,timeLimit,totalLimit,rarityLimits},result,
     points:{wait:points.wait},extras,deployment:{active:deployment.active,total:deployment.total},
     inspection,focusedActor,receipt,receiptError,continueNotice,continuePrompt,ex,hud:{health:runtime.hud.health}},
    pose,coreMs,sceneMs:scene.computeMs,phoneStats:stats};
   // 監視の応答を待つ描画は作らず、遅い接続には次の最新状態を送る。
   inFlight=true;
   const deadline=AbortSignal.any([signal,AbortSignal.timeout(1500)]);
   void readBattleJson(path('sample'),post(data,deadline)).catch(()=>{
    if(observation?.inspection&&!query?.inspection){query={...query,inspection:observation.inspection};queryDirty=true;}
   }).finally(()=>{inFlight=false;});
  },
  stats:samples.stats,
  stop,
 };
}
