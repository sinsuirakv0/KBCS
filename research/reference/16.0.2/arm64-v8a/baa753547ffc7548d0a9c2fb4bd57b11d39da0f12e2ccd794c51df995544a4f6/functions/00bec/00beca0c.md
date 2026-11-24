# 00beca0c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0082.md#review-d7bacce714309f5374539685658c68af)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0044.md#review-d7bacce714309f5374539685658c68af)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beca0c",
  "name": "FUN_00beca0c",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bca8ad55d8cb5cc8909fb6a58e1eaa2186fa6a692888727ccfa1a89ecdbd8301",
  "source_text_sha256": "bca8ad55d8cb5cc8909fb6a58e1eaa2186fa6a692888727ccfa1a89ecdbd8301",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beca0c",
        "00becb33"
      ]
    ],
    "bytes_sha256": "7af8958b2e3b37bc1438b9e225358afb247dcc98f171dd23589f0eba4b23784e",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be5c64](../00be5/00be5c64.md)
- [00bec76c](../00bec/00bec76c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1481 bytes

~~~c

void FUN_00beca0c(long *param_1,long *param_2,long *param_3,long *param_4,long *param_5)

{
  long lVar1;
  long lVar2;
  long lVar3;
  
  lVar1 = *param_2;
  lVar2 = *param_1;
  lVar3 = *param_3;
  if (lVar1 < lVar2) {
    if (lVar3 < lVar1) {
      *param_1 = lVar3;
    }
    else {
      *param_1 = lVar1;
      *param_2 = lVar2;
      lVar3 = *param_3;
      if (lVar2 <= lVar3) goto LAB_00beca8c;
      *param_2 = lVar3;
    }
    *param_3 = lVar2;
    lVar3 = lVar2;
  }
  else if (lVar3 < lVar1) {
    *param_2 = lVar3;
    *param_3 = lVar1;
    lVar2 = *param_1;
    lVar3 = lVar1;
    if (*param_2 < lVar2) {
      *param_1 = *param_2;
      *param_2 = lVar2;
      lVar3 = *param_3;
    }
  }
LAB_00beca8c:
  if (*param_4 < lVar3) {
    *param_3 = *param_4;
    *param_4 = lVar3;
    lVar3 = *param_2;
    if (*param_3 < lVar3) {
      *param_2 = *param_3;
      *param_3 = lVar3;
      lVar3 = *param_1;
      if (*param_2 < lVar3) {
        *param_1 = *param_2;
        *param_2 = lVar3;
      }
    }
  }
  lVar3 = *param_4;
  if (*param_5 < lVar3) {
    *param_4 = *param_5;
    *param_5 = lVar3;
    lVar3 = *param_3;
    if (*param_4 < lVar3) {
      *param_3 = *param_4;
      *param_4 = lVar3;
      lVar3 = *param_2;
      if (*param_3 < lVar3) {
        *param_2 = *param_3;
        *param_3 = lVar3;
        lVar3 = *param_1;
        if (*param_2 < lVar3) {
          *param_1 = *param_2;
          *param_2 = lVar3;
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
<a id="insn-00beca0c"></a> `00beca0c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00beca10"></a> `00beca10` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00beca14"></a> `00beca14` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00beca18"></a> `00beca18` | `4a 00 40 f9` | ldr x10,[x2] | `FALL_THROUGH`
<a id="insn-00beca1c"></a> `00beca1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beca20"></a> `00beca20` | `aa 00 00 54` | b.ge 0x00beca34 | `CONDITIONAL_JUMP`
<a id="insn-00beca24"></a> `00beca24` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00beca28"></a> `00beca28` | `ea 01 00 54` | b.ge 0x00beca64 | `CONDITIONAL_JUMP`
<a id="insn-00beca2c"></a> `00beca2c` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00beca30"></a> `00beca30` | `13 00 00 14` | b 0x00beca7c | `UNCONDITIONAL_JUMP`
<a id="insn-00beca34"></a> `00beca34` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00beca38"></a> `00beca38` | `8a 02 00 54` | b.ge 0x00beca88 | `CONDITIONAL_JUMP`
<a id="insn-00beca3c"></a> `00beca3c` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00beca40"></a> `00beca40` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00beca44"></a> `00beca44` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00beca48"></a> `00beca48` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00beca4c"></a> `00beca4c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00beca50"></a> `00beca50` | `ea 01 00 54` | b.ge 0x00beca8c | `CONDITIONAL_JUMP`
<a id="insn-00beca54"></a> `00beca54` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00beca58"></a> `00beca58` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00beca5c"></a> `00beca5c` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00beca60"></a> `00beca60` | `0b 00 00 14` | b 0x00beca8c | `UNCONDITIONAL_JUMP`
<a id="insn-00beca64"></a> `00beca64` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00beca68"></a> `00beca68` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00beca6c"></a> `00beca6c` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00beca70"></a> `00beca70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beca74"></a> `00beca74` | `ca 00 00 54` | b.ge 0x00beca8c | `CONDITIONAL_JUMP`
<a id="insn-00beca78"></a> `00beca78` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00beca7c"></a> `00beca7c` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00beca80"></a> `00beca80` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00beca84"></a> `00beca84` | `02 00 00 14` | b 0x00beca8c | `UNCONDITIONAL_JUMP`
<a id="insn-00beca88"></a> `00beca88` | `e8 03 0a aa` | mov x8,x10 | `FALL_THROUGH`
<a id="insn-00beca8c"></a> `00beca8c` | `69 00 40 f9` | ldr x9,[x3] | `FALL_THROUGH`
<a id="insn-00beca90"></a> `00beca90` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00beca94"></a> `00beca94` | `ea 01 00 54` | b.ge 0x00becad0 | `CONDITIONAL_JUMP`
<a id="insn-00beca98"></a> `00beca98` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00beca9c"></a> `00beca9c` | `68 00 00 f9` | str x8,[x3] | `FALL_THROUGH`
<a id="insn-00becaa0"></a> `00becaa0` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00becaa4"></a> `00becaa4` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00becaa8"></a> `00becaa8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00becaac"></a> `00becaac` | `2a 01 00 54` | b.ge 0x00becad0 | `CONDITIONAL_JUMP`
<a id="insn-00becab0"></a> `00becab0` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00becab4"></a> `00becab4` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00becab8"></a> `00becab8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00becabc"></a> `00becabc` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00becac0"></a> `00becac0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00becac4"></a> `00becac4` | `6a 00 00 54` | b.ge 0x00becad0 | `CONDITIONAL_JUMP`
<a id="insn-00becac8"></a> `00becac8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00becacc"></a> `00becacc` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00becad0"></a> `00becad0` | `88 00 40 f9` | ldr x8,[x4] | `FALL_THROUGH`
<a id="insn-00becad4"></a> `00becad4` | `69 00 40 f9` | ldr x9,[x3] | `FALL_THROUGH`
<a id="insn-00becad8"></a> `00becad8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00becadc"></a> `00becadc` | `aa 02 00 54` | b.ge 0x00becb30 | `CONDITIONAL_JUMP`
<a id="insn-00becae0"></a> `00becae0` | `68 00 00 f9` | str x8,[x3] | `FALL_THROUGH`
<a id="insn-00becae4"></a> `00becae4` | `89 00 00 f9` | str x9,[x4] | `FALL_THROUGH`
<a id="insn-00becae8"></a> `00becae8` | `68 00 40 f9` | ldr x8,[x3] | `FALL_THROUGH`
<a id="insn-00becaec"></a> `00becaec` | `49 00 40 f9` | ldr x9,[x2] | `FALL_THROUGH`
<a id="insn-00becaf0"></a> `00becaf0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00becaf4"></a> `00becaf4` | `ea 01 00 54` | b.ge 0x00becb30 | `CONDITIONAL_JUMP`
<a id="insn-00becaf8"></a> `00becaf8` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00becafc"></a> `00becafc` | `69 00 00 f9` | str x9,[x3] | `FALL_THROUGH`
<a id="insn-00becb00"></a> `00becb00` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00becb04"></a> `00becb04` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00becb08"></a> `00becb08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00becb0c"></a> `00becb0c` | `2a 01 00 54` | b.ge 0x00becb30 | `CONDITIONAL_JUMP`
<a id="insn-00becb10"></a> `00becb10` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00becb14"></a> `00becb14` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00becb18"></a> `00becb18` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00becb1c"></a> `00becb1c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00becb20"></a> `00becb20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00becb24"></a> `00becb24` | `6a 00 00 54` | b.ge 0x00becb30 | `CONDITIONAL_JUMP`
<a id="insn-00becb28"></a> `00becb28` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00becb2c"></a> `00becb2c` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00becb30"></a> `00becb30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00beca0c`](#insn-00beca0c) 範囲 `[['00beca0c', '00beca23']]`
  - `CONDITIONAL_JUMP` [`00beca20`](#insn-00beca20) → [`00beca34`](#insn-00beca34)
  - `FALL_THROUGH` [`00beca20`](#insn-00beca20) → [`00beca24`](#insn-00beca24)
- ブロック [`00beca24`](#insn-00beca24) 範囲 `[['00beca24', '00beca2b']]`
  - `CONDITIONAL_JUMP` [`00beca28`](#insn-00beca28) → [`00beca64`](#insn-00beca64)
  - `FALL_THROUGH` [`00beca28`](#insn-00beca28) → [`00beca2c`](#insn-00beca2c)
- ブロック [`00beca2c`](#insn-00beca2c) 範囲 `[['00beca2c', '00beca33']]`
  - `UNCONDITIONAL_JUMP` [`00beca30`](#insn-00beca30) → [`00beca7c`](#insn-00beca7c)
- ブロック [`00beca34`](#insn-00beca34) 範囲 `[['00beca34', '00beca3b']]`
  - `CONDITIONAL_JUMP` [`00beca38`](#insn-00beca38) → [`00beca88`](#insn-00beca88)
  - `FALL_THROUGH` [`00beca38`](#insn-00beca38) → [`00beca3c`](#insn-00beca3c)
- ブロック [`00beca3c`](#insn-00beca3c) 範囲 `[['00beca3c', '00beca53']]`
  - `CONDITIONAL_JUMP` [`00beca50`](#insn-00beca50) → [`00beca8c`](#insn-00beca8c)
  - `FALL_THROUGH` [`00beca50`](#insn-00beca50) → [`00beca54`](#insn-00beca54)
- ブロック [`00beca54`](#insn-00beca54) 範囲 `[['00beca54', '00beca63']]`
  - `UNCONDITIONAL_JUMP` [`00beca60`](#insn-00beca60) → [`00beca8c`](#insn-00beca8c)
- ブロック [`00beca64`](#insn-00beca64) 範囲 `[['00beca64', '00beca77']]`
  - `CONDITIONAL_JUMP` [`00beca74`](#insn-00beca74) → [`00beca8c`](#insn-00beca8c)
  - `FALL_THROUGH` [`00beca74`](#insn-00beca74) → [`00beca78`](#insn-00beca78)
- ブロック [`00beca78`](#insn-00beca78) 範囲 `[['00beca78', '00beca7b']]`
  - `FALL_THROUGH` [`00beca78`](#insn-00beca78) → [`00beca7c`](#insn-00beca7c)
- ブロック [`00beca7c`](#insn-00beca7c) 範囲 `[['00beca7c', '00beca87']]`
  - `UNCONDITIONAL_JUMP` [`00beca84`](#insn-00beca84) → [`00beca8c`](#insn-00beca8c)
- ブロック [`00beca88`](#insn-00beca88) 範囲 `[['00beca88', '00beca8b']]`
  - `FALL_THROUGH` [`00beca88`](#insn-00beca88) → [`00beca8c`](#insn-00beca8c)
- ブロック [`00beca8c`](#insn-00beca8c) 範囲 `[['00beca8c', '00beca97']]`
  - `CONDITIONAL_JUMP` [`00beca94`](#insn-00beca94) → [`00becad0`](#insn-00becad0)
  - `FALL_THROUGH` [`00beca94`](#insn-00beca94) → [`00beca98`](#insn-00beca98)
- ブロック [`00beca98`](#insn-00beca98) 範囲 `[['00beca98', '00becaaf']]`
  - `CONDITIONAL_JUMP` [`00becaac`](#insn-00becaac) → [`00becad0`](#insn-00becad0)
  - `FALL_THROUGH` [`00becaac`](#insn-00becaac) → [`00becab0`](#insn-00becab0)
- ブロック [`00becab0`](#insn-00becab0) 範囲 `[['00becab0', '00becac7']]`
  - `CONDITIONAL_JUMP` [`00becac4`](#insn-00becac4) → [`00becad0`](#insn-00becad0)
  - `FALL_THROUGH` [`00becac4`](#insn-00becac4) → [`00becac8`](#insn-00becac8)
- ブロック [`00becac8`](#insn-00becac8) 範囲 `[['00becac8', '00becacf']]`
  - `FALL_THROUGH` [`00becacc`](#insn-00becacc) → [`00becad0`](#insn-00becad0)
- ブロック [`00becad0`](#insn-00becad0) 範囲 `[['00becad0', '00becadf']]`
  - `CONDITIONAL_JUMP` [`00becadc`](#insn-00becadc) → [`00becb30`](#insn-00becb30)
  - `FALL_THROUGH` [`00becadc`](#insn-00becadc) → [`00becae0`](#insn-00becae0)
- ブロック [`00becae0`](#insn-00becae0) 範囲 `[['00becae0', '00becaf7']]`
  - `CONDITIONAL_JUMP` [`00becaf4`](#insn-00becaf4) → [`00becb30`](#insn-00becb30)
  - `FALL_THROUGH` [`00becaf4`](#insn-00becaf4) → [`00becaf8`](#insn-00becaf8)
- ブロック [`00becaf8`](#insn-00becaf8) 範囲 `[['00becaf8', '00becb0f']]`
  - `CONDITIONAL_JUMP` [`00becb0c`](#insn-00becb0c) → [`00becb30`](#insn-00becb30)
  - `FALL_THROUGH` [`00becb0c`](#insn-00becb0c) → [`00becb10`](#insn-00becb10)
- ブロック [`00becb10`](#insn-00becb10) 範囲 `[['00becb10', '00becb27']]`
  - `CONDITIONAL_JUMP` [`00becb24`](#insn-00becb24) → [`00becb30`](#insn-00becb30)
  - `FALL_THROUGH` [`00becb24`](#insn-00becb24) → [`00becb28`](#insn-00becb28)
- ブロック [`00becb28`](#insn-00becb28) 範囲 `[['00becb28', '00becb2f']]`
  - `FALL_THROUGH` [`00becb2c`](#insn-00becb2c) → [`00becb30`](#insn-00becb30)
- ブロック [`00becb30`](#insn-00becb30) 範囲 `[['00becb30', '00becb33']]`

## 命令位置別の参照

- [`00beca20`](#insn-00beca20) → [`00beca34`](#insn-00beca34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beca28`](#insn-00beca28) → [`00beca64`](#insn-00beca64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beca30`](#insn-00beca30) → [`00beca7c`](#insn-00beca7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beca38`](#insn-00beca38) → [`00beca88`](#insn-00beca88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beca50`](#insn-00beca50) → [`00beca8c`](#insn-00beca8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beca60`](#insn-00beca60) → [`00beca8c`](#insn-00beca8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beca74`](#insn-00beca74) → [`00beca8c`](#insn-00beca8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beca84`](#insn-00beca84) → [`00beca8c`](#insn-00beca8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beca94`](#insn-00beca94) → [`00becad0`](#insn-00becad0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becaac`](#insn-00becaac) → [`00becad0`](#insn-00becad0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becac4`](#insn-00becac4) → [`00becad0`](#insn-00becad0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becadc`](#insn-00becadc) → [`00becb30`](#insn-00becb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becaf4`](#insn-00becaf4) → [`00becb30`](#insn-00becb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becb0c`](#insn-00becb0c) → [`00becb30`](#insn-00becb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becb24`](#insn-00becb24) → [`00becb30`](#insn-00becb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beca20`](#insn-00beca20)

~~~json
{
  "source": "00beca20",
  "target": "00beca34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beca28`](#insn-00beca28)

~~~json
{
  "source": "00beca28",
  "target": "00beca64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beca30`](#insn-00beca30)

~~~json
{
  "source": "00beca30",
  "target": "00beca7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beca38`](#insn-00beca38)

~~~json
{
  "source": "00beca38",
  "target": "00beca88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beca50`](#insn-00beca50)

~~~json
{
  "source": "00beca50",
  "target": "00beca8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beca60`](#insn-00beca60)

~~~json
{
  "source": "00beca60",
  "target": "00beca8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beca74`](#insn-00beca74)

~~~json
{
  "source": "00beca74",
  "target": "00beca8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beca84`](#insn-00beca84)

~~~json
{
  "source": "00beca84",
  "target": "00beca8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beca94`](#insn-00beca94)

~~~json
{
  "source": "00beca94",
  "target": "00becad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becaac`](#insn-00becaac)

~~~json
{
  "source": "00becaac",
  "target": "00becad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becac4`](#insn-00becac4)

~~~json
{
  "source": "00becac4",
  "target": "00becad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becadc`](#insn-00becadc)

~~~json
{
  "source": "00becadc",
  "target": "00becb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becaf4`](#insn-00becaf4)

~~~json
{
  "source": "00becaf4",
  "target": "00becb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becb0c`](#insn-00becb0c)

~~~json
{
  "source": "00becb0c",
  "target": "00becb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becb24`](#insn-00becb24)

~~~json
{
  "source": "00becb24",
  "target": "00becb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
