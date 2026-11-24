# 00afdbc4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afcbd0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afcbd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-3a3ead16d6eaff533366423327197136)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afdbc4",
  "name": "FUN_00afdbc4",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8596dd132e5f6692774df78ab1b1168e433a802692a80b82e12db141ec15ce8f",
  "source_text_sha256": "8596dd132e5f6692774df78ab1b1168e433a802692a80b82e12db141ec15ce8f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afdbc4",
        "00afdc03"
      ]
    ],
    "bytes_sha256": "f715a4b9720a4b7ec526a957445c7cbddfa61420c7dbb04bc302eeb8dc3a8388",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007082e8](../00708/007082e8.md)
- [00717198](../00717/00717198.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 620 bytes

~~~c

undefined4 FUN_00afdbc4(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afd460 with catch @ 00afdbd4
                       catch() { ... } // from try @ 00afd544 with catch @ 00afdbd4 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afd278 with catch @ 00afdbe4 */
                    /* catch() { ... } // from try @ 00afd234 with catch @ 00afdbfc
                       catch() { ... } // from try @ 00afd328 with catch @ 00afdbfc */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bd4);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afdbc4"></a> `00afdbc4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afdbc8"></a> `00afdbc8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afdbcc"></a> `00afdbcc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afdbd0"></a> `00afdbd0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afdbd4"></a> `00afdbd4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afdbd8"></a> `00afdbd8` | `49 52 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afdbdc"></a> `00afdbdc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afdbe0"></a> `00afdbe0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afdbe4"></a> `00afdbe4` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afdbe8"></a> `00afdbe8` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afdbec"></a> `00afdbec` | `89 7a 89 52` | mov w9,#0x4bd4 | `FALL_THROUGH`
<a id="insn-00afdbf0"></a> `00afdbf0` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afdbf4"></a> `00afdbf4` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afdbf8"></a> `00afdbf8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afdbfc"></a> `00afdbfc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afdc00"></a> `00afdc00` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afdbc4`](#insn-00afdbc4) 範囲 `[['00afdbc4', '00afdbd3']]`
  - `FALL_THROUGH` [`00afdbd0`](#insn-00afdbd0) → [`00afdbd4`](#insn-00afdbd4)
- ブロック [`00afdbd4`](#insn-00afdbd4) 範囲 `[['00afdbd4', '00afdbe3']]`
  - `FALL_THROUGH` [`00afdbe0`](#insn-00afdbe0) → [`00afdbe4`](#insn-00afdbe4)
- ブロック [`00afdbe4`](#insn-00afdbe4) 範囲 `[['00afdbe4', '00afdbfb']]`
  - `FALL_THROUGH` [`00afdbf8`](#insn-00afdbf8) → [`00afdbfc`](#insn-00afdbfc)
- ブロック [`00afdbfc`](#insn-00afdbfc) 範囲 `[['00afdbfc', '00afdc03']]`

## 命令位置別の参照

- [`00afdbc4`](#insn-00afdbc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbc8`](#insn-00afdbc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbd8`](#insn-00afdbd8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afdbf8`](#insn-00afdbf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbfc`](#insn-00afdbfc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afdbc4`](#insn-00afdbc4)

~~~json
{
  "source": "00afdbc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbc8`](#insn-00afdbc8)

~~~json
{
  "source": "00afdbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbd8`](#insn-00afdbd8)

~~~json
{
  "source": "00afdbd8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdbf8`](#insn-00afdbf8)

~~~json
{
  "source": "00afdbf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbfc`](#insn-00afdbfc)

~~~json
{
  "source": "00afdbfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
