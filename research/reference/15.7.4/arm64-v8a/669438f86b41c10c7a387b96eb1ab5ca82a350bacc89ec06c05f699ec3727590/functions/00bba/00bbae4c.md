# 00bbae4c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbae08`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae08.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-464a9619817586e7004d0f1e9fdec20e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37894`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37894.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-8c857abf98ce13536db757f586ee6cf8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbae4c",
  "name": "_ZNKSt20bad_array_new_length4whatEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c87f6e86e381961e56dd3140164c74c536511616b24e70960dd27f65437bcc9d",
  "source_text_sha256": "c87f6e86e381961e56dd3140164c74c536511616b24e70960dd27f65437bcc9d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbae4c",
        "00bbae5b"
      ]
    ],
    "bytes_sha256": "608a667ea3f9ce899963fde9d31b6f44847198ba5e1d67f6bca88454a7128746",
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
"bad_array_new_length"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 350 bytes

~~~c

char * _ZNKSt20bad_array_new_length4whatEv(void)

{
                    /* catch() { ... } // from try @ 00bb605c with catch @ 00bbae50 */
                    /* catch() { ... } // from try @ 00bb5c9c with catch @ 00bbae54 */
                    /* catch() { ... } // from try @ 00bb58dc with catch @ 00bbae58 */
  return "bad_array_new_length";
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbae4c"></a> `00bbae4c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbae50"></a> `00bbae50` | `c0 b6 ff f0` | adrp x0,0x295000 | `FALL_THROUGH`
<a id="insn-00bbae54"></a> `00bbae54` | `00 18 1c 91` | add x0,x0,#0x706 | `FALL_THROUGH`
<a id="insn-00bbae58"></a> `00bbae58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbae4c`](#insn-00bbae4c) 範囲 `[['00bbae4c', '00bbae4f']]`
  - `FALL_THROUGH` [`00bbae4c`](#insn-00bbae4c) → [`00bbae50`](#insn-00bbae50)
- ブロック [`00bbae50`](#insn-00bbae50) 範囲 `[['00bbae50', '00bbae53']]`
  - `FALL_THROUGH` [`00bbae50`](#insn-00bbae50) → [`00bbae54`](#insn-00bbae54)
- ブロック [`00bbae54`](#insn-00bbae54) 範囲 `[['00bbae54', '00bbae57']]`
  - `FALL_THROUGH` [`00bbae54`](#insn-00bbae54) → [`00bbae58`](#insn-00bbae58)
- ブロック [`00bbae58`](#insn-00bbae58) 範囲 `[['00bbae58', '00bbae5b']]`

## 命令位置別の参照

- [`00bbae54`](#insn-00bbae54) → `00295706`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbae54`](#insn-00bbae54)

~~~json
{
  "source": "00bbae54",
  "target": "00295706",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00295706",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "6261645f61727261795f6e65775f6c656e67746800",
  "capture_start": "00295706",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
