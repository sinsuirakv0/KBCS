import {formationLayout} from './formation-layout.js';
import {resolveFormationMember} from './formation-model.js';
import {escapeHtml as esc} from './src/shared/game/database-view.js';

// 00a82394→DAT_002f2664の19要素。20は同じアトラスの追加画像。
const slotNumberCuts=[44,45,46,47,48,49,50,51,52,53,113,114,115,116,117,125,126,138,140,141];

// 00a82394: 編成不可cut139は枠の右端+3、上端+61へ右揃えで重ねる。
export function blockedBadgeSvg(manifest,x=0,y=0){
  const rect=manifest.atlases.img029_ja.rects[139];
  return '<svg x="'+(x+113-rect[2])+'" y="'+(y+61)+'" width="'+rect[2]+'" height="'+rect[3]+'" viewBox="'+rect.join(' ')+'"><image href="/images/native-formation/img029_ja.png"/></svg>';
}
export function formationIconHtml(database,form,manifest,reason=''){
  const image=form.icon?'<svg width="110" height="85" viewBox="9 21 110 85"><image href="'+esc(database.imageBase+form.icon)+'"/></svg>':'<rect width="110" height="85" fill="#23334c"/>';
  return '<svg class="formation-unit-icon" viewBox="0 0 110 85" role="img" aria-label="'+esc(form.name+(reason?'：編成不可 '+reason:''))+'"><title>'+esc(form.name+(reason?'：'+reason:''))+'</title>'+image+(reason?blockedBadgeSvg(manifest):'')+'</svg>';
}

// 00a82394/00a8b028。同じ描画を編集・出撃準備へ使い、保存状態には触れない。
export function createFormationView(database,manifest){
 const units=new Map(database.units.map(unit=>[unit.id,unit])),escape=esc;
 const names=['にゃんこ砲','スロウ砲','鉄壁砲','かみなり砲','水鉄砲','エンジェル砲','キャノンブレイク砲','呪い砲'];
function spriteRect(atlas,rect,x,y,width,height,extra=''){
  const [sx,sy,w,h]=rect,sheet=manifest.atlases[atlas];
  return '<svg x="'+x+'" y="'+y+'" width="'+(width??w)+'" height="'+(height??h)+'" viewBox="'+[sx,sy,w,h].join(' ')+'" preserveAspectRatio="none" '+extra+'><image href="/images/native-formation/'+atlas+'.png"'+(sheet.width?' width="'+sheet.width+'" height="'+sheet.height+'"':'')+'/></svg>';
}
const sprite=(atlas,cut,...args)=>spriteRect(atlas,manifest.atlases[atlas].rects[cut],...args);
// 00446784と同じ中央伸縮。四隅と縁は原本の画素幅を保つ。
function panel(outer,inner,x,y,width,height){
  const a=manifest.atlases.img029_ja.rects[outer],b=manifest.atlases.img029_ja.rects[inner];
  const sw=[b[0]-a[0],b[2],a[0]+a[2]-b[0]-b[2]],sh=[b[1]-a[1],b[3],a[1]+a[3]-b[1]-b[3]],dw=[sw[0],width-sw[0]-sw[2],sw[2]],dh=[sh[0],height-sh[0]-sh[2],sh[2]];
  let result='',sy=a[1],dy=y;
  for(let row=0;row<3;row++){let sx=a[0],dx=x;for(let column=0;column<3;column++){result+=spriteRect('img029_ja',[sx,sy,sw[column],sh[row]],dx,dy,dw[column],dh[row]);sx+=sw[column];dx+=dw[column];}sy+=sh[row];dy+=dh[row];}return result;
}
function digits(text,atlas,first,x,y,height,gap=0){
  let result='';for(const character of String(text)){const cut=first===12?(Number(character)===0?21:11+Number(character)):first+Number(character),rect=manifest.atlases[atlas].rects[cut],width=rect[2]*height/rect[3];result+=sprite(atlas,cut,x,y,width,height);x+=width+gap;}return result;
}
function actionSvg(label,action,content){
  const layout=formationLayout();
  const [x,y,w,h]={menu:[layout.badgeX,61,147,36],previous:[layout.leftX,134,62,97],next:[layout.rightX,134,62,97],cannon:[layout.width-65,80,66,51],clear:[-7,220,80,80]}[action];
  return content+'<rect role="button" tabindex="0" aria-label="'+escape(label)+'" data-action="'+action+'" x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="transparent"/>';
}
 return (doc,{index=1,selected=-1,floating=null,shifts=Array.from({length:10},()=>({x:0,y:0})),deployment=null,preview=false,tray=false,ghost=false,hiddenSlot=-1}={})=>{
  const layout=formationLayout();
  let body='<rect width="1188" height="278" fill="#d4b15f"/>'+sprite('img008_ja',0,0,0,1188,55)+sprite('img008_ja',3,8,3,297,46)+'<path d="M0 55H1188V79H0Z" fill="#ffe290"/><path d="M0 79H1188" stroke="#706241"/>';
  if(!tray&&!ghost){
  // 原本の子スプライトは親中心+51、中心揃え。21以降はPC拡張として原画の数字を合成する。
  const number=String(index),numberX=layout.badgeX+124-Math.trunc(25/2),cut=slotNumberCuts[index-1];
  const badgeNumber=cut!==undefined?sprite('img029_ja',cut,numberX,67,25,24):[...number].map((character,i)=>{
    // 0はcut53（10）の右側。原画の黒縁を含む16×24の範囲を使う。
    const rect=character==='0'?[829,167,16,24]:manifest.atlases.img029_ja.rects[43+Number(character)];
    return spriteRect('img029_ja',rect,numberX+i*25/number.length,67,25/number.length,24);
  }).join('');
  body+=actionSvg('出陣スロットの操作','menu',sprite('img029_ja',5,layout.badgeX,61,147,36)+badgeNumber);
  // 00a71320 / 00a82394: 名前欄はcut120/121、中央揃え、原本param.tsvの余白。
  const parameters=manifest.parameters.values;
  if(doc.slotName)body+=panel(120,121,layout.badgeX,parameters.slot_bg_y,147,27)+'<text data-slot-name x="'+(layout.badgeX+73)+'" y="'+(parameters.slot_bg_y+parameters.slot_name_margin_top)+'" text-anchor="middle" dominant-baseline="text-before-edge" fill="white" font-size="'+parameters.slot_font_size+'">'+escape(doc.slotName)+'</text>';
  body+=actionSvg('前の編成','previous',sprite('img006_ja',8,layout.leftX,134,62,97));
  body+=actionSvg('次の編成','next','<g transform="translate('+(2*layout.rightX+62)+' 0) scale(-1 1)">'+sprite('img006_ja',8,layout.rightX,134,62,97)+'</g>');
  body+=sprite('img029_ja',7,layout.pageX,110+manifest.parameters.values.slot_page_y_offset)+sprite('img029_ja',8,layout.pageX,205+manifest.parameters.values.slot_page_y_offset);
  body+='<rect x="290" y="160" width="696" height="4" fill="#9b8247"/><rect x="290" y="255" width="696" height="4" fill="#9b8247"/>';
  }else if(tray)body='<rect x="288" y="88" width="698" height="89" fill="#d4b15f"/>';
  if(ghost)body='';
  // 00a82394は占有状態に関係なく、番号付きの10枠を先に描く。
  for(const [slot,{x,y}] of layout.slots.slice(0,ghost?0:tray?5:10).entries()){
    const rect=manifest.atlases.img029_ja.rects[64+slot];
    body+='<rect x="'+(x+2)+'" y="'+(y+2)+'" width="111" height="85" fill="#54472a"/><rect x="'+x+'" y="'+y+'" width="111" height="85" fill="#9b8247"/>'+sprite('img029_ja',64+slot,x+55-Math.trunc(rect[2]/2),y+42-Math.trunc(rect[3]/2),rect[2],rect[3]);
  }
  let floatingBody='';
  for(let slot=0;slot<(tray?5:10);slot++){
    const {x,y}=layout.slots[slot],member=doc.slots[slot],unit=member&&units.get(member.unitId),effective=unit&&resolveFormationMember(unit,member),form=unit?.forms.find(form=>form.index===effective.form);
    let contents='';
    if(form){
      // 0063fa4c / 00a8b028: 元画像の自然寸法を保ち、uni.imgcutの110×85を切り抜く。
      contents+='<svg x="'+x+'" y="'+y+'" width="110" height="85" viewBox="'+manifest.unitIcon.rect.join(' ')+'" preserveAspectRatio="none"><image href="'+escape(database.imageBase+form.icon)+'"/></svg>';
      // 005d1bb4 → 00448048。通常編成のcut60〜70、文字間隔-3、右寄せと円の予約幅22。
      const price=deployment?String(deployment.slots[slot].cost):null;
      if(price!==null)contents+=digits(price,'img023_ja',60,x+88-price.length*15,y+61,26,-3)+sprite('img023_ja',70,x+91,y+61,22,26);
    }
    if(form&&deployment?.slots[slot].reasons)contents+=blockedBadgeSvg(manifest,x,y);
    if(selected===slot&&form&&floating?.slot!==slot)contents+=panel(9,25,x,y,110,85);
    if(floating?.slot===slot){
      const width=110+Math.trunc(floating.growth*110/100),height=85+Math.trunc(floating.growth*85/100);
      const left=x+floating.x-Math.trunc(floating.growth*110/200),top=y+floating.y-Math.trunc(floating.growth*85/200);
      floatingBody='<g pointer-events="none" opacity="'+((255-floating.alpha)/255)+'" transform="translate('+left+' '+top+') scale('+(width/110)+' '+(height/85)+') translate('+(-x)+' '+(-y)+')">'+contents+'</g>';
    }else if(slot!==hiddenSlot)body+='<g transform="translate('+shifts[slot].x+' '+shifts[slot].y+')">'+contents+'</g>';
    body+='<rect role="button" tabindex="0" data-slot="'+slot+'" aria-label="枠'+(slot+1)+' '+escape(form?.name??'空き')+'" aria-pressed="'+(selected===slot)+'" x="'+x+'" y="'+y+'" width="110" height="85" fill="transparent"/>';

  }
  if(!tray&&!ghost){
    const cannon=panel(101,102,layout.width-172,59,271,27)+'<text x="'+(layout.width-86)+'" y="79" text-anchor="middle" fill="white" font-size="18" font-weight="bold">'+names[doc.cannon.id]+'</text>'+sprite('img029_ja',100,layout.width-55,90,46,36);
    body+=preview?cannon:actionSvg('城砲を変更','cannon',cannon);
  }
  if(!preview&&!tray&&!ghost)body+=actionSvg('編成中のキャラをすべて外す','clear',sprite('img029_ja',132,13,230,40,40));body+=floatingBody;
  return '<svg class="formation-native" viewBox="'+(ghost?'290 90 110 85':tray?'288 88 698 89':'0 0 1188 278')+'" aria-label="'+(tray?'一時キャラ枠':'キャラクター編成')+'">'+body+'</svg>';
 };
}
export function fitFormationName(root,manifest){
 const label=root.querySelector('[data-slot-name]'),width=147-2*manifest.parameters.values.slot_name_margin_left;
 if(label&&label.getComputedTextLength()>width){label.setAttribute('textLength',width);label.setAttribute('lengthAdjust','spacingAndGlyphs');}
}
