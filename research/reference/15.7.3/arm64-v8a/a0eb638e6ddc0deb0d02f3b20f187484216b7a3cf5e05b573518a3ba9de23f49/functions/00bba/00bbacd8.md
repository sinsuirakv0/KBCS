# 00bbacd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbac10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac10.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-56ebe19c96f4c16b37e474a75eefaae7)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbad1c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad1c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-38c191c7040e0b2e2f9f9055f3058b25)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbacd8",
  "name": "__cxa_deleted_virtual",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3b3897887f50e4fda770934f06cf0ca9e4ba99690801a0a87724c8e7e826c71",
  "source_text_sha256": "e3b3897887f50e4fda770934f06cf0ca9e4ba99690801a0a87724c8e7e826c71",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbacd8",
        "00bbacef"
      ]
    ],
    "bytes_sha256": "7946daff21bbddb52abf6124fa1c5416e87c60fd68a04f327ec2466c19d681c2",
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

- [00bbb158](../00bbb/00bbb158.md)

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
                    /* catch() { ... } // from try @ 00bb42d4 with catch @ 00bbacdc */
                    /* catch() { ... } // from try @ 00bb3ee8 with catch @ 00bbace0 */
                    /* catch() { ... } // from try @ 00bb3ac8 with catch @ 00bbace4 */
                    /* catch() { ... } // from try @ 00bb41e8 with catch @ 00bbace8 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb41d0 with catch @ 00bbacec */
  FUN_00bbb158("Deleted virtual function called!");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbacd8"></a> `00bbacd8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbacdc"></a> `00bbacdc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbace0"></a> `00bbace0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbace4"></a> `00bbace4` | `40 b7 ff f0` | adrp x0,0x2a5000 | `FALL_THROUGH`
<a id="insn-00bbace8"></a> `00bbace8` | `00 bc 0a 91` | add x0,x0,#0x2af | `FALL_THROUGH`
<a id="insn-00bbacec"></a> `00bbacec` | `1b 01 00 94` | bl 0x00bbb158 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbacd8`](#insn-00bbacd8) 範囲 `[['00bbacd8', '00bbacdb']]`
  - `FALL_THROUGH` [`00bbacd8`](#insn-00bbacd8) → [`00bbacdc`](#insn-00bbacdc)
- ブロック [`00bbacdc`](#insn-00bbacdc) 範囲 `[['00bbacdc', '00bbacdf']]`
  - `FALL_THROUGH` [`00bbacdc`](#insn-00bbacdc) → [`00bbace0`](#insn-00bbace0)
- ブロック [`00bbace0`](#insn-00bbace0) 範囲 `[['00bbace0', '00bbace3']]`
  - `FALL_THROUGH` [`00bbace0`](#insn-00bbace0) → [`00bbace4`](#insn-00bbace4)
- ブロック [`00bbace4`](#insn-00bbace4) 範囲 `[['00bbace4', '00bbace7']]`
  - `FALL_THROUGH` [`00bbace4`](#insn-00bbace4) → [`00bbace8`](#insn-00bbace8)
- ブロック [`00bbace8`](#insn-00bbace8) 範囲 `[['00bbace8', '00bbaceb']]`
  - `FALL_THROUGH` [`00bbace8`](#insn-00bbace8) → [`00bbacec`](#insn-00bbacec)
- ブロック [`00bbacec`](#insn-00bbacec) 範囲 `[['00bbacec', '00bbacef']]`

## 命令位置別の参照

- [`00bbacdc`](#insn-00bbacdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbace8`](#insn-00bbace8) → `002a52af`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbacec`](#insn-00bbacec) → [`00bbb158`](../00bbb/00bbb158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb158` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbacdc`](#insn-00bbacdc)

~~~json
{
  "source": "00bbacdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbace8`](#insn-00bbace8)

~~~json
{
  "source": "00bbace8",
  "target": "002a52af",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a52af",
  "offset": 0,
  "size": 33,
  "datatype": "string",
  "bytes": "44656c65746564207669727475616c2066756e6374696f6e2063616c6c656421",
  "capture_start": "002a52af",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbacec`](#insn-00bbacec)

~~~json
{
  "source": "00bbacec",
  "target": "00bbb158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
