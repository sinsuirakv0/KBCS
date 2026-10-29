const element=id=>document.getElementById(id);
import {observeUpdates,downloadUpdate,checkUpdates,applyUpdate} from './updates.js';
let running=false,updates,manual=false;
async function status(){
  try{
    const response=await fetch('/api/status');const value=await response.json();
    const metadata=value.metadata;
    element('data-state').textContent=metadata?metadata.region.toUpperCase()+' データv'+metadata.version:'データ未導入';
    if(!element('asset-source').value)element('asset-source').value=value.source;
    element('storage-state').textContent='保存先: '+value.dataDir;
    element('import-button').disabled=value.busy||!!updates?.busy;
    element('manual-import-button').disabled=value.busy||!!updates?.busy;
    const useUpdate=updates?.job&&!manual;
    element('import-state').textContent=useUpdate?updates.message:value.message;
    const error=useUpdate?updates.error:value.error;
    element('import-error').hidden=!error;element('import-error').textContent=error||'';
    running=value.busy;
  }catch(error){element('import-error').hidden=false;element('import-error').textContent=error.message;}
}
async function startImport(source){
  manual=true;
  element('import-button').disabled=true;element('manual-import-button').disabled=true;
  try{const response=await fetch('/api/import',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({source})});const value=await response.json();if(!response.ok)throw Error(value.error);running=true;await status();}
  catch(error){element('import-error').hidden=false;element('import-error').textContent=error.message;element('import-button').disabled=false;element('manual-import-button').disabled=false;}
}
element('import-form').addEventListener('submit',async event=>{event.preventDefault();manual=false;try{await downloadUpdate('data');}catch(error){showError(error);}});
element('manual-import-form').addEventListener('submit',async event=>{event.preventDefault();await startImport(element('asset-source').value);});
function showError(error){element('import-error').hidden=false;element('import-error').textContent=error.message;}
element('update-check').onclick=()=>checkUpdates().catch(showError);
element('app-update').onclick=()=>downloadUpdate('app').catch(showError);
element('app-apply').onclick=()=>applyUpdate().catch(showError);
observeUpdates(value=>{
  const completed=updates?.busy&&!value.busy;updates=value;
  if(value.busy)manual=false;
  element('update-check').disabled=value.checking||value.busy;
  element('update-check-state').textContent=value.checking?'確認中…':value.dataError||value.appError?'更新確認に失敗しました。再試行できます。':'確認済み';
  element('data-release-state').textContent=value.data?'統合データ v'+value.data.version+' / '+(value.data.available?'ダウンロード可能':'導入済み'):value.dataError||'データの配布情報を確認しています';
  element('app-release-state').textContent='現在 v'+value.currentVersion+(value.app?.available?' / v'+value.app.version+' が利用可能':'');
  element('app-update').disabled=value.busy||!value.app?.available;
  element('app-apply').hidden=!value.app?.ready||!value.desktop;
  element('app-apply').disabled=value.busy;
  element('import-button').disabled=value.busy||running;
  element('manual-import-button').disabled=value.busy||running;
  if(value.job&&!manual){element('import-state').textContent=value.message;element('import-error').hidden=!value.error;element('import-error').textContent=value.error||'';}
  else if(value.error)showError(Error(value.error));
  if(completed)void status();
});
if(location.hash==='#data-management')element('data-management').open=true;
await status();setInterval(()=>{if(running)status();},1000);
