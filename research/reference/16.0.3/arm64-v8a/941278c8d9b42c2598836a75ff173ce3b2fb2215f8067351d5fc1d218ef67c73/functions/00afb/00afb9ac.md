# 00afb9ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afa9b8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa9b8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-8412ca6f7ea5c970b1cffb29ed46f403)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb9ac",
  "name": "FUN_00afb9ac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5b318924ebcfb257dd54c1c65a9b436509c605d2802e5319cf2bae6e9237746",
  "source_text_sha256": "c5b318924ebcfb257dd54c1c65a9b436509c605d2802e5319cf2bae6e9237746",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb9ac",
        "00afb9eb"
      ]
    ],
    "bytes_sha256": "db449ab551c058a4d6e8676e9452a642551d7644b41366e78aa959533216c5fc",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0071412c](../00714/0071412c.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 452 bytes

~~~c

undefined4 FUN_00afb9ac(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afb1c8 with catch @ 00afb9cc */
                    /* catch() { ... } // from try @ 00afb138 with catch @ 00afb9d0 */
                    /* catch() { ... } // from try @ 00afb8c8 with catch @ 00afb9d8 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ca0);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afb9ac"></a> `00afb9ac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afb9b0"></a> `00afb9b0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb9b4"></a> `00afb9b4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afb9b8"></a> `00afb9b8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afb9bc"></a> `00afb9bc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afb9c0"></a> `00afb9c0` | `cf 5a f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afb9c4"></a> `00afb9c4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afb9c8"></a> `00afb9c8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afb9cc"></a> `00afb9cc` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afb9d0"></a> `00afb9d0` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afb9d4"></a> `00afb9d4` | `09 94 89 52` | mov w9,#0x4ca0 | `FALL_THROUGH`
<a id="insn-00afb9d8"></a> `00afb9d8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb9dc"></a> `00afb9dc` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb9e0"></a> `00afb9e0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb9e4"></a> `00afb9e4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afb9e8"></a> `00afb9e8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb9ac`](#insn-00afb9ac) 範囲 `[['00afb9ac', '00afb9cb']]`
  - `FALL_THROUGH` [`00afb9c8`](#insn-00afb9c8) → [`00afb9cc`](#insn-00afb9cc)
- ブロック [`00afb9cc`](#insn-00afb9cc) 範囲 `[['00afb9cc', '00afb9cf']]`
  - `FALL_THROUGH` [`00afb9cc`](#insn-00afb9cc) → [`00afb9d0`](#insn-00afb9d0)
- ブロック [`00afb9d0`](#insn-00afb9d0) 範囲 `[['00afb9d0', '00afb9d7']]`
  - `FALL_THROUGH` [`00afb9d4`](#insn-00afb9d4) → [`00afb9d8`](#insn-00afb9d8)
- ブロック [`00afb9d8`](#insn-00afb9d8) 範囲 `[['00afb9d8', '00afb9eb']]`

## 命令位置別の参照

- [`00afb9ac`](#insn-00afb9ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb9b0`](#insn-00afb9b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb9c0`](#insn-00afb9c0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afb9e0`](#insn-00afb9e0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb9e4`](#insn-00afb9e4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb9ac`](#insn-00afb9ac)

~~~json
{
  "source": "00afb9ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb9b0`](#insn-00afb9b0)

~~~json
{
  "source": "00afb9b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb9c0`](#insn-00afb9c0)

~~~json
{
  "source": "00afb9c0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb9e0`](#insn-00afb9e0)

~~~json
{
  "source": "00afb9e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb9e4`](#insn-00afb9e4)

~~~json
{
  "source": "00afb9e4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
