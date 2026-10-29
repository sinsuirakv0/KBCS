// 006ddfb8/006e15e8..006e1b9c。描画値を返し、GPU・文字列・DBへ依存しない。
extern "C" uint32_t kbcs_core_battle_score_display(int32_t score,KbcsScoreDisplay *state){
 if(!state||state->phase<0||state->phase>2||state->frame<0||state->frame>5)return 1;auto &s=*state;
 if(s.phase==2){s.origin=s.value=score;s.scale=150-s.frame*8;if(s.frame++>4)s.phase=s.frame=0;}
 else if(s.phase==1){const int delta=int32_t(uint32_t(score)-uint32_t(s.origin));s.scale=100+s.frame*12;s.value=int32_t(uint32_t(s.origin)+uint32_t(delta/4)*uint32_t(s.frame));if(s.frame++>2){s.phase=2;s.frame=0;}}
 else{s.scale=100;s.origin=s.value=score;}return 0;
}
namespace {
struct TopDraw {
 const KbcsRenderCut *cuts;int size;KbcsDrawCommand *out;int capacity,count=0;int texture=0;int red=255,green=255,blue=255;
 void rect(KbcsRenderCut cut,double x,double y,double w,double h){
  if(count>=capacity)throw std::out_of_range("top capacity");auto &c=out[count++];c={};c.texture=texture;c.layer=10;c.count=4;c.opacity=1;
  const double points[]={x,y,x,y+h,x+w,y+h,x+w,y};std::copy_n(points,8,c.points);c.cut[0]=cut.x;c.cut[1]=cut.y;c.cut[2]=cut.width;c.cut[3]=cut.height;c.colors[0]=red;c.colors[1]=green;c.colors[2]=blue;c.colors[3]=1;
 }
 const KbcsRenderCut &cut(int id) const {if(id<0||id>=size)throw std::out_of_range("top cut");return cuts[id];}
 void sprite(int id,double x,double y){const auto &c=cut(id);rect(c,x,y,c.width,c.height);}
 void number(int value,int base,float x,float y,int gap,float scale,int flags,int places=0){
  value=std::max(0,value);std::vector<int> digits;do{digits.push_back(value%10);value/=10;}while(value);while(int(digits.size())<places)digits.push_back(0);
  float width=float(gap*(int(digits.size())-1));for(int digit:digits)width+=scale*float(cut(base+digit).width);
  if(flags&1)x-=width*.5f;else if(flags&2)x-=width;
  if(flags&4)y-=float(cut(base).height)*scale*.5f;
  for(auto i=digits.rbegin();i!=digits.rend();++i){const auto &c=cut(base+*i);rect(c,x,y,float(c.width)*scale,float(c.height)*scale);x+=float(gap)+float(c.width)*scale;}
 }
 void box(int id,int pad,int x,int y,int w,int h){
  const auto &c=cut(id);const int xs[]={x,x+pad,x+w-pad},ws[]={pad,w-pad*2,pad};
  // この部品は高さ42の横伸縮。上下paddingは原本で0なので3区画だけ。
  for(int i=0;i<3;++i)rect({c.x+(i==0?0:i==1?pad:c.width-pad),c.y,i==1?c.width-pad*2:pad,c.height},xs[i],y,ws[i],h);
 }
};
}
extern "C" uint32_t kbcs_core_battle_top_draw(const KbcsBattle *battle,const KbcsRenderCut *cuts,int32_t count,const KbcsRenderCut *fever,int32_t fever_count,const KbcsRenderCut *title,KbcsDrawCommand *out,int32_t capacity,int32_t *written){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!cuts||count<0||!out||capacity<0||!written||fever_count<0||(!fever&&fever_count))return 1;
 try{
  TopDraw d{cuts,count,out,capacity};const auto &r=battle->result;const auto &rules=battle->config.rules;const int center=battle->config.screen.viewport_width/2;
  // 006e11ac。タイトルをスコア枠より先に描く。PCの安全領域は0。
  if(title){d.texture=2;d.rect(*title,62,10,title->width,title->height);d.texture=0;}
  if(rules.score_type!=1&&rules.score_type!=3){*written=d.count;return 0;}
  if(count<160)return 1;
  d.box(106,cuts[107].x-cuts[106].x,center-134,10,269,42);d.sprite(rules.score_type==3?159:104,center-(rules.score_type==3?119:122),rules.score_type==3?15:17);d.sprite(105,center+100,19);
  const int value=rules.score_type==3?battle->points.score:battle->score_display.value;int digits=1;for(int v=std::max(0,value);v>=10;v/=10)++digits;
  d.number(value,14,float(center+100-(cuts[14].width-1)*digits/2),float(17+cuts[14].height/2),-1,rules.score_type==3?1.f:float(battle->score_display.scale)/100.f,5);
  if(rules.score_type==3&&rules.point.fever_count>=3&&fever_count>9){
   TopDraw f{fever,fever_count,out+d.count,capacity-d.count};f.texture=1;const int x=center-fever[8].width/2,y=70;
   f.sprite(battle->points.wait>0?8+(battle->points.frame/3)%2:8,x,y);
   const int blank=battle->points.wait>0?int((1.-double(battle->points.wait)/rules.point.fever[2])*294.):294-battle->points.gauge;
   if(blank>0)f.rect(f.cut(7),x+301-blank,77,blank,32);
   f.sprite(6,x+fever[8].width/2-fever[6].width/2,y+fever[8].height/2-fever[6].height/2);d.count+=f.count;
  }
  if((rules.score_type==1&&r.mode!=4)||(rules.score_type==3&&r.mode==0&&rules.time_limit>=0)){
   const int remaining=std::max(0,rules.time_limit-r.timer);if(remaining<=900)d.green=d.blue=0;
   d.number(remaining/1800,83,8,64,0,1,16,2);d.rect(d.cut(93),56,64,27,46);
   d.number(remaining/30%60,83,83,64,0,1,16,2);d.rect(d.cut(93),131,71.666668f,22.5f,38.333332f);
   d.number(remaining%30*100/30,83,153,64,0,1,16,2);
  }
  *written=d.count;return 0;
 }catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_battle_overlay(const KbcsBattle *battle,KbcsDrawCommand *out,int32_t capacity,int32_t *written){
 ActorPoolScope pool_scope(battle?&battle->pool:nullptr);
 if(!battle||!out||capacity<2||!written)return 1;KbcsBattleEnding e{};const auto code=kbcs_core_battle_ending(battle,&e);if(code)return code;int count=0;
 const auto rect=[&](int x,int y,int w,int h,int red,int green,int blue){auto &c=out[count++];c={};c.texture=-2;c.layer=11;c.count=4;c.blend=2;c.opacity=1;const double p[]={double(x),double(y),double(x),double(y+h),double(x+w),double(y+h),double(x+w),double(y)};std::copy_n(p,8,c.points);c.colors[0]=red;c.colors[1]=green;c.colors[2]=blue;};
 if(e.shade)rect(0,0,battle->config.screen.viewport_width,640,255-e.shade,255-e.shade,255-e.shade);
 if(battle->result.mode&&battle->result.mode!=2&&e.phase>1)rect(e.bar_x,315,battle->config.screen.viewport_width,55,40,40,77);
 *written=count;return 0;
}
