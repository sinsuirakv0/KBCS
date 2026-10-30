import {mountAppearance,openSiteSettings} from './src/shared/browser/game-settings.js';
import {battleKeyActions,readBattleKeys,saveBattleKeys,defaultBattleKeys,normalizeBattleKeys,keyLabel} from './keyboard.js';
import {observeUpdates,downloadUpdate,checkUpdates,applyUpdate} from './updates.js';
import {copyText} from './src/shared/browser/clipboard.js';
const element=id=>document.getElementById(id),bytes=value=>value==null?'—':new Intl.NumberFormat('ja',{maximumFractionDigits:1}).format(value/1024**(value>=2**30?3:value>=2**20?2:1))+(value>=2**30?' GiB':value>=2**20?' MiB':' KiB');
let section='',updates,busy=false,manual=false,statusValue,folder='',entries=[],page=0,listening=null,keys=readBattleKeys(),diagnostics;
async function request(path,body,method='POST'){
 const response=await fetch(path,body===undefined?{}:{method,headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),value=await response.json();if(!response.ok)throw Error(value.error||'処理に失敗しました');return value;
}
function showError(error){element('import-error').hidden=false;element('import-error').textContent=error.message;}
function cards(container,values){container.replaceChildren();for(const [label,value] of values){const node=document.createElement('div');node.className='settings-stat';const name=document.createElement('span'),output=document.createElement('strong');name.textContent=label;output.textContent=value??'—';node.append(name,output);container.append(node);}}
function selectSection(){
 listening=null;const next=location.hash.slice(1)||'appearance';section=['appearance','data','keyboard','system'].includes(next)?next:'appearance';
 for(const node of document.querySelectorAll('[data-settings-section]'))node.hidden=node.dataset.settingsSection!==section;
 for(const link of element('settings-navigation').querySelectorAll('a')){if(link.hash==='#'+section)link.setAttribute('aria-current','page');else link.removeAttribute('aria-current');}
 if(section==='data'){void refreshData().catch(showError);void loadFiles(folder).catch(showError);}
 if(section==='system')void refreshSystem().catch(error=>element('system-status').textContent=error.message);
}
async function confirmAction(title,message){
 return new Promise(resolve=>{const dialog=document.createElement('dialog');dialog.className='update-dialog';const heading=document.createElement('h2'),text=document.createElement('p'),actions=document.createElement('div'),no=document.createElement('button'),yes=document.createElement('button');heading.textContent=title;text.textContent=message;no.textContent='キャンセル';yes.textContent='実行';actions.className='settings-actions';const finish=value=>{dialog.close();dialog.remove();resolve(value);};no.onclick=()=>finish(false);yes.onclick=()=>finish(true);dialog.addEventListener('cancel',event=>{event.preventDefault();finish(false);});actions.append(no,yes);dialog.append(heading,text,actions);document.body.append(dialog);dialog.showModal();});
}
mountAppearance(element('appearance-settings'));
element('settings-display').onclick=()=>openSiteSettings('database');element('settings-transfer').onclick=()=>openSiteSettings('transfer');
async function refreshStatus(){
 statusValue=await request('/api/status');busy=statusValue.busy;
 element('settings-data-version').textContent=statusValue.metadata?statusValue.metadata.region.toUpperCase()+' データv'+statusValue.metadata.version:'データ未導入';
 element('settings-task').textContent=updates?.busy?updates.message:busy?statusValue.message:'';
 if(!element('asset-source').value)element('asset-source').value=statusValue.source;
 element('storage-state').textContent=statusValue.dataDir;
 const useUpdate=updates?.job&&!manual;
 element('import-state').textContent=useUpdate?updates.message:statusValue.message;
 const error=useUpdate?updates.error:statusValue.error;element('import-error').hidden=!error;element('import-error').textContent=error||'';
 for(const id of ['import-button','manual-import-button','data-rebuild','data-verify','data-repair']){const node=element(id);if(node)node.disabled=busy||!!updates?.busy;}
 if(statusValue.verification){element('verification-output').hidden=false;element('verification-output').textContent=JSON.stringify(statusValue.verification,null,2);}
}
async function refreshData(){
 const value=await request('/api/data/summary');
 cards(element('database-summary'),[['保存先の空き容量',bytes(value.storage?.available)],['キャラ',value.counts.unit],['形態',value.counts.form],['敵キャラ',value.counts.enemy],['ステージ',value.counts.stage_entry],['素材索引',value.counts.asset_reference],['変換器',(value.metadata?.importer_version??'未導入')+' → '+value.importerVersion]]);
 element('database-metadata').textContent=JSON.stringify({database:value.database,metadata:value.metadata,error:value.databaseError},null,2);
 await refreshStatus();
}
element('import-form').onsubmit=event=>{event.preventDefault();manual=false;void downloadUpdate('data').catch(showError);};
element('manual-import-form').onsubmit=event=>{event.preventDefault();manual=true;void request('/api/import',{source:element('asset-source').value}).then(refreshStatus).catch(showError);};
element('update-check').onclick=()=>checkUpdates().catch(showError);element('app-update').onclick=()=>downloadUpdate('app').catch(showError);element('app-apply').onclick=()=>applyUpdate().catch(showError);
element('data-verify').onclick=()=>{manual=true;return request('/api/data/verify',{}).then(refreshStatus).catch(showError);};
element('data-rebuild').onclick=async()=>{try{
 if(!await confirmAction('DBを作り直します','保存済みの原本から、新しいDBを生成して切り替えます。編成・持ち物は保持します。'))return;
 manual=true;await refreshStatus();const metadata=statusValue.metadata;if(!metadata)throw Error('先にデータ取得・更新を実行してください');
 const source=metadata.release_tag?statusValue.assetDir+'/releases/'+metadata.release_tag:metadata.origin;
 await request('/api/import',{source,rebuild:true});await refreshStatus();
 }catch(error){showError(error);}};
const repair=document.createElement('button');repair.id='data-repair';repair.textContent='原本を再取得・修復';repair.onclick=async()=>{if(await confirmAction('原本を再取得します','全ZIPを再ダウンロードし、原本とDBを作り直します。通信量が大きいため、通常のDB再生成で直らない場合に使用してください。')){manual=false;downloadUpdate('repair').catch(showError);}};element('data-rebuild').after(repair);
function renderFiles(){
 const list=element('storage-files');list.replaceChildren();
 for(const entry of entries.slice(page*150,(page+1)*150)){
  const row=document.createElement('tr');for(const value of [entry.name,entry.directory?'フォルダ':'ファイル',bytes(entry.size),entry.modified?new Date(entry.modified*1000).toLocaleString():'—']){const cell=document.createElement('td');cell.textContent=value;row.append(cell);}
  const actions=document.createElement('td'),open=document.createElement('button');open.textContent=entry.directory?'開く':'閲覧';open.onclick=()=>{if(entry.directory)loadFiles(entry.path).catch(showError);else request('/api/storage?'+new URLSearchParams({path:entry.path,inspect:1})).then(value=>{element('storage-preview').hidden=false;element('storage-preview').textContent=JSON.stringify(value,null,2);}).catch(showError);};actions.append(open);
  if(entry.deletable){const remove=document.createElement('button');remove.textContent='削除';remove.disabled=busy||!!updates?.busy;remove.onclick=async()=>{if(await confirmAction('保存データを削除します',entry.path+' を削除します。この操作は元に戻せません。')){try{await request('/api/storage?'+new URLSearchParams({path:entry.path}),{},'DELETE');await loadFiles(folder);}catch(error){showError(error);}}};actions.append(remove);}
  row.append(actions);list.append(row);
 }
 element('storage-path').textContent=(folder||'データ保存先')+' / '+entries.length+'件';previous.disabled=page===0;next.disabled=(page+1)*150>=entries.length;
}
const previous=document.createElement('button'),next=document.createElement('button');previous.textContent='前の150件';next.textContent='次の150件';previous.onclick=()=>{page--;renderFiles();};next.onclick=()=>{page++;renderFiles();};element('storage-refresh').after(previous,next);
async function loadFiles(path){const value=await request('/api/storage?'+new URLSearchParams({path}));folder=path;entries=value.entries;page=0;renderFiles();}
element('storage-parent').onclick=()=>loadFiles(folder.split('/').slice(0,-1).join('/')).catch(showError);element('storage-refresh').onclick=()=>loadFiles(folder).catch(showError);
function renderKeys(){
 const list=element('keyboard-bindings');list.replaceChildren();let group;
 for(const action of battleKeyActions){if(action.group!==group){group=action.group;const heading=document.createElement('h2');heading.textContent=group;heading.className='keyboard-group';list.append(heading);}
  const row=document.createElement('div');row.className='keyboard-row';const label=document.createElement('span'),key=document.createElement('button'),clear=document.createElement('button');label.textContent=action.label;key.textContent=keyLabel(keys[action.id]);key.className='keyboard-key';key.dataset.action=action.id;key.setAttribute('aria-label',action.label+'：'+key.textContent+' を変更');key.onclick=()=>{listening=action.id;for(const button of list.querySelectorAll('[data-action]'))button.dataset.listening=String(button===key);element('keyboard-status').textContent='割り当てるキーを押してください。';};clear.textContent='解除';clear.onclick=()=>{keys=saveBattleKeys({...keys,[action.id]:''});listening=null;renderKeys();};row.append(label,key,clear);list.append(row);
 }
}
document.addEventListener('keydown',event=>{
 if(!listening)return;event.preventDefault();event.stopPropagation();if(event.repeat||event.isComposing||event.metaKey||event.altKey||event.ctrlKey)return;
 if(normalizeBattleKeys({[listening]:event.code})[listening]!==event.code){element('keyboard-status').textContent='このキーは割り当てできません。';return;}
 const conflict=battleKeyActions.find(v=>v.id!==listening&&keys[v.id]===event.code);if(conflict){element('keyboard-status').textContent=conflict.label+' に割り当て済みです。先に解除してください。';return;}
 try{keys=saveBattleKeys({...keys,[listening]:event.code});listening=null;renderKeys();element('keyboard-status').textContent='保存しました';}catch(error){element('keyboard-status').textContent=error.message;}
},true);
const cancelKey=document.createElement('button');cancelKey.textContent='キー入力を中止';cancelKey.onclick=()=>{listening=null;renderKeys();element('keyboard-status').textContent='中止しました';};element('keyboard-reset').after(cancelKey);
element('keyboard-reset').onclick=()=>{keys=saveBattleKeys(defaultBattleKeys);listening=null;renderKeys();element('keyboard-status').textContent='初期配置に戻しました';};renderKeys();
let gpuInfo;
async function refreshSystem(){
 if(gpuInfo===undefined){const gl=document.createElement('canvas').getContext('webgl');if(gl){const debug=gl.getExtension('WEBGL_debug_renderer_info');gpuInfo={vendor:gl.getParameter(debug?.UNMASKED_VENDOR_WEBGL??gl.VENDOR),renderer:gl.getParameter(debug?.UNMASKED_RENDERER_WEBGL??gl.RENDERER),version:gl.getParameter(gl.VERSION)};gl.getExtension('WEBGL_lose_context')?.loseContext();}else gpuInfo=null;}

 diagnostics=await request('/api/system');
 diagnostics.browser={userAgent:navigator.userAgent,language:navigator.language,logicalProcessors:navigator.hardwareConcurrency,memoryGiB:navigator.deviceMemory,viewport:[innerWidth,innerHeight],pixelRatio:devicePixelRatio,jsHeap:performance.memory?{used:performance.memory.usedJSHeapSize,total:performance.memory.totalJSHeapSize,limit:performance.memory.jsHeapSizeLimit}:null,gpu:gpuInfo};
 const runtime=diagnostics.runtime;
 cards(element('system-overview'),[['保存先の空き容量',bytes(diagnostics.data.storage?.available)],['KBCS','v'+diagnostics.version],['OS / CPU',diagnostics.platform.os+' / '+diagnostics.platform.architecture],['稼働時間',Math.floor(diagnostics.uptimeSeconds/60)+'分'],['CPU使用率',runtime.cpuPercent==null?'計測中':runtime.cpuPercent.toFixed(1)+'%'],['メモリ使用',bytes((runtime.memoryTotal!=null&&runtime.memoryAvailable!=null)?runtime.memoryTotal-runtime.memoryAvailable:null)+' / '+bytes(runtime.memoryTotal)],['KBCS本体メモリ（WebView除外）',bytes(runtime.hostWorkingSet)],['戦闘セッション',diagnostics.activeBattles],['ABI / ルール版',diagnostics.abi+' / '+diagnostics.ruleset]]);
 element('system-details').textContent=JSON.stringify(diagnostics,null,2);element('settings-version').textContent='KBCS v'+diagnostics.version;
}
element('system-copy').onclick=()=>{if(!diagnostics)return;return copyText(JSON.stringify(diagnostics,null,2)).then(()=>element('system-status').textContent='コピーしました').catch(()=>element('system-status').textContent='コピーできませんでした');};
element('system-export').onclick=()=>{if(!diagnostics)return;const url=URL.createObjectURL(new Blob([JSON.stringify(diagnostics,null,2)],{type:'application/json'})),link=document.createElement('a');link.href=url;link.download='KBCS-system.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
observeUpdates(value=>{
 const completed=updates?.busy&&!value.busy;updates=value;if(value.busy)manual=false;
 element('settings-version').textContent='KBCS v'+value.currentVersion;
 element('update-check').disabled=value.checking||value.busy;
 element('update-check-state').textContent=value.checking?'確認中…':value.dataError||value.appError?'更新確認に失敗しました':'確認済み';
 element('data-release-state').textContent=value.data?'統合データ v'+value.data.version+' / '+(value.data.rebuildRequired?'DBの再生成が必要':value.data.available?'ダウンロード可能':'導入済み'):value.dataError||'配布情報を確認しています';
 element('app-release-state').textContent='現在 v'+value.currentVersion+(value.app?.available?' / v'+value.app.version+' が利用可能':'');
 element('app-update').disabled=value.busy||!value.app?.available;element('app-apply').hidden=!value.app?.ready||!value.desktop;element('app-apply').disabled=value.busy;
 if(completed)void refreshData().catch(showError);else void refreshStatus().catch(showError);
});
window.addEventListener('hashchange',selectSection);selectSection();void refreshStatus().catch(showError);
const timer=setInterval(()=>{if(section==='system')refreshSystem().catch(error=>element('system-status').textContent=error.message);if(busy||updates?.busy)refreshStatus().catch(showError);},1500);window.addEventListener('pagehide',()=>clearInterval(timer),{once:true});
