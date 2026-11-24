# 00bfafd8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfaf3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaf3c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0011.md#compare-dc391372d390537c1ceb297eb0003719)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfbfcc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbfcc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0011.md#compare-9a8f40e8be56728e95a1de9f16f0415d)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfafd8",
  "name": "_ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c31b556accdabe0af91f8fa2f56ba22ac5caa64446adca4529bd358f643c60eb",
  "source_text_sha256": "c31b556accdabe0af91f8fa2f56ba22ac5caa64446adca4529bd358f643c60eb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfafd8",
        "00bfb017"
      ]
    ],
    "bytes_sha256": "c4b5b7b0ac4e621970c6eb97d104afc1ab7c8f09def5e80007bc64caa785a68d",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e220](../00c5e/00c5e220.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 437 bytes

~~~c

void _ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE
               (long *param_1,undefined8 param_2,undefined8 *param_3)

{
  _ZNSt6__ndk112system_errorC2ENS_10error_codeERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
            (param_1,*param_3,param_3[1],param_2);
  *param_1 = (long)(PTR__ZTVNSt6__ndk18ios_base7failureE_00c9bbb8 + 0x10);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfafd8"></a> `00bfafd8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfafdc"></a> `00bfafdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfafe0"></a> `00bfafe0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfafe4"></a> `00bfafe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfafe8"></a> `00bfafe8` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bfafec"></a> `00bfafec` | `41 08 40 a9` | ldp x1,x2,[x2] | `FALL_THROUGH`
<a id="insn-00bfaff0"></a> `00bfaff0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfaff4"></a> `00bfaff4` | `8b 8c 01 94` | bl 0x00c5e220 | `UNCONDITIONAL_CALL`
<a id="insn-00bfaff8"></a> `00bfaff8` | `08 05 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfaffc"></a> `00bfaffc` | `08 dd 45 f9` | ldr x8,[x8, #0xbb8] | `FALL_THROUGH`
<a id="insn-00bfb000"></a> `00bfb000` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bfb004"></a> `00bfb004` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfb008"></a> `00bfb008` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb00c"></a> `00bfb00c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfb010"></a> `00bfb010` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb014"></a> `00bfb014` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfafd8`](#insn-00bfafd8) 範囲 `[['00bfafd8', '00bfb017']]`

## 命令位置別の参照

- [`00bfafdc`](#insn-00bfafdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfafe0`](#insn-00bfafe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaff4`](#insn-00bfaff4) → [`00c5e220`](../00c5e/00c5e220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e220` · 推定シンボル `None` · 推定型 `None`
- [`00bfaffc`](#insn-00bfaffc) → `00c9bbb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfb004`](#insn-00bfb004) → `00c92e50`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bfb008`](#insn-00bfb008) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb00c`](#insn-00bfb00c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfafdc`](#insn-00bfafdc)

~~~json
{
  "source": "00bfafdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfafe0`](#insn-00bfafe0)

~~~json
{
  "source": "00bfafe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaff4`](#insn-00bfaff4)

~~~json
{
  "source": "00bfaff4",
  "target": "00c5e220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfaffc`](#insn-00bfaffc)

~~~json
{
  "source": "00bfaffc",
  "target": "00c9bbb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bbb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfb004`](#insn-00bfb004)

~~~json
{
  "source": "00bfb004",
  "target": "00c92e50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92e40",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bfb008`](#insn-00bfb008)

~~~json
{
  "source": "00bfb008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb00c`](#insn-00bfb00c)

~~~json
{
  "source": "00bfb00c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
