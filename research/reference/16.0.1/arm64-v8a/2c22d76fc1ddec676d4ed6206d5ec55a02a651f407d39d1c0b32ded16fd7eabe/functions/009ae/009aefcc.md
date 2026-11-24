# 009aefcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009aee30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009aee30.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0055.md#compare-fb84174c5a6560453dd77c5cb67f3884)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `009af020`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af020.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0057.md#compare-577c34165eacfd548fe23fa460d2262d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009aefcc",
  "name": "FUN_009aefcc",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04dac6a96c52ad60926373969ead29410a3a9e512e0b99d27b199715a432ed33",
  "source_text_sha256": "04dac6a96c52ad60926373969ead29410a3a9e512e0b99d27b199715a432ed33",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009aefcc",
        "009af0fb"
      ],
      [
        "009af120",
        "009af123"
      ]
    ],
    "bytes_sha256": "4c48eb2042aceafd60b3c34f9cf0e83bc971bc3703651f2db20f070acc3dcdb7",
    "instruction_count": 77,
    "instruction_bytes": 308,
    "body_bytes": 308,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00769d84](../00769/00769d84.md)

## 呼び出し先

- [009b5ca4](../009b5/009b5ca4.md)
- [009b5ce8](../009b5/009b5ce8.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4419 bytes

~~~c

void FUN_009aefcc(long *param_1)

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
  
                    /* try { // try from 009aefdc to 00aaefe3 has its CatchHandler @ 009af044 */
                    /* catch() { ... } // from try @ 009aeb9c with catch @ 009aefe4
                       try { // try from 009aefe4 to 00aaf0b3 has its CatchHandler @ 009ae804 */
  lVar2 = tpidr_el0;
                    /* catch() { ... } // from try @ 009aeb60 with catch @ 009aefec */
  lVar7 = *(long *)(lVar2 + 0x28);
                    /* catch() { ... } // from try @ 009aeb50 with catch @ 009aeff0 */
  lVar5 = *param_1;
                    /* catch() { ... } // from try @ 009aeea8 with catch @ 009aeff8 */
                    /* catch() { ... } // from try @ 009aea4c with catch @ 009aeffc
                       catch() { ... } // from try @ 009aee98 with catch @ 009aeffc */
  if (param_1[1] != lVar5) {
    uVar8 = 0;
                    /* catch() { ... } // from try @ 009aebd0 with catch @ 009af004 */
    do {
                    /* catch() { ... } // from try @ 009aee8c with catch @ 009af01c */
      puVar1 = (undefined8 *)(lVar5 + uVar8 * 0x10);
      plVar9 = (long *)puVar1[1];
      uVar6 = *puVar1;
                    /* catch() { ... } // from try @ 009aecc8 with catch @ 009af020 */
                    /* catch() { ... } // from try @ 009aebe8 with catch @ 009af024 */
                    /* catch() { ... } // from try @ 009aeee8 with catch @ 009af028 */
      if (plVar9 != (long *)0x0) {
                    /* catch() { ... } // from try @ 009aee50 with catch @ 009af030 */
                    /* catch() { ... } // from try @ 009aef00 with catch @ 009af038 */
        FUN_00c53cd0(1,plVar9 + 1);
                    /* catch() { ... } // from try @ 009aec44 with catch @ 009af03c */
      }
                    /* catch() { ... } // from try @ 009ae998 with catch @ 009af040 */
                    /* catch() { ... } // from try @ 009aedb4 with catch @ 009af044
                       catch() { ... } // from try @ 009aefdc with catch @ 009af044 */
      iVar3 = FUN_009b5ca4(uVar6);
                    /* catch() { ... } // from try @ 009aede0 with catch @ 009af04c */
                    /* catch() { ... } // from try @ 009aecec with catch @ 009af05c
                       catch() { ... } // from try @ 009aefc4 with catch @ 009af05c */
      if ((iVar3 == 4) && (uVar4 = FUN_009b5ce8(uVar6), (uVar4 & 1) != 0)) {
        *(int *)((long)param_1 + 0x1c) = (int)uVar8;
                    /* try { // try from 009af0b4 to 00aaf23b has its CatchHandler @ 009af0b4
                       catch() { ... } // from try @ 009af0b4 with catch @ 009af0b4
                       catch() { ... } // from try @ 009af2fc with catch @ 009af0b4
                       catch() { ... } // from try @ 009af590 with catch @ 009af0b4
                       catch() { ... } // from try @ 009af650 with catch @ 009af0b4
                       catch() { ... } // from try @ 009af7e0 with catch @ 009af0b4
                       catch() { ... } // from try @ 009af86c with catch @ 009af0b4 */
        if ((plVar9 != (long *)0x0) &&
           (lVar5 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)) {
          (**(code **)(*plVar9 + 0x10))(plVar9);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
        }
        uVar6 = 1;
        goto LAB_009af0d4;
      }
                    /* catch() { ... } // from try @ 009aed34 with catch @ 009af064 */
      if ((plVar9 != (long *)0x0) &&
         (lVar5 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
      lVar5 = *param_1;
                    /* catch() { ... } // from try @ 009aea08 with catch @ 009af00c */
      uVar8 = uVar8 + 1;
                    /* catch() { ... } // from try @ 009ae9f8 with catch @ 009af010 */
                    /* catch() { ... } // from try @ 009aeb34 with catch @ 009af018 */
    } while (uVar8 < (ulong)(param_1[1] - lVar5 >> 4));
  }
  uVar6 = 0;
  *(undefined4 *)((long)param_1 + 0x1c) = 0xffffffff;
LAB_009af0d4:
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
<a id="insn-009aefcc"></a> `009aefcc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009aefd0"></a> `009aefd0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009aefd4"></a> `009aefd4` | `f7 23 00 f9` | str x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009aefd8"></a> `009aefd8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009aefdc"></a> `009aefdc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009aefe0"></a> `009aefe0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-009aefe4"></a> `009aefe4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009aefe8"></a> `009aefe8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009aefec"></a> `009aefec` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-009aeff0"></a> `009aeff0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009aeff4"></a> `009aeff4` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-009aeff8"></a> `009aeff8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-009aeffc"></a> `009aeffc` | `a0 04 00 54` | b.eq 0x009af090 | `CONDITIONAL_JUMP`
<a id="insn-009af000"></a> `009af000` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-009af004"></a> `009af004` | `06 00 00 14` | b 0x009af01c | `UNCONDITIONAL_JUMP`
<a id="insn-009af008"></a> `009af008` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-009af00c"></a> `009af00c` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-009af010"></a> `009af010` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-009af014"></a> `009af014` | `ff 12 89 eb` | cmp x23,x9, ASR #0x4 | `FALL_THROUGH`
<a id="insn-009af018"></a> `009af018` | `c2 03 00 54` | b.cs 0x009af090 | `CONDITIONAL_JUMP`
<a id="insn-009af01c"></a> `009af01c` | `00 79 f7 3c` | ldr q0,[x8,x23, lsl #4] | `FALL_THROUGH`
<a id="insn-009af020"></a> `009af020` | `14 3c 18 4e` | mov x20,v0.D[0x1] | `FALL_THROUGH`
<a id="insn-009af024"></a> `009af024` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009af028"></a> `009af028` | `d4 00 00 b4` | cbz x20,0x009af040 | `CONDITIONAL_JUMP`
<a id="insn-009af02c"></a> `009af02c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009af030"></a> `009af030` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009af034"></a> `009af034` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-009af038"></a> `009af038` | `26 93 0a 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-009af03c"></a> `009af03c` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-009af040"></a> `009af040` | `15 00 66 9e` | fmov x21,d0 | `FALL_THROUGH`
<a id="insn-009af044"></a> `009af044` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009af048"></a> `009af048` | `17 1b 00 94` | bl 0x009b5ca4 | `UNCONDITIONAL_CALL`
<a id="insn-009af04c"></a> `009af04c` | `1f 10 00 71` | cmp w0,#0x4 | `FALL_THROUGH`
<a id="insn-009af050"></a> `009af050` | `81 00 00 54` | b.ne 0x009af060 | `CONDITIONAL_JUMP`
<a id="insn-009af054"></a> `009af054` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009af058"></a> `009af058` | `24 1b 00 94` | bl 0x009b5ce8 | `UNCONDITIONAL_CALL`
<a id="insn-009af05c"></a> `009af05c` | `20 02 00 37` | tbnz w0,#0x0,0x009af0a0 | `CONDITIONAL_JUMP`
<a id="insn-009af060"></a> `009af060` | `54 fd ff b4` | cbz x20,0x009af008 | `CONDITIONAL_JUMP`
<a id="insn-009af064"></a> `009af064` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009af068"></a> `009af068` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009af06c"></a> `009af06c` | `25 93 0a 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-009af070"></a> `009af070` | `c0 fc ff b5` | cbnz x0,0x009af008 | `CONDITIONAL_JUMP`
<a id="insn-009af074"></a> `009af074` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009af078"></a> `009af078` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009af07c"></a> `009af07c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009af080"></a> `009af080` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009af084"></a> `009af084` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009af088"></a> `009af088` | `7e a3 0a 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-009af08c"></a> `009af08c` | `df ff ff 17` | b 0x009af008 | `UNCONDITIONAL_JUMP`
<a id="insn-009af090"></a> `009af090` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-009af094"></a> `009af094` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-009af098"></a> `009af098` | `68 1e 00 b9` | str w8,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-009af09c"></a> `009af09c` | `0e 00 00 14` | b 0x009af0d4 | `UNCONDITIONAL_JUMP`
<a id="insn-009af0a0"></a> `009af0a0` | `77 1e 00 b9` | str w23,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-009af0a4"></a> `009af0a4` | `74 01 00 b4` | cbz x20,0x009af0d0 | `CONDITIONAL_JUMP`
<a id="insn-009af0a8"></a> `009af0a8` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009af0ac"></a> `009af0ac` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009af0b0"></a> `009af0b0` | `14 93 0a 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-009af0b4"></a> `009af0b4` | `e0 00 00 b5` | cbnz x0,0x009af0d0 | `CONDITIONAL_JUMP`
<a id="insn-009af0b8"></a> `009af0b8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009af0bc"></a> `009af0bc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009af0c0"></a> `009af0c0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009af0c4"></a> `009af0c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009af0c8"></a> `009af0c8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009af0cc"></a> `009af0cc` | `6d a3 0a 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-009af0d0"></a> `009af0d0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009af0d4"></a> `009af0d4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-009af0d8"></a> `009af0d8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009af0dc"></a> `009af0dc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009af0e0"></a> `009af0e0` | `01 02 00 54` | b.ne 0x009af120 | `CONDITIONAL_JUMP`
<a id="insn-009af0e4"></a> `009af0e4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009af0e8"></a> `009af0e8` | `f7 23 40 f9` | ldr x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009af0ec"></a> `009af0ec` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009af0f0"></a> `009af0f0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009af0f4"></a> `009af0f4` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009af0f8"></a> `009af0f8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009af120"></a> `009af120` | `70 a3 0a 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009aefcc`](#insn-009aefcc) 範囲 `[['009aefcc', '009aefdb']]`
  - `FALL_THROUGH` [`009aefd8`](#insn-009aefd8) → [`009aefdc`](#insn-009aefdc)
- ブロック [`009aefdc`](#insn-009aefdc) 範囲 `[['009aefdc', '009aefe3']]`
  - `FALL_THROUGH` [`009aefe0`](#insn-009aefe0) → [`009aefe4`](#insn-009aefe4)
- ブロック [`009aefe4`](#insn-009aefe4) 範囲 `[['009aefe4', '009aefeb']]`
  - `FALL_THROUGH` [`009aefe8`](#insn-009aefe8) → [`009aefec`](#insn-009aefec)
- ブロック [`009aefec`](#insn-009aefec) 範囲 `[['009aefec', '009aefef']]`
  - `FALL_THROUGH` [`009aefec`](#insn-009aefec) → [`009aeff0`](#insn-009aeff0)
- ブロック [`009aeff0`](#insn-009aeff0) 範囲 `[['009aeff0', '009aeff7']]`
  - `FALL_THROUGH` [`009aeff4`](#insn-009aeff4) → [`009aeff8`](#insn-009aeff8)
- ブロック [`009aeff8`](#insn-009aeff8) 範囲 `[['009aeff8', '009aeffb']]`
  - `FALL_THROUGH` [`009aeff8`](#insn-009aeff8) → [`009aeffc`](#insn-009aeffc)
- ブロック [`009aeffc`](#insn-009aeffc) 範囲 `[['009aeffc', '009aefff']]`
  - `CONDITIONAL_JUMP` [`009aeffc`](#insn-009aeffc) → [`009af090`](#insn-009af090)
  - `FALL_THROUGH` [`009aeffc`](#insn-009aeffc) → [`009af000`](#insn-009af000)
- ブロック [`009af000`](#insn-009af000) 範囲 `[['009af000', '009af003']]`
  - `FALL_THROUGH` [`009af000`](#insn-009af000) → [`009af004`](#insn-009af004)
- ブロック [`009af004`](#insn-009af004) 範囲 `[['009af004', '009af007']]`
  - `UNCONDITIONAL_JUMP` [`009af004`](#insn-009af004) → [`009af01c`](#insn-009af01c)
- ブロック [`009af008`](#insn-009af008) 範囲 `[['009af008', '009af00b']]`
  - `FALL_THROUGH` [`009af008`](#insn-009af008) → [`009af00c`](#insn-009af00c)
- ブロック [`009af00c`](#insn-009af00c) 範囲 `[['009af00c', '009af00f']]`
  - `FALL_THROUGH` [`009af00c`](#insn-009af00c) → [`009af010`](#insn-009af010)
- ブロック [`009af010`](#insn-009af010) 範囲 `[['009af010', '009af017']]`
  - `FALL_THROUGH` [`009af014`](#insn-009af014) → [`009af018`](#insn-009af018)
- ブロック [`009af018`](#insn-009af018) 範囲 `[['009af018', '009af01b']]`
  - `CONDITIONAL_JUMP` [`009af018`](#insn-009af018) → [`009af090`](#insn-009af090)
  - `FALL_THROUGH` [`009af018`](#insn-009af018) → [`009af01c`](#insn-009af01c)
- ブロック [`009af01c`](#insn-009af01c) 範囲 `[['009af01c', '009af01f']]`
  - `FALL_THROUGH` [`009af01c`](#insn-009af01c) → [`009af020`](#insn-009af020)
- ブロック [`009af020`](#insn-009af020) 範囲 `[['009af020', '009af023']]`
  - `FALL_THROUGH` [`009af020`](#insn-009af020) → [`009af024`](#insn-009af024)
- ブロック [`009af024`](#insn-009af024) 範囲 `[['009af024', '009af027']]`
  - `FALL_THROUGH` [`009af024`](#insn-009af024) → [`009af028`](#insn-009af028)
- ブロック [`009af028`](#insn-009af028) 範囲 `[['009af028', '009af02b']]`
  - `CONDITIONAL_JUMP` [`009af028`](#insn-009af028) → [`009af040`](#insn-009af040)
  - `FALL_THROUGH` [`009af028`](#insn-009af028) → [`009af02c`](#insn-009af02c)
- ブロック [`009af02c`](#insn-009af02c) 範囲 `[['009af02c', '009af02f']]`
  - `FALL_THROUGH` [`009af02c`](#insn-009af02c) → [`009af030`](#insn-009af030)
- ブロック [`009af030`](#insn-009af030) 範囲 `[['009af030', '009af037']]`
  - `FALL_THROUGH` [`009af034`](#insn-009af034) → [`009af038`](#insn-009af038)
- ブロック [`009af038`](#insn-009af038) 範囲 `[['009af038', '009af03b']]`
  - `FALL_THROUGH` [`009af038`](#insn-009af038) → [`009af03c`](#insn-009af03c)
- ブロック [`009af03c`](#insn-009af03c) 範囲 `[['009af03c', '009af03f']]`
  - `FALL_THROUGH` [`009af03c`](#insn-009af03c) → [`009af040`](#insn-009af040)
- ブロック [`009af040`](#insn-009af040) 範囲 `[['009af040', '009af043']]`
  - `FALL_THROUGH` [`009af040`](#insn-009af040) → [`009af044`](#insn-009af044)
- ブロック [`009af044`](#insn-009af044) 範囲 `[['009af044', '009af04b']]`
  - `FALL_THROUGH` [`009af048`](#insn-009af048) → [`009af04c`](#insn-009af04c)
- ブロック [`009af04c`](#insn-009af04c) 範囲 `[['009af04c', '009af053']]`
  - `CONDITIONAL_JUMP` [`009af050`](#insn-009af050) → [`009af060`](#insn-009af060)
  - `FALL_THROUGH` [`009af050`](#insn-009af050) → [`009af054`](#insn-009af054)
- ブロック [`009af054`](#insn-009af054) 範囲 `[['009af054', '009af05b']]`
  - `FALL_THROUGH` [`009af058`](#insn-009af058) → [`009af05c`](#insn-009af05c)
- ブロック [`009af05c`](#insn-009af05c) 範囲 `[['009af05c', '009af05f']]`
  - `CONDITIONAL_JUMP` [`009af05c`](#insn-009af05c) → [`009af0a0`](#insn-009af0a0)
  - `FALL_THROUGH` [`009af05c`](#insn-009af05c) → [`009af060`](#insn-009af060)
- ブロック [`009af060`](#insn-009af060) 範囲 `[['009af060', '009af063']]`
  - `CONDITIONAL_JUMP` [`009af060`](#insn-009af060) → [`009af008`](#insn-009af008)
  - `FALL_THROUGH` [`009af060`](#insn-009af060) → [`009af064`](#insn-009af064)
- ブロック [`009af064`](#insn-009af064) 範囲 `[['009af064', '009af073']]`
  - `CONDITIONAL_JUMP` [`009af070`](#insn-009af070) → [`009af008`](#insn-009af008)
  - `FALL_THROUGH` [`009af070`](#insn-009af070) → [`009af074`](#insn-009af074)
- ブロック [`009af074`](#insn-009af074) 範囲 `[['009af074', '009af08f']]`
  - `UNCONDITIONAL_JUMP` [`009af08c`](#insn-009af08c) → [`009af008`](#insn-009af008)
- ブロック [`009af090`](#insn-009af090) 範囲 `[['009af090', '009af09f']]`
  - `UNCONDITIONAL_JUMP` [`009af09c`](#insn-009af09c) → [`009af0d4`](#insn-009af0d4)
- ブロック [`009af0a0`](#insn-009af0a0) 範囲 `[['009af0a0', '009af0a7']]`
  - `CONDITIONAL_JUMP` [`009af0a4`](#insn-009af0a4) → [`009af0d0`](#insn-009af0d0)
  - `FALL_THROUGH` [`009af0a4`](#insn-009af0a4) → [`009af0a8`](#insn-009af0a8)
- ブロック [`009af0a8`](#insn-009af0a8) 範囲 `[['009af0a8', '009af0b3']]`
  - `FALL_THROUGH` [`009af0b0`](#insn-009af0b0) → [`009af0b4`](#insn-009af0b4)
- ブロック [`009af0b4`](#insn-009af0b4) 範囲 `[['009af0b4', '009af0b7']]`
  - `CONDITIONAL_JUMP` [`009af0b4`](#insn-009af0b4) → [`009af0d0`](#insn-009af0d0)
  - `FALL_THROUGH` [`009af0b4`](#insn-009af0b4) → [`009af0b8`](#insn-009af0b8)
- ブロック [`009af0b8`](#insn-009af0b8) 範囲 `[['009af0b8', '009af0cf']]`
  - `FALL_THROUGH` [`009af0cc`](#insn-009af0cc) → [`009af0d0`](#insn-009af0d0)
- ブロック [`009af0d0`](#insn-009af0d0) 範囲 `[['009af0d0', '009af0d3']]`
  - `FALL_THROUGH` [`009af0d0`](#insn-009af0d0) → [`009af0d4`](#insn-009af0d4)
- ブロック [`009af0d4`](#insn-009af0d4) 範囲 `[['009af0d4', '009af0e3']]`
  - `CONDITIONAL_JUMP` [`009af0e0`](#insn-009af0e0) → [`009af120`](#insn-009af120)
  - `FALL_THROUGH` [`009af0e0`](#insn-009af0e0) → [`009af0e4`](#insn-009af0e4)
- ブロック [`009af0e4`](#insn-009af0e4) 範囲 `[['009af0e4', '009af0fb']]`
- ブロック [`009af120`](#insn-009af120) 範囲 `[['009af120', '009af123']]`

## 命令位置別の参照

- [`009aefd0`](#insn-009aefd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aefd4`](#insn-009aefd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aefd8`](#insn-009aefd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aefdc`](#insn-009aefdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aeff0`](#insn-009aeff0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aeffc`](#insn-009aeffc) → [`009af090`](#insn-009af090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af004`](#insn-009af004) → [`009af01c`](#insn-009af01c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af018`](#insn-009af018) → [`009af090`](#insn-009af090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af024`](#insn-009af024) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af028`](#insn-009af028) → [`009af040`](#insn-009af040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af034`](#insn-009af034) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af038`](#insn-009af038) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`009af03c`](#insn-009af03c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af048`](#insn-009af048) → [`009b5ca4`](../009b5/009b5ca4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5ca4` · 推定シンボル `None` · 推定型 `None`
- [`009af050`](#insn-009af050) → [`009af060`](#insn-009af060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af058`](#insn-009af058) → [`009b5ce8`](../009b5/009b5ce8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5ce8` · 推定シンボル `None` · 推定型 `None`
- [`009af05c`](#insn-009af05c) → [`009af0a0`](#insn-009af0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af060`](#insn-009af060) → [`009af008`](#insn-009af008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af06c`](#insn-009af06c) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`009af070`](#insn-009af070) → [`009af008`](#insn-009af008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af088`](#insn-009af088) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`009af08c`](#insn-009af08c) → [`009af008`](#insn-009af008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af09c`](#insn-009af09c) → [`009af0d4`](#insn-009af0d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af0a4`](#insn-009af0a4) → [`009af0d0`](#insn-009af0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af0b0`](#insn-009af0b0) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`009af0b4`](#insn-009af0b4) → [`009af0d0`](#insn-009af0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af0cc`](#insn-009af0cc) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`009af0d8`](#insn-009af0d8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af0e0`](#insn-009af0e0) → [`009af120`](#insn-009af120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af0e4`](#insn-009af0e4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af0e8`](#insn-009af0e8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af0ec`](#insn-009af0ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af0f0`](#insn-009af0f0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009af120`](#insn-009af120) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009aefd0`](#insn-009aefd0)

~~~json
{
  "source": "009aefd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aefd4`](#insn-009aefd4)

~~~json
{
  "source": "009aefd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aefd8`](#insn-009aefd8)

~~~json
{
  "source": "009aefd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aefdc`](#insn-009aefdc)

~~~json
{
  "source": "009aefdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aeff0`](#insn-009aeff0)

~~~json
{
  "source": "009aeff0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aeffc`](#insn-009aeffc)

~~~json
{
  "source": "009aeffc",
  "target": "009af090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af004`](#insn-009af004)

~~~json
{
  "source": "009af004",
  "target": "009af01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af018`](#insn-009af018)

~~~json
{
  "source": "009af018",
  "target": "009af090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af024`](#insn-009af024)

~~~json
{
  "source": "009af024",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af028`](#insn-009af028)

~~~json
{
  "source": "009af028",
  "target": "009af040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af034`](#insn-009af034)

~~~json
{
  "source": "009af034",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af038`](#insn-009af038)

~~~json
{
  "source": "009af038",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009af03c`](#insn-009af03c)

~~~json
{
  "source": "009af03c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af048`](#insn-009af048)

~~~json
{
  "source": "009af048",
  "target": "009b5ca4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009af050`](#insn-009af050)

~~~json
{
  "source": "009af050",
  "target": "009af060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af058`](#insn-009af058)

~~~json
{
  "source": "009af058",
  "target": "009b5ce8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009af05c`](#insn-009af05c)

~~~json
{
  "source": "009af05c",
  "target": "009af0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af060`](#insn-009af060)

~~~json
{
  "source": "009af060",
  "target": "009af008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af06c`](#insn-009af06c)

~~~json
{
  "source": "009af06c",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009af070`](#insn-009af070)

~~~json
{
  "source": "009af070",
  "target": "009af008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af088`](#insn-009af088)

~~~json
{
  "source": "009af088",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009af08c`](#insn-009af08c)

~~~json
{
  "source": "009af08c",
  "target": "009af008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af09c`](#insn-009af09c)

~~~json
{
  "source": "009af09c",
  "target": "009af0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af0a4`](#insn-009af0a4)

~~~json
{
  "source": "009af0a4",
  "target": "009af0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af0b0`](#insn-009af0b0)

~~~json
{
  "source": "009af0b0",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009af0b4`](#insn-009af0b4)

~~~json
{
  "source": "009af0b4",
  "target": "009af0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af0cc`](#insn-009af0cc)

~~~json
{
  "source": "009af0cc",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009af0d8`](#insn-009af0d8)

~~~json
{
  "source": "009af0d8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af0e0`](#insn-009af0e0)

~~~json
{
  "source": "009af0e0",
  "target": "009af120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af0e4`](#insn-009af0e4)

~~~json
{
  "source": "009af0e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af0e8`](#insn-009af0e8)

~~~json
{
  "source": "009af0e8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af0ec`](#insn-009af0ec)

~~~json
{
  "source": "009af0ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af0f0`](#insn-009af0f0)

~~~json
{
  "source": "009af0f0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009af120`](#insn-009af120)

~~~json
{
  "source": "009af120",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
