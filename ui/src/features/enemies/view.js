import {escapeHtml,formatNumber,formatTime,propertyIconHtml} from '../../shared/game/database-view.js';
import {enemyDetailUrl} from '../../shared/game/enemy-stats.js';

import {enemyImageHtml,enemyAttributesHtml,enemyAbilitiesHtml} from '../../shared/game/enemy-view.js';
export {enemyImageHtml,enemyAttributesHtml,enemyAbilitiesHtml};

export function enemySheetHtml(database,enemy,stats,settings) {
  const value=(label,text)=>'<th scope="row">'+label+'</th><td class="unit-value">'+text+'</td>';
  const time=key=>formatTime(stats[key],settings.seconds);
  const hits='<table class="enemy-hit-table"><thead><tr><th>攻撃</th>'+enemy.attacks.map((_,index)=>'<th>'+ (index+1)+'撃目</th>').join('')+'</tr></thead><tbody>'+[
    ['攻撃力',stats.attacks.map(formatNumber)],['攻撃発生',enemy.foreswings.map(value=>formatTime(value,settings.seconds))],['効果',enemy.abilityHits.map(value=>value?'あり':'なし')],
    ...(enemy.ranges.length?[['攻撃範囲',enemy.ranges.map(range=>range.join('〜'))]]:[]),
  ].map(([label,values])=>'<tr><th scope="row">'+label+'</th>'+values.map(value=>'<td>'+value+'</td>').join('')+'</tr>').join('')+'</tbody></table>';
  return '<table class="unit-sheet"><colgroup>'+Array.from({length:6},()=>'<col>').join('')+'</colgroup><tbody>'+
    '<tr><th>ID '+enemy.id+'</th><th colspan="3" class="unit-form-name"><h2>'+escapeHtml(enemy.name)+'</h2></th><td colspan="2">'+propertyIconHtml(database,enemy.attackType==='範囲'?'area':'single',enemy.attackType)+' '+escapeHtml(enemy.attackType)+'</td></tr>'+
    '<tr><td rowspan="3" colspan="2" class="unit-portrait">'+enemyImageHtml(database,enemy,54)+'</td>'+value('体力',formatNumber(stats.hp))+value('KB',formatNumber(stats.knockbacks))+'</tr>'+
    '<tr>'+value(enemy.attacks.length>1?'総攻撃力':'攻撃力',formatNumber(stats.attack))+value('速度',formatNumber(stats.speed))+'</tr>'+
    '<tr>'+value('DPS',formatNumber(stats.dps))+value('射程',formatNumber(stats.range)+'<br><small class="db-meta">自城感知 '+formatNumber(enemy.castleRange)+'</small>')+'</tr>'+
    '<tr>'+value('お金',formatNumber(stats.drop)+'<span class="enemy-money-base" title="会計力Lv'+settings.accountingLevel+'を反映。元データの基本値: '+enemy.drop+'"> / お宝未補正: '+formatNumber(stats.dropWithoutTreasure)+'</span>')+value('攻撃頻度',time('attackCycle'))+value('攻撃発生',time('foreswing'))+'</tr>'+
    '<tr>'+value('回数制限',enemy.attackLimit<0?'無制限':formatNumber(enemy.attackLimit))+value('待機時間',formatTime(Math.max(0,enemy.attackInterval-1),settings.seconds))+value('攻撃後',time('backswing'))+'</tr>'+
    '<tr><th>属性・種族</th><td colspan="5" class="unit-information">'+enemyAttributesHtml(database,enemy)+'</td></tr>'+
    '<tr><th>特性</th><td colspan="5" class="unit-information"><ul class="unit-abilities">'+(enemyAbilitiesHtml(database,enemy,settings,stats)||'<li>なし</li>')+'</ul></td></tr>'+
    (enemy.attacks.length>1?'<tr><th>攻撃内訳</th><td colspan="5">'+hits+'</td></tr>':enemy.ranges.length?'<tr><th>攻撃範囲</th><td colspan="5">'+enemy.ranges[0].join('〜')+'</td></tr>':'')+
    '<tr><th>説明</th><td colspan="5" class="unit-description">'+(escapeHtml(enemy.description)||'図鑑説明なし')+'</td></tr>'+
    '<tr><th>表示</th><td colspan="5">'+(enemy.motion?'<a href="/pages/unit-motion/?enemy='+enemy.id+'">モーション</a> ':'')+'<button type="button" data-capture="enemy-sheet-output">画像保存</button></td></tr></tbody></table>'+
    '<p class="db-meta enemy-settings-note">体力'+settings.health+'% / 攻撃'+settings.attack+'%'+(stats.crystal!==1?' / お宝補正×'+stats.crystal:'')+'。お金は会計力Lv'+settings.accountingLevel+'・お宝'+settings.accountingTreasure+'%。「お宝未補正」は会計力Lvのみ反映（基本値'+enemy.drop+'）。'+(enemy.attackCycle===null?'攻撃モーション未収録のため、DPSは未計算。':'DPSは一連の攻撃合計 ÷ 攻撃頻度。波動・烈波などの追加ダメージは含みません。')+'</p>';
}
export function enemyConditionControls(enemy,settings,prefix) {
  const number=(key,label,max)=>'<label>'+label+' %<input type="number" id="'+prefix+key+'" min="0" max="'+max+'" value="'+settings[key]+'" data-enemy-condition="'+key+'"></label>';
  let html='';
  for(const [key,label] of [['strengthen','攻撃力アップ発動'],['critical','クリティカル発動'],['savage','渾身の一撃発動']])if(enemy.abilities.some(ability=>ability.key===key))html+='<label><input type="checkbox" id="'+prefix+key+'" data-enemy-condition="'+key+'"'+(settings[key]?' checked':'')+'>'+label+'</label>';
  return html?'<div class="db-toolbar">'+html+'</div><p class="db-meta">発動時の値を表示します。発動率による期待値ではありません。</p>':'';
}
export function enemyComparisonHtml(database,entries,seconds) {
  const metrics=[['体力','hp'],['総攻撃力','attack'],['DPS','dps'],['射程','range'],['速度','speed'],['KB','knockbacks'],['お金','drop'],['攻撃頻度','attackCycle'],['攻撃発生','foreswing'],['悪魔シールド','shield'],['バリア','barrier']];
  return '<div class="db-table-wrap"><table class="db-table enemy-compare-table"><thead><tr><th>項目</th>'+entries.map(({enemy,settings,stats})=>'<th><a href="'+escapeHtml(enemyDetailUrl(enemy,settings))+'">'+enemyImageHtml(database,enemy)+escapeHtml(enemy.name)+'</a><div class="db-meta">ID '+enemy.id+' / 体力'+settings.health+'%・攻撃'+settings.attack+'%'+(stats.crystal!==1?' / お宝補正×'+stats.crystal:'')+'</div><div class="db-meta">'+[['strengthen','攻撃力アップ発動'],['critical','クリティカル発動'],['savage','渾身の一撃発動']].filter(([key])=>settings[key]&&enemy.abilities.some(ability=>ability.key===key)).map(([,label])=>label).join(' / ')+'</div></th>').join('')+'</tr></thead><tbody>'+metrics.map(([label,key])=>'<tr><th scope="row">'+label+'</th>'+entries.map(({stats})=>'<td>'+(['attackCycle','foreswing'].includes(key)?formatTime(stats[key],seconds):formatNumber(stats[key]))+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>';
}
export function enemyRadarHtml(entries) {
  const metrics=[['体力','hp'],['攻撃力','attack'],['DPS','dps'],['射程','range'],['速度','speed'],['KB','knockbacks']],point=(index,value)=>{
    const angle=index*Math.PI/3-Math.PI/2;return [160+Math.cos(angle)*value,145+Math.sin(angle)*value];
  };
  const maxima=metrics.map(([,key])=>Math.max(1,...entries.map(entry=>entry.stats[key]||0)));
  const polygon=radius=>metrics.map((_,index)=>point(index,radius).join(',')).join(' ');
  return '<svg class="enemy-chart" viewBox="0 0 320 290" role="img" aria-label="敵のステータス比較。各軸は比較中の最大値を100%として表示。"><title>敵のステータス比較</title>'+[.25,.5,.75,1].map(rate=>'<polygon class="grid" points="'+polygon(100*rate)+'"/>').join('')+
    metrics.map(([label],index)=>{const [x,y]=point(index,123);return '<text x="'+x+'" y="'+y+'" text-anchor="middle" dominant-baseline="middle">'+label+'</text>';}).join('')+
    entries.map(({stats},series)=>'<polygon class="series-'+series+'" points="'+metrics.map(([,key],index)=>point(index,100*(stats[key]||0)/maxima[index]).join(',')).join(' ')+'"/>').join('')+'</svg>'+
    '<p class="db-meta">各軸は比較中の最大値を100%として表示。実数値は表で確認できます。</p>';
}
