// 006d6d04のボス走査。出現Fの通常行動/攻撃が済んだ後に行動7へ移す。
extern "C" uint32_t kbcs_core_actor_boss(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,int32_t frames,int32_t *sounds,int32_t *shakes){
 if(!actors||!environment||!sounds||!shakes||frames<0)return 1;*sounds=0;*shakes=0;if(environment->unit_modes[1]&1)return 0;
 for(int boss=0;boss<actorEnd();++boss){auto &w=actorAt(actors,1,boss).words;if(!w[64])continue;
  if(!w[65]){++*sounds;if(w[64]==2)++*shakes;
   KbcsActorDefinition definition{};KbcsActorEnvironment environment{};KbcsSpawnRequest request{};uint32_t seed=1;Context c{definition,environment,actors,request,seed};
   for(int slot=1;slot<actorEnd();++slot)if(n_00a94484(c,0,slot,-1)&&!actorAt(actors,0,slot).words[116]){n_00a94274(c,0,slot,7);n_00a9478c(c,0,slot,0);}
  }
  w[65]=std::min(w[65]+1,frames);
 }return 0;
}
// actor.cppの原本getterと所有効果を共有し、フレーム中に個体配列を複製しない。
extern "C" uint32_t kbcs_core_actor_summon(const KbcsSummonInput *input,KbcsSummonState *state,KbcsActor actors[2][51],
 const KbcsActorEnvironment *environment,uint32_t *seed,KbcsSpawnConstructor construct,void *user,KbcsSummonOutput *out){
 if(!input||!state||!actors||!environment||!seed||!*seed||!construct||!out||input->slot<0||input->slot>9||input->parent_raw<2||input->child.side!=0)return 1;
 try{
  const int slot=input->slot;KbcsSummonOutput result{0,-1,-1,15,-1};
  if(!state->active[slot]||state->wait[slot]>0||state->used[slot]){*out=result;return 0;}
  for(int parent=1;parent<actorEnd();++parent){const auto &source=actorAt(actors,0,parent).words;if(source[0]!=input->parent_raw||source[1]==4)continue;
   const int child=construct(user,&input->child,seed);result.last_slot=child;
   if(child== -1){result.failure_sound=15;*out=result;return 0;}if(child<1||child>=actorEnd()||!*seed)return 1;
   state->used[slot]=1;if(!result.count)result.sound=162;
   KbcsActorDefinition definition{};auto env=*environment;Context context{definition,env,actors,input->child,*seed};
   n_00a991a0(context,0,child,slot);
   const int extent=actorAt(actors,0,child).words[13];int x=source[3]-input->position*4;
   if(x-extent<3200)x=extent+3200;x=std::min(x,environment->stage_width-3200);
   n_00a9486c(context,0,child,x);n_00a95338(context,0,child,1);n_00a95ebc(context,0,child,2);
   n_00a9b7d0(context,0,child,100);n_00a9b85c(context,0,child,10000);n_00a9b50c(context,0,child,1);n_00a94274(context,0,child,2);
   ++result.count;result.failure_sound=-1;
  }
  if(result.count)result.completion_sound=19;
  *out=result;return 0;
 }catch(...){return 3;}
}
struct KbcsBattle {
 KbcsBattleRewardRules reward_rules=[]{KbcsBattleRewardRules r{};r.music[0]=-1;r.music[1]=-1;r.start_sound=-1;return r;}();KbcsBattleRewards rewards{};KbcsBattleEnding ending{};bool popup_release=false,ending_clicked=false;
 bool end_sound=false;KbcsScoreDisplay score_display{0,0,0,0,100};
 KbcsBattleMusic music{-1,0,0,0,0,0};
 KbcsBattleEndCamera end_camera{};KbcsExTransitionOutput ex{};
 KbcsBattleConfig config;
 std::vector<KbcsBattleProfile> definitions;
 std::vector<KbcsStageRow> rows;
 std::vector<KbcsStageState> states;
 std::vector<int32_t> seen;
 std::vector<KbcsBattleVisual> visuals,transient;
 std::vector<KbcsBattleSound> sounds;
 std::array<KbcsBattleVisual,30> killer_visuals{},barrier_visuals{},shield_visuals{};
 std::array<KbcsBattleVisual,200> critical_visuals{};
 KbcsActor actors[2][51]{};
 int32_t profiles[2][51]{};
 mutable ActorPool pool{actors,{}};
 mutable std::vector<KbcsBattleActorRef> actor_refs;
 KbcsActorHits hits;
 KbcsActorAreas areas;
 KbcsActorWaves waves{};
 KbcsActorWaveSegments segments{};
 KbcsProductionState production{};
 std::vector<KbcsProductionExtra> extras;
 KbcsSummonState summons{};
 KbcsActorCannon cannon{};
 KbcsActorSniper sniper{};float sniper_phase=0;int32_t camera=0;double camera_zoom=1;
 KbcsComputerState computer{};
 KbcsBattleResult result{};
 KbcsBattlePoints points{};
 int32_t warning[2]{};
 KbcsStageContext stage{};
 int32_t impacts[2][56][4]{};
 int32_t notice[2]{},kills=0,current_frame=0,preserve_castle=0;
 bool bonus_slots[51]{};
 uint32_t seed;
 bool failed=false;
 uint32_t cheats=0;
 int32_t diagnostic[4]{};
 explicit KbcsBattle(const KbcsBattleConfig &value):config(value),seed(value.seed){
  for(auto &side:profiles)std::fill_n(side,51,-1);
 }
 int32_t &profileIndex(int side,int slot){return slot<51?profiles[side][slot]:pool.extra[slot-51].profiles[side];}
 int32_t profileIndex(int side,int slot) const {return slot<51?profiles[side][slot]:pool.extra[slot-51].profiles[side];}
 bool &bonusSlot(int slot){return slot<51?bonus_slots[slot]:pool.extra[slot-51].bonus;}
 auto &impactAt(int side,int slot){return slot<51?impacts[side][slot]:pool.extra[slot-51].impacts[side];}
 void check(uint32_t code){if(code)throw AttackFailure{code};}
 void sound(int frame,int id){if(id>=0)sounds.push_back({frame,id});}
 void battleSound(int id){if(!result.mode)sound(current_frame,id);}
 int effectLength(int phase,bool plain=false) const {for(const auto &clock:config.effect_clocks)if(clock[0]==phase)return clock[plain?2:1];throw std::out_of_range("effect clock");}
 static KbcsBattleVisual effect(int phase,int x,int y){return {6,0,-1,phase,0,x,y,0,{}};}
 template<size_t N> static KbcsBattleVisual *freeEffect(std::array<KbcsBattleVisual,N> &pool){auto it=std::find_if(pool.begin(),pool.end(),[](const auto &v){return !v.phase;});return it==pool.end()?nullptr:&*it;}
 void effectClock(){
  const auto advance=[&](auto &pool){for(auto &v:pool)if(v.phase){if(v.phase==0x10e8&&!v.frame)battleSound(44);if(++v.frame>=effectLength(v.phase,true)){if(v.phase==0x10e8)v={};else v.phase=0;}}};
  for(auto &side:impacts)for(auto &v:side)if(v[0]>0)--v[0];for(auto &record:pool.extra)for(auto &v:record.impacts)if(v[0]>0)--v[0];
  advance(critical_visuals);advance(killer_visuals);advance(barrier_visuals);advance(shield_visuals);
  // 可変長リストは末尾から更新・削除し、初回SEも原本の順序を保つ。
  for(int phase:{0x35b8,0x3628,0x16480,0x16560})for(size_t i=transient.size();i-->0;){auto &v=transient[i];if(v.phase!=phase)continue;if(!v.frame)battleSound(v.phase==0x35b8?90:v.phase==0x3628?110:v.phase==0x16560?188:-1);if(++v.frame>=effectLength(v.phase))transient.erase(transient.begin()+i);}
 }
 void addMoney(KbcsBattleScreenState &screen,int32_t amount){
  if(!amount)return;KbcsBattleScreenInput input{};KbcsBattleScreenState copy{};KbcsBattleScreenLayout layout{};
  check(kbcs_core_battle_screen_step(&config.screen,&screen,&input,&copy,&layout));
  // 005c2990は加算直後に0..財布上限へ丸める。財布暗号化のOS乱数は戦闘RNGと別。
  screen.money=std::clamp(screen.money+amount,0,layout.wallet_max);
 }
 int occupied(int side) const {int count=0;for(int j=1;j<actorEnd();++j)count+=actorAt(actors,side,j).words[0]!=0;return count;}
 bool summonActive(int slot) const {return !(cheats&KBCS_BATTLE_HIDE_SUMMON)&&summons.active[slot];}
 bool unitLimit() const {if(cheats&KBCS_BATTLE_NO_LIMIT)return false;const int count=occupied(0);return (config.unit_max>0&&count>=config.unit_max)||(!pool.extra.empty()&&count>=50);}
 void refill(KbcsBattleScreenState &screen){
  if(!(cheats&KBCS_BATTLE_MONEY)||result.mode)return;
  KbcsBattleScreenInput input{};KbcsBattleScreenState copy{};KbcsBattleScreenLayout layout{};
  check(kbcs_core_battle_screen_step(&config.screen,&screen,&input,&copy,&layout));screen.money=layout.wallet_max;production.money=screen.money;
 }
 bool productionCondition(int slot) const {
  int32_t enabled=0;const auto code=kbcs_core_production_condition(production.produced[slot],config.rules.production_kind,config.rules.production_periods[config.rules.slot_rarity[slot]],&enabled);
  if(code)throw AttackFailure{code};return enabled!=0;
 }
 KbcsBattleDeployment deployment(const KbcsBattleScreenState &screen) const {
  KbcsBattleDeployment out{};out.total=production.total;std::copy_n(warning,2,out.warning);
  for(int j=1;j<actorEnd();++j){if(actorAt(actors,0,j).words[0]<2||profileIndex(0,j)<0)continue;const int slot=profile(0,j).deployment_slot;
   if(slot>=0&&slot<10)++out.active[config.rules.slot_rarity[slot]];
  }
  const bool full=unitLimit();
  for(const auto &p:definitions)if(!p.spawn.side&&p.deployment_slot>=0&&p.deployment_slot<10){const int i=p.deployment_slot,rarity=config.rules.slot_rarity[i];
   if(config.screen.blocked[i]||full)out.blocked[i]=config.screen.blocked[i]|(full?128:0);
   else if(!summonActive(i)){KbcsBattleLimit in{config.screen.fixed_money>=0,(cheats&KBCS_BATTLE_MONEY)?std::max(screen.money,cost(p)):screen.money,cost(p),(cheats&KBCS_BATTLE_NO_LIMIT)?0:config.rules.rarity_limits[rarity],out.active[rarity],(cheats&KBCS_BATTLE_NO_LIMIT)?-1:config.rules.total_limit,production.total};
    const auto code=kbcs_core_battle_limit(&in,&out.blocked[i]);if(code)throw AttackFailure{code};}
  }
  return out;
 }
 void display(){
  // 006d7208。倍速の論理ループでは消さず、表示更新の先頭だけで初期化する。
  preserve_castle=0;
  if(result.mode){if(end_camera.width)check(kbcs_core_battle_end_camera_step(&end_camera));advanceEnding();}
  if(config.rules.score_type==3)check(kbcs_core_battle_point_display(&config.rules.point,&points));
  if(result.mode)return;
  // 006d6d04の表示更新。全体数/総生産数の上限は警告30Fを(0,1)へ上書きする。
  if((!(cheats&KBCS_BATTLE_NO_LIMIT)&&occupied(0)>=50)||unitLimit()||(!(cheats&KBCS_BATTLE_NO_LIMIT)&&config.rules.total_limit>=0&&production.total>=config.rules.total_limit)){warning[0]=0;warning[1]=1;}
  else if((warning[1]&~1)!=2)warning[1]=0;
  else if(warning[0]<=0||!--warning[0])warning[1]=0;
 }
 void musicDisplay(){
  if(result.mode||music.started)return;
  if(!music.delay&&reward_rules.start_sound>=0)sound(current_frame,reward_rules.start_sound);
  if(!reward_rules.music_delay||++music.delay==reward_rules.music_delay){music.started=1;music.id=reward_rules.music[0];++music.serial;}
 }
 void complete(){
  if(!result.mode||rewards.ready)return;
  KbcsBattleRewards out{};out.winner=-1;out.seed_before=seed;
  const auto draw=[&](int bound){int32_t value=0;check(kbcs_core_random_bounded(&seed,bound,&value));return value;};
  const auto &r=reward_rules;
  if(result.mode==1&&r.enabled){
   if(r.mode>= -2){
    KbcsLegendRewardInput input{};input.mode=r.mode;input.acquired=r.acquired;input.radar=r.radar;std::copy_n(r.chances,3,input.chances);
    for(int i=0;i<r.count;++i){input.count=i+1;input.rolls[i]=draw(100);KbcsLegendRewardOutput value{};check(kbcs_core_stage_reward_pick(&input,&value));out.winner=value.winner;out.mark=value.mark_acquired;out.radar_blocked=value.radar_blocked;if(value.winner>=0||value.radar_blocked)break;}
   }else{
    int32_t total=0;check(kbcs_core_reward_weight_total(r.chances,r.count,&total));const int roll=draw(total);int32_t winner=-1;check(kbcs_core_reward_weight_pick(r.chances,r.count,roll,&winner));
    KbcsWeightedFinishInput input{r.mode,r.acquired,r.radar,winner};KbcsWeightedFinishOutput value{};check(kbcs_core_reward_weight_finish(&input,&value));out.winner=value.grant_column>=0?winner:-1;out.mark=value.mark_history;out.radar_blocked=value.radar_blocked;
   }
  }
  if(result.mode==1&&r.material_enabled){
   KbcsMaterialOutput plan{};check(kbcs_core_material_plan(&r.material,&plan));
   int total=0;for(int weight:r.material.weights)total+=weight;
   for(int i=0;i<plan.draws;++i){const int miss=draw(100),weight=miss>=r.material.miss?draw(total):-1;int32_t slot=-1;check(kbcs_core_material_pick(&r.material,miss,weight,&slot));if(slot>=0)++out.materials[slot];}
  }
  out.seed_after=seed;out.ready=1;rewards=out;
 }
 void endSound(bool win,bool timed=false){
  if(end_sound)return;end_sound=true;music.id=-1;++music.serial;
  end_camera={camera,std::clamp(int(camera_zoom*10000),100,10000),timed&&config.rules.score_type==1?0:win?2:1,config.environment.stage_width,config.state.rows};
  if(!win&&config.rules.score_type==1){sound(current_frame,config.hit.effects.notifications?189:57);return;}
  const auto &r=reward_rules;const int count=win?r.win_count:r.lose_count,type=win?r.win_type:r.lose_type;const auto *ids=win?r.win_sounds:r.lose_sounds;
  if(!count){sound(current_frame,win?8:9);return;}
  if(type==1){for(int i=0;i<count;++i)sound(current_frame,ids[i]);}
  else if(!type){int32_t index=0;check(kbcs_core_random_bounded(&seed,count,&index));sound(current_frame,ids[index]);}
 }
 void advanceEnding(){
  if(ending.phase==8){
   auto &p=ending.popup;const bool release=popup_release&&p.phase==1;popup_release=false;
   check(kbcs_core_battle_popup_step(release,&p));++ending.frame;if(release)sound(current_frame,11);
   if(p.phase==3){++p.index;p.phase=p.scale_frame=p.flash=p.wait=0;ending.phase=3;ending.frame=30;}
   return;
  }
  if(ending.phase==3&&ending.frame+1>=30&&ending.popup.index<ending.popup.count){ending.phase=8;ending.frame=0;sound(current_frame,29);return;}
  // 005bc00cが終了カメラの完了を返すまで、phase0を進めない。
  if(!ending.phase&&ending.frame>=19&&end_camera.moving){++ending.frame;return;}
  const int previous=ending.phase;check(kbcs_core_battle_ending_step(result.mode,config.rules.score_type==3,&ending));if(ending_clicked){ending.guard=1;ending_clicked=false;}if(previous==6&&ending.phase==7&&result.mode==1)check(kbcs_core_stage_ex(&reward_rules.ex,reward_rules.ex_choices,reward_rules.ex_count,&seed,&ex));
 }
 void endingInput(const KbcsBattleScreenInput &input){
  if(ending.phase==8){if(input.phase==2&&ending.popup.phase==1)popup_release=true;return;}
  if(ending.guard||ending.action)return;KbcsBattleEnding view{};check(kbcs_core_battle_ending(this,&view));
  const auto *b=view.button;const bool inside=input.x>=b[0]&&input.x<=b[0]+b[2]&&input.y>=b[1]&&input.y<=b[1]+b[3];
  if(input.phase==1){ending.pressed=view.ready&&inside;if(ending.pressed)sound(current_frame,10);}
  else if(input.phase==2){if(ending.pressed&&inside&&view.ready){ending_clicked=true;sound(current_frame,11);}ending.pressed=0;}
  else if(input.phase==3)ending.pressed=0;
 }
 int cost(const KbcsBattleProfile &p) const {
  if(p.deployment_slot<0||p.deployment_slot>9)return p.cost;
  const int i=p.deployment_slot;int base=p.cost;if(p.price.enabled){auto price=p.price;price.orb_enabled=p.spawn.form>=2&&productionCondition(i);const auto code=kbcs_core_production_cost(&price,&base);if(code)throw AttackFailure{code};}
  KbcsProductionPrice input{base,production.last_cost[i],config.price_rule[0],{config.price_rule[1],config.price_rule[2],config.price_rule[3]}};
  int32_t value=0;const auto code=kbcs_core_production_price(&input,&value);if(code)throw AttackFailure{code};return value;
 }
 int recharge(const KbcsBattleProfile &p) const {
  const auto &r=config.rules.point;
  if(points.wait>0&&!config.rules.recharge_fixed&&r.fever_count>4&&r.fever[3]==6&&p.deployment_slot>=0){
   const int rarity=config.rules.slot_rarity[p.deployment_slot];if(r.fever_count<=4+rarity)throw std::out_of_range("fever recharge");
   const int64_t value=int64_t(p.recharge_plain)*r.fever[4+rarity];if(value<0||value>INT32_MAX)throw AttackFailure{2};return int(value/100);
  }
  return p.recharge;
 }
 const KbcsBattleProfile &profile(int side,int slot) const {
  const int index=profileIndex(side,slot);if(index<0||size_t(index)>=definitions.size())throw std::out_of_range("battle profile");return definitions[index];
 }
 int find(const KbcsSpawnRequest &request) const {
  for(size_t i=0;i<definitions.size();++i){const auto &p=definitions[i];if(p.spawn.side==request.side&&p.spawn.raw==request.raw&&p.spawn.form==request.form)return int(i);}
  throw std::out_of_range("spawn profile");
 }
 static int32_t construct(void *user,const KbcsSpawnRequest *request,uint32_t *random){
  auto &battle=*static_cast<KbcsBattle*>(user);const int index=battle.find(*request);const auto &p=battle.definitions[index];
  auto environment=battle.config.environment;
  if(request->side){
   if(request->row<0||size_t(request->row)>=battle.rows.size())throw std::out_of_range("spawn row");
   std::copy_n(battle.rows[request->row].cells,14,environment.spawn_row);
   environment.hp_percent=environment.spawn_row[9];environment.attack_percent=environment.spawn_row[11];
  }
  if(request->side||!(battle.cheats&KBCS_BATTLE_NO_LIMIT)){
   bool free=false;for(int i=1;i<51;++i)if(!battle.actors[request->side][i].words[0]){free=true;break;}if(!free)return -1;
  }else if(battle.occupied(0)>=actorEnd()-1){
   if(battle.pool.extra.size()>=size_t(actorStride/0x3ec-51))throw std::length_error("actor capacity");
   battle.pool.extra.emplace_back();
  }
  std::copy_n(battle.config.environment.spawned,2,environment.spawned);
  auto definition=p.definition;
  if(!request->side&&p.deployment_slot>=0&&p.deployment_slot<10)definition.orb_enabled=definition.orb_enabled&&battle.productionCondition(p.deployment_slot);
  int32_t slot= -1;battle.check(kbcs_core_actor_initialize(&definition,&environment,battle.actors,request,random,&slot));
  std::copy_n(environment.spawned,2,battle.config.environment.spawned);
  if(slot>0){
   battle.profileIndex(request->side,slot)=index;
   if(slot<51)battle.config.clock.forms[request->side][slot]=request->form;else battle.pool.extra[slot-51].forms[request->side]=request->form;
   if(!request->side){if(slot<51)battle.config.clock.kill_orb[slot]=p.definition.orb_present[18];else battle.pool.extra[slot-51].kill_orb=p.definition.orb_present[18];}
  }
  return slot;
 }
 KbcsActorHitContext hitContext(const KbcsActorSecondaryHit &call){
  auto context=config.hit;const auto &hit=call.hit;const int unit_slot=hit.side?hit.target:hit.slot;
  if(unit_slot){
   const auto &p=profile(0,unit_slot);context.form=p.spawn.form;
   auto environment=config.environment;Context source{p.definition,environment,actors,p.spawn,seed};const int id=p.spawn.raw-2,form=p.spawn.form;
   context.effects.target_count=std::max(1,int(n_00aa30a8(source,0,id,form,0))+int(n_00aa3168(source,0,id,form,0))+int(n_00aa3228(source,0,id,form,0))+int(n_00aa32e8(source,0,id,form,0))+int(n_00aa35e8(source,0,id,form,0))+int(n_00aa33a8(source,0,id,form,0))+int(n_00a9f838(source,0,id,form,0))+int(n_00aa3468(source,0,id,form,0))+int(n_00aa4b70(source,0,id,form,0))+int(n_00aa4c30(source,0,id,form,0))+int(n_00aa3528(source,0,id,form,0))+int(n_00aa3bec(source,0,id,form,0)));
   std::copy_n(p.raw_attack,3,context.raw_attack);
   std::copy_n(&p.definition.orbs[0][0],KBCS_ACTOR_ORBS*4,&context.orbs[0][0]);
   std::copy_n(p.definition.orb_present,KBCS_ACTOR_ORBS,context.orb_present);
   for(auto &orb:context.targeted_orbs)std::fill_n(orb,2,0);
   const int enemy=hit.side?hit.slot:hit.target;
   const KbcsActorDefinition empty{};const KbcsSpawnRequest request{};
   Context adapter{empty,environment,actors,request,seed};
   const bool traits[]={n_00a96a38(adapter,1,enemy),n_00a96b18(adapter,1,enemy),n_00a96bf8(adapter,1,enemy),n_00a96cd8(adapter,1,enemy),n_00a96e38(adapter,1,enemy),n_00a96f18(adapter,1,enemy),n_00a96ff8(adapter,1,enemy),n_00a97148(adapter,1,enemy),n_00a96d58(adapter,1,enemy),n_00a97068(adapter,1,enemy),n_00a970d8(adapter,1,enemy),n_00a971b8(adapter,1,enemy)};
   uint32_t mask=0;for(int i=0;i<12;++i)if(traits[i])mask|=1U<<i;
   for(int i=0;i<p.orb_count;++i){const auto &orb=p.orbs[i];if(orb.effect<0||orb.effect>=5||!(uint32_t(orb.mask)&mask))continue;for(int j=0;j<2;++j)context.targeted_orbs[orb.effect][j]+=orb.values[j];}
  }else{
   context.form=0;context.effects.target_count=1;std::fill_n(context.raw_attack,3,0);for(auto &orb:context.targeted_orbs)std::fill_n(orb,2,0);
  }
  return context;
 }
 static uint32_t secondary(void *user,KbcsActor (*)[51],uint32_t*,const KbcsActorSecondaryHit *call,int32_t *applied){
  auto &battle=*static_cast<KbcsBattle*>(user);const auto context=battle.hitContext(*call);KbcsActorEffectEvents events{};
  KbcsActorDamageContext damage{battle.config.guard_enabled,{battle.notice[0],battle.notice[1]},battle.rows.data(),battle.states.data(),int32_t(battle.rows.size())};
  const auto code=kbcs_core_actor_hit(&battle.hits,battle.actors,&battle.config.environment,&context,&battle.config.clock,&damage,call,&battle.seed,applied,&events);
  std::copy_n(damage.notice,2,battle.notice);return code;
 }
 static uint32_t direct(void *user,KbcsActor (*actors)[51],uint32_t *random,const KbcsActorDirectHit *call,int32_t *applied){
  const KbcsActorSecondaryHit hit{*call,0};return secondary(user,actors,random,&hit,applied);
 }
 static uint32_t attack(void *user,KbcsActor (*)[51],uint32_t*,const KbcsActorAttackSelection *selection){
  auto &battle=*static_cast<KbcsBattle*>(user);KbcsActorEmission emission{};
  battle.check(kbcs_core_actor_emit_direct(battle.actors,&battle.config.environment,selection,&battle.seed,direct,&battle,&emission));
  int32_t slot;battle.check(kbcs_core_actor_emit_wave(battle.actors,&battle.config.environment,selection,&emission,&battle.waves,&battle.seed,&slot));
  KbcsActorAreaEmission area{};battle.check(kbcs_core_actor_emit_area(battle.actors,&battle.config.environment,selection,&emission,&battle.seed,&area));
  return kbcs_core_actor_areas_append(&battle.areas,&area);
 }
 void deathSurge(int side,int slot,bool unit_route,const KbcsBattleProfile &p,KbcsBattleScreenState &screen){
  auto &words=actorAt(actors,side,slot).words;
  const int duration=std::max(1,std::max(config.death_surge_time,config.death_surge_motion[side]));
  if(words[2]==config.death_surge_time){
   Context context{p.definition,config.environment,actors,p.spawn,seed};n_006e9c88(context,0,side,slot,0);
   KbcsActorAreaEmission value{};value.surge_present=1;auto &surge=value.surge;
   surge.side=side;surge.slot=slot;surge.kind=2;surge.parameter=n_00a9adf0(context,side,slot);
   const int offset=n_00a98b00(context,side,slot),span=n_00a98b8c(context,side,slot);
   const int draw=n_0044a8d8(context,span<0?-span:span),delta=offset+(span>0?draw:-draw);
   surge.x=words[3]+(unit_route?-delta:delta);surge.level=n_00a98c18(context,side,slot);surge.mini=n_00a98d30(context,side,slot)!=0;
   for(int i=0;i<12;++i)surge.flags[i]=context.procs[storedProcOrder[i]]!=0;
   check(kbcs_core_actor_areas_append(&areas,&value));
  }
  if(words[2]<duration){check(kbcs_core_actor_motion(actors,side,slot,&p.motion));return;}
  int32_t blocked=0;check(kbcs_core_actor_areas_retirement_blocked(&areas,&waves,side,slot,unit_route,&blocked));
  if(blocked)return;
  // 行動21と4は同じ解放末尾へ入るが、21に通常死亡の通知を発生させない。
  KbcsActorRetirement retirement{0,0,0,std::max(0,p.deployment_slot),actorAt(actors,0,0).words[11],screen.cannon};KbcsActorRetirementResult result{};
  const int action=words[1];words[1]=4;words[2]=std::max(words[2],1);
  check(kbcs_core_actor_retire(actors,&config.environment,side,slot,&retirement,&result));
  if(words[0])words[1]=action;
  if(result.reset_production&&result.production_slot>=0&&result.production_slot<10)summons.active[result.production_slot]=0;
  screen.cannon=result.cannon_remaining;
 }
 void action(int side,int slot,KbcsBattleScreenState &screen){
  auto &words=actorAt(actors,side,slot).words;check(kbcs_core_actor_begin(actors,&config.environment,side,slot));
  if(!words[0])return;
  if(!slot){if(!side||(config.environment.unit_modes[side]&1))check(kbcs_core_actor_cannon_action(&cannon,actors,&config.cannon,side));return;}
  const auto &p=profile(side,slot);const bool unit_route=!side||(config.environment.unit_modes[side]&1);
  if(side&&!unit_route){int32_t count=0;check(kbcs_core_actor_sniper_hit(&sniper,actors,&config.environment,slot,&seed,&count));}
  // 陣営0は006eb464、陣営1だけがunit-mode時に同経路へ委譲する。
  const int state=words[1];int32_t handled=0,sound= -1;
  if(state==0||(!unit_route&&state>=11&&state<=16)){
   Context context{p.definition,config.environment,actors,p.spawn,seed};context.motion=&p.motion;
   if(unit_route)n_006eb8c0(context,0,0,side,slot);else n_006ecfec(context,0,0,side,slot);return;
  }
  if(state==3||state==5||state==6||(unit_route&&state==7)){
   if(unit_route){
    KbcsActorKnockback input{p.boundary,cost(p),config.rules.score_type==1,result.mode};KbcsActorKnockbackResult output{};
    check(kbcs_core_actor_unit_knockback(actors,&config.environment,side,slot,&input,&output));addMoney(screen,output.refund);
   }else if(state==3){
    const auto credit=hits.credits.find(words[240]);KbcsActorEnemyDeath input{};input.boundary=p.boundary;input.money_base=p.money_base;input.accounting_level=config.accounting_level;
    input.game_mode=result.mode;input.quiet=input.score_enabled=config.rules.score_type==1;input.notifications=config.hit.effects.notifications;input.money_disabled=config.screen.fixed_money>=0;input.timer=result.timer;input.limit=config.rules.time_limit;input.score=result.score;input.recording=config.rules.score_type==3;
    input.cohort_present=credit!=hits.credits.end();if(input.cohort_present){input.cohort=credit->second.data();input.cohort_count=int32_t(credit->second.size());}
    KbcsActorEnemyDeathResult output{};check(kbcs_core_actor_enemy_knockback(actors,&config.environment,side,slot,&input,&output));addMoney(screen,output.money);
    if(output.score_updated){result.score=output.score;score_display.phase=int32_t(output.score_display);score_display.frame=int32_t(output.score_display>>32);}
    if(output.record_requested){const KbcsPointInput point{1,2,{output.record_values[0],output.record_values[1]},result.timer,config.rules.time_limit};check(kbcs_core_battle_point_add(&config.rules.point,&points,&point));}
    if(output.erase_cohort)hits.credits.erase(output.cohort_serial);
    if(output.selected_bonus_slot>=0&&output.selected_bonus_slot<actorEnd())bonusSlot(output.selected_bonus_slot)=true;
   }else check(kbcs_core_actor_enemy_displacement(actors,&config.environment,side,slot,p.boundary,&handled));
   return;
  }
  if(state==4){
   int32_t blocked=0;check(kbcs_core_actor_areas_retirement_blocked(&areas,&waves,side,slot,unit_route,&blocked));
   KbcsActorRetirement input{blocked,p.death_body_frames,p.death_soul_frames,std::max(0,p.deployment_slot),actorAt(actors,0,0).words[11],screen.cannon};KbcsActorRetirementResult result{};
   check(kbcs_core_actor_retire(actors,&config.environment,side,slot,&input,&result));screen.cannon=result.cannon_remaining;
   if(result.reset_production&&result.production_slot>=0&&result.production_slot<10)summons.active[result.production_slot]=0;
   return;
  }
  if(state==21){deathSurge(side,slot,unit_route,p,screen);return;}
  if(!unit_route&&state==17)return;
  check(kbcs_core_actor_transition(actors,&config.environment,side,slot,&p.motion,p.boundary,&sound));
 }
 void logical(KbcsBattleScreenState &screen){
  current_frame=screen.frame;diagnostic[0]=screen.frame;diagnostic[1]=1;sniper_phase+=6.f;
  if(!result.mode&&config.rules.score_type==3){int32_t changed=0;check(kbcs_core_battle_point_fever(&config.rules.point,&points,&changed));if(changed>0)sound(screen.frame,194);}
  // 追加生産は制限時間より先。通常の可否/費用/回数/再生産/SEを通さない。
  KbcsSpawnRequest requests[10]{};for(const auto &p:definitions)if(!p.spawn.side&&p.deployment_slot>=0&&p.deployment_slot<10)requests[p.deployment_slot]=p.spawn;
  int32_t extra_count=int32_t(extras.size());check(kbcs_core_production_extra_tick(extras.data(),&extra_count,&production,requests,&seed,construct,this));extras.resize(extra_count);
  if(!result.mode&&((config.rules.score_type==1&&result.timer!=INT32_MAX&&result.timer+1>=config.rules.time_limit)||(config.rules.score_type==3&&config.rules.time_limit>=0&&result.timer+1>=config.rules.time_limit)))endSound(config.rules.score_type==3,true);
  check(kbcs_core_battle_result_step(&config.rules,&result,0,screen.frame,config.environment.castle_slot,actors,&seed));
  complete();
  if(config.rules.score_type==3&&result.mode)points.ending=1; // 005d996c/005e02b0→00645630。
  config.waves.game_mode=result.mode;
  diagnostic[1]=2;stage.active_enemies=occupied(1);stage.kill_delta=kills;kills=0;stage.castle_hp=actorAt(actors,1,0).words[8];stage.castle_max_hp=actorAt(actors,1,0).words[7];
  if(stage.damage_condition)stage.castle_damage=actorAt(actors,1,config.environment.castle_slot).words[112];
  if(!result.mode){KbcsEnemyProductionOutput birth{};check(kbcs_core_production_enemy(rows.data(),states.data(),int32_t(rows.size()),&stage,&seed,seen.data(),int32_t(seen.size()),construct,this,&birth));}
  diagnostic[1]=3;check(kbcs_core_actor_clock(actors,&config.clock));
  for(int side=0;side<2;++side){
   if(side){const KbcsSniperInput input{(screen.items_on>>5)&1,camera,640,sniper_phase};int32_t fired= -1;check(kbcs_core_actor_sniper_step(&sniper,&input,actors,&config.environment,&fired));}
   for(int slot=0;slot<actorEnd();++slot){diagnostic[1]=4;diagnostic[2]=side;diagnostic[3]=slot;action(side,slot,screen);}
  }
  for(int slot=1;slot<actorEnd();++slot)if(bonusSlot(slot)){actorAt(actors,0,slot).words[243]=0;bonusSlot(slot)=false;}
  diagnostic[1]=5;int32_t burrow=0;check(kbcs_core_actor_intent(actors,&config.environment,&burrow));
  for(int side=0;side<2;++side)for(int slot=1;slot<actorEnd();++slot){
   if(!actorAt(actors,side,slot).words[0])continue;const auto &p=profile(side,slot);int32_t handled=0;
   diagnostic[1]=6;diagnostic[2]=side;diagnostic[3]=slot;check(kbcs_core_actor_attack_wait(actors,&config.environment,side,slot,&p.motion,burrow,&handled));
   diagnostic[1]=7;KbcsActorAttackResult result{};check(kbcs_core_actor_attack(actors,&config.environment,side,slot,&p.motion,&seed,attack,this,&result));
  }
  int32_t boss_sounds=0,boss_shakes=0;check(kbcs_core_actor_boss(actors,&config.environment,config.boss_frames,&boss_sounds,&boss_shakes));for(int i=0;i<boss_sounds;++i)sound(screen.frame,45);
  for(int phase=0;phase<2;++phase){diagnostic[1]=8+phase;int32_t sounds=0;check(kbcs_core_actor_waves_step(phase,&waves,&segments,actors,&config.environment,&config.waves,&seed,secondary,this,&sounds));for(int i=0;i<sounds;++i)sound(screen.frame,26);}
  for(int phase=0;phase<3;++phase){diagnostic[1]=10+phase;check(kbcs_core_actor_areas_step(&areas,phase,actors,&config.environment,&config.areas,&seed,secondary,this));for(const auto &event:areas.events)if(!event.kind){if(phase==1)sound(screen.frame,event.value);else battleSound(event.value);}}
  for(int side=0;side<2;++side){
   diagnostic[1]=17;diagnostic[2]=side;diagnostic[3]=0;KbcsActorEffectEvents events{};KbcsActorDamageContext damage{config.guard_enabled,{notice[0],notice[1]},rows.data(),states.data(),int32_t(rows.size())};
   check(kbcs_core_actor_cannon_step(&cannon,actors,&config.environment,&config.hit,&config.clock,&damage,&config.cannon,side,&seed,&events));std::copy_n(damage.notice,2,notice);
  }
  diagnostic[1]=13;bool shield_hits[2][51]{};std::vector<std::array<bool,2>> extra_hits(pool.extra.size());const auto shieldHit=[&](int side,int slot)->bool&{return slot<51?shield_hits[side][slot]:extra_hits[slot-51][side];};
  for(int side=0;side<2;++side)for(int slot=0;slot<actorEnd();++slot){
   auto &actor=actorAt(actors,side,slot);auto &words=actor.words;
   // 006d951c。空き枠も含めて表示時計を進め、同Fの被弾ではprotectが再び0へ戻す。
   check(kbcs_core_actor_protection_clock(&actor,words[133]?effectLength(0x2328):0,words[192]?effectLength(0x2440+words[192]*0x38):0));
   if(!words[0])continue;
   if(side){
    const auto metal=hits.metal.find(slot);if(metal!=hits.metal.end()){
     int basis=words[8];for(int rate:metal->second){const int damage=std::max(1,(rate*basis)/100);KbcsActorDamageContext context{config.guard_enabled,{notice[0],notice[1]},rows.data(),states.data(),int32_t(rows.size())};check(kbcs_core_actor_damage(actors,&config.environment,&context,side,slot,damage));std::copy_n(context.notice,2,notice);basis=std::max(0,basis-damage);}
    }
   }
   KbcsActorProtection protection{};check(kbcs_core_actor_protect(actors,side,slot,&protection));shieldHit(side,slot)=protection.shield_hit;
   if(config.hit.effects.notifications&&result.mode!=4){auto &w=actorAt(actors,side,slot).words;result.score=int32_t(uint32_t(result.score)+uint32_t(w[232]));w[232]=0;}
   for(int i=0;i<protection.visual_count;++i){const auto &v=protection.visuals[i];auto *free=freeEffect(v[0]?shield_visuals:barrier_visuals);if(free)*free=effect(v[0]?(v[3]?0x2558:0x2520):(v[3]?0x2398:0x2360),v[1]/10,v[2]/10);}

  }
  // 保護処理後・特殊城HPの複写前。006d9e44は今回の保留ダメージで条件を判定する。
  auto guard=stage;guard.castle_hp=actorAt(actors,1,0).words[8];guard.castle_max_hp=actorAt(actors,1,0).words[7];
  if(guard.damage_condition)guard.castle_damage=actorAt(actors,1,config.environment.castle_slot).words[112];
  check(kbcs_core_stage_castle_guard(rows.data(),states.data(),int32_t(rows.size()),&guard,actorAt(actors,1,0).words[19],&preserve_castle));
  if(config.environment.special_castle>0){const int slot=config.environment.castle_slot;if(slot<1||slot>=actorEnd())throw std::out_of_range("castle slot");for(int word:{7,8,19})actorAt(actors,1,0).words[word]=actorAt(actors,1,slot).words[word];}
  int impact_sound=0;
  for(int side=0;side<2;++side)for(int slot=0;slot<actorEnd();++slot){
   auto &words=actorAt(actors,side,slot).words;if(!words[0]||(!words[19]&&!shieldHit(side,slot)))continue;
   if(side&&!slot&&config.environment.special_castle>0)continue;
   impact_sound=std::max(impact_sound,!slot||(side&&slot==config.environment.castle_slot)?2:1);
   const KbcsActorDefinition definition{};const KbcsSpawnRequest request{};Context context{definition,config.environment,actors,request,seed};
   const bool critical=n_00a9be18(context,side,slot)!=0;
   auto *critical_entry=critical?freeEffect(critical_visuals):nullptr;
   if(critical_entry)*critical_entry=effect(0x10e8,0,0);
   const auto hitPoint=[&](){const int dx=n_0044a8d8(context,46),dy=n_0044a8d8(context,slot?31:25);return std::array<int,2>{slot?words[3]-dx*10-437:words[3]+dx*10-937,slot?words[4]+dy*10-1325:words[4]-dy*10-1175};};
   // 006da2b0: 渾身→毒撃→メタルキラーの演出抽選を通常被弾より先に行う。
   // 00a9cbb8/00a9ce0c/00a9d2e4のフラグはword166/173/219。
   for(const auto &[active,phase]:{std::pair{bool(words[166]),0x35b8},std::pair{bool(words[173]),0x3628},std::pair{bool(words[219]),0x16480}})if(active){const auto point=hitPoint();transient.push_back(effect(phase,point[0]/10+68,point[1]/10+77));}
   if(critical){const auto point=hitPoint();auto &v=critical_entry?*critical_entry:critical_visuals[0];v.x=point[0]/10+68;v.y=point[1]/10+77;}
   const auto impact=hitPoint();auto &visual=impactAt(side,slot);visual[0]=12;visual[1]=impact[0];visual[2]=impact[1];visual[3]=slot?words[96]:int(words[96]==1);
   int deployment= -1,cooldown=0;if(!side&&slot){const auto &p=profile(side,slot);deployment=p.deployment_slot;cooldown=recharge(p);}
   diagnostic[1]=14;diagnostic[2]=side;diagnostic[3]=slot;KbcsActorHealth health{deployment,cooldown,preserve_castle};KbcsActorHealthResult result{};check(kbcs_core_actor_health(actors,side,slot,&health,&seed,&result));
   if(result.delay_slot>=0&&result.delay_slot<10){production.wait[result.delay_slot]+=result.delay_frames;transient.push_back(effect(0x16560,result.delay_x/10+68,result.delay_y/10+77));}
   const int previous=result.previous_hp;if(words[8]<1){words[8]=0;if(!side)++kills;}
   diagnostic[1]=15;auto *free=freeEffect(killer_visuals);
   KbcsActorReaction reaction{previous,free!=nullptr};KbcsActorReactionResult output{};check(kbcs_core_actor_react(actors,&config.environment,side,slot,&reaction,&seed,&output));
   if(output.death_visual&&free)*free=effect(0x2248,output.death_x/10,output.death_y/10-40);
   // 006db1c0..006db340: 敵城HPが閾値を跨いだFで停止し、45論理F後に後半曲へ。
   if(side&&slot==std::max(0,config.environment.castle_slot))check(kbcs_core_battle_music_cross(&reward_rules,previous,words[8],words[7],&music));
  }
  if(!result.mode&&(!actorAt(actors,1,0).words[8]||!actorAt(actors,0,0).words[8]))endSound(!actorAt(actors,1,0).words[8]);
  check(kbcs_core_battle_result_step(&config.rules,&result,1,screen.frame,config.environment.castle_slot,actors,&seed));screen.battle_mode=result.mode;
  complete();
  if(result.reason==2)extras.clear();
  if(config.rules.score_type==3){result.score=points.score;if(result.mode)points.ending=1;}
  if(!result.mode)check(kbcs_core_battle_music_tick(&reward_rules,&music));
  // 006db4f8..006db618。勝敗判定の後、被弾全体に対して一度だけ抽選する。
  if(!result.mode&&impact_sound){int32_t choice=0;if(impact_sound==1)check(kbcs_core_random_bounded(&seed,2,&choice));sound(screen.frame,impact_sound==2?22:20+choice);}
  if(!result.mode){uint32_t ready=0;int32_t recharges[10]{};for(const auto &p:definitions)if(p.deployment_slot>=0&&p.deployment_slot<10)recharges[p.deployment_slot]=recharge(p);
   check(kbcs_core_production_clock(&production,recharges,&ready));for(int i=0;i<10;++i)if(ready&(1U<<i))sound(screen.frame,27);
  }
  const int previous_cannon=screen.cannon;kbcs_core_battle_screen_economy(&config.screen,&screen);
  if(previous_cannon>0&&!screen.cannon)sound(screen.frame,28);
  hits.metal.clear();production.money=screen.money;actorAt(actors,0,0).words[12]=screen.cannon;
  effectClock();
  for(auto &impact:sniper.impacts)for(int i:{0,3})if(impact[i]>0)--impact[i];
  for(int i=0;i<10;++i)if(summons.active[i]&&summons.wait[i]>0)--summons.wait[i];
 }
 void deploy(KbcsBattleScreenState &screen,bool notify=true){
  if(result.mode)return;
  diagnostic[0]=screen.frame;diagnostic[1]=16;diagnostic[2]=0;diagnostic[3]=screen.request_slot;const int slot=screen.request_slot;const auto found=std::find_if(definitions.begin(),definitions.end(),[&](const auto &p){return p.spawn.side==0&&p.deployment_slot==slot;});
  if(found==definitions.end())throw std::out_of_range("deployment slot");
  const auto limits=deployment(screen);const bool root_allowed=!config.screen.blocked[slot]&&!unitLimit();
  if(!root_allowed){warning[0]=30;warning[1]=2;sound(screen.frame,15);return;}
  if(summonActive(slot)){
   const int raw=found->definition.cells[110]+2;
   const auto child=std::find_if(definitions.begin(),definitions.end(),[&](const auto &p){return p.spawn.side==0&&p.spawn.raw==raw&&p.spawn.form==0;});
   if(child==definitions.end())throw std::out_of_range("summon profile");
   KbcsSummonInput input{child->spawn,slot,found->spawn.raw,config.summon_position};KbcsSummonOutput result{};
   check(kbcs_core_actor_summon(&input,&summons,actors,&config.environment,&seed,construct,this,&result));sound(screen.frame,result.sound);sound(screen.frame,result.failure_sound);sound(screen.frame,result.completion_sound);return;
  }
  production.money=(cheats&KBCS_BATTLE_MONEY)?std::max(screen.money,cost(*found)):screen.money;
  if(cheats&KBCS_BATTLE_INSTANT)production.wait[slot]=0;
  KbcsProductionInput input{};input.spawn=found->spawn;input.slot=slot;input.present=1;input.allowed=1;input.blocked=limits.blocked[slot]!=0;input.cost=cost(*found);input.recharge=recharge(*found);input.reduction= -1;input.recharge_enabled=1;input.notify_failure=notify;input.summon_mode=found->summon_mode;
  KbcsProductionOutput result{};check(kbcs_core_production_deploy(&input,&production,&seed,construct,this,&result));screen.money=production.money;sound(screen.frame,result.sound);
  if(result.slot>0){
   if(productionCondition(slot)&&!config.rules.recharge_fixed){int rate=actorAt(actors,0,result.slot).words[250];if(rate<1)rate=found->spawn.form>=2?found->definition.orbs[19][0]:0;
    int32_t wait=0;check(kbcs_core_production_wait(recharge(*found),rate,&wait));production.wait[slot]=production.maximum[slot]=wait;
   }
   const auto &rule=config.rules.extra_rule;const int count=(uint32_t(rule[0])&(1U<<config.rules.slot_rarity[slot]))?std::max(0,rule[1]):0;
   const auto begin=extras.size();extras.resize(begin+count);int32_t scheduled=0;check(kbcs_core_production_extra_plan(rule,config.rules.slot_rarity[slot],slot,count?extras.data()+begin:nullptr,count,&scheduled));
   if(config.rules.score_type==3){const int value=(config.rules.cost_chapter+2)*(found->definition.cells[6]/100)/2;const KbcsPointInput point{0,1,{value,0},this->result.timer,config.rules.time_limit};check(kbcs_core_battle_point_add(&config.rules.point,&points,&point));this->result.score=points.score;}
  }
  if(result.slot>0&&found->definition.cells[110]>=0){summons.active[slot]=1;summons.wait[slot]=15;summons.used[slot]=0;}
  if(cheats&KBCS_BATTLE_INSTANT)production.wait[slot]=production.maximum[slot]=0;
  refill(screen);
 }
 void fire(KbcsBattleScreenState &screen,bool notify=true){
  if(result.mode)return;
  const auto wall=std::find_if(definitions.begin(),definitions.end(),[&](const auto &p){return !p.spawn.side&&p.spawn.raw==actorAt(actors,0,0).words[26]+2&&p.spawn.form==0;});
  KbcsCannonFire result{};check(kbcs_core_actor_cannon_fire(actors,&config.environment,wall==definitions.end()?nullptr:&wall->spawn,&seed,construct,this,&result));screen.cannon=actorAt(actors,0,0).words[12];if(result.fired||notify)sound(screen.frame,result.sound);if(result.fired){computer.action=0;sound(screen.frame,19);}
 }
 void automatic(KbcsBattleScreenState &screen){
  if(result.mode)return;
  KbcsComputerInput input{};input.enabled=(screen.items_on>>3)&1;
  input.mode=warning[0];
  if(!input.enabled)return;
  KbcsBattleScreenState copy{};KbcsBattleScreenLayout layout{};KbcsBattleScreenInput idle{};
  check(kbcs_core_battle_screen_step(&config.screen,&screen,&idle,&copy,&layout));
  input.worker=screen.worker;input.money=screen.money;input.wallet=layout.wallet_max;input.upgrade_cost=layout.upgrade_cost;input.worker_level=config.screen.worker_level;
  input.page=screen.page;input.page_frame=screen.page_frame;input.page_direction=screen.page_direction;input.page_step=screen.page_step;
  const auto limits=deployment(screen);const int units=occupied(0);input.full=!(cheats&KBCS_BATTLE_NO_LIMIT)&&units>=50;input.cannon_wait=screen.cannon;input.cannon_action=actorAt(actors,0,0).words[9];input.cannon_range=actorAt(actors,0,0).words[6];input.castle_x=actorAt(actors,0,0).words[3];input.camera=camera;
  std::fill_n(input.raw,10,-1);
  for(const auto &p:definitions)if(!p.spawn.side&&p.deployment_slot>=0&&p.deployment_slot<10){
   const int i=p.deployment_slot;input.raw[i]=p.spawn.raw;input.cost[i]=cost(p);input.eligible[i]=!limits.blocked[i];input.wait[i]=production.wait[i];input.summoned[i]=summonActive(i);
  }
  KbcsComputerOutput result{};check(kbcs_core_battle_computer(&input,&computer,actors[1],&seed,&result));
  if(result.page_start){screen.page_frame=1;screen.page_direction=1;screen.holding=-1;screen.hold_frames=0;screen.gesture=1;}
  screen.page_step=result.page_step;
  if(result.upgrade){screen.money-=layout.upgrade_cost;++screen.worker;screen.wallet_flash=14;sound(screen.frame,19);}
  if(result.fire)fire(screen,false);
  if(result.deploy>=0){screen.request_slot=result.deploy;deploy(screen,false);}
 }
 static uint32_t hook(void *user,int32_t event,KbcsBattleScreenState *screen){
  auto &battle=*static_cast<KbcsBattle*>(user);battle.current_frame=screen->frame;
  try{
   if(event==0)battle.logical(*screen);else if(event==1)battle.deploy(*screen);
   else if(event==2)battle.fire(*screen);
   else if(event==3)battle.automatic(*screen);
   else if(event==4){battle.display();if(battle.ending.action)screen->request_action=battle.ending.action;}
   else if(event==5){if(!screen->paused)battle.musicDisplay();if(battle.config.rules.score_type==3)battle.check(kbcs_core_battle_point_render(&battle.config.rules.point,&battle.points));if(battle.config.rules.score_type==1)battle.check(kbcs_core_battle_score_display(battle.result.score,&battle.score_display));}
   else if(event>=KBCS_BATTLE_SCREEN_SOUND)battle.sound(screen->frame,event-KBCS_BATTLE_SCREEN_SOUND);

   if(event==0||event==1||event==3||event==5)battle.refill(*screen);
   if((battle.cheats&KBCS_BATTLE_INSTANT)&&event==0){std::fill_n(battle.production.wait,10,0);std::fill_n(battle.production.maximum,10,0);}
   return 0;
  }
  catch(const AttackFailure &error){return error.code;}catch(...){return 3;}
 }
};

extern "C" uint32_t kbcs_core_battle_create(const KbcsBattleConfig *config,const KbcsBattleProfile *profiles,int32_t count,const KbcsStageRow *rows,int32_t row_count,KbcsBattle **out){
 if(!config||!out||!config->seed||count<0||count>4096||row_count<0||row_count>4096||(!profiles&&count)||(!rows&&row_count)||config->environment.stage_width<2800||config->unit_max<0||config->enemy_max<1||config->enemy_max>50)return 1;
 if(config->state.battle_mode||config->rules.score_type<0||config->rules.score_type>3||config->rules.time_limit< -1||config->rules.total_limit< -1)return 1;
 if(config->rules.unit_combo_count<0||config->rules.unit_combo_count>32)return 1;
 if(config->rules.score_type==3&&(config->rules.point.tier_count<1||config->rules.point.tier_count>32))return 1;
 for(int rarity:config->rules.slot_rarity)if(rarity<0||rarity>5)return 1;
 KbcsBattle *battle=nullptr;
 try{
  KbcsBattleScreenInput input{};KbcsBattleScreenState screen{};KbcsBattleScreenLayout layout{};
  const auto valid=kbcs_core_battle_screen_step(&config->screen,&config->state,&input,&screen,&layout);if(valid)return valid;
  battle=new KbcsBattle(*config);ActorPoolScope pool_scope(battle->pool);battle->config.state.cannon=layout.cannon_initial;if(count)battle->definitions.assign(profiles,profiles+count);if(row_count)battle->rows.assign(rows,rows+row_count);battle->states.resize(row_count);
  int seen_count=0;for(const auto &p:battle->definitions){if(p.orb_count<0||p.orb_count>8)throw AttackFailure{1};if(p.spawn.side)seen_count=std::max(seen_count,p.spawn.raw-1);}battle->seen.resize(seen_count);
  actorAt(battle->actors,0,0)=config->castle;
  for(int side=0;side<2;++side){auto &w=actorAt(battle->actors,side,0).words;w[0]=1;w[3]=side?3200:config->environment.stage_width-3200;w[4]=4400;w[7]=w[8]=config->castle_hp[side];}
  for(const auto &p:battle->definitions)if(p.spawn.side==1&&p.spawn.raw==config->environment.special_castle)battle->stage.damage_condition=p.definition.cells[49]!=0;
  actorAt(battle->actors,0,0).words[11]=layout.cannon_max;actorAt(battle->actors,0,0).words[12]=layout.cannon_initial;
  battle->stage.max_enemies=config->enemy_max;battle->stage.global_min=config->global_min;battle->stage.global_max=config->global_max;
  KbcsStageStartOutput start{};KbcsEnemyProductionOutput birth{};const int castle_raw=config->environment.special_castle>0?config->environment.special_castle:0;
  battle->check(kbcs_core_production_start(battle->rows.data(),battle->states.data(),row_count,config->global_min,config->global_max,castle_raw,&battle->seed,KbcsBattle::construct,battle,&start,&birth));
  battle->stage.global_wait=start.global_wait;*out=battle;return 0;
 }catch(const AttackFailure &error){delete battle;return error.code;}catch(...){delete battle;return 3;}
}
extern "C" void kbcs_core_battle_destroy(KbcsBattle *battle){delete battle;}
extern "C" uint32_t kbcs_core_battle_cheats(KbcsBattle *battle,uint32_t flags){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||battle->failed||(flags&~15U))return 1;battle->cheats=flags;
 if(flags&KBCS_BATTLE_INSTANT){std::fill_n(battle->production.wait,10,0);std::fill_n(battle->production.maximum,10,0);}
 return 0;
}
extern "C" uint32_t kbcs_core_battle_advance(KbcsBattle *battle,const KbcsBattleScreenInput *input,KbcsBattleScreenState *out,KbcsBattleScreenLayout *view){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||battle->failed||!input||!out||!view)return 1;
 battle->sounds.clear();battle->current_frame=battle->config.state.frame;BattleSoundScope sound_scope(battle->sounds,battle->current_frame);BattleRulesScope rules_scope(battle->config.rules,battle->result.mode);auto screen=battle->config.screen;
 auto resolved_input=*input;
 try{if(battle->result.mode){battle->endingInput(*input);resolved_input.phase=0;resolved_input.control=input->control==10?10:0;battle->config.state.paused=0;input=&resolved_input;}}catch(const AttackFailure &error){return error.code;}catch(...){return 3;}
 // 精霊の再召喚は通常の資金/再生産待ちを条件にしない。原本の別入口で再検査する。
 for(int i=0;i<10;++i)if(battle->summonActive(i))screen.costs[i]=0;
 try{battle->refill(battle->config.state);}catch(const AttackFailure &error){return error.code;}catch(...){return 3;}
 const auto code=kbcs_core_battle_screen_advance_custom(&screen,&battle->config.state,input,out,view,KbcsBattle::hook,battle,(battle->cheats&KBCS_BATTLE_INSTANT)!=0);
 if(code){battle->failed=true;return code;}battle->config.state=*out;return 0;
}
extern "C" uint32_t kbcs_core_battle_actors(const KbcsBattle *battle,const KbcsActor **actors,const int32_t **profiles){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!actors||!profiles)return 1;*actors=&actorAt(battle->actors,0,0);*profiles=&battle->profiles[0][0];return 0;
}
extern "C" uint32_t kbcs_core_battle_production(const KbcsBattle *battle,KbcsProductionState *out,uint32_t *seed){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!out||!seed)return 1;*out=battle->production;*seed=battle->seed;return 0;
}
extern "C" uint32_t kbcs_core_battle_extras(const KbcsBattle *battle,const KbcsProductionExtra **out,int32_t *count){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);if(!battle||!out||!count)return 1;*out=battle->extras.data();*count=int32_t(battle->extras.size());return 0;}
extern "C" uint32_t kbcs_core_battle_points(const KbcsBattle *battle,KbcsBattlePoints *out){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);if(!battle||!out)return 1;*out=battle->points;return 0;}
extern "C" uint32_t kbcs_core_battle_computer_state(const KbcsBattle *battle,KbcsComputerState *out){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!out)return 1;*out=battle->computer;return 0;
}
extern "C" uint32_t kbcs_core_battle_result(const KbcsBattle *battle,KbcsBattleResult *out){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);if(!battle||!out)return 1;*out=battle->result;return 0;}
extern "C" uint32_t kbcs_core_battle_reward_rules(KbcsBattle *battle,const KbcsBattleRewardRules *input){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!input||battle->config.state.frame||battle->result.mode||input->enabled<0||input->enabled>1||input->material_enabled<0||input->material_enabled>1)return 1;
 const auto &r=*input;
 if(r.ex_count<0||r.ex_count>32)return 1;uint32_t ex_seed=1;KbcsExTransitionOutput ex_out{};const auto ex_code=kbcs_core_stage_ex(&r.ex,r.ex_choices,r.ex_count,&ex_seed,&ex_out);if(ex_code)return ex_code;
 if(r.win_count<0||r.win_count>32||r.lose_count<0||r.lose_count>32||r.win_type<0||r.lose_type<0)return 1;
 if(r.enabled){
  if(r.mode< -4||r.mode>2||r.count<1||r.count>(r.mode< -2?10:3)||r.acquired<0||r.acquired>1||r.radar<0||r.radar>1)return 1;
  if(r.mode>= -2){KbcsLegendRewardInput in{};in.mode=r.mode;in.count=r.count;in.acquired=r.acquired;in.radar=r.radar;std::copy_n(r.chances,3,in.chances);KbcsLegendRewardOutput out{};const auto code=kbcs_core_stage_reward_pick(&in,&out);if(code)return code;}
  else{int32_t total=0;const auto code=kbcs_core_reward_weight_total(r.chances,r.count,&total);if(code)return code;}
 }
 if(r.material_enabled){KbcsMaterialOutput out{};const auto code=kbcs_core_material_plan(&r.material,&out);if(code)return code;}
 battle->reward_rules=r;return 0;
}
extern "C" uint32_t kbcs_core_battle_rewards(const KbcsBattle *battle,KbcsBattleRewards *out){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);if(!battle||!out)return 1;*out=battle->rewards;return 0;}
extern "C" uint32_t kbcs_core_battle_notifications(KbcsBattle *battle,int32_t count){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);if(!battle||count<0||count>128||battle->ending.phase>3||battle->ending.popup.count)return 1;battle->ending.popup.count=count;return 0;}
extern "C" uint32_t kbcs_core_battle_music(const KbcsBattle *battle,KbcsBattleMusic *out){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);if(!battle||!out)return 1;*out=battle->music;return 0;}
extern "C" uint32_t kbcs_core_battle_ex(const KbcsBattle *battle,KbcsExTransitionOutput *out){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);if(!battle||!out)return 1;*out=battle->ex;return 0;}
extern "C" uint32_t kbcs_core_battle_end_camera(const KbcsBattle *battle,KbcsBattleEndCamera *out){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);if(!battle||!out)return 1;*out=battle->end_camera;return 0;}
extern "C" uint32_t kbcs_core_battle_ending(const KbcsBattle *battle,KbcsBattleEnding *out){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!out)return 1;auto e=battle->ending;const auto &r=battle->result;const int width=battle->config.screen.viewport_width;
 static constexpr int slide[]={960,960,512,256,128,64,32,16,8,4,2,1,0};
 static constexpr int fall[]={-132,-94,-57,-20,17,54,92,129,167,204,242,235,227,224,220,219,217,216,215,216,217,218,220,223,227,234,242,241,240,239,237,238,240,241,242,242,242,242,242,242,242,242,242,242};
 e.title[2]=-1;
 if(r.mode&&e.phase){
  const int x=slide[e.phase==1?std::clamp(e.frame,0,12):12];
  if(r.mode==2){e.title[0]=width/2-152;e.title[1]=fall[e.phase==1?std::clamp(e.frame,0,43):43];e.title[2]=3;e.shade=e.phase==2?std::clamp(e.frame,0,80)*255/80:0;if(e.phase>=4)e.shade=255;}
  else {e.title[0]=width/2-x-239;e.title[1]=190;e.title[2]=(r.mode==7||battle->config.rules.score_type==3)?12:0;e.bar_x=e.phase>1?-slide[e.phase==2?std::clamp(e.frame,0,12):12]:-width;}
 }
 e.number_x=e.bar_x;
 if(r.mode==1&&battle->config.rules.score_type==3&&e.phase==2&&e.frame<0){const int progress=e.frame+100;e.bar_x=-slide[std::clamp(progress,0,12)];e.number_x=progress>32?slide[std::clamp(45-progress,0,12)]:e.bar_x;}
 e.ready=(r.mode==2?e.phase==4:e.phase==7);e.button[0]=width/2-190;e.button[1]=632-(r.mode==2?82:e.panel);e.button[2]=381;e.button[3]=88;
 // 006e296c..2a7c: img101部品3とimg006部品1。安全領域/画面のY余白はPCでは0。
 static constexpr int pressed[]={0,0,6,-10,0,0};const int delta=pressed[std::clamp(e.guard,0,5)];
 e.visual_button[0]=width/2-190-delta/2;e.visual_button[1]=e.button[1]+8-delta/2;e.visual_button[2]=381+delta;e.visual_button[3]=72+delta;
 e.label[0]=width/2-127-delta/2;e.label[1]=e.button[1]+17-delta/2;e.label[2]=254+delta;e.label[3]=55+delta;
 *out=e;return 0;
}
extern "C" uint32_t kbcs_core_battle_deployment(const KbcsBattle *battle,KbcsBattleDeployment *out){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!out)return 1;try{*out=battle->deployment(battle->config.state);return 0;}catch(const AttackFailure &error){return error.code;}catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_battle_prices(const KbcsBattle *battle,int32_t out[10]){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!out)return 1;
 try{int32_t values[10]{};for(const auto &p:battle->definitions)if(!p.spawn.side&&p.deployment_slot>=0&&p.deployment_slot<10)values[p.deployment_slot]=battle->cost(p);std::copy_n(values,10,out);return 0;}
 catch(const AttackFailure &error){return error.code;}catch(...){return 3;}
}

extern "C" uint32_t kbcs_core_battle_viewport(KbcsBattle *battle,int32_t width){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||battle->failed||width<960||width>3840)return 1;battle->config.screen.viewport_width=width;return 0;
}

extern "C" uint32_t kbcs_core_battle_error(const KbcsBattle *battle,int32_t out[4]){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!out)return 1;std::copy_n(battle->diagnostic,4,out);return 0;
}

extern "C" uint32_t kbcs_core_battle_hud(const KbcsBattle *battle,const KbcsSceneLayout *scene,const int32_t point[2],KbcsBattleHud *out){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!scene||!point||!out||!std::isfinite(scene->zoom)||scene->zoom<=0)return 1;
 KbcsBattleScreenInput input{};KbcsBattleScreenState state{};KbcsBattleScreenLayout slots{};
 const auto code=kbcs_core_battle_screen_step(&battle->config.screen,&battle->config.state,&input,&state,&slots);if(code)return code;
 KbcsBattleHud value{};value.title[0]=62;value.title[1]=10;value.scale=scene->zoom;
 for(int i=0;i<10;++i){auto &s=value.summons[i];s[0]=battle->summonActive(i);s[2]=battle->summons.wait[i];s[3]=battle->summons.used[i];
  s[4]=int(float(std::cos(double(s[2]*10)*3.141592653589793/180.))*31.f+224.f);if(!s[0]||s[3]||s[2]>0)continue;for(const auto &p:battle->definitions)if(p.deployment_slot==i)for(int j=1;j<actorEnd();++j)if(actorAt(battle->actors,0,j).words[0]==p.spawn.raw&&actorAt(battle->actors,0,j).words[1]!=4)s[1]=1;
 }
 // 005d18a4: 押下時のアイコン拡縮とは別の、元の枠座標へゲージを置く。
 for(const auto &p:battle->definitions)if(p.deployment_slot>=0&&p.deployment_slot<10){
  const int i=p.deployment_slot,wait=battle->production.wait[i],recharge=battle->recharge(p);if(wait<=0)continue;
  auto &g=value.gauges[i];g[0]=slots.labels[i][0]+6;g[1]=slots.labels[i][1]+62;g[2]=1;
  g[3]=recharge?std::min(93,int(int64_t(recharge-wait)*93/recharge)):0;
  g[4]=recharge&&battle->production.produced[i]>0?int(int64_t(recharge-battle->production.maximum[i])*93/recharge):0;
 }
 const auto &env=battle->config.environment;const auto &offset=battle->config.castle_offsets;
 for(int side=0;side<2;++side){
  const int slot=side&&env.special_castle>0?env.castle_slot:0;if(slot<0||slot>=actorEnd())return 1;
  const auto &w=actorAt(battle->actors,side,slot).words;double x=0,y=137;
  if(!side){x=w[3]/10-24+offset[0];y+=offset[1];}
  else if(!slot){const int size=env.castle_scale;x=(w[3]-size*1180/100)/10+size*env.castle_offset/100+size*127/200+86+offset[2];y+=offset[3];}
  else{x=w[3]/10+point[0]+offset[4];y=w[4]/10+w[5]*4+point[1]+offset[5];}
  value.anchors[side][0]=scene->viewport_width*.5+(x-scene->center)*scene->zoom;
  value.anchors[side][1]=scene->y_origin+(y-scene->y_origin+scene->y_offset)*scene->zoom;
  value.health[side][0]=w[8];value.health[side][1]=std::min(w[7],99999999);value.health[side][2]=slot&&w[111]!=0;
 }
 *out=value;return 0;
}

extern "C" uint32_t kbcs_core_battle_visuals(KbcsBattle *battle,const KbcsBattleVisual **out,int32_t *count){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!out||!count)return 1;
 try{
  auto &list=battle->visuals;list.clear();
  // 005d3910/005d3f6c/005d57d0。描画時計を戦闘時計から作り、RNGを消費しない。
  for(int i=0;i<200;++i){const auto &wave=battle->waves.records[i];if(wave.state<1||wave.state>2)continue;
   const int side=wave.state-1,layer=actorAt(battle->actors,side,wave.slot).words[5];
   for(const auto &part:battle->segments.records[i])if(part.frame){
    const int offset=wave.side==2?160*5-540:0;
    list.push_back({wave.mini?1:0,side,wave.slot,0,battle->config.waves.motion_frames[wave.mini!=0]-1-part.frame,(part.x+offset)/10,460+layer*4,layer});
   }
  }
  for(const auto &entry:battle->areas.surges){const auto &value=entry.record;const int start=15,period=value.level*20;int phase=0,frame=value.frame;
   if(frame>=start){frame-=start;phase=frame<period?1:2;if(phase==2)frame-=period;}
   const int layer=actorAt(battle->actors,value.side,value.slot).words[5];list.push_back({value.mini?3:2,value.side,value.slot,phase,frame,value.x/10,460+layer*4,layer});
  }
  for(const auto &value:battle->areas.reflections){const int layer=actorAt(battle->actors,value.side,value.slot).words[5];list.push_back({9,value.side,value.slot,0x29d8+value.side*0x38,value.frame,value.x/10,460+layer*4,layer,{}});}
  for(const auto &entry:battle->areas.explosions){const auto &value=entry.record;if(value.frame<0)continue;
   const int phase=value.frame<battle->config.areas.explosion_frames[0]?0:1,layer=actorAt(battle->actors,value.side,value.slot).words[5];
   list.push_back({4,value.side,value.slot,phase,value.frame-phase*battle->config.areas.explosion_frames[0],value.x/10,460+layer*4,layer});
  }
  for(int side=0;side<2;++side){const auto &w=actorAt(battle->actors,side,0).words;const int action=w[9],frame=w[10],x=w[3]/10+(side?-27:27),y=w[4]/10-160;
   const auto model=[&](int phase,int at,int px,int py,int sx=1000,int sy=1000){list.push_back({5,side,0,phase,at,px,py,0,{sx,sy}});};
   if(action==4||action==7)model(1,frame,w[3]/10+85,130);
   else if(action==5||action==8)model(0,frame,w[18]/10,470);
   else if(action==6)model(0,frame,x-10,y+5);
   else if(action==9&&frame>1)model(0,frame,x+(side?1:-1)*160*w[6]*frame/16+150,480);
   else if(action==12)model(0,frame,x,y);
   else if(action==11){if(frame>4)model(1,frame-5,x+20,y);if(frame>9){model(0,frame-10,w[18]/10,500);model(2,frame-10,w[18]/10,500,frame>10?w[21]*1000/1600:1000);}}
   for(const auto &segment:battle->cannon.segments[side])if(segment[0]){
    if(w[17]==0)model(0,11-segment[0],segment[1]/10+80,500,2500,2500);
    else if(w[17]==5)model(1,battle->config.cannon.encoded[1]-segment[0],segment[1]/10+80,500);
   }
  }
  for(const auto &v:battle->transient)if(v.phase==0x16480)list.push_back(v);
  for(const auto &v:battle->critical_visuals)if(v.phase)list.push_back(v);
  for(const auto *pool:{&battle->killer_visuals,&battle->barrier_visuals,&battle->shield_visuals})for(const auto &v:*pool)if(v.phase)list.push_back(v);
  for(int phase:{0x35b8,0x3628,0x16560})for(const auto &v:battle->transient)if(v.phase==phase)list.push_back(v);
  KbcsActorDefinition definition{};KbcsSpawnRequest request{};Context context{definition,battle->config.environment,battle->actors,request,battle->seed};context.clock=&battle->config.clock;
  for(int side=0;side<2;++side)for(int slot=1;slot<actorEnd();++slot){const auto &w=actorAt(battle->actors,side,slot).words;if(!w[0])continue;
   const int x=w[3]/10,y=w[4]/10+w[5]*4;
   // 006ddfb8の死亡列。21は専用悪魔魂のみで、4/21の状態異常表示は出さない。
   if(w[1]==21)list.push_back({10,side,slot,0x27f8+side*0x38,w[2],x,y-97,w[5],{}});
   if(w[1]==4||w[1]==21)continue;
   const auto draw=[&](int phase,int at,int px,int py){list.push_back({7,side,slot,phase,at,px,py,w[5],{}});};
   if(w[1]!=14&&w[1]!=15&&w[1]!=18&&w[1]!=19&&w[1]!=20)for(int i=0;i<4;++i){const int px=x+i*(side?60:-60);switch(n_00a9cafc(context,side,slot,i)){
    case 1:if(int(n_00a9bfcc(context,side,slot))>0&&w[66]>0)draw(side?0x1d08:0x16e8,w[66]-n_00a9bfcc(context,side,slot),px,y);else if(int(n_00a9c1c4(context,side,slot))>0&&w[67]>0)draw(side?0x1c28:0x1608,w[67]-n_00a9c1c4(context,side,slot),px,y);break;
    case 2:if(int(n_00a9c3bc(context,side,slot))>0&&int(n_00a9c49c(context,side,slot))>0)draw(side?0x1ec8:0x18a8,n_00a9c49c(context,side,slot)-n_00a9c3bc(context,side,slot),px,y);else if(n_00a999e4(context,side,slot)>0)draw(side?0x1b48:0x1528,w[80],px,y);break;
    case 3:if(w[77]>0)draw(side?0x1de8:0x17c8,w[78],px,y);break;
    case 4:if(int(n_00a96948(context,side,slot))>0&&w[151]>0)draw(side?0x2e00:0x2dc8,w[151]-n_00a96948(context,side,slot),px,y);break;
    case 5:if(int(n_00a9cd2c(context,side,slot))>0&&(int(n_00a9cc4c(context,side,slot))>0||int(n_00a9d204(context,side,slot))>0||int(n_00a9d378(context,side,slot))>0))draw(0x35f0,n_00a9cd2c(context,side,slot),px,y);break;
   }}
   if(w[93]>0)draw(side?0x1fa8:0x1988,w[92],x,y);
   if(w[95]>0)draw(side?0x2088:0x1a68,w[94],x,y-42);
   if(w[102]>0)draw(0x2168,w[101],x,y-42);
   if(n_00a9c81c(context,side,slot))draw(0x2328,w[134],x,y-42);
   const int shield=n_00a9cfb8(context,side,slot);if(shield>0)draw(0x2440+shield*0x38,w[193],x,y-42);
  }
  if(!(battle->config.environment.unit_modes[1]&1)){const auto &e=battle->config.environment;int anchor[2];battle->check(kbcs_core_boss_effect_anchor(e.castle_x,actorAt(battle->actors,1,0).words[4],e.castle_scale,e.castle_offset,battle->config.castle_y_offset,anchor));for(int slot=0;slot<actorEnd();++slot){const auto &w=actorAt(battle->actors,1,slot).words;if(w[64]&&w[65]<=battle->config.boss_frames)list.push_back({8,0,-1,0x1040,w[65],anchor[0],anchor[1],0,{}});}}
  *out=list.data();*count=int32_t(list.size());return 0;
 }catch(...){return 3;}
}

extern "C" uint32_t kbcs_core_battle_sounds(const KbcsBattle *battle,const KbcsBattleSound **out,int32_t *count){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);if(!battle||!out||!count)return 1;*out=battle->sounds.data();*count=int32_t(battle->sounds.size());return 0;}

#include "actor_top.inc"

extern "C" uint32_t kbcs_core_battle_slots(const KbcsBattle *battle,int32_t *count){
 if(!battle||!count)return 1;*count=battle->pool.size();return 0;
}
extern "C" uint32_t kbcs_core_battle_actor_refs(const KbcsBattle *battle,const KbcsBattleActorRef **out,int32_t *count){
 if(!battle||!out||!count)return 1;ActorPoolScope pool_scope(battle->pool);
 try{auto &refs=battle->actor_refs;refs.clear();
  for(int side=0;side<2;++side)for(int slot=0;slot<actorEnd();++slot){const auto &actor=actorAt(battle->actors,side,slot);if(!slot||actor.words[0])refs.push_back({&actor,side,slot,battle->profileIndex(side,slot)});}
  *out=refs.data();*count=int32_t(refs.size());return 0;
 }catch(...){return 3;}
}
