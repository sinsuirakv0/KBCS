// 所有戦闘の通常出撃・攻撃を通し、未出現ボスの前後を連続更新する。
#include "kbcs_battle.h"
#include <algorithm>
#include <cassert>
#include <cstdio>

static KbcsBattleProfile profile(int side){
 KbcsBattleProfile p{};int raw[119]{};raw[0]=side?1000000:10000;raw[1]=1;raw[3]=side?0:10000;
 raw[4]=1;raw[5]=10000;raw[9]=10000;raw[15]=9;raw[12]=1;raw[13]=1;raw[59]=side?0:10000;raw[61]=2;raw[110]=-1;
 if(!side){raw[55]=raw[57]=raw[66]=-1;raw[63]=1;}else{raw[50]=raw[51]=raw[53]=-1;}
 assert(kbcs_core_actor_load(raw,side?113:119,!side,p.definition.cells)==0);p.definition.count=side?113:119;
 std::fill_n(p.definition.growth,20,100);p.spawn={side,2,0,0,0,0,0};p.deployment_slot=side?-1:0;
 std::fill_n(p.motion.encoded,8,20);std::fill_n(p.motion.plain,8,20);p.motion.soul_frames=30;
 p.motion.encoded[2]=p.motion.plain[2]=3;p.death_soul_frames=30;p.raw_attack[0]=p.raw_attack[1]=side?0:10000;
 p.price.raw=0;p.price.fixed=-1;p.price.rarity_rate=100;return p;
}
int main(int argc,char**){
 KbcsBattleConfig config{};config.environment.unit_modes[0]=1;config.environment.stage_width=16000;
 config.environment.castle_slot=-1;config.environment.castle_x=3200;config.environment.castle_scale=100;
 config.environment.hp_percent=config.environment.attack_percent=100;
 config.screen.speed=2;config.screen.fixed_money=0;config.screen.present[0]=1;config.screen.viewport_width=960;
 config.state.rows=2;config.state.intro=24;config.state.holding=config.state.pending_control=-1;
 config.state.description_item=-1;config.castle_hp[0]=10000;config.castle_hp[1]=100;config.enemy_max=config.unit_max=50;
 if(argc>1){config.screen.items=1;config.state.items_on=1;config.state.speed_mode=1;}
 config.rules.total_limit=-1;config.seed=1572;config.boss_frames=33;config.cannon.encoded[0]=config.cannon.encoded[1]=config.cannon.encoded[2]=-1;
 const int phases[]={0x1040,0x10e8,0x2248,0x35b8,0x3628,0x16480};for(int i=0;i<6;++i){config.effect_clocks[i][0]=phases[i];config.effect_clocks[i][1]=config.effect_clocks[i][2]=33;}
 KbcsBattleProfile profiles[]={profile(0),profile(1)};KbcsStageRow row{{2,1,0,10,10,50,0,0,1,100,0,100,0,0}};
 KbcsBattle *battle=nullptr;assert(kbcs_core_battle_create(&config,profiles,2,&row,1,&battle)==0);
 KbcsBattleScreenState state{};KbcsBattleScreenLayout view{};KbcsBattleScreenInput input{};
 assert(kbcs_core_battle_advance(battle,&input,&state,&view)==0);
 input.ticks=1;input.phase=2;input.x=view.slots[0][0]+20;input.y=view.slots[0][1]+20;
 bool preserved=false,won=false;int saved_frame=-1;
 for(int frame=0;frame<100;++frame){
  const auto code=kbcs_core_battle_advance(battle,&input,&state,&view);if(code){int error[4];kbcs_core_battle_error(battle,error);std::printf("error=%u at %d/%d/%d/%d\n",code,error[0],error[1],error[2],error[3]);return 1;}input.phase=0;
  const KbcsActor *actors=nullptr;const int32_t *indices=nullptr;assert(kbcs_core_battle_actors(battle,&actors,&indices)==0);
  const auto &castle=actors[51].words;const auto &unit=actors[1].words;const auto &boss=actors[52].words;
  KbcsBattleResult result{};assert(kbcs_core_battle_result(battle,&result)==0);
  if(argc>1&&castle[8]==1){assert(!result.mode&&boss[0]==2&&unit[1]==7);std::printf("{\"speed\":2,\"frame\":%d,\"castleHp\":1,\"unitAction\":7,\"bossAction\":%d,\"mode\":0}\n",state.frame,boss[1]);won=true;break;}
  if(castle[8]==1&&!preserved){const KbcsBattleSound *sounds=nullptr;int count=0;kbcs_core_battle_sounds(battle,&sounds,&count);assert(std::any_of(sounds,sounds+count,[](auto s){return s.id==22;}));preserved=true;saved_frame=state.frame;assert(!result.mode&&!boss[0]);}
  if(result.mode){
   if(!preserved){std::printf("{\"failure\":\"castle destroyed before boss\",\"frame\":%d,\"bossRaw\":%d}\n",state.frame,boss[0]);kbcs_core_battle_destroy(battle);return 2;}
   assert(preserved&&result.mode==1&&state.frame==saved_frame+1);assert(!castle[8]&&unit[1]==7&&boss[0]==2&&boss[1]==4&&!boss[8]&&boss[2]==0&&boss[65]==1);
   const KbcsBattleSound *sounds=nullptr;int count=0;kbcs_core_battle_sounds(battle,&sounds,&count);assert(std::any_of(sounds,sounds+count,[](auto s){return s.id==45;}));assert(std::none_of(sounds,sounds+count,[](auto s){return s.id==22;}));
   const KbcsBattleVisual *visuals=nullptr;kbcs_core_battle_visuals(battle,&visuals,&count);assert(std::any_of(visuals,visuals+count,[](auto v){return v.kind==8&&v.phase==0x1040;}));
   std::printf("{\"preservedFrame\":%d,\"victoryFrame\":%d,\"castleHp\":%d,\"unitAction\":%d,\"bossAction\":%d,\"shock\":true}\n",saved_frame,state.frame,castle[8],unit[1],boss[1]);won=true;break;
  }
 }
 assert(won);kbcs_core_battle_destroy(battle);
}
