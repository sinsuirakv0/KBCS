# 00afcbd0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afcb34`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcb34.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0007.md#compare-9fffb7ca0094db2eae6b9a4304fb1e23)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00afdbc4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afdbc4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-3a3ead16d6eaff533366423327197136)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcbd0",
  "name": "FUN_00afcbd0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d61106c17658076a3c8011997a5fc222274b3e324a214d5af3a94e29186e966c",
  "source_text_sha256": "d61106c17658076a3c8011997a5fc222274b3e324a214d5af3a94e29186e966c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcbd0",
        "00afcc0f"
      ]
    ],
    "bytes_sha256": "7a8832a371b789e25abbb4e29192eb9ff30f3a11612d663fee24c88403e913ba",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00707f38](../00707/00707f38.md)
- [00716de8](../00716/00716de8.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 794 bytes

~~~c

undefined4 FUN_00afcbd0(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afc0b8 with catch @ 00afcbfc */
                    /* catch() { ... } // from try @ 00afc088 with catch @ 00afcc00
                       catch() { ... } // from try @ 00afc164 with catch @ 00afcc00 */
                    /* catch() { ... } // from try @ 00afbf44 with catch @ 00afcc04 */
                    /* catch() { ... } // from try @ 00afc770 with catch @ 00afcc08 */
                    /* catch() { ... } // from try @ 00afc734 with catch @ 00afcc0c
                       catch() { ... } // from try @ 00afc818 with catch @ 00afcc0c */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bd4);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcbd0"></a> `00afcbd0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afcbd4"></a> `00afcbd4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcbd8"></a> `00afcbd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcbdc"></a> `00afcbdc` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afcbe0"></a> `00afcbe0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afcbe4"></a> `00afcbe4` | `5b 52 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00afcbe8"></a> `00afcbe8` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcbec"></a> `00afcbec` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcbf0"></a> `00afcbf0` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcbf4"></a> `00afcbf4` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afcbf8"></a> `00afcbf8` | `89 7a 89 52` | mov w9,#0x4bd4 | `FALL_THROUGH`
<a id="insn-00afcbfc"></a> `00afcbfc` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afcc00"></a> `00afcc00` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcc04"></a> `00afcc04` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcc08"></a> `00afcc08` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afcc0c"></a> `00afcc0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcbd0`](#insn-00afcbd0) 範囲 `[['00afcbd0', '00afcbfb']]`
  - `FALL_THROUGH` [`00afcbf8`](#insn-00afcbf8) → [`00afcbfc`](#insn-00afcbfc)
- ブロック [`00afcbfc`](#insn-00afcbfc) 範囲 `[['00afcbfc', '00afcbff']]`
  - `FALL_THROUGH` [`00afcbfc`](#insn-00afcbfc) → [`00afcc00`](#insn-00afcc00)
- ブロック [`00afcc00`](#insn-00afcc00) 範囲 `[['00afcc00', '00afcc03']]`
  - `FALL_THROUGH` [`00afcc00`](#insn-00afcc00) → [`00afcc04`](#insn-00afcc04)
- ブロック [`00afcc04`](#insn-00afcc04) 範囲 `[['00afcc04', '00afcc07']]`
  - `FALL_THROUGH` [`00afcc04`](#insn-00afcc04) → [`00afcc08`](#insn-00afcc08)
- ブロック [`00afcc08`](#insn-00afcc08) 範囲 `[['00afcc08', '00afcc0b']]`
  - `FALL_THROUGH` [`00afcc08`](#insn-00afcc08) → [`00afcc0c`](#insn-00afcc0c)
- ブロック [`00afcc0c`](#insn-00afcc0c) 範囲 `[['00afcc0c', '00afcc0f']]`

## 命令位置別の参照

- [`00afcbd0`](#insn-00afcbd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcbd4`](#insn-00afcbd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcbe4`](#insn-00afcbe4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00afcc04`](#insn-00afcc04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcc08`](#insn-00afcc08) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcbd0`](#insn-00afcbd0)

~~~json
{
  "source": "00afcbd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcbd4`](#insn-00afcbd4)

~~~json
{
  "source": "00afcbd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcbe4`](#insn-00afcbe4)

~~~json
{
  "source": "00afcbe4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcc04`](#insn-00afcc04)

~~~json
{
  "source": "00afcc04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcc08`](#insn-00afcc08)

~~~json
{
  "source": "00afcc08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
