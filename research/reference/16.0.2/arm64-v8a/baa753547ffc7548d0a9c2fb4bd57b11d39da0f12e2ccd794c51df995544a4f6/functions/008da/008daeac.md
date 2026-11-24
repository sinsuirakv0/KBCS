# 008daeac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008dae58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008dae58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0029.md#compare-f904a8cda02441467145e0ea17694dad)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `008dbe58`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008db/008dbe58.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0022.md#compare-abd203938290840dadf6aced25eec09b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008daeac",
  "name": "FUN_008daeac",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "940005ebf360b8202cfaa405fc2525029c9c044d2af0c41f86973b3a3db62a54",
  "source_text_sha256": "940005ebf360b8202cfaa405fc2525029c9c044d2af0c41f86973b3a3db62a54",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008daeac",
        "008daefb"
      ]
    ],
    "bytes_sha256": "10ceedb3fb004b45b07fc2458bc9d015c0e357873da47266eba8fc8d172721de",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [008d6d34](../008d6/008d6d34.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 406 bytes

~~~c

void FUN_008daeac(void *param_1)

{
  long *plVar1;
  long *plVar2;
  long lVar3;
  
  plVar1 = *(long **)((long)param_1 + 0x40);
  plVar2 = (long *)((long)param_1 + 0x20);
  if (plVar1 == plVar2) {
    lVar3 = 0x20;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_008daeec;
    lVar3 = 0x28;
    plVar2 = plVar1;
  }
  (**(code **)(*plVar2 + lVar3))();
LAB_008daeec:
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008daeac"></a> `008daeac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-008daeb0"></a> `008daeb0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008daeb4"></a> `008daeb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008daeb8"></a> `008daeb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008daebc"></a> `008daebc` | `00 20 40 f9` | ldr x0,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-008daec0"></a> `008daec0` | `69 82 00 91` | add x9,x19,#0x20 | `FALL_THROUGH`
<a id="insn-008daec4"></a> `008daec4` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-008daec8"></a> `008daec8` | `80 00 00 54` | b.eq 0x008daed8 | `CONDITIONAL_JUMP`
<a id="insn-008daecc"></a> `008daecc` | `00 01 00 b4` | cbz x0,0x008daeec | `CONDITIONAL_JUMP`
<a id="insn-008daed0"></a> `008daed0` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-008daed4"></a> `008daed4` | `03 00 00 14` | b 0x008daee0 | `UNCONDITIONAL_JUMP`
<a id="insn-008daed8"></a> `008daed8` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-008daedc"></a> `008daedc` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-008daee0"></a> `008daee0` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-008daee4"></a> `008daee4` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008daee8"></a> `008daee8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008daeec"></a> `008daeec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008daef0"></a> `008daef0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008daef4"></a> `008daef4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-008daef8"></a> `008daef8` | `22 f4 0d 14` | b 0x00c57f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008daeac`](#insn-008daeac) 範囲 `[['008daeac', '008daecb']]`
  - `CONDITIONAL_JUMP` [`008daec8`](#insn-008daec8) → [`008daed8`](#insn-008daed8)
  - `FALL_THROUGH` [`008daec8`](#insn-008daec8) → [`008daecc`](#insn-008daecc)
- ブロック [`008daecc`](#insn-008daecc) 範囲 `[['008daecc', '008daecf']]`
  - `CONDITIONAL_JUMP` [`008daecc`](#insn-008daecc) → [`008daeec`](#insn-008daeec)
  - `FALL_THROUGH` [`008daecc`](#insn-008daecc) → [`008daed0`](#insn-008daed0)
- ブロック [`008daed0`](#insn-008daed0) 範囲 `[['008daed0', '008daed7']]`
  - `UNCONDITIONAL_JUMP` [`008daed4`](#insn-008daed4) → [`008daee0`](#insn-008daee0)
- ブロック [`008daed8`](#insn-008daed8) 範囲 `[['008daed8', '008daedf']]`
  - `FALL_THROUGH` [`008daedc`](#insn-008daedc) → [`008daee0`](#insn-008daee0)
- ブロック [`008daee0`](#insn-008daee0) 範囲 `[['008daee0', '008daeeb']]`
  - `FALL_THROUGH` [`008daee8`](#insn-008daee8) → [`008daeec`](#insn-008daeec)
- ブロック [`008daeec`](#insn-008daeec) 範囲 `[['008daeec', '008daefb']]`

## 命令位置別の参照

- [`008daeac`](#insn-008daeac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daeb0`](#insn-008daeb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daec8`](#insn-008daec8) → [`008daed8`](#insn-008daed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daecc`](#insn-008daecc) → [`008daeec`](#insn-008daeec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daed4`](#insn-008daed4) → [`008daee0`](#insn-008daee0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daef0`](#insn-008daef0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daef4`](#insn-008daef4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daef8`](#insn-008daef8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008daeac`](#insn-008daeac)

~~~json
{
  "source": "008daeac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daeb0`](#insn-008daeb0)

~~~json
{
  "source": "008daeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daec8`](#insn-008daec8)

~~~json
{
  "source": "008daec8",
  "target": "008daed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daecc`](#insn-008daecc)

~~~json
{
  "source": "008daecc",
  "target": "008daeec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daed4`](#insn-008daed4)

~~~json
{
  "source": "008daed4",
  "target": "008daee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daef0`](#insn-008daef0)

~~~json
{
  "source": "008daef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daef4`](#insn-008daef4)

~~~json
{
  "source": "008daef4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daef8`](#insn-008daef8)

~~~json
{
  "source": "008daef8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
