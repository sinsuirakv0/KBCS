# 00ae5ecc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae5e04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5e04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-9377384ca33fc35111724d9ca228c58a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae5f10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0061.md#compare-d58a2b1f6cb0168ce6fb036f4e944b81)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae5ecc",
  "name": "_ZN8firebase4util3log11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8ba03516ad9d6dbcdc977be0b8b9ffae727d0368ed20af6d13dcaad057d7695f",
  "source_text_sha256": "8ba03516ad9d6dbcdc977be0b8b9ffae727d0368ed20af6d13dcaad057d7695f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae5ecc",
        "00ae5f07"
      ]
    ],
    "bytes_sha256": "e56ac84f87be768db22aa3b1b141596a8958b774ed832330c855a0d874907de0",
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
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 910 bytes

~~~c

undefined8 _ZN8firebase4util3log11GetMethodIdENS1_6MethodE(uint param_1)

{
                    /* try { // try from 00ae5edc to 00be5ee3 has its CatchHandler @ 00ae5ee4 */
  if (0 < (int)param_1) {
                    /* catch() { ... } // from try @ 00ae5de4 with catch @ 00ae5ee4
                       catch() { ... } // from try @ 00ae5edc with catch @ 00ae5ee4
                       try { // try from 00ae5ee4 to 00be5f1f has its CatchHandler @ 00ae596c */
                    /* catch() { ... } // from try @ 00ae5cfc with catch @ 00ae5ee8
                       catch() { ... } // from try @ 00ae5e58 with catch @ 00ae5ee8 */
                    /* catch() { ... } // from try @ 00ae5c64 with catch @ 00ae5eec */
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
                    /* catch() { ... } // from try @ 00ae5bfc with catch @ 00ae5ef0 */
  return (&DAT_010a03e8)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae5ecc"></a> `00ae5ecc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae5ed0"></a> `00ae5ed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae5ed4"></a> `00ae5ed4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae5ed8"></a> `00ae5ed8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00ae5edc"></a> `00ae5edc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ae5ee0"></a> `00ae5ee0` | `8b 00 00 54` | b.lt 0x00ae5ef0 | `CONDITIONAL_JUMP`
<a id="insn-00ae5ee4"></a> `00ae5ee4` | `80 bd ff f0` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00ae5ee8"></a> `00ae5ee8` | `00 50 17 91` | add x0,x0,#0x5d4 | `FALL_THROUGH`
<a id="insn-00ae5eec"></a> `00ae5eec` | `91 e0 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00ae5ef0"></a> `00ae5ef0` | `c8 2d 00 f0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae5ef4"></a> `00ae5ef4` | `08 a1 0f 91` | add x8,x8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00ae5ef8"></a> `00ae5ef8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00ae5efc"></a> `00ae5efc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae5f00"></a> `00ae5f00` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae5f04"></a> `00ae5f04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae5ecc`](#insn-00ae5ecc) 範囲 `[['00ae5ecc', '00ae5edb']]`
  - `FALL_THROUGH` [`00ae5ed8`](#insn-00ae5ed8) → [`00ae5edc`](#insn-00ae5edc)
- ブロック [`00ae5edc`](#insn-00ae5edc) 範囲 `[['00ae5edc', '00ae5ee3']]`
  - `CONDITIONAL_JUMP` [`00ae5ee0`](#insn-00ae5ee0) → [`00ae5ef0`](#insn-00ae5ef0)
  - `FALL_THROUGH` [`00ae5ee0`](#insn-00ae5ee0) → [`00ae5ee4`](#insn-00ae5ee4)
- ブロック [`00ae5ee4`](#insn-00ae5ee4) 範囲 `[['00ae5ee4', '00ae5ee7']]`
  - `FALL_THROUGH` [`00ae5ee4`](#insn-00ae5ee4) → [`00ae5ee8`](#insn-00ae5ee8)
- ブロック [`00ae5ee8`](#insn-00ae5ee8) 範囲 `[['00ae5ee8', '00ae5eeb']]`
  - `FALL_THROUGH` [`00ae5ee8`](#insn-00ae5ee8) → [`00ae5eec`](#insn-00ae5eec)
- ブロック [`00ae5eec`](#insn-00ae5eec) 範囲 `[['00ae5eec', '00ae5eef']]`
  - `FALL_THROUGH` [`00ae5eec`](#insn-00ae5eec) → [`00ae5ef0`](#insn-00ae5ef0)
- ブロック [`00ae5ef0`](#insn-00ae5ef0) 範囲 `[['00ae5ef0', '00ae5f07']]`

## 命令位置別の参照

- [`00ae5ecc`](#insn-00ae5ecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae5ed0`](#insn-00ae5ed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae5ee0`](#insn-00ae5ee0) → [`00ae5ef0`](#insn-00ae5ef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae5ee8`](#insn-00ae5ee8) → `002985d4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae5eec`](#insn-00ae5eec) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00ae5ef8`](#insn-00ae5ef8) → `010a03e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae5efc`](#insn-00ae5efc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae5ecc`](#insn-00ae5ecc)

~~~json
{
  "source": "00ae5ecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae5ed0`](#insn-00ae5ed0)

~~~json
{
  "source": "00ae5ed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae5ee0`](#insn-00ae5ee0)

~~~json
{
  "source": "00ae5ee0",
  "target": "00ae5ef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae5ee8`](#insn-00ae5ee8)

~~~json
{
  "source": "00ae5ee8",
  "target": "002985d4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002985d4",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002985d4",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae5eec`](#insn-00ae5eec)

~~~json
{
  "source": "00ae5eec",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae5ef8`](#insn-00ae5ef8)

~~~json
{
  "source": "00ae5ef8",
  "target": "010a03e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae5efc`](#insn-00ae5efc)

~~~json
{
  "source": "00ae5efc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
