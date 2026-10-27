#include "kbcs_production.h"
#include <algorithm>
#include <climits>

namespace {
bool flag(int32_t value) { return value==0||value==1; }
bool valid(const KbcsSpawnRequest &r) {
 return (r.side==0||r.side==1)&&(r.raw==-1||r.raw>=2)&&r.level_index>=0&&
     r.form>=0&&r.form<=3&&r.row>=0;
}
bool slotResult(int32_t slot) { return slot>=-2&&slot!=0&&slot<=50; }
KbcsSpawnRequest enemyRequest(const KbcsStageRow &row,int32_t index) {
 return {1,row.cells[0],0,row.cells[6],row.cells[7],0,index};
}
uint32_t validateRows(const KbcsStageRow *rows,int32_t count) {
 if(count<0||count>4096||(count&&!rows))return 1;
 for(int32_t i=0;i<count;++i)if(!valid(enemyRequest(rows[i],i)))return 1;
 return 0;
}
}

extern "C" uint32_t kbcs_core_spawn_prepare(const KbcsSpawnRequest *request,
    const KbcsSpawnGeometry *geometry,const int32_t occupied[51],uint32_t *seed,
    KbcsSpawnPlacement *out) {
 if(!request||!geometry||!occupied||!seed||!*seed||!out||!valid(*request))return 1;
 const auto &r=*request;const auto &g=*geometry;
 if(g.stage_width<2800||g.castle_slot< -1||g.castle_slot>50)return 1;
 const int64_t range=int64_t(r.layer_max)-r.layer_min;
 if(range>INT32_MAX-1||range<INT32_MIN)return 2;
 KbcsSpawnPlacement result{-2,r.raw==-1?-1:r.raw-2,0,0,0};
 if(r.raw!=-1){
  result.slot=-1;
  for(int32_t slot=1;slot<=50;++slot)if(occupied[slot]==0){
   int32_t roll=0;
   kbcs_core_random_bounded(seed,int32_t(std::max<int64_t>(0,range))+1,&roll);
   result={slot,r.raw-2,r.side==0?g.stage_width-2800:slot==g.castle_slot?3200:2800,
       4480,r.layer_min+roll};
   break;
  }
 }
 *out=result;return 0;
}

extern "C" uint32_t kbcs_core_spawn_boss_position(int32_t castle_x,int32_t scale,
    int32_t offset,int32_t *out) {
 if(!out||scale<0)return 1;
 const int64_t a=int64_t(scale)*1180,b=int64_t(scale)*offset,c=int64_t(scale)*127;
 if(a>INT32_MAX||b<INT32_MIN||b>INT32_MAX||c>INT32_MAX)return 2;
 const int64_t result=int64_t(castle_x)-a/100+b/10+c/10;
 if(result<INT32_MIN||result>INT32_MAX)return 2;
 *out=int32_t(result);return 0;
}

extern "C" uint32_t kbcs_core_production_recharge(const KbcsRechargeInput *input,int32_t *out) {
 if(!input||!out||input->base<0||input->talent<0||input->research_level<0||
     input->treasure<0||input->combo<0||input->stage_percent<0||input->override_frames< -1)return 1;
 const auto &in=*input;
 if(in.override_frames>=0){*out=in.override_frames;return 0;}
 const int64_t research=int64_t(in.research_level)*6+in.treasure;
 if(research>INT32_MAX||research*in.combo>INT32_MAX)return 2;
 const int64_t base=std::max(0,in.base-in.talent);
 const int64_t reduced=base-research-research*in.combo/100;
 if(reduced<INT32_MIN)return 2;
 const int64_t value=std::max<int64_t>(60,reduced)*in.stage_percent;
 if(value>INT32_MAX)return 2;
 // ステージ率は最低60Fを適用したあと。固定値0も有効な上書きとして保持する。
 *out=int32_t(value/100);return 0;
}

extern "C" uint32_t kbcs_core_production_price(const KbcsProductionPrice *input,int32_t *out){
 if(!input||!out||input->base<0||input->last_cost<0||input->count<0||input->count>3)return 1;
 const auto &in=*input;int64_t value=in.base;
 if(in.count&&in.last_cost){
  if(in.count<3)return 1;
  value=in.last_cost;
  if(in.rule[0]==0||in.rule[0]==1){
   value+=int64_t((in.rule[0]?in.last_cost:in.base)/100)*in.rule[1]/100*100;
  }
  if(in.count>2&&int64_t(in.rule[2])*100<=value)value=int64_t(in.rule[2])*100;
 }
 if(value<0||value>INT32_MAX)return 2;*out=int32_t(value);return 0;
}

extern "C" uint32_t kbcs_core_production_deploy(const KbcsProductionInput *input,
    KbcsProductionState *state,uint32_t *seed,KbcsSpawnConstructor construct,void *user,
    KbcsProductionOutput *out) {
 if(!input||!state||!seed||!*seed||!construct||!out)return 1;
 const auto &in=*input;auto &s=*state;
 if(!valid(in.spawn)||in.spawn.side!=0||in.slot<0||in.slot>=10||
     !flag(in.present)||!flag(in.allowed)||!flag(in.blocked)||!flag(in.recharge_enabled)||!flag(in.notify_failure)||
     in.summon_mode<0||in.cost<0||in.recharge<0||in.reduction< -1||in.reduction>100||
     s.money<0||s.wait[in.slot]<0||s.produced[in.slot]<0||s.total<0)return 1;
 // 精霊の再召喚を通常生産へ置き換えない。未対応の別入口として明示的に拒否する。
 if(in.summon_mode)return 4;
 int32_t wait=0;if(in.recharge_enabled){const auto code=kbcs_core_production_wait(in.recharge,in.reduction,&wait);if(code)return code;}
 KbcsProductionOutput result{-1,15};
 if(in.present&&in.allowed&&!in.blocked&&s.wait[in.slot]==0&&s.money>=in.cost){
  if(s.produced[in.slot]==INT32_MAX||s.total==INT32_MAX)return 2;
  result.slot=construct(user,&in.spawn,seed);
  if(!slotResult(result.slot)||!*seed)return 1;
  if(result.slot<0&&!in.notify_failure)result.sound=-1;
  if(result.slot>0){
   s.last_cost[in.slot]=in.cost;++s.produced[in.slot];++s.total;
   s.money-=in.cost;
   s.wait[in.slot]=s.maximum[in.slot]=wait;
   result.sound=19;
  }
 }
 *out=result;return 0;
}

extern "C" uint32_t kbcs_core_production_condition(int32_t produced,int32_t kind,int32_t period,int32_t *out){
 if(!out)return 1;const int32_t next=int32_t(uint32_t(produced)+1U);
 *out=kind?next==period:period?int64_t(next)%period==0:next==0;return 0;
}
extern "C" uint32_t kbcs_core_production_wait(int32_t base,int32_t reduction,int32_t *out){
 if(!out||base<0||reduction< -1||reduction>100)return 1;
 if(reduction<0){*out=base;return 0;}const int64_t value=int64_t(100-reduction)*base;
 if(value>INT32_MAX)return 2;*out=std::max(int32_t(value/100),std::min(base,60));return 0;
}
// 00aa0568の各乗算は32bit。途中の整数化をまとめない。
extern "C" uint32_t kbcs_core_production_cost(const KbcsProductionCost *input,int32_t *out){
 if(!input||!out||input->raw<0||input->talent<0||input->chapter<0||input->chapter>2||input->fixed< -1||input->combo_count<0||input->combo_count>32)return 1;
 const auto &in=*input;const auto multiply=[](int a,int b){return int32_t(uint32_t(a)*uint32_t(b));};
 if(in.fixed>=0){*out=multiply(in.fixed,100);return 0;}
 int value=std::max(0,int32_t(uint32_t(in.raw)-uint32_t(in.talent)*100U))/100;
 value=in.multiplier?multiply(value,in.multiplier):multiply(multiply(value,in.chapter+2)/2,100);
 const auto reduce=[&](int rate){value=multiply(multiply(int32_t(100U-uint32_t(rate)),value)/10000,100);};
 if(in.orb_enabled)reduce(in.orb_rate);for(int i=0;i<in.combo_count;++i)reduce(in.combos[i]);
 *out=std::max(0,multiply(value,in.rarity_rate)/100);return 0;
}
extern "C" uint32_t kbcs_core_production_extra_plan(const int32_t rule[3],int32_t rarity,int32_t slot,KbcsProductionExtra *out,int32_t capacity,int32_t *count){
 if(!rule||!count||rarity<0||rarity>5||slot<0||slot>9||capacity<0)return 1;
 const int size=(uint32_t(rule[0])&(1U<<rarity))?std::max(0,rule[1]):0;
 if(size>capacity||(size&&!out))return 1;
 for(int i=0;i<size;++i)out[i]={slot,int32_t(uint32_t(rule[2])*(uint32_t(i)+1U))};
 *count=size;return 0;
}
extern "C" uint32_t kbcs_core_production_extra_tick(KbcsProductionExtra *records,int32_t *count,KbcsProductionState *production,const KbcsSpawnRequest slots[10],uint32_t *seed,KbcsSpawnConstructor construct,void *user){
 if(!count||*count<0||(*count&&!records)||!production||!slots||!seed||!*seed||!construct)return 1;
 for(int i=0;i<*count;++i)if(records[i].slot<0||records[i].slot>9||!valid(slots[records[i].slot]))return 1;
 for(int i=*count;i-->0;){auto &record=records[i];if(record.wait>0){--record.wait;continue;}
  auto &produced=production->produced[record.slot];const int previous=produced;produced=int32_t(uint32_t(produced)-1U);
  int result= -1;try{result=construct(user,&slots[record.slot],seed);}catch(...){produced=previous;return 3;}produced=previous;
  if(!slotResult(result)||!*seed)return 1;
  // 006d6d04は生成に失敗しても再試行しない。後ろから走査し、残りの順序を保持する。
  std::move(records+i+1,records+*count,records+i);--*count;
 }
 return 0;
}

extern "C" uint32_t kbcs_core_production_clock(KbcsProductionState *state,
    const int32_t recharge[10],uint32_t *ready) {
 if(!state||!recharge||!ready)return 1;
 for(int i=0;i<10;++i)if(state->wait[i]<0||recharge[i]<0)return 1;
 uint32_t result=0;
 for(int i=0;i<10;++i)if(state->wait[i]>0){
  if(state->wait[i]>recharge[i])state->wait[i]=state->maximum[i]=recharge[i];
  else --state->wait[i];
  if(state->wait[i]==0)result|=1U<<i;
 }
 *ready=result;return 0;
}

extern "C" uint32_t kbcs_core_production_enemy(const KbcsStageRow *rows,
    KbcsStageState *states,int32_t count,KbcsStageContext *context,uint32_t *seed,
    int32_t *seen,int32_t seen_count,KbcsSpawnConstructor construct,void *user,
    KbcsEnemyProductionOutput *out) {
 if(!seed||!*seed||!construct||!out||seen_count<0||(seen_count&&!seen))return 1;
 const auto validation=validateRows(rows,count);if(validation)return validation;
 for(int32_t i=0;i<count;++i)if(rows[i].cells[0]>=2&&rows[i].cells[0]-2>=seen_count)return 1;
 int32_t candidate=-1;
 auto error=kbcs_core_stage_tick(rows,states,count,context,&candidate);if(error)return error;
 KbcsEnemyProductionOutput result{candidate,-1};
 if(candidate>=0){
  if(states[candidate].spawned==INT32_MAX)return 2;
  const auto request=enemyRequest(rows[candidate],candidate);
  // 呼出側は個体の構築中にも同じ乱数状態を使う。成功したことにして間隔を進めない。
  result.slot=construct(user,&request,seed);
  if(!slotResult(result.slot)||!*seed)return 1;
  if(result.slot>0){
   const auto &row=rows[candidate].cells;
   int32_t global_roll=0,row_roll=0;
   kbcs_core_random_bounded(seed,context->global_max-context->global_min+1,&global_roll);
   kbcs_core_random_bounded(seed,row[4]-row[3]+1,&row_roll);
   error=kbcs_core_stage_commit(rows,states,count,context,candidate,global_roll,row_roll);
   if(error)return error;
   if(row[0]<2)return 1;
   if(seen[row[0]-2]==0)seen[row[0]-2]=1;
  }
 }
 *out=result;return 0;
}

extern "C" uint32_t kbcs_core_production_start(const KbcsStageRow *rows,
    KbcsStageState *states,int32_t count,int32_t minimum,int32_t maximum,int32_t castle_raw,
    uint32_t *seed,KbcsSpawnConstructor construct,void *user,KbcsStageStartOutput *out,
    KbcsEnemyProductionOutput *spawn) {
 if(!seed||!*seed||!construct||!out||!spawn)return 1;
 auto error=validateRows(rows,count);if(error)return error;
 // 初期化APIの検証を乱数消費より前に実行する。前状態は参照されない。
 KbcsStageStart start{minimum,maximum,0,castle_raw};KbcsStageStartOutput result{};
 error=kbcs_core_stage_initialize(rows,states,count,&start,&result);if(error)return error;
 kbcs_core_random_bounded(seed,maximum-minimum+1,&start.global_roll);
 result.global_wait=minimum+start.global_roll;
 KbcsEnemyProductionOutput birth{result.castle_row,-1};
 if(result.castle_row>=0){
  const auto request=enemyRequest(rows[result.castle_row],result.castle_row);
  birth.slot=construct(user,&request,seed);
  if(!slotResult(birth.slot)||!*seed)return 1;
 }
 *out=result;*spawn=birth;return 0;
}
