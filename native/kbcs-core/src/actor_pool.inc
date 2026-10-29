// 通常の51枠ABIは維持し、所有戦闘の追加個体だけを動的領域へ置く。
namespace {
constexpr int64_t actorBase=0x40000000LL,actorStride=0x10000000LL;
struct ActorExtra {
 KbcsActor actors[2]{};
 int32_t profiles[2]{-1,-1},forms[2]{},kill_orb=0,impacts[2][4]{};
 bool bonus=false;
 std::array<uint8_t,200> waves{};
};
struct ActorPool {
 KbcsActor (*base)[51];std::deque<ActorExtra> extra;
 int size() const {return 51+int(extra.size());}
};
thread_local ActorPool *activePool=nullptr;
struct ActorPoolScope {
 ActorPool *previous;
 explicit ActorPoolScope(ActorPool &pool):previous(activePool){activePool=&pool;}
 explicit ActorPoolScope(ActorPool *pool):previous(activePool){activePool=pool;}
 ~ActorPoolScope(){activePool=previous;}
};
int actorEnd(){return activePool?activePool->size():51;}
int actorCount(const KbcsActor (*base)[51]){return activePool&&activePool->base==base?activePool->size():51;}
KbcsActor &actorAt(KbcsActor (*base)[51],int side,int slot){
 if(side<0||side>1||slot<0||slot>=actorCount(base))throw std::out_of_range("actor slot");
 return slot<51?base[side][slot]:activePool->extra[slot-51].actors[side];
}
const KbcsActor &actorAt(const KbcsActor (*base)[51],int side,int slot){return actorAt(const_cast<KbcsActor (*)[51]>(base),side,slot);}
int actorForm(const KbcsActorClock *clock,int side,int slot){return slot<51?clock->forms[side][slot]:activePool->extra[slot-51].forms[side];}
int actorKillOrb(const KbcsActorClock *clock,int slot){return slot<51?clock->kill_orb[slot]:activePool->extra[slot-51].kill_orb;}
thread_local const KbcsActorAttackSelection *extendedSelection=nullptr;
thread_local const std::vector<int> *extendedTargets=nullptr;
struct ActorTargetScope {
 const KbcsActorAttackSelection *previous;const std::vector<int> *targets;
 ActorTargetScope(const KbcsActorAttackSelection &value,const std::vector<int> &values):previous(extendedSelection),targets(extendedTargets){extendedSelection=&value;extendedTargets=&values;}
 ~ActorTargetScope(){extendedSelection=previous;extendedTargets=targets;}
};
}
extern "C" int32_t kbcs_core_actor_slot_count(){return actorEnd();}
