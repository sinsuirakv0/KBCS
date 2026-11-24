# 00bba9bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb99c8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb99c8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-ef44b9388bad0927f408cc6a8ebe55a2)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba9bc",
  "name": "_ZN8firebase9messaging8internal13IsInitializedEv",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1db4b0c3cd6cc1adc8646bad72329f55a60c2fa754f39af36e7d60c1c0560300",
  "source_text_sha256": "1db4b0c3cd6cc1adc8646bad72329f55a60c2fa754f39af36e7d60c1c0560300",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bba9bc",
        "00bba9cf"
      ]
    ],
    "bytes_sha256": "b0566e31de113f1d29bf8da3937963df37992099b27ba7fbaf264ae27e16f346",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e4b0](../00c5e/00c5e4b0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 95 bytes

~~~c

bool _ZN8firebase9messaging8internal13IsInitializedEv(void)

{
  return DAT_01127420 != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bba9bc"></a> `00bba9bc` | `68 2b 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bba9c0"></a> `00bba9c0` | `08 11 42 f9` | ldr x8,[x8, #0x420] | `FALL_THROUGH`
<a id="insn-00bba9c4"></a> `00bba9c4` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bba9c8"></a> `00bba9c8` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bba9cc"></a> `00bba9cc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bba9bc`](#insn-00bba9bc) 範囲 `[['00bba9bc', '00bba9cf']]`

## 命令位置別の参照

- [`00bba9c0`](#insn-00bba9c0) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bba9c0`](#insn-00bba9c0)

~~~json
{
  "source": "00bba9c0",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
