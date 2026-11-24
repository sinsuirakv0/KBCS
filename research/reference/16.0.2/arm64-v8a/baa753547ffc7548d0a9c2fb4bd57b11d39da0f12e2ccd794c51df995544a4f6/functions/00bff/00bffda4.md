# 00bffda4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffd08`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffd08.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0087.md#compare-15fca007f9567e4b6452c573bda7d999)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c00d98`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00d98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-222d64f0ed90b05337711f24a76b946a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffda4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC2Ev",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c38ade80ac5501d07f0d776ae1dc148d1b5ac19309eabed0f5219de363fb15b7",
  "source_text_sha256": "c38ade80ac5501d07f0d776ae1dc148d1b5ac19309eabed0f5219de363fb15b7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffda4",
        "00bffde7"
      ]
    ],
    "bytes_sha256": "b51145198c08a8092697975285b870dc35c11fb693beb4d40f3d0ef25a2c6a37",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e4b0](../00c5e/00c5e4b0.md)

## 呼び出し先

- [00c5a870](../00c5a/00c5a870.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 340 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC2Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEE_00c9bc00 + 0x10);
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
<a id="insn-00bffda4"></a> `00bffda4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffda8"></a> `00bffda8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bffdac"></a> `00bffdac` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffdb0"></a> `00bffdb0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bffdb4"></a> `00bffdb4` | `e8 04 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bffdb8"></a> `00bffdb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bffdbc"></a> `00bffdbc` | `08 01 46 f9` | ldr x8,[x8, #0xc00] | `FALL_THROUGH`
<a id="insn-00bffdc0"></a> `00bffdc0` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bffdc4"></a> `00bffdc4` | `08 84 00 f8` | str x8,[x0], #0x8 | `FALL_THROUGH`
<a id="insn-00bffdc8"></a> `00bffdc8` | `aa 6a 01 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bffdcc"></a> `00bffdcc` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bffdd0"></a> `00bffdd0` | `60 02 01 ad` | stp q0,q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bffdd4"></a> `00bffdd4` | `60 06 80 3d` | str q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bffdd8"></a> `00bffdd8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffddc"></a> `00bffddc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bffde0"></a> `00bffde0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffde4"></a> `00bffde4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffda4`](#insn-00bffda4) 範囲 `[['00bffda4', '00bffde7']]`

## 命令位置別の参照

- [`00bffda8`](#insn-00bffda8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffdac`](#insn-00bffdac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffdbc`](#insn-00bffdbc) → `00c9bc00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bffdc4`](#insn-00bffdc4) → `00c93048`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00bffdc8`](#insn-00bffdc8) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bffdd8`](#insn-00bffdd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffddc`](#insn-00bffddc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffda8`](#insn-00bffda8)

~~~json
{
  "source": "00bffda8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffdac`](#insn-00bffdac)

~~~json
{
  "source": "00bffdac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffdbc`](#insn-00bffdbc)

~~~json
{
  "source": "00bffdbc",
  "target": "00c9bc00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bffdc4`](#insn-00bffdc4)

~~~json
{
  "source": "00bffdc4",
  "target": "00c93048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93038",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bffdc8`](#insn-00bffdc8)

~~~json
{
  "source": "00bffdc8",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffdd8`](#insn-00bffdd8)

~~~json
{
  "source": "00bffdd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffddc`](#insn-00bffddc)

~~~json
{
  "source": "00bffddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
