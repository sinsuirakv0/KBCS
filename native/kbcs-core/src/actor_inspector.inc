// KBCS専用の観測記録。ゲーム状態・乱数を変更せず、枠の再利用前に個体を分離する。
struct BattleInspector {
 std::vector<KbcsBattleInspection> records;
 std::vector<std::array<int32_t,2>> slots;
 std::vector<std::array<std::vector<KbcsBattleInspectionSource>,2>> pending;
 std::vector<std::vector<KbcsBattleInspectionSource>> metal;
 std::map<int,std::vector<KbcsBattleInspectionSource>> attackers;
 void spawn(int side,int slot,int profile,int frame,const KbcsActor &actor){
  if(slot<1)return;
  if(slots.size()<=size_t(slot))slots.resize(slot+1,{-1,-1});
  KbcsBattleInspection value{};value.id=int32_t(records.size()+1);value.side=side;value.slot=slot;value.profile=profile;
  value.serial=actor.words[240];value.born_frame=frame;value.retired_frame=-1;value.barrier_max=actor.words[130];
  value.revives_max=actor.words[103];value.burrows_max=actor.words[97];
  value.death_frame=-1;
  slots[slot][side]=int32_t(records.size());records.push_back(value);sample(side,slot,frame,actor);
 }
 KbcsBattleInspection *find(int side,int slot){
  if(slot<1||size_t(slot)>=slots.size()||slots[slot][side]<0)return nullptr;
  return &records[slots[slot][side]];
 }
 void sample(int side,int slot,int frame,const KbcsActor &actor){
  auto *value=find(side,slot);if(!value)return;const auto &w=actor.words;
  if(w[240]!=value->serial||value->retired_frame>=0)return;
  // 原本の解放はrawと27〜29だけを消す。残る最終座標・時計もこのFで保存する。
  if(!w[0])value->retired_frame=frame;
  value->last_frame=frame;value->action=w[1];value->animation=w[2];value->hp=w[8];value->maximum=w[7];
  value->x=w[3];value->y=w[4];value->layer=w[5];value->barrier=w[130];value->shield=w[190];value->shield_max=w[184];
  value->revives=w[103];value->revive_wait=w[205];value->burrows=w[97];
  value->stop=w[61];value->slow=w[62];value->weaken=w[75];value->weaken_rate=w[79];value->curse=w[150];
  value->survive=w[77];value->kills=w[241];
 }
 void begin(){for(auto &slot:pending)for(auto &side:slot)side.clear();for(auto &slot:metal)slot.clear();}
 void reset(int side,int slot){if(slot>=0&&size_t(slot)<pending.size())pending[slot][side].clear();}
 void reserveMetal(int slot,KbcsBattleInspectionSource source){if(metal.size()<=size_t(slot))metal.resize(slot+1);metal[slot].push_back(source);}
 KbcsBattleInspectionSource source(int kind,int side,int slot,int detail){
  KbcsBattleInspectionSource result{kind,0,side,-1,detail,0};
  if(kind==1){if(auto *value=find(side,slot)){result.actor_id=value->id;result.profile=value->profile;}else result.kind=4;}
  return result;
 }
 void reserve(int side,int slot,KbcsBattleInspectionSource source,int64_t amount){
  if(slot<1)return;if(pending.size()<=size_t(slot))pending.resize(slot+1);auto &values=pending[slot][side];if(!source.kind)source={4,0,-1,-1,0,0};
  auto found=std::find_if(values.begin(),values.end(),[&](const auto &value){return value.kind==source.kind&&value.actor_id==source.actor_id&&value.side==source.side&&value.detail==source.detail;});
  if(found!=values.end())found->reserved+=amount;else{source.reserved=amount;values.push_back(source);}
 }
 void death(int side,int slot,int previous,int hp,int reserved,int frame){
  if(previous>0&&hp<=0)if(auto *value=find(side,slot)){++value->deaths;value->death_frame=frame;
   if(reserved>0&&size_t(slot)<pending.size())attackers[value->id]=pending[slot][side];else attackers.erase(value->id);
  }
 }
 void revival(int side,int slot){if(auto *value=find(side,slot)){++value->revivals;attackers.erase(value->id);}}
};

namespace {
// 単体APIを変えず、所有戦闘の同期呼出中だけ予約量と発生元を観測する。
thread_local BattleInspector *activeInspector=nullptr;
thread_local KbcsBattleInspectionSource activeInspectorSource{};
struct InspectorScope {
 BattleInspector *previous;KbcsBattleInspectionSource source;
 explicit InspectorScope(BattleInspector &value):previous(activeInspector),source(activeInspectorSource){activeInspector=&value;activeInspectorSource={};}
 ~InspectorScope(){activeInspector=previous;activeInspectorSource=source;}
};
struct InspectorSourceScope {
 KbcsBattleInspectionSource previous;
 InspectorSourceScope(int kind,int side,int slot,int detail=0):previous(activeInspectorSource){if(activeInspector)activeInspectorSource=activeInspector->source(kind,side,slot,detail);}
 explicit InspectorSourceScope(KbcsBattleInspectionSource value):previous(activeInspectorSource){if(activeInspector)activeInspectorSource=value;}
 ~InspectorSourceScope(){activeInspectorSource=previous;}
};
}
