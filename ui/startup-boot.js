// moduleとページ本文より前に実行し、初回のホームの描画を止める。
(()=>{
 let first=true;try{first=!sessionStorage.getItem('kbcs:startup-seen');}catch{}
 if(!first)return;
 document.documentElement.setAttribute('data-kbcs-starting','');
 const style=document.createElement('style');
 style.textContent='html[data-kbcs-starting]{background:#0b1c3f!important}html[data-kbcs-starting] body{visibility:hidden}html[data-kbcs-starting]::before{content:"";position:fixed;inset:0;z-index:2147483647;background:#0b1c3f url(/images/brand/loading-center.png) center / min(100vw,160vh) auto no-repeat}';
 document.head.append(style);
})();
