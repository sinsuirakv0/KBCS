# 00ad3bfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00ad3bfc.md)

## 関数情報

~~~json
{
  "address": "00ad3bfc",
  "name": "FUN_00ad3bfc",
  "size": 592,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4408e604ad25cc0bf019ab44a709493c988d8b88843afc8cfe140915d001c4e",
  "source_text_sha256": "f4408e604ad25cc0bf019ab44a709493c988d8b88843afc8cfe140915d001c4e"
}
~~~
## 呼び出し元

- [0041cad8](../0041c/0041cad8.md)

## 呼び出し先

- [00449b7c](../00449/00449b7c.md)
- [00551e14](../00551/00551e14.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

## 関連文字列（未確認候補）

~~~text
"(Ljava/lang/String;FZ)V"
"(Ljava/lang/String;FZII)V"
"admobShow"
~~~
## 疑似コード 1/1 / UTF-8 4356 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00ad3bfc(float param_1,uint param_2,undefined8 param_3,undefined8 param_4,
                 undefined8 param_5)

{
  undefined4 uVar1;
  undefined4 uVar2;
  long lVar3;
  undefined8 uVar4;
  undefined *puVar5;
  long *plVar6;
  undefined8 uVar7;
  ulong uVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  ulong local_90;
  undefined8 uStack_88;
  char *local_80;
  byte local_78;
  char local_77 [8];
  undefined2 local_6f;
  void *local_68;
  long local_60;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  plVar6 = (long *)FUN_00565f94();
  uVar7 = (**(code **)(*plVar6 + 0x538))(plVar6,param_5);
  puVar5 = PTR_DAT_00c1ad78;
  uVar8 = FUN_00449b7c(PTR_DAT_00c1ad78);
  if ((uVar8 & 1) == 0) {
    uVar11 = FUN_00566284();
    local_78 = 0x12;
    local_77[0] = s_admobShow_002a1e3b[0];
    local_77[1] = s_admobShow_002a1e3b[1];
    local_77[2] = s_admobShow_002a1e3b[2];
    local_77[3] = s_admobShow_002a1e3b[3];
    local_77[4] = s_admobShow_002a1e3b[4];
    local_77[5] = s_admobShow_002a1e3b[5];
    local_77[6] = s_admobShow_002a1e3b[6];
    local_77[7] = s_admobShow_002a1e3b[7];
    local_6f = 0x77;
    local_80 = (char *)_Znwm(0x19);
    uStack_88 = _UNK_002b0e18;
    local_90 = _DAT_002b0e10;
    uVar4 = s__Ljava_lang_String_FZ_V_002a4e5b._0_8_;
    uVar10 = CONCAT71(s__Ljava_lang_String_FZ_V_002a4e5b._16_7_,
                      s__Ljava_lang_String_FZ_V_002a4e5b[0xf]);
    *(ulong *)(local_80 + 8) =
         CONCAT17(s__Ljava_lang_String_FZ_V_002a4e5b[0xf],s__Ljava_lang_String_FZ_V_002a4e5b._8_7_);
    *(undefined8 *)local_80 = uVar4;
    *(undefined8 *)(local_80 + 0xf) = uVar10;
    local_80[0x17] = '\0';
    local_60 = FUN_00566448(uVar11,&local_78,&local_90,plVar6);
    if ((local_90 & 1) != 0) {
      _ZdlPv(local_80);
    }
    if ((local_78 & 1) != 0) {
      _ZdlPv(local_68);
    }
    uVar8 = FUN_0056626c(&local_60);
    if ((uVar8 & 1) != 0) {
      FUN_00566284();
      uVar10 = FUN_00566978();
      if (local_60 != 0) {
        FUN_00551e14((double)param_1,plVar6,uVar10,local_60,uVar7,param_2 & 1);
      }
      goto LAB_00ad3e1c;
    }
  }
  else {
    uVar9 = FUN_00566284();
    local_78 = 0x12;
    local_77[0] = s_admobShow_002a1e3b[0];
    local_77[1] = s_admobShow_002a1e3b[1];
    local_77[2] = s_admobShow_002a1e3b[2];
    local_77[3] = s_admobShow_002a1e3b[3];
    local_77[4] = s_admobShow_002a1e3b[4];
    local_77[5] = s_admobShow_002a1e3b[5];
    local_77[6] = s_admobShow_002a1e3b[6];
    local_77[7] = s_admobShow_002a1e3b[7];
    local_6f = 0x77;
    local_80 = (char *)_Znwm(0x20);
    uStack_88 = _UNK_002b1128;
    local_90 = _DAT_002b1120;
    uVar11 = s__Ljava_lang_String_FZII_V_002973c2._17_8_;
    uVar4 = s__Ljava_lang_String_FZII_V_002973c2._0_8_;
    uVar10 = CONCAT17(s__Ljava_lang_String_FZII_V_002973c2[0x10],
                      s__Ljava_lang_String_FZII_V_002973c2._9_7_);
                    /* try { // try from 00ad3ca8 to 00bd3d2f has its CatchHandler @ 00ad3e14 */
    *(ulong *)(local_80 + 8) =
         CONCAT71(s__Ljava_lang_String_FZII_V_002973c2._9_7_,s__Ljava_lang_String_FZII_V_002973c2[8]
                 );
    *(undefined8 *)local_80 = uVar4;
    *(undefined8 *)(local_80 + 0x11) = uVar11;
    *(undefined8 *)(local_80 + 9) = uVar10;
    local_80[0x19] = '\0';
    local_60 = FUN_00566448(uVar9,&local_78,&local_90,plVar6);
    if ((local_90 & 1) != 0) {
      _ZdlPv(local_80);
    }
    if ((local_78 & 1) != 0) {
      _ZdlPv(local_68);
    }
    uVar8 = FUN_0056626c(&local_60);
    if ((uVar8 & 1) != 0) {
      uVar1 = *(undefined4 *)(puVar5 + 0x34);
      uVar2 = *(undefined4 *)(puVar5 + 0x40);
      FUN_00566284();
      uVar10 = FUN_00566978();
      if (local_60 != 0) {
                    /* try { // try from 00ad3d30 to 00bd3ee3 has its CatchHandler @ 00ad3b54 */
        FUN_00551e14((double)param_1,plVar6,uVar10,local_60,uVar7,param_2 & 1,uVar1,uVar2);
      }
      goto LAB_00ad3e1c;
    }
  }
                    /* catch() { ... } // from try @ 00ad3ca8 with catch @ 00ad3e14 */
  (**(code **)(*plVar6 + 0xb8))(plVar6,uVar7);
LAB_00ad3e1c:
  if (*(long *)(lVar3 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
