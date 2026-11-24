# 00befaa4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befa08`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa08.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-629e6170cc24c4cd8c8c04c3fbdbf6e2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf0a98`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0a98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-4f84bc13e870928a66d909437b869ffc)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befaa4",
  "name": "_ZNSt6__ndk16chrono12steady_clock3nowEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f786a19d96d4d6bd97bfbe16c71d2c3731ce5e31e9fd9f46d8152ba90213d511",
  "source_text_sha256": "f786a19d96d4d6bd97bfbe16c71d2c3731ce5e31e9fd9f46d8152ba90213d511",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befaa4",
        "00befaf7"
      ]
    ],
    "bytes_sha256": "ae739f487ea75ab85dded3261871d6a2dfb701fc549ba227ddc3b1d3e06394b2",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c57f90](../00c57/00c57f90.md)

## 呼び出し先

- [00c58190](../00c58/00c58190.md)
- [00c581f0](../00c58/00c581f0.md)
- [00c597d0](../00c59/00c597d0.md)

## 関連文字列（未確認候補）

~~~text
"clock_gettime(CLOCK_MONOTONIC) failed"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 429 bytes

~~~c

long _ZNSt6__ndk16chrono12steady_clock3nowEv(void)

{
  int iVar1;
  undefined4 *puVar2;
  timespec local_20;
  
  iVar1 = clock_gettime(1,&local_20);
  if (iVar1 == 0) {
    return local_20.tv_nsec + local_20.tv_sec * 1000000000;
  }
  puVar2 = (undefined4 *)__errno();
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(*puVar2,"clock_gettime(CLOCK_MONOTONIC) failed");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befaa4"></a> `00befaa4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00befaa8"></a> `00befaa8` | `ff 83 00 d1` | sub sp,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00befaac"></a> `00befaac` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befab0"></a> `00befab0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00befab4"></a> `00befab4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00befab8"></a> `00befab8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00befabc"></a> `00befabc` | `45 a7 01 94` | bl 0x00c597d0 | `UNCONDITIONAL_CALL`
<a id="insn-00befac0"></a> `00befac0` | `20 01 00 35` | cbnz w0,0x00befae4 | `CONDITIONAL_JUMP`
<a id="insn-00befac4"></a> `00befac4` | `e8 2b 40 a9` | ldp x8,x10,[sp] | `FALL_THROUGH`
<a id="insn-00befac8"></a> `00befac8` | `09 40 99 52` | mov w9,#0xca00 | `FALL_THROUGH`
<a id="insn-00befacc"></a> `00befacc` | `49 73 a7 72` | movk w9,#0x3b9a, LSL #16 | `FALL_THROUGH`
<a id="insn-00befad0"></a> `00befad0` | `00 29 09 9b` | madd x0,x8,x9,x10 | `FALL_THROUGH`
<a id="insn-00befad4"></a> `00befad4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befad8"></a> `00befad8` | `ff 83 00 91` | add sp,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00befadc"></a> `00befadc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00befae0"></a> `00befae0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00befae4"></a> `00befae4` | `ab a1 01 94` | bl 0x00c58190 | `UNCONDITIONAL_CALL`
<a id="insn-00befae8"></a> `00befae8` | `00 00 40 b9` | ldr w0,[x0] | `FALL_THROUGH`
<a id="insn-00befaec"></a> `00befaec` | `a1 b5 ff d0` | adrp x1,0x2a5000 | `FALL_THROUGH`
<a id="insn-00befaf0"></a> `00befaf0` | `21 0c 05 91` | add x1,x1,#0x143 | `FALL_THROUGH`
<a id="insn-00befaf4"></a> `00befaf4` | `bf a1 01 94` | bl 0x00c581f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befaa4`](#insn-00befaa4) 範囲 `[['00befaa4', '00befac3']]`
  - `CONDITIONAL_JUMP` [`00befac0`](#insn-00befac0) → [`00befae4`](#insn-00befae4)
  - `FALL_THROUGH` [`00befac0`](#insn-00befac0) → [`00befac4`](#insn-00befac4)
- ブロック [`00befac4`](#insn-00befac4) 範囲 `[['00befac4', '00befae3']]`
- ブロック [`00befae4`](#insn-00befae4) 範囲 `[['00befae4', '00befaf7']]`

## 命令位置別の参照

- [`00befaac`](#insn-00befaac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befabc`](#insn-00befabc) → [`00c597d0`](../00c59/00c597d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c597d0` · 推定シンボル `None` · 推定型 `None`
- [`00befac0`](#insn-00befac0) → [`00befae4`](#insn-00befae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befac4`](#insn-00befac4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befad4`](#insn-00befad4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befae4`](#insn-00befae4) → [`00c58190`](../00c58/00c58190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58190` · 推定シンボル `None` · 推定型 `None`
- [`00befaf0`](#insn-00befaf0) → `002a5143`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00befaf4`](#insn-00befaf4) → [`00c581f0`](../00c58/00c581f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befaac`](#insn-00befaac)

~~~json
{
  "source": "00befaac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befabc`](#insn-00befabc)

~~~json
{
  "source": "00befabc",
  "target": "00c597d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befac0`](#insn-00befac0)

~~~json
{
  "source": "00befac0",
  "target": "00befae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befac4`](#insn-00befac4)

~~~json
{
  "source": "00befac4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befad4`](#insn-00befad4)

~~~json
{
  "source": "00befad4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befae4`](#insn-00befae4)

~~~json
{
  "source": "00befae4",
  "target": "00c58190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befaf0`](#insn-00befaf0)

~~~json
{
  "source": "00befaf0",
  "target": "002a5143",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a5143",
  "offset": 0,
  "size": 38,
  "datatype": "string",
  "bytes": "636c6f636b5f67657474696d6528434c4f434b5f4d4f4e4f544f4e4943292066",
  "capture_start": "002a5143",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00befaf4`](#insn-00befaf4)

~~~json
{
  "source": "00befaf4",
  "target": "00c581f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
