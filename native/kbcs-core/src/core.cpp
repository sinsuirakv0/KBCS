#include "kbcs_core.h"

extern "C" uint32_t kbcs_core_abi_version(void) { return 4; }
extern "C" uint32_t kbcs_core_ruleset_version(void) { return 1507021; }

// 非負のゲーム値だけを受け、各段で整数化する。桁あふれを未定義動作にしない。
static bool valid(int64_t value) { return value >= 0 && value <= INT32_MAX; }
static bool percent(int32_t value) { return value >= 0 && value <= 100; }

extern "C" uint32_t kbcs_core_prepare_attack(const KbcsAttackPreparation *input, int32_t *output) {
  if (!input || !output || input->attack < 0 || input->kind < 0 || input->kind > 2 ||
      input->percent < 0 || input->percent > 10000 || input->wave_percent < 0 || input->wave_percent > 10000) return 1;
  const int64_t product=int64_t(input->attack)*input->percent;
  if (product > INT32_MAX) return 2;
  int64_t value=product/(input->kind == 2 ? 500 : 100);
  if (input->kind == 1) value=value*input->wave_percent/100;
  if (!valid(value)) return 2;
  *output=int32_t(value);
  return 0;
}

extern "C" uint32_t kbcs_core_stat(const KbcsStatInput *in, KbcsStatOutput *out) {
  if (!in || !out || in->base < 0 || in->growth < 0 || in->growth > 100000 ||
      in->treasure < 0 || in->treasure > 10000 || in->combo < 0 || in->combo > 1000 ||
      in->talent < 0 || in->talent > 1000 || in->extra < 0 || in->extra > 1000) return 1;
  KbcsStatOutput result{};
  int64_t value = (int64_t(in->base) * in->growth + 50) / 100;
  result.stages[0] = value;
  if (!valid(value)) return 2;
  value += value * in->treasure / 100;
  result.stages[1] = value;
  const int32_t rates[] = {in->combo, in->talent, in->extra};
  for (int index=0; index<3; ++index) {
    if (!valid(value)) return 2;
    value = value * (100 + rates[index]) / 100;
    result.stages[index+2] = value;
  }
  result.stages[5] = value;
  if (!valid(value)) return 2;
  *out=result;
  return 0;
}

static uint32_t calculateHit(const KbcsHitInput *in, KbcsHitOutput *out, bool incoming) {
  if (!in || !out || in->attack < 0 || in->raw_attack < 0 || !percent(in->weaken) ||
      !percent(in->resistance) || in->fruit < 0 || in->fruit > 300 ||
      in->strengthen < 0 || in->strengthen > 10000 || in->savage < 0 || in->savage > 10000 ||
      in->base_reduction < 0 || in->base_reduction > 10000 ||
      in->decoration_reduction < 0 || in->decoration_reduction > 10000) return 1;
  if (!percent(in->strong_combo) || !percent(in->resistant_combo) ||
      ((!percent(in->strong_orb)) && incoming) || !percent(in->resistant_orb) ||
      !percent(in->defense_orb) || in->witch_combo > 400 || in->eva_combo > 400) return 1;
  const int32_t bounded[] = {in->strong_combo,in->massive_combo,in->resistant_combo,
      in->witch_combo,in->eva_combo,in->strong_orb,in->massive_orb,in->resistant_orb,
      in->attack_orb,in->defense_orb,in->behemoth_rate,in->sage_rate,in->kill_strengthen,in->villain_rate};
  for (auto value : bounded) if (value < 0 || value > 10000) return 1;
  if (in->abilities<0 || (in->abilities & ~2047)!=0) return 1;
  if (!in->castle && (((in->abilities & KBCS_BEHEMOTH) && !in->behemoth_rate) ||
      ((in->abilities & KBCS_SAGE) && !in->sage_rate) ||
      ((in->abilities & KBCS_VILLAIN) && !in->villain_rate))) return 1;
  KbcsHitOutput result{};
  int64_t value = in->blocked ? 0 : in->attack;
  int index=0;
  auto save = [&]() { result.stages[index++] = value; return valid(value); };
  auto scale = [&](int64_t numerator, int64_t denominator) {
    value = value * numerator / denominator;
  };
  auto has = [&](int32_t flag) { return !in->castle && (in->abilities & flag) != 0; };
  if (in->blocked) { *out = {}; return 0; }
  if (!save()) return 2;
  if (in->critical) value *= 2;
  if (!save()) return 2;
  scale(100+in->strengthen,100); if (!save()) return 2;
  if (!incoming) scale(100+in->kill_strengthen,100); if (!save()) return 2;
  scale(in->weaken,100); if (!save()) return 2;
  scale(100+in->savage,100); if (!save()) return 2;
  if (in->castle) {
    if (in->castle_breaker) value *= 4;
  } else if (!incoming) {
    if (has(KBCS_STRONG)) {
      scale(1500+in->fruit+in->strong_orb,1000); scale(100+in->strong_combo,100);
    }
    if (!save()) return 2;
    if (has(KBCS_MASSIVE)) {
      scale(900+in->fruit+in->massive_orb,300); scale(100+in->massive_combo,100);
    }
    if (!save()) return 2;
    if (has(KBCS_EXTREME)) scale(1500+in->fruit,300);
  } else {
    if (has(KBCS_STRONG)) {
      scale(1500-in->fruit,3000); scale(100-in->strong_combo,100); scale(100-in->strong_orb,100);
    }
    if (!save()) return 2;
    if (has(KBCS_RESISTANT)) {
      scale(1500-in->fruit,6000); scale(100-in->resistant_combo,100); scale(100-in->resistant_orb,100);
    }
    if (!save()) return 2;
    if (has(KBCS_SUPER_RESISTANT)) scale(2100-in->fruit,12600);
  }
  // 城では属性特性を通らないが、結果の段番号は固定する。
  if (in->castle) { if (!save() || !save()) return 2; }
  if (!save()) return 2;
  if (has(KBCS_WITCH)) {
    if (incoming) { value /= 10; scale(5-in->witch_combo/100,5); }
    else scale(int64_t(100+in->witch_combo)*5,100);
  }
  if (!save()) return 2;
  if (has(KBCS_EVA)) {
    if (incoming) { value /= 5; scale(5-in->eva_combo/100,5); }
    else scale(int64_t(100+in->eva_combo)*5,100);
  }
  if (!save()) return 2;
  if (has(KBCS_COLOSSUS)) scale(incoming?70:160,100);
  if (!save()) return 2;
  if (has(KBCS_BEHEMOTH)) scale(in->behemoth_rate,1000);
  if (!save()) return 2;
  if (has(KBCS_SAGE)) scale(in->sage_rate,1000);
  if (!save()) return 2;
  if (has(KBCS_VILLAIN) && in->villain_rate>0) scale(incoming?1000:in->villain_rate,incoming?in->villain_rate:1000);
  if (!save()) return 2;
  if (!incoming) value += int64_t(in->raw_attack)*in->attack_orb/100;
  else scale(100-in->resistance,100);
  if (!save()) return 2;
  if (incoming) {
    scale(100-in->defense_orb,100); if (!save()) return 2;
    scale(10000-in->base_reduction,10000); if (!save()) return 2;
    scale(10000-in->decoration_reduction,10000); if (!save()) return 2;
  } else { if (!save() || !save() || !save()) return 2; }
  if (in->metal && !in->critical && value > 0) value = 1;
  if (!save()) return 2;
  if (in->immune) value = 0;
  if (!save()) return 2;
  while (index<21) result.stages[index++]=value;
  result.damage=value;
  *out=result;
  return 0;
}

extern "C" double kbcs_core_expectation(const int64_t *outcomes, int32_t critical, int32_t savage) {
  if (!outcomes || !percent(critical) || !percent(savage)) return -1;
  return (double(outcomes[0])*(100-critical)*(100-savage) +
      double(outcomes[1])*critical*(100-savage) +
      double(outcomes[2])*(100-critical)*savage + double(outcomes[3])*critical*savage)/10000;
}

// 公開入口を攻撃側ごとに分ける。状態・対象の決定は呼出側、整数演算は共用する。
extern "C" uint32_t kbcs_core_unit_hit(const KbcsHitInput *in, KbcsHitOutput *out) {
  return calculateHit(in,out,false);
}
extern "C" uint32_t kbcs_core_enemy_hit(const KbcsHitInput *in, KbcsHitOutput *out) {
  return calculateHit(in,out,true);
}
// 最低1の百分率演算だけを共用し、基準HPと呼出条件は攻撃側で分ける。
static uint32_t minimumPercentage(int32_t hp, int32_t rate, int64_t &damage) {
  if (hp<0 || rate<1 || rate>100) return 1;
  const int64_t product=int64_t(hp)*rate;
  if (product>INT32_MAX) return 2;
  damage=product/100>0?product/100:1;
  return 0;
}
extern "C" uint32_t kbcs_core_unit_metal_killer(int32_t hp, int32_t rate, KbcsMetalKillerOutput *out) {
  if (!out) return 1;
  const uint32_t code=minimumPercentage(hp,rate,out->damage);
  if (code) return code;
  out->remaining_basis=hp>out->damage?int32_t(hp-out->damage):0;
  return 0;
}
extern "C" uint32_t kbcs_core_enemy_poison(const KbcsPoisonInput *in, KbcsPoisonOutput *out) {
  if (!in || !out || in->max_hp<0 || in->percent<1 || in->percent>100 ||
      !percent(in->resistance) || in->decoration_reduction<0 || in->decoration_reduction>10000) return 1;
  KbcsPoisonOutput result{};result.stages[0]=in->max_hp;
  if (in->immune) { *out=result; return 0; }
  int64_t value=0;
  const uint32_t code=minimumPercentage(in->max_hp,in->percent,value);
  if (code) return code;
  result.stages[1]=value;
  value=value*(100-in->resistance)/100;
  if (value<1) value=1;
  result.stages[2]=value;
  result.damage=value*(10000-in->decoration_reduction)/10000;
  result.stages[3]=result.damage;
  *out=result;
  return 0;
}
