# 00bfbb9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbb00`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb00.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-65d3b15066248a961a09571b62729782)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfcb90`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcb90.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-e2c70e5233c497ecae0799d51dd4726e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbb9c",
  "name": "_ZNSt6__ndk18ios_base15sync_with_stdioEb",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c8e368c8dd658f1cde99e599a10e6b8cf8c28e0b3ce67600ee39e0e9ff713ad6",
  "source_text_sha256": "c8e368c8dd658f1cde99e599a10e6b8cf8c28e0b3ce67600ee39e0e9ff713ad6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbb9c",
        "00bfbbb7"
      ]
    ],
    "bytes_sha256": "f5871099c6b6d0a9af94a3228c83993534a040f4ff5ee5865ce6333574d3f584",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 168 bytes

~~~c

undefined1 _ZNSt6__ndk18ios_base15sync_with_stdioEb(undefined1 param_1)

{
  undefined1 uVar1;
  
  uVar1 = DAT_00ca48d8;
  DAT_00ca48d8 = param_1;
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbb9c"></a> `00bfbb9c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbba0"></a> `00bfbba0` | `4a 05 00 b0` | adrp x10,0xca4000 | `FALL_THROUGH`
<a id="insn-00bfbba4"></a> `00bfbba4` | `e9 03 00 2a` | mov w9,w0 | `FALL_THROUGH`
<a id="insn-00bfbba8"></a> `00bfbba8` | `48 61 63 39` | ldrb w8,[x10, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bfbbac"></a> `00bfbbac` | `49 61 23 39` | strb w9,[x10, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bfbbb0"></a> `00bfbbb0` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00bfbbb4"></a> `00bfbbb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbb9c`](#insn-00bfbb9c) 範囲 `[['00bfbb9c', '00bfbbb7']]`

## 命令位置別の参照

- [`00bfbba8`](#insn-00bfbba8) → `00ca48d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfbbac`](#insn-00bfbbac) → `00ca48d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbba8`](#insn-00bfbba8)

~~~json
{
  "source": "00bfbba8",
  "target": "00ca48d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca48d8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfbbac`](#insn-00bfbbac)

~~~json
{
  "source": "00bfbbac",
  "target": "00ca48d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca48d8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
