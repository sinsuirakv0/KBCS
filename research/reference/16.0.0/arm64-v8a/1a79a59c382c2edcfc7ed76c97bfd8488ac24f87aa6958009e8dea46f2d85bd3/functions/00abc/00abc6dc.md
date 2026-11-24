# 00abc6dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a5e724`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md) · 移動量 `+0x5dfb8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-b652a483bea84fb5224a85e86715ccb1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abc8d8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abc/00abc8d8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-20f76ac67e17f0e334fc8a7b5e323cd3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abc6dc",
  "name": "FUN_00abc6dc",
  "size": 1348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1919a6683e4a8984809399acc0c061016070bee5efa93da4b5c852d5d5cb6c12",
  "source_text_sha256": "1919a6683e4a8984809399acc0c061016070bee5efa93da4b5c852d5d5cb6c12",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abc6dc",
        "00abcc1b"
      ],
      [
        "00abccb4",
        "00abccb7"
      ]
    ],
    "bytes_sha256": "9000cf84dad0f8d11fd121759706480d80c1991ab4125bca0dc37787d919c33e",
    "instruction_count": 337,
    "instruction_bytes": 1348,
    "body_bytes": 1348,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00abe1c8](../00abe/00abe1c8.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [0046da08](../0046d/0046da08.md)
- [00470800](../00470/00470800.md)
- [0049f3b0](../0049f/0049f3b0.md)
- [00615c90](../00615/00615c90.md)
- [00728b2c](../00728/00728b2c.md)
- [0080b388](../0080b/0080b388.md)
- [00abccb8](../00abc/00abccb8.md)
- [00abce14](../00abc/00abce14.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57c00](../00c57/00c57c00.md)
- [00c58050](../00c58/00c58050.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 14365 bytes

~~~c

byte FUN_00abc6dc(int *param_1,long param_2,int param_3)

{
  undefined4 *puVar1;
  wchar_t *pwVar2;
  undefined4 *puVar3;
  ulong uVar4;
  byte bVar5;
  int iVar6;
  int *__ptr;
  int *piVar7;
  wchar_t *pwVar8;
  ulong uVar9;
  void *__dest;
  ulong uVar10;
  undefined8 *puVar11;
  undefined8 *__ptr_00;
  int *piVar12;
  ulong uVar13;
  undefined8 *extraout_x8;
  undefined8 *puVar14;
  ulong uVar15;
  ulong uVar16;
  undefined8 *puVar17;
  wchar_t *pwVar18;
  void *pvVar19;
  int *piVar20;
  ulong uVar21;
  undefined4 *puVar22;
  long lVar23;
  void *local_a0;
  void *pvStack_98;
  undefined8 local_90;
  undefined8 *local_80;
  undefined8 *local_78;
  undefined8 *local_70;
  long local_68;
  
                    /* catch() { ... } // from try @ 00abb854 with catch @ 00abc6e0 */
                    /* catch() { ... } // from try @ 00abb764 with catch @ 00abc6f4 */
  uVar4 = tpidr_el0;
                    /* catch() { ... } // from try @ 00abb674 with catch @ 00abc708 */
  local_68 = *(long *)(uVar4 + 0x28);
  __ptr = (int *)_Znwm(4);
                    /* catch() { ... } // from try @ 00abb3c4 with catch @ 00abc71c */
  iVar6 = *param_1;
  bVar5 = 0;
  *__ptr = 0;
                    /* catch() { ... } // from try @ 00abb2c8 with catch @ 00abc730 */
  piVar7 = __ptr;
  if (iVar6 < 2) {
    if (iVar6 == 0) {
      piVar7 = (int *)_Znwm(8);
LAB_00abc78c:
                    /* catch() { ... } // from try @ 00abb3b0 with catch @ 00abc78c */
      iVar6 = 3;
      goto LAB_00abc7ec;
    }
    if (iVar6 == 1) {
      iVar6 = param_1[0x1d];
                    /* catch() { ... } // from try @ 00abb840 with catch @ 00abc744 */
      piVar20 = __ptr + 1;
      if (iVar6 < 2) {
        if (iVar6 == 0) {
                    /* catch() { ... } // from try @ 00abb820 with catch @ 00abc7d0 */
                    /* catch() { ... } // from try @ 00abb730 with catch @ 00abc7d4 */
          piVar7 = (int *)_Znwm(8);
                    /* catch() { ... } // from try @ 00abb640 with catch @ 00abc7d8 */
          goto LAB_00abc78c;
        }
        if (iVar6 == 1) {
                    /* catch() { ... } // from try @ 00abb750 with catch @ 00abc75c */
          piVar7 = (int *)_Znwm(8);
LAB_00abc7c4:
                    /* catch() { ... } // from try @ 00abb654 with catch @ 00abc7c4 */
                    /* catch() { ... } // from try @ 00abb3a4 with catch @ 00abc7c8 */
          iVar6 = 1;
                    /* catch() { ... } // from try @ 00abb2a8 with catch @ 00abc7cc */
          goto LAB_00abc7ec;
        }
      }
      else {
        if (iVar6 == 2) {
                    /* catch() { ... } // from try @ 00abb390 with catch @ 00abc7dc */
                    /* catch() { ... } // from try @ 00abb294 with catch @ 00abc7e0 */
          piVar7 = (int *)_Znwm(8);
                    /* catch() { ... } // from try @ 00abb81c with catch @ 00abc7e4 */
                    /* catch() { ... } // from try @ 00abb728 with catch @ 00abc7e8 */
          iVar6 = 2;
          goto LAB_00abc7ec;
        }
        if (iVar6 == 4) {
                    /* catch() { ... } // from try @ 00abb834 with catch @ 00abc7bc */
                    /* catch() { ... } // from try @ 00abb744 with catch @ 00abc7c0 */
          piVar7 = (int *)_Znwm(8);
          goto LAB_00abc7c4;
        }
      }
      goto LAB_00abc808;
    }
  }
  else {
    if (iVar6 != 2) {
                    /* catch() { ... } // from try @ 00abb660 with catch @ 00abc774 */
      if (iVar6 != 3) goto LAB_00abc8cc;
      piVar7 = (int *)_Znwm(8);
      goto LAB_00abc78c;
    }
    piVar7 = (int *)_Znwm(8);
                    /* catch() { ... } // from try @ 00abb2b4 with catch @ 00abc7a4 */
    iVar6 = 4;
LAB_00abc7ec:
                    /* catch() { ... } // from try @ 00abb638 with catch @ 00abc7ec */
                    /* catch() { ... } // from try @ 00abb388 with catch @ 00abc7f0 */
                    /* catch() { ... } // from try @ 00abb28c with catch @ 00abc7f4 */
    piVar20 = piVar7 + 2;
                    /* catch() { ... } // from try @ 00abaeb8 with catch @ 00abc7f8 */
    *piVar7 = *__ptr;
    piVar7[1] = iVar6;
    _ZdlPv(__ptr);
    __ptr = piVar7;
LAB_00abc808:
    do {
      piVar12 = __ptr;
      if (*__ptr == param_3) break;
      __ptr = __ptr + 1;
      piVar12 = piVar20;
    } while (__ptr != piVar20);
    if (piVar12 == piVar20) {
LAB_00abc8c8:
      bVar5 = 0;
    }
    else {
      iVar6 = *param_1;
      if (iVar6 < 2) {
        if (iVar6 == 0) {
          local_80 = (undefined8 *)0x0;
          local_78 = (undefined8 *)0x0;
                    /* catch() { ... } // from try @ 00abb038 with catch @ 00abc910 */
          lVar23 = *(long *)(param_1 + 0x14);
          local_70 = (undefined8 *)0x0;
          if (*(long *)(param_1 + 0x16) == lVar23) {
LAB_00abca8c:
            bVar5 = 1;
          }
          else {
            uVar21 = 0;
            uVar10 = uVar4;
            do {
              if (-1 < *(int *)(lVar23 + uVar21 * 4)) {
                local_a0 = (void *)0x0;
                pvStack_98 = (void *)0x0;
                local_90 = 0;
                    /* catch() { ... } // from try @ 00abac98 with catch @ 00abc960 */
                if (local_78 < local_70) {
                  *local_78 = 0;
                  local_78[1] = 0;
                  local_78[2] = 0;
                  local_78[1] = 0;
                  *local_78 = 0;
                  local_78[2] = 0;
                  local_78 = local_78 + 3;
                }
                else {
                  local_78 = (undefined8 *)FUN_00615c90(&local_80,&local_a0);
                  if (local_a0 != (void *)0x0) {
                    pvStack_98 = local_a0;
                    _ZdlPv(local_a0);
                    /* catch() { ... } // from try @ 00abb19c with catch @ 00abc9b0 */
                  }
                }
              }
              puVar11 = local_78;
              if (local_78 == local_80) {
                if (*(long *)(uVar4 + 0x28) != local_68) goto LAB_00abccb4;
                FUN_0080b388(&local_80);
                goto LAB_00abcbd0;
              }
              if ((ulong)(*(long *)(param_1 + 0x16) - *(long *)(param_1 + 0x14) >> 2) <= uVar21) {
                if (*(long *)(uVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                  FUN_0049f3b0(param_1 + 0x14);
                }
                goto LAB_00abccb4;
              }
                    /* catch() { ... } // from try @ 00abb028 with catch @ 00abc9d4 */
              uVar9 = FUN_0046da08(*(undefined4 *)(*(long *)(param_1 + 0x14) + uVar21 * 4));
              puVar3 = (undefined4 *)puVar11[-2];
              if (puVar3 < (undefined4 *)puVar11[-1]) {
                puVar22 = puVar3 + 1;
                *puVar3 = (int)uVar9;
              }
              else {
                puVar14 = puVar11 + -3;
                pvVar19 = (void *)*puVar14;
                lVar23 = (long)puVar3 - (long)pvVar19 >> 2;
                uVar16 = lVar23 + 1;
                    /* catch() { ... } // from try @ 00abac88 with catch @ 00abc9f8 */
                if (uVar16 >> 0x3e != 0) goto LAB_00abcbe8;
                uVar13 = (long)puVar11[-1] - (long)pvVar19;
                uVar15 = (long)uVar13 >> 1;
                if (uVar15 <= uVar16) {
                  uVar15 = uVar16;
                }
                    /* catch() { ... } // from try @ 00abb190 with catch @ 00abca1c */
                if (0x7ffffffffffffffb < uVar13) {
                  uVar15 = 0x3fffffffffffffff;
                }
                if (uVar15 == 0) {
                  __dest = (void *)0x0;
                }
                else {
                  if (uVar15 >> 0x3e != 0) {
                    if (*(long *)(uVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                      FUN_00440e80();
                    }
                    goto LAB_00abccb4;
                  }
                  uVar9 = uVar9 & 0xffffffff;
                  __dest = (void *)_Znwm(uVar15 << 2);
                  uVar10 = uVar9;
                }
                puVar1 = (undefined4 *)((long)__dest + lVar23 * 4);
                puVar22 = puVar1 + 1;
                *puVar1 = (int)uVar9;
                    /* catch() { ... } // from try @ 00abb01c with catch @ 00abca60 */
                memcpy(__dest,pvVar19,(long)puVar3 - (long)pvVar19);
                puVar11[-3] = __dest;
                puVar11[-2] = puVar22;
                puVar11[-1] = (void *)((long)__dest + uVar15 * 4);
                if (pvVar19 != (void *)0x0) {
                  _ZdlPv(pvVar19);
                }
              }
              puVar11[-2] = puVar22;
              uVar21 = uVar21 + 1;
              lVar23 = *(long *)(param_1 + 0x14);
            } while (uVar21 < (ulong)(*(long *)(param_1 + 0x16) - lVar23 >> 2));
            puVar11 = local_80;
            if (local_78 != local_80) {
                    /* catch() { ... } // from try @ 00abac7c with catch @ 00abcaa4 */
              uVar21 = 0;
              do {
                uVar9 = ((long)local_78 - (long)local_80 >> 3) * -0x5555555555555555;
                uVar10 = uVar4;
                if (uVar9 < uVar21 || uVar9 - uVar21 == 0) goto LAB_00abcbd0;
                lVar23 = local_80[uVar21 * 3];
                if ((local_80 + uVar21 * 3)[1] == lVar23) {
LAB_00abcb34:
                    /* catch() { ... } // from try @ 00abb138 with catch @ 00abcb34 */
                  bVar5 = 0;
                    /* catch() { ... } // from try @ 00abafc4 with catch @ 00abcb38 */
                  __ptr_00 = local_78;
                  puVar11 = local_78;
                  puVar14 = local_80;
                    /* catch() { ... } // from try @ 00abac24 with catch @ 00abcb3c */
                  if (local_78 == local_80) goto LAB_00abcb8c;
                  goto LAB_00abcb70;
                }
                uVar9 = 0;
                while( true ) {
                  uVar10 = FUN_00abccb8(param_1,*(undefined4 *)(lVar23 + uVar9 * 4));
                    /* catch() { ... } // from try @ 00abb144 with catch @ 00abcae8 */
                  uVar16 = ((long)local_78 - (long)local_80 >> 3) * -0x5555555555555555;
                  if ((uVar10 & 1) != 0) break;
                    /* catch() { ... } // from try @ 00abafd0 with catch @ 00abcb00 */
                  uVar10 = uVar4;
                  if (uVar16 < uVar21 || uVar16 - uVar21 == 0) goto LAB_00abcbd0;
                  uVar9 = uVar9 + 1;
                  lVar23 = local_80[uVar21 * 3];
                    /* catch() { ... } // from try @ 00abac30 with catch @ 00abcb18 */
                  if ((ulong)((local_80 + uVar21 * 3)[1] - lVar23 >> 2) <= uVar9) goto LAB_00abcb34;
                }
                uVar21 = uVar21 + 1;
                puVar11 = local_78;
              } while (uVar21 <= uVar16 && uVar16 - uVar21 != 0);
            }
            bVar5 = 1;
                    /* catch() { ... } // from try @ 00abb114 with catch @ 00abcb50 */
            if (local_80 != (undefined8 *)0x0) {
                    /* catch() { ... } // from try @ 00abafa0 with catch @ 00abcb54 */
              __ptr_00 = puVar11;
              puVar14 = local_80;
                    /* catch() { ... } // from try @ 00abac00 with catch @ 00abcb58 */
              if (puVar11 != local_80) {
LAB_00abcb70:
                do {
                  puVar17 = puVar11 + -3;
                  pvVar19 = (void *)*puVar17;
                  if (pvVar19 != (void *)0x0) {
                    puVar11[-2] = pvVar19;
                    /* catch() { ... } // from try @ 00abbd00 with catch @ 00abcb80 */
                    _ZdlPv(pvVar19);
                    /* catch() { ... } // from try @ 00abbc40 with catch @ 00abcb84 */
                  }
                    /* catch() { ... } // from try @ 00abbd10 with catch @ 00abcb64 */
                  __ptr_00 = local_80;
                  puVar11 = puVar17;
                } while (puVar17 != puVar14);
              }
LAB_00abcb8c:
              local_78 = puVar14;
              _ZdlPv(__ptr_00);
            }
          }
        }
        else {
          if (iVar6 != 1) goto LAB_00abc8c8;
                    /* catch() { ... } // from try @ 00abaea8 with catch @ 00abc844 */
          iVar6 = FUN_00abce14(param_2,param_1[0x1d]);
          bVar5 = param_1[0x1e] <= iVar6;
        }
      }
      else {
                    /* catch() { ... } // from try @ 00abae9c with catch @ 00abc864 */
        if (iVar6 == 2) {
          bVar5 = FUN_00728b2c(param_1[0x1f]);
        }
        else {
          if (iVar6 != 3) goto LAB_00abc8c8;
          lVar23 = *(long *)(param_1 + 8);
          if (*(long *)(param_1 + 10) == lVar23) goto LAB_00abca8c;
          pwVar18 = *(wchar_t **)(param_2 + 0x38);
          uVar21 = 0;
          do {
            pwVar8 = wmemchr(*(wchar_t **)(param_2 + 0x30),*(wchar_t *)(lVar23 + uVar21 * 4),
                             (long)pwVar18 - (long)*(wchar_t **)(param_2 + 0x30) >> 2);
            pwVar2 = pwVar18;
            if (pwVar8 != (wchar_t *)0x0) {
              pwVar2 = pwVar8;
            }
            pwVar18 = *(wchar_t **)(param_2 + 0x38);
                    /* catch() { ... } // from try @ 00abae50 with catch @ 00abc8a4 */
            bVar5 = pwVar2 != pwVar18;
            if (pwVar2 == pwVar18) break;
            lVar23 = *(long *)(param_1 + 8);
            uVar21 = uVar21 + 1;
                    /* catch() { ... } // from try @ 00abae44 with catch @ 00abc8b8 */
                    /* catch() { ... } // from try @ 00abae18 with catch @ 00abc8bc */
                    /* catch() { ... } // from try @ 00abb1ac with catch @ 00abc8c0 */
          } while (uVar21 < (ulong)(*(long *)(param_1 + 10) - lVar23 >> 2));
        }
      }
    }
  }
LAB_00abc8cc:
  _ZdlPv(piVar7);
  if (*(long *)(uVar4 + 0x28) == local_68) {
    return bVar5 & 1;
  }
LAB_00abccb4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
LAB_00abcbd0:
  if (*(long *)(uVar10 + 0x28) == local_68) {
    FUN_0080b388(&local_80);
    puVar14 = extraout_x8;
LAB_00abcbe8:
    if (*(long *)(uVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
      FUN_00470800(puVar14);
    }
  }
  goto LAB_00abccb4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abc6dc"></a> `00abc6dc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00abc6e0"></a> `00abc6e0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abc6e4"></a> `00abc6e4` | `fc 6f 06 a9` | stp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abc6e8"></a> `00abc6e8` | `fa 67 07 a9` | stp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abc6ec"></a> `00abc6ec` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abc6f0"></a> `00abc6f0` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abc6f4"></a> `00abc6f4` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abc6f8"></a> `00abc6f8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00abc6fc"></a> `00abc6fc` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abc700"></a> `00abc700` | `f6 03 02 2a` | mov w22,w2 | `FALL_THROUGH`
<a id="insn-00abc704"></a> `00abc704` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00abc708"></a> `00abc708` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00abc70c"></a> `00abc70c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00abc710"></a> `00abc710` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abc714"></a> `00abc714` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00abc718"></a> `00abc718` | `de 6c 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abc71c"></a> `00abc71c` | `88 02 40 b9` | ldr w8,[x20] | `FALL_THROUGH`
<a id="insn-00abc720"></a> `00abc720` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abc724"></a> `00abc724` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00abc728"></a> `00abc728` | `1f 00 00 b9` | str wzr,[x0] | `FALL_THROUGH`
<a id="insn-00abc72c"></a> `00abc72c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abc730"></a> `00abc730` | `cc 01 00 54` | b.gt 0x00abc768 | `CONDITIONAL_JUMP`
<a id="insn-00abc734"></a> `00abc734` | `88 02 00 34` | cbz w8,0x00abc784 | `CONDITIONAL_JUMP`
<a id="insn-00abc738"></a> `00abc738` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abc73c"></a> `00abc73c` | `81 0c 00 54` | b.ne 0x00abc8cc | `CONDITIONAL_JUMP`
<a id="insn-00abc740"></a> `00abc740` | `88 76 40 b9` | ldr w8,[x20, #0x74] | `FALL_THROUGH`
<a id="insn-00abc744"></a> `00abc744` | `78 12 00 91` | add x24,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00abc748"></a> `00abc748` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abc74c"></a> `00abc74c` | `0c 03 00 54` | b.gt 0x00abc7ac | `CONDITIONAL_JUMP`
<a id="insn-00abc750"></a> `00abc750` | `08 04 00 34` | cbz w8,0x00abc7d0 | `CONDITIONAL_JUMP`
<a id="insn-00abc754"></a> `00abc754` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abc758"></a> `00abc758` | `61 05 00 54` | b.ne 0x00abc804 | `CONDITIONAL_JUMP`
<a id="insn-00abc75c"></a> `00abc75c` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00abc760"></a> `00abc760` | `cc 6c 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abc764"></a> `00abc764` | `18 00 00 14` | b 0x00abc7c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abc768"></a> `00abc768` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00abc76c"></a> `00abc76c` | `60 01 00 54` | b.eq 0x00abc798 | `CONDITIONAL_JUMP`
<a id="insn-00abc770"></a> `00abc770` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00abc774"></a> `00abc774` | `c1 0a 00 54` | b.ne 0x00abc8cc | `CONDITIONAL_JUMP`
<a id="insn-00abc778"></a> `00abc778` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00abc77c"></a> `00abc77c` | `c5 6c 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abc780"></a> `00abc780` | `03 00 00 14` | b 0x00abc78c | `UNCONDITIONAL_JUMP`
<a id="insn-00abc784"></a> `00abc784` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00abc788"></a> `00abc788` | `c2 6c 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abc78c"></a> `00abc78c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00abc790"></a> `00abc790` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00abc794"></a> `00abc794` | `16 00 00 14` | b 0x00abc7ec | `UNCONDITIONAL_JUMP`
<a id="insn-00abc798"></a> `00abc798` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00abc79c"></a> `00abc79c` | `bd 6c 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abc7a0"></a> `00abc7a0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00abc7a4"></a> `00abc7a4` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00abc7a8"></a> `00abc7a8` | `11 00 00 14` | b 0x00abc7ec | `UNCONDITIONAL_JUMP`
<a id="insn-00abc7ac"></a> `00abc7ac` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00abc7b0"></a> `00abc7b0` | `60 01 00 54` | b.eq 0x00abc7dc | `CONDITIONAL_JUMP`
<a id="insn-00abc7b4"></a> `00abc7b4` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00abc7b8"></a> `00abc7b8` | `61 02 00 54` | b.ne 0x00abc804 | `CONDITIONAL_JUMP`
<a id="insn-00abc7bc"></a> `00abc7bc` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00abc7c0"></a> `00abc7c0` | `b4 6c 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abc7c4"></a> `00abc7c4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00abc7c8"></a> `00abc7c8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abc7cc"></a> `00abc7cc` | `08 00 00 14` | b 0x00abc7ec | `UNCONDITIONAL_JUMP`
<a id="insn-00abc7d0"></a> `00abc7d0` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00abc7d4"></a> `00abc7d4` | `af 6c 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abc7d8"></a> `00abc7d8` | `ed ff ff 17` | b 0x00abc78c | `UNCONDITIONAL_JUMP`
<a id="insn-00abc7dc"></a> `00abc7dc` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00abc7e0"></a> `00abc7e0` | `ac 6c 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abc7e4"></a> `00abc7e4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00abc7e8"></a> `00abc7e8` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00abc7ec"></a> `00abc7ec` | `69 02 40 b9` | ldr w9,[x19] | `FALL_THROUGH`
<a id="insn-00abc7f0"></a> `00abc7f0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abc7f4"></a> `00abc7f4` | `f8 22 00 91` | add x24,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00abc7f8"></a> `00abc7f8` | `e9 22 00 29` | stp w9,w8,[x23] | `FALL_THROUGH`
<a id="insn-00abc7fc"></a> `00abc7fc` | `ad 6c 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abc800"></a> `00abc800` | `f3 03 17 aa` | mov x19,x23 | `FALL_THROUGH`
<a id="insn-00abc804"></a> `00abc804` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00abc808"></a> `00abc808` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00abc80c"></a> `00abc80c` | `3f 01 16 6b` | cmp w9,w22 | `FALL_THROUGH`
<a id="insn-00abc810"></a> `00abc810` | `a0 00 00 54` | b.eq 0x00abc824 | `CONDITIONAL_JUMP`
<a id="insn-00abc814"></a> `00abc814` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00abc818"></a> `00abc818` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00abc81c"></a> `00abc81c` | `61 ff ff 54` | b.ne 0x00abc808 | `CONDITIONAL_JUMP`
<a id="insn-00abc820"></a> `00abc820` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00abc824"></a> `00abc824` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00abc828"></a> `00abc828` | `00 05 00 54` | b.eq 0x00abc8c8 | `CONDITIONAL_JUMP`
<a id="insn-00abc82c"></a> `00abc82c` | `88 02 40 b9` | ldr w8,[x20] | `FALL_THROUGH`
<a id="insn-00abc830"></a> `00abc830` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abc834"></a> `00abc834` | `6c 01 00 54` | b.gt 0x00abc860 | `CONDITIONAL_JUMP`
<a id="insn-00abc838"></a> `00abc838` | `88 06 00 34` | cbz w8,0x00abc908 | `CONDITIONAL_JUMP`
<a id="insn-00abc83c"></a> `00abc83c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abc840"></a> `00abc840` | `41 04 00 54` | b.ne 0x00abc8c8 | `CONDITIONAL_JUMP`
<a id="insn-00abc844"></a> `00abc844` | `81 76 40 b9` | ldr w1,[x20, #0x74] | `FALL_THROUGH`
<a id="insn-00abc848"></a> `00abc848` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abc84c"></a> `00abc84c` | `72 01 00 94` | bl 0x00abce14 | `UNCONDITIONAL_CALL`
<a id="insn-00abc850"></a> `00abc850` | `88 7a 40 b9` | ldr w8,[x20, #0x78] | `FALL_THROUGH`
<a id="insn-00abc854"></a> `00abc854` | `1f 00 08 6b` | cmp w0,w8 | `FALL_THROUGH`
<a id="insn-00abc858"></a> `00abc858` | `f7 b7 9f 1a` | cset w23,ge | `FALL_THROUGH`
<a id="insn-00abc85c"></a> `00abc85c` | `1c 00 00 14` | b 0x00abc8cc | `UNCONDITIONAL_JUMP`
<a id="insn-00abc860"></a> `00abc860` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00abc864"></a> `00abc864` | `c0 10 00 54` | b.eq 0x00abca7c | `CONDITIONAL_JUMP`
<a id="insn-00abc868"></a> `00abc868` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00abc86c"></a> `00abc86c` | `e1 02 00 54` | b.ne 0x00abc8c8 | `CONDITIONAL_JUMP`
<a id="insn-00abc870"></a> `00abc870` | `88 26 42 a9` | ldp x8,x9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00abc874"></a> `00abc874` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00abc878"></a> `00abc878` | `a0 10 00 54` | b.eq 0x00abca8c | `CONDITIONAL_JUMP`
<a id="insn-00abc87c"></a> `00abc87c` | `b6 1e 40 f9` | ldr x22,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00abc880"></a> `00abc880` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00abc884"></a> `00abc884` | `a0 1a 40 f9` | ldr x0,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00abc888"></a> `00abc888` | `01 79 78 b8` | ldr w1,[x8, x24, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abc88c"></a> `00abc88c` | `c9 02 00 cb` | sub x9,x22,x0 | `FALL_THROUGH`
<a id="insn-00abc890"></a> `00abc890` | `22 fd 42 93` | asr x2,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00abc894"></a> `00abc894` | `ef 6d 06 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00abc898"></a> `00abc898` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00abc89c"></a> `00abc89c` | `c8 02 80 9a` | csel x8,x22,x0,eq | `FALL_THROUGH`
<a id="insn-00abc8a0"></a> `00abc8a0` | `b6 1e 40 f9` | ldr x22,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00abc8a4"></a> `00abc8a4` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00abc8a8"></a> `00abc8a8` | `f7 07 9f 1a` | cset w23,ne | `FALL_THROUGH`
<a id="insn-00abc8ac"></a> `00abc8ac` | `00 01 00 54` | b.eq 0x00abc8cc | `CONDITIONAL_JUMP`
<a id="insn-00abc8b0"></a> `00abc8b0` | `88 26 42 a9` | ldp x8,x9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00abc8b4"></a> `00abc8b4` | `18 07 00 91` | add x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00abc8b8"></a> `00abc8b8` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00abc8bc"></a> `00abc8bc` | `1f 0b 89 eb` | cmp x24,x9, ASR #0x2 | `FALL_THROUGH`
<a id="insn-00abc8c0"></a> `00abc8c0` | `23 fe ff 54` | b.cc 0x00abc884 | `CONDITIONAL_JUMP`
<a id="insn-00abc8c4"></a> `00abc8c4` | `02 00 00 14` | b 0x00abc8cc | `UNCONDITIONAL_JUMP`
<a id="insn-00abc8c8"></a> `00abc8c8` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00abc8cc"></a> `00abc8cc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abc8d0"></a> `00abc8d0` | `78 6c 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abc8d4"></a> `00abc8d4` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00abc8d8"></a> `00abc8d8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abc8dc"></a> `00abc8dc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abc8e0"></a> `00abc8e0` | `a1 1e 00 54` | b.ne 0x00abccb4 | `CONDITIONAL_JUMP`
<a id="insn-00abc8e4"></a> `00abc8e4` | `e0 02 00 12` | and w0,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00abc8e8"></a> `00abc8e8` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abc8ec"></a> `00abc8ec` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abc8f0"></a> `00abc8f0` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abc8f4"></a> `00abc8f4` | `fa 67 47 a9` | ldp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abc8f8"></a> `00abc8f8` | `fc 6f 46 a9` | ldp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abc8fc"></a> `00abc8fc` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abc900"></a> `00abc900` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00abc904"></a> `00abc904` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abc908"></a> `00abc908` | `ea 03 14 aa` | mov x10,x20 | `FALL_THROUGH`
<a id="insn-00abc90c"></a> `00abc90c` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abc910"></a> `00abc910` | `48 25 c5 a9` | ldp x8,x9,[x10, #0x50]! | `FALL_THROUGH`
<a id="insn-00abc914"></a> `00abc914` | `bf 03 1f f8` | stur xzr,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abc918"></a> `00abc918` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00abc91c"></a> `00abc91c` | `80 0b 00 54` | b.eq 0x00abca8c | `CONDITIONAL_JUMP`
<a id="insn-00abc920"></a> `00abc920` | `fb 03 1f aa` | mov x27,xzr | `FALL_THROUGH`
<a id="insn-00abc924"></a> `00abc924` | `ea 6b 00 a9` | stp x10,x26,[sp] | `FALL_THROUGH`
<a id="insn-00abc928"></a> `00abc928` | `08 00 00 14` | b 0x00abc948 | `UNCONDITIONAL_JUMP`
<a id="insn-00abc92c"></a> `00abc92c` | `80 47 00 b8` | str w0,[x28], #0x4 | `FALL_THROUGH`
<a id="insn-00abc930"></a> `00abc930` | `dc 02 1f f8` | stur x28,[x22, #-0x10] | `FALL_THROUGH`
<a id="insn-00abc934"></a> `00abc934` | `7b 07 00 91` | add x27,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00abc938"></a> `00abc938` | `88 26 45 a9` | ldp x8,x9,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00abc93c"></a> `00abc93c` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00abc940"></a> `00abc940` | `7f 0b 89 eb` | cmp x27,x9, ASR #0x2 | `FALL_THROUGH`
<a id="insn-00abc944"></a> `00abc944` | `82 0a 00 54` | b.cs 0x00abca94 | `CONDITIONAL_JUMP`
<a id="insn-00abc948"></a> `00abc948` | `08 79 7b b8` | ldr w8,[x8, x27, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abc94c"></a> `00abc94c` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00abc950"></a> `00abc950` | `28 03 f8 37` | tbnz w8,#0x1f,0x00abc9b4 | `CONDITIONAL_JUMP`
<a id="insn-00abc954"></a> `00abc954` | `a8 03 5f f8` | ldur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abc958"></a> `00abc958` | `ff 7f 01 a9` | stp xzr,xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abc95c"></a> `00abc95c` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abc960"></a> `00abc960` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00abc964"></a> `00abc964` | `42 01 00 54` | b.cs 0x00abc98c | `CONDITIONAL_JUMP`
<a id="insn-00abc968"></a> `00abc968` | `df 7e 00 a9` | stp xzr,xzr,[x22] | `FALL_THROUGH`
<a id="insn-00abc96c"></a> `00abc96c` | `df 0a 00 f9` | str xzr,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00abc970"></a> `00abc970` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abc974"></a> `00abc974` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00abc978"></a> `00abc978` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abc97c"></a> `00abc97c` | `c8 0a 00 f9` | str x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00abc980"></a> `00abc980` | `d6 62 00 91` | add x22,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00abc984"></a> `00abc984` | `b6 83 1e f8` | stur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00abc988"></a> `00abc988` | `0b 00 00 14` | b 0x00abc9b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abc98c"></a> `00abc98c` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abc990"></a> `00abc990` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00abc994"></a> `00abc994` | `bf 64 ed 97` | bl 0x00615c90 | `UNCONDITIONAL_CALL`
<a id="insn-00abc998"></a> `00abc998` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00abc99c"></a> `00abc99c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abc9a0"></a> `00abc9a0` | `b6 83 1e f8` | stur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00abc9a4"></a> `00abc9a4` | `80 00 00 b4` | cbz x0,0x00abc9b4 | `CONDITIONAL_JUMP`
<a id="insn-00abc9a8"></a> `00abc9a8` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abc9ac"></a> `00abc9ac` | `41 6c 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abc9b0"></a> `00abc9b0` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00abc9b4"></a> `00abc9b4` | `a8 03 5e f8` | ldur x8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abc9b8"></a> `00abc9b8` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00abc9bc"></a> `00abc9bc` | `c0 0f 00 54` | b.eq 0x00abcbb4 | `CONDITIONAL_JUMP`
<a id="insn-00abc9c0"></a> `00abc9c0` | `88 26 45 a9` | ldp x8,x9,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00abc9c4"></a> `00abc9c4` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00abc9c8"></a> `00abc9c8` | `7f 0b 89 eb` | cmp x27,x9, ASR #0x2 | `FALL_THROUGH`
<a id="insn-00abc9cc"></a> `00abc9cc` | `62 0e 00 54` | b.cs 0x00abcb98 | `CONDITIONAL_JUMP`
<a id="insn-00abc9d0"></a> `00abc9d0` | `00 79 7b b8` | ldr w0,[x8, x27, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abc9d4"></a> `00abc9d4` | `0d c4 e6 97` | bl 0x0046da08 | `UNCONDITIONAL_CALL`
<a id="insn-00abc9d8"></a> `00abc9d8` | `dc 26 7f a9` | ldp x28,x9,[x22, #-0x10] | `FALL_THROUGH`
<a id="insn-00abc9dc"></a> `00abc9dc` | `9f 03 09 eb` | cmp x28,x9 | `FALL_THROUGH`
<a id="insn-00abc9e0"></a> `00abc9e0` | `63 fa ff 54` | b.cc 0x00abc92c | `CONDITIONAL_JUMP`
<a id="insn-00abc9e4"></a> `00abc9e4` | `c8 62 00 d1` | sub x8,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00abc9e8"></a> `00abc9e8` | `17 01 40 f9` | ldr x23,[x8] | `FALL_THROUGH`
<a id="insn-00abc9ec"></a> `00abc9ec` | `98 03 17 cb` | sub x24,x28,x23 | `FALL_THROUGH`
<a id="insn-00abc9f0"></a> `00abc9f0` | `1c ff 42 93` | asr x28,x24,#0x2 | `FALL_THROUGH`
<a id="insn-00abc9f4"></a> `00abc9f4` | `8a 07 00 91` | add x10,x28,#0x1 | `FALL_THROUGH`
<a id="insn-00abc9f8"></a> `00abc9f8` | `4b fd 7e d3` | lsr x11,x10,#0x3e | `FALL_THROUGH`
<a id="insn-00abc9fc"></a> `00abc9fc` | `6b 0f 00 b5` | cbnz x11,0x00abcbe8 | `CONDITIONAL_JUMP`
<a id="insn-00abca00"></a> `00abca00` | `28 01 17 cb` | sub x8,x9,x23 | `FALL_THROUGH`
<a id="insn-00abca04"></a> `00abca04` | `09 fd 41 93` | asr x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abca08"></a> `00abca08` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00abca0c"></a> `00abca0c` | `29 81 8a 9a` | csel x9,x9,x10,hi | `FALL_THROUGH`
<a id="insn-00abca10"></a> `00abca10` | `ea f3 7e b2` | orr x10,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-00abca14"></a> `00abca14` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00abca18"></a> `00abca18` | `08 00 f8 92` | mov x8,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-00abca1c"></a> `00abca1c` | `35 31 88 9a` | csel x21,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00abca20"></a> `00abca20` | `35 01 00 b4` | cbz x21,0x00abca44 | `CONDITIONAL_JUMP`
<a id="insn-00abca24"></a> `00abca24` | `a8 fe 7e d3` | lsr x8,x21,#0x3e | `FALL_THROUGH`
<a id="insn-00abca28"></a> `00abca28` | `e8 0e 00 b5` | cbnz x8,0x00abcc04 | `CONDITIONAL_JUMP`
<a id="insn-00abca2c"></a> `00abca2c` | `fa 03 00 2a` | mov w26,w0 | `FALL_THROUGH`
<a id="insn-00abca30"></a> `00abca30` | `a0 f6 7e d3` | lsl x0,x21,#0x2 | `FALL_THROUGH`
<a id="insn-00abca34"></a> `00abca34` | `17 6c 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abca38"></a> `00abca38` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00abca3c"></a> `00abca3c` | `e0 03 1a 2a` | mov w0,w26 | `FALL_THROUGH`
<a id="insn-00abca40"></a> `00abca40` | `02 00 00 14` | b 0x00abca48 | `UNCONDITIONAL_JUMP`
<a id="insn-00abca44"></a> `00abca44` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00abca48"></a> `00abca48` | `3c 0b 1c 8b` | add x28,x25,x28, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00abca4c"></a> `00abca4c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00abca50"></a> `00abca50` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00abca54"></a> `00abca54` | `35 0b 15 8b` | add x21,x25,x21, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00abca58"></a> `00abca58` | `80 47 00 b8` | str w0,[x28], #0x4 | `FALL_THROUGH`
<a id="insn-00abca5c"></a> `00abca5c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00abca60"></a> `00abca60` | `68 6c 06 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-00abca64"></a> `00abca64` | `d9 f2 3e a9` | stp x25,x28,[x22, #-0x18] | `FALL_THROUGH`
<a id="insn-00abca68"></a> `00abca68` | `d5 82 1f f8` | stur x21,[x22, #-0x8] | `FALL_THROUGH`
<a id="insn-00abca6c"></a> `00abca6c` | `37 f6 ff b4` | cbz x23,0x00abc930 | `CONDITIONAL_JUMP`
<a id="insn-00abca70"></a> `00abca70` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00abca74"></a> `00abca74` | `0f 6c 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abca78"></a> `00abca78` | `ae ff ff 17` | b 0x00abc930 | `UNCONDITIONAL_JUMP`
<a id="insn-00abca7c"></a> `00abca7c` | `80 7e 40 b9` | ldr w0,[x20, #0x7c] | `FALL_THROUGH`
<a id="insn-00abca80"></a> `00abca80` | `2b b0 f1 97` | bl 0x00728b2c | `UNCONDITIONAL_CALL`
<a id="insn-00abca84"></a> `00abca84` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00abca88"></a> `00abca88` | `91 ff ff 17` | b 0x00abc8cc | `UNCONDITIONAL_JUMP`
<a id="insn-00abca8c"></a> `00abca8c` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00abca90"></a> `00abca90` | `8f ff ff 17` | b 0x00abc8cc | `UNCONDITIONAL_JUMP`
<a id="insn-00abca94"></a> `00abca94` | `b5 03 7e a9` | ldp x21,x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abca98"></a> `00abca98` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00abca9c"></a> `00abca9c` | `40 05 00 54` | b.eq 0x00abcb44 | `CONDITIONAL_JUMP`
<a id="insn-00abcaa0"></a> `00abcaa0` | `f7 f3 01 b2` | orr x23,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00abcaa4"></a> `00abcaa4` | `fa 07 40 f9` | ldr x26,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abcaa8"></a> `00abcaa8` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00abcaac"></a> `00abcaac` | `77 55 95 f2` | movk x23,#0xaaab | `FALL_THROUGH`
<a id="insn-00abcab0"></a> `00abcab0` | `18 03 80 52` | mov w24,#0x18 | `FALL_THROUGH`
<a id="insn-00abcab4"></a> `00abcab4` | `08 00 15 cb` | sub x8,x0,x21 | `FALL_THROUGH`
<a id="insn-00abcab8"></a> `00abcab8` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00abcabc"></a> `00abcabc` | `08 7d 17 9b` | mul x8,x8,x23 | `FALL_THROUGH`
<a id="insn-00abcac0"></a> `00abcac0` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00abcac4"></a> `00abcac4` | `69 08 00 54` | b.ls 0x00abcbd0 | `CONDITIONAL_JUMP`
<a id="insn-00abcac8"></a> `00abcac8` | `c8 56 18 9b` | madd x8,x22,x24,x21 | `FALL_THROUGH`
<a id="insn-00abcacc"></a> `00abcacc` | `08 25 40 a9` | ldp x8,x9,[x8] | `FALL_THROUGH`
<a id="insn-00abcad0"></a> `00abcad0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00abcad4"></a> `00abcad4` | `00 03 00 54` | b.eq 0x00abcb34 | `CONDITIONAL_JUMP`
<a id="insn-00abcad8"></a> `00abcad8` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00abcadc"></a> `00abcadc` | `01 79 79 b8` | ldr w1,[x8, x25, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abcae0"></a> `00abcae0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abcae4"></a> `00abcae4` | `75 00 00 94` | bl 0x00abccb8 | `UNCONDITIONAL_CALL`
<a id="insn-00abcae8"></a> `00abcae8` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-00abcaec"></a> `00abcaec` | `b5 03 7e a9` | ldp x21,x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abcaf0"></a> `00abcaf0` | `09 00 15 cb` | sub x9,x0,x21 | `FALL_THROUGH`
<a id="insn-00abcaf4"></a> `00abcaf4` | `29 fd 43 93` | asr x9,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00abcaf8"></a> `00abcaf8` | `29 7d 17 9b` | mul x9,x9,x23 | `FALL_THROUGH`
<a id="insn-00abcafc"></a> `00abcafc` | `48 01 00 37` | tbnz w8,#0x0,0x00abcb24 | `CONDITIONAL_JUMP`
<a id="insn-00abcb00"></a> `00abcb00` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00abcb04"></a> `00abcb04` | `69 06 00 54` | b.ls 0x00abcbd0 | `CONDITIONAL_JUMP`
<a id="insn-00abcb08"></a> `00abcb08` | `c8 56 18 9b` | madd x8,x22,x24,x21 | `FALL_THROUGH`
<a id="insn-00abcb0c"></a> `00abcb0c` | `39 07 00 91` | add x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00abcb10"></a> `00abcb10` | `08 25 40 a9` | ldp x8,x9,[x8] | `FALL_THROUGH`
<a id="insn-00abcb14"></a> `00abcb14` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00abcb18"></a> `00abcb18` | `3f 0b 89 eb` | cmp x25,x9, ASR #0x2 | `FALL_THROUGH`
<a id="insn-00abcb1c"></a> `00abcb1c` | `03 fe ff 54` | b.cc 0x00abcadc | `CONDITIONAL_JUMP`
<a id="insn-00abcb20"></a> `00abcb20` | `05 00 00 14` | b 0x00abcb34 | `UNCONDITIONAL_JUMP`
<a id="insn-00abcb24"></a> `00abcb24` | `d6 06 00 91` | add x22,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00abcb28"></a> `00abcb28` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00abcb2c"></a> `00abcb2c` | `48 fc ff 54` | b.hi 0x00abcab4 | `CONDITIONAL_JUMP`
<a id="insn-00abcb30"></a> `00abcb30` | `07 00 00 14` | b 0x00abcb4c | `UNCONDITIONAL_JUMP`
<a id="insn-00abcb34"></a> `00abcb34` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00abcb38"></a> `00abcb38` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00abcb3c"></a> `00abcb3c` | `01 01 00 54` | b.ne 0x00abcb5c | `CONDITIONAL_JUMP`
<a id="insn-00abcb40"></a> `00abcb40` | `13 00 00 14` | b 0x00abcb8c | `UNCONDITIONAL_JUMP`
<a id="insn-00abcb44"></a> `00abcb44` | `fa 07 40 f9` | ldr x26,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abcb48"></a> `00abcb48` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abcb4c"></a> `00abcb4c` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00abcb50"></a> `00abcb50` | `f5 eb ff b4` | cbz x21,0x00abc8cc | `CONDITIONAL_JUMP`
<a id="insn-00abcb54"></a> `00abcb54` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00abcb58"></a> `00abcb58` | `a0 01 00 54` | b.eq 0x00abcb8c | `CONDITIONAL_JUMP`
<a id="insn-00abcb5c"></a> `00abcb5c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00abcb60"></a> `00abcb60` | `04 00 00 14` | b 0x00abcb70 | `UNCONDITIONAL_JUMP`
<a id="insn-00abcb64"></a> `00abcb64` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00abcb68"></a> `00abcb68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abcb6c"></a> `00abcb6c` | `e0 00 00 54` | b.eq 0x00abcb88 | `CONDITIONAL_JUMP`
<a id="insn-00abcb70"></a> `00abcb70` | `88 8e 5e f8` | ldr x8,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00abcb74"></a> `00abcb74` | `88 ff ff b4` | cbz x8,0x00abcb64 | `CONDITIONAL_JUMP`
<a id="insn-00abcb78"></a> `00abcb78` | `08 00 1f f8` | stur x8,[x0, #-0x10] | `FALL_THROUGH`
<a id="insn-00abcb7c"></a> `00abcb7c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00abcb80"></a> `00abcb80` | `cc 6b 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abcb84"></a> `00abcb84` | `f8 ff ff 17` | b 0x00abcb64 | `UNCONDITIONAL_JUMP`
<a id="insn-00abcb88"></a> `00abcb88` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abcb8c"></a> `00abcb8c` | `b5 83 1e f8` | stur x21,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00abcb90"></a> `00abcb90` | `c8 6b 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abcb94"></a> `00abcb94` | `4e ff ff 17` | b 0x00abc8cc | `UNCONDITIONAL_JUMP`
<a id="insn-00abcb98"></a> `00abcb98` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abcb9c"></a> `00abcb9c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abcba0"></a> `00abcba0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abcba4"></a> `00abcba4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abcba8"></a> `00abcba8` | `61 08 00 54` | b.ne 0x00abccb4 | `CONDITIONAL_JUMP`
<a id="insn-00abcbac"></a> `00abcbac` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00abcbb0"></a> `00abcbb0` | `00 8a e7 97` | bl 0x0049f3b0 | `CALL_TERMINATOR`
<a id="insn-00abcbb4"></a> `00abcbb4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abcbb8"></a> `00abcbb8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abcbbc"></a> `00abcbbc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abcbc0"></a> `00abcbc0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abcbc4"></a> `00abcbc4` | `81 07 00 54` | b.ne 0x00abccb4 | `CONDITIONAL_JUMP`
<a id="insn-00abcbc8"></a> `00abcbc8` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abcbcc"></a> `00abcbcc` | `ef 39 f5 97` | bl 0x0080b388 | `UNCONDITIONAL_CALL`
<a id="insn-00abcbd0"></a> `00abcbd0` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00abcbd4"></a> `00abcbd4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abcbd8"></a> `00abcbd8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abcbdc"></a> `00abcbdc` | `c1 06 00 54` | b.ne 0x00abccb4 | `CONDITIONAL_JUMP`
<a id="insn-00abcbe0"></a> `00abcbe0` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abcbe4"></a> `00abcbe4` | `e9 39 f5 97` | bl 0x0080b388 | `UNCONDITIONAL_CALL`
<a id="insn-00abcbe8"></a> `00abcbe8` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abcbec"></a> `00abcbec` | `29 15 40 f9` | ldr x9,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00abcbf0"></a> `00abcbf0` | `aa 83 5f f8` | ldur x10,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abcbf4"></a> `00abcbf4` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00abcbf8"></a> `00abcbf8` | `e1 05 00 54` | b.ne 0x00abccb4 | `CONDITIONAL_JUMP`
<a id="insn-00abcbfc"></a> `00abcbfc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00abcc00"></a> `00abcc00` | `00 cf e6 97` | bl 0x00470800 | `CALL_TERMINATOR`
<a id="insn-00abcc04"></a> `00abcc04` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abcc08"></a> `00abcc08` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abcc0c"></a> `00abcc0c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abcc10"></a> `00abcc10` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abcc14"></a> `00abcc14` | `01 05 00 54` | b.ne 0x00abccb4 | `CONDITIONAL_JUMP`
<a id="insn-00abcc18"></a> `00abcc18` | `9a 10 e6 97` | bl 0x00440e80 | `CALL_TERMINATOR`
<a id="insn-00abccb4"></a> `00abccb4` | `8b 6b 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abc6dc`](#insn-00abc6dc) 範囲 `[['00abc6dc', '00abc6df']]`
  - `FALL_THROUGH` [`00abc6dc`](#insn-00abc6dc) → [`00abc6e0`](#insn-00abc6e0)
- ブロック [`00abc6e0`](#insn-00abc6e0) 範囲 `[['00abc6e0', '00abc6f3']]`
  - `FALL_THROUGH` [`00abc6f0`](#insn-00abc6f0) → [`00abc6f4`](#insn-00abc6f4)
- ブロック [`00abc6f4`](#insn-00abc6f4) 範囲 `[['00abc6f4', '00abc707']]`
  - `FALL_THROUGH` [`00abc704`](#insn-00abc704) → [`00abc708`](#insn-00abc708)
- ブロック [`00abc708`](#insn-00abc708) 範囲 `[['00abc708', '00abc71b']]`
  - `FALL_THROUGH` [`00abc718`](#insn-00abc718) → [`00abc71c`](#insn-00abc71c)
- ブロック [`00abc71c`](#insn-00abc71c) 範囲 `[['00abc71c', '00abc72f']]`
  - `FALL_THROUGH` [`00abc72c`](#insn-00abc72c) → [`00abc730`](#insn-00abc730)
- ブロック [`00abc730`](#insn-00abc730) 範囲 `[['00abc730', '00abc733']]`
  - `CONDITIONAL_JUMP` [`00abc730`](#insn-00abc730) → [`00abc768`](#insn-00abc768)
  - `FALL_THROUGH` [`00abc730`](#insn-00abc730) → [`00abc734`](#insn-00abc734)
- ブロック [`00abc734`](#insn-00abc734) 範囲 `[['00abc734', '00abc737']]`
  - `CONDITIONAL_JUMP` [`00abc734`](#insn-00abc734) → [`00abc784`](#insn-00abc784)
  - `FALL_THROUGH` [`00abc734`](#insn-00abc734) → [`00abc738`](#insn-00abc738)
- ブロック [`00abc738`](#insn-00abc738) 範囲 `[['00abc738', '00abc73f']]`
  - `CONDITIONAL_JUMP` [`00abc73c`](#insn-00abc73c) → [`00abc8cc`](#insn-00abc8cc)
  - `FALL_THROUGH` [`00abc73c`](#insn-00abc73c) → [`00abc740`](#insn-00abc740)
- ブロック [`00abc740`](#insn-00abc740) 範囲 `[['00abc740', '00abc743']]`
  - `FALL_THROUGH` [`00abc740`](#insn-00abc740) → [`00abc744`](#insn-00abc744)
- ブロック [`00abc744`](#insn-00abc744) 範囲 `[['00abc744', '00abc74f']]`
  - `CONDITIONAL_JUMP` [`00abc74c`](#insn-00abc74c) → [`00abc7ac`](#insn-00abc7ac)
  - `FALL_THROUGH` [`00abc74c`](#insn-00abc74c) → [`00abc750`](#insn-00abc750)
- ブロック [`00abc750`](#insn-00abc750) 範囲 `[['00abc750', '00abc753']]`
  - `CONDITIONAL_JUMP` [`00abc750`](#insn-00abc750) → [`00abc7d0`](#insn-00abc7d0)
  - `FALL_THROUGH` [`00abc750`](#insn-00abc750) → [`00abc754`](#insn-00abc754)
- ブロック [`00abc754`](#insn-00abc754) 範囲 `[['00abc754', '00abc75b']]`
  - `CONDITIONAL_JUMP` [`00abc758`](#insn-00abc758) → [`00abc804`](#insn-00abc804)
  - `FALL_THROUGH` [`00abc758`](#insn-00abc758) → [`00abc75c`](#insn-00abc75c)
- ブロック [`00abc75c`](#insn-00abc75c) 範囲 `[['00abc75c', '00abc767']]`
  - `UNCONDITIONAL_JUMP` [`00abc764`](#insn-00abc764) → [`00abc7c4`](#insn-00abc7c4)
- ブロック [`00abc768`](#insn-00abc768) 範囲 `[['00abc768', '00abc76f']]`
  - `CONDITIONAL_JUMP` [`00abc76c`](#insn-00abc76c) → [`00abc798`](#insn-00abc798)
  - `FALL_THROUGH` [`00abc76c`](#insn-00abc76c) → [`00abc770`](#insn-00abc770)
- ブロック [`00abc770`](#insn-00abc770) 範囲 `[['00abc770', '00abc773']]`
  - `FALL_THROUGH` [`00abc770`](#insn-00abc770) → [`00abc774`](#insn-00abc774)
- ブロック [`00abc774`](#insn-00abc774) 範囲 `[['00abc774', '00abc777']]`
  - `CONDITIONAL_JUMP` [`00abc774`](#insn-00abc774) → [`00abc8cc`](#insn-00abc8cc)
  - `FALL_THROUGH` [`00abc774`](#insn-00abc774) → [`00abc778`](#insn-00abc778)
- ブロック [`00abc778`](#insn-00abc778) 範囲 `[['00abc778', '00abc783']]`
  - `UNCONDITIONAL_JUMP` [`00abc780`](#insn-00abc780) → [`00abc78c`](#insn-00abc78c)
- ブロック [`00abc784`](#insn-00abc784) 範囲 `[['00abc784', '00abc78b']]`
  - `FALL_THROUGH` [`00abc788`](#insn-00abc788) → [`00abc78c`](#insn-00abc78c)
- ブロック [`00abc78c`](#insn-00abc78c) 範囲 `[['00abc78c', '00abc797']]`
  - `UNCONDITIONAL_JUMP` [`00abc794`](#insn-00abc794) → [`00abc7ec`](#insn-00abc7ec)
- ブロック [`00abc798`](#insn-00abc798) 範囲 `[['00abc798', '00abc7a3']]`
  - `FALL_THROUGH` [`00abc7a0`](#insn-00abc7a0) → [`00abc7a4`](#insn-00abc7a4)
- ブロック [`00abc7a4`](#insn-00abc7a4) 範囲 `[['00abc7a4', '00abc7ab']]`
  - `UNCONDITIONAL_JUMP` [`00abc7a8`](#insn-00abc7a8) → [`00abc7ec`](#insn-00abc7ec)
- ブロック [`00abc7ac`](#insn-00abc7ac) 範囲 `[['00abc7ac', '00abc7b3']]`
  - `CONDITIONAL_JUMP` [`00abc7b0`](#insn-00abc7b0) → [`00abc7dc`](#insn-00abc7dc)
  - `FALL_THROUGH` [`00abc7b0`](#insn-00abc7b0) → [`00abc7b4`](#insn-00abc7b4)
- ブロック [`00abc7b4`](#insn-00abc7b4) 範囲 `[['00abc7b4', '00abc7bb']]`
  - `CONDITIONAL_JUMP` [`00abc7b8`](#insn-00abc7b8) → [`00abc804`](#insn-00abc804)
  - `FALL_THROUGH` [`00abc7b8`](#insn-00abc7b8) → [`00abc7bc`](#insn-00abc7bc)
- ブロック [`00abc7bc`](#insn-00abc7bc) 範囲 `[['00abc7bc', '00abc7bf']]`
  - `FALL_THROUGH` [`00abc7bc`](#insn-00abc7bc) → [`00abc7c0`](#insn-00abc7c0)
- ブロック [`00abc7c0`](#insn-00abc7c0) 範囲 `[['00abc7c0', '00abc7c3']]`
  - `FALL_THROUGH` [`00abc7c0`](#insn-00abc7c0) → [`00abc7c4`](#insn-00abc7c4)
- ブロック [`00abc7c4`](#insn-00abc7c4) 範囲 `[['00abc7c4', '00abc7c7']]`
  - `FALL_THROUGH` [`00abc7c4`](#insn-00abc7c4) → [`00abc7c8`](#insn-00abc7c8)
- ブロック [`00abc7c8`](#insn-00abc7c8) 範囲 `[['00abc7c8', '00abc7cb']]`
  - `FALL_THROUGH` [`00abc7c8`](#insn-00abc7c8) → [`00abc7cc`](#insn-00abc7cc)
- ブロック [`00abc7cc`](#insn-00abc7cc) 範囲 `[['00abc7cc', '00abc7cf']]`
  - `UNCONDITIONAL_JUMP` [`00abc7cc`](#insn-00abc7cc) → [`00abc7ec`](#insn-00abc7ec)
- ブロック [`00abc7d0`](#insn-00abc7d0) 範囲 `[['00abc7d0', '00abc7d3']]`
  - `FALL_THROUGH` [`00abc7d0`](#insn-00abc7d0) → [`00abc7d4`](#insn-00abc7d4)
- ブロック [`00abc7d4`](#insn-00abc7d4) 範囲 `[['00abc7d4', '00abc7d7']]`
  - `FALL_THROUGH` [`00abc7d4`](#insn-00abc7d4) → [`00abc7d8`](#insn-00abc7d8)
- ブロック [`00abc7d8`](#insn-00abc7d8) 範囲 `[['00abc7d8', '00abc7db']]`
  - `UNCONDITIONAL_JUMP` [`00abc7d8`](#insn-00abc7d8) → [`00abc78c`](#insn-00abc78c)
- ブロック [`00abc7dc`](#insn-00abc7dc) 範囲 `[['00abc7dc', '00abc7df']]`
  - `FALL_THROUGH` [`00abc7dc`](#insn-00abc7dc) → [`00abc7e0`](#insn-00abc7e0)
- ブロック [`00abc7e0`](#insn-00abc7e0) 範囲 `[['00abc7e0', '00abc7e3']]`
  - `FALL_THROUGH` [`00abc7e0`](#insn-00abc7e0) → [`00abc7e4`](#insn-00abc7e4)
- ブロック [`00abc7e4`](#insn-00abc7e4) 範囲 `[['00abc7e4', '00abc7e7']]`
  - `FALL_THROUGH` [`00abc7e4`](#insn-00abc7e4) → [`00abc7e8`](#insn-00abc7e8)
- ブロック [`00abc7e8`](#insn-00abc7e8) 範囲 `[['00abc7e8', '00abc7eb']]`
  - `FALL_THROUGH` [`00abc7e8`](#insn-00abc7e8) → [`00abc7ec`](#insn-00abc7ec)
- ブロック [`00abc7ec`](#insn-00abc7ec) 範囲 `[['00abc7ec', '00abc7ef']]`
  - `FALL_THROUGH` [`00abc7ec`](#insn-00abc7ec) → [`00abc7f0`](#insn-00abc7f0)
- ブロック [`00abc7f0`](#insn-00abc7f0) 範囲 `[['00abc7f0', '00abc7f3']]`
  - `FALL_THROUGH` [`00abc7f0`](#insn-00abc7f0) → [`00abc7f4`](#insn-00abc7f4)
- ブロック [`00abc7f4`](#insn-00abc7f4) 範囲 `[['00abc7f4', '00abc7f7']]`
  - `FALL_THROUGH` [`00abc7f4`](#insn-00abc7f4) → [`00abc7f8`](#insn-00abc7f8)
- ブロック [`00abc7f8`](#insn-00abc7f8) 範囲 `[['00abc7f8', '00abc803']]`
  - `FALL_THROUGH` [`00abc800`](#insn-00abc800) → [`00abc804`](#insn-00abc804)
- ブロック [`00abc804`](#insn-00abc804) 範囲 `[['00abc804', '00abc807']]`
  - `FALL_THROUGH` [`00abc804`](#insn-00abc804) → [`00abc808`](#insn-00abc808)
- ブロック [`00abc808`](#insn-00abc808) 範囲 `[['00abc808', '00abc813']]`
  - `CONDITIONAL_JUMP` [`00abc810`](#insn-00abc810) → [`00abc824`](#insn-00abc824)
  - `FALL_THROUGH` [`00abc810`](#insn-00abc810) → [`00abc814`](#insn-00abc814)
- ブロック [`00abc814`](#insn-00abc814) 範囲 `[['00abc814', '00abc81f']]`
  - `CONDITIONAL_JUMP` [`00abc81c`](#insn-00abc81c) → [`00abc808`](#insn-00abc808)
  - `FALL_THROUGH` [`00abc81c`](#insn-00abc81c) → [`00abc820`](#insn-00abc820)
- ブロック [`00abc820`](#insn-00abc820) 範囲 `[['00abc820', '00abc823']]`
  - `FALL_THROUGH` [`00abc820`](#insn-00abc820) → [`00abc824`](#insn-00abc824)
- ブロック [`00abc824`](#insn-00abc824) 範囲 `[['00abc824', '00abc82b']]`
  - `CONDITIONAL_JUMP` [`00abc828`](#insn-00abc828) → [`00abc8c8`](#insn-00abc8c8)
  - `FALL_THROUGH` [`00abc828`](#insn-00abc828) → [`00abc82c`](#insn-00abc82c)
- ブロック [`00abc82c`](#insn-00abc82c) 範囲 `[['00abc82c', '00abc837']]`
  - `CONDITIONAL_JUMP` [`00abc834`](#insn-00abc834) → [`00abc860`](#insn-00abc860)
  - `FALL_THROUGH` [`00abc834`](#insn-00abc834) → [`00abc838`](#insn-00abc838)
- ブロック [`00abc838`](#insn-00abc838) 範囲 `[['00abc838', '00abc83b']]`
  - `CONDITIONAL_JUMP` [`00abc838`](#insn-00abc838) → [`00abc908`](#insn-00abc908)
  - `FALL_THROUGH` [`00abc838`](#insn-00abc838) → [`00abc83c`](#insn-00abc83c)
- ブロック [`00abc83c`](#insn-00abc83c) 範囲 `[['00abc83c', '00abc843']]`
  - `CONDITIONAL_JUMP` [`00abc840`](#insn-00abc840) → [`00abc8c8`](#insn-00abc8c8)
  - `FALL_THROUGH` [`00abc840`](#insn-00abc840) → [`00abc844`](#insn-00abc844)
- ブロック [`00abc844`](#insn-00abc844) 範囲 `[['00abc844', '00abc85f']]`
  - `UNCONDITIONAL_JUMP` [`00abc85c`](#insn-00abc85c) → [`00abc8cc`](#insn-00abc8cc)
- ブロック [`00abc860`](#insn-00abc860) 範囲 `[['00abc860', '00abc863']]`
  - `FALL_THROUGH` [`00abc860`](#insn-00abc860) → [`00abc864`](#insn-00abc864)
- ブロック [`00abc864`](#insn-00abc864) 範囲 `[['00abc864', '00abc867']]`
  - `CONDITIONAL_JUMP` [`00abc864`](#insn-00abc864) → [`00abca7c`](#insn-00abca7c)
  - `FALL_THROUGH` [`00abc864`](#insn-00abc864) → [`00abc868`](#insn-00abc868)
- ブロック [`00abc868`](#insn-00abc868) 範囲 `[['00abc868', '00abc86f']]`
  - `CONDITIONAL_JUMP` [`00abc86c`](#insn-00abc86c) → [`00abc8c8`](#insn-00abc8c8)
  - `FALL_THROUGH` [`00abc86c`](#insn-00abc86c) → [`00abc870`](#insn-00abc870)
- ブロック [`00abc870`](#insn-00abc870) 範囲 `[['00abc870', '00abc87b']]`
  - `CONDITIONAL_JUMP` [`00abc878`](#insn-00abc878) → [`00abca8c`](#insn-00abca8c)
  - `FALL_THROUGH` [`00abc878`](#insn-00abc878) → [`00abc87c`](#insn-00abc87c)
- ブロック [`00abc87c`](#insn-00abc87c) 範囲 `[['00abc87c', '00abc883']]`
  - `FALL_THROUGH` [`00abc880`](#insn-00abc880) → [`00abc884`](#insn-00abc884)
- ブロック [`00abc884`](#insn-00abc884) 範囲 `[['00abc884', '00abc8a3']]`
  - `FALL_THROUGH` [`00abc8a0`](#insn-00abc8a0) → [`00abc8a4`](#insn-00abc8a4)
- ブロック [`00abc8a4`](#insn-00abc8a4) 範囲 `[['00abc8a4', '00abc8af']]`
  - `CONDITIONAL_JUMP` [`00abc8ac`](#insn-00abc8ac) → [`00abc8cc`](#insn-00abc8cc)
  - `FALL_THROUGH` [`00abc8ac`](#insn-00abc8ac) → [`00abc8b0`](#insn-00abc8b0)
- ブロック [`00abc8b0`](#insn-00abc8b0) 範囲 `[['00abc8b0', '00abc8b7']]`
  - `FALL_THROUGH` [`00abc8b4`](#insn-00abc8b4) → [`00abc8b8`](#insn-00abc8b8)
- ブロック [`00abc8b8`](#insn-00abc8b8) 範囲 `[['00abc8b8', '00abc8bb']]`
  - `FALL_THROUGH` [`00abc8b8`](#insn-00abc8b8) → [`00abc8bc`](#insn-00abc8bc)
- ブロック [`00abc8bc`](#insn-00abc8bc) 範囲 `[['00abc8bc', '00abc8bf']]`
  - `FALL_THROUGH` [`00abc8bc`](#insn-00abc8bc) → [`00abc8c0`](#insn-00abc8c0)
- ブロック [`00abc8c0`](#insn-00abc8c0) 範囲 `[['00abc8c0', '00abc8c3']]`
  - `CONDITIONAL_JUMP` [`00abc8c0`](#insn-00abc8c0) → [`00abc884`](#insn-00abc884)
  - `FALL_THROUGH` [`00abc8c0`](#insn-00abc8c0) → [`00abc8c4`](#insn-00abc8c4)
- ブロック [`00abc8c4`](#insn-00abc8c4) 範囲 `[['00abc8c4', '00abc8c7']]`
  - `UNCONDITIONAL_JUMP` [`00abc8c4`](#insn-00abc8c4) → [`00abc8cc`](#insn-00abc8cc)
- ブロック [`00abc8c8`](#insn-00abc8c8) 範囲 `[['00abc8c8', '00abc8cb']]`
  - `FALL_THROUGH` [`00abc8c8`](#insn-00abc8c8) → [`00abc8cc`](#insn-00abc8cc)
- ブロック [`00abc8cc`](#insn-00abc8cc) 範囲 `[['00abc8cc', '00abc8e3']]`
  - `CONDITIONAL_JUMP` [`00abc8e0`](#insn-00abc8e0) → [`00abccb4`](#insn-00abccb4)
  - `FALL_THROUGH` [`00abc8e0`](#insn-00abc8e0) → [`00abc8e4`](#insn-00abc8e4)
- ブロック [`00abc8e4`](#insn-00abc8e4) 範囲 `[['00abc8e4', '00abc907']]`
- ブロック [`00abc908`](#insn-00abc908) 範囲 `[['00abc908', '00abc90f']]`
  - `FALL_THROUGH` [`00abc90c`](#insn-00abc90c) → [`00abc910`](#insn-00abc910)
- ブロック [`00abc910`](#insn-00abc910) 範囲 `[['00abc910', '00abc91f']]`
  - `CONDITIONAL_JUMP` [`00abc91c`](#insn-00abc91c) → [`00abca8c`](#insn-00abca8c)
  - `FALL_THROUGH` [`00abc91c`](#insn-00abc91c) → [`00abc920`](#insn-00abc920)
- ブロック [`00abc920`](#insn-00abc920) 範囲 `[['00abc920', '00abc92b']]`
  - `UNCONDITIONAL_JUMP` [`00abc928`](#insn-00abc928) → [`00abc948`](#insn-00abc948)
- ブロック [`00abc92c`](#insn-00abc92c) 範囲 `[['00abc92c', '00abc92f']]`
  - `FALL_THROUGH` [`00abc92c`](#insn-00abc92c) → [`00abc930`](#insn-00abc930)
- ブロック [`00abc930`](#insn-00abc930) 範囲 `[['00abc930', '00abc947']]`
  - `CONDITIONAL_JUMP` [`00abc944`](#insn-00abc944) → [`00abca94`](#insn-00abca94)
  - `FALL_THROUGH` [`00abc944`](#insn-00abc944) → [`00abc948`](#insn-00abc948)
- ブロック [`00abc948`](#insn-00abc948) 範囲 `[['00abc948', '00abc953']]`
  - `CONDITIONAL_JUMP` [`00abc950`](#insn-00abc950) → [`00abc9b4`](#insn-00abc9b4)
  - `FALL_THROUGH` [`00abc950`](#insn-00abc950) → [`00abc954`](#insn-00abc954)
- ブロック [`00abc954`](#insn-00abc954) 範囲 `[['00abc954', '00abc95f']]`
  - `FALL_THROUGH` [`00abc95c`](#insn-00abc95c) → [`00abc960`](#insn-00abc960)
- ブロック [`00abc960`](#insn-00abc960) 範囲 `[['00abc960', '00abc967']]`
  - `CONDITIONAL_JUMP` [`00abc964`](#insn-00abc964) → [`00abc98c`](#insn-00abc98c)
  - `FALL_THROUGH` [`00abc964`](#insn-00abc964) → [`00abc968`](#insn-00abc968)
- ブロック [`00abc968`](#insn-00abc968) 範囲 `[['00abc968', '00abc98b']]`
  - `UNCONDITIONAL_JUMP` [`00abc988`](#insn-00abc988) → [`00abc9b4`](#insn-00abc9b4)
- ブロック [`00abc98c`](#insn-00abc98c) 範囲 `[['00abc98c', '00abc9a7']]`
  - `CONDITIONAL_JUMP` [`00abc9a4`](#insn-00abc9a4) → [`00abc9b4`](#insn-00abc9b4)
  - `FALL_THROUGH` [`00abc9a4`](#insn-00abc9a4) → [`00abc9a8`](#insn-00abc9a8)
- ブロック [`00abc9a8`](#insn-00abc9a8) 範囲 `[['00abc9a8', '00abc9af']]`
  - `FALL_THROUGH` [`00abc9ac`](#insn-00abc9ac) → [`00abc9b0`](#insn-00abc9b0)
- ブロック [`00abc9b0`](#insn-00abc9b0) 範囲 `[['00abc9b0', '00abc9b3']]`
  - `FALL_THROUGH` [`00abc9b0`](#insn-00abc9b0) → [`00abc9b4`](#insn-00abc9b4)
- ブロック [`00abc9b4`](#insn-00abc9b4) 範囲 `[['00abc9b4', '00abc9bf']]`
  - `CONDITIONAL_JUMP` [`00abc9bc`](#insn-00abc9bc) → [`00abcbb4`](#insn-00abcbb4)
  - `FALL_THROUGH` [`00abc9bc`](#insn-00abc9bc) → [`00abc9c0`](#insn-00abc9c0)
- ブロック [`00abc9c0`](#insn-00abc9c0) 範囲 `[['00abc9c0', '00abc9cf']]`
  - `CONDITIONAL_JUMP` [`00abc9cc`](#insn-00abc9cc) → [`00abcb98`](#insn-00abcb98)
  - `FALL_THROUGH` [`00abc9cc`](#insn-00abc9cc) → [`00abc9d0`](#insn-00abc9d0)
- ブロック [`00abc9d0`](#insn-00abc9d0) 範囲 `[['00abc9d0', '00abc9d3']]`
  - `FALL_THROUGH` [`00abc9d0`](#insn-00abc9d0) → [`00abc9d4`](#insn-00abc9d4)
- ブロック [`00abc9d4`](#insn-00abc9d4) 範囲 `[['00abc9d4', '00abc9e3']]`
  - `CONDITIONAL_JUMP` [`00abc9e0`](#insn-00abc9e0) → [`00abc92c`](#insn-00abc92c)
  - `FALL_THROUGH` [`00abc9e0`](#insn-00abc9e0) → [`00abc9e4`](#insn-00abc9e4)
- ブロック [`00abc9e4`](#insn-00abc9e4) 範囲 `[['00abc9e4', '00abc9f7']]`
  - `FALL_THROUGH` [`00abc9f4`](#insn-00abc9f4) → [`00abc9f8`](#insn-00abc9f8)
- ブロック [`00abc9f8`](#insn-00abc9f8) 範囲 `[['00abc9f8', '00abc9ff']]`
  - `CONDITIONAL_JUMP` [`00abc9fc`](#insn-00abc9fc) → [`00abcbe8`](#insn-00abcbe8)
  - `FALL_THROUGH` [`00abc9fc`](#insn-00abc9fc) → [`00abca00`](#insn-00abca00)
- ブロック [`00abca00`](#insn-00abca00) 範囲 `[['00abca00', '00abca1b']]`
  - `FALL_THROUGH` [`00abca18`](#insn-00abca18) → [`00abca1c`](#insn-00abca1c)
- ブロック [`00abca1c`](#insn-00abca1c) 範囲 `[['00abca1c', '00abca23']]`
  - `CONDITIONAL_JUMP` [`00abca20`](#insn-00abca20) → [`00abca44`](#insn-00abca44)
  - `FALL_THROUGH` [`00abca20`](#insn-00abca20) → [`00abca24`](#insn-00abca24)
- ブロック [`00abca24`](#insn-00abca24) 範囲 `[['00abca24', '00abca2b']]`
  - `CONDITIONAL_JUMP` [`00abca28`](#insn-00abca28) → [`00abcc04`](#insn-00abcc04)
  - `FALL_THROUGH` [`00abca28`](#insn-00abca28) → [`00abca2c`](#insn-00abca2c)
- ブロック [`00abca2c`](#insn-00abca2c) 範囲 `[['00abca2c', '00abca43']]`
  - `UNCONDITIONAL_JUMP` [`00abca40`](#insn-00abca40) → [`00abca48`](#insn-00abca48)
- ブロック [`00abca44`](#insn-00abca44) 範囲 `[['00abca44', '00abca47']]`
  - `FALL_THROUGH` [`00abca44`](#insn-00abca44) → [`00abca48`](#insn-00abca48)
- ブロック [`00abca48`](#insn-00abca48) 範囲 `[['00abca48', '00abca5f']]`
  - `FALL_THROUGH` [`00abca5c`](#insn-00abca5c) → [`00abca60`](#insn-00abca60)
- ブロック [`00abca60`](#insn-00abca60) 範囲 `[['00abca60', '00abca6f']]`
  - `CONDITIONAL_JUMP` [`00abca6c`](#insn-00abca6c) → [`00abc930`](#insn-00abc930)
  - `FALL_THROUGH` [`00abca6c`](#insn-00abca6c) → [`00abca70`](#insn-00abca70)
- ブロック [`00abca70`](#insn-00abca70) 範囲 `[['00abca70', '00abca7b']]`
  - `UNCONDITIONAL_JUMP` [`00abca78`](#insn-00abca78) → [`00abc930`](#insn-00abc930)
- ブロック [`00abca7c`](#insn-00abca7c) 範囲 `[['00abca7c', '00abca8b']]`
  - `UNCONDITIONAL_JUMP` [`00abca88`](#insn-00abca88) → [`00abc8cc`](#insn-00abc8cc)
- ブロック [`00abca8c`](#insn-00abca8c) 範囲 `[['00abca8c', '00abca93']]`
  - `UNCONDITIONAL_JUMP` [`00abca90`](#insn-00abca90) → [`00abc8cc`](#insn-00abc8cc)
- ブロック [`00abca94`](#insn-00abca94) 範囲 `[['00abca94', '00abca9f']]`
  - `CONDITIONAL_JUMP` [`00abca9c`](#insn-00abca9c) → [`00abcb44`](#insn-00abcb44)
  - `FALL_THROUGH` [`00abca9c`](#insn-00abca9c) → [`00abcaa0`](#insn-00abcaa0)
- ブロック [`00abcaa0`](#insn-00abcaa0) 範囲 `[['00abcaa0', '00abcaa3']]`
  - `FALL_THROUGH` [`00abcaa0`](#insn-00abcaa0) → [`00abcaa4`](#insn-00abcaa4)
- ブロック [`00abcaa4`](#insn-00abcaa4) 範囲 `[['00abcaa4', '00abcab3']]`
  - `FALL_THROUGH` [`00abcab0`](#insn-00abcab0) → [`00abcab4`](#insn-00abcab4)
- ブロック [`00abcab4`](#insn-00abcab4) 範囲 `[['00abcab4', '00abcac7']]`
  - `CONDITIONAL_JUMP` [`00abcac4`](#insn-00abcac4) → [`00abcbd0`](#insn-00abcbd0)
  - `FALL_THROUGH` [`00abcac4`](#insn-00abcac4) → [`00abcac8`](#insn-00abcac8)
- ブロック [`00abcac8`](#insn-00abcac8) 範囲 `[['00abcac8', '00abcad7']]`
  - `CONDITIONAL_JUMP` [`00abcad4`](#insn-00abcad4) → [`00abcb34`](#insn-00abcb34)
  - `FALL_THROUGH` [`00abcad4`](#insn-00abcad4) → [`00abcad8`](#insn-00abcad8)
- ブロック [`00abcad8`](#insn-00abcad8) 範囲 `[['00abcad8', '00abcadb']]`
  - `FALL_THROUGH` [`00abcad8`](#insn-00abcad8) → [`00abcadc`](#insn-00abcadc)
- ブロック [`00abcadc`](#insn-00abcadc) 範囲 `[['00abcadc', '00abcae7']]`
  - `FALL_THROUGH` [`00abcae4`](#insn-00abcae4) → [`00abcae8`](#insn-00abcae8)
- ブロック [`00abcae8`](#insn-00abcae8) 範囲 `[['00abcae8', '00abcaff']]`
  - `CONDITIONAL_JUMP` [`00abcafc`](#insn-00abcafc) → [`00abcb24`](#insn-00abcb24)
  - `FALL_THROUGH` [`00abcafc`](#insn-00abcafc) → [`00abcb00`](#insn-00abcb00)
- ブロック [`00abcb00`](#insn-00abcb00) 範囲 `[['00abcb00', '00abcb07']]`
  - `CONDITIONAL_JUMP` [`00abcb04`](#insn-00abcb04) → [`00abcbd0`](#insn-00abcbd0)
  - `FALL_THROUGH` [`00abcb04`](#insn-00abcb04) → [`00abcb08`](#insn-00abcb08)
- ブロック [`00abcb08`](#insn-00abcb08) 範囲 `[['00abcb08', '00abcb17']]`
  - `FALL_THROUGH` [`00abcb14`](#insn-00abcb14) → [`00abcb18`](#insn-00abcb18)
- ブロック [`00abcb18`](#insn-00abcb18) 範囲 `[['00abcb18', '00abcb1f']]`
  - `CONDITIONAL_JUMP` [`00abcb1c`](#insn-00abcb1c) → [`00abcadc`](#insn-00abcadc)
  - `FALL_THROUGH` [`00abcb1c`](#insn-00abcb1c) → [`00abcb20`](#insn-00abcb20)
- ブロック [`00abcb20`](#insn-00abcb20) 範囲 `[['00abcb20', '00abcb23']]`
  - `UNCONDITIONAL_JUMP` [`00abcb20`](#insn-00abcb20) → [`00abcb34`](#insn-00abcb34)
- ブロック [`00abcb24`](#insn-00abcb24) 範囲 `[['00abcb24', '00abcb2f']]`
  - `CONDITIONAL_JUMP` [`00abcb2c`](#insn-00abcb2c) → [`00abcab4`](#insn-00abcab4)
  - `FALL_THROUGH` [`00abcb2c`](#insn-00abcb2c) → [`00abcb30`](#insn-00abcb30)
- ブロック [`00abcb30`](#insn-00abcb30) 範囲 `[['00abcb30', '00abcb33']]`
  - `UNCONDITIONAL_JUMP` [`00abcb30`](#insn-00abcb30) → [`00abcb4c`](#insn-00abcb4c)
- ブロック [`00abcb34`](#insn-00abcb34) 範囲 `[['00abcb34', '00abcb37']]`
  - `FALL_THROUGH` [`00abcb34`](#insn-00abcb34) → [`00abcb38`](#insn-00abcb38)
- ブロック [`00abcb38`](#insn-00abcb38) 範囲 `[['00abcb38', '00abcb3b']]`
  - `FALL_THROUGH` [`00abcb38`](#insn-00abcb38) → [`00abcb3c`](#insn-00abcb3c)
- ブロック [`00abcb3c`](#insn-00abcb3c) 範囲 `[['00abcb3c', '00abcb3f']]`
  - `CONDITIONAL_JUMP` [`00abcb3c`](#insn-00abcb3c) → [`00abcb5c`](#insn-00abcb5c)
  - `FALL_THROUGH` [`00abcb3c`](#insn-00abcb3c) → [`00abcb40`](#insn-00abcb40)
- ブロック [`00abcb40`](#insn-00abcb40) 範囲 `[['00abcb40', '00abcb43']]`
  - `UNCONDITIONAL_JUMP` [`00abcb40`](#insn-00abcb40) → [`00abcb8c`](#insn-00abcb8c)
- ブロック [`00abcb44`](#insn-00abcb44) 範囲 `[['00abcb44', '00abcb4b']]`
  - `FALL_THROUGH` [`00abcb48`](#insn-00abcb48) → [`00abcb4c`](#insn-00abcb4c)
- ブロック [`00abcb4c`](#insn-00abcb4c) 範囲 `[['00abcb4c', '00abcb4f']]`
  - `FALL_THROUGH` [`00abcb4c`](#insn-00abcb4c) → [`00abcb50`](#insn-00abcb50)
- ブロック [`00abcb50`](#insn-00abcb50) 範囲 `[['00abcb50', '00abcb53']]`
  - `CONDITIONAL_JUMP` [`00abcb50`](#insn-00abcb50) → [`00abc8cc`](#insn-00abc8cc)
  - `FALL_THROUGH` [`00abcb50`](#insn-00abcb50) → [`00abcb54`](#insn-00abcb54)
- ブロック [`00abcb54`](#insn-00abcb54) 範囲 `[['00abcb54', '00abcb57']]`
  - `FALL_THROUGH` [`00abcb54`](#insn-00abcb54) → [`00abcb58`](#insn-00abcb58)
- ブロック [`00abcb58`](#insn-00abcb58) 範囲 `[['00abcb58', '00abcb5b']]`
  - `CONDITIONAL_JUMP` [`00abcb58`](#insn-00abcb58) → [`00abcb8c`](#insn-00abcb8c)
  - `FALL_THROUGH` [`00abcb58`](#insn-00abcb58) → [`00abcb5c`](#insn-00abcb5c)
- ブロック [`00abcb5c`](#insn-00abcb5c) 範囲 `[['00abcb5c', '00abcb5f']]`
  - `FALL_THROUGH` [`00abcb5c`](#insn-00abcb5c) → [`00abcb60`](#insn-00abcb60)
- ブロック [`00abcb60`](#insn-00abcb60) 範囲 `[['00abcb60', '00abcb63']]`
  - `UNCONDITIONAL_JUMP` [`00abcb60`](#insn-00abcb60) → [`00abcb70`](#insn-00abcb70)
- ブロック [`00abcb64`](#insn-00abcb64) 範囲 `[['00abcb64', '00abcb6f']]`
  - `CONDITIONAL_JUMP` [`00abcb6c`](#insn-00abcb6c) → [`00abcb88`](#insn-00abcb88)
  - `FALL_THROUGH` [`00abcb6c`](#insn-00abcb6c) → [`00abcb70`](#insn-00abcb70)
- ブロック [`00abcb70`](#insn-00abcb70) 範囲 `[['00abcb70', '00abcb77']]`
  - `CONDITIONAL_JUMP` [`00abcb74`](#insn-00abcb74) → [`00abcb64`](#insn-00abcb64)
  - `FALL_THROUGH` [`00abcb74`](#insn-00abcb74) → [`00abcb78`](#insn-00abcb78)
- ブロック [`00abcb78`](#insn-00abcb78) 範囲 `[['00abcb78', '00abcb7f']]`
  - `FALL_THROUGH` [`00abcb7c`](#insn-00abcb7c) → [`00abcb80`](#insn-00abcb80)
- ブロック [`00abcb80`](#insn-00abcb80) 範囲 `[['00abcb80', '00abcb83']]`
  - `FALL_THROUGH` [`00abcb80`](#insn-00abcb80) → [`00abcb84`](#insn-00abcb84)
- ブロック [`00abcb84`](#insn-00abcb84) 範囲 `[['00abcb84', '00abcb87']]`
  - `UNCONDITIONAL_JUMP` [`00abcb84`](#insn-00abcb84) → [`00abcb64`](#insn-00abcb64)
- ブロック [`00abcb88`](#insn-00abcb88) 範囲 `[['00abcb88', '00abcb8b']]`
  - `FALL_THROUGH` [`00abcb88`](#insn-00abcb88) → [`00abcb8c`](#insn-00abcb8c)
- ブロック [`00abcb8c`](#insn-00abcb8c) 範囲 `[['00abcb8c', '00abcb97']]`
  - `UNCONDITIONAL_JUMP` [`00abcb94`](#insn-00abcb94) → [`00abc8cc`](#insn-00abc8cc)
- ブロック [`00abcb98`](#insn-00abcb98) 範囲 `[['00abcb98', '00abcbab']]`
  - `CONDITIONAL_JUMP` [`00abcba8`](#insn-00abcba8) → [`00abccb4`](#insn-00abccb4)
  - `FALL_THROUGH` [`00abcba8`](#insn-00abcba8) → [`00abcbac`](#insn-00abcbac)
- ブロック [`00abcbac`](#insn-00abcbac) 範囲 `[['00abcbac', '00abcbb3']]`
- ブロック [`00abcbb4`](#insn-00abcbb4) 範囲 `[['00abcbb4', '00abcbc7']]`
  - `CONDITIONAL_JUMP` [`00abcbc4`](#insn-00abcbc4) → [`00abccb4`](#insn-00abccb4)
  - `FALL_THROUGH` [`00abcbc4`](#insn-00abcbc4) → [`00abcbc8`](#insn-00abcbc8)
- ブロック [`00abcbc8`](#insn-00abcbc8) 範囲 `[['00abcbc8', '00abcbcf']]`
  - `FALL_THROUGH` [`00abcbcc`](#insn-00abcbcc) → [`00abcbd0`](#insn-00abcbd0)
- ブロック [`00abcbd0`](#insn-00abcbd0) 範囲 `[['00abcbd0', '00abcbdf']]`
  - `CONDITIONAL_JUMP` [`00abcbdc`](#insn-00abcbdc) → [`00abccb4`](#insn-00abccb4)
  - `FALL_THROUGH` [`00abcbdc`](#insn-00abcbdc) → [`00abcbe0`](#insn-00abcbe0)
- ブロック [`00abcbe0`](#insn-00abcbe0) 範囲 `[['00abcbe0', '00abcbe7']]`
  - `FALL_THROUGH` [`00abcbe4`](#insn-00abcbe4) → [`00abcbe8`](#insn-00abcbe8)
- ブロック [`00abcbe8`](#insn-00abcbe8) 範囲 `[['00abcbe8', '00abcbfb']]`
  - `CONDITIONAL_JUMP` [`00abcbf8`](#insn-00abcbf8) → [`00abccb4`](#insn-00abccb4)
  - `FALL_THROUGH` [`00abcbf8`](#insn-00abcbf8) → [`00abcbfc`](#insn-00abcbfc)
- ブロック [`00abcbfc`](#insn-00abcbfc) 範囲 `[['00abcbfc', '00abcc03']]`
- ブロック [`00abcc04`](#insn-00abcc04) 範囲 `[['00abcc04', '00abcc17']]`
  - `CONDITIONAL_JUMP` [`00abcc14`](#insn-00abcc14) → [`00abccb4`](#insn-00abccb4)
  - `FALL_THROUGH` [`00abcc14`](#insn-00abcc14) → [`00abcc18`](#insn-00abcc18)
- ブロック [`00abcc18`](#insn-00abcc18) 範囲 `[['00abcc18', '00abcc1b']]`
- ブロック [`00abccb4`](#insn-00abccb4) 範囲 `[['00abccb4', '00abccb7']]`

## 命令位置別の参照

- [`00abc6e0`](#insn-00abc6e0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc6e4`](#insn-00abc6e4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc6e8`](#insn-00abc6e8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc6ec`](#insn-00abc6ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc6f0`](#insn-00abc6f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc6f4`](#insn-00abc6f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc710`](#insn-00abc710) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc718`](#insn-00abc718) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abc730`](#insn-00abc730) → [`00abc768`](#insn-00abc768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc734`](#insn-00abc734) → [`00abc784`](#insn-00abc784) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc73c`](#insn-00abc73c) → [`00abc8cc`](#insn-00abc8cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc74c`](#insn-00abc74c) → [`00abc7ac`](#insn-00abc7ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc750`](#insn-00abc750) → [`00abc7d0`](#insn-00abc7d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc758`](#insn-00abc758) → [`00abc804`](#insn-00abc804) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc760`](#insn-00abc760) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abc764`](#insn-00abc764) → [`00abc7c4`](#insn-00abc7c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc76c`](#insn-00abc76c) → [`00abc798`](#insn-00abc798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc774`](#insn-00abc774) → [`00abc8cc`](#insn-00abc8cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc77c`](#insn-00abc77c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abc780`](#insn-00abc780) → [`00abc78c`](#insn-00abc78c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc788`](#insn-00abc788) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abc794`](#insn-00abc794) → [`00abc7ec`](#insn-00abc7ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc79c`](#insn-00abc79c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abc7a8`](#insn-00abc7a8) → [`00abc7ec`](#insn-00abc7ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc7b0`](#insn-00abc7b0) → [`00abc7dc`](#insn-00abc7dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc7b8`](#insn-00abc7b8) → [`00abc804`](#insn-00abc804) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc7c0`](#insn-00abc7c0) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abc7cc`](#insn-00abc7cc) → [`00abc7ec`](#insn-00abc7ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc7d4`](#insn-00abc7d4) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abc7d8`](#insn-00abc7d8) → [`00abc78c`](#insn-00abc78c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc7e0`](#insn-00abc7e0) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abc7fc`](#insn-00abc7fc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abc810`](#insn-00abc810) → [`00abc824`](#insn-00abc824) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc81c`](#insn-00abc81c) → [`00abc808`](#insn-00abc808) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc828`](#insn-00abc828) → [`00abc8c8`](#insn-00abc8c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc834`](#insn-00abc834) → [`00abc860`](#insn-00abc860) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc838`](#insn-00abc838) → [`00abc908`](#insn-00abc908) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc840`](#insn-00abc840) → [`00abc8c8`](#insn-00abc8c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc84c`](#insn-00abc84c) → [`00abce14`](00abce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00abce14` · 推定シンボル `None` · 推定型 `None`
- [`00abc85c`](#insn-00abc85c) → [`00abc8cc`](#insn-00abc8cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc864`](#insn-00abc864) → [`00abca7c`](#insn-00abca7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc86c`](#insn-00abc86c) → [`00abc8c8`](#insn-00abc8c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc878`](#insn-00abc878) → [`00abca8c`](#insn-00abca8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc894`](#insn-00abc894) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00abc8ac`](#insn-00abc8ac) → [`00abc8cc`](#insn-00abc8cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc8c0`](#insn-00abc8c0) → [`00abc884`](#insn-00abc884) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc8c4`](#insn-00abc8c4) → [`00abc8cc`](#insn-00abc8cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc8d0`](#insn-00abc8d0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abc8d8`](#insn-00abc8d8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc8e0`](#insn-00abc8e0) → [`00abccb4`](#insn-00abccb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc8e8`](#insn-00abc8e8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc8ec`](#insn-00abc8ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc8f0`](#insn-00abc8f0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc8f4`](#insn-00abc8f4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc8f8`](#insn-00abc8f8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc8fc`](#insn-00abc8fc) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc90c`](#insn-00abc90c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc914`](#insn-00abc914) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc91c`](#insn-00abc91c) → [`00abca8c`](#insn-00abca8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc924`](#insn-00abc924) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc928`](#insn-00abc928) → [`00abc948`](#insn-00abc948) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc944`](#insn-00abc944) → [`00abca94`](#insn-00abca94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc94c`](#insn-00abc94c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc950`](#insn-00abc950) → [`00abc9b4`](#insn-00abc9b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc954`](#insn-00abc954) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc958`](#insn-00abc958) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc95c`](#insn-00abc95c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc964`](#insn-00abc964) → [`00abc98c`](#insn-00abc98c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc970`](#insn-00abc970) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc978`](#insn-00abc978) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc984`](#insn-00abc984) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc988`](#insn-00abc988) → [`00abc9b4`](#insn-00abc9b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc994`](#insn-00abc994) → [`00615c90`](../00615/00615c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00615c90` · 推定シンボル `None` · 推定型 `None`
- [`00abc99c`](#insn-00abc99c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc9a0`](#insn-00abc9a0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc9a4`](#insn-00abc9a4) → [`00abc9b4`](#insn-00abc9b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc9a8`](#insn-00abc9a8) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc9ac`](#insn-00abc9ac) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abc9b0`](#insn-00abc9b0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc9b4`](#insn-00abc9b4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc9bc`](#insn-00abc9bc) → [`00abcbb4`](#insn-00abcbb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc9cc`](#insn-00abc9cc) → [`00abcb98`](#insn-00abcb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc9d4`](#insn-00abc9d4) → [`0046da08`](../0046d/0046da08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046da08` · 推定シンボル `None` · 推定型 `None`
- [`00abc9e0`](#insn-00abc9e0) → [`00abc92c`](#insn-00abc92c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abc9fc`](#insn-00abc9fc) → [`00abcbe8`](#insn-00abcbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abca20`](#insn-00abca20) → [`00abca44`](#insn-00abca44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abca28`](#insn-00abca28) → [`00abcc04`](#insn-00abcc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abca34`](#insn-00abca34) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abca40`](#insn-00abca40) → [`00abca48`](#insn-00abca48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abca60`](#insn-00abca60) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`00abca6c`](#insn-00abca6c) → [`00abc930`](#insn-00abc930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abca74`](#insn-00abca74) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abca78`](#insn-00abca78) → [`00abc930`](#insn-00abc930) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abca80`](#insn-00abca80) → [`00728b2c`](../00728/00728b2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00728b2c` · 推定シンボル `None` · 推定型 `None`
- [`00abca88`](#insn-00abca88) → [`00abc8cc`](#insn-00abc8cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abca90`](#insn-00abca90) → [`00abc8cc`](#insn-00abc8cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abca94`](#insn-00abca94) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abca9c`](#insn-00abca9c) → [`00abcb44`](#insn-00abcb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcaa4`](#insn-00abcaa4) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcac4`](#insn-00abcac4) → [`00abcbd0`](#insn-00abcbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcad4`](#insn-00abcad4) → [`00abcb34`](#insn-00abcb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcae4`](#insn-00abcae4) → [`00abccb8`](00abccb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00abccb8` · 推定シンボル `None` · 推定型 `None`
- [`00abcaec`](#insn-00abcaec) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcafc`](#insn-00abcafc) → [`00abcb24`](#insn-00abcb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb04`](#insn-00abcb04) → [`00abcbd0`](#insn-00abcbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb1c`](#insn-00abcb1c) → [`00abcadc`](#insn-00abcadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb20`](#insn-00abcb20) → [`00abcb34`](#insn-00abcb34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb2c`](#insn-00abcb2c) → [`00abcab4`](#insn-00abcab4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb30`](#insn-00abcb30) → [`00abcb4c`](#insn-00abcb4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb3c`](#insn-00abcb3c) → [`00abcb5c`](#insn-00abcb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb40`](#insn-00abcb40) → [`00abcb8c`](#insn-00abcb8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb44`](#insn-00abcb44) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb50`](#insn-00abcb50) → [`00abc8cc`](#insn-00abc8cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb58`](#insn-00abcb58) → [`00abcb8c`](#insn-00abcb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb60`](#insn-00abcb60) → [`00abcb70`](#insn-00abcb70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb6c`](#insn-00abcb6c) → [`00abcb88`](#insn-00abcb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb74`](#insn-00abcb74) → [`00abcb64`](#insn-00abcb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb80`](#insn-00abcb80) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abcb84`](#insn-00abcb84) → [`00abcb64`](#insn-00abcb64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb88`](#insn-00abcb88) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb8c`](#insn-00abcb8c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb90`](#insn-00abcb90) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abcb94`](#insn-00abcb94) → [`00abc8cc`](#insn-00abc8cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcb98`](#insn-00abcb98) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcba0`](#insn-00abcba0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcba8`](#insn-00abcba8) → [`00abccb4`](#insn-00abccb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcbac`](#insn-00abcbac) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcbb0`](#insn-00abcbb0) → [`0049f3b0`](../0049f/0049f3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0049f3b0` · 推定シンボル `None` · 推定型 `None`
- [`00abcbb4`](#insn-00abcbb4) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcbbc`](#insn-00abcbbc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcbc4`](#insn-00abcbc4) → [`00abccb4`](#insn-00abccb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcbcc`](#insn-00abcbcc) → [`0080b388`](../0080b/0080b388.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0080b388` · 推定シンボル `None` · 推定型 `None`
- [`00abcbd4`](#insn-00abcbd4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcbdc`](#insn-00abcbdc) → [`00abccb4`](#insn-00abccb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcbe4`](#insn-00abcbe4) → [`0080b388`](../0080b/0080b388.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0080b388` · 推定シンボル `None` · 推定型 `None`
- [`00abcbe8`](#insn-00abcbe8) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcbf0`](#insn-00abcbf0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcbf8`](#insn-00abcbf8) → [`00abccb4`](#insn-00abccb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcc00`](#insn-00abcc00) → [`00470800`](../00470/00470800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470800` · 推定シンボル `None` · 推定型 `None`
- [`00abcc04`](#insn-00abcc04) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcc0c`](#insn-00abcc0c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcc14`](#insn-00abcc14) → [`00abccb4`](#insn-00abccb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcc18`](#insn-00abcc18) → [`00440e80`](../00440/00440e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440e80` · 推定シンボル `None` · 推定型 `None`
- [`00abccb4`](#insn-00abccb4) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abc6e0`](#insn-00abc6e0)

~~~json
{
  "source": "00abc6e0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc6e4`](#insn-00abc6e4)

~~~json
{
  "source": "00abc6e4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc6e8`](#insn-00abc6e8)

~~~json
{
  "source": "00abc6e8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc6ec`](#insn-00abc6ec)

~~~json
{
  "source": "00abc6ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc6f0`](#insn-00abc6f0)

~~~json
{
  "source": "00abc6f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc6f4`](#insn-00abc6f4)

~~~json
{
  "source": "00abc6f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc710`](#insn-00abc710)

~~~json
{
  "source": "00abc710",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc718`](#insn-00abc718)

~~~json
{
  "source": "00abc718",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc730`](#insn-00abc730)

~~~json
{
  "source": "00abc730",
  "target": "00abc768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc734`](#insn-00abc734)

~~~json
{
  "source": "00abc734",
  "target": "00abc784",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc73c`](#insn-00abc73c)

~~~json
{
  "source": "00abc73c",
  "target": "00abc8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc74c`](#insn-00abc74c)

~~~json
{
  "source": "00abc74c",
  "target": "00abc7ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc750`](#insn-00abc750)

~~~json
{
  "source": "00abc750",
  "target": "00abc7d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc758`](#insn-00abc758)

~~~json
{
  "source": "00abc758",
  "target": "00abc804",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc760`](#insn-00abc760)

~~~json
{
  "source": "00abc760",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc764`](#insn-00abc764)

~~~json
{
  "source": "00abc764",
  "target": "00abc7c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc76c`](#insn-00abc76c)

~~~json
{
  "source": "00abc76c",
  "target": "00abc798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc774`](#insn-00abc774)

~~~json
{
  "source": "00abc774",
  "target": "00abc8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc77c`](#insn-00abc77c)

~~~json
{
  "source": "00abc77c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc780`](#insn-00abc780)

~~~json
{
  "source": "00abc780",
  "target": "00abc78c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc788`](#insn-00abc788)

~~~json
{
  "source": "00abc788",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc794`](#insn-00abc794)

~~~json
{
  "source": "00abc794",
  "target": "00abc7ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc79c`](#insn-00abc79c)

~~~json
{
  "source": "00abc79c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc7a8`](#insn-00abc7a8)

~~~json
{
  "source": "00abc7a8",
  "target": "00abc7ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc7b0`](#insn-00abc7b0)

~~~json
{
  "source": "00abc7b0",
  "target": "00abc7dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc7b8`](#insn-00abc7b8)

~~~json
{
  "source": "00abc7b8",
  "target": "00abc804",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc7c0`](#insn-00abc7c0)

~~~json
{
  "source": "00abc7c0",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc7cc`](#insn-00abc7cc)

~~~json
{
  "source": "00abc7cc",
  "target": "00abc7ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc7d4`](#insn-00abc7d4)

~~~json
{
  "source": "00abc7d4",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc7d8`](#insn-00abc7d8)

~~~json
{
  "source": "00abc7d8",
  "target": "00abc78c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc7e0`](#insn-00abc7e0)

~~~json
{
  "source": "00abc7e0",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc7fc`](#insn-00abc7fc)

~~~json
{
  "source": "00abc7fc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc810`](#insn-00abc810)

~~~json
{
  "source": "00abc810",
  "target": "00abc824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc81c`](#insn-00abc81c)

~~~json
{
  "source": "00abc81c",
  "target": "00abc808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc828`](#insn-00abc828)

~~~json
{
  "source": "00abc828",
  "target": "00abc8c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc834`](#insn-00abc834)

~~~json
{
  "source": "00abc834",
  "target": "00abc860",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc838`](#insn-00abc838)

~~~json
{
  "source": "00abc838",
  "target": "00abc908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc840`](#insn-00abc840)

~~~json
{
  "source": "00abc840",
  "target": "00abc8c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc84c`](#insn-00abc84c)

~~~json
{
  "source": "00abc84c",
  "target": "00abce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc85c`](#insn-00abc85c)

~~~json
{
  "source": "00abc85c",
  "target": "00abc8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc864`](#insn-00abc864)

~~~json
{
  "source": "00abc864",
  "target": "00abca7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc86c`](#insn-00abc86c)

~~~json
{
  "source": "00abc86c",
  "target": "00abc8c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc878`](#insn-00abc878)

~~~json
{
  "source": "00abc878",
  "target": "00abca8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc894`](#insn-00abc894)

~~~json
{
  "source": "00abc894",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc8ac`](#insn-00abc8ac)

~~~json
{
  "source": "00abc8ac",
  "target": "00abc8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc8c0`](#insn-00abc8c0)

~~~json
{
  "source": "00abc8c0",
  "target": "00abc884",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc8c4`](#insn-00abc8c4)

~~~json
{
  "source": "00abc8c4",
  "target": "00abc8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc8d0`](#insn-00abc8d0)

~~~json
{
  "source": "00abc8d0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc8d8`](#insn-00abc8d8)

~~~json
{
  "source": "00abc8d8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc8e0`](#insn-00abc8e0)

~~~json
{
  "source": "00abc8e0",
  "target": "00abccb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc8e8`](#insn-00abc8e8)

~~~json
{
  "source": "00abc8e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc8ec`](#insn-00abc8ec)

~~~json
{
  "source": "00abc8ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc8f0`](#insn-00abc8f0)

~~~json
{
  "source": "00abc8f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc8f4`](#insn-00abc8f4)

~~~json
{
  "source": "00abc8f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc8f8`](#insn-00abc8f8)

~~~json
{
  "source": "00abc8f8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc8fc`](#insn-00abc8fc)

~~~json
{
  "source": "00abc8fc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc90c`](#insn-00abc90c)

~~~json
{
  "source": "00abc90c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc914`](#insn-00abc914)

~~~json
{
  "source": "00abc914",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc91c`](#insn-00abc91c)

~~~json
{
  "source": "00abc91c",
  "target": "00abca8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc924`](#insn-00abc924)

~~~json
{
  "source": "00abc924",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc928`](#insn-00abc928)

~~~json
{
  "source": "00abc928",
  "target": "00abc948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc944`](#insn-00abc944)

~~~json
{
  "source": "00abc944",
  "target": "00abca94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc94c`](#insn-00abc94c)

~~~json
{
  "source": "00abc94c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc950`](#insn-00abc950)

~~~json
{
  "source": "00abc950",
  "target": "00abc9b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc954`](#insn-00abc954)

~~~json
{
  "source": "00abc954",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc958`](#insn-00abc958)

~~~json
{
  "source": "00abc958",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc95c`](#insn-00abc95c)

~~~json
{
  "source": "00abc95c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc964`](#insn-00abc964)

~~~json
{
  "source": "00abc964",
  "target": "00abc98c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc970`](#insn-00abc970)

~~~json
{
  "source": "00abc970",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc978`](#insn-00abc978)

~~~json
{
  "source": "00abc978",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc984`](#insn-00abc984)

~~~json
{
  "source": "00abc984",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc988`](#insn-00abc988)

~~~json
{
  "source": "00abc988",
  "target": "00abc9b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc994`](#insn-00abc994)

~~~json
{
  "source": "00abc994",
  "target": "00615c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc99c`](#insn-00abc99c)

~~~json
{
  "source": "00abc99c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc9a0`](#insn-00abc9a0)

~~~json
{
  "source": "00abc9a0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc9a4`](#insn-00abc9a4)

~~~json
{
  "source": "00abc9a4",
  "target": "00abc9b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc9a8`](#insn-00abc9a8)

~~~json
{
  "source": "00abc9a8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc9ac`](#insn-00abc9ac)

~~~json
{
  "source": "00abc9ac",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc9b0`](#insn-00abc9b0)

~~~json
{
  "source": "00abc9b0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc9b4`](#insn-00abc9b4)

~~~json
{
  "source": "00abc9b4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc9bc`](#insn-00abc9bc)

~~~json
{
  "source": "00abc9bc",
  "target": "00abcbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc9cc`](#insn-00abc9cc)

~~~json
{
  "source": "00abc9cc",
  "target": "00abcb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc9d4`](#insn-00abc9d4)

~~~json
{
  "source": "00abc9d4",
  "target": "0046da08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abc9e0`](#insn-00abc9e0)

~~~json
{
  "source": "00abc9e0",
  "target": "00abc92c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abc9fc`](#insn-00abc9fc)

~~~json
{
  "source": "00abc9fc",
  "target": "00abcbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abca20`](#insn-00abca20)

~~~json
{
  "source": "00abca20",
  "target": "00abca44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abca28`](#insn-00abca28)

~~~json
{
  "source": "00abca28",
  "target": "00abcc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abca34`](#insn-00abca34)

~~~json
{
  "source": "00abca34",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abca40`](#insn-00abca40)

~~~json
{
  "source": "00abca40",
  "target": "00abca48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abca60`](#insn-00abca60)

~~~json
{
  "source": "00abca60",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abca6c`](#insn-00abca6c)

~~~json
{
  "source": "00abca6c",
  "target": "00abc930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abca74`](#insn-00abca74)

~~~json
{
  "source": "00abca74",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abca78`](#insn-00abca78)

~~~json
{
  "source": "00abca78",
  "target": "00abc930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abca80`](#insn-00abca80)

~~~json
{
  "source": "00abca80",
  "target": "00728b2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abca88`](#insn-00abca88)

~~~json
{
  "source": "00abca88",
  "target": "00abc8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abca90`](#insn-00abca90)

~~~json
{
  "source": "00abca90",
  "target": "00abc8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abca94`](#insn-00abca94)

~~~json
{
  "source": "00abca94",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abca9c`](#insn-00abca9c)

~~~json
{
  "source": "00abca9c",
  "target": "00abcb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcaa4`](#insn-00abcaa4)

~~~json
{
  "source": "00abcaa4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcac4`](#insn-00abcac4)

~~~json
{
  "source": "00abcac4",
  "target": "00abcbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcad4`](#insn-00abcad4)

~~~json
{
  "source": "00abcad4",
  "target": "00abcb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcae4`](#insn-00abcae4)

~~~json
{
  "source": "00abcae4",
  "target": "00abccb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcaec`](#insn-00abcaec)

~~~json
{
  "source": "00abcaec",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcafc`](#insn-00abcafc)

~~~json
{
  "source": "00abcafc",
  "target": "00abcb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb04`](#insn-00abcb04)

~~~json
{
  "source": "00abcb04",
  "target": "00abcbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb1c`](#insn-00abcb1c)

~~~json
{
  "source": "00abcb1c",
  "target": "00abcadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb20`](#insn-00abcb20)

~~~json
{
  "source": "00abcb20",
  "target": "00abcb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb2c`](#insn-00abcb2c)

~~~json
{
  "source": "00abcb2c",
  "target": "00abcab4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb30`](#insn-00abcb30)

~~~json
{
  "source": "00abcb30",
  "target": "00abcb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb3c`](#insn-00abcb3c)

~~~json
{
  "source": "00abcb3c",
  "target": "00abcb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb40`](#insn-00abcb40)

~~~json
{
  "source": "00abcb40",
  "target": "00abcb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb44`](#insn-00abcb44)

~~~json
{
  "source": "00abcb44",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb50`](#insn-00abcb50)

~~~json
{
  "source": "00abcb50",
  "target": "00abc8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb58`](#insn-00abcb58)

~~~json
{
  "source": "00abcb58",
  "target": "00abcb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb60`](#insn-00abcb60)

~~~json
{
  "source": "00abcb60",
  "target": "00abcb70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb6c`](#insn-00abcb6c)

~~~json
{
  "source": "00abcb6c",
  "target": "00abcb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb74`](#insn-00abcb74)

~~~json
{
  "source": "00abcb74",
  "target": "00abcb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb80`](#insn-00abcb80)

~~~json
{
  "source": "00abcb80",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcb84`](#insn-00abcb84)

~~~json
{
  "source": "00abcb84",
  "target": "00abcb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb88`](#insn-00abcb88)

~~~json
{
  "source": "00abcb88",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb8c`](#insn-00abcb8c)

~~~json
{
  "source": "00abcb8c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb90`](#insn-00abcb90)

~~~json
{
  "source": "00abcb90",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcb94`](#insn-00abcb94)

~~~json
{
  "source": "00abcb94",
  "target": "00abc8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcb98`](#insn-00abcb98)

~~~json
{
  "source": "00abcb98",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcba0`](#insn-00abcba0)

~~~json
{
  "source": "00abcba0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcba8`](#insn-00abcba8)

~~~json
{
  "source": "00abcba8",
  "target": "00abccb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcbac`](#insn-00abcbac)

~~~json
{
  "source": "00abcbac",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcbb0`](#insn-00abcbb0)

~~~json
{
  "source": "00abcbb0",
  "target": "0049f3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcbb4`](#insn-00abcbb4)

~~~json
{
  "source": "00abcbb4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcbbc`](#insn-00abcbbc)

~~~json
{
  "source": "00abcbbc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcbc4`](#insn-00abcbc4)

~~~json
{
  "source": "00abcbc4",
  "target": "00abccb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcbcc`](#insn-00abcbcc)

~~~json
{
  "source": "00abcbcc",
  "target": "0080b388",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcbd4`](#insn-00abcbd4)

~~~json
{
  "source": "00abcbd4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcbdc`](#insn-00abcbdc)

~~~json
{
  "source": "00abcbdc",
  "target": "00abccb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcbe4`](#insn-00abcbe4)

~~~json
{
  "source": "00abcbe4",
  "target": "0080b388",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcbe8`](#insn-00abcbe8)

~~~json
{
  "source": "00abcbe8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcbf0`](#insn-00abcbf0)

~~~json
{
  "source": "00abcbf0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcbf8`](#insn-00abcbf8)

~~~json
{
  "source": "00abcbf8",
  "target": "00abccb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcc00`](#insn-00abcc00)

~~~json
{
  "source": "00abcc00",
  "target": "00470800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcc04`](#insn-00abcc04)

~~~json
{
  "source": "00abcc04",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcc0c`](#insn-00abcc0c)

~~~json
{
  "source": "00abcc0c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcc14`](#insn-00abcc14)

~~~json
{
  "source": "00abcc14",
  "target": "00abccb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcc18`](#insn-00abcc18)

~~~json
{
  "source": "00abcc18",
  "target": "00440e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abccb4`](#insn-00abccb4)

~~~json
{
  "source": "00abccb4",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
