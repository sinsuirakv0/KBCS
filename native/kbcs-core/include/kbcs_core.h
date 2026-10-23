#pragma once
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif
uint32_t kbcs_core_abi_version(void);
uint32_t kbcs_core_ruleset_version(void);
typedef struct { int32_t kind, index; } KbcsMapIdentity;
uint32_t kbcs_core_map_decode(int32_t id, KbcsMapIdentity *output);
uint32_t kbcs_core_map_encode(const KbcsMapIdentity *input, int32_t *output);
typedef struct { int32_t mode, selected_kind, zombie, invasion, invasion_zombie, ignore, ex_override, ex_marker; } KbcsCurrentKind;
uint32_t kbcs_core_stage_current_kind(const KbcsCurrentKind *input, int32_t *output);
uint32_t kbcs_core_random_bounded(uint32_t *state, int32_t bound, int32_t *output);

typedef struct { int32_t attack, kind, percent, wave_percent; } KbcsAttackPreparation;
uint32_t kbcs_core_prepare_attack(const KbcsAttackPreparation *input, int32_t *output);
typedef struct {
  int32_t base, growth, treasure, combo, talent, extra;
} KbcsStatInput;
typedef struct { int64_t stages[6]; } KbcsStatOutput;

typedef struct {
  int32_t base, row_percent, crown_percent, crystal_max, crystal_treasure, castle_attack;
} KbcsEnemyStatInput;
typedef struct { int64_t stages[3]; } KbcsEnemyStatOutput;
uint32_t kbcs_core_enemy_stat(const KbcsEnemyStatInput *input, KbcsEnemyStatOutput *output);

typedef struct { int32_t count, mode, acquired, radar, chances[3], rolls[3]; } KbcsLegendRewardInput;
typedef struct { int32_t winner, consumed, mark_acquired, radar_blocked; } KbcsLegendRewardOutput;
uint32_t kbcs_core_legend_reward_pick(const KbcsLegendRewardInput *input, KbcsLegendRewardOutput *output);

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
uint32_t kbcs_core_stage_row_decode(const int32_t *cells, int32_t count, KbcsStageRow *output);
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
typedef struct { int32_t base, study_level, treasure, combo, okame; } KbcsEventExperienceInput;
uint32_t kbcs_core_event_experience(const KbcsEventExperienceInput *input, KbcsExperienceOutput *output);
typedef struct { int32_t mode, kind, stage, base, clears, study_level, treasure, combo, okame; } KbcsStageExperienceInput;
uint32_t kbcs_core_stage_experience(const KbcsStageExperienceInput *input, KbcsExperienceOutput *output);

typedef struct { int32_t elapsed, best, count, thresholds[10]; } KbcsStageScoreInput;
typedef struct { int32_t score, best, improved, reward_mask; } KbcsStageScoreOutput;
uint32_t kbcs_core_stage_score(const KbcsStageScoreInput *input, KbcsStageScoreOutput *output);
uint32_t kbcs_core_stage_score_tick(int32_t elapsed, int32_t phase, int32_t *output);
typedef struct { int32_t chance, map_index, minimum, maximum, group_present; } KbcsExTransitionInput;
typedef struct { int32_t group, threshold, map_index, stage; } KbcsExChoice;
typedef struct { int32_t group, source, map_index, stage, consumed, bounds[3], rolls[3]; } KbcsExTransitionOutput;
uint32_t kbcs_core_stage_ex(const KbcsExTransitionInput *input, const KbcsExChoice *choices,
    int32_t count, uint32_t *state, KbcsExTransitionOutput *output);
uint32_t kbcs_core_stage_reward_pick(const KbcsLegendRewardInput *input, KbcsLegendRewardOutput *output);
uint32_t kbcs_core_reward_weight_total(const int32_t *weights, int32_t count, int32_t *total);
uint32_t kbcs_core_reward_weight_pick(const int32_t *weights, int32_t count, int32_t roll, int32_t *winner);
typedef struct { int32_t mode, seen, radar, winner; } KbcsWeightedFinishInput;
typedef struct { int32_t grant_column, mark_history, radar_blocked; } KbcsWeightedFinishOutput;
uint32_t kbcs_core_reward_weight_finish(const KbcsWeightedFinishInput *input, KbcsWeightedFinishOutput *output);
typedef struct { int32_t redirect, factor, limit; } KbcsItemDefinition;
typedef struct { int32_t target, total, change; } KbcsItemGrant;
uint32_t kbcs_core_item_add(const KbcsItemDefinition *definitions, int32_t *counts,
    int32_t count, int32_t index, int32_t amount, KbcsItemGrant *output);
typedef struct { float count, multiplier; int32_t miss, weights[16]; } KbcsMaterialInput;
typedef struct { double chance, at_least_one, expected; } KbcsMaterialChance;
typedef struct { int32_t draws; double miss, none; KbcsMaterialChance items[16]; } KbcsMaterialOutput;
uint32_t kbcs_core_material_plan(const KbcsMaterialInput *input, KbcsMaterialOutput *output);
uint32_t kbcs_core_material_pick(const KbcsMaterialInput *input, int32_t miss_roll, int32_t weight_roll, int32_t *slot);
// 描画側がKBと昇天の時計を別々に進めないための共有入力。
typedef struct { int32_t elapsed; int32_t soul_frames; int32_t special_frames; } KbcsMotionPlaybackInput;
typedef struct { int32_t phase; int32_t frame; double x; double y; } KbcsMotionPlaybackOutput;
uint32_t kbcs_core_motion_playback(const KbcsMotionPlaybackInput* in, KbcsMotionPlaybackOutput* out);

#ifdef __cplusplus
}
#endif
