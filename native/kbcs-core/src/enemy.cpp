#include "kbcs_core.h"

extern "C" uint32_t kbcs_core_enemy_stat(const KbcsEnemyStatInput *input, KbcsEnemyStatOutput *output) {
  if (!input || !output || input->base < 0 || input->row_percent < 0 || input->row_percent > 1000000 ||
      input->crown_percent < 0 || input->crown_percent > 1000000 || input->crystal_max < 0 ||
      input->crystal_max > 10000 || input->crystal_treasure < 0 || input->crystal_treasure > input->crystal_max ||
      input->castle_attack < 0 || input->castle_attack > 1) return 1;
  KbcsEnemyStatOutput result{};
  // 出現行の倍率で丸めてから冠を切り捨て、最後にクリスタル不足分を加える。
  result.stages[0]=(int64_t(input->base)*input->row_percent+50)/100;
  if (result.stages[0] > INT32_MAX) return 2;
  result.stages[1]=result.stages[0]*(input->castle_attack ? 100 : input->crown_percent)/100;
  if (result.stages[1] > INT32_MAX) return 2;
  result.stages[2]=result.stages[1]+result.stages[1]*(input->crystal_max-input->crystal_treasure)/100;
  if (result.stages[2] > INT32_MAX) return 2;
  *output=result;
  return 0;
}
