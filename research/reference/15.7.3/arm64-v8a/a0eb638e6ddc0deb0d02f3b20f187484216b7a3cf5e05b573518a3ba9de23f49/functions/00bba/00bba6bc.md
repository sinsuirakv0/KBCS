# 00bba6bc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bba5f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-60911775bc5710ca1a7045cc8892f402)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bba700`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba700.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-07a55b8acbe31945fe294a8848478cf8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba6bc",
  "name": "__cxa_guard_acquire",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f305b0ed2b1ee80b214a9efca506681cf6c727a281c9d09a2fd5b2015883e43",
  "source_text_sha256": "3f305b0ed2b1ee80b214a9efca506681cf6c727a281c9d09a2fd5b2015883e43",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bba6bc",
        "00bba7e3"
      ]
    ],
    "bytes_sha256": "db71291d01af0b3e826a0b6026df695aaff105cc80645bb9583161d0db9f2ff8",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdafb0](../00bda/00bdafb0.md)

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)
- [00bde7d0](../00bde/00bde7d0.md)
- [00bde7e0](../00bde/00bde7e0.md)
- [00be1180](../00be1/00be1180.md)
- [00be1da0](../00be1/00be1da0.md)

## 関連文字列（未確認候補）

~~~text
"%s failed to acquire mutex"
"%s failed to release mutex"
"__cxa_guard_acquire"
"__cxa_guard_acquire detected recursive initialization: do you have a function-local static variable whose initialization depends on that function?"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2774 bytes

~~~c

bool __cxa_guard_acquire(char *param_1)

{
  byte bVar1;
  byte bVar2;
  bool bVar3;
  int iVar4;
  long lVar5;
  int unaff_w20;
  
                    /* catch() { ... } // from try @ 00bb6a7c with catch @ 00bba6c4 */
                    /* catch() { ... } // from try @ 00bb6a70 with catch @ 00bba6d8 */
                    /* catch() { ... } // from try @ 00bb66d8 with catch @ 00bba6dc */
  if (*param_1 == '\0') {
                    /* catch() { ... } // from try @ 00bb66c8 with catch @ 00bba6f4 */
    iVar4 = pthread_mutex_lock((pthread_mutex_t *)&DAT_010a36c0);
    if (iVar4 != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00bbb158("%s failed to acquire mutex","__cxa_guard_acquire");
    }
    bVar1 = param_1[1];
    if ((bVar1 >> 1 & 1) != 0) {
      iVar4 = *(int *)(param_1 + 4);
                    /* catch() { ... } // from try @ 00bb66bc with catch @ 00bba714 */
                    /* catch() { ... } // from try @ 00bb6324 with catch @ 00bba718 */
      lVar5 = syscall(0xb2);
      unaff_w20 = (int)lVar5;
      if (iVar4 == unaff_w20) {
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb5b94 with catch @ 00bba7e0 */
        FUN_00bbb158(
                    "__cxa_guard_acquire detected recursive initialization: do you have a function-local static variable whose initialization depends on that function?"
                    );
      }
    }
    while (bVar2 = param_1[1], (bVar2 >> 1 & 1) != 0) {
                    /* catch() { ... } // from try @ 00bb6314 with catch @ 00bba744 */
      param_1[1] = bVar2 | 4;
      pthread_cond_wait((pthread_cond_t *)&DAT_010a36e8,(pthread_mutex_t *)&DAT_010a36c0);
    }
                    /* catch() { ... } // from try @ 00bb6308 with catch @ 00bba758 */
                    /* catch() { ... } // from try @ 00bb5f70 with catch @ 00bba75c */
    if (bVar2 != 1) {
      if ((bVar1 >> 1 & 1) == 0) {
        lVar5 = syscall(0xb2);
        unaff_w20 = (int)lVar5;
      }
      *(int *)(param_1 + 4) = unaff_w20;
      param_1[1] = '\x02';
    }
    iVar4 = pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a36c0);
                    /* catch() { ... } // from try @ 00bb5f60 with catch @ 00bba788 */
    if (iVar4 != 0) {
                    /* catch() { ... } // from try @ 00bb5ba0 with catch @ 00bba7cc */
                    /* WARNING: Subroutine does not return */
      FUN_00bbb158("%s failed to release mutex","__cxa_guard_acquire");
    }
    bVar3 = bVar2 != 1;
  }
  else {
    bVar3 = false;
  }
                    /* catch() { ... } // from try @ 00bb5f54 with catch @ 00bba79c */
                    /* catch() { ... } // from try @ 00bb5bb0 with catch @ 00bba7a0 */
  return bVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bba6bc"></a> `00bba6bc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bba6c0"></a> `00bba6c0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bba6c4"></a> `00bba6c4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba6c8"></a> `00bba6c8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bba6cc"></a> `00bba6cc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bba6d0"></a> `00bba6d0` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bba6d4"></a> `00bba6d4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bba6d8"></a> `00bba6d8` | `08 fc df 08` | ldarb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bba6dc"></a> `00bba6dc` | `68 00 00 34` | cbz w8,0x00bba6e8 | `CONDITIONAL_JUMP`
<a id="insn-00bba6e0"></a> `00bba6e0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bba6e4"></a> `00bba6e4` | `2c 00 00 14` | b 0x00bba794 | `UNCONDITIONAL_JUMP`
<a id="insn-00bba6e8"></a> `00bba6e8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bba6ec"></a> `00bba6ec` | `68 b7 ff b0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bba6f0"></a> `00bba6f0` | `08 b5 08 91` | add x8,x8,#0x22d | `FALL_THROUGH`
<a id="insn-00bba6f4"></a> `00bba6f4` | `40 27 00 b0` | adrp x0,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bba6f8"></a> `00bba6f8` | `00 00 1b 91` | add x0,x0,#0x6c0 | `FALL_THROUGH`
<a id="insn-00bba6fc"></a> `00bba6fc` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bba700"></a> `00bba700` | `34 90 00 94` | bl 0x00bde7d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba704"></a> `00bba704` | `60 05 00 35` | cbnz w0,0x00bba7b0 | `CONDITIONAL_JUMP`
<a id="insn-00bba708"></a> `00bba708` | `77 06 40 39` | ldrb w23,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bba70c"></a> `00bba70c` | `f7 00 08 36` | tbz w23,#0x1,0x00bba728 | `CONDITIONAL_JUMP`
<a id="insn-00bba710"></a> `00bba710` | `75 06 40 b9` | ldr w21,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00bba714"></a> `00bba714` | `40 16 80 52` | mov w0,#0xb2 | `FALL_THROUGH`
<a id="insn-00bba718"></a> `00bba718` | `a2 9d 00 94` | bl 0x00be1da0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba71c"></a> `00bba71c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bba720"></a> `00bba720` | `bf 02 14 6b` | cmp w21,w20 | `FALL_THROUGH`
<a id="insn-00bba724"></a> `00bba724` | `a0 05 00 54` | b.eq 0x00bba7d8 | `CONDITIONAL_JUMP`
<a id="insn-00bba728"></a> `00bba728` | `55 27 00 b0` | adrp x21,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bba72c"></a> `00bba72c` | `b5 a2 1b 91` | add x21,x21,#0x6e8 | `FALL_THROUGH`
<a id="insn-00bba730"></a> `00bba730` | `56 27 00 b0` | adrp x22,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bba734"></a> `00bba734` | `d6 02 1b 91` | add x22,x22,#0x6c0 | `FALL_THROUGH`
<a id="insn-00bba738"></a> `00bba738` | `78 06 40 39` | ldrb w24,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bba73c"></a> `00bba73c` | `f8 00 08 36` | tbz w24,#0x1,0x00bba758 | `CONDITIONAL_JUMP`
<a id="insn-00bba740"></a> `00bba740` | `08 03 1e 32` | orr w8,w24,#0x4 | `FALL_THROUGH`
<a id="insn-00bba744"></a> `00bba744` | `68 06 00 39` | strb w8,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bba748"></a> `00bba748` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bba74c"></a> `00bba74c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bba750"></a> `00bba750` | `8c 9a 00 94` | bl 0x00be1180 | `UNCONDITIONAL_CALL`
<a id="insn-00bba754"></a> `00bba754` | `f9 ff ff 17` | b 0x00bba738 | `UNCONDITIONAL_JUMP`
<a id="insn-00bba758"></a> `00bba758` | `1f 07 00 71` | cmp w24,#0x1 | `FALL_THROUGH`
<a id="insn-00bba75c"></a> `00bba75c` | `00 01 00 54` | b.eq 0x00bba77c | `CONDITIONAL_JUMP`
<a id="insn-00bba760"></a> `00bba760` | `97 00 08 37` | tbnz w23,#0x1,0x00bba770 | `CONDITIONAL_JUMP`
<a id="insn-00bba764"></a> `00bba764` | `40 16 80 52` | mov w0,#0xb2 | `FALL_THROUGH`
<a id="insn-00bba768"></a> `00bba768` | `8e 9d 00 94` | bl 0x00be1da0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba76c"></a> `00bba76c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bba770"></a> `00bba770` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bba774"></a> `00bba774` | `74 06 00 b9` | str w20,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00bba778"></a> `00bba778` | `68 06 00 39` | strb w8,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bba77c"></a> `00bba77c` | `40 27 00 b0` | adrp x0,0x10a3000 | `FALL_THROUGH`
<a id="insn-00bba780"></a> `00bba780` | `00 00 1b 91` | add x0,x0,#0x6c0 | `FALL_THROUGH`
<a id="insn-00bba784"></a> `00bba784` | `17 90 00 94` | bl 0x00bde7e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba788"></a> `00bba788` | `e0 01 00 35` | cbnz w0,0x00bba7c4 | `CONDITIONAL_JUMP`
<a id="insn-00bba78c"></a> `00bba78c` | `1f 07 00 71` | cmp w24,#0x1 | `FALL_THROUGH`
<a id="insn-00bba790"></a> `00bba790` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bba794"></a> `00bba794` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bba798"></a> `00bba798` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bba79c"></a> `00bba79c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bba7a0"></a> `00bba7a0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba7a4"></a> `00bba7a4` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bba7a8"></a> `00bba7a8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bba7ac"></a> `00bba7ac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bba7b0"></a> `00bba7b0` | `e0 b6 ff 90` | adrp x0,0x296000 | `FALL_THROUGH`
<a id="insn-00bba7b4"></a> `00bba7b4` | `00 40 20 91` | add x0,x0,#0x810 | `FALL_THROUGH`
<a id="insn-00bba7b8"></a> `00bba7b8` | `61 b7 ff b0` | adrp x1,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bba7bc"></a> `00bba7bc` | `21 b4 08 91` | add x1,x1,#0x22d | `FALL_THROUGH`
<a id="insn-00bba7c0"></a> `00bba7c0` | `66 02 00 94` | bl 0x00bbb158 | `CALL_TERMINATOR`
<a id="insn-00bba7c4"></a> `00bba7c4` | `a0 b6 ff f0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00bba7c8"></a> `00bba7c8` | `00 84 1f 91` | add x0,x0,#0x7e1 | `FALL_THROUGH`
<a id="insn-00bba7cc"></a> `00bba7cc` | `61 b7 ff b0` | adrp x1,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bba7d0"></a> `00bba7d0` | `21 b4 08 91` | add x1,x1,#0x22d | `FALL_THROUGH`
<a id="insn-00bba7d4"></a> `00bba7d4` | `61 02 00 94` | bl 0x00bbb158 | `CALL_TERMINATOR`
<a id="insn-00bba7d8"></a> `00bba7d8` | `80 b7 ff d0` | adrp x0,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bba7dc"></a> `00bba7dc` | `00 cc 14 91` | add x0,x0,#0x533 | `FALL_THROUGH`
<a id="insn-00bba7e0"></a> `00bba7e0` | `5e 02 00 94` | bl 0x00bbb158 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bba6bc`](#insn-00bba6bc) 範囲 `[['00bba6bc', '00bba6c3']]`
  - `FALL_THROUGH` [`00bba6c0`](#insn-00bba6c0) → [`00bba6c4`](#insn-00bba6c4)
- ブロック [`00bba6c4`](#insn-00bba6c4) 範囲 `[['00bba6c4', '00bba6d7']]`
  - `FALL_THROUGH` [`00bba6d4`](#insn-00bba6d4) → [`00bba6d8`](#insn-00bba6d8)
- ブロック [`00bba6d8`](#insn-00bba6d8) 範囲 `[['00bba6d8', '00bba6db']]`
  - `FALL_THROUGH` [`00bba6d8`](#insn-00bba6d8) → [`00bba6dc`](#insn-00bba6dc)
- ブロック [`00bba6dc`](#insn-00bba6dc) 範囲 `[['00bba6dc', '00bba6df']]`
  - `CONDITIONAL_JUMP` [`00bba6dc`](#insn-00bba6dc) → [`00bba6e8`](#insn-00bba6e8)
  - `FALL_THROUGH` [`00bba6dc`](#insn-00bba6dc) → [`00bba6e0`](#insn-00bba6e0)
- ブロック [`00bba6e0`](#insn-00bba6e0) 範囲 `[['00bba6e0', '00bba6e7']]`
  - `UNCONDITIONAL_JUMP` [`00bba6e4`](#insn-00bba6e4) → [`00bba794`](#insn-00bba794)
- ブロック [`00bba6e8`](#insn-00bba6e8) 範囲 `[['00bba6e8', '00bba6f3']]`
  - `FALL_THROUGH` [`00bba6f0`](#insn-00bba6f0) → [`00bba6f4`](#insn-00bba6f4)
- ブロック [`00bba6f4`](#insn-00bba6f4) 範囲 `[['00bba6f4', '00bba707']]`
  - `CONDITIONAL_JUMP` [`00bba704`](#insn-00bba704) → [`00bba7b0`](#insn-00bba7b0)
  - `FALL_THROUGH` [`00bba704`](#insn-00bba704) → [`00bba708`](#insn-00bba708)
- ブロック [`00bba708`](#insn-00bba708) 範囲 `[['00bba708', '00bba70f']]`
  - `CONDITIONAL_JUMP` [`00bba70c`](#insn-00bba70c) → [`00bba728`](#insn-00bba728)
  - `FALL_THROUGH` [`00bba70c`](#insn-00bba70c) → [`00bba710`](#insn-00bba710)
- ブロック [`00bba710`](#insn-00bba710) 範囲 `[['00bba710', '00bba713']]`
  - `FALL_THROUGH` [`00bba710`](#insn-00bba710) → [`00bba714`](#insn-00bba714)
- ブロック [`00bba714`](#insn-00bba714) 範囲 `[['00bba714', '00bba717']]`
  - `FALL_THROUGH` [`00bba714`](#insn-00bba714) → [`00bba718`](#insn-00bba718)
- ブロック [`00bba718`](#insn-00bba718) 範囲 `[['00bba718', '00bba727']]`
  - `CONDITIONAL_JUMP` [`00bba724`](#insn-00bba724) → [`00bba7d8`](#insn-00bba7d8)
  - `FALL_THROUGH` [`00bba724`](#insn-00bba724) → [`00bba728`](#insn-00bba728)
- ブロック [`00bba728`](#insn-00bba728) 範囲 `[['00bba728', '00bba737']]`
  - `FALL_THROUGH` [`00bba734`](#insn-00bba734) → [`00bba738`](#insn-00bba738)
- ブロック [`00bba738`](#insn-00bba738) 範囲 `[['00bba738', '00bba73f']]`
  - `CONDITIONAL_JUMP` [`00bba73c`](#insn-00bba73c) → [`00bba758`](#insn-00bba758)
  - `FALL_THROUGH` [`00bba73c`](#insn-00bba73c) → [`00bba740`](#insn-00bba740)
- ブロック [`00bba740`](#insn-00bba740) 範囲 `[['00bba740', '00bba743']]`
  - `FALL_THROUGH` [`00bba740`](#insn-00bba740) → [`00bba744`](#insn-00bba744)
- ブロック [`00bba744`](#insn-00bba744) 範囲 `[['00bba744', '00bba757']]`
  - `UNCONDITIONAL_JUMP` [`00bba754`](#insn-00bba754) → [`00bba738`](#insn-00bba738)
- ブロック [`00bba758`](#insn-00bba758) 範囲 `[['00bba758', '00bba75b']]`
  - `FALL_THROUGH` [`00bba758`](#insn-00bba758) → [`00bba75c`](#insn-00bba75c)
- ブロック [`00bba75c`](#insn-00bba75c) 範囲 `[['00bba75c', '00bba75f']]`
  - `CONDITIONAL_JUMP` [`00bba75c`](#insn-00bba75c) → [`00bba77c`](#insn-00bba77c)
  - `FALL_THROUGH` [`00bba75c`](#insn-00bba75c) → [`00bba760`](#insn-00bba760)
- ブロック [`00bba760`](#insn-00bba760) 範囲 `[['00bba760', '00bba763']]`
  - `CONDITIONAL_JUMP` [`00bba760`](#insn-00bba760) → [`00bba770`](#insn-00bba770)
  - `FALL_THROUGH` [`00bba760`](#insn-00bba760) → [`00bba764`](#insn-00bba764)
- ブロック [`00bba764`](#insn-00bba764) 範囲 `[['00bba764', '00bba76f']]`
  - `FALL_THROUGH` [`00bba76c`](#insn-00bba76c) → [`00bba770`](#insn-00bba770)
- ブロック [`00bba770`](#insn-00bba770) 範囲 `[['00bba770', '00bba77b']]`
  - `FALL_THROUGH` [`00bba778`](#insn-00bba778) → [`00bba77c`](#insn-00bba77c)
- ブロック [`00bba77c`](#insn-00bba77c) 範囲 `[['00bba77c', '00bba787']]`
  - `FALL_THROUGH` [`00bba784`](#insn-00bba784) → [`00bba788`](#insn-00bba788)
- ブロック [`00bba788`](#insn-00bba788) 範囲 `[['00bba788', '00bba78b']]`
  - `CONDITIONAL_JUMP` [`00bba788`](#insn-00bba788) → [`00bba7c4`](#insn-00bba7c4)
  - `FALL_THROUGH` [`00bba788`](#insn-00bba788) → [`00bba78c`](#insn-00bba78c)
- ブロック [`00bba78c`](#insn-00bba78c) 範囲 `[['00bba78c', '00bba793']]`
  - `FALL_THROUGH` [`00bba790`](#insn-00bba790) → [`00bba794`](#insn-00bba794)
- ブロック [`00bba794`](#insn-00bba794) 範囲 `[['00bba794', '00bba79b']]`
  - `FALL_THROUGH` [`00bba798`](#insn-00bba798) → [`00bba79c`](#insn-00bba79c)
- ブロック [`00bba79c`](#insn-00bba79c) 範囲 `[['00bba79c', '00bba79f']]`
  - `FALL_THROUGH` [`00bba79c`](#insn-00bba79c) → [`00bba7a0`](#insn-00bba7a0)
- ブロック [`00bba7a0`](#insn-00bba7a0) 範囲 `[['00bba7a0', '00bba7af']]`
- ブロック [`00bba7b0`](#insn-00bba7b0) 範囲 `[['00bba7b0', '00bba7c3']]`
- ブロック [`00bba7c4`](#insn-00bba7c4) 範囲 `[['00bba7c4', '00bba7cb']]`
  - `FALL_THROUGH` [`00bba7c8`](#insn-00bba7c8) → [`00bba7cc`](#insn-00bba7cc)
- ブロック [`00bba7cc`](#insn-00bba7cc) 範囲 `[['00bba7cc', '00bba7d7']]`
- ブロック [`00bba7d8`](#insn-00bba7d8) 範囲 `[['00bba7d8', '00bba7df']]`
  - `FALL_THROUGH` [`00bba7dc`](#insn-00bba7dc) → [`00bba7e0`](#insn-00bba7e0)
- ブロック [`00bba7e0`](#insn-00bba7e0) 範囲 `[['00bba7e0', '00bba7e3']]`

## 命令位置別の参照

- [`00bba6c4`](#insn-00bba6c4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba6c8`](#insn-00bba6c8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba6cc`](#insn-00bba6cc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba6d0`](#insn-00bba6d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba6dc`](#insn-00bba6dc) → [`00bba6e8`](#insn-00bba6e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba6e4`](#insn-00bba6e4) → [`00bba794`](#insn-00bba794) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba6f8`](#insn-00bba6f8) → `010a36c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba6fc`](#insn-00bba6fc) → `002a722d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba6fc`](#insn-00bba6fc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba700`](#insn-00bba700) → [`00bde7d0`](../00bde/00bde7d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde7d0` · 推定シンボル `None` · 推定型 `None`
- [`00bba704`](#insn-00bba704) → [`00bba7b0`](#insn-00bba7b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba70c`](#insn-00bba70c) → [`00bba728`](#insn-00bba728) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba718`](#insn-00bba718) → [`00be1da0`](../00be1/00be1da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1da0` · 推定シンボル `None` · 推定型 `None`
- [`00bba724`](#insn-00bba724) → [`00bba7d8`](#insn-00bba7d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba73c`](#insn-00bba73c) → [`00bba758`](#insn-00bba758) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba748`](#insn-00bba748) → `010a36e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba74c`](#insn-00bba74c) → `010a36c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba750`](#insn-00bba750) → [`00be1180`](../00be1/00be1180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1180` · 推定シンボル `None` · 推定型 `None`
- [`00bba754`](#insn-00bba754) → [`00bba738`](#insn-00bba738) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba75c`](#insn-00bba75c) → [`00bba77c`](#insn-00bba77c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba760`](#insn-00bba760) → [`00bba770`](#insn-00bba770) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba768`](#insn-00bba768) → [`00be1da0`](../00be1/00be1da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1da0` · 推定シンボル `None` · 推定型 `None`
- [`00bba780`](#insn-00bba780) → `010a36c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba784`](#insn-00bba784) → [`00bde7e0`](../00bde/00bde7e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde7e0` · 推定シンボル `None` · 推定型 `None`
- [`00bba788`](#insn-00bba788) → [`00bba7c4`](#insn-00bba7c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba794`](#insn-00bba794) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba798`](#insn-00bba798) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba79c`](#insn-00bba79c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba7a0`](#insn-00bba7a0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba7b4`](#insn-00bba7b4) → `00296810`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba7bc`](#insn-00bba7bc) → `002a722d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba7c0`](#insn-00bba7c0) → [`00bbb158`](../00bbb/00bbb158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb158` · 推定シンボル `None` · 推定型 `None`
- [`00bba7c8`](#insn-00bba7c8) → `002917e1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba7d0`](#insn-00bba7d0) → `002a722d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba7d4`](#insn-00bba7d4) → [`00bbb158`](../00bbb/00bbb158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb158` · 推定シンボル `None` · 推定型 `None`
- [`00bba7dc`](#insn-00bba7dc) → `002ac533`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba7e0`](#insn-00bba7e0) → [`00bbb158`](../00bbb/00bbb158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb158` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bba6c4`](#insn-00bba6c4)

~~~json
{
  "source": "00bba6c4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba6c8`](#insn-00bba6c8)

~~~json
{
  "source": "00bba6c8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba6cc`](#insn-00bba6cc)

~~~json
{
  "source": "00bba6cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba6d0`](#insn-00bba6d0)

~~~json
{
  "source": "00bba6d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba6dc`](#insn-00bba6dc)

~~~json
{
  "source": "00bba6dc",
  "target": "00bba6e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba6e4`](#insn-00bba6e4)

~~~json
{
  "source": "00bba6e4",
  "target": "00bba794",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba6f8`](#insn-00bba6f8)

~~~json
{
  "source": "00bba6f8",
  "target": "010a36c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba6fc`](#insn-00bba6fc)

~~~json
{
  "source": "00bba6fc",
  "target": "002a722d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a722d",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "5f5f6378615f67756172645f6163717569726500",
  "capture_start": "002a722d",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba6fc`](#insn-00bba6fc)

~~~json
{
  "source": "00bba6fc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba700`](#insn-00bba700)

~~~json
{
  "source": "00bba700",
  "target": "00bde7d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba704`](#insn-00bba704)

~~~json
{
  "source": "00bba704",
  "target": "00bba7b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba70c`](#insn-00bba70c)

~~~json
{
  "source": "00bba70c",
  "target": "00bba728",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba718`](#insn-00bba718)

~~~json
{
  "source": "00bba718",
  "target": "00be1da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba724`](#insn-00bba724)

~~~json
{
  "source": "00bba724",
  "target": "00bba7d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba73c`](#insn-00bba73c)

~~~json
{
  "source": "00bba73c",
  "target": "00bba758",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba748`](#insn-00bba748)

~~~json
{
  "source": "00bba748",
  "target": "010a36e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba74c`](#insn-00bba74c)

~~~json
{
  "source": "00bba74c",
  "target": "010a36c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba750`](#insn-00bba750)

~~~json
{
  "source": "00bba750",
  "target": "00be1180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba754`](#insn-00bba754)

~~~json
{
  "source": "00bba754",
  "target": "00bba738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba75c`](#insn-00bba75c)

~~~json
{
  "source": "00bba75c",
  "target": "00bba77c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba760`](#insn-00bba760)

~~~json
{
  "source": "00bba760",
  "target": "00bba770",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba768`](#insn-00bba768)

~~~json
{
  "source": "00bba768",
  "target": "00be1da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba780`](#insn-00bba780)

~~~json
{
  "source": "00bba780",
  "target": "010a36c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba784`](#insn-00bba784)

~~~json
{
  "source": "00bba784",
  "target": "00bde7e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba788`](#insn-00bba788)

~~~json
{
  "source": "00bba788",
  "target": "00bba7c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba794`](#insn-00bba794)

~~~json
{
  "source": "00bba794",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba798`](#insn-00bba798)

~~~json
{
  "source": "00bba798",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba79c`](#insn-00bba79c)

~~~json
{
  "source": "00bba79c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba7a0`](#insn-00bba7a0)

~~~json
{
  "source": "00bba7a0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba7b4`](#insn-00bba7b4)

~~~json
{
  "source": "00bba7b4",
  "target": "00296810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296810",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "2573206661696c656420746f2061637175697265206d7574657800",
  "capture_start": "00296810",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba7bc`](#insn-00bba7bc)

~~~json
{
  "source": "00bba7bc",
  "target": "002a722d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a722d",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "5f5f6378615f67756172645f6163717569726500",
  "capture_start": "002a722d",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba7c0`](#insn-00bba7c0)

~~~json
{
  "source": "00bba7c0",
  "target": "00bbb158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba7c8`](#insn-00bba7c8)

~~~json
{
  "source": "00bba7c8",
  "target": "002917e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002917e1",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "2573206661696c656420746f2072656c65617365206d7574657800",
  "capture_start": "002917e1",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba7d0`](#insn-00bba7d0)

~~~json
{
  "source": "00bba7d0",
  "target": "002a722d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a722d",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "5f5f6378615f67756172645f6163717569726500",
  "capture_start": "002a722d",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba7d4`](#insn-00bba7d4)

~~~json
{
  "source": "00bba7d4",
  "target": "00bbb158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba7dc`](#insn-00bba7dc)

~~~json
{
  "source": "00bba7dc",
  "target": "002ac533",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac533",
  "offset": 0,
  "size": 147,
  "datatype": "string",
  "bytes": "5f5f6378615f67756172645f6163717569726520646574656374656420726563",
  "capture_start": "002ac533",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bba7e0`](#insn-00bba7e0)

~~~json
{
  "source": "00bba7e0",
  "target": "00bbb158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
