import {defaultGameSettings,gameSettingFields,normalizeGameSettings} from './game-settings.js';

export const defaultSiteSettings={theme:'original',scale:100,border:50};
export function normalizeSiteSettings(value={}) {
  const bounded=(key,min,max)=>value?.[key]!=null&&Number.isFinite(Number(value[key]))?Math.min(max,Math.max(min,Math.round(Number(value[key])))):defaultSiteSettings[key];
  return {theme:['original','dark','light'].includes(value?.theme)?value.theme:'original',scale:bounded('scale',75,150),border:bounded('border',0,100)};
}
export function encodeSettings(site,database) {
  const bytes=new TextEncoder().encode(JSON.stringify({version:1,site:normalizeSiteSettings(site),database:normalizeGameSettings(database)}));
  return 'KBC1.'+btoa(String.fromCharCode(...bytes)).replaceAll('+','-').replaceAll('/','_').replace(/=+$/,'');
}
export function decodeSettings(text) {
  if(typeof text!=='string'||text.trim().length>12000||!/^KBC1\.[A-Za-z0-9_-]+$/.test(text.trim()))throw Error('KBCの設定文字列を貼り付けてください。');
  let value;
  try {value=JSON.parse(new TextDecoder('utf-8',{fatal:true}).decode(Uint8Array.from(atob(text.trim().slice(5).replaceAll('-','+').replaceAll('_','/')),char=>char.charCodeAt(0))));}
  catch {throw Error('設定文字列が壊れています。元の文字列をすべてコピーしてください。');}
  const record=item=>item&&typeof item==='object'&&!Array.isArray(item);
  if(!record(value)||value.version!==1||!record(value.site)||!record(value.database))throw Error('対応していない設定形式です。');
  const site=normalizeSiteSettings(value.site),database=normalizeGameSettings(value.database);
  if(Object.keys(value).some(key=>!['version','site','database'].includes(key))||Object.keys(value.site).length!==3||Object.keys(site).some(key=>site[key]!==value.site[key])||Object.keys(value.database).length!==gameSettingFields.length||gameSettingFields.some(({key})=>database[key]!==value.database[key]))throw Error('設定に範囲外の値または不明な項目があります。');
  return {site,database};
}
export const defaultSettings={site:defaultSiteSettings,database:defaultGameSettings};

export function siteBorderColor(theme,border=50){
  const palette={original:['526784','0b1c3f','f4f6fa'],dark:['616161','0d0d0d','f4f6fa'],light:['8291a5','f0f4f8','1a202c']}[theme]||['526784','0b1c3f','f4f6fa'];
  const target=palette[border<50?1:2],amount=Math.min(1,Math.abs(border-50)/50)*.8;
  return '#'+[0,2,4].map(index=>Math.round(parseInt(palette[0].slice(index,index+2),16)*(1-amount)+parseInt(target.slice(index,index+2),16)*amount).toString(16).padStart(2,'0')).join('');
}
