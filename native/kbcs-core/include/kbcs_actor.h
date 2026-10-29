#pragma once
#include "kbcs_production.h"

#ifdef __cplusplus
extern "C" {
#endif

#define KBCS_ACTOR_WORDS 251
typedef struct { int32_t active[10],wait[10],used[10]; } KbcsSummonState;
typedef struct { KbcsSpawnRequest child;int32_t slot,parent_raw,position; } KbcsSummonInput;
typedef struct { int32_t count,last_slot,sound,failure_sound,completion_sound; } KbcsSummonOutput;
#define KBCS_ACTOR_COLUMNS 119
#define KBCS_ACTOR_SKILLS 73
#define KBCS_ACTOR_ORBS 32
/* 原本の0x3ec個体領域。型付きの動作参照と、全初期化フィールドの照合を共用する。 */
typedef struct { int32_t words[KBCS_ACTOR_WORDS]; } KbcsActor;
typedef struct {
 int32_t cells[KBCS_ACTOR_COLUMNS],count,growth[20];
 int32_t talents[KBCS_ACTOR_SKILLS][4],talent_active[KBCS_ACTOR_SKILLS],talent_min_level[KBCS_ACTOR_SKILLS];
 int32_t added_targets,orb_enabled,orbs[KBCS_ACTOR_ORBS][4],orb_present[KBCS_ACTOR_ORBS];
 int32_t speed_rule,speed_value;
} KbcsActorDefinition;
typedef struct {
 int32_t unit_modes[2],stage_width,castle_slot,castle_x,castle_scale,castle_offset;
 int32_t stage_kind,zombie,chapter_rate,crown,hp_percent,attack_percent;
 int32_t crystal_max[5],crystal[5],treasures[32],combos[32],orb_stage,talents_disabled;
 int32_t parameters[2],spawned[2],spawn_row[14],special_castle;
} KbcsActorEnvironment;
typedef struct {int32_t segments[2][15][3];} KbcsActorCannon;
typedef struct {int32_t encoded[4],attack_rate;} KbcsCannonRules;
typedef struct {int32_t kind,level,range_level,attack_level,treasure,combo,status[6];} KbcsCannonSetup;
typedef struct {int32_t kind,end,value1,value2,easing;} KbcsCannonGrowth;
typedef struct {int32_t fired,slot,sound;} KbcsCannonFire;
typedef struct { int32_t active,x,y,target,angle,speed; } KbcsSniperBullet;
typedef struct {
 float angle,desired;
 int32_t target,wait,firing,frame,gun_recoil,body_bump;
 KbcsSniperBullet bullets[50];int32_t impacts[50][6];
 int32_t smoke_active,smoke[4][5];
} KbcsActorSniper;
typedef struct { int32_t enabled,camera,height;float phase; } KbcsSniperInput;
/* 005ce564。位相は006d6d04側で1論理Fにつき6を加算する。 */
uint32_t kbcs_core_actor_sniper_step(KbcsActorSniper*,const KbcsSniperInput*,const KbcsActor actors[2][51],const KbcsActorEnvironment*,int32_t *fired);
/* 005ced48。敵の行動更新前に呼び、HPへの適用は後段の保護/healthへ残す。 */
uint32_t kbcs_core_actor_sniper_hit(KbcsActorSniper*,KbcsActor actors[2][51],const KbcsActorEnvironment*,int32_t slot,uint32_t*,int32_t *hits);
uint32_t kbcs_core_actor_summon(const KbcsSummonInput*,KbcsSummonState*,KbcsActor actors[2][51],
    const KbcsActorEnvironment*,uint32_t*,KbcsSpawnConstructor,void*,KbcsSummonOutput*);
uint32_t kbcs_core_actor_load(const int32_t *raw,int32_t count,int32_t unit_mode,int32_t loaded[KBCS_ACTOR_COLUMNS]);
/* 個体初期化の全分岐。出力個体は空き枠へ構築し、成功番号を返す。 */
uint32_t kbcs_core_actor_initialize(const KbcsActorDefinition*,KbcsActorEnvironment*,
    KbcsActor actors[2][51],const KbcsSpawnRequest*,uint32_t*,int32_t *slot);
int64_t kbcs_core_actor_last_error(void);
/* 006dda04: 通常/遠方/全方位、城・潜行中の対象を含む捕捉判定。 */
uint32_t kbcs_core_actor_contact(const KbcsActor actors[2][51],int32_t side,int32_t slot,
    int32_t target,int32_t hit,int32_t castle_slot,int32_t special_castle,int32_t *out);
uint32_t kbcs_core_actor_matches(const KbcsActor actors[2][51],const KbcsActorEnvironment*,
    int32_t side,int32_t slot,int32_t target,int32_t *out);
/* 006e9c88: 1攻撃段につき12抽選。能力確率0でも乱数を消費する。 */
uint32_t kbcs_core_actor_roll(const KbcsActor actors[2][51],int32_t side,int32_t slot,
    int32_t hit,uint32_t *seed,int32_t flags[12]);
typedef struct {
 int32_t fruit,base_reductions[4],sage[11],notifications,target_count,scenario_level;
} KbcsActorEffectContext;
typedef struct { int32_t count,events[16][2]; } KbcsActorEffectEvents;
/* 命中時のプロフィール値。form/raw_attackは味方、玉は相手の属性mapで解決する。 */
typedef struct {
 KbcsActorEffectContext effects;
 int32_t form,raw_attack[3],targeted_orbs[5][2],fruit_rates[32];
 int32_t orbs[KBCS_ACTOR_ORBS][4],orb_present[KBCS_ACTOR_ORBS];
 int32_t parameters[5],base_reductions[12],decoration_reductions[3];
} KbcsActorHitContext;
typedef struct KbcsActorHits KbcsActorHits;
uint32_t kbcs_core_actor_hits_create(KbcsActorHits**);
void kbcs_core_actor_hits_destroy(KbcsActorHits*);
/* kind0=敵slot別メタルキラー予約、kind1=敵生成通番別の攻撃者通番。 */
uint32_t kbcs_core_actor_hits_values(const KbcsActorHits*,int32_t kind,int32_t key,int32_t*,int32_t capacity,int32_t *count);
uint32_t kbcs_core_actor_hits_erase(KbcsActorHits*,int32_t kind,int32_t key);
/* BattleTextureContextの1de8/1988/1a68/2168。-1による平文側への分岐も保持する。 */
typedef struct { int32_t encoded[4],plain[4],forms[2][51],kill_orb[51],kill_threshold; } KbcsActorClock;
/* 味方006eb6b0/敵006ece50。個体の行動更新直前に被弾前の妨害値等を保存する。 */
/* beginと敵の砲/衝撃波処理の後。歩行0、敵の潜行11..13/蘇生待機14..16だけを処理し、対応可否を返す。 */
uint32_t kbcs_core_actor_walk(KbcsActor actors[2][51],const KbcsActorEnvironment*,int32_t side,int32_t slot,int32_t *handled);
uint32_t kbcs_core_actor_begin(KbcsActor actors[2][51],const KbcsActorEnvironment*,int32_t side,int32_t slot);
uint32_t kbcs_core_actor_clock(KbcsActor actors[2][51],const KbcsActorClock*);
typedef struct { int32_t encoded[8],plain[8],soul_frames; } KbcsActorMotion;
uint32_t kbcs_core_actor_motion(KbcsActor actors[2][51],int32_t side,int32_t slot,const KbcsActorMotion*);
/* 006ecae4。境界は00a9490cのモデル/城を含む取得経路から解決する。 */
uint32_t kbcs_core_actor_transition(KbcsActor actors[2][51],const KbcsActorEnvironment*,
    int32_t side,int32_t slot,const KbcsActorMotion*,int32_t boundary,int32_t *sound);
uint32_t kbcs_core_actor_resume(KbcsActor actors[2][51],int32_t side,int32_t slot);
/* 006d97dc..006d9da0。表示要求は描画側の30枠プールへ別途渡す。 */
typedef struct { int32_t shield_hit,sound_count,sounds[2],visual_count,visuals[2][4]; } KbcsActorProtection;
uint32_t kbcs_core_actor_protect(KbcsActor actors[2][51],int32_t side,int32_t slot,KbcsActorProtection*);

/* 006da994..006dac68。被弾表示のRNG後に呼び、死亡/KB判定より前へ置く。 */
typedef struct { int32_t deployment_slot,cooldown,preserve_enemy_castle; } KbcsActorHealth;
typedef struct { int32_t previous_hp,delay_slot,delay_frames,delay_x,delay_y,sound; } KbcsActorHealthResult;
uint32_t kbcs_core_actor_health(KbcsActor actors[2][51],int32_t side,int32_t slot,
    const KbcsActorHealth*,uint32_t *seed,KbcsActorHealthResult*);

/* 006dac8c..006db1ac。HPを0へ丸め、死亡の集計を行った後のKB/ワープ判定。 */
typedef struct { int32_t previous_hp,death_visual_available; } KbcsActorReaction;
typedef struct { int32_t sound_count,sounds[2],death_visual,death_x,death_y; } KbcsActorReactionResult;
uint32_t kbcs_core_actor_react(KbcsActor actors[2][51],const KbcsActorEnvironment*,
    int32_t side,int32_t slot,const KbcsActorReaction*,uint32_t *seed,KbcsActorReactionResult*);

typedef struct { int32_t boundary,cost,quiet,game_mode; } KbcsActorKnockback;
/* 006d6d04: 攻撃後・波動前のボス衝撃。shakesは表示条件の要求数。 */
uint32_t kbcs_core_actor_boss(KbcsActor actors[2][51],const KbcsActorEnvironment*,int32_t motion_frames,int32_t *sounds,int32_t *shakes);
typedef struct { int32_t handled,refund,sound; } KbcsActorKnockbackResult;
/* 味方モードの行動3/5/6/7。敵の死亡/蘇生経路へ代用しない。 */
uint32_t kbcs_core_actor_unit_knockback(KbcsActor actors[2][51],const KbcsActorEnvironment*,
    int32_t side,int32_t slot,const KbcsActorKnockback*,KbcsActorKnockbackResult*);

/* 敵の行動5/6。果実・コンボ・軽減から移動量を求める。行動3の死亡処理とは別。 */
uint32_t kbcs_core_actor_enemy_displacement(KbcsActor actors[2][51],const KbcsActorEnvironment*,
    int32_t side,int32_t slot,int32_t boundary,int32_t *handled);

typedef struct {
 int32_t boundary,quiet,game_mode,money_base,accounting_level;
 int32_t score_enabled,notifications,money_disabled,recording,timer,limit,score;
 int32_t cohort_present,cohort_count;const int32_t *cohort;
} KbcsActorEnemyDeath;
typedef struct {
 uint64_t score_display;
 int32_t handled,money,selected_bonus_slot,bonus_visual_slot,erase_cohort,cohort_serial;
 int32_t score,score_updated,record_requested,record_values[2],sound;
} KbcsActorEnemyDeathResult;
/* 敵の行動3。蘇生/盾再生成、撃破数、報酬要求を元の終了時点で確定する。 */
uint32_t kbcs_core_actor_enemy_knockback(KbcsActor actors[2][51],const KbcsActorEnvironment*,
    int32_t side,int32_t slot,const KbcsActorEnemyDeath*,KbcsActorEnemyDeathResult*);

/* 行動4の死亡演出と枠解放。残存する攻撃効果による解放保留を入力する。 */
typedef struct { int32_t blocked,body_frames,soul_frames,production_slot,cannon_base,cannon_remaining; } KbcsActorRetirement;
typedef struct { int32_t handled,removed,death_notice,reset_production,production_slot,cannon_remaining; } KbcsActorRetirementResult;
uint32_t kbcs_core_actor_retire(KbcsActor actors[2][51],const KbcsActorEnvironment*,int32_t side,int32_t slot,
    const KbcsActorRetirement*,KbcsActorRetirementResult*);
/* 両陣営の行動更新後。攻撃待機/自滅時計と、接触による攻撃・潜行開始を選ぶ。 */
uint32_t kbcs_core_actor_intent(KbcsActor actors[2][51],const KbcsActorEnvironment*,int32_t *burrow_blocked);
/* 行動1の待機。2へ移った同じ論理Fで、続く攻撃時計/発生判定も実行する。 */
uint32_t kbcs_core_actor_attack_wait(KbcsActor actors[2][51],const KbcsActorEnvironment*,int32_t side,int32_t slot,
    const KbcsActorMotion*,int32_t burrow_blocked,int32_t *handled);

typedef struct { int32_t side,slot,hit,count,targets[51]; } KbcsActorAttackSelection;
/* 同期呼出中だけ借用。命中入口はこの時点で実行し、後続段へ状態/RNGを返す。 */
typedef uint32_t (*KbcsActorAttackSink)(void*,KbcsActor actors[2][51],uint32_t*,const KbcsActorAttackSelection*);
typedef struct { int32_t handled,emitted; } KbcsActorAttackResult;
/* 行動2。段発生・単体/範囲の対象選出まで。失敗時は戦闘を停止し、部分状態で継続しない。 */
uint32_t kbcs_core_actor_attack(KbcsActor actors[2][51],const KbcsActorEnvironment*,int32_t side,int32_t slot,
    const KbcsActorMotion*,uint32_t*,KbcsActorAttackSink,void*,KbcsActorAttackResult*);

typedef struct { int32_t side,slot,target,hit,kind,parameter,rate,flags[12]; } KbcsActorDirectHit;
typedef struct { int32_t flags[12],parameter; } KbcsActorEmission;
typedef uint32_t (*KbcsActorHitSink)(void*,KbcsActor actors[2][51],uint32_t*,const KbcsActorDirectHit*,int32_t *applied);
/* 006e92bc/006ea1c0の直接命中区間。出力の抽選結果を続く波動/烈波/爆波へ同じ順で渡す。 */
uint32_t kbcs_core_actor_emit_direct(KbcsActor actors[2][51],const KbcsActorEnvironment*,const KbcsActorAttackSelection*,
    uint32_t*,KbcsActorHitSink,void*,KbcsActorEmission*);

/* 原本の48byte×200枠と、対象51行×200枠の命中履歴。予約/表示の有無で省略しない。 */
typedef struct {
 int32_t side,slot,state,frame,x,level,hit;
 uint8_t flags[12];int32_t parameter;uint8_t mini,reserved[3];
} KbcsActorWave;
typedef struct { KbcsActorWave records[200];uint8_t hits[51][200]; } KbcsActorWaves;
/* 直接命中の直後、烈波/爆波より前。生成した枠番号、未生成なら-1を返す。 */
uint32_t kbcs_core_actor_emit_wave(const KbcsActor actors[2][51],const KbcsActorEnvironment*,const KbcsActorAttackSelection*,
    const KbcsActorEmission*,KbcsActorWaves*,uint32_t*,int32_t *slot);

/* 原本レコードの数値部分。末尾の履歴木/ポインタは所有ランタイムで管理する。 */
typedef struct {
 int32_t side,slot,frame,x,level,hit;
 uint8_t flags[12];int32_t parameter;uint8_t mini,reserved[3];int32_t kind;
} KbcsActorSurge;
typedef struct {
 int32_t side,slot,frame,x,hit;uint8_t flags[12];int32_t parameter;
} KbcsActorExplosion;
typedef struct {
 int32_t surge_present,explosion_present;KbcsActorSurge surge;KbcsActorExplosion explosion;
} KbcsActorAreaEmission;
/* 波動の後に呼び、烈波→爆波の順に生成する。記録は次の攻撃段より前に所有者へ登録する。 */
uint32_t kbcs_core_actor_emit_area(const KbcsActor actors[2][51],const KbcsActorEnvironment*,const KbcsActorAttackSelection*,
    const KbcsActorEmission*,uint32_t*,KbcsActorAreaEmission*);

/* 005d3af8→005d4158→005d4988。描画と独立して履歴/反射待ち/寿命を所有する。 */
typedef struct KbcsActorAreas KbcsActorAreas;
typedef struct { KbcsActorDirectHit hit;int32_t attack_type; } KbcsActorSecondaryHit;
typedef uint32_t (*KbcsActorSecondarySink)(void*,KbcsActor actors[2][51],uint32_t*,const KbcsActorSecondaryHit*,int32_t *applied);
/* 波動は6つの表示/接触区間を持つ。履歴と区間の時計を所有者が保持する。 */
typedef struct { int32_t frame,x; } KbcsActorWaveSegment;
typedef struct { KbcsActorWaveSegment records[200][6]; } KbcsActorWaveSegments;
typedef struct { int32_t small_interval,small_start,small_end,motion_frames[2],game_mode; } KbcsActorWaveRules;
/* phase0=005d287c（生成・消滅）、phase1=005d2c18（遮断→候補→命中）。 */
uint32_t kbcs_core_actor_waves_step(int32_t phase,KbcsActorWaves*,KbcsActorWaveSegments*,
    KbcsActor actors[2][51],const KbcsActorEnvironment*,const KbcsActorWaveRules*,uint32_t*,
    KbcsActorSecondarySink,void*,int32_t *sounds);
typedef struct {
 int32_t summon_sound_frame,summon_frame,summon_motion[2];
 int32_t explosion_frames[4],explosion_widths[3],explosion_damage[3];
} KbcsActorAreaRules;
typedef struct { int32_t side,slot,state,frame,x,level,offset,span;uint8_t mini,reserved[3]; } KbcsActorReflection;
typedef struct { int32_t cycles[51];uint8_t present[51]; } KbcsActorAreaHistory;
typedef struct { uint8_t hits[51][5]; } KbcsActorExplosionHistory;
typedef struct { int32_t surges,reflections,explosions,events; } KbcsActorAreaCounts;
/* kind0=SE、kind1=画面振動。各phase開始時に前の通知だけを解除する。 */
typedef struct { int32_t kind,value; } KbcsActorAreaEvent;
uint32_t kbcs_core_actor_areas_create(KbcsActorAreas**);
void kbcs_core_actor_areas_destroy(KbcsActorAreas*);
uint32_t kbcs_core_actor_areas_append(KbcsActorAreas*,const KbcsActorAreaEmission*);
uint32_t kbcs_core_actor_areas_counts(const KbcsActorAreas*,KbcsActorAreaCounts*);
/* 006eb978/006ed4ec。unit_routeは行動関数の経路。爆波を独自の解放待ち条件に加えない。 */
uint32_t kbcs_core_actor_areas_retirement_blocked(const KbcsActorAreas*,const KbcsActorWaves*,int32_t side,int32_t slot,int32_t unit_route,int32_t*);
uint32_t kbcs_core_actor_areas_surge(const KbcsActorAreas*,int32_t,KbcsActorSurge*,KbcsActorAreaHistory*);
uint32_t kbcs_core_actor_areas_reflection(const KbcsActorAreas*,int32_t,KbcsActorReflection*);
uint32_t kbcs_core_actor_areas_explosion(const KbcsActorAreas*,int32_t,KbcsActorExplosion*,KbcsActorExplosionHistory*);
uint32_t kbcs_core_actor_areas_event(const KbcsActorAreas*,int32_t,KbcsActorAreaEvent*);
/* phase0=烈波、1=反射待ち、2=爆波。callback失敗後の所有状態は破棄し、継続しない。 */
uint32_t kbcs_core_actor_areas_step(KbcsActorAreas*,int32_t phase,KbcsActor actors[2][51],const KbcsActorEnvironment*,
    const KbcsActorAreaRules*,uint32_t*,KbcsActorSecondarySink,void*);

typedef struct {
 int32_t guard_enabled,notice[2];
 const KbcsStageRow *rows;const KbcsStageState *states;int32_t count;
} KbcsActorDamageContext;
/* 006e4aec/006e79bc本体。回避・無効・毒撃・妨害・予約・寄与者記録を含む。 */
uint32_t kbcs_core_actor_hit(KbcsActorHits*,KbcsActor actors[2][51],const KbcsActorEnvironment*,
    const KbcsActorHitContext*,const KbcsActorClock*,KbcsActorDamageContext*,
    const KbcsActorSecondaryHit*,uint32_t*,int32_t *applied,KbcsActorEffectEvents*);
/* HUDの表示更新と論理Fを区別する。同じbatch内の要求も発生時点で処理する。 */
// SEはKBCS_BATTLE_SCREEN_SOUND + 音源ID。既存の更新イベント0..5とは分離する。
enum { KBCS_BATTLE_SCREEN_SOUND = 0x10000 };
typedef uint32_t (*KbcsBattleScreenHook)(void*,int32_t event,KbcsBattleScreenState*);
uint32_t kbcs_core_battle_screen_advance(const KbcsBattleScreenConfig*,const KbcsBattleScreenState*,
    const KbcsBattleScreenInput*,KbcsBattleScreenState*,KbcsBattleScreenLayout*,KbcsBattleScreenHook,void*);
/* ホスト拡張。通常の入口は即時生産を無効にして同じ本体を呼ぶ。 */
uint32_t kbcs_core_battle_screen_advance_custom(const KbcsBattleScreenConfig*,const KbcsBattleScreenState*,
    const KbcsBattleScreenInput*,KbcsBattleScreenState*,KbcsBattleScreenLayout*,KbcsBattleScreenHook,void*,int32_t immediate);
/* 00a9bbac/005bbc90。ダメージを予約し、個別の一撃とバリアを比較する。 */
uint32_t kbcs_core_actor_damage(KbcsActor actors[2][51],const KbcsActorEnvironment*,
    KbcsActorDamageContext*,int32_t side,int32_t slot,int32_t damage);
/* 対象一致・呪い・攻撃種別の条件を通過した妨害だけを入力する。命中入口全体とは分離。 */
uint32_t kbcs_core_actor_effects(KbcsActor actors[2][51],const KbcsActorEnvironment*,
    const KbcsActorEffectContext*,int32_t side,int32_t slot,int32_t target,
    const int32_t flags[7],uint32_t *seed,KbcsActorEffectEvents*);

uint32_t kbcs_core_actor_cannon_setup(KbcsActor*,const KbcsCannonSetup*,const KbcsCannonGrowth*,int32_t);
uint32_t kbcs_core_actor_cannon_fire(KbcsActor actors[2][51],const KbcsActorEnvironment*,const KbcsSpawnRequest*,uint32_t*,KbcsSpawnConstructor,void*,KbcsCannonFire*);
uint32_t kbcs_core_actor_cannon_action(KbcsActorCannon*,KbcsActor actors[2][51],const KbcsCannonRules*,int32_t);
uint32_t kbcs_core_actor_cannon_hit(KbcsActorCannon*,KbcsActor actors[2][51],const KbcsActorEnvironment*,const KbcsActorHitContext*,const KbcsActorClock*,KbcsActorDamageContext*,const KbcsCannonRules*,int32_t,int32_t,int32_t,uint32_t*,KbcsActorEffectEvents*);
uint32_t kbcs_core_actor_cannon_step(KbcsActorCannon*,KbcsActor actors[2][51],const KbcsActorEnvironment*,const KbcsActorHitContext*,const KbcsActorClock*,KbcsActorDamageContext*,const KbcsCannonRules*,int32_t,uint32_t*,KbcsActorEffectEvents*);
#ifdef __cplusplus
}
#endif
