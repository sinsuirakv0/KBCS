# 00afaddc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9de8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9de8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0006.md#compare-aaa17509ac785fdf524fad1be655bae6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaddc",
  "name": "FUN_00afaddc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c662995c24288112bd9009ff3b1642f402a918aececf5a66d4813b29107a4846",
  "source_text_sha256": "c662995c24288112bd9009ff3b1642f402a918aececf5a66d4813b29107a4846",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaddc",
        "00afae4b"
      ]
    ],
    "bytes_sha256": "001056db5d8b5a48832ddab666de79338e7790acfd002180db1bd739c06527e2",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 542 bytes

~~~c

void FUN_00afaddc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
    lVar1 = FUN_008524fc();
    *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a80) = param_3 & 1;
  }
                    /* try { // try from 00afae40 to 00bfae43 has its CatchHandler @ 00afaeb4 */
                    /* try { // try from 00afae44 to 00bfaedf has its CatchHandler @ 00afad10 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaddc"></a> `00afaddc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afade0"></a> `00afade0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afade4"></a> `00afade4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afade8"></a> `00afade8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afadec"></a> `00afadec` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00afadf0"></a> `00afadf0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afadf4"></a> `00afadf4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afadf8"></a> `00afadf8` | `c1 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afadfc"></a> `00afadfc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afae00"></a> `00afae00` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afae04"></a> `00afae04` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afae08"></a> `00afae08` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afae0c"></a> `00afae0c` | `81 b2 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afae10"></a> `00afae10` | `60 01 00 36` | tbz w0,#0x0,0x00afae3c | `CONDITIONAL_JUMP`
<a id="insn-00afae14"></a> `00afae14` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afae18"></a> `00afae18` | `94 02 00 12` | and w20,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00afae1c"></a> `00afae1c` | `b8 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afae20"></a> `00afae20` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afae24"></a> `00afae24` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afae28"></a> `00afae28` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afae2c"></a> `00afae2c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afae30"></a> `00afae30` | `09 50 89 52` | mov w9,#0x4a80 | `FALL_THROUGH`
<a id="insn-00afae34"></a> `00afae34` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afae38"></a> `00afae38` | `14 69 29 b8` | str w20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afae3c"></a> `00afae3c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afae40"></a> `00afae40` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afae44"></a> `00afae44` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afae48"></a> `00afae48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaddc`](#insn-00afaddc) 範囲 `[['00afaddc', '00afae13']]`
  - `CONDITIONAL_JUMP` [`00afae10`](#insn-00afae10) → [`00afae3c`](#insn-00afae3c)
  - `FALL_THROUGH` [`00afae10`](#insn-00afae10) → [`00afae14`](#insn-00afae14)
- ブロック [`00afae14`](#insn-00afae14) 範囲 `[['00afae14', '00afae3b']]`
  - `FALL_THROUGH` [`00afae38`](#insn-00afae38) → [`00afae3c`](#insn-00afae3c)
- ブロック [`00afae3c`](#insn-00afae3c) 範囲 `[['00afae3c', '00afae3f']]`
  - `FALL_THROUGH` [`00afae3c`](#insn-00afae3c) → [`00afae40`](#insn-00afae40)
- ブロック [`00afae40`](#insn-00afae40) 範囲 `[['00afae40', '00afae43']]`
  - `FALL_THROUGH` [`00afae40`](#insn-00afae40) → [`00afae44`](#insn-00afae44)
- ブロック [`00afae44`](#insn-00afae44) 範囲 `[['00afae44', '00afae4b']]`

## 命令位置別の参照

- [`00afaddc`](#insn-00afaddc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afade0`](#insn-00afade0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afade4`](#insn-00afade4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadf8`](#insn-00afadf8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afae0c`](#insn-00afae0c) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afae10`](#insn-00afae10) → [`00afae3c`](#insn-00afae3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae1c`](#insn-00afae1c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afae3c`](#insn-00afae3c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae40`](#insn-00afae40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae44`](#insn-00afae44) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaddc`](#insn-00afaddc)

~~~json
{
  "source": "00afaddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afade0`](#insn-00afade0)

~~~json
{
  "source": "00afade0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afade4`](#insn-00afade4)

~~~json
{
  "source": "00afade4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadf8`](#insn-00afadf8)

~~~json
{
  "source": "00afadf8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae0c`](#insn-00afae0c)

~~~json
{
  "source": "00afae0c",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae10`](#insn-00afae10)

~~~json
{
  "source": "00afae10",
  "target": "00afae3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae1c`](#insn-00afae1c)

~~~json
{
  "source": "00afae1c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae3c`](#insn-00afae3c)

~~~json
{
  "source": "00afae3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae40`](#insn-00afae40)

~~~json
{
  "source": "00afae40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae44`](#insn-00afae44)

~~~json
{
  "source": "00afae44",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
