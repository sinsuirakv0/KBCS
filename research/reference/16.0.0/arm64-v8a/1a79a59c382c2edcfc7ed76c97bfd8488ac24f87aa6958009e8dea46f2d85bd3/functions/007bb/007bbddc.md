# 007bbddc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007bbddc",
  "name": "FUN_007bbddc",
  "size": 5848,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "248b03aa8e5908054998bc470c8bef61539b89fb401f9edc99ed27884b51b73e",
  "source_text_sha256": "248b03aa8e5908054998bc470c8bef61539b89fb401f9edc99ed27884b51b73e"
}
~~~

## 呼び出し元

- [007b09d8](../007b0/007b09d8.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [0043bb64](../0043b/0043bb64.md)
- [0046e784](../0046e/0046e784.md)
- [0046e864](../0046e/0046e864.md)
- [0046e930](../0046e/0046e930.md)
- [0046f074](../0046f/0046f074.md)
- [0046f62c](../0046f/0046f62c.md)
- [00470314](../00470/00470314.md)
- [0047e5cc](../0047e/0047e5cc.md)
- [00492dc8](../00492/00492dc8.md)
- [007583a4](../00758/007583a4.md)
- [007f1854](../007f1/007f1854.md)
- [007f1c70](../007f1/007f1c70.md)
- [00802678](../00802/00802678.md)
- [00802b18](../00802/00802b18.md)
- [00803d08](../00803/00803d08.md)
- [008514b8](../00851/008514b8.md)
- [0085c10c](../0085c/0085c10c.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c53b3c](../00c53/00c53b3c.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c58030](../00c58/00c58030.md)

## 関連文字列（未確認候補）

~~~text
"NSt6__ndk110__function6__funcIZN14RoguelikePopup20openChangeCharaPopupEP9NewDialogNS_8functionIFviiEEEE3$_2NS_9allocatorIS8_EEFvS4_20NewDialogChangeStateiEEE"
"img031_char_%s.imgcut"
"img031_char_%s.mamodel"
"img031_char_%s.png"
"img031_char_%s_walkL.maanim"
"img031_char_%s_walkR.maanim"
~~~

## 疑似コード / UTF-8 46082 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_007bbddc(long param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  byte bVar6;
  undefined7 uVar7;
  char cVar8;
  undefined6 uVar9;
  char cVar10;
  undefined4 uVar11;
  int iVar12;
  int iVar13;
  long lVar14;
  undefined8 uVar15;
  long lVar16;
  undefined8 *puVar17;
  undefined8 *puVar18;
  ulong uVar19;
  long lVar20;
  char *pcVar21;
  long lVar22;
  undefined8 *puVar23;
  long *plVar24;
  undefined8 uVar25;
  long *plVar26;
  undefined8 *puVar27;
  char cVar28;
  undefined8 local_1d0;
  long *local_1c8;
  ulong local_1c0;
  undefined8 uStack_1b8;
  void *local_1b0;
  ulong local_1a0;
  undefined8 uStack_198;
  void *local_190;
  byte local_188;
  undefined7 uStack_187;
  long lStack_180;
  void *local_178;
  undefined4 local_170;
  byte local_168;
  undefined7 uStack_167;
  long lStack_160;
  long local_158;
  ulong local_150;
  undefined8 uStack_148;
  void *local_140;
  ulong local_130;
  undefined8 uStack_128;
  void *local_120;
  byte local_110;
  char local_10f [8];
  char acStack_107 [5];
  undefined2 uStack_102;
  char cStack_100;
  char acStack_ff [5];
  undefined1 uStack_fa;
  undefined1 uStack_f9;
  byte local_f8 [16];
  void *local_e8;
  ulong local_e0;
  undefined8 uStack_d8;
  void *local_d0;
  undefined8 local_c0;
  long *plStack_b8;
  byte local_a8;
  undefined4 uStack_a7;
  undefined3 uStack_a3;
  undefined8 uStack_a0;
  void *local_98;
  byte local_90;
  undefined7 uStack_8f;
  char cStack_88;
  undefined6 uStack_87;
  char cStack_81;
  char cStack_80;
  undefined2 uStack_7f;
  uint uStack_7d;
  undefined1 uStack_79;
  long local_78;
  
  lVar1 = tpidr_el0;
  local_78 = *(long *)(lVar1 + 0x28);
  local_a8 = 6;
  uStack_a7 = 0x303030;
  lVar14 = FUN_008514b8();
  if ((*(int *)((long)&fde_table_entry_00333970.data_loc + lVar14) == 3) &&
     (lVar14 = FUN_008514b8(), (*(byte *)(lVar14 + 0x33d9) & 1) == 0)) {
    lVar14 = FUN_008514b8();
    lVar16 = FUN_008514b8();
    plVar26 = *(long **)(lVar14 + 0x2738);
    if (plVar26 != (long *)0x0) {
      do {
        if ((int)plVar26[4] <= *(int *)(lVar16 + 0x44e368)) {
          if (*(int *)(lVar16 + 0x44e368) <= (int)plVar26[4]) {
            lVar14 = FUN_008514b8();
            lVar16 = FUN_008514b8();
            iVar12 = *(int *)(lVar16 + 0x44e368);
            puVar23 = *(undefined8 **)(lVar14 + 0x2738);
            if (*(undefined8 **)(lVar14 + 0x2738) != (undefined8 *)0x0) goto LAB_007bc274;
            puVar27 = (undefined8 *)(lVar14 + 0x2738);
            puVar18 = (undefined8 *)(lVar14 + 0x2738);
            goto LAB_007bc298;
          }
          plVar26 = plVar26 + 1;
        }
        plVar26 = (long *)*plVar26;
      } while (plVar26 != (long *)0x0);
    }
    goto LAB_007bc640;
  }
  lVar14 = FUN_008514b8();
  if (*(int *)(lVar14 + 0x44e370) == -1) {
    uVar15 = FUN_008514b8();
                    /* try { // try from 007bbe6c to 008bbe7b has its CatchHandler @ 007be84c */
    uVar11 = FUN_0085c10c(uVar15,2);
    lVar14 = FUN_008514b8();
                    /* try { // try from 007bbe7c to 008bbe87 has its CatchHandler @ 007be834 */
    *(undefined4 *)(lVar14 + 0x44e370) = uVar11;
  }
  lVar14 = FUN_008514b8();
  if (*(int *)(lVar14 + 0x44e370) == -1) {
LAB_007bcc28:
    cVar28 = '\0';
  }
  else {
    iVar12 = FUN_00802678(0);
                    /* try { // try from 007bbea8 to 008bbeb3 has its CatchHandler @ 007be824 */
                    /* try { // try from 007bbeb4 to 008bcca3 has its CatchHandler @ 007bbc58 */
    if ((iVar12 == -2) || (iVar12 = FUN_00802678(0), iVar12 == -0xc)) {
      lVar14 = FUN_008514b8();
      lVar16 = FUN_008514b8();
      iVar12 = *(int *)(lVar16 + 0x44e370);
      puVar23 = *(undefined8 **)(lVar14 + 0x2738);
      if (*(undefined8 **)(lVar14 + 0x2738) == (undefined8 *)0x0) {
        puVar27 = (undefined8 *)(lVar14 + 0x2738);
        puVar18 = (undefined8 *)(lVar14 + 0x2738);
      }
      else {
        do {
          while (puVar17 = puVar23, puVar27 = puVar17, iVar12 < *(int *)(puVar17 + 4)) {
            puVar23 = (undefined8 *)*puVar17;
            puVar18 = puVar17;
            if ((undefined8 *)*puVar17 == (undefined8 *)0x0) goto LAB_007bbf1c;
          }
          if (iVar12 <= *(int *)(puVar17 + 4)) goto LAB_007bc120;
          puVar23 = (undefined8 *)puVar17[1];
        } while ((undefined8 *)puVar17[1] != (undefined8 *)0x0);
        puVar18 = puVar17 + 1;
      }
LAB_007bbf1c:
      puVar17 = (undefined8 *)_Znwm(0x160);
      *(int *)(puVar17 + 4) = iVar12;
      puVar17[0x2b] = 0;
      *puVar17 = 0;
      puVar17[1] = 0;
      puVar17[2] = puVar27;
      puVar17[8] = 0;
      puVar17[7] = 0;
      puVar17[10] = 0;
      puVar17[9] = 0;
      puVar17[0xc] = 0;
      puVar17[0xb] = 0;
      puVar17[0xe] = 0;
      puVar17[0xd] = 0;
      puVar17[0x10] = 0;
      puVar17[0xf] = 0;
      puVar17[0x12] = 0;
      puVar17[0x11] = 0;
      puVar17[0x14] = 0;
      puVar17[0x13] = 0;
      puVar17[0x16] = 0;
      puVar17[0x15] = 0;
      puVar17[0x18] = 0;
      puVar17[0x17] = 0;
      puVar17[0x1a] = 0;
      puVar17[0x19] = 0;
      puVar17[0x1c] = 0;
      puVar17[0x1b] = 0;
      puVar17[0x1e] = 0;
      puVar17[0x1d] = 0;
      puVar17[0x20] = 0;
      puVar17[0x1f] = 0;
      puVar17[6] = 0;
      puVar17[5] = 0;
      puVar17[0x22] = 0;
      puVar17[0x21] = 0;
      puVar17[0x24] = 0;
      puVar17[0x23] = 0;
      puVar17[0x26] = 0;
      puVar17[0x25] = 0;
      puVar17[0x28] = 0;
      puVar17[0x27] = 0;
      puVar17[0x2a] = 0;
      puVar17[0x29] = 0;
      *puVar18 = puVar17;
      puVar23 = puVar17;
      if (**(long **)(lVar14 + 0x2730) != 0) {
        *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
        puVar23 = (undefined8 *)*puVar18;
      }
      FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
      *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
LAB_007bc120:
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
                (&local_a8,puVar17 + 0x14);
      lVar14 = FUN_008514b8();
      lVar16 = FUN_008514b8();
      iVar12 = *(int *)(lVar16 + 0x44e370);
      puVar23 = *(undefined8 **)(lVar14 + 0x2738);
      if (*(undefined8 **)(lVar14 + 0x2738) == (undefined8 *)0x0) {
        puVar27 = (undefined8 *)(lVar14 + 0x2738);
        puVar17 = puVar27;
      }
      else {
        do {
          while (puVar27 = puVar23, *(int *)(puVar27 + 4) <= iVar12) {
            if (iVar12 <= *(int *)(puVar27 + 4)) {
              cVar28 = *(char *)((long)puVar27 + 0x105);
              goto LAB_007bcc2c;
            }
            puVar23 = (undefined8 *)puVar27[1];
            if ((undefined8 *)puVar27[1] == (undefined8 *)0x0) {
              puVar17 = puVar27 + 1;
              goto LAB_007bc18c;
            }
          }
          puVar23 = (undefined8 *)*puVar27;
          puVar17 = puVar27;
        } while ((undefined8 *)*puVar27 != (undefined8 *)0x0);
      }
LAB_007bc18c:
      puVar18 = (undefined8 *)_Znwm(0x160);
      *(int *)(puVar18 + 4) = iVar12;
      puVar18[0x2b] = 0;
      *puVar18 = 0;
      puVar18[1] = 0;
      puVar18[2] = puVar27;
      puVar18[8] = 0;
      puVar18[7] = 0;
      puVar18[10] = 0;
      puVar18[9] = 0;
      puVar18[0xc] = 0;
      puVar18[0xb] = 0;
      puVar18[0xe] = 0;
      puVar18[0xd] = 0;
      puVar18[0x10] = 0;
      puVar18[0xf] = 0;
      puVar18[0x12] = 0;
      puVar18[0x11] = 0;
      puVar18[0x14] = 0;
      puVar18[0x13] = 0;
      puVar18[0x16] = 0;
      puVar18[0x15] = 0;
      puVar18[0x18] = 0;
      puVar18[0x17] = 0;
      puVar18[0x1a] = 0;
      puVar18[0x19] = 0;
      puVar18[0x1c] = 0;
      puVar18[0x1b] = 0;
      puVar18[0x1e] = 0;
      puVar18[0x1d] = 0;
      puVar18[0x20] = 0;
      puVar18[0x1f] = 0;
      puVar18[6] = 0;
      puVar18[5] = 0;
      puVar18[0x22] = 0;
      puVar18[0x21] = 0;
      puVar18[0x24] = 0;
      puVar18[0x23] = 0;
      puVar18[0x26] = 0;
      puVar18[0x25] = 0;
      puVar18[0x28] = 0;
      puVar18[0x27] = 0;
      puVar18[0x2a] = 0;
      puVar18[0x29] = 0;
      *puVar17 = puVar18;
      puVar23 = puVar18;
      if (**(long **)(lVar14 + 0x2730) != 0) {
        *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
        puVar23 = (undefined8 *)*puVar17;
      }
      FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
      *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
      cVar28 = *(char *)((long)puVar18 + 0x105);
    }
    else {
      iVar12 = FUN_00802678(0);
      if ((iVar12 == -3) || (iVar12 = FUN_00802678(0), iVar12 == -0xd)) {
        lVar14 = FUN_008514b8();
        lVar16 = FUN_008514b8();
        iVar12 = *(int *)(lVar16 + 0x44e370);
        puVar23 = *(undefined8 **)(lVar14 + 0x2738);
        if (*(undefined8 **)(lVar14 + 0x2738) == (undefined8 *)0x0) {
          puVar27 = (undefined8 *)(lVar14 + 0x2738);
          puVar18 = (undefined8 *)(lVar14 + 0x2738);
        }
        else {
          do {
            while (puVar17 = puVar23, puVar27 = puVar17, iVar12 < *(int *)(puVar17 + 4)) {
              puVar23 = (undefined8 *)*puVar17;
              puVar18 = puVar17;
              if ((undefined8 *)*puVar17 == (undefined8 *)0x0) goto LAB_007bc080;
            }
            if (iVar12 <= *(int *)(puVar17 + 4)) goto LAB_007bc398;
            puVar23 = (undefined8 *)puVar17[1];
          } while ((undefined8 *)puVar17[1] != (undefined8 *)0x0);
          puVar18 = puVar17 + 1;
        }
LAB_007bc080:
        puVar17 = (undefined8 *)_Znwm(0x160);
        *(int *)(puVar17 + 4) = iVar12;
        puVar17[0x2b] = 0;
        *puVar17 = 0;
        puVar17[1] = 0;
        puVar17[2] = puVar27;
        puVar17[8] = 0;
        puVar17[7] = 0;
        puVar17[10] = 0;
        puVar17[9] = 0;
        puVar17[0xc] = 0;
        puVar17[0xb] = 0;
        puVar17[0xe] = 0;
        puVar17[0xd] = 0;
        puVar17[0x10] = 0;
        puVar17[0xf] = 0;
        puVar17[0x12] = 0;
        puVar17[0x11] = 0;
        puVar17[0x14] = 0;
        puVar17[0x13] = 0;
        puVar17[0x16] = 0;
        puVar17[0x15] = 0;
        puVar17[0x18] = 0;
        puVar17[0x17] = 0;
        puVar17[0x1a] = 0;
        puVar17[0x19] = 0;
        puVar17[0x1c] = 0;
        puVar17[0x1b] = 0;
        puVar17[0x1e] = 0;
        puVar17[0x1d] = 0;
        puVar17[0x20] = 0;
        puVar17[0x1f] = 0;
        puVar17[6] = 0;
        puVar17[5] = 0;
        puVar17[0x22] = 0;
        puVar17[0x21] = 0;
        puVar17[0x24] = 0;
        puVar17[0x23] = 0;
        puVar17[0x26] = 0;
        puVar17[0x25] = 0;
        puVar17[0x28] = 0;
        puVar17[0x27] = 0;
        puVar17[0x2a] = 0;
        puVar17[0x29] = 0;
        *puVar18 = puVar17;
        puVar23 = puVar17;
        if (**(long **)(lVar14 + 0x2730) != 0) {
          *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
          puVar23 = (undefined8 *)*puVar18;
        }
        FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
        *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
LAB_007bc398:
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
                  (&local_a8,puVar17 + 0x17);
        lVar14 = FUN_008514b8();
        lVar16 = FUN_008514b8();
        iVar12 = *(int *)(lVar16 + 0x44e370);
        puVar23 = *(undefined8 **)(lVar14 + 0x2738);
        if (*(undefined8 **)(lVar14 + 0x2738) == (undefined8 *)0x0) {
          puVar27 = (undefined8 *)(lVar14 + 0x2738);
          puVar17 = puVar27;
        }
        else {
          do {
            while (puVar27 = puVar23, *(int *)(puVar27 + 4) <= iVar12) {
              if (iVar12 <= *(int *)(puVar27 + 4)) {
                cVar28 = *(char *)((long)puVar27 + 0x106);
                goto LAB_007bcc2c;
              }
              puVar23 = (undefined8 *)puVar27[1];
              if ((undefined8 *)puVar27[1] == (undefined8 *)0x0) {
                puVar17 = puVar27 + 1;
                goto LAB_007bc404;
              }
            }
            puVar23 = (undefined8 *)*puVar27;
            puVar17 = puVar27;
          } while ((undefined8 *)*puVar27 != (undefined8 *)0x0);
        }
LAB_007bc404:
        puVar18 = (undefined8 *)_Znwm(0x160);
        *(int *)(puVar18 + 4) = iVar12;
        puVar18[0x2b] = 0;
        *puVar18 = 0;
        puVar18[1] = 0;
        puVar18[2] = puVar27;
        puVar18[8] = 0;
        puVar18[7] = 0;
        puVar18[10] = 0;
        puVar18[9] = 0;
        puVar18[0xc] = 0;
        puVar18[0xb] = 0;
        puVar18[0xe] = 0;
        puVar18[0xd] = 0;
        puVar18[0x10] = 0;
        puVar18[0xf] = 0;
        puVar18[0x12] = 0;
        puVar18[0x11] = 0;
        puVar18[0x14] = 0;
        puVar18[0x13] = 0;
        puVar18[0x16] = 0;
        puVar18[0x15] = 0;
        puVar18[0x18] = 0;
        puVar18[0x17] = 0;
        puVar18[0x1a] = 0;
        puVar18[0x19] = 0;
        puVar18[0x1c] = 0;
        puVar18[0x1b] = 0;
        puVar18[0x1e] = 0;
        puVar18[0x1d] = 0;
        puVar18[0x20] = 0;
        puVar18[0x1f] = 0;
        puVar18[6] = 0;
        puVar18[5] = 0;
        puVar18[0x22] = 0;
        puVar18[0x21] = 0;
        puVar18[0x24] = 0;
        puVar18[0x23] = 0;
        puVar18[0x26] = 0;
        puVar18[0x25] = 0;
        puVar18[0x28] = 0;
        puVar18[0x27] = 0;
        puVar18[0x2a] = 0;
        puVar18[0x29] = 0;
        *puVar17 = puVar18;
        puVar23 = puVar18;
        if (**(long **)(lVar14 + 0x2730) != 0) {
          *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
          puVar23 = (undefined8 *)*puVar17;
        }
        FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
        *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
        cVar28 = *(char *)((long)puVar18 + 0x106);
      }
      else {
        uVar19 = FUN_00803d08();
        if ((uVar19 & 1) == 0) {
          iVar12 = FUN_00802678(0);
          if ((iVar12 != 3) && (iVar12 = FUN_00802678(0), iVar12 != 4)) goto LAB_007bcc28;
          lVar14 = FUN_008514b8();
          lVar16 = FUN_008514b8();
          lVar14 = FUN_007583a4(lVar14 + 0x2730,lVar16 + 0x44e370);
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
                    (&local_a8,lVar14 + 0xc0);
          lVar14 = FUN_008514b8();
          lVar16 = FUN_008514b8();
          lVar14 = FUN_007583a4(lVar14 + 0x2730,lVar16 + 0x44e370);
          cVar28 = *(char *)(lVar14 + 0xe0);
        }
        else {
          lVar14 = FUN_008514b8();
          lVar16 = FUN_008514b8();
          lVar14 = FUN_007583a4(lVar14 + 0x2730,lVar16 + 0x44e370);
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
                    (&local_a8,lVar14 + 0xa8);
          lVar14 = FUN_008514b8();
          lVar16 = FUN_008514b8();
          lVar14 = FUN_007583a4(lVar14 + 0x2730,lVar16 + 0x44e370);
          cVar28 = *(char *)(lVar14 + 0xdf);
        }
      }
    }
  }
  goto LAB_007bcc2c;
  while (puVar23 = (undefined8 *)*puVar17, puVar18 = puVar17,
        (undefined8 *)*puVar17 != (undefined8 *)0x0) {
LAB_007bc274:
    puVar17 = puVar23;
    puVar27 = puVar17;
    if (*(int *)(puVar17 + 4) <= iVar12) {
      if (iVar12 <= *(int *)(puVar17 + 4)) goto LAB_007bc52c;
      puVar23 = (undefined8 *)puVar17[1];
      if ((undefined8 *)puVar17[1] == (undefined8 *)0x0) {
        puVar18 = puVar17 + 1;
        break;
      }
      goto LAB_007bc274;
    }
  }
LAB_007bc298:
  puVar17 = (undefined8 *)_Znwm(0x160);
  *(int *)(puVar17 + 4) = iVar12;
  puVar17[0x2b] = 0;
  *puVar17 = 0;
  puVar17[1] = 0;
  puVar17[2] = puVar27;
  puVar17[8] = 0;
  puVar17[7] = 0;
  puVar17[10] = 0;
  puVar17[9] = 0;
  puVar17[0xc] = 0;
  puVar17[0xb] = 0;
  puVar17[0xe] = 0;
  puVar17[0xd] = 0;
  puVar17[0x10] = 0;
  puVar17[0xf] = 0;
  puVar17[0x12] = 0;
  puVar17[0x11] = 0;
  puVar17[0x14] = 0;
  puVar17[0x13] = 0;
  puVar17[0x16] = 0;
  puVar17[0x15] = 0;
  puVar17[0x18] = 0;
  puVar17[0x17] = 0;
  puVar17[0x1a] = 0;
  puVar17[0x19] = 0;
  puVar17[0x1c] = 0;
  puVar17[0x1b] = 0;
  puVar17[0x1e] = 0;
  puVar17[0x1d] = 0;
  puVar17[0x20] = 0;
  puVar17[0x1f] = 0;
  puVar17[6] = 0;
  puVar17[5] = 0;
  puVar17[0x22] = 0;
  puVar17[0x21] = 0;
  puVar17[0x24] = 0;
  puVar17[0x23] = 0;
  puVar17[0x26] = 0;
  puVar17[0x25] = 0;
  puVar17[0x28] = 0;
  puVar17[0x27] = 0;
  puVar17[0x2a] = 0;
  puVar17[0x29] = 0;
  *puVar18 = puVar17;
  puVar23 = puVar17;
  if (**(long **)(lVar14 + 0x2730) != 0) {
    *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
    puVar23 = (undefined8 *)*puVar18;
  }
  FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
  *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
LAB_007bc52c:
  uVar19 = (ulong)(*(byte *)(puVar17 + 0x11) >> 1);
  if ((*(byte *)(puVar17 + 0x11) & 1) != 0) {
    uVar19 = puVar17[0x12];
  }
  if (uVar19 == 0) {
LAB_007bc640:
    iVar12 = -1;
  }
  else {
    lVar14 = FUN_008514b8();
    lVar16 = FUN_008514b8();
    iVar12 = *(int *)(lVar16 + 0x44e368);
    puVar23 = *(undefined8 **)(lVar14 + 0x2738);
    if (*(undefined8 **)(lVar14 + 0x2738) == (undefined8 *)0x0) {
      puVar27 = (undefined8 *)(lVar14 + 0x2738);
      puVar18 = (undefined8 *)(lVar14 + 0x2738);
    }
    else {
      do {
        while (puVar17 = puVar23, puVar27 = puVar17, iVar12 < *(int *)(puVar17 + 4)) {
          puVar23 = (undefined8 *)*puVar17;
          puVar18 = puVar17;
          if ((undefined8 *)*puVar17 == (undefined8 *)0x0) goto LAB_007bc5a4;
        }
        if (iVar12 <= *(int *)(puVar17 + 4)) goto LAB_007bcab0;
        puVar23 = (undefined8 *)puVar17[1];
      } while ((undefined8 *)puVar17[1] != (undefined8 *)0x0);
      puVar18 = puVar17 + 1;
    }
LAB_007bc5a4:
    puVar17 = (undefined8 *)_Znwm(0x160);
    *(int *)(puVar17 + 4) = iVar12;
    puVar17[0x2b] = 0;
    *puVar17 = 0;
    puVar17[1] = 0;
    puVar17[2] = puVar27;
    puVar17[8] = 0;
    puVar17[7] = 0;
    puVar17[10] = 0;
    puVar17[9] = 0;
    puVar17[0xc] = 0;
    puVar17[0xb] = 0;
    puVar17[0xe] = 0;
    puVar17[0xd] = 0;
    puVar17[0x10] = 0;
    puVar17[0xf] = 0;
    puVar17[0x12] = 0;
    puVar17[0x11] = 0;
    puVar17[0x14] = 0;
    puVar17[0x13] = 0;
    puVar17[0x16] = 0;
    puVar17[0x15] = 0;
    puVar17[0x18] = 0;
    puVar17[0x17] = 0;
    puVar17[0x1a] = 0;
    puVar17[0x19] = 0;
    puVar17[0x1c] = 0;
    puVar17[0x1b] = 0;
    puVar17[0x1e] = 0;
    puVar17[0x1d] = 0;
    puVar17[0x20] = 0;
    puVar17[0x1f] = 0;
    puVar17[6] = 0;
    puVar17[5] = 0;
    puVar17[0x22] = 0;
    puVar17[0x21] = 0;
    puVar17[0x24] = 0;
    puVar17[0x23] = 0;
    puVar17[0x26] = 0;
    puVar17[0x25] = 0;
    puVar17[0x28] = 0;
    puVar17[0x27] = 0;
    puVar17[0x2a] = 0;
    puVar17[0x29] = 0;
    *puVar18 = puVar17;
    puVar23 = puVar17;
    if (**(long **)(lVar14 + 0x2730) != 0) {
      *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
      puVar23 = (undefined8 *)*puVar18;
    }
    FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
    *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
LAB_007bcab0:
    iVar12 = *(int *)(puVar17 + 0x20);
  }
  lVar14 = FUN_008514b8();
  iVar13 = FUN_00802b18(0);
  for (plVar26 = *(long **)(lVar14 + 0x2738); plVar26 != (long *)0x0; plVar26 = (long *)*plVar26) {
    if (*(int *)(plVar26 + 4) <= iVar13) {
      if (iVar13 <= *(int *)(plVar26 + 4)) {
        lVar14 = FUN_008514b8();
        iVar13 = FUN_00802b18(0);
        puVar23 = *(undefined8 **)(lVar14 + 0x2738);
        if (*(undefined8 **)(lVar14 + 0x2738) != (undefined8 *)0x0) goto LAB_007bc7bc;
        puVar27 = (undefined8 *)(lVar14 + 0x2738);
        puVar18 = (undefined8 *)(lVar14 + 0x2738);
        goto LAB_007bc7e0;
      }
      plVar26 = plVar26 + 1;
    }
  }
LAB_007bc65c:
  iVar13 = -1;
  if (iVar12 == 2) goto LAB_007bc668;
LAB_007bcac8:
  if (iVar13 == -1) {
    if (iVar12 != 1) goto LAB_007bcc28;
    lVar14 = FUN_008514b8();
    lVar16 = FUN_008514b8();
    lVar14 = FUN_007583a4(lVar14 + 0x2730,lVar16 + 0x44e368);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
              (&local_a8,lVar14 + 0x60);
    lVar14 = FUN_008514b8();
    lVar16 = FUN_008514b8();
    lVar14 = FUN_007583a4(lVar14 + 0x2730,lVar16 + 0x44e368);
    cVar28 = *(char *)(lVar14 + 0xdc);
  }
  else {
    lVar14 = FUN_008514b8();
    iVar12 = FUN_00802b18(0);
    puVar23 = *(undefined8 **)(lVar14 + 0x2738);
    if (*(undefined8 **)(lVar14 + 0x2738) == (undefined8 *)0x0) {
      puVar27 = (undefined8 *)(lVar14 + 0x2738);
      puVar18 = (undefined8 *)(lVar14 + 0x2738);
    }
    else {
      do {
        while (puVar17 = puVar23, puVar27 = puVar17, iVar12 < *(int *)(puVar17 + 4)) {
          puVar23 = (undefined8 *)*puVar17;
          puVar18 = puVar17;
          if ((undefined8 *)*puVar17 == (undefined8 *)0x0) goto LAB_007bcb2c;
        }
        if (iVar12 <= *(int *)(puVar17 + 4)) goto LAB_007bd2e4;
        puVar23 = (undefined8 *)puVar17[1];
      } while ((undefined8 *)puVar17[1] != (undefined8 *)0x0);
      puVar18 = puVar17 + 1;
    }
LAB_007bcb2c:
    puVar17 = (undefined8 *)_Znwm(0x160);
    *(int *)(puVar17 + 4) = iVar12;
    puVar17[0x2b] = 0;
    *puVar17 = 0;
    puVar17[1] = 0;
    puVar17[2] = puVar27;
    puVar17[8] = 0;
    puVar17[7] = 0;
    puVar17[10] = 0;
    puVar17[9] = 0;
    puVar17[0xc] = 0;
    puVar17[0xb] = 0;
    puVar17[0xe] = 0;
    puVar17[0xd] = 0;
    puVar17[0x10] = 0;
    puVar17[0xf] = 0;
    puVar17[0x12] = 0;
    puVar17[0x11] = 0;
    puVar17[0x14] = 0;
    puVar17[0x13] = 0;
    puVar17[0x16] = 0;
    puVar17[0x15] = 0;
    puVar17[0x18] = 0;
    puVar17[0x17] = 0;
    puVar17[0x1a] = 0;
    puVar17[0x19] = 0;
    puVar17[0x1c] = 0;
    puVar17[0x1b] = 0;
    puVar17[0x1e] = 0;
    puVar17[0x1d] = 0;
    puVar17[0x20] = 0;
    puVar17[0x1f] = 0;
    puVar17[6] = 0;
    puVar17[5] = 0;
    puVar17[0x22] = 0;
    puVar17[0x21] = 0;
    puVar17[0x24] = 0;
    puVar17[0x23] = 0;
    puVar17[0x26] = 0;
    puVar17[0x25] = 0;
    puVar17[0x28] = 0;
    puVar17[0x27] = 0;
    puVar17[0x2a] = 0;
    puVar17[0x29] = 0;
    *puVar18 = puVar17;
    puVar23 = puVar17;
    if (**(long **)(lVar14 + 0x2730) != 0) {
      *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
      puVar23 = (undefined8 *)*puVar18;
    }
    FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
    *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
LAB_007bd2e4:
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
              (&local_a8,puVar17 + 0x11);
    lVar14 = FUN_008514b8();
    iVar12 = FUN_00802b18(0);
    puVar23 = *(undefined8 **)(lVar14 + 0x2738);
    if (*(undefined8 **)(lVar14 + 0x2738) == (undefined8 *)0x0) {
      puVar27 = (undefined8 *)(lVar14 + 0x2738);
      puVar17 = puVar27;
    }
    else {
      do {
        while (puVar27 = puVar23, *(int *)(puVar27 + 4) <= iVar12) {
          if (iVar12 <= *(int *)(puVar27 + 4)) {
            cVar28 = *(char *)((long)puVar27 + 0x104);
            goto LAB_007bcc2c;
          }
          puVar23 = (undefined8 *)puVar27[1];
          if ((undefined8 *)puVar27[1] == (undefined8 *)0x0) {
            puVar17 = puVar27 + 1;
            goto LAB_007bd34c;
          }
        }
        puVar23 = (undefined8 *)*puVar27;
        puVar17 = puVar27;
      } while ((undefined8 *)*puVar27 != (undefined8 *)0x0);
    }
LAB_007bd34c:
    puVar18 = (undefined8 *)_Znwm(0x160);
    *(int *)(puVar18 + 4) = iVar12;
    puVar18[0x2b] = 0;
    *puVar18 = 0;
    puVar18[1] = 0;
    puVar18[2] = puVar27;
    puVar18[8] = 0;
    puVar18[7] = 0;
    puVar18[10] = 0;
    puVar18[9] = 0;
    puVar18[0xc] = 0;
    puVar18[0xb] = 0;
    puVar18[0xe] = 0;
    puVar18[0xd] = 0;
    puVar18[0x10] = 0;
    puVar18[0xf] = 0;
    puVar18[0x12] = 0;
    puVar18[0x11] = 0;
    puVar18[0x14] = 0;
    puVar18[0x13] = 0;
    puVar18[0x16] = 0;
    puVar18[0x15] = 0;
    puVar18[0x18] = 0;
    puVar18[0x17] = 0;
    puVar18[0x1a] = 0;
    puVar18[0x19] = 0;
    puVar18[0x1c] = 0;
    puVar18[0x1b] = 0;
    puVar18[0x1e] = 0;
    puVar18[0x1d] = 0;
    puVar18[0x20] = 0;
    puVar18[0x1f] = 0;
    puVar18[6] = 0;
    puVar18[5] = 0;
    puVar18[0x22] = 0;
    puVar18[0x21] = 0;
    puVar18[0x24] = 0;
    puVar18[0x23] = 0;
    puVar18[0x26] = 0;
    puVar18[0x25] = 0;
    puVar18[0x28] = 0;
    puVar18[0x27] = 0;
    puVar18[0x2a] = 0;
    puVar18[0x29] = 0;
    *puVar17 = puVar18;
    puVar23 = puVar18;
    if (**(long **)(lVar14 + 0x2730) != 0) {
      *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
      puVar23 = (undefined8 *)*puVar17;
    }
    FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
    *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
    cVar28 = *(char *)((long)puVar18 + 0x104);
  }
  goto LAB_007bcc2c;
  while (puVar23 = (undefined8 *)*puVar17, puVar18 = puVar17,
        (undefined8 *)*puVar17 != (undefined8 *)0x0) {
LAB_007bc7bc:
    puVar17 = puVar23;
    puVar27 = puVar17;
    if (*(int *)(puVar17 + 4) <= iVar13) {
      if (iVar13 <= *(int *)(puVar17 + 4)) goto LAB_007bc99c;
      puVar23 = (undefined8 *)puVar17[1];
      if ((undefined8 *)puVar17[1] == (undefined8 *)0x0) {
        puVar18 = puVar17 + 1;
        break;
      }
      goto LAB_007bc7bc;
    }
  }
LAB_007bc7e0:
  puVar17 = (undefined8 *)_Znwm(0x160);
  *(int *)(puVar17 + 4) = iVar13;
  puVar17[0x2b] = 0;
  *puVar17 = 0;
  puVar17[1] = 0;
  puVar17[2] = puVar27;
  puVar17[8] = 0;
  puVar17[7] = 0;
  puVar17[10] = 0;
  puVar17[9] = 0;
  puVar17[0xc] = 0;
  puVar17[0xb] = 0;
  puVar17[0xe] = 0;
  puVar17[0xd] = 0;
  puVar17[0x10] = 0;
  puVar17[0xf] = 0;
  puVar17[0x12] = 0;
  puVar17[0x11] = 0;
  puVar17[0x14] = 0;
  puVar17[0x13] = 0;
  puVar17[0x16] = 0;
  puVar17[0x15] = 0;
  puVar17[0x18] = 0;
  puVar17[0x17] = 0;
  puVar17[0x1a] = 0;
  puVar17[0x19] = 0;
  puVar17[0x1c] = 0;
  puVar17[0x1b] = 0;
  puVar17[0x1e] = 0;
  puVar17[0x1d] = 0;
  puVar17[0x20] = 0;
  puVar17[0x1f] = 0;
  puVar17[6] = 0;
  puVar17[5] = 0;
  puVar17[0x22] = 0;
  puVar17[0x21] = 0;
  puVar17[0x24] = 0;
  puVar17[0x23] = 0;
  puVar17[0x26] = 0;
  puVar17[0x25] = 0;
  puVar17[0x28] = 0;
  puVar17[0x27] = 0;
  puVar17[0x2a] = 0;
  puVar17[0x29] = 0;
  *puVar18 = puVar17;
  puVar23 = puVar17;
  if (**(long **)(lVar14 + 0x2730) != 0) {
    *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
    puVar23 = (undefined8 *)*puVar18;
  }
  FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
  *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
LAB_007bc99c:
  uVar19 = (ulong)(*(byte *)(puVar17 + 0x11) >> 1);
  if ((*(byte *)(puVar17 + 0x11) & 1) != 0) {
    uVar19 = puVar17[0x12];
  }
  if (uVar19 == 0) goto LAB_007bc65c;
  lVar14 = FUN_008514b8();
  iVar13 = FUN_00802b18(0);
  puVar23 = *(undefined8 **)(lVar14 + 0x2738);
  if (*(undefined8 **)(lVar14 + 0x2738) == (undefined8 *)0x0) {
    puVar27 = (undefined8 *)(lVar14 + 0x2738);
    puVar18 = (undefined8 *)(lVar14 + 0x2738);
  }
  else {
    do {
      while (puVar17 = puVar23, puVar27 = puVar17, *(int *)(puVar17 + 4) <= iVar13) {
        if (iVar13 <= *(int *)(puVar17 + 4)) goto LAB_007bcabc;
        puVar23 = (undefined8 *)puVar17[1];
        if ((undefined8 *)puVar17[1] == (undefined8 *)0x0) {
          puVar18 = puVar17 + 1;
          goto LAB_007bca10;
        }
      }
      puVar23 = (undefined8 *)*puVar17;
      puVar18 = puVar17;
    } while ((undefined8 *)*puVar17 != (undefined8 *)0x0);
  }
LAB_007bca10:
  puVar17 = (undefined8 *)_Znwm(0x160);
  *(int *)(puVar17 + 4) = iVar13;
  puVar17[0x2b] = 0;
  *puVar17 = 0;
  puVar17[1] = 0;
  puVar17[2] = puVar27;
  puVar17[8] = 0;
  puVar17[7] = 0;
  puVar17[10] = 0;
  puVar17[9] = 0;
  puVar17[0xc] = 0;
  puVar17[0xb] = 0;
  puVar17[0xe] = 0;
  puVar17[0xd] = 0;
  puVar17[0x10] = 0;
  puVar17[0xf] = 0;
  puVar17[0x12] = 0;
  puVar17[0x11] = 0;
  puVar17[0x14] = 0;
  puVar17[0x13] = 0;
  puVar17[0x16] = 0;
  puVar17[0x15] = 0;
  puVar17[0x18] = 0;
  puVar17[0x17] = 0;
  puVar17[0x1a] = 0;
  puVar17[0x19] = 0;
  puVar17[0x1c] = 0;
  puVar17[0x1b] = 0;
  puVar17[0x1e] = 0;
  puVar17[0x1d] = 0;
  puVar17[0x20] = 0;
  puVar17[0x1f] = 0;
  puVar17[6] = 0;
  puVar17[5] = 0;
  puVar17[0x22] = 0;
  puVar17[0x21] = 0;
  puVar17[0x24] = 0;
  puVar17[0x23] = 0;
  puVar17[0x26] = 0;
  puVar17[0x25] = 0;
  puVar17[0x28] = 0;
  puVar17[0x27] = 0;
  puVar17[0x2a] = 0;
  puVar17[0x29] = 0;
  *puVar18 = puVar17;
  puVar23 = puVar17;
  if (**(long **)(lVar14 + 0x2730) != 0) {
    *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
    puVar23 = (undefined8 *)*puVar18;
  }
  FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
  *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
LAB_007bcabc:
  iVar13 = *(int *)(puVar17 + 0x20);
  if (iVar12 != 2) goto LAB_007bcac8;
LAB_007bc668:
  lVar14 = FUN_008514b8();
  lVar16 = FUN_008514b8();
  iVar12 = *(int *)(lVar16 + 0x44e368);
  puVar23 = *(undefined8 **)(lVar14 + 0x2738);
  if (*(undefined8 **)(lVar14 + 0x2738) == (undefined8 *)0x0) {
    puVar27 = (undefined8 *)(lVar14 + 0x2738);
    puVar18 = (undefined8 *)(lVar14 + 0x2738);
  }
  else {
    do {
      while (puVar17 = puVar23, puVar27 = puVar17, iVar12 < *(int *)(puVar17 + 4)) {
        puVar23 = (undefined8 *)*puVar17;
        puVar18 = puVar17;
        if ((undefined8 *)*puVar17 == (undefined8 *)0x0) goto LAB_007bc714;
      }
      if (iVar12 <= *(int *)(puVar17 + 4)) goto LAB_007bc880;
      puVar23 = (undefined8 *)puVar17[1];
    } while ((undefined8 *)puVar17[1] != (undefined8 *)0x0);
    puVar18 = puVar17 + 1;
  }
LAB_007bc714:
  puVar17 = (undefined8 *)_Znwm(0x160);
  *(int *)(puVar17 + 4) = iVar12;
  puVar17[0x2b] = 0;
  *puVar17 = 0;
  puVar17[1] = 0;
  puVar17[2] = puVar27;
  puVar17[8] = 0;
  puVar17[7] = 0;
  puVar17[10] = 0;
  puVar17[9] = 0;
  puVar17[0xc] = 0;
  puVar17[0xb] = 0;
  puVar17[0xe] = 0;
  puVar17[0xd] = 0;
  puVar17[0x10] = 0;
  puVar17[0xf] = 0;
  puVar17[0x12] = 0;
  puVar17[0x11] = 0;
  puVar17[0x14] = 0;
  puVar17[0x13] = 0;
  puVar17[0x16] = 0;
  puVar17[0x15] = 0;
  puVar17[0x18] = 0;
  puVar17[0x17] = 0;
  puVar17[0x1a] = 0;
  puVar17[0x19] = 0;
  puVar17[0x1c] = 0;
  puVar17[0x1b] = 0;
  puVar17[0x1e] = 0;
  puVar17[0x1d] = 0;
  puVar17[0x20] = 0;
  puVar17[0x1f] = 0;
  puVar17[6] = 0;
  puVar17[5] = 0;
  puVar17[0x22] = 0;
  puVar17[0x21] = 0;
  puVar17[0x24] = 0;
  puVar17[0x23] = 0;
  puVar17[0x26] = 0;
  puVar17[0x25] = 0;
  puVar17[0x28] = 0;
  puVar17[0x27] = 0;
  puVar17[0x2a] = 0;
  puVar17[0x29] = 0;
  *puVar18 = puVar17;
  puVar23 = puVar17;
  if (**(long **)(lVar14 + 0x2730) != 0) {
    *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
    puVar23 = (undefined8 *)*puVar18;
  }
  FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
  *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
LAB_007bc880:
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
            (&local_a8,puVar17 + 0x11);
  lVar14 = FUN_008514b8();
  lVar16 = FUN_008514b8();
  iVar12 = *(int *)(lVar16 + 0x44e368);
  puVar23 = *(undefined8 **)(lVar14 + 0x2738);
  if (*(undefined8 **)(lVar14 + 0x2738) == (undefined8 *)0x0) {
    puVar27 = (undefined8 *)(lVar14 + 0x2738);
    puVar17 = puVar27;
  }
  else {
    do {
      while (puVar27 = puVar23, *(int *)(puVar27 + 4) <= iVar12) {
        if (iVar12 <= *(int *)(puVar27 + 4)) {
          cVar28 = *(char *)((long)puVar27 + 0x104);
          goto LAB_007bcc2c;
        }
        puVar23 = (undefined8 *)puVar27[1];
        if ((undefined8 *)puVar27[1] == (undefined8 *)0x0) {
          puVar17 = puVar27 + 1;
          goto LAB_007bc8ec;
        }
      }
      puVar23 = (undefined8 *)*puVar27;
      puVar17 = puVar27;
    } while ((undefined8 *)*puVar27 != (undefined8 *)0x0);
  }
LAB_007bc8ec:
  puVar18 = (undefined8 *)_Znwm(0x160);
  *(int *)(puVar18 + 4) = iVar12;
  puVar18[0x2b] = 0;
  *puVar18 = 0;
  puVar18[1] = 0;
  puVar18[2] = puVar27;
  puVar18[8] = 0;
  puVar18[7] = 0;
  puVar18[10] = 0;
  puVar18[9] = 0;
  puVar18[0xc] = 0;
  puVar18[0xb] = 0;
  puVar18[0xe] = 0;
  puVar18[0xd] = 0;
  puVar18[0x10] = 0;
  puVar18[0xf] = 0;
  puVar18[0x12] = 0;
  puVar18[0x11] = 0;
  puVar18[0x14] = 0;
  puVar18[0x13] = 0;
  puVar18[0x16] = 0;
  puVar18[0x15] = 0;
  puVar18[0x18] = 0;
  puVar18[0x17] = 0;
  puVar18[0x1a] = 0;
  puVar18[0x19] = 0;
  puVar18[0x1c] = 0;
  puVar18[0x1b] = 0;
  puVar18[0x1e] = 0;
  puVar18[0x1d] = 0;
  puVar18[0x20] = 0;
  puVar18[0x1f] = 0;
  puVar18[6] = 0;
  puVar18[5] = 0;
  puVar18[0x22] = 0;
  puVar18[0x21] = 0;
  puVar18[0x24] = 0;
  puVar18[0x23] = 0;
  puVar18[0x26] = 0;
  puVar18[0x25] = 0;
  puVar18[0x28] = 0;
  puVar18[0x27] = 0;
  puVar18[0x2a] = 0;
  puVar18[0x29] = 0;
  *puVar17 = puVar18;
  puVar23 = puVar18;
  if (**(long **)(lVar14 + 0x2730) != 0) {
    *(long *)(lVar14 + 0x2730) = **(long **)(lVar14 + 0x2730);
    puVar23 = (undefined8 *)*puVar17;
  }
  FUN_0043bb64(*(undefined8 *)(lVar14 + 0x2738),puVar23);
  *(long *)(lVar14 + 0x2740) = *(long *)(lVar14 + 0x2740) + 1;
  cVar28 = *(char *)((long)puVar18 + 0x104);
LAB_007bcc2c:
  if (((DAT_00ca4b38 & 1) == 0) && (iVar12 = __cxa_guard_acquire(&DAT_00ca4b38), iVar12 != 0)) {
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  local_90 = 0x24;
  uStack_7d = uStack_7d & 0xffffff00;
  uStack_7f = 0x676e;
  uStack_87 = (undefined6)s_img031_char__s_png_002bf0d6._8_8_;
  cStack_81 = SUB81(s_img031_char__s_png_002bf0d6._8_8_,6);
  cStack_80 = SUB81(s_img031_char__s_png_002bf0d6._8_8_,7);
  uStack_8f = (undefined7)s_img031_char__s_png_002bf0d6._0_8_;
  cStack_88 = SUB81(s_img031_char__s_png_002bf0d6._0_8_,7);
  if ((local_a8 & 1) == 0) {
    local_e0 = CONCAT35(uStack_a3,CONCAT41(uStack_a7,local_a8));
    uStack_d8 = uStack_a0;
    local_d0 = local_98;
  }
  else {
    FUN_0043bae0(&local_e0,local_98,uStack_a0);
  }
  FUN_00492dc8(&local_188,&local_90,&local_e0);
                    /* try { // try from 007bcca4 to 008bccbf has its CatchHandler @ 007be860 */
  local_110 = 0x2a;
  uStack_fa = 0;
  acStack_107[0] = s_img031_char__s_imgcut_002a8fbd[8];
  acStack_107[1] = s_img031_char__s_imgcut_002a8fbd[9];
  acStack_107[2] = s_img031_char__s_imgcut_002a8fbd[10];
  acStack_107[3] = s_img031_char__s_imgcut_002a8fbd[0xb];
  acStack_107[4] = s_img031_char__s_imgcut_002a8fbd[0xc];
  local_10f[0] = s_img031_char__s_imgcut_002a8fbd[0];
  local_10f[1] = s_img031_char__s_imgcut_002a8fbd[1];
  local_10f[2] = s_img031_char__s_imgcut_002a8fbd[2];
  local_10f[3] = s_img031_char__s_imgcut_002a8fbd[3];
  local_10f[4] = s_img031_char__s_imgcut_002a8fbd[4];
  local_10f[5] = s_img031_char__s_imgcut_002a8fbd[5];
  local_10f[6] = s_img031_char__s_imgcut_002a8fbd[6];
  local_10f[7] = s_img031_char__s_imgcut_002a8fbd[7];
  uStack_102 = (undefined2)s_img031_char__s_imgcut_002a8fbd._13_3_;
  cStack_100 = SUB31(s_img031_char__s_imgcut_002a8fbd._13_3_,2);
  acStack_ff[0] = s_img031_char__s_imgcut_002a8fbd[0x10];
  acStack_ff[1] = s_img031_char__s_imgcut_002a8fbd[0x11];
  acStack_ff[2] = s_img031_char__s_imgcut_002a8fbd[0x12];
  acStack_ff[3] = s_img031_char__s_imgcut_002a8fbd[0x13];
  acStack_ff[4] = s_img031_char__s_imgcut_002a8fbd[0x14];
  if ((local_a8 & 1) == 0) {
                    /* try { // try from 007bccc4 to 008bcd57 has its CatchHandler @ 007be92c */
    local_130 = CONCAT35(uStack_a3,CONCAT41(uStack_a7,local_a8));
    uStack_128 = uStack_a0;
    local_120 = local_98;
  }
  else {
    FUN_0043bae0(&local_130,local_98,uStack_a0);
  }
  FUN_00492dc8(local_f8,&local_110,&local_130);
  FUN_0047e5cc(&local_c0,&DAT_00ca4b00,&local_188,local_f8,0x2601);
  plVar26 = plStack_b8;
  uVar15 = local_c0;
  plVar24 = *(long **)(param_1 + 0x9a0);
  local_c0 = 0;
  plStack_b8 = (long *)0x0;
  *(long **)(param_1 + 0x9a0) = plVar26;
  *(undefined8 *)(param_1 + 0x998) = uVar15;
  plVar26 = plStack_b8;
  if ((plVar24 != (long *)0x0) &&
     (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar24 + 1), plVar26 = plStack_b8, lVar14 == 0)) {
    (**(code **)(*plVar24 + 0x10))(plVar24);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar24);
    plVar26 = plStack_b8;
  }
  plStack_b8 = plVar26;
  if ((plVar26 != (long *)0x0) &&
     (lVar14 = FUN_00c538e0(0xffffffffffffffff,(long *)((long)plVar26 + 8)), lVar14 == 0)) {
    (**(code **)(*plVar26 + 0x10))(plVar26);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar26);
  }
  if ((local_f8[0] & 1) != 0) {
    _ZdlPv(local_e8);
  }
  if ((local_130 & 1) != 0) {
    _ZdlPv(local_120);
  }
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_f9,CONCAT16(uStack_fa,CONCAT51(acStack_ff,cStack_100))));
  }
  if ((local_188 & 1) != 0) {
    _ZdlPv(local_178);
  }
  if ((local_e0 & 1) != 0) {
    _ZdlPv(local_d0);
  }
                    /* try { // try from 007bcd7c to 008bcdcf has its CatchHandler @ 007be928 */
  if ((local_90 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_79,CONCAT43(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
  }
  local_90 = 0x2c;
  uStack_79 = 0;
  uStack_87._0_1_ = s_img031_char__s_mamodel_002bca2f[8];
  uStack_87._1_1_ = s_img031_char__s_mamodel_002bca2f[9];
  uStack_87._2_1_ = s_img031_char__s_mamodel_002bca2f[10];
  uStack_87._3_1_ = s_img031_char__s_mamodel_002bca2f[0xb];
  uStack_87._4_1_ = s_img031_char__s_mamodel_002bca2f[0xc];
  uStack_87._5_1_ = s_img031_char__s_mamodel_002bca2f[0xd];
  uStack_8f = (undefined7)s_img031_char__s_mamodel_002bca2f._0_8_;
  cStack_88 = SUB81(s_img031_char__s_mamodel_002bca2f._0_8_,7);
  cStack_81 = (char)s_img031_char__s_mamodel_002bca2f._14_2_;
  cStack_80 = SUB21(s_img031_char__s_mamodel_002bca2f._14_2_,1);
  uStack_7f = (undefined2)s_img031_char__s_mamodel_002bca2f._16_6_;
  uStack_7d = SUB64(s_img031_char__s_mamodel_002bca2f._16_6_,2);
  if ((local_a8 & 1) == 0) {
    local_150 = CONCAT35(uStack_a3,CONCAT41(uStack_a7,local_a8));
    uStack_148 = uStack_a0;
    local_140 = local_98;
  }
  else {
                    /* try { // try from 007bcdd0 to 008be0d3 has its CatchHandler @ 007bbc58 */
    FUN_0043bae0(&local_150,local_98,uStack_a0);
  }
  FUN_00492dc8(&local_188,&local_90,&local_150);
  FUN_0046f074(param_1 + 0x9a8,&local_188);
  if ((local_188 & 1) != 0) {
    _ZdlPv(local_178);
  }
  if ((local_150 & 1) != 0) {
    _ZdlPv(local_140);
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_79,CONCAT43(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
  }
  lVar14 = *(long *)(param_1 + 0xa58);
  lVar16 = *(long *)(param_1 + 0xa50);
  while (lVar14 != lVar16) {
    lVar14 = lVar14 + -0x38;
    FUN_0046e864(lVar14);
  }
  *(long *)(param_1 + 0xa58) = lVar16;
  FUN_0046e784(&local_188);
  lVar14 = lStack_180;
  plVar26 = *(long **)(param_1 + 0xa58);
  if (plVar26 < *(long **)(param_1 + 0xa60)) {
    *plVar26 = 0;
    plVar26[1] = 0;
    plVar26[2] = 0;
    lVar22 = CONCAT71(uStack_187,local_188);
    local_90 = (byte)plVar26;
    uStack_8f = (undefined7)((ulong)plVar26 >> 8);
    cStack_88 = '\0';
    lVar16 = lStack_180 - lVar22;
    if (lVar16 == 0) {
LAB_007bcec0:
      *(undefined4 *)(plVar26 + 3) = local_170;
      if ((local_168 & 1) == 0) {
        plVar26[6] = local_158;
        plVar26[5] = lStack_160;
        plVar26[4] = CONCAT71(uStack_167,local_168);
      }
      else {
        FUN_0043bae0(plVar26 + 4,local_158,lStack_160);
      }
      plVar26 = plVar26 + 7;
      *(long **)(param_1 + 0xa58) = plVar26;
      goto LAB_007bcf30;
    }
    if ((ulong)((lVar16 >> 3) * -0x3333333333333333) < 0x666666666666667) {
      lVar20 = _Znwm(lVar16);
      *plVar26 = lVar20;
      plVar26[1] = lVar20;
      plVar26[2] = lVar20 + lVar16;
      lVar14 = FUN_007f1c70(plVar26 + 2,lVar22,lVar14,lVar20);
      plVar26[1] = lVar14;
      goto LAB_007bcec0;
    }
    if (*(long *)(lVar1 + 0x28) != local_78) goto LAB_007bd694;
    FUN_00470314(plVar26);
LAB_007bd468:
    if (*(long *)(lVar1 + 0x28) == local_78) {
      uVar15 = FUN_00470314(plVar26);
      if ((local_a8 & 1) != 0) {
        _ZdlPv(local_98);
      }
      if (*(long *)(lVar1 + 0x28) == local_78) {
                    /* WARNING: Subroutine does not return */
        FUN_00c53b3c(uVar15);
      }
    }
  }
  else {
    plVar26 = (long *)FUN_007f1854(param_1 + 0xa50,&local_188);
LAB_007bcf30:
    *(long **)(param_1 + 0xa58) = plVar26;
    FUN_0046e864(&local_188);
    uVar25 = *(undefined8 *)(param_1 + 0xa50);
    pcVar21 = (char *)_Znwm(0x20);
    uVar5 = _UNK_002c2648;
    uVar4 = _DAT_002c2640;
    uVar3 = s_img031_char__s_walkR_maanim_002ba6b6._19_8_;
    uVar2 = s_img031_char__s_walkR_maanim_002ba6b6._0_8_;
    uVar15 = CONCAT35(s_img031_char__s_walkR_maanim_002ba6b6._16_3_,
                      s_img031_char__s_walkR_maanim_002ba6b6._11_5_);
    cStack_80 = (char)pcVar21;
    uStack_7f = (undefined2)((ulong)pcVar21 >> 8);
    uStack_7d = (uint)((ulong)pcVar21 >> 0x18);
    uStack_79 = (undefined1)((ulong)pcVar21 >> 0x38);
    *(ulong *)(pcVar21 + 8) =
         CONCAT53(s_img031_char__s_walkR_maanim_002ba6b6._11_5_,
                  s_img031_char__s_walkR_maanim_002ba6b6._8_3_);
    *(undefined8 *)pcVar21 = uVar2;
    *(undefined8 *)(pcVar21 + 0x13) = uVar3;
    *(undefined8 *)(pcVar21 + 0xb) = uVar15;
    cStack_88 = (char)uVar5;
    cVar8 = cStack_88;
    uStack_87 = (undefined6)((ulong)uVar5 >> 8);
    uVar9 = uStack_87;
    cStack_81 = (char)((ulong)uVar5 >> 0x38);
    cVar10 = cStack_81;
    local_90 = (byte)uVar4;
    bVar6 = local_90;
    uStack_8f = (undefined7)((ulong)uVar4 >> 8);
    uVar7 = uStack_8f;
    pcVar21[0x1b] = '\0';
    if ((local_a8 & 1) == 0) {
      local_1a0 = CONCAT35(uStack_a3,CONCAT41(uStack_a7,local_a8));
      uStack_198 = uStack_a0;
      local_190 = local_98;
    }
    else {
      FUN_0043bae0(&local_1a0,local_98,uStack_a0);
    }
    FUN_00492dc8(&local_188,&local_90,&local_1a0);
    FUN_0046e930(uVar25,&local_188);
    if ((local_188 & 1) != 0) {
      _ZdlPv(local_178);
    }
    if ((local_1a0 & 1) != 0) {
      _ZdlPv(local_190);
    }
    if ((local_90 & 1) != 0) {
      _ZdlPv((void *)CONCAT17(uStack_79,CONCAT43(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
    }
    if (cVar28 != '\0') {
      FUN_0046e784(&local_188);
      plVar26 = *(long **)(param_1 + 0xa58);
      if (plVar26 < *(long **)(param_1 + 0xa60)) {
        *plVar26 = 0;
        plVar26[1] = 0;
        plVar26[2] = 0;
        lVar16 = CONCAT71(uStack_187,local_188);
        local_90 = (byte)plVar26;
        uStack_8f = (undefined7)((ulong)plVar26 >> 8);
        cStack_88 = '\0';
        lVar14 = lStack_180 - lVar16;
        if (lVar14 != 0) {
          if (0x666666666666666 < (ulong)((lVar14 >> 3) * -0x3333333333333333)) goto LAB_007bd468;
          lVar22 = _Znwm(lVar14);
          *plVar26 = lVar22;
          plVar26[1] = lVar22;
          plVar26[2] = lVar22 + lVar14;
          lVar14 = FUN_007f1c70(plVar26 + 2,lVar16,lStack_180,lVar22);
          plVar26[1] = lVar14;
        }
        *(undefined4 *)(plVar26 + 3) = local_170;
        if ((local_168 & 1) == 0) {
          plVar26[6] = local_158;
          plVar26[5] = lStack_160;
          plVar26[4] = CONCAT71(uStack_167,local_168);
        }
        else {
          FUN_0043bae0(plVar26 + 4,local_158,lStack_160);
        }
        plVar26 = plVar26 + 7;
        *(long **)(param_1 + 0xa58) = plVar26;
      }
      else {
        plVar26 = (long *)FUN_007f1854(param_1 + 0xa50,&local_188);
      }
      *(long **)(param_1 + 0xa58) = plVar26;
      FUN_0046e864(&local_188);
      lVar14 = *(long *)(param_1 + 0xa50);
      pcVar21 = (char *)_Znwm(0x20);
      uVar3 = s_img031_char__s_walkL_maanim_002a45d3._19_8_;
      uVar2 = s_img031_char__s_walkL_maanim_002a45d3._0_8_;
      cStack_80 = (char)pcVar21;
      uStack_7f = (undefined2)((ulong)pcVar21 >> 8);
      uStack_7d = (uint)((ulong)pcVar21 >> 0x18);
      uStack_79 = (undefined1)((ulong)pcVar21 >> 0x38);
      uVar15 = CONCAT35(s_img031_char__s_walkL_maanim_002a45d3._16_3_,
                        s_img031_char__s_walkL_maanim_002a45d3._11_5_);
      *(ulong *)(pcVar21 + 8) =
           CONCAT53(s_img031_char__s_walkL_maanim_002a45d3._11_5_,
                    s_img031_char__s_walkL_maanim_002a45d3._8_3_);
      *(undefined8 *)pcVar21 = uVar2;
      *(undefined8 *)(pcVar21 + 0x13) = uVar3;
      *(undefined8 *)(pcVar21 + 0xb) = uVar15;
      pcVar21[0x1b] = '\0';
      local_90 = bVar6;
      uStack_8f = uVar7;
      cStack_88 = cVar8;
      uStack_87 = uVar9;
      cStack_81 = cVar10;
      if ((local_a8 & 1) == 0) {
        local_1c0 = CONCAT35(uStack_a3,CONCAT41(uStack_a7,local_a8));
        uStack_1b8 = uStack_a0;
        local_1b0 = local_98;
      }
      else {
        FUN_0043bae0(&local_1c0,local_98,uStack_a0);
      }
      FUN_00492dc8(&local_188,&local_90,&local_1c0);
      FUN_0046e930(lVar14 + 0x38,&local_188);
      if ((local_188 & 1) != 0) {
        _ZdlPv(local_178);
      }
      if ((local_1c0 & 1) != 0) {
        _ZdlPv(local_1b0);
      }
      if ((local_90 & 1) != 0) {
        _ZdlPv((void *)CONCAT17(uStack_79,CONCAT43(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
      }
    }
    local_1d0 = *(undefined8 *)(param_1 + 0x998);
    local_1c8 = *(long **)(param_1 + 0x9a0);
    if (local_1c8 != (long *)0x0) {
      FUN_00c538b0(1,local_1c8 + 1);
    }
    FUN_0046f62c(param_1 + 0x9a8,&local_1d0);
    plVar26 = local_1c8;
    if ((local_1c8 != (long *)0x0) &&
       (lVar14 = FUN_00c538e0(0xffffffffffffffff,local_1c8 + 1), lVar14 == 0)) {
      (**(code **)(*plVar26 + 0x10))(plVar26);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar26);
    }
    if ((local_a8 & 1) != 0) {
      _ZdlPv(local_98);
    }
    if (*(long *)(lVar1 + 0x28) == local_78) {
      return;
    }
  }
LAB_007bd694:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
