#pragma once
#include "kbcs_core.h"

#ifdef __cplusplus
extern "C" {
#endif

/* 009f1e64のparam_2..8。rawはDBのID+2、level_indexは内部の0始まり。 */
typedef struct { int32_t side,raw,level_index,layer_min,layer_max,form,row; } KbcsSpawnRequest;
typedef struct { int32_t stage_width,castle_slot; } KbcsSpawnGeometry;
typedef struct { int32_t slot,unit_id,x,y,layer; } KbcsSpawnPlacement;
/* occupiedは城用0を含む51枠。空き探索とレイヤー抽選までで、個体を完成扱いにしない。 */
uint32_t kbcs_core_spawn_prepare(const KbcsSpawnRequest*,const KbcsSpawnGeometry*,
    const int32_t occupied[51],uint32_t*,KbcsSpawnPlacement*);
uint32_t kbcs_core_spawn_boss_position(int32_t castle_x,int32_t scale,int32_t offset,int32_t*);
/* 00aa08f8→0058c05c。base/talentは読込済みF、研究力Lvは内部0始まり。 */
typedef struct { int32_t base,talent,research_level,treasure,combo,stage_percent,override_frames; } KbcsRechargeInput;
uint32_t kbcs_core_production_recharge(const KbcsRechargeInput*,int32_t*);
/* 005be130。base/last_costは1/100円、ruleは特殊ルール11の原本順。 */
typedef struct {int32_t base,last_cost,count,rule[3];} KbcsProductionPrice;
uint32_t kbcs_core_production_price(const KbcsProductionPrice*,int32_t*);
/* 00aa0568。comboは対象を解決した原本順の率。固定価格は全修飾を迂回する。 */
typedef struct {int32_t enabled,raw,talent,chapter,multiplier,fixed,rarity_rate,orb_rate,orb_enabled,combo_count,combos[32];} KbcsProductionCost;
uint32_t kbcs_core_production_cost(const KbcsProductionCost*,int32_t*);
/* 005c2f88と009f4a74。producedは呼出時点の通常生産数。 */
uint32_t kbcs_core_production_condition(int32_t produced,int32_t kind,int32_t period,int32_t*);
uint32_t kbcs_core_production_wait(int32_t base,int32_t reduction,int32_t*);

/* 呼出中だけ借用する実個体構築。成功は1..50、失敗は-1/-2。例外を境界外へ出さない。 */
typedef int32_t (*KbcsSpawnConstructor)(void*,const KbcsSpawnRequest*,uint32_t*);
typedef struct {
 int32_t money,wait[10],maximum[10],produced[10],last_cost[10],total;
} KbcsProductionState;
typedef struct {
 KbcsSpawnRequest spawn;
 int32_t slot,present,allowed,blocked,summon_mode,cost,recharge,reduction,recharge_enabled,notify_failure;
} KbcsProductionInput;
typedef struct { int32_t slot,sound; } KbcsProductionOutput;
typedef struct {int32_t slot,wait;} KbcsProductionExtra;
uint32_t kbcs_core_production_extra_plan(const int32_t rule[3],int32_t rarity,int32_t slot,KbcsProductionExtra*,int32_t capacity,int32_t* count);
uint32_t kbcs_core_production_extra_tick(KbcsProductionExtra*,int32_t* count,KbcsProductionState*,const KbcsSpawnRequest slots[10],uint32_t*,KbcsSpawnConstructor,void*);
uint32_t kbcs_core_production_deploy(const KbcsProductionInput*,KbcsProductionState*,
    uint32_t*,KbcsSpawnConstructor,void*,KbcsProductionOutput*);
/* 006d6d04の再生産待ち1論理F。上限へ戻すFには減算しない。 */
uint32_t kbcs_core_production_clock(KbcsProductionState*,const int32_t recharge[10],uint32_t* ready);

typedef struct { int32_t row,slot; } KbcsEnemyProductionOutput;
/* 生成→全体抽選→行抽選→commit→初回出現フラグを同じ呼出内で行う。 */
uint32_t kbcs_core_production_enemy(const KbcsStageRow*,KbcsStageState*,int32_t,
    KbcsStageContext*,uint32_t*,int32_t* seen,int32_t seen_count,
    KbcsSpawnConstructor,void*,KbcsEnemyProductionOutput*);
/* 敵城行は通常commitと異なり、構築失敗でも初期化時点で行を消費する。 */
uint32_t kbcs_core_production_start(const KbcsStageRow*,KbcsStageState*,int32_t,
    int32_t global_min,int32_t global_max,int32_t castle_raw,uint32_t*,
    KbcsSpawnConstructor,void*,KbcsStageStartOutput*,KbcsEnemyProductionOutput*);

#ifdef __cplusplus
}
#endif
