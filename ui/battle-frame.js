const decoder=new TextDecoder();

// 数値配列をコピーせず、LEレコードから借用する。計算やfloat32化はしない。
function parseBattleFrame(header,buffer,start){
 const data=new DataView(buffer),length=header.getUint32(4,true),count=header.getUint32(8,true),size=header.getUint32(12,true);
 const offset=Math.ceil((start+length)/8)*8;
 if(size!==192||offset>buffer.byteLength||offset+count*size!==buffer.byteLength)throw Error('戦闘フレームの形式が一致しません');
 const value=JSON.parse(decoder.decode(new Uint8Array(buffer,start,length)));
 if(!value.scene&&count)throw Error('描画命令の所属がありません');
 const commands=new Array(count);
 for(let index=0;index<count;++index){
  const at=offset+index*size;
  commands[index]={texture:data.getInt32(at,true),layer:data.getInt32(at+4,true),count:data.getInt32(at+8,true),blend:data.getInt32(at+12,true),opacity:data.getFloat64(at+16,true),points:new Float64Array(buffer,at+24,16),cut:new Int32Array(buffer,at+152,4),colors:new Int32Array(buffer,at+168,6)};
 }
 if(value.scene)value.scene.commands=commands;
 value.serverMs=header.getFloat64(16,true);value.encodeMs=header.getFloat64(24,true);
 return value;
}

export function decodeBattleFrame(buffer){
 if(buffer.byteLength<32)throw Error('戦闘フレームが途中で切れています');
 const header=new DataView(buffer);
 if(header.getUint32(0,true)!==0x3146424b)throw Error('戦闘フレームの形式が一致しません');
 return parseBattleFrame(header,buffer,32);
}

export async function unpackBattleFrame(buffer){
 if(buffer.byteLength<32)throw Error('戦闘フレームが途中で切れています');
 const header=new DataView(buffer);
 if(header.getUint32(0,true)!==0x3147424b)return decodeBattleFrame(buffer);
 if(header.getUint32(12,true)!==192)throw Error('戦闘フレームの形式が一致しません');
 const payload=await new Response(new Blob([new Uint8Array(buffer,32)]).stream().pipeThrough(new DecompressionStream('gzip'))).arrayBuffer();
 return parseBattleFrame(header,payload,0);
}

export function createBattleFrameClient(){
 const samples=new Float64Array(120);let count=0;
 return {
  async load(payload,signal){
   const started=performance.now(),body=JSON.stringify({...payload,packed:true,compressed:typeof DecompressionStream==='function'});
   const response=await fetch(payload.session?'/api/battle-session/frame':'/api/battle-frame',{method:'POST',headers:{'Content-Type':'application/json'},body,signal});
   if(!response.ok){const value=await response.json();throw Error(value.error||'戦闘フレームを取得できません');}
   const buffer=await response.arrayBuffer(),received=performance.now(),value=await unpackBattleFrame(buffer),finished=performance.now();
   const timing={apiMs:finished-started,serverMs:value.serverMs,encodeMs:value.encodeMs,decodeMs:finished-received,transferMs:Math.max(0,received-started-value.serverMs),payloadBytes:buffer.byteLength};
   samples[count++%samples.length]=timing.apiMs;
   return {value,timing};
  },
  stats(){const values=[...samples.subarray(0,Math.min(count,samples.length))].sort((a,b)=>a-b);return {apiP95Ms:values[Math.ceil(values.length*.95)-1]||0,apiMaxMs:values.at(-1)||0,apiSamples:values.length};},
 };
}
