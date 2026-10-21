#include "kbcs_core.h"
#include <cmath>

static uint32_t validate(const KbcsMaterialInput *input, int32_t &draws, int32_t &total) {
  if (!input || !std::isfinite(input->count) || !std::isfinite(input->multiplier) ||
      input->count < 0 || input->multiplier < 0 || input->miss < 0 || input->miss > 100) return 1;
  // 現版はfloatで乗算し、doubleへ拡張して0.5を加える。
  const float product=input->count*input->multiplier;
  if (!std::isfinite(product) || double(product)+0.5 >= 4097) return 2;
  draws=int32_t(double(product)+0.5);
  int64_t sum=0;
  for (const auto weight : input->weights) {
    if (weight < 0) return 1;
    sum+=weight;
  }
  if (sum > INT32_MAX) return 2;
  total=int32_t(sum);
  if (draws && input->miss < 100 && !total) return 1;
  return 0;
}

extern "C" uint32_t kbcs_core_material_plan(const KbcsMaterialInput *input, KbcsMaterialOutput *output) {
  if (!output) return 1;
  int32_t draws=0,total=0;
  const auto error=validate(input,draws,total);
  if (error) return error;
  KbcsMaterialOutput result{};
  result.draws=draws;
  result.miss=input->miss/100.0;
  result.none=std::pow(result.miss,draws);
  for (int32_t slot=0; slot<16; ++slot) {
    const double chance=total ? (1-result.miss)*input->weights[slot]/total : 0;
    result.items[slot]={chance,1-std::pow(1-chance,draws),chance*draws};
  }
  *output=result;
  return 0;
}

extern "C" uint32_t kbcs_core_material_pick(const KbcsMaterialInput *input,
    int32_t miss_roll, int32_t weight_roll, int32_t *slot) {
  if (!slot || miss_roll < 0 || miss_roll >= 100) return 1;
  int32_t draws=0,total=0;
  const auto error=validate(input,draws,total);
  if (error) return error;
  if (!draws) return 1;
  if (miss_roll < input->miss) {
    if (weight_roll != -1) return 1;
    *slot=-1;
    return 0;
  }
  if (weight_roll < 0 || weight_roll >= total) return 1;
  int32_t sum=0;
  for (int32_t index=0; index<16; ++index) {
    sum+=input->weights[index];
    if (weight_roll < sum) { *slot=index; return 0; }
  }
  return 1;
}
