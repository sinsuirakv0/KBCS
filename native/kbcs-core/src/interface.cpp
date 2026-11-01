#include "kbcs_interface.h"
#include <algorithm>
#include <vector>
#include "interface_data.inc"

namespace {
bool active(const KbcsComboDefinition &combo,const KbcsComboSelection &selection){
 for(int i=0;i<5&&combo.units[i]>=0;++i){bool found=false;for(int j=0;j<5;++j)if(selection.team[j]==combo.units[i]&&selection.forms[j]>=combo.forms[i])found=true;if(!found)return false;}return true;
}
}
// 00893ea0→00895118。コンボを構成する既存キャラの個別設定は呼出側が移動する。
extern "C" uint32_t kbcs_core_combo_plan(const KbcsComboDefinition *combos,int32_t count,const KbcsComboSelection *input,KbcsComboPlan *out){
 if(!combos||!input||!out||count<1||count>4096||input->selected<0||input->selected>=count)return 1;
 for(int i=0;i<10;++i)if(input->team[i]<-1||input->team[i]>100000||input->forms[i]<0||input->forms[i]>3||input->locked[i]<0||input->locked[i]>1)return 1;
 for(int i=0;i<count;++i)for(int j=0;j<5;++j)if(combos[i].units[j]<-1||combos[i].units[j]>100000||combos[i].forms[j]<0||combos[i].forms[j]>3)return 1;
 try{
  std::vector<int> order;
  for(int slot=0;slot<5;++slot)for(int i=0;i<count;++i)if(active(combos[i],*input)&&std::find(combos[i].units,combos[i].units+5,input->team[slot])!=combos[i].units+5&&input->team[slot]>=0)order.push_back(i);
  // 0089c2ecは右端までのrotate。等しいコンボの出現を隣接させる。
  for(size_t i=0;i<order.size();++i)for(size_t j=i+1;j-->0;)if(order[i]==order[j])std::rotate(order.begin()+j,order.begin()+j+1,order.begin()+i+1);
  std::vector<int> first;int previous=-1,member=0;
  for(int id:order){if(previous!=id)member=0;const int unit=combos[id].units[member++];if(std::find(first.begin(),first.end(),unit)==first.end())first.push_back(unit);previous=id;}
  for(int i=0;i<5;++i){const int unit=input->team[i];if(std::find(first.begin(),first.end(),unit)==first.end()&&!(unit<0&&!first.empty()))first.push_back(unit);}
  const auto &selected=combos[input->selected];
  for(int i=0;i<5&&selected.units[i]>=0;++i){std::erase(first,selected.units[i]);first.insert(first.begin()+i,selected.units[i]);}
  for(size_t i=first.size();i-->0&&first.size()>5;){bool locked=false;for(int slot=0;slot<10;++slot)if(input->team[slot]==first[i]&&input->locked[slot])locked=true;if(!locked)first.erase(first.begin()+i);}
  if(first.size()>5)return 1;
  KbcsComboPlan result;std::fill_n(result.first,5,-1);std::fill_n(result.slots,10,-1);
  for(size_t i=0;i<first.size();++i)result.first[i]=first[i];
  // 原本は10枠内の重複を除いて1行目を上書きし、空欄を詰め直す。
  std::vector<int> remaining(input->team,input->team+10);
  for(int unit:first)std::replace(remaining.begin(),remaining.end(),unit,-1);
  for(size_t i=0;i<first.size();++i)remaining[i]=first[i];
  std::erase(remaining,-1);std::copy(remaining.begin(),remaining.end(),result.slots);
  *out=result;return 0;
 }catch(...){return 3;}
}
// 005d5afc / 005d63f8。0080dd1cの定数002b0c00は30,120,192,6。
extern "C" uint32_t kbcs_core_combo_intro(int32_t frame,int32_t width,int32_t count,const int32_t *groups,KbcsComboIntro *out){
 if(!out||frame<0||frame>100000000||width<640||width>3840||count<0||count>4096||(!groups&&count))return 1;
 KbcsComboIntro result{};result.index=-1;result.blink=frame%4;
 if(frame>=30){const int elapsed=frame-30,index=elapsed/120,age=elapsed%120+1;if(index<count&&age<120){
  result.index=index;result.age=age;const int open=std::min(6,age),offset=(age>=6?groups[index]!=-1:index>0&&groups[index-1]!=-1)?-15:0;
  result.band[0]=0;result.band[1]=160+offset-open*10;result.band[2]=width;result.band[3]=open*20+(offset?30:0);
  result.text_x=std::min(width,std::max(0,age-5)*192)-width/2;
  result.text_y[0]=110+offset;result.text_y[1]=170+offset;result.text_y[2]=200+offset;
  result.skip[0]=width-87;result.skip[1]=194-offset;
 }}
 *out=result;return 0;
}
extern "C" uint32_t kbcs_core_combo_row(int32_t width,int32_t row,int32_t grouped,KbcsComboRow *out){
 if(!out||width<960||width>3840||row<0||row>3||grouped<0||grouped>1)return 1;
 KbcsComboRow result{};const int x=int(width*0.5-440),y=136+row*100;
 result.panel[0]=x;result.panel[1]=y;result.panel[2]=880;result.panel[3]=90;
 result.name[0]=result.effect[0]=result.group[0]=x+190;result.name[1]=y+(grouped?5:14);result.effect[1]=result.name[1]+(grouped?30:34);result.group[1]=y+60;
 for(int i=0;i<5;++i){auto &icon=result.icons[i];icon[0]=x+380+i*96;icon[1]=y+12;icon[2]=88;icon[3]=68;}
 *out=result;return 0;
}
// 0088627c / 00886068 / 00886a84。type1、flags0x8cの確認窓。
extern "C" uint32_t kbcs_core_combo_dialog(int32_t width,int32_t phase,KbcsComboDialog *out){
 if(!out||width<960||width>3840||phase<0||phase>4)return 1;
 constexpr int scales[5]={0,50,80,90,100};const int scale=scales[phase],center=width/2;
 KbcsComboDialog result{{center-354*scale/100,280-221*scale/100,709*scale/100,442*scale/100},{center-84,509,168,72},{center+319,23,72,72}};
 *out=result;return 0;
}
// 006a4e9c。戦闘の画面種別0では図鑑専用の半透明矢印を描かない。
extern "C" uint32_t kbcs_core_unit_info(const KbcsUnitInfoInput *input,KbcsUnitInfoLayout *out){
 if(!input||!out||input->center< -3840||input->center>3840||input->y<0||input->y>640||input->form<0||input->form>3||input->orbs<0||input->orbs>8)return 1;
 const auto &in=*input;for(int i=0;i<88;++i)if(in.abilities[i]<0||in.abilities[i]>1||in.talents[i]<0||in.talents[i]>2)return 1;
 for(int i=0;i<10;++i)if(in.attributes[i]<0||in.attributes[i]>1||in.new_attributes[i]<0||in.new_attributes[i]>1)return 1;
 KbcsUnitInfoLayout result{};
 const auto sprite=[&](int cut,int x,int y,int tint=255){auto &v=result.sprites[result.count++];v[0]=cut;v[1]=x;v[2]=y;v[3]=tint;};
 const int center=in.center,y=in.y,orb_count=in.form>=2?in.orbs:0;
 int effects=0,abilities=0;bool all=true;for(int v:in.attributes)all&=v!=0;
 for(int i=0;i<88;++i)if(in.abilities[i]){effects+=infoAbilities[i][1]==0;abilities+=infoAbilities[i][1]==1;}
 const int half=(abilities*42-2)>>1,offset=abilities>=6?(abilities*42-210)>>1:0;
 const bool full=effects>0||all;int base=0,ability_y=0;
 if(full){
  for(int i=0;i<10;++i){sprite(77+i,center-394+i*43,y,in.attributes[i]?255:128);if(in.new_attributes[i])sprite(271,center-394+i*43,y);}
  sprite(249,center+113,y+1);int index=0;
  for(int order=0;order<88;++order)for(int i=0;i<88;++i)if(in.abilities[i]&&infoAbilities[i][0]==order&&infoAbilities[i][1]==0){const int x=center+189+index++*42;sprite(infoAbilities[i][2],x,y-1);if(in.form>=2&&in.talents[i])sprite(271+in.talents[i],x,y-2);}
  const int orb_half=orb_count?(orb_count*51+117)>>1:0,label=center-half-orb_half-39;sprite(252,label,y+56);base=offset-half+label+182;ability_y=y+54;
 }else{const int label=center-half-39,top=y+(orb_count?1:26);sprite(252,label,top);base=label-half+offset+182;ability_y=top-2;}
 int index=0;
 for(int order=0;order<88;++order)for(int i=0;i<88;++i)if(in.abilities[i]&&infoAbilities[i][0]==order&&infoAbilities[i][1]==1){const int x=base+index++*42;sprite(infoAbilities[i][2],x,ability_y);if(in.form>=2&&in.talents[i])sprite(271+in.talents[i],x,full?y+54:ability_y-1);}
 if(orb_count){
  const int label=full?base+abilities*42+26:center-((orb_count*51+117)>>1);sprite(290,label,y+(full?54:56));result.orb_count=orb_count;
  for(int i=0;i<orb_count;++i){const int x=label+113+i*51-23,top=y+(full?51:53);sprite(291,x,top);result.orbs[i][0]=x;result.orbs[i][1]=top;}
 }
 *out=result;return 0;
}
