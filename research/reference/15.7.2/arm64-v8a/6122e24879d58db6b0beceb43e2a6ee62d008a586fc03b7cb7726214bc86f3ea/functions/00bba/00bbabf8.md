# 00bbabf8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbacc0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacc0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-43d7b3734e869e28f7ca5276a0fcca03)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbabf8",
  "name": "__cxa_pure_virtual",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a5bcc2284be8b639bd1ef9812477c15987034708e0e46a1d5790ba5fea38c9b",
  "source_text_sha256": "3a5bcc2284be8b639bd1ef9812477c15987034708e0e46a1d5790ba5fea38c9b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbabf8",
        "00bbac0f"
      ]
    ],
    "bytes_sha256": "dd3445587bfc18c6f64a787609c96fd46cd1a5b2543d7b6b11c04aea3954763b",
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

- [00bbb090](../00bbb/00bbb090.md)

## 関連文字列（未確認候補）

~~~text
"Pure virtual function called!"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 751 bytes

~~~c

void __cxa_pure_virtual(void)

{
                    /* catch() { ... } // from try @ 00bb4e28 with catch @ 00bbabfc */
                    /* catch() { ... } // from try @ 00bb4a48 with catch @ 00bbac00 */
                    /* catch() { ... } // from try @ 00bb4688 with catch @ 00bbac04 */
                    /* catch() { ... } // from try @ 00bba368 with catch @ 00bbac08
                       catch() { ... } // from try @ 00bba3b0 with catch @ 00bbac08 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bba350 with catch @ 00bbac0c
                       catch() { ... } // from try @ 00bba398 with catch @ 00bbac0c */
  FUN_00bbb090("Pure virtual function called!");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbabf8"></a> `00bbabf8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbabfc"></a> `00bbabfc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbac00"></a> `00bbac00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbac04"></a> `00bbac04` | `a0 b6 ff d0` | adrp x0,0x290000 | `FALL_THROUGH`
<a id="insn-00bbac08"></a> `00bbac08` | `00 f8 20 91` | add x0,x0,#0x83e | `FALL_THROUGH`
<a id="insn-00bbac0c"></a> `00bbac0c` | `21 01 00 94` | bl 0x00bbb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbabf8`](#insn-00bbabf8) 範囲 `[['00bbabf8', '00bbabfb']]`
  - `FALL_THROUGH` [`00bbabf8`](#insn-00bbabf8) → [`00bbabfc`](#insn-00bbabfc)
- ブロック [`00bbabfc`](#insn-00bbabfc) 範囲 `[['00bbabfc', '00bbabff']]`
  - `FALL_THROUGH` [`00bbabfc`](#insn-00bbabfc) → [`00bbac00`](#insn-00bbac00)
- ブロック [`00bbac00`](#insn-00bbac00) 範囲 `[['00bbac00', '00bbac03']]`
  - `FALL_THROUGH` [`00bbac00`](#insn-00bbac00) → [`00bbac04`](#insn-00bbac04)
- ブロック [`00bbac04`](#insn-00bbac04) 範囲 `[['00bbac04', '00bbac07']]`
  - `FALL_THROUGH` [`00bbac04`](#insn-00bbac04) → [`00bbac08`](#insn-00bbac08)
- ブロック [`00bbac08`](#insn-00bbac08) 範囲 `[['00bbac08', '00bbac0b']]`
  - `FALL_THROUGH` [`00bbac08`](#insn-00bbac08) → [`00bbac0c`](#insn-00bbac0c)
- ブロック [`00bbac0c`](#insn-00bbac0c) 範囲 `[['00bbac0c', '00bbac0f']]`

## 命令位置別の参照

- [`00bbabfc`](#insn-00bbabfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac08`](#insn-00bbac08) → `0029083e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbac0c`](#insn-00bbac0c) → [`00bbb090`](../00bbb/00bbb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbabfc`](#insn-00bbabfc)

~~~json
{
  "source": "00bbabfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac08`](#insn-00bbac08)

~~~json
{
  "source": "00bbac08",
  "target": "0029083e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029083e",
  "offset": 0,
  "size": 30,
  "datatype": "string",
  "bytes": "50757265207669727475616c2066756e6374696f6e2063616c6c65642100",
  "capture_start": "0029083e",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbac0c`](#insn-00bbac0c)

~~~json
{
  "source": "00bbac0c",
  "target": "00bbb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
