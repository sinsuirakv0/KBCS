#include "kbcs_actor.h"
#include <algorithm>
#include <cstdint>
#include <cmath>

namespace {
using I = int64_t;
int width(const KbcsBattleScreenConfig &c){return c.viewport_width?c.viewport_width:960;}
int press(int counter){const int sizes[6]={0,0,6,-10,0,0};return sizes[counter];}
void toggle_speed(const KbcsBattleScreenConfig &c,KbcsBattleScreenState &s){s.speed_mode=(s.speed_mode+1)%(c.speed==3?3:2);if(s.speed_mode)s.items_on|=1;else s.items_on&=~1;}
void change_page(KbcsBattleScreenState &s,int direction){if(s.rows!=1)return;if(!s.page_frame){s.page_frame=1;s.page_direction=direction;s.page_step=1;}else if(s.page_direction!=direction){s.page_step=-1;}s.holding=-1;s.hold_frames=0;s.gesture=1;}
int wallet(const KbcsBattleScreenConfig &c,int worker) {
 if(c.fixed_money>=0)return c.fixed_money;
 return int(((I(worker*5+10)*(c.wallet_level+1)*1000+c.wallet_treasure)*(100+c.wallet_combo))/100);
}
int income(const KbcsBattleScreenConfig &c,int worker) {
 return int(((I(worker+10)*(c.worker_level*10+25)/10+c.income_treasure)*(100+c.income_combo))/100);
}
int upgrade(const KbcsBattleScreenConfig &c,int worker) {
 const int base=c.worker_level<7?4000+c.worker_level*1000:-2000+c.worker_level*2000;
 return base*(worker+1);
}
int charge(const KbcsBattleScreenConfig &c) {
 return std::max(950,(std::max(0,c.attack_level*50-c.speed_treasure)+std::min(c.chapter,3)*450-c.charge_level*50-c.charge_treasure+1500)*(100-c.charge_combo)/100);
}
bool inside(int x,int y,int left,int top,int width,int height) {
 // 009a6f44の左上を含み右下も含む矩形判定。
 return left<=x&&x<=left+width&&top<=y&&y<=top+height;
}
void layout(const KbcsBattleScreenConfig &c,const KbcsBattleScreenState &s,KbcsBattleScreenLayout &o) {
 const int xs[10]={159,289,419,549,679,171,301,431,561,691};
 const int screen=width(c),center=screen/2,shift=(screen-960)/2;
 o.scene_y=s.rows==2?-51:0;o.wallet_max=wallet(c,s.worker);o.income=income(c,s.worker);o.upgrade_cost=upgrade(c,s.worker);o.cannon_max=charge(c);o.cannon_initial=o.cannon_max*(100-c.charge_start_combo)/100;o.cannon_gauge=(o.cannon_max-s.cannon)*130/o.cannon_max;
 o.money_base=s.wallet_flash%4==1||s.wallet_flash%4==2?68:0;o.speed_value=s.speed_mode?s.speed_mode+1:1;
 const bool flash=s.hud_frame%6>=3;o.cannon_base=s.cannon?8:flash?7:-1;o.cannon_label=s.cannon?-1:flash?10:9;o.cannon_bands=s.cannon?o.cannon_gauge/13:flash?0:10;o.wallet_base=s.worker==7||s.money>=o.upgrade_cost?6:5;
 for(int i=0;i<10;++i) {
  int x=xs[i]+shift,y=544,mode=1;
  if(s.rows==2) {x=xs[i%5]+shift;if(i<5)y-=95;}
  else if(s.page_frame) {
   const int wave[6]={0,20,40,80,40,20};
   const int sign=s.page_direction==0?-1:1,offset=wave[s.page_frame]*sign;
   y+=(i<5?(s.page==0?offset:-offset):(s.page==0?-offset:offset));mode=2;
  } else if(i/5!=s.page){y+=12;mode=2;}
  o.labels[i][0]=x;o.labels[i][1]=y;
  if(s.guard&&s.pending_control==i&&mode==1){const int sizes[6]={0,0,6,-10,0,0};const int z=sizes[s.guard];x-=z/2;y-=z/2;o.slots[i][2]=110+z;o.slots[i][3]=85+z;}else{o.slots[i][2]=110;o.slots[i][3]=85;}
  o.slots[i][0]=x;o.slots[i][1]=y;o.modes[i]=mode;
 }
 const int front=s.page_frame>=4?1-s.page:s.page;
 for(int i=0;i<10;++i)o.order[i]=s.rows==2?i:(i<5?(1-front)*5+i:front*5+i-5);
 int position=5;
 for(int id=5;id>=0;--id){if(!(c.items&(1<<id)))continue;const int z=s.guard&&s.pending_control==200+id?press(s.guard):0;const bool boosted=id==0&&s.speed_mode==2;const int size=boosted?80:58;
  int *icon=o.item_icons[id];icon[0]=id+((s.items_on&(1<<id))?0:6);if(boosted)icon[0]=16;icon[1]=screen+position*88-(boosted?524:513)-z/2;icon[2]=(boosted?47:58)-z/2;icon[3]=icon[4]=size+z;--position;}
 const int pz=s.guard&&s.pending_control==100?press(s.guard):0;o.pause_icon[0]=4-pz/2;o.pause_icon[1]=4-pz/2;o.pause_icon[2]=o.pause_icon[3]=58+pz;
 if(s.description_item>=0&&s.description_wait){int *box=o.description_box;box[0]=screen-718;box[1]=134;box[2]=710;box[3]=159;int position=5;for(int id=5;id>s.description_item;--id)if(c.items&(1<<id))--position;const int x=screen+position*88;o.description_arrow[0]=x-484;o.description_arrow[1]=118;o.description_arrow[2]=x-469;o.description_arrow[3]=134;o.description_arrow[4]=x-499;o.description_arrow[5]=134;}
 // 008f9e20/008fb5f4: 二段切替を持つ戦闘オプションの原本矩形。
 const int controls[8][5]={{300,center+174,108,96,96},{301,center-200,242,171,52},{304,center-5,242,52,52},{305,center+60,242,52,52},{306,center+125,242,52,52},{303,center-23,316,169,48},{302,center-158,397,315,61},{307,center-461,566,128,63}};
 for(int i=0;i<8;++i)std::copy_n(controls[i],5,o.controls[i]);
 auto sprite=[&](int atlas,int cut,int x,int y,int w,int h){int *p=o.menu_sprites[o.menu_count++];p[0]=atlas;p[1]=cut;p[2]=x;p[3]=y;p[4]=w;p[5]=h;};
 if(s.paused&&!s.info_mode){
  sprite(0,53,center-198,215,406,191);sprite(0,79,center-198,142,406,93);sprite(0,49,center-198,382,391,91);sprite(0,52,center-232,215,39,191);sprite(0,80,center-232,142,164,93);sprite(0,48,center-232,382,164,91);sprite(0,52,center+232,215,-39,191);sprite(0,78,center+190,142,42,93);sprite(0,51,center+190,382,42,91);sprite(0,16,center-87,158,179,49);sprite(0,75,center-147,324,114,31);
  for(const auto &r:controls){const int action=r[0],x=r[1],y=r[2],w=r[3],h=r[4];const bool active=s.guard&&s.pending_control==action;const int blink=active?1+(s.ui_frame/2)%2:0;
   if(action==300)sprite(0,21+blink,x,y,w,h);
   else if(action==301){sprite(0,74,x,y,w,h);sprite(0,73,x+(w-129)/2,y+(h-35)/2,129,35);if(blink)sprite(0,blink==1?30:31,x,y,w,h);}
   else if(action==302){sprite(0,6,x,y,w,h);sprite(0,10,x+(w-155)/2,y+(h-45)/2,155,45);if(blink)sprite(0,blink==1?17:18,x,y,w,h);}
   else if(action==303)sprite(0,s.rows==2?77:76,x,y,w,h);
   else if(action==304){const int cuts[4]={5,97,96,4};sprite(0,cuts[s.bgm_level],x,y,w,h);}
   else if(action==305){const int cuts[4]={8,95,94,7};sprite(0,cuts[s.se_level],x,y,w,h);}
   else if(action==306)sprite(0,107,x,y,w,h);
   else if(action==307){sprite(1,339,x,y,w,h);sprite(1,343,x+8,y+14,112,34);}
  }
 }
 if(s.info_mode){o.info_box[0]=center-473;o.info_box[1]=93;o.info_box[2]=946;o.info_box[3]=180+39*c.description_lines[s.info_slot];}
 if(s.intro>=24)return;
 auto triangle=[&](int x0,int y0,int x1,int y1,int x2,int y2){const int i=o.fade_count++;o.fade_sizes[i]=3;int *p=o.fade[i];p[0]=x0;p[1]=y0;p[2]=x1;p[3]=y1;p[4]=x2;p[5]=y2;};
 auto rect=[&](int x,int width){const int i=o.fade_count++;o.fade_sizes[i]=4;int *p=o.fade[i];p[0]=x;p[1]=0;p[2]=x;p[3]=640;p[4]=x+width;p[5]=640;p[6]=x+width;p[7]=0;};
 // 006994e8: 11/12Fで全面を覆い、13Fから右側を露出する。
 if(s.intro==11||s.intro==12){rect(0,screen);return;}
 if(s.intro<11){const int x=screen-screen*s.intro/10;for(int y=-384;y!=1196;y+=158)triangle(x-110,y+55,x,y,x,y+110);for(int y=-274;y!=1306;y+=158)triangle(x-55,y+24,x,y,x,y+48);rect(x,screen*2);}
 else {const int delta=screen*(s.intro-1)/10,x=screen*2-delta;for(int y=-384;y!=1196;y+=158)triangle(x+220,y+55,x+110,y,x+110,y+110);for(int y=-274;y!=1306;y+=158)triangle(x+165,y+24,x+110,y,x+110,y+48);rect(screen-delta,screen+110);}
}
int hit(const KbcsBattleScreenConfig &c,const KbcsBattleScreenState &s,int x,int y) {
 const int xs[10]={159,289,419,549,679,171,301,431,561,691};
 if(s.info_mode){if(inside(x,y,width(c)/2-461,566,128,63))return 308;}
 if(s.paused&&!s.info_mode){KbcsBattleScreenLayout o{};layout(c,s,o);for(const auto &r:o.controls)if(inside(x,y,r[1],r[2],r[3],r[4]))return r[0];return -1;}
 if(inside(x,y,0,0,88,88))return 100;
 if(inside(x,y,width(c)-146,510,194,130))return 101;
 if(inside(x,y,-48,519,194,125))return 102;
 int position=5;for(int id=5;id>=0;--id){if(!(c.items&(1<<id)))continue;if(inside(x,y,width(c)+position*88-528,43,88,88))return 200+id;--position;}
 if(s.page_frame)return -1;
 for(int i=0;i<(s.rows==2?10:5);++i){int slot=s.rows==2?i:s.page*5+i,top=544-(s.rows==2&&i<5?95:0);if(inside(x,y,xs[s.rows==2?i%5:slot]+(width(c)-960)/2,top-1,110,88))return slot;}
 return -1;
}
}
extern "C" void kbcs_core_battle_screen_economy(const KbcsBattleScreenConfig *config,KbcsBattleScreenState *state){
 if(!state->battle_mode){if(config->fixed_money<0)state->money=std::min(wallet(*config,state->worker),state->money+income(*config,state->worker));if(state->cannon>0)--state->cannon;}
}
extern "C" uint32_t kbcs_core_battle_screen_advance(const KbcsBattleScreenConfig *config,const KbcsBattleScreenState *state,const KbcsBattleScreenInput *input,KbcsBattleScreenState *out,KbcsBattleScreenLayout *view,KbcsBattleScreenHook hook,void *user) {
 if(!config||!state||!input||!out||!view)return 1;
 const auto &c=*config;auto s=*state;const auto &in=*input;
 // ホストのコマ送りは速度アイテムを保持し、1更新を1論理Fとして進める。
 const bool stepping=in.control==10;
 if(stepping&&(s.paused||s.intro<24||in.phase||in.ticks<1))return 1;
 if(c.worker_level<0||c.worker_level>29||c.wallet_level<0||c.wallet_level>29||c.attack_level<0||c.attack_level>29||c.charge_level<0||c.charge_level>29||c.chapter<0||c.chapter>3||c.income_treasure<0||c.income_treasure>10000||c.wallet_treasure<0||c.wallet_treasure>10000000||c.charge_treasure<0||c.charge_treasure>10000||c.speed_treasure<0||c.speed_treasure>10000||c.income_combo<0||c.income_combo>1000||c.wallet_combo<0||c.wallet_combo>1000||c.charge_combo<0||c.charge_combo>100||c.charge_start_combo<0||c.charge_start_combo>100||c.items<0||c.items>63||c.speed<2||c.speed>3||c.fixed_money< -1||c.fixed_money>1000000000||s.frame<0||s.frame>100000000||s.intro<0||s.intro>24||s.rows<1||s.rows>2||s.page<0||s.page>1||s.page_frame<0||s.page_frame>5||s.page_direction<0||s.page_direction>1||s.paused<0||s.paused>1||s.money<0||s.money>1000000000||s.worker<0||s.worker>7||s.cannon<0||s.cannon>100000||s.holding< -1||s.holding>9||s.pointer_down<0||s.pointer_down>1||s.items_on<0||s.items_on>63||(s.items_on&~c.items)||s.hold_frames<0||s.hold_frames>100000||s.guard<0||s.guard>5||s.pending_control< -1||s.pending_control>308||in.ticks<0||in.ticks>30||in.phase<0||in.phase>4||in.control<0||in.control>10||c.viewport_width<0||c.viewport_width>3840||s.speed_mode<0||s.speed_mode>2||s.wallet_flash<0||s.wallet_flash>14||s.description_item< -1||s.description_item>5||s.description_wait<0||s.description_wait>5||s.ui_frame<0||s.ui_frame>100000000||s.gesture<0||s.gesture>1||s.page_step< -1||s.page_step>1||s.bgm_level<0||s.bgm_level>3||s.se_level<0||s.se_level>3||s.vibration_on<0||s.vibration_on>1||s.info_mode<0||s.info_mode>1||s.info_slot<0||s.info_slot>9||s.saved_rows<0||s.saved_rows>2||s.hud_frame<0||s.hud_frame>100000000)return 1;
 for(int i=0;i<10;++i)if(c.costs[i]<0||c.costs[i]>10000000||c.present[i]<0||c.present[i]>1||c.blocked[i]<0||c.description_lines[i]<0||c.description_lines[i]>3)return 1;
 s.request_slot=-1;s.request_cannon=0;s.request_action=0;
 const auto sound=[&](int id){return hook?hook(user,KBCS_BATTLE_SCREEN_SOUND+id,&s):0;};
 if(in.control==1){if(s.info_mode){s.info_mode=0;s.rows=s.saved_rows?s.saved_rows:2;}s.paused=0;}
 if(in.control==2){s.paused=1;s.pointer_down=0;s.holding=-1;s.hold_frames=0;}
 if(in.control==3){s.rows=3-s.rows;s.page_frame=0;s.pointer_down=0;s.holding=-1;s.hold_frames=0;}
 if(in.control==4)change_page(s,1);
 if(in.control==8)change_page(s,0);
 if(in.control==9)change_page(s,1);
 if(in.control==5&&(c.items&1))toggle_speed(c,s);
 if(in.control==6&&(c.items&8))s.items_on^=8;
 if(in.control==7&&(c.items&32))s.items_on^=32;
 for(int tick=0;tick<in.ticks;++tick){
  const int previous_target=s.pointer_down?hit(c,s,s.pointer_x,s.pointer_y):-1;
  ++s.ui_frame;
  if(s.wallet_flash&&!s.paused)--s.wallet_flash;
  if(s.intro<24){++s.intro;continue;}
  if(s.battle_mode){s.speed_mode=0;s.pointer_down=0;s.holding=-1;s.hold_frames=0;s.guard=0;s.pending_control=-1;}
  if(hook&&!s.paused){const auto code=hook(user,4,&s);if(code)return code;}
  if(s.page_frame&&!s.paused&&!(tick==0&&(in.control==4||in.control==8||in.control==9))){s.page_frame+=s.page_step?s.page_step:1;if(s.page_frame>5){s.page=1-s.page;s.page_frame=0;}else if(s.page_frame<1)s.page_frame=0;}
  if(tick==0&&in.phase){s.pointer_x=in.x;s.pointer_y=in.y;if(in.phase==1){s.pointer_down=1;s.start_x=in.x;s.start_y=in.y;s.gesture=0;}}
  if(!s.paused){++s.hud_frame;const int steps=stepping?1:s.speed_mode?s.speed_mode+1:1;
   for(int i=0;i<steps;++i){++s.frame;if(hook){const auto code=hook(user,0,&s);if(code)return code;}else kbcs_core_battle_screen_economy(&c,&s);}}
  // 006d6d04: 経済は論理更新、ボタンの待機は表示更新で一度だけ進める。
  if(s.guard){if(++s.guard>5){s.guard=0;const int target=s.pending_control;s.pending_control=-1;
    if(target>=0&&target<10&&c.present[target]&&!c.blocked[target]&&(hook||I(c.costs[target])*100<=s.money)){s.request_slot=target;if(hook){const auto code=hook(user,1,&s);if(code)return code;}}
    else if(target==200)toggle_speed(c,s);
    else if(target==203||target==205)s.items_on^=1<<(target-200);
    else if(target==100)s.paused=1;
    else if(target==300)s.paused=0;
    else if(target==301||target==302)s.request_action=target;
    else if(target==307){s.info_mode=1;s.saved_rows=s.rows;s.rows=2;s.page_frame=0;s.info_slot=0;}
    else if(target==308){s.info_mode=0;s.rows=s.saved_rows?s.saved_rows:2;s.paused=0;}
    else if(target==303){s.rows=3-s.rows;s.page_frame=0;}


   }if(tick==0&&(in.phase==2||in.phase==3))s.pointer_down=0;if(s.description_wait)--s.description_wait;if(hook){const auto code=hook(user,5,&s);if(code)return code;}continue;}
  if(!s.paused&&hook){const auto code=hook(user,3,&s);if(code)return code;}
  int target=hit(c,s,s.pointer_x,s.pointer_y);
  // 006dca34..006dcf80 / オプションのcallback event0。押し直し・領域への再進入だけ。
  const bool press_sound=(target>=0&&target<10)||(target>=100&&target<=102)||(target>=300&&target<=308&&target!=306);
  if(!s.battle_mode&&s.pointer_down&&!s.gesture&&press_sound&&(target!=previous_target||(tick==0&&in.phase==1))){
   const auto code=sound(10);if(code)return code;
  }
  if(s.pointer_down&&!s.paused&&target>=200&&target<=205){s.description_item=target-200;s.description_wait=5;}
  // 009f4228: 縦変位25px以上、上225度超315度未満/下45〜135度。
  if(s.pointer_down&&!s.paused&&s.rows==1&&!s.gesture&&s.hold_frames<14&&s.description_wait==0){
   const int dx=s.pointer_x-s.start_x,dy=s.pointer_y-s.start_y;
   double angle=std::atan2(double(dy),double(dx))*180/3.141592653589793;if(angle<0)angle+=360;
   const int direction=int(angle);
   if((dy< -24&&direction>224&&direction<316)||(dy>24&&direction>=45&&direction<=135))change_page(s,dy>0?1:0);
  }
  if(tick==0&&in.phase==2){
   if(s.paused){if(s.info_mode&&target>=0&&target<10&&c.present[target])s.info_slot=target;if(target>=300&&target!=306){
     // 008ff260/008ff388はrelease時に音量を変え、その音量でSE11を鳴らす。
     if(target==304)s.bgm_level=(s.bgm_level+1)%4;
     if(target==305)s.se_level=(s.se_level+1)%4;
     const auto code=sound(11);if(code)return code;s.pending_control=target;s.guard=1;
    }}
   else if(!s.gesture&&!s.battle_mode){
    if(target==100||target==200||target==203||target==205){const auto code=sound(11);if(code)return code;s.pending_control=target;s.guard=1;}
    if(target==101){s.request_cannon=1;if(hook){const auto code=hook(user,2,&s);if(code)return code;}}
    if(target==102){const bool allowed=s.worker<7&&s.money>=upgrade(c,s.worker);if(allowed){s.money-=upgrade(c,s.worker);++s.worker;s.wallet_flash=13;}const auto code=sound(allowed?19:15);if(code)return code;}
    if(target>=0&&target<10&&s.hold_frames<14){s.pending_control=target;s.guard=1;}
   }
   s.pointer_down=0;s.holding=-1;s.hold_frames=0;
  }else if(tick==0&&in.phase==3){s.pointer_down=0;s.holding=-1;s.hold_frames=0;}
  if(s.pointer_down&&!s.paused&&!s.gesture&&target>=0&&target<10){if(s.holding!=target){s.holding=target;s.hold_frames=0;}else s.hold_frames=std::min(14,s.hold_frames+1);}
  if(s.description_wait)--s.description_wait;
  if(hook){const auto code=hook(user,5,&s);if(code)return code;}

 }
 KbcsBattleScreenLayout result{};layout(c,s,result);*out=s;*view=result;return 0;
}

extern "C" uint32_t kbcs_core_battle_screen_step(const KbcsBattleScreenConfig *config,const KbcsBattleScreenState *state,const KbcsBattleScreenInput *input,KbcsBattleScreenState *out,KbcsBattleScreenLayout *view){
 return kbcs_core_battle_screen_advance(config,state,input,out,view,nullptr,nullptr);
}
