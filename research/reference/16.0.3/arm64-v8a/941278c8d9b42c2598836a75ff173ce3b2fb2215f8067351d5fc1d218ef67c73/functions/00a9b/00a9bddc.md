# 00a9bddc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0080.md#review-3014ad752f2f9c7e1fb7d17a21cdd891)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9bddc",
  "name": "FUN_00a9bddc",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1cf568b9efdb8d181270a6e48000da66676e44f8a4c7ed4d99f8a57d72f8e588",
  "source_text_sha256": "1cf568b9efdb8d181270a6e48000da66676e44f8a4c7ed4d99f8a57d72f8e588",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9bddc",
        "00a9bde7"
      ]
    ],
    "bytes_sha256": "1523cf8f71928bab3807033e091fea2499b8df3750496f60e3571351eb919af1",
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

## 疑似コード / UTF-8 121 bytes

~~~c

pointer_____offset_0x10___ * FUN_00a9bddc(void)

{
  return &PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c8df68;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9bddc"></a> `00a9bddc` | `80 0f 00 d0` | adrp x0,0xc8d000 | `FALL_THROUGH`
<a id="insn-00a9bde0"></a> `00a9bde0` | `00 a0 3d 91` | add x0,x0,#0xf68 | `FALL_THROUGH`
<a id="insn-00a9bde4"></a> `00a9bde4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9bddc`](#insn-00a9bddc) 範囲 `[['00a9bddc', '00a9bde7']]`

## 命令位置別の参照

- [`00a9bde0`](#insn-00a9bde0) → `00c8df68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9bde0`](#insn-00a9bde0)

~~~json
{
  "source": "00a9bde0",
  "target": "00c8df68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df68",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
