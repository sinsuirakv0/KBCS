// 取得待ちの通知・終了境界・同一SE・ミュート・破棄を、音声デバイスを使わず検査する。
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
const requests=new Map(),sources=[];
let context;
globalThis.fetch=url=>{const id=Number(url.split('/').at(-1));let resolve;const promise=new Promise(done=>resolve=done);requests.set(id,()=>resolve({ok:true,arrayBuffer:async()=>Uint32Array.of(id).buffer}));return promise;};
globalThis.AudioContext=class {
 constructor(){context=this;this.currentTime=0;}
 createGain(){return this.gain={gain:{value:1},connect(){}};}
 resume(){return Promise.resolve();}
 close(){this.closed=true;return Promise.resolve();}
 async decodeAudioData(data){return {id:new Uint32Array(data)[0]};}
 createBufferSource(){const source={connect(){},disconnect(){},start(when){this.started=when;},stop(when){this.stopped=when??0;}};sources.push(source);return source;}
};
const text=await readFile(new URL('../battle-audio.js',import.meta.url),'utf8');
const {createBattleSounds}=await import('data:text/javascript;base64,'+Buffer.from(text).toString('base64'));
const flush=async()=>{for(let i=0;i<3;++i)await new Promise(setImmediate);};
const errors=new Map(),sounds=createBattleSounds(errors);
sounds.update([{frame:1,id:10}],3);requests.get(10)();await flush();
const press=sources.at(-1);assert.equal(press.buffer.id,10);
sounds.update([{frame:2,id:20}],3);await flush();
sounds.update([{frame:3,id:8}],3,1,false,true);requests.get(8)();await flush();
assert.equal(sources.at(-1).buffer.id,8);assert.equal(press.stopped,undefined);
requests.get(20)();await flush();assert(!sources.some(source=>source.buffer.id===20));
const first=sources.at(-1);sounds.update([{frame:4,id:8},{frame:4,id:8}],3,1,false,true);await flush();
assert.equal(sources.filter(source=>source.buffer.id===8).length,3);assert.equal(first.stopped,0);
sounds.update([{frame:5,id:21}],3,1,false,true);await flush();
sounds.update([],0,1,false,true);assert.equal(context.gain.gain.value,0);
sounds.update([{frame:6,id:11}],1,1,false,true);requests.get(11)();await flush();
assert.equal(context.gain.gain.value,.25);assert.equal(sources.at(-1).buffer.id,11);
requests.get(21)();await flush();assert(!sources.some(source=>source.buffer.id===21));
sounds.update([{frame:7,id:9}],3,1,false,true);sounds.stop();requests.get(9)();await flush();
assert(context.closed);assert(!sources.some(source=>source.buffer.id===9));assert.equal(errors.size,0);
console.log('SE lifetime, finish, repeat and mute passed');
