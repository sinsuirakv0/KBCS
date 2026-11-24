# 009affcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `009af020`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af020.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0024.md#compare-06d98bfbc40232158a8ca06d372c084e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009affcc",
  "name": "FUN_009affcc",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "868aad525f352bf1349955cd8a519282f42c4a47ca1046fd14b57b0abeefb72b",
  "source_text_sha256": "868aad525f352bf1349955cd8a519282f42c4a47ca1046fd14b57b0abeefb72b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009affcc",
        "009b00fb"
      ],
      [
        "009b0120",
        "009b0123"
      ]
    ],
    "bytes_sha256": "50fb24a644707d3e311356a48a6585b4ae26bca82052ee79930a5373c9ac6336",
    "instruction_count": 77,
    "instruction_bytes": 308,
    "body_bytes": 308,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [0076a1b8](../0076a/0076a1b8.md)

## 呼び出し先

- [009b6ca4](../009b6/009b6ca4.md)
- [009b6ce8](../009b6/009b6ce8.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4419 bytes

~~~c

void FUN_009affcc(long *param_1)

{
  undefined8 *puVar1;
  long lVar2;
  int iVar3;
  ulong uVar4;
  long lVar5;
  undefined8 uVar6;
  long lVar7;
  ulong uVar8;
  long *plVar9;
  
                    /* try { // try from 009affe0 to 00aaffe7 has its CatchHandler @ 009b0048 */
  lVar2 = tpidr_el0;
                    /* catch() { ... } // from try @ 009afba0 with catch @ 009affe8
                       try { // try from 009affe8 to 00ab00b7 has its CatchHandler @ 009af808 */
  lVar7 = *(long *)(lVar2 + 0x28);
                    /* catch() { ... } // from try @ 009afb64 with catch @ 009afff0 */
                    /* catch() { ... } // from try @ 009afb54 with catch @ 009afff4 */
  lVar5 = *param_1;
                    /* catch() { ... } // from try @ 009afeac with catch @ 009afffc */
  if (param_1[1] != lVar5) {
                    /* catch() { ... } // from try @ 009afa50 with catch @ 009b0000
                       catch() { ... } // from try @ 009afe9c with catch @ 009b0000 */
    uVar8 = 0;
    do {
                    /* catch() { ... } // from try @ 009afb38 with catch @ 009b001c */
      puVar1 = (undefined8 *)(lVar5 + uVar8 * 0x10);
      plVar9 = (long *)puVar1[1];
      uVar6 = *puVar1;
                    /* catch() { ... } // from try @ 009afe90 with catch @ 009b0020 */
                    /* catch() { ... } // from try @ 009afccc with catch @ 009b0024 */
                    /* catch() { ... } // from try @ 009afbec with catch @ 009b0028 */
      if (plVar9 != (long *)0x0) {
                    /* catch() { ... } // from try @ 009afeec with catch @ 009b002c */
                    /* catch() { ... } // from try @ 009afe54 with catch @ 009b0034 */
        FUN_00c54d60(1,plVar9 + 1);
                    /* catch() { ... } // from try @ 009aff04 with catch @ 009b003c */
      }
                    /* catch() { ... } // from try @ 009afc48 with catch @ 009b0040 */
                    /* catch() { ... } // from try @ 009af99c with catch @ 009b0044 */
                    /* catch() { ... } // from try @ 009afdb8 with catch @ 009b0048
                       catch() { ... } // from try @ 009affe0 with catch @ 009b0048 */
      iVar3 = FUN_009b6ca4(uVar6);
                    /* catch() { ... } // from try @ 009afde4 with catch @ 009b0050 */
      if ((iVar3 == 4) && (uVar4 = FUN_009b6ce8(uVar6), (uVar4 & 1) != 0)) {
        *(int *)((long)param_1 + 0x1c) = (int)uVar8;
        if ((plVar9 != (long *)0x0) &&
           (lVar5 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)) {
                    /* try { // try from 009b00b8 to 00ab023f has its CatchHandler @ 009b00b8
                       catch() { ... } // from try @ 009b00b8 with catch @ 009b00b8
                       catch() { ... } // from try @ 009b0300 with catch @ 009b00b8
                       catch() { ... } // from try @ 009b0594 with catch @ 009b00b8
                       catch() { ... } // from try @ 009b0654 with catch @ 009b00b8
                       catch() { ... } // from try @ 009b07e4 with catch @ 009b00b8
                       catch() { ... } // from try @ 009b0870 with catch @ 009b00b8 */
          (**(code **)(*plVar9 + 0x10))(plVar9);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
        }
        uVar6 = 1;
        goto LAB_009b00d4;
      }
                    /* catch() { ... } // from try @ 009afcf0 with catch @ 009b0060
                       catch() { ... } // from try @ 009affc8 with catch @ 009b0060 */
                    /* catch() { ... } // from try @ 009afd38 with catch @ 009b0068 */
      if ((plVar9 != (long *)0x0) &&
         (lVar5 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
                    /* catch() { ... } // from try @ 009afbd4 with catch @ 009b0008 */
      lVar5 = *param_1;
      uVar8 = uVar8 + 1;
                    /* catch() { ... } // from try @ 009afa0c with catch @ 009b0010 */
                    /* catch() { ... } // from try @ 009af9fc with catch @ 009b0014 */
    } while (uVar8 < (ulong)(param_1[1] - lVar5 >> 4));
  }
  uVar6 = 0;
  *(undefined4 *)((long)param_1 + 0x1c) = 0xffffffff;
LAB_009b00d4:
  if (*(long *)(lVar2 + 0x28) == lVar7) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar6);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009affcc"></a> `009affcc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009affd0"></a> `009affd0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009affd4"></a> `009affd4` | `f7 23 00 f9` | str x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009affd8"></a> `009affd8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009affdc"></a> `009affdc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009affe0"></a> `009affe0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-009affe4"></a> `009affe4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009affe8"></a> `009affe8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009affec"></a> `009affec` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-009afff0"></a> `009afff0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009afff4"></a> `009afff4` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-009afff8"></a> `009afff8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-009afffc"></a> `009afffc` | `a0 04 00 54` | b.eq 0x009b0090 | `CONDITIONAL_JUMP`
<a id="insn-009b0000"></a> `009b0000` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-009b0004"></a> `009b0004` | `06 00 00 14` | b 0x009b001c | `UNCONDITIONAL_JUMP`
<a id="insn-009b0008"></a> `009b0008` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-009b000c"></a> `009b000c` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-009b0010"></a> `009b0010` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-009b0014"></a> `009b0014` | `ff 12 89 eb` | cmp x23,x9, ASR #0x4 | `FALL_THROUGH`
<a id="insn-009b0018"></a> `009b0018` | `c2 03 00 54` | b.cs 0x009b0090 | `CONDITIONAL_JUMP`
<a id="insn-009b001c"></a> `009b001c` | `00 79 f7 3c` | ldr q0,[x8,x23, lsl #4] | `FALL_THROUGH`
<a id="insn-009b0020"></a> `009b0020` | `14 3c 18 4e` | mov x20,v0.D[0x1] | `FALL_THROUGH`
<a id="insn-009b0024"></a> `009b0024` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009b0028"></a> `009b0028` | `d4 00 00 b4` | cbz x20,0x009b0040 | `CONDITIONAL_JUMP`
<a id="insn-009b002c"></a> `009b002c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009b0030"></a> `009b0030` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009b0034"></a> `009b0034` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-009b0038"></a> `009b0038` | `4a 93 0a 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-009b003c"></a> `009b003c` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-009b0040"></a> `009b0040` | `15 00 66 9e` | fmov x21,d0 | `FALL_THROUGH`
<a id="insn-009b0044"></a> `009b0044` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009b0048"></a> `009b0048` | `17 1b 00 94` | bl 0x009b6ca4 | `UNCONDITIONAL_CALL`
<a id="insn-009b004c"></a> `009b004c` | `1f 10 00 71` | cmp w0,#0x4 | `FALL_THROUGH`
<a id="insn-009b0050"></a> `009b0050` | `81 00 00 54` | b.ne 0x009b0060 | `CONDITIONAL_JUMP`
<a id="insn-009b0054"></a> `009b0054` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009b0058"></a> `009b0058` | `24 1b 00 94` | bl 0x009b6ce8 | `UNCONDITIONAL_CALL`
<a id="insn-009b005c"></a> `009b005c` | `20 02 00 37` | tbnz w0,#0x0,0x009b00a0 | `CONDITIONAL_JUMP`
<a id="insn-009b0060"></a> `009b0060` | `54 fd ff b4` | cbz x20,0x009b0008 | `CONDITIONAL_JUMP`
<a id="insn-009b0064"></a> `009b0064` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009b0068"></a> `009b0068` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009b006c"></a> `009b006c` | `49 93 0a 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-009b0070"></a> `009b0070` | `c0 fc ff b5` | cbnz x0,0x009b0008 | `CONDITIONAL_JUMP`
<a id="insn-009b0074"></a> `009b0074` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009b0078"></a> `009b0078` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009b007c"></a> `009b007c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009b0080"></a> `009b0080` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009b0084"></a> `009b0084` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009b0088"></a> `009b0088` | `a6 a3 0a 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-009b008c"></a> `009b008c` | `df ff ff 17` | b 0x009b0008 | `UNCONDITIONAL_JUMP`
<a id="insn-009b0090"></a> `009b0090` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-009b0094"></a> `009b0094` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-009b0098"></a> `009b0098` | `68 1e 00 b9` | str w8,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-009b009c"></a> `009b009c` | `0e 00 00 14` | b 0x009b00d4 | `UNCONDITIONAL_JUMP`
<a id="insn-009b00a0"></a> `009b00a0` | `77 1e 00 b9` | str w23,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-009b00a4"></a> `009b00a4` | `74 01 00 b4` | cbz x20,0x009b00d0 | `CONDITIONAL_JUMP`
<a id="insn-009b00a8"></a> `009b00a8` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009b00ac"></a> `009b00ac` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009b00b0"></a> `009b00b0` | `38 93 0a 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-009b00b4"></a> `009b00b4` | `e0 00 00 b5` | cbnz x0,0x009b00d0 | `CONDITIONAL_JUMP`
<a id="insn-009b00b8"></a> `009b00b8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009b00bc"></a> `009b00bc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009b00c0"></a> `009b00c0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009b00c4"></a> `009b00c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009b00c8"></a> `009b00c8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009b00cc"></a> `009b00cc` | `95 a3 0a 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-009b00d0"></a> `009b00d0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009b00d4"></a> `009b00d4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-009b00d8"></a> `009b00d8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009b00dc"></a> `009b00dc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009b00e0"></a> `009b00e0` | `01 02 00 54` | b.ne 0x009b0120 | `CONDITIONAL_JUMP`
<a id="insn-009b00e4"></a> `009b00e4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009b00e8"></a> `009b00e8` | `f7 23 40 f9` | ldr x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009b00ec"></a> `009b00ec` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009b00f0"></a> `009b00f0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009b00f4"></a> `009b00f4` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009b00f8"></a> `009b00f8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009b0120"></a> `009b0120` | `98 a3 0a 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009affcc`](#insn-009affcc) 範囲 `[['009affcc', '009affdf']]`
  - `FALL_THROUGH` [`009affdc`](#insn-009affdc) → [`009affe0`](#insn-009affe0)
- ブロック [`009affe0`](#insn-009affe0) 範囲 `[['009affe0', '009affe7']]`
  - `FALL_THROUGH` [`009affe4`](#insn-009affe4) → [`009affe8`](#insn-009affe8)
- ブロック [`009affe8`](#insn-009affe8) 範囲 `[['009affe8', '009affef']]`
  - `FALL_THROUGH` [`009affec`](#insn-009affec) → [`009afff0`](#insn-009afff0)
- ブロック [`009afff0`](#insn-009afff0) 範囲 `[['009afff0', '009afff3']]`
  - `FALL_THROUGH` [`009afff0`](#insn-009afff0) → [`009afff4`](#insn-009afff4)
- ブロック [`009afff4`](#insn-009afff4) 範囲 `[['009afff4', '009afffb']]`
  - `FALL_THROUGH` [`009afff8`](#insn-009afff8) → [`009afffc`](#insn-009afffc)
- ブロック [`009afffc`](#insn-009afffc) 範囲 `[['009afffc', '009affff']]`
  - `CONDITIONAL_JUMP` [`009afffc`](#insn-009afffc) → [`009b0090`](#insn-009b0090)
  - `FALL_THROUGH` [`009afffc`](#insn-009afffc) → [`009b0000`](#insn-009b0000)
- ブロック [`009b0000`](#insn-009b0000) 範囲 `[['009b0000', '009b0007']]`
  - `UNCONDITIONAL_JUMP` [`009b0004`](#insn-009b0004) → [`009b001c`](#insn-009b001c)
- ブロック [`009b0008`](#insn-009b0008) 範囲 `[['009b0008', '009b000f']]`
  - `FALL_THROUGH` [`009b000c`](#insn-009b000c) → [`009b0010`](#insn-009b0010)
- ブロック [`009b0010`](#insn-009b0010) 範囲 `[['009b0010', '009b0013']]`
  - `FALL_THROUGH` [`009b0010`](#insn-009b0010) → [`009b0014`](#insn-009b0014)
- ブロック [`009b0014`](#insn-009b0014) 範囲 `[['009b0014', '009b001b']]`
  - `CONDITIONAL_JUMP` [`009b0018`](#insn-009b0018) → [`009b0090`](#insn-009b0090)
  - `FALL_THROUGH` [`009b0018`](#insn-009b0018) → [`009b001c`](#insn-009b001c)
- ブロック [`009b001c`](#insn-009b001c) 範囲 `[['009b001c', '009b001f']]`
  - `FALL_THROUGH` [`009b001c`](#insn-009b001c) → [`009b0020`](#insn-009b0020)
- ブロック [`009b0020`](#insn-009b0020) 範囲 `[['009b0020', '009b0023']]`
  - `FALL_THROUGH` [`009b0020`](#insn-009b0020) → [`009b0024`](#insn-009b0024)
- ブロック [`009b0024`](#insn-009b0024) 範囲 `[['009b0024', '009b0027']]`
  - `FALL_THROUGH` [`009b0024`](#insn-009b0024) → [`009b0028`](#insn-009b0028)
- ブロック [`009b0028`](#insn-009b0028) 範囲 `[['009b0028', '009b002b']]`
  - `CONDITIONAL_JUMP` [`009b0028`](#insn-009b0028) → [`009b0040`](#insn-009b0040)
  - `FALL_THROUGH` [`009b0028`](#insn-009b0028) → [`009b002c`](#insn-009b002c)
- ブロック [`009b002c`](#insn-009b002c) 範囲 `[['009b002c', '009b0033']]`
  - `FALL_THROUGH` [`009b0030`](#insn-009b0030) → [`009b0034`](#insn-009b0034)
- ブロック [`009b0034`](#insn-009b0034) 範囲 `[['009b0034', '009b003b']]`
  - `FALL_THROUGH` [`009b0038`](#insn-009b0038) → [`009b003c`](#insn-009b003c)
- ブロック [`009b003c`](#insn-009b003c) 範囲 `[['009b003c', '009b003f']]`
  - `FALL_THROUGH` [`009b003c`](#insn-009b003c) → [`009b0040`](#insn-009b0040)
- ブロック [`009b0040`](#insn-009b0040) 範囲 `[['009b0040', '009b0043']]`
  - `FALL_THROUGH` [`009b0040`](#insn-009b0040) → [`009b0044`](#insn-009b0044)
- ブロック [`009b0044`](#insn-009b0044) 範囲 `[['009b0044', '009b0047']]`
  - `FALL_THROUGH` [`009b0044`](#insn-009b0044) → [`009b0048`](#insn-009b0048)
- ブロック [`009b0048`](#insn-009b0048) 範囲 `[['009b0048', '009b004f']]`
  - `FALL_THROUGH` [`009b004c`](#insn-009b004c) → [`009b0050`](#insn-009b0050)
- ブロック [`009b0050`](#insn-009b0050) 範囲 `[['009b0050', '009b0053']]`
  - `CONDITIONAL_JUMP` [`009b0050`](#insn-009b0050) → [`009b0060`](#insn-009b0060)
  - `FALL_THROUGH` [`009b0050`](#insn-009b0050) → [`009b0054`](#insn-009b0054)
- ブロック [`009b0054`](#insn-009b0054) 範囲 `[['009b0054', '009b005f']]`
  - `CONDITIONAL_JUMP` [`009b005c`](#insn-009b005c) → [`009b00a0`](#insn-009b00a0)
  - `FALL_THROUGH` [`009b005c`](#insn-009b005c) → [`009b0060`](#insn-009b0060)
- ブロック [`009b0060`](#insn-009b0060) 範囲 `[['009b0060', '009b0063']]`
  - `CONDITIONAL_JUMP` [`009b0060`](#insn-009b0060) → [`009b0008`](#insn-009b0008)
  - `FALL_THROUGH` [`009b0060`](#insn-009b0060) → [`009b0064`](#insn-009b0064)
- ブロック [`009b0064`](#insn-009b0064) 範囲 `[['009b0064', '009b0067']]`
  - `FALL_THROUGH` [`009b0064`](#insn-009b0064) → [`009b0068`](#insn-009b0068)
- ブロック [`009b0068`](#insn-009b0068) 範囲 `[['009b0068', '009b0073']]`
  - `CONDITIONAL_JUMP` [`009b0070`](#insn-009b0070) → [`009b0008`](#insn-009b0008)
  - `FALL_THROUGH` [`009b0070`](#insn-009b0070) → [`009b0074`](#insn-009b0074)
- ブロック [`009b0074`](#insn-009b0074) 範囲 `[['009b0074', '009b008f']]`
  - `UNCONDITIONAL_JUMP` [`009b008c`](#insn-009b008c) → [`009b0008`](#insn-009b0008)
- ブロック [`009b0090`](#insn-009b0090) 範囲 `[['009b0090', '009b009f']]`
  - `UNCONDITIONAL_JUMP` [`009b009c`](#insn-009b009c) → [`009b00d4`](#insn-009b00d4)
- ブロック [`009b00a0`](#insn-009b00a0) 範囲 `[['009b00a0', '009b00a7']]`
  - `CONDITIONAL_JUMP` [`009b00a4`](#insn-009b00a4) → [`009b00d0`](#insn-009b00d0)
  - `FALL_THROUGH` [`009b00a4`](#insn-009b00a4) → [`009b00a8`](#insn-009b00a8)
- ブロック [`009b00a8`](#insn-009b00a8) 範囲 `[['009b00a8', '009b00b7']]`
  - `CONDITIONAL_JUMP` [`009b00b4`](#insn-009b00b4) → [`009b00d0`](#insn-009b00d0)
  - `FALL_THROUGH` [`009b00b4`](#insn-009b00b4) → [`009b00b8`](#insn-009b00b8)
- ブロック [`009b00b8`](#insn-009b00b8) 範囲 `[['009b00b8', '009b00cf']]`
  - `FALL_THROUGH` [`009b00cc`](#insn-009b00cc) → [`009b00d0`](#insn-009b00d0)
- ブロック [`009b00d0`](#insn-009b00d0) 範囲 `[['009b00d0', '009b00d3']]`
  - `FALL_THROUGH` [`009b00d0`](#insn-009b00d0) → [`009b00d4`](#insn-009b00d4)
- ブロック [`009b00d4`](#insn-009b00d4) 範囲 `[['009b00d4', '009b00e3']]`
  - `CONDITIONAL_JUMP` [`009b00e0`](#insn-009b00e0) → [`009b0120`](#insn-009b0120)
  - `FALL_THROUGH` [`009b00e0`](#insn-009b00e0) → [`009b00e4`](#insn-009b00e4)
- ブロック [`009b00e4`](#insn-009b00e4) 範囲 `[['009b00e4', '009b00fb']]`
- ブロック [`009b0120`](#insn-009b0120) 範囲 `[['009b0120', '009b0123']]`

## 命令位置別の参照

- [`009affd0`](#insn-009affd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affd4`](#insn-009affd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affd8`](#insn-009affd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affdc`](#insn-009affdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009afff0`](#insn-009afff0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009afffc`](#insn-009afffc) → [`009b0090`](#insn-009b0090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0004`](#insn-009b0004) → [`009b001c`](#insn-009b001c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0018`](#insn-009b0018) → [`009b0090`](#insn-009b0090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0024`](#insn-009b0024) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0028`](#insn-009b0028) → [`009b0040`](#insn-009b0040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0034`](#insn-009b0034) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0038`](#insn-009b0038) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`009b003c`](#insn-009b003c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0048`](#insn-009b0048) → [`009b6ca4`](../009b6/009b6ca4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b6ca4` · 推定シンボル `None` · 推定型 `None`
- [`009b0050`](#insn-009b0050) → [`009b0060`](#insn-009b0060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0058`](#insn-009b0058) → [`009b6ce8`](../009b6/009b6ce8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b6ce8` · 推定シンボル `None` · 推定型 `None`
- [`009b005c`](#insn-009b005c) → [`009b00a0`](#insn-009b00a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0060`](#insn-009b0060) → [`009b0008`](#insn-009b0008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b006c`](#insn-009b006c) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`009b0070`](#insn-009b0070) → [`009b0008`](#insn-009b0008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0088`](#insn-009b0088) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`009b008c`](#insn-009b008c) → [`009b0008`](#insn-009b0008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b009c`](#insn-009b009c) → [`009b00d4`](#insn-009b00d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00a4`](#insn-009b00a4) → [`009b00d0`](#insn-009b00d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00b0`](#insn-009b00b0) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`009b00b4`](#insn-009b00b4) → [`009b00d0`](#insn-009b00d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00cc`](#insn-009b00cc) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`009b00d8`](#insn-009b00d8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00e0`](#insn-009b00e0) → [`009b0120`](#insn-009b0120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00e4`](#insn-009b00e4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00e8`](#insn-009b00e8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00ec`](#insn-009b00ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00f0`](#insn-009b00f0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0120`](#insn-009b0120) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009affd0`](#insn-009affd0)

~~~json
{
  "source": "009affd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affd4`](#insn-009affd4)

~~~json
{
  "source": "009affd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affd8`](#insn-009affd8)

~~~json
{
  "source": "009affd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affdc`](#insn-009affdc)

~~~json
{
  "source": "009affdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009afff0`](#insn-009afff0)

~~~json
{
  "source": "009afff0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009afffc`](#insn-009afffc)

~~~json
{
  "source": "009afffc",
  "target": "009b0090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0004`](#insn-009b0004)

~~~json
{
  "source": "009b0004",
  "target": "009b001c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0018`](#insn-009b0018)

~~~json
{
  "source": "009b0018",
  "target": "009b0090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0024`](#insn-009b0024)

~~~json
{
  "source": "009b0024",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0028`](#insn-009b0028)

~~~json
{
  "source": "009b0028",
  "target": "009b0040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0034`](#insn-009b0034)

~~~json
{
  "source": "009b0034",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0038`](#insn-009b0038)

~~~json
{
  "source": "009b0038",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b003c`](#insn-009b003c)

~~~json
{
  "source": "009b003c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0048`](#insn-009b0048)

~~~json
{
  "source": "009b0048",
  "target": "009b6ca4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0050`](#insn-009b0050)

~~~json
{
  "source": "009b0050",
  "target": "009b0060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0058`](#insn-009b0058)

~~~json
{
  "source": "009b0058",
  "target": "009b6ce8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b005c`](#insn-009b005c)

~~~json
{
  "source": "009b005c",
  "target": "009b00a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0060`](#insn-009b0060)

~~~json
{
  "source": "009b0060",
  "target": "009b0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b006c`](#insn-009b006c)

~~~json
{
  "source": "009b006c",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0070`](#insn-009b0070)

~~~json
{
  "source": "009b0070",
  "target": "009b0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0088`](#insn-009b0088)

~~~json
{
  "source": "009b0088",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b008c`](#insn-009b008c)

~~~json
{
  "source": "009b008c",
  "target": "009b0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b009c`](#insn-009b009c)

~~~json
{
  "source": "009b009c",
  "target": "009b00d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00a4`](#insn-009b00a4)

~~~json
{
  "source": "009b00a4",
  "target": "009b00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00b0`](#insn-009b00b0)

~~~json
{
  "source": "009b00b0",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b00b4`](#insn-009b00b4)

~~~json
{
  "source": "009b00b4",
  "target": "009b00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00cc`](#insn-009b00cc)

~~~json
{
  "source": "009b00cc",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b00d8`](#insn-009b00d8)

~~~json
{
  "source": "009b00d8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00e0`](#insn-009b00e0)

~~~json
{
  "source": "009b00e0",
  "target": "009b0120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00e4`](#insn-009b00e4)

~~~json
{
  "source": "009b00e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00e8`](#insn-009b00e8)

~~~json
{
  "source": "009b00e8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00ec`](#insn-009b00ec)

~~~json
{
  "source": "009b00ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00f0`](#insn-009b00f0)

~~~json
{
  "source": "009b00f0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0120`](#insn-009b0120)

~~~json
{
  "source": "009b0120",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
