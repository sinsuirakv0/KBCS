# 00befb4c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befab0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befab0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-263d816a7f0177b15b6e1057f9e24e27)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf0b40`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0b40.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-cded7bc4ba445495a8246fdad5e60c45)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befb4c",
  "name": "_ZNSt13exception_ptraSERKS_",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6a4f2b6986ae6b3efb7483c629be87c5306bc0480dbf480a3c7b17005fe96bd8",
  "source_text_sha256": "6a4f2b6986ae6b3efb7483c629be87c5306bc0480dbf480a3c7b17005fe96bd8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befb4c",
        "00befb9b"
      ]
    ],
    "bytes_sha256": "94c2e68f5be4da6db96600e151d2414acdd9c2e8949e372e51b70b5dcca72d70",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e000](../00c5e/00c5e000.md)

## 呼び出し先

- [00c5dfe0](../00c5d/00c5dfe0.md)
- [00c5dff0](../00c5d/00c5dff0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 240 bytes

~~~c

long * _ZNSt13exception_ptraSERKS_(long *param_1,long *param_2)

{
  if (*param_1 != *param_2) {
    __cxa_increment_exception_refcount();
    __cxa_decrement_exception_refcount(*param_1);
    *param_1 = *param_2;
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befb4c"></a> `00befb4c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00befb50"></a> `00befb50` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00befb54"></a> `00befb54` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befb58"></a> `00befb58` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00befb5c"></a> `00befb5c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00befb60"></a> `00befb60` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00befb64"></a> `00befb64` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00befb68"></a> `00befb68` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00befb6c"></a> `00befb6c` | `e0 00 00 54` | b.eq 0x00befb88 | `CONDITIONAL_JUMP`
<a id="insn-00befb70"></a> `00befb70` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00befb74"></a> `00befb74` | `1f b9 01 94` | bl 0x00c5dff0 | `UNCONDITIONAL_CALL`
<a id="insn-00befb78"></a> `00befb78` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00befb7c"></a> `00befb7c` | `19 b9 01 94` | bl 0x00c5dfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00befb80"></a> `00befb80` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00befb84"></a> `00befb84` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00befb88"></a> `00befb88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00befb8c"></a> `00befb8c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befb90"></a> `00befb90` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00befb94"></a> `00befb94` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00befb98"></a> `00befb98` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befb4c`](#insn-00befb4c) 範囲 `[['00befb4c', '00befb6f']]`
  - `CONDITIONAL_JUMP` [`00befb6c`](#insn-00befb6c) → [`00befb88`](#insn-00befb88)
  - `FALL_THROUGH` [`00befb6c`](#insn-00befb6c) → [`00befb70`](#insn-00befb70)
- ブロック [`00befb70`](#insn-00befb70) 範囲 `[['00befb70', '00befb87']]`
  - `FALL_THROUGH` [`00befb84`](#insn-00befb84) → [`00befb88`](#insn-00befb88)
- ブロック [`00befb88`](#insn-00befb88) 範囲 `[['00befb88', '00befb9b']]`

## 命令位置別の参照

- [`00befb50`](#insn-00befb50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befb54`](#insn-00befb54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befb6c`](#insn-00befb6c) → [`00befb88`](#insn-00befb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befb74`](#insn-00befb74) → [`00c5dff0`](../00c5d/00c5dff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dff0` · 推定シンボル `None` · 推定型 `None`
- [`00befb7c`](#insn-00befb7c) → [`00c5dfe0`](../00c5d/00c5dfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dfe0` · 推定シンボル `None` · 推定型 `None`
- [`00befb8c`](#insn-00befb8c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befb90`](#insn-00befb90) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befb50`](#insn-00befb50)

~~~json
{
  "source": "00befb50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befb54`](#insn-00befb54)

~~~json
{
  "source": "00befb54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befb6c`](#insn-00befb6c)

~~~json
{
  "source": "00befb6c",
  "target": "00befb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befb74`](#insn-00befb74)

~~~json
{
  "source": "00befb74",
  "target": "00c5dff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befb7c`](#insn-00befb7c)

~~~json
{
  "source": "00befb7c",
  "target": "00c5dfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befb8c`](#insn-00befb8c)

~~~json
{
  "source": "00befb8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befb90`](#insn-00befb90)

~~~json
{
  "source": "00befb90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
