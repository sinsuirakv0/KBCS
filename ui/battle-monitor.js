// 計測は1秒ごと。数値は表示/提出時間で、GPU実行時間と混同しない。
export function createBattleMonitor(root,read){
 const fields=new Map([...root.querySelectorAll('[data-stat]')].map(node=>[node.dataset.stat,node]));
 let at=performance.now(),lastFrame=0,lastPaints=0,polling=false,resource=null,latest;
 const controller=new AbortController(),number=(value,digits=1)=>Number.isFinite(value)?value.toFixed(digits):'—';
 const show=(key,value,title)=>{const node=fields.get(key);if(node){node.textContent=value;if(title)node.title=title;}};
 async function tick(){
  const now=performance.now(),value=read(),seconds=(now-at)/1000;
  latest={...value,fps:(value.paints-lastPaints)/seconds,progress:(value.frame-lastFrame)/30/seconds,resources:resource};
  show('fps',number(latest.fps)+' FPS');show('progress','進行 '+number(latest.progress,2)+'×');
  show('core','更新計算 '+number(value.coreMs)+'ms');show('scene','戦闘API '+number(value.apiMs)+'ms / p95 '+number(value.apiP95Ms)+'ms','直近'+value.apiSamples+'要求 / 最大 '+number(value.apiMaxMs)+'ms\nサーバー '+number(value.serverMs)+'ms（背景 '+number(value.computeMs)+' / 変換 '+number(value.encodeMs)+'）\n受渡・待機 '+number(value.transferMs)+'ms / 復元 '+number(value.decodeMs)+'ms / '+number(value.payloadBytes/1024,0)+'KB');
  show('draw','描画提出 '+number(value.drawMs)+'ms','CPUからWebGLへ送る時間。GPU実行時間は含めません');
  show('lag','待ち '+Math.ceil(value.lag)+'F');
  const images=value.images,total=images.hits+images.misses;
  show('images','画像 '+number(images.bytes/1048576,0)+'MB / 読込 '+images.pending+' / hit '+(total?Math.round(images.hits/total*100):0)+'%','画像メモリは展開後の寸法からの目安です');
  at=now;lastFrame=value.frame;lastPaints=value.paints;
  if(polling)return;polling=true;
  try{const response=await fetch('/api/runtime',{signal:controller.signal});if(!response.ok)throw Error('計測できません');resource=await response.json();
   show('cpu','CPU '+number(resource.cpuPercent,0)+'%','PC全体。Rust本体のRAM '+number(resource.hostWorkingSet/1048576,0)+'MB（WebView/GPUは別プロセス）');
   show('memory',resource.memoryTotal?'RAM '+number((resource.memoryTotal-resource.memoryAvailable)/1073741824)+' / '+number(resource.memoryTotal/1073741824)+'GB':'RAM —','PC全体の物理メモリ');
   const pools=Object.values(resource.workers);show('queue','要求 '+pools.reduce((n,p)=>n+p.active,0)+' / 待機 '+pools.reduce((n,p)=>n+p.queued,0),JSON.stringify(resource.caches));
  }catch(error){if(error.name!=='AbortError'){show('cpu','CPU —');show('memory','RAM —');}}finally{polling=false;}
 }
 const timer=setInterval(tick,1000);
 return {stop:()=>{clearInterval(timer);controller.abort();},snapshot:()=>latest||read()};
}
