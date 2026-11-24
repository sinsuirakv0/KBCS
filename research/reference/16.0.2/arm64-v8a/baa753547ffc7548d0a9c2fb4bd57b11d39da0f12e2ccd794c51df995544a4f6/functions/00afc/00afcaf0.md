# 00afcaf0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afca54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afca54.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0007.md#compare-2038f24cdd08dd1d0f1e6109f5989455)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00afdae4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afdae4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-e6180b42019630ef7291b5deb303dbb6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcaf0",
  "name": "FUN_00afcaf0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb425c186296bba233bb1033e2f5ade9d8cc12c0b398a4660c2182dc759d2a59",
  "source_text_sha256": "eb425c186296bba233bb1033e2f5ade9d8cc12c0b398a4660c2182dc759d2a59",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcaf0",
        "00afcb2f"
      ]
    ],
    "bytes_sha256": "f9771da4f064321163a0b93729bb7a9cebe69a1bf8453e658d664c9f9256ba7f",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700b50](../00700/00700b50.md)
- [00707f38](../00707/00707f38.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 365 bytes

~~~c

undefined4 FUN_00afcaf0(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afb854 with catch @ 00afcb20 */
                    /* catch() { ... } // from try @ 00afb744 with catch @ 00afcb28 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bcc);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcaf0"></a> `00afcaf0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afcaf4"></a> `00afcaf4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcaf8"></a> `00afcaf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcafc"></a> `00afcafc` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afcb00"></a> `00afcb00` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afcb04"></a> `00afcb04` | `93 52 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00afcb08"></a> `00afcb08` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcb0c"></a> `00afcb0c` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcb10"></a> `00afcb10` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcb14"></a> `00afcb14` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afcb18"></a> `00afcb18` | `89 79 89 52` | mov w9,#0x4bcc | `FALL_THROUGH`
<a id="insn-00afcb1c"></a> `00afcb1c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afcb20"></a> `00afcb20` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcb24"></a> `00afcb24` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcb28"></a> `00afcb28` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afcb2c"></a> `00afcb2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcaf0`](#insn-00afcaf0) 範囲 `[['00afcaf0', '00afcb1f']]`
  - `FALL_THROUGH` [`00afcb1c`](#insn-00afcb1c) → [`00afcb20`](#insn-00afcb20)
- ブロック [`00afcb20`](#insn-00afcb20) 範囲 `[['00afcb20', '00afcb27']]`
  - `FALL_THROUGH` [`00afcb24`](#insn-00afcb24) → [`00afcb28`](#insn-00afcb28)
- ブロック [`00afcb28`](#insn-00afcb28) 範囲 `[['00afcb28', '00afcb2f']]`

## 命令位置別の参照

- [`00afcaf0`](#insn-00afcaf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcaf4`](#insn-00afcaf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcb04`](#insn-00afcb04) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00afcb24`](#insn-00afcb24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcb28`](#insn-00afcb28) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcaf0`](#insn-00afcaf0)

~~~json
{
  "source": "00afcaf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcaf4`](#insn-00afcaf4)

~~~json
{
  "source": "00afcaf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcb04`](#insn-00afcb04)

~~~json
{
  "source": "00afcb04",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcb24`](#insn-00afcb24)

~~~json
{
  "source": "00afcb24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcb28`](#insn-00afcb28)

~~~json
{
  "source": "00afcb28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
