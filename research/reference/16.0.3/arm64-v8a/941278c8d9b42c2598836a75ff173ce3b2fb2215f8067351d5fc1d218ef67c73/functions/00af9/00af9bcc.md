# 00af9bcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af8bd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8bd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-23e1f8626e33e5d9e59f3ec95a400453)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af9bcc",
  "name": "FUN_00af9bcc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3c2bec73b8a74b421edc088ae6c667b32c3ca0b1adbfff207c5d4c2a981abfe",
  "source_text_sha256": "d3c2bec73b8a74b421edc088ae6c667b32c3ca0b1adbfff207c5d4c2a981abfe",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af9bcc",
        "00af9c17"
      ]
    ],
    "bytes_sha256": "33fecf59ec7d3d2940682767ebde5fb9d50940e5c08e6a19d8ca2e0ade17ee2a",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 907 bytes

~~~c

void FUN_00af9bcc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00af98c4 with catch @ 00af9bcc
                       catch() { ... } // from try @ 00af9b9c with catch @ 00af9bcc */
                    /* catch() { ... } // from try @ 00af9888 with catch @ 00af9be4
                       catch() { ... } // from try @ 00af9b80 with catch @ 00af9be4 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00af9764 with catch @ 00af9c00 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c1c) = param_3;
                    /* catch() { ... } // from try @ 00af975c with catch @ 00af9c08 */
                    /* catch() { ... } // from try @ 00af96f0 with catch @ 00af9c10 */
                    /* catch() { ... } // from try @ 00af9680 with catch @ 00af9c14 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af9bcc"></a> `00af9bcc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af9bd0"></a> `00af9bd0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af9bd4"></a> `00af9bd4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af9bd8"></a> `00af9bd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af9bdc"></a> `00af9bdc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00af9be0"></a> `00af9be0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af9be4"></a> `00af9be4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af9be8"></a> `00af9be8` | `45 62 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af9bec"></a> `00af9bec` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af9bf0"></a> `00af9bf0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af9bf4"></a> `00af9bf4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af9bf8"></a> `00af9bf8` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af9bfc"></a> `00af9bfc` | `89 83 89 52` | mov w9,#0x4c1c | `FALL_THROUGH`
<a id="insn-00af9c00"></a> `00af9c00` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af9c04"></a> `00af9c04` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af9c08"></a> `00af9c08` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af9c0c"></a> `00af9c0c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af9c10"></a> `00af9c10` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af9c14"></a> `00af9c14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af9bcc`](#insn-00af9bcc) 範囲 `[['00af9bcc', '00af9be3']]`
  - `FALL_THROUGH` [`00af9be0`](#insn-00af9be0) → [`00af9be4`](#insn-00af9be4)
- ブロック [`00af9be4`](#insn-00af9be4) 範囲 `[['00af9be4', '00af9bff']]`
  - `FALL_THROUGH` [`00af9bfc`](#insn-00af9bfc) → [`00af9c00`](#insn-00af9c00)
- ブロック [`00af9c00`](#insn-00af9c00) 範囲 `[['00af9c00', '00af9c07']]`
  - `FALL_THROUGH` [`00af9c04`](#insn-00af9c04) → [`00af9c08`](#insn-00af9c08)
- ブロック [`00af9c08`](#insn-00af9c08) 範囲 `[['00af9c08', '00af9c0f']]`
  - `FALL_THROUGH` [`00af9c0c`](#insn-00af9c0c) → [`00af9c10`](#insn-00af9c10)
- ブロック [`00af9c10`](#insn-00af9c10) 範囲 `[['00af9c10', '00af9c13']]`
  - `FALL_THROUGH` [`00af9c10`](#insn-00af9c10) → [`00af9c14`](#insn-00af9c14)
- ブロック [`00af9c14`](#insn-00af9c14) 範囲 `[['00af9c14', '00af9c17']]`

## 命令位置別の参照

- [`00af9bcc`](#insn-00af9bcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9bd0`](#insn-00af9bd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9bd4`](#insn-00af9bd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9be8`](#insn-00af9be8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af9c08`](#insn-00af9c08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9c0c`](#insn-00af9c0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9c10`](#insn-00af9c10) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af9bcc`](#insn-00af9bcc)

~~~json
{
  "source": "00af9bcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9bd0`](#insn-00af9bd0)

~~~json
{
  "source": "00af9bd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9bd4`](#insn-00af9bd4)

~~~json
{
  "source": "00af9bd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9be8`](#insn-00af9be8)

~~~json
{
  "source": "00af9be8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af9c08`](#insn-00af9c08)

~~~json
{
  "source": "00af9c08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9c0c`](#insn-00af9c0c)

~~~json
{
  "source": "00af9c0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9c10`](#insn-00af9c10)

~~~json
{
  "source": "00af9c10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
