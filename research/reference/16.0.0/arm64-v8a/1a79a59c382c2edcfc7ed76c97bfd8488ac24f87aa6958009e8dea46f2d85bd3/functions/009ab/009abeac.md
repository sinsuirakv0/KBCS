# 009abeac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `009763c8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/009763c8.md) · 移動量 `+0x35ae4`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0011.md#compare-714894f29ea4034721e6e2f43158aa13)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `009ac048`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac048.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0003.md#compare-7ca43dac62a26448dd69ec3eabdc4969)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009abeac",
  "name": "FUN_009abeac",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1102df87fce6b4c4c1f787cae99f84d9ac237d6646562d9fd3d136775c3131a8",
  "source_text_sha256": "1102df87fce6b4c4c1f787cae99f84d9ac237d6646562d9fd3d136775c3131a8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009abeac",
        "009abebf"
      ]
    ],
    "bytes_sha256": "6aeb6cab193042a97cc277789067ecbc143506944172b71c6ec18d97cc71b047",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009abb24](../009ab/009abb24.md)
- [009ac11c](../009ac/009ac11c.md)

## 呼び出し先

- [0043b738](../0043b/0043b738.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 216 bytes

~~~c

void FUN_009abeac(void)

{
                    /* try { // try from 009abeb0 to 00aabecb has its CatchHandler @ 009abcb4 */
                    /* WARNING: Subroutine does not return */
  FUN_0043b738("vector");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009abeac"></a> `009abeac` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-009abeb0"></a> `009abeb0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009abeb4"></a> `009abeb4` | `60 c8 ff 90` | adrp x0,0x2b7000 | `FALL_THROUGH`
<a id="insn-009abeb8"></a> `009abeb8` | `00 30 3c 91` | add x0,x0,#0xf0c | `FALL_THROUGH`
<a id="insn-009abebc"></a> `009abebc` | `1f 3e ea 97` | bl 0x0043b738 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009abeac`](#insn-009abeac) 範囲 `[['009abeac', '009abeaf']]`
  - `FALL_THROUGH` [`009abeac`](#insn-009abeac) → [`009abeb0`](#insn-009abeb0)
- ブロック [`009abeb0`](#insn-009abeb0) 範囲 `[['009abeb0', '009abebf']]`

## 命令位置別の参照

- [`009abeac`](#insn-009abeac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009abeb8`](#insn-009abeb8) → `002b7f0c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009abebc`](#insn-009abebc) → [`0043b738`](../0043b/0043b738.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b738` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009abeac`](#insn-009abeac)

~~~json
{
  "source": "009abeac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009abeb8`](#insn-009abeb8)

~~~json
{
  "source": "009abeb8",
  "target": "002b7f0c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7f0c",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "766563746f7200",
  "capture_start": "002b7f0c",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009abebc`](#insn-009abebc)

~~~json
{
  "source": "009abebc",
  "target": "0043b738",
  "target_space": "ram",
  "resolution": "function"
}
~~~
