# 00befb0c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bef6e4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef6e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-a8d5c05308f5fb9cdde0768dabf47587)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00befba8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befba8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-67f9ab61d2706e7551f5fd7903552f69)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befb0c",
  "name": "_ZNSt16nested_exceptionC2Ev",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a83acee3a1d12a3c199bb2987b2e0ae2f296cabb3dc6e06dd77650a9794d5fee",
  "source_text_sha256": "a83acee3a1d12a3c199bb2987b2e0ae2f296cabb3dc6e06dd77650a9794d5fee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befb0c",
        "00befb47"
      ]
    ],
    "bytes_sha256": "71227331b1212078ea5cf510c4ade232e43f16a0c4b5c265a79a05e0c250f0c3",
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

- [00c5df40](../00c5d/00c5df40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 216 bytes

~~~c

void _ZNSt16nested_exceptionC2Ev(long *param_1)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVSt16nested_exception_00c9ba70 + 0x10);
  lVar1 = __cxa_current_primary_exception();
  param_1[1] = lVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befb0c"></a> `00befb0c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00befb10"></a> `00befb10` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00befb14"></a> `00befb14` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befb18"></a> `00befb18` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00befb1c"></a> `00befb1c` | `68 05 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00befb20"></a> `00befb20` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00befb24"></a> `00befb24` | `08 39 45 f9` | ldr x8,[x8, #0xa70] | `FALL_THROUGH`
<a id="insn-00befb28"></a> `00befb28` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00befb2c"></a> `00befb2c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00befb30"></a> `00befb30` | `04 b9 01 94` | bl 0x00c5df40 | `UNCONDITIONAL_CALL`
<a id="insn-00befb34"></a> `00befb34` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00befb38"></a> `00befb38` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befb3c"></a> `00befb3c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00befb40"></a> `00befb40` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00befb44"></a> `00befb44` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befb0c`](#insn-00befb0c) 範囲 `[['00befb0c', '00befb47']]`

## 命令位置別の参照

- [`00befb10`](#insn-00befb10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befb14`](#insn-00befb14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befb24`](#insn-00befb24) → `00c9ba70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00befb2c`](#insn-00befb2c) → `00c929d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[32]`
- [`00befb30`](#insn-00befb30) → [`00c5df40`](../00c5d/00c5df40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5df40` · 推定シンボル `None` · 推定型 `None`
- [`00befb38`](#insn-00befb38) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befb3c`](#insn-00befb3c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befb10`](#insn-00befb10)

~~~json
{
  "source": "00befb10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befb14`](#insn-00befb14)

~~~json
{
  "source": "00befb14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befb24`](#insn-00befb24)

~~~json
{
  "source": "00befb24",
  "target": "00c9ba70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00befb2c`](#insn-00befb2c)

~~~json
{
  "source": "00befb2c",
  "target": "00c929d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c929c8",
  "offset": 16,
  "size": 32,
  "datatype": "undefined1[32]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00befb30`](#insn-00befb30)

~~~json
{
  "source": "00befb30",
  "target": "00c5df40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befb38`](#insn-00befb38)

~~~json
{
  "source": "00befb38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befb3c`](#insn-00befb3c)

~~~json
{
  "source": "00befb3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
