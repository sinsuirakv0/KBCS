import {escapeHtml,formatNumber,formatTime,propertyIconHtml} from './database-view.js';

export function enemyImageHtml(database,enemy,size=28) {
  return enemy.icon?'<span class="enemy-icon" style="width:'+size+'px;height:'+size+'px"><img data-enemy-image src="'+escapeHtml(database.imageBase+enemy.icon)+'" alt="" loading="lazy"></span>':'<span class="db-meta" title="画像未収録">—</span>';
}
export function enemyAttributesHtml(database,enemy) {
  return [...enemy.attributes,...enemy.species].map(key=>propertyIconHtml(database,key,[...database.attributes,...database.species].find(item=>item.key===key)?.label||key)).join('')+(enemy.star===1?'<span class="db-meta" title="スターエイリアン">★</span>':'');
}
function enemyAbilityValues(ability,seconds) {
  const values=[];
  if(ability.probability!=null)values.push(ability.probability+'%');
  if(ability.duration!=null)values.push(formatTime(ability.duration,seconds));
  if(ability.health!=null)values.push(ability.health+'%以下');
  if(ability.power!=null)values.push('倍率×'+ability.power/100);
  if(ability.level!=null)values.push('Lv'+ability.level);
  if(ability.count!=null)values.push(ability.count<0?'無制限':ability.count+'回');
  if(ability.distance!=null)values.push('距離'+ability.distance);
  if(ability.hp!=null)values.push('耐久'+formatNumber(ability.hp));
  if(ability.percent!=null)values.push(ability.key==='revive'?'体力'+ability.percent+'%':ability.percent+'%');
  if(ability.regen!=null)values.push('KB時'+ability.regen+'%再生');
  if(ability.range)values.push('範囲'+ability.range.join('〜'));
  return values;
}
export function enemyAbilitiesHtml(database,enemy,settings,stats,compact=false) {
  return enemy.abilities.filter(ability=>ability.key!=='multi-hit').map(original=>{
    const ability=original.key==='aku-shield'?{...original,hp:stats.shield}:original;
    const values=compact?[]:enemyAbilityValues(ability,settings.seconds);
    const label=ability.label+(values.length?'：'+values.join(' / '):'');
    const hasImage=database.propertyImages?.[ability.key]||database.propertyAtlas.icons[ability.key];
    const icon=hasImage?propertyIconHtml(database,ability.key,label,18,!compact):'<span title="'+escapeHtml(label)+'">'+escapeHtml(ability.label)+'</span>';
    return compact?icon:'<li>'+icon+(values.length?'<span>'+escapeHtml(values.join(' / '))+'</span>':'')+'</li>';
  }).join('');
}
