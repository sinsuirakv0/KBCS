// 006ee6c8。GUI・資金暗号化・プロフィール取得だけを解決済み入力へ置き換える。
extern "C" uint32_t kbcs_core_battle_computer(const KbcsComputerInput *input,KbcsComputerState *state,
 const KbcsActor opponents[51],uint32_t *seed,KbcsComputerOutput *out){
 if(!input||!state||!opponents||!seed||!*seed||!out)return 1;
 const auto &in=*input;auto s=*state;KbcsComputerOutput result{-1,0,0,0,in.page_step};
 if(s.selected<0||s.selected>9||s.action<0||s.action>3||s.cannon_state<0||s.cannon_state>4||
    in.worker<0||in.worker>7||in.money<0||in.wallet<0||in.upgrade_cost<0||in.page<0||in.page>1)return 1;
 for(int i=0;i<10;++i)if(in.cost[i]<0||in.wait[i]<0||s.choices[i]<-1||s.choices[i]>9)return 1;
 if(!in.enabled){*out=result;return 0;}
 const auto draw=[&](int bound){int32_t value=0;kbcs_core_random_bounded(seed,bound,&value);return value;};
 const auto eligible=[&](int i){return in.raw[i]!=-1&&in.eligible[i];};
 if(in.mode>0)s.action=0;
 if(!s.action){
  std::fill_n(s.choices,10,-1);
  for(int i=0;i<10;++i)s.candidates[i]=eligible(i)&&!in.summoned[i]&&!in.full&&!in.wait[i]?i:-1;
  if(draw(100)<30||in.mode==1){
   if(in.worker==7){
    int count=0;for(int i=0;i<10;++i)if(s.candidates[i]!=-1&&eligible(i)&&in.cost[i]<=in.wallet)s.choices[count++]=i;
    if(!count)s.action=0;
    else if(!in.mode){s.selected=draw(count);s.action=3;}
   }else s.action=2;
  }else{
   int count=0;for(int i=0;i<10;++i)if(s.candidates[i]!=-1)s.choices[count++]=i;
   if(!count){s.action=0;if(in.worker!=7&&in.worker_level>6)s.action=2;}
   else{
    if(!in.mode){s.selected=draw(count);s.action=3;}
    if(in.mode&&s.action==0){if(in.worker!=7&&in.worker_level>6)s.action=2;}
    else if(in.wallet<in.cost[s.choices[s.selected]])s.action=in.worker!=7?2:0;
   }
  }
 }
 // 005bf6c8/005bf658の比較は、相対座標の整数化前にカメラを消去しない。
 const auto relative=[&](int x){return (x-in.camera)/10;};
 const auto inRange=[&](int x){return relative(in.castle_x)-in.cannon_range*160+89<relative(x);};
 if(!in.cannon_wait&&!in.cannon_action){
  for(int i=1;i<actorEnd();++i)if(opponents[i].words[0]&&opponents[i].words[1]!=4&&inRange(opponents[i].words[3])&&!s.cannon_state)s.cannon_state=1;
  for(int i=1;i<actorEnd();++i)if(opponents[i].words[0]&&relative(in.castle_x)+27-200<relative(opponents[i].words[3])){s.action=1;s.cannon_state=0;}
 }
 if(s.cannon_state==1){s.cannon_wait=draw(150);s.cannon_state=2;}
 else if(s.cannon_state==2){if(--s.cannon_wait<=0)s.cannon_state=draw(2)+3;}
 else if(s.cannon_state==3){
  if(!in.cannon_wait&&!in.cannon_action)for(int i=1;i<actorEnd();++i)if(opponents[i].words[0]&&opponents[i].words[1]!=4&&inRange(opponents[i].words[3]))s.action=1;
  s.cannon_state=0;
 }else if(s.cannon_state==4)s.cannon_state=0;
 const int chosen=s.choices[s.selected];
 if(chosen>=0&&in.money>=in.cost[chosen]&&((chosen>=5&&in.page==0)||(chosen<5&&in.page==1))){
  if(!in.page_frame){result.page_start=1;result.page_step=1;}
  else if(in.page_step==-1&&in.page_direction==1)result.page_step=1;
  else if(in.page_step==1&&in.page_direction==0)result.page_step=-1;
 }
 if(s.action<3||in.mode<1){
  if(s.action==2&&in.worker!=7){
   if(in.wallet<in.upgrade_cost)s.action=0;
   if(in.money>=in.upgrade_cost){
    s.action=0;int count=0;for(int i=0;i<10;++i)if(eligible(i))++count;
    const int index=count?draw(count):0;s.pending_raw=s.choices[index];
    for(int i=0;i<10;++i)if(eligible(i)&&s.pending_raw==in.raw[i]&&in.wallet<in.cost[i]){s.pending_raw=-1;break;}
    result.upgrade=1;
   }
  }else if(s.action==2)s.action=0;
  else if(s.action==1)result.fire=1;
  else if(s.action>=3&&chosen>=0&&in.money>=in.cost[chosen]&&!in.page_frame&&!result.page_start&&chosen/5==in.page)result.deploy=chosen;
  // 発射の成功時リセットは005d8f58側。失敗すると発射の選択を保持する。
  if(result.deploy>=0)s.action=0;
 }else s.action=0;
 *state=s;*out=result;return 0;
}
