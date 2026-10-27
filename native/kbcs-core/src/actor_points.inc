// 00a0cdf4/00a0cfec。保存・所持Ptの付与とは別の、戦闘中イベントの整数化。
extern "C" uint32_t kbcs_core_battle_point_add(const KbcsPointRules *rules,KbcsBattlePoints *state,const KbcsPointInput *input){
 if(!rules||!state||!input||rules->tier_count<1||rules->tier_count>32||input->count<0||input->count>2||input->timer<0||input->limit< -1)return 1;
 if(rules->kind)return 0;const auto &in=*input;uint32_t value=0;
 if(in.event==0&&in.count==1){
  int rate=rules->tiers[rules->tier_count-1][1],previous=0;
  for(int i=0;i<rules->tier_count;++i){const auto &tier=rules->tiers[i];if(previous<in.values[0]&&in.values[0]<=tier[0]){rate=tier[1];break;}previous=tier[0];}
  value=uint32_t(Context::divide(int32_t(uint32_t(rate)*uint32_t(in.values[0])),100));
 }else if(in.event==1&&in.count==2){
  const int sum=int32_t(uint32_t(in.values[0])+uint32_t(in.values[1]));
  if(in.limit== -1)value=uint32_t(Context::divide(int32_t(uint32_t(rules->rate)*uint32_t(sum)),100));
  else{
   const double amount=((2.0-double(in.timer)/double(in.limit))*double(sum)*double(rules->rate))/100.0;
   // 疑似コードはuint表記だが、実命令FCVTZS W20は符号付き32bitへ飽和する。
   value=uint32_t(std::isnan(amount)?0:amount>=double(INT32_MAX)?INT32_MAX:amount<=double(INT32_MIN)?INT32_MIN:int32_t(amount));
  }
 }
 const int score=int32_t(uint32_t(state->score)+value);state->score=score>999999998?999999999:score;return 0;
}
static int pointGauge(const KbcsPointRules &rules,const KbcsBattlePoints &state){
 const double raw=(double(state.score)-double(state.origin))*294.0/double(rules.fever[1]);
 return std::isnan(raw)?0:raw>=double(INT32_MAX)?INT32_MAX:raw<=double(INT32_MIN)?INT32_MIN:int(raw);
}
extern "C" uint32_t kbcs_core_battle_point_fever(const KbcsPointRules *rules,KbcsBattlePoints *state,int32_t *changed){
 if(!rules||!state||!changed||rules->fever_count<0||rules->fever_count>10)return 1;*changed=0;
 if(!rules->fever_count)return 0;if(rules->fever_count<3||rules->fever[1]<=0)return 1;
 auto &s=*state;const auto &r=rules->fever;
 if(s.wait>0){if(!--s.wait){s.origin=s.score;*changed=-1;}return 0;}
 if(r[0])return 0;
 const int gauge=pointGauge(*rules,s);
 // ADDSのLT条件とASR。加算overflow時も、単純な符号付き除算へ置換しない。
 int smooth=int32_t(uint32_t(s.gauge)+uint32_t(gauge));
 smooth=int32_t(uint32_t(smooth)+uint32_t(int64_t(s.gauge)+int64_t(gauge)<0))>>1;
 if(int32_t(uint32_t(smooth)-uint32_t(s.gauge))<2)smooth=int32_t(uint32_t(s.gauge)+1U);
 s.gauge=gauge<=s.gauge?gauge:smooth;
 if(s.score<int32_t(uint32_t(r[1])+uint32_t(s.origin)))return 0;
 s.wait=r[2];s.frame=s.phase=s.ending=0;s.gauge=-1;*changed=1;return 0;
}
extern "C" uint32_t kbcs_core_battle_point_display(const KbcsPointRules *rules,KbcsBattlePoints *state){
 if(!rules||!state||rules->fever_count<0||rules->fever_count>10)return 1;if(!rules->fever_count||state->wait<=0)return 0;
 if(rules->fever_count<3)return 1;auto &s=*state;++s.frame;
 if(!s.ending)s.phase=s.wait>5?0:6-s.wait;else if(s.phase<5)++s.phase;return 0;
}
extern "C" uint32_t kbcs_core_battle_point_render(const KbcsPointRules *rules,KbcsBattlePoints *state){
 if(!rules||!state||rules->fever_count<0||rules->fever_count>10)return 1;
 if(state->gauge!= -1||!rules->fever_count)return 0;
 if(rules->fever_count<2||rules->fever[1]<=0)return 1;state->gauge=pointGauge(*rules,*state);return 0;
}
