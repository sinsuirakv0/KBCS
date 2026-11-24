# 00bffbdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffb40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffb40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-047f56273b254c92e3e0773514710951)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c00bd0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00bd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/reference_unresolved-0001.md#compare-dbe79fd03b25247be313dcf098457a9a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffbdc",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8in_availEv",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a5242ff87ed926a138a0843e7934c1af57247d4450860301d6706786a46b3dc8",
  "source_text_sha256": "a5242ff87ed926a138a0843e7934c1af57247d4450860301d6706786a46b3dc8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffbdc",
        "00bffc03"
      ]
    ],
    "bytes_sha256": "6ea1344968a22d2f65819df62bf7321f60f34f6069f1557a4842c3c06d297e1f",
    "instruction_count": 10,
    "instruction_bytes": 40,
    "body_bytes": 40,
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

long _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8in_availEv(long *param_1)

{
  long lVar1;
  
  if ((ulong)param_1[3] < (ulong)param_1[4]) {
    return param_1[4] - param_1[3] >> 2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffc00. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  lVar1 = (**(code **)(*param_1 + 0x38))();
  return lVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffbdc"></a> `00bffbdc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bffbe0"></a> `00bffbe0` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bffbe4"></a> `00bffbe4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bffbe8"></a> `00bffbe8` | `82 00 00 54` | b.cs 0x00bffbf8 | `CONDITIONAL_JUMP`
<a id="insn-00bffbec"></a> `00bffbec` | `28 01 08 cb` | sub x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00bffbf0"></a> `00bffbf0` | `00 fd 42 93` | asr x0,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bffbf4"></a> `00bffbf4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bffbf8"></a> `00bffbf8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bffbfc"></a> `00bffbfc` | `10 1d 40 f9` | ldr x16,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bffc00"></a> `00bffc00` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bffbdc`](#insn-00bffbdc) 範囲 `[['00bffbdc', '00bffbeb']]`
  - `CONDITIONAL_JUMP` [`00bffbe8`](#insn-00bffbe8) → [`00bffbf8`](#insn-00bffbf8)
  - `FALL_THROUGH` [`00bffbe8`](#insn-00bffbe8) → [`00bffbec`](#insn-00bffbec)
- ブロック [`00bffbec`](#insn-00bffbec) 範囲 `[['00bffbec', '00bffbf7']]`
- ブロック [`00bffbf8`](#insn-00bffbf8) 範囲 `[['00bffbf8', '00bffc03']]`

## 命令位置別の参照

- [`00bffbe8`](#insn-00bffbe8) → [`00bffbf8`](#insn-00bffbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffbe8`](#insn-00bffbe8)

~~~json
{
  "source": "00bffbe8",
  "target": "00bffbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
