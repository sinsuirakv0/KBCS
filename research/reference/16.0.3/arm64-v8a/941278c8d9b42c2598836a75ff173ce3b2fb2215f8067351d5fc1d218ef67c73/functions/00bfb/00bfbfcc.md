# 00bfbfcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfafd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfafd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0011.md#compare-9a8f40e8be56728e95a1de9f16f0415d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbfcc",
  "name": "_ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bdda3bb9d57b4bc8891875a8cfcf761f3764879e4c70b83fb75043c761da9009",
  "source_text_sha256": "bdda3bb9d57b4bc8891875a8cfcf761f3764879e4c70b83fb75043c761da9009",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbfcc",
        "00bfc00b"
      ]
    ],
    "bytes_sha256": "b6d1b4288c6fd3a975ef7df72786bd390ce687c34b5403e5f1b965c0c280c23a",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5f1f0](../00c5f/00c5f1f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 437 bytes

~~~c

void _ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE
               (long *param_1,undefined8 param_2,undefined8 *param_3)

{
  _ZNSt6__ndk112system_errorC2ENS_10error_codeERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
            (param_1,*param_3,param_3[1],param_2);
  *param_1 = (long)(PTR__ZTVNSt6__ndk18ios_base7failureE_00c9cb88 + 0x10);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbfcc"></a> `00bfbfcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbfd0"></a> `00bfbfd0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfbfd4"></a> `00bfbfd4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbfd8"></a> `00bfbfd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbfdc"></a> `00bfbfdc` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bfbfe0"></a> `00bfbfe0` | `41 08 40 a9` | ldp x1,x2,[x2] | `FALL_THROUGH`
<a id="insn-00bfbfe4"></a> `00bfbfe4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfbfe8"></a> `00bfbfe8` | `82 8c 01 94` | bl 0x00c5f1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbfec"></a> `00bfbfec` | `08 05 00 b0` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bfbff0"></a> `00bfbff0` | `08 c5 45 f9` | ldr x8,[x8, #0xb88] | `FALL_THROUGH`
<a id="insn-00bfbff4"></a> `00bfbff4` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bfbff8"></a> `00bfbff8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfbffc"></a> `00bfbffc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfc000"></a> `00bfc000` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfc004"></a> `00bfc004` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfc008"></a> `00bfc008` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbfcc`](#insn-00bfbfcc) 範囲 `[['00bfbfcc', '00bfc00b']]`

## 命令位置別の参照

- [`00bfbfd0`](#insn-00bfbfd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbfd4`](#insn-00bfbfd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbfe8`](#insn-00bfbfe8) → [`00c5f1f0`](../00c5f/00c5f1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f1f0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbff0`](#insn-00bfbff0) → `00c9cb88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfbff8`](#insn-00bfbff8) → `00c93e20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bfbffc`](#insn-00bfbffc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc000`](#insn-00bfc000) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbfd0`](#insn-00bfbfd0)

~~~json
{
  "source": "00bfbfd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbfd4`](#insn-00bfbfd4)

~~~json
{
  "source": "00bfbfd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbfe8`](#insn-00bfbfe8)

~~~json
{
  "source": "00bfbfe8",
  "target": "00c5f1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbff0`](#insn-00bfbff0)

~~~json
{
  "source": "00bfbff0",
  "target": "00c9cb88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9cb88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfbff8`](#insn-00bfbff8)

~~~json
{
  "source": "00bfbff8",
  "target": "00c93e20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93e10",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bfbffc`](#insn-00bfbffc)

~~~json
{
  "source": "00bfbffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc000`](#insn-00bfc000)

~~~json
{
  "source": "00bfc000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
