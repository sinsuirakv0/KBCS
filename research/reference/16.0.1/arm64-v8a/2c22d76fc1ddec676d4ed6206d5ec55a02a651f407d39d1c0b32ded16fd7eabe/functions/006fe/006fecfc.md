# 006fecfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0060.md#review-58195f6d40b0e92406584de666b518f7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0021.md#review-58195f6d40b0e92406584de666b518f7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fecfc",
  "name": "FUN_006fecfc",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fa699a0eee758d9cb378a799cc47b7d9257fc02c96ac843e2b025511c2ffcee9",
  "source_text_sha256": "fa699a0eee758d9cb378a799cc47b7d9257fc02c96ac843e2b025511c2ffcee9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006fecfc",
        "006fed07"
      ]
    ],
    "bytes_sha256": "348886b7d8e94495c990d89e8bce7ec025b800129ca12bac6911c5d5664363bb",
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

pointer_____offset_0x10___ * FUN_006fecfc(void)

{
                    /* try { // try from 006fed04 to 007fed5b has its CatchHandler @ 00704984 */
  return &PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c770f8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006fecfc"></a> `006fecfc` | `c0 2b 00 b0` | adrp x0,0xc77000 | `FALL_THROUGH`
<a id="insn-006fed00"></a> `006fed00` | `00 e0 03 91` | add x0,x0,#0xf8 | `FALL_THROUGH`
<a id="insn-006fed04"></a> `006fed04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006fecfc`](#insn-006fecfc) 範囲 `[['006fecfc', '006fed03']]`
  - `FALL_THROUGH` [`006fed00`](#insn-006fed00) → [`006fed04`](#insn-006fed04)
- ブロック [`006fed04`](#insn-006fed04) 範囲 `[['006fed04', '006fed07']]`

## 命令位置別の参照

- [`006fed00`](#insn-006fed00) → `00c770f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006fed00`](#insn-006fed00)

~~~json
{
  "source": "006fed00",
  "target": "00c770f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c770f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
