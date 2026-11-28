// 描画前の遮蔽、入力時点でのキー解決、報酬通知の一括準備を検査する。
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {runInNewContext} from 'node:vm';
import {battleKeyAction,defaultBattleKeys,editableKeyTarget} from '../keyboard.js';
import {createResultPopup} from '../battle-result-popup.js';
import {battleScreenConfiguration} from '../battle-screen.js';
import {battleCameraView} from '../battle-view.js';
import {catalog} from '../simulation-profile.js';
import {calculateNative} from '../native-calculation.js';

const originalFetch=globalThis.fetch;
try{
 for(const abi of [5,4]){
  globalThis.fetch=async()=>({ok:true,json:async()=>({abi,ruleset:catalog.versionCode})});
  if(abi===5)assert.equal((await calculateNative({})).abi,5);
  else await assert.rejects(calculateNative({}),/計算コアの版/);
 }
}finally{globalThis.fetch=originalFetch;}

const boot=readFileSync(new URL('../startup-boot.js',import.meta.url),'utf8');
for(const seen of [false,true]){
 const attributes=new Map(),styles=[];
 runInNewContext(boot,{sessionStorage:{getItem:()=>seen?'1':null},document:{documentElement:{setAttribute:(key,value)=>attributes.set(key,value)},createElement:()=>({}),head:{append:style=>styles.push(style)}}});
 assert.equal(attributes.has('data-kbcs-starting'),!seen);assert.equal(styles.length,seen?0:1);
 if(!seen)assert.ok(styles[0].textContent.includes('visibility:hidden'));
}
const state={rows:2,page:0,page_frame:0,guard:0,paused:0};
assert.deepEqual(battleKeyAction('KeyD',defaultBattleKeys,state),{target:0});
assert.equal(battleKeyAction('Space',defaultBattleKeys,state),null);
assert.deepEqual(battleKeyAction('KeyC',defaultBattleKeys,{...state,rows:1,page:1}),{target:5});
const focusedInput=type=>({closest:selector=>selector==='input'?{type}:null});
assert.equal(editableKeyTarget(focusedInput('checkbox')),false);
assert.equal(editableKeyTarget(focusedInput('number')),true);
assert.equal(editableKeyTarget({closest:selector=>selector.includes('select')?{}:null}),false);
assert.equal(editableKeyTarget({closest:selector=>selector.includes('dialog[open]')?{}:null}),true);
const screen=readFileSync(new URL('../battle-screen.js',import.meta.url),'utf8');
const sortie=readFileSync(new URL('../pages/stage-sortie/index.html',import.meta.url),'utf8');
assert.match(sortie,/class="sortie-launch-options"><button[^>]*data-recording>録画<\/button><label><input type="checkbox" id="sortie-large-start"/);
assert.match(sortie,/data-debug="large"/);
assert.match(screen,/large&&!phone&&event\.code==='Escape'/);
assert.ok(!screen.includes('keyQueue'));
assert.ok(screen.includes("readBattleJson('/api/battle-session/input'"));
const live={...state,intro:24},camera={center:1000,zoom:2.5,minimum:.49};
assert.equal(battleCameraView({...live,intro:23},{},camera,1422),null);
assert.equal(battleCameraView({...live,paused:1},{},camera,1422),null);
assert.equal(battleCameraView(live,{endCameraActive:true},camera,1422),null);
assert.deepEqual(battleCameraView(live,{endCameraActive:false,cameraMaximum:.9633},camera,1422),
 {...camera,viewport_width:1422,cameraWidth:960,maximum:.9633});
const snapshot={formation:{slots:Array(10).fill(null),profile:{facilities:Object.fromEntries(['worker','wallet','cannonAttack','cannonCharge'].map(key=>[key,{level:1,plus:0}])),treasures:Object.fromEntries(catalog.treasures.map(v=>[v.id,100]))}},map:{series:'EOC',number:1,rules:[]},items:{speedup:true},deployment:{slots:Array.from({length:10},()=>({cost:0,reasons:0}))}};
for(const speed of [2,3]){
 const {config,speedMode}=battleScreenConfiguration({combos:[]},{...snapshot,speed});
 assert.equal(config.speed,speed);assert.equal(config.items,1);assert.equal(speedMode,speed-1);
}
const noSpeed=battleScreenConfiguration({combos:[]},{...snapshot,items:{speedup:false},speed:3});
assert.equal(noSpeed.config.items&1,1);assert.equal(noSpeed.itemsOn&1,0);assert.equal(noSpeed.speedMode,0);

const beforeDocument=globalThis.document,beforeFetch=globalThis.fetch;
const calls=[],draws=[],errors=[];
globalThis.document={createElement(){return {getContext:()=>({measureText:()=>({width:200,fontBoundingBoxAscent:24,fontBoundingBoxDescent:6}),fillText(){}})};}};
globalThis.fetch=async(path,options)=>{
 assert.equal(path,'/api/battle-popup');const input=JSON.parse(options.body);calls.push(input);
 assert.ok(input.length<=50);assert.ok(Buffer.byteLength(options.body)<=16384);
 return {ok:true,json:async()=>input.map(row=>({body:[0,401,670,144],parts:[[0,0,10,10,0,0,10,10]],textScale:Array(row.count).fill(1),textX:Array(row.count).fill(100),textY:300}))};
};
try{
 const popup=createResultPopup(error=>errors.push(error)),atlas={atlases:{img005_1:{image:'popup',rects:[[0,0,100,100],[],[],[],[],[],[],[],[6,6]]}}};
 const messages=Array.from({length:12},(_,index)=>'reward '+index);
 messages[0]='material 1 material 2<br>';
 messages[1]='material 1 material 2<br>material 3 material 4<br>';
 await popup.prepare(messages,1422,atlas);assert.deepEqual(calls.map(v=>v.length),[50,10]);
 assert.deepEqual(calls[0].slice(0,10).map(row=>row.count),[1,1,1,1,1,2,2,2,2,2]);
 await popup.prepare(messages,1422,atlas);assert.equal(calls.length,2);
 const translations=[],context={save(){},restore(){},translate:(...args)=>translations.push(args),drawImage:(...args)=>draws.push(args)};
 const ready={index:11,scaleFrame:4,phase:1,flash:0},images=new Map([['popup',{}]]);
 popup.paint(context,ready,atlas,images);
 assert.equal(draws.length,2);assert.deepEqual(errors,[]);
 assert.deepEqual(translations,[]);
 popup.paint(context,ready,atlas,images,480);
 assert.deepEqual(translations,[[0,7]]);
 popup.stop();draws.length=0;popup.paint(context,{index:0},atlas,images);assert.equal(draws.length,0);
}finally{globalThis.document=beforeDocument;globalThis.fetch=beforeFetch;}
console.log('first paint, direct keys and batched reward popup passed');
