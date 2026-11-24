# 00afcefc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afceb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afceb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-5a483935a9d03232310a656bf5962a2c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5cc80`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cc80.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0061.md#compare-acec3a22db9b30249ad0e20faf131b0a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcefc",
  "name": "_ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "24c49c8f458be78cbd8c95ee97fa6ab3d7bbd4b1fcab448236debe4f49d86e1e",
  "source_text_sha256": "24c49c8f458be78cbd8c95ee97fa6ab3d7bbd4b1fcab448236debe4f49d86e1e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcefc",
        "00afcf17"
      ]
    ],
    "bytes_sha256": "b8382aa290949b2362783c0a6986285bf907d5f55d348f34ed25a0b29046a752",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bded30](../00bde/00bded30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 403 bytes

~~~c

void _ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00afcf08 to 00bfcf6b has its CatchHandler @ 00af5650 */
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcefc"></a> `00afcefc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00afcf00"></a> `00afcf00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcf04"></a> `00afcf04` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00afcf08"></a> `00afcf08` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00afcf0c"></a> `00afcf0c` | `89 87 03 94` | bl 0x00bded30 | `UNCONDITIONAL_CALL`
<a id="insn-00afcf10"></a> `00afcf10` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00afcf14"></a> `00afcf14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcefc`](#insn-00afcefc) 範囲 `[['00afcefc', '00afcf07']]`
  - `FALL_THROUGH` [`00afcf04`](#insn-00afcf04) → [`00afcf08`](#insn-00afcf08)
- ブロック [`00afcf08`](#insn-00afcf08) 範囲 `[['00afcf08', '00afcf17']]`

## 命令位置別の参照

- [`00afcefc`](#insn-00afcefc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf0c`](#insn-00afcf0c) → [`00bded30`](../00bde/00bded30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded30` · 推定シンボル `None` · 推定型 `None`
- [`00afcf10`](#insn-00afcf10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcefc`](#insn-00afcefc)

~~~json
{
  "source": "00afcefc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf0c`](#insn-00afcf0c)

~~~json
{
  "source": "00afcf0c",
  "target": "00bded30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcf10`](#insn-00afcf10)

~~~json
{
  "source": "00afcf10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
