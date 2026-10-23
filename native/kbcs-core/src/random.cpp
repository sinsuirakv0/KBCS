#include "kbcs_core.h"

extern "C" uint32_t kbcs_core_random_bounded(uint32_t *state, int32_t bound, int32_t *output) {
  // シード0のOS依存初期化は行わず、呼出側に明示した非0シードを要求する。
  if (!state || !output || !*state) return 1;
  // 非正の範囲は原本同様0を返し、乱数状態を進めない。範囲1は進める。
  if (bound < 1) { *output=0; return 0; }
  uint32_t value=*state;
  value^=value<<13;
  value^=value>>17;
  value^=value<<15;
  *state=value;
  *output=int32_t(value%uint32_t(bound));
  return 0;
}
