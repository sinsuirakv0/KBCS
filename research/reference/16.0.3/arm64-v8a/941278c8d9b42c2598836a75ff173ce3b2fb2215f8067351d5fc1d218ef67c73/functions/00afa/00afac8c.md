# 00afac8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9c98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9c98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-12622b219ec35ea407b93199e17233bd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afac8c",
  "name": "FUN_00afac8c",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "590cf423cbb1cc908154c8580d8c1813059da794dc47bfcc72211bb3ea432de6",
  "source_text_sha256": "590cf423cbb1cc908154c8580d8c1813059da794dc47bfcc72211bb3ea432de6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afac8c",
        "00afacfb"
      ]
    ],
    "bytes_sha256": "0e6604cd5efb2b70b0d636e7a24ba05907387d7ae4bb03ca9ea6789badbd9ff8",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070ee64](../0070e/0070ee64.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 907 bytes

~~~c

bool FUN_00afac8c(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
                    /* catch() { ... } // from try @ 00afaa68 with catch @ 00afac94 */
  lVar2 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afaa98 with catch @ 00afacac */
                    /* catch() { ... } // from try @ 00afa9f0 with catch @ 00afacb0 */
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
                    /* catch() { ... } // from try @ 00afaa50 with catch @ 00afacc0 */
  }
  else {
                    /* catch() { ... } // from try @ 00afaa34 with catch @ 00afacc4 */
                    /* catch() { ... } // from try @ 00afa9d4 with catch @ 00afacc8 */
    lVar2 = FUN_008524fc();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a78) != 0;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afac8c"></a> `00afac8c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afac90"></a> `00afac90` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afac94"></a> `00afac94` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afac98"></a> `00afac98` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afac9c"></a> `00afac9c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afaca0"></a> `00afaca0` | `17 5e f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afaca4"></a> `00afaca4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afaca8"></a> `00afaca8` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afacac"></a> `00afacac` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afacb0"></a> `00afacb0` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afacb4"></a> `00afacb4` | `d7 b2 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afacb8"></a> `00afacb8` | `60 00 00 37` | tbnz w0,#0x0,0x00afacc4 | `CONDITIONAL_JUMP`
<a id="insn-00afacbc"></a> `00afacbc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afacc0"></a> `00afacc0` | `0c 00 00 14` | b 0x00afacf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afacc4"></a> `00afacc4` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00afacc8"></a> `00afacc8` | `0d 5e f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afaccc"></a> `00afaccc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afacd0"></a> `00afacd0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afacd4"></a> `00afacd4` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afacd8"></a> `00afacd8` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afacdc"></a> `00afacdc` | `09 4f 89 52` | mov w9,#0x4a78 | `FALL_THROUGH`
<a id="insn-00aface0"></a> `00aface0` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00aface4"></a> `00aface4` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aface8"></a> `00aface8` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afacec"></a> `00afacec` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afacf0"></a> `00afacf0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afacf4"></a> `00afacf4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afacf8"></a> `00afacf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afac8c`](#insn-00afac8c) 範囲 `[['00afac8c', '00afac93']]`
  - `FALL_THROUGH` [`00afac90`](#insn-00afac90) → [`00afac94`](#insn-00afac94)
- ブロック [`00afac94`](#insn-00afac94) 範囲 `[['00afac94', '00afacab']]`
  - `FALL_THROUGH` [`00afaca8`](#insn-00afaca8) → [`00afacac`](#insn-00afacac)
- ブロック [`00afacac`](#insn-00afacac) 範囲 `[['00afacac', '00afacaf']]`
  - `FALL_THROUGH` [`00afacac`](#insn-00afacac) → [`00afacb0`](#insn-00afacb0)
- ブロック [`00afacb0`](#insn-00afacb0) 範囲 `[['00afacb0', '00afacbb']]`
  - `CONDITIONAL_JUMP` [`00afacb8`](#insn-00afacb8) → [`00afacc4`](#insn-00afacc4)
  - `FALL_THROUGH` [`00afacb8`](#insn-00afacb8) → [`00afacbc`](#insn-00afacbc)
- ブロック [`00afacbc`](#insn-00afacbc) 範囲 `[['00afacbc', '00afacbf']]`
  - `FALL_THROUGH` [`00afacbc`](#insn-00afacbc) → [`00afacc0`](#insn-00afacc0)
- ブロック [`00afacc0`](#insn-00afacc0) 範囲 `[['00afacc0', '00afacc3']]`
  - `UNCONDITIONAL_JUMP` [`00afacc0`](#insn-00afacc0) → [`00afacf0`](#insn-00afacf0)
- ブロック [`00afacc4`](#insn-00afacc4) 範囲 `[['00afacc4', '00afacc7']]`
  - `FALL_THROUGH` [`00afacc4`](#insn-00afacc4) → [`00afacc8`](#insn-00afacc8)
- ブロック [`00afacc8`](#insn-00afacc8) 範囲 `[['00afacc8', '00afacef']]`
  - `FALL_THROUGH` [`00afacec`](#insn-00afacec) → [`00afacf0`](#insn-00afacf0)
- ブロック [`00afacf0`](#insn-00afacf0) 範囲 `[['00afacf0', '00afacfb']]`

## 命令位置別の参照

- [`00afac8c`](#insn-00afac8c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac90`](#insn-00afac90) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaca0`](#insn-00afaca0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afacb4`](#insn-00afacb4) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afacb8`](#insn-00afacb8) → [`00afacc4`](#insn-00afacc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacc0`](#insn-00afacc0) → [`00afacf0`](#insn-00afacf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacc8`](#insn-00afacc8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afacf0`](#insn-00afacf0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacf4`](#insn-00afacf4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afac8c`](#insn-00afac8c)

~~~json
{
  "source": "00afac8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac90`](#insn-00afac90)

~~~json
{
  "source": "00afac90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaca0`](#insn-00afaca0)

~~~json
{
  "source": "00afaca0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afacb4`](#insn-00afacb4)

~~~json
{
  "source": "00afacb4",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afacb8`](#insn-00afacb8)

~~~json
{
  "source": "00afacb8",
  "target": "00afacc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacc0`](#insn-00afacc0)

~~~json
{
  "source": "00afacc0",
  "target": "00afacf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacc8`](#insn-00afacc8)

~~~json
{
  "source": "00afacc8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afacf0`](#insn-00afacf0)

~~~json
{
  "source": "00afacf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacf4`](#insn-00afacf4)

~~~json
{
  "source": "00afacf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
