const encoder=new TextEncoder(),decoder=new TextDecoder();
const module=import('/phone-runtime/kbcs-phone.mjs').then(({default:create})=>create());
// Wasmの入力と出力は次の呼出しまで。フレームは1回コピーして描画側に所有権を渡す。
self.onmessage=async({data:{id,operation,payload}})=>{
 try{
  const wasm=await module;
  const input=payload instanceof ArrayBuffer?new Uint8Array(payload):encoder.encode(JSON.stringify(payload));
  const address=wasm._kbcs_phone_input(input.length);
  wasm.HEAPU8.set(input,address);
  const failed=wasm._kbcs_phone_call(operation),start=wasm._kbcs_phone_output(),length=wasm._kbcs_phone_length();
  const bytes=wasm.HEAPU8.subarray(start,start+length);
  if(failed)throw Error(decoder.decode(bytes));
  if(operation===1){
   const buffer=bytes.slice().buffer;
   self.postMessage({id,value:buffer},[buffer]);
  }else self.postMessage({id,value:length?JSON.parse(decoder.decode(bytes)):null});
 }catch(error){self.postMessage({id,error:error.message});}
};
