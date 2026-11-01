// 004460b0 / 00446784 / 0044626c。原画の矩形と縁を共通に転送する。
export function createNativeSprites(manifest){
 function rect(atlas,cut,x,y,width=cut[2],height=cut[3]){return '<svg x="'+x+'" y="'+y+'" width="'+Math.abs(width)+'" height="'+Math.abs(height)+'" viewBox="'+cut.join(' ')+'" preserveAspectRatio="none"><image href="'+manifest.atlases[atlas].url+'"/></svg>';}
 function sprite(atlas,index,x,y,width,height){return rect(atlas,manifest.atlases[atlas].rects[index],x,y,width,height);}
 function panel(atlas,outer,inner,x,y,width,height,scale=1){
  const a=manifest.atlases[atlas].rects[outer],b=manifest.atlases[atlas].rects[inner];
  return slice(atlas,a,[b[0]-a[0],b[1]-a[1],b[2],b[3]],x,y,width,height,scale);
 }
 function slice(atlas,a,b,x,y,width,height,scale=1){
  const sw=[b[0],b[2],a[2]-b[0]-b[2]],sh=[b[1],b[3],a[3]-b[1]-b[3]],scaled=value=>Math.fround(Math.fround(value)*Math.fround(scale));
  // 0044626cは右/下の始点を別々にfloat32で整数化する。左からの加算で置き換えない。
  const dx=[x,Math.trunc(Math.fround(Math.fround(x)+scaled(sw[0]))),Math.trunc(Math.fround(Math.fround(x+width)-scaled(sw[2])))],dy=[y,Math.trunc(Math.fround(Math.fround(y)+scaled(sh[0]))),Math.trunc(Math.fround(Math.fround(y+height)-scaled(sh[2])))];
  const dw=[Math.trunc(scaled(sw[0])),Math.trunc(Math.fround(Math.fround(width)-scaled(sw[0]+sw[2]))),Math.trunc(scaled(sw[2]))],dh=[Math.trunc(scaled(sh[0])),Math.trunc(Math.fround(Math.fround(height)-scaled(sh[0]+sh[2]))),Math.trunc(scaled(sh[2]))];
  let html='',sy=a[1];
  for(let row=0;row<3;row++){let sx=a[0];for(let col=0;col<3;col++){if(dw[col]>0&&dh[row]>0)html+=rect(atlas,[sx,sy,sw[col],sh[row]],dx[col],dy[row],dw[col],dh[row]);sx+=sw[col];}sy+=sh[row];}return html;
 }
 return {rect,sprite,panel,slice};
}
