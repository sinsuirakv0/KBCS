// 外部画像とSVGの実際の色を取り込み、操作ボタンを除いたPNGを保存する。
async function loadImage(src) {
  const image=new Image();image.src=src;await image.decode();return image;
}
async function renderSvgImage(svg,images,zoom=1) {
  const clone=svg.cloneNode(true),originals=[svg,...svg.querySelectorAll('*')],copies=[clone,...clone.querySelectorAll('*')];
  for(const [index,node] of copies.entries()){
    const style=getComputedStyle(originals[index]);
    for(const key of ['fill','stroke','stroke-width','stroke-dasharray','fill-opacity','font-size','font-family','color'])node.style.setProperty(key,style.getPropertyValue(key));
  }
  // SVGの外部画像も埋め込み、PNG化したときに属性画像が欠けないようにする。
  for(const image of clone.querySelectorAll('image')){const data=images.get(image.getAttribute('href'));if(data)image.setAttribute('href',data.url);}
  const bounds=svg.getBoundingClientRect(),rect={width:bounds.width/zoom,height:bounds.height/zoom};clone.setAttribute('width',rect.width);clone.setAttribute('height',rect.height);clone.style.width=rect.width+'px';clone.style.height=rect.height+'px';clone.style.margin='0';
  const url=URL.createObjectURL(new Blob([new XMLSerializer().serializeToString(clone)],{type:'image/svg+xml'}));
  try{const image=await loadImage(url),canvas=document.createElement('canvas');canvas.width=Math.ceil(rect.width*2);canvas.height=Math.ceil(rect.height*2);canvas.getContext('2d').drawImage(image,0,0,canvas.width,canvas.height);return {url:canvas.toDataURL('image/png'),width:rect.width,height:rect.height};}
  finally{URL.revokeObjectURL(url);}
}
export async function saveElementImage(target,filename) {
  if(!target||!target.getClientRects().length)throw Error('保存する表示を開いてください。');
  const {default:html2canvas}=await import('/vendor/html2canvas.js');
  const shell=target.closest('.site-shell'),zoom=shell?Number(getComputedStyle(shell).zoom)||1:1,layoutWidth=shell?.offsetWidth;
  const include=node=>{
    const closed=node.closest('details:not([open])');
    return !node.closest('[data-capture-exclude="'+CSS.escape(target.id)+'"]')&&(!closed||node.closest('summary')?.parentElement===closed);
  };
  const sources=[...new Set([...target.querySelectorAll('img,svg image')].filter(include).map(image=>image.currentSrc||image.getAttribute('href')||image.src).filter(Boolean))];
  const images=new Map(await Promise.all(sources.map(async src=>{
    try{const response=await fetch(src);if(!response.ok)throw Error();const blob=await response.blob();const url=await new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(reader.result);reader.onerror=reject;reader.readAsDataURL(blob);});const image=await loadImage(url);return [src,{url,width:image.naturalWidth,height:image.naturalHeight}];}catch{return [src,null];}
  })));
  const includeSvg=node=>include(node)&&!node.parentElement.closest('svg');
  const charts=await Promise.all([...target.querySelectorAll('svg')].filter(includeSvg).map(svg=>renderSvgImage(svg,images,zoom)));
  const canvas=await html2canvas(target,{scale:2,useCORS:true,backgroundColor:getComputedStyle(document.documentElement).getPropertyValue('--color-bg').trim(),logging:false,ignoreElements:node=>node.tagName==='BUTTON'&&!node.hasAttribute('data-capture-include')||node.getAttribute('data-capture-exclude')===target.id,onclone:document=>{
    const clone=document.getElementById(target.id);
    const shell=clone.closest('.site-shell');if(shell){shell.style.zoom='1';shell.style.width=layoutWidth+'px';}
    // html2canvasが閉じたdetailsの内容を重ねて描くため、保存用の複製で明示的に隠す。
    for(const details of clone.querySelectorAll('details:not([open])'))for(const child of details.children)if(child.tagName!=='SUMMARY')child.style.setProperty('display','none','important');
    for(const image of clone.querySelectorAll('img')){const data=images.get(image.currentSrc||image.src);if(data)image.src=data.url;}
    [...clone.querySelectorAll('svg')].filter(includeSvg).forEach((node,index)=>{const chart=charts[index],image=document.createElement('img');image.src=chart.url;image.style.cssText='display:block;margin:auto;width:'+chart.width+'px;height:'+chart.height+'px';node.replaceWith(image);});
    for(const summary of clone.querySelectorAll('summary'))summary.style.listStyleType='none';
  }});
  return saveCanvasImage(canvas,filename);
}
export async function saveCanvasImage(canvas,filename){
  const blob=await new Promise(resolve=>canvas.toBlob(resolve,'image/png'));if(!blob)throw Error('画像を作成できませんでした。');
  const url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download=filename+'.png';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
}
