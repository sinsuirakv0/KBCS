# 00afb9ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afa9f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa9f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-8b53d9ece6e4058b92480496a08f3d13)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb9ec",
  "name": "FUN_00afb9ec",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e007265a18f29f8607a7ea158480179f1d22ce42dafbca85ccaba35e35b488ce",
  "source_text_sha256": "e007265a18f29f8607a7ea158480179f1d22ce42dafbca85ccaba35e35b488ce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb9ec",
        "00afba37"
      ]
    ],
    "bytes_sha256": "26de3d886c79fc7926411c3a39a124f9d483d3ac6beecb9921c20e30222f6feb",
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

## 疑似コード / UTF-8 565 bytes

~~~c

void FUN_00afb9ec(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afb7d4 with catch @ 00afb9f4 */
                    /* catch() { ... } // from try @ 00afb6bc with catch @ 00afb9f8 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afb5d0 with catch @ 00afba14 */
                    /* catch() { ... } // from try @ 00afb4bc with catch @ 00afba18 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ca0) = param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afb9ec"></a> `00afb9ec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afb9f0"></a> `00afb9f0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb9f4"></a> `00afb9f4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb9f8"></a> `00afb9f8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afb9fc"></a> `00afb9fc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afba00"></a> `00afba00` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afba04"></a> `00afba04` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afba08"></a> `00afba08` | `bd 5a f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afba0c"></a> `00afba0c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afba10"></a> `00afba10` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afba14"></a> `00afba14` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afba18"></a> `00afba18` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afba1c"></a> `00afba1c` | `09 94 89 52` | mov w9,#0x4ca0 | `FALL_THROUGH`
<a id="insn-00afba20"></a> `00afba20` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afba24"></a> `00afba24` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afba28"></a> `00afba28` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afba2c"></a> `00afba2c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afba30"></a> `00afba30` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afba34"></a> `00afba34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb9ec`](#insn-00afb9ec) 範囲 `[['00afb9ec', '00afb9f3']]`
  - `FALL_THROUGH` [`00afb9f0`](#insn-00afb9f0) → [`00afb9f4`](#insn-00afb9f4)
- ブロック [`00afb9f4`](#insn-00afb9f4) 範囲 `[['00afb9f4', '00afb9f7']]`
  - `FALL_THROUGH` [`00afb9f4`](#insn-00afb9f4) → [`00afb9f8`](#insn-00afb9f8)
- ブロック [`00afb9f8`](#insn-00afb9f8) 範囲 `[['00afb9f8', '00afba13']]`
  - `FALL_THROUGH` [`00afba10`](#insn-00afba10) → [`00afba14`](#insn-00afba14)
- ブロック [`00afba14`](#insn-00afba14) 範囲 `[['00afba14', '00afba17']]`
  - `FALL_THROUGH` [`00afba14`](#insn-00afba14) → [`00afba18`](#insn-00afba18)
- ブロック [`00afba18`](#insn-00afba18) 範囲 `[['00afba18', '00afba37']]`

## 命令位置別の参照

- [`00afb9ec`](#insn-00afb9ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb9f0`](#insn-00afb9f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb9f4`](#insn-00afb9f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afba08`](#insn-00afba08) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afba28`](#insn-00afba28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afba2c`](#insn-00afba2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afba30`](#insn-00afba30) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb9ec`](#insn-00afb9ec)

~~~json
{
  "source": "00afb9ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb9f0`](#insn-00afb9f0)

~~~json
{
  "source": "00afb9f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb9f4`](#insn-00afb9f4)

~~~json
{
  "source": "00afb9f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afba08`](#insn-00afba08)

~~~json
{
  "source": "00afba08",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afba28`](#insn-00afba28)

~~~json
{
  "source": "00afba28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afba2c`](#insn-00afba2c)

~~~json
{
  "source": "00afba2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afba30`](#insn-00afba30)

~~~json
{
  "source": "00afba30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
