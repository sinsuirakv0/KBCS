import {escapeHtml} from './src/shared/game/database-view.js';

export const isUnsupported = effect => effect?.support === 'unsupported';
export const unsupportedEffect = 'この効果は現在のKBCSでは未実装です。今後のKBCSのアップデートをお待ちください。';
export const partialCalculation = '未実装または未検証の効果が含まれるため、計算結果が本家と異なる可能性があります。';
export const talentMaximum = talent => Number.isInteger(talent.comboUnlock) ? 1 : talent.maxLevel;
export const comboAvailable = (combo, slots = []) => !isUnsupported(combo) && (combo.active !== false ||
  (combo.unlock || []).some(unlock => slots.some(member => member?.unitId === unlock.unitId &&
    member.level + member.plus >= unlock.minimumLevel && member.talents[unlock.talentIndex] > 0)));

export function unsupportedTalentHtml(talent) {
  const raw = talent.raw;
  const id = `本能ID ${talent.id}`;
  const parameters = raw ? `枠 ${raw.slot + 1} ／ 原本最大Lv ${raw.cells[1]} ／ パラメータ ${raw.cells.slice(2,10).join(', ')}` : '';
  return `<div class="unit-talent-entry"><strong>${escapeHtml(talent.name)}（未実装）</strong><div>${escapeHtml(id)}</div><div>${escapeHtml(talent.description)}</div><small>${escapeHtml(parameters)}</small><p>${unsupportedEffect}</p></div>`;
}
