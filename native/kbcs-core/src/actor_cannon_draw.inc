// 005d76a0の固定画像部分。モーション部品はbattle_visualsと共通poseへ渡す。
extern "C" uint32_t kbcs_core_actor_cannon_draw(const KbcsActor *castle,int32_t camera,const KbcsSceneLayout *scene,const KbcsBattleAtlases *paint,KbcsDrawCommand *out,int32_t capacity,int32_t *count){
 if(!castle||!scene||!paint||!out||!count||capacity<1||capacity>4096)return 1;*count=0;
 const auto &w=castle->words;const int action=w[9],frame=w[10];if(action!=1&&action!=3&&action!=9&&action!=12)return 0;
 if(!paint->cuts[0]||paint->counts[0]<1)return 1;
 try{
  const float shift=float(scene->viewport_width-960.)*.5f;double opacity=1;int blend=0;
  const auto rect=[&](int cut)->const KbcsRenderCut&{if(cut<0||cut>=paint->counts[0])throw std::out_of_range("cannon cut");return paint->cuts[0][cut];};
  const auto quad=[&](int cut,const int points[8],int crop_x=0,int crop_width=0){
   if(*count>=capacity)throw std::out_of_range("cannon capacity");const auto &r=rect(cut);
   KbcsDrawCommand c{paint->textures[0],2,4,blend,opacity,{},{r.x+crop_x,r.y,crop_width?crop_width:r.width,r.height},{}};
   for(int i=0;i<4;++i){c.points[i*2]=points[i*2]*scene->zoom+shift*(1.-scene->zoom);c.points[i*2+1]=scene->y_origin+(points[i*2+1]-scene->y_origin+scene->y_offset)*scene->zoom;}
   out[(*count)++]=c;
  };
  const auto sprite=[&](int cut,int x,int y,int width,int height){const int points[]={x,y,x,y+height,x+width,y+height,x+width,y};quad(cut,points);};
  const int x=int((w[3]-camera)/10+27+double(shift)),y=w[4]/10-160;
  const int end=int((w[3]-camera)/10+27-160*w[6]*frame/((action==1||action==9)?16:32)+double(shift));
  const float angle=nativeAngle(float(490-y),float(end-x))+180.f,cs=nativeCos(angle),sn=nativeSin(angle);
  const int length=int(std::sqrt(float((y-490)*(y-490)+(x-end)*(x-end))));
  const float tx=std::fma(cs,float(-x),std::fma(-sn,float(-y),float(x))),ty=std::fma(sn,float(-x),std::fma(cs,float(-y),float(y)));
  const auto beam=[&](int cut,int left,int right,int half,int crop_x=0,int crop_width=0){
   const int source[]={left,y-half,left,y+half,right,y+half,right,y-half};int points[8];
   for(int i=0;i<4;++i){points[i*2]=int(std::fma(float(source[i*2]),cs,std::fma(float(source[i*2+1]),-sn,tx)));points[i*2+1]=int(std::fma(float(source[i*2]),sn,std::fma(float(source[i*2+1]),cs,ty)));}
   quad(cut,points,crop_x,crop_width);
  };
  if(action==1){
   beam(9,x-length,x,rect(9).height/2);sprite(frame%4/2+5,end-30,450,132,50);
   blend=1;const auto &r=rect(7);sprite(7,x-r.width/2,y-r.height/2,r.width,r.height);sprite(7,x-r.width,y-r.height,r.width*2,r.height*2);return 0;
  }
  opacity=frame<2?64./255.:frame>30?double(255-(frame-30)*255/3)/255.:1.;
  if(action==12){
   beam(4,x-length,x,rect(4).height/2);constexpr int cuts[]={2,2,2,3,3};const int cut=cuts[frame%5];sprite(cut,end-30,450,rect(cut).width,rect(cut).height);return 0;
  }
  if(action==9){
   if(frame>1){int at=0;uint32_t random=uint32_t(frame/2);do{const int width=std::min(rect(5).width,length-at);const int before=at;at+=width;
     const int cut=int(random&3)+3;random^=random<<13;random^=random>>17;random^=random<<15;beam(cut,x-before,x-at,rect(5).height/2,0,width);
     if(width<1)break;
    }while(at<length);
    blend=1;const auto &r=rect(1);sprite(1,x-r.width,y-r.height,r.width*2,r.height*2);
   }return 0;
  }
  if(frame>1){
   int at=0;do{const int width=std::min(rect(5).width/2,length-at),before=at;at+=width;beam(5,x-before,x-at,(frame%4>1?-rect(5).height:rect(5).height)/2,rect(5).width/4,width);if(width<1)break;}while(at<length);
   constexpr int cuts[]={0,0,1,1,6,6};const int cut=cuts[frame%6];sprite(cut,end-80,370,rect(cut).width*3,rect(cut).height*3);
  }
  blend=1;
  if(frame>1){const auto &a=rect(2);sprite(2,end+5-a.width*3,505-a.height*3,a.width*6,a.height*3);const auto &b=rect(4);sprite(4,end+5-b.width*3,505,b.width*6,b.height);}
  const auto &r=rect(3);sprite(3,x-r.width,y-r.height,r.width*2,r.height*2);sprite(3,x-r.width*5/2,y-r.height*5/2,r.width*5,r.height*5);return 0;
 }catch(...){*count=0;return 3;}
}

extern "C" uint32_t kbcs_core_battle_cannon_draw(const KbcsBattle *battle,const KbcsSceneLayout *scene,const KbcsBattleAtlases *paint,KbcsDrawCommand *out,int32_t capacity,int32_t *count){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle)return 1;return kbcs_core_actor_cannon_draw(&actorAt(battle->actors,0,0),battle->camera,scene,paint,out,capacity,count);
}

// 005cca80: 被弾の12F記録。メタル/特殊被弾は通常色の後に加算色を重ねる。
extern "C" uint32_t kbcs_core_battle_hit_draw(const KbcsBattle *battle,const KbcsSceneLayout *scene,const KbcsBattleAtlases *paint,KbcsDrawCommand *out,int32_t capacity,int32_t *count){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!scene||!paint||!out||!count||!paint->cuts[0]||paint->counts[0]<14||capacity<224+(actorEnd()-51)*4)return 1;*count=0;
 const int shift=int(scene->viewport_width-960)/2;
 for(int side=0;side<2;++side)for(int slot=0;slot<std::max(56,actorEnd());++slot){const auto &v=slot<51?battle->impacts[side][slot]:slot<actorEnd()?battle->pool.extra[slot-51].impacts[side]:battle->impacts[side][slot];if(v[0]<=1)continue;
  const auto &r=paint->cuts[0][13-v[0]/2];const int x=(v[1]-battle->camera)/10+shift,y=v[2]/10;
  const auto sprite=[&](int blend,int red,int green,int blue){KbcsDrawCommand c{paint->textures[0],2,4,blend,1,{},{r.x,r.y,r.width,r.height},{red,green,blue,1,0,0}};
   const int points[8]={x,y,x,y+117,x+137,y+117,x+137,y};
   for(int i=0;i<4;++i){c.points[i*2]=points[i*2]*scene->zoom+shift*(1.-scene->zoom);c.points[i*2+1]=scene->y_origin+(points[i*2+1]-scene->y_origin+scene->y_offset)*scene->zoom;}out[(*count)++]=c;};
  if(v[3]==2){sprite(0,200,170,255);sprite(1,145,135,165);}
  else if(v[3]==1){sprite(0,204,204,204);sprite(1,255,255,255);}
  else sprite(0,255,255,255);
 }
 return 0;
}
