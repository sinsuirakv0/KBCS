const isDetail=page=>page.endsWith('-detail');
const stateKey=(page,route)=>'kbcs:view:'+page+(isDetail(page)?':'+(route.get('id')||route.get('map')||'0'):'');

export function writePageParams(page,params,search=location.search){
  try{sessionStorage.setItem(stateKey(page,new URLSearchParams(search)),params.toString());}catch{}
}

export function readPageParams(page){
  const route=new URLSearchParams(location.search);
  let params=new URLSearchParams();
  try{params=new URLSearchParams(sessionStorage.getItem(stateKey(page,route))||'');}catch{}
  const navigation=new URLSearchParams();
  if(page==='stage-detail'&&route.has('crown'))params.set('crown',route.get('crown'));
  if(isDetail(page))for(const key of (page==='stage-detail'?['map','stage']:['id','form']))if(route.has(key)){
    params.set(key,route.get(key));navigation.set(key,route.get(key));
  }
  history.replaceState(null,'',location.pathname+(navigation.size?'?'+navigation:'')+location.hash);
  return params;
}

export function clearPageParams(page){
  try{sessionStorage.removeItem(stateKey(page,new URLSearchParams(location.search)));}catch{}
}

export function bindDetailNavigation(page,path,getParams){
  const save=event=>{
    const link=event.target.closest('a[href]');
    if(!link)return;
    const target=new URL(link.href,location.origin);
    if(target.origin===location.origin&&target.pathname===path)writePageParams(page,getParams(target,link),target.search);
  };
  document.addEventListener('click',save);
  document.addEventListener('auxclick',save);
}
