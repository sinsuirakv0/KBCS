# 00bcadfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bca9d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-cb53573ca96c0e06b6c8e4d3090c0dcf)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcae98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcae98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-9f5fae9aa6279343cc4620c0dfece785)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcadfc",
  "name": "_ZN8firebase4auth4Auth3appEv",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d091b0ac1e4e2de17e851ba733b61c7dae759f81724e54341b7d3ae1144371b",
  "source_text_sha256": "5d091b0ac1e4e2de17e851ba733b61c7dae759f81724e54341b7d3ae1144371b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcadfc",
        "00bcae33"
      ]
    ],
    "bytes_sha256": "30cf1a83076b968c0559ec35379e2220f53be4dc31f01569e648544def2aaaa9",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5da80](../00c5d/00c5da80.md)

## 呼び出し先

- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"auth_data_ != nullptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 282 bytes

~~~c

undefined8 _ZN8firebase4auth4Auth3appEv(undefined8 *param_1)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)*param_1;
  if (puVar1 == (undefined8 *)0x0) {
    _ZN8firebase9LogAssertEPKcz("auth_data_ != nullptr");
    puVar1 = (undefined8 *)*param_1;
  }
  return *puVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcadfc"></a> `00bcadfc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcae00"></a> `00bcae00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcae04"></a> `00bcae04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcae08"></a> `00bcae08` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcae0c"></a> `00bcae0c` | `c8 00 00 b5` | cbnz x8,0x00bcae24 | `CONDITIONAL_JUMP`
<a id="insn-00bcae10"></a> `00bcae10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcae14"></a> `00bcae14` | `20 b7 ff f0` | adrp x0,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bcae18"></a> `00bcae18` | `00 20 1c 91` | add x0,x0,#0x708 | `FALL_THROUGH`
<a id="insn-00bcae1c"></a> `00bcae1c` | `79 40 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bcae20"></a> `00bcae20` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcae24"></a> `00bcae24` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcae28"></a> `00bcae28` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcae2c"></a> `00bcae2c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcae30"></a> `00bcae30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcadfc`](#insn-00bcadfc) 範囲 `[['00bcadfc', '00bcae0f']]`
  - `CONDITIONAL_JUMP` [`00bcae0c`](#insn-00bcae0c) → [`00bcae24`](#insn-00bcae24)
  - `FALL_THROUGH` [`00bcae0c`](#insn-00bcae0c) → [`00bcae10`](#insn-00bcae10)
- ブロック [`00bcae10`](#insn-00bcae10) 範囲 `[['00bcae10', '00bcae23']]`
  - `FALL_THROUGH` [`00bcae20`](#insn-00bcae20) → [`00bcae24`](#insn-00bcae24)
- ブロック [`00bcae24`](#insn-00bcae24) 範囲 `[['00bcae24', '00bcae33']]`

## 命令位置別の参照

- [`00bcadfc`](#insn-00bcadfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae00`](#insn-00bcae00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae0c`](#insn-00bcae0c) → [`00bcae24`](#insn-00bcae24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae18`](#insn-00bcae18) → `002b1708`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcae1c`](#insn-00bcae1c) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bcae28`](#insn-00bcae28) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcadfc`](#insn-00bcadfc)

~~~json
{
  "source": "00bcadfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae00`](#insn-00bcae00)

~~~json
{
  "source": "00bcae00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae0c`](#insn-00bcae0c)

~~~json
{
  "source": "00bcae0c",
  "target": "00bcae24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae18`](#insn-00bcae18)

~~~json
{
  "source": "00bcae18",
  "target": "002b1708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1708",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "617574685f646174615f20213d206e756c6c70747200",
  "capture_start": "002b1708",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcae1c`](#insn-00bcae1c)

~~~json
{
  "source": "00bcae1c",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcae28`](#insn-00bcae28)

~~~json
{
  "source": "00bcae28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
