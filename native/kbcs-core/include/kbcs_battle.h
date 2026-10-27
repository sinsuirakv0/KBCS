#pragma once
#include "kbcs_actor.h"
#ifdef __cplusplus
extern "C" {
#endif

/* DB・描画から独立した所有戦闘。生成時に入力を複製し、外部ポインタを保持しない。 */
typedef struct { int32_t effect,mask,values[4]; } KbcsBattleOrb;
typedef struct {int32_t unit_id,values[32];} KbcsBattleUnitCombo;
typedef struct {int32_t kind,rate,tier_count,tiers[32][2],fever_count,fever[10];} KbcsPointRules;
typedef struct {int32_t score,origin,wait,frame,phase,ending,gauge;} KbcsBattlePoints;
typedef struct {int32_t event,count,values[2],timer,limit;} KbcsPointInput;
uint32_t kbcs_core_battle_point_add(const KbcsPointRules*,KbcsBattlePoints*,const KbcsPointInput*);
uint32_t kbcs_core_battle_point_fever(const KbcsPointRules*,KbcsBattlePoints*,int32_t *changed);
uint32_t kbcs_core_battle_point_display(const KbcsPointRules*,KbcsBattlePoints*);
uint32_t kbcs_core_battle_point_render(const KbcsPointRules*,KbcsBattlePoints*);
/* 原本のマップ種別と解決済みルール。総生産上限の-1はルールなし。 */
typedef struct {
 int32_t native_kind,score_type,time_limit,bonus[32],rarity_limits[6],slot_rarity[10],total_limit;
 int32_t extra_rule[3],production_kind,production_periods[6],recharge_fixed;
 int32_t cost_chapter;
 KbcsPointRules point;
 int32_t unit_combo_count;KbcsBattleUnitCombo unit_combos[32];
} KbcsBattleRules;
typedef struct {int32_t mode,timer,elapsed,score,finished_frame,reason;} KbcsBattleResult;
/* 006e15e8。スコア加算と表示補間は別。表示更新1回ごとに進める。 */
typedef struct {int32_t phase,frame,origin,value,scale;} KbcsScoreDisplay;
uint32_t kbcs_core_battle_score_display(int32_t,KbcsScoreDisplay*);
typedef struct {int32_t blocked[10],active[6],total,warning[2];} KbcsBattleDeployment;
typedef struct {int32_t fixed_money,money,cost,rarity_limit,active,total_limit,total;} KbcsBattleLimit;
uint32_t kbcs_core_battle_limit(const KbcsBattleLimit*,int32_t*);
uint32_t kbcs_core_battle_bonus(const KbcsBattleRules*,int32_t type,int32_t count,int32_t*);
void kbcs_core_battle_screen_economy(const KbcsBattleScreenConfig*,KbcsBattleScreenState*);
uint32_t kbcs_core_battle_result_step(const KbcsBattleRules*,KbcsBattleResult*,int32_t phase,int32_t frame,int32_t castle_slot,KbcsActor actors[2][51],uint32_t*);
typedef struct {
 KbcsActorDefinition definition;
 KbcsSpawnRequest spawn;
 KbcsActorMotion motion;
 int32_t deployment_slot,cost,recharge,recharge_plain,money_base,boundary,death_body_frames,death_soul_frames,summon_mode;
 int32_t raw_attack[3],orb_count;KbcsBattleOrb orbs[8];
 KbcsProductionCost price;
} KbcsBattleProfile;
typedef struct {
 KbcsActorEnvironment environment;
 KbcsBattleScreenConfig screen;
 KbcsBattleScreenState state;
 KbcsActorClock clock;
 KbcsActorHitContext hit;
 KbcsActorAreaRules areas;
 KbcsActorWaveRules waves;
 int32_t castle_hp[2],enemy_max,unit_max,global_min,global_max;
 int32_t accounting_level,death_surge_time,death_surge_motion[2],guard_enabled;
 int32_t castle_offsets[6],summon_position,boss_frames,castle_y_offset,effect_clocks[64][3];
 int32_t price_rule[4];
 KbcsBattleRules rules;
 KbcsActor castle;KbcsCannonRules cannon;
 uint32_t seed;
} KbcsBattleConfig;
typedef struct {int32_t kind,side,slot,phase,frame,x,y,layer,root[2];} KbcsBattleVisual;
typedef struct { int32_t gauges[10][5],health[2][3];double anchors[2][2],scale;int32_t title[2],summons[10][5]; } KbcsBattleHud;
typedef struct {int32_t frame,id;} KbcsBattleSound;

/* 006ee6c8。候補選択は表示更新ごと。可否と価格は呼出時の値を渡す。 */
typedef struct {
 int32_t enabled,mode,worker,money,wallet,upgrade_cost,worker_level;
 int32_t page,page_frame,page_direction,page_step,full;
 int32_t cannon_wait,cannon_action,cannon_range,castle_x,camera;
 int32_t raw[10],cost[10],eligible[10],wait[10],summoned[10];
} KbcsComputerInput;
typedef struct {
 int32_t action,selected,pending_raw,cannon_state,cannon_wait,candidates[10],choices[10];
} KbcsComputerState;
typedef struct {int32_t deploy,upgrade,fire,page_start,page_step;} KbcsComputerOutput;
uint32_t kbcs_core_battle_computer(const KbcsComputerInput*,KbcsComputerState*,const KbcsActor opponents[51],uint32_t*,KbcsComputerOutput*);
typedef struct KbcsBattle KbcsBattle;
/* 006ddfb8の上部表示と、終了帯の原本描画。texture0=img001、1=FeverEffect、2=任意のステージ名。 */
uint32_t kbcs_core_battle_top_draw(const KbcsBattle*,const KbcsRenderCut*,int32_t,const KbcsRenderCut*,int32_t,const KbcsRenderCut*,KbcsDrawCommand*,int32_t,int32_t*);
uint32_t kbcs_core_battle_overlay(const KbcsBattle*,KbcsDrawCommand*,int32_t,int32_t*);
/* 報酬抽選は勝敗確定の同じ論理Fで行い、保存だけをホストへ返す。 */
typedef struct {int32_t enabled,mode,count,acquired,radar,chances[10],material_enabled;KbcsMaterialInput material;int32_t win_type,win_count,win_sounds[32],lose_type,lose_count,lose_sounds[32];int32_t music[2],music_threshold,music_delay,start_sound;KbcsExTransitionInput ex;int32_t ex_count;KbcsExChoice ex_choices[32];} KbcsBattleRewardRules;
typedef struct {int32_t id,serial,wait,changed,started,delay;} KbcsBattleMusic;
typedef struct {int32_t left,zoom,moving,width,rows;} KbcsBattleEndCamera;
typedef struct {int32_t ready,winner,mark,radar_blocked,materials[16];uint32_t seed_before,seed_after;} KbcsBattleRewards;
typedef struct {int32_t index,count,phase,scale_frame,flash,wait;} KbcsBattlePopup;
typedef struct {int32_t viewport,count,widths[8],scale_frame,cut[4],padding[2];} KbcsBattlePopupInput;
typedef struct {int32_t body[4],text_y,text_x[8],parts[9][8];float text_scale[8];} KbcsBattlePopupLayout;
typedef struct {int32_t phase,frame,panel,title[3],bar_x,number_x,shade,ready,button[4],visual_button[4],label[4],pressed,guard,action;KbcsBattlePopup popup;} KbcsBattleEnding;
uint32_t kbcs_core_battle_notifications(KbcsBattle*,int32_t count);
uint32_t kbcs_core_battle_popup_step(int32_t release,KbcsBattlePopup*);
uint32_t kbcs_core_battle_popup_layout(const KbcsBattlePopupInput*,KbcsBattlePopupLayout*);
uint32_t kbcs_core_battle_reward_rules(KbcsBattle*,const KbcsBattleRewardRules*);
uint32_t kbcs_core_battle_rewards(const KbcsBattle*,KbcsBattleRewards*);
uint32_t kbcs_core_battle_ending(const KbcsBattle*,KbcsBattleEnding*);
uint32_t kbcs_core_battle_ending_step(int32_t mode,int32_t point,KbcsBattleEnding*);
uint32_t kbcs_core_battle_music(const KbcsBattle*,KbcsBattleMusic*);
uint32_t kbcs_core_battle_end_camera(const KbcsBattle*,KbcsBattleEndCamera*);
uint32_t kbcs_core_battle_ex(const KbcsBattle*,KbcsExTransitionOutput*);
uint32_t kbcs_core_battle_end_camera_step(KbcsBattleEndCamera*);
uint32_t kbcs_core_battle_music_cross(const KbcsBattleRewardRules*,int32_t previous,int32_t current,int32_t maximum,KbcsBattleMusic*);
uint32_t kbcs_core_battle_music_tick(const KbcsBattleRewardRules*,KbcsBattleMusic*);
typedef struct {const KbcsRenderCut *cuts[2];int32_t counts[2],textures[2];} KbcsBattleAtlases;
uint32_t kbcs_core_battle_camera(KbcsBattle*,const KbcsSceneLayout*);
uint32_t kbcs_core_battle_sniper_draw(const KbcsBattle*,const KbcsSceneLayout*,const KbcsBattleAtlases*,KbcsDrawCommand*,int32_t,int32_t*);
uint32_t kbcs_core_actor_cannon_draw(const KbcsActor*,int32_t,const KbcsSceneLayout*,const KbcsBattleAtlases*,KbcsDrawCommand*,int32_t,int32_t*);
uint32_t kbcs_core_battle_hit_draw(const KbcsBattle*,const KbcsSceneLayout*,const KbcsBattleAtlases*,KbcsDrawCommand*,int32_t,int32_t*);
uint32_t kbcs_core_battle_cannon_draw(const KbcsBattle*,const KbcsSceneLayout*,const KbcsBattleAtlases*,KbcsDrawCommand*,int32_t,int32_t*);
uint32_t kbcs_core_battle_sniper_status(const KbcsBattle*,int32_t out[5]);
uint32_t kbcs_core_battle_viewport(KbcsBattle*,int32_t);
uint32_t kbcs_core_battle_error(const KbcsBattle*,int32_t out[4]);
uint32_t kbcs_core_battle_sounds(const KbcsBattle*,const KbcsBattleSound**,int32_t*);
uint32_t kbcs_core_battle_computer_state(const KbcsBattle*,KbcsComputerState*);
uint32_t kbcs_core_battle_result(const KbcsBattle*,KbcsBattleResult*);
uint32_t kbcs_core_battle_deployment(const KbcsBattle*,KbcsBattleDeployment*);
uint32_t kbcs_core_battle_visuals(KbcsBattle*,const KbcsBattleVisual**,int32_t*);
uint32_t kbcs_core_battle_hud(const KbcsBattle*,const KbcsSceneLayout*,const int32_t point[2],KbcsBattleHud*);
uint32_t kbcs_core_battle_create(const KbcsBattleConfig*,const KbcsBattleProfile*,int32_t,
    const KbcsStageRow*,int32_t,KbcsBattle**);
void kbcs_core_battle_destroy(KbcsBattle*);
uint32_t kbcs_core_battle_advance(KbcsBattle*,const KbcsBattleScreenInput*,KbcsBattleScreenState*,KbcsBattleScreenLayout*);
/* 借用は次のadvance/破棄まで。同じhandleへ並列にアクセスしない。 */
uint32_t kbcs_core_battle_actors(const KbcsBattle*,const KbcsActor **actors,const int32_t **profiles);
uint32_t kbcs_core_battle_production(const KbcsBattle*,KbcsProductionState*,uint32_t *seed);
uint32_t kbcs_core_battle_prices(const KbcsBattle*,int32_t out[10]);
uint32_t kbcs_core_battle_extras(const KbcsBattle*,const KbcsProductionExtra**,int32_t*);
uint32_t kbcs_core_battle_points(const KbcsBattle*,KbcsBattlePoints*);
#ifdef __cplusplus
}
#endif
