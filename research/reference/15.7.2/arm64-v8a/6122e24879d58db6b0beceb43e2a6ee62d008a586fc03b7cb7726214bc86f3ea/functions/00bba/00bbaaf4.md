# 00bbaaf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbabbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabbc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-82f26159aaf0038f9ada00043b253df8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaaf4",
  "name": "FUN_00bbaaf4",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1a159dcdd11055ae0967db7cbc007dc55007530ea348a3bafab8ca96881ebc2d",
  "source_text_sha256": "1a159dcdd11055ae0967db7cbc007dc55007530ea348a3bafab8ca96881ebc2d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaaf4",
        "00bbab13"
      ]
    ],
    "bytes_sha256": "123654ec4efbfde99f4fdebc0fe3f3c2a55b87256eee9baef6e37decb30a72ce",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb0d0](../00bdb/00bdb0d0.md)

## 関連文字列（未確認候補）

~~~text
"unexpected"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 426 bytes

~~~c

void FUN_00bbaaf4(void)

{
                    /* catch() { ... } // from try @ 00bb7aec with catch @ 00bbaaf8 */
                    /* catch() { ... } // from try @ 00bb369c with catch @ 00bbaafc */
                    /* catch() { ... } // from try @ 00bb36a8 with catch @ 00bbab0c */
  PTR_s_uncaught_00c248a0 = s_unexpected_002a1122;
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaaf4"></a> `00bbaaf4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaaf8"></a> `00bbaaf8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbaafc"></a> `00bbaafc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbab00"></a> `00bbab00` | `48 03 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00bbab04"></a> `00bbab04` | `29 b7 ff f0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00bbab08"></a> `00bbab08` | `29 89 04 91` | add x9,x9,#0x122 | `FALL_THROUGH`
<a id="insn-00bbab0c"></a> `00bbab0c` | `09 51 04 f9` | str x9,[x8, #0x8a0] | `FALL_THROUGH`
<a id="insn-00bbab10"></a> `00bbab10` | `70 81 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaaf4`](#insn-00bbaaf4) 範囲 `[['00bbaaf4', '00bbaaf7']]`
  - `FALL_THROUGH` [`00bbaaf4`](#insn-00bbaaf4) → [`00bbaaf8`](#insn-00bbaaf8)
- ブロック [`00bbaaf8`](#insn-00bbaaf8) 範囲 `[['00bbaaf8', '00bbaafb']]`
  - `FALL_THROUGH` [`00bbaaf8`](#insn-00bbaaf8) → [`00bbaafc`](#insn-00bbaafc)
- ブロック [`00bbaafc`](#insn-00bbaafc) 範囲 `[['00bbaafc', '00bbab0b']]`
  - `FALL_THROUGH` [`00bbab08`](#insn-00bbab08) → [`00bbab0c`](#insn-00bbab0c)
- ブロック [`00bbab0c`](#insn-00bbab0c) 範囲 `[['00bbab0c', '00bbab13']]`

## 命令位置別の参照

- [`00bbaaf8`](#insn-00bbaaf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab0c`](#insn-00bbab0c) → `00c248a0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbab0c`](#insn-00bbab0c) → `002a1122`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbab10`](#insn-00bbab10) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaaf8`](#insn-00bbaaf8)

~~~json
{
  "source": "00bbaaf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab0c`](#insn-00bbab0c)

~~~json
{
  "source": "00bbab0c",
  "target": "00c248a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c248a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbab0c`](#insn-00bbab0c)

~~~json
{
  "source": "00bbab0c",
  "target": "002a1122",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1122",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "756e657870656374656400",
  "capture_start": "002a1122",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbab10`](#insn-00bbab10)

~~~json
{
  "source": "00bbab10",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
