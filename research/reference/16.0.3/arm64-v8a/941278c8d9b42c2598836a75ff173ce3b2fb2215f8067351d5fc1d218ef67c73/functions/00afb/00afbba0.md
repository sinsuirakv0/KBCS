# 00afbba0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afabac`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afabac.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-e005517c49dcf4af1b59a57902d59908)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbba0",
  "name": "FUN_00afbba0",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "efd86632ff69ed9d592df1539c26b8c5b82e630b34e2c8182b7ecc4df932351d",
  "source_text_sha256": "efd86632ff69ed9d592df1539c26b8c5b82e630b34e2c8182b7ecc4df932351d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbba0",
        "00afbbeb"
      ]
    ],
    "bytes_sha256": "a59b9aa6babd26ca4e933a9651d0a67b0f4b14c2eebe3f826d10deae9980869e",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 978 bytes

~~~c

void FUN_00afbba0(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afbbcc to 00bfbc67 has its CatchHandler @ 00afbbcc
                       catch() { ... } // from try @ 00afbbcc with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afbc80 with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afbd40 with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afbe0c with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afbfa8 with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afbff8 with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afc0a4 with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afc180 with catch @ 00afbbcc */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a24) = param_3 & 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbba0"></a> `00afbba0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afbba4"></a> `00afbba4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbba8"></a> `00afbba8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbbac"></a> `00afbbac` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afbbb0"></a> `00afbbb0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afbbb4"></a> `00afbbb4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afbbb8"></a> `00afbbb8` | `55 00 00 12` | and w21,w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afbbbc"></a> `00afbbbc` | `50 5a f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afbbc0"></a> `00afbbc0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afbbc4"></a> `00afbbc4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afbbc8"></a> `00afbbc8` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afbbcc"></a> `00afbbcc` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afbbd0"></a> `00afbbd0` | `89 44 89 52` | mov w9,#0x4a24 | `FALL_THROUGH`
<a id="insn-00afbbd4"></a> `00afbbd4` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afbbd8"></a> `00afbbd8` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afbbdc"></a> `00afbbdc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbbe0"></a> `00afbbe0` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbbe4"></a> `00afbbe4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afbbe8"></a> `00afbbe8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbba0`](#insn-00afbba0) 範囲 `[['00afbba0', '00afbbcb']]`
  - `FALL_THROUGH` [`00afbbc8`](#insn-00afbbc8) → [`00afbbcc`](#insn-00afbbcc)
- ブロック [`00afbbcc`](#insn-00afbbcc) 範囲 `[['00afbbcc', '00afbbeb']]`

## 命令位置別の参照

- [`00afbba0`](#insn-00afbba0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbba4`](#insn-00afbba4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbba8`](#insn-00afbba8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbbbc`](#insn-00afbbbc) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afbbdc`](#insn-00afbbdc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbbe0`](#insn-00afbbe0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbbe4`](#insn-00afbbe4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbba0`](#insn-00afbba0)

~~~json
{
  "source": "00afbba0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbba4`](#insn-00afbba4)

~~~json
{
  "source": "00afbba4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbba8`](#insn-00afbba8)

~~~json
{
  "source": "00afbba8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbbbc`](#insn-00afbbbc)

~~~json
{
  "source": "00afbbbc",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbbdc`](#insn-00afbbdc)

~~~json
{
  "source": "00afbbdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbbe0`](#insn-00afbbe0)

~~~json
{
  "source": "00afbbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbbe4`](#insn-00afbbe4)

~~~json
{
  "source": "00afbbe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
