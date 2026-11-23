# 00bbabbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbaaf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbaaf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-82f26159aaf0038f9ada00043b253df8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbac00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-e08bbd64bd56e2e3817e6ce525693676)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbabbc",
  "name": "FUN_00bbabbc",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b8622db1d8e450b225c0c01ccff765112b1570972b07fbae74fe7d1f56cca8a",
  "source_text_sha256": "8b8622db1d8e450b225c0c01ccff765112b1570972b07fbae74fe7d1f56cca8a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbabbc",
        "00bbabdb"
      ]
    ],
    "bytes_sha256": "774232b6b84edd241c56ad0308bd5884ec113dd85599b8c0b7f7c7e24cf593a1",
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

- [00bdb180](../00bdb/00bdb180.md)

## 関連文字列（未確認候補）

~~~text
"unexpected"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 426 bytes

~~~c

void FUN_00bbabbc(void)

{
                    /* catch() { ... } // from try @ 00bb7bb4 with catch @ 00bbabc0 */
                    /* catch() { ... } // from try @ 00bb3764 with catch @ 00bbabc4 */
                    /* catch() { ... } // from try @ 00bb3770 with catch @ 00bbabd4 */
  PTR_s_uncaught_00c24950 = s_unexpected_002a11af;
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbabbc"></a> `00bbabbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbabc0"></a> `00bbabc0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbabc4"></a> `00bbabc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbabc8"></a> `00bbabc8` | `48 03 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00bbabcc"></a> `00bbabcc` | `29 b7 ff f0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00bbabd0"></a> `00bbabd0` | `29 bd 06 91` | add x9,x9,#0x1af | `FALL_THROUGH`
<a id="insn-00bbabd4"></a> `00bbabd4` | `09 a9 04 f9` | str x9,[x8, #0x950] | `FALL_THROUGH`
<a id="insn-00bbabd8"></a> `00bbabd8` | `6a 81 00 94` | bl 0x00bdb180 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbabbc`](#insn-00bbabbc) 範囲 `[['00bbabbc', '00bbabbf']]`
  - `FALL_THROUGH` [`00bbabbc`](#insn-00bbabbc) → [`00bbabc0`](#insn-00bbabc0)
- ブロック [`00bbabc0`](#insn-00bbabc0) 範囲 `[['00bbabc0', '00bbabc3']]`
  - `FALL_THROUGH` [`00bbabc0`](#insn-00bbabc0) → [`00bbabc4`](#insn-00bbabc4)
- ブロック [`00bbabc4`](#insn-00bbabc4) 範囲 `[['00bbabc4', '00bbabd3']]`
  - `FALL_THROUGH` [`00bbabd0`](#insn-00bbabd0) → [`00bbabd4`](#insn-00bbabd4)
- ブロック [`00bbabd4`](#insn-00bbabd4) 範囲 `[['00bbabd4', '00bbabdb']]`

## 命令位置別の参照

- [`00bbabc0`](#insn-00bbabc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabd4`](#insn-00bbabd4) → `00c24950`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbabd4`](#insn-00bbabd4) → `002a11af`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbabd8`](#insn-00bbabd8) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbabc0`](#insn-00bbabc0)

~~~json
{
  "source": "00bbabc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabd4`](#insn-00bbabd4)

~~~json
{
  "source": "00bbabd4",
  "target": "00c24950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24950",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbabd4`](#insn-00bbabd4)

~~~json
{
  "source": "00bbabd4",
  "target": "002a11af",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a11af",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "756e657870656374656400",
  "capture_start": "002a11af",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbabd8`](#insn-00bbabd8)

~~~json
{
  "source": "00bbabd8",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
