import {battleItems} from './battle-support.js';
import {escapeHtml as esc} from './src/shared/game/database-view.js';

export function readSortiePreferences(local,session){
 const read=storage=>{try{return JSON.parse(storage.getItem('kbcs:sortie')||'{}')||{};}catch{return {};}};
 const saved={...read(session),...read(local)};
 return {...saved,items:Object.fromEntries(battleItems.map(item=>[item.key,!!saved.items?.[item.key]])),speed:saved.speed===3?3:2};
}
// 006dca34/006ddfb8のmapicon: ON=0..5、OFF=6..11、3倍=16。
export function sortieItemsHtml(manifest,items,speed){
 return battleItems.map((item,index)=>{
  const cut=index===0&&items.speedup&&speed===3?16:index+(items[item.key]?0:6),rect=manifest.atlases.mapicon.rects[cut];
  return '<button type="button" data-item="'+item.key+'" aria-pressed="'+!!items[item.key]+'" aria-label="'+esc(item.name+(index===0&&items.speedup?' '+speed+'倍':'')+(items[item.key]?'：有効':'：無効'))+'"><span class="sortie-item-image"><svg viewBox="'+rect.join(' ')+'" width="'+rect[2]+'" height="'+rect[3]+'" aria-hidden="true"><image href="/images/native-battle/mapicon.png"/></svg></span><span>'+item.name+(index===0&&items.speedup?' '+speed+'倍':'')+'</span></button>';
 }).join('');
}
export function toggleSortieItem(items,speed,key){
 if(key==='speedup'){
  if(!items.speedup){items.speedup=true;return 2;}
  if(speed===2)return 3;
  items.speedup=false;return 2;
 }
 items[key]=!items[key];return speed;
}
// 007acf88 / 007b3c90..007b3d2c。右端から320、y411の原本2スプライト。
export function sortieLaunchLayout(width,press=0){
 const half=Math.trunc(press/2);
 return [[10,width-320-half,411-half,304+press,74+press],[11,width-282-half,417-half,231+press,62+press]];
}
export function sortieLaunchHtml(manifest,press=0){
 const atlas=manifest.atlases.img031_ja;
 return '<svg viewBox="0 0 304 74" aria-hidden="true">'+sortieLaunchLayout(320,press).map(([cut,x,y,w,h])=>'<svg x="'+x+'" y="'+(y-411)+'" width="'+w+'" height="'+h+'" viewBox="'+atlas.rects[cut].join(' ')+'" preserveAspectRatio="none"><image href="'+atlas.url+'"/></svg>').join('')+'</svg>';
}
