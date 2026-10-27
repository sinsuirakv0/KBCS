#include "kbcs_core.h"

// 取得元と初期補正だけを分け、以降の整数化を共用する。
static uint32_t calculateExperience(const KbcsLegendExperienceInput *input, KbcsExperienceOutput *output, int32_t multiplier, int32_t clearLimit, int32_t divisor) {
  if (!input || !output || input->base < 0 || input->clears < 0 || input->study_level < 1 ||
      input->study_level > 30 || input->treasure < 0 || input->treasure > 225 ||
      input->combo < 0 || input->combo > 100 || input->okame < 0 || input->okame > 1) return 1;
  KbcsExperienceOutput result{};
  auto &value=result.stages;
  value[0]=int64_t(input->base)*multiplier;
  const int32_t clears=input->clears < clearLimit ? input->clears : clearLimit;
  if (value[0] > INT32_MAX || value[0]*clears > INT32_MAX) return 2;
  value[1]=value[0]-value[0]*clears/divisor;
  const int64_t study=value[1]*(100+(input->study_level-1)*5+input->treasure);
  if (study > INT32_MAX) return 2;
  value[2]=study/100;
  const int64_t combo=value[2]*(100+input->combo);
  if (combo > INT32_MAX) return 2;
  value[3]=combo/100;
  if (input->okame && value[3]*15 > INT32_MAX) return 2;
  value[4]=input->okame ? value[3]*15/10 : value[3];
  *output=result;
  return 0;
}

extern "C" uint32_t kbcs_core_legend_experience(const KbcsLegendExperienceInput *input, KbcsExperienceOutput *output) {
  return calculateExperience(input,output,9,4,5);
}

extern "C" uint32_t kbcs_core_event_experience(const KbcsEventExperienceInput *input, KbcsExperienceOutput *output) {
  if (!input) return 1;
  const KbcsLegendExperienceInput resolved{input->base,0,input->study_level,input->treasure,input->combo,input->okame};
  return calculateExperience(&resolved,output,1,0,5);
}

extern "C" uint32_t kbcs_core_stage_experience(const KbcsStageExperienceInput *input, KbcsExperienceOutput *output) {
  if (!input || input->stage < 0 || input->stage > 99 || input->kind < -26 || input->kind > 4) return 1;
  const int32_t mode=input->mode;
  if (mode != 3 && mode != 99 && !(mode >= 0 && mode <= 2) && !(mode >= 4 && mode <= 9)) return 1;
  const bool chapter=mode != 3 && mode != 99;
  const bool legend=mode == 3 && (input->kind == 0 || input->kind == -9 || input->kind == -22);
  // 章はCSVの元XPを使わず、面番号から生成する。EXは減衰を通らない。
  const KbcsLegendExperienceInput resolved{chapter ? (input->stage*6000+20000)/10 : input->base,
      input->clears,input->study_level,input->treasure,input->combo,input->okame};
  return calculateExperience(&resolved,output,legend ? 9 : 1,chapter ? 13 : legend ? 4 : 0,chapter ? 14 : 5);
}

extern "C" uint32_t kbcs_core_stage_score(const KbcsStageScoreInput *input, KbcsStageScoreOutput *output) {
  if (!input || !output || input->elapsed < 0 || input->best < 0 || input->best > 10000 ||
      input->count < 1 || input->count > 10) return 1;
  for (int32_t index=0; index<input->count; ++index)
    if (input->thresholds[index] < 0 || input->thresholds[index] > 10000) return 1;
  const int32_t elapsed=input->elapsed;
  const int32_t score=elapsed <= 9000 ? 10000-elapsed : elapsed < 19000 ? 1000-(elapsed-9000)/10 : 0;
  KbcsStageScoreOutput result{score,input->best,int32_t(score > input->best),0};
  if (result.improved) {
    result.best=score;
    // 今回新たにまたいだ閾値だけ要求する。原本の報酬順・重複を保持する。
    for (int32_t index=0; index<input->count; ++index)
      if (input->best < input->thresholds[index] && input->thresholds[index] <= score)
        result.reward_mask |= 1 << index;
  }
  *output=result;
  return 0;
}

extern "C" uint32_t kbcs_core_stage_score_tick(int32_t elapsed, int32_t phase, int32_t *output) {
  if (!output || elapsed < 0 || phase < 0) return 1;
  // 受理された戦闘更新1回分。休止・倍速による呼出回数の制御は所有側で行う。
  *output=phase == 0 ? (elapsed < 29999 ? elapsed+1 : 30000) : elapsed;
  return 0;
}

extern "C" uint32_t kbcs_core_stage_ex(const KbcsExTransitionInput *input, const KbcsExChoice *choices,
    int32_t count, uint32_t *state, KbcsExTransitionOutput *output) {
  if (!input || !state || !*state || !output || count < 0 || count > 32 || (count && !choices) ||
      input->chance < 0 || input->chance > 100 || input->map_index < 0 || input->map_index > 999 ||
      input->minimum < 0 || input->maximum < input->minimum || input->maximum > 99 ||
      input->group_present < 0 || input->group_present > 1 || (!input->group_present && count)) return 1;
  for (int32_t index=0; index<count; ++index) {
    const auto &choice=choices[index];
    if (choice.threshold < 0 || choice.threshold > 100 || choice.group < -1 ||
        (choice.group == -1 ? (choice.map_index != -1 || choice.stage != -1)
        : (choice.map_index < 0 || choice.map_index > 999 || choice.stage < 0 || choice.stage > 99))) return 1;
  }
  uint32_t next=*state;
  KbcsExTransitionOutput result{};
  result.group=-1; result.map_index=-1; result.stage=-1;
  auto draw=[&](int32_t bound) {
    const int32_t index=result.consumed++;
    result.bounds[index]=bound;
    // 非0状態と正の範囲を検査済み。同じ所有状態から最大3回だけ進める。
    kbcs_core_random_bounded(&next,bound,&result.rolls[index]);
    return result.rolls[index];
  };
  const KbcsExChoice *fallback=nullptr;
  if (input->group_present) {
    const int32_t roll=draw(100);
    for (int32_t index=0; index<count; ++index) {
      if (roll < choices[index].threshold) {
        fallback=&choices[index]; result.group=fallback->group; break;
      }
    }
  }
  // 候補抽選は直接EXが当たる場合にも先に消費する。
  if (draw(100) < input->chance) {
    result.source=1; result.map_index=input->map_index;
    result.stage=input->minimum+draw(input->maximum-input->minimum+1);
  } else if (fallback && fallback->group >= 0) {
    result.source=2; result.map_index=fallback->map_index; result.stage=fallback->stage;
  }
  *state=next;
  *output=result;
  return 0;
}

// 敵城の有無と開始モードは呼出側で解決し、生成する最初の該当行を返す。
extern "C" uint32_t kbcs_core_stage_initialize(const KbcsStageRow *rows, KbcsStageState *states,
    int32_t count, const KbcsStageStart *input, KbcsStageStartOutput *output) {
  if (!input || !output || count < 0 || count > 4096 || (count && (!rows || !states)) ||
      input->global_min < 0 || input->global_max < input->global_min || input->global_roll < 0 ||
      input->global_roll > input->global_max-input->global_min ||
      input->castle_raw < 0 || input->castle_raw == 1) return 1;
  if (input->global_max-input->global_min == INT32_MAX) return 2;
  for (int32_t index=0; index<count; ++index) {
    if (rows[index].cells[0] < 2) return 1;
    if (rows[index].cells[2] == INT32_MIN) return 2;
  }
  int32_t castle=-1;
  for (int32_t index=0; index<count; ++index) {
    states[index]={rows[index].cells[2],0,0};
    if (castle < 0 && input->castle_raw && rows[index].cells[0] == input->castle_raw) {
      castle=index;
      states[index]={1,1,0};
    }
  }
  *output={input->global_min+input->global_roll,castle};
  return 0;
}

// 006d9e44..006d9fc0。通常の出現tickと異なり、待機・撃破条件は再検査しない。
extern "C" uint32_t kbcs_core_stage_castle_guard(const KbcsStageRow *rows,const KbcsStageState *states,
    int32_t count,const KbcsStageContext *context,int32_t pending_damage,int32_t *preserve){
  if(!context||!preserve||count<0||count>4096||(count&&(!rows||!states))||*preserve<0||*preserve>1)return 1;
  int value=*preserve;
  for(int i=0;i<count;++i){const auto &row=rows[i].cells;
    const int threshold=int32_t(uint32_t(row[5])*uint32_t(context->castle_max_hp))/100;
    const bool ready=context->damage_condition?context->castle_damage>=row[5]
        :int32_t(uint32_t(context->castle_hp)-uint32_t(pending_damage))<=threshold;
    if(ready&&(!row[1]||states[i].spawned<row[1])&&row[8]&&context->castle_hp>1)value=1;
  }
  *preserve=value;return 0;
}

// 読込済み14整数と呼出側の状態を借用する。原本解析・敵生成・乱数生成は行わない。
static uint32_t validateStage(const KbcsStageRow *rows, const KbcsStageState *states,
    int32_t count, const KbcsStageContext *context) {
  if (!context || count < 0 || count > 4096 || (count && (!rows || !states))) return 1;
  if (context->kill_delta < 0 || context->active_enemies < 0 || context->active_enemies > 50 ||
      context->max_enemies < 0 || context->max_enemies > 50 || context->castle_hp < 0 ||
      context->castle_max_hp < 0 || context->castle_damage < 0 ||
      context->global_min < 0 || context->global_max < 0) return 1;
  if (context->global_wait == INT32_MIN || context->global_max - context->global_min == INT32_MAX) return 2;
  for (int32_t index=0; index<count; ++index) {
    const auto &row = rows[index].cells;
    const auto &state = states[index];
    if (row[1] < 0 || row[3] < 0 || row[4] < 0 || row[5] < 0 || row[13] < 0 ||
        state.spawned < 0 || state.kills < 0) return 1;
    if (state.wait == INT32_MIN || row[4] - row[3] == INT32_MAX || int64_t(state.kills) + context->kill_delta > INT32_MAX ||
        (!context->damage_condition && int64_t(row[5]) * context->castle_max_hp > INT32_MAX)) return 2;
  }
  return 0;
}

extern "C" uint32_t kbcs_core_stage_tick(const KbcsStageRow *rows, KbcsStageState *states,
    int32_t count, KbcsStageContext *context, int32_t *candidate) {
  if (!candidate) return 1;
  const auto error = validateStage(rows, states, count, context);
  if (error) return error;
  *candidate = -1;
  const int32_t kills = context->kill_delta;
  context->kill_delta = 0;
  if (context->paused) return 0;
  --context->global_wait;
  for (int32_t index=0; index<count; ++index) {
    const auto &row = rows[index].cells;
    auto &state = states[index];
    const bool ready = context->damage_condition
        ? context->castle_damage >= row[5]
        : context->castle_hp <= (int64_t(row[5]) * context->castle_max_hp) / 100;
    if (ready) state.kills += kills;
    if (state.kills < row[13] && state.wait < 2) {
      state.wait = 1;
    } else if (ready) {
      if (row[1] == 0 || state.spawned < row[1]) --state.wait;
    } else if (row[12] == 0) {
      state.wait = 1;
    }
  }
  if (context->global_wait < 1 && context->active_enemies < context->max_enemies) {
    // ネイティブと同様、最後の出現可能行だけを選ぶ。
    for (int32_t index=count; index>0; --index) {
      if (states[index-1].wait <= 0) { *candidate = index-1; break; }
    }
  }
  return 0;
}

extern "C" uint32_t kbcs_core_stage_commit(const KbcsStageRow *rows, KbcsStageState *states,
    int32_t count, KbcsStageContext *context, int32_t candidate,
    int32_t global_roll, int32_t row_roll) {
  const auto error = validateStage(rows, states, count, context);
  if (error) return error;
  if (candidate < 0 || candidate >= count || context->paused || global_roll < 0 || row_roll < 0) return 1;
  const auto &row = rows[candidate].cells;
  auto &state = states[candidate];
  if (context->global_wait > 0 || state.wait > 0 || context->active_enemies >= context->max_enemies ||
      global_roll > (context->global_max > context->global_min ? context->global_max-context->global_min : 0) ||
      row_roll > (row[4] > row[3] ? row[4]-row[3] : 0)) return 1;
  // 候補は待機だけで決まる。回数上限・城条件を再検査すると原本の0待機経路を落とす。
  for (int32_t index=candidate+1; index<count; ++index)
    if (states[index].wait <= 0) return 1;
  if (state.spawned == INT32_MAX) return 2;
  // 敵生成の成功後だけ呼ぶ。失敗時は間隔乱数を引かず、この関数も呼ばない。
  context->global_wait = context->global_min + global_roll;
  state.wait = row[3] + row_roll;
  ++state.spawned;
  return 0;
}
