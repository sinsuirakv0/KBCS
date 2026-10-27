// actor.cpp内で同版getter/Contextを共有する。原本の履歴木を対象1..50の配列へ正規化する。
static_assert(sizeof(KbcsActorReflection)==36&&sizeof(KbcsActorSecondaryHit)==80&&sizeof(KbcsActorAreaRules)==56);
struct KbcsActorAreas {
 struct Surge {KbcsActorSurge record;KbcsActorAreaHistory history{};};
 struct Explosion {KbcsActorExplosion record;KbcsActorExplosionHistory history{};};
 std::vector<Surge> surges;
 std::vector<KbcsActorReflection> reflections;
 std::vector<Explosion> explosions;
 std::vector<KbcsActorAreaEvent> events;
 bool busy=false,failed=false;
};
namespace {
constexpr int storedProcOrder[]={0,1,2,3,4,6,8,7,5,9,10,11};
int32_t areaPosition(Context &context,int side,int slot){
 const auto &words=context.actors[side][slot].words;
 return side?words[3]-words[14]:words[3]+words[14];
}
bool secondaryHit(Context &context,KbcsActorSecondarySink sink,void *user,int type,int side,int slot,int target,
 int hit,int mini,int parameter,int rate,const uint8_t *flags){
 KbcsActorSecondaryHit call{};call.attack_type=type;
 auto &value=call.hit;value.side=side;value.slot=slot;value.target=target;value.hit=hit;
 value.kind=mini;value.parameter=parameter;value.rate=rate;
 for(int i=0;i<12;++i)value.flags[storedProcOrder[i]]=flags[i];
 if(!side){value.flags[9]=0;value.flags[11]=0;}
 int32_t applied=0;const uint32_t code=sink(user,context.actors,&context.seed,&call,&applied);
 if(code||!context.seed||applied<0||applied>1)throw AttackFailure{code?code:1};
 return applied!=0;
}
void surgeHit(KbcsActorAreas &areas,Context &context,KbcsActorAreas::Surge &state,int target,KbcsActorSecondarySink sink,void *user){
 const auto &value=state.record;const int side=value.side,slot=value.slot;
 const int rate=side?100:value.kind==1?int32_t(n_00a98e50(context,side,slot)):value.kind==2?int32_t(n_00a98ca4(context,side,slot)):100;
 if(!secondaryHit(context,sink,user,2,side,slot,target,value.hit,int(value.mini)<<1,side?0:value.parameter,rate,value.flags))return;
 const int other=1-side;
 if(!n_00a98dbc(context,other,target)||state.history.present[target]||value.kind==1)return;
 KbcsActorReflection reflection{};reflection.side=other;reflection.slot=target;
 reflection.x=n_00a9482c(context,other,target);
 if(value.kind==2){
  reflection.level=n_00a98c18(context,side,slot);reflection.offset=n_00a98b00(context,side,slot);
  reflection.span=n_00a98b8c(context,side,slot);reflection.mini=n_00a98d30(context,side,slot)!=0;
 }else{
  reflection.level=n_00a989dc(context,side,slot);reflection.offset=n_00a988c4(context,side,slot);
  reflection.span=n_00a98950(context,side,slot);reflection.mini=n_00a987f8(context,side,slot)!=0;
 }
 areas.reflections.push_back(reflection);
 if(n_00a98edc(context,other,target)){n_00a98e04(context,other,target,0);n_00a98f24(context,other,target,0);}
}
void stepSurges(KbcsActorAreas &areas,Context &context,KbcsActorSecondarySink sink,void *user){
 const int width=context.read(0xc23e68,4),start=context.read(0xc23e6c,4),period=context.read(0xc23e70,4);
 const int tail=context.read(0xc23e74,4),offset=context.read(0xc23e78,4);
 for(size_t i=0;i<areas.surges.size();){
  auto &state=areas.surges[i];auto &value=state.record;
  const int previous=value.frame;const int elapsed=++value.frame-start;
  if(elapsed<0){if(previous==0)areas.events.push_back({0,0x6f});}
  else{
   const int duration=value.level*period;
   if(elapsed<duration){
    const int cycle=Context::divide(elapsed,period);
    if(elapsed==cycle*period){areas.events.push_back({1,2});areas.events.push_back({0,0x70});}
    const int other=1-value.side;
    for(int target=1;target<51;++target){
     if(!n_00a93f08(context,other,target)||!n_00a94484(context,other,target,value.slot))continue;
     if(state.history.present[target]&&state.history.cycles[target]==cycle)continue;
     const int x=areaPosition(context,other,target)+(value.side==1?-offset:offset);
     if(value.x-width/2<=x&&x<value.x+width/2){
      surgeHit(areas,context,state,target,sink,user);
      state.history.present[target]=1;state.history.cycles[target]=cycle;
     }
    }
   }else if(duration+tail<=elapsed){areas.surges.erase(areas.surges.begin()+i);continue;}
  }
  ++i;
 }
}
void stepReflections(KbcsActorAreas &areas,Context &context,const KbcsActorAreaRules &rules){
 for(size_t i=0;i<areas.reflections.size();){
  auto &value=areas.reflections[i];
  if(value.state==1){areas.reflections.erase(areas.reflections.begin()+i);continue;}
  if(value.frame==rules.summon_sound_frame)areas.events.push_back({0,0x9f});
  ++value.frame;
  if(value.frame==rules.summon_frame){
   n_006e9c88(context,0,value.side,value.slot,0);
   KbcsActorSurge surge{};surge.side=value.side;surge.slot=value.slot;surge.level=value.level;
   const int span=value.span,draw=n_0044a8d8(context,span<0?-span:span);
   const int delta=value.offset+(span>0?draw:-draw);
   surge.x=n_00a9482c(context,value.side,value.slot)+(value.side==1?delta:-delta);
   for(int j=0;j<12;++j)surge.flags[j]=context.procs[storedProcOrder[j]]!=0;
   surge.parameter=n_00a9adf0(context,value.side,value.slot);surge.mini=value.mini;surge.kind=1;
   areas.surges.push_back({surge,{}});
   // 生成したFは、演出寿命の判定を飛ばして次の待機へ進む。
   ++i;continue;
  }
  if(value.frame>=rules.summon_frame&&value.frame>=rules.summon_motion[value.side]){areas.reflections.erase(areas.reflections.begin()+i);continue;}
  ++i;
 }
}
void stepExplosions(KbcsActorAreas &areas,Context &context,const KbcsActorAreaRules &rules,KbcsActorSecondarySink sink,void *user){
 const int wait=rules.explosion_frames[0],active=rules.explosion_frames[1],tail=rules.explosion_frames[2],interval=rules.explosion_frames[3];
 for(size_t i=0;i<areas.explosions.size();){
  auto &state=areas.explosions[i];auto &value=state.record;++value.frame;
  const int phases=std::min(Context::divide(value.frame,interval)+1,3);
  for(int phase=0;phase<phases;++phase){
   const int distance=phase==0?0:phase==1?rules.explosion_widths[0]+rules.explosion_widths[1]:rules.explosion_widths[0]+rules.explosion_widths[1]*2+rules.explosion_widths[2];
   const int elapsed=value.frame-interval*phase;
   if(elapsed==wait)areas.events.push_back({0,0xa7+phase});
   if(elapsed<wait||elapsed>=wait+active)continue;
   const int other=1-value.side;
   for(int target=1;target<51;++target){
    if(!n_00a93f08(context,other,target)||!n_00a94484(context,other,target,value.slot))continue;
    const int x=areaPosition(context,other,target);
    for(int half=0;half<(phase?2:1);++half){
     const int part=phase+(half?2:0),center=value.x-distance/2+half*distance,width=rules.explosion_widths[phase]/2;
     if(state.history.hits[target][part]||x<center-width||x>=center+width)continue;
     secondaryHit(context,sink,user,3,value.side,value.slot,target,value.hit,0,value.side?0:value.parameter,rules.explosion_damage[phase],value.flags);
     state.history.hits[target][part]=1;
    }
   }
  }
  if(wait+interval*2+active+tail<=value.frame){areas.explosions.erase(areas.explosions.begin()+i);continue;}
  ++i;
 }
}
bool validAreaActor(int side,int slot){return side>=0&&side<2&&slot>0&&slot<51;}
}
extern "C" uint32_t kbcs_core_actor_areas_create(KbcsActorAreas **out){if(!out)return 1;try{*out=new KbcsActorAreas;return 0;}catch(...){return 3;}}
extern "C" void kbcs_core_actor_areas_destroy(KbcsActorAreas *areas){delete areas;}
extern "C" uint32_t kbcs_core_actor_areas_append(KbcsActorAreas *areas,const KbcsActorAreaEmission *value){
 if(!areas||!value||areas->busy||areas->failed||value->surge_present<0||value->surge_present>1||value->explosion_present<0||value->explosion_present>1)return 1;
 if(value->surge_present&&(!validAreaActor(value->surge.side,value->surge.slot)||value->surge.hit<0||value->surge.hit>2))return 1;
 if(value->explosion_present&&(!validAreaActor(value->explosion.side,value->explosion.slot)||value->explosion.hit<0||value->explosion.hit>2))return 1;
 try{if(value->surge_present)areas->surges.push_back({value->surge,{}});if(value->explosion_present)areas->explosions.push_back({value->explosion,{}});return 0;}
 catch(...){areas->failed=true;return 3;}
}
extern "C" uint32_t kbcs_core_actor_areas_counts(const KbcsActorAreas *areas,KbcsActorAreaCounts *out){
 if(!areas||!out||areas->busy)return 1;
 if(areas->surges.size()>INT32_MAX||areas->reflections.size()>INT32_MAX||areas->explosions.size()>INT32_MAX||areas->events.size()>INT32_MAX)return 2;
 *out={int32_t(areas->surges.size()),int32_t(areas->reflections.size()),int32_t(areas->explosions.size()),int32_t(areas->events.size())};return 0;
}
extern "C" uint32_t kbcs_core_actor_areas_retirement_blocked(const KbcsActorAreas *areas,const KbcsActorWaves *waves,int32_t side,int32_t slot,int32_t unit_route,int32_t *out){
 if(!areas||!waves||!out||areas->busy||!validAreaActor(side,slot)||unit_route<0||unit_route>1)return 1;
 bool blocked=false;
 for(const auto &value:waves->records)if(value.slot==slot&&value.state==(unit_route?1:2)){blocked=true;break;}
 for(const auto &value:areas->surges)if(value.record.side==side&&value.record.slot==slot){blocked=true;break;}
 if(!unit_route)for(const auto &value:areas->reflections)if(value.side==side&&value.slot==slot){blocked=true;break;}
 *out=blocked;return 0;
}
extern "C" uint32_t kbcs_core_actor_areas_surge(const KbcsActorAreas *areas,int32_t i,KbcsActorSurge *out,KbcsActorAreaHistory *history){
 if(!areas||!out||areas->busy||i<0||size_t(i)>=areas->surges.size())return 1;*out=areas->surges[i].record;if(history)*history=areas->surges[i].history;return 0;
}
extern "C" uint32_t kbcs_core_actor_areas_reflection(const KbcsActorAreas *areas,int32_t i,KbcsActorReflection *out){
 if(!areas||!out||areas->busy||i<0||size_t(i)>=areas->reflections.size())return 1;*out=areas->reflections[i];return 0;
}
extern "C" uint32_t kbcs_core_actor_areas_explosion(const KbcsActorAreas *areas,int32_t i,KbcsActorExplosion *out,KbcsActorExplosionHistory *history){
 if(!areas||!out||areas->busy||i<0||size_t(i)>=areas->explosions.size())return 1;*out=areas->explosions[i].record;if(history)*history=areas->explosions[i].history;return 0;
}
extern "C" uint32_t kbcs_core_actor_areas_event(const KbcsActorAreas *areas,int32_t i,KbcsActorAreaEvent *out){
 if(!areas||!out||areas->busy||i<0||size_t(i)>=areas->events.size())return 1;*out=areas->events[i];return 0;
}
extern "C" uint32_t kbcs_core_actor_areas_step(KbcsActorAreas *areas,int32_t phase,KbcsActor actors[2][51],const KbcsActorEnvironment *environment,
 const KbcsActorAreaRules *rules,uint32_t *seed,KbcsActorSecondarySink sink,void *user){
 if(!areas||areas->busy||areas->failed||phase<0||phase>2||!actors||!environment||!rules||!seed||!*seed||!sink)return 1;
 areas->busy=true;
 try{
  KbcsActorDefinition definition{};auto copy=*environment;KbcsSpawnRequest request{};
  Context context{definition,copy,actors,request,*seed};areas->events.clear();
  if(phase==0)stepSurges(*areas,context,sink,user);else if(phase==1)stepReflections(*areas,context,*rules);else stepExplosions(*areas,context,*rules,sink,user);
  areas->busy=false;return 0;
 }catch(const AttackFailure &error){areas->busy=false;areas->failed=true;return error.code;}
 catch(...){areas->busy=false;areas->failed=true;return 3;}
}
