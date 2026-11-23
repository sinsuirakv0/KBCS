# 00bbcac8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbca00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbc/00bbca00.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-a5d1e7b72eeab3dcd71a8976c382d522)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbcb0c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcb0c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-914d337d18c1732d2adc52b0fbf7f268)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcac8",
  "name": "FUN_00bbcac8",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fcb55918311e486ff2611679b123a6c6928c55ac1a9ed8063237c4eb368f959b",
  "source_text_sha256": "fcb55918311e486ff2611679b123a6c6928c55ac1a9ed8063237c4eb368f959b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcac8",
        "00bbcbcb"
      ]
    ],
    "bytes_sha256": "bb57999fd2d6c1ec94127c990d95bf2bc781c1a40742fd8dcb483049bd71b385",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde980](../00bde/00bde980.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1713 bytes

~~~c

void FUN_00bbcac8(long param_1,long param_2,long param_3,long param_4,int param_5,uint param_6)

{
  int iVar1;
  long lVar2;
  
  lVar2 = *(long *)(param_2 + 0x10);
  if ((param_6 & 1) == 0) {
    if (*(long *)(param_1 + 8) != *(long *)(lVar2 + 8)) {
      return;
    }
  }
  else {
                    /* try { // try from 00bbcb20 to 00cbcb23 has its CatchHandler @ 00bbd2c0 */
                    /* try { // try from 00bbcb24 to 00cbcb6b has its CatchHandler @ 00bbb8ec */
    if ((lVar2 != param_1) &&
       (iVar1 = strcmp(*(char **)(param_1 + 8),*(char **)(lVar2 + 8)), iVar1 != 0)) {
      return;
    }
  }
  *(undefined1 *)(param_2 + 0x4d) = 1;
  if (*(long *)(param_2 + 8) == param_4) {
    *(undefined1 *)(param_2 + 0x4c) = 1;
    if (*(long *)(param_2 + 0x20) == 0) {
      *(long *)(param_2 + 0x20) = param_3;
      *(int *)(param_2 + 0x30) = param_5;
      *(undefined4 *)(param_2 + 0x3c) = 1;
      iVar1 = param_5;
    }
    else {
                    /* try { // try from 00bbcb6c to 00cbcb73 has its CatchHandler @ 00bbd2e8 */
      if (*(long *)(param_2 + 0x20) != param_3) {
                    /* try { // try from 00bbcb74 to 00cbcb7b has its CatchHandler @ 00bbd0d0 */
        *(int *)(param_2 + 0x3c) = *(int *)(param_2 + 0x3c) + 1;
        goto LAB_00bbcbc0;
      }
      iVar1 = *(int *)(param_2 + 0x30);
      if (*(int *)(param_2 + 0x30) == 2) {
                    /* try { // try from 00bbcba8 to 00cbcbbb has its CatchHandler @ 00bbd0cc */
        *(int *)(param_2 + 0x30) = param_5;
        iVar1 = param_5;
      }
    }
    if ((iVar1 == 1) && (*(int *)(param_2 + 0x48) == 1)) {
LAB_00bbcbc0:
      *(undefined1 *)(param_2 + 0x4e) = 1;
      return;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbcac8"></a> `00bbcac8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbcacc"></a> `00bbcacc` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcad0"></a> `00bbcad0` | `45 03 00 36` | tbz w5,#0x0,0x00bbcb38 | `CONDITIONAL_JUMP`
<a id="insn-00bbcad4"></a> `00bbcad4` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00bbcad8"></a> `00bbcad8` | `80 03 00 54` | b.eq 0x00bbcb48 | `CONDITIONAL_JUMP`
<a id="insn-00bbcadc"></a> `00bbcadc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbcae0"></a> `00bbcae0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbcae4"></a> `00bbcae4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcae8"></a> `00bbcae8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcaec"></a> `00bbcaec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbcaf0"></a> `00bbcaf0` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcaf4"></a> `00bbcaf4` | `00 04 40 f9` | ldr x0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcaf8"></a> `00bbcaf8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbcafc"></a> `00bbcafc` | `f5 03 04 2a` | mov w21,w4 | `FALL_THROUGH`
<a id="insn-00bbcb00"></a> `00bbcb00` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00bbcb04"></a> `00bbcb04` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bbcb08"></a> `00bbcb08` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bbcb0c"></a> `00bbcb0c` | `9d 87 00 94` | bl 0x00bde980 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb10"></a> `00bbcb10` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bbcb14"></a> `00bbcb14` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bbcb18"></a> `00bbcb18` | `e4 03 15 2a` | mov w4,w21 | `FALL_THROUGH`
<a id="insn-00bbcb1c"></a> `00bbcb1c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbcb20"></a> `00bbcb20` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcb24"></a> `00bbcb24` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcb28"></a> `00bbcb28` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbcb2c"></a> `00bbcb2c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbcb30"></a> `00bbcb30` | `c0 00 00 34` | cbz w0,0x00bbcb48 | `CONDITIONAL_JUMP`
<a id="insn-00bbcb34"></a> `00bbcb34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbcb38"></a> `00bbcb38` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcb3c"></a> `00bbcb3c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcb40"></a> `00bbcb40` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbcb44"></a> `00bbcb44` | `81 ff ff 54` | b.ne 0x00bbcb34 | `CONDITIONAL_JUMP`
<a id="insn-00bbcb48"></a> `00bbcb48` | `29 04 40 f9` | ldr x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcb4c"></a> `00bbcb4c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcb50"></a> `00bbcb50` | `28 34 01 39` | strb w8,[x1, #0x4d] | `FALL_THROUGH`
<a id="insn-00bbcb54"></a> `00bbcb54` | `3f 01 03 eb` | cmp x9,x3 | `FALL_THROUGH`
<a id="insn-00bbcb58"></a> `00bbcb58` | `e1 fe ff 54` | b.ne 0x00bbcb34 | `CONDITIONAL_JUMP`
<a id="insn-00bbcb5c"></a> `00bbcb5c` | `29 10 40 f9` | ldr x9,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcb60"></a> `00bbcb60` | `28 30 01 39` | strb w8,[x1, #0x4c] | `FALL_THROUGH`
<a id="insn-00bbcb64"></a> `00bbcb64` | `e9 00 00 b4` | cbz x9,0x00bbcb80 | `CONDITIONAL_JUMP`
<a id="insn-00bbcb68"></a> `00bbcb68` | `3f 01 02 eb` | cmp x9,x2 | `FALL_THROUGH`
<a id="insn-00bbcb6c"></a> `00bbcb6c` | `60 01 00 54` | b.eq 0x00bbcb98 | `CONDITIONAL_JUMP`
<a id="insn-00bbcb70"></a> `00bbcb70` | `28 3c 40 b9` | ldr w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbcb74"></a> `00bbcb74` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcb78"></a> `00bbcb78` | `28 3c 00 b9` | str w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbcb7c"></a> `00bbcb7c` | `11 00 00 14` | b 0x00bbcbc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcb80"></a> `00bbcb80` | `9f 04 00 71` | cmp w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcb84"></a> `00bbcb84` | `22 10 00 f9` | str x2,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcb88"></a> `00bbcb88` | `24 30 00 b9` | str w4,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcb8c"></a> `00bbcb8c` | `28 3c 00 b9` | str w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbcb90"></a> `00bbcb90` | `20 01 00 54` | b.eq 0x00bbcbb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbcb94"></a> `00bbcb94` | `e8 ff ff 17` | b 0x00bbcb34 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcb98"></a> `00bbcb98` | `28 30 40 b9` | ldr w8,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcb9c"></a> `00bbcb9c` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbcba0"></a> `00bbcba0` | `61 00 00 54` | b.ne 0x00bbcbac | `CONDITIONAL_JUMP`
<a id="insn-00bbcba4"></a> `00bbcba4` | `e8 03 04 2a` | mov w8,w4 | `FALL_THROUGH`
<a id="insn-00bbcba8"></a> `00bbcba8` | `24 30 00 b9` | str w4,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcbac"></a> `00bbcbac` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcbb0"></a> `00bbcbb0` | `21 fc ff 54` | b.ne 0x00bbcb34 | `CONDITIONAL_JUMP`
<a id="insn-00bbcbb4"></a> `00bbcbb4` | `28 48 40 b9` | ldr w8,[x1, #0x48] | `FALL_THROUGH`
<a id="insn-00bbcbb8"></a> `00bbcbb8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcbbc"></a> `00bbcbbc` | `c1 fb ff 54` | b.ne 0x00bbcb34 | `CONDITIONAL_JUMP`
<a id="insn-00bbcbc0"></a> `00bbcbc0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcbc4"></a> `00bbcbc4` | `28 38 01 39` | strb w8,[x1, #0x4e] | `FALL_THROUGH`
<a id="insn-00bbcbc8"></a> `00bbcbc8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbcac8`](#insn-00bbcac8) 範囲 `[['00bbcac8', '00bbcad3']]`
  - `CONDITIONAL_JUMP` [`00bbcad0`](#insn-00bbcad0) → [`00bbcb38`](#insn-00bbcb38)
  - `FALL_THROUGH` [`00bbcad0`](#insn-00bbcad0) → [`00bbcad4`](#insn-00bbcad4)
- ブロック [`00bbcad4`](#insn-00bbcad4) 範囲 `[['00bbcad4', '00bbcadb']]`
  - `CONDITIONAL_JUMP` [`00bbcad8`](#insn-00bbcad8) → [`00bbcb48`](#insn-00bbcb48)
  - `FALL_THROUGH` [`00bbcad8`](#insn-00bbcad8) → [`00bbcadc`](#insn-00bbcadc)
- ブロック [`00bbcadc`](#insn-00bbcadc) 範囲 `[['00bbcadc', '00bbcb1f']]`
  - `FALL_THROUGH` [`00bbcb1c`](#insn-00bbcb1c) → [`00bbcb20`](#insn-00bbcb20)
- ブロック [`00bbcb20`](#insn-00bbcb20) 範囲 `[['00bbcb20', '00bbcb23']]`
  - `FALL_THROUGH` [`00bbcb20`](#insn-00bbcb20) → [`00bbcb24`](#insn-00bbcb24)
- ブロック [`00bbcb24`](#insn-00bbcb24) 範囲 `[['00bbcb24', '00bbcb33']]`
  - `CONDITIONAL_JUMP` [`00bbcb30`](#insn-00bbcb30) → [`00bbcb48`](#insn-00bbcb48)
  - `FALL_THROUGH` [`00bbcb30`](#insn-00bbcb30) → [`00bbcb34`](#insn-00bbcb34)
- ブロック [`00bbcb34`](#insn-00bbcb34) 範囲 `[['00bbcb34', '00bbcb37']]`
- ブロック [`00bbcb38`](#insn-00bbcb38) 範囲 `[['00bbcb38', '00bbcb47']]`
  - `CONDITIONAL_JUMP` [`00bbcb44`](#insn-00bbcb44) → [`00bbcb34`](#insn-00bbcb34)
  - `FALL_THROUGH` [`00bbcb44`](#insn-00bbcb44) → [`00bbcb48`](#insn-00bbcb48)
- ブロック [`00bbcb48`](#insn-00bbcb48) 範囲 `[['00bbcb48', '00bbcb5b']]`
  - `CONDITIONAL_JUMP` [`00bbcb58`](#insn-00bbcb58) → [`00bbcb34`](#insn-00bbcb34)
  - `FALL_THROUGH` [`00bbcb58`](#insn-00bbcb58) → [`00bbcb5c`](#insn-00bbcb5c)
- ブロック [`00bbcb5c`](#insn-00bbcb5c) 範囲 `[['00bbcb5c', '00bbcb67']]`
  - `CONDITIONAL_JUMP` [`00bbcb64`](#insn-00bbcb64) → [`00bbcb80`](#insn-00bbcb80)
  - `FALL_THROUGH` [`00bbcb64`](#insn-00bbcb64) → [`00bbcb68`](#insn-00bbcb68)
- ブロック [`00bbcb68`](#insn-00bbcb68) 範囲 `[['00bbcb68', '00bbcb6b']]`
  - `FALL_THROUGH` [`00bbcb68`](#insn-00bbcb68) → [`00bbcb6c`](#insn-00bbcb6c)
- ブロック [`00bbcb6c`](#insn-00bbcb6c) 範囲 `[['00bbcb6c', '00bbcb6f']]`
  - `CONDITIONAL_JUMP` [`00bbcb6c`](#insn-00bbcb6c) → [`00bbcb98`](#insn-00bbcb98)
  - `FALL_THROUGH` [`00bbcb6c`](#insn-00bbcb6c) → [`00bbcb70`](#insn-00bbcb70)
- ブロック [`00bbcb70`](#insn-00bbcb70) 範囲 `[['00bbcb70', '00bbcb73']]`
  - `FALL_THROUGH` [`00bbcb70`](#insn-00bbcb70) → [`00bbcb74`](#insn-00bbcb74)
- ブロック [`00bbcb74`](#insn-00bbcb74) 範囲 `[['00bbcb74', '00bbcb7f']]`
  - `UNCONDITIONAL_JUMP` [`00bbcb7c`](#insn-00bbcb7c) → [`00bbcbc0`](#insn-00bbcbc0)
- ブロック [`00bbcb80`](#insn-00bbcb80) 範囲 `[['00bbcb80', '00bbcb93']]`
  - `CONDITIONAL_JUMP` [`00bbcb90`](#insn-00bbcb90) → [`00bbcbb4`](#insn-00bbcbb4)
  - `FALL_THROUGH` [`00bbcb90`](#insn-00bbcb90) → [`00bbcb94`](#insn-00bbcb94)
- ブロック [`00bbcb94`](#insn-00bbcb94) 範囲 `[['00bbcb94', '00bbcb97']]`
  - `UNCONDITIONAL_JUMP` [`00bbcb94`](#insn-00bbcb94) → [`00bbcb34`](#insn-00bbcb34)
- ブロック [`00bbcb98`](#insn-00bbcb98) 範囲 `[['00bbcb98', '00bbcba3']]`
  - `CONDITIONAL_JUMP` [`00bbcba0`](#insn-00bbcba0) → [`00bbcbac`](#insn-00bbcbac)
  - `FALL_THROUGH` [`00bbcba0`](#insn-00bbcba0) → [`00bbcba4`](#insn-00bbcba4)
- ブロック [`00bbcba4`](#insn-00bbcba4) 範囲 `[['00bbcba4', '00bbcba7']]`
  - `FALL_THROUGH` [`00bbcba4`](#insn-00bbcba4) → [`00bbcba8`](#insn-00bbcba8)
- ブロック [`00bbcba8`](#insn-00bbcba8) 範囲 `[['00bbcba8', '00bbcbab']]`
  - `FALL_THROUGH` [`00bbcba8`](#insn-00bbcba8) → [`00bbcbac`](#insn-00bbcbac)
- ブロック [`00bbcbac`](#insn-00bbcbac) 範囲 `[['00bbcbac', '00bbcbb3']]`
  - `CONDITIONAL_JUMP` [`00bbcbb0`](#insn-00bbcbb0) → [`00bbcb34`](#insn-00bbcb34)
  - `FALL_THROUGH` [`00bbcbb0`](#insn-00bbcbb0) → [`00bbcbb4`](#insn-00bbcbb4)
- ブロック [`00bbcbb4`](#insn-00bbcbb4) 範囲 `[['00bbcbb4', '00bbcbbf']]`
  - `CONDITIONAL_JUMP` [`00bbcbbc`](#insn-00bbcbbc) → [`00bbcb34`](#insn-00bbcb34)
  - `FALL_THROUGH` [`00bbcbbc`](#insn-00bbcbbc) → [`00bbcbc0`](#insn-00bbcbc0)
- ブロック [`00bbcbc0`](#insn-00bbcbc0) 範囲 `[['00bbcbc0', '00bbcbcb']]`

## 命令位置別の参照

- [`00bbcad0`](#insn-00bbcad0) → [`00bbcb38`](#insn-00bbcb38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcad8`](#insn-00bbcad8) → [`00bbcb48`](#insn-00bbcb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcae0`](#insn-00bbcae0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcae4`](#insn-00bbcae4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcae8`](#insn-00bbcae8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb0c`](#insn-00bbcb0c) → [`00bde980`](../00bde/00bde980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde980` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb20`](#insn-00bbcb20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb24`](#insn-00bbcb24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb28`](#insn-00bbcb28) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb30`](#insn-00bbcb30) → [`00bbcb48`](#insn-00bbcb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb44`](#insn-00bbcb44) → [`00bbcb34`](#insn-00bbcb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb58`](#insn-00bbcb58) → [`00bbcb34`](#insn-00bbcb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb64`](#insn-00bbcb64) → [`00bbcb80`](#insn-00bbcb80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb6c`](#insn-00bbcb6c) → [`00bbcb98`](#insn-00bbcb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb7c`](#insn-00bbcb7c) → [`00bbcbc0`](#insn-00bbcbc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb90`](#insn-00bbcb90) → [`00bbcbb4`](#insn-00bbcbb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb94`](#insn-00bbcb94) → [`00bbcb34`](#insn-00bbcb34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcba0`](#insn-00bbcba0) → [`00bbcbac`](#insn-00bbcbac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbb0`](#insn-00bbcbb0) → [`00bbcb34`](#insn-00bbcb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbbc`](#insn-00bbcbbc) → [`00bbcb34`](#insn-00bbcb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcad0`](#insn-00bbcad0)

~~~json
{
  "source": "00bbcad0",
  "target": "00bbcb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcad8`](#insn-00bbcad8)

~~~json
{
  "source": "00bbcad8",
  "target": "00bbcb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcae0`](#insn-00bbcae0)

~~~json
{
  "source": "00bbcae0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcae4`](#insn-00bbcae4)

~~~json
{
  "source": "00bbcae4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcae8`](#insn-00bbcae8)

~~~json
{
  "source": "00bbcae8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb0c`](#insn-00bbcb0c)

~~~json
{
  "source": "00bbcb0c",
  "target": "00bde980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb20`](#insn-00bbcb20)

~~~json
{
  "source": "00bbcb20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb24`](#insn-00bbcb24)

~~~json
{
  "source": "00bbcb24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb28`](#insn-00bbcb28)

~~~json
{
  "source": "00bbcb28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb30`](#insn-00bbcb30)

~~~json
{
  "source": "00bbcb30",
  "target": "00bbcb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb44`](#insn-00bbcb44)

~~~json
{
  "source": "00bbcb44",
  "target": "00bbcb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb58`](#insn-00bbcb58)

~~~json
{
  "source": "00bbcb58",
  "target": "00bbcb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb64`](#insn-00bbcb64)

~~~json
{
  "source": "00bbcb64",
  "target": "00bbcb80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb6c`](#insn-00bbcb6c)

~~~json
{
  "source": "00bbcb6c",
  "target": "00bbcb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb7c`](#insn-00bbcb7c)

~~~json
{
  "source": "00bbcb7c",
  "target": "00bbcbc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb90`](#insn-00bbcb90)

~~~json
{
  "source": "00bbcb90",
  "target": "00bbcbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb94`](#insn-00bbcb94)

~~~json
{
  "source": "00bbcb94",
  "target": "00bbcb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcba0`](#insn-00bbcba0)

~~~json
{
  "source": "00bbcba0",
  "target": "00bbcbac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbb0`](#insn-00bbcbb0)

~~~json
{
  "source": "00bbcbb0",
  "target": "00bbcb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbbc`](#insn-00bbcbbc)

~~~json
{
  "source": "00bbcbbc",
  "target": "00bbcb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
