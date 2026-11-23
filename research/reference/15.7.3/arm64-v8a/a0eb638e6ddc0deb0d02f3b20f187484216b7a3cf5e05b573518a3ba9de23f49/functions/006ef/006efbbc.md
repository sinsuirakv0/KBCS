# 006efbbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `006efbbc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ef/006efbbc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0031.md#compare-831684a8614515c54cb0c1407eb12a2b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `006efbbc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006efbbc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0031.md#compare-17e4fde55685efe0327c76da9ab4f62b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "dcb94c03561d462046e94fa27e7377c80d8c41076741e5a7bb4d5886f5519092",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006efbbc",
        "006f00a7"
      ],
      [
        "006f0128",
        "006f012b"
      ]
    ],
    "bytes_sha256": "e1cd54b50d407988a30f63722ac5550a285406491c95a2385925ba71e5b97998",
    "instruction_count": 316,
    "instruction_bytes": 1264,
    "body_bytes": 1264,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006efbbc"></a> `006efbbc` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-006efbc0"></a> `006efbc0` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006efbc4"></a> `006efbc4` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006efbc8"></a> `006efbc8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006efbcc"></a> `006efbcc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006efbd0"></a> `006efbd0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006efbd4"></a> `006efbd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006efbd8"></a> `006efbd8` | `ff c3 06 d1` | sub sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-006efbdc"></a> `006efbdc` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-006efbe0"></a> `006efbe0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006efbe4"></a> `006efbe4` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efbe8"></a> `006efbe8` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006efbec"></a> `006efbec` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-006efbf0"></a> `006efbf0` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-006efbf4"></a> `006efbf4` | `d5 d4 f5 97` | bl 0x00464f48 | `UNCONDITIONAL_CALL`
<a id="insn-006efbf8"></a> `006efbf8` | `75 5a 40 a9` | ldp x21,x22,[x19] | `FALL_THROUGH`
<a id="insn-006efbfc"></a> `006efbfc` | `c8 27 00 90` | adrp x8,0xbe7000 | `FALL_THROUGH`
<a id="insn-006efc00"></a> `006efc00` | `08 a1 34 91` | add x8,x8,#0xd28 | `FALL_THROUGH`
<a id="insn-006efc04"></a> `006efc04` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-006efc08"></a> `006efc08` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-006efc0c"></a> `006efc0c` | `21 19 00 54` | b.ne 0x006eff30 | `CONDITIONAL_JUMP`
<a id="insn-006efc10"></a> `006efc10` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006efc14"></a> `006efc14` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-006efc18"></a> `006efc18` | `f6 ac 13 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-006efc1c"></a> `006efc1c` | `2a dd ff 90` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-006efc20"></a> `006efc20` | `4a d5 30 91` | add x10,x10,#0xc35 | `FALL_THROUGH`
<a id="insn-006efc24"></a> `006efc24` | `08 de ff d0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-006efc28"></a> `006efc28` | `41 09 40 ad` | ldp q1,q2,[x10] | `FALL_THROUGH`
<a id="insn-006efc2c"></a> `006efc2c` | `c9 85 8e 52` | mov w9,#0x742e | `FALL_THROUGH`
<a id="insn-006efc30"></a> `006efc30` | `00 89 c1 3d` | ldr q0,[x8, #0x620] | `FALL_THROUGH`
<a id="insn-006efc34"></a> `006efc34` | `69 ce ae 72` | movk w9,#0x7673, LSL #16 | `FALL_THROUGH`
<a id="insn-006efc38"></a> `006efc38` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006efc3c"></a> `006efc3c` | `09 20 00 b9` | str w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-006efc40"></a> `006efc40` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006efc44"></a> `006efc44` | `01 08 00 ad` | stp q1,q2,[x0] | `FALL_THROUGH`
<a id="insn-006efc48"></a> `006efc48` | `1f 90 00 39` | strb wzr,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-006efc4c"></a> `006efc4c` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efc50"></a> `006efc50` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-006efc54"></a> `006efc54` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-006efc58"></a> `006efc58` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006efc5c"></a> `006efc5c` | `65 05 0f 94` | bl 0x00ab11f0 | `UNCONDITIONAL_CALL`
<a id="insn-006efc60"></a> `006efc60` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006efc64"></a> `006efc64` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-006efc68"></a> `006efc68` | `68 00 00 36` | tbz w8,#0x0,0x006efc74 | `CONDITIONAL_JUMP`
<a id="insn-006efc6c"></a> `006efc6c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006efc70"></a> `006efc70` | `e8 ac 13 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-006efc74"></a> `006efc74` | `54 18 00 36` | tbz w20,#0x0,0x006eff7c | `CONDITIONAL_JUMP`
<a id="insn-006efc78"></a> `006efc78` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efc7c"></a> `006efc7c` | `76 d3 f5 97` | bl 0x00464a54 | `UNCONDITIONAL_CALL`
<a id="insn-006efc80"></a> `006efc80` | `68 42 00 91` | add x8,x19,#0x10 | `FALL_THROUGH`
<a id="insn-006efc84"></a> `006efc84` | `fa ef 7d b2` | orr x26,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-006efc88"></a> `006efc88` | `1b 00 fc 92` | mov x27,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-006efc8c"></a> `006efc8c` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006efc90"></a> `006efc90` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efc94"></a> `006efc94` | `70 d3 f5 97` | bl 0x00464a54 | `UNCONDITIONAL_CALL`
<a id="insn-006efc98"></a> `006efc98` | `e0 16 00 36` | tbz w0,#0x0,0x006eff74 | `CONDITIONAL_JUMP`
<a id="insn-006efc9c"></a> `006efc9c` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efca0"></a> `006efca0` | `78 d6 f5 97` | bl 0x00465680 | `UNCONDITIONAL_CALL`
<a id="insn-006efca4"></a> `006efca4` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-006efca8"></a> `006efca8` | `6b 16 00 54` | b.lt 0x006eff74 | `CONDITIONAL_JUMP`
<a id="insn-006efcac"></a> `006efcac` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-006efcb0"></a> `006efcb0` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efcb4"></a> `006efcb4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006efcb8"></a> `006efcb8` | `b5 d3 f5 97` | bl 0x00464b8c | `UNCONDITIONAL_CALL`
<a id="insn-006efcbc"></a> `006efcbc` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006efcc0"></a> `006efcc0` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-006efcc4"></a> `006efcc4` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006efcc8"></a> `006efcc8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-006efccc"></a> `006efccc` | `54 01 89 9a` | csel x20,x10,x9,eq | `FALL_THROUGH`
<a id="insn-006efcd0"></a> `006efcd0` | `68 00 00 36` | tbz w8,#0x0,0x006efcdc | `CONDITIONAL_JUMP`
<a id="insn-006efcd4"></a> `006efcd4` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006efcd8"></a> `006efcd8` | `ce ac 13 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-006efcdc"></a> `006efcdc` | `d4 14 00 b4` | cbz x20,0x006eff74 | `CONDITIONAL_JUMP`
<a id="insn-006efce0"></a> `006efce0` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-006efce4"></a> `006efce4` | `c3 ac 13 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-006efce8"></a> `006efce8` | `78 de 40 a9` | ldp x24,x23,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006efcec"></a> `006efcec` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-006efcf0"></a> `006efcf0` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006efcf4"></a> `006efcf4` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-006efcf8"></a> `006efcf8` | `00 00 00 ad` | stp q0,q0,[x0] | `FALL_THROUGH`
<a id="insn-006efcfc"></a> `006efcfc` | `62 00 00 54` | b.cs 0x006efd08 | `CONDITIONAL_JUMP`
<a id="insn-006efd00"></a> `006efd00` | `00 87 00 f8` | str x0,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-006efd04"></a> `006efd04` | `26 00 00 14` | b 0x006efd9c | `UNCONDITIONAL_JUMP`
<a id="insn-006efd08"></a> `006efd08` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-006efd0c"></a> `006efd0c` | `15 03 14 cb` | sub x21,x24,x20 | `FALL_THROUGH`
<a id="insn-006efd10"></a> `006efd10` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-006efd14"></a> `006efd14` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-006efd18"></a> `006efd18` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-006efd1c"></a> `006efd1c` | `c9 1a 00 b5` | cbnz x9,0x006f0074 | `CONDITIONAL_JUMP`
<a id="insn-006efd20"></a> `006efd20` | `e9 02 14 cb` | sub x9,x23,x20 | `FALL_THROUGH`
<a id="insn-006efd24"></a> `006efd24` | `2a fd 42 93` | asr x10,x9,#0x2 | `FALL_THROUGH`
<a id="insn-006efd28"></a> `006efd28` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-006efd2c"></a> `006efd2c` | `48 81 88 9a` | csel x8,x10,x8,hi | `FALL_THROUGH`
<a id="insn-006efd30"></a> `006efd30` | `3f 01 1a eb` | cmp x9,x26 | `FALL_THROUGH`
<a id="insn-006efd34"></a> `006efd34` | `19 31 9b 9a` | csel x25,x8,x27,cc | `FALL_THROUGH`
<a id="insn-006efd38"></a> `006efd38` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006efd3c"></a> `006efd3c` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006efd40"></a> `006efd40` | `39 01 00 b4` | cbz x25,0x006efd64 | `CONDITIONAL_JUMP`
<a id="insn-006efd44"></a> `006efd44` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-006efd48"></a> `006efd48` | `48 1a 00 b5` | cbnz x8,0x006f0090 | `CONDITIONAL_JUMP`
<a id="insn-006efd4c"></a> `006efd4c` | `fc 03 00 aa` | mov x28,x0 | `FALL_THROUGH`
<a id="insn-006efd50"></a> `006efd50` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-006efd54"></a> `006efd54` | `a7 ac 13 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-006efd58"></a> `006efd58` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-006efd5c"></a> `006efd5c` | `e0 03 1c aa` | mov x0,x28 | `FALL_THROUGH`
<a id="insn-006efd60"></a> `006efd60` | `02 00 00 14` | b 0x006efd68 | `UNCONDITIONAL_JUMP`
<a id="insn-006efd64"></a> `006efd64` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-006efd68"></a> `006efd68` | `d8 0e 18 8b` | add x24,x22,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-006efd6c"></a> `006efd6c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-006efd70"></a> `006efd70` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-006efd74"></a> `006efd74` | `d9 0e 19 8b` | add x25,x22,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-006efd78"></a> `006efd78` | `00 87 00 f8` | str x0,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-006efd7c"></a> `006efd7c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-006efd80"></a> `006efd80` | `f8 ac 13 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-006efd84"></a> `006efd84` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-006efd88"></a> `006efd88` | `76 62 00 a9` | stp x22,x24,[x19] | `FALL_THROUGH`
<a id="insn-006efd8c"></a> `006efd8c` | `79 0a 00 f9` | str x25,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-006efd90"></a> `006efd90` | `f4 5f 03 a9` | stp x20,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006efd94"></a> `006efd94` | `f4 53 02 a9` | stp x20,x20,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006efd98"></a> `006efd98` | `23 01 00 94` | bl 0x006f0224 | `UNCONDITIONAL_CALL`
<a id="insn-006efd9c"></a> `006efd9c` | `78 06 00 f9` | str x24,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006efda0"></a> `006efda0` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efda4"></a> `006efda4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006efda8"></a> `006efda8` | `2f d3 f5 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-006efdac"></a> `006efdac` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006efdb0"></a> `006efdb0` | `08 81 5f f8` | ldur x8,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-006efdb4"></a> `006efdb4` | `00 01 00 b9` | str w0,[x8] | `FALL_THROUGH`
<a id="insn-006efdb8"></a> `006efdb8` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efdbc"></a> `006efdbc` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006efdc0"></a> `006efdc0` | `29 d3 f5 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-006efdc4"></a> `006efdc4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006efdc8"></a> `006efdc8` | `94 00 80 52` | mov w20,#0x4 | `FALL_THROUGH`
<a id="insn-006efdcc"></a> `006efdcc` | `08 81 5f f8` | ldur x8,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-006efdd0"></a> `006efdd0` | `00 05 00 b9` | str w0,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-006efdd4"></a> `006efdd4` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efdd8"></a> `006efdd8` | `2a d6 f5 97` | bl 0x00465680 | `UNCONDITIONAL_CALL`
<a id="insn-006efddc"></a> `006efddc` | `9f 02 00 6b` | cmp w20,w0 | `FALL_THROUGH`
<a id="insn-006efde0"></a> `006efde0` | `95 0a 00 51` | sub w21,w20,#0x2 | `FALL_THROUGH`
<a id="insn-006efde4"></a> `006efde4` | `6a f5 ff 54` | b.ge 0x006efc90 | `CONDITIONAL_JUMP`
<a id="insn-006efde8"></a> `006efde8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006efdec"></a> `006efdec` | `1c 81 5f f8` | ldur x28,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-006efdf0"></a> `006efdf0` | `80 01 80 52` | mov w0,#0xc | `FALL_THROUGH`
<a id="insn-006efdf4"></a> `006efdf4` | `7f ac 13 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-006efdf8"></a> `006efdf8` | `1f 08 00 b9` | str wzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-006efdfc"></a> `006efdfc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-006efe00"></a> `006efe00` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-006efe04"></a> `006efe04` | `98 23 41 a9` | ldp x24,x8,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-006efe08"></a> `006efe08` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-006efe0c"></a> `006efe0c` | `62 00 00 54` | b.cs 0x006efe18 | `CONDITIONAL_JUMP`
<a id="insn-006efe10"></a> `006efe10` | `16 87 00 f8` | str x22,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-006efe14"></a> `006efe14` | `25 00 00 14` | b 0x006efea8 | `UNCONDITIONAL_JUMP`
<a id="insn-006efe18"></a> `006efe18` | `89 83 40 f8` | ldur x9,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-006efe1c"></a> `006efe1c` | `0a 03 09 cb` | sub x10,x24,x9 | `FALL_THROUGH`
<a id="insn-006efe20"></a> `006efe20` | `57 fd 43 93` | asr x23,x10,#0x3 | `FALL_THROUGH`
<a id="insn-006efe24"></a> `006efe24` | `ea 06 00 91` | add x10,x23,#0x1 | `FALL_THROUGH`
<a id="insn-006efe28"></a> `006efe28` | `4b fd 7d d3` | lsr x11,x10,#0x3d | `FALL_THROUGH`
<a id="insn-006efe2c"></a> `006efe2c` | `ab 10 00 b5` | cbnz x11,0x006f0040 | `CONDITIONAL_JUMP`
<a id="insn-006efe30"></a> `006efe30` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-006efe34"></a> `006efe34` | `09 fd 42 93` | asr x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-006efe38"></a> `006efe38` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-006efe3c"></a> `006efe3c` | `29 81 8a 9a` | csel x9,x9,x10,hi | `FALL_THROUGH`
<a id="insn-006efe40"></a> `006efe40` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-006efe44"></a> `006efe44` | `39 31 9b 9a` | csel x25,x9,x27,cc | `FALL_THROUGH`
<a id="insn-006efe48"></a> `006efe48` | `f9 00 00 b4` | cbz x25,0x006efe64 | `CONDITIONAL_JUMP`
<a id="insn-006efe4c"></a> `006efe4c` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-006efe50"></a> `006efe50` | `68 10 00 b5` | cbnz x8,0x006f005c | `CONDITIONAL_JUMP`
<a id="insn-006efe54"></a> `006efe54` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-006efe58"></a> `006efe58` | `66 ac 13 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-006efe5c"></a> `006efe5c` | `88 0b 40 f9` | ldr x8,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-006efe60"></a> `006efe60` | `03 00 00 14` | b 0x006efe6c | `UNCONDITIONAL_JUMP`
<a id="insn-006efe64"></a> `006efe64` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-006efe68"></a> `006efe68` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-006efe6c"></a> `006efe6c` | `09 0c 17 8b` | add x9,x0,x23, LSL #0x3 | `FALL_THROUGH`
<a id="insn-006efe70"></a> `006efe70` | `19 0c 19 8b` | add x25,x0,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-006efe74"></a> `006efe74` | `f8 03 09 aa` | mov x24,x9 | `FALL_THROUGH`
<a id="insn-006efe78"></a> `006efe78` | `16 87 00 f8` | str x22,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-006efe7c"></a> `006efe7c` | `96 07 40 f9` | ldr x22,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-006efe80"></a> `006efe80` | `02 01 16 cb` | sub x2,x8,x22 | `FALL_THROUGH`
<a id="insn-006efe84"></a> `006efe84` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-006efe88"></a> `006efe88` | `37 01 02 cb` | sub x23,x9,x2 | `FALL_THROUGH`
<a id="insn-006efe8c"></a> `006efe8c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-006efe90"></a> `006efe90` | `b4 ac 13 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-006efe94"></a> `006efe94` | `97 e3 00 a9` | stp x23,x24,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-006efe98"></a> `006efe98` | `99 0f 00 f9` | str x25,[x28, #0x18] | `FALL_THROUGH`
<a id="insn-006efe9c"></a> `006efe9c` | `76 00 00 b4` | cbz x22,0x006efea8 | `CONDITIONAL_JUMP`
<a id="insn-006efea0"></a> `006efea0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-006efea4"></a> `006efea4` | `5b ac 13 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-006efea8"></a> `006efea8` | `98 0b 00 f9` | str x24,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-006efeac"></a> `006efeac` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efeb0"></a> `006efeb0` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-006efeb4"></a> `006efeb4` | `ec d2 f5 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-006efeb8"></a> `006efeb8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006efebc"></a> `006efebc` | `81 06 00 51` | sub w1,w20,#0x1 | `FALL_THROUGH`
<a id="insn-006efec0"></a> `006efec0` | `08 81 5f f8` | ldur x8,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-006efec4"></a> `006efec4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006efec8"></a> `006efec8` | `08 81 5f f8` | ldur x8,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-006efecc"></a> `006efecc` | `00 01 00 b9` | str w0,[x8] | `FALL_THROUGH`
<a id="insn-006efed0"></a> `006efed0` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efed4"></a> `006efed4` | `e4 d2 f5 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-006efed8"></a> `006efed8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006efedc"></a> `006efedc` | `08 81 5f f8` | ldur x8,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-006efee0"></a> `006efee0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006efee4"></a> `006efee4` | `08 81 5f f8` | ldur x8,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-006efee8"></a> `006efee8` | `00 05 00 b9` | str w0,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-006efeec"></a> `006efeec` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006efef0"></a> `006efef0` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-006efef4"></a> `006efef4` | `dc d2 f5 97` | bl 0x00464a64 | `UNCONDITIONAL_CALL`
<a id="insn-006efef8"></a> `006efef8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006efefc"></a> `006efefc` | `94 0e 00 11` | add w20,w20,#0x3 | `FALL_THROUGH`
<a id="insn-006eff00"></a> `006eff00` | `08 81 5f f8` | ldur x8,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-006eff04"></a> `006eff04` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006eff08"></a> `006eff08` | `08 81 5f f8` | ldur x8,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-006eff0c"></a> `006eff0c` | `00 09 00 b9` | str w0,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-006eff10"></a> `006eff10` | `b1 ff ff 17` | b 0x006efdd4 | `UNCONDITIONAL_JUMP`
<a id="insn-006eff14"></a> `006eff14` | `80 06 40 f9` | ldr x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-006eff18"></a> `006eff18` | `97 0a 00 f9` | str x23,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-006eff1c"></a> `006eff1c` | `3d ac 13 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-006eff20"></a> `006eff20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006eff24"></a> `006eff24` | `3b ac 13 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-006eff28"></a> `006eff28` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-006eff2c"></a> `006eff2c` | `20 e7 ff 54` | b.eq 0x006efc10 | `CONDITIONAL_JUMP`
<a id="insn-006eff30"></a> `006eff30` | `d4 8e 5f f8` | ldr x20,[x22, #-0x8]! | `FALL_THROUGH`
<a id="insn-006eff34"></a> `006eff34` | `df 02 00 f9` | str xzr,[x22] | `FALL_THROUGH`
<a id="insn-006eff38"></a> `006eff38` | `94 ff ff b4` | cbz x20,0x006eff28 | `CONDITIONAL_JUMP`
<a id="insn-006eff3c"></a> `006eff3c` | `97 06 40 f9` | ldr x23,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-006eff40"></a> `006eff40` | `17 ff ff b4` | cbz x23,0x006eff20 | `CONDITIONAL_JUMP`
<a id="insn-006eff44"></a> `006eff44` | `98 0a 40 f9` | ldr x24,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-006eff48"></a> `006eff48` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-006eff4c"></a> `006eff4c` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-006eff50"></a> `006eff50` | `81 00 00 54` | b.ne 0x006eff60 | `CONDITIONAL_JUMP`
<a id="insn-006eff54"></a> `006eff54` | `f1 ff ff 17` | b 0x006eff18 | `UNCONDITIONAL_JUMP`
<a id="insn-006eff58"></a> `006eff58` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-006eff5c"></a> `006eff5c` | `c0 fd ff 54` | b.eq 0x006eff14 | `CONDITIONAL_JUMP`
<a id="insn-006eff60"></a> `006eff60` | `00 8f 5f f8` | ldr x0,[x24, #-0x8]! | `FALL_THROUGH`
<a id="insn-006eff64"></a> `006eff64` | `1f 03 00 f9` | str xzr,[x24] | `FALL_THROUGH`
<a id="insn-006eff68"></a> `006eff68` | `80 ff ff b4` | cbz x0,0x006eff58 | `CONDITIONAL_JUMP`
<a id="insn-006eff6c"></a> `006eff6c` | `29 ac 13 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-006eff70"></a> `006eff70` | `fa ff ff 17` | b 0x006eff58 | `UNCONDITIONAL_JUMP`
<a id="insn-006eff74"></a> `006eff74` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006eff78"></a> `006eff78` | `02 d6 f5 97` | bl 0x00465780 | `UNCONDITIONAL_CALL`
<a id="insn-006eff7c"></a> `006eff7c` | `48 29 00 f0` | adrp x8,0xc1a000 | `FALL_THROUGH`
<a id="insn-006eff80"></a> `006eff80` | `55 29 00 f0` | adrp x21,0xc1a000 | `FALL_THROUGH`
<a id="insn-006eff84"></a> `006eff84` | `f4 23 01 91` | add x20,sp,#0x48 | `FALL_THROUGH`
<a id="insn-006eff88"></a> `006eff88` | `08 b9 46 f9` | ldr x8,[x8, #0xd70] | `FALL_THROUGH`
<a id="insn-006eff8c"></a> `006eff8c` | `b5 be 46 f9` | ldr x21,[x21, #0xd78] | `FALL_THROUGH`
<a id="insn-006eff90"></a> `006eff90` | `93 22 01 91` | add x19,x20,#0x48 | `FALL_THROUGH`
<a id="insn-006eff94"></a> `006eff94` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-006eff98"></a> `006eff98` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-006eff9c"></a> `006eff9c` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-006effa0"></a> `006effa0` | `e9 4b 00 f9` | str x9,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-006effa4"></a> `006effa4` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-006effa8"></a> `006effa8` | `a9 0e 40 f9` | ldr x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-006effac"></a> `006effac` | `69 6a 28 f8` | str x9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006effb0"></a> `006effb0` | `48 29 00 f0` | adrp x8,0xc1a000 | `FALL_THROUGH`
<a id="insn-006effb4"></a> `006effb4` | `08 c1 46 f9` | ldr x8,[x8, #0xd80] | `FALL_THROUGH`
<a id="insn-006effb8"></a> `006effb8` | `e9 63 43 39` | ldrb w9,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-006effbc"></a> `006effbc` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-006effc0"></a> `006effc0` | `e8 4f 00 f9` | str x8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-006effc4"></a> `006effc4` | `69 00 00 36` | tbz w9,#0x0,0x006effd0 | `CONDITIONAL_JUMP`
<a id="insn-006effc8"></a> `006effc8` | `e0 77 40 f9` | ldr x0,[sp, #0xe8] | `FALL_THROUGH`
<a id="insn-006effcc"></a> `006effcc` | `11 ac 13 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-006effd0"></a> `006effd0` | `80 42 01 91` | add x0,x20,#0x50 | `FALL_THROUGH`
<a id="insn-006effd4"></a> `006effd4` | `4b ac 13 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-006effd8"></a> `006effd8` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-006effdc"></a> `006effdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006effe0"></a> `006effe0` | `4c ac 13 94` | bl 0x00bdb110 | `UNCONDITIONAL_CALL`
<a id="insn-006effe4"></a> `006effe4` | `80 e2 02 91` | add x0,x20,#0xb8 | `FALL_THROUGH`
<a id="insn-006effe8"></a> `006effe8` | `4e ac 13 94` | bl 0x00bdb120 | `UNCONDITIONAL_CALL`
<a id="insn-006effec"></a> `006effec` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-006efff0"></a> `006efff0` | `68 00 00 36` | tbz w8,#0x0,0x006efffc | `CONDITIONAL_JUMP`
<a id="insn-006efff4"></a> `006efff4` | `e0 3f 40 f9` | ldr x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-006efff8"></a> `006efff8` | `06 ac 13 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-006efffc"></a> `006efffc` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006f0000"></a> `006f0000` | `60 00 00 b4` | cbz x0,0x006f000c | `CONDITIONAL_JUMP`
<a id="insn-006f0004"></a> `006f0004` | `e0 2f 00 f9` | str x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-006f0008"></a> `006f0008` | `02 ac 13 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-006f000c"></a> `006f000c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006f0010"></a> `006f0010` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-006f0014"></a> `006f0014` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-006f0018"></a> `006f0018` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006f001c"></a> `006f001c` | `61 08 00 54` | b.ne 0x006f0128 | `CONDITIONAL_JUMP`
<a id="insn-006f0020"></a> `006f0020` | `ff c3 06 91` | add sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-006f0024"></a> `006f0024` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006f0028"></a> `006f0028` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006f002c"></a> `006f002c` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006f0030"></a> `006f0030` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006f0034"></a> `006f0034` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006f0038"></a> `006f0038` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-006f003c"></a> `006f003c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006f0040"></a> `006f0040` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006f0044"></a> `006f0044` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-006f0048"></a> `006f0048` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-006f004c"></a> `006f004c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006f0050"></a> `006f0050` | `c1 06 00 54` | b.ne 0x006f0128 | `CONDITIONAL_JUMP`
<a id="insn-006f0054"></a> `006f0054` | `80 23 00 91` | add x0,x28,#0x8 | `FALL_THROUGH`
<a id="insn-006f0058"></a> `006f0058` | `a7 00 00 94` | bl 0x006f02f4 | `UNCONDITIONAL_CALL`
<a id="insn-006f005c"></a> `006f005c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006f0060"></a> `006f0060` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-006f0064"></a> `006f0064` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-006f0068"></a> `006f0068` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006f006c"></a> `006f006c` | `e1 05 00 54` | b.ne 0x006f0128 | `CONDITIONAL_JUMP`
<a id="insn-006f0070"></a> `006f0070` | `c4 b8 f4 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-006f0074"></a> `006f0074` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006f0078"></a> `006f0078` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-006f007c"></a> `006f007c` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-006f0080"></a> `006f0080` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006f0084"></a> `006f0084` | `21 05 00 54` | b.ne 0x006f0128 | `CONDITIONAL_JUMP`
<a id="insn-006f0088"></a> `006f0088` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006f008c"></a> `006f008c` | `95 00 00 94` | bl 0x006f02e0 | `UNCONDITIONAL_CALL`
<a id="insn-006f0090"></a> `006f0090` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006f0094"></a> `006f0094` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-006f0098"></a> `006f0098` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-006f009c"></a> `006f009c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006f00a0"></a> `006f00a0` | `41 04 00 54` | b.ne 0x006f0128 | `CONDITIONAL_JUMP`
<a id="insn-006f00a4"></a> `006f00a4` | `b7 b8 f4 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-006f0128"></a> `006f0128` | `c6 ab 13 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006efbbc`](#insn-006efbbc) 範囲 `[['006efbbc', '006efc0f']]`
  - `CONDITIONAL_JUMP` [`006efc0c`](#insn-006efc0c) → [`006eff30`](#insn-006eff30)
  - `FALL_THROUGH` [`006efc0c`](#insn-006efc0c) → [`006efc10`](#insn-006efc10)
- ブロック [`006efc10`](#insn-006efc10) 範囲 `[['006efc10', '006efc6b']]`
  - `CONDITIONAL_JUMP` [`006efc68`](#insn-006efc68) → [`006efc74`](#insn-006efc74)
  - `FALL_THROUGH` [`006efc68`](#insn-006efc68) → [`006efc6c`](#insn-006efc6c)
- ブロック [`006efc6c`](#insn-006efc6c) 範囲 `[['006efc6c', '006efc73']]`
  - `FALL_THROUGH` [`006efc70`](#insn-006efc70) → [`006efc74`](#insn-006efc74)
- ブロック [`006efc74`](#insn-006efc74) 範囲 `[['006efc74', '006efc77']]`
  - `CONDITIONAL_JUMP` [`006efc74`](#insn-006efc74) → [`006eff7c`](#insn-006eff7c)
  - `FALL_THROUGH` [`006efc74`](#insn-006efc74) → [`006efc78`](#insn-006efc78)
- ブロック [`006efc78`](#insn-006efc78) 範囲 `[['006efc78', '006efc8f']]`
  - `FALL_THROUGH` [`006efc8c`](#insn-006efc8c) → [`006efc90`](#insn-006efc90)
- ブロック [`006efc90`](#insn-006efc90) 範囲 `[['006efc90', '006efc9b']]`
  - `CONDITIONAL_JUMP` [`006efc98`](#insn-006efc98) → [`006eff74`](#insn-006eff74)
  - `FALL_THROUGH` [`006efc98`](#insn-006efc98) → [`006efc9c`](#insn-006efc9c)
- ブロック [`006efc9c`](#insn-006efc9c) 範囲 `[['006efc9c', '006efcab']]`
  - `CONDITIONAL_JUMP` [`006efca8`](#insn-006efca8) → [`006eff74`](#insn-006eff74)
  - `FALL_THROUGH` [`006efca8`](#insn-006efca8) → [`006efcac`](#insn-006efcac)
- ブロック [`006efcac`](#insn-006efcac) 範囲 `[['006efcac', '006efcd3']]`
  - `CONDITIONAL_JUMP` [`006efcd0`](#insn-006efcd0) → [`006efcdc`](#insn-006efcdc)
  - `FALL_THROUGH` [`006efcd0`](#insn-006efcd0) → [`006efcd4`](#insn-006efcd4)
- ブロック [`006efcd4`](#insn-006efcd4) 範囲 `[['006efcd4', '006efcdb']]`
  - `FALL_THROUGH` [`006efcd8`](#insn-006efcd8) → [`006efcdc`](#insn-006efcdc)
- ブロック [`006efcdc`](#insn-006efcdc) 範囲 `[['006efcdc', '006efcdf']]`
  - `CONDITIONAL_JUMP` [`006efcdc`](#insn-006efcdc) → [`006eff74`](#insn-006eff74)
  - `FALL_THROUGH` [`006efcdc`](#insn-006efcdc) → [`006efce0`](#insn-006efce0)
- ブロック [`006efce0`](#insn-006efce0) 範囲 `[['006efce0', '006efcff']]`
  - `CONDITIONAL_JUMP` [`006efcfc`](#insn-006efcfc) → [`006efd08`](#insn-006efd08)
  - `FALL_THROUGH` [`006efcfc`](#insn-006efcfc) → [`006efd00`](#insn-006efd00)
- ブロック [`006efd00`](#insn-006efd00) 範囲 `[['006efd00', '006efd07']]`
  - `UNCONDITIONAL_JUMP` [`006efd04`](#insn-006efd04) → [`006efd9c`](#insn-006efd9c)
- ブロック [`006efd08`](#insn-006efd08) 範囲 `[['006efd08', '006efd1f']]`
  - `CONDITIONAL_JUMP` [`006efd1c`](#insn-006efd1c) → [`006f0074`](#insn-006f0074)
  - `FALL_THROUGH` [`006efd1c`](#insn-006efd1c) → [`006efd20`](#insn-006efd20)
- ブロック [`006efd20`](#insn-006efd20) 範囲 `[['006efd20', '006efd43']]`
  - `CONDITIONAL_JUMP` [`006efd40`](#insn-006efd40) → [`006efd64`](#insn-006efd64)
  - `FALL_THROUGH` [`006efd40`](#insn-006efd40) → [`006efd44`](#insn-006efd44)
- ブロック [`006efd44`](#insn-006efd44) 範囲 `[['006efd44', '006efd4b']]`
  - `CONDITIONAL_JUMP` [`006efd48`](#insn-006efd48) → [`006f0090`](#insn-006f0090)
  - `FALL_THROUGH` [`006efd48`](#insn-006efd48) → [`006efd4c`](#insn-006efd4c)
- ブロック [`006efd4c`](#insn-006efd4c) 範囲 `[['006efd4c', '006efd63']]`
  - `UNCONDITIONAL_JUMP` [`006efd60`](#insn-006efd60) → [`006efd68`](#insn-006efd68)
- ブロック [`006efd64`](#insn-006efd64) 範囲 `[['006efd64', '006efd67']]`
  - `FALL_THROUGH` [`006efd64`](#insn-006efd64) → [`006efd68`](#insn-006efd68)
- ブロック [`006efd68`](#insn-006efd68) 範囲 `[['006efd68', '006efd9b']]`
  - `FALL_THROUGH` [`006efd98`](#insn-006efd98) → [`006efd9c`](#insn-006efd9c)
- ブロック [`006efd9c`](#insn-006efd9c) 範囲 `[['006efd9c', '006efdd3']]`
  - `FALL_THROUGH` [`006efdd0`](#insn-006efdd0) → [`006efdd4`](#insn-006efdd4)
- ブロック [`006efdd4`](#insn-006efdd4) 範囲 `[['006efdd4', '006efde7']]`
  - `CONDITIONAL_JUMP` [`006efde4`](#insn-006efde4) → [`006efc90`](#insn-006efc90)
  - `FALL_THROUGH` [`006efde4`](#insn-006efde4) → [`006efde8`](#insn-006efde8)
- ブロック [`006efde8`](#insn-006efde8) 範囲 `[['006efde8', '006efe0f']]`
  - `CONDITIONAL_JUMP` [`006efe0c`](#insn-006efe0c) → [`006efe18`](#insn-006efe18)
  - `FALL_THROUGH` [`006efe0c`](#insn-006efe0c) → [`006efe10`](#insn-006efe10)
- ブロック [`006efe10`](#insn-006efe10) 範囲 `[['006efe10', '006efe17']]`
  - `UNCONDITIONAL_JUMP` [`006efe14`](#insn-006efe14) → [`006efea8`](#insn-006efea8)
- ブロック [`006efe18`](#insn-006efe18) 範囲 `[['006efe18', '006efe2f']]`
  - `CONDITIONAL_JUMP` [`006efe2c`](#insn-006efe2c) → [`006f0040`](#insn-006f0040)
  - `FALL_THROUGH` [`006efe2c`](#insn-006efe2c) → [`006efe30`](#insn-006efe30)
- ブロック [`006efe30`](#insn-006efe30) 範囲 `[['006efe30', '006efe4b']]`
  - `CONDITIONAL_JUMP` [`006efe48`](#insn-006efe48) → [`006efe64`](#insn-006efe64)
  - `FALL_THROUGH` [`006efe48`](#insn-006efe48) → [`006efe4c`](#insn-006efe4c)
- ブロック [`006efe4c`](#insn-006efe4c) 範囲 `[['006efe4c', '006efe53']]`
  - `CONDITIONAL_JUMP` [`006efe50`](#insn-006efe50) → [`006f005c`](#insn-006f005c)
  - `FALL_THROUGH` [`006efe50`](#insn-006efe50) → [`006efe54`](#insn-006efe54)
- ブロック [`006efe54`](#insn-006efe54) 範囲 `[['006efe54', '006efe63']]`
  - `UNCONDITIONAL_JUMP` [`006efe60`](#insn-006efe60) → [`006efe6c`](#insn-006efe6c)
- ブロック [`006efe64`](#insn-006efe64) 範囲 `[['006efe64', '006efe6b']]`
  - `FALL_THROUGH` [`006efe68`](#insn-006efe68) → [`006efe6c`](#insn-006efe6c)
- ブロック [`006efe6c`](#insn-006efe6c) 範囲 `[['006efe6c', '006efe9f']]`
  - `CONDITIONAL_JUMP` [`006efe9c`](#insn-006efe9c) → [`006efea8`](#insn-006efea8)
  - `FALL_THROUGH` [`006efe9c`](#insn-006efe9c) → [`006efea0`](#insn-006efea0)
- ブロック [`006efea0`](#insn-006efea0) 範囲 `[['006efea0', '006efea7']]`
  - `FALL_THROUGH` [`006efea4`](#insn-006efea4) → [`006efea8`](#insn-006efea8)
- ブロック [`006efea8`](#insn-006efea8) 範囲 `[['006efea8', '006efee7']]`
  - `FALL_THROUGH` [`006efee4`](#insn-006efee4) → [`006efee8`](#insn-006efee8)
- ブロック [`006efee8`](#insn-006efee8) 範囲 `[['006efee8', '006eff13']]`
  - `UNCONDITIONAL_JUMP` [`006eff10`](#insn-006eff10) → [`006efdd4`](#insn-006efdd4)
- ブロック [`006eff14`](#insn-006eff14) 範囲 `[['006eff14', '006eff17']]`
  - `FALL_THROUGH` [`006eff14`](#insn-006eff14) → [`006eff18`](#insn-006eff18)
- ブロック [`006eff18`](#insn-006eff18) 範囲 `[['006eff18', '006eff1f']]`
  - `FALL_THROUGH` [`006eff1c`](#insn-006eff1c) → [`006eff20`](#insn-006eff20)
- ブロック [`006eff20`](#insn-006eff20) 範囲 `[['006eff20', '006eff27']]`
  - `FALL_THROUGH` [`006eff24`](#insn-006eff24) → [`006eff28`](#insn-006eff28)
- ブロック [`006eff28`](#insn-006eff28) 範囲 `[['006eff28', '006eff2f']]`
  - `CONDITIONAL_JUMP` [`006eff2c`](#insn-006eff2c) → [`006efc10`](#insn-006efc10)
  - `FALL_THROUGH` [`006eff2c`](#insn-006eff2c) → [`006eff30`](#insn-006eff30)
- ブロック [`006eff30`](#insn-006eff30) 範囲 `[['006eff30', '006eff3b']]`
  - `CONDITIONAL_JUMP` [`006eff38`](#insn-006eff38) → [`006eff28`](#insn-006eff28)
  - `FALL_THROUGH` [`006eff38`](#insn-006eff38) → [`006eff3c`](#insn-006eff3c)
- ブロック [`006eff3c`](#insn-006eff3c) 範囲 `[['006eff3c', '006eff43']]`
  - `CONDITIONAL_JUMP` [`006eff40`](#insn-006eff40) → [`006eff20`](#insn-006eff20)
  - `FALL_THROUGH` [`006eff40`](#insn-006eff40) → [`006eff44`](#insn-006eff44)
- ブロック [`006eff44`](#insn-006eff44) 範囲 `[['006eff44', '006eff4b']]`
  - `FALL_THROUGH` [`006eff48`](#insn-006eff48) → [`006eff4c`](#insn-006eff4c)
- ブロック [`006eff4c`](#insn-006eff4c) 範囲 `[['006eff4c', '006eff53']]`
  - `CONDITIONAL_JUMP` [`006eff50`](#insn-006eff50) → [`006eff60`](#insn-006eff60)
  - `FALL_THROUGH` [`006eff50`](#insn-006eff50) → [`006eff54`](#insn-006eff54)
- ブロック [`006eff54`](#insn-006eff54) 範囲 `[['006eff54', '006eff57']]`
  - `UNCONDITIONAL_JUMP` [`006eff54`](#insn-006eff54) → [`006eff18`](#insn-006eff18)
- ブロック [`006eff58`](#insn-006eff58) 範囲 `[['006eff58', '006eff5f']]`
  - `CONDITIONAL_JUMP` [`006eff5c`](#insn-006eff5c) → [`006eff14`](#insn-006eff14)
  - `FALL_THROUGH` [`006eff5c`](#insn-006eff5c) → [`006eff60`](#insn-006eff60)
- ブロック [`006eff60`](#insn-006eff60) 範囲 `[['006eff60', '006eff6b']]`
  - `CONDITIONAL_JUMP` [`006eff68`](#insn-006eff68) → [`006eff58`](#insn-006eff58)
  - `FALL_THROUGH` [`006eff68`](#insn-006eff68) → [`006eff6c`](#insn-006eff6c)
- ブロック [`006eff6c`](#insn-006eff6c) 範囲 `[['006eff6c', '006eff73']]`
  - `UNCONDITIONAL_JUMP` [`006eff70`](#insn-006eff70) → [`006eff58`](#insn-006eff58)
- ブロック [`006eff74`](#insn-006eff74) 範囲 `[['006eff74', '006eff7b']]`
  - `FALL_THROUGH` [`006eff78`](#insn-006eff78) → [`006eff7c`](#insn-006eff7c)
- ブロック [`006eff7c`](#insn-006eff7c) 範囲 `[['006eff7c', '006eff9b']]`
  - `FALL_THROUGH` [`006eff98`](#insn-006eff98) → [`006eff9c`](#insn-006eff9c)
- ブロック [`006eff9c`](#insn-006eff9c) 範囲 `[['006eff9c', '006effa3']]`
  - `FALL_THROUGH` [`006effa0`](#insn-006effa0) → [`006effa4`](#insn-006effa4)
- ブロック [`006effa4`](#insn-006effa4) 範囲 `[['006effa4', '006effbf']]`
  - `FALL_THROUGH` [`006effbc`](#insn-006effbc) → [`006effc0`](#insn-006effc0)
- ブロック [`006effc0`](#insn-006effc0) 範囲 `[['006effc0', '006effc7']]`
  - `CONDITIONAL_JUMP` [`006effc4`](#insn-006effc4) → [`006effd0`](#insn-006effd0)
  - `FALL_THROUGH` [`006effc4`](#insn-006effc4) → [`006effc8`](#insn-006effc8)
- ブロック [`006effc8`](#insn-006effc8) 範囲 `[['006effc8', '006effcf']]`
  - `FALL_THROUGH` [`006effcc`](#insn-006effcc) → [`006effd0`](#insn-006effd0)
- ブロック [`006effd0`](#insn-006effd0) 範囲 `[['006effd0', '006efff3']]`
  - `CONDITIONAL_JUMP` [`006efff0`](#insn-006efff0) → [`006efffc`](#insn-006efffc)
  - `FALL_THROUGH` [`006efff0`](#insn-006efff0) → [`006efff4`](#insn-006efff4)
- ブロック [`006efff4`](#insn-006efff4) 範囲 `[['006efff4', '006efffb']]`
  - `FALL_THROUGH` [`006efff8`](#insn-006efff8) → [`006efffc`](#insn-006efffc)
- ブロック [`006efffc`](#insn-006efffc) 範囲 `[['006efffc', '006f0003']]`
  - `CONDITIONAL_JUMP` [`006f0000`](#insn-006f0000) → [`006f000c`](#insn-006f000c)
  - `FALL_THROUGH` [`006f0000`](#insn-006f0000) → [`006f0004`](#insn-006f0004)
- ブロック [`006f0004`](#insn-006f0004) 範囲 `[['006f0004', '006f000b']]`
  - `FALL_THROUGH` [`006f0008`](#insn-006f0008) → [`006f000c`](#insn-006f000c)
- ブロック [`006f000c`](#insn-006f000c) 範囲 `[['006f000c', '006f001f']]`
  - `CONDITIONAL_JUMP` [`006f001c`](#insn-006f001c) → [`006f0128`](#insn-006f0128)
  - `FALL_THROUGH` [`006f001c`](#insn-006f001c) → [`006f0020`](#insn-006f0020)
- ブロック [`006f0020`](#insn-006f0020) 範囲 `[['006f0020', '006f002b']]`
  - `FALL_THROUGH` [`006f0028`](#insn-006f0028) → [`006f002c`](#insn-006f002c)
- ブロック [`006f002c`](#insn-006f002c) 範囲 `[['006f002c', '006f003b']]`
  - `FALL_THROUGH` [`006f0038`](#insn-006f0038) → [`006f003c`](#insn-006f003c)
- ブロック [`006f003c`](#insn-006f003c) 範囲 `[['006f003c', '006f003f']]`
- ブロック [`006f0040`](#insn-006f0040) 範囲 `[['006f0040', '006f004b']]`
  - `FALL_THROUGH` [`006f0048`](#insn-006f0048) → [`006f004c`](#insn-006f004c)
- ブロック [`006f004c`](#insn-006f004c) 範囲 `[['006f004c', '006f0053']]`
  - `CONDITIONAL_JUMP` [`006f0050`](#insn-006f0050) → [`006f0128`](#insn-006f0128)
  - `FALL_THROUGH` [`006f0050`](#insn-006f0050) → [`006f0054`](#insn-006f0054)
- ブロック [`006f0054`](#insn-006f0054) 範囲 `[['006f0054', '006f005b']]`
  - `FALL_THROUGH` [`006f0058`](#insn-006f0058) → [`006f005c`](#insn-006f005c)
- ブロック [`006f005c`](#insn-006f005c) 範囲 `[['006f005c', '006f006f']]`
  - `CONDITIONAL_JUMP` [`006f006c`](#insn-006f006c) → [`006f0128`](#insn-006f0128)
  - `FALL_THROUGH` [`006f006c`](#insn-006f006c) → [`006f0070`](#insn-006f0070)
- ブロック [`006f0070`](#insn-006f0070) 範囲 `[['006f0070', '006f0073']]`
- ブロック [`006f0074`](#insn-006f0074) 範囲 `[['006f0074', '006f0087']]`
  - `CONDITIONAL_JUMP` [`006f0084`](#insn-006f0084) → [`006f0128`](#insn-006f0128)
  - `FALL_THROUGH` [`006f0084`](#insn-006f0084) → [`006f0088`](#insn-006f0088)
- ブロック [`006f0088`](#insn-006f0088) 範囲 `[['006f0088', '006f008f']]`
  - `FALL_THROUGH` [`006f008c`](#insn-006f008c) → [`006f0090`](#insn-006f0090)
- ブロック [`006f0090`](#insn-006f0090) 範囲 `[['006f0090', '006f00a3']]`
  - `CONDITIONAL_JUMP` [`006f00a0`](#insn-006f00a0) → [`006f0128`](#insn-006f0128)
  - `FALL_THROUGH` [`006f00a0`](#insn-006f00a0) → [`006f00a4`](#insn-006f00a4)
- ブロック [`006f00a4`](#insn-006f00a4) 範囲 `[['006f00a4', '006f00a7']]`
- ブロック [`006f0128`](#insn-006f0128) 範囲 `[['006f0128', '006f012b']]`

## 命令位置別の参照

- [`006efbbc`](#insn-006efbbc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efbc0`](#insn-006efbc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efbc4`](#insn-006efbc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efbc8`](#insn-006efbc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efbcc`](#insn-006efbcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efbd0`](#insn-006efbd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efbe8`](#insn-006efbe8) → `Stack[-0x208]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efbf0`](#insn-006efbf0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efbf4`](#insn-006efbf4) → [`00464f48`](../00464/00464f48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464f48` · 推定シンボル `None` · 推定型 `None`
- [`006efc04`](#insn-006efc04) → `00be7d28`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`006efc04`](#insn-006efc04) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efc0c`](#insn-006efc0c) → [`006eff30`](#insn-006eff30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efc18`](#insn-006efc18) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`006efc28`](#insn-006efc28) → `00293c35`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006efc28`](#insn-006efc28) → `00293c45`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006efc30`](#insn-006efc30) → `002b1620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efc38`](#insn-006efc38) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efc40`](#insn-006efc40) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efc5c`](#insn-006efc5c) → [`00ab11f0`](../00ab1/00ab11f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab11f0` · 推定シンボル `None` · 推定型 `None`
- [`006efc60`](#insn-006efc60) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efc68`](#insn-006efc68) → [`006efc74`](#insn-006efc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efc6c`](#insn-006efc6c) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efc70`](#insn-006efc70) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`006efc74`](#insn-006efc74) → [`006eff7c`](#insn-006eff7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efc7c`](#insn-006efc7c) → [`00464a54`](../00464/00464a54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a54` · 推定シンボル `None` · 推定型 `None`
- [`006efc8c`](#insn-006efc8c) → `Stack[-0x200]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efc94`](#insn-006efc94) → [`00464a54`](../00464/00464a54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a54` · 推定シンボル `None` · 推定型 `None`
- [`006efc98`](#insn-006efc98) → [`006eff74`](#insn-006eff74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efca0`](#insn-006efca0) → [`00465680`](../00465/00465680.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465680` · 推定シンボル `None` · 推定型 `None`
- [`006efca8`](#insn-006efca8) → [`006eff74`](#insn-006eff74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efcb8`](#insn-006efcb8) → [`00464b8c`](../00464/00464b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464b8c` · 推定シンボル `None` · 推定型 `None`
- [`006efcbc`](#insn-006efcbc) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efcc0`](#insn-006efcc0) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efcd0`](#insn-006efcd0) → [`006efcdc`](#insn-006efcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efcd4`](#insn-006efcd4) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efcd8`](#insn-006efcd8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`006efcdc`](#insn-006efcdc) → [`006eff74`](#insn-006eff74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efce4`](#insn-006efce4) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`006efcf0`](#insn-006efcf0) → `Stack[-0x1f8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efcfc`](#insn-006efcfc) → [`006efd08`](#insn-006efd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efd04`](#insn-006efd04) → [`006efd9c`](#insn-006efd9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efd1c`](#insn-006efd1c) → [`006f0074`](#insn-006f0074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efd38`](#insn-006efd38) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efd3c`](#insn-006efd3c) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efd40`](#insn-006efd40) → [`006efd64`](#insn-006efd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efd48`](#insn-006efd48) → [`006f0090`](#insn-006f0090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efd54`](#insn-006efd54) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`006efd60`](#insn-006efd60) → [`006efd68`](#insn-006efd68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efd80`](#insn-006efd80) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`006efd90`](#insn-006efd90) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efd94`](#insn-006efd94) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efd98`](#insn-006efd98) → [`006f0224`](../006f0/006f0224.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f0224` · 推定シンボル `None` · 推定型 `None`
- [`006efda8`](#insn-006efda8) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`006efdc0`](#insn-006efdc0) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`006efdd8`](#insn-006efdd8) → [`00465680`](../00465/00465680.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465680` · 推定シンボル `None` · 推定型 `None`
- [`006efde4`](#insn-006efde4) → [`006efc90`](#insn-006efc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efdf4`](#insn-006efdf4) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`006efe0c`](#insn-006efe0c) → [`006efe18`](#insn-006efe18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efe14`](#insn-006efe14) → [`006efea8`](#insn-006efea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efe2c`](#insn-006efe2c) → [`006f0040`](#insn-006f0040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efe48`](#insn-006efe48) → [`006efe64`](#insn-006efe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efe50`](#insn-006efe50) → [`006f005c`](#insn-006f005c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efe58`](#insn-006efe58) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`006efe60`](#insn-006efe60) → [`006efe6c`](#insn-006efe6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efe90`](#insn-006efe90) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`006efe9c`](#insn-006efe9c) → [`006efea8`](#insn-006efea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efea4`](#insn-006efea4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`006efeb4`](#insn-006efeb4) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`006efed4`](#insn-006efed4) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`006efef4`](#insn-006efef4) → [`00464a64`](../00464/00464a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00464a64` · 推定シンボル `None` · 推定型 `None`
- [`006eff10`](#insn-006eff10) → [`006efdd4`](#insn-006efdd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eff1c`](#insn-006eff1c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`006eff24`](#insn-006eff24) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`006eff2c`](#insn-006eff2c) → [`006efc10`](#insn-006efc10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eff38`](#insn-006eff38) → [`006eff28`](#insn-006eff28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eff40`](#insn-006eff40) → [`006eff20`](#insn-006eff20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eff50`](#insn-006eff50) → [`006eff60`](#insn-006eff60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eff54`](#insn-006eff54) → [`006eff18`](#insn-006eff18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eff5c`](#insn-006eff5c) → [`006eff14`](#insn-006eff14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eff68`](#insn-006eff68) → [`006eff58`](#insn-006eff58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eff6c`](#insn-006eff6c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`006eff70`](#insn-006eff70) → [`006eff58`](#insn-006eff58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006eff78`](#insn-006eff78) → [`00465780`](../00465/00465780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00465780` · 推定シンボル `None` · 推定型 `None`
- [`006eff88`](#insn-006eff88) → `00c1ad70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006eff8c`](#insn-006eff8c) → `00c1ad78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006eff94`](#insn-006eff94) → `00c13408`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`006eff9c`](#insn-006eff9c) → `00be8808`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`006eff9c`](#insn-006eff9c) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006effa0`](#insn-006effa0) → `00c113a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006effa0`](#insn-006effa0) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006effa4`](#insn-006effa4) → `00c11390`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`006effa8`](#insn-006effa8) → `00c13420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`006effac`](#insn-006effac) → `00c113d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006effb4`](#insn-006effb4) → `00c1ad80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006effb8`](#insn-006effb8) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006effc0`](#insn-006effc0) → `00c11128`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`006effc0`](#insn-006effc0) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006effc4`](#insn-006effc4) → [`006effd0`](#insn-006effd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006effc8`](#insn-006effc8) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006effcc`](#insn-006effcc) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`006effd4`](#insn-006effd4) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`006effd8`](#insn-006effd8) → `00c13410`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`006effe0`](#insn-006effe0) → [`00bdb110`](../00bdb/00bdb110.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb110` · 推定シンボル `None` · 推定型 `None`
- [`006effe8`](#insn-006effe8) → [`00bdb120`](../00bdb/00bdb120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb120` · 推定シンボル `None` · 推定型 `None`
- [`006effec`](#insn-006effec) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efff0`](#insn-006efff0) → [`006efffc`](#insn-006efffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efff4`](#insn-006efff4) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006efff8`](#insn-006efff8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`006efffc`](#insn-006efffc) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0000`](#insn-006f0000) → [`006f000c`](#insn-006f000c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0004`](#insn-006f0004) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0008`](#insn-006f0008) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`006f000c`](#insn-006f000c) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0014`](#insn-006f0014) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f001c`](#insn-006f001c) → [`006f0128`](#insn-006f0128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0024`](#insn-006f0024) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0028`](#insn-006f0028) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f002c`](#insn-006f002c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0030`](#insn-006f0030) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0034`](#insn-006f0034) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0038`](#insn-006f0038) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0040`](#insn-006f0040) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0048`](#insn-006f0048) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0050`](#insn-006f0050) → [`006f0128`](#insn-006f0128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0058`](#insn-006f0058) → [`006f02f4`](../006f0/006f02f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f02f4` · 推定シンボル `None` · 推定型 `None`
- [`006f005c`](#insn-006f005c) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0064`](#insn-006f0064) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f006c`](#insn-006f006c) → [`006f0128`](#insn-006f0128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0070`](#insn-006f0070) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`006f0074`](#insn-006f0074) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f007c`](#insn-006f007c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0084`](#insn-006f0084) → [`006f0128`](#insn-006f0128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f008c`](#insn-006f008c) → [`006f02e0`](../006f0/006f02e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f02e0` · 推定シンボル `None` · 推定型 `None`
- [`006f0090`](#insn-006f0090) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f0098`](#insn-006f0098) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f00a0`](#insn-006f00a0) → [`006f0128`](#insn-006f0128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006f00a4`](#insn-006f00a4) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`006f0128`](#insn-006f0128) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006efbbc`](#insn-006efbbc)

~~~json
{
  "source": "006efbbc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efbc0`](#insn-006efbc0)

~~~json
{
  "source": "006efbc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efbc4`](#insn-006efbc4)

~~~json
{
  "source": "006efbc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efbc8`](#insn-006efbc8)

~~~json
{
  "source": "006efbc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efbcc`](#insn-006efbcc)

~~~json
{
  "source": "006efbcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efbd0`](#insn-006efbd0)

~~~json
{
  "source": "006efbd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efbe8`](#insn-006efbe8)

~~~json
{
  "source": "006efbe8",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efbf0`](#insn-006efbf0)

~~~json
{
  "source": "006efbf0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efbf4`](#insn-006efbf4)

~~~json
{
  "source": "006efbf4",
  "target": "00464f48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efc04`](#insn-006efc04)

~~~json
{
  "source": "006efc04",
  "target": "00be7d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be7d28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006efc04`](#insn-006efc04)

~~~json
{
  "source": "006efc04",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efc0c`](#insn-006efc0c)

~~~json
{
  "source": "006efc0c",
  "target": "006eff30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efc18`](#insn-006efc18)

~~~json
{
  "source": "006efc18",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efc28`](#insn-006efc28)

~~~json
{
  "source": "006efc28",
  "target": "00293c35",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00293c35",
  "offset": 0,
  "size": 37,
  "datatype": "string",
  "bytes": "4761747961446174615f4f7074696f6e5f4368616e6365416e696d6174696f6e",
  "capture_start": "00293c35",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006efc28`](#insn-006efc28)

~~~json
{
  "source": "006efc28",
  "target": "00293c45",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00293c35",
  "offset": 16,
  "size": 37,
  "datatype": "string",
  "bytes": "4761747961446174615f4f7074696f6e5f4368616e6365416e696d6174696f6e",
  "capture_start": "00293c35",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006efc30`](#insn-006efc30)

~~~json
{
  "source": "006efc30",
  "target": "002b1620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efc38`](#insn-006efc38)

~~~json
{
  "source": "006efc38",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efc40`](#insn-006efc40)

~~~json
{
  "source": "006efc40",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efc5c`](#insn-006efc5c)

~~~json
{
  "source": "006efc5c",
  "target": "00ab11f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efc60`](#insn-006efc60)

~~~json
{
  "source": "006efc60",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efc68`](#insn-006efc68)

~~~json
{
  "source": "006efc68",
  "target": "006efc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efc6c`](#insn-006efc6c)

~~~json
{
  "source": "006efc6c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efc70`](#insn-006efc70)

~~~json
{
  "source": "006efc70",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efc74`](#insn-006efc74)

~~~json
{
  "source": "006efc74",
  "target": "006eff7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efc7c`](#insn-006efc7c)

~~~json
{
  "source": "006efc7c",
  "target": "00464a54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efc8c`](#insn-006efc8c)

~~~json
{
  "source": "006efc8c",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efc94`](#insn-006efc94)

~~~json
{
  "source": "006efc94",
  "target": "00464a54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efc98`](#insn-006efc98)

~~~json
{
  "source": "006efc98",
  "target": "006eff74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efca0`](#insn-006efca0)

~~~json
{
  "source": "006efca0",
  "target": "00465680",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efca8`](#insn-006efca8)

~~~json
{
  "source": "006efca8",
  "target": "006eff74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efcb8`](#insn-006efcb8)

~~~json
{
  "source": "006efcb8",
  "target": "00464b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efcbc`](#insn-006efcbc)

~~~json
{
  "source": "006efcbc",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efcc0`](#insn-006efcc0)

~~~json
{
  "source": "006efcc0",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efcd0`](#insn-006efcd0)

~~~json
{
  "source": "006efcd0",
  "target": "006efcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efcd4`](#insn-006efcd4)

~~~json
{
  "source": "006efcd4",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efcd8`](#insn-006efcd8)

~~~json
{
  "source": "006efcd8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efcdc`](#insn-006efcdc)

~~~json
{
  "source": "006efcdc",
  "target": "006eff74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efce4`](#insn-006efce4)

~~~json
{
  "source": "006efce4",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efcf0`](#insn-006efcf0)

~~~json
{
  "source": "006efcf0",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efcfc`](#insn-006efcfc)

~~~json
{
  "source": "006efcfc",
  "target": "006efd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efd04`](#insn-006efd04)

~~~json
{
  "source": "006efd04",
  "target": "006efd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efd1c`](#insn-006efd1c)

~~~json
{
  "source": "006efd1c",
  "target": "006f0074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efd38`](#insn-006efd38)

~~~json
{
  "source": "006efd38",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efd3c`](#insn-006efd3c)

~~~json
{
  "source": "006efd3c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efd40`](#insn-006efd40)

~~~json
{
  "source": "006efd40",
  "target": "006efd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efd48`](#insn-006efd48)

~~~json
{
  "source": "006efd48",
  "target": "006f0090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efd54`](#insn-006efd54)

~~~json
{
  "source": "006efd54",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efd60`](#insn-006efd60)

~~~json
{
  "source": "006efd60",
  "target": "006efd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efd80`](#insn-006efd80)

~~~json
{
  "source": "006efd80",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efd90`](#insn-006efd90)

~~~json
{
  "source": "006efd90",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efd94`](#insn-006efd94)

~~~json
{
  "source": "006efd94",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efd98`](#insn-006efd98)

~~~json
{
  "source": "006efd98",
  "target": "006f0224",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efda8`](#insn-006efda8)

~~~json
{
  "source": "006efda8",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efdc0`](#insn-006efdc0)

~~~json
{
  "source": "006efdc0",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efdd8`](#insn-006efdd8)

~~~json
{
  "source": "006efdd8",
  "target": "00465680",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efde4`](#insn-006efde4)

~~~json
{
  "source": "006efde4",
  "target": "006efc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efdf4`](#insn-006efdf4)

~~~json
{
  "source": "006efdf4",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efe0c`](#insn-006efe0c)

~~~json
{
  "source": "006efe0c",
  "target": "006efe18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efe14`](#insn-006efe14)

~~~json
{
  "source": "006efe14",
  "target": "006efea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efe2c`](#insn-006efe2c)

~~~json
{
  "source": "006efe2c",
  "target": "006f0040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efe48`](#insn-006efe48)

~~~json
{
  "source": "006efe48",
  "target": "006efe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efe50`](#insn-006efe50)

~~~json
{
  "source": "006efe50",
  "target": "006f005c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efe58`](#insn-006efe58)

~~~json
{
  "source": "006efe58",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efe60`](#insn-006efe60)

~~~json
{
  "source": "006efe60",
  "target": "006efe6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efe90`](#insn-006efe90)

~~~json
{
  "source": "006efe90",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efe9c`](#insn-006efe9c)

~~~json
{
  "source": "006efe9c",
  "target": "006efea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efea4`](#insn-006efea4)

~~~json
{
  "source": "006efea4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efeb4`](#insn-006efeb4)

~~~json
{
  "source": "006efeb4",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efed4`](#insn-006efed4)

~~~json
{
  "source": "006efed4",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efef4`](#insn-006efef4)

~~~json
{
  "source": "006efef4",
  "target": "00464a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eff10`](#insn-006eff10)

~~~json
{
  "source": "006eff10",
  "target": "006efdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eff1c`](#insn-006eff1c)

~~~json
{
  "source": "006eff1c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eff24`](#insn-006eff24)

~~~json
{
  "source": "006eff24",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eff2c`](#insn-006eff2c)

~~~json
{
  "source": "006eff2c",
  "target": "006efc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eff38`](#insn-006eff38)

~~~json
{
  "source": "006eff38",
  "target": "006eff28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eff40`](#insn-006eff40)

~~~json
{
  "source": "006eff40",
  "target": "006eff20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eff50`](#insn-006eff50)

~~~json
{
  "source": "006eff50",
  "target": "006eff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eff54`](#insn-006eff54)

~~~json
{
  "source": "006eff54",
  "target": "006eff18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eff5c`](#insn-006eff5c)

~~~json
{
  "source": "006eff5c",
  "target": "006eff14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eff68`](#insn-006eff68)

~~~json
{
  "source": "006eff68",
  "target": "006eff58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eff6c`](#insn-006eff6c)

~~~json
{
  "source": "006eff6c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eff70`](#insn-006eff70)

~~~json
{
  "source": "006eff70",
  "target": "006eff58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006eff78`](#insn-006eff78)

~~~json
{
  "source": "006eff78",
  "target": "00465780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006eff88`](#insn-006eff88)

~~~json
{
  "source": "006eff88",
  "target": "00c1ad70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ad70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006eff8c`](#insn-006eff8c)

~~~json
{
  "source": "006eff8c",
  "target": "00c1ad78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ad78",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006eff94`](#insn-006eff94)

~~~json
{
  "source": "006eff94",
  "target": "00c13408",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13408",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006eff9c`](#insn-006eff9c)

~~~json
{
  "source": "006eff9c",
  "target": "00be8808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8808",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006eff9c`](#insn-006eff9c)

~~~json
{
  "source": "006eff9c",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006effa0`](#insn-006effa0)

~~~json
{
  "source": "006effa0",
  "target": "00c113a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c113a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006effa0`](#insn-006effa0)

~~~json
{
  "source": "006effa0",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006effa4`](#insn-006effa4)

~~~json
{
  "source": "006effa4",
  "target": "00c11390",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11390",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c11390",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006effa8`](#insn-006effa8)

~~~json
{
  "source": "006effa8",
  "target": "00c13420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13420",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006effac`](#insn-006effac)

~~~json
{
  "source": "006effac",
  "target": "00c113d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c113d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006effb4`](#insn-006effb4)

~~~json
{
  "source": "006effb4",
  "target": "00c1ad80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ad80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006effb8`](#insn-006effb8)

~~~json
{
  "source": "006effb8",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006effc0`](#insn-006effc0)

~~~json
{
  "source": "006effc0",
  "target": "00c11128",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11118",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`006effc0`](#insn-006effc0)

~~~json
{
  "source": "006effc0",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006effc4`](#insn-006effc4)

~~~json
{
  "source": "006effc4",
  "target": "006effd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006effc8`](#insn-006effc8)

~~~json
{
  "source": "006effc8",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006effcc`](#insn-006effcc)

~~~json
{
  "source": "006effcc",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006effd4`](#insn-006effd4)

~~~json
{
  "source": "006effd4",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006effd8`](#insn-006effd8)

~~~json
{
  "source": "006effd8",
  "target": "00c13410",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13410",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006effe0`](#insn-006effe0)

~~~json
{
  "source": "006effe0",
  "target": "00bdb110",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006effe8`](#insn-006effe8)

~~~json
{
  "source": "006effe8",
  "target": "00bdb120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006effec`](#insn-006effec)

~~~json
{
  "source": "006effec",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efff0`](#insn-006efff0)

~~~json
{
  "source": "006efff0",
  "target": "006efffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efff4`](#insn-006efff4)

~~~json
{
  "source": "006efff4",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006efff8`](#insn-006efff8)

~~~json
{
  "source": "006efff8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006efffc`](#insn-006efffc)

~~~json
{
  "source": "006efffc",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0000`](#insn-006f0000)

~~~json
{
  "source": "006f0000",
  "target": "006f000c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0004`](#insn-006f0004)

~~~json
{
  "source": "006f0004",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0008`](#insn-006f0008)

~~~json
{
  "source": "006f0008",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006f000c`](#insn-006f000c)

~~~json
{
  "source": "006f000c",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0014`](#insn-006f0014)

~~~json
{
  "source": "006f0014",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f001c`](#insn-006f001c)

~~~json
{
  "source": "006f001c",
  "target": "006f0128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0024`](#insn-006f0024)

~~~json
{
  "source": "006f0024",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0028`](#insn-006f0028)

~~~json
{
  "source": "006f0028",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f002c`](#insn-006f002c)

~~~json
{
  "source": "006f002c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0030`](#insn-006f0030)

~~~json
{
  "source": "006f0030",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0034`](#insn-006f0034)

~~~json
{
  "source": "006f0034",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0038`](#insn-006f0038)

~~~json
{
  "source": "006f0038",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0040`](#insn-006f0040)

~~~json
{
  "source": "006f0040",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0048`](#insn-006f0048)

~~~json
{
  "source": "006f0048",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0050`](#insn-006f0050)

~~~json
{
  "source": "006f0050",
  "target": "006f0128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0058`](#insn-006f0058)

~~~json
{
  "source": "006f0058",
  "target": "006f02f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006f005c`](#insn-006f005c)

~~~json
{
  "source": "006f005c",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0064`](#insn-006f0064)

~~~json
{
  "source": "006f0064",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f006c`](#insn-006f006c)

~~~json
{
  "source": "006f006c",
  "target": "006f0128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0070`](#insn-006f0070)

~~~json
{
  "source": "006f0070",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006f0074`](#insn-006f0074)

~~~json
{
  "source": "006f0074",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f007c`](#insn-006f007c)

~~~json
{
  "source": "006f007c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0084`](#insn-006f0084)

~~~json
{
  "source": "006f0084",
  "target": "006f0128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f008c`](#insn-006f008c)

~~~json
{
  "source": "006f008c",
  "target": "006f02e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006f0090`](#insn-006f0090)

~~~json
{
  "source": "006f0090",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f0098`](#insn-006f0098)

~~~json
{
  "source": "006f0098",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f00a0`](#insn-006f00a0)

~~~json
{
  "source": "006f00a0",
  "target": "006f0128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006f00a4`](#insn-006f00a4)

~~~json
{
  "source": "006f00a4",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006f0128`](#insn-006f0128)

~~~json
{
  "source": "006f0128",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
