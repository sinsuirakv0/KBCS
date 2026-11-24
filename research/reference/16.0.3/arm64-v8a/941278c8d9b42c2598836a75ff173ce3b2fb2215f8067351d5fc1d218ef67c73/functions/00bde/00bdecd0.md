# 00bdecd0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddcdc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddcdc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0010.md#compare-ac5c8a17dad3d78bd550f73f413a18c2)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdecd0",
  "name": "_ZN8firebase4auth18userprofilebuilder8GetClassEv",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d934cdb7850f78a077141af991111690d9467e86392d901b54d3b2f72c1b0fa",
  "source_text_sha256": "7d934cdb7850f78a077141af991111690d9467e86392d901b54d3b2f72c1b0fa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdecd0",
        "00bdecdb"
      ]
    ],
    "bytes_sha256": "9bd5dd78b088845e45496bf4b8164b64ea023d12675518b54b9c0bfaa4d194ff",
    "instruction_count": 3,
    "instruction_bytes": 12,
    "body_bytes": 12,
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

## 疑似コード / UTF-8 96 bytes

~~~c

undefined8 _ZN8firebase4auth18userprofilebuilder8GetClassEv(void)

{
  return DAT_01127ee8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdecd0"></a> `00bdecd0` | `48 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdecd4"></a> `00bdecd4` | `00 75 47 f9` | ldr x0,[x8, #0xee8] | `FALL_THROUGH`
<a id="insn-00bdecd8"></a> `00bdecd8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdecd0`](#insn-00bdecd0) 範囲 `[['00bdecd0', '00bdecdb']]`

## 命令位置別の参照

- [`00bdecd4`](#insn-00bdecd4) → `01127ee8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdecd4`](#insn-00bdecd4)

~~~json
{
  "source": "00bdecd4",
  "target": "01127ee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
