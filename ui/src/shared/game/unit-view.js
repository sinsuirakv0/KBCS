import {escapeHtml} from './database-view.js';
const unitImages = {};

export function unitImageUrl(database,form){return form?.icon?unitImages[form.icon]||database.imageBase+form.icon:'';}
export function imageHtml(database, form, width = 28, height = 22) {
  if (!form.icon) return '<span class="db-meta" title="画像未収録">—</span>';
  if(form.iconCrop){const {rect:[x,y,w,h],width:sheetWidth,height:sheetHeight}=form.iconCrop,scale=Math.min(width/w,height/h);return '<span class="unit-icon is-sprite" style="width:'+width+'px;height:'+height+'px"><span class="unit-property-image" style="width:'+w*scale+'px;height:'+h*scale+'px"><img src="'+escapeHtml(unitImageUrl(database,form))+'" alt="" loading="lazy" style="width:'+sheetWidth*scale+'px;height:'+sheetHeight*scale+'px;left:'+ -x*scale+'px;top:'+ -y*scale+'px"></span></span>';}
  return '<span class="unit-icon" style="width:' + width + 'px;height:' + height + 'px"><img data-unit-image src="' + escapeHtml(unitImageUrl(database,form)) + '" alt="" width="128" height="128" loading="lazy"></span>';
}
export function handleUnitImages(root = document) {
  root.addEventListener("load", event => {
    const image = event.target;
    if (image.matches?.("img[data-unit-image]") && (image.naturalWidth !== 128 || image.naturalHeight !== 128)) image.parentElement.classList.add("is-full");
  }, true);
  root.addEventListener("error", event => { if (event.target.matches?.("img[data-unit-image]")) { event.target.hidden = true; event.target.parentElement.title = "画像未収録"; } }, true);
}

