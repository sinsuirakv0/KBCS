# 006fedec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0060.md#review-0aebd8082be51e3b2dde07d58e7cba65)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0021.md#review-0aebd8082be51e3b2dde07d58e7cba65)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fedec",
  "name": "FUN_006fedec",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f8a847fc7bb5a80d23b9f78a61765e8d8af95e14c7cf5f584a174ecf402af3d4",
  "source_text_sha256": "f8a847fc7bb5a80d23b9f78a61765e8d8af95e14c7cf5f584a174ecf402af3d4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006fedec",
        "006fedfb"
      ]
    ],
    "bytes_sha256": "66a943f6e09166f536e4d2193e1d8a5a83ab4ce58fa884e81adbe6d318962d41",
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

## 疑似コード / UTF-8 204 bytes

~~~c

void FUN_006fedec(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c77118;
                    /* try { // try from 006fedf8 to 007fedff has its CatchHandler @ 00704900 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006fedec"></a> `006fedec` | `c8 2b 00 b0` | adrp x8,0xc77000 | `FALL_THROUGH`
<a id="insn-006fedf0"></a> `006fedf0` | `08 61 04 91` | add x8,x8,#0x118 | `FALL_THROUGH`
<a id="insn-006fedf4"></a> `006fedf4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-006fedf8"></a> `006fedf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006fedec`](#insn-006fedec) 範囲 `[['006fedec', '006fedf7']]`
  - `FALL_THROUGH` [`006fedf4`](#insn-006fedf4) → [`006fedf8`](#insn-006fedf8)
- ブロック [`006fedf8`](#insn-006fedf8) 範囲 `[['006fedf8', '006fedfb']]`

## 命令位置別の参照

- [`006fedf4`](#insn-006fedf4) → `00c77118`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006fedf4`](#insn-006fedf4)

~~~json
{
  "source": "006fedf4",
  "target": "00c77118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c77118",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
