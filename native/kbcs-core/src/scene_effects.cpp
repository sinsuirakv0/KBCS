#include "kbcs_core.h"
#include <algorithm>
#include <cmath>
#include <memory>
#include <unordered_map>
#include <vector>

namespace {
constexpr double pi=3.141592653589793;
double rad(double a){return a*pi/180.;}
struct Particle {KbcsEffectParticle out{};int segment;double wait,life,angular,speed,vx,vy,direction,bounds[4];bool bounded[4];};
struct Classic {int kind,index,variant,color;bool front;double x,y,phase,size,age,speed,angle,velocity,alpha,slope=0,fall_speed=0,amplitude=0,rotation=0;};
struct Runtime {
  std::vector<KbcsEffectSegment> segments;std::vector<double> values;std::vector<int> assets,lengths;
  std::vector<Particle> particles;std::vector<Classic> weather;
  double width,minimum,margin,top,bottom,weather_top,weather_bottom,span;int classic,frame=0;uint32_t seed,state;
  uint32_t next(){state^=state<<13;state^=state>>17;state^=state<<15;return state;}
  double random(double bound){if(!(bound>0)||!std::isfinite(bound))throw 1;return std::floor(double(next())/4294967296.*bound);}
  double base(int kind,double n,int asset) {
    switch(kind){case 1:return float(n-margin);case 2:return float(n+width+margin);case 3:return float(n+top);case 4:return float(n+bottom);
      case 6:return n+960;case 7:return n+640;case 8:return float(n/30);case 9:return float(n/100);case 10:return float(n*255/100);
      case 11:case 12:return float(n+(asset>=0?lengths[size_t(asset)]:0));case 13:return n*960;default:return float(n);}
  }
  double sample(const KbcsEffectSpec &s,int asset,std::unordered_map<int,double> &groups,double fallback=0,bool integer=false){
    if(!s.kind)return fallback;
    if(s.kind==3){if(s.first<0||s.count<1||size_t(s.first+s.count)>values.size())throw 1;return base(s.base,values[size_t(s.first+int(random(s.count)))],asset);}
    if(s.kind!=2)return base(s.base,s.value,asset);
    const double low=base(s.low_base,s.low,asset),high=base(s.high_base,s.high,asset);
    if(s.group>=0){if(!groups.contains(s.group))groups[s.group]=random(10001)/10000.;return float(low+float(float(high-low)*groups[s.group]));}
    if(integer)return std::min(low,high)+random(std::abs(high-low)+1);
    const double range=std::trunc(double(float(std::abs(high-low)*10000)));
    return float(double(float(double(float(std::min(low,high)*10000))+random(range+1)))/10000.);
  }
  void spawn(Particle &p,bool initial){
    const auto &segment=segments[size_t(p.segment)];const auto &s=segment.properties;std::unordered_map<int,double> groups;
    const int selected=segment.first+int(random(segment.count));if(selected<0||size_t(selected)>=assets.size())throw 1;
    p.out={};p.out.asset=assets[size_t(selected)];if(p.out.asset<0||size_t(p.out.asset)>=lengths.size())throw 1;
    const auto value=[&](int key,double fallback=0,bool integer=false){
      // x..moveAngleの初期値はstartX..startMoveAngleを優先する。
      const int initial_key=key>=1&&key<=15?key+21:-1;
      const int chosen=initial&&initial_key>=0&&s[initial_key].kind?initial_key:key;
      return sample(s[chosen],p.out.asset,groups,fallback,integer);
    };
    p.out.x=value(1);p.out.y=value(2);p.out.frame=value(3,0,true);p.wait=value(4,0,true);p.life=value(5,-1,true);
    p.out.scale=value(6,1);p.out.sx=value(7,1);p.out.sy=value(8,1);p.out.angle=value(9);p.angular=value(10);p.out.alpha=value(11,255);
    p.speed=value(12);p.vx=value(13);p.vy=value(14);p.direction=value(15);p.out.front=s[20].base==14;
    for(int i=0;i<4;++i){p.bounded[i]=s[16+i].kind!=0;p.bounds[i]=p.bounded[i]?value(16+i):0;}
    if(s[21].kind){p.out.spacing_min=int(s[21].low);p.out.spacing_max=int(s[21].high);p.out.spacing=base(s[21].base,s[21].value,p.out.asset);}
    if(p.out.spacing_min>p.out.spacing_max||p.out.spacing_max-p.out.spacing_min>4096)throw 1;
  }
  void add(int kind,int count,bool front){for(int i=0;i<count;++i){Classic p{};p.kind=kind;p.front=front;p.index=i;p.x=random(span);p.y=weather_top+random(std::max(1.,weather_bottom-weather_top));p.phase=random(360);p.size=100+random(40);p.variant=int(random(2));p.age=random(400);p.speed=5+random(20);p.color=int(random(7));p.angle=175-random(85);p.velocity=200+random(600);p.alpha=255;weather.push_back(p);}}
  bool is(std::initializer_list<int> ids) const {return std::find(ids.begin(),ids.end(),classic)!=ids.end();}
  void reset(){
    frame=0;state=seed;particles.clear();weather.clear();
    for(size_t index=0;index<segments.size();++index){std::unordered_map<int,double> groups;const double requested=sample(segments[index].properties[0],-1,groups,1,true);if(!std::isfinite(requested))throw 1;const int count=int(std::clamp(requested,0.,10000.));
      if(particles.size()+size_t(count)>10000)throw 1;
      for(int i=0;i<count;++i){Particle p{};p.segment=int(index);spawn(p,true);particles.push_back(p);}}
    if(is({2,14,26,27,34,1074}))add(1,100,false);
    if(is({3,27,197}))add(2,100,true);
    if(is({13,15,72}))add(3,100,true);
    if(is({81,101,123,146,169}))add(4,50,true);
    if(classic==55)add(5,100,false);
    if(is({33,58})){add(6,30,false);add(7,60,true);}
    if(is({40,46,47})){add(classic==40?9:10,100,true);add(classic==40?9:10,100,true);for(auto &p:weather){p.size=50+random(150);p.velocity=50+random(150);p.phase=random(360);p.slope=2000+random(6000);p.fall_speed=random(100);p.amplitude=random(100);}}
    if(is({41,75,1008})){add(8,100,false);add(8,30,true);for(auto &p:weather){p.size=p.front?200+random(100):50+random(50);p.velocity=70+random(60);p.variant=(classic==41?0:1)+(p.front?0:random(10)==0?1:0);p.rotation=random(360);}}
  }
  void update(){
    for(auto &p:particles){if(p.wait>0){--p.wait;continue;}
      p.out.x=float(p.out.x+float(p.vx+float(p.speed*float(std::cos(rad(p.direction))))));
      p.out.y=float(p.out.y+float(p.vy+float(p.speed*float(std::sin(rad(p.direction))))));
      p.out.angle=float(p.out.angle+p.angular);const double previous=p.out.frame++;
      if((p.life>0&&previous>=p.life)||(p.bounded[0]&&p.out.x<p.bounds[0])||(p.bounded[1]&&p.out.x>p.bounds[1])||(p.bounded[2]&&p.out.y<p.bounds[2])||(p.bounded[3]&&p.out.y>p.bounds[3]))spawn(p,false);
    }
    const double zoom=minimum*100;
    for(auto &p:weather){++p.phase;switch(p.kind){
      case 1:p.age+=p.speed;if(p.age>399){p.age=0;p.x=std::fmod(p.index*192+random(192),span);p.y=weather_top+random(200+20*(100-zoom))+(classic==14?-60:classic==34?-200:0);p.speed=5+random(20);p.color=int(random(7));}break;
      case 2:p.x=std::trunc(p.x*100+std::cos(rad(p.angle))*p.velocity)/100;p.x=std::fmod(p.x+span,span);p.y=std::trunc(p.y*100+std::sin(rad(p.angle))*p.velocity)/100;if(p.y>=weather_bottom){p.y=weather_top;p.angle=175-random(85);p.velocity=200+random(600);}break;
      case 3:case 4:p.y-=p.kind==3?3:1;if(p.y<weather_top&&random(2000)==0){p.x=std::fmod(p.index*192+random(192),span);p.y=1280-std::trunc((100-zoom)*120/100);p.phase=random(360);p.size=100+random(40);p.variant=int(random(2));}break;
      case 6:p.x=random(span);p.y=420+random(90);break;
      case 7:p.x=random(span);p.y=weather_top+random(640+20*(100-zoom));p.alpha=100+random(100);break;
      case 5:++p.age;if(p.age>10)p.age=-1-random(60);else if(p.age==0){p.x=random(span);p.y=150+random(450);}break;
      case 8:p.y-=std::trunc(p.velocity*p.size/100)/100;++p.age;if(p.y<weather_top){p.x=random(span);p.y=p.front?480+std::trunc(20000/zoom)+random(50):340-random(50);p.age=0;p.size=p.front?200+random(100):50+random(50);p.velocity=70+random(60);p.variant=(classic==41?0:1)+(p.front?0:random(10)==0?1:0);}break;
      case 9:p.y+=std::trunc((170+p.fall_speed)*p.velocity/100)/100;if(p.y>=weather_bottom){p.y=weather_top;p.x=random(span);p.size=50+random(150);p.velocity=50+random(150);p.fall_speed=random(100);p.amplitude=random(100);}break;
      case 10:p.x+=std::trunc((p.slope+170)*p.velocity/100)/100;p.y+=std::trunc(4170*p.velocity/100)/100;if(p.x>=span)p.x=0;if(p.y>=weather_bottom){p.y=weather_top;p.x=random(span);p.size=50+random(150);p.velocity=50+random(150);p.slope=2000+random(6000);p.fall_speed=random(100);p.amplitude=random(100);}break;
    }}
    ++frame;
  }
};
}
extern "C" uint32_t kbcs_core_effect_create(double width,int32_t classic,const KbcsEffectSegment *segments,int32_t segment_count,
    const double *values,int32_t value_count,const int32_t *assets,const int32_t *lengths,int32_t asset_count,uint32_t seed,void **out){
  if(!out||!seed||!std::isfinite(width)||width<=0||width>10000000||segment_count<0||segment_count>2048||value_count<0||value_count>100000||asset_count<0||asset_count>8192||(segment_count&&!segments)||(value_count&&!values)||(asset_count&&(!assets||!lengths)))return 1;
  try{auto state=std::make_unique<Runtime>();width=std::max(1.,width*.4);state->width=width;state->classic=classic;state->seed=seed;
    if(segment_count)state->segments.assign(segments,segments+segment_count);
    if(value_count)state->values.assign(values,values+value_count);
    if(asset_count){state->assets.assign(assets,assets+asset_count);state->lengths.assign(lengths,lengths+asset_count);}
    for(double value:state->values)if(!std::isfinite(value)||std::abs(value)>1000000000)return 1;
    for(const auto &s:state->segments){
      if(s.first<0||s.count<1||int64_t(s.first)+s.count>asset_count)return 1;
      for(const auto &p:s.properties){
        if(p.kind<0||p.kind>3||p.group < -1||!std::isfinite(p.value)||!std::isfinite(p.low)||!std::isfinite(p.high)||std::abs(p.value)>1000000000||std::abs(p.low)>1000000000||std::abs(p.high)>1000000000)return 1;
        if(p.kind==3&&(p.first<0||p.count<1||int64_t(p.first)+p.count>value_count))return 1;
      }
    }
    state->minimum=std::min(1.,960/width);state->margin=960/state->minimum-width;
    state->top=std::ceil(40*state->minimum-20)+480-std::trunc(500/state->minimum);state->bottom=520+std::trunc(120/state->minimum);
    state->weather_top=-20*(100-state->minimum*100);state->weather_bottom=1300-std::trunc((100-state->minimum*100)*120/100);state->span=width+state->margin*2;
    state->reset();*out=state.release();return 0;
  }catch(int code){return uint32_t(code);}catch(...){return 3;}
}
extern "C" void kbcs_core_effect_destroy(void *handle){delete static_cast<Runtime*>(handle);}
extern "C" uint32_t kbcs_core_effect_frame(void *handle,int32_t frame,KbcsEffectParticle *output,int32_t capacity,int32_t *written){
  if(!handle||!output||!written||frame<0||frame>1000000||capacity<1||capacity>16384)return 1;
  auto &state=*static_cast<Runtime*>(handle);
  try{if(frame<state.frame)state.reset();while(state.frame<frame)state.update();
    std::vector<KbcsEffectParticle> result;
    for(const auto &p:state.particles)if(p.wait<=0)result.push_back(p.out);
    const int colors[7][3]={{255,255,255},{255,180,180},{180,255,180},{180,180,255},{255,255,180},{255,180,255},{180,255,255}};
    for(const auto &p:state.weather){KbcsEffectParticle command{};command.asset=-1;command.kind=p.kind;command.front=p.front;command.variant=p.variant;command.x=p.x;command.y=p.y;command.scale=p.size/100;command.sx=command.sy=1;command.alpha=255;std::fill_n(command.color,3,255);
      if(p.kind==1){std::copy_n(colors[state.classic==14?0:p.color],3,command.color);command.alpha=std::max(0.,std::sin(rad(p.age*.45)))*255;}
      if(p.kind==9||p.kind==10)command.x+=std::cos(rad(std::trunc(p.phase*p.velocity/100)))*p.amplitude*4/100;
      if(p.kind==3)command.x+=std::cos(rad(p.phase*18))*10;
      if(p.kind==4)command.x+=std::cos(rad(p.phase*3))*10;
      if(p.kind==6)command.alpha=50;
      if(p.kind==7){command.alpha=p.alpha;command.angle=60;}
      if(p.kind==8){command.alpha=(p.age<30?p.age/30:1)*255;command.angle=p.rotation;command.x+=4+(p.front?std::fmod(p.age,2)*2:0);}
      if(p.kind==5)command.scale=p.age<0?0:p.age<3?p.age/3:1-(p.age-3)/8;
      result.push_back(command);
    }
    if(result.size()>size_t(capacity))return 2;
    std::copy(result.begin(),result.end(),output);*written=int32_t(result.size());return 0;
  }catch(int code){return uint32_t(code);}catch(...){return 3;}
}
extern "C" uint32_t kbcs_core_weather_draw(const KbcsSceneLayout *layout,const KbcsEffectParticle *p,
    const KbcsRenderCut *cuts,int32_t count,const KbcsRenderCut *common,int32_t common_count,const int32_t *sizes,KbcsDrawCommand *output){
  if(!layout||!p||!sizes||!output||count<0||common_count<0||(count&&!cuts)||(common_count&&!common))return 1;
  const int layer=p->front?3:1;
  if(p->kind==1||p->kind==2){
    KbcsDrawCommand shape{-2,layer,p->kind==1?4:8,0,p->alpha/255.,{},{},{}};
    std::copy_n(p->color,3,shape.colors);
    if(p->kind==1){shape.points[3]=4;shape.points[4]=4;shape.points[5]=4;shape.points[6]=4;}
    else for(int i=0;i<8;++i){shape.points[i*2]=std::cos(i*pi/4)*12;shape.points[i*2+1]=std::sin(i*pi/4)*12;}
    return kbcs_core_scene_transform(layout,&shape,p->x,p->y,0,output);
  }
  KbcsRenderCut cut{};int texture=0;double w=0,h=0;
  if(p->kind==3||p->kind==9||p->kind==10){
    texture=p->kind==3?5:6;const int offset=p->kind==3?0:2;cut={0,0,sizes[offset],sizes[offset+1]};
    const double size=p->kind==3?1.8:p->scale;w=cut.width*size;h=cut.height*size;
  }else if(p->kind==6||p->kind==7){
    const int index=p->kind==7?29:28;if(index>=common_count){*output={};return 0;}cut=common[index];texture=7;w=cut.width;h=cut.height;
  }else{
    const int index=20+((p->kind==4||p->kind==8)?p->variant:0);if(index<0||index>=count){*output={};return 0;}
    cut=cuts[index];w=cut.width*p->scale;h=cut.height*p->scale;
  }
  if(w<=0||h<=0){*output={};return 0;}
  KbcsSpriteInput sprite{{p->x-(p->kind==4?w/2:0),p->y,w,h},p->angle,p->alpha/255.,texture,layer,p->kind==5?1:0,{cut.x,cut.y,cut.width,cut.height}};
  return kbcs_core_scene_sprite(layout,&sprite,output);
}
