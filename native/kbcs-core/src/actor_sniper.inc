// 005ce564/005ced48。画像の有無で照準・弾・命中の時計と乱数を省略しない。
namespace {
float nativeSin(float angle){return float(std::sin((double(angle)*3.141592653589793)/180.));}
float nativeCos(float angle){return float(std::cos((double(angle)*3.141592653589793)/180.));}
float nativeAngle(float y,float x){
 const float value=std::atan2(y,x);double degrees=double(value*180.f)/3.141592653589793;
 if(y<0)degrees+=360.;return float(degrees);
}
}
extern "C" uint32_t kbcs_core_actor_sniper_step(KbcsActorSniper *state,const KbcsSniperInput *input,const KbcsActor actors[2][51],const KbcsActorEnvironment *environment,int32_t *fired){
 if(!state||!input||!actors||!environment||!fired||input->enabled<0||input->enabled>1||input->height<1||!std::isfinite(input->phase)||!std::isfinite(state->angle))return 1;
 try{
  auto &s=*state;s.target=0;*fired=-1;
  if(!input->enabled){s.smoke_active=0;s.firing=0;for(auto &bullet:s.bullets)bullet.active=0;return 0;}
  KbcsActorDefinition definition{};auto env=*environment;KbcsSpawnRequest request{};uint32_t random=1;
  Context context{definition,env,const_cast<KbcsActor (*)[51]>(actors),request,random};
  int maximum=0;
  for(int i=1;i<actorEnd();++i)if(actorAt(actors,1,i).words[0]&&n_00a94484(context,1,i,-1)&&i!=env.castle_slot&&maximum<=actorAt(actors,1,i).words[3]){maximum=actorAt(actors,1,i).words[3];s.target=i;}
  const auto &castle=actorAt(actors,0,0).words;const float wave=nativeSin(input->phase);
  s.desired=0;
  if(s.target){const auto &target=actorAt(actors,1,s.target).words;
   const int x=(castle[3]-input->camera)/10+203,y=int(std::fma(wave,10.f,float(castle[4]/10-369)));
   const float degrees=nativeAngle(float(y-target[4]/10-target[5]*4+58),float(x-(target[3]-input->camera)/10));
   if(360.f-degrees>0)s.desired=-(360.f-degrees);
  }
  bool aligned=false;
  if(s.desired<=s.angle){s.angle-=1.f;if(s.angle<=s.desired){s.angle=s.desired;aligned=true;}}
  else if(s.angle<=s.desired){s.angle+=1.f;if(s.desired<=s.angle){s.angle=s.desired;aligned=true;}}
  if(!s.target)aligned=false;
  s.wait=s.wait<299?s.wait+1:300;
  if(aligned&&s.wait>299&&!s.firing){s.wait=0;s.firing=1;s.frame=0;}
  if(s.firing){const int previous=s.frame;++s.frame;
   if(previous==1||previous==3)s.gun_recoil=-6;
   else if(previous==2)s.gun_recoil=-10;
   else{
    s.gun_recoil=0;
    if(s.frame==11){
     if(s.angle==s.desired&&s.target&&actorAt(actors,1,s.target).words[0]&&actorAt(actors,1,s.target).words[1]<3){
      for(int i=0;i<50;++i)if(!s.bullets[i].active){
       s.bullets[i]={1,castle[3]+1770,int(std::fma(wave*10.f,10.f,float(castle[4]-3958))),s.target,int(s.desired),1500};
       s.wait=0;s.smoke_active=1;for(auto &part:s.smoke)std::fill_n(part,5,0);
       s.smoke[0][3]=30;s.smoke[1][3]=-30;s.smoke[2][4]=30;s.smoke[3][4]=-30;*fired=i;break;
      }
     }else{s.firing=0;s.frame=0;s.wait=300;}
    }
    if(s.frame>11&&s.smoke_active)for(auto &part:s.smoke){const int previous=part[2]++;part[0]+=part[3];part[1]+=part[4];part[3]/=2;part[4]/=2;if(previous>8)s.smoke_active=0;}
    if(s.frame>=11&&s.frame<=15){constexpr int bump[]={20,-10,5,-2,1};s.body_bump=bump[s.frame-11];}
    else if(s.frame==16)s.body_bump=0;
    if(s.frame>27)s.firing=0;
   }
  }
  for(auto &bullet:s.bullets)if(bullet.active){
   bullet.x=int(std::fma(-float(bullet.speed),nativeCos(float(bullet.angle)),float(bullet.x)));
   bullet.y=int(std::fma(-float(bullet.speed),nativeSin(float(bullet.angle)),float(bullet.y)));
   if(input->height<=bullet.y/10||bullet.x< -999)bullet.active=0;
  }
  return 0;
 }catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_actor_sniper_hit(KbcsActorSniper *state,KbcsActor actors[2][51],const KbcsActorEnvironment *environment,int32_t slot,uint32_t *seed,int32_t *hits){
 if(!state||!actors||!environment||slot<1||slot>=actorEnd()||!seed||!*seed||!hits)return 1;
 try{
  KbcsActorDefinition definition{};auto env=*environment;KbcsSpawnRequest request{};Context context{definition,env,actors,request,*seed};*hits=0;
  auto &target=actorAt(actors,1,slot).words;
  for(int i=0;i<50;++i){auto &bullet=state->bullets[i];if(!bullet.active||bullet.target!=slot||target[3]<bullet.x)continue;
   const bool eligible=n_00a94484(context,1,slot,-1);bullet.active=0;bool visual=!eligible;
   if(eligible){
    if(n_00a9cc4c(context,1,slot)<1){const int roll=n_0044a8d8(context,100);
     if(int(n_00a9b790(context,1,slot))<=roll){
      n_00a9bbac(context,1,slot,n_00a96cd8(context,1,slot)?1:actorAt(actors,0,0).words[7]/20);
      target[23]=1;visual=true;++*hits;
     }else{n_00a9cc8c(context,1,slot,n_00a9b81c(context,1,slot));n_00a9cd6c(context,1,slot,1);}
    }
   }
   if(visual){auto &impact=state->impacts[i];impact[0]=12;impact[1]=target[3]-n_0044a8d8(context,100)*10-187;impact[2]=target[4]+n_0044a8d8(context,60)*10-1475;
    impact[3]=12;impact[4]=target[3]-n_0044a8d8(context,100)*10-187;impact[5]=target[4]+n_0044a8d8(context,60)*10-1475;
   }
  }
  return 0;
 }catch(...){return 3;}
}

extern "C" uint32_t kbcs_core_battle_camera(KbcsBattle *battle,const KbcsSceneLayout *layout){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||battle->failed||!layout||!std::isfinite(layout->center)||!std::isfinite(layout->zoom)||layout->zoom<=0)return 1;
 const double value=(layout->center-480./layout->zoom)*10.;if(value<INT32_MIN||value>INT32_MAX)return 1;
 battle->camera=int32_t(value);battle->camera_zoom=layout->zoom;return 0;
}
extern "C" uint32_t kbcs_core_battle_sniper_status(const KbcsBattle *battle,int32_t out[5]){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!out)return 1;out[0]=(battle->config.state.items_on>>5)&1;out[1]=battle->sniper.target;out[2]=battle->sniper.wait;
 out[3]=0;for(const auto &bullet:battle->sniper.bullets)out[3]+=bullet.active!=0;out[4]=battle->sniper.firing;return 0;
}
extern "C" uint32_t kbcs_core_battle_sniper_draw(const KbcsBattle *battle,const KbcsSceneLayout *scene,const KbcsBattleAtlases *paint,KbcsDrawCommand *out,int32_t capacity,int32_t *count){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!scene||!paint||!out||!count||capacity<164||!std::isfinite(scene->zoom)||scene->zoom<=0)return 1;
 *count=0;if(!(battle->config.state.items_on&(1<<5)))return 0;
 if(!paint->cuts[0]||!paint->cuts[1]||paint->counts[0]<10||paint->counts[1]<14)return 1;
 const auto &s=battle->sniper;const auto &castle=actorAt(battle->actors,0,0).words;const float shift=float(scene->viewport_width-960.)*.5f;
 const auto sprite=[&](int atlas,int cut,float x,float y,float w,float h,bool flip=false,float angle=0,float px=0,float py=0){
  if(cut<0||cut>=paint->counts[atlas])throw std::out_of_range("sniper cut");
  const auto &rect=paint->cuts[atlas][cut];KbcsDrawCommand c{paint->textures[atlas],2,4,0,1,{},{rect.x,rect.y,rect.width,rect.height},{}};
  const float radians=float(double(angle)*3.141592653589793/180.),sn=std::sin(radians),cs=std::cos(radians);
  const float corners[4][2]={{flip?w:0,0},{flip?w:0,h},{flip?0:w,h},{flip?0:w,0}};
  for(int i=0;i<4;++i){const float dx=corners[i][0]-px,dy=corners[i][1]-py;
   const float vx=x+shift+px+std::fma(sn,dy,cs*dx),vy=y+py+std::fma(-sn,dx,cs*dy);
   c.points[i*2]=scene->zoom*vx+double(shift)*(1.-scene->zoom);
   c.points[i*2+1]=scene->y_origin+(vy-scene->y_origin+scene->y_offset)*scene->zoom;
  }
  out[(*count)++]=c;
 };
 try{
  // 005cefb4の部品順、浮動小数点寸法、反転と砲身の回転基準点。
  const float x=float((castle[3]-battle->camera)/10+100+s.body_bump);
  const float y=float(int(std::fma(nativeSin(battle->sniper_phase),10.f,float(castle[4]/10-683))));
  sprite(0,6,x,y+114.56f,53.7f,161.1f);sprite(0,6,x+132.46f,y+114.56f,53.7f,161.1f,true);
  sprite(0,s.firing?5:4,x+(s.firing?53.7f:51.91f),y+202.27f+(s.firing?s.gun_recoil:0),82.34f,91.29f);
  sprite(0,3,x+42.96f,y+286.4f,91.29f,42.96f);
  sprite(0,2,x+34.01f,y+288.19f,93.08f,57.28f,false,s.angle,68.f,26.f);
  sprite(0,1,x+34.01f,y+268.5f,118.14f,59.07f);
  sprite(0,0,x,y,93.08f,187.95f);sprite(0,0,x+93.08f,y,93.08f,187.95f,true);
  sprite(0,9,x+(s.firing?51.91f:50.12f),y+(s.firing?186.16f+s.gun_recoil:193.32f),89.5f,69.81f);
  if(s.smoke_active)for(const auto &part:s.smoke){const float sx=float(int(x-int(nativeCos(s.angle)*47.f)+part[0]+35));
   sprite(1,part[2]/2+8,sx,y-int(nativeSin(s.angle)*28.f)+part[1]+256,137,117);
  }
  sprite(0,7,float((castle[3]-battle->camera)/10+153+s.body_bump),float(castle[4]/10+47),80.55f,7.16f);
  for(const auto &bullet:s.bullets)if(bullet.active)sprite(0,8,float((bullet.x-battle->camera)/10),float(bullet.y/10),53,53);
  for(const auto &impact:s.impacts)for(int j:{0,3})if(impact[j]>1)sprite(1,13-impact[j]/2,float((impact[j+1]-battle->camera)/10),float(impact[j+2]/10),137,117);
  return 0;
 }catch(...){*count=0;return 3;}
}
