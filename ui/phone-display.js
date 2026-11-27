import {enterPhoneFullscreen} from './phone-connection.js';

const standby=document.getElementById('phone-standby'),viewport=document.getElementById('phone-viewport');
const status=document.getElementById('phone-status');
let current=null,checksFailed=0;
const fullscreen=document.getElementById('phone-fullscreen'),displayError=document.getElementById('phone-display-error');
const fullscreenHint=document.getElementById('phone-fullscreen-hint');
let noticeTimer,fullscreenHintTimer;
fullscreen.onclick=async()=>{
 const message=await enterPhoneFullscreen();
 clearTimeout(noticeTimer);
 displayError.textContent=message;displayError.hidden=!message;
 if(message)noticeTimer=setTimeout(()=>{displayError.hidden=true;},5000);
};
document.addEventListener('fullscreenchange',()=>{
 clearTimeout(fullscreenHintTimer);
 fullscreenHint.hidden=document.fullscreenElement!==document.documentElement;
 // Chrome側の案内が閉じたことはページから取得できないため、表示時間を区切る。
 if(!fullscreenHint.hidden)fullscreenHintTimer=setTimeout(()=>{fullscreenHint.hidden=true;},4000);
 if(!document.fullscreenElement)displayError.hidden=true;
});
window.screen.orientation?.addEventListener('change',()=>{if(window.matchMedia('(orientation: landscape)').matches)displayError.hidden=true;});
function show(route,message){
 if(route!==current){
  document.documentElement.classList.remove('phone-playing');
  // 画面を外す前に、同一オリジンの戦闘と準備中の要求を終了させる。
  try{viewport.querySelector('iframe')?.contentWindow?.dispatchEvent(new Event('kbcs:phone-leave'));}catch{}
  current=route;viewport.replaceChildren();
  if(route){
   const frame=document.createElement('iframe');frame.title='KBCS 出撃準備・戦闘';
   frame.allow='fullscreen; autoplay';frame.src=route;viewport.append(frame);
  }
 }
 standby.hidden=!!route;viewport.hidden=!route;status.textContent=message;
}
async function poll(){
 try{
  const response=await fetch('/api/phone/screen',{signal:AbortSignal.timeout(1600)});
  if(!response.ok)throw Error('スマホ接続を確認できません');
  const {route}=await response.json();
  checksFailed=0;show(route,'PCでステージを選んでください');
 }catch{
  if(++checksFailed>=2)show(null,'USB接続を待っています');
 }
 setTimeout(poll,current?800:280);
}
poll();
