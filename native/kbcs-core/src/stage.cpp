#include "kbcs_core.h"

// 0番台のXP。元値→繰返し減衰→勉強力・お宝→コンボ→おかめの順に整数化する。
extern "C" uint32_t kbcs_core_legend_experience(const KbcsLegendExperienceInput *input, KbcsExperienceOutput *output) {
  if (!input || !output || input->base < 0 || input->clears < 0 || input->study_level < 1 ||
      input->study_level > 30 || input->treasure < 0 || input->treasure > 225 ||
      input->combo < 0 || input->combo > 100 || input->okame < 0 || input->okame > 1) return 1;
  KbcsExperienceOutput result{};
  auto &value=result.stages;
  value[0]=int64_t(input->base)*9;
  const int32_t clears=input->clears < 4 ? input->clears : 4;
  if (value[0] > INT32_MAX || value[0]*clears > INT32_MAX) return 2;
  value[1]=value[0]-value[0]*clears/5;
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

// 読込済み14整数と呼出側の状態を借用する。原本解析・敵生成・乱数生成は行わない。
static uint32_t validateStage(const KbcsStageRow *rows, const KbcsStageState *states,
    int32_t count, const KbcsStageContext *context) {
  if (!context || count < 0 || count > 4096 || (count && (!rows || !states))) return 1;
  if (context->kill_delta < 0 || context->active_enemies < 0 || context->active_enemies > 50 ||
      context->max_enemies < 0 || context->max_enemies > 50 || context->castle_hp < 0 ||
      context->castle_max_hp < 0 || context->castle_damage < 0 ||
      context->global_min < 0 || context->global_max < context->global_min) return 1;
  if (context->global_wait == INT32_MIN || context->global_max - context->global_min == INT32_MAX) return 2;
  for (int32_t index=0; index<count; ++index) {
    const auto &row = rows[index].cells;
    const auto &state = states[index];
    if (row[1] < 0 || row[3] < 0 || row[4] < row[3] || row[5] < 0 || row[13] < 0 ||
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
      global_roll > context->global_max - context->global_min || row_roll > row[4] - row[3]) return 1;
  if (state.spawned == INT32_MAX) return 2;
  // 敵生成の成功後だけ呼ぶ。失敗時は乱数を引かず、この関数も呼ばない。
  context->global_wait = context->global_min + global_roll;
  state.wait = row[3] + row_roll;
  ++state.spawned;
  return 0;
}
