# 00bcc9fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc960`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc960.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-8032f4780840c2c3bff77244426469d0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcd9f0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcd9f0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-d27a07cdfe901f7624056ba7004508d9)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcc9fc",
  "name": "_ZN8firebase4auth17signinmethodquery10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af7a6705d0cdd5ad347952e47006820c8ae5e534dc15811c22ea448297200e9f",
  "source_text_sha256": "af7a6705d0cdd5ad347952e47006820c8ae5e534dc15811c22ea448297200e9f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcc9fc",
        "00bcca37"
      ]
    ],
    "bytes_sha256": "a10244d00c0f6d1a46fa3c80d66a53ac789f68aa652711d1176f0d7c17a566b8",
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

- [00c5b0d0](../00c5b/00c5b0d0.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 241 bytes

~~~c

undefined8 _ZN8firebase4auth17signinmethodquery10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_011268e8 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcc9fc"></a> `00bcc9fc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcca00"></a> `00bcca00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcca04"></a> `00bcca04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcca08"></a> `00bcca08` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bcca0c"></a> `00bcca0c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bcca10"></a> `00bcca10` | `8b 00 00 54` | b.lt 0x00bcca20 | `CONDITIONAL_JUMP`
<a id="insn-00bcca14"></a> `00bcca14` | `e0 b6 ff b0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bcca18"></a> `00bcca18` | `00 34 15 91` | add x0,x0,#0x54d | `FALL_THROUGH`
<a id="insn-00bcca1c"></a> `00bcca1c` | `ad 39 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcca20"></a> `00bcca20` | `c8 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcca24"></a> `00bcca24` | `08 a1 23 91` | add x8,x8,#0x8e8 | `FALL_THROUGH`
<a id="insn-00bcca28"></a> `00bcca28` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bcca2c"></a> `00bcca2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcca30"></a> `00bcca30` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcca34"></a> `00bcca34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcc9fc`](#insn-00bcc9fc) 範囲 `[['00bcc9fc', '00bcca13']]`
  - `CONDITIONAL_JUMP` [`00bcca10`](#insn-00bcca10) → [`00bcca20`](#insn-00bcca20)
  - `FALL_THROUGH` [`00bcca10`](#insn-00bcca10) → [`00bcca14`](#insn-00bcca14)
- ブロック [`00bcca14`](#insn-00bcca14) 範囲 `[['00bcca14', '00bcca1f']]`
  - `FALL_THROUGH` [`00bcca1c`](#insn-00bcca1c) → [`00bcca20`](#insn-00bcca20)
- ブロック [`00bcca20`](#insn-00bcca20) 範囲 `[['00bcca20', '00bcca37']]`

## 命令位置別の参照

- [`00bcc9fc`](#insn-00bcc9fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca00`](#insn-00bcca00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca10`](#insn-00bcca10) → [`00bcca20`](#insn-00bcca20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca18`](#insn-00bcca18) → `002a954d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcca1c`](#insn-00bcca1c) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcca28`](#insn-00bcca28) → `011268e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcca2c`](#insn-00bcca2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcc9fc`](#insn-00bcc9fc)

~~~json
{
  "source": "00bcc9fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca00`](#insn-00bcca00)

~~~json
{
  "source": "00bcca00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca10`](#insn-00bcca10)

~~~json
{
  "source": "00bcca10",
  "target": "00bcca20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca18`](#insn-00bcca18)

~~~json
{
  "source": "00bcca18",
  "target": "002a954d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a954d",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002a954d",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcca1c`](#insn-00bcca1c)

~~~json
{
  "source": "00bcca1c",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcca28`](#insn-00bcca28)

~~~json
{
  "source": "00bcca28",
  "target": "011268e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcca2c`](#insn-00bcca2c)

~~~json
{
  "source": "00bcca2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
