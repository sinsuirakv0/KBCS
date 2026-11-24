# 00bbadf8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbadb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbadb4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-5d341b15bfada6d92d315fa23b77882c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37840`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37840.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-4ed1231e343c9666855a023bf2910c3e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbadf8",
  "name": "_ZNKSt9bad_alloc4whatEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "323a567f05491d6dd88d40b0687775744efbc2a37505ead74f633de0716d8a5c",
  "source_text_sha256": "323a567f05491d6dd88d40b0687775744efbc2a37505ead74f633de0716d8a5c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbadf8",
        "00bbae07"
      ]
    ],
    "bytes_sha256": "5934e83efdb7cf7cdc34ff80c9a7b245dafc5d711f1439cedbe970f4c7a5e9ca",
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

## 関連文字列（未確認候補）

~~~text
"std::bad_alloc"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 332 bytes

~~~c

char * _ZNKSt9bad_alloc4whatEv(void)

{
                    /* catch() { ... } // from try @ 00bb58ec with catch @ 00bbadfc */
                    /* catch() { ... } // from try @ 00bb5904 with catch @ 00bbae00 */
                    /* catch() { ... } // from try @ 00bb5174 with catch @ 00bbae04 */
  return "std::bad_alloc";
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbadf8"></a> `00bbadf8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbadfc"></a> `00bbadfc` | `00 b7 ff 90` | adrp x0,0x29a000 | `FALL_THROUGH`
<a id="insn-00bbae00"></a> `00bbae00` | `00 c8 2a 91` | add x0,x0,#0xab2 | `FALL_THROUGH`
<a id="insn-00bbae04"></a> `00bbae04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbadf8`](#insn-00bbadf8) 範囲 `[['00bbadf8', '00bbadfb']]`
  - `FALL_THROUGH` [`00bbadf8`](#insn-00bbadf8) → [`00bbadfc`](#insn-00bbadfc)
- ブロック [`00bbadfc`](#insn-00bbadfc) 範囲 `[['00bbadfc', '00bbadff']]`
  - `FALL_THROUGH` [`00bbadfc`](#insn-00bbadfc) → [`00bbae00`](#insn-00bbae00)
- ブロック [`00bbae00`](#insn-00bbae00) 範囲 `[['00bbae00', '00bbae03']]`
  - `FALL_THROUGH` [`00bbae00`](#insn-00bbae00) → [`00bbae04`](#insn-00bbae04)
- ブロック [`00bbae04`](#insn-00bbae04) 範囲 `[['00bbae04', '00bbae07']]`

## 命令位置別の参照

- [`00bbae00`](#insn-00bbae00) → `0029aab2`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbae00`](#insn-00bbae00)

~~~json
{
  "source": "00bbae00",
  "target": "0029aab2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029aab2",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "7374643a3a6261645f616c6c6f6300",
  "capture_start": "0029aab2",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
