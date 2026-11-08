# 006efbbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "006efbbc",
  "name": "FUN_006efbbc",
  "size": 1264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dcb94c03561d462046e94fa27e7377c80d8c41076741e5a7bb4d5886f5519092",
  "source_text_sha256": "dcb94c03561d462046e94fa27e7377c80d8c41076741e5a7bb4d5886f5519092"
}
~~~

## 呼び出し元

- [009a311c](../009a3/009a311c.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00464a54](../00464/00464a54.md)
- [00464a64](../00464/00464a64.md)
- [00464b8c](../00464/00464b8c.md)
- [00464f48](../00464/00464f48.md)
- [00465680](../00465/00465680.md)
- [00465780](../00465/00465780.md)
- [006f0224](../006f0/006f0224.md)
- [006f02e0](../006f0/006f02e0.md)
- [006f02f4](../006f0/006f02f4.md)
- [00ab11f0](../00ab1/00ab11f0.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb100](../00bdb/00bdb100.md)
- [00bdb110](../00bdb/00bdb110.md)
- [00bdb120](../00bdb/00bdb120.md)
- [00bdb160](../00bdb/00bdb160.md)

## 関連文字列（未確認候補）

~~~text
"GatyaData_Option_ChanceAnimation.tsv"
~~~

## 疑似コード / UTF-8 9853 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_006efbbc(undefined8 *param_1)

{
  undefined8 *puVar1;
  long lVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined *puVar7;
  int iVar8;
  undefined4 uVar9;
  int iVar10;
  ulong uVar11;
  undefined8 *puVar12;
  undefined8 *puVar13;
  long lVar14;
  ulong uVar15;
  undefined8 *puVar16;
  ulong uVar17;
  char *pcVar18;
  void *pvVar19;
  long lVar20;
  void *pvVar21;
  undefined8 *puVar22;
  undefined8 *puVar23;
  long lVar24;
  char *local_1f0;
  char *pcStack_1e8;
  char *local_1e0;
  undefined8 *puStack_1d8;
  undefined8 *local_1d0;
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
  
  lVar2 = tpidr_el0;
  local_70 = *(long *)(lVar2 + 0x28);
  FUN_00464f48(&local_1c8);
  puVar1 = (undefined8 *)*param_1;
  puVar16 = (undefined8 *)param_1[1];
  local_1c8 = &PTR_FUN_00be7d28;
  while (puVar16 != puVar1) {
    puVar16 = puVar16 + -1;
    pvVar19 = (void *)*puVar16;
    *puVar16 = 0;
    if (pvVar19 != (void *)0x0) {
      puVar13 = *(undefined8 **)((long)pvVar19 + 8);
      if (puVar13 != (undefined8 *)0x0) {
                    /* try { // try from 006eff44 to 007eff4b has its CatchHandler @ 006f003c */
        puVar23 = *(undefined8 **)((long)pvVar19 + 0x10);
                    /* try { // try from 006eff4c to 007eff9b has its CatchHandler @ 006efee8 */
        puVar12 = puVar13;
        if (puVar23 != puVar13) {
          do {
            puVar23 = puVar23 + -1;
            pvVar21 = (void *)*puVar23;
            *puVar23 = 0;
            if (pvVar21 != (void *)0x0) {
              _ZdlPv(pvVar21);
            }
          } while (puVar23 != puVar13);
          puVar12 = *(undefined8 **)((long)pvVar19 + 8);
        }
        *(undefined8 **)((long)pvVar19 + 0x10) = puVar13;
        _ZdlPv(puVar12);
      }
      _ZdlPv(pvVar19);
    }
  }
  param_1[1] = puVar1;
  local_1e0 = (char *)_Znwm(0x28);
  pcStack_1e8 = _UNK_002b1628;
  local_1f0 = _DAT_002b1620;
  uVar6 = s_GatyaData_Option_ChanceAnimation_00293c35._24_8_;
  uVar5 = s_GatyaData_Option_ChanceAnimation_00293c35._16_8_;
  uVar4 = s_GatyaData_Option_ChanceAnimation_00293c35._8_8_;
  uVar3 = s_GatyaData_Option_ChanceAnimation_00293c35._0_8_;
  local_1e0[0x20] = '.';
  local_1e0[0x21] = 't';
  local_1e0[0x22] = 's';
  local_1e0[0x23] = 'v';
  *(undefined8 *)(local_1e0 + 8) = uVar4;
  *(undefined8 *)local_1e0 = uVar3;
  *(undefined8 *)(local_1e0 + 0x18) = uVar6;
  *(undefined8 *)(local_1e0 + 0x10) = uVar5;
  local_1e0[0x24] = '\0';
  uVar11 = FUN_00ab11f0(&local_1c8,&local_1f0,0,0);
  if (((ulong)local_1f0 & 1) != 0) {
    _ZdlPv(local_1e0);
  }
  if ((uVar11 & 1) != 0) {
    FUN_00464a54(&local_1c8);
    puVar1 = param_1 + 2;
    while ((uVar11 = FUN_00464a54(&local_1c8), (uVar11 & 1) != 0 &&
           (iVar8 = FUN_00465680(&local_1c8), 1 < iVar8))) {
      FUN_00464b8c(&local_1f0,&local_1c8,0);
      pcVar18 = (char *)((ulong)local_1f0 >> 1 & 0x7f);
      if (((ulong)local_1f0 & 1) != 0) {
        pcVar18 = pcStack_1e8;
      }
      if (((ulong)local_1f0 & 1) != 0) {
        _ZdlPv(local_1e0);
      }
      if (pcVar18 == (char *)0x0) break;
      puVar12 = (undefined8 *)_Znwm(0x20);
      puVar16 = (undefined8 *)param_1[1];
      puVar13 = (undefined8 *)param_1[2];
      puVar12[1] = 0;
      *puVar12 = 0;
      puVar12[3] = 0;
      puVar12[2] = 0;
      if (puVar16 < puVar13) {
        puVar22 = puVar16 + 1;
        *puVar16 = puVar12;
      }
      else {
        pcVar18 = (char *)*param_1;
        lVar24 = (long)puVar16 - (long)pcVar18 >> 3;
        uVar11 = lVar24 + 1;
        if (uVar11 >> 0x3d != 0) {
          if (*(long *)(lVar2 + 0x28) == local_70) {
            FUN_006f02e0(param_1);
LAB_006f0090:
            if (*(long *)(lVar2 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
              FUN_0041e380();
            }
          }
          goto LAB_006f0128;
        }
        uVar17 = (long)puVar13 - (long)pcVar18 >> 2;
        if (uVar17 <= uVar11) {
          uVar17 = uVar11;
        }
        if (0x7ffffffffffffff7 < (ulong)((long)puVar13 - (long)pcVar18)) {
          uVar17 = 0x1fffffffffffffff;
        }
        local_1d0 = puVar1;
        if (uVar17 == 0) {
          pvVar19 = (void *)0x0;
        }
        else {
          if (uVar17 >> 0x3d != 0) goto LAB_006f0090;
          pvVar19 = (void *)_Znwm(uVar17 << 3);
        }
        puVar23 = (undefined8 *)((long)pvVar19 + lVar24 * 8);
        puVar22 = puVar23 + 1;
        *puVar23 = puVar12;
        memcpy(pvVar19,pcVar18,(long)puVar16 - (long)pcVar18);
        *param_1 = pvVar19;
        param_1[1] = puVar22;
        param_1[2] = (void *)((long)pvVar19 + uVar17 * 8);
        local_1f0 = pcVar18;
        pcStack_1e8 = pcVar18;
        local_1e0 = pcVar18;
        puStack_1d8 = puVar13;
        FUN_006f0224(&local_1f0);
      }
      param_1[1] = puVar22;
      uVar9 = FUN_00464a64(&local_1c8,0);
      **(undefined4 **)(param_1[1] + -8) = uVar9;
      uVar9 = FUN_00464a64(&local_1c8,1);
      iVar8 = 4;
      *(undefined4 *)(*(long *)(param_1[1] + -8) + 4) = uVar9;
      while( true ) {
        iVar10 = FUN_00465680(&local_1c8);
        if (iVar10 <= iVar8) break;
        lVar24 = *(long *)(param_1[1] + -8);
        puVar13 = (undefined8 *)_Znwm(0xc);
        *(undefined4 *)(puVar13 + 1) = 0;
        *puVar13 = 0;
        puVar16 = *(undefined8 **)(lVar24 + 0x10);
        if (puVar16 < *(undefined8 **)(lVar24 + 0x18)) {
          puVar23 = puVar16 + 1;
          *puVar16 = puVar13;
        }
        else {
          lVar20 = (long)puVar16 - *(long *)(lVar24 + 8) >> 3;
          uVar11 = lVar20 + 1;
          if (uVar11 >> 0x3d != 0) {
                    /* catch() { ... } // from try @ 006effa4 with catch @ 006f004c */
            if (*(long *)(lVar2 + 0x28) == local_70) {
              FUN_006f02f4(lVar24 + 8);
LAB_006f005c:
              if (*(long *)(lVar2 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
                FUN_0041e380();
              }
            }
            goto LAB_006f0128;
          }
          uVar15 = (long)*(undefined8 **)(lVar24 + 0x18) - *(long *)(lVar24 + 8);
          uVar17 = (long)uVar15 >> 2;
          if (uVar17 <= uVar11) {
            uVar17 = uVar11;
          }
          if (0x7ffffffffffffff7 < uVar15) {
            uVar17 = 0x1fffffffffffffff;
          }
          if (uVar17 == 0) {
            lVar14 = 0;
          }
          else {
            if (uVar17 >> 0x3d != 0) goto LAB_006f005c;
            lVar14 = _Znwm(uVar17 << 3);
            puVar16 = *(undefined8 **)(lVar24 + 0x10);
          }
          puVar12 = (undefined8 *)(lVar14 + lVar20 * 8);
          puVar23 = puVar12 + 1;
          *puVar12 = puVar13;
          pvVar19 = *(void **)(lVar24 + 8);
          pvVar21 = (void *)((long)puVar12 - ((long)puVar16 - (long)pvVar19));
          memcpy(pvVar21,pvVar19,(long)puVar16 - (long)pvVar19);
          *(void **)(lVar24 + 8) = pvVar21;
          *(undefined8 **)(lVar24 + 0x10) = puVar23;
          *(ulong *)(lVar24 + 0x18) = lVar14 + uVar17 * 8;
          if (pvVar19 != (void *)0x0) {
            _ZdlPv(pvVar19);
          }
        }
        *(undefined8 **)(lVar24 + 0x10) = puVar23;
        uVar9 = FUN_00464a64(&local_1c8,iVar8 + -2);
        **(undefined4 **)(*(long *)(*(long *)(param_1[1] + -8) + 0x10) + -8) = uVar9;
        uVar9 = FUN_00464a64(&local_1c8,iVar8 + -1);
                    /* catch() { ... } // from try @ 006eff4c with catch @ 006efee8
                       catch() { ... } // from try @ 006effc0 with catch @ 006efee8 */
        *(undefined4 *)(*(long *)(*(long *)(*(long *)(param_1[1] + -8) + 0x10) + -8) + 4) = uVar9;
        uVar9 = FUN_00464a64(&local_1c8,iVar8);
        iVar8 = iVar8 + 3;
        *(undefined4 *)(*(long *)(*(long *)(*(long *)(param_1[1] + -8) + 0x10) + -8) + 8) = uVar9;
      }
    }
    FUN_00465780(&local_1c8);
  }
  puVar7 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ad78
  ;
  local_180 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ad78
  ;
  local_1c8 = (undefined **)(PTR_DAT_00c1ad70 + 0x10);
                    /* try { // try from 006eff9c to 007effa3 has its CatchHandler @ 006f002c */
                    /* try { // try from 006effa4 to 007effbf has its CatchHandler @ 006f004c */
  *(undefined8 *)((long)&local_180 + *(long *)(local_180 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ad78 +
        0x18);
  local_178[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ad80
                 + 0x10;
                    /* try { // try from 006effc0 to 007f00af has its CatchHandler @ 006efee8 */
  if ((local_138 & 1) != 0) {
    _ZdlPv(local_128);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_178);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_180,puVar7 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_110);
  if ((local_1a8 & 1) != 0) {
    _ZdlPv(local_198);
  }
  if (local_1c0 != (void *)0x0) {
    local_1b8 = local_1c0;
    _ZdlPv(local_1c0);
  }
  if (*(long *)(lVar2 + 0x28) == local_70) {
                    /* catch() { ... } // from try @ 006eff9c with catch @ 006f002c */
                    /* catch() { ... } // from try @ 006eff44 with catch @ 006f003c */
    return;
  }
LAB_006f0128:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
