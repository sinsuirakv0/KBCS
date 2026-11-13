# 00aafaa4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aafaa4",
  "name": "FUN_00aafaa4",
  "size": 1500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2a2e80129a25659dad0d2ea57788af5e7e49d3dac6d2d26fd34948a80de6116",
  "source_text_sha256": "d2a2e80129a25659dad0d2ea57788af5e7e49d3dac6d2d26fd34948a80de6116"
}
~~~

## 呼び出し元

- [00b1f4c4](../00b1f/00b1f4c4.md)

## 呼び出し先

- [0043bbe4](../0043b/0043bbe4.md)
- [00440f00](../00440/00440f00.md)
- [0048795c](../00487/0048795c.md)
- [0048797c](../00487/0048797c.md)
- [00487e60](../00487/00487e60.md)
- [00488598](../00488/00488598.md)
- [00488698](../00488/00488698.md)
- [008003d0](../00800/008003d0.md)
- [00800684](../00800/00800684.md)
- [0086950c](../00869/0086950c.md)
- [00ab17f4](../00ab1/00ab17f4.md)
- [00b11188](../00b11/00b11188.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58070](../00c58/00c58070.md)
- [00c58080](../00c58/00c58080.md)
- [00c58090](../00c58/00c58090.md)
- [00c580d0](../00c58/00c580d0.md)

## 関連文字列（未確認候補）

~~~text
"MapStage_Shortcut.csv"
~~~

## 疑似コード / UTF-8 15136 bytes

~~~c

void FUN_00aafaa4(long *param_1)

{
  undefined4 *puVar1;
  undefined4 *puVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined5 uVar6;
  undefined5 uVar7;
  undefined3 uVar8;
  undefined5 uVar9;
  undefined5 uVar10;
  undefined *puVar11;
  int iVar12;
  int iVar13;
  undefined4 uVar14;
  undefined4 uVar15;
  undefined4 uVar16;
  undefined4 uVar17;
  int iVar18;
  ulong uVar19;
  long *plVar20;
  void *pvVar21;
  long *plVar22;
  long *plVar23;
  ulong uVar24;
  ulong uVar25;
  long *plVar26;
  long *plVar27;
  long lVar28;
  void *pvVar29;
  long *plVar30;
  undefined4 local_1ec;
  undefined4 local_1e8;
  undefined1 local_1e4;
  byte local_1e0;
  char local_1df [8];
  char acStack_1d7 [5];
  undefined2 uStack_1d2;
  char cStack_1d0;
  char acStack_1cf [5];
  undefined1 uStack_1ca;
  undefined1 uStack_1c9;
  undefined **local_1c8;
  void *local_1c0;
  void *local_1b8;
  byte local_1a8;
  void *local_198;
  long local_180;
  undefined *local_178 [8];
  byte local_138;
  void *local_128;
  undefined1 auStack_110 [160];
  long local_70;
  
  lVar3 = tpidr_el0;
  local_70 = *(long *)(lVar3 + 0x28);
  FUN_00487e60(&local_1c8);
  plVar26 = param_1 + 1;
                    /* try { // try from 00aafae8 to 00bafb0f has its CatchHandler @ 00aafdf0 */
  local_1c8 = &PTR_FUN_00c64e08;
  FUN_0086950c(param_1,*plVar26);
  *param_1 = (long)plVar26;
  plVar27 = param_1 + 4;
  param_1[2] = 0;
  *plVar26 = 0;
  FUN_0086950c(param_1 + 3,*plVar27);
  uVar9 = s_MapStage_Shortcut_csv_002b6b66._16_5_;
  uVar8 = s_MapStage_Shortcut_csv_002b6b66._13_3_;
  uVar6 = s_MapStage_Shortcut_csv_002b6b66._8_5_;
  uVar4 = s_MapStage_Shortcut_csv_002b6b66._0_8_;
  local_1e0 = 0x2a;
                    /* try { // try from 00aafb30 to 00bafb53 has its CatchHandler @ 00aafdb4 */
  param_1[3] = (long)plVar27;
  param_1[5] = 0;
  *plVar27 = 0;
  uVar10 = s_MapStage_Shortcut_csv_002b6b66._16_5_;
  uVar7 = s_MapStage_Shortcut_csv_002b6b66._8_5_;
  uVar5 = s_MapStage_Shortcut_csv_002b6b66._0_8_;
  s_MapStage_Shortcut_csv_002b6b66[8] = (char)uVar6;
  s_MapStage_Shortcut_csv_002b6b66[9] = SUB51(uVar6,1);
  s_MapStage_Shortcut_csv_002b6b66[10] = SUB51(uVar6,2);
  s_MapStage_Shortcut_csv_002b6b66[0xb] = SUB51(uVar6,3);
  s_MapStage_Shortcut_csv_002b6b66[0xc] = SUB51(uVar6,4);
  acStack_1d7[0] = s_MapStage_Shortcut_csv_002b6b66[8];
  acStack_1d7[1] = s_MapStage_Shortcut_csv_002b6b66[9];
  acStack_1d7[2] = s_MapStage_Shortcut_csv_002b6b66[10];
  acStack_1d7[3] = s_MapStage_Shortcut_csv_002b6b66[0xb];
  acStack_1d7[4] = s_MapStage_Shortcut_csv_002b6b66[0xc];
  s_MapStage_Shortcut_csv_002b6b66[0] = (char)uVar4;
  s_MapStage_Shortcut_csv_002b6b66[1] = SUB81(uVar4,1);
  s_MapStage_Shortcut_csv_002b6b66[2] = SUB81(uVar4,2);
  s_MapStage_Shortcut_csv_002b6b66[3] = SUB81(uVar4,3);
  s_MapStage_Shortcut_csv_002b6b66[4] = SUB81(uVar4,4);
  s_MapStage_Shortcut_csv_002b6b66[5] = SUB81(uVar4,5);
  s_MapStage_Shortcut_csv_002b6b66[6] = SUB81(uVar4,6);
  s_MapStage_Shortcut_csv_002b6b66[7] = SUB81(uVar4,7);
  local_1df[0] = s_MapStage_Shortcut_csv_002b6b66[0];
  local_1df[1] = s_MapStage_Shortcut_csv_002b6b66[1];
  local_1df[2] = s_MapStage_Shortcut_csv_002b6b66[2];
  local_1df[3] = s_MapStage_Shortcut_csv_002b6b66[3];
  local_1df[4] = s_MapStage_Shortcut_csv_002b6b66[4];
  local_1df[5] = s_MapStage_Shortcut_csv_002b6b66[5];
  local_1df[6] = s_MapStage_Shortcut_csv_002b6b66[6];
  local_1df[7] = s_MapStage_Shortcut_csv_002b6b66[7];
  uStack_1d2 = (undefined2)uVar8;
  cStack_1d0 = SUB31(uVar8,2);
  s_MapStage_Shortcut_csv_002b6b66[0x10] = (char)uVar9;
  s_MapStage_Shortcut_csv_002b6b66[0x11] = SUB51(uVar9,1);
  s_MapStage_Shortcut_csv_002b6b66[0x12] = SUB51(uVar9,2);
  s_MapStage_Shortcut_csv_002b6b66[0x13] = SUB51(uVar9,3);
  s_MapStage_Shortcut_csv_002b6b66[0x14] = SUB51(uVar9,4);
  acStack_1cf[0] = s_MapStage_Shortcut_csv_002b6b66[0x10];
  acStack_1cf[1] = s_MapStage_Shortcut_csv_002b6b66[0x11];
  acStack_1cf[2] = s_MapStage_Shortcut_csv_002b6b66[0x12];
  acStack_1cf[3] = s_MapStage_Shortcut_csv_002b6b66[0x13];
  acStack_1cf[4] = s_MapStage_Shortcut_csv_002b6b66[0x14];
  uStack_1ca = 0;
  s_MapStage_Shortcut_csv_002b6b66._0_8_ = uVar5;
  s_MapStage_Shortcut_csv_002b6b66._8_5_ = uVar7;
  s_MapStage_Shortcut_csv_002b6b66._16_5_ = uVar10;
                    /* try { // try from 00aafb58 to 00bafb5f has its CatchHandler @ 00aafe30 */
  uVar19 = FUN_00b11188(&local_1c8,&local_1e0,0,0);
  if ((local_1e0 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_1c9,CONCAT16(uStack_1ca,CONCAT51(acStack_1cf,cStack_1d0))));
  }
  if ((uVar19 & 1) != 0) {
    while (uVar19 = FUN_0048795c(&local_1c8), (uVar19 & 1) != 0) {
      iVar12 = FUN_0048797c(&local_1c8,0);
                    /* try { // try from 00aafbcc to 00bafbef has its CatchHandler @ 00aafd6c */
      iVar13 = FUN_0048797c(&local_1c8,1);
      uVar14 = FUN_0048797c(&local_1c8,2);
      uVar15 = FUN_008003d0();
      uVar14 = FUN_00800684(uVar14);
                    /* try { // try from 00aafbf4 to 00bafc03 has its CatchHandler @ 00aafdf8 */
      uVar16 = FUN_0048797c(&local_1c8,3);
                    /* try { // try from 00aafc04 to 00bafd63 has its CatchHandler @ 00aaf9dc */
      uVar17 = FUN_0048797c(&local_1c8,4);
      iVar18 = FUN_00488598(&local_1c8);
      if ((iVar18 < 6) || (iVar18 = FUN_0048797c(&local_1c8,5), iVar18 == -1)) {
        local_1e4 = 0;
      }
      else {
        uVar17 = FUN_0048797c(&local_1c8,5);
        local_1e4 = 1;
      }
      iVar18 = FUN_00488598(&local_1c8);
      if (iVar18 < 7) {
        local_1e8 = 0xffffffff;
      }
      else {
        local_1e8 = FUN_0048797c(&local_1c8,6);
      }
      iVar18 = FUN_00488598(&local_1c8);
      if (iVar18 < 8) {
        local_1ec = 0xffffffff;
      }
      else {
        local_1ec = FUN_0048797c(&local_1c8,7);
      }
      plVar22 = plVar27;
      if (iVar12 == 1) {
        while (plVar20 = (long *)*plVar22, plVar30 = plVar22, (long *)*plVar22 != (long *)0x0) {
                    /* try { // try from 00aafd64 to 00bafd6b has its CatchHandler @ 00aafe50 */
          while (plVar22 = plVar20, (int)plVar22[4] <= iVar13) {
                    /* catch() { ... } // from try @ 00aafbcc with catch @ 00aafd6c
                       try { // try from 00aafd6c to 00bafe77 has its CatchHandler @ 00aaf9dc */
            if (iVar13 <= (int)plVar22[4]) goto LAB_00aafddc;
            plVar20 = (long *)plVar22[1];
            if ((long *)plVar22[1] == (long *)0x0) {
              plVar30 = plVar22 + 1;
              goto LAB_00aafd80;
            }
          }
        }
LAB_00aafd80:
        plVar20 = (long *)_Znwm(0x40);
        plVar20[2] = (long)plVar22;
        plVar20[6] = 0;
        plVar20[7] = 0;
        plVar20[5] = 0;
        *plVar20 = 0;
        plVar20[1] = 0;
                    /* catch() { ... } // from try @ 00aafb90 with catch @ 00aafda4 */
        *plVar30 = (long)plVar20;
        plVar23 = (long *)param_1[3];
        *(int *)(plVar20 + 4) = iVar13;
                    /* catch() { ... } // from try @ 00aafb30 with catch @ 00aafdb4 */
        plVar22 = plVar20;
        if (*plVar23 != 0) {
          param_1[3] = *plVar23;
          plVar22 = (long *)*plVar30;
        }
        FUN_0043bbe4(param_1[4],plVar22);
        param_1[5] = param_1[5] + 1;
        plVar22 = plVar20;
LAB_00aafddc:
        puVar2 = (undefined4 *)plVar22[6];
        if (puVar2 < (undefined4 *)plVar22[7]) {
          *puVar2 = uVar15;
          puVar2[1] = uVar14;
                    /* catch() { ... } // from try @ 00aafae8 with catch @ 00aafdf0 */
          puVar2[2] = uVar16;
          puVar2[3] = uVar17;
                    /* catch() { ... } // from try @ 00aafbf4 with catch @ 00aafdf8 */
          puVar2[4] = local_1e8;
          puVar2[5] = local_1ec;
          puVar2[7] = 0;
          *(undefined1 *)(puVar2 + 6) = local_1e4;
          plVar22[6] = (long)(puVar2 + 8);
        }
        else {
          pvVar29 = (void *)plVar22[5];
          lVar28 = (long)puVar2 - (long)pvVar29 >> 5;
          uVar19 = lVar28 + 1;
          if (uVar19 >> 0x3b != 0) goto LAB_00ab004c;
          uVar24 = plVar22[7] - (long)pvVar29;
                    /* catch() { ... } // from try @ 00aafb58 with catch @ 00aafe30 */
          uVar25 = (long)uVar24 >> 4;
          if (uVar25 <= uVar19) {
            uVar25 = uVar19;
          }
          if (0x7fffffffffffffdf < uVar24) {
            uVar25 = 0x7ffffffffffffff;
          }
          if (uVar25 != 0) {
                    /* catch() { ... } // from try @ 00aafa28 with catch @ 00aafe50
                       catch() { ... } // from try @ 00aafd64 with catch @ 00aafe50 */
            if (uVar25 >> 0x3b == 0) {
              pvVar21 = (void *)_Znwm(uVar25 << 5);
              goto LAB_00aaff2c;
            }
            goto LAB_00ab0064;
          }
          pvVar21 = (void *)0x0;
LAB_00aaff2c:
          puVar1 = (undefined4 *)((long)pvVar21 + lVar28 * 0x20);
          puVar1[4] = local_1e8;
          puVar1[5] = local_1ec;
          *puVar1 = uVar15;
          puVar1[1] = uVar14;
          puVar1[2] = uVar16;
          puVar1[3] = uVar17;
                    /* try { // try from 00aaff58 to 00baff5b has its CatchHandler @ 00ab0418 */
          *(undefined1 *)(puVar1 + 6) = local_1e4;
          puVar1[7] = 0;
          memcpy(pvVar21,pvVar29,(long)puVar2 - (long)pvVar29);
          plVar22[5] = (long)pvVar21;
          plVar22[6] = (long)(puVar1 + 8);
                    /* try { // try from 00aaff68 to 00baff73 has its CatchHandler @ 00ab0410 */
          plVar22[7] = (long)((long)pvVar21 + uVar25 * 0x20);
          if (pvVar29 != (void *)0x0) {
                    /* try { // try from 00aaff74 to 00baff7f has its CatchHandler @ 00ab0408 */
            _ZdlPv(pvVar29);
          }
          plVar22[6] = (long)(puVar1 + 8);
        }
      }
      else {
        plVar22 = plVar26;
        if (iVar12 == 0) {
          while (plVar20 = (long *)*plVar22, plVar30 = plVar22, (long *)*plVar22 != (long *)0x0) {
            while (plVar22 = plVar20, (int)plVar22[4] <= iVar13) {
              if (iVar13 <= (int)plVar22[4]) goto LAB_00aafe6c;
              plVar20 = (long *)plVar22[1];
              if ((long *)plVar22[1] == (long *)0x0) {
                plVar30 = plVar22 + 1;
                goto LAB_00aafcf4;
              }
            }
          }
LAB_00aafcf4:
          plVar20 = (long *)_Znwm(0x40);
          plVar20[2] = (long)plVar22;
          plVar20[6] = 0;
          plVar20[7] = 0;
          plVar20[5] = 0;
          *plVar20 = 0;
          plVar20[1] = 0;
          *plVar30 = (long)plVar20;
          plVar23 = (long *)*param_1;
          *(int *)(plVar20 + 4) = iVar13;
          plVar22 = plVar20;
          if (*plVar23 != 0) {
            *param_1 = *plVar23;
            plVar22 = (long *)*plVar30;
          }
          FUN_0043bbe4(param_1[1],plVar22);
          param_1[2] = param_1[2] + 1;
          plVar22 = plVar20;
LAB_00aafe6c:
          puVar2 = (undefined4 *)plVar22[6];
          if (puVar2 < (undefined4 *)plVar22[7]) {
            *puVar2 = uVar15;
            puVar2[1] = uVar14;
                    /* try { // try from 00aafb90 to 00bafbb3 has its CatchHandler @ 00aafda4 */
            puVar2[2] = uVar16;
            puVar2[3] = uVar17;
            puVar2[4] = local_1e8;
            puVar2[5] = local_1ec;
            puVar2[7] = 0;
            *(undefined1 *)(puVar2 + 6) = local_1e4;
            plVar22[6] = (long)(puVar2 + 8);
          }
          else {
            pvVar29 = (void *)plVar22[5];
            lVar28 = (long)puVar2 - (long)pvVar29 >> 5;
            uVar19 = lVar28 + 1;
            if (uVar19 >> 0x3b != 0) {
LAB_00ab004c:
              if (*(long *)(lVar3 + 0x28) == local_70) {
                FUN_00ab17f4();
LAB_00ab0064:
                if (*(long *)(lVar3 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
                  FUN_00440f00();
                }
              }
              goto LAB_00ab00d0;
            }
            uVar24 = plVar22[7] - (long)pvVar29;
            uVar25 = (long)uVar24 >> 4;
            if (uVar25 <= uVar19) {
              uVar25 = uVar19;
            }
            if (0x7fffffffffffffdf < uVar24) {
              uVar25 = 0x7ffffffffffffff;
            }
            if (uVar25 == 0) {
              pvVar21 = (void *)0x0;
            }
            else {
              if (uVar25 >> 0x3b != 0) goto LAB_00ab0064;
              pvVar21 = (void *)_Znwm(uVar25 << 5);
            }
            puVar1 = (undefined4 *)((long)pvVar21 + lVar28 * 0x20);
            puVar1[4] = local_1e8;
            puVar1[5] = local_1ec;
            *puVar1 = uVar15;
            puVar1[1] = uVar14;
                    /* try { // try from 00aafefc to 00baff57 has its CatchHandler @ 00aafefc
                       catch() { ... } // from try @ 00aafefc with catch @ 00aafefc
                       catch() { ... } // from try @ 00ab037c with catch @ 00aafefc */
            puVar1[2] = uVar16;
            puVar1[3] = uVar17;
            *(undefined1 *)(puVar1 + 6) = local_1e4;
            puVar1[7] = 0;
            memcpy(pvVar21,pvVar29,(long)puVar2 - (long)pvVar29);
            plVar22[5] = (long)pvVar21;
            plVar22[6] = (long)(puVar1 + 8);
            plVar22[7] = (long)((long)pvVar21 + uVar25 * 0x20);
            if (pvVar29 != (void *)0x0) {
              _ZdlPv(pvVar29);
            }
            plVar22[6] = (long)(puVar1 + 8);
          }
        }
      }
    }
                    /* try { // try from 00aaff80 to 00baff87 has its CatchHandler @ 00ab0400 */
    FUN_00488698(&local_1c8);
  }
  puVar11 = 
  PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88;
  local_180 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
  local_1c8 = (undefined **)(PTR_DAT_00c9ac80 + 0x10);
  *(undefined8 *)((long)&local_180 + *(long *)(local_180 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88 +
        0x18);
  local_178[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac90
                 + 0x10;
                    /* try { // try from 00aaffcc to 00baffeb has its CatchHandler @ 00ab03e8 */
  if ((local_138 & 1) != 0) {
    _ZdlPv(local_128);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_178);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_180,puVar11 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_110);
                    /* try { // try from 00aafffc to 00bb0007 has its CatchHandler @ 00ab03d0 */
  if ((local_1a8 & 1) != 0) {
    _ZdlPv(local_198);
  }
  if (local_1c0 != (void *)0x0) {
    local_1b8 = local_1c0;
    _ZdlPv(local_1c0);
  }
                    /* try { // try from 00ab0018 to 00bb0027 has its CatchHandler @ 00ab03c4 */
  if (*(long *)(lVar3 + 0x28) == local_70) {
    return;
  }
LAB_00ab00d0:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
