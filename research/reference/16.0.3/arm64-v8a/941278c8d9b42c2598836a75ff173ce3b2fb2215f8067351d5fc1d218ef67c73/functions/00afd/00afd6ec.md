# 00afd6ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afc6f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afc6f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-b6587c4620e2a0069c874095b574d6b4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afd6ec",
  "name": "FUN_00afd6ec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00eb8dd54df6217aed0d3f97e39cba997f053a3524182b49752b9a9716c33132",
  "source_text_sha256": "00eb8dd54df6217aed0d3f97e39cba997f053a3524182b49752b9a9716c33132",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afd6ec",
        "00afd72b"
      ]
    ],
    "bytes_sha256": "f90d7da86298439e2e60fb6bc6675d73fbc87704a9c8fea6a8d4580d6335b6af",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)
- [005f3e60](../005f3/005f3e60.md)
- [005fbd2c](../005fb/005fbd2c.md)
- [007082e8](../00708/007082e8.md)
- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 385 bytes

~~~c

undefined4 FUN_00afd6ec(int param_1,int param_2)

{
  long lVar1;
  
                    /* try { // try from 00afd6f8 to 00bfd70f has its CatchHandler @ 00afd9f0 */
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afd71c to 00bfd743 has its CatchHandler @ 00afdbb4 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b64);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afd6ec"></a> `00afd6ec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afd6f0"></a> `00afd6f0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd6f4"></a> `00afd6f4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afd6f8"></a> `00afd6f8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afd6fc"></a> `00afd6fc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afd700"></a> `00afd700` | `7f 53 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afd704"></a> `00afd704` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afd708"></a> `00afd708` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afd70c"></a> `00afd70c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afd710"></a> `00afd710` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afd714"></a> `00afd714` | `89 6c 89 52` | mov w9,#0x4b64 | `FALL_THROUGH`
<a id="insn-00afd718"></a> `00afd718` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afd71c"></a> `00afd71c` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afd720"></a> `00afd720` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd724"></a> `00afd724` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afd728"></a> `00afd728` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afd6ec`](#insn-00afd6ec) 範囲 `[['00afd6ec', '00afd6f7']]`
  - `FALL_THROUGH` [`00afd6f4`](#insn-00afd6f4) → [`00afd6f8`](#insn-00afd6f8)
- ブロック [`00afd6f8`](#insn-00afd6f8) 範囲 `[['00afd6f8', '00afd71b']]`
  - `FALL_THROUGH` [`00afd718`](#insn-00afd718) → [`00afd71c`](#insn-00afd71c)
- ブロック [`00afd71c`](#insn-00afd71c) 範囲 `[['00afd71c', '00afd72b']]`

## 命令位置別の参照

- [`00afd6ec`](#insn-00afd6ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd6f0`](#insn-00afd6f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd700`](#insn-00afd700) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afd720`](#insn-00afd720) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd724`](#insn-00afd724) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afd6ec`](#insn-00afd6ec)

~~~json
{
  "source": "00afd6ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd6f0`](#insn-00afd6f0)

~~~json
{
  "source": "00afd6f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd700`](#insn-00afd700)

~~~json
{
  "source": "00afd700",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd720`](#insn-00afd720)

~~~json
{
  "source": "00afd720",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd724`](#insn-00afd724)

~~~json
{
  "source": "00afd724",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
