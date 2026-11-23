# 00bbaa2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bba964`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-3e33183f14e253a74a4465eeb69e7434)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbaa70`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-38b251ab7d4beb1477769a4e6776acbb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaa2c",
  "name": "FUN_00bbaa2c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3c4a59b84a0dec90c688fdb2338a13d3aed80cdc07faf334dbb6d99edda8781b",
  "source_text_sha256": "3c4a59b84a0dec90c688fdb2338a13d3aed80cdc07faf334dbb6d99edda8781b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaa2c",
        "00bbaa47"
      ]
    ],
    "bytes_sha256": "a1b7bb1207e3894dc6a82616c74194b93451ef2404b860b54c7d144632c8b7de",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bba9a0](../00bba/00bba9a0.md)
- [00bd5144](../00bd5/00bd5144.md)
- [00bd524c](../00bd5/00bd524c.md)
- [00bd5414](../00bd5/00bd5414.md)
- [00bd56c4](../00bd5/00bd56c4.md)
- [00bd5a94](../00bd5/00bd5a94.md)
- [00bd6030](../00bd6/00bd6030.md)
- [00bd63f4](../00bd6/00bd63f4.md)

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)

## 関連文字列（未確認候補）

~~~text
"terminate_handler unexpectedly returned"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 264 bytes

~~~c

void FUN_00bbaa2c(code *param_1)

{
                    /* catch() { ... } // from try @ 00bb3920 with catch @ 00bbaa30 */
  (*param_1)();
                    /* WARNING: Subroutine does not return */
  FUN_00bbb158("terminate_handler unexpectedly returned");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaa2c"></a> `00bbaa2c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaa30"></a> `00bbaa30` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbaa34"></a> `00bbaa34` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbaa38"></a> `00bbaa38` | `00 00 3f d6` | blr x0 | `COMPUTED_CALL`
<a id="insn-00bbaa3c"></a> `00bbaa3c` | `e0 b6 ff d0` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00bbaa40"></a> `00bbaa40` | `00 44 2d 91` | add x0,x0,#0xb51 | `FALL_THROUGH`
<a id="insn-00bbaa44"></a> `00bbaa44` | `c5 01 00 94` | bl 0x00bbb158 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaa2c`](#insn-00bbaa2c) 範囲 `[['00bbaa2c', '00bbaa2f']]`
  - `FALL_THROUGH` [`00bbaa2c`](#insn-00bbaa2c) → [`00bbaa30`](#insn-00bbaa30)
- ブロック [`00bbaa30`](#insn-00bbaa30) 範囲 `[['00bbaa30', '00bbaa47']]`

## 命令位置別の参照

- [`00bbaa30`](#insn-00bbaa30) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaa40`](#insn-00bbaa40) → `00298b51`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbaa44`](#insn-00bbaa44) → [`00bbb158`](../00bbb/00bbb158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb158` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaa30`](#insn-00bbaa30)

~~~json
{
  "source": "00bbaa30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaa40`](#insn-00bbaa40)

~~~json
{
  "source": "00bbaa40",
  "target": "00298b51",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298b51",
  "offset": 0,
  "size": 40,
  "datatype": "string",
  "bytes": "7465726d696e6174655f68616e646c657220756e65787065637465646c792072",
  "capture_start": "00298b51",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbaa44`](#insn-00bbaa44)

~~~json
{
  "source": "00bbaa44",
  "target": "00bbb158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
