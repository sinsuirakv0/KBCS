// 005e97d8 / 005ecde0 / 005ee758 / 005efbac。時計と座標はC++が返す。
import {createResultPopup} from './battle-result-popup.js';
import {nativeFont} from './native-font.js';
export function createBattleResults(controls,{drawing=true,summary=true,pixel8TextPreview=false,loadLayouts}={}){
 const panel=document.createElement('section');panel.className='battle-receipt';panel.hidden=true;panel.setAttribute('aria-label','戦闘結果');
 const host=document.querySelector('.workspace-right .workspace-panel-content');(host||controls).append(panel);
 const button=document.createElement('button');button.type='button';button.textContent='報酬・記録';button.hidden=true;controls.querySelector('.battle-actions').append(button);
 let runtime,last,lastEx;const metadata=new Map();
 const popup=drawing?createResultPopup(error=>{panel.hidden=false;panel.textContent='通知の配置を取得できません：'+error;},{pixel8TextPreview,loadLayouts}):null;
 function open(){const toggle=document.querySelector('[data-workspace-toggle=right]');if(toggle?.getAttribute('aria-expanded')==='false')toggle.click();panel.scrollIntoView({block:'nearest'});}
 button.addEventListener('click',open);
 function render(){
  panel.replaceChildren();const receipt=runtime.receipt;
  const heading=document.createElement('h3');heading.textContent=runtime.result.mode===1?'クリア結果':runtime.result.mode===4||runtime.result.mode===7?'戦闘結果':'敗北';panel.append(heading);
  if(runtime.result.mode===2&&runtime.continueNotice){const note=document.createElement('p');note.textContent=runtime.continueNotice;panel.append(note);}
  if(runtime.continuePrompt){
   if(runtime.continuePrompt.error){const note=document.createElement('p');note.setAttribute('role','alert');note.textContent=runtime.continuePrompt.error;panel.append(note);}
   return;
  }
  if(runtime.receiptError){const error=document.createElement('p');error.setAttribute('role','alert');error.textContent='報酬を保存できませんでした。再試行中：'+runtime.receiptError;panel.append(error);return;}
  if(!receipt){panel.append(document.createTextNode('結果を保存しています…'));return;}
  const title=document.createElement('p');title.textContent=receipt.stageName;panel.append(title);
  if(runtime.rules.scoreType||receipt.score){const score=document.createElement('p');score.textContent=(runtime.rules.scoreType===3?'Pt ':'Score ')+receipt.score.toLocaleString();panel.append(score);}
  const list=document.createElement('dl');
  for(const reward of receipt.rewards){
   const item=metadata.get(reward.id),name=document.createElement('dt'),value=document.createElement('dd');
   if(item?.icon){const image=new Image();image.src='/api/asset/'+item.icon;image.alt='';image.width=32;image.height=32;image.loading='lazy';name.append(image);}
   name.append(document.createTextNode(item?.name||'報酬 '+reward.id));value.textContent='＋'+reward.amount.toLocaleString()+'　'+reward.before.toLocaleString()+' → '+reward.after.toLocaleString();list.append(name,value);
  }
  panel.append(list);
  if(!receipt.rewards.length){const empty=document.createElement('p');empty.textContent=receipt.mode===1?'今回の報酬はありません':'報酬なし';panel.append(empty);}
  if(receipt.radarBlocked){const note=document.createElement('p');note.textContent='レーダー対象の報酬は取得済みです';panel.append(note);}
  const link=document.createElement('a');link.href='/pages/inventory/';link.textContent='持ち物を開く';panel.append(link);if(runtime.ex?.source>0){const next=document.createElement('a');next.href='/pages/stage-sortie/?'+new URLSearchParams({map:'EX'+String(runtime.ex.mapIndex).padStart(3,'0'),stage:runtime.ex.stage,crown:1});next.textContent='EXステージへ';panel.append(document.createElement('br'),next);}
 }
 if(summary)fetch('/api/inventory/catalog').then(r=>r.json()).then(value=>{for(const item of value.items||[])metadata.set(item.id,item);if(runtime?.receipt)render();}).catch(()=>{});
 return {
  update(value,width,atlas){runtime=value;
   // phase0から準備し、勝利文字/経験値の演出中に通知の配置を取得する。
   if(runtime.result.mode===2&&runtime.continueNotice){
    popup?.prepare([[runtime.continueNotice,runtime.defeatBossHp].filter(Boolean).join('<br>')],width,atlas);
   }
   else if(runtime.receipt)popup?.prepare(runtime.receipt.notifications||[],width,atlas);
   if(!summary)return;
   const visible=!!(runtime.result.mode&&(runtime.receipt||runtime.receiptError||runtime.continuePrompt?.error));button.hidden=!visible;panel.hidden=!visible;if(!visible){last=undefined;return;}
   const key=runtime.receipt?'saved':runtime.receiptError||runtime.continuePrompt?.error;if(key!==last||lastEx!==runtime.ex?.source){last=key;lastEx=runtime.ex?.source;render();}
  },
  paint(context,width,sprite,number,atlas,images){
   if(!runtime?.result.mode)return;
   const e=runtime.ending,r=runtime.result,dojo=r.mode===4,name=dojo?'img004_DOJO_ja':'img004_ja';
   if(e.title[2]>=0)sprite(name,e.title[2],e.title[0],e.title[1]);
   // 005eb040は00887594のYオフセットに画面高の1/4を渡す。
   if(e.phase===5){popup.paint(context,e.popup,atlas,images,640/2+640/4);return;}
   const prompt=runtime.continuePrompt;
   if(prompt){
    const {layout,lines,cost,balance,error}=prompt,center=Math.trunc(width/2);
    if(layout.panel[2])sprite('img005',0,...layout.panel);
    if(!layout.ready)return;
    context.save();context.font=nativeFont(30);context.fillStyle='#fff';context.textAlign='center';context.textBaseline='top';
    const text=error?[error]:lines;for(const [i,line] of text.entries())context.fillText(line,center,440-text.length*18+i*36,650);
    context.restore();
    // 005ecde0: 必要ネコカンと、「はい」「いいえ」の部品。
    number(cost,0,center+345,306);sprite('img006_ja',21,center+162,306,55,42);sprite('img002_ja',43,center+113,320,60,30);
    for(const [i,b] of layout.buttons.entries()){
     sprite('img101',0,...b);sprite('img006_ja',4+i,...layout.labels[i]);
     if(layout.pressed===i+1)sprite('img101',layout.guard&&Math.trunc(layout.guard/2)%2?2:1,...b);
    }
    // 00751608: img024_ja部品11の幅290を右端から引いた基準位置。
    if(balance!=null){sprite('img006_ja',21,width-272,588,55,42);sprite('img006_ja',18,width-230,588,27,26);sprite('img006_ja',24,width-280,617,76,25);number(balance,0,width-6,592);}
    return;
   }
   if(runtime.receipt&&runtime.endingMap?.[2])sprite('img001_ja',120,...runtime.endingMap);
   const hint=runtime.defeatHint;
   if(r.mode===2&&e.phase===4&&hint?.layout.id>=0){
    sprite('img005',0,...hint.layout.panel);
    if(hint.layout.ready){context.save();context.font=nativeFont(30);context.fillStyle='#fff';context.textAlign='center';context.textBaseline='top';for(const [i,line]of(hint.lines||[]).entries())context.fillText(line,width/2,hint.layout.textY+i*36);context.restore();}
   }
   if(e.phase>1&&r.mode!==2){
    const xp=runtime.receipt?.rewards.filter(v=>v.source==='experience').reduce((n,v)=>n+v.amount,0)||0,points=(dojo||runtime.rules.scoreType===3||runtime.rules.nativeKind===-6)&&!(e.phase===2&&e.frame<0),value=points?r.score:xp;
    const rects=atlas.atlases[name].rects,base=atlas.atlases.img001_ja.rects;
    const digits=String(Math.max(0,value)).split('').map(Number),digitWidth=digits.reduce((n,v)=>n+base[v][2]-1,1);
    const leftCut=points?(runtime.rules.scoreType===3?11:5):1,rightCut=points?4:2;
    const left=rects[leftCut],right=rects[rightCut],start=width/2+e.numberX-(digitWidth+left[2]+right[2]+40)/2;
    sprite(name,leftCut,start,points?324:322);number(value,0,start+left[2]+20+digitWidth,321);sprite(name,rightCut,start+left[2]+40+digitWidth,points?323:324);
    if(points&&e.phase>2&&runtime.receipt?.newRecord){const cut=6+Math.trunc(e.frame/2)%2;sprite(name,cut,width/2-rects[cut][2]/2,300);}
   }
   if(e.ready){
    const b=e.visualButton,buttons=runtime.rules.scoreType===1?'img101_nekoDojo':'img101';sprite(buttons,3,...b);sprite('img006_ja',1,...e.label);if(e.pressed||e.guard)sprite(buttons,e.guard&&Math.trunc(e.guard/2)%2?5:4,...b);
   }
   if(runtime.receipt&&e.phase===8)popup.paint(context,e.popup,atlas,images);
  },
  stop(){popup?.stop();panel.remove();button.remove();},
 };
}
