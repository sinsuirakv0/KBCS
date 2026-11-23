# 00ae7eec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae7fb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7fb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-141a725d7bf888fae506c1566416aa62)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae7eec",
  "name": "_ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23a6603c785c41e1b684fe1e4b364388603a87eedf689257b3e7d1b430f698c1",
  "source_text_sha256": "23a6603c785c41e1b684fe1e4b364388603a87eedf689257b3e7d1b430f698c1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae7eec",
        "00ae7f27"
      ]
    ],
    "bytes_sha256": "6d749d143ceb1ec981aea62637376fdfa31386f880a8e56d789e2445047f3b6e",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde340](../00bde/00bde340.md)

## 呼び出し先

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 408 bytes

~~~c

undefined8 _ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
                    /* try { // try from 00ae7f0c to 00be7f17 has its CatchHandler @ 00ae8974 */
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
                    /* try { // try from 00ae7f18 to 00be7f2b has its CatchHandler @ 00ae896c */
  return (&DAT_010a04d0)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae7eec"></a> `00ae7eec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae7ef0"></a> `00ae7ef0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7ef4"></a> `00ae7ef4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae7ef8"></a> `00ae7ef8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00ae7efc"></a> `00ae7efc` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00ae7f00"></a> `00ae7f00` | `8b 00 00 54` | b.lt 0x00ae7f10 | `CONDITIONAL_JUMP`
<a id="insn-00ae7f04"></a> `00ae7f04` | `80 bd ff b0` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00ae7f08"></a> `00ae7f08` | `00 1c 15 91` | add x0,x0,#0x547 | `FALL_THROUGH`
<a id="insn-00ae7f0c"></a> `00ae7f0c` | `5d d8 03 94` | bl 0x00bde080 | `UNCONDITIONAL_CALL`
<a id="insn-00ae7f10"></a> `00ae7f10` | `c8 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae7f14"></a> `00ae7f14` | `08 41 13 91` | add x8,x8,#0x4d0 | `FALL_THROUGH`
<a id="insn-00ae7f18"></a> `00ae7f18` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00ae7f1c"></a> `00ae7f1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7f20"></a> `00ae7f20` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae7f24"></a> `00ae7f24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae7eec`](#insn-00ae7eec) 範囲 `[['00ae7eec', '00ae7f03']]`
  - `CONDITIONAL_JUMP` [`00ae7f00`](#insn-00ae7f00) → [`00ae7f10`](#insn-00ae7f10)
  - `FALL_THROUGH` [`00ae7f00`](#insn-00ae7f00) → [`00ae7f04`](#insn-00ae7f04)
- ブロック [`00ae7f04`](#insn-00ae7f04) 範囲 `[['00ae7f04', '00ae7f0b']]`
  - `FALL_THROUGH` [`00ae7f08`](#insn-00ae7f08) → [`00ae7f0c`](#insn-00ae7f0c)
- ブロック [`00ae7f0c`](#insn-00ae7f0c) 範囲 `[['00ae7f0c', '00ae7f0f']]`
  - `FALL_THROUGH` [`00ae7f0c`](#insn-00ae7f0c) → [`00ae7f10`](#insn-00ae7f10)
- ブロック [`00ae7f10`](#insn-00ae7f10) 範囲 `[['00ae7f10', '00ae7f17']]`
  - `FALL_THROUGH` [`00ae7f14`](#insn-00ae7f14) → [`00ae7f18`](#insn-00ae7f18)
- ブロック [`00ae7f18`](#insn-00ae7f18) 範囲 `[['00ae7f18', '00ae7f27']]`

## 命令位置別の参照

- [`00ae7eec`](#insn-00ae7eec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7ef0`](#insn-00ae7ef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7f00`](#insn-00ae7f00) → [`00ae7f10`](#insn-00ae7f10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7f08`](#insn-00ae7f08) → `00298547`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae7f0c`](#insn-00ae7f0c) → [`00bde080`](../00bde/00bde080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde080` · 推定シンボル `None` · 推定型 `None`
- [`00ae7f18`](#insn-00ae7f18) → `010a04d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7f1c`](#insn-00ae7f1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae7eec`](#insn-00ae7eec)

~~~json
{
  "source": "00ae7eec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7ef0`](#insn-00ae7ef0)

~~~json
{
  "source": "00ae7ef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7f00`](#insn-00ae7f00)

~~~json
{
  "source": "00ae7f00",
  "target": "00ae7f10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7f08`](#insn-00ae7f08)

~~~json
{
  "source": "00ae7f08",
  "target": "00298547",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298547",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "00298547",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae7f0c`](#insn-00ae7f0c)

~~~json
{
  "source": "00ae7f0c",
  "target": "00bde080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae7f18`](#insn-00ae7f18)

~~~json
{
  "source": "00ae7f18",
  "target": "010a04d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7f1c`](#insn-00ae7f1c)

~~~json
{
  "source": "00ae7f1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
