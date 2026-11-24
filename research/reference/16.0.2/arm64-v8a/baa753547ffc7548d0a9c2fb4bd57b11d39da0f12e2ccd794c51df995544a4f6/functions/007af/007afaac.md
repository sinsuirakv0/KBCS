# 007afaac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `007afa54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afa54.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0039.md#compare-95170b49b11c624c441647fb2fb8da78)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `007b04d0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007b0/007b04d0.md) · 移動量 `+0xa24`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0040.md#compare-1665ff2e54345f862eaffc2050c10a66)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007afaac",
  "name": "FUN_007afaac",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db8ba7870a5ddb9145b5c0446aeeb519e04ebb0b2630c5815379806e885a79e5",
  "source_text_sha256": "db8ba7870a5ddb9145b5c0446aeeb519e04ebb0b2630c5815379806e885a79e5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007afaac",
        "007afb07"
      ]
    ],
    "bytes_sha256": "31195277777bb2d5912295a8c97399c3d3308a37704ad1f065b0a42ae5b605ab",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_007afaac(undefined8 *param_1)

{
  long *plVar1;
  long *plVar2;
  long lVar3;
  
  plVar1 = (long *)param_1[6];
  plVar2 = param_1 + 2;
  *param_1 = &PTR_FUN_00c7aa68;
  if (plVar1 == plVar2) {
    lVar3 = 0x20;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_007afaf8;
    lVar3 = 0x28;
    plVar2 = plVar1;
  }
  (**(code **)(*plVar2 + lVar3))();
LAB_007afaf8:
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007afaac"></a> `007afaac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007afab0"></a> `007afab0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007afab4"></a> `007afab4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007afab8"></a> `007afab8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007afabc"></a> `007afabc` | `00 18 40 f9` | ldr x0,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-007afac0"></a> `007afac0` | `48 26 00 f0` | adrp x8,0xc7a000 | `FALL_THROUGH`
<a id="insn-007afac4"></a> `007afac4` | `08 a1 29 91` | add x8,x8,#0xa68 | `FALL_THROUGH`
<a id="insn-007afac8"></a> `007afac8` | `69 42 00 91` | add x9,x19,#0x10 | `FALL_THROUGH`
<a id="insn-007afacc"></a> `007afacc` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-007afad0"></a> `007afad0` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-007afad4"></a> `007afad4` | `80 00 00 54` | b.eq 0x007afae4 | `CONDITIONAL_JUMP`
<a id="insn-007afad8"></a> `007afad8` | `00 01 00 b4` | cbz x0,0x007afaf8 | `CONDITIONAL_JUMP`
<a id="insn-007afadc"></a> `007afadc` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-007afae0"></a> `007afae0` | `03 00 00 14` | b 0x007afaec | `UNCONDITIONAL_JUMP`
<a id="insn-007afae4"></a> `007afae4` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-007afae8"></a> `007afae8` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-007afaec"></a> `007afaec` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-007afaf0"></a> `007afaf0` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007afaf4"></a> `007afaf4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007afaf8"></a> `007afaf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007afafc"></a> `007afafc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007afb00"></a> `007afb00` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007afb04"></a> `007afb04` | `1f a1 12 14` | b 0x00c57f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007afaac`](#insn-007afaac) 範囲 `[['007afaac', '007afad7']]`
  - `CONDITIONAL_JUMP` [`007afad4`](#insn-007afad4) → [`007afae4`](#insn-007afae4)
  - `FALL_THROUGH` [`007afad4`](#insn-007afad4) → [`007afad8`](#insn-007afad8)
- ブロック [`007afad8`](#insn-007afad8) 範囲 `[['007afad8', '007afadb']]`
  - `CONDITIONAL_JUMP` [`007afad8`](#insn-007afad8) → [`007afaf8`](#insn-007afaf8)
  - `FALL_THROUGH` [`007afad8`](#insn-007afad8) → [`007afadc`](#insn-007afadc)
- ブロック [`007afadc`](#insn-007afadc) 範囲 `[['007afadc', '007afae3']]`
  - `UNCONDITIONAL_JUMP` [`007afae0`](#insn-007afae0) → [`007afaec`](#insn-007afaec)
- ブロック [`007afae4`](#insn-007afae4) 範囲 `[['007afae4', '007afaeb']]`
  - `FALL_THROUGH` [`007afae8`](#insn-007afae8) → [`007afaec`](#insn-007afaec)
- ブロック [`007afaec`](#insn-007afaec) 範囲 `[['007afaec', '007afaf7']]`
  - `FALL_THROUGH` [`007afaf4`](#insn-007afaf4) → [`007afaf8`](#insn-007afaf8)
- ブロック [`007afaf8`](#insn-007afaf8) 範囲 `[['007afaf8', '007afb07']]`

## 命令位置別の参照

- [`007afaac`](#insn-007afaac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afab0`](#insn-007afab0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afad0`](#insn-007afad0) → `00c7aa68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007afad4`](#insn-007afad4) → [`007afae4`](#insn-007afae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afad8`](#insn-007afad8) → [`007afaf8`](#insn-007afaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afae0`](#insn-007afae0) → [`007afaec`](#insn-007afaec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afafc`](#insn-007afafc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afb00`](#insn-007afb00) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afb04`](#insn-007afb04) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007afaac`](#insn-007afaac)

~~~json
{
  "source": "007afaac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afab0`](#insn-007afab0)

~~~json
{
  "source": "007afab0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afad0`](#insn-007afad0)

~~~json
{
  "source": "007afad0",
  "target": "00c7aa68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7aa68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007afad4`](#insn-007afad4)

~~~json
{
  "source": "007afad4",
  "target": "007afae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afad8`](#insn-007afad8)

~~~json
{
  "source": "007afad8",
  "target": "007afaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afae0`](#insn-007afae0)

~~~json
{
  "source": "007afae0",
  "target": "007afaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afafc`](#insn-007afafc)

~~~json
{
  "source": "007afafc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afb00`](#insn-007afb00)

~~~json
{
  "source": "007afb00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afb04`](#insn-007afb04)

~~~json
{
  "source": "007afb04",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
