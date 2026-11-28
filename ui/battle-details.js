import {actorState} from './battle-inspector.js';
import {createStagePainter} from './src/features/stages/native-media.js';

const number=value=>Number(value).toLocaleString('ja-JP');
const remaining=value=>value<0?'∞':number(value);
const counters=[['barrier','バリア'],['shield','悪魔シールド'],['revives','残り蘇生回数'],['burrows','残り潜行回数'],['survive','生き残る']];
const timers=[['stop','停止'],['slow','鈍足'],['weaken','攻撃力低下'],['curse','呪い'],['reviveWait','蘇生待ち']];

export function observedActorChanges(before,after){
 if(!before)return ['観測開始：'+actorState(after)+' / HP '+number(after.hp)];
 const changes=[];
 if(before.action!==after.action||before.retiredFrame!==after.retiredFrame)changes.push(actorState(before)+' → '+actorState(after));
 if(before.hp!==after.hp)changes.push('HP '+number(before.hp)+' → '+number(after.hp));
 for(const [key,label] of counters)if(before[key]!==after[key])changes.push(label+' '+before[key]+' → '+after[key]);
 for(const [key,label] of timers){
  if(before[key]===after[key])continue;
  if(!after[key])changes.push(label+'：終了');
  else if(!before[key]||after[key]>before[key])changes.push(label+'：残り '+after[key]+'F');
 }
 return changes;
}

function fitPose(commands,width,height){
 let left=Infinity,top=Infinity,right=-Infinity,bottom=-Infinity;
 for(const command of commands)for(let i=0;i<command.count*2;i+=2){
  const x=command.points[i],y=command.points[i+1];
  left=Math.min(left,x);right=Math.max(right,x);top=Math.min(top,y);bottom=Math.max(bottom,y);
 }
 if(!Number.isFinite(right-left)||!Number.isFinite(bottom-top))return [];
 const scale=Math.min((width-16)/Math.max(1,right-left),(height-16)/Math.max(1,bottom-top));
 return commands.map(command=>({...command,points:command.points.map((value,i)=>i%2?(value-(top+bottom)/2)*scale+height/2:(value-(left+right)/2)*scale+width/2)}));
}

export function createBattleDetails(root,assets,images,onChange){
 const buttons=[...root.querySelectorAll('[role=tab]:not([hidden])')],panel=id=>root.querySelector('#battle-detail-'+id);
 const actorPanel=panel('actor'),sheet=actorPanel.querySelector('dl'),log=actorPanel.querySelector('ol');
 const heading=actorPanel.querySelector('[data-actor-name]'),hint=actorPanel.querySelector('[data-pose-status]');
 const canvas=actorPanel.querySelector('canvas'),shelf=root.closest('details');
 let tab,selected=null,last=null,lastFrame=null,painter,busy=false,previewAvailable=true,stopped=false;
 const controller=new AbortController(),options={signal:controller.signal};
 function open(id){
  tab=id;
  for(const button of buttons){
   const current=button.dataset.detailTab===id;button.setAttribute('aria-selected',String(current));button.tabIndex=current?0:-1;panel(button.dataset.detailTab).hidden=!current;
  }
  onChange();
 }
 root.addEventListener('click',event=>{const button=event.target.closest('[data-detail-tab]');if(button)open(button.dataset.detailTab);},options);
 root.addEventListener('keydown',event=>{
  const i=buttons.indexOf(event.target);if(i<0)return;
  const next=event.key==='Home'?0:event.key==='End'?buttons.length-1:event.key==='ArrowRight'?(i+1)%buttons.length:event.key==='ArrowLeft'?(i+buttons.length-1)%buttons.length:-1;
  if(next>=0){event.preventDefault();buttons[next].focus();open(buttons[next].dataset.detailTab);}
 },options);
 shelf?.addEventListener('toggle',onChange,options);
 function reset(){
  last=null;lastFrame=null;log.replaceChildren();sheet.replaceChildren();canvas.hidden=true;
  heading.textContent=selected==null?'サイドバーから個体を選択':'個体 #'+selected;
  hint.textContent=selected==null?'戦闘中の姿勢を表示します':'読み込み中';
 }
 open(buttons[0].dataset.detailTab);reset();
 return {
  setAssets(value){assets=value;},
  select(id){if(selected!==id){selected=id;reset();}if(shelf)shelf.open=true;open('actor');},
  focus(){return tab==='actor'&&(!shelf||shelf.open)?selected:null;},
  update(actor,frame,range,scene){
   if(tab!=='actor'||shelf&&!shelf.open||actor?.id!==selected||!actor)return;
   const profile=assets.profiles[actor.profile];
   if(!last||lastFrame!==actor.lastFrame||actor.retiredFrame!==last.retiredFrame||actor.action!==last.action||actor.hp!==last.hp){
    const changes=observedActorChanges(last,actor);
    const span=lastFrame!=null&&frame-lastFrame>1?(lastFrame+1)+'–'+frame:frame;
    if(changes.length){
     const entry=document.createElement('li');entry.textContent=span+'F　'+changes.join(' / ');log.prepend(entry);if(log.childElementCount>80)log.lastElementChild.remove();
    }
    last=actor;lastFrame=frame;
    heading.textContent='#'+actor.id+' '+(profile?.name||'個体')+' / '+actorState(actor);
    const values=[
     ['HP',number(actor.hp)+' / '+number(actor.maximum)],['座標',actor.x/10+' / '+actor.y/10],['レイヤー',actor.layer],
     ['行動 / アニメF',actor.action+' / '+actor.animation],['陣営 / 枠 / 通番',actor.side+' / '+actor.slot+' / '+actor.serial],
     ['生成 / 最終更新',actor.bornFrame+'F / '+actor.lastFrame+'F'],['死亡 / 蘇生',actor.deaths+' / '+actor.revivals],
     ...(actor.barrierMax?[['バリア',number(actor.barrier)+' / '+number(actor.barrierMax)]]:[]),
     ...(actor.shieldMax?[['悪魔シールド',number(actor.shield)+' / '+number(actor.shieldMax)]]:[]),
     ...(actor.revivesMax?[['残り蘇生回数',remaining(actor.revives)+' / '+remaining(actor.revivesMax)]]:[]),
     ...(actor.burrowsMax?[['残り潜行回数',remaining(actor.burrows)+' / '+remaining(actor.burrowsMax)]]:[]),
     ...(actor.survive?[['生き残る',actor.survive===1?'発動':'使用済']]:[]),
     ...timers.filter(([key])=>actor[key]>0).map(([key,label])=>[label,actor[key]+'F'+(key==='weaken'?' / '+actor.weakenRate+'%':'')]),
    ];
    if(actor.retiredFrame>=0)values.push(['退場',actor.retiredFrame+'F']);
    if(actor.deathFrame>=0)values.push(['直近のHP0',actor.deathFrame+'F']);
    for(const source of actor.attackers||[]){
     const name=source.kind===1?'#'+source.actorId+' '+(assets.profiles[source.profile]?.name||'個体'):source.kind===2?'にゃんこ砲':source.kind===3?'スニャイパー':'その他';
     values.push(['HP0時の攻撃元',name+'（予約 '+number(source.reserved)+'）']);
    }
    for(const [i,[key,value]] of values.entries()){
     let term=sheet.children[i*2];if(!term){term=document.createElement('dt');sheet.append(term,document.createElement('dd'));}
     term.textContent=key;term.nextElementSibling.textContent=value;
    }
    while(sheet.childElementCount>values.length*2)sheet.lastElementChild.remove();
   }
   if(!range||!scene||!previewAvailable){canvas.hidden=true;hint.textContent=actor.retiredFrame>=0?'退場済み':previewAvailable?'このフレームには描画がありません':'プレビューを初期化できません';return;}
   if(busy||stopped)return;
   try{painter??=createStagePainter(canvas,onChange,images,{transparent:true});}catch{previewAvailable=false;canvas.hidden=true;hint.textContent='プレビューを初期化できません';return;}
   canvas.hidden=false;hint.textContent='行動 '+actor.action+' / アニメ '+actor.animation+'F';
   const commands=fitPose(scene.commands.slice(...range),canvas.width,canvas.height);
   busy=true;painter.paint({commands,textures:scene.textures,layout:{viewport_width:canvas.width}}).catch(()=>{previewAvailable=false;canvas.hidden=true;hint.textContent='プレビューを描画できません';}).finally(()=>{busy=false;});
  },
  stop(){stopped=true;controller.abort();painter?.dispose();reset();},
 };
}
