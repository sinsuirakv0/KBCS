# 00acfac4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0162.md#review-5ce2d2d1ae9d3b59c50f3b44e6ae2f1b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acfcc0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acf/00acfcc0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-313b479720196df2ccd9986ea2856999)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfac4",
  "name": "FUN_00acfac4",
  "size": 1708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fcbe1e6c9b4f54b2f752ce68ae1648ba26930ca30257599641fef53fc17f5fa0",
  "source_text_sha256": "fcbe1e6c9b4f54b2f752ce68ae1648ba26930ca30257599641fef53fc17f5fa0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfac4",
        "00ad016b"
      ],
      [
        "00ad01a0",
        "00ad01a3"
      ]
    ],
    "bytes_sha256": "4f0379d98e9d61603e2b870ec8161e98b595c536bc64a4fe6c13104f5464b4bc",
    "instruction_count": 427,
    "instruction_bytes": 1708,
    "body_bytes": 1708,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

- [00ad075c](../00ad0/00ad075c.md)
- [00ad6d50](../00ad6/00ad6d50.md)
- [00aec538](../00aec/00aec538.md)

## 呼び出し先

- [00498190](../00498/00498190.md)
- [006337a4](../00633/006337a4.md)
- [00666be8](../00666/00666be8.md)
- [00695b6c](../00695/00695b6c.md)
- [009a2998](../009a2/009a2998.md)
- [009df498](../009df/009df498.md)
- [009e0e24](../009e0/009e0e24.md)
- [009e2df8](../009e2/009e2df8.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c58210](../00c58/00c58210.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 13156 bytes

~~~c

void FUN_00acfac4(long param_1,ulong param_2)

{
  bool bVar1;
  long lVar2;
  long *plVar3;
  ulong uVar4;
  uint uVar5;
  ulong uVar6;
  long lVar7;
  int iVar8;
  long lVar9;
  ulong uVar10;
  long lVar11;
  long lVar12;
  int *piVar13;
  undefined4 *puVar14;
  ulong uVar15;
  ulong uVar16;
  ulong uVar17;
  byte *pbVar18;
  int iVar19;
  long *plVar20;
  long lVar21;
  long lVar22;
  long *plVar23;
  undefined2 uVar24;
  undefined8 uVar25;
  long local_88;
  long *local_80;
  int local_78;
  undefined1 uStack_71;
  int *local_70;
  long local_68;
  
  lVar7 = tpidr_el0;
  local_68 = *(long *)(lVar7 + 0x28);
  iVar8 = *(int *)((long)&fde_table_entry_00333a28.initial_loc + param_1);
  if (((param_2 & 1) != 0) || (DAT_00ca4220 != iVar8)) {
    DAT_00ca4220 = iVar8;
    if (DAT_00ca4578 == 0) {
      lVar9 = 0;
    }
    else {
      lVar9 = __dynamic_cast(DAT_00ca4578,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65a58,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d550,0);
    }
    if (*(int *)((long)&fde_table_entry_00333f48.data_loc + param_1) == 3) {
      pbVar18 = (byte *)(param_1 + 0x82a7b);
      iVar19 = 0;
      lVar2 = (long)iVar8 + 5;
      lVar22 = (long)iVar8 + -5;
      lVar21 = 0x378;
      do {
        if (((uint)(*(byte *)(param_1 + 0x8385a) ^ pbVar18[-1]) << 0x10 |
             (uint)(*(byte *)(param_1 + 0x8385b) ^ *pbVar18) << 0x18 |
             (uint)(*(byte *)(param_1 + 0x83859) ^ pbVar18[-2]) << 8 |
            (uint)(*(byte *)(param_1 + 0x83858) ^ pbVar18[-3])) != 0xffffffff) {
          if ((iVar19 < (int)lVar22) || ((int)lVar2 < iVar19)) {
            local_88 = 0;
            local_80 = (long *)0x0;
            local_70 = (int *)CONCAT44(local_70._4_4_,iVar19);
            FUN_009a2998(lVar9 + 0x318,&local_70);
          }
          else {
            if (((DAT_00ca4b38 & 1) == 0) &&
               (iVar8 = __cxa_guard_acquire(&DAT_00ca4b38), iVar8 != 0)) {
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
            uVar5 = (uint)(*(byte *)(param_1 + 0x8385a) ^ pbVar18[-1]) << 0x10 |
                    (uint)(*(byte *)(param_1 + 0x8385b) ^ *pbVar18) << 0x18 |
                    (uint)(*(byte *)(param_1 + 0x83859) ^ pbVar18[-2]) << 8 |
                    (uint)(*(byte *)(param_1 + 0x83858) ^ pbVar18[-3]);
            uVar10 = FUN_009e0e24(param_1 + 0x50,0xffffffff,0xffffffff);
            if ((((uVar10 & 1) == 0) ||
                (lVar11 = FUN_009e2df8(param_1 + 0x50,0xffffffff,0xffffffff), lVar11 == 0)) ||
               (lVar11 = FUN_009df498(lVar11,uVar5), lVar11 == 0)) {
              piVar13 = (int *)(param_1 + 0x49934 + (long)(int)uVar5 * 4);
            }
            else {
              piVar13 = (int *)(lVar11 + 4);
            }
            FUN_006337a4(&local_88,&DAT_00ca4b00,
                         "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                         + (long)*piVar13 * 0x78 + (long)(int)uVar5 * 0x1e0 + param_1 + 0x60,
                         PTR_DAT_00c9a8a0,0x1e,0,0,0);
            local_78 = iVar19;
            if (local_88 == 0) {
              FUN_009a2998(lVar9 + 0x318,&local_78);
            }
            else {
              local_70 = &local_78;
              lVar12 = FUN_00695b6c(lVar9 + 0x318,&local_78,&DAT_002c86b5,&local_70,&uStack_71);
              plVar3 = local_80;
              lVar11 = local_88;
              if (local_80 != (long *)0x0) {
                FUN_00c538b0(1,local_80 + 1);
              }
              plVar23 = *(long **)(lVar12 + 0x20);
              *(long *)(lVar12 + 0x18) = lVar11;
              *(long **)(lVar12 + 0x20) = plVar3;
              if ((plVar23 != (long *)0x0) &&
                 (lVar11 = FUN_00c538e0(0xffffffffffffffff,plVar23 + 1), lVar11 == 0)) {
                (**(code **)(*plVar23 + 0x10))(plVar23);
                _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar23);
              }
            }
          }
          plVar3 = local_80;
          if ((local_80 != (long *)0x0) &&
             (lVar11 = FUN_00c538e0(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
            (**(code **)(*plVar3 + 0x10))(plVar3);
            _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
          }
          iVar19 = iVar19 + 1;
        }
        lVar21 = lVar21 + -1;
        pbVar18 = pbVar18 + 4;
      } while (lVar21 != 0);
      if (-1 < *(int *)((long)&fde_table_entry_00335f78.initial_loc + param_1)) {
        plVar3 = (long *)(lVar9 + 0x2f0);
        lVar21 = 0;
        do {
                    /* try { // try from 00acfe60 to 00bcfec3 has its CatchHandler @ 00acfe60
                       catch() { ... } // from try @ 00acfe60 with catch @ 00acfe60
                       catch() { ... } // from try @ 00acfed8 with catch @ 00acfe60
                       catch() { ... } // from try @ 00acffa0 with catch @ 00acfe60
                       catch() { ... } // from try @ 00ad002c with catch @ 00acfe60 */
          if ((lVar21 < lVar22) || (lVar2 < lVar21)) {
            uVar10 = *(ulong *)(lVar9 + 0x2f8);
            if (uVar10 != 0) {
              uVar4 = lVar21 + 0xb;
              uVar25 = CONCAT17(POPCOUNT((char)(uVar10 >> 0x38)),
                                CONCAT16(POPCOUNT((char)(uVar10 >> 0x30)),
                                         CONCAT15(POPCOUNT((char)(uVar10 >> 0x28)),
                                                  CONCAT14(POPCOUNT((char)(uVar10 >> 0x20)),
                                                           CONCAT13(POPCOUNT((char)(uVar10 >> 0x18))
                                                                    ,CONCAT12(POPCOUNT((char)(uVar10
                                                                                             >> 0x10
                                                  )),CONCAT11(POPCOUNT((char)(uVar10 >> 8)),
                                                              POPCOUNT((char)uVar10))))))));
              uVar24 = NEON_uaddlv(uVar25,1);
              uVar15 = CONCAT62((int6)((ulong)uVar25 >> 0x10),uVar24) & 0xffffffff;
              if (uVar15 < 2) {
                    /* try { // try from 00acff18 to 00bcff2b has its CatchHandler @ 00ad0150 */
                uVar16 = uVar10 + 0x7fffffff & uVar4;
              }
              else {
                uVar16 = uVar4;
                if (uVar10 <= uVar4) {
                  uVar16 = 0;
                  if (uVar10 != 0) {
                    uVar16 = uVar4 / uVar10;
                  }
                  uVar16 = uVar4 - uVar16 * uVar10;
                }
              }
              plVar23 = *(long **)(*plVar3 + uVar16 * 8);
                    /* try { // try from 00ad0020 to 00bd002b has its CatchHandler @ 00ad014c */
              if ((plVar23 != (long *)0x0) && (plVar23 = (long *)*plVar23, plVar23 != (long *)0x0))
              {
                do {
                  uVar17 = plVar23[1];
                  if (uVar17 == uVar4) {
                    /* try { // try from 00ad002c to 00bd0183 has its CatchHandler @ 00acfe60 */
                    if (uVar4 == *(uint *)(plVar23 + 2)) {
                      local_88 = 0;
                      local_80 = (long *)0x0;
                      local_70 = (int *)CONCAT44(local_70._4_4_,(int)uVar4);
                      FUN_009a2998(plVar3,&local_70);
                      plVar23 = local_80;
                      if ((local_80 != (long *)0x0) &&
                         (lVar11 = FUN_00c538e0(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
                        (**(code **)(*plVar23 + 0x10))(plVar23);
                        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar23);
                      }
                      break;
                    }
                  }
                  else {
                    if (uVar15 < 2) {
                      uVar17 = uVar17 & uVar10 - 1;
                    }
                    else if (uVar10 <= uVar17) {
                      uVar6 = 0;
                      if (uVar10 != 0) {
                        uVar6 = uVar17 / uVar10;
                      }
                      uVar17 = uVar17 - uVar6 * uVar10;
                    }
                    if (uVar17 != uVar16) break;
                  }
                  plVar23 = (long *)*plVar23;
                } while (plVar23 != (long *)0x0);
              }
            }
          }
          else {
            pbVar18 = (byte *)(param_1 + 0x82a78 + lVar21 * 4);
            uVar5 = (uint)(*(byte *)(param_1 + 0x8385a) ^ pbVar18[2]) << 0x10 |
                    (uint)(*(byte *)(param_1 + 0x8385b) ^ pbVar18[3]) << 0x18 |
                    (uint)(*(byte *)(param_1 + 0x83859) ^ pbVar18[1]) << 8 |
                    (uint)(*(byte *)(param_1 + 0x83858) ^ *pbVar18);
            uVar10 = FUN_009e0e24(param_1 + 0x50,0xffffffff,0xffffffff);
                    /* try { // try from 00acfec4 to 00bcfed7 has its CatchHandler @ 00ad0134 */
                    /* try { // try from 00acfed8 to 00bcff17 has its CatchHandler @ 00acfe60 */
            if ((((uVar10 & 1) == 0) ||
                (lVar11 = FUN_009e2df8(param_1 + 0x50,0xffffffff,0xffffffff), lVar11 == 0)) ||
               (lVar11 = FUN_009df498(lVar11,uVar5), lVar11 == 0)) {
              puVar14 = (undefined4 *)(param_1 + 0x49934 + (long)(int)uVar5 * 4);
            }
            else {
              puVar14 = (undefined4 *)(lVar11 + 4);
            }
                    /* try { // try from 00acff38 to 00bcff43 has its CatchHandler @ 00ad0158 */
            FUN_00666be8(&local_88,uVar5,*puVar14);
            local_78 = (int)lVar21 + 0xb;
            if (local_88 == 0) {
              FUN_009a2998(plVar3,&local_78);
            }
            else {
              local_70 = &local_78;
                    /* try { // try from 00acff60 to 00bcff67 has its CatchHandler @ 00ad014c */
              lVar12 = FUN_00695b6c(plVar3,&local_78,&DAT_002c86b5,&local_70,&uStack_71);
              plVar23 = local_80;
              lVar11 = local_88;
              if (local_80 != (long *)0x0) {
                FUN_00c538b0(1,local_80 + 1);
              }
              plVar20 = *(long **)(lVar12 + 0x20);
              *(long *)(lVar12 + 0x18) = lVar11;
              *(long **)(lVar12 + 0x20) = plVar23;
                    /* try { // try from 00acff8c to 00bcff9f has its CatchHandler @ 00ad0130 */
              if ((plVar20 != (long *)0x0) &&
                 (lVar11 = FUN_00c538e0(0xffffffffffffffff,plVar20 + 1), lVar11 == 0)) {
                    /* try { // try from 00acffa0 to 00bcffdf has its CatchHandler @ 00acfe60 */
                (**(code **)(*plVar20 + 0x10))(plVar20);
                _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar20);
              }
            }
            plVar23 = local_80;
            if ((local_80 != (long *)0x0) &&
               (lVar11 = FUN_00c538e0(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
                    /* try { // try from 00acffe0 to 00bcfff3 has its CatchHandler @ 00ad0154 */
              (**(code **)(*plVar23 + 0x10))(plVar23);
              _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar23);
                    /* try { // try from 00acfff8 to 00bd0003 has its CatchHandler @ 00ad015c */
            }
          }
          bVar1 = lVar21 < *(int *)((long)&fde_table_entry_00335f78.initial_loc + param_1);
          lVar21 = lVar21 + 1;
        } while (bVar1);
      }
    }
  }
  if (((DAT_00ca4b38 & 1) == 0) && (iVar8 = __cxa_guard_acquire(&DAT_00ca4b38), iVar8 != 0)) {
                    /* catch() { ... } // from try @ 00acff8c with catch @ 00ad0130 */
                    /* catch() { ... } // from try @ 00acfec4 with catch @ 00ad0134 */
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
                    /* catch() { ... } // from try @ 00acff60 with catch @ 00ad014c
                       catch() { ... } // from try @ 00ad0020 with catch @ 00ad014c */
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
                    /* catch() { ... } // from try @ 00acff18 with catch @ 00ad0150 */
    DAT_00ca4b20 = 0;
                    /* catch() { ... } // from try @ 00acffe0 with catch @ 00ad0154 */
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
                    /* catch() { ... } // from try @ 00acff38 with catch @ 00ad0158 */
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
                    /* catch() { ... } // from try @ 00acfff8 with catch @ 00ad015c */
    __cxa_guard_release(&DAT_00ca4b38);
  }
  if (DAT_00ca4b30 != 0) {
    FUN_00498190();
  }
  if (*(long *)(lVar7 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acfac4"></a> `00acfac4` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00acfac8"></a> `00acfac8` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acfacc"></a> `00acfacc` | `fc 6f 07 a9` | stp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acfad0"></a> `00acfad0` | `fa 67 08 a9` | stp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acfad4"></a> `00acfad4` | `f8 5f 09 a9` | stp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acfad8"></a> `00acfad8` | `f6 57 0a a9` | stp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acfadc"></a> `00acfadc` | `f4 4f 0b a9` | stp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acfae0"></a> `00acfae0` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acfae4"></a> `00acfae4` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acfae8"></a> `00acfae8` | `09 cc 4c 91` | add x9,x0,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00acfaec"></a> `00acfaec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acfaf0"></a> `00acfaf0` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acfaf4"></a> `00acfaf4` | `36 a1 28 91` | add x22,x9,#0xa28 | `FALL_THROUGH`
<a id="insn-00acfaf8"></a> `00acfaf8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00acfafc"></a> `00acfafc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfb00"></a> `00acfb00` | `a8 0e 00 b0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfb04"></a> `00acfb04` | `d4 02 40 b9` | ldr w20,[x22] | `FALL_THROUGH`
<a id="insn-00acfb08"></a> `00acfb08` | `81 00 00 37` | tbnz w1,#0x0,0x00acfb18 | `CONDITIONAL_JUMP`
<a id="insn-00acfb0c"></a> `00acfb0c` | `09 21 42 b9` | ldr w9,[x8, #0x220] | `FALL_THROUGH`
<a id="insn-00acfb10"></a> `00acfb10` | `3f 01 14 6b` | cmp w9,w20 | `FALL_THROUGH`
<a id="insn-00acfb14"></a> `00acfb14` | `60 2d 00 54` | b.eq 0x00ad00c0 | `CONDITIONAL_JUMP`
<a id="insn-00acfb18"></a> `00acfb18` | `a9 0e 00 b0` | adrp x9,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfb1c"></a> `00acfb1c` | `14 21 02 b9` | str w20,[x8, #0x220] | `FALL_THROUGH`
<a id="insn-00acfb20"></a> `00acfb20` | `20 bd 42 f9` | ldr x0,[x9, #0x578] | `FALL_THROUGH`
<a id="insn-00acfb24"></a> `00acfb24` | `20 01 00 b4` | cbz x0,0x00acfb48 | `CONDITIONAL_JUMP`
<a id="insn-00acfb28"></a> `00acfb28` | `a1 0c 00 d0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00acfb2c"></a> `00acfb2c` | `21 60 29 91` | add x1,x1,#0xa58 | `FALL_THROUGH`
<a id="insn-00acfb30"></a> `00acfb30` | `e2 0d 00 d0` | adrp x2,0xc8d000 | `FALL_THROUGH`
<a id="insn-00acfb34"></a> `00acfb34` | `42 40 15 91` | add x2,x2,#0x550 | `FALL_THROUGH`
<a id="insn-00acfb38"></a> `00acfb38` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00acfb3c"></a> `00acfb3c` | `b5 21 06 94` | bl 0x00c58210 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb40"></a> `00acfb40` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acfb44"></a> `00acfb44` | `02 00 00 14` | b 0x00acfb4c | `UNCONDITIONAL_JUMP`
<a id="insn-00acfb48"></a> `00acfb48` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00acfb4c"></a> `00acfb4c` | `c8 26 45 b9` | ldr w8,[x22, #0x524] | `FALL_THROUGH`
<a id="insn-00acfb50"></a> `00acfb50` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00acfb54"></a> `00acfb54` | `61 2b 00 54` | b.ne 0x00ad00c0 | `CONDITIONAL_JUMP`
<a id="insn-00acfb58"></a> `00acfb58` | `89 7e 40 93` | sxtw x9,w20 | `FALL_THROUGH`
<a id="insn-00acfb5c"></a> `00acfb5c` | `68 0a 42 91` | add x8,x19,#0x82, LSL #12 | `FALL_THROUGH`
<a id="insn-00acfb60"></a> `00acfb60` | `6a 0a 42 91` | add x10,x19,#0x82, LSL #12 | `FALL_THROUGH`
<a id="insn-00acfb64"></a> `00acfb64` | `17 ed 29 91` | add x23,x8,#0xa7b | `FALL_THROUGH`
<a id="insn-00acfb68"></a> `00acfb68` | `4b e1 29 91` | add x11,x10,#0xa78 | `FALL_THROUGH`
<a id="insn-00acfb6c"></a> `00acfb6c` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00acfb70"></a> `00acfb70` | `28 15 00 91` | add x8,x9,#0x5 | `FALL_THROUGH`
<a id="insn-00acfb74"></a> `00acfb74` | `3a 15 00 d1` | sub x26,x9,#0x5 | `FALL_THROUGH`
<a id="insn-00acfb78"></a> `00acfb78` | `19 6f 80 52` | mov w25,#0x378 | `FALL_THROUGH`
<a id="insn-00acfb7c"></a> `00acfb7c` | `f5 a3 02 a9` | stp x21,x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acfb80"></a> `00acfb80` | `68 12 4b 91` | add x8,x19,#0x2c4, LSL #12 | `FALL_THROUGH`
<a id="insn-00acfb84"></a> `00acfb84` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00acfb88"></a> `00acfb88` | `08 61 1a 91` | add x8,x8,#0x698 | `FALL_THROUGH`
<a id="insn-00acfb8c"></a> `00acfb8c` | `eb 23 01 a9` | stp x11,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfb90"></a> `00acfb90` | `68 26 41 91` | add x8,x19,#0x49, LSL #12 | `FALL_THROUGH`
<a id="insn-00acfb94"></a> `00acfb94` | `08 d1 24 91` | add x8,x8,#0x934 | `FALL_THROUGH`
<a id="insn-00acfb98"></a> `00acfb98` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfb9c"></a> `00acfb9c` | `05 00 00 14` | b 0x00acfbb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfba0"></a> `00acfba0` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00acfba4"></a> `00acfba4` | `39 07 00 f1` | subs x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00acfba8"></a> `00acfba8` | `94 12 00 91` | add x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00acfbac"></a> `00acfbac` | `60 13 00 54` | b.eq 0x00acfe18 | `CONDITIONAL_JUMP`
<a id="insn-00acfbb0"></a> `00acfbb0` | `88 f2 5f 38` | ldurb w8,[x20, #-0x1] | `FALL_THROUGH`
<a id="insn-00acfbb4"></a> `00acfbb4` | `e9 7e 77 39` | ldrb w9,[x23, #0xddf] | `FALL_THROUGH`
<a id="insn-00acfbb8"></a> `00acfbb8` | `ea 82 77 39` | ldrb w10,[x23, #0xde0] | `FALL_THROUGH`
<a id="insn-00acfbbc"></a> `00acfbbc` | `8b e2 5f 38` | ldurb w11,[x20, #-0x2] | `FALL_THROUGH`
<a id="insn-00acfbc0"></a> `00acfbc0` | `ec 7a 77 39` | ldrb w12,[x23, #0xdde] | `FALL_THROUGH`
<a id="insn-00acfbc4"></a> `00acfbc4` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00acfbc8"></a> `00acfbc8` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00acfbcc"></a> `00acfbcc` | `08 3d 10 53` | lsl w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00acfbd0"></a> `00acfbd0` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00acfbd4"></a> `00acfbd4` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00acfbd8"></a> `00acfbd8` | `ea 76 77 39` | ldrb w10,[x23, #0xddd] | `FALL_THROUGH`
<a id="insn-00acfbdc"></a> `00acfbdc` | `08 61 09 2a` | orr w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00acfbe0"></a> `00acfbe0` | `89 d2 5f 38` | ldurb w9,[x20, #-0x3] | `FALL_THROUGH`
<a id="insn-00acfbe4"></a> `00acfbe4` | `08 21 0b 2a` | orr w8,w8,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00acfbe8"></a> `00acfbe8` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00acfbec"></a> `00acfbec` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00acfbf0"></a> `00acfbf0` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfbf4"></a> `00acfbf4` | `80 fd ff 54` | b.eq 0x00acfba4 | `CONDITIONAL_JUMP`
<a id="insn-00acfbf8"></a> `00acfbf8` | `1f 03 1a 6b` | cmp w24,w26 | `FALL_THROUGH`
<a id="insn-00acfbfc"></a> `00acfbfc` | `0b 05 00 54` | b.lt 0x00acfc9c | `CONDITIONAL_JUMP`
<a id="insn-00acfc00"></a> `00acfc00` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acfc04"></a> `00acfc04` | `1f 03 08 6b` | cmp w24,w8 | `FALL_THROUGH`
<a id="insn-00acfc08"></a> `00acfc08` | `ac 04 00 54` | b.gt 0x00acfc9c | `CONDITIONAL_JUMP`
<a id="insn-00acfc0c"></a> `00acfc0c` | `a8 0e 00 b0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfc10"></a> `00acfc10` | `08 e1 2c 91` | add x8,x8,#0xb38 | `FALL_THROUGH`
<a id="insn-00acfc14"></a> `00acfc14` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00acfc18"></a> `00acfc18` | `48 0d 00 36` | tbz w8,#0x0,0x00acfdc0 | `CONDITIONAL_JUMP`
<a id="insn-00acfc1c"></a> `00acfc1c` | `88 f2 5f 38` | ldurb w8,[x20, #-0x1] | `FALL_THROUGH`
<a id="insn-00acfc20"></a> `00acfc20` | `e9 7e 77 39` | ldrb w9,[x23, #0xddf] | `FALL_THROUGH`
<a id="insn-00acfc24"></a> `00acfc24` | `60 42 01 91` | add x0,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00acfc28"></a> `00acfc28` | `ea 82 77 39` | ldrb w10,[x23, #0xde0] | `FALL_THROUGH`
<a id="insn-00acfc2c"></a> `00acfc2c` | `8b e2 5f 38` | ldurb w11,[x20, #-0x2] | `FALL_THROUGH`
<a id="insn-00acfc30"></a> `00acfc30` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfc34"></a> `00acfc34` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00acfc38"></a> `00acfc38` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00acfc3c"></a> `00acfc3c` | `ec 7a 77 39` | ldrb w12,[x23, #0xdde] | `FALL_THROUGH`
<a id="insn-00acfc40"></a> `00acfc40` | `08 3d 10 53` | lsl w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00acfc44"></a> `00acfc44` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfc48"></a> `00acfc48` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00acfc4c"></a> `00acfc4c` | `ea 76 77 39` | ldrb w10,[x23, #0xddd] | `FALL_THROUGH`
<a id="insn-00acfc50"></a> `00acfc50` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00acfc54"></a> `00acfc54` | `08 61 09 2a` | orr w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00acfc58"></a> `00acfc58` | `89 d2 5f 38` | ldurb w9,[x20, #-0x3] | `FALL_THROUGH`
<a id="insn-00acfc5c"></a> `00acfc5c` | `08 21 0b 2a` | orr w8,w8,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00acfc60"></a> `00acfc60` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00acfc64"></a> `00acfc64` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00acfc68"></a> `00acfc68` | `1b 7d 40 93` | sxtw x27,w8 | `FALL_THROUGH`
<a id="insn-00acfc6c"></a> `00acfc6c` | `6e 44 fc 97` | bl 0x009e0e24 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc70"></a> `00acfc70` | `20 02 00 36` | tbz w0,#0x0,0x00acfcb4 | `CONDITIONAL_JUMP`
<a id="insn-00acfc74"></a> `00acfc74` | `60 42 01 91` | add x0,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00acfc78"></a> `00acfc78` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfc7c"></a> `00acfc7c` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfc80"></a> `00acfc80` | `5e 4c fc 97` | bl 0x009e2df8 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc84"></a> `00acfc84` | `80 01 00 b4` | cbz x0,0x00acfcb4 | `CONDITIONAL_JUMP`
<a id="insn-00acfc88"></a> `00acfc88` | `e1 03 1b 2a` | mov w1,w27 | `FALL_THROUGH`
<a id="insn-00acfc8c"></a> `00acfc8c` | `03 3e fc 97` | bl 0x009df498 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc90"></a> `00acfc90` | `20 01 00 b4` | cbz x0,0x00acfcb4 | `CONDITIONAL_JUMP`
<a id="insn-00acfc94"></a> `00acfc94` | `08 10 00 91` | add x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00acfc98"></a> `00acfc98` | `09 00 00 14` | b 0x00acfcbc | `UNCONDITIONAL_JUMP`
<a id="insn-00acfc9c"></a> `00acfc9c` | `bf ff 3d a9` | stp xzr,xzr,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acfca0"></a> `00acfca0` | `b8 03 1f b8` | stur w24,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acfca4"></a> `00acfca4` | `a0 62 0c 91` | add x0,x21,#0x318 | `FALL_THROUGH`
<a id="insn-00acfca8"></a> `00acfca8` | `a1 43 00 d1` | sub x1,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00acfcac"></a> `00acfcac` | `3b 4b fb 97` | bl 0x009a2998 | `UNCONDITIONAL_CALL`
<a id="insn-00acfcb0"></a> `00acfcb0` | `37 00 00 14` | b 0x00acfd8c | `UNCONDITIONAL_JUMP`
<a id="insn-00acfcb4"></a> `00acfcb4` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfcb8"></a> `00acfcb8` | `08 09 1b 8b` | add x8,x8,x27, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00acfcbc"></a> `00acfcbc` | `08 01 80 b9` | ldrsw x8,[x8] | `FALL_THROUGH`
<a id="insn-00acfcc0"></a> `00acfcc0` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acfcc4"></a> `00acfcc4` | `0a 3c 80 52` | mov w10,#0x1e0 | `FALL_THROUGH`
<a id="insn-00acfcc8"></a> `00acfcc8` | `69 27 2a 9b` | smaddl x9,w27,w10,x9 | `FALL_THROUGH`
<a id="insn-00acfccc"></a> `00acfccc` | `0a 0f 80 52` | mov w10,#0x78 | `FALL_THROUGH`
<a id="insn-00acfcd0"></a> `00acfcd0` | `42 0e 00 f0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00acfcd4"></a> `00acfcd4` | `01 25 2a 9b` | smaddl x1,w8,w10,x9 | `FALL_THROUGH`
<a id="insn-00acfcd8"></a> `00acfcd8` | `42 50 44 f9` | ldr x2,[x2, #0x8a0] | `FALL_THROUGH`
<a id="insn-00acfcdc"></a> `00acfcdc` | `a8 a3 00 d1` | sub x8,x29,#0x28 | `FALL_THROUGH`
<a id="insn-00acfce0"></a> `00acfce0` | `a0 0e 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfce4"></a> `00acfce4` | `00 00 2c 91` | add x0,x0,#0xb00 | `FALL_THROUGH`
<a id="insn-00acfce8"></a> `00acfce8` | `c3 03 80 52` | mov w3,#0x1e | `FALL_THROUGH`
<a id="insn-00acfcec"></a> `00acfcec` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00acfcf0"></a> `00acfcf0` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00acfcf4"></a> `00acfcf4` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00acfcf8"></a> `00acfcf8` | `ab 8e ed 97` | bl 0x006337a4 | `UNCONDITIONAL_CALL`
<a id="insn-00acfcfc"></a> `00acfcfc` | `a8 83 5d f8` | ldur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acfd00"></a> `00acfd00` | `b8 83 1e b8` | stur w24,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00acfd04"></a> `00acfd04` | `e8 03 00 b4` | cbz x8,0x00acfd80 | `CONDITIONAL_JUMP`
<a id="insn-00acfd08"></a> `00acfd08` | `a8 63 00 d1` | sub x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acfd0c"></a> `00acfd0c` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acfd10"></a> `00acfd10` | `a0 62 0c 91` | add x0,x21,#0x318 | `FALL_THROUGH`
<a id="insn-00acfd14"></a> `00acfd14` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acfd18"></a> `00acfd18` | `a3 43 00 d1` | sub x3,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00acfd1c"></a> `00acfd1c` | `a4 47 00 d1` | sub x4,x29,#0x11 | `FALL_THROUGH`
<a id="insn-00acfd20"></a> `00acfd20` | `c2 bf ff b0` | adrp x2,0x2c8000 | `FALL_THROUGH`
<a id="insn-00acfd24"></a> `00acfd24` | `42 d4 1a 91` | add x2,x2,#0x6b5 | `FALL_THROUGH`
<a id="insn-00acfd28"></a> `00acfd28` | `91 17 ef 97` | bl 0x00695b6c | `UNCONDITIONAL_CALL`
<a id="insn-00acfd2c"></a> `00acfd2c` | `b5 db 7d a9` | ldp x21,x22,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acfd30"></a> `00acfd30` | `fc 03 00 aa` | mov x28,x0 | `FALL_THROUGH`
<a id="insn-00acfd34"></a> `00acfd34` | `96 00 00 b4` | cbz x22,0x00acfd44 | `CONDITIONAL_JUMP`
<a id="insn-00acfd38"></a> `00acfd38` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00acfd3c"></a> `00acfd3c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acfd40"></a> `00acfd40` | `dc 0e 06 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd44"></a> `00acfd44` | `9b 13 40 f9` | ldr x27,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00acfd48"></a> `00acfd48` | `95 db 01 a9` | stp x21,x22,[x28, #0x18] | `FALL_THROUGH`
<a id="insn-00acfd4c"></a> `00acfd4c` | `f5 17 40 f9` | ldr x21,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acfd50"></a> `00acfd50` | `fb 01 00 b4` | cbz x27,0x00acfd8c | `CONDITIONAL_JUMP`
<a id="insn-00acfd54"></a> `00acfd54` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00acfd58"></a> `00acfd58` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acfd5c"></a> `00acfd5c` | `e1 0e 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd60"></a> `00acfd60` | `60 01 00 b5` | cbnz x0,0x00acfd8c | `CONDITIONAL_JUMP`
<a id="insn-00acfd64"></a> `00acfd64` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00acfd68"></a> `00acfd68` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00acfd6c"></a> `00acfd6c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acfd70"></a> `00acfd70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acfd74"></a> `00acfd74` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00acfd78"></a> `00acfd78` | `42 1f 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd7c"></a> `00acfd7c` | `04 00 00 14` | b 0x00acfd8c | `UNCONDITIONAL_JUMP`
<a id="insn-00acfd80"></a> `00acfd80` | `a0 62 0c 91` | add x0,x21,#0x318 | `FALL_THROUGH`
<a id="insn-00acfd84"></a> `00acfd84` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acfd88"></a> `00acfd88` | `04 4b fb 97` | bl 0x009a2998 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd8c"></a> `00acfd8c` | `bb 03 5e f8` | ldur x27,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acfd90"></a> `00acfd90` | `9b f0 ff b4` | cbz x27,0x00acfba0 | `CONDITIONAL_JUMP`
<a id="insn-00acfd94"></a> `00acfd94` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00acfd98"></a> `00acfd98` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acfd9c"></a> `00acfd9c` | `d1 0e 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfda0"></a> `00acfda0` | `00 f0 ff b5` | cbnz x0,0x00acfba0 | `CONDITIONAL_JUMP`
<a id="insn-00acfda4"></a> `00acfda4` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00acfda8"></a> `00acfda8` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00acfdac"></a> `00acfdac` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acfdb0"></a> `00acfdb0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acfdb4"></a> `00acfdb4` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00acfdb8"></a> `00acfdb8` | `32 1f 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00acfdbc"></a> `00acfdbc` | `79 ff ff 17` | b 0x00acfba0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfdc0"></a> `00acfdc0` | `a0 0e 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfdc4"></a> `00acfdc4` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00acfdc8"></a> `00acfdc8` | `22 1f 06 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00acfdcc"></a> `00acfdcc` | `80 f2 ff 34` | cbz w0,0x00acfc1c | `CONDITIONAL_JUMP`
<a id="insn-00acfdd0"></a> `00acfdd0` | `a1 0e 00 b0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfdd4"></a> `00acfdd4` | `21 00 2c 91` | add x1,x1,#0xb00 | `FALL_THROUGH`
<a id="insn-00acfdd8"></a> `00acfdd8` | `60 cd ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00acfddc"></a> `00acfddc` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00acfde0"></a> `00acfde0` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acfde4"></a> `00acfde4` | `82 0c 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00acfde8"></a> `00acfde8` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00acfdec"></a> `00acfdec` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00acfdf0"></a> `00acfdf0` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00acfdf4"></a> `00acfdf4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acfdf8"></a> `00acfdf8` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00acfdfc"></a> `00acfdfc` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acfe00"></a> `00acfe00` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00acfe04"></a> `00acfe04` | `0b 1f 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00acfe08"></a> `00acfe08` | `a0 0e 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfe0c"></a> `00acfe0c` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00acfe10"></a> `00acfe10` | `18 1f 06 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00acfe14"></a> `00acfe14` | `82 ff ff 17` | b 0x00acfc1c | `UNCONDITIONAL_JUMP`
<a id="insn-00acfe18"></a> `00acfe18` | `08 ef 8b 52` | mov w8,#0x5f78 | `FALL_THROUGH`
<a id="insn-00acfe1c"></a> `00acfe1c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acfe20"></a> `00acfe20` | `68 6a 68 b8` | ldr w8,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acfe24"></a> `00acfe24` | `e8 14 f8 37` | tbnz w8,#0x1f,0x00ad00c0 | `CONDITIONAL_JUMP`
<a id="insn-00acfe28"></a> `00acfe28` | `fc 03 1f aa` | mov x28,xzr | `FALL_THROUGH`
<a id="insn-00acfe2c"></a> `00acfe2c` | `b6 c2 0b 91` | add x22,x21,#0x2f0 | `FALL_THROUGH`
<a id="insn-00acfe30"></a> `00acfe30` | `db bf ff b0` | adrp x27,0x2c8000 | `FALL_THROUGH`
<a id="insn-00acfe34"></a> `00acfe34` | `7b d7 1a 91` | add x27,x27,#0x6b5 | `FALL_THROUGH`
<a id="insn-00acfe38"></a> `00acfe38` | `08 00 00 14` | b 0x00acfe58 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfe3c"></a> `00acfe3c` | `f5 17 40 f9` | ldr x21,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acfe40"></a> `00acfe40` | `08 ef 8b 52` | mov w8,#0x5f78 | `FALL_THROUGH`
<a id="insn-00acfe44"></a> `00acfe44` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acfe48"></a> `00acfe48` | `68 6a a8 b8` | ldrsw x8,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acfe4c"></a> `00acfe4c` | `9f 03 08 eb` | cmp x28,x8 | `FALL_THROUGH`
<a id="insn-00acfe50"></a> `00acfe50` | `9c 07 00 91` | add x28,x28,#0x1 | `FALL_THROUGH`
<a id="insn-00acfe54"></a> `00acfe54` | `6a 13 00 54` | b.ge 0x00ad00c0 | `CONDITIONAL_JUMP`
<a id="insn-00acfe58"></a> `00acfe58` | `9f 03 1a eb` | cmp x28,x26 | `FALL_THROUGH`
<a id="insn-00acfe5c"></a> `00acfe5c` | `ab 04 00 54` | b.lt 0x00acfef0 | `CONDITIONAL_JUMP`
<a id="insn-00acfe60"></a> `00acfe60` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acfe64"></a> `00acfe64` | `9f 03 08 eb` | cmp x28,x8 | `FALL_THROUGH`
<a id="insn-00acfe68"></a> `00acfe68` | `4c 04 00 54` | b.gt 0x00acfef0 | `CONDITIONAL_JUMP`
<a id="insn-00acfe6c"></a> `00acfe6c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfe70"></a> `00acfe70` | `ea 7e 77 39` | ldrb w10,[x23, #0xddf] | `FALL_THROUGH`
<a id="insn-00acfe74"></a> `00acfe74` | `60 42 01 91` | add x0,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00acfe78"></a> `00acfe78` | `eb 82 77 39` | ldrb w11,[x23, #0xde0] | `FALL_THROUGH`
<a id="insn-00acfe7c"></a> `00acfe7c` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfe80"></a> `00acfe80` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfe84"></a> `00acfe84` | `08 09 1c 8b` | add x8,x8,x28, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00acfe88"></a> `00acfe88` | `09 09 40 39` | ldrb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00acfe8c"></a> `00acfe8c` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00acfe90"></a> `00acfe90` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00acfe94"></a> `00acfe94` | `0a 0d 40 39` | ldrb w10,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00acfe98"></a> `00acfe98` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00acfe9c"></a> `00acfe9c` | `29 3d 10 53` | lsl w9,w9,#0x10 | `FALL_THROUGH`
<a id="insn-00acfea0"></a> `00acfea0` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00acfea4"></a> `00acfea4` | `eb 7a 77 39` | ldrb w11,[x23, #0xdde] | `FALL_THROUGH`
<a id="insn-00acfea8"></a> `00acfea8` | `29 61 0a 2a` | orr w9,w9,w10, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00acfeac"></a> `00acfeac` | `ea 76 77 39` | ldrb w10,[x23, #0xddd] | `FALL_THROUGH`
<a id="insn-00acfeb0"></a> `00acfeb0` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00acfeb4"></a> `00acfeb4` | `29 21 0b 2a` | orr w9,w9,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00acfeb8"></a> `00acfeb8` | `48 01 08 4a` | eor w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00acfebc"></a> `00acfebc` | `38 01 08 2a` | orr w24,w9,w8 | `FALL_THROUGH`
<a id="insn-00acfec0"></a> `00acfec0` | `d9 43 fc 97` | bl 0x009e0e24 | `UNCONDITIONAL_CALL`
<a id="insn-00acfec4"></a> `00acfec4` | `00 03 00 36` | tbz w0,#0x0,0x00acff24 | `CONDITIONAL_JUMP`
<a id="insn-00acfec8"></a> `00acfec8` | `60 42 01 91` | add x0,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00acfecc"></a> `00acfecc` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfed0"></a> `00acfed0` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfed4"></a> `00acfed4` | `c9 4b fc 97` | bl 0x009e2df8 | `UNCONDITIONAL_CALL`
<a id="insn-00acfed8"></a> `00acfed8` | `60 02 00 b4` | cbz x0,0x00acff24 | `CONDITIONAL_JUMP`
<a id="insn-00acfedc"></a> `00acfedc` | `e1 03 18 2a` | mov w1,w24 | `FALL_THROUGH`
<a id="insn-00acfee0"></a> `00acfee0` | `6e 3d fc 97` | bl 0x009df498 | `UNCONDITIONAL_CALL`
<a id="insn-00acfee4"></a> `00acfee4` | `00 02 00 b4` | cbz x0,0x00acff24 | `CONDITIONAL_JUMP`
<a id="insn-00acfee8"></a> `00acfee8` | `08 10 00 91` | add x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00acfeec"></a> `00acfeec` | `10 00 00 14` | b 0x00acff2c | `UNCONDITIONAL_JUMP`
<a id="insn-00acfef0"></a> `00acfef0` | `a8 7e 41 f9` | ldr x8,[x21, #0x2f8] | `FALL_THROUGH`
<a id="insn-00acfef4"></a> `00acfef4` | `68 fa ff b4` | cbz x8,0x00acfe40 | `CONDITIONAL_JUMP`
<a id="insn-00acfef8"></a> `00acfef8` | `00 01 67 9e` | fmov d0,x8 | `FALL_THROUGH`
<a id="insn-00acfefc"></a> `00acfefc` | `89 2f 00 91` | add x9,x28,#0xb | `FALL_THROUGH`
<a id="insn-00acff00"></a> `00acff00` | `00 58 20 0e` | cnt v0.8B,v0.8B | `FALL_THROUGH`
<a id="insn-00acff04"></a> `00acff04` | `00 38 30 2e` | uaddlv h0,v0.8B | `FALL_THROUGH`
<a id="insn-00acff08"></a> `00acff08` | `0a 00 26 1e` | fmov w10,s0 | `FALL_THROUGH`
<a id="insn-00acff0c"></a> `00acff0c` | `5f 05 00 f1` | cmp x10,#0x1 | `FALL_THROUGH`
<a id="insn-00acff10"></a> `00acff10` | `68 07 00 54` | b.hi 0x00acfffc | `CONDITIONAL_JUMP`
<a id="insn-00acff14"></a> `00acff14` | `0b 00 b0 12` | mov w11,#0x7fffffff | `FALL_THROUGH`
<a id="insn-00acff18"></a> `00acff18` | `0b 01 0b 8b` | add x11,x8,x11 | `FALL_THROUGH`
<a id="insn-00acff1c"></a> `00acff1c` | `6b 01 09 8a` | and x11,x11,x9 | `FALL_THROUGH`
<a id="insn-00acff20"></a> `00acff20` | `3c 00 00 14` | b 0x00ad0010 | `UNCONDITIONAL_JUMP`
<a id="insn-00acff24"></a> `00acff24` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acff28"></a> `00acff28` | `08 c9 38 8b` | add x8,x8,w24, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00acff2c"></a> `00acff2c` | `01 01 40 b9` | ldr w1,[x8] | `FALL_THROUGH`
<a id="insn-00acff30"></a> `00acff30` | `a8 a3 00 d1` | sub x8,x29,#0x28 | `FALL_THROUGH`
<a id="insn-00acff34"></a> `00acff34` | `e0 03 18 2a` | mov w0,w24 | `FALL_THROUGH`
<a id="insn-00acff38"></a> `00acff38` | `2c 5b ee 97` | bl 0x00666be8 | `UNCONDITIONAL_CALL`
<a id="insn-00acff3c"></a> `00acff3c` | `a8 83 5d f8` | ldur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acff40"></a> `00acff40` | `89 2f 00 11` | add w9,w28,#0xb | `FALL_THROUGH`
<a id="insn-00acff44"></a> `00acff44` | `a9 83 1e b8` | stur w9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00acff48"></a> `00acff48` | `a8 03 00 b4` | cbz x8,0x00acffbc | `CONDITIONAL_JUMP`
<a id="insn-00acff4c"></a> `00acff4c` | `a8 63 00 d1` | sub x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acff50"></a> `00acff50` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acff54"></a> `00acff54` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acff58"></a> `00acff58` | `a3 43 00 d1` | sub x3,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00acff5c"></a> `00acff5c` | `a4 47 00 d1` | sub x4,x29,#0x11 | `FALL_THROUGH`
<a id="insn-00acff60"></a> `00acff60` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00acff64"></a> `00acff64` | `e2 03 1b aa` | mov x2,x27 | `FALL_THROUGH`
<a id="insn-00acff68"></a> `00acff68` | `01 17 ef 97` | bl 0x00695b6c | `UNCONDITIONAL_CALL`
<a id="insn-00acff6c"></a> `00acff6c` | `b5 d3 7d a9` | ldp x21,x20,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acff70"></a> `00acff70` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00acff74"></a> `00acff74` | `94 00 00 b4` | cbz x20,0x00acff84 | `CONDITIONAL_JUMP`
<a id="insn-00acff78"></a> `00acff78` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acff7c"></a> `00acff7c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acff80"></a> `00acff80` | `4c 0e 06 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-00acff84"></a> `00acff84` | `38 13 40 f9` | ldr x24,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00acff88"></a> `00acff88` | `35 d3 01 a9` | stp x21,x20,[x25, #0x18] | `FALL_THROUGH`
<a id="insn-00acff8c"></a> `00acff8c` | `f8 01 00 b4` | cbz x24,0x00acffc8 | `CONDITIONAL_JUMP`
<a id="insn-00acff90"></a> `00acff90` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00acff94"></a> `00acff94` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acff98"></a> `00acff98` | `52 0e 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acff9c"></a> `00acff9c` | `60 01 00 b5` | cbnz x0,0x00acffc8 | `CONDITIONAL_JUMP`
<a id="insn-00acffa0"></a> `00acffa0` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00acffa4"></a> `00acffa4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00acffa8"></a> `00acffa8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acffac"></a> `00acffac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acffb0"></a> `00acffb0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00acffb4"></a> `00acffb4` | `b3 1e 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00acffb8"></a> `00acffb8` | `04 00 00 14` | b 0x00acffc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acffbc"></a> `00acffbc` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acffc0"></a> `00acffc0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00acffc4"></a> `00acffc4` | `75 4a fb 97` | bl 0x009a2998 | `UNCONDITIONAL_CALL`
<a id="insn-00acffc8"></a> `00acffc8` | `b8 03 5e f8` | ldur x24,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acffcc"></a> `00acffcc` | `98 f3 ff b4` | cbz x24,0x00acfe3c | `CONDITIONAL_JUMP`
<a id="insn-00acffd0"></a> `00acffd0` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00acffd4"></a> `00acffd4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acffd8"></a> `00acffd8` | `42 0e 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acffdc"></a> `00acffdc` | `00 f3 ff b5` | cbnz x0,0x00acfe3c | `CONDITIONAL_JUMP`
<a id="insn-00acffe0"></a> `00acffe0` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00acffe4"></a> `00acffe4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00acffe8"></a> `00acffe8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acffec"></a> `00acffec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acfff0"></a> `00acfff0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00acfff4"></a> `00acfff4` | `a3 1e 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00acfff8"></a> `00acfff8` | `91 ff ff 17` | b 0x00acfe3c | `UNCONDITIONAL_JUMP`
<a id="insn-00acfffc"></a> `00acfffc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad0000"></a> `00ad0000` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00ad0004"></a> `00ad0004` | `68 00 00 54` | b.hi 0x00ad0010 | `CONDITIONAL_JUMP`
<a id="insn-00ad0008"></a> `00ad0008` | `2b 09 c8 9a` | udiv x11,x9,x8 | `FALL_THROUGH`
<a id="insn-00ad000c"></a> `00ad000c` | `6b a5 08 9b` | msub x11,x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00ad0010"></a> `00ad0010` | `cc 02 40 f9` | ldr x12,[x22] | `FALL_THROUGH`
<a id="insn-00ad0014"></a> `00ad0014` | `8c 79 6b f8` | ldr x12,[x12, x11, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ad0018"></a> `00ad0018` | `4c f1 ff b4` | cbz x12,0x00acfe40 | `CONDITIONAL_JUMP`
<a id="insn-00ad001c"></a> `00ad001c` | `8c 01 40 f9` | ldr x12,[x12] | `FALL_THROUGH`
<a id="insn-00ad0020"></a> `00ad0020` | `0c f1 ff b4` | cbz x12,0x00acfe40 | `CONDITIONAL_JUMP`
<a id="insn-00ad0024"></a> `00ad0024` | `0d 05 00 d1` | sub x13,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad0028"></a> `00ad0028` | `06 00 00 14` | b 0x00ad0040 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad002c"></a> `00ad002c` | `8e 11 40 b9` | ldr w14,[x12, #0x10] | `FALL_THROUGH`
<a id="insn-00ad0030"></a> `00ad0030` | `3f 01 0e eb` | cmp x9,x14 | `FALL_THROUGH`
<a id="insn-00ad0034"></a> `00ad0034` | `20 02 00 54` | b.eq 0x00ad0078 | `CONDITIONAL_JUMP`
<a id="insn-00ad0038"></a> `00ad0038` | `8c 01 40 f9` | ldr x12,[x12] | `FALL_THROUGH`
<a id="insn-00ad003c"></a> `00ad003c` | `2c f0 ff b4` | cbz x12,0x00acfe40 | `CONDITIONAL_JUMP`
<a id="insn-00ad0040"></a> `00ad0040` | `8e 05 40 f9` | ldr x14,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00ad0044"></a> `00ad0044` | `df 01 09 eb` | cmp x14,x9 | `FALL_THROUGH`
<a id="insn-00ad0048"></a> `00ad0048` | `20 ff ff 54` | b.eq 0x00ad002c | `CONDITIONAL_JUMP`
<a id="insn-00ad004c"></a> `00ad004c` | `5f 05 00 f1` | cmp x10,#0x1 | `FALL_THROUGH`
<a id="insn-00ad0050"></a> `00ad0050` | `68 00 00 54` | b.hi 0x00ad005c | `CONDITIONAL_JUMP`
<a id="insn-00ad0054"></a> `00ad0054` | `ce 01 0d 8a` | and x14,x14,x13 | `FALL_THROUGH`
<a id="insn-00ad0058"></a> `00ad0058` | `05 00 00 14` | b 0x00ad006c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad005c"></a> `00ad005c` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00ad0060"></a> `00ad0060` | `63 00 00 54` | b.cc 0x00ad006c | `CONDITIONAL_JUMP`
<a id="insn-00ad0064"></a> `00ad0064` | `cf 09 c8 9a` | udiv x15,x14,x8 | `FALL_THROUGH`
<a id="insn-00ad0068"></a> `00ad0068` | `ee b9 08 9b` | msub x14,x15,x8,x14 | `FALL_THROUGH`
<a id="insn-00ad006c"></a> `00ad006c` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00ad0070"></a> `00ad0070` | `40 fe ff 54` | b.eq 0x00ad0038 | `CONDITIONAL_JUMP`
<a id="insn-00ad0074"></a> `00ad0074` | `73 ff ff 17` | b 0x00acfe40 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad0078"></a> `00ad0078` | `bf ff 3d a9` | stp xzr,xzr,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00ad007c"></a> `00ad007c` | `a9 03 1f b8` | stur w9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ad0080"></a> `00ad0080` | `a1 43 00 d1` | sub x1,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00ad0084"></a> `00ad0084` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ad0088"></a> `00ad0088` | `44 4a fb 97` | bl 0x009a2998 | `UNCONDITIONAL_CALL`
<a id="insn-00ad008c"></a> `00ad008c` | `b8 03 5e f8` | ldur x24,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ad0090"></a> `00ad0090` | `98 ed ff b4` | cbz x24,0x00acfe40 | `CONDITIONAL_JUMP`
<a id="insn-00ad0094"></a> `00ad0094` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00ad0098"></a> `00ad0098` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ad009c"></a> `00ad009c` | `11 0e 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad00a0"></a> `00ad00a0` | `00 ed ff b5` | cbnz x0,0x00acfe40 | `CONDITIONAL_JUMP`
<a id="insn-00ad00a4"></a> `00ad00a4` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00ad00a8"></a> `00ad00a8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00ad00ac"></a> `00ad00ac` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad00b0"></a> `00ad00b0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad00b4"></a> `00ad00b4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00ad00b8"></a> `00ad00b8` | `72 1e 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00ad00bc"></a> `00ad00bc` | `61 ff ff 17` | b 0x00acfe40 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad00c0"></a> `00ad00c0` | `a8 0e 00 90` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad00c4"></a> `00ad00c4` | `08 e1 2c 91` | add x8,x8,#0xb38 | `FALL_THROUGH`
<a id="insn-00ad00c8"></a> `00ad00c8` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ad00cc"></a> `00ad00cc` | `48 02 00 36` | tbz w8,#0x0,0x00ad0114 | `CONDITIONAL_JUMP`
<a id="insn-00ad00d0"></a> `00ad00d0` | `a8 0e 00 90` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad00d4"></a> `00ad00d4` | `00 99 45 f9` | ldr x0,[x8, #0xb30] | `FALL_THROUGH`
<a id="insn-00ad00d8"></a> `00ad00d8` | `40 00 00 b4` | cbz x0,0x00ad00e0 | `CONDITIONAL_JUMP`
<a id="insn-00ad00dc"></a> `00ad00dc` | `2d 20 e7 97` | bl 0x00498190 | `UNCONDITIONAL_CALL`
<a id="insn-00ad00e0"></a> `00ad00e0` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad00e4"></a> `00ad00e4` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ad00e8"></a> `00ad00e8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad00ec"></a> `00ad00ec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad00f0"></a> `00ad00f0` | `81 05 00 54` | b.ne 0x00ad01a0 | `CONDITIONAL_JUMP`
<a id="insn-00ad00f4"></a> `00ad00f4` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00ad00f8"></a> `00ad00f8` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ad00fc"></a> `00ad00fc` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ad0100"></a> `00ad0100` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ad0104"></a> `00ad0104` | `fc 6f 47 a9` | ldp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad0108"></a> `00ad0108` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad010c"></a> `00ad010c` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00ad0110"></a> `00ad0110` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad0114"></a> `00ad0114` | `a0 0e 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad0118"></a> `00ad0118` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00ad011c"></a> `00ad011c` | `4d 1e 06 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00ad0120"></a> `00ad0120` | `80 fd ff 34` | cbz w0,0x00ad00d0 | `CONDITIONAL_JUMP`
<a id="insn-00ad0124"></a> `00ad0124` | `a1 0e 00 90` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad0128"></a> `00ad0128` | `21 00 2c 91` | add x1,x1,#0xb00 | `FALL_THROUGH`
<a id="insn-00ad012c"></a> `00ad012c` | `60 cd ff d0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00ad0130"></a> `00ad0130` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00ad0134"></a> `00ad0134` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ad0138"></a> `00ad0138` | `82 0c 00 d0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00ad013c"></a> `00ad013c` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00ad0140"></a> `00ad0140` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00ad0144"></a> `00ad0144` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00ad0148"></a> `00ad0148` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ad014c"></a> `00ad014c` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00ad0150"></a> `00ad0150` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00ad0154"></a> `00ad0154` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00ad0158"></a> `00ad0158` | `36 1e 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00ad015c"></a> `00ad015c` | `a0 0e 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad0160"></a> `00ad0160` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00ad0164"></a> `00ad0164` | `43 1e 06 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00ad0168"></a> `00ad0168` | `da ff ff 17` | b 0x00ad00d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad01a0"></a> `00ad01a0` | `50 1e 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfac4`](#insn-00acfac4) 範囲 `[['00acfac4', '00acfb0b']]`
  - `CONDITIONAL_JUMP` [`00acfb08`](#insn-00acfb08) → [`00acfb18`](#insn-00acfb18)
  - `FALL_THROUGH` [`00acfb08`](#insn-00acfb08) → [`00acfb0c`](#insn-00acfb0c)
- ブロック [`00acfb0c`](#insn-00acfb0c) 範囲 `[['00acfb0c', '00acfb17']]`
  - `CONDITIONAL_JUMP` [`00acfb14`](#insn-00acfb14) → [`00ad00c0`](#insn-00ad00c0)
  - `FALL_THROUGH` [`00acfb14`](#insn-00acfb14) → [`00acfb18`](#insn-00acfb18)
- ブロック [`00acfb18`](#insn-00acfb18) 範囲 `[['00acfb18', '00acfb27']]`
  - `CONDITIONAL_JUMP` [`00acfb24`](#insn-00acfb24) → [`00acfb48`](#insn-00acfb48)
  - `FALL_THROUGH` [`00acfb24`](#insn-00acfb24) → [`00acfb28`](#insn-00acfb28)
- ブロック [`00acfb28`](#insn-00acfb28) 範囲 `[['00acfb28', '00acfb47']]`
  - `UNCONDITIONAL_JUMP` [`00acfb44`](#insn-00acfb44) → [`00acfb4c`](#insn-00acfb4c)
- ブロック [`00acfb48`](#insn-00acfb48) 範囲 `[['00acfb48', '00acfb4b']]`
  - `FALL_THROUGH` [`00acfb48`](#insn-00acfb48) → [`00acfb4c`](#insn-00acfb4c)
- ブロック [`00acfb4c`](#insn-00acfb4c) 範囲 `[['00acfb4c', '00acfb57']]`
  - `CONDITIONAL_JUMP` [`00acfb54`](#insn-00acfb54) → [`00ad00c0`](#insn-00ad00c0)
  - `FALL_THROUGH` [`00acfb54`](#insn-00acfb54) → [`00acfb58`](#insn-00acfb58)
- ブロック [`00acfb58`](#insn-00acfb58) 範囲 `[['00acfb58', '00acfb9f']]`
  - `UNCONDITIONAL_JUMP` [`00acfb9c`](#insn-00acfb9c) → [`00acfbb0`](#insn-00acfbb0)
- ブロック [`00acfba0`](#insn-00acfba0) 範囲 `[['00acfba0', '00acfba3']]`
  - `FALL_THROUGH` [`00acfba0`](#insn-00acfba0) → [`00acfba4`](#insn-00acfba4)
- ブロック [`00acfba4`](#insn-00acfba4) 範囲 `[['00acfba4', '00acfbaf']]`
  - `CONDITIONAL_JUMP` [`00acfbac`](#insn-00acfbac) → [`00acfe18`](#insn-00acfe18)
  - `FALL_THROUGH` [`00acfbac`](#insn-00acfbac) → [`00acfbb0`](#insn-00acfbb0)
- ブロック [`00acfbb0`](#insn-00acfbb0) 範囲 `[['00acfbb0', '00acfbf7']]`
  - `CONDITIONAL_JUMP` [`00acfbf4`](#insn-00acfbf4) → [`00acfba4`](#insn-00acfba4)
  - `FALL_THROUGH` [`00acfbf4`](#insn-00acfbf4) → [`00acfbf8`](#insn-00acfbf8)
- ブロック [`00acfbf8`](#insn-00acfbf8) 範囲 `[['00acfbf8', '00acfbff']]`
  - `CONDITIONAL_JUMP` [`00acfbfc`](#insn-00acfbfc) → [`00acfc9c`](#insn-00acfc9c)
  - `FALL_THROUGH` [`00acfbfc`](#insn-00acfbfc) → [`00acfc00`](#insn-00acfc00)
- ブロック [`00acfc00`](#insn-00acfc00) 範囲 `[['00acfc00', '00acfc0b']]`
  - `CONDITIONAL_JUMP` [`00acfc08`](#insn-00acfc08) → [`00acfc9c`](#insn-00acfc9c)
  - `FALL_THROUGH` [`00acfc08`](#insn-00acfc08) → [`00acfc0c`](#insn-00acfc0c)
- ブロック [`00acfc0c`](#insn-00acfc0c) 範囲 `[['00acfc0c', '00acfc1b']]`
  - `CONDITIONAL_JUMP` [`00acfc18`](#insn-00acfc18) → [`00acfdc0`](#insn-00acfdc0)
  - `FALL_THROUGH` [`00acfc18`](#insn-00acfc18) → [`00acfc1c`](#insn-00acfc1c)
- ブロック [`00acfc1c`](#insn-00acfc1c) 範囲 `[['00acfc1c', '00acfc73']]`
  - `CONDITIONAL_JUMP` [`00acfc70`](#insn-00acfc70) → [`00acfcb4`](#insn-00acfcb4)
  - `FALL_THROUGH` [`00acfc70`](#insn-00acfc70) → [`00acfc74`](#insn-00acfc74)
- ブロック [`00acfc74`](#insn-00acfc74) 範囲 `[['00acfc74', '00acfc87']]`
  - `CONDITIONAL_JUMP` [`00acfc84`](#insn-00acfc84) → [`00acfcb4`](#insn-00acfcb4)
  - `FALL_THROUGH` [`00acfc84`](#insn-00acfc84) → [`00acfc88`](#insn-00acfc88)
- ブロック [`00acfc88`](#insn-00acfc88) 範囲 `[['00acfc88', '00acfc93']]`
  - `CONDITIONAL_JUMP` [`00acfc90`](#insn-00acfc90) → [`00acfcb4`](#insn-00acfcb4)
  - `FALL_THROUGH` [`00acfc90`](#insn-00acfc90) → [`00acfc94`](#insn-00acfc94)
- ブロック [`00acfc94`](#insn-00acfc94) 範囲 `[['00acfc94', '00acfc9b']]`
  - `UNCONDITIONAL_JUMP` [`00acfc98`](#insn-00acfc98) → [`00acfcbc`](#insn-00acfcbc)
- ブロック [`00acfc9c`](#insn-00acfc9c) 範囲 `[['00acfc9c', '00acfcb3']]`
  - `UNCONDITIONAL_JUMP` [`00acfcb0`](#insn-00acfcb0) → [`00acfd8c`](#insn-00acfd8c)
- ブロック [`00acfcb4`](#insn-00acfcb4) 範囲 `[['00acfcb4', '00acfcbb']]`
  - `FALL_THROUGH` [`00acfcb8`](#insn-00acfcb8) → [`00acfcbc`](#insn-00acfcbc)
- ブロック [`00acfcbc`](#insn-00acfcbc) 範囲 `[['00acfcbc', '00acfd07']]`
  - `CONDITIONAL_JUMP` [`00acfd04`](#insn-00acfd04) → [`00acfd80`](#insn-00acfd80)
  - `FALL_THROUGH` [`00acfd04`](#insn-00acfd04) → [`00acfd08`](#insn-00acfd08)
- ブロック [`00acfd08`](#insn-00acfd08) 範囲 `[['00acfd08', '00acfd37']]`
  - `CONDITIONAL_JUMP` [`00acfd34`](#insn-00acfd34) → [`00acfd44`](#insn-00acfd44)
  - `FALL_THROUGH` [`00acfd34`](#insn-00acfd34) → [`00acfd38`](#insn-00acfd38)
- ブロック [`00acfd38`](#insn-00acfd38) 範囲 `[['00acfd38', '00acfd43']]`
  - `FALL_THROUGH` [`00acfd40`](#insn-00acfd40) → [`00acfd44`](#insn-00acfd44)
- ブロック [`00acfd44`](#insn-00acfd44) 範囲 `[['00acfd44', '00acfd53']]`
  - `CONDITIONAL_JUMP` [`00acfd50`](#insn-00acfd50) → [`00acfd8c`](#insn-00acfd8c)
  - `FALL_THROUGH` [`00acfd50`](#insn-00acfd50) → [`00acfd54`](#insn-00acfd54)
- ブロック [`00acfd54`](#insn-00acfd54) 範囲 `[['00acfd54', '00acfd63']]`
  - `CONDITIONAL_JUMP` [`00acfd60`](#insn-00acfd60) → [`00acfd8c`](#insn-00acfd8c)
  - `FALL_THROUGH` [`00acfd60`](#insn-00acfd60) → [`00acfd64`](#insn-00acfd64)
- ブロック [`00acfd64`](#insn-00acfd64) 範囲 `[['00acfd64', '00acfd7f']]`
  - `UNCONDITIONAL_JUMP` [`00acfd7c`](#insn-00acfd7c) → [`00acfd8c`](#insn-00acfd8c)
- ブロック [`00acfd80`](#insn-00acfd80) 範囲 `[['00acfd80', '00acfd8b']]`
  - `FALL_THROUGH` [`00acfd88`](#insn-00acfd88) → [`00acfd8c`](#insn-00acfd8c)
- ブロック [`00acfd8c`](#insn-00acfd8c) 範囲 `[['00acfd8c', '00acfd93']]`
  - `CONDITIONAL_JUMP` [`00acfd90`](#insn-00acfd90) → [`00acfba0`](#insn-00acfba0)
  - `FALL_THROUGH` [`00acfd90`](#insn-00acfd90) → [`00acfd94`](#insn-00acfd94)
- ブロック [`00acfd94`](#insn-00acfd94) 範囲 `[['00acfd94', '00acfda3']]`
  - `CONDITIONAL_JUMP` [`00acfda0`](#insn-00acfda0) → [`00acfba0`](#insn-00acfba0)
  - `FALL_THROUGH` [`00acfda0`](#insn-00acfda0) → [`00acfda4`](#insn-00acfda4)
- ブロック [`00acfda4`](#insn-00acfda4) 範囲 `[['00acfda4', '00acfdbf']]`
  - `UNCONDITIONAL_JUMP` [`00acfdbc`](#insn-00acfdbc) → [`00acfba0`](#insn-00acfba0)
- ブロック [`00acfdc0`](#insn-00acfdc0) 範囲 `[['00acfdc0', '00acfdcf']]`
  - `CONDITIONAL_JUMP` [`00acfdcc`](#insn-00acfdcc) → [`00acfc1c`](#insn-00acfc1c)
  - `FALL_THROUGH` [`00acfdcc`](#insn-00acfdcc) → [`00acfdd0`](#insn-00acfdd0)
- ブロック [`00acfdd0`](#insn-00acfdd0) 範囲 `[['00acfdd0', '00acfe17']]`
  - `UNCONDITIONAL_JUMP` [`00acfe14`](#insn-00acfe14) → [`00acfc1c`](#insn-00acfc1c)
- ブロック [`00acfe18`](#insn-00acfe18) 範囲 `[['00acfe18', '00acfe27']]`
  - `CONDITIONAL_JUMP` [`00acfe24`](#insn-00acfe24) → [`00ad00c0`](#insn-00ad00c0)
  - `FALL_THROUGH` [`00acfe24`](#insn-00acfe24) → [`00acfe28`](#insn-00acfe28)
- ブロック [`00acfe28`](#insn-00acfe28) 範囲 `[['00acfe28', '00acfe3b']]`
  - `UNCONDITIONAL_JUMP` [`00acfe38`](#insn-00acfe38) → [`00acfe58`](#insn-00acfe58)
- ブロック [`00acfe3c`](#insn-00acfe3c) 範囲 `[['00acfe3c', '00acfe3f']]`
  - `FALL_THROUGH` [`00acfe3c`](#insn-00acfe3c) → [`00acfe40`](#insn-00acfe40)
- ブロック [`00acfe40`](#insn-00acfe40) 範囲 `[['00acfe40', '00acfe57']]`
  - `CONDITIONAL_JUMP` [`00acfe54`](#insn-00acfe54) → [`00ad00c0`](#insn-00ad00c0)
  - `FALL_THROUGH` [`00acfe54`](#insn-00acfe54) → [`00acfe58`](#insn-00acfe58)
- ブロック [`00acfe58`](#insn-00acfe58) 範囲 `[['00acfe58', '00acfe5f']]`
  - `CONDITIONAL_JUMP` [`00acfe5c`](#insn-00acfe5c) → [`00acfef0`](#insn-00acfef0)
  - `FALL_THROUGH` [`00acfe5c`](#insn-00acfe5c) → [`00acfe60`](#insn-00acfe60)
- ブロック [`00acfe60`](#insn-00acfe60) 範囲 `[['00acfe60', '00acfe6b']]`
  - `CONDITIONAL_JUMP` [`00acfe68`](#insn-00acfe68) → [`00acfef0`](#insn-00acfef0)
  - `FALL_THROUGH` [`00acfe68`](#insn-00acfe68) → [`00acfe6c`](#insn-00acfe6c)
- ブロック [`00acfe6c`](#insn-00acfe6c) 範囲 `[['00acfe6c', '00acfec3']]`
  - `FALL_THROUGH` [`00acfec0`](#insn-00acfec0) → [`00acfec4`](#insn-00acfec4)
- ブロック [`00acfec4`](#insn-00acfec4) 範囲 `[['00acfec4', '00acfec7']]`
  - `CONDITIONAL_JUMP` [`00acfec4`](#insn-00acfec4) → [`00acff24`](#insn-00acff24)
  - `FALL_THROUGH` [`00acfec4`](#insn-00acfec4) → [`00acfec8`](#insn-00acfec8)
- ブロック [`00acfec8`](#insn-00acfec8) 範囲 `[['00acfec8', '00acfed7']]`
  - `FALL_THROUGH` [`00acfed4`](#insn-00acfed4) → [`00acfed8`](#insn-00acfed8)
- ブロック [`00acfed8`](#insn-00acfed8) 範囲 `[['00acfed8', '00acfedb']]`
  - `CONDITIONAL_JUMP` [`00acfed8`](#insn-00acfed8) → [`00acff24`](#insn-00acff24)
  - `FALL_THROUGH` [`00acfed8`](#insn-00acfed8) → [`00acfedc`](#insn-00acfedc)
- ブロック [`00acfedc`](#insn-00acfedc) 範囲 `[['00acfedc', '00acfee7']]`
  - `CONDITIONAL_JUMP` [`00acfee4`](#insn-00acfee4) → [`00acff24`](#insn-00acff24)
  - `FALL_THROUGH` [`00acfee4`](#insn-00acfee4) → [`00acfee8`](#insn-00acfee8)
- ブロック [`00acfee8`](#insn-00acfee8) 範囲 `[['00acfee8', '00acfeef']]`
  - `UNCONDITIONAL_JUMP` [`00acfeec`](#insn-00acfeec) → [`00acff2c`](#insn-00acff2c)
- ブロック [`00acfef0`](#insn-00acfef0) 範囲 `[['00acfef0', '00acfef7']]`
  - `CONDITIONAL_JUMP` [`00acfef4`](#insn-00acfef4) → [`00acfe40`](#insn-00acfe40)
  - `FALL_THROUGH` [`00acfef4`](#insn-00acfef4) → [`00acfef8`](#insn-00acfef8)
- ブロック [`00acfef8`](#insn-00acfef8) 範囲 `[['00acfef8', '00acff13']]`
  - `CONDITIONAL_JUMP` [`00acff10`](#insn-00acff10) → [`00acfffc`](#insn-00acfffc)
  - `FALL_THROUGH` [`00acff10`](#insn-00acff10) → [`00acff14`](#insn-00acff14)
- ブロック [`00acff14`](#insn-00acff14) 範囲 `[['00acff14', '00acff17']]`
  - `FALL_THROUGH` [`00acff14`](#insn-00acff14) → [`00acff18`](#insn-00acff18)
- ブロック [`00acff18`](#insn-00acff18) 範囲 `[['00acff18', '00acff23']]`
  - `UNCONDITIONAL_JUMP` [`00acff20`](#insn-00acff20) → [`00ad0010`](#insn-00ad0010)
- ブロック [`00acff24`](#insn-00acff24) 範囲 `[['00acff24', '00acff2b']]`
  - `FALL_THROUGH` [`00acff28`](#insn-00acff28) → [`00acff2c`](#insn-00acff2c)
- ブロック [`00acff2c`](#insn-00acff2c) 範囲 `[['00acff2c', '00acff37']]`
  - `FALL_THROUGH` [`00acff34`](#insn-00acff34) → [`00acff38`](#insn-00acff38)
- ブロック [`00acff38`](#insn-00acff38) 範囲 `[['00acff38', '00acff4b']]`
  - `CONDITIONAL_JUMP` [`00acff48`](#insn-00acff48) → [`00acffbc`](#insn-00acffbc)
  - `FALL_THROUGH` [`00acff48`](#insn-00acff48) → [`00acff4c`](#insn-00acff4c)
- ブロック [`00acff4c`](#insn-00acff4c) 範囲 `[['00acff4c', '00acff5f']]`
  - `FALL_THROUGH` [`00acff5c`](#insn-00acff5c) → [`00acff60`](#insn-00acff60)
- ブロック [`00acff60`](#insn-00acff60) 範囲 `[['00acff60', '00acff77']]`
  - `CONDITIONAL_JUMP` [`00acff74`](#insn-00acff74) → [`00acff84`](#insn-00acff84)
  - `FALL_THROUGH` [`00acff74`](#insn-00acff74) → [`00acff78`](#insn-00acff78)
- ブロック [`00acff78`](#insn-00acff78) 範囲 `[['00acff78', '00acff83']]`
  - `FALL_THROUGH` [`00acff80`](#insn-00acff80) → [`00acff84`](#insn-00acff84)
- ブロック [`00acff84`](#insn-00acff84) 範囲 `[['00acff84', '00acff8b']]`
  - `FALL_THROUGH` [`00acff88`](#insn-00acff88) → [`00acff8c`](#insn-00acff8c)
- ブロック [`00acff8c`](#insn-00acff8c) 範囲 `[['00acff8c', '00acff8f']]`
  - `CONDITIONAL_JUMP` [`00acff8c`](#insn-00acff8c) → [`00acffc8`](#insn-00acffc8)
  - `FALL_THROUGH` [`00acff8c`](#insn-00acff8c) → [`00acff90`](#insn-00acff90)
- ブロック [`00acff90`](#insn-00acff90) 範囲 `[['00acff90', '00acff9f']]`
  - `CONDITIONAL_JUMP` [`00acff9c`](#insn-00acff9c) → [`00acffc8`](#insn-00acffc8)
  - `FALL_THROUGH` [`00acff9c`](#insn-00acff9c) → [`00acffa0`](#insn-00acffa0)
- ブロック [`00acffa0`](#insn-00acffa0) 範囲 `[['00acffa0', '00acffbb']]`
  - `UNCONDITIONAL_JUMP` [`00acffb8`](#insn-00acffb8) → [`00acffc8`](#insn-00acffc8)
- ブロック [`00acffbc`](#insn-00acffbc) 範囲 `[['00acffbc', '00acffc7']]`
  - `FALL_THROUGH` [`00acffc4`](#insn-00acffc4) → [`00acffc8`](#insn-00acffc8)
- ブロック [`00acffc8`](#insn-00acffc8) 範囲 `[['00acffc8', '00acffcf']]`
  - `CONDITIONAL_JUMP` [`00acffcc`](#insn-00acffcc) → [`00acfe3c`](#insn-00acfe3c)
  - `FALL_THROUGH` [`00acffcc`](#insn-00acffcc) → [`00acffd0`](#insn-00acffd0)
- ブロック [`00acffd0`](#insn-00acffd0) 範囲 `[['00acffd0', '00acffdf']]`
  - `CONDITIONAL_JUMP` [`00acffdc`](#insn-00acffdc) → [`00acfe3c`](#insn-00acfe3c)
  - `FALL_THROUGH` [`00acffdc`](#insn-00acffdc) → [`00acffe0`](#insn-00acffe0)
- ブロック [`00acffe0`](#insn-00acffe0) 範囲 `[['00acffe0', '00acfff7']]`
  - `FALL_THROUGH` [`00acfff4`](#insn-00acfff4) → [`00acfff8`](#insn-00acfff8)
- ブロック [`00acfff8`](#insn-00acfff8) 範囲 `[['00acfff8', '00acfffb']]`
  - `UNCONDITIONAL_JUMP` [`00acfff8`](#insn-00acfff8) → [`00acfe3c`](#insn-00acfe3c)
- ブロック [`00acfffc`](#insn-00acfffc) 範囲 `[['00acfffc', '00ad0007']]`
  - `CONDITIONAL_JUMP` [`00ad0004`](#insn-00ad0004) → [`00ad0010`](#insn-00ad0010)
  - `FALL_THROUGH` [`00ad0004`](#insn-00ad0004) → [`00ad0008`](#insn-00ad0008)
- ブロック [`00ad0008`](#insn-00ad0008) 範囲 `[['00ad0008', '00ad000f']]`
  - `FALL_THROUGH` [`00ad000c`](#insn-00ad000c) → [`00ad0010`](#insn-00ad0010)
- ブロック [`00ad0010`](#insn-00ad0010) 範囲 `[['00ad0010', '00ad001b']]`
  - `CONDITIONAL_JUMP` [`00ad0018`](#insn-00ad0018) → [`00acfe40`](#insn-00acfe40)
  - `FALL_THROUGH` [`00ad0018`](#insn-00ad0018) → [`00ad001c`](#insn-00ad001c)
- ブロック [`00ad001c`](#insn-00ad001c) 範囲 `[['00ad001c', '00ad001f']]`
  - `FALL_THROUGH` [`00ad001c`](#insn-00ad001c) → [`00ad0020`](#insn-00ad0020)
- ブロック [`00ad0020`](#insn-00ad0020) 範囲 `[['00ad0020', '00ad0023']]`
  - `CONDITIONAL_JUMP` [`00ad0020`](#insn-00ad0020) → [`00acfe40`](#insn-00acfe40)
  - `FALL_THROUGH` [`00ad0020`](#insn-00ad0020) → [`00ad0024`](#insn-00ad0024)
- ブロック [`00ad0024`](#insn-00ad0024) 範囲 `[['00ad0024', '00ad002b']]`
  - `UNCONDITIONAL_JUMP` [`00ad0028`](#insn-00ad0028) → [`00ad0040`](#insn-00ad0040)
- ブロック [`00ad002c`](#insn-00ad002c) 範囲 `[['00ad002c', '00ad0037']]`
  - `CONDITIONAL_JUMP` [`00ad0034`](#insn-00ad0034) → [`00ad0078`](#insn-00ad0078)
  - `FALL_THROUGH` [`00ad0034`](#insn-00ad0034) → [`00ad0038`](#insn-00ad0038)
- ブロック [`00ad0038`](#insn-00ad0038) 範囲 `[['00ad0038', '00ad003f']]`
  - `CONDITIONAL_JUMP` [`00ad003c`](#insn-00ad003c) → [`00acfe40`](#insn-00acfe40)
  - `FALL_THROUGH` [`00ad003c`](#insn-00ad003c) → [`00ad0040`](#insn-00ad0040)
- ブロック [`00ad0040`](#insn-00ad0040) 範囲 `[['00ad0040', '00ad004b']]`
  - `CONDITIONAL_JUMP` [`00ad0048`](#insn-00ad0048) → [`00ad002c`](#insn-00ad002c)
  - `FALL_THROUGH` [`00ad0048`](#insn-00ad0048) → [`00ad004c`](#insn-00ad004c)
- ブロック [`00ad004c`](#insn-00ad004c) 範囲 `[['00ad004c', '00ad0053']]`
  - `CONDITIONAL_JUMP` [`00ad0050`](#insn-00ad0050) → [`00ad005c`](#insn-00ad005c)
  - `FALL_THROUGH` [`00ad0050`](#insn-00ad0050) → [`00ad0054`](#insn-00ad0054)
- ブロック [`00ad0054`](#insn-00ad0054) 範囲 `[['00ad0054', '00ad005b']]`
  - `UNCONDITIONAL_JUMP` [`00ad0058`](#insn-00ad0058) → [`00ad006c`](#insn-00ad006c)
- ブロック [`00ad005c`](#insn-00ad005c) 範囲 `[['00ad005c', '00ad0063']]`
  - `CONDITIONAL_JUMP` [`00ad0060`](#insn-00ad0060) → [`00ad006c`](#insn-00ad006c)
  - `FALL_THROUGH` [`00ad0060`](#insn-00ad0060) → [`00ad0064`](#insn-00ad0064)
- ブロック [`00ad0064`](#insn-00ad0064) 範囲 `[['00ad0064', '00ad006b']]`
  - `FALL_THROUGH` [`00ad0068`](#insn-00ad0068) → [`00ad006c`](#insn-00ad006c)
- ブロック [`00ad006c`](#insn-00ad006c) 範囲 `[['00ad006c', '00ad0073']]`
  - `CONDITIONAL_JUMP` [`00ad0070`](#insn-00ad0070) → [`00ad0038`](#insn-00ad0038)
  - `FALL_THROUGH` [`00ad0070`](#insn-00ad0070) → [`00ad0074`](#insn-00ad0074)
- ブロック [`00ad0074`](#insn-00ad0074) 範囲 `[['00ad0074', '00ad0077']]`
  - `UNCONDITIONAL_JUMP` [`00ad0074`](#insn-00ad0074) → [`00acfe40`](#insn-00acfe40)
- ブロック [`00ad0078`](#insn-00ad0078) 範囲 `[['00ad0078', '00ad0093']]`
  - `CONDITIONAL_JUMP` [`00ad0090`](#insn-00ad0090) → [`00acfe40`](#insn-00acfe40)
  - `FALL_THROUGH` [`00ad0090`](#insn-00ad0090) → [`00ad0094`](#insn-00ad0094)
- ブロック [`00ad0094`](#insn-00ad0094) 範囲 `[['00ad0094', '00ad00a3']]`
  - `CONDITIONAL_JUMP` [`00ad00a0`](#insn-00ad00a0) → [`00acfe40`](#insn-00acfe40)
  - `FALL_THROUGH` [`00ad00a0`](#insn-00ad00a0) → [`00ad00a4`](#insn-00ad00a4)
- ブロック [`00ad00a4`](#insn-00ad00a4) 範囲 `[['00ad00a4', '00ad00bf']]`
  - `UNCONDITIONAL_JUMP` [`00ad00bc`](#insn-00ad00bc) → [`00acfe40`](#insn-00acfe40)
- ブロック [`00ad00c0`](#insn-00ad00c0) 範囲 `[['00ad00c0', '00ad00cf']]`
  - `CONDITIONAL_JUMP` [`00ad00cc`](#insn-00ad00cc) → [`00ad0114`](#insn-00ad0114)
  - `FALL_THROUGH` [`00ad00cc`](#insn-00ad00cc) → [`00ad00d0`](#insn-00ad00d0)
- ブロック [`00ad00d0`](#insn-00ad00d0) 範囲 `[['00ad00d0', '00ad00db']]`
  - `CONDITIONAL_JUMP` [`00ad00d8`](#insn-00ad00d8) → [`00ad00e0`](#insn-00ad00e0)
  - `FALL_THROUGH` [`00ad00d8`](#insn-00ad00d8) → [`00ad00dc`](#insn-00ad00dc)
- ブロック [`00ad00dc`](#insn-00ad00dc) 範囲 `[['00ad00dc', '00ad00df']]`
  - `FALL_THROUGH` [`00ad00dc`](#insn-00ad00dc) → [`00ad00e0`](#insn-00ad00e0)
- ブロック [`00ad00e0`](#insn-00ad00e0) 範囲 `[['00ad00e0', '00ad00f3']]`
  - `CONDITIONAL_JUMP` [`00ad00f0`](#insn-00ad00f0) → [`00ad01a0`](#insn-00ad01a0)
  - `FALL_THROUGH` [`00ad00f0`](#insn-00ad00f0) → [`00ad00f4`](#insn-00ad00f4)
- ブロック [`00ad00f4`](#insn-00ad00f4) 範囲 `[['00ad00f4', '00ad0113']]`
- ブロック [`00ad0114`](#insn-00ad0114) 範囲 `[['00ad0114', '00ad0123']]`
  - `CONDITIONAL_JUMP` [`00ad0120`](#insn-00ad0120) → [`00ad00d0`](#insn-00ad00d0)
  - `FALL_THROUGH` [`00ad0120`](#insn-00ad0120) → [`00ad0124`](#insn-00ad0124)
- ブロック [`00ad0124`](#insn-00ad0124) 範囲 `[['00ad0124', '00ad012f']]`
  - `FALL_THROUGH` [`00ad012c`](#insn-00ad012c) → [`00ad0130`](#insn-00ad0130)
- ブロック [`00ad0130`](#insn-00ad0130) 範囲 `[['00ad0130', '00ad0133']]`
  - `FALL_THROUGH` [`00ad0130`](#insn-00ad0130) → [`00ad0134`](#insn-00ad0134)
- ブロック [`00ad0134`](#insn-00ad0134) 範囲 `[['00ad0134', '00ad014b']]`
  - `FALL_THROUGH` [`00ad0148`](#insn-00ad0148) → [`00ad014c`](#insn-00ad014c)
- ブロック [`00ad014c`](#insn-00ad014c) 範囲 `[['00ad014c', '00ad014f']]`
  - `FALL_THROUGH` [`00ad014c`](#insn-00ad014c) → [`00ad0150`](#insn-00ad0150)
- ブロック [`00ad0150`](#insn-00ad0150) 範囲 `[['00ad0150', '00ad0153']]`
  - `FALL_THROUGH` [`00ad0150`](#insn-00ad0150) → [`00ad0154`](#insn-00ad0154)
- ブロック [`00ad0154`](#insn-00ad0154) 範囲 `[['00ad0154', '00ad0157']]`
  - `FALL_THROUGH` [`00ad0154`](#insn-00ad0154) → [`00ad0158`](#insn-00ad0158)
- ブロック [`00ad0158`](#insn-00ad0158) 範囲 `[['00ad0158', '00ad015b']]`
  - `FALL_THROUGH` [`00ad0158`](#insn-00ad0158) → [`00ad015c`](#insn-00ad015c)
- ブロック [`00ad015c`](#insn-00ad015c) 範囲 `[['00ad015c', '00ad016b']]`
  - `UNCONDITIONAL_JUMP` [`00ad0168`](#insn-00ad0168) → [`00ad00d0`](#insn-00ad00d0)
- ブロック [`00ad01a0`](#insn-00ad01a0) 範囲 `[['00ad01a0', '00ad01a3']]`

## 命令位置別の参照

- [`00acfac8`](#insn-00acfac8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfacc`](#insn-00acfacc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfad0`](#insn-00acfad0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfad4`](#insn-00acfad4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfad8`](#insn-00acfad8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfadc`](#insn-00acfadc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfaf0`](#insn-00acfaf0) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfafc`](#insn-00acfafc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb04`](#insn-00acfb04) → `00333a28`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acfb08`](#insn-00acfb08) → [`00acfb18`](#insn-00acfb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb0c`](#insn-00acfb0c) → `00ca4220`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acfb14`](#insn-00acfb14) → [`00ad00c0`](#insn-00ad00c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb1c`](#insn-00acfb1c) → `00ca4220`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acfb20`](#insn-00acfb20) → `00ca4578`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfb24`](#insn-00acfb24) → [`00acfb48`](#insn-00acfb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb2c`](#insn-00acfb2c) → `00c65a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00acfb34`](#insn-00acfb34) → `00c8d550`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00acfb3c`](#insn-00acfb3c) → [`00c58210`](../00c58/00c58210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58210` · 推定シンボル `None` · 推定型 `None`
- [`00acfb44`](#insn-00acfb44) → [`00acfb4c`](#insn-00acfb4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb4c`](#insn-00acfb4c) → `00333f4c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acfb54`](#insn-00acfb54) → [`00ad00c0`](#insn-00ad00c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb7c`](#insn-00acfb7c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb8c`](#insn-00acfb8c) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb98`](#insn-00acfb98) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb9c`](#insn-00acfb9c) → [`00acfbb0`](#insn-00acfbb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbac`](#insn-00acfbac) → [`00acfe18`](#insn-00acfe18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbf4`](#insn-00acfbf4) → [`00acfba4`](#insn-00acfba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbfc`](#insn-00acfbfc) → [`00acfc9c`](#insn-00acfc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc00`](#insn-00acfc00) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc08`](#insn-00acfc08) → [`00acfc9c`](#insn-00acfc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc14`](#insn-00acfc14) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acfc18`](#insn-00acfc18) → [`00acfdc0`](#insn-00acfdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc6c`](#insn-00acfc6c) → [`009e0e24`](../009e0/009e0e24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e0e24` · 推定シンボル `None` · 推定型 `None`
- [`00acfc70`](#insn-00acfc70) → [`00acfcb4`](#insn-00acfcb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc80`](#insn-00acfc80) → [`009e2df8`](../009e2/009e2df8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e2df8` · 推定シンボル `None` · 推定型 `None`
- [`00acfc84`](#insn-00acfc84) → [`00acfcb4`](#insn-00acfcb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc8c`](#insn-00acfc8c) → [`009df498`](../009df/009df498.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009df498` · 推定シンボル `None` · 推定型 `None`
- [`00acfc90`](#insn-00acfc90) → [`00acfcb4`](#insn-00acfcb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc98`](#insn-00acfc98) → [`00acfcbc`](#insn-00acfcbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc9c`](#insn-00acfc9c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfca0`](#insn-00acfca0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcac`](#insn-00acfcac) → [`009a2998`](../009a2/009a2998.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a2998` · 推定シンボル `None` · 推定型 `None`
- [`00acfcb0`](#insn-00acfcb0) → [`00acfd8c`](#insn-00acfd8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcb4`](#insn-00acfcb4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcc0`](#insn-00acfcc0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcd8`](#insn-00acfcd8) → `00c9a8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acfcd8`](#insn-00acfcd8) → `00ca4bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acfce4`](#insn-00acfce4) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfcf8`](#insn-00acfcf8) → [`006337a4`](../00633/006337a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006337a4` · 推定シンボル `None` · 推定型 `None`
- [`00acfcfc`](#insn-00acfcfc) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd00`](#insn-00acfd00) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd04`](#insn-00acfd04) → [`00acfd80`](#insn-00acfd80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd0c`](#insn-00acfd0c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd24`](#insn-00acfd24) → `002c86b5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd28`](#insn-00acfd28) → [`00695b6c`](../00695/00695b6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00695b6c` · 推定シンボル `None` · 推定型 `None`
- [`00acfd2c`](#insn-00acfd2c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd34`](#insn-00acfd34) → [`00acfd44`](#insn-00acfd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd40`](#insn-00acfd40) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`00acfd4c`](#insn-00acfd4c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd50`](#insn-00acfd50) → [`00acfd8c`](#insn-00acfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd5c`](#insn-00acfd5c) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00acfd60`](#insn-00acfd60) → [`00acfd8c`](#insn-00acfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd78`](#insn-00acfd78) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00acfd7c`](#insn-00acfd7c) → [`00acfd8c`](#insn-00acfd8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd88`](#insn-00acfd88) → [`009a2998`](../009a2/009a2998.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a2998` · 推定シンボル `None` · 推定型 `None`
- [`00acfd8c`](#insn-00acfd8c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd90`](#insn-00acfd90) → [`00acfba0`](#insn-00acfba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd9c`](#insn-00acfd9c) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00acfda0`](#insn-00acfda0) → [`00acfba0`](#insn-00acfba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdb8`](#insn-00acfdb8) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00acfdbc`](#insn-00acfdbc) → [`00acfba0`](#insn-00acfba0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdc4`](#insn-00acfdc4) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acfdc8`](#insn-00acfdc8) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00acfdcc`](#insn-00acfdcc) → [`00acfc1c`](#insn-00acfc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdd4`](#insn-00acfdd4) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfddc`](#insn-00acfddc) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00acfde8`](#insn-00acfde8) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acfdec`](#insn-00acfdec) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfdf0`](#insn-00acfdf0) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfdf0`](#insn-00acfdf0) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfdf8`](#insn-00acfdf8) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfdf8`](#insn-00acfdf8) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfdfc`](#insn-00acfdfc) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfe00`](#insn-00acfe00) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfe00`](#insn-00acfe00) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfe00`](#insn-00acfe00) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfe04`](#insn-00acfe04) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00acfe0c`](#insn-00acfe0c) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acfe10`](#insn-00acfe10) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00acfe14`](#insn-00acfe14) → [`00acfc1c`](#insn-00acfc1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe20`](#insn-00acfe20) → `00335f78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acfe24`](#insn-00acfe24) → [`00ad00c0`](#insn-00ad00c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe38`](#insn-00acfe38) → [`00acfe58`](#insn-00acfe58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe3c`](#insn-00acfe3c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe48`](#insn-00acfe48) → `00335f78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acfe54`](#insn-00acfe54) → [`00ad00c0`](#insn-00ad00c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe5c`](#insn-00acfe5c) → [`00acfef0`](#insn-00acfef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe60`](#insn-00acfe60) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe68`](#insn-00acfe68) → [`00acfef0`](#insn-00acfef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe6c`](#insn-00acfe6c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfec0`](#insn-00acfec0) → [`009e0e24`](../009e0/009e0e24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e0e24` · 推定シンボル `None` · 推定型 `None`
- [`00acfec4`](#insn-00acfec4) → [`00acff24`](#insn-00acff24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfed4`](#insn-00acfed4) → [`009e2df8`](../009e2/009e2df8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e2df8` · 推定シンボル `None` · 推定型 `None`
- [`00acfed8`](#insn-00acfed8) → [`00acff24`](#insn-00acff24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfee0`](#insn-00acfee0) → [`009df498`](../009df/009df498.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009df498` · 推定シンボル `None` · 推定型 `None`
- [`00acfee4`](#insn-00acfee4) → [`00acff24`](#insn-00acff24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfeec`](#insn-00acfeec) → [`00acff2c`](#insn-00acff2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfef4`](#insn-00acfef4) → [`00acfe40`](#insn-00acfe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff10`](#insn-00acff10) → [`00acfffc`](#insn-00acfffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff20`](#insn-00acff20) → [`00ad0010`](#insn-00ad0010) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff24`](#insn-00acff24) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff38`](#insn-00acff38) → [`00666be8`](../00666/00666be8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00666be8` · 推定シンボル `None` · 推定型 `None`
- [`00acff3c`](#insn-00acff3c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff44`](#insn-00acff44) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff48`](#insn-00acff48) → [`00acffbc`](#insn-00acffbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff50`](#insn-00acff50) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff64`](#insn-00acff64) → `002c86b5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff68`](#insn-00acff68) → [`00695b6c`](../00695/00695b6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00695b6c` · 推定シンボル `None` · 推定型 `None`
- [`00acff6c`](#insn-00acff6c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff74`](#insn-00acff74) → [`00acff84`](#insn-00acff84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff80`](#insn-00acff80) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`00acff8c`](#insn-00acff8c) → [`00acffc8`](#insn-00acffc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff98`](#insn-00acff98) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00acff9c`](#insn-00acff9c) → [`00acffc8`](#insn-00acffc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffb4`](#insn-00acffb4) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00acffb8`](#insn-00acffb8) → [`00acffc8`](#insn-00acffc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffc4`](#insn-00acffc4) → [`009a2998`](../009a2/009a2998.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a2998` · 推定シンボル `None` · 推定型 `None`
- [`00acffc8`](#insn-00acffc8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffcc`](#insn-00acffcc) → [`00acfe3c`](#insn-00acfe3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffd8`](#insn-00acffd8) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00acffdc`](#insn-00acffdc) → [`00acfe3c`](#insn-00acfe3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfff4`](#insn-00acfff4) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00acfff8`](#insn-00acfff8) → [`00acfe3c`](#insn-00acfe3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0004`](#insn-00ad0004) → [`00ad0010`](#insn-00ad0010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0018`](#insn-00ad0018) → [`00acfe40`](#insn-00acfe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0020`](#insn-00ad0020) → [`00acfe40`](#insn-00acfe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0028`](#insn-00ad0028) → [`00ad0040`](#insn-00ad0040) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0034`](#insn-00ad0034) → [`00ad0078`](#insn-00ad0078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad003c`](#insn-00ad003c) → [`00acfe40`](#insn-00acfe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0048`](#insn-00ad0048) → [`00ad002c`](#insn-00ad002c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0050`](#insn-00ad0050) → [`00ad005c`](#insn-00ad005c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0058`](#insn-00ad0058) → [`00ad006c`](#insn-00ad006c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0060`](#insn-00ad0060) → [`00ad006c`](#insn-00ad006c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0070`](#insn-00ad0070) → [`00ad0038`](#insn-00ad0038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0074`](#insn-00ad0074) → [`00acfe40`](#insn-00acfe40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0078`](#insn-00ad0078) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad007c`](#insn-00ad007c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0088`](#insn-00ad0088) → [`009a2998`](../009a2/009a2998.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a2998` · 推定シンボル `None` · 推定型 `None`
- [`00ad008c`](#insn-00ad008c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0090`](#insn-00ad0090) → [`00acfe40`](#insn-00acfe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad009c`](#insn-00ad009c) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00ad00a0`](#insn-00ad00a0) → [`00acfe40`](#insn-00acfe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00b8`](#insn-00ad00b8) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00ad00bc`](#insn-00ad00bc) → [`00acfe40`](#insn-00acfe40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00c8`](#insn-00ad00c8) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ad00cc`](#insn-00ad00cc) → [`00ad0114`](#insn-00ad0114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00d4`](#insn-00ad00d4) → `00ca4b30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad00d8`](#insn-00ad00d8) → [`00ad00e0`](#insn-00ad00e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00dc`](#insn-00ad00dc) → [`00498190`](../00498/00498190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00498190` · 推定シンボル `None` · 推定型 `None`
- [`00ad00e0`](#insn-00ad00e0) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00e8`](#insn-00ad00e8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00f0`](#insn-00ad00f0) → [`00ad01a0`](#insn-00ad01a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00f4`](#insn-00ad00f4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00f8`](#insn-00ad00f8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00fc`](#insn-00ad00fc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0100`](#insn-00ad0100) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0104`](#insn-00ad0104) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0108`](#insn-00ad0108) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0118`](#insn-00ad0118) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ad011c`](#insn-00ad011c) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00ad0120`](#insn-00ad0120) → [`00ad00d0`](#insn-00ad00d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0128`](#insn-00ad0128) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0130`](#insn-00ad0130) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00ad013c`](#insn-00ad013c) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ad0140`](#insn-00ad0140) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0144`](#insn-00ad0144) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0144`](#insn-00ad0144) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad014c`](#insn-00ad014c) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad014c`](#insn-00ad014c) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0150`](#insn-00ad0150) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0154`](#insn-00ad0154) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0154`](#insn-00ad0154) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0154`](#insn-00ad0154) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0158`](#insn-00ad0158) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00ad0160`](#insn-00ad0160) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ad0164`](#insn-00ad0164) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00ad0168`](#insn-00ad0168) → [`00ad00d0`](#insn-00ad00d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad01a0`](#insn-00ad01a0) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfac8`](#insn-00acfac8)

~~~json
{
  "source": "00acfac8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfacc`](#insn-00acfacc)

~~~json
{
  "source": "00acfacc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfad0`](#insn-00acfad0)

~~~json
{
  "source": "00acfad0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfad4`](#insn-00acfad4)

~~~json
{
  "source": "00acfad4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfad8`](#insn-00acfad8)

~~~json
{
  "source": "00acfad8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfadc`](#insn-00acfadc)

~~~json
{
  "source": "00acfadc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfaf0`](#insn-00acfaf0)

~~~json
{
  "source": "00acfaf0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfafc`](#insn-00acfafc)

~~~json
{
  "source": "00acfafc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb04`](#insn-00acfb04)

~~~json
{
  "source": "00acfb04",
  "target": "00333a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a28",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "b0c26a00707a0900",
  "capture_start": "00333a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acfb08`](#insn-00acfb08)

~~~json
{
  "source": "00acfb08",
  "target": "00acfb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb0c`](#insn-00acfb0c)

~~~json
{
  "source": "00acfb0c",
  "target": "00ca4220",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4220",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfb14`](#insn-00acfb14)

~~~json
{
  "source": "00acfb14",
  "target": "00ad00c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb1c`](#insn-00acfb1c)

~~~json
{
  "source": "00acfb1c",
  "target": "00ca4220",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4220",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfb20`](#insn-00acfb20)

~~~json
{
  "source": "00acfb20",
  "target": "00ca4578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfb24`](#insn-00acfb24)

~~~json
{
  "source": "00acfb24",
  "target": "00acfb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb2c`](#insn-00acfb2c)

~~~json
{
  "source": "00acfb2c",
  "target": "00c65a58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65a58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acfb34`](#insn-00acfb34)

~~~json
{
  "source": "00acfb34",
  "target": "00c8d550",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d550",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acfb3c`](#insn-00acfb3c)

~~~json
{
  "source": "00acfb3c",
  "target": "00c58210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb44`](#insn-00acfb44)

~~~json
{
  "source": "00acfb44",
  "target": "00acfb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb4c`](#insn-00acfb4c)

~~~json
{
  "source": "00acfb4c",
  "target": "00333f4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f48",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "4cb66c00dc8d0900",
  "capture_start": "00333f48",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acfb54`](#insn-00acfb54)

~~~json
{
  "source": "00acfb54",
  "target": "00ad00c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb7c`](#insn-00acfb7c)

~~~json
{
  "source": "00acfb7c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb8c`](#insn-00acfb8c)

~~~json
{
  "source": "00acfb8c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb98`](#insn-00acfb98)

~~~json
{
  "source": "00acfb98",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb9c`](#insn-00acfb9c)

~~~json
{
  "source": "00acfb9c",
  "target": "00acfbb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbac`](#insn-00acfbac)

~~~json
{
  "source": "00acfbac",
  "target": "00acfe18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbf4`](#insn-00acfbf4)

~~~json
{
  "source": "00acfbf4",
  "target": "00acfba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbfc`](#insn-00acfbfc)

~~~json
{
  "source": "00acfbfc",
  "target": "00acfc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc00`](#insn-00acfc00)

~~~json
{
  "source": "00acfc00",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc08`](#insn-00acfc08)

~~~json
{
  "source": "00acfc08",
  "target": "00acfc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc14`](#insn-00acfc14)

~~~json
{
  "source": "00acfc14",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfc18`](#insn-00acfc18)

~~~json
{
  "source": "00acfc18",
  "target": "00acfdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc6c`](#insn-00acfc6c)

~~~json
{
  "source": "00acfc6c",
  "target": "009e0e24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc70`](#insn-00acfc70)

~~~json
{
  "source": "00acfc70",
  "target": "00acfcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc80`](#insn-00acfc80)

~~~json
{
  "source": "00acfc80",
  "target": "009e2df8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc84`](#insn-00acfc84)

~~~json
{
  "source": "00acfc84",
  "target": "00acfcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc8c`](#insn-00acfc8c)

~~~json
{
  "source": "00acfc8c",
  "target": "009df498",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc90`](#insn-00acfc90)

~~~json
{
  "source": "00acfc90",
  "target": "00acfcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc98`](#insn-00acfc98)

~~~json
{
  "source": "00acfc98",
  "target": "00acfcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc9c`](#insn-00acfc9c)

~~~json
{
  "source": "00acfc9c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfca0`](#insn-00acfca0)

~~~json
{
  "source": "00acfca0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcac`](#insn-00acfcac)

~~~json
{
  "source": "00acfcac",
  "target": "009a2998",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfcb0`](#insn-00acfcb0)

~~~json
{
  "source": "00acfcb0",
  "target": "00acfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcb4`](#insn-00acfcb4)

~~~json
{
  "source": "00acfcb4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcc0`](#insn-00acfcc0)

~~~json
{
  "source": "00acfcc0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcd8`](#insn-00acfcd8)

~~~json
{
  "source": "00acfcd8",
  "target": "00c9a8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acfcd8`](#insn-00acfcd8)

~~~json
{
  "source": "00acfcd8",
  "target": "00ca4bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4bd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfce4`](#insn-00acfce4)

~~~json
{
  "source": "00acfce4",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfcf8`](#insn-00acfcf8)

~~~json
{
  "source": "00acfcf8",
  "target": "006337a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfcfc`](#insn-00acfcfc)

~~~json
{
  "source": "00acfcfc",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd00`](#insn-00acfd00)

~~~json
{
  "source": "00acfd00",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd04`](#insn-00acfd04)

~~~json
{
  "source": "00acfd04",
  "target": "00acfd80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd0c`](#insn-00acfd0c)

~~~json
{
  "source": "00acfd0c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd24`](#insn-00acfd24)

~~~json
{
  "source": "00acfd24",
  "target": "002c86b5",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd28`](#insn-00acfd28)

~~~json
{
  "source": "00acfd28",
  "target": "00695b6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd2c`](#insn-00acfd2c)

~~~json
{
  "source": "00acfd2c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd34`](#insn-00acfd34)

~~~json
{
  "source": "00acfd34",
  "target": "00acfd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd40`](#insn-00acfd40)

~~~json
{
  "source": "00acfd40",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd4c`](#insn-00acfd4c)

~~~json
{
  "source": "00acfd4c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd50`](#insn-00acfd50)

~~~json
{
  "source": "00acfd50",
  "target": "00acfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd5c`](#insn-00acfd5c)

~~~json
{
  "source": "00acfd5c",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd60`](#insn-00acfd60)

~~~json
{
  "source": "00acfd60",
  "target": "00acfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd78`](#insn-00acfd78)

~~~json
{
  "source": "00acfd78",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd7c`](#insn-00acfd7c)

~~~json
{
  "source": "00acfd7c",
  "target": "00acfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd88`](#insn-00acfd88)

~~~json
{
  "source": "00acfd88",
  "target": "009a2998",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd8c`](#insn-00acfd8c)

~~~json
{
  "source": "00acfd8c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd90`](#insn-00acfd90)

~~~json
{
  "source": "00acfd90",
  "target": "00acfba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd9c`](#insn-00acfd9c)

~~~json
{
  "source": "00acfd9c",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfda0`](#insn-00acfda0)

~~~json
{
  "source": "00acfda0",
  "target": "00acfba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdb8`](#insn-00acfdb8)

~~~json
{
  "source": "00acfdb8",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfdbc`](#insn-00acfdbc)

~~~json
{
  "source": "00acfdbc",
  "target": "00acfba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdc4`](#insn-00acfdc4)

~~~json
{
  "source": "00acfdc4",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfdc8`](#insn-00acfdc8)

~~~json
{
  "source": "00acfdc8",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfdcc`](#insn-00acfdcc)

~~~json
{
  "source": "00acfdcc",
  "target": "00acfc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdd4`](#insn-00acfdd4)

~~~json
{
  "source": "00acfdd4",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfddc`](#insn-00acfddc)

~~~json
{
  "source": "00acfddc",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfde8`](#insn-00acfde8)

~~~json
{
  "source": "00acfde8",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acfdec`](#insn-00acfdec)

~~~json
{
  "source": "00acfdec",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfdf0`](#insn-00acfdf0)

~~~json
{
  "source": "00acfdf0",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfdf0`](#insn-00acfdf0)

~~~json
{
  "source": "00acfdf0",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfdf8`](#insn-00acfdf8)

~~~json
{
  "source": "00acfdf8",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfdf8`](#insn-00acfdf8)

~~~json
{
  "source": "00acfdf8",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfdfc`](#insn-00acfdfc)

~~~json
{
  "source": "00acfdfc",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfe00`](#insn-00acfe00)

~~~json
{
  "source": "00acfe00",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfe00`](#insn-00acfe00)

~~~json
{
  "source": "00acfe00",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfe00`](#insn-00acfe00)

~~~json
{
  "source": "00acfe00",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfe04`](#insn-00acfe04)

~~~json
{
  "source": "00acfe04",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfe0c`](#insn-00acfe0c)

~~~json
{
  "source": "00acfe0c",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfe10`](#insn-00acfe10)

~~~json
{
  "source": "00acfe10",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfe14`](#insn-00acfe14)

~~~json
{
  "source": "00acfe14",
  "target": "00acfc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe20`](#insn-00acfe20)

~~~json
{
  "source": "00acfe20",
  "target": "00335f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f78",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "447f750090631100",
  "capture_start": "00335f78",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acfe24`](#insn-00acfe24)

~~~json
{
  "source": "00acfe24",
  "target": "00ad00c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe38`](#insn-00acfe38)

~~~json
{
  "source": "00acfe38",
  "target": "00acfe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe3c`](#insn-00acfe3c)

~~~json
{
  "source": "00acfe3c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe48`](#insn-00acfe48)

~~~json
{
  "source": "00acfe48",
  "target": "00335f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f78",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "447f750090631100",
  "capture_start": "00335f78",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acfe54`](#insn-00acfe54)

~~~json
{
  "source": "00acfe54",
  "target": "00ad00c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe5c`](#insn-00acfe5c)

~~~json
{
  "source": "00acfe5c",
  "target": "00acfef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe60`](#insn-00acfe60)

~~~json
{
  "source": "00acfe60",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe68`](#insn-00acfe68)

~~~json
{
  "source": "00acfe68",
  "target": "00acfef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe6c`](#insn-00acfe6c)

~~~json
{
  "source": "00acfe6c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfec0`](#insn-00acfec0)

~~~json
{
  "source": "00acfec0",
  "target": "009e0e24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfec4`](#insn-00acfec4)

~~~json
{
  "source": "00acfec4",
  "target": "00acff24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfed4`](#insn-00acfed4)

~~~json
{
  "source": "00acfed4",
  "target": "009e2df8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfed8`](#insn-00acfed8)

~~~json
{
  "source": "00acfed8",
  "target": "00acff24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfee0`](#insn-00acfee0)

~~~json
{
  "source": "00acfee0",
  "target": "009df498",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfee4`](#insn-00acfee4)

~~~json
{
  "source": "00acfee4",
  "target": "00acff24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfeec`](#insn-00acfeec)

~~~json
{
  "source": "00acfeec",
  "target": "00acff2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfef4`](#insn-00acfef4)

~~~json
{
  "source": "00acfef4",
  "target": "00acfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff10`](#insn-00acff10)

~~~json
{
  "source": "00acff10",
  "target": "00acfffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff20`](#insn-00acff20)

~~~json
{
  "source": "00acff20",
  "target": "00ad0010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff24`](#insn-00acff24)

~~~json
{
  "source": "00acff24",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff38`](#insn-00acff38)

~~~json
{
  "source": "00acff38",
  "target": "00666be8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff3c`](#insn-00acff3c)

~~~json
{
  "source": "00acff3c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff44`](#insn-00acff44)

~~~json
{
  "source": "00acff44",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff48`](#insn-00acff48)

~~~json
{
  "source": "00acff48",
  "target": "00acffbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff50`](#insn-00acff50)

~~~json
{
  "source": "00acff50",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff64`](#insn-00acff64)

~~~json
{
  "source": "00acff64",
  "target": "002c86b5",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff68`](#insn-00acff68)

~~~json
{
  "source": "00acff68",
  "target": "00695b6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff6c`](#insn-00acff6c)

~~~json
{
  "source": "00acff6c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff74`](#insn-00acff74)

~~~json
{
  "source": "00acff74",
  "target": "00acff84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff80`](#insn-00acff80)

~~~json
{
  "source": "00acff80",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff8c`](#insn-00acff8c)

~~~json
{
  "source": "00acff8c",
  "target": "00acffc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff98`](#insn-00acff98)

~~~json
{
  "source": "00acff98",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff9c`](#insn-00acff9c)

~~~json
{
  "source": "00acff9c",
  "target": "00acffc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffb4`](#insn-00acffb4)

~~~json
{
  "source": "00acffb4",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acffb8`](#insn-00acffb8)

~~~json
{
  "source": "00acffb8",
  "target": "00acffc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffc4`](#insn-00acffc4)

~~~json
{
  "source": "00acffc4",
  "target": "009a2998",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acffc8`](#insn-00acffc8)

~~~json
{
  "source": "00acffc8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffcc`](#insn-00acffcc)

~~~json
{
  "source": "00acffcc",
  "target": "00acfe3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffd8`](#insn-00acffd8)

~~~json
{
  "source": "00acffd8",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acffdc`](#insn-00acffdc)

~~~json
{
  "source": "00acffdc",
  "target": "00acfe3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfff4`](#insn-00acfff4)

~~~json
{
  "source": "00acfff4",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfff8`](#insn-00acfff8)

~~~json
{
  "source": "00acfff8",
  "target": "00acfe3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0004`](#insn-00ad0004)

~~~json
{
  "source": "00ad0004",
  "target": "00ad0010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0018`](#insn-00ad0018)

~~~json
{
  "source": "00ad0018",
  "target": "00acfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0020`](#insn-00ad0020)

~~~json
{
  "source": "00ad0020",
  "target": "00acfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0028`](#insn-00ad0028)

~~~json
{
  "source": "00ad0028",
  "target": "00ad0040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0034`](#insn-00ad0034)

~~~json
{
  "source": "00ad0034",
  "target": "00ad0078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad003c`](#insn-00ad003c)

~~~json
{
  "source": "00ad003c",
  "target": "00acfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0048`](#insn-00ad0048)

~~~json
{
  "source": "00ad0048",
  "target": "00ad002c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0050`](#insn-00ad0050)

~~~json
{
  "source": "00ad0050",
  "target": "00ad005c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0058`](#insn-00ad0058)

~~~json
{
  "source": "00ad0058",
  "target": "00ad006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0060`](#insn-00ad0060)

~~~json
{
  "source": "00ad0060",
  "target": "00ad006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0070`](#insn-00ad0070)

~~~json
{
  "source": "00ad0070",
  "target": "00ad0038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0074`](#insn-00ad0074)

~~~json
{
  "source": "00ad0074",
  "target": "00acfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0078`](#insn-00ad0078)

~~~json
{
  "source": "00ad0078",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad007c`](#insn-00ad007c)

~~~json
{
  "source": "00ad007c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0088`](#insn-00ad0088)

~~~json
{
  "source": "00ad0088",
  "target": "009a2998",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad008c`](#insn-00ad008c)

~~~json
{
  "source": "00ad008c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0090`](#insn-00ad0090)

~~~json
{
  "source": "00ad0090",
  "target": "00acfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad009c`](#insn-00ad009c)

~~~json
{
  "source": "00ad009c",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad00a0`](#insn-00ad00a0)

~~~json
{
  "source": "00ad00a0",
  "target": "00acfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00b8`](#insn-00ad00b8)

~~~json
{
  "source": "00ad00b8",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad00bc`](#insn-00ad00bc)

~~~json
{
  "source": "00ad00bc",
  "target": "00acfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00c8`](#insn-00ad00c8)

~~~json
{
  "source": "00ad00c8",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad00cc`](#insn-00ad00cc)

~~~json
{
  "source": "00ad00cc",
  "target": "00ad0114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00d4`](#insn-00ad00d4)

~~~json
{
  "source": "00ad00d4",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad00d8`](#insn-00ad00d8)

~~~json
{
  "source": "00ad00d8",
  "target": "00ad00e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00dc`](#insn-00ad00dc)

~~~json
{
  "source": "00ad00dc",
  "target": "00498190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad00e0`](#insn-00ad00e0)

~~~json
{
  "source": "00ad00e0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00e8`](#insn-00ad00e8)

~~~json
{
  "source": "00ad00e8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00f0`](#insn-00ad00f0)

~~~json
{
  "source": "00ad00f0",
  "target": "00ad01a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00f4`](#insn-00ad00f4)

~~~json
{
  "source": "00ad00f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00f8`](#insn-00ad00f8)

~~~json
{
  "source": "00ad00f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00fc`](#insn-00ad00fc)

~~~json
{
  "source": "00ad00fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0100`](#insn-00ad0100)

~~~json
{
  "source": "00ad0100",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0104`](#insn-00ad0104)

~~~json
{
  "source": "00ad0104",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0108`](#insn-00ad0108)

~~~json
{
  "source": "00ad0108",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0118`](#insn-00ad0118)

~~~json
{
  "source": "00ad0118",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad011c`](#insn-00ad011c)

~~~json
{
  "source": "00ad011c",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0120`](#insn-00ad0120)

~~~json
{
  "source": "00ad0120",
  "target": "00ad00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0128`](#insn-00ad0128)

~~~json
{
  "source": "00ad0128",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0130`](#insn-00ad0130)

~~~json
{
  "source": "00ad0130",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad013c`](#insn-00ad013c)

~~~json
{
  "source": "00ad013c",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ad0140`](#insn-00ad0140)

~~~json
{
  "source": "00ad0140",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0144`](#insn-00ad0144)

~~~json
{
  "source": "00ad0144",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0144`](#insn-00ad0144)

~~~json
{
  "source": "00ad0144",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad014c`](#insn-00ad014c)

~~~json
{
  "source": "00ad014c",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad014c`](#insn-00ad014c)

~~~json
{
  "source": "00ad014c",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0150`](#insn-00ad0150)

~~~json
{
  "source": "00ad0150",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0154`](#insn-00ad0154)

~~~json
{
  "source": "00ad0154",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0154`](#insn-00ad0154)

~~~json
{
  "source": "00ad0154",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0154`](#insn-00ad0154)

~~~json
{
  "source": "00ad0154",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0158`](#insn-00ad0158)

~~~json
{
  "source": "00ad0158",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0160`](#insn-00ad0160)

~~~json
{
  "source": "00ad0160",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0164`](#insn-00ad0164)

~~~json
{
  "source": "00ad0164",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0168`](#insn-00ad0168)

~~~json
{
  "source": "00ad0168",
  "target": "00ad00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad01a0`](#insn-00ad01a0)

~~~json
{
  "source": "00ad01a0",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
