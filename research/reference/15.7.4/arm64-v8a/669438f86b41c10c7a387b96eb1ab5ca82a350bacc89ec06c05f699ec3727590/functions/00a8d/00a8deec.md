# 00a8deec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 要確認
  - [v15.7.3 → v15.7.4 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/review-0037.md#review-912cff9b1d6ed1823181bd263cf25449)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0080.md#review-912cff9b1d6ed1823181bd263cf25449)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a8deec",
  "name": "FUN_00a8deec",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a7a5b23ec5e4fe9fb63e5486f7f458c64d6a54089c70a1dfdaafa74209e5d277",
  "source_text_sha256": "a7a5b23ec5e4fe9fb63e5486f7f458c64d6a54089c70a1dfdaafa74209e5d277",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a8deec",
        "00a8def7"
      ]
    ],
    "bytes_sha256": "532230fab3a335ab43dbb0425c9532a74818502d8f7324ed454216dbb034dd95",
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

## 疑似コード / UTF-8 218 bytes

~~~c

pointer_____offset_0x10___ * FUN_00a8deec(void)

{
                    /* try { // try from 00a8def4 to 00b8defb has its CatchHandler @ 00a8fafc */
  return &PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c0e138;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a8deec"></a> `00a8deec` | `00 0c 00 b0` | adrp x0,0xc0e000 | `FALL_THROUGH`
<a id="insn-00a8def0"></a> `00a8def0` | `00 e0 04 91` | add x0,x0,#0x138 | `FALL_THROUGH`
<a id="insn-00a8def4"></a> `00a8def4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a8deec`](#insn-00a8deec) 範囲 `[['00a8deec', '00a8def3']]`
  - `FALL_THROUGH` [`00a8def0`](#insn-00a8def0) → [`00a8def4`](#insn-00a8def4)
- ブロック [`00a8def4`](#insn-00a8def4) 範囲 `[['00a8def4', '00a8def7']]`

## 命令位置別の参照

- [`00a8def0`](#insn-00a8def0) → `00c0e138`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a8def0`](#insn-00a8def0)

~~~json
{
  "source": "00a8def0",
  "target": "00c0e138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0e138",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
