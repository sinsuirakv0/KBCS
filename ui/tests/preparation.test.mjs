import {bindDetailNavigation} from '../native-state.js';
import {createSessionId} from '../src/shared/browser/session-id.js';
// BGMのシーク・取得待ちの取消、編成設定の復元、速度と表示比率の回帰。
import assert from 'node:assert/strict';
import {createAudioPreview} from '../src/shared/browser/audio-preview.js';
import {readSortiePreferences,toggleSortieItem} from '../sortie-view.js';
import {battleViewportWidth,battlePlaybackRate} from '../battle-view.js';

const local={getItem:()=>JSON.stringify({formation:7,items:{speedup:true},speed:3})},session={getItem:()=>JSON.stringify({formation:1,speed:2})};
assert.equal(readSortiePreferences(local,session).formation,7);assert.equal(readSortiePreferences(local,session).speed,3);
assert.equal(readSortiePreferences({getItem(){throw Error('blocked');}},session).formation,1);
const items={};let speed=2;speed=toggleSortieItem(items,speed,'speedup');assert.equal(speed,2);assert.equal(items.speedup,true);speed=toggleSortieItem(items,speed,'speedup');assert.equal(speed,3);speed=toggleSortieItem(items,speed,'speedup');assert.equal(items.speedup,false);
for(const [ratio,expected]of [['20:9',1422],['16:9',1138],['18:9',1280],['21:9',1493]]){assert.equal(battleViewportWidth(ratio,300,600),expected);assert.equal(battleViewportWidth(ratio,1600,600),expected);}
assert.equal(battleViewportWidth('auto',960,640),960);assert.equal(battleViewportWidth('unknown',960,640),1422);
class AudioMock{
 constructor(){this.dataset={source:'/api/stage-audio/193'};this.paused=true;this.duration=NaN;this.currentTime=0;}
 load(){assert.ok(this.src.startsWith('blob:'));this.duration=120;this.onloadedmetadata?.();}
 play(){this.paused=false;this.onplay?.();return Promise.resolve();}
 pause(){this.paused=true;this.onpause?.();}
 removeAttribute(){delete this.src;}
}
const make=()=>{const audio=new AudioMock(),button={},seek=new EventTarget(),time={};seek.value='0';const player=createAudioPreview(audio,button,seek,time,()=>{});return {audio,button,seek,time,player};};
const originalFetch=globalThis.fetch;globalThis.fetch=async()=>({ok:true,blob:async()=>new Blob(['ogg'])});
try{
 const a=make();await a.player.toggle();assert.equal(a.audio.paused,false);assert.equal(a.seek.disabled,false);
 a.seek.dispatchEvent(new Event('pointerdown'));a.seek.value='75';a.seek.dispatchEvent(new Event('input'));assert.equal(a.audio.currentTime,90);
 a.audio.currentTime=1;a.audio.ontimeupdate();assert.equal(a.seek.value,'75');
 a.seek.dispatchEvent(new Event('change'));assert.equal(a.audio.currentTime,90);a.player.pause();assert.equal(a.audio.paused,true);a.player.dispose();assert.equal(a.audio.src,undefined);
 let finish;globalThis.fetch=()=>new Promise(resolve=>finish=resolve);const b=make(),waiting=b.player.toggle();b.player.dispose();finish({ok:true,blob:async()=>new Blob(['ogg'])});await waiting;assert.equal(b.audio.paused,true);assert.equal(b.audio.src,undefined);
}finally{globalThis.fetch=originalFetch;}
console.log('seek, cancellation, saved formation, speed cycle and aspect settings passed');

// 一時枠は上の最小空き番号だけに手動で移り、既存設定を破壊しない。
const {addFormationMember,moveTrayMember}=await import('../formation-tray.js');
const slots=Array.from({length:10},(_,i)=>({unitId:i,level:60,orbs:[17]})),tray=Array(5).fill(null),member={unitId:50,level:31,orbs:[12]};
assert.deepEqual(addFormationMember(slots,tray,member),{group:'tray',index:0,changed:true});
slots[7]=null;slots[3]=null;assert.equal(tray[0],member);assert.equal(moveTrayMember(slots,tray,0),3);assert.equal(slots[3],member);assert.equal(tray[0],null);
assert.deepEqual(addFormationMember(slots,tray,{unitId:2}),{group:'slots',index:2,changed:false});assert.deepEqual(slots[2].orbs,[17]);
assert.equal(addFormationMember(slots,tray,{unitId:51}).index,7);
for(let mode=0;mode<=2;++mode){assert.equal(battlePlaybackRate(0,mode),1);assert.equal(battlePlaybackRate(20,mode)*(mode+1),20);}
console.log('formation tray and absolute playback rate passed');

assert.equal(createSessionId({getRandomValues:bytes=>bytes.fill(0)}),'00000000-0000-4000-8000-000000000000');

// custom schemeのoriginはnullになり得る。履歴の保存に無効なbaseを渡さない。
const oldLocation=globalThis.location,oldDocument=globalThis.document,oldSession=globalThis.sessionStorage;
const saved=new Map(),handlers=[];
globalThis.location=new URL('kbcs://localhost/pages/unit-search/');
globalThis.document={addEventListener:(name,handler)=>handlers.push(handler)};
globalThis.sessionStorage={setItem:(key,value)=>saved.set(key,value)};
bindDetailNavigation('unit-detail','/pages/unit-detail/',()=>new URLSearchParams('id=42'));
handlers[0]({target:{closest:()=>({href:'kbcs://localhost/pages/unit-detail/?id=42'})}});
assert.equal(saved.get('kbcs:view:unit-detail:42'),'id=42');
globalThis.location=oldLocation;globalThis.document=oldDocument;globalThis.sessionStorage=oldSession;

// 円単位の価格を桁落ちさせず、編集と準備で同じ値引き済み結果を描く。
const {readFileSync}=await import('node:fs');
const {createFormationView}=await import('../formation-view.js');
const {resolveFormationMember}=await import('../formation-model.js');
const {stageDeployment}=await import('../battle-support.js');
const artwork=JSON.parse(readFileSync(new URL('../images/native-formation/manifest.json',import.meta.url),'utf8').replace(/^\uFEFF/,''));
const unit={id:45,rarity:1,orbSlots:0,forms:[{index:0,name:'a',icon:'a.png',cost:300},{index:1,name:'b',icon:'b.png',cost:600}],talents:[]};
const stored={unitId:45,form:2,level:50,plus:0,talents:{},orbs:[]},document={slots:[stored,...Array(9).fill(null)],cannon:{id:0}},db={units:[unit],imageBase:'/api/asset/'};
assert.equal(resolveFormationMember(unit,stored).form,1);assert.equal(stored.form,2);
const paint=createFormationView(db,artwork),deployment={slots:Array.from({length:10},()=>({cost:4500,reasons:0}))};
for(const preview of [false,true])assert.equal((paint(document,{deployment,preview}).match(/native-formation\/img023_ja.png/g)||[]).length,5);
const fetchBefore=globalThis.fetch;
globalThis.fetch=async(path,options)=>{const input=JSON.parse(options.body);assert.equal(input.costs[0].raw,600);assert.equal(input.costs[0].reduction,100);return {ok:true,json:async()=>({costs:[750,...Array(9).fill(0)],checks:[0,0]})};};
try{
 unit.talents=[{index:0,effect:{key:'cost'},values:[[100,0,0,0]]}];unit.forms.push({index:2,name:'c',icon:'c.png',cost:600});stored.talents={0:1};
 const costs=await stageDeployment(db,null,null,null,document);assert.equal(costs.slots[0].cost,750);
}finally{globalThis.fetch=fetchBefore;}
const {swapTrayMember}=await import('../formation-tray.js');
const pending=tray[0]={unitId:99,level:33,talents:{2:7},orbs:[5]},previous=slots[1];
assert.equal(swapTrayMember(slots,tray,0,1),true);assert.equal(slots[1],pending);assert.equal(tray[0],previous);
assert.equal(swapTrayMember(slots,tray,0,-1),false);
for(const mode of [0,1,2])assert.ok(Math.abs(battlePlaybackRate(.1,mode)*(mode+1)-.1)<1e-10);
console.log('price units, discounts, unavailable forms, tray swap and slow playback passed');

// 合計Lv60境界と、空の一時枠への逆方向の移動も個別設定を保持する。
const advanced={...unit,rarity:4,forms:[...unit.forms,{index:3}],talents:[{index:1,limit:1}]};
const advancedMember={...stored,form:3,level:59,plus:1,talents:{1:10}};
assert.equal(resolveFormationMember(advanced,advancedMember).form,3);
assert.equal(resolveFormationMember(advanced,advancedMember).talents[1],10);
assert.equal(resolveFormationMember(advanced,{...advancedMember,plus:0}).form,2);
assert.equal(resolveFormationMember(advanced,{...advancedMember,plus:0}).talents[1],0);
const reverseSlots=[pending,null],reverseTray=[null,previous];
assert.equal(swapTrayMember(reverseSlots,reverseTray,0,0),true);
assert.equal(reverseSlots[0],null);assert.equal(reverseTray[0],pending);
assert.equal(swapTrayMember(reverseSlots,reverseTray,1,1),true);
assert.equal(reverseSlots[1],previous);assert.equal(reverseTray[1],null);
assert.equal(swapTrayMember(reverseSlots,reverseTray,-1,0),false);
console.log('total level unlock and bidirectional tray transfers passed');

// 原本19要素の番号表と追加の20画像。21以降も文字フォントへ戻さない。
for(const [index,cut]of [[1,44],[10,53],[11,113],[16,125],[17,126],[18,138],[19,140],[20,141]]){
 assert.ok(paint(document,{index}).includes('viewBox="'+artwork.atlases.img029_ja.rects[cut].join(' ')+'"'));
}
for(const index of [21,100,1234])assert.ok(!paint(document,{index}).includes('>'+index+'</text>'));
assert.ok(!paint(document,{preview:true}).includes('data-action="cannon"'));

// 共用ジェスチャーは浮遊画像をbodyへ出し、取消で個別設定ごと戻す。準備では枠外でも削除しない。
const {createFormationReorder}=await import('../formation-reorder.js');
const beforeWindow=globalThis.window,beforeInterval=globalThis.setInterval;
let tick,overlay=null,selected=-1,commits=0;
const events={},capture=new Set(),a={unitId:1,level:59,plus:1,orbs:[17]},b={unitId:2,level:40,orbs:[]};
const editing={...document,slots:[a,b,...Array(8).fill(null)]};
const surface={addEventListener:(name,callback)=>events[name]=callback,querySelector:()=>({getBoundingClientRect:()=>({left:0,top:0,width:1188,height:278})}),setPointerCapture:id=>capture.add(id),hasPointerCapture:id=>capture.has(id),releasePointerCapture:id=>capture.delete(id)};
globalThis.window={addEventListener(){},document:{createElement:()=>({style:{},setAttribute(){},remove(){overlay=null;}}),body:{append:value=>overlay=value}}};
globalThis.setInterval=callback=>{tick=callback;};
try{
 let reorder;
 reorder=createFormationReorder(surface,{getDocument:()=>editing,getDeployment:()=>deployment,paint,allowRemove:false,onSelect:slot=>selected=slot,onDraw:()=>reorder.renderFloating(),onCommit:()=>++commits});
 const pointer=(type,slot,x,y)=>events[type]({target:{closest:()=>({dataset:{slot}})},button:0,pointerId:7,clientX:x,clientY:y});
 pointer('pointerdown',0,320,120);for(let i=0;i<4;++i)tick();assert.equal(overlay,null);
 tick();assert.ok(overlay);assert.equal(reorder.view.hiddenSlot,0);assert.equal(overlay.style.left,'290px');
 pointer('pointermove',0,470,120);tick();assert.equal(selected,1);assert.deepEqual(editing.slots.slice(0,2),[b,a]);
 events.pointercancel();assert.equal(overlay,null);assert.equal(reorder.active,false);assert.equal(editing.slots[0],a);assert.equal(commits,0);
 pointer('pointerdown',0,320,120);for(let i=0;i<5;++i)tick();pointer('pointermove',0,470,120);tick();pointer('pointerup',0,470,120);
 assert.equal(commits,1);assert.equal(editing.slots[1],a);for(let i=0;i<12;++i)tick();assert.equal(overlay,null);
 pointer('pointerdown',1,470,120);for(let i=0;i<5;++i)tick();pointer('pointermove',1,470,500);tick();pointer('pointerup',1,470,500);for(let i=0;i<16;++i)tick();
 assert.equal(editing.slots[1],a);assert.equal(commits,1);assert.equal(overlay,null);
}finally{globalThis.window=beforeWindow;globalThis.setInterval=beforeInterval;}
console.log('native slot number sprites, global drag overlay, reorder cancellation and preparation drops passed');

// 1段時だけ下段のキーを表示中5枠へ対応させ、編成番号との対応を保持する。
const {defaultBattleKeys,battleKeyAction,normalizeBattleKeys}=await import('../keyboard.js');
assert.deepEqual(battleKeyAction('KeyD',defaultBattleKeys,{rows:2,page:0}),{target:0});
assert.deepEqual(battleKeyAction('KeyM',defaultBattleKeys,{rows:2,page:0}),{target:9});
assert.equal(battleKeyAction('KeyD',defaultBattleKeys,{rows:1,page:0}),null);
assert.deepEqual(battleKeyAction('KeyC',defaultBattleKeys,{rows:1,page:0}),{target:0});
assert.deepEqual(battleKeyAction('KeyM',defaultBattleKeys,{rows:1,page:1}),{target:9});
assert.deepEqual(battleKeyAction('Space',defaultBattleKeys,{rows:1,page:0}),{control:4});
assert.equal(battleKeyAction('Space',defaultBattleKeys,{rows:2,page:0}),null);
assert.equal(normalizeBattleKeys({wallet:'invalid'}).wallet,'KeyX');
assert.equal(normalizeBattleKeys({wallet:''}).wallet,'');
