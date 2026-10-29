// 起動通知の拒否・受諾・初回取得と、ホームの再取得/再起動要求だけを検証する。
import assert from 'node:assert/strict';
class Element {
  constructor(tag,owner){this.tag=tag;this.owner=owner;this.children=[];this.handlers={};this.textContent='';}
  append(...children){this.children.push(...children);}
  replaceChildren(...children){this.children=children;}
  setAttribute(){}
  removeAttribute(){}
  addEventListener(event,handler){this.handlers[event]=handler;}
  showModal(){this.owner.dialogs.push(this);}
  close(){this.handlers.close?.();}
  remove(){this.owner.dialogs=this.owner.dialogs.filter(dialog=>dialog!==this);}
}
const tick=()=>new Promise(resolve=>setImmediate(resolve));
async function settle(check){for(let i=0;i<100;i++){await tick();if(check())return;}assert.fail('更新通知が完了しませんでした');}
const originalFetch=globalThis.fetch;
try{
  for(const accept of [false,true]){
    const document={dialogs:[],createElement(tag){return new Element(tag,this);},createTextNode(text){return {textContent:text};},getElementById(){return null;}};
    document.body=new Element('body',document);globalThis.document=document;globalThis.window={};
    const value={checking:false,checked:true,startupPending:true,busy:false,desktop:true,currentVersion:'0.1.35',data:{version:'15.7.4',size:900000000,available:true,missing:false},app:{available:false}};
    const calls=[];
    globalThis.fetch=async(url,options={})=>{
      calls.push([url,options]);
      if(url.endsWith('/startup'))return {ok:true,json:async()=>{value.startupPending=false;return {claimed:true};}};
      if(url.endsWith('/download')){value.data.available=false;return {ok:true,json:async()=>({accepted:true})};}
      return {ok:true,json:async()=>structuredClone(value)};
    };
    const updates=await import('../updates.js?accept='+accept);updates.initializeUpdates();
    await settle(()=>document.dialogs.length===1);
    const actions=document.dialogs[0].children.at(-1);
    actions.children[accept?1:0].onclick();
    await settle(()=>document.dialogs.length===0&&(!accept||calls.some(([url])=>url.endsWith('/download'))));
    assert.equal(calls.filter(([url])=>url.endsWith('/download')).length,accept?1:0);
    if(!accept)assert.ok(document.body.children.some(node=>node.id==='update-notice'));
    await updates.downloadUpdate('data');
    assert.equal(JSON.parse(calls.findLast(([url])=>url.endsWith('/download'))[1].body).kind,'data');
    let restarted=false;window.ipc={postMessage(value){assert.equal(value,'kbcs:restart-for-update');restarted=true;}};
    await updates.applyUpdate();assert.ok(restarted);
  }
  const document={dialogs:[],createElement(tag){return new Element(tag,this);},createTextNode(text){return {textContent:text};},getElementById(){return null;}};
  document.body=new Element('body',document);globalThis.document=document;globalThis.window={};
  const first={checking:false,checked:true,startupPending:true,busy:true,job:'data',message:'ZIP 1/10',data:{missing:true,available:true},app:{available:false}};
  let downloads=0;
  globalThis.fetch=async(url)=>{
    if(url.endsWith('/download'))downloads++;
    if(url.endsWith('/startup')){first.startupPending=false;return {ok:true,json:async()=>({claimed:true})};}
    return {ok:true,json:async()=>structuredClone(first)};
  };
  const updates=await import('../updates.js?first-run');updates.initializeUpdates();
  await settle(()=>document.dialogs.length===1);
  assert.equal(downloads,0);
  assert.equal(document.dialogs[0].children[0].textContent,'初回データをダウンロードしています');
  first.busy=false;await updates.checkUpdates();
  assert.equal(document.dialogs[0].children[0].textContent,'データの導入が完了しました');
  document.dialogs[0].children.at(-1).onclick();
}finally{globalThis.fetch=originalFetch;delete globalThis.document;delete globalThis.window;}
console.log('startup consent, decline notice, manual download and restart passed');
