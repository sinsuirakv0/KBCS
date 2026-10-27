// 009eadc8/0063a050の設定と005d8f58の発射。陣営の通常個体の攻撃と混ぜない。
extern "C" uint32_t kbcs_core_actor_cannon_setup(KbcsActor *out,const KbcsCannonSetup *input,const KbcsCannonGrowth *growth,int32_t count){
 if(!out||!input||(!growth&&count)||count<0||count>512||input->kind<0||input->kind>7||input->level<1||input->level>30||input->range_level<0||input->range_level>9||input->attack_level<0||input->attack_level>29)return 1;
 try{
  KbcsActor actors[2][51]{};
  const auto value=[&](int type){int start=1;for(int i=0;i<count;++i){const auto &g=growth[i];if(g.kind!=type)continue;
   if(input->level>=start&&input->level<=g.end){const int elapsed=input->level-start,span=g.end-start,delta=g.value2-g.value1;
    if(!g.easing)return g.value1+(span?delta*elapsed/span:0);if(g.easing<1||g.easing>2)return 0;
    float at=float(elapsed)/float(span);if(g.easing==2)at+=-1.f;at=std::pow(at,3.f);if(g.easing==2)at+=1.f;return int(std::fma(at,float(delta),float(g.value1)));
   }start=g.end;
  }return 0;};
  KbcsActorDefinition definition{};KbcsActorEnvironment environment{};KbcsSpawnRequest request{};uint32_t seed=1;Context context{definition,environment,actors,request,seed};auto &w=actors[0][0].words;
  w[6]=input->range_level+3;w[16]=std::max(0,((input->combo+100)*(input->treasure+input->attack_level*50+100))/100);
  w[17]=input->kind;w[20]=value(0)*w[16]/100;w[26]=-3;w[22]=0;
  n_00a932e8(context,0,input->status[1]);n_00a93914(context,0,input->status[3]);n_00a93988(context,0,input->status[4]);n_00a93b6c(context,0,input->status[5]);
  if(input->kind==2){w[21]=value(3);w[22]=value(4);w[26]=input->status[2];w[27]=value(6);}
  else if(input->kind==4){w[22]=input->status[2];w[27]=value(7);w[30]=value(8);}
  else if(input->kind==5){w[22]=input->status[2];w[27]=value(9);w[30]=value(11);w[31]=value(10);}
  if(input->kind==3||input->kind==4||input->kind==6)w[21]=value(5);
  const int slow=value(1),stop=value(2),curse=value(12);
  n_00a93b2c(context,0,slow>0?100:0);n_00a93b38(context,0,std::max(0,slow));
  n_00a93b0c(context,0,stop>0?100:0);n_00a93b18(context,0,std::max(0,stop));
  n_00a93b4c(context,0,curse>0?100:0);n_00a93b58(context,0,std::max(0,curse));*out=actors[0][0];return 0;
 }catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_actor_cannon_fire(KbcsActor actors[2][51],const KbcsActorEnvironment *environment,const KbcsSpawnRequest *iron,uint32_t *seed,KbcsSpawnConstructor construct,void *user,KbcsCannonFire *out){
 if(!actors||!environment||!seed||!*seed||!out)return 1;
 try{KbcsCannonFire result{0,-1,15};auto &castle=actors[0][0].words;
 if(castle[12]||castle[9]){*out=result;return 0;}
 const int type=castle[17];if(type<0||type>7)return 1;
 int position=environment->stage_width-3200;
 if(type==2||type==6){position=3200;for(const auto &enemy:actors[1])if(enemy.words[0]&&enemy.words[0]!=1&&position<enemy.words[3])position=enemy.words[3];}
 if(type==2){
  if(!iron||!construct)return 1;const int slot=construct(user,iron,seed);if(slot<0){*out=result;return slot== -1?0:1;}if(slot<1||slot>50)return 1;
  auto &wall=actors[0][slot].words;wall[3]=position+castle[27];wall[7]=castle[21]*wall[7]/100;wall[8]=wall[7];wall[117]=castle[22];result.slot=slot;
 }
 if(type==3||type==4){
  KbcsActorDefinition definition{};auto env=*environment;KbcsSpawnRequest request{};Context context{definition,env,actors,request,*seed};
  for(int i=0;i<51;++i)if(actors[0][i].words[0]&&actors[0][i].words[0]!=1&&actors[0][i].words[3]<position&&n_00a9467c(context,0,i))position=actors[0][i].words[3];
  castle[18]=position-castle[21]/2;
 }else if(type==6)castle[18]=position;
 constexpr int actions[]={1,3,6,4,7,9,11,12},sounds[]={25,60,61,37,65,84,-1,124};
 castle[9]=actions[type];castle[10]=0;castle[12]=castle[11];++castle[13];result.fired=1;result.sound=sounds[type];*out=result;return 0;
 }catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_actor_cannon_action(KbcsActorCannon *state,KbcsActor actors[2][51],const KbcsCannonRules *rules,int32_t side){
 if(!state||!actors||!rules||side<0||side>1)return 1;auto &w=actors[side][0].words;const int action=w[9];
 if(action==1||action==9){if(++w[10]>16){w[9]=action==1?2:10;w[10]=0;}}
 else if(action==2||action==10){++w[10];if(!(w[10]&3))for(auto &segment:state->segments[side])if(!segment[0]){
   if(w[17]==0)segment[0]=rules->encoded[3]-1;else if(w[17]==5)segment[0]=rules->encoded[1];
   segment[1]=w[3]+(side?-270:270)+(side?-1850:0)+(side?1:-1)*160*(w[10]/4)*10;segment[2]=w[13];
   if(w[6]<=w[10]/4){w[9]=0;w[10]=0;}break;
  }}
 else if(action==3||action==12){if(++w[10]>32){actors[0][0].words[9]=0;actors[0][0].words[10]=0;}}
 else if(action==4||action==7){if(++w[10]>rules->encoded[1]){actors[0][0].words[9]=action==4?5:8;actors[0][0].words[10]=0;}}
 else if(action==5||action==8||action==6||action==11){++w[10];const int limit=action==6?rules->encoded[0]:action==11?rules->encoded[2]+10:rules->encoded[1];if(w[10]>limit){actors[0][0].words[9]=0;actors[0][0].words[10]=0;}}
 return 0;
}
extern "C" uint32_t kbcs_core_actor_cannon_hit(KbcsActorCannon *state,KbcsActor actors[2][51],const KbcsActorEnvironment *environment,const KbcsActorHitContext *hit,const KbcsActorClock *clock,KbcsActorDamageContext *damage,const KbcsCannonRules *rules,int32_t side,int32_t target,int32_t id,uint32_t *seed,KbcsActorEffectEvents *events){
 if(!state||!actors||!environment||!hit||!clock||!damage||!rules||!seed||!*seed||!events||side<0||side>1||target<1||target>50)return 1;
 try{KbcsActorDefinition definition{};auto env=*environment;KbcsSpawnRequest request{};Context context{definition,env,actors,request,*seed};
  context.cannon=state;context.cannonRules=rules;context.hit=hit;context.effects=&hit->effects;context.events=events;context.clock=clock;context.damage=damage;
  n_005d6c3c(context,0,side,target,id);return 0;
 }catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_actor_cannon_step(KbcsActorCannon *state,KbcsActor actors[2][51],const KbcsActorEnvironment *environment,const KbcsActorHitContext *hit,const KbcsActorClock *clock,KbcsActorDamageContext *damage,const KbcsCannonRules *rules,int32_t side,uint32_t *seed,KbcsActorEffectEvents *events){
 if(!state||!actors||!environment||!hit||!clock||!damage||!rules||!seed||!*seed||!events||side<0||side>1)return 1;
 try{KbcsActorDefinition definition{};auto env=*environment;KbcsSpawnRequest request{};Context context{definition,env,actors,request,*seed};
  context.cannon=state;context.cannonRules=rules;context.hit=hit;context.effects=&hit->effects;context.events=events;context.clock=clock;context.damage=damage;
  n_005d6740(context,0,side);return 0;
 }catch(...){return 3;}
}
