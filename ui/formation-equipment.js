import {escapeHtml as escape} from './src/shared/game/database-view.js';

export function equipmentKind(item) {
  const {content,attribute}=item.equipment;
  return content+':'+(attribute??'-');
}

export function equipmentKinds(items,allowed) {
  const ids=new Set(allowed),kinds=new Map();
  for(const item of items.values()){
    if(!ids.has(item.id))continue;
    const key=equipmentKind(item);
    if(!kinds.has(key))kinds.set(key,[]);
    kinds.get(key).push(item);
  }
  for(const grades of kinds.values())grades.sort((a,b)=>a.equipment.gradeID-b.equipment.gradeID);
  return kinds;
}

export function chooseEquipment(grades,grade) {
  return grades?.find(item=>item.equipment.gradeID===grade)??grades?.at(-1);
}

export function setEquipment(member,slot,id) {
  while(member.orbs.length<=slot)member.orbs.push(null);
  member.orbs[slot]=id;
  // 空欄を詰めると第2枠が第1枠へ移るため、末尾だけ整理する。
  while(member.orbs.length&&member.orbs.at(-1)===null)member.orbs.pop();
}

export function equipmentRows(member,items,selection,kinds) {
  const option=(value,name,selected=false,disabled=false)=>
    '<option value="'+escape(String(value))+'"'+(selected?' selected':'')+(disabled?' disabled':'')+'>'+escape(name)+'</option>';
  return selection.slots.map((slot,index)=>{
    const id=member.orbs[index],item=items.get(id),key=item&&equipmentKind(item);
    const grades=kinds.get(key),active=grades?.some(grade=>grade.id===id);
    const retained=id!=null&&!active;
    const reason=selection.formLocked?'第3形態以降で有効':slot.unsupportedCondition!=null?
      '未実装の解放条件（ID '+slot.unsupportedCondition+'）':!slot.unlocked?
      '合計Lv'+slot.minimumLevel+'で解放':item?.support==='unsupported'?'未実装の本能玉':retained?'現在の形態・本能では無効':'';
    const typeOptions=option('','なし',id==null)+(retained?
      option('retained',item?.kindName??'未収録 ID '+id,true,true):'')+
      [...kinds].map(([kind,rows])=>option(kind,rows[0].kindName,active&&kind===key)).join('');
    const gradeOptions=active?grades.map(row=>option(row.equipment.gradeID,row.gradeName,row.id===id)).join(''):
      option('',item?.gradeName??'—');
    const details=item?'<p class="formation-orb-description">'+escape(item.description)+'</p>':'';
    return '<fieldset class="formation-orb"><legend>本能玉'+(index+1)+'</legend>'+
      '<div class="formation-orb-controls"><label>種類<select data-orb-kind="'+index+'"'+(slot.unlocked?'':' disabled')+'>'+typeOptions+'</select></label>'+
      '<label>等級<select data-orb-grade="'+index+'"'+(slot.unlocked&&active?'':' disabled')+'>'+gradeOptions+'</select></label>'+
      '<button type="button" data-orb-remove="'+index+'" aria-label="本能玉'+(index+1)+'を外す"'+(id==null?' disabled':'')+'>×</button></div>'+
      (reason?'<p class="formation-orb-lock">'+escape(reason)+(id!=null?'・装着記録を保持':'')+'</p>':'')+details+'</fieldset>';
  }).join('');
}
