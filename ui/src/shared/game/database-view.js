export function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>"']/g, character => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[character]);
}
const number = new Intl.NumberFormat("ja-JP", { maximumFractionDigits: 0 });
const decimal = new Intl.NumberFormat("ja-JP", { maximumFractionDigits: 2 });
export function atlasImageHtml(database, atlas, key, size) {
  const rect=atlas?.icons[key];if(!rect)return '';
  const [x,y,width,height]=rect,scale=size/width;
  return '<span class="unit-property-image" style="width:'+size+'px;height:'+height*scale+'px"><img src="'+escapeHtml(database.imageBase+atlas.path)+'" alt="" style="width:'+atlas.width*scale+'px;height:'+atlas.height*scale+'px;left:'+ -x*scale+'px;top:'+ -y*scale+'px"></span>';
}
export function orbIconHtml(database, orb, size=32) {
  if(orb.type==='none')return '<span class="unit-orb-empty" aria-label="本能玉なし">—</span>';
  const label=(database.targets.find(target=>target.key===orb.target)?.label||'属性なし')+' / '+(database.equipment?.types.find(type=>type.key===orb.type)?.name||orb.type)+' / '+['D','C','B','A','S'][orb.grade];
  return '<span class="unit-orb-image" role="img" aria-label="'+escapeHtml(label)+'" title="'+escapeHtml(label)+'" style="width:'+size+'px;height:'+size+'px">'+atlasImageHtml(database,database.orbAtlases.attribute,orb.target,size)+atlasImageHtml(database,database.orbAtlases.effect,orb.type,size)+atlasImageHtml(database,database.orbAtlases.grade,orb.grade,size)+'</span>';
}
export function formatNumber(value) { return value == null || !Number.isFinite(value) ? "—" : number.format(value); }
export function formatTime(value, seconds) { return value == null ? "—" : seconds ? decimal.format(value / 30) + "秒" : value + "F"; }
export function propertyIconHtml(database, key, label, size = 18, focusable = true) {
  const atlas = database.propertyAtlas, rect = atlas?.icons[key];
  const image=database.propertyImages?.[key];
  if(image)return '<span class="unit-property" role="img" aria-label="'+escapeHtml(label)+'" title="'+escapeHtml(label)+'"'+(focusable?' tabindex="0"':'')+'><span class="unit-property-image" style="width:'+size+'px;height:'+size+'px"><img src="'+escapeHtml(image)+'" alt="" style="width:100%;height:100%;left:0;top:0"></span></span>';
  if (!rect) return '<span title="' + escapeHtml(label) + '">' + escapeHtml(label) + '</span>';
  const [x, y, width, height] = rect, scale = size / width;
  return '<span class="unit-property" role="img" aria-label="' + escapeHtml(label) + '" title="' + escapeHtml(label) + '"' + (focusable ? ' tabindex="0"' : '') + '><span class="unit-property-image" style="width:' + size + 'px;height:' + height * scale + 'px"><img src="' + escapeHtml(database.imageBase + atlas.path) + '" alt="" style="width:' + atlas.width * scale + 'px;height:' + atlas.height * scale + 'px;left:' + -x * scale + 'px;top:' + -y * scale + 'px"></span></span>';
}

export function iconChoiceHtml(database,{key,label,value=key,checked=false,attributes=''}) {
  const hasImage=!!(database.propertyImages?.[key]||database.propertyAtlas.icons[key]),rarity=key.startsWith('rarity-');
  const image=hasImage?propertyIconHtml(database,key,label,rarity?58:18,false).replace('role="img"','aria-hidden="true"'):escapeHtml(label);
  return '<label class="db-chip unit-icon-choice'+(hasImage?' has-image':'')+(rarity?' is-rarity':'')+'" title="'+escapeHtml(label)+'" data-icon-label="'+escapeHtml(label)+'"><input type="checkbox" value="'+escapeHtml(value)+'" aria-label="'+escapeHtml(label)+'"'+(checked?' checked':'')+attributes+'><span>'+image+'</span></label>';
}

// SVG内ではHTMLの絶対配置を使わず、同じアトラスをSVGの座標で切り出す。
export function propertyIconSvgHtml(database, key, label, x, y, size=20) {
  const atlas=database.propertyAtlas,rect=atlas?.icons[key];
  if(!rect)return '<text x="'+x+'" y="'+y+'">'+escapeHtml(label)+'</text>';
  return '<svg class="unit-radar-icon" x="'+(x-size/2)+'" y="'+(y-size/2)+'" width="'+size+'" height="'+size+'" viewBox="'+rect.join(' ')+'" overflow="hidden"><title>'+escapeHtml(label)+'</title><image href="'+escapeHtml(database.imageBase+atlas.path)+'" x="0" y="0" width="'+atlas.width+'" height="'+atlas.height+'"/></svg>';
}
export function bindIconHints(root,output) {
  const show=event=>{const label=event.target.closest('[data-icon-label]');if(label&&root.contains(label)){const text=label.title||label.dataset.iconLabel;if(output.textContent!==text)output.textContent=text;}};
  for(const type of ['focusin','click','change'])root.addEventListener(type,show);
}
export function abilityIconHtml(database,ability,seconds,size=18) {
  if(ability.orb)return '<span title="'+escapeHtml(abilityText(ability,seconds))+'">'+orbIconHtml(database,ability.orb,size)+'</span>';
  const key=ability.key.endsWith('-immune')&&ability.resistance<100?ability.key.replace(/-immune$/,'-resist'):ability.key;
  return propertyIconHtml(database,key,abilityText(ability,seconds),size);
}

export function abilityText(ability, seconds) {
  const values = [];
  if (ability.probability != null) values.push(ability.probability + "%");
  if (ability.duration != null) values.push(formatTime(ability.duration, seconds));
  if (ability.level != null) values.push("Lv" + ability.level);
  if (ability.percent != null) values.push(ability.percent + "%");
  if (ability.health != null) values.push("体力" + ability.health + "%以下 / 攻撃" + ability.power + "%");
  else if (ability.power != null) values.push("攻撃" + ability.power + "%");
  if (ability.resistance != null) values.push(ability.resistance + "%");
  if (ability.range) values.push(ability.range.join("〜"));
  const label=ability.key.endsWith('-immune')&&ability.resistance<100?ability.label.replace(/無効$/,'耐性'):ability.label;
  return label + (values.length ? "：" + values.join(" / ") : "");
}

