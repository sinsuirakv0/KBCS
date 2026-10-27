"""ABI4の戦闘Rules。原本照合ツール間で同じCレイアウトを共有する。"""
import ctypes as c

class PointRules(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['kind','rate','tier_count']]+[('tiers',(c.c_int32*2)*32),('fever_count',c.c_int32),('fever',c.c_int32*10)]
class UnitCombo(c.Structure):
 _fields_=[('unit_id',c.c_int32),('values',c.c_int32*32)]
class Rules(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['native_kind','score_type','time_limit']]+[
  ('bonus',c.c_int32*32),('rarity_limits',c.c_int32*6),('slot_rarity',c.c_int32*10),('total_limit',c.c_int32),
  ('extra_rule',c.c_int32*3),('production_kind',c.c_int32),('production_periods',c.c_int32*6),('recharge_fixed',c.c_int32),
  ('cost_chapter',c.c_int32),('point',PointRules),('unit_combo_count',c.c_int32),('unit_combos',UnitCombo*32)]
class Result(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['mode','timer','elapsed','score','finished_frame','reason']]
