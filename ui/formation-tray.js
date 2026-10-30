// 一時枠は編成の10枠と分離し、キャラの個別設定を同じオブジェクトで移す。
export function addFormationMember(slots,tray,member){
 for(const [group,values]of [['slots',slots],['tray',tray]]){
  const index=values.findIndex(value=>value?.unitId===member.unitId);
  if(index>=0){
   const target=group==='tray'?moveTrayMember(slots,tray,index):-1;
   return target>=0?{group:'slots',index:target,changed:true}:{group,index,changed:false};
  }
 }
 const index=slots.findIndex(value=>!value);
 if(index>=0){slots[index]=member;return {group:'slots',index,changed:true};}
 const pending=tray.findIndex(value=>!value);
 if(pending<0)return null;
 tray[pending]=member;return {group:'tray',index:pending,changed:true};
}
export function moveTrayMember(slots,tray,index){
 const target=slots.findIndex(value=>!value);
 if(target<0||!tray[index])return -1;
 slots[target]=tray[index];tray[index]=null;return target;
}

// ドロップ先の個別設定も一時枠へ戻し、どちらのキャラも失わない。
export function swapTrayMember(slots,tray,index,target){
 if(!Number.isInteger(target)||target<0||target>=slots.length||!Number.isInteger(index)||index<0||index>=tray.length||(!tray[index]&&!slots[target]))return false;
 [slots[target],tray[index]]=[tray[index],slots[target]];return true;
}
