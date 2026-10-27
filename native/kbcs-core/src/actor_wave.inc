// 005d287c/005d2c18。遮断の走査を全波動の命中より先に行い、候補を後から確定する。
namespace {
void stopWave(KbcsActorWave &wave,KbcsActorWaveSegment (&segments)[6]){
 wave.side=0;wave.frame=0;wave.level=0;for(auto &part:segments)part.frame=0;
}
void waveStopped(Context &context,int side,int slot){context.actors[side][slot].words[94]=0;context.actors[side][slot].words[95]=1;}
int waveElapsed(const KbcsActorWave &wave,const KbcsActorWaveSegment &part,const KbcsActorWaveRules &rules){
 return rules.motion_frames[wave.mini!=0]-part.frame-2;
}
bool waveContact(Context &context,const KbcsActorWave &wave,const KbcsActorWaveSegment &part,int target,int width){
 const int other=wave.state==1?1:0;
 const auto &actor=context.actors[other][target].words;
 const int position=other?actor[3]-actor[14]:actor[3]+actor[14]-width;
 return part.x-width<=position&&position<part.x+width;
}
bool waveTarget(Context &context,const KbcsActorWave &wave,int target,bool hit_phase){
 if(wave.state!=1&&wave.state!=2)return false;
 const int other=wave.state==1?1:0;
 if(!context.actors[other][target].words[0])return false;
 if(other&&hit_phase&&target==context.environment.castle_slot)return false;
 return n_00a94484(context,other,target,wave.slot);
}
void advanceWaves(Context &context,KbcsActorWaves &waves,KbcsActorWaveSegments &segments,const KbcsActorWaveRules &rules,int &sounds){
 const int stride=int(context.read(0xc24400,4))*5;
 for(int i=0;i<200;++i){
  auto &wave=waves.records[i];const int interval=wave.mini?rules.small_interval:4;
  if(wave.side!=1&&wave.side!=2)continue;
  const int frame=++wave.frame,cycle=Context::divide(frame,interval);
  if(frame!=cycle*interval)continue;
  auto &parts=segments.records[i];auto *free=std::find_if(std::begin(parts),std::end(parts),[](auto &part){return !part.frame;});
  if(free==std::end(parts))continue;
  if(!rules.game_mode)++sounds;
  free->frame=rules.motion_frames[wave.mini!=0]-1;wave.state=wave.side;
  free->x=wave.x+(wave.side==1?-stride*cycle:-stride+stride*cycle)+270;
  if(wave.level<=cycle){wave.side=0;wave.frame=0;}
 }
 for(int i=0;i<200;++i){
  auto &wave=waves.records[i];const auto &parts=segments.records[i];
  if(!wave.side&&wave.state&&std::none_of(std::begin(parts),std::end(parts),[](auto &part){return part.frame>0;}))wave.state=0;
 }
}
void hitWaves(Context &context,KbcsActorWaves &waves,KbcsActorWaveSegments &segments,const KbcsActorWaveRules &rules,KbcsActorSecondarySink sink,void *user){
 const int width=int(context.read(0xc24400,4))*5;
 for(int i=0;i<200;++i){
  auto &wave=waves.records[i];auto &parts=segments.records[i];
  for(auto &part:parts){
   if(part.frame<=0)continue;--part.frame;
   const int elapsed=waveElapsed(wave,part,rules),start=wave.mini?rules.small_start:3,end=wave.mini?rules.small_end:7;
   if(elapsed<start||elapsed>end)continue;
   for(int target=1;target<51;++target){
    if(waves.hits[target][i]||!waveTarget(context,wave,target,false)||!waveContact(context,wave,part,target,width))continue;
    const int other=wave.state==1?1:0;
    if(context.actors[other][target].words[87]!=1)continue;
    stopWave(wave,parts);waveStopped(context,other,target);
   }
  }
 }
 struct Candidate {int wave,target;};std::vector<Candidate> candidates;std::array<int,200> stoppers;stoppers.fill(-1);
 for(int i=0;i<200;++i){
  const auto &wave=waves.records[i];
  for(const auto &part:segments.records[i]){
   if(part.frame<=0||waveElapsed(wave,part,rules)!=(wave.mini?rules.small_end:7))continue;
   for(int target=1;target<51;++target){
    if(waves.hits[target][i]||!waveTarget(context,wave,target,true)||!waveContact(context,wave,part,target,width))continue;
    const int other=wave.state==1?1:0;
    if(n_00a9b0b8(context,other,target)){
     const int previous=stoppers[i];
     if(previous<0||context.actors[other][target].words[3]<context.actors[other][candidates[previous].target].words[3])stoppers[i]=int(candidates.size());
    }
    candidates.push_back({i,target});
   }
  }
 }
 for(size_t j=0;j<candidates.size();++j){
  const auto [index,target]=candidates[j];auto &wave=waves.records[index];const int other=wave.state==1?1:0;
  if(stoppers[index]>=0&&stoppers[index]!=int(j)){
   const int x=context.actors[other][target].words[3];
   if(wave.state==2?wave.x<x:x<wave.x)continue;
  }
  waves.hits[target][index]=1;
  if(wave.state!=1&&wave.state!=2)continue;
  const int side=wave.state-1;
  const bool applied=secondaryHit(context,sink,user,1,side,wave.slot,target,wave.hit,wave.mini,side?0:wave.parameter,100,wave.flags);
  if(applied&&n_00a9b0b8(context,other,target)){stopWave(wave,segments.records[index]);waveStopped(context,other,target);}
 }
}
}
extern "C" uint32_t kbcs_core_actor_waves_step(int32_t phase,KbcsActorWaves *waves,KbcsActorWaveSegments *segments,
 KbcsActor actors[2][51],const KbcsActorEnvironment *environment,const KbcsActorWaveRules *rules,uint32_t *seed,
 KbcsActorSecondarySink sink,void *user,int32_t *sounds){
 if(phase<0||phase>1||!waves||!segments||!actors||!environment||!rules||!seed||!*seed||!sink||!sounds)return 1;
 try{
  const KbcsActorDefinition definition{};auto copy=*environment;const KbcsSpawnRequest request{};Context context{definition,copy,actors,request,*seed};int count=0;
  if(phase)hitWaves(context,*waves,*segments,*rules,sink,user);else advanceWaves(context,*waves,*segments,*rules,count);
  *sounds=count;return 0;
 }catch(const AttackFailure &failure){return failure.code;}catch(...){return 3;}
}
