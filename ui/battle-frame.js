const decoder=new TextDecoder();

// 数値配列をコピーせず、LEレコードから借用する。計算やfloat32化はしない。
function parseBattleFrame(header,buffer,start,mobile=false){
 const data=new DataView(buffer),length=header.getUint32(4,true),count=header.getUint32(8,true),size=header.getUint32(12,true);
 const offset=Math.ceil((start+length)/8)*8;
 if(size!==(mobile?0:192)||offset>buffer.byteLength||count>Math.floor((buffer.byteLength-offset)/(mobile?64:192))||!mobile&&offset+count*size!==buffer.byteLength)throw Error('戦闘フレームの形式が一致しません');
 const value=JSON.parse(decoder.decode(new Uint8Array(buffer,start,length)));
 if(!value.scene&&count)throw Error('描画命令の所属がありません');
 const commands=new Array(count);
 let at=offset;
 for(let index=0;index<count;++index){
  if(at+64>buffer.byteLength)throw Error('戦闘フレームが途中で切れています');
  const vertices=data.getInt32(at+8,true),points=mobile?2*vertices:16,cut=at+24+points*8;
  if(vertices<0||vertices>8||cut+40>buffer.byteLength)throw Error('戦闘フレームの頂点数が不正です');
  commands[index]={texture:data.getInt32(at,true),layer:data.getInt32(at+4,true),count:vertices,blend:data.getInt32(at+12,true),opacity:data.getFloat64(at+16,true),points:new Float64Array(buffer,at+24,points),cut:new Int32Array(buffer,cut,4),colors:new Int32Array(buffer,cut+16,6)};
  at=cut+40;
 }
 if(at!==buffer.byteLength)throw Error('戦闘フレームの描画命令が一致しません');
 if(value.scene)value.scene.commands=commands;
 value.serverMs=header.getFloat64(16,true);value.encodeMs=header.getFloat64(24,true);
 return value;
}

export function decodeBattleFrame(buffer){
 if(buffer.byteLength<32)throw Error('戦闘フレームが途中で切れています');
 const header=new DataView(buffer);
 const format=header.getUint32(0,true);
 if(format!==0x3146424b&&format!==0x3150424b)throw Error('戦闘フレームの形式が一致しません');
 return parseBattleFrame(header,buffer,32,format===0x3150424b);
}

export async function unpackBattleFrame(buffer){
 if(buffer.byteLength<32)throw Error('戦闘フレームが途中で切れています');
 const header=new DataView(buffer);
 if(header.getUint32(0,true)!==0x3147424b)return decodeBattleFrame(buffer);
 if(header.getUint32(12,true)!==192)throw Error('戦闘フレームの形式が一致しません');
 const payload=await new Response(new Blob([new Uint8Array(buffer,32)]).stream().pipeThrough(new DecompressionStream('gzip'))).arrayBuffer();
 return parseBattleFrame(header,payload,0);
}

export function createBattleFrameClient({compress=true}={}){
 const samples=new Float64Array(120);let count=0;
 return {
  async load(payload,signal){
   const started=performance.now(),body=JSON.stringify({...payload,packed:true,compressed:compress&&typeof DecompressionStream==='function'});
   const response=await fetch(payload.session?'/api/battle-session/frame':'/api/battle-frame',{method:'POST',headers:{'Content-Type':'application/json'},body,signal});
   const headersReceived=performance.now();
   if(!response.ok){const value=await response.json();throw Error(value.error||'戦闘フレームを取得できません');}
   const buffer=await response.arrayBuffer(),received=performance.now(),value=await unpackBattleFrame(buffer),finished=performance.now();
   const wireBytes=Number(response.headers.get('Content-Length'))||buffer.byteLength;
   const timing={apiMs:finished-started,serverMs:value.serverMs,encodeMs:value.encodeMs,decodeMs:finished-received,transferMs:Math.max(0,received-started-value.serverMs),payloadBytes:wireBytes};
   const gzipMs=response.headers.get('X-KBCS-Gzip-Ms');
   if(gzipMs!==null)Object.assign(timing,{headersMs:headersReceived-started,bodyMs:received-headersReceived,gzipMs:Number(gzipMs)});
   samples[count++%samples.length]=timing.apiMs;
   return {value,timing};
  },
  stats(){const values=[...samples.subarray(0,Math.min(count,samples.length))].sort((a,b)=>a-b);return {apiP95Ms:values[Math.ceil(values.length*.95)-1]||0,apiMaxMs:values.at(-1)||0,apiSamples:values.length};},
 };
}
