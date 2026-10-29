#include "kbcs_actor.h"
#include <algorithm>
#include "kbcs_battle.h"
#include <array>
#include <climits>
#include <cmath>
#include <cstdint>
#include <stdexcept>
#include <type_traits>
#include <vector>
#include <map>
#include <deque>

#include "actor_pool.inc"

struct KbcsActorHits {
 std::map<int32_t,std::vector<int32_t>> metal,credits;
 bool failed=false;
};

namespace {
// 所有戦闘の同期更新だけへSE通知を接続する。単体APIの結果契約は保つ。
thread_local std::vector<KbcsBattleSound> *activeSounds=nullptr;
thread_local const int32_t *activeSoundFrame=nullptr;
struct BattleSoundScope {
 std::vector<KbcsBattleSound> *previous;const int32_t *frame;
 BattleSoundScope(std::vector<KbcsBattleSound> &sounds,const int32_t &current):previous(activeSounds),frame(activeSoundFrame){activeSounds=&sounds;activeSoundFrame=&current;}
 ~BattleSoundScope(){activeSounds=previous;activeSoundFrame=frame;}
};
void notifySound(int id){if(activeSounds)activeSounds->push_back({*activeSoundFrame,id});}
// 同期する所有戦闘だけが原本のScoreBonusMapを解決する。単体APIは捕捉イベント契約を保持する。
thread_local const KbcsBattleRules *activeRules=nullptr;
thread_local const int32_t *activeMode=nullptr;
struct BattleRulesScope {
 const KbcsBattleRules *previous;const int32_t *mode;
 BattleRulesScope(const KbcsBattleRules &rules,const int32_t &current):previous(activeRules),mode(activeMode){activeRules=&rules;activeMode=&current;}
 ~BattleRulesScope(){activeRules=previous;activeMode=mode;}
};
thread_local int64_t failureAddress=0;
struct AttackFailure {uint32_t code;};
struct Context;
template<class T> struct Cell {
 Context &context;int64_t address;
 operator T() const;
 Cell &operator=(T value);
};
struct Context {
 const KbcsActorDefinition &definition;
 KbcsActorEnvironment &environment;
 KbcsActor (*actors)[51];
 const KbcsSpawnRequest &request;
 uint32_t &seed;
 int32_t procs[12]{};
 const KbcsActorEffectContext *effects=nullptr;
 KbcsActorEffectEvents *events=nullptr;
 const KbcsActorHitContext *hit=nullptr;
 KbcsActorHits *hits=nullptr;
 void reserveMetal(int slot,int rate){if(!hits)throw std::out_of_range("hit owner");hits->metal[slot].push_back(rate);}
 void creditHit(int source,int target){
  if(!hits)throw std::out_of_range("hit owner");
  auto &credits=hits->credits[actorAt(actors,1,target).words[240]];const int serial=actorAt(actors,0,source).words[240];
  if(std::find(credits.begin(),credits.end(),serial)==credits.end())credits.push_back(serial);
 }
 KbcsActorCannon *cannon=nullptr;const KbcsCannonRules *cannonRules=nullptr;
 const KbcsActorClock *clock=nullptr;
 const KbcsActorMotion *motion=nullptr;
 KbcsActorDamageContext *damage=nullptr;
 KbcsActorProtection *protection=nullptr;
 const KbcsActorEnemyDeath *enemyDeath=nullptr;
 KbcsActorEnemyDeathResult *enemyDeathResult=nullptr;
 const KbcsActorRetirement *retirement=nullptr;
 KbcsActorRetirementResult *retirementResult=nullptr;
 int32_t intentBlocked=0;
 KbcsActorAttackSink attackSink=nullptr;void *attackUser=nullptr;int32_t attackEmitted=0;
 int limit() const {return actorCount(actors);}
 void selectAttack(int32_t side,int32_t slot,int32_t hit);
 int enemyCredit(int side,int slot){
  int maximum=0;if(!enemyDeath||!enemyDeathResult)throw std::out_of_range("enemy credit");
  if(!enemyDeath->cohort_present)return 0;
  enemyDeathResult->erase_cohort=1;enemyDeathResult->cohort_serial=actorAt(actors,side,slot).words[240];
  for(int i=0;i<enemyDeath->cohort_count;++i)for(int j=1;j<actorEnd();++j){
   auto &peer=actorAt(actors,1-side,j).words;
   if(peer[240]!=enemyDeath->cohort[i])continue;
   ++peer[241];if(peer[243]>0&&maximum<peer[243]){maximum=peer[243];enemyDeathResult->selected_bonus_slot=j;}
  }
  return maximum;
 }
 const KbcsActorKnockback *knockback=nullptr;
 KbcsActorKnockbackResult *knockbackResult=nullptr;
 const KbcsActorHealth *health=nullptr;
 KbcsActorHealthResult *healthResult=nullptr;
 const KbcsActorReaction *reaction=nullptr;
 KbcsActorReactionResult *reactionResult=nullptr;
 const int32_t *boundary=nullptr;int32_t *transitionSound=nullptr;
 void protectionVisual(int kind,int side,int slot,bool breaker){
  if(!protection||protection->visual_count>=2)throw std::out_of_range("protection visual");
  auto &out=protection->visuals[protection->visual_count++];const auto &actor=actorAt(actors,side,slot);
  out[0]=kind;out[1]=actor.words[3];out[2]=actor.words[4]-(kind?420:0);out[3]=breaker;
 }
 static int divide(int32_t value,int32_t by){
  // ARM64 SDIVの0除算とINT_MIN/-1も未定義動作にしない。
  return !by?0:value==INT32_MIN&&by== -1?INT32_MIN:value/by;
 }
 int clockValue(int64_t address,bool plain) const {
  if(cannonRules){const int offsets[]={0x2d38,0x2d70,0x2da8,0x30d8};for(int i=0;i<4;++i)if(address==offsets[i])return cannonRules->encoded[i];}
  if(motion){
   if(address<0x20000000||address>=0x20000040||address%8)throw std::out_of_range("motion address");
   const int index=int((address-0x20000000)/8);return plain?motion->plain[index]:motion->encoded[index];
  }
  if(!clock)throw std::out_of_range("actor clock");
  const int offsets[]={0x1de8,0x1988,0x1a68,0x2168};
  for(int index=0;index<4;++index)if(address==offsets[index])return plain?clock->plain[index]:clock->encoded[index];
  throw std::out_of_range("actor clock address");
 }
 int effectParameter(int index) const {
  if(!effects||index<0||index>=11)throw std::out_of_range("effect parameter");
  return effects->sage[index];
 }
 int64_t read(int64_t address,int width) const;
 void write(int64_t address,int width,uint64_t value);
 Cell<int32_t> s32(int64_t address){return {*this,address};}
 Cell<uint32_t> u32(int64_t address){return {*this,address};}
 Cell<int64_t> s64(int64_t address){return {*this,address};}
 Cell<uint64_t> u64(int64_t address){return {*this,address};}
 Cell<uint8_t> u8(int64_t address){return {*this,address};}
 Cell<uint16_t> u16(int64_t address){return {*this,address};}
 bool unit() const {return (environment.unit_modes[request.side]&1)!=0;}
 bool hasTalent(int effect) const {
  return unit()&&request.form>=2&&!environment.talents_disabled&&effect>=0&&effect<KBCS_ACTOR_SKILLS&&
      definition.talent_active[effect]&&request.level_index+1>=definition.talent_min_level[effect];
 }
 int talent(int effect,int parameter) const {
  if(parameter<0||parameter>=4)throw std::out_of_range("talent parameter");
  return hasTalent(effect)?definition.talents[effect][parameter]:0;
 }
 int orbValue(int effect,int parameter) const {
  if(effect<0||effect>=KBCS_ACTOR_ORBS||parameter<0||parameter>=4)throw std::out_of_range("orb parameter");
  return hit?hit->orbs[effect][parameter]:definition.orbs[effect][parameter];
 }
 bool orb() const {return request.side==0&&unit()&&request.form>=2&&definition.orb_enabled;}
 int parameter(int id,int) const {return environment.parameters[id];}
 int bossPosition() const {int value=0;if(kbcs_core_spawn_boss_position(environment.castle_x,environment.castle_scale,environment.castle_offset,&value))throw std::range_error("boss position");return value;}
 int combo(int type,int unit_id) const {
  if(type<0||type>=32)throw std::out_of_range("combo");int value=environment.combos[type];
  if(activeRules)for(int i=0;i<activeRules->unit_combo_count;++i){const auto &combo=activeRules->unit_combos[i];if(combo.unit_id==unit_id){value+=combo.values[type];break;}}
  return value;
 }
 int stat(int index,bool castle) const;
};
template<class T> Cell<T>::operator T() const{return T(context.read(address,sizeof(T)));}
template<class T> Cell<T> &Cell<T>::operator=(T value){context.write(address,sizeof(T),uint64_t(value));return *this;}

int64_t n_0081f580(Context &,...){return 0;}
int32_t n_005c2710(Context &c,int64_t address){return c.environment.unit_modes[(address-0x2678)/0x1f0];}
int32_t n_0044abfc(Context &,int32_t a,int32_t b){return std::min(a,b);}
int32_t n_0044abe4(Context &,int32_t a,int32_t b){return std::max(a,b);}
int32_t n_0044beb4(Context &c,int64_t address){return c.clockValue(address,false);}
int32_t n_0044bf2c(Context &c,int64_t address){return c.clockValue(address,true);}
void n_00a9490c(Context &c,int64_t,int32_t side,int32_t slot){
 if(!c.boundary)throw std::out_of_range("actor boundary");
 actorAt(c.actors,side,slot).words[30]=*c.boundary;
 // 00a9490c: 通常の敵限界へボスの出現基準を加える。unit-modeには適用しない。
 if(side==1&&!(c.environment.unit_modes[side]&1)&&actorAt(c.actors,side,slot).words[64])actorAt(c.actors,side,slot).words[30]+=c.bossPosition();
}
void n_00459f04(Context &c,int64_t,int32_t sound){
 // 00459f04は005bc058が0の時だけ再生する。単体APIの状態も同じ判定へ渡す。
 if(activeMode?*activeMode!=0:c.enemyDeath?c.enemyDeath->game_mode!=0:c.knockback&&c.knockback->game_mode!=0)return;
 notifySound(sound);
 if(c.enemyDeathResult){c.enemyDeathResult->sound=sound;return;}
 if(c.transitionSound){*c.transitionSound=sound;return;}
 if(c.reactionResult){
  if(c.reactionResult->sound_count>=2)throw std::out_of_range("reaction sound");
  c.reactionResult->sounds[c.reactionResult->sound_count++]=sound;return;
 }
 if(!c.protection&&activeSounds)return;
 if(!c.protection||c.protection->sound_count>=2)throw std::out_of_range("protection sound");
 c.protection->sounds[c.protection->sound_count++]=sound;
}
int32_t n_005bc058(Context &c){if(c.enemyDeath)return c.enemyDeath->game_mode;if(!c.knockback)throw std::out_of_range("game mode");return c.knockback->game_mode;}
int32_t n_005be130(Context &c,int32_t,int32_t){if(!c.knockback)throw std::out_of_range("unit cost");return c.knockback->cost;}
void n_005c2990(Context &c,int64_t,int32_t amount){if(c.enemyDeathResult){c.enemyDeathResult->money=amount;return;}if(!c.knockbackResult)throw std::out_of_range("unit refund");c.knockbackResult->refund=amount;}
int32_t n_005bc1dc(Context &c,int32_t,int32_t slot){return c.retirement?c.retirement->production_slot:slot;}
int32_t n_00a93074(Context &c,int32_t){if(!c.retirement)throw std::out_of_range("cannon base");return c.retirement->cannon_base;}
void n_006fce54(Context &c,int64_t,int32_t,int32_t kind){if(!c.retirementResult||kind!=1)throw std::out_of_range("death notice");c.retirementResult->death_notice=1;}
int64_t n_005bde34(Context &,int64_t,int32_t,int32_t,int32_t kind){if(kind<0||kind>=8)throw std::out_of_range("motion kind");return 0x20000000+kind*8;}
int32_t n_0044a8d8(Context &c,int32_t bound){int32_t value=0;if(kbcs_core_random_bounded(&c.seed,bound,&value))throw std::range_error("random");return value;}
int32_t n_00457e1c(Context &){return 0;}
void n_00459efc(Context &c,int64_t,int32_t sound,int32_t){notifySound(sound);if(c.enemyDeathResult)c.enemyDeathResult->sound=sound;if(c.healthResult)c.healthResult->sound=sound;if(c.knockbackResult)c.knockbackResult->sound=sound;}
int32_t n_005bbc10(Context &c,...){return c.environment.castle_slot;}
bool n_005bbbc8(Context &c){return c.environment.special_castle>0;}
int32_t n_0063c178(Context &,int64_t){return 0;}
int32_t n_0068c330(Context &c,int64_t,int32_t){if(!c.effects)throw std::out_of_range("effect context");return c.effects->scenario_level-1;}
bool n_008cfcf0(Context &,int64_t,int32_t,int32_t,int32_t){return false;}
int64_t n_0063c480(Context &,int64_t){return 0;}
int32_t n_0063a050(Context &c,int64_t,int32_t effect,int32_t){
 if(c.hit){
  if(effect>=100&&effect<112)return c.hit->base_reductions[effect-100];
  if(effect>=201&&effect<=205&&effect%2)return c.hit->decoration_reductions[(effect-201)/2];
 }
 if(!c.effects||effect<200||effect>206||effect%2)throw std::out_of_range("base effect");return c.effects->base_reductions[(effect-200)/2];
}
int32_t n_0063c21c(Context &,int64_t){return 0;}
int32_t n_0063c3a0(Context &,int64_t){return 0;}
int32_t n_0068c30c(Context &c,int64_t,int32_t){if(!c.hit)throw std::out_of_range("base level");return 0;}
int32_t n_005bce20(Context &c,int32_t,int32_t){if(!c.hit)throw std::out_of_range("hit form");return c.hit->form;}
int32_t n_00663c44(Context &c,int64_t,int32_t,int32_t effect,int32_t parameter,int64_t,int32_t){
 if(!c.hit||effect<0||effect>=5||parameter<0||parameter>1)throw std::out_of_range("targeted orb");
 return c.hit->targeted_orbs[effect][parameter];
}
int32_t n_0058b674(Context &c,int32_t index){if(!c.enemyDeath||index!=8)throw std::out_of_range("accounting level");return c.enemyDeath->accounting_level;}
int32_t n_005bbba0(Context &c){if(!c.enemyDeath)throw std::out_of_range("score limit");return c.enemyDeath->limit;}
bool n_005e1400(Context &c,int64_t){if(!c.enemyDeath)throw std::out_of_range("score enabled");return c.enemyDeath->score_enabled;}
bool n_006440f0(Context &c,int64_t,int32_t,int32_t){if(!c.enemyDeath)throw std::out_of_range("money rule");return c.enemyDeath->money_disabled;}
int32_t n_007cf950(Context &c,int32_t){if(!c.enemyDeath)throw std::out_of_range("map source");return 0;}
int32_t n_00a5b084(Context &c,int64_t,int32_t type){if(type<0||type>=32)throw std::out_of_range("treasure");return c.environment.treasures[type];}
int32_t n_00a5b1b4(Context &c,int64_t,int32_t type,int32_t){
 if(c.hit){if(type<0||type>=32)throw std::out_of_range("fruit type");return c.hit->fruit_rates[type];}
 if(!c.effects)throw std::out_of_range("fruit");return c.effects->fruit;
}
bool n_005bc198(Context &c){return c.effects&&c.effects->notifications&&(!activeMode||*activeMode!=4);}
bool n_009d49e4(Context &c,int64_t){return c.enemyDeath?c.enemyDeath->notifications:c.effects&&c.effects->notifications;}
int32_t n_00a960ac(Context &c,int32_t,int32_t){if(!c.effects)throw std::out_of_range("target count");return c.effects->target_count;}
int32_t n_009d4e1c(Context &c,int64_t,int32_t type,int32_t count){
 if(!c.events||c.events->count>=16)throw std::out_of_range("effect events");
 const int index=c.events->count++;c.events->events[index][0]=type;c.events->events[index][1]=count;
 if(activeRules){int32_t value=0;const auto code=kbcs_core_battle_bonus(activeRules,type,count,&value);if(code)throw AttackFailure{code};return value;}return index+1;
}
bool n_005c2ec0(Context &c,...){return c.orb();}
int32_t n_0066398c(Context &c,int64_t,int32_t,int32_t effect,int32_t parameter,int32_t){return c.orbValue(effect,parameter);}
int32_t n_00663af4(Context &c,int64_t,int32_t,int32_t effect,int32_t parameter,int32_t){return c.orbValue(effect,parameter);}
bool n_0066367c(Context &c,int64_t,int32_t,int32_t effect){c.orbValue(effect,0);return (c.hit?c.hit->orb_present[effect]:c.definition.orb_present[effect])!=0;}
int32_t n_0088f9e4(Context &c,int64_t,int32_t type,int32_t unit_id){return c.combo(type,unit_id);}
int32_t n_00a9f0e0(Context &c,int32_t,int32_t,int32_t,int32_t effect,int32_t parameter){return c.talent(effect,parameter);}
bool n_00aa2c2c(Context &c,int64_t,int32_t,int32_t,int32_t effect){return c.hasTalent(effect);}
bool n_00aa4fb0(Context &c,int64_t,int32_t,int32_t,uint32_t mask){return c.request.form>=2&&!c.environment.talents_disabled&&(c.definition.added_targets&mask)!=0;}
uint32_t n_00a9e9fc(Context &c,int32_t,int32_t,int32_t,uint32_t,int32_t){return c.stat(0,false);}
uint32_t n_00a9fb88(Context &c,int32_t,int32_t,int32_t,uint32_t,int32_t,int32_t hit,uint32_t,uint32_t castle){
 if(c.hit){if(hit<0||hit>2)throw std::out_of_range("raw attack");return c.hit->raw_attack[hit];}
 return c.stat(hit+1,castle!=0);
}
int32_t n_00a9f9fc(Context &c,int32_t,int32_t,int32_t){
 const auto &d=c.definition;int64_t speed=d.cells[2];
 if(c.unit())speed=(speed+int64_t(c.talent(27,0))*2)*(100+c.combo(2,c.request.raw-2))/100;
 if(speed&&d.speed_rule==1)speed=int64_t(d.speed_value)*2;
 else if(speed&&d.speed_rule==2)speed=speed*d.speed_value/100;
 if(speed<INT32_MIN||speed>INT32_MAX)throw std::range_error("speed");
 return int32_t(speed);
}
int32_t n_00aa68ec(Context &c,int32_t,int32_t,int32_t,int32_t){
 if(c.unit())return 0;
 KbcsEnemyStatInput input{c.definition.cells[87],c.environment.hp_percent,c.environment.crown,0,0,0};
 KbcsEnemyStatOutput output{};
 if(c.environment.stage_kind<3&&!c.environment.zombie)return int32_t((int64_t(input.base)*(c.environment.chapter_rate+10)+5)/10);
 if(c.environment.stage_kind!=3)input.crown_percent=100;
 if(kbcs_core_enemy_stat(&input,&output))throw std::range_error("shield");
 return int32_t(output.stages[2]);
}

#include "actor_generated.inc"

void Context::selectAttack(int32_t side,int32_t slot,int32_t hit){
 struct Target {int32_t slot,metric;};
 std::array<Target,51> regular{};std::vector<Target> extra;Target *candidates=regular.data();if(limit()>51){extra.resize(limit());candidates=extra.data();}int count=0;
 for(int target=0;target<actorEnd();++target){
  if(!n_006dda04(*this,0,side,slot,target,hit))continue;
  if(!side&&n_00a97c8c(*this,0,slot)){
   const bool matches=n_00a962a8(*this,0,slot,target)&1;
   if(target&&!matches&&target!=n_005bbc10(*this))continue;
  }
  const auto &words=actorAt(actors,1-side,target).words;
  candidates[count++]={target,side?words[3]+words[14]:words[3]-words[14]};
 }
 if(!count)return;
 KbcsActorAttackSelection selection{};std::vector<int> targets;selection.side=side;selection.slot=slot;selection.hit=hit;
 if(!n_00a97980(*this,side,slot)){
  // 原本の選択ソートと同率時の順序を保つ。範囲1でも抽選を省略しない。
  std::fill_n(procs,12,0);
  for(int i=0;i<count-1;++i){
   int best=i;
   for(int j=i+1;j<count;++j)if(side?candidates[j].metric<candidates[best].metric:candidates[best].metric<candidates[j].metric)best=j;
   std::swap(candidates[i],candidates[best]);
  }
  int ties=1;while(ties<count&&candidates[ties].metric==candidates[0].metric)++ties;
  selection.count=1;selection.targets[0]=candidates[n_0044a8d8(*this,ties)].slot;
 }else{
  selection.count=std::min(count,51);for(int i=0;i<selection.count;++i)selection.targets[i]=candidates[i].slot;
  if(count>51){targets.reserve(count);for(int i=0;i<count;++i)targets.push_back(candidates[i].slot);}
 }
 if(!attackSink)throw std::out_of_range("attack sink");
 ActorTargetScope selected(selection,targets);++attackEmitted;const uint32_t code=attackSink(attackUser,actors,&seed,&selection);
 if(code||!seed)throw AttackFailure{code?code:1};
}

void emitDirect(Context &context,const KbcsActorAttackSelection &selection,KbcsActorHitSink sink,void *user,KbcsActorEmission &result){
 const int side=selection.side,slot=selection.slot,hit=selection.hit;
 n_006e9c88(context,0,side,slot,hit);std::copy_n(context.procs,12,result.flags);
 result.parameter=side?0:n_00a9adf0(context,0,slot);
 const bool extended=&selection==extendedSelection&&extendedTargets&&!extendedTargets->empty();
 const int count=extended?int(extendedTargets->size()):selection.count;
 for(int i=0;i<count;++i){
  const int target=extended?(*extendedTargets)[i]:selection.targets[i];
  KbcsActorDirectHit call{};call.side=side;call.slot=slot;call.target=target;call.hit=hit;call.rate=100;call.parameter=result.parameter;
  std::copy_n(result.flags,12,call.flags);
  // 味方の直接命中には敵専用の毒撃/再生産遅延を渡さない。後続効果には元の12値を保持する。
  if(!side){call.flags[9]=0;call.flags[11]=0;}
  int32_t applied=0;const uint32_t code=sink(user,context.actors,&context.seed,&call,&applied);
  if(code||!context.seed||applied<0||applied>1)throw AttackFailure{code?code:1};
  if(!applied)continue;
  int marker;
  if(!side&&n_00a94630(context,0,slot)&&n_00a94234(context,1,target)==14)marker=2;
  else marker=n_00a97f6c(context,side,slot,hit)&1;
  actorAt(context.actors,1-side,target).words[96]=marker;
 }
}
#include "actor_rom.inc"

int Context::stat(int index,bool castle) const {
 const int columns[2][4]={{0,3,55,56},{0,3,59,60}};
 const int base=definition.cells[columns[unit()][index]];
 if(unit()){
  int64_t growth=100;
  for(int level=1;level<request.level_index+1&&level<200;++level)growth+=definition.growth[level/10];
  int talentBonus=talent(index?31:32,0);
  if(request.form>=2&&environment.orb_stage)talentBonus+=orbValue(environment.orb_stage,index?1:0);
  KbcsStatInput input{base,int32_t(growth),environment.treasures[index?10:9],combo(index?0:1,request.raw-2),talentBonus,talent(index?70:71,0)};
  KbcsStatOutput output{};
  if(growth>INT32_MAX||kbcs_core_stat(&input,&output))throw std::range_error("unit stat");
  return int(output.stages[5]);
 }
 if(environment.stage_kind<3&&!environment.zombie)return int32_t((int64_t(base)*(environment.chapter_rate+10)+5)/10);
 const int star=definition.cells[69];int crystal=-1;
 if(definition.cells[18]&&star==0)crystal=0;
 else if(definition.cells[18]&&star==1)crystal=1;
 else if(star>=2&&star<=4)crystal=star;
 KbcsEnemyStatInput input{base,index&&environment.attack_percent?environment.attack_percent:environment.hp_percent,
     environment.stage_kind==3?environment.crown:100,crystal<0?0:environment.crystal_max[crystal],crystal<0?0:environment.crystal[crystal],int(index&&castle)};
 KbcsEnemyStatOutput output{};
 if(kbcs_core_enemy_stat(&input,&output))throw std::range_error("enemy stat");
 return int(output.stages[2]);
}

int64_t Context::read(int64_t address,int width) const {
 if(address>=actorBase&&address<actorBase+2*actorStride&&(width==1||width==2)){
  const int side=int((address-actorBase)/actorStride),index=int((address-actorBase)%actorStride),byte=index%4;if(byte+width>4)throw std::out_of_range("actor read bytes");
  return (uint32_t(actorAt(actors,side,index/0x3ec).words[index%0x3ec/4])>>(byte*8))&((1U<<(width*8))-1);
 }
 // 未解決のアドレスを0に補完しない。分岐の追加時は原本と対応付けて拡張する。
 if((width!=4&&width!=8)||address%4){failureAddress=address;throw std::out_of_range("actor read width");}
 if(cannon&&address>=0x9d788&&address+width<=0x9d8f0&&width==4)return cannon->segments[(address-0x9d788)/180][(address-0x9d788)%180/12][(address-0x9d788)%12/4];
 if(address>=actorBase&&address<actorBase+2*actorStride){
  const int side=int((address-actorBase)/actorStride),offset=int((address-actorBase)%actorStride);
  if(offset%0x3ec+width>0x3ec){failureAddress=address;throw std::out_of_range("actor address");}
  const auto &record=actorAt(actors,side,offset/0x3ec).words;const int word=(offset%0x3ec)/4;
  uint64_t value=uint32_t(record[word]);if(width==8)value|=uint64_t(uint32_t(record[word+1]))<<32;
  return width==4?int32_t(value):int64_t(value);
 }
 const int64_t first=unit()?0x9ee88+int64_t(request.raw)*0x770+request.form*0x1dc:0x239da8+int64_t(request.raw)*0x1c4;
 if(address>=first&&address<first+int64_t(unit()?119:113)*4&&width==4)return definition.cells[(address-first)/4];
 if(enemyDeath){
  if(address==0x32ec&&width==4)return enemyDeathResult->score;
  if(address==0x32f0&&width==4)return enemyDeath->timer;
 }
 if(address==0x284c||address==0x2a3c)return environment.spawned[address==0x284c?0:1];
 if(address==0x9ee48)return environment.stage_width;
 if(address==0x4dc)return -1;
 if(address==0x9ee70)return 0x10000000;
 if(damage){
  if(address==0x9ee68)return damage->guard_enabled;
  if(address==0x9ee78)return 0x10000000+int64_t(damage->count)*56;
  if(address==0x84050)return 0x11000000;
  if((address==0x898||address==0x89c)&&width==4)return damage->notice[(address-0x898)/4];
  if(address>=0x10000000&&address+width<=0x10000000+int64_t(damage->count)*56&&width==4){
   const int index=int((address-0x10000000)/4);return damage->rows[index/14].cells[index%14];
  }
  if(address>=0x11000000&&address+width<=0x11000000+int64_t(damage->count)*12&&width==4){
   const int index=int((address-0x11000000)/4);const auto &state=damage->states[index/3];
   return index%3==0?state.wait:index%3==1?state.spawned:state.kills;
  }
 }
 if(address>=0x38fb8c&&address+width<=0x38fbbc){
  uint64_t value=uint32_t(procs[(address-0x38fb8c)/4]);
  if(width==8)value|=uint64_t(uint32_t(procs[(address-0x38fb8c)/4+1]))<<32;
  return int64_t(value);
 }
 const int64_t row=0x10000000+int64_t(request.row)*0x38;
 if(address>=row&&address<row+0x38&&width==4)return environment.spawn_row[(address-row)/4];
 const auto entry=std::lower_bound(std::begin(actorRom),std::end(actorRom),address,[](auto value,int64_t key){return value.first<key;});
 if(entry!=std::end(actorRom)&&entry->first==address&&width==4)return entry->second;
 failureAddress=address;throw std::out_of_range("unresolved actor address");
}
void Context::write(int64_t address,int width,uint64_t value){
 if(address>=actorBase&&address<actorBase+2*actorStride&&(width==1||width==2)){
  const int side=int((address-actorBase)/actorStride),index=int((address-actorBase)%actorStride),byte=index%4;if(byte+width>4)throw std::out_of_range("actor write bytes");
  auto &word=actorAt(actors,side,index/0x3ec).words[index%0x3ec/4];const uint32_t mask=((1U<<(width*8))-1)<<(byte*8);
  word=int32_t((uint32_t(word)&~mask)|((uint32_t(value)<<(byte*8))&mask));return;
 }
 if(cannon&&address>=0x9d788&&address+width<=0x9d8f0&&width==4){cannon->segments[(address-0x9d788)/180][(address-0x9d788)%180/12][(address-0x9d788)%12/4]=int32_t(value);return;}
 if((width!=4&&width!=8)||address%4){failureAddress=address;throw std::out_of_range("actor write width");}
 if(address>=actorBase&&address<actorBase+2*actorStride){
  const int side=int((address-actorBase)/actorStride),offset=int((address-actorBase)%actorStride);
  if(offset%0x3ec+width>0x3ec){failureAddress=address;throw std::out_of_range("actor address");}
  auto &record=actorAt(actors,side,offset/0x3ec).words;const int word=(offset%0x3ec)/4;
  record[word]=int32_t(value);if(width==8)record[word+1]=int32_t(value>>32);return;
 }
 if(enemyDeathResult&&address==0x32ec&&width==4){enemyDeathResult->score=int32_t(value);return;}
 if(address==0x284c||address==0x2a3c){environment.spawned[address==0x284c?0:1]=int32_t(value);return;}
 if(damage&&(address==0x898||address==0x89c)&&width==4){damage->notice[(address-0x898)/4]=int32_t(value);return;}
 if(address>=0x38fb8c&&address+width<=0x38fbbc){
  procs[(address-0x38fb8c)/4]=int32_t(value);
  if(width==8)procs[(address-0x38fb8c)/4+1]=int32_t(value>>32);
  return;
 }
 failureAddress=address;throw std::out_of_range("unresolved actor write");
}
}

extern "C" uint32_t kbcs_core_actor_initialize(const KbcsActorDefinition *definition,
    KbcsActorEnvironment *environment,KbcsActor actors[2][51],const KbcsSpawnRequest *request,
    uint32_t *seed,int32_t *slot){
 if(!definition||!environment||!actors||!request||!seed||!*seed||!slot)return 1;
 if(request->side<0||request->side>1||(request->raw<2&&request->raw!=-1)||request->form<0||request->form>3||request->level_index<0||request->level_index>199||request->row<0||request->row>4095||definition->count<0||definition->count>119||environment->stage_width<2800)return 1;
 if(int64_t(request->layer_max)-request->layer_min>INT32_MAX-1||int64_t(request->layer_max)-request->layer_min<INT32_MIN)return 2;
 failureAddress=0;
 int free_slot=-1;
 for(int index=1;index<actorEnd();++index)if(!actorAt(actors,request->side,index).words[0]){free_slot=index;break;}
 const auto backup=free_slot>0?actorAt(actors,request->side,free_slot):KbcsActor{};
 const auto previous_seed=*seed;const int32_t counts[]={environment->spawned[0],environment->spawned[1]};
 const auto restore=[&]{if(free_slot>0)actorAt(actors,request->side,free_slot)=backup;*seed=previous_seed;std::copy_n(counts,2,environment->spawned);};
 try{Context context{*definition,*environment,actors,*request,*seed};*slot=int32_t(n_009f1e64(context,0,request->side,request->raw,request->level_index,request->layer_min,request->layer_max,request->form,request->row));return 0;}
 catch(const std::range_error &){restore();return 2;}catch(...){restore();return 3;}
}
extern "C" int64_t kbcs_core_actor_last_error(){return failureAddress;}

#include "actor_secondary.inc"
#include "actor_wave.inc"
#include "actor_cannon.inc"

extern "C" uint32_t kbcs_core_actor_hits_create(KbcsActorHits **out){
 if(!out)return 1;try{*out=new KbcsActorHits;return 0;}catch(...){return 3;}
}
extern "C" void kbcs_core_actor_hits_destroy(KbcsActorHits *owner){delete owner;}
extern "C" uint32_t kbcs_core_actor_hits_values(const KbcsActorHits *owner,int32_t kind,int32_t key,int32_t *values,int32_t capacity,int32_t *count){
 if(!owner||!count||kind<0||kind>1||capacity<0||(!values&&capacity))return 1;
 const auto &entries=kind?owner->credits:owner->metal;const auto found=entries.find(key);
 const auto size=found==entries.end()?0:found->second.size();if(size>INT32_MAX)return 2;
 *count=int32_t(size);if(size>size_t(capacity))return capacity?1:0;
 if(size)std::copy(found->second.begin(),found->second.end(),values);return 0;
}
extern "C" uint32_t kbcs_core_actor_hits_erase(KbcsActorHits *owner,int32_t kind,int32_t key){
 if(!owner||kind<0||kind>1)return 1;(kind?owner->credits:owner->metal).erase(key);return 0;
}
extern "C" uint32_t kbcs_core_actor_hit(KbcsActorHits *owner,KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
 const KbcsActorHitContext *hit,const KbcsActorClock *clock,KbcsActorDamageContext *damage,
 const KbcsActorSecondaryHit *call,uint32_t *seed,int32_t *applied,KbcsActorEffectEvents *out){
 if(!owner||owner->failed||!actors||!environment||!hit||!clock||!damage||!call||!seed||!*seed||!applied||!out)return 1;
 const auto &input=call->hit;
 if(input.side<0||input.side>1||input.slot<1||input.slot>=actorEnd()||input.target<0||input.target>=actorEnd()||input.hit<0||input.hit>2||input.kind<0||input.kind>2||call->attack_type<0||call->attack_type>3||damage->count<0||(!damage->rows&&damage->count)||(!damage->states&&damage->count))return 1;
 for(auto flag:input.flags)if(flag<0||flag>1)return 1;
 if(hit->form<0||hit->form>3||hit->effects.target_count<1||hit->effects.target_count>12)return 1;
 try{
  const KbcsActorDefinition definition{};KbcsSpawnRequest request{};auto copy=*environment;KbcsActorEffectEvents events{};
  Context context{definition,copy,actors,request,*seed};context.hit=hit;context.hits=owner;context.effects=&hit->effects;context.events=&events;context.clock=clock;context.damage=damage;
  const auto &f=input.flags;uint32_t result;
  if(input.side)result=n_006e79bc(context,0,call->attack_type,input.slot,input.target,input.hit,input.kind,f[0],f[5],f[1],f[2],f[3],f[4],f[6],f[8],f[7],f[9],f[10],f[11],input.rate);
  else result=n_006e4aec(context,0,call->attack_type,input.slot,input.target,input.hit,input.kind,f[0],f[5],f[1],f[2],f[3],f[4],f[6],f[8],f[7],0,f[10],input.parameter,input.rate);
  *applied=int32_t(result);*out=events;return 0;
 }catch(...){owner->failed=true;return 3;}
}

extern "C" uint32_t kbcs_core_actor_emit_area(const KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    const KbcsActorAttackSelection *source,const KbcsActorEmission *emission,uint32_t *seed,KbcsActorAreaEmission *out){
 static_assert(sizeof(KbcsActorSurge)==48&&sizeof(KbcsActorExplosion)==36);
 if(!actors||!environment||!source||!emission||!seed||!*seed||!out||source->side<0||source->side>1||source->slot<1||source->slot>=actorEnd()||source->hit<0||source->hit>2)return 1;
 for(int flag:emission->flags)if(flag<0||flag>1)return 1;
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};
  Context context{definition,copy,const_cast<KbcsActor (*)[51]>(actors),request,*seed};KbcsActorAreaEmission result{};
  const int side=source->side,actor=source->slot,hit=source->hit;
  if(n_00a95f08(context,side,actor,hit)){
   const auto position=[&](int32_t offset,int32_t span){
    // CNEGのINT_MINも32bitのまま保持。0/負の抽選範囲はRNGを進めない。
    const int32_t bound=span<0?-span:span;
    const int32_t x=n_00a9482c(context,side,actor);
    const int32_t draw=n_0044a8d8(context,bound);
    const int32_t delta=(side?span<1:span>0)?-draw:draw;
    return (side?x+offset:x-offset)+delta;
   };
   const auto flags=[&](uint8_t *target){
    for(int i=0;i<12;++i)target[i]=uint8_t(emission->flags[storedProcOrder[i]]);
   };
   if(int32_t(n_00a98838(context,side,actor))>0&&n_0044a8d8(context,100)<int32_t(n_00a98838(context,side,actor))){
    auto &surge=result.surge;result.surge_present=1;
    surge.side=side;surge.slot=actor;surge.hit=hit;
    surge.x=position(n_00a988c4(context,side,actor),n_00a98950(context,side,actor));
    surge.level=n_00a989dc(context,side,actor);flags(surge.flags);
    surge.parameter=side?0:emission->parameter;surge.mini=n_00a987f8(context,side,actor)!=0;
   }
   if(int32_t(n_00a98f70(context,side,actor))>0&&n_0044a8d8(context,100)<int32_t(n_00a98f70(context,side,actor))){
    auto &explosion=result.explosion;result.explosion_present=1;
    explosion.side=side;explosion.slot=actor;explosion.hit=hit;
    explosion.x=position(n_00a98ffc(context,side,actor),n_00a99088(context,side,actor));
    flags(explosion.flags);explosion.parameter=side?0:emission->parameter;
   }
  }
  *out=result;return 0;
 }catch(...){return 3;}
}

extern "C" uint32_t kbcs_core_actor_emit_wave(const KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    const KbcsActorAttackSelection *source,const KbcsActorEmission *emission,KbcsActorWaves *waves,uint32_t *seed,int32_t *slot){
 static_assert(sizeof(KbcsActorWave)==48);
 if(!actors||!environment||!source||!emission||!waves||!seed||!*seed||!slot||source->side<0||source->side>1||source->slot<1||source->slot>=actorEnd()||source->hit<0||source->hit>2)return 1;
 for(int flag:emission->flags)if(flag<0||flag>1)return 1;
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};
  Context context{definition,copy,const_cast<KbcsActor (*)[51]>(actors),request,*seed};int result= -1;
  const int side=source->side,actor=source->slot,hit=source->hit;
  if(n_00a95f08(context,side,actor,hit)&&int32_t(n_00a97b38(context,side,actor))>0){
   const int roll=n_0044a8d8(context,100);
   if(roll<int32_t(n_00a97b38(context,side,actor)))for(int i=0;i<200;++i){
    auto &wave=waves->records[i];if(wave.side||wave.state)continue;
    wave.side=side+1;wave.slot=actor;wave.state=side+1;wave.frame=0;
    wave.x=n_00a9482c(context,side,actor);wave.level=n_00a97b78(context,side,actor);wave.hit=hit;
    for(int j=0;j<12;++j)wave.flags[j]=uint8_t(emission->flags[storedProcOrder[j]]);
    wave.parameter=side?0:emission->parameter;wave.mini=n_00a97a14(context,side,actor)==1;
    for(auto &row:waves->hits)row[i]=0;if(activePool)for(auto &row:activePool->extra)row.waves[i]=0;
    result=i;break;
   }
  }
  *slot=result;return 0;
 }catch(...){return 3;}
}

extern "C" uint32_t kbcs_core_actor_emit_direct(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    const KbcsActorAttackSelection *selection,uint32_t *seed,KbcsActorHitSink sink,void *user,KbcsActorEmission *out){
 if(!actors||!environment||!selection||!seed||!*seed||!sink||!out||selection->side<0||selection->side>1||selection->slot<1||selection->slot>=actorEnd()||selection->hit<0||selection->hit>2||selection->count<0||selection->count>51)return 1;
 for(int i=0;i<selection->count;++i)if(selection->targets[i]<0||selection->targets[i]>=actorEnd())return 1;
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};KbcsActorEmission result{};
  Context context{definition,copy,actors,request,*seed};emitDirect(context,*selection,sink,user,result);*out=result;return 0;
 }catch(const AttackFailure &failure){return failure.code;}catch(...){return 3;}
}

extern "C" uint32_t kbcs_core_actor_attack(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    int32_t side,int32_t slot,const KbcsActorMotion *motion,uint32_t *seed,KbcsActorAttackSink sink,void *user,KbcsActorAttackResult *out){
 if(!actors||!environment||!motion||!seed||!*seed||!sink||!out||side<0||side>1||slot<1||slot>=actorEnd())return 1;
 KbcsActorAttackResult result{};const auto &words=actorAt(actors,side,slot).words;
 if(!words[0]||words[1]!=2||words[61]>0){*out=result;return 0;}
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};
  Context context{definition,copy,actors,request,*seed};context.motion=motion;context.attackSink=sink;context.attackUser=user;
  if(side)n_006d8cf8(context,0,0,slot);else n_006d8584(context,0,0,slot);
  result.handled=1;result.emitted=context.attackEmitted;*out=result;return 0;
 }catch(const AttackFailure &failure){return failure.code;}catch(...){return 3;}
}

extern "C" uint32_t kbcs_core_actor_attack_wait(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    int32_t side,int32_t slot,const KbcsActorMotion *motion,int32_t burrow_blocked,int32_t *handled){
 if(!actors||!environment||!motion||!handled||side<0||side>1||slot<1||slot>=actorEnd()||burrow_blocked<0||burrow_blocked>1)return 1;
 const auto backup=actorAt(actors,side,slot);
 if(!backup.words[0]||backup.words[1]!=1||backup.words[61]>0){*handled=0;return 0;}
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,copy,actors,request,seed};context.motion=motion;context.intentBlocked=burrow_blocked;
  if(side)n_006d8cc0(context,0,0,slot);else n_006d8558(context,0,0,slot);
  *handled=1;return 0;
 }catch(...){actorAt(actors,side,slot)=backup;return 3;}
}

extern "C" uint32_t kbcs_core_actor_intent(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,int32_t *burrow_blocked){
 if(!actors||!environment||!burrow_blocked)return 1;
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,copy,actors,request,seed};n_006d823c(context,0);*burrow_blocked=context.intentBlocked;return 0;
 }catch(...){return 3;}
}

extern "C" uint32_t kbcs_core_actor_retire(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    int32_t side,int32_t slot,const KbcsActorRetirement *input,KbcsActorRetirementResult *out){
 if(!actors||!environment||!input||!out||side<0||side>1||slot<1||slot>=actorEnd()||input->blocked<0||input->blocked>1||input->production_slot<0||input->production_slot>20)return 1;
 const auto backup=actorAt(actors,side,slot);KbcsActorRetirementResult result{};result.production_slot= -1;result.cannon_remaining=input->cannon_remaining;
 if(!backup.words[0]||backup.words[1]!=4){*out=result;return 0;}
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,copy,actors,request,seed};context.retirement=input;context.retirementResult=&result;
  if(environment->unit_modes[side]&1)n_006ebb0c(context,0,0,side,slot);else n_006ed5e0(context,0,0,side,slot);
  result.handled=1;*out=result;return 0;
 }catch(...){actorAt(actors,side,slot)=backup;return 3;}
}

extern "C" uint32_t kbcs_core_actor_enemy_knockback(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    int32_t side,int32_t slot,const KbcsActorEnemyDeath *input,KbcsActorEnemyDeathResult *out){
 if(!actors||!environment||!input||!out||side<0||side>1||slot<1||slot>=actorEnd()||input->cohort_count<0||(input->cohort_count&&!input->cohort))return 1;
 for(int value:{input->quiet,input->score_enabled,input->notifications,input->money_disabled,input->recording,input->cohort_present})if(value<0||value>1)return 1;
 const auto backup=actorAt(actors,side,slot);KbcsActorEnemyDeathResult result{};result.selected_bonus_slot=result.bonus_visual_slot=result.cohort_serial=result.sound= -1;result.score=input->score;
 if(!backup.words[0]||(environment->unit_modes[side]&1)||backup.words[1]!=3){*out=result;return 0;}
 std::array<int32_t,51> regular{};std::vector<int32_t> extra;int32_t *kills=regular.data();if(actorEnd()>51){extra.resize(actorEnd());kills=extra.data();}for(int i=0;i<actorEnd();++i)kills[i]=actorAt(actors,1-side,i).words[241];
 try{
  KbcsActorDefinition definition{};definition.cells[6]=input->money_base;auto copy=*environment;KbcsSpawnRequest request{};request.side=side;request.raw=backup.words[0];uint32_t seed=1;
  Context context{definition,copy,actors,request,seed};context.boundary=&input->boundary;context.enemyDeath=input;context.enemyDeathResult=&result;
  n_006ed43c(context,0,0,side,slot);result.handled=1;*out=result;return 0;
 }catch(...){actorAt(actors,side,slot)=backup;for(int i=0;i<actorEnd();++i)actorAt(actors,1-side,i).words[241]=kills[i];return 3;}
}

extern "C" uint32_t kbcs_core_actor_enemy_displacement(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    int32_t side,int32_t slot,int32_t boundary,int32_t *handled){
 if(!actors||!environment||!handled||side<0||side>1||slot<1||slot>=actorEnd())return 1;
 const auto backup=actorAt(actors,side,slot);const auto action=backup.words[1];
 if(!backup.words[0]||(environment->unit_modes[side]&1)||(action!=5&&action!=6)){*handled=0;return 0;}
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,copy,actors,request,seed};context.boundary=&boundary;
  n_006ed8d4(context,0,0,side,slot);*handled=1;return 0;
 }catch(...){actorAt(actors,side,slot)=backup;return 3;}
}

extern "C" uint32_t kbcs_core_actor_unit_knockback(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    int32_t side,int32_t slot,const KbcsActorKnockback *input,KbcsActorKnockbackResult *out){
 if(!actors||!environment||!input||!out||side<0||side>1||slot<1||slot>=actorEnd()||input->cost<0)return 1;
 const auto backup=actorAt(actors,side,slot);const auto action=backup.words[1];KbcsActorKnockbackResult result{0,0,-1};
 if(!backup.words[0]||!(environment->unit_modes[side]&1)||(action!=3&&action!=5&&action!=6&&action!=7)){*out=result;return 0;}
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,copy,actors,request,seed};context.knockback=input;context.knockbackResult=&result;context.boundary=&input->boundary;
  n_006eb7e0(context,0,0,side,slot);result.handled=1;*out=result;return 0;
 }catch(...){actorAt(actors,side,slot)=backup;return 3;}
}

extern "C" uint32_t kbcs_core_actor_walk(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,int32_t side,int32_t slot,int32_t *handled){
 if(!actors||!environment||!handled||side<0||side>1||slot<1||slot>=actorEnd())return 1;
 const auto backup=actorAt(actors,side,slot);const auto action=backup.words[1];const bool unit_mode=(environment->unit_modes[side]&1)!=0;
 if(!backup.words[0]||(action!=0&&(unit_mode||action<11||action>16))){*handled=0;return 0;}
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,copy,actors,request,seed};
  if(unit_mode)n_006eb8c0(context,0,0,side,slot);else n_006ecfec(context,0,0,side,slot);
  *handled=1;return 0;
 }catch(...){actorAt(actors,side,slot)=backup;return 3;}
}

extern "C" uint32_t kbcs_core_actor_begin(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,int32_t side,int32_t slot){
 if(!actors||!environment||side<0||side>1||slot<0||slot>=actorEnd())return 1;
 const auto backup=actorAt(actors,side,slot);
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,copy,actors,request,seed};n_006eb6b0(context,0,side,slot);return 0;
 }catch(...){actorAt(actors,side,slot)=backup;return 3;}
}

extern "C" uint32_t kbcs_core_actor_react(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    int32_t side,int32_t slot,const KbcsActorReaction *input,uint32_t *seed,KbcsActorReactionResult *out){
 if(!actors||!environment||!input||!seed||!*seed||!out||side<0||side>1||slot<0||slot>=actorEnd())return 1;
 const auto backup=actorAt(actors,side,slot);const auto previous_seed=*seed;
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};
  KbcsActorReactionResult result{};Context context{definition,copy,actors,request,*seed};context.reaction=input;context.reactionResult=&result;
  if(slot&&actorAt(actors,side,slot).words[19])n_006dac8c(context,0,side,slot);
  *out=result;return 0;
 }catch(...){actorAt(actors,side,slot)=backup;*seed=previous_seed;return 3;}
}

extern "C" uint32_t kbcs_core_actor_health(KbcsActor actors[2][51],int32_t side,int32_t slot,
    const KbcsActorHealth *input,uint32_t *seed,KbcsActorHealthResult *out){
 if(!actors||!input||!seed||!*seed||!out||side<0||side>1||slot<0||slot>=actorEnd()||input->deployment_slot< -1||input->deployment_slot>20)return 1;
 if(side==0&&actorAt(actors,side,slot).words[248]>0&&input->cooldown>0&&input->deployment_slot<0)return 1;
 const auto backup=actorAt(actors,side,slot);const auto previous_seed=*seed;
 try{
  KbcsActorDefinition definition{};KbcsActorEnvironment environment{};KbcsSpawnRequest request{};
  KbcsActorHealthResult result{};result.delay_slot= -1;result.sound= -1;
  Context context{definition,environment,actors,request,*seed};context.health=input;context.healthResult=&result;
  n_006da994(context,0,side,slot);*out=result;return 0;
 }catch(...){actorAt(actors,side,slot)=backup;*seed=previous_seed;return 3;}
}

extern "C" uint32_t kbcs_core_actor_protect(KbcsActor actors[2][51],int32_t side,int32_t slot,KbcsActorProtection *out){
 if(!actors||!out||side<0||side>1||slot<0||slot>=actorEnd())return 1;
 const auto backup=actorAt(actors,side,slot);
 try{
  KbcsActorDefinition definition{};KbcsActorEnvironment environment{};KbcsSpawnRequest request{};uint32_t seed=1;
  KbcsActorProtection result{};Context context{definition,environment,actors,request,seed};context.protection=&result;
  n_006d97dc(context,side,slot);*out=result;return 0;
 }catch(...){actorAt(actors,side,slot)=backup;return 3;}
}

extern "C" uint32_t kbcs_core_actor_damage(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    KbcsActorDamageContext *damage,int32_t side,int32_t slot,int32_t amount){
 if(!actors||!environment||!damage||side<0||side>1||slot<0||slot>=actorEnd()||amount<0||damage->count<0||damage->count>4096||(damage->count&&(!damage->rows||!damage->states)))return 1;
 const auto backup=actorAt(actors,side,slot);const int32_t notice[]={damage->notice[0],damage->notice[1]};
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,copy,actors,request,seed};context.damage=damage;
  n_00a9bbac(context,side,slot,amount);return 0;
 }catch(...){actorAt(actors,side,slot)=backup;std::copy_n(notice,2,damage->notice);return 3;}
}

extern "C" uint32_t kbcs_core_actor_motion(KbcsActor actors[2][51],int32_t side,int32_t slot,const KbcsActorMotion *motion){
 if(!actors||!motion||side<0||side>1||slot<1||slot>=actorEnd())return 1;
 try{
  KbcsActorDefinition definition{};KbcsActorEnvironment environment{};KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,environment,actors,request,seed};context.motion=motion;
  n_009f4688(context,0,0,side,slot);return 0;
 }catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_actor_transition(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    int32_t side,int32_t slot,const KbcsActorMotion *motion,int32_t boundary,int32_t *sound){
 if(!actors||!environment||!motion||!sound||side<0||side>1||slot<1||slot>=actorEnd())return 1;
 const auto backup=actorAt(actors,side,slot);
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};uint32_t seed=1;int32_t result= -1;
  Context context{definition,copy,actors,request,seed};context.motion=motion;context.boundary=&boundary;context.transitionSound=&result;
  n_006ecae4(context,0,0,side,slot);*sound=result;return 0;
 }catch(...){actorAt(actors,side,slot)=backup;return 3;}
}

extern "C" uint32_t kbcs_core_actor_resume(KbcsActor actors[2][51],int32_t side,int32_t slot){
 if(!actors||side<0||side>1||slot<1||slot>=actorEnd())return 1;
 try{
  KbcsActorDefinition definition{};KbcsActorEnvironment environment{};KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,environment,actors,request,seed};n_006ec9f4(context,0,side,slot);return 0;
 }catch(...){return 3;}
}

extern "C" uint32_t kbcs_core_actor_clock(KbcsActor actors[2][51],const KbcsActorClock *clock){
 if(!actors||!clock)return 1;
 for(int side=0;side<2;++side)for(int slot=0;slot<actorEnd();++slot)if(actorForm(clock,side,slot)<0||actorForm(clock,side,slot)>3)return 1;
 for(int value:clock->kill_orb)if(value<0||value>1)return 1;
 if(clock->kill_threshold<0)return 1;
 try{
  KbcsActorDefinition definition{};KbcsActorEnvironment environment{};KbcsSpawnRequest request{};uint32_t seed=1;
  Context context{definition,environment,actors,request,seed};context.clock=clock;
  n_005ce03c(context,0,0);return 0;
 }catch(...){return 3;}
}

extern "C" uint32_t kbcs_core_actor_contact(const KbcsActor actors[2][51],int32_t side,
    int32_t slot,int32_t target,int32_t hit,int32_t castle_slot,int32_t special_castle,int32_t *out){
 if(!actors||!out||side<0||side>1||slot<1||slot>=actorEnd()||target<0||target>=actorEnd()||hit<0||hit>2||castle_slot< -1||castle_slot>50)return 1;
 try{
  KbcsActorDefinition definition{};KbcsActorEnvironment environment{};environment.castle_slot=castle_slot;environment.special_castle=special_castle;
  KbcsSpawnRequest request{};request.side=side;uint32_t seed=1;
  Context context{definition,environment,const_cast<KbcsActor (*)[51]>(actors),request,seed};
  *out=int32_t(n_006dda04(context,0,side,slot,target,hit));return 0;
 }catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_actor_matches(const KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    int32_t side,int32_t slot,int32_t target,int32_t *out){
 if(!actors||!environment||!out||side<0||side>1||slot<1||slot>=actorEnd()||target<0||target>=actorEnd())return 1;
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};request.side=side;uint32_t seed=1;
  Context context{definition,copy,const_cast<KbcsActor (*)[51]>(actors),request,seed};
  *out=int32_t(n_00a962a8(context,side,slot,target));return 0;
 }catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_actor_roll(const KbcsActor actors[2][51],int32_t side,
    int32_t slot,int32_t hit,uint32_t *seed,int32_t flags[12]){
 if(!actors||!flags||!seed||!*seed||side<0||side>1||slot<1||slot>=actorEnd()||hit<0||hit>2)return 1;
 try{
  KbcsActorDefinition definition{};KbcsActorEnvironment environment{};KbcsSpawnRequest request{};request.side=side;
  Context context{definition,environment,const_cast<KbcsActor (*)[51]>(actors),request,*seed};
  n_006e9c88(context,0,side,slot,hit);std::copy_n(context.procs,12,flags);return 0;
 }catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_actor_effects(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
    const KbcsActorEffectContext *effects,int32_t side,int32_t slot,int32_t target,const int32_t flags[7],uint32_t *seed,KbcsActorEffectEvents *out){
 if(!actors||!environment||!effects||!flags||!seed||!*seed||!out||side<0||side>1||slot<1||slot>=actorEnd()||target<0||target>=actorEnd()||effects->fruit<0||effects->fruit>300||effects->target_count<1||effects->target_count>12||effects->notifications<0||effects->notifications>1||effects->scenario_level<1)return 1;
 for(int i=0;i<7;++i)if(flags[i]<0||flags[i]>1)return 1;
 for(int value:effects->base_reductions)if(value<0||value>10000)return 1;
 for(int value:effects->sage)if(value<0||value>100)return 1;
 const auto backup=actorAt(actors,1-side,target);const auto previous_seed=*seed;
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};request.side=side;KbcsActorEffectEvents events{};
  Context context{definition,copy,actors,request,*seed};context.effects=effects;context.events=&events;
  n_006e62f8(context,0,side,slot,target,0,flags[0],flags[1],flags[2],flags[3],flags[4],flags[5],flags[6]);*out=events;return 0;
 }catch(...){actorAt(actors,1-side,target)=backup;*seed=previous_seed;return 3;}
}

extern "C" uint32_t kbcs_core_actor_load(const int32_t *raw,int32_t count,int32_t unit,int32_t *loaded){
 if(!loaded||count<0||count>4096||(count&&!raw)||(unit!=0&&unit!=1))return 1;
 int32_t values[119]{};
 if(unit){for(int column:{55,57,66,110})values[column]=-1;values[63]=1;}
 else {for(int column:{50,51,53})values[column]=-1;values[59]=1;}
 std::copy_n(raw,std::min(count,unit?119:113),values);
 for(int column:{2,4,5,unit?7:8,unit?9:35,unit?44:36,unit?45:6}){
  const int factor=column==2||column==4||(unit&&column==7)?2:(!unit&&column==6)?100:4;
  const int64_t result=int64_t(values[column])*factor;
  if(result<INT32_MIN||result>INT32_MAX)return 2;
  values[column]=int32_t(result);
 }
 if(unit){const int64_t cost=int64_t(values[6])*100;if(cost<INT32_MIN||cost>INT32_MAX)return 2;values[6]=int32_t(cost);}
 std::copy_n(values,119,loaded);return 0;
}

#include "actor_computer.inc"
#include "actor_points.inc"
#include "actor_result.inc"
#include "actor_ending.inc"
#include "actor_battle.inc"
#include "actor_sniper.inc"

#include "actor_cannon_draw.inc"
