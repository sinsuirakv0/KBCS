// 描画前の遮蔽、0tick/通信待ちのキー保持、報酬通知の一括準備を検査する。
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {runInNewContext} from 'node:vm';
import {createBattleKeyQueue,defaultBattleKeys} from '../keyboard.js';
import {createResultPopup} from '../battle-result-popup.js';
import {battleScreenConfiguration} from '../battle-screen.js';
import {catalog} from '../simulation-profile.js';

const boot=readFileSync(new URL('../startup-boot.js',import.meta.url),'utf8');
for(const seen of [false,true]){
 const attributes=new Map(),styles=[];
 runInNewContext(boot,{sessionStorage:{getItem:()=>seen?'1':null},document:{documentElement:{setAttribute:(key,value)=>attributes.set(key,value)},createElement:()=>({}),head:{append:style=>styles.push(style)}}});
 assert.equal(attributes.has('data-kbcs-starting'),!seen);assert.equal(styles.length,seen?0:1);
 if(!seen)assert.ok(styles[0].textContent.includes('visibility:hidden'));
}
const queue=createBattleKeyQueue(defaultBattleKeys),state={rows:2,page:0,page_frame:0,guard:0,paused:0};
queue.push('KeyD');queue.push('KeyF');
assert.equal(queue.take(state,0),null);assert.equal(queue.pending,true);
assert.deepEqual(queue.take(state,1),{target:0});
assert.equal(queue.take({...state,guard:3},1),null);
assert.deepEqual(queue.take(state,1),{target:1});assert.equal(queue.pending,false);
queue.push('Space');queue.push('KeyC');
assert.deepEqual(queue.take({...state,rows:1},1),{control:4});
assert.equal(queue.take({...state,rows:1,page_frame:4},1),null);
assert.deepEqual(queue.take({...state,rows:1,page:1},1),{target:5});
queue.push('KeyD');assert.deepEqual(queue.take({...state,guard:4},0,true),{target:0});
queue.push('KeyF');queue.clear();assert.equal(queue.pending,false);
const snapshot={formation:{slots:Array(10).fill(null),profile:{facilities:Object.fromEntries(['worker','wallet','cannonAttack','cannonCharge'].map(key=>[key,{level:1,plus:0}])),treasures:Object.fromEntries(catalog.treasures.map(v=>[v.id,100]))}},map:{series:'EOC',number:1,rules:[]},items:{speedup:true},deployment:{slots:Array.from({length:10},()=>({cost:0,reasons:0}))}};
for(const speed of [2,3]){const {config}=battleScreenConfiguration({combos:[]},{...snapshot,speed});assert.equal(config.speed,speed);assert.equal(config.items,1);}

const beforeDocument=globalThis.document,beforeFetch=globalThis.fetch;
const calls=[],draws=[],errors=[];
globalThis.document={createElement(){return {getContext:()=>({measureText:()=>({width:200,fontBoundingBoxAscent:24,fontBoundingBoxDescent:6}),fillText(){}})};}};
globalThis.fetch=async(path,options)=>{
 assert.equal(path,'/api/battle-popup');const input=JSON.parse(options.body);calls.push(input);
 assert.ok(input.length<=50);assert.ok(Buffer.byteLength(options.body)<=16384);
 return {ok:true,json:async()=>input.map(row=>({parts:[[0,0,10,10,0,0,10,10]],textScale:Array(row.count).fill(1),textX:Array(row.count).fill(100),textY:300}))};
};
try{
 const popup=createResultPopup(error=>errors.push(error)),atlas={atlases:{img005_1:{image:'popup',rects:[[0,0,100,100],[],[],[],[],[],[],[],[6,6]]}}};
 const messages=Array.from({length:12},(_,index)=>'reward '+index);
 await popup.prepare(messages,1422,atlas);assert.deepEqual(calls.map(v=>v.length),[50,10]);
 await popup.prepare(messages,1422,atlas);assert.equal(calls.length,2);
 const context={save(){},restore(){},drawImage:(...args)=>draws.push(args)};
 popup.paint(context,{index:11,scaleFrame:4,phase:1,flash:0},1422,atlas,new Map([['popup',{}]]));
 assert.equal(draws.length,2);assert.deepEqual(errors,[]);
 popup.stop();draws.length=0;popup.paint(context,{index:0},1422,atlas,new Map());assert.equal(draws.length,0);
}finally{globalThis.document=beforeDocument;globalThis.fetch=beforeFetch;}
console.log('first paint, queued keys and batched reward popup passed');
