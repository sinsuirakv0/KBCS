#include "kbcs_core.h"

static uint32_t calculateReward(const KbcsLegendRewardInput *input, KbcsLegendRewardOutput *output) {
  if (!input || !output || input->count < 1 || input->count > 3 ||
      input->mode < -2 || input->mode > 2 || input->acquired < 0 || input->acquired > 1 ||
      input->radar < 0 || input->radar > 1) return 1;
  for (int index=0; index<3; ++index) {
    if (input->chances[index] < 0 || input->chances[index] > 100 ||
        input->rolls[index] < 0 || input->rolls[index] > 99) return 1;
  }
  KbcsLegendRewardOutput result{-1,0,0,0};
  for (int index=0; index<input->count; ++index) {
    ++result.consumed;
    if (!input->radar && input->rolls[index] >= input->chances[index]) continue;
    if (index == 0 && (input->mode == 1 || input->mode == 2) && input->acquired) {
      // 取得済みでも比較乱数は消費済み。レーダー時は後続候補へ進まない。
      if (input->radar) { result.radar_blocked=1; break; }
      continue;
    }
    result.winner=index;
    result.mark_acquired=int(index == 0 && (input->mode == 1 || input->mode == 2));
    break;
  }
  *output=result;
  return 0;
}

extern "C" uint32_t kbcs_core_legend_reward_pick(const KbcsLegendRewardInput *input, KbcsLegendRewardOutput *output) {
  if (!input || (input->mode != -1 && input->mode != 1)) return 1;
  return calculateReward(input,output);
}

extern "C" uint32_t kbcs_core_stage_reward_pick(const KbcsLegendRewardInput *input, KbcsLegendRewardOutput *output) {
  if (!input || (input->mode < 0 && input->count != 1)) return 1;
  return calculateReward(input,output);
}

extern "C" uint32_t kbcs_core_reward_weight_total(const int32_t *weights, int32_t count, int32_t *total) {
  // 元関数が終端を見つけて扱う1..10枠。11枠使い切りの異常経路は受理しない。
  if (!weights || !total || count < 1 || count > 10) return 1;
  int64_t sum=0;
  for (int32_t index=0; index<count; ++index) {
    if (weights[index] < 0) return 1;
    sum+=weights[index];
  }
  if (sum > INT32_MAX) return 2;
  if (sum == 0) return 1;
  *total=int32_t(sum);
  return 0;
}

extern "C" uint32_t kbcs_core_reward_weight_pick(const int32_t *weights, int32_t count, int32_t roll, int32_t *winner) {
  if (!winner) return 1;
  int32_t total=0;
  const auto code=kbcs_core_reward_weight_total(weights,count,&total);
  if (code) return code;
  if (roll < 0 || roll >= total) return 1;
  int32_t cumulative=0;
  for (int32_t index=0; index<count; ++index) {
    cumulative+=weights[index];
    if (roll < cumulative) { *winner=index; return 0; }
  }
  return 1;
}

extern "C" uint32_t kbcs_core_reward_weight_finish(const KbcsWeightedFinishInput *input, KbcsWeightedFinishOutput *output) {
  if (!input || !output || (input->mode != -3 && input->mode != -4) || input->seen < 0 ||
      input->seen > 1 || input->radar < 0 || input->radar > 1 || input->winner < 0 || input->winner > 9) return 1;
  const bool first=input->mode == -3 && !input->seen;
  const bool grant=input->mode == -4 || first;
  // 履歴要求を先に適用してから付与する。付与結果1でも履歴を巻き戻さない。
  *output={grant ? (input->winner == 0 ? 6 : input->winner*3+7) : -1,
      int32_t(first),int32_t(input->mode == -3 && input->seen && input->radar)};
  return 0;
}

extern "C" uint32_t kbcs_core_item_add(const KbcsItemDefinition *definitions, int32_t *counts,
    int32_t count, int32_t index, int32_t amount, KbcsItemGrant *output) {
  if (!definitions || !counts || !output || count < 1 || count > 4096 || index < 0 || index >= count || amount < 0) return 1;
  int32_t target=index,steps=0;
  while (definitions[target].redirect != -1) {
    const auto &definition=definitions[target];
    if (++steps >= count || definition.factor < 0 || definition.redirect < 0 || definition.redirect >= count) return 1;
    target=definition.redirect;
  }
  const int32_t limit=definitions[target].limit,current=counts[target];
  if (limit < 0 || current < 0 || current > limit) return 1;
  const bool redirected=definitions[index].redirect != -1;
  int64_t total=int64_t(current)+int64_t(amount)*(redirected ? definitions[index].factor : 1);
  if (total > INT32_MAX) return 2;
  // 原本は加算後の合計を後続変換へ渡す。変換率を単に連乗して差分へ掛けない。
  if (redirected) {
    int32_t next=definitions[index].redirect;
    while (definitions[next].redirect != -1) {
      total*=definitions[next].factor;
      if (total > INT32_MAX) return 2;
      next=definitions[next].redirect;
    }
  }
  if (total > limit) total=limit;
  const KbcsItemGrant result{target,int32_t(total),int32_t(total-current)};
  counts[target]=result.total;
  *output=result;
  return 0;
}
