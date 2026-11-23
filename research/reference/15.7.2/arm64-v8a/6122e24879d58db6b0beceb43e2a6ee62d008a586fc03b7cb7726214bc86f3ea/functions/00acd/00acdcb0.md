# 00acdcb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acdd78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acdd78.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-ef40c902752d8c0121bbb220e81a7402)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acdcb0",
  "name": "FUN_00acdcb0",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c2a146f4031a944ed272ce513f1b77267345167b1a18dce871575c9667fccb2f",
  "source_text_sha256": "c2a146f4031a944ed272ce513f1b77267345167b1a18dce871575c9667fccb2f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acdcb0",
        "00acdcf3"
      ]
    ],
    "bytes_sha256": "d0c81ec8e29ea891765d707ebdba2008ce4bbca05a02ab428917ebe36fcb2cd4",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00657e7c](../00657/00657e7c.md)

## 呼び出し先

- [00adcbcc](../00adc/00adcbcc.md)
- [00bdb140](../00bdb/00bdb140.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 188 bytes

~~~c

void FUN_00acdcb0(undefined8 *param_1)

{
  FUN_00adcbcc();
  *param_1 = &PTR_FUN_00bf7208;
  memset(param_1 + 0x15,0,0x220);
  *(undefined4 *)(param_1 + 0x59) = 0x3f800000;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acdcb0"></a> `00acdcb0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acdcb4"></a> `00acdcb4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acdcb8"></a> `00acdcb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acdcbc"></a> `00acdcbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acdcc0"></a> `00acdcc0` | `c3 3b 00 94` | bl 0x00adcbcc | `UNCONDITIONAL_CALL`
<a id="insn-00acdcc4"></a> `00acdcc4` | `48 09 00 d0` | adrp x8,0xbf7000 | `FALL_THROUGH`
<a id="insn-00acdcc8"></a> `00acdcc8` | `08 21 08 91` | add x8,x8,#0x208 | `FALL_THROUGH`
<a id="insn-00acdccc"></a> `00acdccc` | `60 a2 02 91` | add x0,x19,#0xa8 | `FALL_THROUGH`
<a id="insn-00acdcd0"></a> `00acdcd0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acdcd4"></a> `00acdcd4` | `02 44 80 52` | mov w2,#0x220 | `FALL_THROUGH`
<a id="insn-00acdcd8"></a> `00acdcd8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00acdcdc"></a> `00acdcdc` | `19 35 04 94` | bl 0x00bdb140 | `UNCONDITIONAL_CALL`
<a id="insn-00acdce0"></a> `00acdce0` | `08 f0 a7 52` | mov w8,#0x3f800000 | `FALL_THROUGH`
<a id="insn-00acdce4"></a> `00acdce4` | `68 ca 02 b9` | str w8,[x19, #0x2c8] | `FALL_THROUGH`
<a id="insn-00acdce8"></a> `00acdce8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acdcec"></a> `00acdcec` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acdcf0"></a> `00acdcf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acdcb0`](#insn-00acdcb0) 範囲 `[['00acdcb0', '00acdcf3']]`

## 命令位置別の参照

- [`00acdcb0`](#insn-00acdcb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acdcb4`](#insn-00acdcb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acdcc0`](#insn-00acdcc0) → [`00adcbcc`](../00adc/00adcbcc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adcbcc` · 推定シンボル `None` · 推定型 `None`
- [`00acdcd8`](#insn-00acdcd8) → `00bf7208`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acdcdc`](#insn-00acdcdc) → [`00bdb140`](../00bdb/00bdb140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb140` · 推定シンボル `None` · 推定型 `None`
- [`00acdce8`](#insn-00acdce8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acdcec`](#insn-00acdcec) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acdcb0`](#insn-00acdcb0)

~~~json
{
  "source": "00acdcb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acdcb4`](#insn-00acdcb4)

~~~json
{
  "source": "00acdcb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acdcc0`](#insn-00acdcc0)

~~~json
{
  "source": "00acdcc0",
  "target": "00adcbcc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acdcd8`](#insn-00acdcd8)

~~~json
{
  "source": "00acdcd8",
  "target": "00bf7208",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf7208",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acdcdc`](#insn-00acdcdc)

~~~json
{
  "source": "00acdcdc",
  "target": "00bdb140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acdce8`](#insn-00acdce8)

~~~json
{
  "source": "00acdce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acdcec`](#insn-00acdcec)

~~~json
{
  "source": "00acdcec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
