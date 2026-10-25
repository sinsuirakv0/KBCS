#pragma once
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif
uint32_t kbcs_core_abi_version(void);
uint32_t kbcs_core_ruleset_version(void);

typedef struct { int32_t facility_level,development_level,treasure_bonus,combo_percent; } KbcsCastleHealthInput;
typedef struct { int32_t facility,development,before_combo,maximum,sniper; } KbcsCastleHealthOutput;
uint32_t kbcs_core_castle_health(const KbcsCastleHealthInput*,KbcsCastleHealthOutput*);
typedef struct { int32_t castle_maximum,metal,dodge_active,dodge_chance,roll; } KbcsSniperHitInput;
typedef struct { int32_t damage,knockback,random_consumed,dodged; } KbcsSniperHitOutput;
uint32_t kbcs_core_sniper_hit(const KbcsSniperHitInput*,KbcsSniperHitOutput*);
uint32_t kbcs_core_battle_steps(int32_t speed,int32_t paused,int32_t* output);
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


// 009e505c / 00aa0568。選択済みの制限行とコスト設定だけを受け取る。
typedef struct { int32_t raw,reduction,chapter,multiplier,fixed,rarity_rate; } KbcsDeployCostInput;
uint32_t kbcs_core_deploy_cost(const KbcsDeployCostInput*,int32_t*);
typedef struct { int32_t rarity,slot,cost,mask,slots,minimum,maximum,group_type,in_group,phase,rarity_limit,preceding; } KbcsDeploymentInput;
uint32_t kbcs_core_deployment(const KbcsDeploymentInput*,uint32_t*);

// 正規化した原本を借用し、整数姿勢とGPU非依存の描画四角形を返す。
typedef struct { int32_t cells[13]; } KbcsRenderPart;
typedef struct { int32_t x,y,width,height; } KbcsRenderCut;
typedef struct { int32_t frame,value,easing,power; } KbcsRenderKey;
typedef struct { int32_t part,property,loop,first,count; } KbcsRenderTrack;
typedef struct { int32_t units[3],frame,loop,anchor,facing,config[6],root_override; double root[5]; } KbcsPoseInput;
typedef struct { int32_t part,cut,blend; double opacity; int32_t points[8]; } KbcsPosePacket;
uint32_t kbcs_core_pose(const KbcsPoseInput*,const KbcsRenderPart*,int32_t,const KbcsRenderCut*,int32_t,const KbcsRenderTrack*,int32_t,const KbcsRenderKey*,int32_t,KbcsPosePacket*,int32_t*);
// 背景・城の描画座標。UIや描画デバイスの状態を参照しない。
typedef struct { double width,center,zoom; int32_t cut_height,castle[3],focus,viewport_width,battle_rows; } KbcsSceneInput;
typedef struct { double width,center,zoom,minimum,top,bottom,enemy[4],player_x,viewport_width,y_origin,y_offset; } KbcsSceneLayout;
uint32_t kbcs_core_scene_layout(const KbcsSceneInput*,KbcsSceneLayout*);


typedef struct { int32_t texture,layer,count,blend; double opacity,points[16]; int32_t cut[4],colors[6]; } KbcsDrawCommand;
typedef struct { KbcsSceneInput scene; int32_t cut[4],top[4],colors[12],overlay[7],self_sizes[6],show_enemy,show_player; } KbcsPaintInput;
uint32_t kbcs_core_scene_paint(const KbcsPaintInput*,KbcsSceneLayout*,KbcsDrawCommand*,int32_t,int32_t*);
uint32_t kbcs_core_scene_transform(const KbcsSceneLayout*,const KbcsDrawCommand*,double,double,double,KbcsDrawCommand*);
typedef struct { double rect[4],angle,opacity; int32_t texture,layer,blend,cut[4]; } KbcsSpriteInput;
uint32_t kbcs_core_scene_sprite(const KbcsSceneLayout*,const KbcsSpriteInput*,KbcsDrawCommand*);


#define KBCS_EFFECT_PROPERTIES 37
typedef struct { int32_t kind,base,low_base,high_base; double value,low,high; int32_t first,count,group; } KbcsEffectSpec;
typedef struct { KbcsEffectSpec properties[KBCS_EFFECT_PROPERTIES]; int32_t first,count; } KbcsEffectSegment;
typedef struct { int32_t asset,front,kind,variant; double x,y,frame,scale,sx,sy,angle,alpha,spacing; int32_t spacing_min,spacing_max,color[3]; } KbcsEffectParticle;
uint32_t kbcs_core_effect_create(double,int32_t,const KbcsEffectSegment*,int32_t,const double*,int32_t,const int32_t*,const int32_t*,int32_t,uint32_t,void**);
uint32_t kbcs_core_effect_frame(void*,int32_t,KbcsEffectParticle*,int32_t,int32_t*);
void kbcs_core_effect_destroy(void*);

uint32_t kbcs_core_weather_draw(const KbcsSceneLayout*,const KbcsEffectParticle*,const KbcsRenderCut*,int32_t,const KbcsRenderCut*,int32_t,const int32_t*,KbcsDrawCommand*);

uint32_t kbcs_core_scene_instance(const KbcsSceneLayout*,const KbcsDrawCommand*,double,double,double,int32_t,KbcsDrawCommand*);


/* 戦闘画面の時計・入力。個体生成は要求の出力までで、成功を仮定しない。 */
typedef struct {
 int32_t worker_level,wallet_level,attack_level,charge_level,chapter;
 int32_t income_treasure,wallet_treasure,charge_treasure,speed_treasure;
 int32_t income_combo,wallet_combo,charge_combo,charge_start_combo,items,speed,fixed_money;
 int32_t costs[10],present[10],blocked[10],viewport_width,description_lines[10];
} KbcsBattleScreenConfig;
typedef struct {
 int32_t frame,intro,rows,page,page_frame,page_direction,paused,money,worker,cannon;
 int32_t holding,hold_frames,pointer_down,pointer_x,pointer_y,guard,pending_control,items_on,request_slot,request_cannon;
 int32_t ui_frame,speed_mode,wallet_flash,description_item,description_wait,start_x,start_y,gesture,page_step,request_action,bgm_level,se_level,vibration_on,info_mode,info_slot,saved_rows,hud_frame;
} KbcsBattleScreenState;
typedef struct { int32_t ticks,phase,x,y,control; } KbcsBattleScreenInput;
typedef struct {
 int32_t slots[10][4],labels[10][2],modes[10],order[10],scene_y,wallet_max,income,upgrade_cost,cannon_max,cannon_initial,cannon_gauge;
 int32_t fade_count,fade_sizes[21],fade[21][8];
 int32_t controls[8][5],item_icons[6][5],pause_icon[4],money_base,speed_value,cannon_base,cannon_label,cannon_bands,wallet_base,info_box[4],description_box[4],description_arrow[6];
 int32_t menu_count,menu_sprites[24][6];
} KbcsBattleScreenLayout;
uint32_t kbcs_core_battle_screen_step(const KbcsBattleScreenConfig*,const KbcsBattleScreenState*,const KbcsBattleScreenInput*,KbcsBattleScreenState*,KbcsBattleScreenLayout*);

#ifdef __cplusplus
}
#endif
