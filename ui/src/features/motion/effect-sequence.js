// 波動の発生処理と、烈波・爆波の描画分岐を同じ絶対時刻から評価する。
export function createEffectSequence(id,animations,config,level=3){
  const name=id.replace(/_e$/,''),enemy=id.endsWith('_e');
  const count=Math.max(1,Math.min(20,Math.trunc(Number(level))||1));
  if(/^skill_(?:smallwave|wave)_attack$/.test(name)){
    const interval=name.includes('smallwave')?config.smallWaveInterval:config.waveInterval;
    const visible=animations[0].frames-2,first=interval-1;
    return {kind:'wave',level:count,duration:first+(count-1)*interval+visible,instances(frame){
      const instances=[];
      for(let index=0;index<count;index++){
        const age=frame-first-index*interval;
        // 発生と同じ更新内でタイマーが減り、初めて描く姿勢は1Fになる。
        if(age>=0&&age<visible)instances.push({motion:0,frame:age+1,x:(enemy?-27:-53)+(enemy?80:-80)*index});
      }
      return instances;
    }};
  }
  if(/^skill_(?:smallvolcano|volcano)$/.test(name)){
    const start=15,end=start+count*20;
    return {kind:'surge',level:count,duration:end+10,instances(frame){
      if(frame<0||frame>=this.duration)return [];
      return [{motion:frame<start?0:frame<end?1:2,frame:frame<start?frame:frame<end?frame-start:frame-end,x:0}];
    }};
  }
  if(name==='skill_explosion'){
    const start=config.explosionStart;
    const duration=start+config.explosionInterval*2+config.explosionActive+config.explosionEnd;
    return {kind:'explosion',duration,instances(frame){
      if(frame<0||frame>=duration)return [];
      // 15.7.1は00→01。01の中で中心・左右の爆発が進む。02は選択再生に残す。
      return [{motion:frame<start?0:1,frame:frame<start?frame:frame-start,x:0}];
    }};
  }
  return null;
}
