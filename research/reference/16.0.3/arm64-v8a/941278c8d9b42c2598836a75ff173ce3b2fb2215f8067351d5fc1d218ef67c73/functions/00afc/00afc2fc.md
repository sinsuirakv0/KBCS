# 00afc2fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afb308`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afb/00afb308.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-dcd6904d1f8863ff7d780bfe29ff167b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afc2fc",
  "name": "FUN_00afc2fc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b397a79ded0b99a318b98393b480746e1d973d6e633d203610fdd2f967c77b68",
  "source_text_sha256": "b397a79ded0b99a318b98393b480746e1d973d6e633d203610fdd2f967c77b68",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afc2fc",
        "00afc347"
      ]
    ],
    "bytes_sha256": "78adae7e03fcc90c52c40933d6cc1d573d5caacbf37cbc52871e0e7d7ba5d8c4",
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
- [00a53028](../00a53/00a53028.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 478 bytes

~~~c

void FUN_00afc2fc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afc15c with catch @ 00afc300 */
  lVar1 = FUN_008524fc();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b68) = param_3;
                    /* catch() { ... } // from try @ 00afc064 with catch @ 00afc340 */
                    /* catch() { ... } // from try @ 00afbfec with catch @ 00afc344 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afc2fc"></a> `00afc2fc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afc300"></a> `00afc300` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc304"></a> `00afc304` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afc308"></a> `00afc308` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afc30c"></a> `00afc30c` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afc310"></a> `00afc310` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afc314"></a> `00afc314` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afc318"></a> `00afc318` | `79 58 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afc31c"></a> `00afc31c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afc320"></a> `00afc320` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afc324"></a> `00afc324` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afc328"></a> `00afc328` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afc32c"></a> `00afc32c` | `09 6d 89 52` | mov w9,#0x4b68 | `FALL_THROUGH`
<a id="insn-00afc330"></a> `00afc330` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afc334"></a> `00afc334` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afc338"></a> `00afc338` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afc33c"></a> `00afc33c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc340"></a> `00afc340` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afc344"></a> `00afc344` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afc2fc`](#insn-00afc2fc) 範囲 `[['00afc2fc', '00afc2ff']]`
  - `FALL_THROUGH` [`00afc2fc`](#insn-00afc2fc) → [`00afc300`](#insn-00afc300)
- ブロック [`00afc300`](#insn-00afc300) 範囲 `[['00afc300', '00afc33f']]`
  - `FALL_THROUGH` [`00afc33c`](#insn-00afc33c) → [`00afc340`](#insn-00afc340)
- ブロック [`00afc340`](#insn-00afc340) 範囲 `[['00afc340', '00afc343']]`
  - `FALL_THROUGH` [`00afc340`](#insn-00afc340) → [`00afc344`](#insn-00afc344)
- ブロック [`00afc344`](#insn-00afc344) 範囲 `[['00afc344', '00afc347']]`

## 命令位置別の参照

- [`00afc2fc`](#insn-00afc2fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc300`](#insn-00afc300) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc304`](#insn-00afc304) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc318`](#insn-00afc318) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afc338`](#insn-00afc338) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc33c`](#insn-00afc33c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc340`](#insn-00afc340) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afc2fc`](#insn-00afc2fc)

~~~json
{
  "source": "00afc2fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc300`](#insn-00afc300)

~~~json
{
  "source": "00afc300",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc304`](#insn-00afc304)

~~~json
{
  "source": "00afc304",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc318`](#insn-00afc318)

~~~json
{
  "source": "00afc318",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc338`](#insn-00afc338)

~~~json
{
  "source": "00afc338",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc33c`](#insn-00afc33c)

~~~json
{
  "source": "00afc33c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc340`](#insn-00afc340)

~~~json
{
  "source": "00afc340",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
