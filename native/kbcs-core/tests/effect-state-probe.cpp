// 解析専用DLL。所有者の非公開プールを検査し、配布バイナリには含めない。
#include "../src/actor.cpp"

extern "C" uint32_t kbcs_audit_equipment(const KbcsBattleOrb *orbs,const int32_t *grades,int32_t count,uint32_t traits,int32_t values[26][4],int32_t present[26]){
 if(!values||!present)return 1;
 KbcsActorDefinition definition{};
 const auto code=kbcs_core_battle_equipment(orbs,grades,count,&definition);
 if(code)return code;
 int32_t targeted[5][2]{};
 targetOrbs(orbs,count,traits,targeted);
 for(int effect=0;effect<26;++effect){
  std::copy_n(definition.orbs[effect],4,values[effect]);
  if(effect<5)std::copy_n(targeted[effect],2,values[effect]);
  present[effect]=definition.orb_present[effect];
 }
 return 0;
}

extern "C" uint32_t kbcs_audit_cannon_action(KbcsActorCannon *state,KbcsActor actors[2][51],const KbcsCannonRules *rules,int side,int mode,KbcsBattleSound *out,int *count){
 if(!out||!count)return 1;std::vector<KbcsBattleSound> sounds;const int frame=0;
 BattleSoundScope scope(sounds,frame);KbcsBattleRules battle_rules{};BattleRulesScope rules_scope(battle_rules,mode);
 const auto code=kbcs_core_actor_cannon_action(state,actors,rules,side);*count=int(sounds.size());std::copy(sounds.begin(),sounds.end(),out);return code;
}

extern "C" uint32_t kbcs_audit_defeat(int ticks,KbcsBattleEnding *out,KbcsBattleHint *hint){
 if(ticks<0||ticks>200||!out||!hint)return 1;KbcsBattleConfig config{};config.seed=1;config.screen.viewport_width=960;
 KbcsBattle battle(config);battle.result.mode=2;battle.hint_fallback_lines=3;
 for(int i=0;i<ticks;++i)battle.advanceEnding();
 const auto code=kbcs_core_battle_ending(&battle,out);return code?code:kbcs_core_battle_hint(&battle,hint);
}

extern "C" uint32_t kbcs_audit_effect_pool(int kind,const int32_t lengths[2],const KbcsBattleVisual *before,int count,int ticks,KbcsBattleVisual *after){
 if(!lengths||!before||!after||kind<0||kind>3||count!=(kind?30:200)||ticks<0)return 1;
 KbcsBattleConfig config{};config.seed=1;
 const int phases[4][2]={{0x10e8,0x10e8},{0x2248,0x2248},{0x2360,0x2398},{0x2520,0x2558}};
 for(int i=0;i<2;++i){config.effect_clocks[i][0]=phases[kind][i];config.effect_clocks[i][1]=config.effect_clocks[i][2]=lengths[i];}
 KbcsBattle battle(config);
 auto *pool=kind==0?battle.critical_visuals.data():kind==1?battle.killer_visuals.data():kind==2?battle.barrier_visuals.data():battle.shield_visuals.data();
 std::copy_n(before,count,pool);for(int i=0;i<ticks;++i)battle.effectClock();std::copy_n(pool,count,after);return 0;
}

extern "C" uint32_t kbcs_audit_owner_clock(const KbcsActor *before,const int32_t lengths[4],int ticks,KbcsActor *after,uint32_t *random){
 if(!before||!lengths||!after||!random||ticks<0)return 1;
 KbcsBattleConfig config{};config.seed=0x12345678;config.environment.unit_modes[0]=1;config.environment.stage_width=20000;config.environment.castle_slot=-1;
 config.screen.fixed_money=0;config.screen.viewport_width=960;config.rules.total_limit=-1;
 for(int i=0;i<4;++i){config.effect_clocks[i][0]=i?0x2440+i*0x38:0x2328;config.effect_clocks[i][1]=config.effect_clocks[i][2]=lengths[i];}
 KbcsBattle battle(config);battle.result.mode=4;
 for(int side=0;side<2;++side){auto &w=battle.actors[side][0].words;w[0]=1;w[7]=w[8]=1000;w[3]=side?3200:16800;}
 battle.actors[1][1]=*before;battle.profiles[1][1]=0;battle.definitions.emplace_back();
 auto &p=battle.definitions.back();p.definition.count=113;p.spawn.side=1;p.spawn.raw=before->words[0];p.deployment_slot=-1;
 KbcsBattleScreenState screen{};
 try{for(int i=0;i<ticks;++i){screen.frame=i;battle.logical(screen);}*after=battle.actors[1][1];*random=battle.seed;return 0;}
 catch(const AttackFailure &e){return e.code;}catch(...){return 3;}
}

extern "C" uint32_t kbcs_audit_transient_pool(int phase,int length,const KbcsBattleVisual *before,int count,int ticks,KbcsBattleVisual *after,int *remaining){
 if(!before||!after||!remaining||count<0||count>32||ticks<0)return 1;
 KbcsBattleConfig config{};config.seed=1;config.effect_clocks[0][0]=phase;config.effect_clocks[0][1]=length;
 KbcsBattle battle(config);battle.transient.assign(before,before+count);
 for(int i=0;i<ticks;++i)battle.effectClock();*remaining=int(battle.transient.size());std::copy(battle.transient.begin(),battle.transient.end(),after);return 0;
}

extern "C" uint32_t kbcs_audit_actor_visuals(int side,const KbcsActor *actor,KbcsBattleVisual *after,int *count){
 if(side<0||side>1||!actor||!after||!count)return 1;
 KbcsBattleConfig config{};config.seed=1;config.environment.unit_modes[0]=1;config.environment.castle_scale=100;
 KbcsBattle battle(config);battle.actors[side][1]=*actor;
 const KbcsBattleVisual *values=nullptr;const auto code=kbcs_core_battle_visuals(&battle,&values,count);
 if(code)return code;if(*count>32)return 1;std::copy_n(values,*count,after);return 0;
}

extern "C" uint32_t kbcs_audit_return_wipe(int mode,int ticks,int *action,int *fade,int *frame){
 if((mode!=1&&mode!=2&&mode!=4&&mode!=7)||ticks<1||ticks>30||!action||!fade||!frame)return 1;
 KbcsBattleConfig config{};config.seed=1;config.environment.stage_width=16000;config.environment.unit_modes[0]=1;
 config.screen.speed=2;config.screen.fixed_money=-1;config.screen.viewport_width=1280;config.state.rows=2;config.state.intro=24;
 config.state.holding=config.state.pending_control=config.state.description_item=-1;config.state.battle_mode=mode;
 KbcsBattle battle(config);battle.result.mode=mode;battle.ending.phase=mode==2?4:7;battle.ending.guard=5;
 KbcsBattleScreenInput input{ticks,0,0,0,0};KbcsBattleScreenState state{};KbcsBattleScreenLayout layout{};
 const auto code=kbcs_core_battle_advance(&battle,&input,&state,&layout);if(code)return code;
 *action=state.request_action;*frame=battle.return_frame;*fade=layout.fade_count==1&&layout.fade_sizes[0]==4&&layout.fade[0][0]==0&&layout.fade[0][4]==1280;return 0;
}

// 全251語を受け渡し、原本のフレーム境界と同じ所有側の入口を検証する。
extern "C" uint32_t kbcs_audit_frame_marks(KbcsActor (*actors)[51],const int32_t modes[2]){
 if(!actors||!modes)return 1;KbcsBattleConfig config{};config.seed=1;KbcsBattle battle(config);
 std::copy_n(modes,2,battle.config.environment.unit_modes);std::copy_n(&actors[0][0],102,&battle.actors[0][0]);battle.beginFrame();
 std::copy_n(&battle.actors[0][0],102,&actors[0][0]);return 0;
}
