# 00aadbdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 要確認
  - [v15.7.3 → v15.7.4 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/review-0037.md#review-68c2fd2cadea9dbe8951b46037a67e69)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0089.md#review-68c2fd2cadea9dbe8951b46037a67e69)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadbdc",
  "name": "FUN_00aadbdc",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41e98b6b7a65c57bb62c42f16ce08450109511268df1f0af31267513651cd2de",
  "source_text_sha256": "41e98b6b7a65c57bb62c42f16ce08450109511268df1f0af31267513651cd2de",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadbdc",
        "00aadbe7"
      ]
    ],
    "bytes_sha256": "df0d1b03863ace29e4c0de181cb6176b6ac9b8b74e36efa4a42d4e0e3edf9d43",
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

pointer_____offset_0x10___ * FUN_00aadbdc(void)

{
  return &PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c0f638;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aadbdc"></a> `00aadbdc` | `00 0b 00 d0` | adrp x0,0xc0f000 | `FALL_THROUGH`
<a id="insn-00aadbe0"></a> `00aadbe0` | `00 e0 18 91` | add x0,x0,#0x638 | `FALL_THROUGH`
<a id="insn-00aadbe4"></a> `00aadbe4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadbdc`](#insn-00aadbdc) 範囲 `[['00aadbdc', '00aadbe7']]`

## 命令位置別の参照

- [`00aadbe0`](#insn-00aadbe0) → `00c0f638`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadbe0`](#insn-00aadbe0)

~~~json
{
  "source": "00aadbe0",
  "target": "00c0f638",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f638",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
