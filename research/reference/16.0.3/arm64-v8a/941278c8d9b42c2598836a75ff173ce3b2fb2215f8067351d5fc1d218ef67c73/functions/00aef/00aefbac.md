# 00aefbac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0081.md#review-7f6fd4ad81d90d4b3c2b12dfa88ae896)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefbac",
  "name": "FUN_00aefbac",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df67d870061c4cf4161be0385924ad8a5f4026a25993afd328cdf6d4f518ed0d",
  "source_text_sha256": "df67d870061c4cf4161be0385924ad8a5f4026a25993afd328cdf6d4f518ed0d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefbac",
        "00aefbbb"
      ]
    ],
    "bytes_sha256": "7a293c353d3a6a01268d951e9989964ef0a69318ff70e50fb1d72a0ecfda2a05",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
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

## 疑似コード / UTF-8 107 bytes

~~~c

void FUN_00aefbac(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c8ee78;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aefbac"></a> `00aefbac` | `e8 0c 00 f0` | adrp x8,0xc8e000 | `FALL_THROUGH`
<a id="insn-00aefbb0"></a> `00aefbb0` | `08 e1 39 91` | add x8,x8,#0xe78 | `FALL_THROUGH`
<a id="insn-00aefbb4"></a> `00aefbb4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00aefbb8"></a> `00aefbb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aefbac`](#insn-00aefbac) 範囲 `[['00aefbac', '00aefbbb']]`

## 命令位置別の参照

- [`00aefbb4`](#insn-00aefbb4) → `00c8ee78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aefbb4`](#insn-00aefbb4)

~~~json
{
  "source": "00aefbb4",
  "target": "00c8ee78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8ee78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
