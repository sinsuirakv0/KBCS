# 00bbcb0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbcac8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcac8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-914d337d18c1732d2adc52b0fbf7f268)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0093.md#review-562612e96fb0bd18c580103b570e887e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcb0c",
  "name": "FUN_00bbcb0c",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be3b2d48250300ecacc2a2302f2378420278221aa6d4b3315adc5775d04d9b76",
  "source_text_sha256": "be3b2d48250300ecacc2a2302f2378420278221aa6d4b3315adc5775d04d9b76",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcb0c",
        "00bbcc0f"
      ]
    ],
    "bytes_sha256": "de644d8748d6776050978aa3d4dce42ae894590015c84cea170008c2f4d724a6",
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

- [00bde9d0](../00bde/00bde9d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1713 bytes

~~~c

void FUN_00bbcb0c(long param_1,long param_2,long param_3,long param_4,int param_5,uint param_6)

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
                    /* try { // try from 00bbcb64 to 00cbcb67 has its CatchHandler @ 00bbd304 */
                    /* try { // try from 00bbcb68 to 00cbcbaf has its CatchHandler @ 00bbb930 */
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
                    /* try { // try from 00bbcbb0 to 00cbcbb7 has its CatchHandler @ 00bbd32c */
      if (*(long *)(param_2 + 0x20) != param_3) {
                    /* try { // try from 00bbcbb8 to 00cbcbbf has its CatchHandler @ 00bbd114 */
        *(int *)(param_2 + 0x3c) = *(int *)(param_2 + 0x3c) + 1;
        goto LAB_00bbcc04;
      }
      iVar1 = *(int *)(param_2 + 0x30);
      if (*(int *)(param_2 + 0x30) == 2) {
                    /* try { // try from 00bbcbec to 00cbcbff has its CatchHandler @ 00bbd110 */
        *(int *)(param_2 + 0x30) = param_5;
        iVar1 = param_5;
      }
    }
    if ((iVar1 == 1) && (*(int *)(param_2 + 0x48) == 1)) {
LAB_00bbcc04:
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
<a id="insn-00bbcb0c"></a> `00bbcb0c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbcb10"></a> `00bbcb10` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcb14"></a> `00bbcb14` | `45 03 00 36` | tbz w5,#0x0,0x00bbcb7c | `CONDITIONAL_JUMP`
<a id="insn-00bbcb18"></a> `00bbcb18` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00bbcb1c"></a> `00bbcb1c` | `80 03 00 54` | b.eq 0x00bbcb8c | `CONDITIONAL_JUMP`
<a id="insn-00bbcb20"></a> `00bbcb20` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbcb24"></a> `00bbcb24` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbcb28"></a> `00bbcb28` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcb2c"></a> `00bbcb2c` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcb30"></a> `00bbcb30` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbcb34"></a> `00bbcb34` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcb38"></a> `00bbcb38` | `00 04 40 f9` | ldr x0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcb3c"></a> `00bbcb3c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbcb40"></a> `00bbcb40` | `f5 03 04 2a` | mov w21,w4 | `FALL_THROUGH`
<a id="insn-00bbcb44"></a> `00bbcb44` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00bbcb48"></a> `00bbcb48` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bbcb4c"></a> `00bbcb4c` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bbcb50"></a> `00bbcb50` | `a0 87 00 94` | bl 0x00bde9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb54"></a> `00bbcb54` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bbcb58"></a> `00bbcb58` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bbcb5c"></a> `00bbcb5c` | `e4 03 15 2a` | mov w4,w21 | `FALL_THROUGH`
<a id="insn-00bbcb60"></a> `00bbcb60` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbcb64"></a> `00bbcb64` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcb68"></a> `00bbcb68` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcb6c"></a> `00bbcb6c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbcb70"></a> `00bbcb70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbcb74"></a> `00bbcb74` | `c0 00 00 34` | cbz w0,0x00bbcb8c | `CONDITIONAL_JUMP`
<a id="insn-00bbcb78"></a> `00bbcb78` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbcb7c"></a> `00bbcb7c` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcb80"></a> `00bbcb80` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcb84"></a> `00bbcb84` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbcb88"></a> `00bbcb88` | `81 ff ff 54` | b.ne 0x00bbcb78 | `CONDITIONAL_JUMP`
<a id="insn-00bbcb8c"></a> `00bbcb8c` | `29 04 40 f9` | ldr x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bbcb90"></a> `00bbcb90` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcb94"></a> `00bbcb94` | `28 34 01 39` | strb w8,[x1, #0x4d] | `FALL_THROUGH`
<a id="insn-00bbcb98"></a> `00bbcb98` | `3f 01 03 eb` | cmp x9,x3 | `FALL_THROUGH`
<a id="insn-00bbcb9c"></a> `00bbcb9c` | `e1 fe ff 54` | b.ne 0x00bbcb78 | `CONDITIONAL_JUMP`
<a id="insn-00bbcba0"></a> `00bbcba0` | `29 10 40 f9` | ldr x9,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcba4"></a> `00bbcba4` | `28 30 01 39` | strb w8,[x1, #0x4c] | `FALL_THROUGH`
<a id="insn-00bbcba8"></a> `00bbcba8` | `e9 00 00 b4` | cbz x9,0x00bbcbc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbcbac"></a> `00bbcbac` | `3f 01 02 eb` | cmp x9,x2 | `FALL_THROUGH`
<a id="insn-00bbcbb0"></a> `00bbcbb0` | `60 01 00 54` | b.eq 0x00bbcbdc | `CONDITIONAL_JUMP`
<a id="insn-00bbcbb4"></a> `00bbcbb4` | `28 3c 40 b9` | ldr w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbcbb8"></a> `00bbcbb8` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcbbc"></a> `00bbcbbc` | `28 3c 00 b9` | str w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbcbc0"></a> `00bbcbc0` | `11 00 00 14` | b 0x00bbcc04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcbc4"></a> `00bbcbc4` | `9f 04 00 71` | cmp w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcbc8"></a> `00bbcbc8` | `22 10 00 f9` | str x2,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcbcc"></a> `00bbcbcc` | `24 30 00 b9` | str w4,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcbd0"></a> `00bbcbd0` | `28 3c 00 b9` | str w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbcbd4"></a> `00bbcbd4` | `20 01 00 54` | b.eq 0x00bbcbf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbcbd8"></a> `00bbcbd8` | `e8 ff ff 17` | b 0x00bbcb78 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcbdc"></a> `00bbcbdc` | `28 30 40 b9` | ldr w8,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcbe0"></a> `00bbcbe0` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbcbe4"></a> `00bbcbe4` | `61 00 00 54` | b.ne 0x00bbcbf0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcbe8"></a> `00bbcbe8` | `e8 03 04 2a` | mov w8,w4 | `FALL_THROUGH`
<a id="insn-00bbcbec"></a> `00bbcbec` | `24 30 00 b9` | str w4,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcbf0"></a> `00bbcbf0` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcbf4"></a> `00bbcbf4` | `21 fc ff 54` | b.ne 0x00bbcb78 | `CONDITIONAL_JUMP`
<a id="insn-00bbcbf8"></a> `00bbcbf8` | `28 48 40 b9` | ldr w8,[x1, #0x48] | `FALL_THROUGH`
<a id="insn-00bbcbfc"></a> `00bbcbfc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcc00"></a> `00bbcc00` | `c1 fb ff 54` | b.ne 0x00bbcb78 | `CONDITIONAL_JUMP`
<a id="insn-00bbcc04"></a> `00bbcc04` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcc08"></a> `00bbcc08` | `28 38 01 39` | strb w8,[x1, #0x4e] | `FALL_THROUGH`
<a id="insn-00bbcc0c"></a> `00bbcc0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbcb0c`](#insn-00bbcb0c) 範囲 `[['00bbcb0c', '00bbcb17']]`
  - `CONDITIONAL_JUMP` [`00bbcb14`](#insn-00bbcb14) → [`00bbcb7c`](#insn-00bbcb7c)
  - `FALL_THROUGH` [`00bbcb14`](#insn-00bbcb14) → [`00bbcb18`](#insn-00bbcb18)
- ブロック [`00bbcb18`](#insn-00bbcb18) 範囲 `[['00bbcb18', '00bbcb1f']]`
  - `CONDITIONAL_JUMP` [`00bbcb1c`](#insn-00bbcb1c) → [`00bbcb8c`](#insn-00bbcb8c)
  - `FALL_THROUGH` [`00bbcb1c`](#insn-00bbcb1c) → [`00bbcb20`](#insn-00bbcb20)
- ブロック [`00bbcb20`](#insn-00bbcb20) 範囲 `[['00bbcb20', '00bbcb63']]`
  - `FALL_THROUGH` [`00bbcb60`](#insn-00bbcb60) → [`00bbcb64`](#insn-00bbcb64)
- ブロック [`00bbcb64`](#insn-00bbcb64) 範囲 `[['00bbcb64', '00bbcb67']]`
  - `FALL_THROUGH` [`00bbcb64`](#insn-00bbcb64) → [`00bbcb68`](#insn-00bbcb68)
- ブロック [`00bbcb68`](#insn-00bbcb68) 範囲 `[['00bbcb68', '00bbcb77']]`
  - `CONDITIONAL_JUMP` [`00bbcb74`](#insn-00bbcb74) → [`00bbcb8c`](#insn-00bbcb8c)
  - `FALL_THROUGH` [`00bbcb74`](#insn-00bbcb74) → [`00bbcb78`](#insn-00bbcb78)
- ブロック [`00bbcb78`](#insn-00bbcb78) 範囲 `[['00bbcb78', '00bbcb7b']]`
- ブロック [`00bbcb7c`](#insn-00bbcb7c) 範囲 `[['00bbcb7c', '00bbcb8b']]`
  - `CONDITIONAL_JUMP` [`00bbcb88`](#insn-00bbcb88) → [`00bbcb78`](#insn-00bbcb78)
  - `FALL_THROUGH` [`00bbcb88`](#insn-00bbcb88) → [`00bbcb8c`](#insn-00bbcb8c)
- ブロック [`00bbcb8c`](#insn-00bbcb8c) 範囲 `[['00bbcb8c', '00bbcb9f']]`
  - `CONDITIONAL_JUMP` [`00bbcb9c`](#insn-00bbcb9c) → [`00bbcb78`](#insn-00bbcb78)
  - `FALL_THROUGH` [`00bbcb9c`](#insn-00bbcb9c) → [`00bbcba0`](#insn-00bbcba0)
- ブロック [`00bbcba0`](#insn-00bbcba0) 範囲 `[['00bbcba0', '00bbcbab']]`
  - `CONDITIONAL_JUMP` [`00bbcba8`](#insn-00bbcba8) → [`00bbcbc4`](#insn-00bbcbc4)
  - `FALL_THROUGH` [`00bbcba8`](#insn-00bbcba8) → [`00bbcbac`](#insn-00bbcbac)
- ブロック [`00bbcbac`](#insn-00bbcbac) 範囲 `[['00bbcbac', '00bbcbaf']]`
  - `FALL_THROUGH` [`00bbcbac`](#insn-00bbcbac) → [`00bbcbb0`](#insn-00bbcbb0)
- ブロック [`00bbcbb0`](#insn-00bbcbb0) 範囲 `[['00bbcbb0', '00bbcbb3']]`
  - `CONDITIONAL_JUMP` [`00bbcbb0`](#insn-00bbcbb0) → [`00bbcbdc`](#insn-00bbcbdc)
  - `FALL_THROUGH` [`00bbcbb0`](#insn-00bbcbb0) → [`00bbcbb4`](#insn-00bbcbb4)
- ブロック [`00bbcbb4`](#insn-00bbcbb4) 範囲 `[['00bbcbb4', '00bbcbb7']]`
  - `FALL_THROUGH` [`00bbcbb4`](#insn-00bbcbb4) → [`00bbcbb8`](#insn-00bbcbb8)
- ブロック [`00bbcbb8`](#insn-00bbcbb8) 範囲 `[['00bbcbb8', '00bbcbc3']]`
  - `UNCONDITIONAL_JUMP` [`00bbcbc0`](#insn-00bbcbc0) → [`00bbcc04`](#insn-00bbcc04)
- ブロック [`00bbcbc4`](#insn-00bbcbc4) 範囲 `[['00bbcbc4', '00bbcbd7']]`
  - `CONDITIONAL_JUMP` [`00bbcbd4`](#insn-00bbcbd4) → [`00bbcbf8`](#insn-00bbcbf8)
  - `FALL_THROUGH` [`00bbcbd4`](#insn-00bbcbd4) → [`00bbcbd8`](#insn-00bbcbd8)
- ブロック [`00bbcbd8`](#insn-00bbcbd8) 範囲 `[['00bbcbd8', '00bbcbdb']]`
  - `UNCONDITIONAL_JUMP` [`00bbcbd8`](#insn-00bbcbd8) → [`00bbcb78`](#insn-00bbcb78)
- ブロック [`00bbcbdc`](#insn-00bbcbdc) 範囲 `[['00bbcbdc', '00bbcbe7']]`
  - `CONDITIONAL_JUMP` [`00bbcbe4`](#insn-00bbcbe4) → [`00bbcbf0`](#insn-00bbcbf0)
  - `FALL_THROUGH` [`00bbcbe4`](#insn-00bbcbe4) → [`00bbcbe8`](#insn-00bbcbe8)
- ブロック [`00bbcbe8`](#insn-00bbcbe8) 範囲 `[['00bbcbe8', '00bbcbeb']]`
  - `FALL_THROUGH` [`00bbcbe8`](#insn-00bbcbe8) → [`00bbcbec`](#insn-00bbcbec)
- ブロック [`00bbcbec`](#insn-00bbcbec) 範囲 `[['00bbcbec', '00bbcbef']]`
  - `FALL_THROUGH` [`00bbcbec`](#insn-00bbcbec) → [`00bbcbf0`](#insn-00bbcbf0)
- ブロック [`00bbcbf0`](#insn-00bbcbf0) 範囲 `[['00bbcbf0', '00bbcbf7']]`
  - `CONDITIONAL_JUMP` [`00bbcbf4`](#insn-00bbcbf4) → [`00bbcb78`](#insn-00bbcb78)
  - `FALL_THROUGH` [`00bbcbf4`](#insn-00bbcbf4) → [`00bbcbf8`](#insn-00bbcbf8)
- ブロック [`00bbcbf8`](#insn-00bbcbf8) 範囲 `[['00bbcbf8', '00bbcc03']]`
  - `CONDITIONAL_JUMP` [`00bbcc00`](#insn-00bbcc00) → [`00bbcb78`](#insn-00bbcb78)
  - `FALL_THROUGH` [`00bbcc00`](#insn-00bbcc00) → [`00bbcc04`](#insn-00bbcc04)
- ブロック [`00bbcc04`](#insn-00bbcc04) 範囲 `[['00bbcc04', '00bbcc0f']]`

## 命令位置別の参照

- [`00bbcb14`](#insn-00bbcb14) → [`00bbcb7c`](#insn-00bbcb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb1c`](#insn-00bbcb1c) → [`00bbcb8c`](#insn-00bbcb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb24`](#insn-00bbcb24) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb28`](#insn-00bbcb28) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb2c`](#insn-00bbcb2c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb50`](#insn-00bbcb50) → [`00bde9d0`](../00bde/00bde9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde9d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb64`](#insn-00bbcb64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb68`](#insn-00bbcb68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb6c`](#insn-00bbcb6c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb74`](#insn-00bbcb74) → [`00bbcb8c`](#insn-00bbcb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb88`](#insn-00bbcb88) → [`00bbcb78`](#insn-00bbcb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb9c`](#insn-00bbcb9c) → [`00bbcb78`](#insn-00bbcb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcba8`](#insn-00bbcba8) → [`00bbcbc4`](#insn-00bbcbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbb0`](#insn-00bbcbb0) → [`00bbcbdc`](#insn-00bbcbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbc0`](#insn-00bbcbc0) → [`00bbcc04`](#insn-00bbcc04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbd4`](#insn-00bbcbd4) → [`00bbcbf8`](#insn-00bbcbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbd8`](#insn-00bbcbd8) → [`00bbcb78`](#insn-00bbcb78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbe4`](#insn-00bbcbe4) → [`00bbcbf0`](#insn-00bbcbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbf4`](#insn-00bbcbf4) → [`00bbcb78`](#insn-00bbcb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc00`](#insn-00bbcc00) → [`00bbcb78`](#insn-00bbcb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcb14`](#insn-00bbcb14)

~~~json
{
  "source": "00bbcb14",
  "target": "00bbcb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb1c`](#insn-00bbcb1c)

~~~json
{
  "source": "00bbcb1c",
  "target": "00bbcb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb24`](#insn-00bbcb24)

~~~json
{
  "source": "00bbcb24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb28`](#insn-00bbcb28)

~~~json
{
  "source": "00bbcb28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb2c`](#insn-00bbcb2c)

~~~json
{
  "source": "00bbcb2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb50`](#insn-00bbcb50)

~~~json
{
  "source": "00bbcb50",
  "target": "00bde9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb64`](#insn-00bbcb64)

~~~json
{
  "source": "00bbcb64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb68`](#insn-00bbcb68)

~~~json
{
  "source": "00bbcb68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb6c`](#insn-00bbcb6c)

~~~json
{
  "source": "00bbcb6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb74`](#insn-00bbcb74)

~~~json
{
  "source": "00bbcb74",
  "target": "00bbcb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb88`](#insn-00bbcb88)

~~~json
{
  "source": "00bbcb88",
  "target": "00bbcb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb9c`](#insn-00bbcb9c)

~~~json
{
  "source": "00bbcb9c",
  "target": "00bbcb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcba8`](#insn-00bbcba8)

~~~json
{
  "source": "00bbcba8",
  "target": "00bbcbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbb0`](#insn-00bbcbb0)

~~~json
{
  "source": "00bbcbb0",
  "target": "00bbcbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbc0`](#insn-00bbcbc0)

~~~json
{
  "source": "00bbcbc0",
  "target": "00bbcc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbd4`](#insn-00bbcbd4)

~~~json
{
  "source": "00bbcbd4",
  "target": "00bbcbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbd8`](#insn-00bbcbd8)

~~~json
{
  "source": "00bbcbd8",
  "target": "00bbcb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbe4`](#insn-00bbcbe4)

~~~json
{
  "source": "00bbcbe4",
  "target": "00bbcbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbf4`](#insn-00bbcbf4)

~~~json
{
  "source": "00bbcbf4",
  "target": "00bbcb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc00`](#insn-00bbcc00)

~~~json
{
  "source": "00bbcc00",
  "target": "00bbcb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
