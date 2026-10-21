export function pageNumbers(total,current) {
  total=Math.max(1,Math.trunc(total)||1);current=Math.max(1,Math.min(total,current));
  if(total<=8)return Array.from({length:total},(_,index)=>index+1);
  const pages=new Set([1,2,total-1,total]);
  const start=current<=3?1:current>=total-2?total-3:current-1;
  const end=current<=3?4:current>=total-2?total:current+1;
  for(let page=start;page<=end;page++)pages.add(page);
  const result=[];
  for(const page of [...pages].sort((a,b)=>a-b)) {
    const previous=result.at(-1);
    if(previous&&page-previous===2)result.push(previous+1);
    else if(previous&&page-previous>2)result.push(null);
    result.push(page);
  }
  return result;
}

export function createPagination(root,onChange) {
  root.setAttribute('role','navigation');root.setAttribute('aria-label','検索結果のページ');
  root.innerHTML='<span class="db-pagination-edge"><button type="button" data-step="first" aria-label="最初のページへ">最初</button><button type="button" data-step="previous" aria-label="前のページへ">前</button></span><span class="db-page-numbers"></span><span class="db-pagination-edge"><button type="button" data-step="next" aria-label="次のページへ">次</button><button type="button" data-step="last" aria-label="最後のページへ">最後</button></span><span class="db-page-status visually-hidden" aria-live="polite"></span>';
  let current=1,total=1;
  for(const button of root.querySelectorAll('[data-step]'))button.disabled=true;
  root.addEventListener('click',event=>{
    const button=event.target.closest('button');if(!button||button.disabled)return;
    const page=button.dataset.page?Number(button.dataset.page):({first:1,previous:current-1,next:current+1,last:total})[button.dataset.step];
    onChange(page);root.querySelector('[data-page="'+page+'"]')?.focus({preventScroll:true});
  });
  return {update(page,count){
    current=page;total=count;
    root.querySelector('.db-page-numbers').innerHTML=pageNumbers(total,current).map(value=>value===null?'<span aria-hidden="true">…</span>':'<button type="button" data-page="'+value+'" aria-label="'+value+'ページへ"'+(value===current?' aria-current="page"':'')+'>'+value+'</button>').join('');
    for(const button of root.querySelectorAll('[data-step]'))button.disabled=['first','previous'].includes(button.dataset.step)?current<=1:current>=total;
    root.querySelector('.db-page-status').textContent=current+' / '+total;
  }};
}
