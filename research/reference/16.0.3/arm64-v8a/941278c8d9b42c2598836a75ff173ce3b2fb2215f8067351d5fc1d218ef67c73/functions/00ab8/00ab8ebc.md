# 00ab8ebc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ab7ec8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab7/00ab7ec8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-a4bbb9e05fcbe3279d26946f423c4304)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ab8ebc",
  "name": "FUN_00ab8ebc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f0b213005e45fb39a84de607e69b5be56db163378d8c01585dac061d91fced8",
  "source_text_sha256": "3f0b213005e45fb39a84de607e69b5be56db163378d8c01585dac061d91fced8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ab8ebc",
        "00ab8eef"
      ]
    ],
    "bytes_sha256": "dd8d72260751a6153e25984ebfc99e75f0a5636289fd8f8494b18ae5dcc68a36",
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

- [00c58f30](../00c58/00c58f30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_00ab8ebc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c8e2a8;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ab8ebc"></a> `00ab8ebc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ab8ec0"></a> `00ab8ec0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab8ec4"></a> `00ab8ec4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ab8ec8"></a> `00ab8ec8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ab8ecc"></a> `00ab8ecc` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00ab8ed0"></a> `00ab8ed0` | `18 80 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00ab8ed4"></a> `00ab8ed4` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00ab8ed8"></a> `00ab8ed8` | `a8 0e 00 d0` | adrp x8,0xc8e000 | `FALL_THROUGH`
<a id="insn-00ab8edc"></a> `00ab8edc` | `08 a1 0a 91` | add x8,x8,#0x2a8 | `FALL_THROUGH`
<a id="insn-00ab8ee0"></a> `00ab8ee0` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00ab8ee4"></a> `00ab8ee4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab8ee8"></a> `00ab8ee8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ab8eec"></a> `00ab8eec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ab8ebc`](#insn-00ab8ebc) 範囲 `[['00ab8ebc', '00ab8eef']]`

## 命令位置別の参照

- [`00ab8ebc`](#insn-00ab8ebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab8ec0`](#insn-00ab8ec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab8ed0`](#insn-00ab8ed0) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00ab8ee0`](#insn-00ab8ee0) → `00c8e2a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ab8ee4`](#insn-00ab8ee4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab8ee8`](#insn-00ab8ee8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ab8ebc`](#insn-00ab8ebc)

~~~json
{
  "source": "00ab8ebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab8ec0`](#insn-00ab8ec0)

~~~json
{
  "source": "00ab8ec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab8ed0`](#insn-00ab8ed0)

~~~json
{
  "source": "00ab8ed0",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab8ee0`](#insn-00ab8ee0)

~~~json
{
  "source": "00ab8ee0",
  "target": "00c8e2a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e2a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ab8ee4`](#insn-00ab8ee4)

~~~json
{
  "source": "00ab8ee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab8ee8`](#insn-00ab8ee8)

~~~json
{
  "source": "00ab8ee8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
