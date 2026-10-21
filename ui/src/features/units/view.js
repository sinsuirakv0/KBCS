import {escapeHtml,formatNumber,formatTime,orbIconHtml,atlasImageHtml,propertyIconHtml,iconChoiceHtml,propertyIconSvgHtml,bindIconHints,abilityIconHtml,abilityText} from "../../shared/game/database-view.js";
export {escapeHtml,formatNumber,formatTime,orbIconHtml,atlasImageHtml,propertyIconHtml,iconChoiceHtml,propertyIconSvgHtml,bindIconHints,abilityIconHtml,abilityText};
import { calculateUnitStats, rarityNames, unitDetailUrl } from "../../shared/game/unit-stats.js";

import {unitImageUrl,imageHtml,handleUnitImages} from '../../shared/game/unit-view.js';
export {unitImageUrl,imageHtml,handleUnitImages};

export function rarityIconHtml(database,unit,size=42) {return propertyIconHtml(database,'rarity-'+unit.rarity,rarityName(unit),size);}

export function abilitiesHtml(database, abilities, seconds) {
  return abilities.filter(ability => ability.key !== "multi-hit").map(ability => {
    const values = [];
    if (ability.probability > 0) values.push(ability.probability + "%");
    if (ability.duration > 0) values.push(formatTime(ability.duration, seconds));
    if (ability.level != null) values.push("Lv" + ability.level);
    if (ability.health != null) values.push(ability.health + "%↓ 倍率×" + (ability.power / 100));
    else if (ability.power != null) values.push("倍率×" + (ability.power / 100));
    if (ability.percent != null) values.push(ability.percent + "%");
    if (ability.effectBonus) values.push("距離+" + ability.effectBonus + "%");
    if (ability.resistance > 0 && ability.resistance < 100) values.push(ability.resistance + "%");
    const icon = abilityIconHtml(database, ability, seconds);
    const content = ability.key === "spirit" ? '<a href="/pages/unit-detail/?id=' + ability.unitId + '" aria-label="精霊召喚：ID ' + ability.unitId + 'の詳細">' + icon + '<span>ID ' + ability.unitId + '</span></a>' : icon;
    return '<li>' + content + (values.length ? '<span>' + escapeHtml(values.join(" / ")) + '</span>' : '') + '</li>';
  }).join("");
}

export function comparisonHtml(database, entries, settings) {
  const rows = entries.map(({ unit, form, stats,detailUrl }) => ({ unit, form,detailUrl, stats: stats || calculateUnitStats(unit, form, database.growth[unit.growth], settings) }));
  const labels = [["体力", "hp"], ["攻撃力", "attack"], ["DPS", "dps"], ["射程", "range"], ["コスト", "cost"], ["KB", "knockbacks"], ["速度", "speed"], ["再生産", "respawn"], ["攻撃頻度", "attackCycle"], ["攻撃発生", "foreswing"]];
  return '<table class="db-table"><thead><tr><th>項目</th>' + rows.map(row => '<th class="db-name"><a href="' + escapeHtml(row.detailUrl||unitDetailUrl(row.unit, row.form, settings)) + '">' + escapeHtml(row.form.name) + '</a><span class="db-meta"> Lv' + row.stats.level + '</span></th>').join("") + '</tr></thead><tbody>' + labels.map(([label, key]) => '<tr><th scope="row">' + label + '</th>' + rows.map(row => '<td>' + (["respawn", "attackCycle", "foreswing"].includes(key) ? formatTime(row.stats[key], settings.seconds) : formatNumber(row.stats[key])) + '</td>').join("") + '</tr>').join("") + '</tbody></table>';
}

export function rarityName(unit) { return rarityNames[unit.rarity] || "分類未登録"; }
