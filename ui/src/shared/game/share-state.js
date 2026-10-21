// 初期値と同じ項目を省き、0・false・空配列による明示的な変更は残す。
export function compactState(value,defaults={}) {
  defaults=defaults||{};
  const result={};
  for(const [key,item] of Object.entries(value)) {
    if(item===undefined||JSON.stringify(item)===JSON.stringify(defaults[key]))continue;
    if(item&&typeof item==='object'&&!Array.isArray(item)) {
      const nested=compactState(item,defaults[key]);
      if(Object.keys(nested).length)result[key]=nested;
    } else result[key]=item;
  }
  return result;
}
