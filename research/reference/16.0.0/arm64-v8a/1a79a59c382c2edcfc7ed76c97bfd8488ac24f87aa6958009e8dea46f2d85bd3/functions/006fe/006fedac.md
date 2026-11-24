# 006fedac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0122.md#review-0b398aa8212d31b1c15626e7bfcd49b8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0020.md#review-0b398aa8212d31b1c15626e7bfcd49b8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fedac",
  "name": "FUN_006fedac",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb35fd7cd78cba45e8b6cbdf9012fac1ea125f96f2a0925f47ee8596372ad1f4",
  "source_text_sha256": "bb35fd7cd78cba45e8b6cbdf9012fac1ea125f96f2a0925f47ee8596372ad1f4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006fedac",
        "006fedbb"
      ]
    ],
    "bytes_sha256": "0f52846438c7d6ab872ade2f50fdb9c4322d1aea269c95002e3a4074470d65e7",
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

void FUN_006fedac(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c76d18;
                    /* try { // try from 006fedb8 to 007fedbf has its CatchHandler @ 007048c0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006fedac"></a> `006fedac` | `c8 2b 00 90` | adrp x8,0xc76000 | `FALL_THROUGH`
<a id="insn-006fedb0"></a> `006fedb0` | `08 61 34 91` | add x8,x8,#0xd18 | `FALL_THROUGH`
<a id="insn-006fedb4"></a> `006fedb4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-006fedb8"></a> `006fedb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006fedac`](#insn-006fedac) 範囲 `[['006fedac', '006fedb7']]`
  - `FALL_THROUGH` [`006fedb4`](#insn-006fedb4) → [`006fedb8`](#insn-006fedb8)
- ブロック [`006fedb8`](#insn-006fedb8) 範囲 `[['006fedb8', '006fedbb']]`

## 命令位置別の参照

- [`006fedb4`](#insn-006fedb4) → `00c76d18`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006fedb4`](#insn-006fedb4)

~~~json
{
  "source": "006fedb4",
  "target": "00c76d18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c76d18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
