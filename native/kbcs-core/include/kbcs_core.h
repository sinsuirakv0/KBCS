#pragma once
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif
uint32_t kbcs_core_abi_version(void);
uint32_t kbcs_core_ruleset_version(void);
typedef struct {
  int32_t base, growth, treasure, combo, talent, extra;
} KbcsStatInput;
typedef struct { int64_t stages[6]; } KbcsStatOutput;

enum KbcsAbility {
  KBCS_STRONG=1, KBCS_MASSIVE=2, KBCS_EXTREME=4,
  KBCS_RESISTANT=8, KBCS_SUPER_RESISTANT=16,
  KBCS_WITCH=32, KBCS_EVA=64, KBCS_COLOSSUS=128,
  KBCS_BEHEMOTH=256, KBCS_SAGE=512, KBCS_VILLAIN=1024
};
typedef struct {
  int32_t attack, raw_attack, critical, strengthen, weaken, savage;
  int32_t abilities, fruit, castle, castle_breaker, metal, blocked;
  int32_t strong_combo, massive_combo, resistant_combo, witch_combo, eva_combo;
  int32_t strong_orb, massive_orb, resistant_orb, attack_orb, defense_orb;
  int32_t behemoth_rate, sage_rate, base_reduction, decoration_reduction;
  int32_t resistance, immune, kill_strengthen, villain_rate;
} KbcsHitInput;
typedef struct { int64_t damage; int64_t stages[21]; } KbcsHitOutput;

uint32_t kbcs_core_stat(const KbcsStatInput *input, KbcsStatOutput *output);
uint32_t kbcs_core_unit_hit(const KbcsHitInput *input, KbcsHitOutput *output);
uint32_t kbcs_core_enemy_hit(const KbcsHitInput *input, KbcsHitOutput *output);
typedef struct { int64_t damage; int32_t remaining_basis; } KbcsMetalKillerOutput;
typedef struct { int32_t max_hp, percent, resistance, decoration_reduction, immune; } KbcsPoisonInput;
uint32_t kbcs_core_unit_metal_killer(int32_t hp, int32_t percent, KbcsMetalKillerOutput *output);
typedef struct { int64_t damage; int64_t stages[4]; } KbcsPoisonOutput;
uint32_t kbcs_core_enemy_poison(const KbcsPoisonInput *input, KbcsPoisonOutput *output);
double kbcs_core_expectation(const int64_t *outcomes, int32_t critical, int32_t savage);

typedef struct { int32_t cells[14]; } KbcsStageRow;
typedef struct { int32_t wait, spawned, kills; } KbcsStageState;
typedef struct { int32_t global_min, global_max, global_roll, castle_raw; } KbcsStageStart;
typedef struct { int32_t global_wait, castle_row; } KbcsStageStartOutput;
uint32_t kbcs_core_stage_initialize(const KbcsStageRow *rows, KbcsStageState *states,
    int32_t count, const KbcsStageStart *input, KbcsStageStartOutput *output);
typedef struct {
  int32_t global_wait, kill_delta, active_enemies, max_enemies;
  int32_t castle_hp, castle_max_hp, castle_damage, damage_condition, paused;
  int32_t global_min, global_max;
} KbcsStageContext;

uint32_t kbcs_core_stage_tick(const KbcsStageRow *rows, KbcsStageState *states,
    int32_t count, KbcsStageContext *context, int32_t *candidate);
uint32_t kbcs_core_stage_commit(const KbcsStageRow *rows, KbcsStageState *states,
    int32_t count, KbcsStageContext *context, int32_t candidate,
    int32_t global_roll, int32_t row_roll);
typedef struct { int32_t base, clears, study_level, treasure, combo, okame; } KbcsLegendExperienceInput;
typedef struct { int64_t stages[5]; } KbcsExperienceOutput;
uint32_t kbcs_core_legend_experience(const KbcsLegendExperienceInput *input, KbcsExperienceOutput *output);
typedef struct { float count, multiplier; int32_t miss, weights[16]; } KbcsMaterialInput;
typedef struct { double chance, at_least_one, expected; } KbcsMaterialChance;
typedef struct { int32_t draws; double miss, none; KbcsMaterialChance items[16]; } KbcsMaterialOutput;
uint32_t kbcs_core_material_plan(const KbcsMaterialInput *input, KbcsMaterialOutput *output);
uint32_t kbcs_core_material_pick(const KbcsMaterialInput *input, int32_t miss_roll, int32_t weight_roll, int32_t *slot);
#ifdef __cplusplus
}
#endif
