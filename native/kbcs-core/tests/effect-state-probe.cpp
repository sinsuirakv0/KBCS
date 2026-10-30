// 解析専用DLL。所有者の非公開プールを検査し、配布バイナリには含めない。
#include "../src/actor.cpp"

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
