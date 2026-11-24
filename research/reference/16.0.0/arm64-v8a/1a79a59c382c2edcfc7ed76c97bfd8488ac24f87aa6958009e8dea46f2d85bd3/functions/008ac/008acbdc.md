# 008acbdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0144.md#review-b655a808ee468f8005cd494a62e90f39)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0033.md#review-b655a808ee468f8005cd494a62e90f39)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008acbdc",
  "name": "FUN_008acbdc",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3321b6ffb0d8eae6ee7af2d03870cd679bc2fe8b7210fc700457c18a22a3312c",
  "source_text_sha256": "3321b6ffb0d8eae6ee7af2d03870cd679bc2fe8b7210fc700457c18a22a3312c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008acbdc",
        "008acbeb"
      ]
    ],
    "bytes_sha256": "2ee3fcb8a7bb6c856e5875705791c271f326f205c988325acd906c92161562f9",
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

void FUN_008acbdc(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c83330;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008acbdc"></a> `008acbdc` | `a8 1e 00 f0` | adrp x8,0xc83000 | `FALL_THROUGH`
<a id="insn-008acbe0"></a> `008acbe0` | `08 c1 0c 91` | add x8,x8,#0x330 | `FALL_THROUGH`
<a id="insn-008acbe4"></a> `008acbe4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-008acbe8"></a> `008acbe8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008acbdc`](#insn-008acbdc) 範囲 `[['008acbdc', '008acbeb']]`

## 命令位置別の参照

- [`008acbe4`](#insn-008acbe4) → `00c83330`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008acbe4`](#insn-008acbe4)

~~~json
{
  "source": "008acbe4",
  "target": "00c83330",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c83330",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
