# 00afd9cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afc9d8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afc9d8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-9e60fb65bd72c01dbcddf2e7b01796ee)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afd9cc",
  "name": "FUN_00afd9cc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35fce9dec7b087bd76aa69d27127f53acd5763f854ac64e7b46576510d59aaf4",
  "source_text_sha256": "35fce9dec7b087bd76aa69d27127f53acd5763f854ac64e7b46576510d59aaf4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afd9cc",
        "00afda0b"
      ]
    ],
    "bytes_sha256": "7fc6fd80f28aa0b86bcf02495318d73cd984f864c99c61587c6dbe4375e75e79",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 452 bytes

~~~c

undefined4 FUN_00afd9cc(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afc528 with catch @ 00afd9d8 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afd6f8 with catch @ 00afd9f0 */
                    /* catch() { ... } // from try @ 00afd56c with catch @ 00afd9f4 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bc4);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afd9cc"></a> `00afd9cc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afd9d0"></a> `00afd9d0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd9d4"></a> `00afd9d4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afd9d8"></a> `00afd9d8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afd9dc"></a> `00afd9dc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afd9e0"></a> `00afd9e0` | `c7 52 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afd9e4"></a> `00afd9e4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afd9e8"></a> `00afd9e8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afd9ec"></a> `00afd9ec` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afd9f0"></a> `00afd9f0` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afd9f4"></a> `00afd9f4` | `89 78 89 52` | mov w9,#0x4bc4 | `FALL_THROUGH`
<a id="insn-00afd9f8"></a> `00afd9f8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afd9fc"></a> `00afd9fc` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afda00"></a> `00afda00` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afda04"></a> `00afda04` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afda08"></a> `00afda08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afd9cc`](#insn-00afd9cc) 範囲 `[['00afd9cc', '00afd9d7']]`
  - `FALL_THROUGH` [`00afd9d4`](#insn-00afd9d4) → [`00afd9d8`](#insn-00afd9d8)
- ブロック [`00afd9d8`](#insn-00afd9d8) 範囲 `[['00afd9d8', '00afd9ef']]`
  - `FALL_THROUGH` [`00afd9ec`](#insn-00afd9ec) → [`00afd9f0`](#insn-00afd9f0)
- ブロック [`00afd9f0`](#insn-00afd9f0) 範囲 `[['00afd9f0', '00afd9f3']]`
  - `FALL_THROUGH` [`00afd9f0`](#insn-00afd9f0) → [`00afd9f4`](#insn-00afd9f4)
- ブロック [`00afd9f4`](#insn-00afd9f4) 範囲 `[['00afd9f4', '00afda0b']]`

## 命令位置別の参照

- [`00afd9cc`](#insn-00afd9cc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd9d0`](#insn-00afd9d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd9e0`](#insn-00afd9e0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afda00`](#insn-00afda00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afda04`](#insn-00afda04) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afd9cc`](#insn-00afd9cc)

~~~json
{
  "source": "00afd9cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd9d0`](#insn-00afd9d0)

~~~json
{
  "source": "00afd9d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd9e0`](#insn-00afd9e0)

~~~json
{
  "source": "00afd9e0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afda00`](#insn-00afda00)

~~~json
{
  "source": "00afda00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afda04`](#insn-00afda04)

~~~json
{
  "source": "00afda04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
