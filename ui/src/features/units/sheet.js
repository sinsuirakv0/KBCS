import {escapeHtml,formatNumber,formatTime,propertyIconHtml,imageHtml,rarityIconHtml,abilitiesHtml} from './view.js';
const cells=(label,value)=>'<th scope="row">'+label+'</th><td class="unit-value">'+escapeHtml(value)+'</td>';
export const unitInformationRow=(label,html,extra=false)=>'<tr'+(extra?' class="unit-extra"':'')+'><th scope="row">'+label+'</th><td colspan="5" class="unit-information">'+html+'</td></tr>';
const information=unitInformationRow;
// 表の構造・画像・特性の描画は詳細ページと編成で共用する。
export function unitSheetHtml(database,unit,profile,settings,extraRows=''){
  const form=profile.form;
  const stats=profile.stats,time=value=>formatTime(value,settings.seconds);
  const traits=new Set(['omni','long-range','multi-hit']);
  const abilities=abilitiesHtml(database,form.abilities.filter(ability=>!traits.has(ability.key)),settings.seconds);
  return '<table class="unit-sheet" id="unit-sheet-'+form.code+'"><colgroup><col><col><col><col><col><col></colgroup><tbody>'+
    '<tr><th class="unit-id">'+String(unit.id).padStart(3,'0')+'-'+(form.index+1)+'</th><th colspan="3" class="unit-form-name"><h2>'+escapeHtml(form.name)+'</h2></th><td colspan="2">'+rarityIconHtml(database,unit)+(unit.isSpirit?'・精霊':'')+'</td></tr>'+
    '<tr><td colspan="2" rowspan="3" class="unit-portrait">'+imageHtml(database,form,56,43)+'</td>'+cells('体力',formatNumber(stats.hp))+cells('KB',formatNumber(stats.knockbacks))+'</tr>'+
    '<tr>'+cells('攻撃力',formatNumber(stats.attack))+cells('速度',formatNumber(stats.speed))+'</tr>'+
    '<tr>'+cells('DPS',formatNumber(stats.dps))+cells('射程',formatNumber(stats.range))+'</tr>'+
    '<tr>'+cells('コスト',formatNumber(stats.cost))+cells('攻撃頻度',time(stats.attackCycle))+cells('攻撃発生',time(stats.foreswing))+'</tr>'+
    '<tr>'+cells('再生産',time(stats.respawn))+cells('待機時間',time(stats.attackCycle==null?null:stats.attackCycle-form.foreswings.at(-1)))+cells('攻撃後',time(stats.backswing))+'</tr>'+
    (form.targets.length?information('対象',form.targets.map(key=>propertyIconHtml(database,key,database.targets.find(target=>target.key===key)?.label||key)).join(' ')):'')+
    information('攻撃特性','<ul class="unit-abilities"><li>'+propertyIconHtml(database,form.attackType==='範囲'?'area':'single',form.attackType)+'</li>'+abilitiesHtml(database,form.abilities.filter(ability=>traits.has(ability.key)),settings.seconds)+(stats.attacks.length>1?'<li>連続攻撃 '+stats.attacks.length+'回</li>':'')+'</ul>')+
    information('特性',abilities?'<ul class="unit-abilities">'+abilities+'</ul>':'なし')+
    (form.ranges.length?information('攻撃範囲',escapeHtml(form.ranges.map(range=>range.join('〜')).join(' / '))):'')+
    (stats.attacks.length>1?information('連続攻撃',stats.attacks.map((attack,index)=>escapeHtml(formatNumber(attack)+'（発生 '+time(form.foreswings[index])+'）')).join(' / ')):'')+extraRows+'</tbody></table>';
}
