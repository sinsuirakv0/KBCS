# 00abe7fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abe78c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abe/00abe78c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0005.md#compare-f7ec75e512dd74ebf9b45963edbbbe74)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00abf7f0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00abf/00abf7f0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-b051613330247e4e02919dfd0164cce2)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abe7fc",
  "name": "FUN_00abe7fc",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e1f99fd17e5a8044f7990a08f525f6980bb671d73b884e558cfa9d0c897d5f2",
  "source_text_sha256": "5e1f99fd17e5a8044f7990a08f525f6980bb671d73b884e558cfa9d0c897d5f2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abe7fc",
        "00abe867"
      ]
    ],
    "bytes_sha256": "5322259ef1b508f3c5b6386d6a0b8202c96dbbfde41fb55b2242436724fbc281",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006ee798](../006ee/006ee798.md)
- [006f252c](../006f2/006f252c.md)
- [00a52034](../00a52/00a52034.md)

## 呼び出し先

- [00abd080](../00abd/00abd080.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 509 bytes

~~~c

void FUN_00abe7fc(long param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  
  iVar2 = FUN_00abd080();
                    /* catch() { ... } // from try @ 00abe684 with catch @ 00abe828 */
  iVar1 = iVar2 + param_3;
  if (1999999999 < iVar2 + param_3) {
    iVar1 = 2000000000;
  }
  if (param_2 == 4) {
    *(int *)(param_1 + 0x68) = iVar1;
  }
  else if (param_2 == 1) {
    *(int *)(param_1 + 100) = iVar1;
  }
  else if (param_2 == 0) {
    *(int *)(param_1 + 0x60) = iVar1;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abe7fc"></a> `00abe7fc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00abe800"></a> `00abe800` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abe804"></a> `00abe804` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abe808"></a> `00abe808` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abe80c"></a> `00abe80c` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00abe810"></a> `00abe810` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00abe814"></a> `00abe814` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abe818"></a> `00abe818` | `1a fa ff 97` | bl 0x00abd080 | `UNCONDITIONAL_CALL`
<a id="insn-00abe81c"></a> `00abe81c` | `08 80 92 52` | mov w8,#0x9400 | `FALL_THROUGH`
<a id="insn-00abe820"></a> `00abe820` | `09 00 15 0b` | add w9,w0,w21 | `FALL_THROUGH`
<a id="insn-00abe824"></a> `00abe824` | `a8 e6 ae 72` | movk w8,#0x7735, LSL #16 | `FALL_THROUGH`
<a id="insn-00abe828"></a> `00abe828` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00abe82c"></a> `00abe82c` | `28 b1 88 1a` | csel w8,w9,w8,lt | `FALL_THROUGH`
<a id="insn-00abe830"></a> `00abe830` | `9f 12 00 71` | cmp w20,#0x4 | `FALL_THROUGH`
<a id="insn-00abe834"></a> `00abe834` | `00 01 00 54` | b.eq 0x00abe854 | `CONDITIONAL_JUMP`
<a id="insn-00abe838"></a> `00abe838` | `9f 06 00 71` | cmp w20,#0x1 | `FALL_THROUGH`
<a id="insn-00abe83c"></a> `00abe83c` | `80 00 00 54` | b.eq 0x00abe84c | `CONDITIONAL_JUMP`
<a id="insn-00abe840"></a> `00abe840` | `d4 00 00 35` | cbnz w20,0x00abe858 | `CONDITIONAL_JUMP`
<a id="insn-00abe844"></a> `00abe844` | `68 62 00 b9` | str w8,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00abe848"></a> `00abe848` | `04 00 00 14` | b 0x00abe858 | `UNCONDITIONAL_JUMP`
<a id="insn-00abe84c"></a> `00abe84c` | `68 66 00 b9` | str w8,[x19, #0x64] | `FALL_THROUGH`
<a id="insn-00abe850"></a> `00abe850` | `02 00 00 14` | b 0x00abe858 | `UNCONDITIONAL_JUMP`
<a id="insn-00abe854"></a> `00abe854` | `68 6a 00 b9` | str w8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00abe858"></a> `00abe858` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abe85c"></a> `00abe85c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abe860"></a> `00abe860` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00abe864"></a> `00abe864` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abe7fc`](#insn-00abe7fc) 範囲 `[['00abe7fc', '00abe827']]`
  - `FALL_THROUGH` [`00abe824`](#insn-00abe824) → [`00abe828`](#insn-00abe828)
- ブロック [`00abe828`](#insn-00abe828) 範囲 `[['00abe828', '00abe837']]`
  - `CONDITIONAL_JUMP` [`00abe834`](#insn-00abe834) → [`00abe854`](#insn-00abe854)
  - `FALL_THROUGH` [`00abe834`](#insn-00abe834) → [`00abe838`](#insn-00abe838)
- ブロック [`00abe838`](#insn-00abe838) 範囲 `[['00abe838', '00abe83f']]`
  - `CONDITIONAL_JUMP` [`00abe83c`](#insn-00abe83c) → [`00abe84c`](#insn-00abe84c)
  - `FALL_THROUGH` [`00abe83c`](#insn-00abe83c) → [`00abe840`](#insn-00abe840)
- ブロック [`00abe840`](#insn-00abe840) 範囲 `[['00abe840', '00abe843']]`
  - `CONDITIONAL_JUMP` [`00abe840`](#insn-00abe840) → [`00abe858`](#insn-00abe858)
  - `FALL_THROUGH` [`00abe840`](#insn-00abe840) → [`00abe844`](#insn-00abe844)
- ブロック [`00abe844`](#insn-00abe844) 範囲 `[['00abe844', '00abe84b']]`
  - `UNCONDITIONAL_JUMP` [`00abe848`](#insn-00abe848) → [`00abe858`](#insn-00abe858)
- ブロック [`00abe84c`](#insn-00abe84c) 範囲 `[['00abe84c', '00abe853']]`
  - `UNCONDITIONAL_JUMP` [`00abe850`](#insn-00abe850) → [`00abe858`](#insn-00abe858)
- ブロック [`00abe854`](#insn-00abe854) 範囲 `[['00abe854', '00abe857']]`
  - `FALL_THROUGH` [`00abe854`](#insn-00abe854) → [`00abe858`](#insn-00abe858)
- ブロック [`00abe858`](#insn-00abe858) 範囲 `[['00abe858', '00abe867']]`

## 命令位置別の参照

- [`00abe7fc`](#insn-00abe7fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe800`](#insn-00abe800) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe804`](#insn-00abe804) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe818`](#insn-00abe818) → [`00abd080`](../00abd/00abd080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00abd080` · 推定シンボル `None` · 推定型 `None`
- [`00abe834`](#insn-00abe834) → [`00abe854`](#insn-00abe854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe83c`](#insn-00abe83c) → [`00abe84c`](#insn-00abe84c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe840`](#insn-00abe840) → [`00abe858`](#insn-00abe858) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe848`](#insn-00abe848) → [`00abe858`](#insn-00abe858) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe850`](#insn-00abe850) → [`00abe858`](#insn-00abe858) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe858`](#insn-00abe858) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe85c`](#insn-00abe85c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe860`](#insn-00abe860) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abe7fc`](#insn-00abe7fc)

~~~json
{
  "source": "00abe7fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe800`](#insn-00abe800)

~~~json
{
  "source": "00abe800",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe804`](#insn-00abe804)

~~~json
{
  "source": "00abe804",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe818`](#insn-00abe818)

~~~json
{
  "source": "00abe818",
  "target": "00abd080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe834`](#insn-00abe834)

~~~json
{
  "source": "00abe834",
  "target": "00abe854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe83c`](#insn-00abe83c)

~~~json
{
  "source": "00abe83c",
  "target": "00abe84c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe840`](#insn-00abe840)

~~~json
{
  "source": "00abe840",
  "target": "00abe858",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe848`](#insn-00abe848)

~~~json
{
  "source": "00abe848",
  "target": "00abe858",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe850`](#insn-00abe850)

~~~json
{
  "source": "00abe850",
  "target": "00abe858",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe858`](#insn-00abe858)

~~~json
{
  "source": "00abe858",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe85c`](#insn-00abe85c)

~~~json
{
  "source": "00abe85c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe860`](#insn-00abe860)

~~~json
{
  "source": "00abe860",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
