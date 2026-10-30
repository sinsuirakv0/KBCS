const state=document.getElementById('data-state');
if(location.hash==='#data-management')location.replace('/pages/settings/#data');
try{const response=await fetch('/api/status'),value=await response.json();state.textContent=value.metadata?'JP データv'+value.metadata.version:'データ未導入';}catch(error){state.textContent=error.message;}
