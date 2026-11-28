// 計測は1秒ごと。数値は表示/提出時間で、GPU実行時間と混同しない。
export function createBattleMonitor(root,read){
 const fields=new Map([...root.querySelectorAll('[data-stat]')].map(node=>[node.dataset.stat,node]));
 let at=performance.now(),lastFrame=0,lastPaints=0,lastPaint,polling=false,resource=null,latest;
 const controller=new AbortController(),number=(value,digits=1)=>Number.isFinite(value)?value.toFixed(digits):'—';
 const show=(key,value,title)=>{const node=fields.get(key);if(node){node.textContent=value;if(title)node.title=title;}};
 async function tick(){
  const now=performance.now(),value=read(),seconds=(now-at)/1000;
  const count=value.paints-lastPaints,intervals=count-(lastPaint==null?1:0),span=value.lastPaint-(lastPaint??value.firstPaint);
  latest={...value,fps:intervals>0&&span>0?intervals*1000/Math.max(span,now-value.lastPaint):null,progress:(value.frame-lastFrame)/30/seconds,resources:resource};
  show('fps',number(latest.fps)+' FPS / 上限 '+value.fpsLimit);show('progress','進行 '+number(latest.progress,2)+'×');
  latest.averageFps=value.activeMs>0?value.activePaints*1000/value.activeMs:null;
  show('average-fps','平均 '+number(latest.averageFps)+' FPS','連続した戦闘描画の間隔の平均。非表示と一時停止の時間を除きます');
  show('core','更新計算 '+number(value.coreMs)+'ms');show('scene','戦闘API '+number(value.apiMs)+'ms / p95 '+number(value.apiP95Ms)+'ms','直近'+value.apiSamples+'要求 / 最大 '+number(value.apiMaxMs)+'ms\nサーバー '+number(value.serverMs)+'ms（背景 '+number(value.computeMs)+' / 変換 '+number(value.encodeMs)+'）\n受渡・待機 '+number(value.transferMs)+'ms / 復元 '+number(value.decodeMs)+'ms / '+number(value.payloadBytes/1024,0)+'KB');
  show('draw','WebGL '+number(value.drawMs)+'ms / HUD '+number(value.hudMs)+'ms','CPUからの描画提出時間。GPU実行時間は含めません');
  const usbTiming=Number.isFinite(value.headersMs)?'ヘッダー受信まで '+number(value.headersMs)+'ms / 本文受信・展開 '+number(value.bodyMs)+'ms\nUSB応答のgzip判定・圧縮 '+number(value.gzipMs)+'ms（ヘッダー受信までに含む）':undefined;
  show('transfer','転送 '+number(value.payloadBytes/1024,0)+'KB / 復元 '+number(value.decodeMs)+'ms',usbTiming);
  show('lag','未処理 '+Math.ceil(value.lag)+'F / 描画待ち '+number(value.displayWaitMs)+'ms','フレーム受信後の待ち。FPS上限による待ち時間も含みます');
  const images=value.images;
  show('images','画像 '+number(images.bytes/1048576,0)+'MB / 読込 '+images.pending,'展開後の推定値。開始前にGPUへ転送 '+number(value.warmTextureBytes/1048576,0)+'MB');
  at=now;lastFrame=value.frame;lastPaints=value.paints;lastPaint=value.lastPaint;
  if(polling)return;polling=true;
  try{const response=await fetch('/api/runtime',{signal:controller.signal});if(!response.ok)throw Error('計測できません');resource=await response.json();
   show('cpu','CPU '+number(resource.cpuPercent,0)+'%','PC全体。Rust本体のRAM '+number(resource.hostWorkingSet/1048576,0)+'MB（WebView/GPUは別プロセス）');
   show('memory',resource.memoryTotal?'RAM '+number((resource.memoryTotal-resource.memoryAvailable)/1073741824)+' / '+number(resource.memoryTotal/1073741824)+'GB':'RAM —','PC全体の物理メモリ');
   show('host-memory','KBCS RAM '+number(resource.hostWorkingSet==null?NaN:resource.hostWorkingSet/1048576,0)+'MB','KBCS本体のみ。WebViewやGPUのプロセスは含みません');
   const pools=Object.values(resource.workers);show('queue','要求 '+pools.reduce((n,p)=>n+p.active,0)+' / 待機 '+pools.reduce((n,p)=>n+p.queued,0),JSON.stringify(resource.caches));
  }catch(error){if(error.name!=='AbortError'){show('cpu','CPU —');show('memory','RAM —');show('host-memory','KBCS RAM —');}}finally{polling=false;}
 }
 const timer=setInterval(tick,1000);
 return {stop:()=>{clearInterval(timer);controller.abort();},snapshot:()=>latest||read()};
}
