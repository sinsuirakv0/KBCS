# 00bffcc0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffc24`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffc24.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-1e8ff9ae06d0737ef9ecd6a9a73e720f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c00cb4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00cb4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/reference_unresolved-0001.md#compare-0292df092b10744c8a239b41bf20c270)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffcc0",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sgetcEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eace3b2d029b66dbc474267230cc40d5d029ce718ad9441d6096c05ad9821988",
  "source_text_sha256": "eace3b2d029b66dbc474267230cc40d5d029ce718ad9441d6096c05ad9821988",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffcc0",
        "00bffce3"
      ]
    ],
    "bytes_sha256": "3b22e2eeea29877065f720ae17e473daa83ea86e84a00867b4762fc7de4a188f",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 422 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sgetcEv(long *param_1)

{
  ulong uVar1;
  
  if ((uint *)param_1[3] != (uint *)param_1[4]) {
    return (ulong)*(uint *)param_1[3];
  }
                    /* WARNING: Could not recover jumptable at 0x00bffce0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar1 = (**(code **)(*param_1 + 0x48))();
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffcc0"></a> `00bffcc0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bffcc4"></a> `00bffcc4` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bffcc8"></a> `00bffcc8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bffccc"></a> `00bffccc` | `60 00 00 54` | b.eq 0x00bffcd8 | `CONDITIONAL_JUMP`
<a id="insn-00bffcd0"></a> `00bffcd0` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00bffcd4"></a> `00bffcd4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bffcd8"></a> `00bffcd8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bffcdc"></a> `00bffcdc` | `10 25 40 f9` | ldr x16,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bffce0"></a> `00bffce0` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bffcc0`](#insn-00bffcc0) 範囲 `[['00bffcc0', '00bffccf']]`
  - `CONDITIONAL_JUMP` [`00bffccc`](#insn-00bffccc) → [`00bffcd8`](#insn-00bffcd8)
  - `FALL_THROUGH` [`00bffccc`](#insn-00bffccc) → [`00bffcd0`](#insn-00bffcd0)
- ブロック [`00bffcd0`](#insn-00bffcd0) 範囲 `[['00bffcd0', '00bffcd7']]`
- ブロック [`00bffcd8`](#insn-00bffcd8) 範囲 `[['00bffcd8', '00bffce3']]`

## 命令位置別の参照

- [`00bffccc`](#insn-00bffccc) → [`00bffcd8`](#insn-00bffcd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffccc`](#insn-00bffccc)

~~~json
{
  "source": "00bffccc",
  "target": "00bffcd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
