# 00afcbc0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afc798`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc798.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0007.md#compare-a8acf62e109fe63ce3b8625a7e7f514e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afcc5c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afcc5c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0007.md#compare-56514f619c5367fd2be5faf9357c56d1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcbc0",
  "name": "FUN_00afcbc0",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e312347ecf49bceaa1f9774d8efd58d882304c8f789bfa4fef6ed6124b72c81",
  "source_text_sha256": "2e312347ecf49bceaa1f9774d8efd58d882304c8f789bfa4fef6ed6124b72c81",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcbc0",
        "00afcc13"
      ]
    ],
    "bytes_sha256": "031a58c1e7475b94d13ed256629b9aec7c40724ea99463db374834a774a1aa3f",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00716d90](../00716/00716d90.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 851 bytes

~~~c

void FUN_00afcbc0(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afc460 with catch @ 00afcbd4
                       catch() { ... } // from try @ 00afc544 with catch @ 00afcbd4 */
  lVar1 = FUN_008514f8();
                    /* catch() { ... } // from try @ 00afc278 with catch @ 00afcbe4 */
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
                    /* catch() { ... } // from try @ 00afc234 with catch @ 00afcbfc
                       catch() { ... } // from try @ 00afc328 with catch @ 00afcbfc */
  *(int *)(lVar1 + 0x84bd4) = *(int *)(lVar1 + 0x84bd4) + param_3;
                    /* catch() { ... } // from try @ 00afbc28 with catch @ 00afcc0c */
                    /* catch() { ... } // from try @ 00afb8b0 with catch @ 00afcc10 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcbc0"></a> `00afcbc0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afcbc4"></a> `00afcbc4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcbc8"></a> `00afcbc8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcbcc"></a> `00afcbcc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcbd0"></a> `00afcbd0` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afcbd4"></a> `00afcbd4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afcbd8"></a> `00afcbd8` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afcbdc"></a> `00afcbdc` | `47 52 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcbe0"></a> `00afcbe0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcbe4"></a> `00afcbe4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcbe8"></a> `00afcbe8` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcbec"></a> `00afcbec` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afcbf0"></a> `00afcbf0` | `89 7a 89 52` | mov w9,#0x4bd4 | `FALL_THROUGH`
<a id="insn-00afcbf4"></a> `00afcbf4` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afcbf8"></a> `00afcbf8` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcbfc"></a> `00afcbfc` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00afcc00"></a> `00afcc00` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcc04"></a> `00afcc04` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcc08"></a> `00afcc08` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcc0c"></a> `00afcc0c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afcc10"></a> `00afcc10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcbc0`](#insn-00afcbc0) 範囲 `[['00afcbc0', '00afcbd3']]`
  - `FALL_THROUGH` [`00afcbd0`](#insn-00afcbd0) → [`00afcbd4`](#insn-00afcbd4)
- ブロック [`00afcbd4`](#insn-00afcbd4) 範囲 `[['00afcbd4', '00afcbe3']]`
  - `FALL_THROUGH` [`00afcbe0`](#insn-00afcbe0) → [`00afcbe4`](#insn-00afcbe4)
- ブロック [`00afcbe4`](#insn-00afcbe4) 範囲 `[['00afcbe4', '00afcbfb']]`
  - `FALL_THROUGH` [`00afcbf8`](#insn-00afcbf8) → [`00afcbfc`](#insn-00afcbfc)
- ブロック [`00afcbfc`](#insn-00afcbfc) 範囲 `[['00afcbfc', '00afcc0b']]`
  - `FALL_THROUGH` [`00afcc08`](#insn-00afcc08) → [`00afcc0c`](#insn-00afcc0c)
- ブロック [`00afcc0c`](#insn-00afcc0c) 範囲 `[['00afcc0c', '00afcc0f']]`
  - `FALL_THROUGH` [`00afcc0c`](#insn-00afcc0c) → [`00afcc10`](#insn-00afcc10)
- ブロック [`00afcc10`](#insn-00afcc10) 範囲 `[['00afcc10', '00afcc13']]`

## 命令位置別の参照

- [`00afcbc0`](#insn-00afcbc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcbc4`](#insn-00afcbc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcbc8`](#insn-00afcbc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcbdc`](#insn-00afcbdc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afcc04`](#insn-00afcc04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcc08`](#insn-00afcc08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcc0c`](#insn-00afcc0c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcbc0`](#insn-00afcbc0)

~~~json
{
  "source": "00afcbc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcbc4`](#insn-00afcbc4)

~~~json
{
  "source": "00afcbc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcbc8`](#insn-00afcbc8)

~~~json
{
  "source": "00afcbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcbdc`](#insn-00afcbdc)

~~~json
{
  "source": "00afcbdc",
  "target": "008514f8",
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
- 参照命令 [`00afcc0c`](#insn-00afcc0c)

~~~json
{
  "source": "00afcc0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
