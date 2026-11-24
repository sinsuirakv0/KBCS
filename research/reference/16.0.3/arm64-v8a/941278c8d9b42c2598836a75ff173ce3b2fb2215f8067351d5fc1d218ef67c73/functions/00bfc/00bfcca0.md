# 00bfcca0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbcac`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbcac.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-cfdfa1b7f3fc6d4879bbadbe7bf3a292)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcca0",
  "name": "FUN_00bfcca0",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2e43176f5aa2d08d040b47906c3dd808a9a2e7ac1800487c2c58778a32e4dfa",
  "source_text_sha256": "b2e43176f5aa2d08d040b47906c3dd808a9a2e7ac1800487c2c58778a32e4dfa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcca0",
        "00bfcccb"
      ]
    ],
    "bytes_sha256": "ea3e668d52e5c7158aedd60a80e925e6651c9f935af82f9234af091113e85aeb",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c5f3f0](../00c5f/00c5f3f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void FUN_00bfcca0(void *param_1)

{
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfcca0"></a> `00bfcca0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcca4"></a> `00bfcca4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfcca8"></a> `00bfcca8` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfccac"></a> `00bfccac` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfccb0"></a> `00bfccb0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfccb4"></a> `00bfccb4` | `cf 89 01 94` | bl 0x00c5f3f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfccb8"></a> `00bfccb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfccbc"></a> `00bfccbc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfccc0"></a> `00bfccc0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfccc4"></a> `00bfccc4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfccc8"></a> `00bfccc8` | `a2 70 01 14` | b 0x00c58f50 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcca0`](#insn-00bfcca0) 範囲 `[['00bfcca0', '00bfcccb']]`

## 命令位置別の参照

- [`00bfcca4`](#insn-00bfcca4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcca8`](#insn-00bfcca8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfccb4`](#insn-00bfccb4) → [`00c5f3f0`](../00c5f/00c5f3f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f3f0` · 推定シンボル `None` · 推定型 `None`
- [`00bfccbc`](#insn-00bfccbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfccc0`](#insn-00bfccc0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfccc8`](#insn-00bfccc8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcca4`](#insn-00bfcca4)

~~~json
{
  "source": "00bfcca4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcca8`](#insn-00bfcca8)

~~~json
{
  "source": "00bfcca8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfccb4`](#insn-00bfccb4)

~~~json
{
  "source": "00bfccb4",
  "target": "00c5f3f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfccbc`](#insn-00bfccbc)

~~~json
{
  "source": "00bfccbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfccc0`](#insn-00bfccc0)

~~~json
{
  "source": "00bfccc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfccc8`](#insn-00bfccc8)

~~~json
{
  "source": "00bfccc8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
