# 00acfcc0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acfac4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acfac4.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-313b479720196df2ccd9986ea2856999)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acfd30`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfd30.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-015991eba31d1b616fb4ce6413a8a848)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfcc0",
  "name": "FUN_00acfcc0",
  "size": 1708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "78f24d98e1ff8cef201f50cfbb3721e992eba79d62764adcf5f06869af059de4",
  "source_text_sha256": "78f24d98e1ff8cef201f50cfbb3721e992eba79d62764adcf5f06869af059de4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfcc0",
        "00ad0367"
      ],
      [
        "00ad039c",
        "00ad039f"
      ]
    ],
    "bytes_sha256": "f8c7b192acfd85f0a2b1ecf14fb44573684d8ec532d1d477d7b1f16c6b9594d4",
    "instruction_count": 427,
    "instruction_bytes": 1708,
    "body_bytes": 1708,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

- [00ad0958](../00ad0/00ad0958.md)
- [00ad6f4c](../00ad6/00ad6f4c.md)
- [00aec960](../00aec/00aec960.md)

## 呼び出し先

- [004981d0](../00498/004981d0.md)
- [006337e4](../00633/006337e4.md)
- [00666c28](../00666/00666c28.md)
- [00695bac](../00695/00695bac.md)
- [009a2b34](../009a2/009a2b34.md)
- [009df634](../009df/009df634.md)
- [009e0fc0](../009e0/009e0fc0.md)
- [009e2f94](../009e2/009e2f94.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58610](../00c58/00c58610.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 15101 bytes

~~~c

void FUN_00acfcc0(long param_1,ulong param_2)

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
  if (((param_2 & 1) != 0) || (DAT_00ca4620 != iVar8)) {
    DAT_00ca4620 = iVar8;
    if (DAT_00ca4978 == 0) {
      lVar9 = 0;
    }
    else {
      lVar9 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d950,0);
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
            FUN_009a2b34(lVar9 + 0x318,&local_70);
          }
          else {
            if (((DAT_00ca4f38 & 1) == 0) &&
               (iVar8 = __cxa_guard_acquire(&DAT_00ca4f38), iVar8 != 0)) {
              DAT_00ca4f08 = 0;
              DAT_00ca4f00 = &DAT_00ca4f08;
              DAT_00ca4f28 = 0;
              DAT_00ca4f30 = 0;
              DAT_00ca4f20 = 0;
                    /* try { // try from 00acfffc to 00bd005f has its CatchHandler @ 00acfffc
                       catch() { ... } // from try @ 00acfffc with catch @ 00acfffc
                       catch() { ... } // from try @ 00ad0074 with catch @ 00acfffc
                       catch() { ... } // from try @ 00ad013c with catch @ 00acfffc
                       catch() { ... } // from try @ 00ad01c8 with catch @ 00acfffc */
              DAT_00ca4f10 = 0;
              DAT_00ca4f18 = &DAT_00ca4f20;
              __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
              __cxa_guard_release(&DAT_00ca4f38);
            }
            uVar5 = (uint)(*(byte *)(param_1 + 0x8385a) ^ pbVar18[-1]) << 0x10 |
                    (uint)(*(byte *)(param_1 + 0x8385b) ^ *pbVar18) << 0x18 |
                    (uint)(*(byte *)(param_1 + 0x83859) ^ pbVar18[-2]) << 8 |
                    (uint)(*(byte *)(param_1 + 0x83858) ^ pbVar18[-3]);
            uVar10 = FUN_009e0fc0(param_1 + 0x50,0xffffffff,0xffffffff);
            if ((((uVar10 & 1) == 0) ||
                (lVar11 = FUN_009e2f94(param_1 + 0x50,0xffffffff,0xffffffff), lVar11 == 0)) ||
               (lVar11 = FUN_009df634(lVar11,uVar5), lVar11 == 0)) {
              piVar13 = (int *)(param_1 + 0x49934 + (long)(int)uVar5 * 4);
            }
            else {
              piVar13 = (int *)(lVar11 + 4);
            }
            FUN_006337e4(&local_88,&DAT_00ca4f00,
                         "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                         + (long)*piVar13 * 0x78 + (long)(int)uVar5 * 0x1e0 + param_1 + 0x20,
                         PTR_DAT_00c9aca0,0x1e,0,0,0);
            local_78 = iVar19;
            if (local_88 == 0) {
              FUN_009a2b34(lVar9 + 0x318,&local_78);
            }
            else {
              local_70 = &local_78;
              lVar12 = FUN_00695bac(lVar9 + 0x318,&local_78,&DAT_002c86f5,&local_70,&uStack_71);
              plVar3 = local_80;
              lVar11 = local_88;
              if (local_80 != (long *)0x0) {
                FUN_00c53cd0(1,local_80 + 1);
              }
              plVar23 = *(long **)(lVar12 + 0x20);
              *(long *)(lVar12 + 0x18) = lVar11;
              *(long **)(lVar12 + 0x20) = plVar3;
              if ((plVar23 != (long *)0x0) &&
                 (lVar11 = FUN_00c53d00(0xffffffffffffffff,plVar23 + 1), lVar11 == 0)) {
                (**(code **)(*plVar23 + 0x10))(plVar23);
                _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar23);
              }
            }
          }
          plVar3 = local_80;
          if ((local_80 != (long *)0x0) &&
             (lVar11 = FUN_00c53d00(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
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
                    /* try { // try from 00ad0060 to 00bd0073 has its CatchHandler @ 00ad02d0 */
          if ((lVar21 < lVar22) || (lVar2 < lVar21)) {
            uVar10 = *(ulong *)(lVar9 + 0x2f8);
            if (uVar10 != 0) {
              uVar4 = lVar21 + 0xb;
                    /* try { // try from 00ad00fc to 00bd0103 has its CatchHandler @ 00ad02e8 */
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
              if ((plVar23 != (long *)0x0) && (plVar23 = (long *)*plVar23, plVar23 != (long *)0x0))
              {
                do {
                  uVar17 = plVar23[1];
                  if (uVar17 == uVar4) {
                    if (uVar4 == *(uint *)(plVar23 + 2)) {
                      local_88 = 0;
                      local_80 = (long *)0x0;
                      local_70 = (int *)CONCAT44(local_70._4_4_,(int)uVar4);
                      FUN_009a2b34(plVar3,&local_70);
                      plVar23 = local_80;
                      if ((local_80 != (long *)0x0) &&
                         (lVar11 = FUN_00c53d00(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
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
                    /* try { // try from 00ad0074 to 00bd00b3 has its CatchHandler @ 00acfffc */
            pbVar18 = (byte *)(param_1 + 0x82a78 + lVar21 * 4);
                    /* try { // try from 00ad00b4 to 00bd00c7 has its CatchHandler @ 00ad02ec */
            uVar5 = (uint)(*(byte *)(param_1 + 0x8385a) ^ pbVar18[2]) << 0x10 |
                    (uint)(*(byte *)(param_1 + 0x8385b) ^ pbVar18[3]) << 0x18 |
                    (uint)(*(byte *)(param_1 + 0x83859) ^ pbVar18[1]) << 8 |
                    (uint)(*(byte *)(param_1 + 0x83858) ^ *pbVar18);
            uVar10 = FUN_009e0fc0(param_1 + 0x50,0xffffffff,0xffffffff);
                    /* try { // try from 00ad00d4 to 00bd00df has its CatchHandler @ 00ad02f4 */
            if ((((uVar10 & 1) == 0) ||
                (lVar11 = FUN_009e2f94(param_1 + 0x50,0xffffffff,0xffffffff), lVar11 == 0)) ||
               (lVar11 = FUN_009df634(lVar11,uVar5), lVar11 == 0)) {
              puVar14 = (undefined4 *)(param_1 + 0x49934 + (long)(int)uVar5 * 4);
            }
            else {
              puVar14 = (undefined4 *)(lVar11 + 4);
            }
                    /* try { // try from 00ad0128 to 00bd013b has its CatchHandler @ 00ad02cc */
            FUN_00666c28(&local_88,uVar5,*puVar14);
                    /* try { // try from 00ad013c to 00bd017b has its CatchHandler @ 00acfffc */
            local_78 = (int)lVar21 + 0xb;
            if (local_88 == 0) {
                    /* try { // try from 00ad01bc to 00bd01c7 has its CatchHandler @ 00ad02e8 */
              FUN_009a2b34(plVar3,&local_78);
            }
            else {
              local_70 = &local_78;
              lVar12 = FUN_00695bac(plVar3,&local_78,&DAT_002c86f5,&local_70,&uStack_71);
              plVar23 = local_80;
              lVar11 = local_88;
              if (local_80 != (long *)0x0) {
                    /* try { // try from 00ad017c to 00bd018f has its CatchHandler @ 00ad02f0 */
                FUN_00c53cd0(1,local_80 + 1);
              }
              plVar20 = *(long **)(lVar12 + 0x20);
              *(long *)(lVar12 + 0x18) = lVar11;
              *(long **)(lVar12 + 0x20) = plVar23;
                    /* try { // try from 00ad0194 to 00bd019f has its CatchHandler @ 00ad02f8 */
              if ((plVar20 != (long *)0x0) &&
                 (lVar11 = FUN_00c53d00(0xffffffffffffffff,plVar20 + 1), lVar11 == 0)) {
                (**(code **)(*plVar20 + 0x10))(plVar20);
                _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar20);
              }
            }
            plVar23 = local_80;
                    /* try { // try from 00ad01c8 to 00bd031f has its CatchHandler @ 00acfffc */
            if ((local_80 != (long *)0x0) &&
               (lVar11 = FUN_00c53d00(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
              (**(code **)(*plVar23 + 0x10))(plVar23);
              _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar23);
            }
          }
          bVar1 = lVar21 < *(int *)((long)&fde_table_entry_00335f78.initial_loc + param_1);
          lVar21 = lVar21 + 1;
        } while (bVar1);
      }
    }
  }
  if (((DAT_00ca4f38 & 1) == 0) && (iVar8 = __cxa_guard_acquire(&DAT_00ca4f38), iVar8 != 0)) {
                    /* try { // try from 00ad0320 to 00bd045f has its CatchHandler @ 00ad0320
                       catch() { ... } // from try @ 00ad0320 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad0468 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad0924 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad0df8 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2028 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2070 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad20c0 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad21a0 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2268 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad22d0 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2468 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad24c4 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2528 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad25bc with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2610 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2664 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad26b8 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad270c with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad28bc with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2968 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2ab4 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad3264 with catch @ 00ad0320 */
    DAT_00ca4f08 = 0;
    DAT_00ca4f00 = &DAT_00ca4f08;
    DAT_00ca4f28 = 0;
    DAT_00ca4f30 = 0;
    DAT_00ca4f20 = 0;
    DAT_00ca4f10 = 0;
    DAT_00ca4f18 = &DAT_00ca4f20;
    __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_00ca4f38);
  }
                    /* catch() { ... } // from try @ 00ad0128 with catch @ 00ad02cc */
                    /* catch() { ... } // from try @ 00ad0060 with catch @ 00ad02d0 */
  if (DAT_00ca4f30 != 0) {
    FUN_004981d0();
  }
                    /* catch() { ... } // from try @ 00ad00fc with catch @ 00ad02e8
                       catch() { ... } // from try @ 00ad01bc with catch @ 00ad02e8 */
                    /* catch() { ... } // from try @ 00ad00b4 with catch @ 00ad02ec */
  if (*(long *)(lVar7 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* catch() { ... } // from try @ 00ad017c with catch @ 00ad02f0 */
                    /* catch() { ... } // from try @ 00ad00d4 with catch @ 00ad02f4 */
                    /* catch() { ... } // from try @ 00ad0194 with catch @ 00ad02f8 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acfcc0"></a> `00acfcc0` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00acfcc4"></a> `00acfcc4` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acfcc8"></a> `00acfcc8` | `fc 6f 07 a9` | stp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acfccc"></a> `00acfccc` | `fa 67 08 a9` | stp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acfcd0"></a> `00acfcd0` | `f8 5f 09 a9` | stp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acfcd4"></a> `00acfcd4` | `f6 57 0a a9` | stp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acfcd8"></a> `00acfcd8` | `f4 4f 0b a9` | stp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acfcdc"></a> `00acfcdc` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acfce0"></a> `00acfce0` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acfce4"></a> `00acfce4` | `09 cc 4c 91` | add x9,x0,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00acfce8"></a> `00acfce8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acfcec"></a> `00acfcec` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acfcf0"></a> `00acfcf0` | `36 a1 28 91` | add x22,x9,#0xa28 | `FALL_THROUGH`
<a id="insn-00acfcf4"></a> `00acfcf4` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00acfcf8"></a> `00acfcf8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfcfc"></a> `00acfcfc` | `a8 0e 00 b0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfd00"></a> `00acfd00` | `d4 02 40 b9` | ldr w20,[x22] | `FALL_THROUGH`
<a id="insn-00acfd04"></a> `00acfd04` | `81 00 00 37` | tbnz w1,#0x0,0x00acfd14 | `CONDITIONAL_JUMP`
<a id="insn-00acfd08"></a> `00acfd08` | `09 21 46 b9` | ldr w9,[x8, #0x620] | `FALL_THROUGH`
<a id="insn-00acfd0c"></a> `00acfd0c` | `3f 01 14 6b` | cmp w9,w20 | `FALL_THROUGH`
<a id="insn-00acfd10"></a> `00acfd10` | `60 2d 00 54` | b.eq 0x00ad02bc | `CONDITIONAL_JUMP`
<a id="insn-00acfd14"></a> `00acfd14` | `a9 0e 00 b0` | adrp x9,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfd18"></a> `00acfd18` | `14 21 06 b9` | str w20,[x8, #0x620] | `FALL_THROUGH`
<a id="insn-00acfd1c"></a> `00acfd1c` | `20 bd 44 f9` | ldr x0,[x9, #0x978] | `FALL_THROUGH`
<a id="insn-00acfd20"></a> `00acfd20` | `20 01 00 b4` | cbz x0,0x00acfd44 | `CONDITIONAL_JUMP`
<a id="insn-00acfd24"></a> `00acfd24` | `a1 0c 00 d0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00acfd28"></a> `00acfd28` | `21 60 39 91` | add x1,x1,#0xe58 | `FALL_THROUGH`
<a id="insn-00acfd2c"></a> `00acfd2c` | `e2 0d 00 d0` | adrp x2,0xc8d000 | `FALL_THROUGH`
<a id="insn-00acfd30"></a> `00acfd30` | `42 40 25 91` | add x2,x2,#0x950 | `FALL_THROUGH`
<a id="insn-00acfd34"></a> `00acfd34` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00acfd38"></a> `00acfd38` | `36 22 06 94` | bl 0x00c58610 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd3c"></a> `00acfd3c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acfd40"></a> `00acfd40` | `02 00 00 14` | b 0x00acfd48 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfd44"></a> `00acfd44` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00acfd48"></a> `00acfd48` | `c8 26 45 b9` | ldr w8,[x22, #0x524] | `FALL_THROUGH`
<a id="insn-00acfd4c"></a> `00acfd4c` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00acfd50"></a> `00acfd50` | `61 2b 00 54` | b.ne 0x00ad02bc | `CONDITIONAL_JUMP`
<a id="insn-00acfd54"></a> `00acfd54` | `89 7e 40 93` | sxtw x9,w20 | `FALL_THROUGH`
<a id="insn-00acfd58"></a> `00acfd58` | `68 0a 42 91` | add x8,x19,#0x82, LSL #12 | `FALL_THROUGH`
<a id="insn-00acfd5c"></a> `00acfd5c` | `6a 0a 42 91` | add x10,x19,#0x82, LSL #12 | `FALL_THROUGH`
<a id="insn-00acfd60"></a> `00acfd60` | `17 ed 29 91` | add x23,x8,#0xa7b | `FALL_THROUGH`
<a id="insn-00acfd64"></a> `00acfd64` | `4b e1 29 91` | add x11,x10,#0xa78 | `FALL_THROUGH`
<a id="insn-00acfd68"></a> `00acfd68` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00acfd6c"></a> `00acfd6c` | `28 15 00 91` | add x8,x9,#0x5 | `FALL_THROUGH`
<a id="insn-00acfd70"></a> `00acfd70` | `3a 15 00 d1` | sub x26,x9,#0x5 | `FALL_THROUGH`
<a id="insn-00acfd74"></a> `00acfd74` | `19 6f 80 52` | mov w25,#0x378 | `FALL_THROUGH`
<a id="insn-00acfd78"></a> `00acfd78` | `f5 a3 02 a9` | stp x21,x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acfd7c"></a> `00acfd7c` | `68 12 4b 91` | add x8,x19,#0x2c4, LSL #12 | `FALL_THROUGH`
<a id="insn-00acfd80"></a> `00acfd80` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00acfd84"></a> `00acfd84` | `08 61 1a 91` | add x8,x8,#0x698 | `FALL_THROUGH`
<a id="insn-00acfd88"></a> `00acfd88` | `eb 23 01 a9` | stp x11,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfd8c"></a> `00acfd8c` | `68 26 41 91` | add x8,x19,#0x49, LSL #12 | `FALL_THROUGH`
<a id="insn-00acfd90"></a> `00acfd90` | `08 d1 24 91` | add x8,x8,#0x934 | `FALL_THROUGH`
<a id="insn-00acfd94"></a> `00acfd94` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfd98"></a> `00acfd98` | `05 00 00 14` | b 0x00acfdac | `UNCONDITIONAL_JUMP`
<a id="insn-00acfd9c"></a> `00acfd9c` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00acfda0"></a> `00acfda0` | `39 07 00 f1` | subs x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00acfda4"></a> `00acfda4` | `94 12 00 91` | add x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00acfda8"></a> `00acfda8` | `60 13 00 54` | b.eq 0x00ad0014 | `CONDITIONAL_JUMP`
<a id="insn-00acfdac"></a> `00acfdac` | `88 f2 5f 38` | ldurb w8,[x20, #-0x1] | `FALL_THROUGH`
<a id="insn-00acfdb0"></a> `00acfdb0` | `e9 7e 77 39` | ldrb w9,[x23, #0xddf] | `FALL_THROUGH`
<a id="insn-00acfdb4"></a> `00acfdb4` | `ea 82 77 39` | ldrb w10,[x23, #0xde0] | `FALL_THROUGH`
<a id="insn-00acfdb8"></a> `00acfdb8` | `8b e2 5f 38` | ldurb w11,[x20, #-0x2] | `FALL_THROUGH`
<a id="insn-00acfdbc"></a> `00acfdbc` | `ec 7a 77 39` | ldrb w12,[x23, #0xdde] | `FALL_THROUGH`
<a id="insn-00acfdc0"></a> `00acfdc0` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00acfdc4"></a> `00acfdc4` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00acfdc8"></a> `00acfdc8` | `08 3d 10 53` | lsl w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00acfdcc"></a> `00acfdcc` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00acfdd0"></a> `00acfdd0` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00acfdd4"></a> `00acfdd4` | `ea 76 77 39` | ldrb w10,[x23, #0xddd] | `FALL_THROUGH`
<a id="insn-00acfdd8"></a> `00acfdd8` | `08 61 09 2a` | orr w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00acfddc"></a> `00acfddc` | `89 d2 5f 38` | ldurb w9,[x20, #-0x3] | `FALL_THROUGH`
<a id="insn-00acfde0"></a> `00acfde0` | `08 21 0b 2a` | orr w8,w8,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00acfde4"></a> `00acfde4` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00acfde8"></a> `00acfde8` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00acfdec"></a> `00acfdec` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acfdf0"></a> `00acfdf0` | `80 fd ff 54` | b.eq 0x00acfda0 | `CONDITIONAL_JUMP`
<a id="insn-00acfdf4"></a> `00acfdf4` | `1f 03 1a 6b` | cmp w24,w26 | `FALL_THROUGH`
<a id="insn-00acfdf8"></a> `00acfdf8` | `0b 05 00 54` | b.lt 0x00acfe98 | `CONDITIONAL_JUMP`
<a id="insn-00acfdfc"></a> `00acfdfc` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acfe00"></a> `00acfe00` | `1f 03 08 6b` | cmp w24,w8 | `FALL_THROUGH`
<a id="insn-00acfe04"></a> `00acfe04` | `ac 04 00 54` | b.gt 0x00acfe98 | `CONDITIONAL_JUMP`
<a id="insn-00acfe08"></a> `00acfe08` | `a8 0e 00 b0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfe0c"></a> `00acfe0c` | `08 e1 3c 91` | add x8,x8,#0xf38 | `FALL_THROUGH`
<a id="insn-00acfe10"></a> `00acfe10` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00acfe14"></a> `00acfe14` | `48 0d 00 36` | tbz w8,#0x0,0x00acffbc | `CONDITIONAL_JUMP`
<a id="insn-00acfe18"></a> `00acfe18` | `88 f2 5f 38` | ldurb w8,[x20, #-0x1] | `FALL_THROUGH`
<a id="insn-00acfe1c"></a> `00acfe1c` | `e9 7e 77 39` | ldrb w9,[x23, #0xddf] | `FALL_THROUGH`
<a id="insn-00acfe20"></a> `00acfe20` | `60 42 01 91` | add x0,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00acfe24"></a> `00acfe24` | `ea 82 77 39` | ldrb w10,[x23, #0xde0] | `FALL_THROUGH`
<a id="insn-00acfe28"></a> `00acfe28` | `8b e2 5f 38` | ldurb w11,[x20, #-0x2] | `FALL_THROUGH`
<a id="insn-00acfe2c"></a> `00acfe2c` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfe30"></a> `00acfe30` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00acfe34"></a> `00acfe34` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00acfe38"></a> `00acfe38` | `ec 7a 77 39` | ldrb w12,[x23, #0xdde] | `FALL_THROUGH`
<a id="insn-00acfe3c"></a> `00acfe3c` | `08 3d 10 53` | lsl w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00acfe40"></a> `00acfe40` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfe44"></a> `00acfe44` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00acfe48"></a> `00acfe48` | `ea 76 77 39` | ldrb w10,[x23, #0xddd] | `FALL_THROUGH`
<a id="insn-00acfe4c"></a> `00acfe4c` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00acfe50"></a> `00acfe50` | `08 61 09 2a` | orr w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00acfe54"></a> `00acfe54` | `89 d2 5f 38` | ldurb w9,[x20, #-0x3] | `FALL_THROUGH`
<a id="insn-00acfe58"></a> `00acfe58` | `08 21 0b 2a` | orr w8,w8,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00acfe5c"></a> `00acfe5c` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00acfe60"></a> `00acfe60` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00acfe64"></a> `00acfe64` | `1b 7d 40 93` | sxtw x27,w8 | `FALL_THROUGH`
<a id="insn-00acfe68"></a> `00acfe68` | `56 44 fc 97` | bl 0x009e0fc0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfe6c"></a> `00acfe6c` | `20 02 00 36` | tbz w0,#0x0,0x00acfeb0 | `CONDITIONAL_JUMP`
<a id="insn-00acfe70"></a> `00acfe70` | `60 42 01 91` | add x0,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00acfe74"></a> `00acfe74` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfe78"></a> `00acfe78` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfe7c"></a> `00acfe7c` | `46 4c fc 97` | bl 0x009e2f94 | `UNCONDITIONAL_CALL`
<a id="insn-00acfe80"></a> `00acfe80` | `80 01 00 b4` | cbz x0,0x00acfeb0 | `CONDITIONAL_JUMP`
<a id="insn-00acfe84"></a> `00acfe84` | `e1 03 1b 2a` | mov w1,w27 | `FALL_THROUGH`
<a id="insn-00acfe88"></a> `00acfe88` | `eb 3d fc 97` | bl 0x009df634 | `UNCONDITIONAL_CALL`
<a id="insn-00acfe8c"></a> `00acfe8c` | `20 01 00 b4` | cbz x0,0x00acfeb0 | `CONDITIONAL_JUMP`
<a id="insn-00acfe90"></a> `00acfe90` | `08 10 00 91` | add x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00acfe94"></a> `00acfe94` | `09 00 00 14` | b 0x00acfeb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfe98"></a> `00acfe98` | `bf ff 3d a9` | stp xzr,xzr,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acfe9c"></a> `00acfe9c` | `b8 03 1f b8` | stur w24,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acfea0"></a> `00acfea0` | `a0 62 0c 91` | add x0,x21,#0x318 | `FALL_THROUGH`
<a id="insn-00acfea4"></a> `00acfea4` | `a1 43 00 d1` | sub x1,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00acfea8"></a> `00acfea8` | `23 4b fb 97` | bl 0x009a2b34 | `UNCONDITIONAL_CALL`
<a id="insn-00acfeac"></a> `00acfeac` | `37 00 00 14` | b 0x00acff88 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfeb0"></a> `00acfeb0` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfeb4"></a> `00acfeb4` | `08 09 1b 8b` | add x8,x8,x27, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00acfeb8"></a> `00acfeb8` | `08 01 80 b9` | ldrsw x8,[x8] | `FALL_THROUGH`
<a id="insn-00acfebc"></a> `00acfebc` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acfec0"></a> `00acfec0` | `0a 3c 80 52` | mov w10,#0x1e0 | `FALL_THROUGH`
<a id="insn-00acfec4"></a> `00acfec4` | `69 27 2a 9b` | smaddl x9,w27,w10,x9 | `FALL_THROUGH`
<a id="insn-00acfec8"></a> `00acfec8` | `0a 0f 80 52` | mov w10,#0x78 | `FALL_THROUGH`
<a id="insn-00acfecc"></a> `00acfecc` | `42 0e 00 f0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00acfed0"></a> `00acfed0` | `01 25 2a 9b` | smaddl x1,w8,w10,x9 | `FALL_THROUGH`
<a id="insn-00acfed4"></a> `00acfed4` | `42 50 46 f9` | ldr x2,[x2, #0xca0] | `FALL_THROUGH`
<a id="insn-00acfed8"></a> `00acfed8` | `a8 a3 00 d1` | sub x8,x29,#0x28 | `FALL_THROUGH`
<a id="insn-00acfedc"></a> `00acfedc` | `a0 0e 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00acfee0"></a> `00acfee0` | `00 00 3c 91` | add x0,x0,#0xf00 | `FALL_THROUGH`
<a id="insn-00acfee4"></a> `00acfee4` | `c3 03 80 52` | mov w3,#0x1e | `FALL_THROUGH`
<a id="insn-00acfee8"></a> `00acfee8` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00acfeec"></a> `00acfeec` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00acfef0"></a> `00acfef0` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00acfef4"></a> `00acfef4` | `3c 8e ed 97` | bl 0x006337e4 | `UNCONDITIONAL_CALL`
<a id="insn-00acfef8"></a> `00acfef8` | `a8 83 5d f8` | ldur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acfefc"></a> `00acfefc` | `b8 83 1e b8` | stur w24,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00acff00"></a> `00acff00` | `e8 03 00 b4` | cbz x8,0x00acff7c | `CONDITIONAL_JUMP`
<a id="insn-00acff04"></a> `00acff04` | `a8 63 00 d1` | sub x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acff08"></a> `00acff08` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acff0c"></a> `00acff0c` | `a0 62 0c 91` | add x0,x21,#0x318 | `FALL_THROUGH`
<a id="insn-00acff10"></a> `00acff10` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acff14"></a> `00acff14` | `a3 43 00 d1` | sub x3,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00acff18"></a> `00acff18` | `a4 47 00 d1` | sub x4,x29,#0x11 | `FALL_THROUGH`
<a id="insn-00acff1c"></a> `00acff1c` | `c2 bf ff b0` | adrp x2,0x2c8000 | `FALL_THROUGH`
<a id="insn-00acff20"></a> `00acff20` | `42 d4 1b 91` | add x2,x2,#0x6f5 | `FALL_THROUGH`
<a id="insn-00acff24"></a> `00acff24` | `22 17 ef 97` | bl 0x00695bac | `UNCONDITIONAL_CALL`
<a id="insn-00acff28"></a> `00acff28` | `b5 db 7d a9` | ldp x21,x22,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acff2c"></a> `00acff2c` | `fc 03 00 aa` | mov x28,x0 | `FALL_THROUGH`
<a id="insn-00acff30"></a> `00acff30` | `96 00 00 b4` | cbz x22,0x00acff40 | `CONDITIONAL_JUMP`
<a id="insn-00acff34"></a> `00acff34` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00acff38"></a> `00acff38` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acff3c"></a> `00acff3c` | `65 0f 06 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00acff40"></a> `00acff40` | `9b 13 40 f9` | ldr x27,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00acff44"></a> `00acff44` | `95 db 01 a9` | stp x21,x22,[x28, #0x18] | `FALL_THROUGH`
<a id="insn-00acff48"></a> `00acff48` | `f5 17 40 f9` | ldr x21,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acff4c"></a> `00acff4c` | `fb 01 00 b4` | cbz x27,0x00acff88 | `CONDITIONAL_JUMP`
<a id="insn-00acff50"></a> `00acff50` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00acff54"></a> `00acff54` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acff58"></a> `00acff58` | `6a 0f 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00acff5c"></a> `00acff5c` | `60 01 00 b5` | cbnz x0,0x00acff88 | `CONDITIONAL_JUMP`
<a id="insn-00acff60"></a> `00acff60` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00acff64"></a> `00acff64` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00acff68"></a> `00acff68` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acff6c"></a> `00acff6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acff70"></a> `00acff70` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00acff74"></a> `00acff74` | `c3 1f 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00acff78"></a> `00acff78` | `04 00 00 14` | b 0x00acff88 | `UNCONDITIONAL_JUMP`
<a id="insn-00acff7c"></a> `00acff7c` | `a0 62 0c 91` | add x0,x21,#0x318 | `FALL_THROUGH`
<a id="insn-00acff80"></a> `00acff80` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acff84"></a> `00acff84` | `ec 4a fb 97` | bl 0x009a2b34 | `UNCONDITIONAL_CALL`
<a id="insn-00acff88"></a> `00acff88` | `bb 03 5e f8` | ldur x27,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acff8c"></a> `00acff8c` | `9b f0 ff b4` | cbz x27,0x00acfd9c | `CONDITIONAL_JUMP`
<a id="insn-00acff90"></a> `00acff90` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00acff94"></a> `00acff94` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acff98"></a> `00acff98` | `5a 0f 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00acff9c"></a> `00acff9c` | `00 f0 ff b5` | cbnz x0,0x00acfd9c | `CONDITIONAL_JUMP`
<a id="insn-00acffa0"></a> `00acffa0` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00acffa4"></a> `00acffa4` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00acffa8"></a> `00acffa8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acffac"></a> `00acffac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acffb0"></a> `00acffb0` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00acffb4"></a> `00acffb4` | `b3 1f 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00acffb8"></a> `00acffb8` | `79 ff ff 17` | b 0x00acfd9c | `UNCONDITIONAL_JUMP`
<a id="insn-00acffbc"></a> `00acffbc` | `a0 0e 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00acffc0"></a> `00acffc0` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00acffc4"></a> `00acffc4` | `a3 1f 06 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00acffc8"></a> `00acffc8` | `80 f2 ff 34` | cbz w0,0x00acfe18 | `CONDITIONAL_JUMP`
<a id="insn-00acffcc"></a> `00acffcc` | `a1 0e 00 b0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00acffd0"></a> `00acffd0` | `21 00 3c 91` | add x1,x1,#0xf00 | `FALL_THROUGH`
<a id="insn-00acffd4"></a> `00acffd4` | `60 cd ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00acffd8"></a> `00acffd8` | `00 d0 36 91` | add x0,x0,#0xdb4 | `FALL_THROUGH`
<a id="insn-00acffdc"></a> `00acffdc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acffe0"></a> `00acffe0` | `82 0c 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00acffe4"></a> `00acffe4` | `42 40 3e 91` | add x2,x2,#0xf90 | `FALL_THROUGH`
<a id="insn-00acffe8"></a> `00acffe8` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00acffec"></a> `00acffec` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00acfff0"></a> `00acfff0` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acfff4"></a> `00acfff4` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00acfff8"></a> `00acfff8` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acfffc"></a> `00acfffc` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00ad0000"></a> `00ad0000` | `8c 1f 06 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-00ad0004"></a> `00ad0004` | `a0 0e 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad0008"></a> `00ad0008` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ad000c"></a> `00ad000c` | `99 1f 06 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00ad0010"></a> `00ad0010` | `82 ff ff 17` | b 0x00acfe18 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad0014"></a> `00ad0014` | `08 ef 8b 52` | mov w8,#0x5f78 | `FALL_THROUGH`
<a id="insn-00ad0018"></a> `00ad0018` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ad001c"></a> `00ad001c` | `68 6a 68 b8` | ldr w8,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad0020"></a> `00ad0020` | `e8 14 f8 37` | tbnz w8,#0x1f,0x00ad02bc | `CONDITIONAL_JUMP`
<a id="insn-00ad0024"></a> `00ad0024` | `fc 03 1f aa` | mov x28,xzr | `FALL_THROUGH`
<a id="insn-00ad0028"></a> `00ad0028` | `b6 c2 0b 91` | add x22,x21,#0x2f0 | `FALL_THROUGH`
<a id="insn-00ad002c"></a> `00ad002c` | `db bf ff 90` | adrp x27,0x2c8000 | `FALL_THROUGH`
<a id="insn-00ad0030"></a> `00ad0030` | `7b d7 1b 91` | add x27,x27,#0x6f5 | `FALL_THROUGH`
<a id="insn-00ad0034"></a> `00ad0034` | `08 00 00 14` | b 0x00ad0054 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad0038"></a> `00ad0038` | `f5 17 40 f9` | ldr x21,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ad003c"></a> `00ad003c` | `08 ef 8b 52` | mov w8,#0x5f78 | `FALL_THROUGH`
<a id="insn-00ad0040"></a> `00ad0040` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ad0044"></a> `00ad0044` | `68 6a a8 b8` | ldrsw x8,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad0048"></a> `00ad0048` | `9f 03 08 eb` | cmp x28,x8 | `FALL_THROUGH`
<a id="insn-00ad004c"></a> `00ad004c` | `9c 07 00 91` | add x28,x28,#0x1 | `FALL_THROUGH`
<a id="insn-00ad0050"></a> `00ad0050` | `6a 13 00 54` | b.ge 0x00ad02bc | `CONDITIONAL_JUMP`
<a id="insn-00ad0054"></a> `00ad0054` | `9f 03 1a eb` | cmp x28,x26 | `FALL_THROUGH`
<a id="insn-00ad0058"></a> `00ad0058` | `ab 04 00 54` | b.lt 0x00ad00ec | `CONDITIONAL_JUMP`
<a id="insn-00ad005c"></a> `00ad005c` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad0060"></a> `00ad0060` | `9f 03 08 eb` | cmp x28,x8 | `FALL_THROUGH`
<a id="insn-00ad0064"></a> `00ad0064` | `4c 04 00 54` | b.gt 0x00ad00ec | `CONDITIONAL_JUMP`
<a id="insn-00ad0068"></a> `00ad0068` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad006c"></a> `00ad006c` | `ea 7e 77 39` | ldrb w10,[x23, #0xddf] | `FALL_THROUGH`
<a id="insn-00ad0070"></a> `00ad0070` | `60 42 01 91` | add x0,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00ad0074"></a> `00ad0074` | `eb 82 77 39` | ldrb w11,[x23, #0xde0] | `FALL_THROUGH`
<a id="insn-00ad0078"></a> `00ad0078` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ad007c"></a> `00ad007c` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ad0080"></a> `00ad0080` | `08 09 1c 8b` | add x8,x8,x28, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ad0084"></a> `00ad0084` | `09 09 40 39` | ldrb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00ad0088"></a> `00ad0088` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00ad008c"></a> `00ad008c` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00ad0090"></a> `00ad0090` | `0a 0d 40 39` | ldrb w10,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00ad0094"></a> `00ad0094` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ad0098"></a> `00ad0098` | `29 3d 10 53` | lsl w9,w9,#0x10 | `FALL_THROUGH`
<a id="insn-00ad009c"></a> `00ad009c` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00ad00a0"></a> `00ad00a0` | `eb 7a 77 39` | ldrb w11,[x23, #0xdde] | `FALL_THROUGH`
<a id="insn-00ad00a4"></a> `00ad00a4` | `29 61 0a 2a` | orr w9,w9,w10, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00ad00a8"></a> `00ad00a8` | `ea 76 77 39` | ldrb w10,[x23, #0xddd] | `FALL_THROUGH`
<a id="insn-00ad00ac"></a> `00ad00ac` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00ad00b0"></a> `00ad00b0` | `29 21 0b 2a` | orr w9,w9,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00ad00b4"></a> `00ad00b4` | `48 01 08 4a` | eor w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00ad00b8"></a> `00ad00b8` | `38 01 08 2a` | orr w24,w9,w8 | `FALL_THROUGH`
<a id="insn-00ad00bc"></a> `00ad00bc` | `c1 43 fc 97` | bl 0x009e0fc0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad00c0"></a> `00ad00c0` | `00 03 00 36` | tbz w0,#0x0,0x00ad0120 | `CONDITIONAL_JUMP`
<a id="insn-00ad00c4"></a> `00ad00c4` | `60 42 01 91` | add x0,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00ad00c8"></a> `00ad00c8` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ad00cc"></a> `00ad00cc` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ad00d0"></a> `00ad00d0` | `b1 4b fc 97` | bl 0x009e2f94 | `UNCONDITIONAL_CALL`
<a id="insn-00ad00d4"></a> `00ad00d4` | `60 02 00 b4` | cbz x0,0x00ad0120 | `CONDITIONAL_JUMP`
<a id="insn-00ad00d8"></a> `00ad00d8` | `e1 03 18 2a` | mov w1,w24 | `FALL_THROUGH`
<a id="insn-00ad00dc"></a> `00ad00dc` | `56 3d fc 97` | bl 0x009df634 | `UNCONDITIONAL_CALL`
<a id="insn-00ad00e0"></a> `00ad00e0` | `00 02 00 b4` | cbz x0,0x00ad0120 | `CONDITIONAL_JUMP`
<a id="insn-00ad00e4"></a> `00ad00e4` | `08 10 00 91` | add x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00ad00e8"></a> `00ad00e8` | `10 00 00 14` | b 0x00ad0128 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad00ec"></a> `00ad00ec` | `a8 7e 41 f9` | ldr x8,[x21, #0x2f8] | `FALL_THROUGH`
<a id="insn-00ad00f0"></a> `00ad00f0` | `68 fa ff b4` | cbz x8,0x00ad003c | `CONDITIONAL_JUMP`
<a id="insn-00ad00f4"></a> `00ad00f4` | `00 01 67 9e` | fmov d0,x8 | `FALL_THROUGH`
<a id="insn-00ad00f8"></a> `00ad00f8` | `89 2f 00 91` | add x9,x28,#0xb | `FALL_THROUGH`
<a id="insn-00ad00fc"></a> `00ad00fc` | `00 58 20 0e` | cnt v0.8B,v0.8B | `FALL_THROUGH`
<a id="insn-00ad0100"></a> `00ad0100` | `00 38 30 2e` | uaddlv h0,v0.8B | `FALL_THROUGH`
<a id="insn-00ad0104"></a> `00ad0104` | `0a 00 26 1e` | fmov w10,s0 | `FALL_THROUGH`
<a id="insn-00ad0108"></a> `00ad0108` | `5f 05 00 f1` | cmp x10,#0x1 | `FALL_THROUGH`
<a id="insn-00ad010c"></a> `00ad010c` | `68 07 00 54` | b.hi 0x00ad01f8 | `CONDITIONAL_JUMP`
<a id="insn-00ad0110"></a> `00ad0110` | `0b 00 b0 12` | mov w11,#0x7fffffff | `FALL_THROUGH`
<a id="insn-00ad0114"></a> `00ad0114` | `0b 01 0b 8b` | add x11,x8,x11 | `FALL_THROUGH`
<a id="insn-00ad0118"></a> `00ad0118` | `6b 01 09 8a` | and x11,x11,x9 | `FALL_THROUGH`
<a id="insn-00ad011c"></a> `00ad011c` | `3c 00 00 14` | b 0x00ad020c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad0120"></a> `00ad0120` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad0124"></a> `00ad0124` | `08 c9 38 8b` | add x8,x8,w24, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00ad0128"></a> `00ad0128` | `01 01 40 b9` | ldr w1,[x8] | `FALL_THROUGH`
<a id="insn-00ad012c"></a> `00ad012c` | `a8 a3 00 d1` | sub x8,x29,#0x28 | `FALL_THROUGH`
<a id="insn-00ad0130"></a> `00ad0130` | `e0 03 18 2a` | mov w0,w24 | `FALL_THROUGH`
<a id="insn-00ad0134"></a> `00ad0134` | `bd 5a ee 97` | bl 0x00666c28 | `UNCONDITIONAL_CALL`
<a id="insn-00ad0138"></a> `00ad0138` | `a8 83 5d f8` | ldur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00ad013c"></a> `00ad013c` | `89 2f 00 11` | add w9,w28,#0xb | `FALL_THROUGH`
<a id="insn-00ad0140"></a> `00ad0140` | `a9 83 1e b8` | stur w9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00ad0144"></a> `00ad0144` | `a8 03 00 b4` | cbz x8,0x00ad01b8 | `CONDITIONAL_JUMP`
<a id="insn-00ad0148"></a> `00ad0148` | `a8 63 00 d1` | sub x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00ad014c"></a> `00ad014c` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ad0150"></a> `00ad0150` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00ad0154"></a> `00ad0154` | `a3 43 00 d1` | sub x3,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00ad0158"></a> `00ad0158` | `a4 47 00 d1` | sub x4,x29,#0x11 | `FALL_THROUGH`
<a id="insn-00ad015c"></a> `00ad015c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ad0160"></a> `00ad0160` | `e2 03 1b aa` | mov x2,x27 | `FALL_THROUGH`
<a id="insn-00ad0164"></a> `00ad0164` | `92 16 ef 97` | bl 0x00695bac | `UNCONDITIONAL_CALL`
<a id="insn-00ad0168"></a> `00ad0168` | `b5 d3 7d a9` | ldp x21,x20,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00ad016c"></a> `00ad016c` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00ad0170"></a> `00ad0170` | `94 00 00 b4` | cbz x20,0x00ad0180 | `CONDITIONAL_JUMP`
<a id="insn-00ad0174"></a> `00ad0174` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ad0178"></a> `00ad0178` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ad017c"></a> `00ad017c` | `d5 0e 06 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad0180"></a> `00ad0180` | `38 13 40 f9` | ldr x24,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00ad0184"></a> `00ad0184` | `35 d3 01 a9` | stp x21,x20,[x25, #0x18] | `FALL_THROUGH`
<a id="insn-00ad0188"></a> `00ad0188` | `f8 01 00 b4` | cbz x24,0x00ad01c4 | `CONDITIONAL_JUMP`
<a id="insn-00ad018c"></a> `00ad018c` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00ad0190"></a> `00ad0190` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ad0194"></a> `00ad0194` | `db 0e 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00ad0198"></a> `00ad0198` | `60 01 00 b5` | cbnz x0,0x00ad01c4 | `CONDITIONAL_JUMP`
<a id="insn-00ad019c"></a> `00ad019c` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00ad01a0"></a> `00ad01a0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00ad01a4"></a> `00ad01a4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad01a8"></a> `00ad01a8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad01ac"></a> `00ad01ac` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00ad01b0"></a> `00ad01b0` | `34 1f 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00ad01b4"></a> `00ad01b4` | `04 00 00 14` | b 0x00ad01c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad01b8"></a> `00ad01b8` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00ad01bc"></a> `00ad01bc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ad01c0"></a> `00ad01c0` | `5d 4a fb 97` | bl 0x009a2b34 | `UNCONDITIONAL_CALL`
<a id="insn-00ad01c4"></a> `00ad01c4` | `b8 03 5e f8` | ldur x24,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ad01c8"></a> `00ad01c8` | `98 f3 ff b4` | cbz x24,0x00ad0038 | `CONDITIONAL_JUMP`
<a id="insn-00ad01cc"></a> `00ad01cc` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00ad01d0"></a> `00ad01d0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ad01d4"></a> `00ad01d4` | `cb 0e 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00ad01d8"></a> `00ad01d8` | `00 f3 ff b5` | cbnz x0,0x00ad0038 | `CONDITIONAL_JUMP`
<a id="insn-00ad01dc"></a> `00ad01dc` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00ad01e0"></a> `00ad01e0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00ad01e4"></a> `00ad01e4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad01e8"></a> `00ad01e8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad01ec"></a> `00ad01ec` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00ad01f0"></a> `00ad01f0` | `24 1f 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00ad01f4"></a> `00ad01f4` | `91 ff ff 17` | b 0x00ad0038 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad01f8"></a> `00ad01f8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad01fc"></a> `00ad01fc` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00ad0200"></a> `00ad0200` | `68 00 00 54` | b.hi 0x00ad020c | `CONDITIONAL_JUMP`
<a id="insn-00ad0204"></a> `00ad0204` | `2b 09 c8 9a` | udiv x11,x9,x8 | `FALL_THROUGH`
<a id="insn-00ad0208"></a> `00ad0208` | `6b a5 08 9b` | msub x11,x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00ad020c"></a> `00ad020c` | `cc 02 40 f9` | ldr x12,[x22] | `FALL_THROUGH`
<a id="insn-00ad0210"></a> `00ad0210` | `8c 79 6b f8` | ldr x12,[x12, x11, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ad0214"></a> `00ad0214` | `4c f1 ff b4` | cbz x12,0x00ad003c | `CONDITIONAL_JUMP`
<a id="insn-00ad0218"></a> `00ad0218` | `8c 01 40 f9` | ldr x12,[x12] | `FALL_THROUGH`
<a id="insn-00ad021c"></a> `00ad021c` | `0c f1 ff b4` | cbz x12,0x00ad003c | `CONDITIONAL_JUMP`
<a id="insn-00ad0220"></a> `00ad0220` | `0d 05 00 d1` | sub x13,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad0224"></a> `00ad0224` | `06 00 00 14` | b 0x00ad023c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad0228"></a> `00ad0228` | `8e 11 40 b9` | ldr w14,[x12, #0x10] | `FALL_THROUGH`
<a id="insn-00ad022c"></a> `00ad022c` | `3f 01 0e eb` | cmp x9,x14 | `FALL_THROUGH`
<a id="insn-00ad0230"></a> `00ad0230` | `20 02 00 54` | b.eq 0x00ad0274 | `CONDITIONAL_JUMP`
<a id="insn-00ad0234"></a> `00ad0234` | `8c 01 40 f9` | ldr x12,[x12] | `FALL_THROUGH`
<a id="insn-00ad0238"></a> `00ad0238` | `2c f0 ff b4` | cbz x12,0x00ad003c | `CONDITIONAL_JUMP`
<a id="insn-00ad023c"></a> `00ad023c` | `8e 05 40 f9` | ldr x14,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-00ad0240"></a> `00ad0240` | `df 01 09 eb` | cmp x14,x9 | `FALL_THROUGH`
<a id="insn-00ad0244"></a> `00ad0244` | `20 ff ff 54` | b.eq 0x00ad0228 | `CONDITIONAL_JUMP`
<a id="insn-00ad0248"></a> `00ad0248` | `5f 05 00 f1` | cmp x10,#0x1 | `FALL_THROUGH`
<a id="insn-00ad024c"></a> `00ad024c` | `68 00 00 54` | b.hi 0x00ad0258 | `CONDITIONAL_JUMP`
<a id="insn-00ad0250"></a> `00ad0250` | `ce 01 0d 8a` | and x14,x14,x13 | `FALL_THROUGH`
<a id="insn-00ad0254"></a> `00ad0254` | `05 00 00 14` | b 0x00ad0268 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad0258"></a> `00ad0258` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00ad025c"></a> `00ad025c` | `63 00 00 54` | b.cc 0x00ad0268 | `CONDITIONAL_JUMP`
<a id="insn-00ad0260"></a> `00ad0260` | `cf 09 c8 9a` | udiv x15,x14,x8 | `FALL_THROUGH`
<a id="insn-00ad0264"></a> `00ad0264` | `ee b9 08 9b` | msub x14,x15,x8,x14 | `FALL_THROUGH`
<a id="insn-00ad0268"></a> `00ad0268` | `df 01 0b eb` | cmp x14,x11 | `FALL_THROUGH`
<a id="insn-00ad026c"></a> `00ad026c` | `40 fe ff 54` | b.eq 0x00ad0234 | `CONDITIONAL_JUMP`
<a id="insn-00ad0270"></a> `00ad0270` | `73 ff ff 17` | b 0x00ad003c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad0274"></a> `00ad0274` | `bf ff 3d a9` | stp xzr,xzr,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00ad0278"></a> `00ad0278` | `a9 03 1f b8` | stur w9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ad027c"></a> `00ad027c` | `a1 43 00 d1` | sub x1,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00ad0280"></a> `00ad0280` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ad0284"></a> `00ad0284` | `2c 4a fb 97` | bl 0x009a2b34 | `UNCONDITIONAL_CALL`
<a id="insn-00ad0288"></a> `00ad0288` | `b8 03 5e f8` | ldur x24,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ad028c"></a> `00ad028c` | `98 ed ff b4` | cbz x24,0x00ad003c | `CONDITIONAL_JUMP`
<a id="insn-00ad0290"></a> `00ad0290` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00ad0294"></a> `00ad0294` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ad0298"></a> `00ad0298` | `9a 0e 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00ad029c"></a> `00ad029c` | `00 ed ff b5` | cbnz x0,0x00ad003c | `CONDITIONAL_JUMP`
<a id="insn-00ad02a0"></a> `00ad02a0` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00ad02a4"></a> `00ad02a4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00ad02a8"></a> `00ad02a8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad02ac"></a> `00ad02ac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad02b0"></a> `00ad02b0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00ad02b4"></a> `00ad02b4` | `f3 1e 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00ad02b8"></a> `00ad02b8` | `61 ff ff 17` | b 0x00ad003c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad02bc"></a> `00ad02bc` | `a8 0e 00 90` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad02c0"></a> `00ad02c0` | `08 e1 3c 91` | add x8,x8,#0xf38 | `FALL_THROUGH`
<a id="insn-00ad02c4"></a> `00ad02c4` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ad02c8"></a> `00ad02c8` | `48 02 00 36` | tbz w8,#0x0,0x00ad0310 | `CONDITIONAL_JUMP`
<a id="insn-00ad02cc"></a> `00ad02cc` | `a8 0e 00 90` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad02d0"></a> `00ad02d0` | `00 99 47 f9` | ldr x0,[x8, #0xf30] | `FALL_THROUGH`
<a id="insn-00ad02d4"></a> `00ad02d4` | `40 00 00 b4` | cbz x0,0x00ad02dc | `CONDITIONAL_JUMP`
<a id="insn-00ad02d8"></a> `00ad02d8` | `be 1f e7 97` | bl 0x004981d0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad02dc"></a> `00ad02dc` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad02e0"></a> `00ad02e0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ad02e4"></a> `00ad02e4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad02e8"></a> `00ad02e8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad02ec"></a> `00ad02ec` | `81 05 00 54` | b.ne 0x00ad039c | `CONDITIONAL_JUMP`
<a id="insn-00ad02f0"></a> `00ad02f0` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00ad02f4"></a> `00ad02f4` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ad02f8"></a> `00ad02f8` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ad02fc"></a> `00ad02fc` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ad0300"></a> `00ad0300` | `fc 6f 47 a9` | ldp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad0304"></a> `00ad0304` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad0308"></a> `00ad0308` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00ad030c"></a> `00ad030c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad0310"></a> `00ad0310` | `a0 0e 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad0314"></a> `00ad0314` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ad0318"></a> `00ad0318` | `ce 1e 06 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00ad031c"></a> `00ad031c` | `80 fd ff 34` | cbz w0,0x00ad02cc | `CONDITIONAL_JUMP`
<a id="insn-00ad0320"></a> `00ad0320` | `a1 0e 00 90` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad0324"></a> `00ad0324` | `21 00 3c 91` | add x1,x1,#0xf00 | `FALL_THROUGH`
<a id="insn-00ad0328"></a> `00ad0328` | `60 cd ff d0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00ad032c"></a> `00ad032c` | `00 d0 36 91` | add x0,x0,#0xdb4 | `FALL_THROUGH`
<a id="insn-00ad0330"></a> `00ad0330` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ad0334"></a> `00ad0334` | `82 0c 00 d0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00ad0338"></a> `00ad0338` | `42 40 3e 91` | add x2,x2,#0xf90 | `FALL_THROUGH`
<a id="insn-00ad033c"></a> `00ad033c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00ad0340"></a> `00ad0340` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00ad0344"></a> `00ad0344` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ad0348"></a> `00ad0348` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00ad034c"></a> `00ad034c` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00ad0350"></a> `00ad0350` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00ad0354"></a> `00ad0354` | `b7 1e 06 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-00ad0358"></a> `00ad0358` | `a0 0e 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ad035c"></a> `00ad035c` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ad0360"></a> `00ad0360` | `c4 1e 06 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00ad0364"></a> `00ad0364` | `da ff ff 17` | b 0x00ad02cc | `UNCONDITIONAL_JUMP`
<a id="insn-00ad039c"></a> `00ad039c` | `d1 1e 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfcc0`](#insn-00acfcc0) 範囲 `[['00acfcc0', '00acfd07']]`
  - `CONDITIONAL_JUMP` [`00acfd04`](#insn-00acfd04) → [`00acfd14`](#insn-00acfd14)
  - `FALL_THROUGH` [`00acfd04`](#insn-00acfd04) → [`00acfd08`](#insn-00acfd08)
- ブロック [`00acfd08`](#insn-00acfd08) 範囲 `[['00acfd08', '00acfd13']]`
  - `CONDITIONAL_JUMP` [`00acfd10`](#insn-00acfd10) → [`00ad02bc`](#insn-00ad02bc)
  - `FALL_THROUGH` [`00acfd10`](#insn-00acfd10) → [`00acfd14`](#insn-00acfd14)
- ブロック [`00acfd14`](#insn-00acfd14) 範囲 `[['00acfd14', '00acfd23']]`
  - `CONDITIONAL_JUMP` [`00acfd20`](#insn-00acfd20) → [`00acfd44`](#insn-00acfd44)
  - `FALL_THROUGH` [`00acfd20`](#insn-00acfd20) → [`00acfd24`](#insn-00acfd24)
- ブロック [`00acfd24`](#insn-00acfd24) 範囲 `[['00acfd24', '00acfd43']]`
  - `UNCONDITIONAL_JUMP` [`00acfd40`](#insn-00acfd40) → [`00acfd48`](#insn-00acfd48)
- ブロック [`00acfd44`](#insn-00acfd44) 範囲 `[['00acfd44', '00acfd47']]`
  - `FALL_THROUGH` [`00acfd44`](#insn-00acfd44) → [`00acfd48`](#insn-00acfd48)
- ブロック [`00acfd48`](#insn-00acfd48) 範囲 `[['00acfd48', '00acfd53']]`
  - `CONDITIONAL_JUMP` [`00acfd50`](#insn-00acfd50) → [`00ad02bc`](#insn-00ad02bc)
  - `FALL_THROUGH` [`00acfd50`](#insn-00acfd50) → [`00acfd54`](#insn-00acfd54)
- ブロック [`00acfd54`](#insn-00acfd54) 範囲 `[['00acfd54', '00acfd9b']]`
  - `UNCONDITIONAL_JUMP` [`00acfd98`](#insn-00acfd98) → [`00acfdac`](#insn-00acfdac)
- ブロック [`00acfd9c`](#insn-00acfd9c) 範囲 `[['00acfd9c', '00acfd9f']]`
  - `FALL_THROUGH` [`00acfd9c`](#insn-00acfd9c) → [`00acfda0`](#insn-00acfda0)
- ブロック [`00acfda0`](#insn-00acfda0) 範囲 `[['00acfda0', '00acfdab']]`
  - `CONDITIONAL_JUMP` [`00acfda8`](#insn-00acfda8) → [`00ad0014`](#insn-00ad0014)
  - `FALL_THROUGH` [`00acfda8`](#insn-00acfda8) → [`00acfdac`](#insn-00acfdac)
- ブロック [`00acfdac`](#insn-00acfdac) 範囲 `[['00acfdac', '00acfdf3']]`
  - `CONDITIONAL_JUMP` [`00acfdf0`](#insn-00acfdf0) → [`00acfda0`](#insn-00acfda0)
  - `FALL_THROUGH` [`00acfdf0`](#insn-00acfdf0) → [`00acfdf4`](#insn-00acfdf4)
- ブロック [`00acfdf4`](#insn-00acfdf4) 範囲 `[['00acfdf4', '00acfdfb']]`
  - `CONDITIONAL_JUMP` [`00acfdf8`](#insn-00acfdf8) → [`00acfe98`](#insn-00acfe98)
  - `FALL_THROUGH` [`00acfdf8`](#insn-00acfdf8) → [`00acfdfc`](#insn-00acfdfc)
- ブロック [`00acfdfc`](#insn-00acfdfc) 範囲 `[['00acfdfc', '00acfe07']]`
  - `CONDITIONAL_JUMP` [`00acfe04`](#insn-00acfe04) → [`00acfe98`](#insn-00acfe98)
  - `FALL_THROUGH` [`00acfe04`](#insn-00acfe04) → [`00acfe08`](#insn-00acfe08)
- ブロック [`00acfe08`](#insn-00acfe08) 範囲 `[['00acfe08', '00acfe17']]`
  - `CONDITIONAL_JUMP` [`00acfe14`](#insn-00acfe14) → [`00acffbc`](#insn-00acffbc)
  - `FALL_THROUGH` [`00acfe14`](#insn-00acfe14) → [`00acfe18`](#insn-00acfe18)
- ブロック [`00acfe18`](#insn-00acfe18) 範囲 `[['00acfe18', '00acfe6f']]`
  - `CONDITIONAL_JUMP` [`00acfe6c`](#insn-00acfe6c) → [`00acfeb0`](#insn-00acfeb0)
  - `FALL_THROUGH` [`00acfe6c`](#insn-00acfe6c) → [`00acfe70`](#insn-00acfe70)
- ブロック [`00acfe70`](#insn-00acfe70) 範囲 `[['00acfe70', '00acfe83']]`
  - `CONDITIONAL_JUMP` [`00acfe80`](#insn-00acfe80) → [`00acfeb0`](#insn-00acfeb0)
  - `FALL_THROUGH` [`00acfe80`](#insn-00acfe80) → [`00acfe84`](#insn-00acfe84)
- ブロック [`00acfe84`](#insn-00acfe84) 範囲 `[['00acfe84', '00acfe8f']]`
  - `CONDITIONAL_JUMP` [`00acfe8c`](#insn-00acfe8c) → [`00acfeb0`](#insn-00acfeb0)
  - `FALL_THROUGH` [`00acfe8c`](#insn-00acfe8c) → [`00acfe90`](#insn-00acfe90)
- ブロック [`00acfe90`](#insn-00acfe90) 範囲 `[['00acfe90', '00acfe97']]`
  - `UNCONDITIONAL_JUMP` [`00acfe94`](#insn-00acfe94) → [`00acfeb8`](#insn-00acfeb8)
- ブロック [`00acfe98`](#insn-00acfe98) 範囲 `[['00acfe98', '00acfeaf']]`
  - `UNCONDITIONAL_JUMP` [`00acfeac`](#insn-00acfeac) → [`00acff88`](#insn-00acff88)
- ブロック [`00acfeb0`](#insn-00acfeb0) 範囲 `[['00acfeb0', '00acfeb7']]`
  - `FALL_THROUGH` [`00acfeb4`](#insn-00acfeb4) → [`00acfeb8`](#insn-00acfeb8)
- ブロック [`00acfeb8`](#insn-00acfeb8) 範囲 `[['00acfeb8', '00acff03']]`
  - `CONDITIONAL_JUMP` [`00acff00`](#insn-00acff00) → [`00acff7c`](#insn-00acff7c)
  - `FALL_THROUGH` [`00acff00`](#insn-00acff00) → [`00acff04`](#insn-00acff04)
- ブロック [`00acff04`](#insn-00acff04) 範囲 `[['00acff04', '00acff33']]`
  - `CONDITIONAL_JUMP` [`00acff30`](#insn-00acff30) → [`00acff40`](#insn-00acff40)
  - `FALL_THROUGH` [`00acff30`](#insn-00acff30) → [`00acff34`](#insn-00acff34)
- ブロック [`00acff34`](#insn-00acff34) 範囲 `[['00acff34', '00acff3f']]`
  - `FALL_THROUGH` [`00acff3c`](#insn-00acff3c) → [`00acff40`](#insn-00acff40)
- ブロック [`00acff40`](#insn-00acff40) 範囲 `[['00acff40', '00acff4f']]`
  - `CONDITIONAL_JUMP` [`00acff4c`](#insn-00acff4c) → [`00acff88`](#insn-00acff88)
  - `FALL_THROUGH` [`00acff4c`](#insn-00acff4c) → [`00acff50`](#insn-00acff50)
- ブロック [`00acff50`](#insn-00acff50) 範囲 `[['00acff50', '00acff5f']]`
  - `CONDITIONAL_JUMP` [`00acff5c`](#insn-00acff5c) → [`00acff88`](#insn-00acff88)
  - `FALL_THROUGH` [`00acff5c`](#insn-00acff5c) → [`00acff60`](#insn-00acff60)
- ブロック [`00acff60`](#insn-00acff60) 範囲 `[['00acff60', '00acff7b']]`
  - `UNCONDITIONAL_JUMP` [`00acff78`](#insn-00acff78) → [`00acff88`](#insn-00acff88)
- ブロック [`00acff7c`](#insn-00acff7c) 範囲 `[['00acff7c', '00acff87']]`
  - `FALL_THROUGH` [`00acff84`](#insn-00acff84) → [`00acff88`](#insn-00acff88)
- ブロック [`00acff88`](#insn-00acff88) 範囲 `[['00acff88', '00acff8f']]`
  - `CONDITIONAL_JUMP` [`00acff8c`](#insn-00acff8c) → [`00acfd9c`](#insn-00acfd9c)
  - `FALL_THROUGH` [`00acff8c`](#insn-00acff8c) → [`00acff90`](#insn-00acff90)
- ブロック [`00acff90`](#insn-00acff90) 範囲 `[['00acff90', '00acff9f']]`
  - `CONDITIONAL_JUMP` [`00acff9c`](#insn-00acff9c) → [`00acfd9c`](#insn-00acfd9c)
  - `FALL_THROUGH` [`00acff9c`](#insn-00acff9c) → [`00acffa0`](#insn-00acffa0)
- ブロック [`00acffa0`](#insn-00acffa0) 範囲 `[['00acffa0', '00acffbb']]`
  - `UNCONDITIONAL_JUMP` [`00acffb8`](#insn-00acffb8) → [`00acfd9c`](#insn-00acfd9c)
- ブロック [`00acffbc`](#insn-00acffbc) 範囲 `[['00acffbc', '00acffcb']]`
  - `CONDITIONAL_JUMP` [`00acffc8`](#insn-00acffc8) → [`00acfe18`](#insn-00acfe18)
  - `FALL_THROUGH` [`00acffc8`](#insn-00acffc8) → [`00acffcc`](#insn-00acffcc)
- ブロック [`00acffcc`](#insn-00acffcc) 範囲 `[['00acffcc', '00acfffb']]`
  - `FALL_THROUGH` [`00acfff8`](#insn-00acfff8) → [`00acfffc`](#insn-00acfffc)
- ブロック [`00acfffc`](#insn-00acfffc) 範囲 `[['00acfffc', '00ad0013']]`
  - `UNCONDITIONAL_JUMP` [`00ad0010`](#insn-00ad0010) → [`00acfe18`](#insn-00acfe18)
- ブロック [`00ad0014`](#insn-00ad0014) 範囲 `[['00ad0014', '00ad0023']]`
  - `CONDITIONAL_JUMP` [`00ad0020`](#insn-00ad0020) → [`00ad02bc`](#insn-00ad02bc)
  - `FALL_THROUGH` [`00ad0020`](#insn-00ad0020) → [`00ad0024`](#insn-00ad0024)
- ブロック [`00ad0024`](#insn-00ad0024) 範囲 `[['00ad0024', '00ad0037']]`
  - `UNCONDITIONAL_JUMP` [`00ad0034`](#insn-00ad0034) → [`00ad0054`](#insn-00ad0054)
- ブロック [`00ad0038`](#insn-00ad0038) 範囲 `[['00ad0038', '00ad003b']]`
  - `FALL_THROUGH` [`00ad0038`](#insn-00ad0038) → [`00ad003c`](#insn-00ad003c)
- ブロック [`00ad003c`](#insn-00ad003c) 範囲 `[['00ad003c', '00ad0053']]`
  - `CONDITIONAL_JUMP` [`00ad0050`](#insn-00ad0050) → [`00ad02bc`](#insn-00ad02bc)
  - `FALL_THROUGH` [`00ad0050`](#insn-00ad0050) → [`00ad0054`](#insn-00ad0054)
- ブロック [`00ad0054`](#insn-00ad0054) 範囲 `[['00ad0054', '00ad005b']]`
  - `CONDITIONAL_JUMP` [`00ad0058`](#insn-00ad0058) → [`00ad00ec`](#insn-00ad00ec)
  - `FALL_THROUGH` [`00ad0058`](#insn-00ad0058) → [`00ad005c`](#insn-00ad005c)
- ブロック [`00ad005c`](#insn-00ad005c) 範囲 `[['00ad005c', '00ad005f']]`
  - `FALL_THROUGH` [`00ad005c`](#insn-00ad005c) → [`00ad0060`](#insn-00ad0060)
- ブロック [`00ad0060`](#insn-00ad0060) 範囲 `[['00ad0060', '00ad0067']]`
  - `CONDITIONAL_JUMP` [`00ad0064`](#insn-00ad0064) → [`00ad00ec`](#insn-00ad00ec)
  - `FALL_THROUGH` [`00ad0064`](#insn-00ad0064) → [`00ad0068`](#insn-00ad0068)
- ブロック [`00ad0068`](#insn-00ad0068) 範囲 `[['00ad0068', '00ad0073']]`
  - `FALL_THROUGH` [`00ad0070`](#insn-00ad0070) → [`00ad0074`](#insn-00ad0074)
- ブロック [`00ad0074`](#insn-00ad0074) 範囲 `[['00ad0074', '00ad00b3']]`
  - `FALL_THROUGH` [`00ad00b0`](#insn-00ad00b0) → [`00ad00b4`](#insn-00ad00b4)
- ブロック [`00ad00b4`](#insn-00ad00b4) 範囲 `[['00ad00b4', '00ad00c3']]`
  - `CONDITIONAL_JUMP` [`00ad00c0`](#insn-00ad00c0) → [`00ad0120`](#insn-00ad0120)
  - `FALL_THROUGH` [`00ad00c0`](#insn-00ad00c0) → [`00ad00c4`](#insn-00ad00c4)
- ブロック [`00ad00c4`](#insn-00ad00c4) 範囲 `[['00ad00c4', '00ad00d3']]`
  - `FALL_THROUGH` [`00ad00d0`](#insn-00ad00d0) → [`00ad00d4`](#insn-00ad00d4)
- ブロック [`00ad00d4`](#insn-00ad00d4) 範囲 `[['00ad00d4', '00ad00d7']]`
  - `CONDITIONAL_JUMP` [`00ad00d4`](#insn-00ad00d4) → [`00ad0120`](#insn-00ad0120)
  - `FALL_THROUGH` [`00ad00d4`](#insn-00ad00d4) → [`00ad00d8`](#insn-00ad00d8)
- ブロック [`00ad00d8`](#insn-00ad00d8) 範囲 `[['00ad00d8', '00ad00e3']]`
  - `CONDITIONAL_JUMP` [`00ad00e0`](#insn-00ad00e0) → [`00ad0120`](#insn-00ad0120)
  - `FALL_THROUGH` [`00ad00e0`](#insn-00ad00e0) → [`00ad00e4`](#insn-00ad00e4)
- ブロック [`00ad00e4`](#insn-00ad00e4) 範囲 `[['00ad00e4', '00ad00eb']]`
  - `UNCONDITIONAL_JUMP` [`00ad00e8`](#insn-00ad00e8) → [`00ad0128`](#insn-00ad0128)
- ブロック [`00ad00ec`](#insn-00ad00ec) 範囲 `[['00ad00ec', '00ad00f3']]`
  - `CONDITIONAL_JUMP` [`00ad00f0`](#insn-00ad00f0) → [`00ad003c`](#insn-00ad003c)
  - `FALL_THROUGH` [`00ad00f0`](#insn-00ad00f0) → [`00ad00f4`](#insn-00ad00f4)
- ブロック [`00ad00f4`](#insn-00ad00f4) 範囲 `[['00ad00f4', '00ad00fb']]`
  - `FALL_THROUGH` [`00ad00f8`](#insn-00ad00f8) → [`00ad00fc`](#insn-00ad00fc)
- ブロック [`00ad00fc`](#insn-00ad00fc) 範囲 `[['00ad00fc', '00ad010f']]`
  - `CONDITIONAL_JUMP` [`00ad010c`](#insn-00ad010c) → [`00ad01f8`](#insn-00ad01f8)
  - `FALL_THROUGH` [`00ad010c`](#insn-00ad010c) → [`00ad0110`](#insn-00ad0110)
- ブロック [`00ad0110`](#insn-00ad0110) 範囲 `[['00ad0110', '00ad011f']]`
  - `UNCONDITIONAL_JUMP` [`00ad011c`](#insn-00ad011c) → [`00ad020c`](#insn-00ad020c)
- ブロック [`00ad0120`](#insn-00ad0120) 範囲 `[['00ad0120', '00ad0127']]`
  - `FALL_THROUGH` [`00ad0124`](#insn-00ad0124) → [`00ad0128`](#insn-00ad0128)
- ブロック [`00ad0128`](#insn-00ad0128) 範囲 `[['00ad0128', '00ad013b']]`
  - `FALL_THROUGH` [`00ad0138`](#insn-00ad0138) → [`00ad013c`](#insn-00ad013c)
- ブロック [`00ad013c`](#insn-00ad013c) 範囲 `[['00ad013c', '00ad0147']]`
  - `CONDITIONAL_JUMP` [`00ad0144`](#insn-00ad0144) → [`00ad01b8`](#insn-00ad01b8)
  - `FALL_THROUGH` [`00ad0144`](#insn-00ad0144) → [`00ad0148`](#insn-00ad0148)
- ブロック [`00ad0148`](#insn-00ad0148) 範囲 `[['00ad0148', '00ad0173']]`
  - `CONDITIONAL_JUMP` [`00ad0170`](#insn-00ad0170) → [`00ad0180`](#insn-00ad0180)
  - `FALL_THROUGH` [`00ad0170`](#insn-00ad0170) → [`00ad0174`](#insn-00ad0174)
- ブロック [`00ad0174`](#insn-00ad0174) 範囲 `[['00ad0174', '00ad017b']]`
  - `FALL_THROUGH` [`00ad0178`](#insn-00ad0178) → [`00ad017c`](#insn-00ad017c)
- ブロック [`00ad017c`](#insn-00ad017c) 範囲 `[['00ad017c', '00ad017f']]`
  - `FALL_THROUGH` [`00ad017c`](#insn-00ad017c) → [`00ad0180`](#insn-00ad0180)
- ブロック [`00ad0180`](#insn-00ad0180) 範囲 `[['00ad0180', '00ad018b']]`
  - `CONDITIONAL_JUMP` [`00ad0188`](#insn-00ad0188) → [`00ad01c4`](#insn-00ad01c4)
  - `FALL_THROUGH` [`00ad0188`](#insn-00ad0188) → [`00ad018c`](#insn-00ad018c)
- ブロック [`00ad018c`](#insn-00ad018c) 範囲 `[['00ad018c', '00ad0193']]`
  - `FALL_THROUGH` [`00ad0190`](#insn-00ad0190) → [`00ad0194`](#insn-00ad0194)
- ブロック [`00ad0194`](#insn-00ad0194) 範囲 `[['00ad0194', '00ad019b']]`
  - `CONDITIONAL_JUMP` [`00ad0198`](#insn-00ad0198) → [`00ad01c4`](#insn-00ad01c4)
  - `FALL_THROUGH` [`00ad0198`](#insn-00ad0198) → [`00ad019c`](#insn-00ad019c)
- ブロック [`00ad019c`](#insn-00ad019c) 範囲 `[['00ad019c', '00ad01b7']]`
  - `UNCONDITIONAL_JUMP` [`00ad01b4`](#insn-00ad01b4) → [`00ad01c4`](#insn-00ad01c4)
- ブロック [`00ad01b8`](#insn-00ad01b8) 範囲 `[['00ad01b8', '00ad01bb']]`
  - `FALL_THROUGH` [`00ad01b8`](#insn-00ad01b8) → [`00ad01bc`](#insn-00ad01bc)
- ブロック [`00ad01bc`](#insn-00ad01bc) 範囲 `[['00ad01bc', '00ad01c3']]`
  - `FALL_THROUGH` [`00ad01c0`](#insn-00ad01c0) → [`00ad01c4`](#insn-00ad01c4)
- ブロック [`00ad01c4`](#insn-00ad01c4) 範囲 `[['00ad01c4', '00ad01c7']]`
  - `FALL_THROUGH` [`00ad01c4`](#insn-00ad01c4) → [`00ad01c8`](#insn-00ad01c8)
- ブロック [`00ad01c8`](#insn-00ad01c8) 範囲 `[['00ad01c8', '00ad01cb']]`
  - `CONDITIONAL_JUMP` [`00ad01c8`](#insn-00ad01c8) → [`00ad0038`](#insn-00ad0038)
  - `FALL_THROUGH` [`00ad01c8`](#insn-00ad01c8) → [`00ad01cc`](#insn-00ad01cc)
- ブロック [`00ad01cc`](#insn-00ad01cc) 範囲 `[['00ad01cc', '00ad01db']]`
  - `CONDITIONAL_JUMP` [`00ad01d8`](#insn-00ad01d8) → [`00ad0038`](#insn-00ad0038)
  - `FALL_THROUGH` [`00ad01d8`](#insn-00ad01d8) → [`00ad01dc`](#insn-00ad01dc)
- ブロック [`00ad01dc`](#insn-00ad01dc) 範囲 `[['00ad01dc', '00ad01f7']]`
  - `UNCONDITIONAL_JUMP` [`00ad01f4`](#insn-00ad01f4) → [`00ad0038`](#insn-00ad0038)
- ブロック [`00ad01f8`](#insn-00ad01f8) 範囲 `[['00ad01f8', '00ad0203']]`
  - `CONDITIONAL_JUMP` [`00ad0200`](#insn-00ad0200) → [`00ad020c`](#insn-00ad020c)
  - `FALL_THROUGH` [`00ad0200`](#insn-00ad0200) → [`00ad0204`](#insn-00ad0204)
- ブロック [`00ad0204`](#insn-00ad0204) 範囲 `[['00ad0204', '00ad020b']]`
  - `FALL_THROUGH` [`00ad0208`](#insn-00ad0208) → [`00ad020c`](#insn-00ad020c)
- ブロック [`00ad020c`](#insn-00ad020c) 範囲 `[['00ad020c', '00ad0217']]`
  - `CONDITIONAL_JUMP` [`00ad0214`](#insn-00ad0214) → [`00ad003c`](#insn-00ad003c)
  - `FALL_THROUGH` [`00ad0214`](#insn-00ad0214) → [`00ad0218`](#insn-00ad0218)
- ブロック [`00ad0218`](#insn-00ad0218) 範囲 `[['00ad0218', '00ad021f']]`
  - `CONDITIONAL_JUMP` [`00ad021c`](#insn-00ad021c) → [`00ad003c`](#insn-00ad003c)
  - `FALL_THROUGH` [`00ad021c`](#insn-00ad021c) → [`00ad0220`](#insn-00ad0220)
- ブロック [`00ad0220`](#insn-00ad0220) 範囲 `[['00ad0220', '00ad0227']]`
  - `UNCONDITIONAL_JUMP` [`00ad0224`](#insn-00ad0224) → [`00ad023c`](#insn-00ad023c)
- ブロック [`00ad0228`](#insn-00ad0228) 範囲 `[['00ad0228', '00ad0233']]`
  - `CONDITIONAL_JUMP` [`00ad0230`](#insn-00ad0230) → [`00ad0274`](#insn-00ad0274)
  - `FALL_THROUGH` [`00ad0230`](#insn-00ad0230) → [`00ad0234`](#insn-00ad0234)
- ブロック [`00ad0234`](#insn-00ad0234) 範囲 `[['00ad0234', '00ad023b']]`
  - `CONDITIONAL_JUMP` [`00ad0238`](#insn-00ad0238) → [`00ad003c`](#insn-00ad003c)
  - `FALL_THROUGH` [`00ad0238`](#insn-00ad0238) → [`00ad023c`](#insn-00ad023c)
- ブロック [`00ad023c`](#insn-00ad023c) 範囲 `[['00ad023c', '00ad0247']]`
  - `CONDITIONAL_JUMP` [`00ad0244`](#insn-00ad0244) → [`00ad0228`](#insn-00ad0228)
  - `FALL_THROUGH` [`00ad0244`](#insn-00ad0244) → [`00ad0248`](#insn-00ad0248)
- ブロック [`00ad0248`](#insn-00ad0248) 範囲 `[['00ad0248', '00ad024f']]`
  - `CONDITIONAL_JUMP` [`00ad024c`](#insn-00ad024c) → [`00ad0258`](#insn-00ad0258)
  - `FALL_THROUGH` [`00ad024c`](#insn-00ad024c) → [`00ad0250`](#insn-00ad0250)
- ブロック [`00ad0250`](#insn-00ad0250) 範囲 `[['00ad0250', '00ad0257']]`
  - `UNCONDITIONAL_JUMP` [`00ad0254`](#insn-00ad0254) → [`00ad0268`](#insn-00ad0268)
- ブロック [`00ad0258`](#insn-00ad0258) 範囲 `[['00ad0258', '00ad025f']]`
  - `CONDITIONAL_JUMP` [`00ad025c`](#insn-00ad025c) → [`00ad0268`](#insn-00ad0268)
  - `FALL_THROUGH` [`00ad025c`](#insn-00ad025c) → [`00ad0260`](#insn-00ad0260)
- ブロック [`00ad0260`](#insn-00ad0260) 範囲 `[['00ad0260', '00ad0267']]`
  - `FALL_THROUGH` [`00ad0264`](#insn-00ad0264) → [`00ad0268`](#insn-00ad0268)
- ブロック [`00ad0268`](#insn-00ad0268) 範囲 `[['00ad0268', '00ad026f']]`
  - `CONDITIONAL_JUMP` [`00ad026c`](#insn-00ad026c) → [`00ad0234`](#insn-00ad0234)
  - `FALL_THROUGH` [`00ad026c`](#insn-00ad026c) → [`00ad0270`](#insn-00ad0270)
- ブロック [`00ad0270`](#insn-00ad0270) 範囲 `[['00ad0270', '00ad0273']]`
  - `UNCONDITIONAL_JUMP` [`00ad0270`](#insn-00ad0270) → [`00ad003c`](#insn-00ad003c)
- ブロック [`00ad0274`](#insn-00ad0274) 範囲 `[['00ad0274', '00ad028f']]`
  - `CONDITIONAL_JUMP` [`00ad028c`](#insn-00ad028c) → [`00ad003c`](#insn-00ad003c)
  - `FALL_THROUGH` [`00ad028c`](#insn-00ad028c) → [`00ad0290`](#insn-00ad0290)
- ブロック [`00ad0290`](#insn-00ad0290) 範囲 `[['00ad0290', '00ad029f']]`
  - `CONDITIONAL_JUMP` [`00ad029c`](#insn-00ad029c) → [`00ad003c`](#insn-00ad003c)
  - `FALL_THROUGH` [`00ad029c`](#insn-00ad029c) → [`00ad02a0`](#insn-00ad02a0)
- ブロック [`00ad02a0`](#insn-00ad02a0) 範囲 `[['00ad02a0', '00ad02bb']]`
  - `UNCONDITIONAL_JUMP` [`00ad02b8`](#insn-00ad02b8) → [`00ad003c`](#insn-00ad003c)
- ブロック [`00ad02bc`](#insn-00ad02bc) 範囲 `[['00ad02bc', '00ad02cb']]`
  - `CONDITIONAL_JUMP` [`00ad02c8`](#insn-00ad02c8) → [`00ad0310`](#insn-00ad0310)
  - `FALL_THROUGH` [`00ad02c8`](#insn-00ad02c8) → [`00ad02cc`](#insn-00ad02cc)
- ブロック [`00ad02cc`](#insn-00ad02cc) 範囲 `[['00ad02cc', '00ad02cf']]`
  - `FALL_THROUGH` [`00ad02cc`](#insn-00ad02cc) → [`00ad02d0`](#insn-00ad02d0)
- ブロック [`00ad02d0`](#insn-00ad02d0) 範囲 `[['00ad02d0', '00ad02d7']]`
  - `CONDITIONAL_JUMP` [`00ad02d4`](#insn-00ad02d4) → [`00ad02dc`](#insn-00ad02dc)
  - `FALL_THROUGH` [`00ad02d4`](#insn-00ad02d4) → [`00ad02d8`](#insn-00ad02d8)
- ブロック [`00ad02d8`](#insn-00ad02d8) 範囲 `[['00ad02d8', '00ad02db']]`
  - `FALL_THROUGH` [`00ad02d8`](#insn-00ad02d8) → [`00ad02dc`](#insn-00ad02dc)
- ブロック [`00ad02dc`](#insn-00ad02dc) 範囲 `[['00ad02dc', '00ad02e7']]`
  - `FALL_THROUGH` [`00ad02e4`](#insn-00ad02e4) → [`00ad02e8`](#insn-00ad02e8)
- ブロック [`00ad02e8`](#insn-00ad02e8) 範囲 `[['00ad02e8', '00ad02eb']]`
  - `FALL_THROUGH` [`00ad02e8`](#insn-00ad02e8) → [`00ad02ec`](#insn-00ad02ec)
- ブロック [`00ad02ec`](#insn-00ad02ec) 範囲 `[['00ad02ec', '00ad02ef']]`
  - `CONDITIONAL_JUMP` [`00ad02ec`](#insn-00ad02ec) → [`00ad039c`](#insn-00ad039c)
  - `FALL_THROUGH` [`00ad02ec`](#insn-00ad02ec) → [`00ad02f0`](#insn-00ad02f0)
- ブロック [`00ad02f0`](#insn-00ad02f0) 範囲 `[['00ad02f0', '00ad02f3']]`
  - `FALL_THROUGH` [`00ad02f0`](#insn-00ad02f0) → [`00ad02f4`](#insn-00ad02f4)
- ブロック [`00ad02f4`](#insn-00ad02f4) 範囲 `[['00ad02f4', '00ad02f7']]`
  - `FALL_THROUGH` [`00ad02f4`](#insn-00ad02f4) → [`00ad02f8`](#insn-00ad02f8)
- ブロック [`00ad02f8`](#insn-00ad02f8) 範囲 `[['00ad02f8', '00ad030f']]`
- ブロック [`00ad0310`](#insn-00ad0310) 範囲 `[['00ad0310', '00ad031f']]`
  - `CONDITIONAL_JUMP` [`00ad031c`](#insn-00ad031c) → [`00ad02cc`](#insn-00ad02cc)
  - `FALL_THROUGH` [`00ad031c`](#insn-00ad031c) → [`00ad0320`](#insn-00ad0320)
- ブロック [`00ad0320`](#insn-00ad0320) 範囲 `[['00ad0320', '00ad0367']]`
  - `UNCONDITIONAL_JUMP` [`00ad0364`](#insn-00ad0364) → [`00ad02cc`](#insn-00ad02cc)
- ブロック [`00ad039c`](#insn-00ad039c) 範囲 `[['00ad039c', '00ad039f']]`

## 命令位置別の参照

- [`00acfcc4`](#insn-00acfcc4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcc8`](#insn-00acfcc8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfccc`](#insn-00acfccc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcd0`](#insn-00acfcd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcd4`](#insn-00acfcd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcd8`](#insn-00acfcd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcec`](#insn-00acfcec) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcf8`](#insn-00acfcf8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd00`](#insn-00acfd00) → `00333a28`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acfd04`](#insn-00acfd04) → [`00acfd14`](#insn-00acfd14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd08`](#insn-00acfd08) → `00ca4620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acfd10`](#insn-00acfd10) → [`00ad02bc`](#insn-00ad02bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd18`](#insn-00acfd18) → `00ca4620`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acfd1c`](#insn-00acfd1c) → `00ca4978`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfd20`](#insn-00acfd20) → [`00acfd44`](#insn-00acfd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd28`](#insn-00acfd28) → `00c65e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00acfd30`](#insn-00acfd30) → `00c8d950`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00acfd38`](#insn-00acfd38) → [`00c58610`](../00c58/00c58610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58610` · 推定シンボル `None` · 推定型 `None`
- [`00acfd40`](#insn-00acfd40) → [`00acfd48`](#insn-00acfd48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd48`](#insn-00acfd48) → `00333f4c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acfd50`](#insn-00acfd50) → [`00ad02bc`](#insn-00ad02bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd78`](#insn-00acfd78) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd88`](#insn-00acfd88) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd94`](#insn-00acfd94) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd98`](#insn-00acfd98) → [`00acfdac`](#insn-00acfdac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfda8`](#insn-00acfda8) → [`00ad0014`](#insn-00ad0014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdf0`](#insn-00acfdf0) → [`00acfda0`](#insn-00acfda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdf8`](#insn-00acfdf8) → [`00acfe98`](#insn-00acfe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdfc`](#insn-00acfdfc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe04`](#insn-00acfe04) → [`00acfe98`](#insn-00acfe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe10`](#insn-00acfe10) → `00ca4f38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acfe14`](#insn-00acfe14) → [`00acffbc`](#insn-00acffbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe68`](#insn-00acfe68) → [`009e0fc0`](../009e0/009e0fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e0fc0` · 推定シンボル `None` · 推定型 `None`
- [`00acfe6c`](#insn-00acfe6c) → [`00acfeb0`](#insn-00acfeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe7c`](#insn-00acfe7c) → [`009e2f94`](../009e2/009e2f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e2f94` · 推定シンボル `None` · 推定型 `None`
- [`00acfe80`](#insn-00acfe80) → [`00acfeb0`](#insn-00acfeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe88`](#insn-00acfe88) → [`009df634`](../009df/009df634.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009df634` · 推定シンボル `None` · 推定型 `None`
- [`00acfe8c`](#insn-00acfe8c) → [`00acfeb0`](#insn-00acfeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe94`](#insn-00acfe94) → [`00acfeb8`](#insn-00acfeb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe98`](#insn-00acfe98) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe9c`](#insn-00acfe9c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfea8`](#insn-00acfea8) → [`009a2b34`](../009a2/009a2b34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a2b34` · 推定シンボル `None` · 推定型 `None`
- [`00acfeac`](#insn-00acfeac) → [`00acff88`](#insn-00acff88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfeb0`](#insn-00acfeb0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfebc`](#insn-00acfebc) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfed4`](#insn-00acfed4) → `00c9aca0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acfed4`](#insn-00acfed4) → `00ca4fd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acfee0`](#insn-00acfee0) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfef4`](#insn-00acfef4) → [`006337e4`](../00633/006337e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006337e4` · 推定シンボル `None` · 推定型 `None`
- [`00acfef8`](#insn-00acfef8) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfefc`](#insn-00acfefc) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff00`](#insn-00acff00) → [`00acff7c`](#insn-00acff7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff08`](#insn-00acff08) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff20`](#insn-00acff20) → `002c86f5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff24`](#insn-00acff24) → [`00695bac`](../00695/00695bac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00695bac` · 推定シンボル `None` · 推定型 `None`
- [`00acff28`](#insn-00acff28) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff30`](#insn-00acff30) → [`00acff40`](#insn-00acff40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff3c`](#insn-00acff3c) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`00acff48`](#insn-00acff48) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff4c`](#insn-00acff4c) → [`00acff88`](#insn-00acff88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff58`](#insn-00acff58) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00acff5c`](#insn-00acff5c) → [`00acff88`](#insn-00acff88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff74`](#insn-00acff74) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00acff78`](#insn-00acff78) → [`00acff88`](#insn-00acff88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff84`](#insn-00acff84) → [`009a2b34`](../009a2/009a2b34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a2b34` · 推定シンボル `None` · 推定型 `None`
- [`00acff88`](#insn-00acff88) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff8c`](#insn-00acff8c) → [`00acfd9c`](#insn-00acfd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff98`](#insn-00acff98) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00acff9c`](#insn-00acff9c) → [`00acfd9c`](#insn-00acfd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffb4`](#insn-00acffb4) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00acffb8`](#insn-00acffb8) → [`00acfd9c`](#insn-00acfd9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffc0`](#insn-00acffc0) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acffc4`](#insn-00acffc4) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00acffc8`](#insn-00acffc8) → [`00acfe18`](#insn-00acfe18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffd0`](#insn-00acffd0) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acffd8`](#insn-00acffd8) → [`0047edb4`](../0047e/0047edb4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edb4` · 推定シンボル `None` · 推定型 `None`
- [`00acffe4`](#insn-00acffe4) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acffe8`](#insn-00acffe8) → `00ca4f08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acffec`](#insn-00acffec) → `00ca4f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acffec`](#insn-00acffec) → `00ca4f08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfff4`](#insn-00acfff4) → `00ca4f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfff4`](#insn-00acfff4) → `00ca4f30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfff8`](#insn-00acfff8) → `00ca4f20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfffc`](#insn-00acfffc) → `00ca4f10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfffc`](#insn-00acfffc) → `00ca4f18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acfffc`](#insn-00acfffc) → `00ca4f20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0000`](#insn-00ad0000) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`00ad0008`](#insn-00ad0008) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ad000c`](#insn-00ad000c) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00ad0010`](#insn-00ad0010) → [`00acfe18`](#insn-00acfe18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad001c`](#insn-00ad001c) → `00335f78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad0020`](#insn-00ad0020) → [`00ad02bc`](#insn-00ad02bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0034`](#insn-00ad0034) → [`00ad0054`](#insn-00ad0054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0038`](#insn-00ad0038) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0044`](#insn-00ad0044) → `00335f78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad0050`](#insn-00ad0050) → [`00ad02bc`](#insn-00ad02bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0058`](#insn-00ad0058) → [`00ad00ec`](#insn-00ad00ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad005c`](#insn-00ad005c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0064`](#insn-00ad0064) → [`00ad00ec`](#insn-00ad00ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0068`](#insn-00ad0068) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00bc`](#insn-00ad00bc) → [`009e0fc0`](../009e0/009e0fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e0fc0` · 推定シンボル `None` · 推定型 `None`
- [`00ad00c0`](#insn-00ad00c0) → [`00ad0120`](#insn-00ad0120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00d0`](#insn-00ad00d0) → [`009e2f94`](../009e2/009e2f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e2f94` · 推定シンボル `None` · 推定型 `None`
- [`00ad00d4`](#insn-00ad00d4) → [`00ad0120`](#insn-00ad0120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00dc`](#insn-00ad00dc) → [`009df634`](../009df/009df634.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009df634` · 推定シンボル `None` · 推定型 `None`
- [`00ad00e0`](#insn-00ad00e0) → [`00ad0120`](#insn-00ad0120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00e8`](#insn-00ad00e8) → [`00ad0128`](#insn-00ad0128) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00f0`](#insn-00ad00f0) → [`00ad003c`](#insn-00ad003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad010c`](#insn-00ad010c) → [`00ad01f8`](#insn-00ad01f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad011c`](#insn-00ad011c) → [`00ad020c`](#insn-00ad020c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0120`](#insn-00ad0120) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0134`](#insn-00ad0134) → [`00666c28`](../00666/00666c28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00666c28` · 推定シンボル `None` · 推定型 `None`
- [`00ad0138`](#insn-00ad0138) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0140`](#insn-00ad0140) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0144`](#insn-00ad0144) → [`00ad01b8`](#insn-00ad01b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad014c`](#insn-00ad014c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0160`](#insn-00ad0160) → `002c86f5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0164`](#insn-00ad0164) → [`00695bac`](../00695/00695bac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00695bac` · 推定シンボル `None` · 推定型 `None`
- [`00ad0168`](#insn-00ad0168) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0170`](#insn-00ad0170) → [`00ad0180`](#insn-00ad0180) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad017c`](#insn-00ad017c) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`00ad0188`](#insn-00ad0188) → [`00ad01c4`](#insn-00ad01c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0194`](#insn-00ad0194) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00ad0198`](#insn-00ad0198) → [`00ad01c4`](#insn-00ad01c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad01b0`](#insn-00ad01b0) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00ad01b4`](#insn-00ad01b4) → [`00ad01c4`](#insn-00ad01c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad01c0`](#insn-00ad01c0) → [`009a2b34`](../009a2/009a2b34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a2b34` · 推定シンボル `None` · 推定型 `None`
- [`00ad01c4`](#insn-00ad01c4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad01c8`](#insn-00ad01c8) → [`00ad0038`](#insn-00ad0038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad01d4`](#insn-00ad01d4) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00ad01d8`](#insn-00ad01d8) → [`00ad0038`](#insn-00ad0038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad01f0`](#insn-00ad01f0) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00ad01f4`](#insn-00ad01f4) → [`00ad0038`](#insn-00ad0038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0200`](#insn-00ad0200) → [`00ad020c`](#insn-00ad020c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0214`](#insn-00ad0214) → [`00ad003c`](#insn-00ad003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad021c`](#insn-00ad021c) → [`00ad003c`](#insn-00ad003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0224`](#insn-00ad0224) → [`00ad023c`](#insn-00ad023c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0230`](#insn-00ad0230) → [`00ad0274`](#insn-00ad0274) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0238`](#insn-00ad0238) → [`00ad003c`](#insn-00ad003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0244`](#insn-00ad0244) → [`00ad0228`](#insn-00ad0228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad024c`](#insn-00ad024c) → [`00ad0258`](#insn-00ad0258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0254`](#insn-00ad0254) → [`00ad0268`](#insn-00ad0268) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad025c`](#insn-00ad025c) → [`00ad0268`](#insn-00ad0268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad026c`](#insn-00ad026c) → [`00ad0234`](#insn-00ad0234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0270`](#insn-00ad0270) → [`00ad003c`](#insn-00ad003c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0274`](#insn-00ad0274) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0278`](#insn-00ad0278) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0284`](#insn-00ad0284) → [`009a2b34`](../009a2/009a2b34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a2b34` · 推定シンボル `None` · 推定型 `None`
- [`00ad0288`](#insn-00ad0288) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad028c`](#insn-00ad028c) → [`00ad003c`](#insn-00ad003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0298`](#insn-00ad0298) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00ad029c`](#insn-00ad029c) → [`00ad003c`](#insn-00ad003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad02b4`](#insn-00ad02b4) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00ad02b8`](#insn-00ad02b8) → [`00ad003c`](#insn-00ad003c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad02c4`](#insn-00ad02c4) → `00ca4f38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ad02c8`](#insn-00ad02c8) → [`00ad0310`](#insn-00ad0310) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad02d0`](#insn-00ad02d0) → `00ca4f30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad02d4`](#insn-00ad02d4) → [`00ad02dc`](#insn-00ad02dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad02d8`](#insn-00ad02d8) → [`004981d0`](../00498/004981d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004981d0` · 推定シンボル `None` · 推定型 `None`
- [`00ad02dc`](#insn-00ad02dc) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad02e4`](#insn-00ad02e4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad02ec`](#insn-00ad02ec) → [`00ad039c`](#insn-00ad039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad02f0`](#insn-00ad02f0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad02f4`](#insn-00ad02f4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad02f8`](#insn-00ad02f8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad02fc`](#insn-00ad02fc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0300`](#insn-00ad0300) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0304`](#insn-00ad0304) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0314`](#insn-00ad0314) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ad0318`](#insn-00ad0318) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00ad031c`](#insn-00ad031c) → [`00ad02cc`](#insn-00ad02cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0324`](#insn-00ad0324) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad032c`](#insn-00ad032c) → [`0047edb4`](../0047e/0047edb4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edb4` · 推定シンボル `None` · 推定型 `None`
- [`00ad0338`](#insn-00ad0338) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ad033c`](#insn-00ad033c) → `00ca4f08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0340`](#insn-00ad0340) → `00ca4f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0340`](#insn-00ad0340) → `00ca4f08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0348`](#insn-00ad0348) → `00ca4f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0348`](#insn-00ad0348) → `00ca4f30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad034c`](#insn-00ad034c) → `00ca4f20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0350`](#insn-00ad0350) → `00ca4f10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0350`](#insn-00ad0350) → `00ca4f18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0350`](#insn-00ad0350) → `00ca4f20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad0354`](#insn-00ad0354) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`00ad035c`](#insn-00ad035c) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ad0360`](#insn-00ad0360) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00ad0364`](#insn-00ad0364) → [`00ad02cc`](#insn-00ad02cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad039c`](#insn-00ad039c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfcc4`](#insn-00acfcc4)

~~~json
{
  "source": "00acfcc4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcc8`](#insn-00acfcc8)

~~~json
{
  "source": "00acfcc8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfccc`](#insn-00acfccc)

~~~json
{
  "source": "00acfccc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcd0`](#insn-00acfcd0)

~~~json
{
  "source": "00acfcd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcd4`](#insn-00acfcd4)

~~~json
{
  "source": "00acfcd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcd8`](#insn-00acfcd8)

~~~json
{
  "source": "00acfcd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcec`](#insn-00acfcec)

~~~json
{
  "source": "00acfcec",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcf8`](#insn-00acfcf8)

~~~json
{
  "source": "00acfcf8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd00`](#insn-00acfd00)

~~~json
{
  "source": "00acfd00",
  "target": "00333a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a28",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "a0c36a00bc790900",
  "capture_start": "00333a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acfd04`](#insn-00acfd04)

~~~json
{
  "source": "00acfd04",
  "target": "00acfd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd08`](#insn-00acfd08)

~~~json
{
  "source": "00acfd08",
  "target": "00ca4620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4620",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfd10`](#insn-00acfd10)

~~~json
{
  "source": "00acfd10",
  "target": "00ad02bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd18`](#insn-00acfd18)

~~~json
{
  "source": "00acfd18",
  "target": "00ca4620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4620",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfd1c`](#insn-00acfd1c)

~~~json
{
  "source": "00acfd1c",
  "target": "00ca4978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4978",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfd20`](#insn-00acfd20)

~~~json
{
  "source": "00acfd20",
  "target": "00acfd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd28`](#insn-00acfd28)

~~~json
{
  "source": "00acfd28",
  "target": "00c65e58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65e58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acfd30`](#insn-00acfd30)

~~~json
{
  "source": "00acfd30",
  "target": "00c8d950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d950",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acfd38`](#insn-00acfd38)

~~~json
{
  "source": "00acfd38",
  "target": "00c58610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd40`](#insn-00acfd40)

~~~json
{
  "source": "00acfd40",
  "target": "00acfd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd48`](#insn-00acfd48)

~~~json
{
  "source": "00acfd48",
  "target": "00333f4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f48",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8a66c00d48c0900",
  "capture_start": "00333f48",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acfd50`](#insn-00acfd50)

~~~json
{
  "source": "00acfd50",
  "target": "00ad02bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd78`](#insn-00acfd78)

~~~json
{
  "source": "00acfd78",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd88`](#insn-00acfd88)

~~~json
{
  "source": "00acfd88",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd94`](#insn-00acfd94)

~~~json
{
  "source": "00acfd94",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd98`](#insn-00acfd98)

~~~json
{
  "source": "00acfd98",
  "target": "00acfdac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfda8`](#insn-00acfda8)

~~~json
{
  "source": "00acfda8",
  "target": "00ad0014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdf0`](#insn-00acfdf0)

~~~json
{
  "source": "00acfdf0",
  "target": "00acfda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdf8`](#insn-00acfdf8)

~~~json
{
  "source": "00acfdf8",
  "target": "00acfe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdfc`](#insn-00acfdfc)

~~~json
{
  "source": "00acfdfc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe04`](#insn-00acfe04)

~~~json
{
  "source": "00acfe04",
  "target": "00acfe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe10`](#insn-00acfe10)

~~~json
{
  "source": "00acfe10",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfe14`](#insn-00acfe14)

~~~json
{
  "source": "00acfe14",
  "target": "00acffbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe68`](#insn-00acfe68)

~~~json
{
  "source": "00acfe68",
  "target": "009e0fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfe6c`](#insn-00acfe6c)

~~~json
{
  "source": "00acfe6c",
  "target": "00acfeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe7c`](#insn-00acfe7c)

~~~json
{
  "source": "00acfe7c",
  "target": "009e2f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfe80`](#insn-00acfe80)

~~~json
{
  "source": "00acfe80",
  "target": "00acfeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe88`](#insn-00acfe88)

~~~json
{
  "source": "00acfe88",
  "target": "009df634",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfe8c`](#insn-00acfe8c)

~~~json
{
  "source": "00acfe8c",
  "target": "00acfeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe94`](#insn-00acfe94)

~~~json
{
  "source": "00acfe94",
  "target": "00acfeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe98`](#insn-00acfe98)

~~~json
{
  "source": "00acfe98",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe9c`](#insn-00acfe9c)

~~~json
{
  "source": "00acfe9c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfea8`](#insn-00acfea8)

~~~json
{
  "source": "00acfea8",
  "target": "009a2b34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfeac`](#insn-00acfeac)

~~~json
{
  "source": "00acfeac",
  "target": "00acff88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfeb0`](#insn-00acfeb0)

~~~json
{
  "source": "00acfeb0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfebc`](#insn-00acfebc)

~~~json
{
  "source": "00acfebc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfed4`](#insn-00acfed4)

~~~json
{
  "source": "00acfed4",
  "target": "00c9aca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aca0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acfed4`](#insn-00acfed4)

~~~json
{
  "source": "00acfed4",
  "target": "00ca4fd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4fd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfee0`](#insn-00acfee0)

~~~json
{
  "source": "00acfee0",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfef4`](#insn-00acfef4)

~~~json
{
  "source": "00acfef4",
  "target": "006337e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfef8`](#insn-00acfef8)

~~~json
{
  "source": "00acfef8",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfefc`](#insn-00acfefc)

~~~json
{
  "source": "00acfefc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff00`](#insn-00acff00)

~~~json
{
  "source": "00acff00",
  "target": "00acff7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff08`](#insn-00acff08)

~~~json
{
  "source": "00acff08",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff20`](#insn-00acff20)

~~~json
{
  "source": "00acff20",
  "target": "002c86f5",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff24`](#insn-00acff24)

~~~json
{
  "source": "00acff24",
  "target": "00695bac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff28`](#insn-00acff28)

~~~json
{
  "source": "00acff28",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff30`](#insn-00acff30)

~~~json
{
  "source": "00acff30",
  "target": "00acff40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff3c`](#insn-00acff3c)

~~~json
{
  "source": "00acff3c",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff48`](#insn-00acff48)

~~~json
{
  "source": "00acff48",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff4c`](#insn-00acff4c)

~~~json
{
  "source": "00acff4c",
  "target": "00acff88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff58`](#insn-00acff58)

~~~json
{
  "source": "00acff58",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff5c`](#insn-00acff5c)

~~~json
{
  "source": "00acff5c",
  "target": "00acff88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff74`](#insn-00acff74)

~~~json
{
  "source": "00acff74",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff78`](#insn-00acff78)

~~~json
{
  "source": "00acff78",
  "target": "00acff88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff84`](#insn-00acff84)

~~~json
{
  "source": "00acff84",
  "target": "009a2b34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff88`](#insn-00acff88)

~~~json
{
  "source": "00acff88",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff8c`](#insn-00acff8c)

~~~json
{
  "source": "00acff8c",
  "target": "00acfd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff98`](#insn-00acff98)

~~~json
{
  "source": "00acff98",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff9c`](#insn-00acff9c)

~~~json
{
  "source": "00acff9c",
  "target": "00acfd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffb4`](#insn-00acffb4)

~~~json
{
  "source": "00acffb4",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acffb8`](#insn-00acffb8)

~~~json
{
  "source": "00acffb8",
  "target": "00acfd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffc0`](#insn-00acffc0)

~~~json
{
  "source": "00acffc0",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acffc4`](#insn-00acffc4)

~~~json
{
  "source": "00acffc4",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acffc8`](#insn-00acffc8)

~~~json
{
  "source": "00acffc8",
  "target": "00acfe18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffd0`](#insn-00acffd0)

~~~json
{
  "source": "00acffd0",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acffd8`](#insn-00acffd8)

~~~json
{
  "source": "00acffd8",
  "target": "0047edb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acffe4`](#insn-00acffe4)

~~~json
{
  "source": "00acffe4",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acffe8`](#insn-00acffe8)

~~~json
{
  "source": "00acffe8",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acffec`](#insn-00acffec)

~~~json
{
  "source": "00acffec",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acffec`](#insn-00acffec)

~~~json
{
  "source": "00acffec",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfff4`](#insn-00acfff4)

~~~json
{
  "source": "00acfff4",
  "target": "00ca4f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfff4`](#insn-00acfff4)

~~~json
{
  "source": "00acfff4",
  "target": "00ca4f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfff8`](#insn-00acfff8)

~~~json
{
  "source": "00acfff8",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfffc`](#insn-00acfffc)

~~~json
{
  "source": "00acfffc",
  "target": "00ca4f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfffc`](#insn-00acfffc)

~~~json
{
  "source": "00acfffc",
  "target": "00ca4f18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfffc`](#insn-00acfffc)

~~~json
{
  "source": "00acfffc",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0000`](#insn-00ad0000)

~~~json
{
  "source": "00ad0000",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0008`](#insn-00ad0008)

~~~json
{
  "source": "00ad0008",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad000c`](#insn-00ad000c)

~~~json
{
  "source": "00ad000c",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0010`](#insn-00ad0010)

~~~json
{
  "source": "00ad0010",
  "target": "00acfe18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad001c`](#insn-00ad001c)

~~~json
{
  "source": "00ad001c",
  "target": "00335f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f78",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "747f750068ff0900",
  "capture_start": "00335f78",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad0020`](#insn-00ad0020)

~~~json
{
  "source": "00ad0020",
  "target": "00ad02bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0034`](#insn-00ad0034)

~~~json
{
  "source": "00ad0034",
  "target": "00ad0054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0038`](#insn-00ad0038)

~~~json
{
  "source": "00ad0038",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0044`](#insn-00ad0044)

~~~json
{
  "source": "00ad0044",
  "target": "00335f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f78",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "747f750068ff0900",
  "capture_start": "00335f78",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad0050`](#insn-00ad0050)

~~~json
{
  "source": "00ad0050",
  "target": "00ad02bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0058`](#insn-00ad0058)

~~~json
{
  "source": "00ad0058",
  "target": "00ad00ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad005c`](#insn-00ad005c)

~~~json
{
  "source": "00ad005c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0064`](#insn-00ad0064)

~~~json
{
  "source": "00ad0064",
  "target": "00ad00ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0068`](#insn-00ad0068)

~~~json
{
  "source": "00ad0068",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00bc`](#insn-00ad00bc)

~~~json
{
  "source": "00ad00bc",
  "target": "009e0fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad00c0`](#insn-00ad00c0)

~~~json
{
  "source": "00ad00c0",
  "target": "00ad0120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00d0`](#insn-00ad00d0)

~~~json
{
  "source": "00ad00d0",
  "target": "009e2f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad00d4`](#insn-00ad00d4)

~~~json
{
  "source": "00ad00d4",
  "target": "00ad0120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00dc`](#insn-00ad00dc)

~~~json
{
  "source": "00ad00dc",
  "target": "009df634",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad00e0`](#insn-00ad00e0)

~~~json
{
  "source": "00ad00e0",
  "target": "00ad0120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00e8`](#insn-00ad00e8)

~~~json
{
  "source": "00ad00e8",
  "target": "00ad0128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00f0`](#insn-00ad00f0)

~~~json
{
  "source": "00ad00f0",
  "target": "00ad003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad010c`](#insn-00ad010c)

~~~json
{
  "source": "00ad010c",
  "target": "00ad01f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad011c`](#insn-00ad011c)

~~~json
{
  "source": "00ad011c",
  "target": "00ad020c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0120`](#insn-00ad0120)

~~~json
{
  "source": "00ad0120",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0134`](#insn-00ad0134)

~~~json
{
  "source": "00ad0134",
  "target": "00666c28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0138`](#insn-00ad0138)

~~~json
{
  "source": "00ad0138",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0140`](#insn-00ad0140)

~~~json
{
  "source": "00ad0140",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0144`](#insn-00ad0144)

~~~json
{
  "source": "00ad0144",
  "target": "00ad01b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad014c`](#insn-00ad014c)

~~~json
{
  "source": "00ad014c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0160`](#insn-00ad0160)

~~~json
{
  "source": "00ad0160",
  "target": "002c86f5",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0164`](#insn-00ad0164)

~~~json
{
  "source": "00ad0164",
  "target": "00695bac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0168`](#insn-00ad0168)

~~~json
{
  "source": "00ad0168",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0170`](#insn-00ad0170)

~~~json
{
  "source": "00ad0170",
  "target": "00ad0180",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad017c`](#insn-00ad017c)

~~~json
{
  "source": "00ad017c",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0188`](#insn-00ad0188)

~~~json
{
  "source": "00ad0188",
  "target": "00ad01c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0194`](#insn-00ad0194)

~~~json
{
  "source": "00ad0194",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0198`](#insn-00ad0198)

~~~json
{
  "source": "00ad0198",
  "target": "00ad01c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad01b0`](#insn-00ad01b0)

~~~json
{
  "source": "00ad01b0",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad01b4`](#insn-00ad01b4)

~~~json
{
  "source": "00ad01b4",
  "target": "00ad01c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad01c0`](#insn-00ad01c0)

~~~json
{
  "source": "00ad01c0",
  "target": "009a2b34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad01c4`](#insn-00ad01c4)

~~~json
{
  "source": "00ad01c4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad01c8`](#insn-00ad01c8)

~~~json
{
  "source": "00ad01c8",
  "target": "00ad0038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad01d4`](#insn-00ad01d4)

~~~json
{
  "source": "00ad01d4",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad01d8`](#insn-00ad01d8)

~~~json
{
  "source": "00ad01d8",
  "target": "00ad0038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad01f0`](#insn-00ad01f0)

~~~json
{
  "source": "00ad01f0",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad01f4`](#insn-00ad01f4)

~~~json
{
  "source": "00ad01f4",
  "target": "00ad0038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0200`](#insn-00ad0200)

~~~json
{
  "source": "00ad0200",
  "target": "00ad020c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0214`](#insn-00ad0214)

~~~json
{
  "source": "00ad0214",
  "target": "00ad003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad021c`](#insn-00ad021c)

~~~json
{
  "source": "00ad021c",
  "target": "00ad003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0224`](#insn-00ad0224)

~~~json
{
  "source": "00ad0224",
  "target": "00ad023c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0230`](#insn-00ad0230)

~~~json
{
  "source": "00ad0230",
  "target": "00ad0274",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0238`](#insn-00ad0238)

~~~json
{
  "source": "00ad0238",
  "target": "00ad003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0244`](#insn-00ad0244)

~~~json
{
  "source": "00ad0244",
  "target": "00ad0228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad024c`](#insn-00ad024c)

~~~json
{
  "source": "00ad024c",
  "target": "00ad0258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0254`](#insn-00ad0254)

~~~json
{
  "source": "00ad0254",
  "target": "00ad0268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad025c`](#insn-00ad025c)

~~~json
{
  "source": "00ad025c",
  "target": "00ad0268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad026c`](#insn-00ad026c)

~~~json
{
  "source": "00ad026c",
  "target": "00ad0234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0270`](#insn-00ad0270)

~~~json
{
  "source": "00ad0270",
  "target": "00ad003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0274`](#insn-00ad0274)

~~~json
{
  "source": "00ad0274",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0278`](#insn-00ad0278)

~~~json
{
  "source": "00ad0278",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0284`](#insn-00ad0284)

~~~json
{
  "source": "00ad0284",
  "target": "009a2b34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0288`](#insn-00ad0288)

~~~json
{
  "source": "00ad0288",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad028c`](#insn-00ad028c)

~~~json
{
  "source": "00ad028c",
  "target": "00ad003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0298`](#insn-00ad0298)

~~~json
{
  "source": "00ad0298",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad029c`](#insn-00ad029c)

~~~json
{
  "source": "00ad029c",
  "target": "00ad003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad02b4`](#insn-00ad02b4)

~~~json
{
  "source": "00ad02b4",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad02b8`](#insn-00ad02b8)

~~~json
{
  "source": "00ad02b8",
  "target": "00ad003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad02c4`](#insn-00ad02c4)

~~~json
{
  "source": "00ad02c4",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad02c8`](#insn-00ad02c8)

~~~json
{
  "source": "00ad02c8",
  "target": "00ad0310",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad02d0`](#insn-00ad02d0)

~~~json
{
  "source": "00ad02d0",
  "target": "00ca4f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad02d4`](#insn-00ad02d4)

~~~json
{
  "source": "00ad02d4",
  "target": "00ad02dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad02d8`](#insn-00ad02d8)

~~~json
{
  "source": "00ad02d8",
  "target": "004981d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad02dc`](#insn-00ad02dc)

~~~json
{
  "source": "00ad02dc",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad02e4`](#insn-00ad02e4)

~~~json
{
  "source": "00ad02e4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad02ec`](#insn-00ad02ec)

~~~json
{
  "source": "00ad02ec",
  "target": "00ad039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad02f0`](#insn-00ad02f0)

~~~json
{
  "source": "00ad02f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad02f4`](#insn-00ad02f4)

~~~json
{
  "source": "00ad02f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad02f8`](#insn-00ad02f8)

~~~json
{
  "source": "00ad02f8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad02fc`](#insn-00ad02fc)

~~~json
{
  "source": "00ad02fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0300`](#insn-00ad0300)

~~~json
{
  "source": "00ad0300",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0304`](#insn-00ad0304)

~~~json
{
  "source": "00ad0304",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0314`](#insn-00ad0314)

~~~json
{
  "source": "00ad0314",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0318`](#insn-00ad0318)

~~~json
{
  "source": "00ad0318",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad031c`](#insn-00ad031c)

~~~json
{
  "source": "00ad031c",
  "target": "00ad02cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0324`](#insn-00ad0324)

~~~json
{
  "source": "00ad0324",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad032c`](#insn-00ad032c)

~~~json
{
  "source": "00ad032c",
  "target": "0047edb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0338`](#insn-00ad0338)

~~~json
{
  "source": "00ad0338",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ad033c`](#insn-00ad033c)

~~~json
{
  "source": "00ad033c",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0340`](#insn-00ad0340)

~~~json
{
  "source": "00ad0340",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0340`](#insn-00ad0340)

~~~json
{
  "source": "00ad0340",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0348`](#insn-00ad0348)

~~~json
{
  "source": "00ad0348",
  "target": "00ca4f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0348`](#insn-00ad0348)

~~~json
{
  "source": "00ad0348",
  "target": "00ca4f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad034c`](#insn-00ad034c)

~~~json
{
  "source": "00ad034c",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0350`](#insn-00ad0350)

~~~json
{
  "source": "00ad0350",
  "target": "00ca4f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0350`](#insn-00ad0350)

~~~json
{
  "source": "00ad0350",
  "target": "00ca4f18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0350`](#insn-00ad0350)

~~~json
{
  "source": "00ad0350",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0354`](#insn-00ad0354)

~~~json
{
  "source": "00ad0354",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad035c`](#insn-00ad035c)

~~~json
{
  "source": "00ad035c",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad0360`](#insn-00ad0360)

~~~json
{
  "source": "00ad0360",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad0364`](#insn-00ad0364)

~~~json
{
  "source": "00ad0364",
  "target": "00ad02cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad039c`](#insn-00ad039c)

~~~json
{
  "source": "00ad039c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
