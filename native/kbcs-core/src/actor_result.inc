// 009d4e1c / 009e583c。固定資金はレア度別同時数・総生産数の分岐を通らない。
extern "C" uint32_t kbcs_core_battle_bonus(const KbcsBattleRules *rules,int32_t type,int32_t count,int32_t *out){
 if(!rules||!out||type<0||type>=32)return 1;*out=Context::divide(rules->bonus[type],count);return 0;
}
extern "C" uint32_t kbcs_core_battle_limit(const KbcsBattleLimit *input,int32_t *out){
 if(!input||!out||input->cost<0||input->money<0||input->active<0||input->total<0||input->total_limit< -1)return 1;
 const auto &in=*input;int value=0;
 if(in.fixed_money)value=in.money<in.cost?256:0;
 else if(in.rarity_limit>0&&in.active>=in.rarity_limit)value=32;
 else if(in.total_limit>=0&&in.total>=in.total_limit)value=64;
 *out=value;return 0;
}
// 006d6d04の時間判定→行動→城判定。保存・報酬付与はこの数値/個体状態APIに含めない。
extern "C" uint32_t kbcs_core_battle_result_step(const KbcsBattleRules *rules,KbcsBattleResult *state,int32_t phase,int32_t frame,int32_t castle_slot,KbcsActor actors[2][51],uint32_t *seed){
 if(!rules||!state||!actors||!seed||!*seed||phase<0||phase>1||frame<0||castle_slot< -1||castle_slot>50||rules->time_limit< -1||(rules->time_limit<0&&rules->score_type!=3)||state->timer<0||state->elapsed<0)return 1;
 auto &s=*state;if(s.mode)return 0;
 const auto victory=[&](int reason,bool repair){
  s.mode=1;s.reason=reason;s.finished_frame=frame;
  if(repair&&!actorAt(actors,0,0).words[8])actorAt(actors,0,0).words[8]=1;
  // 005d996c: 通常の敵だけを死亡へ移す。特殊城の魂あり状態は変更しない。
  for(int j=1;j<actorEnd();++j){auto &w=actorAt(actors,1,j).words;
   if(w[0]&&w[1]!=4&&j!=castle_slot){w[1]=4;w[2]=0;w[8]=0;}
  }
  if(castle_slot>0&&!actorAt(actors,1,castle_slot).words[111])actorAt(actors,1,castle_slot).words[1]=17;
  if(rules->score_type==2){KbcsStageScoreInput in{};in.elapsed=s.elapsed;in.count=1;KbcsStageScoreOutput out{};kbcs_core_stage_score(&in,&out);s.score=out.score;}
  else if(rules->native_kind== -6)s.score=(30000-s.elapsed)*(30000-s.elapsed);
 };
 if(!phase){
  if(rules->score_type==1&&s.timer!=INT32_MAX){++s.timer;if(rules->time_limit<=s.timer){s.mode=4;s.reason=3;s.finished_frame=frame;}}
  else if(rules->score_type==3){
   if(rules->time_limit== -1||s.timer<rules->time_limit)++s.timer;
   if(rules->time_limit!= -1&&s.timer>=rules->time_limit)victory(3,false);
  }
  if(!s.mode)s.elapsed=s.elapsed<29999?s.elapsed+1:30000;
  return 0;
 }
 if(actorAt(actors,1,0).words[8]==0)victory(1,true);
 else if(!actorAt(actors,0,0).words[8]){
  s.mode=rules->score_type==1?4:rules->score_type==3?7:2;s.reason=2;s.finished_frame=frame;
  // 005e02b0: DAT_002b2bb0は(行動4,時計0)。対象ごとに5回抽選する。
  const auto draw=[&](int bound){int32_t value=0;kbcs_core_random_bounded(seed,bound,&value);return value;};
  for(int j=1;j<actorEnd();++j){auto &w=actorAt(actors,0,j).words;if(!w[0]||w[1]==4)continue;
   w[1]=4;w[2]=0;w[8]=0;w[10]=draw(12)*10+100;w[24]=draw(40)*-10+1000;w[25]=255;
   w[26]=w[10]/10+draw(10);w[27]=draw(40)+20;w[28]=draw(10)+5;w[29]=0;
  }
 }
 return 0;
}
