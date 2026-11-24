# 00afd7cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afc7d8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afc7d8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-fa818206b00665370b413ce5de654fbd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afd7cc",
  "name": "FUN_00afd7cc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9697f89d686e5e4c999b5451779abc470a577e439b61e8d81c1e0568717109c5",
  "source_text_sha256": "9697f89d686e5e4c999b5451779abc470a577e439b61e8d81c1e0568717109c5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afd7cc",
        "00afd80b"
      ]
    ],
    "bytes_sha256": "3f46e6f733cd55a7d5f52a8161a5da51361ce71dc4d416850298d58354fa0985",
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
- [007082e8](../00708/007082e8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 288 bytes

~~~c

undefined4 FUN_00afd7cc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afd7f4 to 00bfd817 has its CatchHandler @ 00afdb68 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b6c);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afd7cc"></a> `00afd7cc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afd7d0"></a> `00afd7d0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd7d4"></a> `00afd7d4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afd7d8"></a> `00afd7d8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afd7dc"></a> `00afd7dc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afd7e0"></a> `00afd7e0` | `47 53 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afd7e4"></a> `00afd7e4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afd7e8"></a> `00afd7e8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afd7ec"></a> `00afd7ec` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afd7f0"></a> `00afd7f0` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afd7f4"></a> `00afd7f4` | `89 6d 89 52` | mov w9,#0x4b6c | `FALL_THROUGH`
<a id="insn-00afd7f8"></a> `00afd7f8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afd7fc"></a> `00afd7fc` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afd800"></a> `00afd800` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd804"></a> `00afd804` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afd808"></a> `00afd808` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afd7cc`](#insn-00afd7cc) 範囲 `[['00afd7cc', '00afd7f3']]`
  - `FALL_THROUGH` [`00afd7f0`](#insn-00afd7f0) → [`00afd7f4`](#insn-00afd7f4)
- ブロック [`00afd7f4`](#insn-00afd7f4) 範囲 `[['00afd7f4', '00afd80b']]`

## 命令位置別の参照

- [`00afd7cc`](#insn-00afd7cc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd7d0`](#insn-00afd7d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd7e0`](#insn-00afd7e0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afd800`](#insn-00afd800) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd804`](#insn-00afd804) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afd7cc`](#insn-00afd7cc)

~~~json
{
  "source": "00afd7cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd7d0`](#insn-00afd7d0)

~~~json
{
  "source": "00afd7d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd7e0`](#insn-00afd7e0)

~~~json
{
  "source": "00afd7e0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd800`](#insn-00afd800)

~~~json
{
  "source": "00afd800",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd804`](#insn-00afd804)

~~~json
{
  "source": "00afd804",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
