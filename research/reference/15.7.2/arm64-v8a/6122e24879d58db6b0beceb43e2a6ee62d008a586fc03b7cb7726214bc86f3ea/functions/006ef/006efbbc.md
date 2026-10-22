# 006efbbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](006efbbc.md)

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
  "source_sha256": "6f9f0d92c964aa90181a9404f0f8d9806d0f6ea306bd23e8235b0981aa9ccf64",
  "source_text_sha256": "6f9f0d92c964aa90181a9404f0f8d9806d0f6ea306bd23e8235b0981aa9ccf64"
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
- [00ab1128](../00ab1/00ab1128.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb050](../00bdb/00bdb050.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb070](../00bdb/00bdb070.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

## 関連文字列（未確認候補）

~~~text
"GatyaData_Option_ChanceAnimation.tsv"
~~~
## 疑似コード 1/1 / UTF-8 10131 bytes

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
  int iVar7;
  undefined4 uVar8;
  int iVar9;
  ulong uVar10;
  undefined8 *puVar11;
  undefined8 *puVar12;
  void *pvVar13;
  ulong uVar14;
  undefined8 *puVar15;
  ulong uVar16;
  char *pcVar17;
  void *pvVar18;
  long lVar19;
  void *__dest;
  undefined8 *puVar20;
  undefined8 *puVar21;
  long lVar22;
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
  basic_ios<char,std::__ndk1::char_traits<char>> abStack_110 [160];
  long local_70;
  
  lVar2 = tpidr_el0;
  local_70 = *(long *)(lVar2 + 0x28);
  FUN_00464f48(&local_1c8);
  puVar1 = (undefined8 *)*param_1;
  puVar15 = (undefined8 *)param_1[1];
  local_1c8 = &PTR_FUN_00be7c78;
  while (puVar15 != puVar1) {
    puVar15 = puVar15 + -1;
    pvVar13 = (void *)*puVar15;
    *puVar15 = 0;
    if (pvVar13 != (void *)0x0) {
      puVar12 = *(undefined8 **)((long)pvVar13 + 8);
      if (puVar12 != (undefined8 *)0x0) {
                    /* try { // try from 006eff44 to 007eff4b has its CatchHandler @ 006f003c */
        puVar21 = *(undefined8 **)((long)pvVar13 + 0x10);
                    /* try { // try from 006eff4c to 007eff9b has its CatchHandler @ 006efee8 */
        puVar11 = puVar12;
        if (puVar21 != puVar12) {
          do {
            puVar21 = puVar21 + -1;
            pvVar18 = (void *)*puVar21;
            *puVar21 = 0;
            if (pvVar18 != (void *)0x0) {
              operator_delete(pvVar18);
            }
          } while (puVar21 != puVar12);
          puVar11 = *(undefined8 **)((long)pvVar13 + 8);
        }
        *(undefined8 **)((long)pvVar13 + 0x10) = puVar12;
        operator_delete(puVar11);
      }
      operator_delete(pvVar13);
    }
  }
  param_1[1] = puVar1;
  local_1e0 = operator_new(0x28);
  pcStack_1e8 = _UNK_002b1628;
  local_1f0 = _DAT_002b1620;
  uVar6 = s_GatyaData_Option_ChanceAnimation_00293ba8._24_8_;
  uVar5 = s_GatyaData_Option_ChanceAnimation_00293ba8._16_8_;
  uVar4 = s_GatyaData_Option_ChanceAnimation_00293ba8._8_8_;
  uVar3 = s_GatyaData_Option_ChanceAnimation_00293ba8._0_8_;
  local_1e0[0x20] = '.';
  local_1e0[0x21] = 't';
  local_1e0[0x22] = 's';
  local_1e0[0x23] = 'v';
  *(undefined8 *)(local_1e0 + 8) = uVar4;
  *(undefined8 *)local_1e0 = uVar3;
  *(undefined8 *)(local_1e0 + 0x18) = uVar6;
  *(undefined8 *)(local_1e0 + 0x10) = uVar5;
  local_1e0[0x24] = '\0';
  uVar10 = FUN_00ab1128(&local_1c8,&local_1f0,0,0);
  if (((ulong)local_1f0 & 1) != 0) {
    operator_delete(local_1e0);
  }
  if ((uVar10 & 1) != 0) {
    FUN_00464a54(&local_1c8);
    puVar1 = param_1 + 2;
    while ((uVar10 = FUN_00464a54(&local_1c8), (uVar10 & 1) != 0 &&
           (iVar7 = FUN_00465680(&local_1c8), 1 < iVar7))) {
      FUN_00464b8c(&local_1f0,&local_1c8,0);
      pcVar17 = (char *)((ulong)local_1f0 >> 1 & 0x7f);
      if (((ulong)local_1f0 & 1) != 0) {
        pcVar17 = pcStack_1e8;
      }
      if (((ulong)local_1f0 & 1) != 0) {
        operator_delete(local_1e0);
      }
      if (pcVar17 == (char *)0x0) break;
      puVar11 = operator_new(0x20);
      puVar15 = (undefined8 *)param_1[1];
      puVar12 = (undefined8 *)param_1[2];
      puVar11[1] = 0;
      *puVar11 = 0;
      puVar11[3] = 0;
      puVar11[2] = 0;
      if (puVar15 < puVar12) {
        puVar20 = puVar15 + 1;
        *puVar15 = puVar11;
      }
      else {
        pcVar17 = (char *)*param_1;
        lVar22 = (long)puVar15 - (long)pcVar17 >> 3;
        uVar10 = lVar22 + 1;
        if (uVar10 >> 0x3d != 0) {
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
        uVar16 = (long)puVar12 - (long)pcVar17 >> 2;
        if (uVar16 <= uVar10) {
          uVar16 = uVar10;
        }
        if (0x7ffffffffffffff7 < (ulong)((long)puVar12 - (long)pcVar17)) {
          uVar16 = 0x1fffffffffffffff;
        }
        local_1d0 = puVar1;
        if (uVar16 == 0) {
          pvVar13 = (void *)0x0;
        }
        else {
          if (uVar16 >> 0x3d != 0) goto LAB_006f0090;
          pvVar13 = operator_new(uVar16 << 3);
        }
        puVar21 = (undefined8 *)((long)pvVar13 + lVar22 * 8);
        puVar20 = puVar21 + 1;
        *puVar21 = puVar11;
        memcpy(pvVar13,pcVar17,(long)puVar15 - (long)pcVar17);
        *param_1 = pvVar13;
        param_1[1] = puVar20;
        param_1[2] = (void *)((long)pvVar13 + uVar16 * 8);
        local_1f0 = pcVar17;
        pcStack_1e8 = pcVar17;
        local_1e0 = pcVar17;
        puStack_1d8 = puVar12;
        FUN_006f0224(&local_1f0);
      }
      param_1[1] = puVar20;
      uVar8 = FUN_00464a64(&local_1c8,0);
      **(undefined4 **)(param_1[1] + -8) = uVar8;
      uVar8 = FUN_00464a64(&local_1c8,1);
      iVar7 = 4;
      *(undefined4 *)(*(long *)(param_1[1] + -8) + 4) = uVar8;
      while( true ) {
        iVar9 = FUN_00465680(&local_1c8);
        if (iVar9 <= iVar7) break;
        lVar22 = *(long *)(param_1[1] + -8);
        puVar12 = operator_new(0xc);
        *(undefined4 *)(puVar12 + 1) = 0;
        *puVar12 = 0;
        puVar15 = *(undefined8 **)(lVar22 + 0x10);
        if (puVar15 < *(undefined8 **)(lVar22 + 0x18)) {
          puVar21 = puVar15 + 1;
          *puVar15 = puVar12;
        }
        else {
          lVar19 = (long)puVar15 - *(long *)(lVar22 + 8) >> 3;
          uVar10 = lVar19 + 1;
          if (uVar10 >> 0x3d != 0) {
                    /* catch() { ... } // from try @ 006effa4 with catch @ 006f004c */
            if (*(long *)(lVar2 + 0x28) == local_70) {
              FUN_006f02f4(lVar22 + 8);
LAB_006f005c:
              if (*(long *)(lVar2 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
                FUN_0041e380();
              }
            }
            goto LAB_006f0128;
          }
          uVar14 = (long)*(undefined8 **)(lVar22 + 0x18) - *(long *)(lVar22 + 8);
          uVar16 = (long)uVar14 >> 2;
          if (uVar16 <= uVar10) {
            uVar16 = uVar10;
          }
          if (0x7ffffffffffffff7 < uVar14) {
            uVar16 = 0x1fffffffffffffff;
          }
          if (uVar16 == 0) {
            pvVar13 = (void *)0x0;
          }
          else {
            if (uVar16 >> 0x3d != 0) goto LAB_006f005c;
            pvVar13 = operator_new(uVar16 << 3);
            puVar15 = *(undefined8 **)(lVar22 + 0x10);
          }
          puVar11 = (undefined8 *)((long)pvVar13 + lVar19 * 8);
          puVar21 = puVar11 + 1;
          *puVar11 = puVar12;
          pvVar18 = *(void **)(lVar22 + 8);
          __dest = (void *)((long)puVar11 - ((long)puVar15 - (long)pvVar18));
          memcpy(__dest,pvVar18,(long)puVar15 - (long)pvVar18);
          *(void **)(lVar22 + 8) = __dest;
          *(undefined8 **)(lVar22 + 0x10) = puVar21;
          *(void **)(lVar22 + 0x18) = (void *)((long)pvVar13 + uVar16 * 8);
          if (pvVar18 != (void *)0x0) {
            operator_delete(pvVar18);
          }
        }
        *(undefined8 **)(lVar22 + 0x10) = puVar21;
        uVar8 = FUN_00464a64(&local_1c8,iVar7 + -2);
        **(undefined4 **)(*(long *)(*(long *)(param_1[1] + -8) + 0x10) + -8) = uVar8;
        uVar8 = FUN_00464a64(&local_1c8,iVar7 + -1);
                    /* catch() { ... } // from try @ 006eff4c with catch @ 006efee8
                       catch() { ... } // from try @ 006effc0 with catch @ 006efee8 */
        *(undefined4 *)(*(long *)(*(long *)(*(long *)(param_1[1] + -8) + 0x10) + -8) + 4) = uVar8;
        uVar8 = FUN_00464a64(&local_1c8,iVar7);
        iVar7 = iVar7 + 3;
        *(undefined4 *)(*(long *)(*(long *)(*(long *)(param_1[1] + -8) + 0x10) + -8) + 8) = uVar8;
      }
    }
    FUN_00465780(&local_1c8);
  }
  local_180 = *(long *)PTR_VTT_00c1acc8;
  local_1c8 = (undefined **)(PTR_DAT_00c1acc0 + 0x10);
                    /* try { // try from 006eff9c to 007effa3 has its CatchHandler @ 006f002c */
                    /* try { // try from 006effa4 to 007effbf has its CatchHandler @ 006f004c */
  *(undefined8 *)
   ((basic_ostream<char,std::__ndk1::char_traits<char>> *)&local_180 + *(long *)(local_180 + -0x18))
       = *(undefined8 *)(PTR_VTT_00c1acc8 + 0x18);
  local_178[0] = PTR_vtable_00c1acd0 + 0x10;
                    /* try { // try from 006effc0 to 007f00af has its CatchHandler @ 006efee8 */
  if ((local_138 & 1) != 0) {
    operator_delete(local_128);
  }
  std::__ndk1::basic_streambuf<char,std::__ndk1::char_traits<char>>::~basic_streambuf
            ((basic_streambuf<char,std::__ndk1::char_traits<char>> *)local_178);
  std::__ndk1::basic_ostream<char,std::__ndk1::char_traits<char>>::~basic_ostream
            ((basic_ostream<char,std::__ndk1::char_traits<char>> *)&local_180);
  std::__ndk1::basic_ios<char,std::__ndk1::char_traits<char>>::~basic_ios(abStack_110);
  if ((local_1a8 & 1) != 0) {
    operator_delete(local_198);
  }
  if (local_1c0 != (void *)0x0) {
    local_1b8 = local_1c0;
    operator_delete(local_1c0);
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
