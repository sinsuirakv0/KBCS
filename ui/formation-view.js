import {escapeHtml as esc} from './src/shared/game/database-view.js';

// 00a82394: 編成不可cut139は枠の右端+3、上端+61へ右揃えで重ねる。
export function blockedBadgeSvg(manifest,x=0,y=0){
  const rect=manifest.atlases.img029_ja.rects[139];
  return '<svg x="'+(x+113-rect[2])+'" y="'+(y+61)+'" width="'+rect[2]+'" height="'+rect[3]+'" viewBox="'+rect.join(' ')+'"><image href="/images/native-formation/img029_ja.png"/></svg>';
}
export function formationIconHtml(database,form,manifest,reason=''){
  const image=form.icon?'<svg width="110" height="85" viewBox="9 21 110 85"><image href="'+esc(database.imageBase+form.icon)+'"/></svg>':'<rect width="110" height="85" fill="#23334c"/>';
  return '<svg class="formation-unit-icon" viewBox="0 0 110 85" role="img" aria-label="'+esc(form.name+(reason?'：編成不可 '+reason:''))+'"><title>'+esc(form.name+(reason?'：'+reason:''))+'</title>'+image+(reason?blockedBadgeSvg(manifest):'')+'</svg>';
}
