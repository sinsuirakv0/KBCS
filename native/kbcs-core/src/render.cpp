#include "kbcs_core.h"
#include <algorithm>
#include <array>
#include <cmath>
#include <limits>
#include <vector>

extern "C" uint32_t kbcs_core_boss_effect_anchor(int32_t x,int32_t y,int32_t scale,int32_t offset_x,int32_t offset_y,int32_t out[2]){
 if(!out)return 1;
 out[0]=(x-scale*1180/100)/10+offset_x*scale/100+64;
 out[1]=y/10-scale*255/100+offset_y*scale/100+224;
 return 0;
}

namespace {
using I = int64_t;
I divide(I a,I b) { if (!b || (a==INT64_MIN && b==-1)) throw 1; return a/b; }
I product(I a,I b) {
  if (a && b && ((a>0 && b>0 && a>INT64_MAX/b) || (a<0 && b<0 && a<INT64_MAX/b) ||
      (a>0 && b<0 && b<INT64_MIN/a) || (a<0 && b>0 && a<INT64_MIN/b))) throw 2;
  return a*b;
}
I modulo(I n,I d) { return d ? (n%d+d)%d : 0; }
int32_t integer(double value) {
  if (!std::isfinite(value) || value<INT32_MIN || value>INT32_MAX) throw 2;
  return int32_t(value);
}
struct Part {
  std::array<I,13> base{},v{};
  I factor_x,factor_y,factor_alpha,sx=0,sy=0,alpha=0;
  bool flip_x=false,flip_y=false,local_x=false,local_y=false,done=false,visible=false;
  std::array<float,6> matrix{};
  std::array<int32_t,8> points{};
};
std::array<int32_t,2> point(const Part &p,I x,I y) {
  const auto &m=p.matrix;
  return {integer(float(double(m[2])+double(float(m[1]*float(y)))+double(float(m[0]*float(x))))),
          integer(float(double(m[5])+double(float(m[4]*float(y)))+double(float(m[3]*float(x)))))};
}
bool valid_parent(const std::vector<Part> &parts,int index,I parent) {
  if (parent<0 || parent>=I(parts.size()) || parent==index) return false;
  for (size_t depth=0;parent>=0;++depth) {
    if (depth>=parts.size() || parent>=I(parts.size()) || parent==index) return false;
    parent=parts[size_t(parent)].v[0];
  }
  return true;
}
I track_value(const KbcsRenderKey *keys,int count,I offset,I frame,bool &active) {
  active=count && frame>=I(keys[0].frame)+offset;
  if (!active) return 0;
  if (keys[0].frame==keys[count-1].frame) return keys[0].value;
  if (frame>=I(keys[count-1].frame)+offset) return keys[count-1].value;
  for (int i=0;i<count;++i) {
    const auto &a=keys[i]; const I first=I(a.frame)+offset;
    if (i+1==count || frame<first || frame>=I(keys[i+1].frame)+offset) continue;
    const auto &b=keys[i+1];
    if (a.easing==1) return a.value;
    if (a.easing==0) return I(a.value)+divide(product(I(b.value)-a.value,frame-first),I(b.frame)-a.frame);
    if (a.easing==2) {
      const double t=double(frame-first)/double(I(b.frame)-a.frame);
      const double eased=a.power<0 ? std::sqrt(1-std::pow(1-t,-double(a.power))) : 1-std::sqrt(1-std::pow(t,a.power));
      return integer(double(a.value)+(double(b.value)-a.value)*eased);
    }
    if (a.easing!=3) throw 1;
    int low=i,high=i;
    while (low>0 && keys[low-1].easing==3) --low;
    while (high<count-1) { ++high; if(keys[high].easing!=3) break; }
    I sum=0;
    for (int j=low;j<=high;++j) {
      I value=product(keys[j].value,4096);
      for (int k=low;k<=high;++k) if(k!=j)
        value=divide(product(value,frame-I(keys[k].frame)-offset),I(keys[j].frame)-keys[k].frame);
      if ((value>0 && sum>INT64_MAX-value) || (value<0 && sum<INT64_MIN-value)) throw 2;
      sum+=value;
    }
    return divide(sum,4096);
  }
  return 0;
}
}

static uint32_t pose(const KbcsPoseInput *in,const KbcsRenderPart *bases,int32_t count,
    const KbcsRenderCut *cuts,int32_t cut_count,const KbcsRenderTrack *tracks,int32_t track_count,
    const KbcsRenderKey *keys,int32_t key_count,KbcsPosePacket *output,int32_t *written,int32_t *contact) {
  if (!in || !bases || !cuts || !output || !written || count<1 || count>4096 || cut_count<1 || cut_count>8192 ||
      track_count<0 || track_count>32768 || key_count<0 || key_count>262144 || (track_count && !tracks) ||
      (key_count && !keys) || in->units[0]<=0 || in->units[1]<=0 || in->units[2]<=0 ||
      (in->facing!=1 && in->facing!=-1) || in->loop<0 || in->loop>1 || in->anchor<0 || in->anchor>2) return 1;
  try {
    const I su=in->units[0],ou=in->units[2];
    I maximum=1;
    for(int i=0;i<track_count;++i) {
      const auto &t=tracks[i];
      if(t.part<0 || t.part>=count || t.property<0 || t.property>14 || t.first<0 || t.count<0 || t.first>I(key_count)-t.count) return 1;
      if(!t.count) continue;
      const auto *k=keys+t.first; const I first=k[0].frame,last=k[t.count-1].frame;
      // 0044c884は原本順に区間を探索する。実素材にも逆順キーがあり、整列・拒否しない。
      const I offset=first<0 || t.loop!=1 ? -first : 0;
      const I end=t.loop==-1 ? last+offset-std::min<I>(offset,0) : t.loop>1 ? first+(last-first)*t.loop : last;
      maximum=std::max(maximum,end);
    }
    const I frame=in->loop ? modulo(in->frame,maximum+1) : in->frame;
    std::vector<Part> parts(size_t(count),Part{});
    for(int i=0;i<count;++i) {
      auto &p=parts[size_t(i)];
      std::copy_n(bases[i].cells,13,p.base.begin());
      if(i==0 && in->root_override) {
        p.base[8]=integer(float(float(in->root[0]*double(su))*in->root[1]));
        p.base[9]=integer(float(float(in->root[0]*double(su))*in->root[2]));
        p.base[10]=integer(float(float(in->root[3]*double(in->units[1]))/360.));
        p.base[11]=integer(float(float(in->root[4]*double(ou))/255.));
      }
      p.v=p.base;p.factor_x=su;p.factor_y=su;p.factor_alpha=ou;

    }
    for(int i=0;i<count;++i) if(parts[size_t(i)].v[0]<-1 || (parts[size_t(i)].v[0]>=0 && !valid_parent(parts,i,parts[size_t(i)].v[0]))) return 1;
    for(int i=0;i<track_count;++i) {
      const auto &t=tracks[i];if(!t.count)continue;
      const auto *k=keys+t.first;const I raw_first=k[0].frame,offset=raw_first<0 || t.loop!=1 ? -raw_first : 0;
      const I first=raw_first+offset,last=I(k[t.count-1].frame)+offset,length=last-first;
      I at=frame+offset;
      if(in->loop) at=modulo(at,t.loop==-1 ? last : maximum+1);
      else if(t.loop==-1 && at>=last && length) at=first+modulo(at-first,length);
      if(t.loop>0 && length) {
        const I end=first+length*t.loop;
        if(at>first && at<end)at=first+modulo(at-first,length);
        else if(at>=end)at=last;
      }
      bool active=false; const I value=track_value(k,t.count,offset,at,active);if(!active)continue;
      auto &p=parts[size_t(t.part)];const auto prop=t.property;
      if(prop==0)p.v[0]=valid_parent(parts,t.part,value)?value:(t.part==0?-1:0);
      else if(prop<=3)p.v[size_t(prop)]=value;
      else if(prop<=7)p.v[size_t(prop)]=p.base[size_t(prop)]+value;
      else if(prop==11)p.v[10]=p.base[10]+value;
      else if(prop==8)p.factor_x=p.factor_y=value;
      else if(prop==9)p.factor_x=value;
      else if(prop==10)p.factor_y=value;
      else if(prop==12)p.factor_alpha=value;
      else if(prop==13)p.local_x=value!=0;
      else if(prop==14)p.local_y=value!=0;
    }
    for(int i=0;i<count;++i) { auto &p=parts[size_t(i)];if(p.v[0]<-1 || p.v[0]>=count || (p.v[0]>=0&&!valid_parent(parts,i,p.v[0])))p.v[0]=i==0?-1:0; }
    int complete=0;
    while(complete<count) {
      bool progressed=false;
      for(auto &p:parts) {
        if(p.done || (p.v[0]>=0 && !parts[size_t(p.v[0])].done))continue;
        p.sx=divide(product(p.base[8],p.factor_x),su);p.sy=divide(product(p.base[9],p.factor_y),su);p.alpha=divide(product(p.base[11],p.factor_alpha),ou);
        if(p.v[0]<0) {
          p.sx*=in->facing;p.flip_x=p.local_x;p.flip_y=p.local_y;
          // 0044af4c: 根は位置の加算値だけを使い、モデルの基礎位置を含めない。
          p.matrix={1,0,float(p.v[4]-p.base[4]),0,1,float(p.v[5]-p.base[5])};
        } else {
          const auto &parent=parts[size_t(p.v[0])];
          p.sx=divide(divide(product(product(p.base[8],p.factor_x),parent.sx),su),su);
          p.sy=divide(divide(product(product(p.base[9],p.factor_y),parent.sy),su),su);
          p.alpha=divide(divide(product(product(p.base[11],p.factor_alpha),parent.alpha),ou),ou);
          p.flip_x=p.local_x!=parent.flip_x;p.flip_y=p.local_y!=parent.flip_y;p.matrix=parent.matrix;
          const float x=float(divide(product(parent.sx,p.v[4]),su)),y=float(divide(product(parent.sy,p.v[5]),su));
          p.matrix[2]=float(double(parent.matrix[2])+double(float(parent.matrix[1]*y))+double(float(parent.matrix[0]*x)));
          p.matrix[5]=float(double(parent.matrix[5])+double(float(parent.matrix[4]*y))+double(float(parent.matrix[3]*x)));
        }
        if(p.local_x)p.sx=-p.sx;if(p.local_y)p.sy=-p.sy;
        double angle=double(p.v[10])*6.283185307179586/double(in->units[1]);
        if(in->facing<0)angle=-angle;if(p.flip_x!=p.flip_y)angle=-angle;
        if(angle!=0) {
          const float sn=float(std::sin(double(float(angle)))),cs=float(std::cos(double(float(angle))));const auto m=p.matrix;
          p.matrix={float(float(sn*m[1])+float(m[0]*cs)),float(float(cs*m[1])-float(m[0]*sn)),m[2],
                    float(float(sn*m[4])+float(m[3]*cs)),float(float(cs*m[4])-float(m[3]*sn)),m[5]};
        }
        if(p.v[1]>=0 && p.v[2]>=0 && p.v[2]<cut_count) {
          const auto &cut=cuts[p.v[2]];
          const I left=divide(product(-p.sx,p.v[6]),su),top=divide(product(-p.sy,p.v[7]),su);
          const I right=left+divide(product(p.sx,cut.width),su),bottom=top+divide(product(p.sy,cut.height),su);
          const std::array<std::array<I,2>,4> corners{{{left,top},{left,bottom},{right,bottom},{right,top}}};
          for(int j=0;j<4;++j){const auto v=point(p,corners[size_t(j)][0],corners[size_t(j)][1]);p.points[size_t(j)*2]=v[0];p.points[size_t(j)*2+1]=v[1];}
          p.visible=true;
        }
        p.done=true;++complete;progressed=true;
      }
      if(!progressed)return 1;
    }
    if(contact) {
      const int index=std::max(0,in->config[0]);if(index>=count)return 1;const auto &p=parts[size_t(index)];
      // 0044b854の0x4c/0x54は原点の基礎値/加算値。位置ではない。
      const auto at=point(p,divide(product(I(in->config[2])-p.v[6],p.sx),su),divide(product(I(in->config[3])-p.v[7],p.sy),su));
      std::copy(at.begin(),at.end(),contact);return 0;
    }
    std::array<int32_t,2> anchor{};
    if(in->anchor) {
      const int index=std::max(0,in->config[0]);if(index>=count)return 1;const auto &p=parts[size_t(index)];
      anchor=point(p,divide(product(I(in->config[2])-p.v[6],p.sx),su),divide(product(I(in->config[3])-p.v[7],p.sy),su));
    }
    std::vector<int> order;for(int i=0;i<count;++i)order.push_back(i);
    std::sort(order.begin(),order.end(),[&](int a,int b){return parts[size_t(a)].v[3]*count+a<parts[size_t(b)].v[3]*count+b;});
    std::vector<KbcsPosePacket> packets;int blend=0;
    for(int i:order) {
      const auto &p=parts[size_t(i)];if(!p.visible)continue;
      if(p.v[12]>=0 && p.v[12]<4)blend=int(p.v[12]);
      const I alpha=divide(product(p.alpha,255),ou);if(!alpha)continue;
      KbcsPosePacket packet{i,int(p.v[2]),blend,std::clamp(double(alpha)/255.,0.,1.),{}};
      for(size_t j=0;j<8;++j)packet.points[j]=integer(double(p.points[j])-anchor[j%2]);packets.push_back(packet);
    }
    std::copy(packets.begin(),packets.end(),output);*written=int32_t(packets.size());return 0;
  } catch(int code) { return uint32_t(code); } catch(...) { return 3; }
}

extern "C" uint32_t kbcs_core_pose(const KbcsPoseInput *in,const KbcsRenderPart *parts,int32_t count,
 const KbcsRenderCut *cuts,int32_t cut_count,const KbcsRenderTrack *tracks,int32_t track_count,
 const KbcsRenderKey *keys,int32_t key_count,KbcsPosePacket *output,int32_t *written) {
 return pose(in,parts,count,cuts,cut_count,tracks,track_count,keys,key_count,output,written,nullptr);
}
extern "C" uint32_t kbcs_core_model_contact(const KbcsPoseInput *in,const KbcsRenderPart *parts,int32_t count,int32_t *out) {
 if(!out)return 1;const KbcsRenderCut cut{};KbcsPosePacket packet{};int32_t written=0;
 return pose(in,parts,count,&cut,1,nullptr,0,nullptr,0,&packet,&written,out);
}

extern "C" uint32_t kbcs_core_pose_contact(const KbcsPoseInput *in,const KbcsRenderPart *parts,int32_t count,
 const KbcsRenderTrack *tracks,int32_t track_count,const KbcsRenderKey *keys,int32_t key_count,int32_t *out) {
 if(!out)return 1;const KbcsRenderCut cut{};KbcsPosePacket packet{};int32_t written=0;
 return pose(in,parts,count,&cut,1,tracks,track_count,keys,key_count,&packet,&written,out);
}

extern "C" uint32_t kbcs_core_scene_layout(const KbcsSceneInput *in,KbcsSceneLayout *out) {
  if(!in||!out||!std::isfinite(in->width)||!std::isfinite(in->center)||!std::isfinite(in->zoom)||in->width<=0||in->width>10000000||in->cut_height<=0||in->cut_height>100000||in->focus<0||in->focus>4||in->viewport_width<0||in->viewport_width>3840||in->battle_rows<0||in->battle_rows>2)return 1;
  const double viewport=in->viewport_width?std::max(960,in->viewport_width):960;
  const double width=std::max(1.,in->width*.4),minimum=std::min(1.,viewport/width),zoom=in->focus==3?minimum:std::clamp(in->zoom,minimum,in->battle_rows?1.:2.);
  const double desired=in->focus==1?320:in->focus==2?width-320:in->focus==3?width/2:in->center;
  const double half=viewport*.5/zoom,center=in->focus==4?desired:width<=half*2?width/2:std::clamp(desired,half,width-half);
  const auto x=[&](double value){return viewport*.5+(value-center)*zoom;};
  // 005c8a6cは二段スロットの上端を超えた分もカメラへ戻す。
  const double anchor=in->battle_rows==2?505:520;
  double offset=in->battle_rows==2?-15:0;
  if(in->battle_rows){const int projected=int((1-zoom)*anchor+(500+offset)*zoom),slot=in->battle_rows==2?449:544;if(projected>slot)offset-=std::trunc((projected-slot)/zoom);}
  const auto y=[&](double value){return anchor+(value-anchor+offset)*zoom;};
  const int size=in->castle[2];if(size<0||size>100000)return 1;
  const double cx=std::trunc((3200-std::trunc(size*1180./100))/10)+std::trunc(size*double(in->castle[0])/100);
  const double cy=440-std::trunc(size*255./100)+std::trunc(size*double(in->castle[1])/100);
  *out={width,center,zoom,minimum,y(640-std::trunc(in->cut_height*640./510)),y(640),{x(cx),y(cy),std::trunc(size*127./100)*zoom,std::trunc(size*255./100)*zoom},x(width-320),viewport,anchor,offset};return 0;
}

extern "C" uint32_t kbcs_core_scene_transform(const KbcsSceneLayout *layout,const KbcsDrawCommand *in,
    double x,double y,double angle,KbcsDrawCommand *out) {
  if(!layout||!in||!out||in->count<3||in->count>8||!std::isfinite(x)||!std::isfinite(y)||!std::isfinite(angle))return 1;
  auto result=*in;const double radians=angle*3.141592653589793/180,sn=std::sin(radians),cs=std::cos(radians);
  for(int i=0;i<in->count;++i){const double px=in->points[i*2],py=in->points[i*2+1];
    result.points[i*2]=(layout->viewport_width?layout->viewport_width:960)*.5+(x+px*cs-py*sn-layout->center)*layout->zoom;
    result.points[i*2+1]=layout->y_origin+(y+px*sn+py*cs-layout->y_origin+layout->y_offset)*layout->zoom;
    if(!std::isfinite(result.points[i*2])||!std::isfinite(result.points[i*2+1]))return 2;
  }
  *out=result;return 0;
}
extern "C" uint32_t kbcs_core_scene_sprite(const KbcsSceneLayout *layout,const KbcsSpriteInput *in,KbcsDrawCommand *out) {
  if(!layout||!in||!out)return 1;
  KbcsDrawCommand command{in->texture,in->layer,4,in->blend,in->opacity,{0,0,0,in->rect[3],in->rect[2],in->rect[3],in->rect[2],0},{},{}};
  std::copy_n(in->cut,4,command.cut);
  return kbcs_core_scene_transform(layout,&command,in->rect[0],in->rect[1],in->angle,out);
}
extern "C" uint32_t kbcs_core_scene_paint(const KbcsPaintInput *in,KbcsSceneLayout *layout,KbcsDrawCommand *out,int32_t capacity,int32_t *written) {
  if(!in||!layout||!out||!written||capacity<1||capacity>16384)return 1;
  try {
  KbcsSceneLayout camera{};const auto code=kbcs_core_scene_layout(&in->scene,&camera);if(code)return code;
  if(in->cut[2]<=0||in->cut[3]<=0)return 1;
  std::vector<KbcsDrawCommand> commands;
  const auto gradient=[&](const int32_t *start,const int32_t *end,double top,double bottom,double alpha,int layer){
    if(bottom<=top)return;
    KbcsDrawCommand command{-1,layer,4,0,alpha,{0,top,0,bottom,camera.viewport_width,bottom,camera.viewport_width,top},{},{}};
    std::copy_n(start,3,command.colors);std::copy_n(end,3,command.colors+3);commands.push_back(command);
  };
  gradient(in->colors,in->colors+3,std::min(0.,camera.top-640*camera.zoom),std::max(0.,camera.top),1,0);
  gradient(in->colors+6,in->colors+9,std::max(0.,camera.bottom),in->scene.battle_rows?680:640,1,0);
  const double left=camera.center-camera.viewport_width*.5/camera.zoom,right=camera.center+camera.viewport_width*.5/camera.zoom;
  const auto sprite=[&](int texture,int layer,const int32_t *cut,double x,double y,double w,double h){
    KbcsSpriteInput source{{x,y,w,h},0,1,texture,layer,0,{}};std::copy_n(cut,4,source.cut);
    KbcsDrawCommand command{};
    if(kbcs_core_scene_sprite(&camera,&source,&command)==0)commands.push_back(command);
  };
  const double height=std::trunc(in->cut[3]*640./510);
  for(double x=std::floor(left/960)*960;x<right;x+=960){
    if(commands.size()>size_t(capacity))return 2;
    if(in->top[2]>0)sprite(0,0,in->top,x,-640,960,640);
    sprite(0,0,in->cut,x,640-height,960,height);
  }
  if(in->show_enemy){
    const double size=in->scene.castle[2];const int32_t cut[4]={0,0,-1,-1};
    sprite(1,2,cut,std::trunc((3200-std::trunc(size*1180/100))/10)+std::trunc(size*in->scene.castle[0]/100),440-std::trunc(size*255/100)+std::trunc(size*in->scene.castle[1]/100),std::trunc(size*127/100),std::trunc(size*255/100));
  }
  if(in->show_player)for(int i=0;i<3;++i){
    if(in->self_sizes[i*2]<=0||in->self_sizes[i*2+1]<=0)continue;
    const int32_t cut[4]={0,0,in->self_sizes[i*2],in->self_sizes[i*2+1]};
    sprite(2+i,2,cut,camera.width-320,i==2?117:280,std::trunc(cut[2]*1.27),std::trunc(cut[3]*1.27));
  }
  if(in->overlay[6]>=0)gradient(in->overlay,in->overlay+3,0,640,double(in->overlay[6])/255,4);
  if(commands.size()>size_t(capacity))return 2;
  std::copy(commands.begin(),commands.end(),out);*written=int32_t(commands.size());*layout=camera;return 0;
  } catch(...) { return 3; }
}

extern "C" uint32_t kbcs_core_scene_instance(const KbcsSceneLayout *layout,const KbcsDrawCommand *input,double x,double y,double spacing,int32_t index,KbcsDrawCommand *output) {
  return kbcs_core_scene_transform(layout,input,x+spacing*index,y,0,output);
}
