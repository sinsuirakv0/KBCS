# 00af8edc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af8ab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8ab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-fdd5230580d7cb7b43896611853d0823)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af8f78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8f78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0036.md#compare-dfadb93fa6d9b9c951f653b3b4b85548)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af8edc",
  "name": "FUN_00af8edc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "093fc55f9e6d291bd3c8388619ccaa4e856a4b40df4937f0e3f969363af7719c",
  "source_text_sha256": "093fc55f9e6d291bd3c8388619ccaa4e856a4b40df4937f0e3f969363af7719c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af8edc",
        "00af8f1b"
      ]
    ],
    "bytes_sha256": "8b493dac4bb39971d45f767a38215334141749c765163c2177c50f1ded3b1ef6",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007102d8](../00710/007102d8.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 385 bytes

~~~c

undefined4 FUN_00af8edc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
                    /* try { // try from 00af8f08 to 00bf8f0f has its CatchHandler @ 00af9200 */
                    /* try { // try from 00af8f10 to 00bf8f43 has its CatchHandler @ 00af8cac */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8499c);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af8edc"></a> `00af8edc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af8ee0"></a> `00af8ee0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af8ee4"></a> `00af8ee4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af8ee8"></a> `00af8ee8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00af8eec"></a> `00af8eec` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00af8ef0"></a> `00af8ef0` | `82 61 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00af8ef4"></a> `00af8ef4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af8ef8"></a> `00af8ef8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af8efc"></a> `00af8efc` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af8f00"></a> `00af8f00` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00af8f04"></a> `00af8f04` | `89 33 89 52` | mov w9,#0x499c | `FALL_THROUGH`
<a id="insn-00af8f08"></a> `00af8f08` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af8f0c"></a> `00af8f0c` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af8f10"></a> `00af8f10` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af8f14"></a> `00af8f14` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af8f18"></a> `00af8f18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af8edc`](#insn-00af8edc) 範囲 `[['00af8edc', '00af8f07']]`
  - `FALL_THROUGH` [`00af8f04`](#insn-00af8f04) → [`00af8f08`](#insn-00af8f08)
- ブロック [`00af8f08`](#insn-00af8f08) 範囲 `[['00af8f08', '00af8f0f']]`
  - `FALL_THROUGH` [`00af8f0c`](#insn-00af8f0c) → [`00af8f10`](#insn-00af8f10)
- ブロック [`00af8f10`](#insn-00af8f10) 範囲 `[['00af8f10', '00af8f1b']]`

## 命令位置別の参照

- [`00af8edc`](#insn-00af8edc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8ee0`](#insn-00af8ee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8ef0`](#insn-00af8ef0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00af8f10`](#insn-00af8f10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8f14`](#insn-00af8f14) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af8edc`](#insn-00af8edc)

~~~json
{
  "source": "00af8edc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8ee0`](#insn-00af8ee0)

~~~json
{
  "source": "00af8ee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8ef0`](#insn-00af8ef0)

~~~json
{
  "source": "00af8ef0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af8f10`](#insn-00af8f10)

~~~json
{
  "source": "00af8f10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8f14`](#insn-00af8f14)

~~~json
{
  "source": "00af8f14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
