#include "kbcs_core.h"

struct MapBand { int32_t base, kind, count; };
static constexpr MapBand bands[]={
  {0,0,1000},{1000,1,1000},{2000,2,1000},{3000,-2,3},{3003,-3,3},{3006,-7,3},
  {4000,-8,1000},{5000,-5,1000},{6000,3,1000},{7000,-4,1000},{11000,4,1000},
  {12000,-6,1000},{13000,-9,1000},{14000,-10,1000},{16000,-11,1000},
  {20000,-12,1000},{21000,-13,1000},{22000,-14,1000},{23000,-15,1000},
  {24000,-16,1000},{25000,-17,1000},{27000,-18,1000},{30000,-19,1000},
  {31000,-20,1000},{33000,-21,1000},{34000,-22,1000},{36000,-23,1000},
  {37000,-24,1000},{38000,-25,1000},{39000,-26,1000}
};

extern "C" uint32_t kbcs_core_map_decode(int32_t id, KbcsMapIdentity *output) {
  if (!output || id < 0 || id >= 40000) return 1;
  for (const auto &band:bands) {
    if (id >= band.base && id-band.base < band.count) {
      *output={band.kind,id-band.base};
      return 0;
    }
  }
  // 原本の未分類はkind=-1。負IDをレジェンドとして受理する挙動は入口で拒否する。
  *output={-1,id%1000};
  return 0;
}

extern "C" uint32_t kbcs_core_map_encode(const KbcsMapIdentity *input, int32_t *output) {
  if (!input || !output || input->index < 0) return 1;
  for (const auto &band:bands) {
    if (input->kind == band.kind) {
      // 範囲外indexの別番台への流出は製品の入力契約で拒否する。
      if (input->index >= band.count) return 1;
      *output=band.base+input->index;
      return 0;
    }
  }
  return 1;
}

extern "C" uint32_t kbcs_core_stage_current_kind(const KbcsCurrentKind *input, int32_t *output) {
  if (!input || !output || input->mode < 0) return 1;
  const int32_t flags[]={input->zombie,input->invasion,input->invasion_zombie,input->ignore,input->ex_override};
  for (int32_t flag:flags)
    if (flag < 0 || flag > 1) return 1;
  int32_t kind=-1;
  const int32_t mode=input->mode;
  if (mode == 3) {
    kind=input->selected_kind >= -26 && input->selected_kind <= 4 ? input->selected_kind : -1;
    if (input->ex_override && input->ex_marker != 300 && !input->ignore) kind=-8;
  } else if (mode <= 2) {
    kind=input->zombie && !input->ignore ? -12 : -2;
  } else if (mode >= 4 && mode <= 6) {
    kind=input->zombie && !input->ignore ? -13 : -3;
  } else if (mode >= 7 && mode <= 9) {
    kind=!input->ignore && input->invasion ? -15 :
        !input->ignore && input->invasion_zombie ? -25 :
        !input->ignore && input->zombie ? -14 : -7;
  } else if (mode == 99) {
    kind=-8;
  }
  *output=kind;
  return 0;
}

extern "C" uint32_t kbcs_core_stage_row_decode(const int32_t *cells, int32_t count, KbcsStageRow *output) {
  if (!output || count < 0 || count > 14 || (count && !cells)) return 1;
  KbcsStageRow result{};
  for (int32_t index=0; index<count; ++index) {
    int64_t value=cells[index];
    // 00a06ae4の初回待機・再出現待機2列だけFを倍にする。
    if (index >= 2 && index <= 4) value*=2;
    if (value < INT32_MIN || value > INT32_MAX) return 2;
    result.cells[index]=int32_t(value);
  }
  *output=result;
  return 0;
}
