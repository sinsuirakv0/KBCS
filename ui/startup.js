let screen,started=false,unsubscribe,minimum,loading=false;
function mount(){
 if(screen)return screen;
 screen=document.createElement('section');screen.className='startup-screen';screen.setAttribute('aria-label','KBCSの読み込み');
 screen.innerHTML='<div class="startup-art"><img src="/images/brand/loading-center.png" alt="KBCS Kenkou Battle Cats Simulator"></div><div class="startup-progress"><h1>KBCSを起動しています</h1><p role="status" aria-live="polite">データを確認しています…</p><progress aria-label="読み込み中"></progress><a href="/pages/settings/#data" hidden>データ管理を開く</a></div>';
 document.body.append(screen);document.documentElement?.removeAttribute('data-kbcs-starting');
 return screen;
}
function raise(){
 const node=screen;if(!node||node.classList.contains('startup-raised'))return;
 node.classList.add('startup-raised');
 const top=new Image();top.src='/images/brand/loading-top.png';
 Promise.all([top.decode(),new Promise(resolve=>setTimeout(resolve,700))]).then(()=>{if(screen===node){node.querySelector('.startup-art img').src=top.src;node.classList.add('startup-top');}}).catch(()=>{});
}
function close(){if(!screen)return;const node=screen;screen=null;node.classList.add('startup-done');setTimeout(()=>node.remove(),220);}
export function showStartupProgress(title,message,error=false){
 const node=mount();raise();node.querySelector('h1').textContent=title;node.querySelector('p').textContent=message;
 node.querySelector('progress').hidden=error;node.querySelector('a').hidden=!error;
}
export function initializeStartup(observeUpdates){
 if(started)return;started=true;
 let first=true;try{first=!sessionStorage.getItem('kbcs:startup-seen');sessionStorage.setItem('kbcs:startup-seen','1');}catch{}
 if(first){mount();minimum=performance.now()+1200;setTimeout(raise,350);}
 unsubscribe=observeUpdates(value=>{
  loading=value.busy&&['data','repair'].includes(value.job);
  if(loading){
   showStartupProgress('データを準備しています',value.message||'原本を取得しています…');
  }else if(screen&&value.error&&['data','repair'].includes(value.job)){
   showStartupProgress('データの取得に失敗しました',value.error,true);
  }else if(screen&&value.localDataPresent===false&&value.dataError){
   showStartupProgress('データの取得に失敗しました',value.dataError,true);
  }else if(screen&&(value.checked||value.localDataPresent||!value.desktop)){
   setTimeout(()=>{if(!loading&&!screen?.querySelector('a:not([hidden])'))close();},Math.max(0,(minimum||0)-performance.now()));
  }
 });
 window.addEventListener('pagehide',()=>unsubscribe?.(),{once:true});
}
