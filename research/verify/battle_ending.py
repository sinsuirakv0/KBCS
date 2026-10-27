"""終了時計を現版ARM64 controllerで連続実行する。オンライン/広告/報酬popupは別責務。"""
import argparse,ctypes as c,json,os,sqlite3,struct,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--python-libs',type=Path,required=True);p.add_argument('--library',type=Path,required=True)
a=p.parse_args();sys.path.insert(0,str(a.python_libs))
from stages import Native,ROOT,SHA,digest
n=Native();g=0x40000000;n.cpu.mem_map(g,0x800000)
controllers={1:0x5e1a5c,2:0x5eb040,4:0x5edb40,7:0x5ef020}
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for address in [*controllers.values(),0x5cb0e0]:n.ends[address]=address+db.execute('SELECT size FROM functions WHERE address=?',(f'{address:08x}',)).fetchone()[0]
runtime=os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name=='nt' else None
lib=c.CDLL(str(a.library.resolve()));assert lib.kbcs_core_abi_version()==4
class Popup(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['index','count','phase','scale_frame','flash','wait']]
class Ending(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['phase','frame','panel']]+[('title',c.c_int32*3)]+[(k,c.c_int32) for k in ['bar_x','number_x','shade','ready']]+[('button',c.c_int32*4),('visual_button',c.c_int32*4),('label',c.c_int32*4)]+[(k,c.c_int32) for k in ['pressed','guard','action']]+[('popup',Popup)]
class Camera(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['left','zoom','moving','width','rows']]
lib.kbcs_core_battle_ending_step.argtypes=[c.c_int32,c.c_int32,c.POINTER(Ending)]
lib.kbcs_core_battle_end_camera_step.argtypes=[c.POINTER(Camera)]
def put(offset,value):n.cpu.mem_write(g+offset,struct.pack('<i',value))
def get(offset):return struct.unpack('<i',n.cpu.mem_read(g+offset,4))[0]
def run(address):
 n.entry=address
 for i in range(8):n.cpu.reg_write(getattr(n.reg,f'UC_ARM64_REG_X{i}'),g if i==0 else 0)
 n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,n.stack+0x8000);n.cpu.reg_write(n.reg.UC_ARM64_REG_LR,n.stop)
 n.cpu.emu_start(address,n.stop+4,count=10000)
 assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in {n.stop,*n.terminals}
counts={}
for mode,point in [(1,0),(1,1),(2,0),(4,0),(7,1)]:
 n.cpu.mem_write(g,bytes(0x800000));put(0x83e48,-1);state=Ending()
 n.helpers={0x9f4228:0,0x5bc00c:0,0xa0b03c:point,0x5e0048:0,0x9bd60c:0,0x5bc058:mode,0x449aec:960,0x449d9c:0,0x7cf950:0,0x7cfaa0:0,0x6562ac:-1,0x44a8d8:0,0xbdaf00:0}
 # 敗北の最終遷移では文字テクスチャ構築の直前で止める。状態書込は実命令。
 n.terminals={0x45ba04} if mode==2 else set()
 for frame in range(200):
  run(controllers[mode]);assert lib.kbcs_core_battle_ending_step(mode,point,c.byref(state))==0
  assert (state.phase,state.frame,state.panel)==(get(0x83e38),get(0x83e3c),get(0x32f808)),(mode,point,frame,list((state.phase,state.frame,state.panel)),[get(0x83e38),get(0x83e3c),get(0x32f808)])
  if state.phase in [4,7]:break
 else:raise AssertionError(('end not reached',mode,point))
 counts[f'controller_{mode}_point_{point}']=frame+1
# 005cb0e0は段別補正をgetterで解決。実際の整数演算と上限分岐を実行する。
n.terminals=set()
for rows,anchor,offset,expected in [(1,520,0,10000),(2,505,-51,8803)]:
 put(0x34a4,anchor);put(0x343c,10000);n.cpu.mem_write(g+0x1405,bytes([rows==2]));n.helpers={0x9019f4:20,0x5c8a6c:offset}
 assert n.call(0x5cb0e0,g)==expected
 state=Camera(0,10000,0,24000,rows);assert lib.kbcs_core_battle_end_camera_step(c.byref(state))==0 and state.zoom==expected
counts['zoom_cap']=2
class Material(c.Structure):
 _fields_=[('count',c.c_float),('multiplier',c.c_float),('miss',c.c_int32),('weights',c.c_int32*16)]
class Ex(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['chance','map_index','minimum','maximum','group_present']]
class Choice(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['group','threshold','map_index','stage']]
class RewardRules(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['enabled','mode','count','acquired','radar']]+[('chances',c.c_int32*10),('material_enabled',c.c_int32),('material',Material)]+[(k,c.c_int32) for k in ['win_type','win_count']]+[('win_sounds',c.c_int32*32)]+[(k,c.c_int32) for k in ['lose_type','lose_count']]+[('lose_sounds',c.c_int32*32),('music',c.c_int32*2)]+[(k,c.c_int32) for k in ['music_threshold','music_delay','start_sound']]+[('ex',Ex),('ex_count',c.c_int32),('ex_choices',Choice*32)]
class Music(c.Structure):
 _fields_=[(k,c.c_int32) for k in ['id','serial','wait','changed','started','delay']]
lib.kbcs_core_battle_music_cross.argtypes=[c.POINTER(RewardRules),c.c_int32,c.c_int32,c.c_int32,c.POINTER(Music)]
lib.kbcs_core_battle_music_tick.argtypes=[c.POINTER(RewardRules),c.POINTER(Music)]
# 命中後の敵城HP境界を原本006d6d04の実命令区間で比較する。
n.ends[0x6d6d04]=0x6dc000;n.entry=0x6d6d04;n.terminals={0x6da0c4}
crosses=0
for maximum in [10000,2147483647]:
 for rate in [0,1,50,99,100]:
  threshold=c.c_int32(rate*maximum).value
  threshold=int(abs(threshold)//100)*(1 if threshold>=0 else -1)
  for previous,current in [(maximum,0),(maximum,maximum),(max(0,threshold),0),(max(0,threshold+1),max(0,threshold)),(max(0,threshold+1),max(0,threshold+1))]:
   n.cpu.mem_write(g+0x296edc,bytes(20));put(0x3c3988,0)
   row=n.memory+0x2000;n.cpu.mem_write(row,bytes(0xbc));n.cpu.mem_write(row+12,struct.pack('<ii',rate,24))
   sp=n.stack+0x8000;n.cpu.mem_write(sp+0x160,struct.pack('<Q',row));n.cpu.mem_write(sp+0xb8,struct.pack('<Q',g+0x296edc))
   for register,value in [('X27',g),('X28',0),('X21',previous),('SP',sp),('D8',1)]:n.cpu.reg_write(getattr(n.reg,'UC_ARM64_REG_'+register),value)
   stopped=[];n.helpers={0xa95824:maximum,0xa958b0:current,0x457e1c:0,0x459bb4:lambda:stopped.append(1) or 0}
   n.cpu.emu_start(0x6db1c0,n.stop+4,count=1000)
   assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)==0x6da0c4
   rules=RewardRules();rules.music_threshold=rate;rules.music[:]=[23,24];music=Music(23,0,0,0,1,0)
   assert lib.kbcs_core_battle_music_cross(c.byref(rules),previous,current,maximum,c.byref(music))==0
   expected=struct.unpack('<5i',n.cpu.mem_read(g+0x296edc,20))
   assert (music.wait,music.changed)==(expected[2],expected[4]),(maximum,rate,previous,current,expected,music.wait,music.changed)
   assert bool(stopped)==bool(music.changed)
   if music.changed:
    for tick in range(45):
     assert lib.kbcs_core_battle_music_tick(c.byref(rules),c.byref(music))==0
     assert music.id==(-1 if tick<44 else 24)
   crosses+=1
counts['music_hp_cross']=crosses
class PopupInput(c.Structure):
 _fields_=[('viewport',c.c_int32),('count',c.c_int32),('widths',c.c_int32*8),('scale_frame',c.c_int32),('cut',c.c_int32*4),('padding',c.c_int32*2)]
class PopupLayout(c.Structure):
 _fields_=[('body',c.c_int32*4),('text_y',c.c_int32),('text_x',c.c_int32*8),('parts',(c.c_int32*8)*9),('text_scale',c.c_float*8)]
lib.kbcs_core_battle_popup_layout.argtypes=[c.POINTER(PopupInput),c.POINTER(PopupLayout)]
lib.kbcs_core_battle_popup_step.argtypes=[c.c_int32,c.POINTER(Popup)]
with sqlite3.connect((n.cache/'cache.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 for address in [0x885170,0x8865b8,0x44626c]:n.ends[address]=address+db.execute('SELECT size FROM functions WHERE address=?',(f'{address:08x}',)).fetchone()[0]
popup=n.memory+0x3000;rows=n.memory+0x4000;sp=n.stack+0x8000
layout_cases=0
for viewport,widths in [(960,[120]),(1280,[315,600]),(960,[480,800,270]),(1280,[1100,800,35,620])]:
 n.cpu.mem_write(popup,bytes(0x200));n.cpu.mem_write(rows,bytes(0x200))
 n.cpu.mem_write(popup+0x18,struct.pack('<QQ',rows,rows+len(widths)*40));n.cpu.mem_write(popup+8,struct.pack('<i',401))
 for i,width in enumerate(widths):n.cpu.mem_write(rows+i*40+4,struct.pack('<i',width))
 n.cpu.mem_write(sp+0x14,struct.pack('<i',1));n.entry=0x885170;n.terminals={0x885cc0}
 n.helpers={0x44abe4:lambda:max(c.c_int32(n.cpu.reg_read(n.reg.UC_ARM64_REG_W0)).value,c.c_int32(n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)).value),0x44abfc:lambda:min(n.cpu.reg_read(n.reg.UC_ARM64_REG_W0),n.cpu.reg_read(n.reg.UC_ARM64_REG_W1)),0x81f580:g,0x449aec:viewport}
 n.cpu.reg_write(n.reg.UC_ARM64_REG_X19,popup);n.cpu.reg_write(n.reg.UC_ARM64_REG_SP,sp);n.cpu.emu_start(0x885af4,n.stop+4,count=1000)
 expected=list(struct.unpack('<2i',n.cpu.mem_read(popup+4,8)))+list(struct.unpack('<2i',n.cpu.mem_read(popup+16,8)))
 for scale_frame in range(1,5):
  data=PopupInput(viewport,len(widths),(c.c_int32*8)(*widths),scale_frame,(c.c_int32*4)(1,1,12,62),(c.c_int32*2)(6,6));out=PopupLayout()
  assert lib.kbcs_core_battle_popup_layout(c.byref(data),c.byref(out))==0
  if scale_frame==4:assert list(out.body)==expected,(widths,list(out.body),expected)
  # 0044626cの9回の実描画要求。幅0のUVも変更せず比較する。
  texture=n.memory+0x6000;cut=n.memory+0x6100;n.cpu.mem_write(texture+0x58,struct.pack('<Q',cut));n.cpu.mem_write(cut,bytes(data.cut));calls=[]
  def draw():
   stack=n.cpu.reg_read(n.reg.UC_ARM64_REG_SP);calls.append([c.c_int32(n.cpu.reg_read(getattr(n.reg,'UC_ARM64_REG_W'+str(i)))).value for i in range(2,8)]+[struct.unpack('<i',n.cpu.mem_read(stack+j*8,4))[0] for j in range(2)]);return 0
  n.helpers={0x467074:cut,0x445e30:draw};n.terminals=set();n.cpu.mem_write(sp,struct.pack('<i',6));n.cpu.reg_write(n.reg.UC_ARM64_REG_S0,struct.unpack('<I',struct.pack('<f',2.7))[0]);n.call(0x44626c,0,texture,*out.body,0,6)
  assert calls==[list(out.parts[i]) for i in [0,1,2,5,8,7,6,3,4]],(scale_frame,calls,[list(v) for v in out.parts])
  layout_cases+=1
counts['popup_layout_and_nine_parts']=layout_cases
n.cpu.mem_write(popup,bytes(0x200));n.cpu.mem_write(popup+0x50,struct.pack('<Q',n.memory+0x5000));n.cpu.mem_write(n.memory+0x5000,struct.pack('<Q',n.memory+0x5100));n.cpu.mem_write(n.memory+0x5130,struct.pack('<Q',n.stop+0x300));n.cpu.mem_write(popup+0xa8,struct.pack('<ii',-1,-1));state=Popup()
def callback():
 event=struct.unpack('<i',n.cpu.mem_read(n.cpu.reg_read(n.reg.UC_ARM64_REG_X2),4))[0]
 if event==2:n.cpu.mem_write(popup+0x60,struct.pack('<i',2))
 return 0
for tick in range(18):
 release=int(tick==10);n.helpers={0x81f580:g,0x829328:release,0x829334:0,n.stop+0x300:callback};n.terminals=set();n.call(0x8865b8,popup,1)
 assert lib.kbcs_core_battle_popup_step(release,c.byref(state))==0
 expected=struct.unpack('<4i',n.cpu.mem_read(popup+0x60,16));assert (state.phase,state.scale_frame,state.flash,state.wait)==expected,(tick,expected,state.phase,state.scale_frame,state.flash,state.wait)
 if state.phase==3:break
counts['popup_continuous']=tick+1
report={'version':'15.7.2','nativeSha256':SHA,'librarySha256':digest(a.library.read_bytes()),'cases':counts,'result':'equal','controlled':['popup queue is empty','point-stage expiry popup absent','EX selection result and entropy are stubbed here; ex_transition.py verifies its kernel','input/window/network getters','camera Y getters resolved to normal 1/2-row values'],'actual':['005e1a5c/005eb040/005edb40/005ef020 continuous controller writes','005cb0e0 scale cap arithmetic']}
(ROOT/'research/.local/battle-ending-1572.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8-sig');print(json.dumps(report,ensure_ascii=True))
