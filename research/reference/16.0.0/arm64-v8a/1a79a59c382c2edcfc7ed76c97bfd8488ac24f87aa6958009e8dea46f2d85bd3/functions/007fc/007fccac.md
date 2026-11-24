# 007fccac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0134.md#review-7dbf4fded726302bd8618b0e41dfa89f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0027.md#review-7dbf4fded726302bd8618b0e41dfa89f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fccac",
  "name": "FUN_007fccac",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d1eb85acb81dd649225f59b2fee17fd68df2b3bb3efeba230f00eed4fb1292fb",
  "source_text_sha256": "d1eb85acb81dd649225f59b2fee17fd68df2b3bb3efeba230f00eed4fb1292fb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fccac",
        "007fccb7"
      ]
    ],
    "bytes_sha256": "c0d1665d99f5bbcc0e945bc8b9434c49dc9726e2a3e022963d5110252d6853d7",
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

pointer_____offset_0x10___ * FUN_007fccac(void)

{
  return &PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c7d310;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fccac"></a> `007fccac` | `00 24 00 b0` | adrp x0,0xc7d000 | `FALL_THROUGH`
<a id="insn-007fccb0"></a> `007fccb0` | `00 40 0c 91` | add x0,x0,#0x310 | `FALL_THROUGH`
<a id="insn-007fccb4"></a> `007fccb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fccac`](#insn-007fccac) 範囲 `[['007fccac', '007fccb7']]`

## 命令位置別の参照

- [`007fccb0`](#insn-007fccb0) → `00c7d310`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fccb0`](#insn-007fccb0)

~~~json
{
  "source": "007fccb0",
  "target": "00c7d310",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7d310",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
