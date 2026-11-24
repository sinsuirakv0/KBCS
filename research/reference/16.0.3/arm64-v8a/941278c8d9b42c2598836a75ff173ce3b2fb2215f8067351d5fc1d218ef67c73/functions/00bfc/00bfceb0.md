# 00bfceb0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbebc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbebc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/reference_unresolved-0001.md#compare-88f70b1c421e23eef85a1e157c02de52)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfceb0",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE7sungetcEv",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e2cea07a0ea076b0dc1f4ed56a17e56591ff479ba5a7ad5aa2d4ad46c9e9861",
  "source_text_sha256": "8e2cea07a0ea076b0dc1f4ed56a17e56591ff479ba5a7ad5aa2d4ad46c9e9861",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfceb0",
        "00bfcedf"
      ]
    ],
    "bytes_sha256": "cc050d2778023f8b1da4c0feec16c763dfa99ef97c0cdc70fabafe181290faf2",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
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

## 疑似コード / UTF-8 488 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE7sungetcEv(long *param_1)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = param_1[3];
  if (param_1[2] != lVar1) {
    param_1[3] = lVar1 + -1;
    return (ulong)*(byte *)(lVar1 + -1);
  }
                    /* WARNING: Could not recover jumptable at 0x00bfcedc. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x58))(param_1,0xffffffff);
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfceb0"></a> `00bfceb0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfceb4"></a> `00bfceb4` | `09 20 41 a9` | ldp x9,x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bfceb8"></a> `00bfceb8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfcebc"></a> `00bfcebc` | `a0 00 00 54` | b.eq 0x00bfced0 | `CONDITIONAL_JUMP`
<a id="insn-00bfcec0"></a> `00bfcec0` | `09 05 00 d1` | sub x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfcec4"></a> `00bfcec4` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfcec8"></a> `00bfcec8` | `00 f1 5f 38` | ldurb w0,[x8, #-0x1] | `FALL_THROUGH`
<a id="insn-00bfcecc"></a> `00bfcecc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfced0"></a> `00bfced0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfced4"></a> `00bfced4` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bfced8"></a> `00bfced8` | `10 2d 40 f9` | ldr x16,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bfcedc"></a> `00bfcedc` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfceb0`](#insn-00bfceb0) 範囲 `[['00bfceb0', '00bfcebf']]`
  - `CONDITIONAL_JUMP` [`00bfcebc`](#insn-00bfcebc) → [`00bfced0`](#insn-00bfced0)
  - `FALL_THROUGH` [`00bfcebc`](#insn-00bfcebc) → [`00bfcec0`](#insn-00bfcec0)
- ブロック [`00bfcec0`](#insn-00bfcec0) 範囲 `[['00bfcec0', '00bfcecf']]`
- ブロック [`00bfced0`](#insn-00bfced0) 範囲 `[['00bfced0', '00bfcedf']]`

## 命令位置別の参照

- [`00bfcebc`](#insn-00bfcebc) → [`00bfced0`](#insn-00bfced0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcebc`](#insn-00bfcebc)

~~~json
{
  "source": "00bfcebc",
  "target": "00bfced0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
