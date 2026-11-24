# 00bbad1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbacd8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacd8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-38c191c7040e0b2e2f9f9055f3058b25)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37764`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37764.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-b864e21ec7c73f14f95e4bd0c1fdb507)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbad1c",
  "name": "__cxa_deleted_virtual",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "03a8ad0217ce692ad18acc6d177bb77bf95dbb6dbd995d3d3a721ebc429a2fe6",
  "source_text_sha256": "03a8ad0217ce692ad18acc6d177bb77bf95dbb6dbd995d3d3a721ebc429a2fe6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbad1c",
        "00bbad33"
      ]
    ],
    "bytes_sha256": "090639e0c28aa836f20268c81b13c23edb0a038da45f645d1d7645f779512d84",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb19c](../00bbb/00bbb19c.md)

## 関連文字列（未確認候補）

~~~text
"Deleted virtual function called!"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 589 bytes

~~~c

void __cxa_deleted_virtual(void)

{
                    /* catch() { ... } // from try @ 00bb4318 with catch @ 00bbad20 */
                    /* catch() { ... } // from try @ 00bb3f2c with catch @ 00bbad24 */
                    /* catch() { ... } // from try @ 00bb3b0c with catch @ 00bbad28 */
                    /* catch() { ... } // from try @ 00bb422c with catch @ 00bbad2c */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb4214 with catch @ 00bbad30 */
  FUN_00bbb19c("Deleted virtual function called!");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbad1c"></a> `00bbad1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbad20"></a> `00bbad20` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbad24"></a> `00bbad24` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbad28"></a> `00bbad28` | `40 b7 ff f0` | adrp x0,0x2a5000 | `FALL_THROUGH`
<a id="insn-00bbad2c"></a> `00bbad2c` | `00 e8 0c 91` | add x0,x0,#0x33a | `FALL_THROUGH`
<a id="insn-00bbad30"></a> `00bbad30` | `1b 01 00 94` | bl 0x00bbb19c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbad1c`](#insn-00bbad1c) 範囲 `[['00bbad1c', '00bbad1f']]`
  - `FALL_THROUGH` [`00bbad1c`](#insn-00bbad1c) → [`00bbad20`](#insn-00bbad20)
- ブロック [`00bbad20`](#insn-00bbad20) 範囲 `[['00bbad20', '00bbad23']]`
  - `FALL_THROUGH` [`00bbad20`](#insn-00bbad20) → [`00bbad24`](#insn-00bbad24)
- ブロック [`00bbad24`](#insn-00bbad24) 範囲 `[['00bbad24', '00bbad27']]`
  - `FALL_THROUGH` [`00bbad24`](#insn-00bbad24) → [`00bbad28`](#insn-00bbad28)
- ブロック [`00bbad28`](#insn-00bbad28) 範囲 `[['00bbad28', '00bbad2b']]`
  - `FALL_THROUGH` [`00bbad28`](#insn-00bbad28) → [`00bbad2c`](#insn-00bbad2c)
- ブロック [`00bbad2c`](#insn-00bbad2c) 範囲 `[['00bbad2c', '00bbad2f']]`
  - `FALL_THROUGH` [`00bbad2c`](#insn-00bbad2c) → [`00bbad30`](#insn-00bbad30)
- ブロック [`00bbad30`](#insn-00bbad30) 範囲 `[['00bbad30', '00bbad33']]`

## 命令位置別の参照

- [`00bbad20`](#insn-00bbad20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad2c`](#insn-00bbad2c) → `002a533a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbad30`](#insn-00bbad30) → [`00bbb19c`](../00bbb/00bbb19c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb19c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbad20`](#insn-00bbad20)

~~~json
{
  "source": "00bbad20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad2c`](#insn-00bbad2c)

~~~json
{
  "source": "00bbad2c",
  "target": "002a533a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a533a",
  "offset": 0,
  "size": 33,
  "datatype": "string",
  "bytes": "44656c65746564207669727475616c2066756e6374696f6e2063616c6c656421",
  "capture_start": "002a533a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbad30`](#insn-00bbad30)

~~~json
{
  "source": "00bbad30",
  "target": "00bbb19c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
