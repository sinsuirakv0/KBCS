#pragma once
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct { int32_t units[5],forms[5]; } KbcsComboDefinition;
typedef struct { int32_t team[10],forms[10],locked[10],selected; } KbcsComboSelection;
typedef struct { int32_t first[5],slots[10]; } KbcsComboPlan;
uint32_t kbcs_core_combo_plan(const KbcsComboDefinition*,int32_t,const KbcsComboSelection*,KbcsComboPlan*);
typedef struct { int32_t index,age,blink,band[4],text_x,text_y[3],skip[2]; } KbcsComboIntro;
uint32_t kbcs_core_combo_intro(int32_t frame,int32_t width,int32_t count,const int32_t *groups,KbcsComboIntro*);
/* 00895e64。文字と画像は呼出側で解決し、座標と描画条件を共有する。 */
typedef struct { int32_t panel[4],name[2],effect[2],group[2],icons[5][4]; } KbcsComboRow;
uint32_t kbcs_core_combo_row(int32_t width,int32_t row,int32_t grouped,KbcsComboRow*);
typedef struct { int32_t window[4],confirm[4],close[4]; } KbcsComboDialog;
uint32_t kbcs_core_combo_dialog(int32_t width,int32_t phase,KbcsComboDialog*);
typedef struct { int32_t center,y,form,attributes[10],abilities[88],talents[88],new_attributes[10],orbs; } KbcsUnitInfoInput;
typedef struct { int32_t count,sprites[192][4],orb_count,orbs[8][2]; } KbcsUnitInfoLayout;
uint32_t kbcs_core_unit_info(const KbcsUnitInfoInput*,KbcsUnitInfoLayout*);
#ifdef __cplusplus
}
#endif
