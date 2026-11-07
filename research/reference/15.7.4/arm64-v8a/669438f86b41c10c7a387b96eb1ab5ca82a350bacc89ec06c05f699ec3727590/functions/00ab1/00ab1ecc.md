# 00ab1ecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00ab1dc0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab1/00ab1dc0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00ab1ecc",
  "name": "FUN_00ab1ecc",
  "size": 4088,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "738cb37fe5b4c98b5b09c2a9579a01ae3b45c15827eb0b43497b541eae9b20e7",
  "source_text_sha256": "738cb37fe5b4c98b5b09c2a9579a01ae3b45c15827eb0b43497b541eae9b20e7"
}
~~~

## 呼び出し元

- [00abf570](../00abf/00abf570.md)

## 呼び出し先

- [00459a90](../00459/00459a90.md)
- [00464a44](../00464/00464a44.md)
- [00464a64](../00464/00464a64.md)
- [00464b8c](../00464/00464b8c.md)
- [00464f48](../00464/00464f48.md)
- [00465394](../00465/00465394.md)
- [00465780](../00465/00465780.md)
- [00469f7c](../00469/00469f7c.md)
- [0046ff30](../0046f/0046ff30.md)
- [00470ac0](../00470/00470ac0.md)
- [006181e8](../00618/006181e8.md)
- [00627d10](../00627/00627d10.md)
- [00692224](../00692/00692224.md)
- [006b0f78](../006b0/006b0f78.md)
- [006b12cc](../006b1/006b12cc.md)
- [006b5fcc](../006b5/006b5fcc.md)
- [00ab1234](../00ab1/00ab1234.md)
- [00ab3178](../00ab3/00ab3178.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb150](../00bdb/00bdb150.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb170](../00bdb/00bdb170.md)

## 関連文字列（未確認候補）

~~~text
"GamatotoExpedition.csv"
"GamatotoExpedition_Limit.csv"
"GamatotoExpedition_Log_%d_%@.csv"
"GamatotoExpedition_Members.csv"
"GamatotoExpedition_Members_name_%@.csv"
"GamatotoExpedition_Message_%@.csv"
"GamatotoExpedition_Stage.csv"
"GamatotoExpedition_Stage_EVENT.csv"
"GamatotoExpedition_Stage_Free_%@.csv"
"GamatotoExpedition_Stage_nameEvent_%@.csv"
"GamatotoExpedition_Stage_name_%@.csv"
~~~

## 疑似コード / UTF-8 29223 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00ab1ecc(long param_1)

{
  bool bVar1;
  long lVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined *puVar8;
  undefined *puVar9;
  undefined *puVar10;
  byte bVar11;
  undefined7 uVar12;
  char cVar13;
  undefined6 uVar14;
  char cVar15;
  undefined **ppuVar16;
  undefined **ppuVar17;
  int iVar18;
  uint uVar19;
  undefined4 uVar20;
  char *pcVar21;
  ulong uVar22;
  ulong uVar23;
  undefined8 *puVar24;
  long lVar25;
  ulong *puVar26;
  ulong *puVar27;
  code *pcVar28;
  long lVar29;
  code *pcVar30;
  undefined8 uVar31;
  ulong *local_428;
  undefined8 *local_408;
  ulong *local_400;
  byte local_3e8 [16];
  void *local_3d8;
  byte local_3d0 [16];
  void *local_3c0;
  byte local_3b8 [16];
  void *local_3a8;
  byte local_3a0 [16];
  void *local_390;
  byte local_388 [16];
  void *local_378;
  byte local_370;
  undefined4 local_36f;
  undefined1 local_36b;
  void *local_360;
  byte local_358 [16];
  void *local_348;
  byte local_340;
  undefined7 uStack_33f;
  char cStack_338;
  undefined6 uStack_337;
  char cStack_331;
  char cStack_330;
  undefined6 uStack_32f;
  undefined1 uStack_329;
  undefined **local_328;
  void *pvStack_320;
  void *local_318;
  byte local_308;
  void *local_2f8;
  long local_2e0;
  undefined *local_2d8 [8];
  byte local_298;
  void *local_288;
  undefined1 auStack_270 [160];
  undefined **local_1d0;
  void *local_1c8;
  void *local_1c0;
  byte local_1b0;
  void *local_1a0;
  long local_188;
  undefined *local_180 [8];
  byte local_140;
  void *local_130;
  undefined1 auStack_118 [160];
  long local_78;
  
  lVar2 = tpidr_el0;
  local_428 = (ulong *)(param_1 + 0x4482a0);
  local_78 = *(long *)(lVar2 + 0x28);
  puVar26 = (ulong *)(param_1 + 0x436c90);
  local_408 = (undefined8 *)(&DAT_00435744 + param_1);
  FUN_00464f48(&local_1d0);
  uVar3 = _UNK_002b1118;
  uVar31 = _DAT_002b1110;
  local_1d0 = &PTR_FUN_00be7d78;
  uVar23 = 0;
  while (uVar23 != 3) {
    pcVar21 = (char *)_Znwm(0x28);
    uVar7 = s_GamatotoExpedition_Log__d____csv_0029edfa._24_8_;
    uVar6 = s_GamatotoExpedition_Log__d____csv_0029edfa._16_8_;
    uVar5 = s_GamatotoExpedition_Log__d____csv_0029edfa._8_8_;
    uVar4 = s_GamatotoExpedition_Log__d____csv_0029edfa._0_8_;
    cStack_330 = (char)pcVar21;
    uStack_32f = (undefined6)((ulong)pcVar21 >> 8);
    uStack_329 = (undefined1)((ulong)pcVar21 >> 0x38);
    cStack_338 = (char)uVar3;
    uStack_337 = (undefined6)((ulong)uVar3 >> 8);
    cStack_331 = (char)((ulong)uVar3 >> 0x38);
    local_340 = (byte)uVar31;
    uStack_33f = (undefined7)((ulong)uVar31 >> 8);
    pcVar21[0x20] = '\0';
    local_370 = 8;
    *(undefined8 *)(pcVar21 + 8) = uVar5;
    *(undefined8 *)pcVar21 = uVar4;
    *(undefined8 *)(pcVar21 + 0x18) = uVar7;
    *(undefined8 *)(pcVar21 + 0x10) = uVar6;
    local_36f = 0x676e616c;
    local_36b = 0;
    FUN_00469f7c(local_358,&local_370);
    FUN_00459a90(&local_328,&local_340,uVar23 + 1 & 0xffffffff,local_358);
    uVar22 = FUN_00ab1234(&local_1d0,&local_328,0,0);
    if (((ulong)local_328 & 1) != 0) {
      _ZdlPv(local_318);
    }
    if ((local_358[0] & 1) != 0) {
      _ZdlPv(local_348);
    }
    if ((local_370 & 1) != 0) {
      _ZdlPv(local_360);
    }
    if ((local_340 & 1) != 0) {
      _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
    }
    if ((uVar22 & 1) != 0) {
      lVar29 = 0;
      puVar27 = puVar26;
      do {
        uVar22 = FUN_00465394(&local_1d0,0x2c);
        if ((uVar22 & 1) == 0) break;
        FUN_00464b8c(&local_328,&local_1d0,0);
        if ((*puVar27 & 1) != 0) {
          _ZdlPv((void *)puVar27[2]);
        }
        ppuVar16 = local_328;
        local_328 = (undefined **)CONCAT71(local_328._1_7_,6);
        ppuVar17 = local_328;
        *(undefined2 *)((ulong)&local_328 | 1) = 0xbcef;
        puVar27[1] = (ulong)pvStack_320;
        *puVar27 = (ulong)ppuVar16;
        puVar27[2] = (ulong)local_318;
        *(undefined1 *)((undefined2 *)((ulong)&local_328 | 1) + 1) = 0xa0;
        local_328._5_3_ = SUB83(ppuVar16,5);
        local_328._0_4_ = (uint)ppuVar17;
        local_328._0_5_ = (uint5)(uint)local_328;
        uVar22 = FUN_00470ac0(puVar27,&local_328);
        if (((ulong)local_328 & 1) != 0) {
          _ZdlPv(local_318);
        }
        if ((uVar22 & 1) != 0) {
          *(int *)(param_1 + 0x448a20 + uVar23 * 4) = (int)lVar29;
          break;
        }
        lVar29 = lVar29 + 1;
        puVar27 = puVar27 + 3;
      } while (lVar29 != 0x200);
    }
    puVar26 = puVar26 + 0x600;
    FUN_00465780(&local_1d0);
    uVar23 = uVar23 + 1;
  }
  pcVar21 = (char *)_Znwm(0x28);
  uVar6 = s_GamatotoExpedition_Members_name__0029a517._16_8_;
  uVar5 = s_GamatotoExpedition_Members_name__0029a517._8_8_;
  uVar4 = s_GamatotoExpedition_Members_name__0029a517._0_8_;
  uVar31 = CONCAT26(s_GamatotoExpedition_Members_name__0029a517._30_2_,
                    s_GamatotoExpedition_Members_name__0029a517._24_6_);
  uVar3 = CONCAT62(s_GamatotoExpedition_Members_name__0029a517._32_6_,
                   s_GamatotoExpedition_Members_name__0029a517._30_2_);
  cStack_330 = (char)pcVar21;
  uStack_32f = (undefined6)((ulong)pcVar21 >> 8);
  uStack_329 = (undefined1)((ulong)pcVar21 >> 0x38);
  pcVar21[0x26] = '\0';
  *(undefined8 *)(pcVar21 + 8) = uVar5;
  *(undefined8 *)pcVar21 = uVar4;
  *(undefined8 *)(pcVar21 + 0x18) = uVar31;
  *(undefined8 *)(pcVar21 + 0x10) = uVar6;
  uVar4 = _UNK_002b1308;
  uVar31 = _DAT_002b1300;
  *(undefined8 *)(pcVar21 + 0x1e) = uVar3;
  local_370 = 8;
  cStack_338 = (char)uVar4;
  uStack_337 = (undefined6)((ulong)uVar4 >> 8);
  cStack_331 = (char)((ulong)uVar4 >> 0x38);
  local_340 = (byte)uVar31;
  uStack_33f = (undefined7)((ulong)uVar31 >> 8);
  local_36f = 0x676e616c;
  local_36b = 0;
  FUN_00469f7c(local_388,&local_370);
  FUN_0046ff30(&local_328,&local_340,local_388);
  uVar23 = FUN_00ab1234(&local_1d0,&local_328,0,0);
  if (((ulong)local_328 & 1) != 0) {
    _ZdlPv(local_318);
  }
  if ((local_388[0] & 1) != 0) {
    _ZdlPv(local_378);
  }
  if ((local_370 & 1) != 0) {
    _ZdlPv(local_360);
  }
  if ((local_340 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
  }
  if ((uVar23 & 1) != 0) {
    lVar25 = 0;
    pcVar28 = FUN_0043fc8c + param_1 + 4;
    lVar29 = param_1 + 0x436080;
    do {
      uVar23 = FUN_00465394(&local_1d0,0x2c);
      if ((uVar23 & 1) == 0) break;
      iVar18 = FUN_00464a64(&local_1d0,0);
      *(int *)(lVar29 + lVar25 * 0xc) = iVar18;
      if (iVar18 != -1) {
        uVar20 = FUN_00464a64(&local_1d0,1);
        *(undefined4 *)(lVar29 + lVar25 * 0xc + 4) = uVar20;
        uVar20 = FUN_00464a64(&local_1d0,2);
        uVar19 = 3;
        *(undefined4 *)(lVar29 + lVar25 * 0xc + 8) = uVar20;
        pcVar30 = pcVar28;
        while( true ) {
          FUN_00464b8c(&local_328,&local_1d0,uVar19);
          if (((byte)*pcVar30 & 1) != 0) {
            _ZdlPv(*(void **)(pcVar30 + 0x10));
          }
          *(void **)(pcVar30 + 8) = pvStack_320;
          *(undefined ***)pcVar30 = local_328;
          *(void **)(pcVar30 + 0x10) = local_318;
          if (5 < uVar19) break;
          uVar19 = uVar19 + 1;
          pcVar30 = pcVar30 + 0x18;
        }
      }
      lVar25 = lVar25 + 1;
      pcVar28 = pcVar28 + 0x60;
    } while (lVar25 != 0x101);
  }
  FUN_00465780(&local_1d0);
  pcVar21 = (char *)_Znwm(0x28);
  uVar5 = s_GamatotoExpedition_Message____cs_002a2c2d._24_8_;
  uVar4 = s_GamatotoExpedition_Message____cs_002a2c2d._16_8_;
  uVar3 = s_GamatotoExpedition_Message____cs_002a2c2d._8_8_;
  uVar31 = s_GamatotoExpedition_Message____cs_002a2c2d._0_8_;
  cStack_330 = (char)pcVar21;
  uStack_32f = (undefined6)((ulong)pcVar21 >> 8);
  uStack_329 = (undefined1)((ulong)pcVar21 >> 0x38);
  cStack_338 = (char)_UNK_002b1048;
  uStack_337 = (undefined6)((ulong)_UNK_002b1048 >> 8);
  cStack_331 = (char)((ulong)_UNK_002b1048 >> 0x38);
  local_340 = (byte)_DAT_002b1040;
  uStack_33f = (undefined7)((ulong)_DAT_002b1040 >> 8);
  pcVar21[0x20] = 'v';
  pcVar21[0x21] = '\0';
  local_370 = 8;
  *(undefined8 *)(pcVar21 + 8) = uVar3;
  *(undefined8 *)pcVar21 = uVar31;
  *(undefined8 *)(pcVar21 + 0x18) = uVar5;
  *(undefined8 *)(pcVar21 + 0x10) = uVar4;
  local_36f = 0x676e616c;
  local_36b = 0;
  FUN_00469f7c(local_3a0,&local_370);
  FUN_0046ff30(&local_328,&local_340,local_3a0);
  uVar23 = FUN_00ab1234(&local_1d0,&local_328,0,0);
  if (((ulong)local_328 & 1) != 0) {
    _ZdlPv(local_318);
  }
  if ((local_3a0[0] & 1) != 0) {
    _ZdlPv(local_390);
  }
  if ((local_370 & 1) != 0) {
    _ZdlPv(local_360);
  }
  if ((local_340 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
  }
  if ((uVar23 & 1) != 0) {
    lVar29 = 0;
    puVar26 = (ulong *)(param_1 + 0x445cf0);
    do {
      uVar23 = FUN_00465394(&local_1d0,0x2c);
      if ((uVar23 & 1) == 0) break;
      puVar27 = puVar26;
      uVar23 = 0;
      do {
        FUN_00464b8c(&local_328,&local_1d0,uVar23 & 0xffffffff);
        if ((*puVar27 & 1) != 0) {
          _ZdlPv((void *)puVar27[2]);
        }
        ppuVar16 = local_328;
        local_328 = (undefined **)CONCAT71(local_328._1_7_,6);
        ppuVar17 = local_328;
        *(undefined2 *)((ulong)&local_328 | 1) = 0xbcef;
        puVar27[1] = (ulong)pvStack_320;
        *puVar27 = (ulong)ppuVar16;
        puVar27[2] = (ulong)local_318;
        *(undefined1 *)((undefined2 *)((ulong)&local_328 | 1) + 1) = 0xa0;
        local_328._5_3_ = SUB83(ppuVar16,5);
        local_328._0_4_ = (uint)ppuVar17;
        local_328._0_5_ = (uint5)(uint)local_328;
        uVar19 = FUN_00470ac0(puVar27,&local_328);
        if (((ulong)local_328 & 1) != 0) {
          _ZdlPv(local_318);
        }
        puVar27 = puVar27 + 3;
        bVar1 = uVar23 < 4;
        uVar23 = uVar23 + 1;
      } while (bVar1 && (uVar19 & 1) == 0);
      lVar29 = lVar29 + 1;
      puVar26 = puVar26 + 0xf;
    } while (lVar29 != 0x2a);
  }
  FUN_00465780(&local_1d0);
  pcVar21 = (char *)_Znwm(0x28);
  uVar5 = s_GamatotoExpedition_Stage_Free____002b038c._24_8_;
  uVar4 = s_GamatotoExpedition_Stage_Free____002b038c._16_8_;
  uVar3 = s_GamatotoExpedition_Stage_Free____002b038c._8_8_;
  uVar31 = s_GamatotoExpedition_Stage_Free____002b038c._0_8_;
  cStack_330 = (char)pcVar21;
  uStack_32f = (undefined6)((ulong)pcVar21 >> 8);
  uStack_329 = (undefined1)((ulong)pcVar21 >> 0x38);
  cStack_338 = (char)_UNK_002b1628;
  cVar13 = cStack_338;
  uStack_337 = (undefined6)((ulong)_UNK_002b1628 >> 8);
  uVar14 = uStack_337;
  cStack_331 = (char)((ulong)_UNK_002b1628 >> 0x38);
  cVar15 = cStack_331;
  local_340 = (byte)_DAT_002b1620;
  bVar11 = local_340;
  uStack_33f = (undefined7)((ulong)_DAT_002b1620 >> 8);
  uVar12 = uStack_33f;
  local_370 = 8;
  pcVar21[0x20] = '.';
  pcVar21[0x21] = 'c';
  pcVar21[0x22] = 's';
  pcVar21[0x23] = 'v';
  *(undefined8 *)(pcVar21 + 8) = uVar3;
  *(undefined8 *)pcVar21 = uVar31;
  *(undefined8 *)(pcVar21 + 0x18) = uVar5;
  *(undefined8 *)(pcVar21 + 0x10) = uVar4;
  pcVar21[0x24] = '\0';
  local_36f = 0x676e616c;
  local_36b = 0;
  FUN_00469f7c(local_3b8,&local_370);
  FUN_0046ff30(&local_328,&local_340,local_3b8);
  uVar23 = FUN_00ab1234(&local_1d0,&local_328,0,0);
  if (((ulong)local_328 & 1) != 0) {
    _ZdlPv(local_318);
  }
  if ((local_3b8[0] & 1) != 0) {
    _ZdlPv(local_3a8);
  }
  if ((local_370 & 1) != 0) {
    _ZdlPv(local_360);
  }
  if ((local_340 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
  }
  if ((uVar23 & 1) != 0) {
    lVar29 = 0x40;
    local_400 = (ulong *)(param_1 + 0x4470a0);
    do {
      uVar23 = FUN_00465394(&local_1d0,0x2c);
      if ((uVar23 & 1) == 0) break;
      FUN_00464b8c(&local_328,&local_1d0,0);
      if ((*local_400 & 1) != 0) {
        _ZdlPv((void *)local_400[2]);
      }
      local_400[1] = (ulong)pvStack_320;
      *local_400 = (ulong)local_328;
      local_400[2] = (ulong)local_318;
      FUN_00464b8c(&local_328,&local_1d0,1);
      if ((local_400[3] & 1) != 0) {
        _ZdlPv((void *)local_400[5]);
      }
      local_400[4] = (ulong)pvStack_320;
      local_400[3] = (ulong)local_328;
      local_400[5] = (ulong)local_318;
      FUN_00464b8c(&local_328,&local_1d0,2);
      if ((local_400[6] & 1) != 0) {
        _ZdlPv((void *)local_400[8]);
      }
      lVar29 = lVar29 + -1;
      local_400[7] = (ulong)pvStack_320;
      local_400[6] = (ulong)local_328;
      local_400[8] = (ulong)local_318;
      local_400 = local_400 + 9;
    } while (lVar29 != 0);
  }
  FUN_00465780(&local_1d0);
  pcVar21 = (char *)_Znwm(0x28);
  uVar5 = s_GamatotoExpedition_Stage_name____002b03b1._24_8_;
  uVar4 = s_GamatotoExpedition_Stage_name____002b03b1._16_8_;
  uVar3 = s_GamatotoExpedition_Stage_name____002b03b1._8_8_;
  uVar31 = s_GamatotoExpedition_Stage_name____002b03b1._0_8_;
  cStack_330 = (char)pcVar21;
  uStack_32f = (undefined6)((ulong)pcVar21 >> 8);
  uStack_329 = (undefined1)((ulong)pcVar21 >> 0x38);
  pcVar21[0x20] = '.';
  pcVar21[0x21] = 'c';
  pcVar21[0x22] = 's';
  pcVar21[0x23] = 'v';
  local_370 = 8;
  *(undefined8 *)(pcVar21 + 8) = uVar3;
  *(undefined8 *)pcVar21 = uVar31;
  *(undefined8 *)(pcVar21 + 0x18) = uVar5;
  *(undefined8 *)(pcVar21 + 0x10) = uVar4;
  pcVar21[0x24] = '\0';
  local_36f = 0x676e616c;
  local_36b = 0;
  local_340 = bVar11;
  uStack_33f = uVar12;
  cStack_338 = cVar13;
  uStack_337 = uVar14;
  cStack_331 = cVar15;
  FUN_00469f7c(local_3d0,&local_370);
  FUN_0046ff30(&local_328,&local_340,local_3d0);
  uVar23 = FUN_00ab1234(&local_1d0,&local_328,0,0);
  if (((ulong)local_328 & 1) != 0) {
    _ZdlPv(local_318);
  }
  if ((local_3d0[0] & 1) != 0) {
    _ZdlPv(local_3c0);
  }
  if ((local_370 & 1) != 0) {
    _ZdlPv(local_360);
  }
  if ((local_340 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
  }
  if ((uVar23 & 1) != 0) {
    lVar29 = 0x40;
    do {
      uVar23 = FUN_00465394(&local_1d0,0x2c);
      if ((uVar23 & 1) == 0) break;
      FUN_00464b8c(&local_328,&local_1d0,0);
      if ((*local_428 & 1) != 0) {
        _ZdlPv((void *)local_428[2]);
      }
      lVar29 = lVar29 + -1;
      local_428[1] = (ulong)pvStack_320;
      *local_428 = (ulong)local_328;
      local_428[2] = (ulong)local_318;
      local_428 = local_428 + 3;
    } while (lVar29 != 0);
  }
  FUN_00465780(&local_1d0);
  pcVar21 = (char *)_Znwm(0x30);
  uVar4 = s_GamatotoExpedition_Stage_nameEve_002a6072._16_8_;
  uVar3 = s_GamatotoExpedition_Stage_nameEve_002a6072._0_8_;
  uVar31 = CONCAT71(s_GamatotoExpedition_Stage_nameEve_002a6072._25_7_,
                    s_GamatotoExpedition_Stage_nameEve_002a6072[0x18]);
  cStack_330 = (char)pcVar21;
  uStack_32f = (undefined6)((ulong)pcVar21 >> 8);
  uStack_329 = (undefined1)((ulong)pcVar21 >> 0x38);
  cStack_338 = (char)_UNK_002b0f18;
  uStack_337 = (undefined6)((ulong)_UNK_002b0f18 >> 8);
  cStack_331 = (char)((ulong)_UNK_002b0f18 >> 0x38);
  local_340 = (byte)_DAT_002b0f10;
  uStack_33f = (undefined7)((ulong)_DAT_002b0f10 >> 8);
  *(undefined8 *)(pcVar21 + 8) = s_GamatotoExpedition_Stage_nameEve_002a6072._8_8_;
  *(undefined8 *)pcVar21 = uVar3;
  *(undefined8 *)(pcVar21 + 0x18) = uVar31;
  *(undefined8 *)(pcVar21 + 0x10) = uVar4;
  uVar31 = CONCAT17(s_GamatotoExpedition_Stage_nameEve_002a6072[0x20],
                    s_GamatotoExpedition_Stage_nameEve_002a6072._25_7_);
  local_370 = 8;
  *(undefined8 *)(pcVar21 + 0x21) = s_GamatotoExpedition_Stage_nameEve_002a6072._33_8_;
  *(undefined8 *)(pcVar21 + 0x19) = uVar31;
  pcVar21[0x29] = '\0';
  local_36f = 0x676e616c;
  local_36b = 0;
  FUN_00469f7c(local_3e8,&local_370);
  FUN_0046ff30(&local_328,&local_340,local_3e8);
  uVar23 = FUN_00ab1234(&local_1d0,&local_328,0,0);
  if (((ulong)local_328 & 1) != 0) {
    _ZdlPv(local_318);
  }
  if ((local_3e8[0] & 1) != 0) {
    _ZdlPv(local_3d8);
  }
  if ((local_370 & 1) != 0) {
    _ZdlPv(local_360);
  }
  if ((local_340 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
  }
  if ((uVar23 & 1) != 0) {
    lVar29 = 0x10;
    puVar26 = (ulong *)(param_1 + 0x4488a0);
    do {
      uVar23 = FUN_00465394(&local_1d0,0x2c);
      if ((uVar23 & 1) == 0) break;
      FUN_00464b8c(&local_328,&local_1d0,0);
      if ((*puVar26 & 1) != 0) {
        _ZdlPv((void *)puVar26[2]);
      }
      lVar29 = lVar29 + -1;
      puVar26[1] = (ulong)pvStack_320;
      *puVar26 = (ulong)local_328;
      puVar26[2] = (ulong)local_318;
      puVar26 = puVar26 + 3;
    } while (lVar29 != 0);
  }
  FUN_00465780(&local_1d0);
  FUN_00464f48(&local_328);
  local_328 = &PTR_FUN_00be7d78;
  pcVar21 = (char *)_Znwm(0x20);
  uVar6 = _UNK_002b1b78;
  uVar5 = _DAT_002b1b70;
  uVar4 = s_GamatotoExpedition_Limit_csv_00296367._20_8_;
  uVar3 = s_GamatotoExpedition_Limit_csv_00296367._0_8_;
  uVar31 = CONCAT44(s_GamatotoExpedition_Limit_csv_00296367._16_4_,
                    s_GamatotoExpedition_Limit_csv_00296367._12_4_);
  cStack_330 = (char)pcVar21;
  uStack_32f = (undefined6)((ulong)pcVar21 >> 8);
  uStack_329 = (undefined1)((ulong)pcVar21 >> 0x38);
  *(ulong *)(pcVar21 + 8) =
       CONCAT44(s_GamatotoExpedition_Limit_csv_00296367._12_4_,
                s_GamatotoExpedition_Limit_csv_00296367._8_4_);
  *(undefined8 *)pcVar21 = uVar3;
  *(undefined8 *)(pcVar21 + 0x14) = uVar4;
  *(undefined8 *)(pcVar21 + 0xc) = uVar31;
  cStack_338 = (char)uVar6;
  cVar13 = cStack_338;
  uStack_337 = (undefined6)((ulong)uVar6 >> 8);
  uVar14 = uStack_337;
  cStack_331 = (char)((ulong)uVar6 >> 0x38);
  cVar15 = cStack_331;
  local_340 = (byte)uVar5;
  bVar11 = local_340;
  uStack_33f = (undefined7)((ulong)uVar5 >> 8);
  uVar12 = uStack_33f;
  pcVar21[0x1c] = '\0';
  uVar23 = FUN_00ab1234(&local_328,&local_340,0,0);
  if ((local_340 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
  }
  if ((uVar23 & 1) != 0) {
    FUN_00464a44(&local_328);
    uVar20 = FUN_00464a64(&local_328,0);
    *(undefined4 *)(param_1 + 0x431ef8) = uVar20;
    uVar20 = FUN_00464a64(&local_328,1);
    *(undefined4 *)(param_1 + 0x431efc) = uVar20;
    uVar20 = FUN_00464a64(&local_328,2);
    *(undefined4 *)(param_1 + 0x431f00) = uVar20;
  }
  FUN_00465780(&local_328);
  pcVar21 = (char *)_Znwm(0x20);
  uVar4 = s_GamatotoExpedition_Stage_csv_002a0e22._20_8_;
  uVar3 = s_GamatotoExpedition_Stage_csv_002a0e22._0_8_;
  cStack_330 = (char)pcVar21;
  uStack_32f = (undefined6)((ulong)pcVar21 >> 8);
  uStack_329 = (undefined1)((ulong)pcVar21 >> 0x38);
  uVar31 = CONCAT44(s_GamatotoExpedition_Stage_csv_002a0e22._16_4_,
                    s_GamatotoExpedition_Stage_csv_002a0e22._12_4_);
  *(ulong *)(pcVar21 + 8) =
       CONCAT44(s_GamatotoExpedition_Stage_csv_002a0e22._12_4_,
                s_GamatotoExpedition_Stage_csv_002a0e22._8_4_);
  *(undefined8 *)pcVar21 = uVar3;
  *(undefined8 *)(pcVar21 + 0x14) = uVar4;
  *(undefined8 *)(pcVar21 + 0xc) = uVar31;
  pcVar21[0x1c] = '\0';
  local_340 = bVar11;
  uStack_33f = uVar12;
  cStack_338 = cVar13;
  uStack_337 = uVar14;
  cStack_331 = cVar15;
  uVar23 = FUN_00ab1234(&local_328,&local_340,0,0);
  if ((local_340 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
  }
  if ((uVar23 & 1) != 0) {
    lVar29 = 0;
    lVar25 = param_1 + 0x431f04;
    do {
      uVar23 = FUN_00464a44(&local_328);
      if ((uVar23 & 1) == 0) {
        puVar24 = (undefined8 *)(param_1 + 0x431f04 + lVar29 * 0xb4);
        *(undefined4 *)(puVar24 + 0x16) = 0xffffffff;
        puVar24[3] = 0xffffffffffffffff;
        puVar24[2] = 0xffffffffffffffff;
        puVar24[5] = 0xffffffffffffffff;
        puVar24[4] = 0xffffffffffffffff;
        puVar24[7] = 0xffffffffffffffff;
        puVar24[6] = 0xffffffffffffffff;
        puVar24[9] = 0xffffffffffffffff;
        puVar24[8] = 0xffffffffffffffff;
        puVar24[0xb] = 0xffffffffffffffff;
        puVar24[10] = 0xffffffffffffffff;
        puVar24[0xd] = 0xffffffffffffffff;
        puVar24[0xc] = 0xffffffffffffffff;
        puVar24[0xf] = 0xffffffffffffffff;
        puVar24[0xe] = 0xffffffffffffffff;
        puVar24[0x11] = 0xffffffffffffffff;
        puVar24[0x10] = 0xffffffffffffffff;
        puVar24[0x13] = 0xffffffffffffffff;
        puVar24[0x12] = 0xffffffffffffffff;
        puVar24[0x15] = 0xffffffffffffffff;
        puVar24[0x14] = 0xffffffffffffffff;
        puVar24[1] = 0xffffffffffffffff;
        *puVar24 = 0xffffffffffffffff;
      }
      else {
        uVar23 = 0;
        do {
          uVar20 = FUN_00464a64(&local_328,uVar23 & 0xffffffff);
          *(undefined4 *)(lVar25 + uVar23 * 4) = uVar20;
          uVar23 = uVar23 + 1;
        } while (uVar23 != 0x2d);
      }
      lVar29 = lVar29 + 1;
      lVar25 = lVar25 + 0xb4;
    } while (lVar29 != 0x40);
  }
  FUN_00465780(&local_328);
  pcVar21 = (char *)_Znwm(0x28);
  uVar7 = _UNK_002b1b88;
  uVar6 = _DAT_002b1b80;
  uVar5 = s_GamatotoExpedition_Stage_EVENT_c_002a3cdb._24_8_;
  uVar4 = s_GamatotoExpedition_Stage_EVENT_c_002a3cdb._16_8_;
  uVar3 = s_GamatotoExpedition_Stage_EVENT_c_002a3cdb._8_8_;
  uVar31 = s_GamatotoExpedition_Stage_EVENT_c_002a3cdb._0_8_;
  cStack_330 = (char)pcVar21;
  uStack_32f = (undefined6)((ulong)pcVar21 >> 8);
  uStack_329 = (undefined1)((ulong)pcVar21 >> 0x38);
  pcVar21[0x20] = 's';
  pcVar21[0x21] = 'v';
  cStack_338 = (char)uVar7;
  uStack_337 = (undefined6)((ulong)uVar7 >> 8);
  cStack_331 = (char)((ulong)uVar7 >> 0x38);
  local_340 = (byte)uVar6;
  uStack_33f = (undefined7)((ulong)uVar6 >> 8);
  *(undefined8 *)(pcVar21 + 8) = uVar3;
  *(undefined8 *)pcVar21 = uVar31;
  *(undefined8 *)(pcVar21 + 0x18) = uVar5;
  *(undefined8 *)(pcVar21 + 0x10) = uVar4;
  pcVar21[0x22] = '\0';
  uVar23 = FUN_00ab1234(&local_328,&local_340,0,0);
  if ((local_340 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
  }
  if ((uVar23 & 1) != 0) {
    lVar29 = 0;
    lVar25 = param_1 + 0x434c04;
    do {
      uVar23 = FUN_00464a44(&local_328);
      if ((uVar23 & 1) == 0) {
        puVar24 = (undefined8 *)(param_1 + 0x434c04 + lVar29 * 0xb4);
        *(undefined4 *)(puVar24 + 0x16) = 0xffffffff;
        puVar24[3] = 0xffffffffffffffff;
        puVar24[2] = 0xffffffffffffffff;
        puVar24[5] = 0xffffffffffffffff;
        puVar24[4] = 0xffffffffffffffff;
        puVar24[7] = 0xffffffffffffffff;
        puVar24[6] = 0xffffffffffffffff;
        puVar24[9] = 0xffffffffffffffff;
        puVar24[8] = 0xffffffffffffffff;
        puVar24[0xb] = 0xffffffffffffffff;
        puVar24[10] = 0xffffffffffffffff;
        puVar24[0xd] = 0xffffffffffffffff;
        puVar24[0xc] = 0xffffffffffffffff;
        puVar24[0xf] = 0xffffffffffffffff;
        puVar24[0xe] = 0xffffffffffffffff;
        puVar24[0x11] = 0xffffffffffffffff;
        puVar24[0x10] = 0xffffffffffffffff;
        puVar24[0x13] = 0xffffffffffffffff;
        puVar24[0x12] = 0xffffffffffffffff;
        puVar24[0x15] = 0xffffffffffffffff;
        puVar24[0x14] = 0xffffffffffffffff;
        puVar24[1] = 0xffffffffffffffff;
        *puVar24 = 0xffffffffffffffff;
      }
      else {
        uVar23 = 0;
        do {
          uVar20 = FUN_00464a64(&local_328,uVar23 & 0xffffffff);
          *(undefined4 *)(lVar25 + uVar23 * 4) = uVar20;
          uVar23 = uVar23 + 1;
        } while (uVar23 != 0x2d);
      }
      lVar29 = lVar29 + 1;
      lVar25 = lVar25 + 0xb4;
    } while (lVar29 != 0x10);
  }
  FUN_00465780(&local_328);
  local_340 = 0x2c;
  uStack_329 = 0;
  uStack_337._0_1_ = s_GamatotoExpedition_csv_002a8b76[8];
  uStack_337._1_1_ = s_GamatotoExpedition_csv_002a8b76[9];
  uStack_337._2_1_ = s_GamatotoExpedition_csv_002a8b76[10];
  uStack_337._3_1_ = s_GamatotoExpedition_csv_002a8b76[0xb];
  uStack_337._4_1_ = s_GamatotoExpedition_csv_002a8b76[0xc];
  uStack_337._5_1_ = s_GamatotoExpedition_csv_002a8b76[0xd];
  uStack_33f = (undefined7)s_GamatotoExpedition_csv_002a8b76._0_8_;
  cStack_338 = SUB81(s_GamatotoExpedition_csv_002a8b76._0_8_,7);
  cStack_331 = (char)s_GamatotoExpedition_csv_002a8b76._14_2_;
  cStack_330 = SUB21(s_GamatotoExpedition_csv_002a8b76._14_2_,1);
  uStack_32f._0_1_ = s_GamatotoExpedition_csv_002a8b76[0x10];
  uStack_32f._1_1_ = s_GamatotoExpedition_csv_002a8b76[0x11];
  uStack_32f._2_1_ = s_GamatotoExpedition_csv_002a8b76[0x12];
  uStack_32f._3_1_ = s_GamatotoExpedition_csv_002a8b76[0x13];
  uStack_32f._4_1_ = s_GamatotoExpedition_csv_002a8b76[0x14];
  uStack_32f._5_1_ = s_GamatotoExpedition_csv_002a8b76[0x15];
  uVar23 = FUN_00ab1234(&local_328,&local_340,0,0);
  if ((local_340 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
  }
  if ((uVar23 & 1) != 0) {
    lVar29 = 0x82;
    do {
      uVar23 = FUN_00464a44(&local_328);
      if ((uVar23 & 1) == 0) {
        *local_408 = 0xffffffffffffffff;
        local_408[1] = 0xffffffffffffffff;
      }
      else {
        uVar20 = FUN_00464a64(&local_328,0);
        *(undefined4 *)local_408 = uVar20;
        uVar20 = FUN_00464a64(&local_328,1);
        *(undefined4 *)((long)local_408 + 4) = uVar20;
        uVar20 = FUN_00464a64(&local_328,2);
        *(undefined4 *)(local_408 + 1) = uVar20;
        uVar20 = FUN_00464a64(&local_328,3);
        *(undefined4 *)((long)local_408 + 0xc) = uVar20;
      }
      lVar29 = lVar29 + -1;
      local_408 = local_408 + 2;
    } while (lVar29 != 0);
  }
  FUN_00465780(&local_328);
  pcVar21 = (char *)_Znwm(0x20);
  uVar6 = _UNK_002b0df8;
  uVar5 = _DAT_002b0df0;
  uVar4 = s_GamatotoExpedition_Members_csv_002a3cfe._22_8_;
  uVar3 = s_GamatotoExpedition_Members_csv_002a3cfe._0_8_;
  uVar31 = CONCAT62(s_GamatotoExpedition_Members_csv_002a3cfe._16_6_,
                    s_GamatotoExpedition_Members_csv_002a3cfe._14_2_);
  cStack_330 = (char)pcVar21;
  uStack_32f = (undefined6)((ulong)pcVar21 >> 8);
  uStack_329 = (undefined1)((ulong)pcVar21 >> 0x38);
  *(ulong *)(pcVar21 + 8) =
       CONCAT26(s_GamatotoExpedition_Members_csv_002a3cfe._14_2_,
                s_GamatotoExpedition_Members_csv_002a3cfe._8_6_);
  *(undefined8 *)pcVar21 = uVar3;
  *(undefined8 *)(pcVar21 + 0x16) = uVar4;
  *(undefined8 *)(pcVar21 + 0xe) = uVar31;
  cStack_338 = (char)uVar6;
  uStack_337 = (undefined6)((ulong)uVar6 >> 8);
  cStack_331 = (char)((ulong)uVar6 >> 0x38);
  local_340 = (byte)uVar5;
  uStack_33f = (undefined7)((ulong)uVar5 >> 8);
  pcVar21[0x1e] = '\0';
  uVar23 = FUN_00ab1234(&local_328,&local_340,0,0);
  if ((local_340 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_329,CONCAT61(uStack_32f,cStack_330)));
  }
  if ((uVar23 & 1) != 0) {
    lVar29 = 0;
    do {
      uVar23 = FUN_00464a44(&local_328);
      if ((uVar23 & 1) == 0) {
        uVar20 = 0xffffffff;
      }
      else {
        uVar20 = FUN_00464a64(&local_328,0);
      }
      *(undefined4 *)(param_1 + 0x435f64 + lVar29) = uVar20;
      lVar29 = lVar29 + 4;
    } while (lVar29 != 0x11c);
  }
  FUN_00465780(&local_328);
  FUN_006181e8(param_1 + 0x431290);
  FUN_00627d10(param_1 + 0x42f8f0);
  FUN_00692224(param_1 + 0x431730);
  FUN_006b5fcc(param_1 + 0x42f7c0);
  FUN_00ab3178(param_1 + 0x42f830);
  FUN_006b0f78(param_1 + 0x42f848);
  FUN_006b12cc(param_1 + 0x42f890);
  puVar10 = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1add0;
  puVar9 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1adc8
  ;
  puVar8 = PTR_DAT_00c1adc0;
  lVar29 = *(long *)
            PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1adc8
  ;
  local_328 = (undefined **)(PTR_DAT_00c1adc0 + 0x10);
  uVar31 = *(undefined8 *)
            (
            PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1adc8
            + 0x18);
  local_2e0 = lVar29;
  *(undefined8 *)((long)&local_2e0 + *(long *)(lVar29 + -0x18)) = uVar31;
  local_2d8[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1add0
                 + 0x10;
  if ((local_298 & 1) != 0) {
    _ZdlPv(local_288);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_2d8);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_2e0,puVar9 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_270);
  if ((local_308 & 1) != 0) {
    _ZdlPv(local_2f8);
  }
  if (pvStack_320 != (void *)0x0) {
    local_318 = pvStack_320;
    _ZdlPv(pvStack_320);
  }
  local_1d0 = (undefined **)(puVar8 + 0x10);
  local_188 = lVar29;
  *(undefined8 *)((long)&local_188 + *(long *)(lVar29 + -0x18)) = uVar31;
  local_180[0] = puVar10 + 0x10;
  if ((local_140 & 1) != 0) {
    _ZdlPv(local_130);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_180);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_188,puVar9 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_118);
  if ((local_1b0 & 1) != 0) {
    _ZdlPv(local_1a0);
  }
  if (local_1c8 != (void *)0x0) {
    local_1c0 = local_1c8;
    _ZdlPv(local_1c8);
  }
  if (*(long *)(lVar2 + 0x28) == local_78) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
