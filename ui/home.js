const element=id=>document.getElementById(id);
let running=false,updateSource;
async function status(){
  try{
    const response=await fetch('/api/status');const value=await response.json();
    const metadata=value.metadata;
    element('data-state').textContent=metadata?metadata.region.toUpperCase()+' データv'+metadata.version:'データ未導入';
    if(!element('asset-source').value)element('asset-source').value=value.source;
    updateSource=value.updateSource;
    element('storage-state').textContent='保存先: '+value.dataDir;
    element('import-button').disabled=value.busy;
    element('manual-import-button').disabled=value.busy;
    element('import-state').textContent=value.message;
    element('import-error').hidden=!value.error;element('import-error').textContent=value.error||'';
    running=value.busy;
  }catch(error){element('import-error').hidden=false;element('import-error').textContent=error.message;}
}
async function startImport(source){
  element('import-button').disabled=true;element('manual-import-button').disabled=true;
  try{const response=await fetch('/api/import',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({source})});const value=await response.json();if(!response.ok)throw Error(value.error);running=true;await status();}
  catch(error){element('import-error').hidden=false;element('import-error').textContent=error.message;element('import-button').disabled=false;element('manual-import-button').disabled=false;}
}
element('import-form').addEventListener('submit',async event=>{event.preventDefault();if(updateSource)await startImport(updateSource);});
element('manual-import-form').addEventListener('submit',async event=>{event.preventDefault();await startImport(element('asset-source').value);});
await status();setInterval(()=>{if(running)status();},1000);
