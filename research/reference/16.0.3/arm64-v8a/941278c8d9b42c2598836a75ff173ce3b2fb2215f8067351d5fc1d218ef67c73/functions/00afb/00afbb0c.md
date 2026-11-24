# 00afbb0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afab18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afab18.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0069.md#compare-2929ae2abd402e93bb4010c7157d640b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbb0c",
  "name": "FUN_00afbb0c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb628c7f0c4e454a534b7c3276a3e7cd3383c0898566f54975022da2241d4e9a",
  "source_text_sha256": "eb628c7f0c4e454a534b7c3276a3e7cd3383c0898566f54975022da2241d4e9a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbb0c",
        "00afbb57"
      ]
    ],
    "bytes_sha256": "0838c453acd0967c6e0fff95b9c0d4ed205ec9865bd43b1f32df5b2b22d2892f",
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

## 疑似コード / UTF-8 725 bytes

~~~c

void FUN_00afbb0c(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afb3b8 with catch @ 00afbb0c
                       catch() { ... } // from try @ 00afb494 with catch @ 00afbb0c */
                    /* catch() { ... } // from try @ 00afb7f8 with catch @ 00afbb10 */
                    /* catch() { ... } // from try @ 00afb7bc with catch @ 00afbb28
                       catch() { ... } // from try @ 00afb8a0 with catch @ 00afbb28 */
  lVar1 = FUN_008524fc();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a20) = param_3 & 1;
                    /* catch() { ... } // from try @ 00afb1e4 with catch @ 00afbb54 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbb0c"></a> `00afbb0c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afbb10"></a> `00afbb10` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbb14"></a> `00afbb14` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbb18"></a> `00afbb18` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afbb1c"></a> `00afbb1c` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afbb20"></a> `00afbb20` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afbb24"></a> `00afbb24` | `55 00 00 12` | and w21,w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afbb28"></a> `00afbb28` | `75 5a f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afbb2c"></a> `00afbb2c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afbb30"></a> `00afbb30` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afbb34"></a> `00afbb34` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afbb38"></a> `00afbb38` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afbb3c"></a> `00afbb3c` | `09 44 89 52` | mov w9,#0x4a20 | `FALL_THROUGH`
<a id="insn-00afbb40"></a> `00afbb40` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afbb44"></a> `00afbb44` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afbb48"></a> `00afbb48` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbb4c"></a> `00afbb4c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbb50"></a> `00afbb50` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afbb54"></a> `00afbb54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbb0c`](#insn-00afbb0c) 範囲 `[['00afbb0c', '00afbb0f']]`
  - `FALL_THROUGH` [`00afbb0c`](#insn-00afbb0c) → [`00afbb10`](#insn-00afbb10)
- ブロック [`00afbb10`](#insn-00afbb10) 範囲 `[['00afbb10', '00afbb27']]`
  - `FALL_THROUGH` [`00afbb24`](#insn-00afbb24) → [`00afbb28`](#insn-00afbb28)
- ブロック [`00afbb28`](#insn-00afbb28) 範囲 `[['00afbb28', '00afbb53']]`
  - `FALL_THROUGH` [`00afbb50`](#insn-00afbb50) → [`00afbb54`](#insn-00afbb54)
- ブロック [`00afbb54`](#insn-00afbb54) 範囲 `[['00afbb54', '00afbb57']]`

## 命令位置別の参照

- [`00afbb0c`](#insn-00afbb0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb10`](#insn-00afbb10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb14`](#insn-00afbb14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb28`](#insn-00afbb28) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afbb48`](#insn-00afbb48) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb4c`](#insn-00afbb4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb50`](#insn-00afbb50) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbb0c`](#insn-00afbb0c)

~~~json
{
  "source": "00afbb0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb10`](#insn-00afbb10)

~~~json
{
  "source": "00afbb10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb14`](#insn-00afbb14)

~~~json
{
  "source": "00afbb14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb28`](#insn-00afbb28)

~~~json
{
  "source": "00afbb28",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbb48`](#insn-00afbb48)

~~~json
{
  "source": "00afbb48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb4c`](#insn-00afbb4c)

~~~json
{
  "source": "00afbb4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb50`](#insn-00afbb50)

~~~json
{
  "source": "00afbb50",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
