#include "kbcs_core.h"

// 15.7.2 ARM64: 0058b7d4 / 0063c560。施設Lvの内部値は表示Lv-1。
extern "C" uint32_t kbcs_core_castle_health(const KbcsCastleHealthInput* in,KbcsCastleHealthOutput* out) {
    if (!in || !out || in->facility_level<1 || in->facility_level>30 || in->development_level<1 || in->development_level>30 || in->treasure_bonus<0 || in->treasure_bonus>42000 || in->combo_percent<0 || in->combo_percent>1000) return 1;
    const int32_t level=in->facility_level-1;
    KbcsCastleHealthOutput value{};
    value.facility=level<4 ? 1000+level*1000 : level<8 ? level*2000-2000 : level*3000-9000;
    // CC_Castle_growth.csvの3区間はいずれも1Lvあたり4000の線形補間。
    value.development=(in->development_level-1)*4000;
    value.before_combo=value.facility+value.development+in->treasure_bonus;
    value.maximum=int32_t(int64_t(value.before_combo)*(100+in->combo_percent)/100);
    value.sniper=value.maximum/20;
    *out=value;
    return 0;
}

// 005ced48 / 00a9327c。候補・弾到達・RNG取得は呼出側。成功時は判定1回＋演出4回を消費する。
extern "C" uint32_t kbcs_core_sniper_hit(const KbcsSniperHitInput* in,KbcsSniperHitOutput* out) {
    if (!in || !out || in->castle_maximum<1 || in->metal<0 || in->metal>1 || in->dodge_active<0 || in->dodge_chance<0 || in->dodge_chance>100 || in->roll<0 || in->roll>99) return 1;
    KbcsSniperHitOutput value{};
    if (!in->dodge_active) {
        value.random_consumed=1;
        if (in->roll>=in->dodge_chance) { value.damage=in->metal ? 1 : in->castle_maximum/20;value.knockback=1;value.random_consumed=5; }
        else value.dodged=1;
    }
    *out=value;
    return 0;
}

// 006d6d04。描画1回に対する論理更新回数で、攻撃力・待機F自体は変えない。
extern "C" uint32_t kbcs_core_battle_steps(int32_t speed,int32_t paused,int32_t* out) {
    if (!out || speed<1 || speed>3 || paused<0 || paused>1) return 1;
    *out=paused ? 0 : speed;
    return 0;
}

// 00aa0568。固定コストの早期分岐と、倍率ごとの整数化を保つ。
extern "C" uint32_t kbcs_core_deploy_cost(const KbcsDeployCostInput* in,int32_t* out) {
    if (!in || !out || in->raw<0 || in->raw>1000000 || in->reduction<0 || in->reduction>1000000 || in->chapter<0 || in->chapter>2 || in->multiplier<0 || in->multiplier>10000 || in->fixed<-1 || in->fixed>1000000 || in->rarity_rate<0 || in->rarity_rate>10000) return 1;
    const int64_t base=in->raw>in->reduction ? in->raw-in->reduction : 0;
    int64_t value=in->fixed>=0 ? int64_t(in->fixed)*100 : in->multiplier ? base*in->multiplier : (base*(in->chapter+2)/2)*100;
    if (in->fixed<0) value=value*in->rarity_rate/100;
    if (value>INT32_MAX) return 2;
    *out=int32_t(value/100);
    return 0;
}

// 出撃可否と動的な同時出撃数を混同しない。理由bit: レア度/枠/コスト/キャラ群/レア度別編成数。
extern "C" uint32_t kbcs_core_deployment(const KbcsDeploymentInput* in,uint32_t* out) {
    if (!in || !out || in->rarity<0 || in->rarity>5 || in->slot<0 || in->slot>9 || in->cost<0 || in->mask<0 || in->mask>63 || in->slots<0 || in->minimum<0 || in->maximum<0 || in->group_type<-1 || in->group_type>2 || in->in_group<0 || in->in_group>1 || in->phase<0 || in->phase>1 || in->rarity_limit<-1 || in->preceding<0 || in->preceding>9) return 1;
    uint32_t reasons=0;
    if (in->mask && !(in->mask & (1<<in->rarity))) reasons|=1;
    if (in->phase && in->slots==1 && in->slot>=5) reasons|=2;
    bool cost=true;
    if (in->minimum && in->maximum && in->minimum>in->maximum) cost=in->cost>=in->minimum || in->cost<=in->maximum;
    else cost=(!in->minimum || in->cost>=in->minimum) && (!in->maximum || in->cost<=in->maximum);
    if (!cost) reasons|=4;
    if ((in->group_type==2 && in->in_group) || ((in->group_type==0 || (in->group_type==1 && !in->phase)) && !in->in_group)) reasons|=8;
    if (in->rarity_limit>=0 && in->preceding>=in->rarity_limit) reasons|=16;
    *out=reasons;
    return 0;
}
