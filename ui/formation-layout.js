// 15.7.2 ARM64: 00a82394の空枠、00a8b028のキャラ枠。
export function formationLayout(width=1188){
  return {width,height:278,badgeX:Math.trunc(width/2-462),pageX:Math.trunc(width/2-404),leftX:Math.trunc(width/2-477),rightX:Math.trunc(width/2+397),slots:Array.from({length:10},(_,index)=>({x:Math.trunc(width/2-304)+(index%5)*146,y:90+Math.floor(index/5)*95,width:110,height:85}))};
}

// 00a7888c: 隣接枠を順に送る。キャラと個別設定を同じオブジェクトで移動する。
export function insertMember(slots,from,to){
  const [member]=slots.splice(from,1);slots.splice(to,0,member);
}

// 00a7888c / 00a82394: 長押し中の拡大・透明度と、離した後の整数除算。
export function stepFloating(state){
  if(state.held){state.growth=state.growth>19?40:(state.growth*2)|1;state.alpha=state.alpha<107?state.alpha+20:127;}
  else{state.growth=Math.trunc(state.growth/2);state.x=Math.trunc(state.x/2);state.y=Math.trunc(state.y/2);}
}
