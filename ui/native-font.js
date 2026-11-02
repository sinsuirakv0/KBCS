// 現版AndroidのTextPaintと同じ標準書体。OS固有の日本語代替へ任せない。
export const nativeFontFamily='"KBCS Roboto", "KBCS Noto CJK JP", sans-serif';
export const nativeFont=(size,weight=400)=>weight+' '+size+'px '+nativeFontFamily;
let loading;
export function loadNativeFonts(){
 return loading??=typeof document!=='undefined'&&document.fonts?Promise.all([
  document.fonts.load('16px "KBCS Roboto"'),document.fonts.load('16px "KBCS Noto CJK JP"'),
 ]):Promise.resolve();
}
