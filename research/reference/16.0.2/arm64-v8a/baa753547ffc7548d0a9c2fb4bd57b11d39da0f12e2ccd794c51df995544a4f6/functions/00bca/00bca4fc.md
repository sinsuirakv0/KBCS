# 00bca4fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bca460`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca460.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-9ebbac5c584d0997e191ebb22d83d3b1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcb4f0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb4f0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-87c369bde74121c05c210ea0c8aab605)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bca4fc",
  "name": "_ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42dc68417f42122a5e1333b86d12283d26c0a14534288f0d5b3861bb373a807b",
  "source_text_sha256": "42dc68417f42122a5e1333b86d12283d26c0a14534288f0d5b3861bb373a807b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bca4fc",
        "00bca53b"
      ]
    ],
    "bytes_sha256": "55266fe8ea0f383aef181510845a5cf4ebf94ef9387aff6d375fd30288960a4c",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5d740](../00c5d/00c5d740.md)

## 呼び出し先

- [00b611c8](../00b61/00b611c8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 618 bytes

~~~c

void _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv
               (long param_1)

{
  long *plVar1;
  
  if (*(char *)(param_1 + 0x40) != '\0') {
    return;
  }
  plVar1 = *(long **)(param_1 + 0x30);
  *(undefined1 *)(param_1 + 0x40) = 1;
  if (plVar1 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00bca534. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*plVar1 + 0x30))(plVar1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00b611c8();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bca4fc"></a> `00bca4fc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bca500"></a> `00bca500` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bca504"></a> `00bca504` | `08 00 41 39` | ldrb w8,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bca508"></a> `00bca508` | `68 00 00 34` | cbz w8,0x00bca514 | `CONDITIONAL_JUMP`
<a id="insn-00bca50c"></a> `00bca50c` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bca510"></a> `00bca510` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bca514"></a> `00bca514` | `08 18 40 f9` | ldr x8,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bca518"></a> `00bca518` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bca51c"></a> `00bca51c` | `09 00 01 39` | strb w9,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bca520"></a> `00bca520` | `c8 00 00 b4` | cbz x8,0x00bca538 | `CONDITIONAL_JUMP`
<a id="insn-00bca524"></a> `00bca524` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bca528"></a> `00bca528` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bca52c"></a> `00bca52c` | `21 19 40 f9` | ldr x1,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00bca530"></a> `00bca530` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bca534"></a> `00bca534` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bca538"></a> `00bca538` | `24 5b fe 97` | bl 0x00b611c8 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bca4fc`](#insn-00bca4fc) 範囲 `[['00bca4fc', '00bca50b']]`
  - `CONDITIONAL_JUMP` [`00bca508`](#insn-00bca508) → [`00bca514`](#insn-00bca514)
  - `FALL_THROUGH` [`00bca508`](#insn-00bca508) → [`00bca50c`](#insn-00bca50c)
- ブロック [`00bca50c`](#insn-00bca50c) 範囲 `[['00bca50c', '00bca513']]`
- ブロック [`00bca514`](#insn-00bca514) 範囲 `[['00bca514', '00bca523']]`
  - `CONDITIONAL_JUMP` [`00bca520`](#insn-00bca520) → [`00bca538`](#insn-00bca538)
  - `FALL_THROUGH` [`00bca520`](#insn-00bca520) → [`00bca524`](#insn-00bca524)
- ブロック [`00bca524`](#insn-00bca524) 範囲 `[['00bca524', '00bca537']]`
- ブロック [`00bca538`](#insn-00bca538) 範囲 `[['00bca538', '00bca53b']]`

## 命令位置別の参照

- [`00bca4fc`](#insn-00bca4fc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca508`](#insn-00bca508) → [`00bca514`](#insn-00bca514) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca50c`](#insn-00bca50c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca520`](#insn-00bca520) → [`00bca538`](#insn-00bca538) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca530`](#insn-00bca530) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca538`](#insn-00bca538) → [`00b611c8`](../00b61/00b611c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b611c8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bca4fc`](#insn-00bca4fc)

~~~json
{
  "source": "00bca4fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca508`](#insn-00bca508)

~~~json
{
  "source": "00bca508",
  "target": "00bca514",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca50c`](#insn-00bca50c)

~~~json
{
  "source": "00bca50c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca520`](#insn-00bca520)

~~~json
{
  "source": "00bca520",
  "target": "00bca538",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca530`](#insn-00bca530)

~~~json
{
  "source": "00bca530",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca538`](#insn-00bca538)

~~~json
{
  "source": "00bca538",
  "target": "00b611c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
