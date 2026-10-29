// ホストの表示設定。戦闘の論理F・カメラ倍率を変更しない。
export const battleAspects=[['20:9','Pixel 8（20:9）'],['16:9','16:9'],['18:9','18:9'],['21:9','21:9'],['auto','領域に合わせる']];
export function battleViewportWidth(choice,width,height){
 const known=battleAspects.some(([value])=>value===choice)?choice:'20:9';
 const ratio=known==='auto'?width/Math.max(1,height):known.split(':').reduce((a,b)=>Number(a)/Number(b));
 return Math.max(960,Math.min(3840,Math.round(ratio*640)));
}

// 指定速度は通常の1倍基準。0は本家スピードアップの設定に従う。
export function battlePlaybackRate(speed,speedMode){
 const nativeRate=speedMode+1;
 return speed>0?Math.min(20,Math.max(1,speed))/nativeRate:1;
}
