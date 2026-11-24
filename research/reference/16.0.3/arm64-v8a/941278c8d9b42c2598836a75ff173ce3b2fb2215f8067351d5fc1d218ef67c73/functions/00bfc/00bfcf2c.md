# 00bfcf2c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbf38`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbf38.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-c3c21abd0f4d9d1dcd7cb76314dc48b8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcf2c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e6968b6809ee53419275acb4760f351208442e6a48aa0152dd94a1dbde90af99",
  "source_text_sha256": "e6968b6809ee53419275acb4760f351208442e6a48aa0152dd94a1dbde90af99",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcf2c",
        "00bfcf6f"
      ]
    ],
    "bytes_sha256": "9531323984778829256113df5f4b8bd7c054a8e96b89499a99352cd295b33686",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c59290](../00c59/00c59290.md)

## 呼び出し先

- [00c5b840](../00c5b/00c5b840.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 340 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEE_00c9c8e8 + 0x10);
  _ZNSt6__ndk16localeC2Ev(param_1 + 1);
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfcf2c"></a> `00bfcf2c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcf30"></a> `00bfcf30` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfcf34"></a> `00bfcf34` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcf38"></a> `00bfcf38` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfcf3c"></a> `00bfcf3c` | `08 05 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bfcf40"></a> `00bfcf40` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfcf44"></a> `00bfcf44` | `08 75 44 f9` | ldr x8,[x8, #0x8e8] | `FALL_THROUGH`
<a id="insn-00bfcf48"></a> `00bfcf48` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bfcf4c"></a> `00bfcf4c` | `08 84 00 f8` | str x8,[x0], #0x8 | `FALL_THROUGH`
<a id="insn-00bfcf50"></a> `00bfcf50` | `3c 7a 01 94` | bl 0x00c5b840 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcf54"></a> `00bfcf54` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bfcf58"></a> `00bfcf58` | `60 02 01 ad` | stp q0,q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcf5c"></a> `00bfcf5c` | `60 06 80 3d` | str q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcf60"></a> `00bfcf60` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcf64"></a> `00bfcf64` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfcf68"></a> `00bfcf68` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfcf6c"></a> `00bfcf6c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcf2c`](#insn-00bfcf2c) 範囲 `[['00bfcf2c', '00bfcf6f']]`

## 命令位置別の参照

- [`00bfcf30`](#insn-00bfcf30) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcf34`](#insn-00bfcf34) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcf44`](#insn-00bfcf44) → `00c9c8e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfcf4c`](#insn-00bfcf4c) → `00c91d50`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00bfcf50`](#insn-00bfcf50) → [`00c5b840`](../00c5b/00c5b840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b840` · 推定シンボル `None` · 推定型 `None`
- [`00bfcf60`](#insn-00bfcf60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcf64`](#insn-00bfcf64) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcf30`](#insn-00bfcf30)

~~~json
{
  "source": "00bfcf30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcf34`](#insn-00bfcf34)

~~~json
{
  "source": "00bfcf34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcf44`](#insn-00bfcf44)

~~~json
{
  "source": "00bfcf44",
  "target": "00c9c8e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfcf4c`](#insn-00bfcf4c)

~~~json
{
  "source": "00bfcf4c",
  "target": "00c91d50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91d40",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bfcf50`](#insn-00bfcf50)

~~~json
{
  "source": "00bfcf50",
  "target": "00c5b840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcf60`](#insn-00bfcf60)

~~~json
{
  "source": "00bfcf60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcf64`](#insn-00bfcf64)

~~~json
{
  "source": "00bfcf64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
