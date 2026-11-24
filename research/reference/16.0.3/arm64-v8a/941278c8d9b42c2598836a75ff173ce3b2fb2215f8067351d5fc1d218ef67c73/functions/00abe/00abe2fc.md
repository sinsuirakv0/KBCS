# 00abe2fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00abd308`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00abd/00abd308.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0027.md#compare-68ced3da8b4f776b0680f3f6428586b8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abe2fc",
  "name": "FUN_00abe2fc",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42294078cecab3d9c50160d6103feae2d77981b23c3bc858887ab937e16ef6b8",
  "source_text_sha256": "42294078cecab3d9c50160d6103feae2d77981b23c3bc858887ab937e16ef6b8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abe2fc",
        "00abe33f"
      ]
    ],
    "bytes_sha256": "6d3eb637c764a3d47d229e37ce453b95d5060274549fef16d8847d5a97aa5299",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0072f498](../0072f/0072f498.md)
- [0072f548](../0072f/0072f548.md)
- [0073077c](../00730/0073077c.md)
- [00731814](../00731/00731814.md)
- [00731930](../00731/00731930.md)

## 呼び出し先

- [00c594f0](../00c59/00c594f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 382 bytes

~~~c

bool FUN_00abe2fc(long param_1,wchar_t param_2)

{
  wchar_t *pwVar1;
  wchar_t *pwVar2;
  
  pwVar2 = *(wchar_t **)(param_1 + 0x38);
  pwVar1 = wmemchr(*(wchar_t **)(param_1 + 0x30),param_2,
                   (long)pwVar2 - (long)*(wchar_t **)(param_1 + 0x30) >> 2);
  if (pwVar1 != (wchar_t *)0x0) {
    pwVar2 = pwVar1;
  }
  return pwVar2 != *(wchar_t **)(param_1 + 0x38);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abe2fc"></a> `00abe2fc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00abe300"></a> `00abe300` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abe304"></a> `00abe304` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abe308"></a> `00abe308` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abe30c"></a> `00abe30c` | `00 18 40 f9` | ldr x0,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00abe310"></a> `00abe310` | `74 1e 40 f9` | ldr x20,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00abe314"></a> `00abe314` | `88 02 00 cb` | sub x8,x20,x0 | `FALL_THROUGH`
<a id="insn-00abe318"></a> `00abe318` | `02 fd 42 93` | asr x2,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00abe31c"></a> `00abe31c` | `75 6c 06 94` | bl 0x00c594f0 | `UNCONDITIONAL_CALL`
<a id="insn-00abe320"></a> `00abe320` | `68 1e 40 f9` | ldr x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00abe324"></a> `00abe324` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00abe328"></a> `00abe328` | `89 02 80 9a` | csel x9,x20,x0,eq | `FALL_THROUGH`
<a id="insn-00abe32c"></a> `00abe32c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00abe330"></a> `00abe330` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00abe334"></a> `00abe334` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abe338"></a> `00abe338` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00abe33c"></a> `00abe33c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abe2fc`](#insn-00abe2fc) 範囲 `[['00abe2fc', '00abe33f']]`

## 命令位置別の参照

- [`00abe2fc`](#insn-00abe2fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe300`](#insn-00abe300) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe31c`](#insn-00abe31c) → [`00c594f0`](../00c59/00c594f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c594f0` · 推定シンボル `None` · 推定型 `None`
- [`00abe334`](#insn-00abe334) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe338`](#insn-00abe338) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abe2fc`](#insn-00abe2fc)

~~~json
{
  "source": "00abe2fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe300`](#insn-00abe300)

~~~json
{
  "source": "00abe300",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe31c`](#insn-00abe31c)

~~~json
{
  "source": "00abe31c",
  "target": "00c594f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe334`](#insn-00abe334)

~~~json
{
  "source": "00abe334",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe338`](#insn-00abe338)

~~~json
{
  "source": "00abe338",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
