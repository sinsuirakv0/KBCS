// 通常入力の待機と、拡張個体への命中/時計/描画用参照を所有APIで検査する。
#include "kbcs_battle.h"
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
static int effect=0;

static KbcsBattleProfile profile(int side){
 KbcsBattleProfile p{};int raw[119]{};raw[0]=10000;raw[1]=1;raw[3]=side?100:1;
 raw[4]=1;raw[5]=10000;raw[9]=10000;raw[15]=9;raw[12]=1;raw[13]=1;raw[110]=-1;
 if(!side)raw[55]=raw[57]=raw[66]=-1;else{raw[11]=1;raw[59]=1;raw[50]=raw[51]=raw[53]=-1;
  if(effect==1){raw[27]=100;raw[28]=20;}
  if(effect==2){raw[81]=100;raw[82]=10400;raw[83]=1;raw[84]=1;}
  if(effect==3){raw[106]=100;raw[107]=10400;raw[108]=1;}
 }
 assert(!kbcs_core_actor_load(raw,side?113:119,!side,p.definition.cells));p.definition.count=side?113:119;
 std::fill_n(p.definition.growth,20,100);p.spawn={side,2,0,0,0,0,0};p.deployment_slot=side?-1:0;
 std::fill_n(p.motion.encoded,8,20);std::fill_n(p.motion.plain,8,20);p.motion.soul_frames=30;
 p.motion.encoded[2]=p.motion.plain[2]=3;p.death_soul_frames=30;p.cost=100000000;p.recharge=500;
 p.price.fixed=-1;p.price.rarity_rate=100;return p;
}
int main(int argc,char **argv){
 if(argc>1)effect=std::atoi(argv[1]);
 KbcsBattleConfig c{};c.environment.unit_modes[0]=1;c.environment.stage_width=16000;c.environment.castle_slot=-1;c.environment.castle_x=3200;c.environment.castle_scale=100;
 c.environment.hp_percent=c.environment.attack_percent=100;c.screen.speed=3;c.screen.fixed_money=-1;c.screen.present[0]=1;c.screen.viewport_width=960;
 c.state.rows=2;c.state.intro=24;c.state.holding=c.state.pending_control=c.state.description_item=-1;c.castle_hp[0]=c.castle_hp[1]=1000000;c.enemy_max=c.unit_max=50;
 c.waves.motion_frames[0]=c.waves.motion_frames[1]=13;c.areas.explosion_frames[0]=8;c.areas.explosion_frames[1]=6;c.areas.explosion_frames[2]=10;c.areas.explosion_frames[3]=4;
 for(int i=0;i<3;++i){c.areas.explosion_widths[i]=400;c.areas.explosion_damage[i]=100;}
 c.rules.total_limit=2;c.rules.rarity_limits[0]=1;c.seed=1572;c.cannon.encoded[0]=c.cannon.encoded[1]=c.cannon.encoded[2]=-1;
 const int phases[]={0x1040,0x10e8,0x2248,0x35b8,0x3628,0x16480};for(int i=0;i<6;++i){c.effect_clocks[i][0]=phases[i];c.effect_clocks[i][1]=c.effect_clocks[i][2]=33;}
 KbcsBattleProfile profiles[]={profile(0),profile(1)};KbcsStageRow row{{2,1,100,1000,1000,100,0,0,0,100,0,100,0,0}};
 KbcsBattle *battle=nullptr;assert(!kbcs_core_battle_create(&c,profiles,2,&row,1,&battle));
 KbcsBattleScreenState state{};KbcsBattleScreenLayout view{};KbcsBattleScreenInput input{};assert(!kbcs_core_battle_advance(battle,&input,&state,&view));
 input={1,2,view.slots[0][0]+20,view.slots[0][1]+20,0};assert(!kbcs_core_battle_advance(battle,&input,&state,&view));assert(state.guard==1);
 input.phase=0;input.ticks=5;assert(!kbcs_core_battle_advance(battle,&input,&state,&view));
 KbcsProductionState production{};uint32_t seed=0;assert(!kbcs_core_battle_production(battle,&production,&seed));assert(production.total==0);
 assert(kbcs_core_battle_cheats(battle,16)==1);assert(!kbcs_core_battle_cheats(battle,7));
 input.ticks=1;input.phase=2;
 for(int i=0;i<80;++i){const auto code=kbcs_core_battle_advance(battle,&input,&state,&view);if(code){int d[4];kbcs_core_battle_error(battle,d);std::printf("error %u at %d/%d/%d/%d\n",code,d[0],d[1],d[2],d[3]);return 1;}assert(!state.guard);assert(state.money==view.wallet_max);}
 assert(!kbcs_core_battle_production(battle,&production,&seed));assert(production.total==80&&production.wait[0]==0);
 const KbcsBattleActorRef *refs=nullptr;int count=0;assert(!kbcs_core_battle_actor_refs(battle,&refs,&count));assert(count==82);
 assert(refs[80].side==0&&refs[80].slot==80&&refs[80].profile==0);const int before=refs[80].actor->words[8];
 input.phase=0;for(int i=0;i<80;++i){const auto code=kbcs_core_battle_advance(battle,&input,&state,&view);if(code){int d[4];kbcs_core_battle_error(battle,d);std::printf("hit error %u at %d/%d/%d/%d\n",code,d[0],d[1],d[2],d[3]);return 2;}}
 assert(!kbcs_core_battle_actor_refs(battle,&refs,&count));if(refs[80].actor->words[8]>=before){for(int i=0;i<count;++i)if(refs[i].side||refs[i].slot==1||refs[i].slot==80){const auto &w=refs[i].actor->words;std::printf("side=%d slot=%d raw=%d hp=%d x=%d state=%d frame=%d range=%d attack=%d\n",refs[i].side,refs[i].slot,w[0],w[8],w[3],w[1],w[2],w[13],w[20]);}std::fflush(stdout);}assert(refs[80].actor->words[8]<before);assert(refs[80].actor->words[8]==refs[1].actor->words[8]);
 assert(!kbcs_core_battle_cheats(battle,0));input.phase=2;assert(!kbcs_core_battle_advance(battle,&input,&state,&view));input.phase=0;input.ticks=5;assert(!kbcs_core_battle_advance(battle,&input,&state,&view));
 assert(!kbcs_core_battle_production(battle,&production,&seed));assert(production.total==80);
 const int expected[]={7500,6800,5500,5300};assert(refs[80].actor->words[8]==expected[effect]);
 std::printf("effect=%d finalHp=%d\n",effect,refs[80].actor->words[8]);
 kbcs_core_battle_destroy(battle);
 // 数量ルールのない場合も、OFF復帰後に51体目以降を増やさない。
 c.unit_max=0;c.rules.total_limit=-1;c.rules.rarity_limits[0]=0;
 assert(!kbcs_core_battle_create(&c,profiles,2,nullptr,0,&battle));assert(!kbcs_core_battle_cheats(battle,7));input.ticks=1;input.phase=2;
 for(int i=0;i<51;++i)assert(!kbcs_core_battle_advance(battle,&input,&state,&view));
 assert(!kbcs_core_battle_cheats(battle,5));assert(!kbcs_core_battle_advance(battle,&input,&state,&view));assert(!kbcs_core_battle_production(battle,&production,&seed));assert(production.total==51);
 kbcs_core_battle_destroy(battle);
 // 召喚状態は保持し、非表示中のボタンだけを通常生産へ戻す。
 effect=0;auto parent=profile(0);parent.definition.cells[110]=1;auto child=profile(0);child.spawn.raw=3;child.deployment_slot=-1;
 const KbcsBattleProfile summon_profiles[]={parent,child};assert(!kbcs_core_battle_create(&c,summon_profiles,2,nullptr,0,&battle));assert(!kbcs_core_battle_cheats(battle,7));
 input.ticks=1;input.phase=2;assert(!kbcs_core_battle_advance(battle,&input,&state,&view));
 KbcsSceneLayout scene{};scene.zoom=1;scene.viewport_width=960;const int point[2]{};KbcsBattleHud hud{};assert(!kbcs_core_battle_hud(battle,&scene,point,&hud));assert(hud.summons[0][0]);
 assert(!kbcs_core_battle_cheats(battle,15));assert(!kbcs_core_battle_advance(battle,&input,&state,&view));assert(!kbcs_core_battle_hud(battle,&scene,point,&hud));assert(!hud.summons[0][0]);
 assert(!kbcs_core_battle_production(battle,&production,&seed));assert(production.total==2);
 assert(!kbcs_core_battle_cheats(battle,7));input.ticks=0;input.phase=0;assert(!kbcs_core_battle_advance(battle,&input,&state,&view));assert(!kbcs_core_battle_hud(battle,&scene,point,&hud));assert(hud.summons[0][0]);
 kbcs_core_battle_destroy(battle);std::puts("80 units, immediate input, funds, stage limits, area hit and disable passed");
}
