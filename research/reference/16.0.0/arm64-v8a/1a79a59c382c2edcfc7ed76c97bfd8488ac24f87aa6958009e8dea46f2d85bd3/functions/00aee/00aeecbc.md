# 00aeecbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0163.md#review-d7f857dba5e8b53bc5fb82fcde07c2bb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0043.md#review-d7f857dba5e8b53bc5fb82fcde07c2bb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeecbc",
  "name": "FUN_00aeecbc",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e6d7781e327b2000d947313aa12c06e18cb44dcebd43104bcaf2da791b83ecf",
  "source_text_sha256": "8e6d7781e327b2000d947313aa12c06e18cb44dcebd43104bcaf2da791b83ecf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeecbc",
        "00aeecc7"
      ]
    ],
    "bytes_sha256": "8dbc2b0ec1bd26aebcd22a1c616b81195fe6a3dada176818a9f541ec401ae058",
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

pointer_____offset_0x10___ * FUN_00aeecbc(void)

{
  return &PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c8dbc8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeecbc"></a> `00aeecbc` | `e0 0c 00 f0` | adrp x0,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeecc0"></a> `00aeecc0` | `00 20 2f 91` | add x0,x0,#0xbc8 | `FALL_THROUGH`
<a id="insn-00aeecc4"></a> `00aeecc4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeecbc`](#insn-00aeecbc) 範囲 `[['00aeecbc', '00aeecc7']]`

## 命令位置別の参照

- [`00aeecc0`](#insn-00aeecc0) → `00c8dbc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeecc0`](#insn-00aeecc0)

~~~json
{
  "source": "00aeecc0",
  "target": "00c8dbc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8dbc8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
