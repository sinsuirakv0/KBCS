# 00b4addc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b4ad14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0004.md#compare-d404ab9d22d6cfd6aeb42898f5a41340)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4ae20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0068.md#compare-5f8f9ad8efa625690b7cda9fcda42bc9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4addc",
  "name": "_ZN8firebase9messaging18firebase_messaging10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "617e11ee129ef3cbe019445429ef8eab1a2b38cfa52df31df2faf5ed64f98a89",
  "source_text_sha256": "617e11ee129ef3cbe019445429ef8eab1a2b38cfa52df31df2faf5ed64f98a89",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4addc",
        "00b4ae17"
      ]
    ],
    "bytes_sha256": "b377dd3b298285c11a51db05cfba3f8fa954b4293d57f762aa8143da8dc3f742",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 538 bytes

~~~c

undefined8 _ZN8firebase9messaging18firebase_messaging10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
                    /* try { // try from 00b4adf8 to 00c4ae03 has its CatchHandler @ 00b4ae98 */
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
                    /* try { // try from 00b4ae04 to 00c4ae0f has its CatchHandler @ 00b4ae94 */
                    /* try { // try from 00b4ae10 to 00c4ae3f has its CatchHandler @ 00b4aed8 */
  return *(undefined8 *)(&DAT_010a1010 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4addc"></a> `00b4addc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4ade0"></a> `00b4ade0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ade4"></a> `00b4ade4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4ade8"></a> `00b4ade8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00b4adec"></a> `00b4adec` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b4adf0"></a> `00b4adf0` | `8b 00 00 54` | b.lt 0x00b4ae00 | `CONDITIONAL_JUMP`
<a id="insn-00b4adf4"></a> `00b4adf4` | `60 ba ff f0` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00b4adf8"></a> `00b4adf8` | `00 fc 19 91` | add x0,x0,#0x67f | `FALL_THROUGH`
<a id="insn-00b4adfc"></a> `00b4adfc` | `cd 4c 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ae00"></a> `00b4ae00` | `a8 2a 00 f0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4ae04"></a> `00b4ae04` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b4ae08"></a> `00b4ae08` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00b4ae0c"></a> `00b4ae0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ae10"></a> `00b4ae10` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4ae14"></a> `00b4ae14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4addc`](#insn-00b4addc) 範囲 `[['00b4addc', '00b4adf3']]`
  - `CONDITIONAL_JUMP` [`00b4adf0`](#insn-00b4adf0) → [`00b4ae00`](#insn-00b4ae00)
  - `FALL_THROUGH` [`00b4adf0`](#insn-00b4adf0) → [`00b4adf4`](#insn-00b4adf4)
- ブロック [`00b4adf4`](#insn-00b4adf4) 範囲 `[['00b4adf4', '00b4adf7']]`
  - `FALL_THROUGH` [`00b4adf4`](#insn-00b4adf4) → [`00b4adf8`](#insn-00b4adf8)
- ブロック [`00b4adf8`](#insn-00b4adf8) 範囲 `[['00b4adf8', '00b4adff']]`
  - `FALL_THROUGH` [`00b4adfc`](#insn-00b4adfc) → [`00b4ae00`](#insn-00b4ae00)
- ブロック [`00b4ae00`](#insn-00b4ae00) 範囲 `[['00b4ae00', '00b4ae03']]`
  - `FALL_THROUGH` [`00b4ae00`](#insn-00b4ae00) → [`00b4ae04`](#insn-00b4ae04)
- ブロック [`00b4ae04`](#insn-00b4ae04) 範囲 `[['00b4ae04', '00b4ae0f']]`
  - `FALL_THROUGH` [`00b4ae0c`](#insn-00b4ae0c) → [`00b4ae10`](#insn-00b4ae10)
- ブロック [`00b4ae10`](#insn-00b4ae10) 範囲 `[['00b4ae10', '00b4ae17']]`

## 命令位置別の参照

- [`00b4addc`](#insn-00b4addc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ade0`](#insn-00b4ade0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4adf0`](#insn-00b4adf0) → [`00b4ae00`](#insn-00b4ae00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4adf8`](#insn-00b4adf8) → `0029967f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4adfc`](#insn-00b4adfc) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4ae08`](#insn-00b4ae08) → `010a1010`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ae0c`](#insn-00b4ae0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4addc`](#insn-00b4addc)

~~~json
{
  "source": "00b4addc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ade0`](#insn-00b4ade0)

~~~json
{
  "source": "00b4ade0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4adf0`](#insn-00b4adf0)

~~~json
{
  "source": "00b4adf0",
  "target": "00b4ae00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4adf8`](#insn-00b4adf8)

~~~json
{
  "source": "00b4adf8",
  "target": "0029967f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029967f",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "0029967f",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4adfc`](#insn-00b4adfc)

~~~json
{
  "source": "00b4adfc",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ae08`](#insn-00b4ae08)

~~~json
{
  "source": "00b4ae08",
  "target": "010a1010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ae0c`](#insn-00b4ae0c)

~~~json
{
  "source": "00b4ae0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
