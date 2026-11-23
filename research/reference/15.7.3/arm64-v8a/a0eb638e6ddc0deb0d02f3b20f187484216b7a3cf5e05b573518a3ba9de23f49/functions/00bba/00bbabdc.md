# 00bbabdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbab14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbab14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-acd312b093b3105b48154d4149274a5a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbac20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-9bf65a3f322b1558cc2df94712e7b0e7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbabdc",
  "name": "_ZSt14set_unexpectedPFvvE",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2528d91edbbb2871e2d91662c615e20378ae582b14e3fa1dc9fc7031f3acc696",
  "source_text_sha256": "2528d91edbbb2871e2d91662c615e20378ae582b14e3fa1dc9fc7031f3acc696",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbabdc",
        "00bbac0f"
      ]
    ],
    "bytes_sha256": "e474cc03b2c5bf9f96615fb4b0b205ffd53bf7a20abda1660a17b044e3b762fb",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bd6d90](../00bd6/00bd6d90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 314 bytes

~~~c

void _ZSt14set_unexpectedPFvvE(code *param_1)

{
  code *pcVar1;
  
  pcVar1 = FUN_00bbabbc;
  if (param_1 != (code *)0x0) {
    pcVar1 = param_1;
  }
  FUN_00bd6d90(pcVar1,PTR___cxa_unexpected_handler_00c1bfa8);
                    /* catch() { ... } // from try @ 00bb3784 with catch @ 00bbac04 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbabdc"></a> `00bbabdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbabe0"></a> `00bbabe0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbabe4"></a> `00bbabe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbabe8"></a> `00bbabe8` | `01 03 00 b0` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbabec"></a> `00bbabec` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bbabf0"></a> `00bbabf0` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbabf4"></a> `00bbabf4` | `48 fe ff 10` | adr x8,0xbbabbc | `FALL_THROUGH`
<a id="insn-00bbabf8"></a> `00bbabf8` | `21 d4 47 f9` | ldr x1,[x1, #0xfa8] | `FALL_THROUGH`
<a id="insn-00bbabfc"></a> `00bbabfc` | `00 01 80 9a` | csel x0,x8,x0,eq | `FALL_THROUGH`
<a id="insn-00bbac00"></a> `00bbac00` | `64 70 00 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac04"></a> `00bbac04` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbac08"></a> `00bbac08` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbac0c"></a> `00bbac0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbabdc`](#insn-00bbabdc) 範囲 `[['00bbabdc', '00bbac03']]`
  - `FALL_THROUGH` [`00bbac00`](#insn-00bbac00) → [`00bbac04`](#insn-00bbac04)
- ブロック [`00bbac04`](#insn-00bbac04) 範囲 `[['00bbac04', '00bbac0f']]`

## 命令位置別の参照

- [`00bbabe0`](#insn-00bbabe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabf8`](#insn-00bbabf8) → `00c1bfa8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbabf8`](#insn-00bbabf8) → `00c24948`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `__cxa_unexpected_handler` · 推定型 `pointer`
- [`00bbabfc`](#insn-00bbabfc) → [`00bbabbc`](00bbabbc.md) · `PARAM` · `ANALYSIS` · 関数 `00bbabbc` · 推定シンボル `None` · 推定型 `None`
- [`00bbac00`](#insn-00bbac00) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00bbac04`](#insn-00bbac04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbabe0`](#insn-00bbabe0)

~~~json
{
  "source": "00bbabe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabf8`](#insn-00bbabf8)

~~~json
{
  "source": "00bbabf8",
  "target": "00c1bfa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bfa8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbabf8`](#insn-00bbabf8)

~~~json
{
  "source": "00bbabf8",
  "target": "00c24948",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24948",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbabfc`](#insn-00bbabfc)

~~~json
{
  "source": "00bbabfc",
  "target": "00bbabbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac00`](#insn-00bbac00)

~~~json
{
  "source": "00bbac00",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac04`](#insn-00bbac04)

~~~json
{
  "source": "00bbac04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
