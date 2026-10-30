import {showStartupProgress} from './startup.js';
let state=null,timer,started=false,pendingStartup=false,presenting=false;
const listeners=new Set();
async function request(path,body){
  const response=await fetch('/api/updates'+path,body===undefined?{}:{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
  const value=await response.json();if(!response.ok)throw Error(value.error||'更新処理に失敗しました');return value;
}
export function observeUpdates(listener){listeners.add(listener);if(state)listener(state);return()=>listeners.delete(listener);}
export async function downloadUpdate(kind){await request('/download',{kind});await refresh();}
export async function checkUpdates(){await request('/check',{});await refresh();}
export async function applyUpdate(){
  if(!window.ipc?.postMessage)throw Error('再起動して更新はKBCSアプリで実行してください');
  await request('/apply',{});window.ipc.postMessage('kbcs:restart-for-update');
}
function notice(message){
  let node=document.getElementById('update-notice');
  if(!node){node=document.createElement('div');node.id='update-notice';node.className='update-notice';node.setAttribute('role','status');document.body.append(node);}
  node.replaceChildren(document.createTextNode(message+' '));
  const link=document.createElement('a');link.href='/pages/settings/#data';link.textContent='データ管理';node.append(link);
  const close=document.createElement('button');close.type='button';close.textContent='×';close.setAttribute('aria-label','閉じる');close.onclick=()=>node.remove();node.append(close);
}
function ask(title,message,positive='ダウンロード',negative='いいえ'){
  return new Promise(resolve=>{
    const dialog=document.createElement('dialog');dialog.className='update-dialog';
    const heading=document.createElement('h2');heading.textContent=title;
    const text=document.createElement('p');text.textContent=message;
    const actions=document.createElement('div');actions.className='update-actions';
    const no=document.createElement('button');no.type='button';no.textContent=negative;
    const yes=document.createElement('button');yes.type='button';yes.textContent=positive;
    const finish=value=>{dialog.close();dialog.remove();resolve(value);};
    no.onclick=()=>finish(false);yes.onclick=()=>finish(true);
    dialog.addEventListener('cancel',event=>{event.preventDefault();finish(false);});
    actions.append(no,yes);dialog.append(heading,text,actions);document.body.append(dialog);dialog.showModal();
  });
}
function progressDialog(){showStartupProgress('初回データを準備しています',state?.message||'原本をダウンロードしています…');}
async function startup(){
  if(presenting||!pendingStartup||!state?.checked)return;
  presenting=true;pendingStartup=false;
  try{
    if(state.data?.missing&&state.busy&&state.job==='data')progressDialog();
    else if(state.data?.available&&!state.busy){
      const size=(state.data.size/1048576).toFixed(0);
      const rebuild=state.data.rebuildRequired&&state.data.localTag===state.data.tag;
      if(await ask(rebuild?'データベースの更新が必要です':'最新のデータをダウンロードする必要があります！',rebuild?'保存済みの原本を確認し、新しい変換器でDBを作り直します。更新しますか？':'データ v'+state.data.version+' が利用可能です（全ZIP 約'+size+' MB）。ダウンロードしますか？',rebuild?'更新する':'ダウンロード'))await downloadUpdate('data');
      else notice('データはホームの「設定 → データ管理」からダウンロードできます。');
    }else if(state.dataError)notice('データの更新確認ができませんでした。ホームの「設定 → データ管理」から再試行できます。');
    if(state.app?.available){
      // データの初回取得と本体更新を同時に走らせない。
      while(state.busy)await new Promise(resolve=>setTimeout(resolve,1000));
      if(await ask('KBCS v'+state.app.version+' が利用可能です！','ダウンロードしますか？ 現在のバージョンは v'+state.currentVersion+' です。')){
        await downloadUpdate('app');
        while(state.busy)await new Promise(resolve=>setTimeout(resolve,1000));
        if(state.app?.ready&&state.desktop&&await ask('KBCSの更新を適用できます','再起動して更新しますか？','再起動して更新','後で'))await applyUpdate();
      }
      else notice('KBCS本体はホームの「設定 → データ管理」から更新できます。');
    }
  }catch(error){notice(error.message+'。ホームの「設定 → データ管理」から再試行できます。');}
  finally{presenting=false;}
}
async function refresh(){
  clearTimeout(timer);
  try{
    state=await request('');for(const listener of listeners)listener(state);
    if(state.checked&&state.startupPending){const claim=await request('/startup',{});pendingStartup=claim.claimed;}
    void startup();
  }catch(error){notice('更新状態を取得できませんでした: '+error.message);}
  if(!state||state.checking||state.busy)timer=setTimeout(refresh,1000);
}
export function initializeUpdates(){if(started)return;started=true;void refresh();}
