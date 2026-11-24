# 00becc0c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 対応未確定
  - [v15.7.4 → v16.0.0 版の比較一覧](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/README.md)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0044.md#review-273754be030a37dbb1fa71422a2e51c0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00becc0c",
  "name": "FUN_00becc0c",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "32e73aa78f1966670805fb8aea062d6b5e59a2b1c7f8f9ff23dfd9b6e3368436",
  "source_text_sha256": "32e73aa78f1966670805fb8aea062d6b5e59a2b1c7f8f9ff23dfd9b6e3368436",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00becc0c",
        "00becd33"
      ]
    ],
    "bytes_sha256": "f8f1254738e345e86b10579253658224786fe5f1e21a43e34379cd1a22852dc9",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be5eb8](../00be5/00be5eb8.md)
- [00bec96c](../00bec/00bec96c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1877 bytes

~~~c

void FUN_00becc0c(ulong *param_1,ulong *param_2,ulong *param_3,ulong *param_4,ulong *param_5)

{
  ulong uVar1;
  ulong uVar2;
  ulong uVar3;
  
  uVar1 = *param_2;
  uVar2 = *param_1;
  uVar3 = *param_3;
  if (uVar1 < uVar2) {
    if (uVar3 < uVar1) {
      *param_1 = uVar3;
    }
    else {
      *param_1 = uVar1;
      *param_2 = uVar2;
      uVar3 = *param_3;
      if (uVar2 <= uVar3) goto LAB_00becc8c;
      *param_2 = uVar3;
    }
                    /* try { // try from 00becc80 to 00cecc8b has its CatchHandler @ 00bece88 */
    *param_3 = uVar2;
    uVar3 = uVar2;
  }
  else if (uVar3 < uVar1) {
    *param_2 = uVar3;
    *param_3 = uVar1;
    uVar2 = *param_1;
    uVar3 = uVar1;
    if (*param_2 < uVar2) {
      *param_1 = *param_2;
      *param_2 = uVar2;
      uVar3 = *param_3;
    }
  }
LAB_00becc8c:
  if (*param_4 < uVar3) {
    *param_3 = *param_4;
    *param_4 = uVar3;
    uVar3 = *param_2;
    if (*param_3 < uVar3) {
      *param_2 = *param_3;
                    /* try { // try from 00beccb4 to 00ceccbf has its CatchHandler @ 00bece78 */
      *param_3 = uVar3;
      uVar3 = *param_1;
                    /* try { // try from 00beccc0 to 00ceccdb has its CatchHandler @ 00bece98 */
      if (*param_2 < uVar3) {
        *param_1 = *param_2;
        *param_2 = uVar3;
      }
    }
  }
  uVar3 = *param_4;
                    /* try { // try from 00beccdc to 00cecf17 has its CatchHandler @ 00bec538 */
  if (*param_5 < uVar3) {
    *param_4 = *param_5;
    *param_5 = uVar3;
    uVar3 = *param_3;
    if (*param_4 < uVar3) {
      *param_3 = *param_4;
      *param_4 = uVar3;
      uVar3 = *param_2;
      if (*param_3 < uVar3) {
        *param_2 = *param_3;
        *param_3 = uVar3;
        uVar3 = *param_1;
        if (*param_2 < uVar3) {
          *param_1 = *param_2;
          *param_2 = uVar3;
        }
      }
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00becc0c"></a> `00becc0c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00becc10"></a> `00becc10` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00becc14"></a> `00becc14` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00becc18"></a> `00becc18` | `4a 00 40 f9` | ldr x10,[x2] | `FALL_THROUGH`
<a id="insn-00becc1c"></a> `00becc1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00becc20"></a> `00becc20` | `a2 00 00 54` | b.cs 0x00becc34 | `CONDITIONAL_JUMP`
<a id="insn-00becc24"></a> `00becc24` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00becc28"></a> `00becc28` | `e2 01 00 54` | b.cs 0x00becc64 | `CONDITIONAL_JUMP`
<a id="insn-00becc2c"></a> `00becc2c` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00becc30"></a> `00becc30` | `13 00 00 14` | b 0x00becc7c | `UNCONDITIONAL_JUMP`
<a id="insn-00becc34"></a> `00becc34` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00becc38"></a> `00becc38` | `82 02 00 54` | b.cs 0x00becc88 | `CONDITIONAL_JUMP`
<a id="insn-00becc3c"></a> `00becc3c` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00becc40"></a> `00becc40` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00becc44"></a> `00becc44` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00becc48"></a> `00becc48` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00becc4c"></a> `00becc4c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00becc50"></a> `00becc50` | `e2 01 00 54` | b.cs 0x00becc8c | `CONDITIONAL_JUMP`
<a id="insn-00becc54"></a> `00becc54` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00becc58"></a> `00becc58` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00becc5c"></a> `00becc5c` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00becc60"></a> `00becc60` | `0b 00 00 14` | b 0x00becc8c | `UNCONDITIONAL_JUMP`
<a id="insn-00becc64"></a> `00becc64` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00becc68"></a> `00becc68` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00becc6c"></a> `00becc6c` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00becc70"></a> `00becc70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00becc74"></a> `00becc74` | `c2 00 00 54` | b.cs 0x00becc8c | `CONDITIONAL_JUMP`
<a id="insn-00becc78"></a> `00becc78` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00becc7c"></a> `00becc7c` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00becc80"></a> `00becc80` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00becc84"></a> `00becc84` | `02 00 00 14` | b 0x00becc8c | `UNCONDITIONAL_JUMP`
<a id="insn-00becc88"></a> `00becc88` | `e8 03 0a aa` | mov x8,x10 | `FALL_THROUGH`
<a id="insn-00becc8c"></a> `00becc8c` | `69 00 40 f9` | ldr x9,[x3] | `FALL_THROUGH`
<a id="insn-00becc90"></a> `00becc90` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00becc94"></a> `00becc94` | `e2 01 00 54` | b.cs 0x00beccd0 | `CONDITIONAL_JUMP`
<a id="insn-00becc98"></a> `00becc98` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00becc9c"></a> `00becc9c` | `68 00 00 f9` | str x8,[x3] | `FALL_THROUGH`
<a id="insn-00becca0"></a> `00becca0` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00becca4"></a> `00becca4` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00becca8"></a> `00becca8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beccac"></a> `00beccac` | `22 01 00 54` | b.cs 0x00beccd0 | `CONDITIONAL_JUMP`
<a id="insn-00beccb0"></a> `00beccb0` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00beccb4"></a> `00beccb4` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00beccb8"></a> `00beccb8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00beccbc"></a> `00beccbc` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00beccc0"></a> `00beccc0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beccc4"></a> `00beccc4` | `62 00 00 54` | b.cs 0x00beccd0 | `CONDITIONAL_JUMP`
<a id="insn-00beccc8"></a> `00beccc8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00becccc"></a> `00becccc` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00beccd0"></a> `00beccd0` | `88 00 40 f9` | ldr x8,[x4] | `FALL_THROUGH`
<a id="insn-00beccd4"></a> `00beccd4` | `69 00 40 f9` | ldr x9,[x3] | `FALL_THROUGH`
<a id="insn-00beccd8"></a> `00beccd8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beccdc"></a> `00beccdc` | `a2 02 00 54` | b.cs 0x00becd30 | `CONDITIONAL_JUMP`
<a id="insn-00becce0"></a> `00becce0` | `68 00 00 f9` | str x8,[x3] | `FALL_THROUGH`
<a id="insn-00becce4"></a> `00becce4` | `89 00 00 f9` | str x9,[x4] | `FALL_THROUGH`
<a id="insn-00becce8"></a> `00becce8` | `68 00 40 f9` | ldr x8,[x3] | `FALL_THROUGH`
<a id="insn-00beccec"></a> `00beccec` | `49 00 40 f9` | ldr x9,[x2] | `FALL_THROUGH`
<a id="insn-00beccf0"></a> `00beccf0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beccf4"></a> `00beccf4` | `e2 01 00 54` | b.cs 0x00becd30 | `CONDITIONAL_JUMP`
<a id="insn-00beccf8"></a> `00beccf8` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00beccfc"></a> `00beccfc` | `69 00 00 f9` | str x9,[x3] | `FALL_THROUGH`
<a id="insn-00becd00"></a> `00becd00` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00becd04"></a> `00becd04` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00becd08"></a> `00becd08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00becd0c"></a> `00becd0c` | `22 01 00 54` | b.cs 0x00becd30 | `CONDITIONAL_JUMP`
<a id="insn-00becd10"></a> `00becd10` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00becd14"></a> `00becd14` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00becd18"></a> `00becd18` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00becd1c"></a> `00becd1c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00becd20"></a> `00becd20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00becd24"></a> `00becd24` | `62 00 00 54` | b.cs 0x00becd30 | `CONDITIONAL_JUMP`
<a id="insn-00becd28"></a> `00becd28` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00becd2c"></a> `00becd2c` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00becd30"></a> `00becd30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00becc0c`](#insn-00becc0c) 範囲 `[['00becc0c', '00becc23']]`
  - `CONDITIONAL_JUMP` [`00becc20`](#insn-00becc20) → [`00becc34`](#insn-00becc34)
  - `FALL_THROUGH` [`00becc20`](#insn-00becc20) → [`00becc24`](#insn-00becc24)
- ブロック [`00becc24`](#insn-00becc24) 範囲 `[['00becc24', '00becc2b']]`
  - `CONDITIONAL_JUMP` [`00becc28`](#insn-00becc28) → [`00becc64`](#insn-00becc64)
  - `FALL_THROUGH` [`00becc28`](#insn-00becc28) → [`00becc2c`](#insn-00becc2c)
- ブロック [`00becc2c`](#insn-00becc2c) 範囲 `[['00becc2c', '00becc33']]`
  - `UNCONDITIONAL_JUMP` [`00becc30`](#insn-00becc30) → [`00becc7c`](#insn-00becc7c)
- ブロック [`00becc34`](#insn-00becc34) 範囲 `[['00becc34', '00becc3b']]`
  - `CONDITIONAL_JUMP` [`00becc38`](#insn-00becc38) → [`00becc88`](#insn-00becc88)
  - `FALL_THROUGH` [`00becc38`](#insn-00becc38) → [`00becc3c`](#insn-00becc3c)
- ブロック [`00becc3c`](#insn-00becc3c) 範囲 `[['00becc3c', '00becc53']]`
  - `CONDITIONAL_JUMP` [`00becc50`](#insn-00becc50) → [`00becc8c`](#insn-00becc8c)
  - `FALL_THROUGH` [`00becc50`](#insn-00becc50) → [`00becc54`](#insn-00becc54)
- ブロック [`00becc54`](#insn-00becc54) 範囲 `[['00becc54', '00becc63']]`
  - `UNCONDITIONAL_JUMP` [`00becc60`](#insn-00becc60) → [`00becc8c`](#insn-00becc8c)
- ブロック [`00becc64`](#insn-00becc64) 範囲 `[['00becc64', '00becc77']]`
  - `CONDITIONAL_JUMP` [`00becc74`](#insn-00becc74) → [`00becc8c`](#insn-00becc8c)
  - `FALL_THROUGH` [`00becc74`](#insn-00becc74) → [`00becc78`](#insn-00becc78)
- ブロック [`00becc78`](#insn-00becc78) 範囲 `[['00becc78', '00becc7b']]`
  - `FALL_THROUGH` [`00becc78`](#insn-00becc78) → [`00becc7c`](#insn-00becc7c)
- ブロック [`00becc7c`](#insn-00becc7c) 範囲 `[['00becc7c', '00becc7f']]`
  - `FALL_THROUGH` [`00becc7c`](#insn-00becc7c) → [`00becc80`](#insn-00becc80)
- ブロック [`00becc80`](#insn-00becc80) 範囲 `[['00becc80', '00becc87']]`
  - `UNCONDITIONAL_JUMP` [`00becc84`](#insn-00becc84) → [`00becc8c`](#insn-00becc8c)
- ブロック [`00becc88`](#insn-00becc88) 範囲 `[['00becc88', '00becc8b']]`
  - `FALL_THROUGH` [`00becc88`](#insn-00becc88) → [`00becc8c`](#insn-00becc8c)
- ブロック [`00becc8c`](#insn-00becc8c) 範囲 `[['00becc8c', '00becc97']]`
  - `CONDITIONAL_JUMP` [`00becc94`](#insn-00becc94) → [`00beccd0`](#insn-00beccd0)
  - `FALL_THROUGH` [`00becc94`](#insn-00becc94) → [`00becc98`](#insn-00becc98)
- ブロック [`00becc98`](#insn-00becc98) 範囲 `[['00becc98', '00beccaf']]`
  - `CONDITIONAL_JUMP` [`00beccac`](#insn-00beccac) → [`00beccd0`](#insn-00beccd0)
  - `FALL_THROUGH` [`00beccac`](#insn-00beccac) → [`00beccb0`](#insn-00beccb0)
- ブロック [`00beccb0`](#insn-00beccb0) 範囲 `[['00beccb0', '00beccb3']]`
  - `FALL_THROUGH` [`00beccb0`](#insn-00beccb0) → [`00beccb4`](#insn-00beccb4)
- ブロック [`00beccb4`](#insn-00beccb4) 範囲 `[['00beccb4', '00beccbf']]`
  - `FALL_THROUGH` [`00beccbc`](#insn-00beccbc) → [`00beccc0`](#insn-00beccc0)
- ブロック [`00beccc0`](#insn-00beccc0) 範囲 `[['00beccc0', '00beccc7']]`
  - `CONDITIONAL_JUMP` [`00beccc4`](#insn-00beccc4) → [`00beccd0`](#insn-00beccd0)
  - `FALL_THROUGH` [`00beccc4`](#insn-00beccc4) → [`00beccc8`](#insn-00beccc8)
- ブロック [`00beccc8`](#insn-00beccc8) 範囲 `[['00beccc8', '00becccf']]`
  - `FALL_THROUGH` [`00becccc`](#insn-00becccc) → [`00beccd0`](#insn-00beccd0)
- ブロック [`00beccd0`](#insn-00beccd0) 範囲 `[['00beccd0', '00beccdb']]`
  - `FALL_THROUGH` [`00beccd8`](#insn-00beccd8) → [`00beccdc`](#insn-00beccdc)
- ブロック [`00beccdc`](#insn-00beccdc) 範囲 `[['00beccdc', '00beccdf']]`
  - `CONDITIONAL_JUMP` [`00beccdc`](#insn-00beccdc) → [`00becd30`](#insn-00becd30)
  - `FALL_THROUGH` [`00beccdc`](#insn-00beccdc) → [`00becce0`](#insn-00becce0)
- ブロック [`00becce0`](#insn-00becce0) 範囲 `[['00becce0', '00beccf7']]`
  - `CONDITIONAL_JUMP` [`00beccf4`](#insn-00beccf4) → [`00becd30`](#insn-00becd30)
  - `FALL_THROUGH` [`00beccf4`](#insn-00beccf4) → [`00beccf8`](#insn-00beccf8)
- ブロック [`00beccf8`](#insn-00beccf8) 範囲 `[['00beccf8', '00becd0f']]`
  - `CONDITIONAL_JUMP` [`00becd0c`](#insn-00becd0c) → [`00becd30`](#insn-00becd30)
  - `FALL_THROUGH` [`00becd0c`](#insn-00becd0c) → [`00becd10`](#insn-00becd10)
- ブロック [`00becd10`](#insn-00becd10) 範囲 `[['00becd10', '00becd27']]`
  - `CONDITIONAL_JUMP` [`00becd24`](#insn-00becd24) → [`00becd30`](#insn-00becd30)
  - `FALL_THROUGH` [`00becd24`](#insn-00becd24) → [`00becd28`](#insn-00becd28)
- ブロック [`00becd28`](#insn-00becd28) 範囲 `[['00becd28', '00becd2f']]`
  - `FALL_THROUGH` [`00becd2c`](#insn-00becd2c) → [`00becd30`](#insn-00becd30)
- ブロック [`00becd30`](#insn-00becd30) 範囲 `[['00becd30', '00becd33']]`

## 命令位置別の参照

- [`00becc20`](#insn-00becc20) → [`00becc34`](#insn-00becc34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becc28`](#insn-00becc28) → [`00becc64`](#insn-00becc64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becc30`](#insn-00becc30) → [`00becc7c`](#insn-00becc7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becc38`](#insn-00becc38) → [`00becc88`](#insn-00becc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becc50`](#insn-00becc50) → [`00becc8c`](#insn-00becc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becc60`](#insn-00becc60) → [`00becc8c`](#insn-00becc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becc74`](#insn-00becc74) → [`00becc8c`](#insn-00becc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becc84`](#insn-00becc84) → [`00becc8c`](#insn-00becc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becc94`](#insn-00becc94) → [`00beccd0`](#insn-00beccd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beccac`](#insn-00beccac) → [`00beccd0`](#insn-00beccd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beccc4`](#insn-00beccc4) → [`00beccd0`](#insn-00beccd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beccdc`](#insn-00beccdc) → [`00becd30`](#insn-00becd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beccf4`](#insn-00beccf4) → [`00becd30`](#insn-00becd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becd0c`](#insn-00becd0c) → [`00becd30`](#insn-00becd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becd24`](#insn-00becd24) → [`00becd30`](#insn-00becd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00becc20`](#insn-00becc20)

~~~json
{
  "source": "00becc20",
  "target": "00becc34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becc28`](#insn-00becc28)

~~~json
{
  "source": "00becc28",
  "target": "00becc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becc30`](#insn-00becc30)

~~~json
{
  "source": "00becc30",
  "target": "00becc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becc38`](#insn-00becc38)

~~~json
{
  "source": "00becc38",
  "target": "00becc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becc50`](#insn-00becc50)

~~~json
{
  "source": "00becc50",
  "target": "00becc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becc60`](#insn-00becc60)

~~~json
{
  "source": "00becc60",
  "target": "00becc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becc74`](#insn-00becc74)

~~~json
{
  "source": "00becc74",
  "target": "00becc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becc84`](#insn-00becc84)

~~~json
{
  "source": "00becc84",
  "target": "00becc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becc94`](#insn-00becc94)

~~~json
{
  "source": "00becc94",
  "target": "00beccd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beccac`](#insn-00beccac)

~~~json
{
  "source": "00beccac",
  "target": "00beccd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beccc4`](#insn-00beccc4)

~~~json
{
  "source": "00beccc4",
  "target": "00beccd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beccdc`](#insn-00beccdc)

~~~json
{
  "source": "00beccdc",
  "target": "00becd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beccf4`](#insn-00beccf4)

~~~json
{
  "source": "00beccf4",
  "target": "00becd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becd0c`](#insn-00becd0c)

~~~json
{
  "source": "00becd0c",
  "target": "00becd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becd24`](#insn-00becd24)

~~~json
{
  "source": "00becd24",
  "target": "00becd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
