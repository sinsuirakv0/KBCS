// 所有戦闘の入力からSEまでを検査する。画面描画や音声デバイスは使用しない。
#include "kbcs_battle.h"
#include <cassert>
#include <cstdio>
#include <vector>

static KbcsBattleConfig config(){
 KbcsBattleConfig c{};c.environment.stage_width=16000;c.environment.castle_slot=-1;c.environment.castle_x=3200;
 c.environment.hp_percent=c.environment.attack_percent=c.environment.castle_scale=100;
 c.screen.speed=3;c.screen.fixed_money=-1;c.screen.viewport_width=960;c.screen.charge_start_combo=100;
 c.state.intro=24;c.state.rows=2;c.state.holding=c.state.pending_control=c.state.description_item=-1;
 c.state.bgm_level=c.state.se_level=3;c.state.money=10000;c.castle_hp[0]=c.castle_hp[1]=10000;
 c.rules.total_limit=-1;c.enemy_max=c.unit_max=50;c.seed=1572;c.cannon.encoded[0]=c.cannon.encoded[1]=c.cannon.encoded[2]=-1;return c;
}
struct Battle {
 KbcsBattle *owner=nullptr;KbcsBattleScreenState state{};KbcsBattleScreenLayout view{};
 explicit Battle(KbcsBattleConfig c){assert(!kbcs_core_battle_create(&c,nullptr,0,nullptr,0,&owner));}
 ~Battle(){kbcs_core_battle_destroy(owner);}
 void input(const char *name,int phase,int x,int y,std::vector<int> expected,int ticks=1){
  KbcsBattleScreenInput input{ticks,phase,x,y,0};assert(!kbcs_core_battle_advance(owner,&input,&state,&view));
  const KbcsBattleSound *values=nullptr;int count=0;assert(!kbcs_core_battle_sounds(owner,&values,&count));
  std::vector<int> actual;for(int i=0;i<count;++i)actual.push_back(values[i].id);
  std::printf("%s:",name);for(int id:actual)std::printf(" %d",id);std::puts("");std::fflush(stdout);assert(actual==expected);
 }
};
int main(){
 Battle wallet(config());wallet.input("wallet down",1,20,600,{10});wallet.input("hold",0,0,0,{},3);wallet.input("wallet upgrade",2,20,600,{19});assert(wallet.state.worker==1);
 auto maximum=config();maximum.state.worker=7;Battle max(maximum);max.input("wallet max down",1,20,600,{10});max.input("wallet max",2,20,600,{15});assert(max.state.worker==7);
 auto poor=config();poor.state.money=0;Battle insufficient(poor);insufficient.input("wallet poor",2,20,600,{15});assert(!insufficient.state.worker);
 Battle cannon(config());cannon.input("cannon down",1,900,600,{10});cannon.input("cannon fire",2,900,600,{25,19});cannon.input("cannon busy",2,900,600,{15});
 auto charging=config();charging.screen.charge_start_combo=0;Battle wait(charging);wait.input("cannon charging",2,900,600,{15});
 auto almost=config();almost.screen.charge_combo=100;almost.screen.charge_start_combo=99;Battle ready(almost);ready.input("charge wait",0,0,0,{},8);ready.input("charge ready",0,0,0,{28});
 Battle options(config());options.input("pause down",1,20,20,{10});options.input("pause release",2,20,20,{11});options.input("pause wait",0,0,0,{},5);assert(options.state.paused);
 options.input("se down",1,550,260,{10});options.input("se muted",2,550,260,{11});assert(!options.state.se_level);options.input("se wait",0,0,0,{},5);
 options.input("se off down",1,550,260,{10});options.input("se 25",2,550,260,{11});assert(options.state.se_level==1);options.input("se wait",0,0,0,{},5);
 options.input("rows down",1,500,330,{10});options.input("rows release",2,500,330,{11});assert(options.state.rows==2);options.input("rows wait",0,0,0,{},5);assert(options.state.rows==1);
 options.input("close down",1,700,140,{10});options.input("close release",2,700,140,{11});options.input("close wait",0,0,0,{},5);assert(!options.state.paused);
 auto items=config();items.screen.items=41;items.state.items_on=0;
 for(int x:{960-88,960-176,960-264}){Battle item(items);item.input("item down",1,x,70,{});item.input("item release",2,x,70,{11});item.input("item wait",0,0,0,{},5);}
 std::puts("battle audio inputs equal");
}
