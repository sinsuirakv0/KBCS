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
