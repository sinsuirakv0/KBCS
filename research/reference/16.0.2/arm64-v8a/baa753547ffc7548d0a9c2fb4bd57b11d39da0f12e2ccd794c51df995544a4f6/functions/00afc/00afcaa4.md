# 00afcaa4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afca08`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afca08.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0007.md#compare-614b782bc9053a89f9b3b2ee129e516c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00afda98`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afda98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-1a2200d55c61c1772d1cae3f4386718e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcaa4",
  "name": "FUN_00afcaa4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2ef84b7ce28af67bcd09b99049ad8adac451d66b7ddd8384bd95cad42ec5374",
  "source_text_sha256": "d2ef84b7ce28af67bcd09b99049ad8adac451d66b7ddd8384bd95cad42ec5374",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcaa4",
        "00afcaef"
      ]
    ],
    "bytes_sha256": "1cd3f2137f5a9f394be711d2d34a8a0cc231bb6833c613f91ff775a73ad23187",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700b50](../00700/00700b50.md)
- [00716de8](../00716/00716de8.md)
- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 478 bytes

~~~c

void FUN_00afcaa4(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afc094 with catch @ 00afcac8 */
                    /* catch() { ... } // from try @ 00afba7c with catch @ 00afcacc */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bc8) = param_3;
                    /* catch() { ... } // from try @ 00afba30 with catch @ 00afcae8 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcaa4"></a> `00afcaa4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afcaa8"></a> `00afcaa8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcaac"></a> `00afcaac` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcab0"></a> `00afcab0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcab4"></a> `00afcab4` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afcab8"></a> `00afcab8` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afcabc"></a> `00afcabc` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afcac0"></a> `00afcac0` | `a4 52 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00afcac4"></a> `00afcac4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcac8"></a> `00afcac8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcacc"></a> `00afcacc` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcad0"></a> `00afcad0` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afcad4"></a> `00afcad4` | `09 79 89 52` | mov w9,#0x4bc8 | `FALL_THROUGH`
<a id="insn-00afcad8"></a> `00afcad8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afcadc"></a> `00afcadc` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcae0"></a> `00afcae0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcae4"></a> `00afcae4` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcae8"></a> `00afcae8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afcaec"></a> `00afcaec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcaa4`](#insn-00afcaa4) 範囲 `[['00afcaa4', '00afcac7']]`
  - `FALL_THROUGH` [`00afcac4`](#insn-00afcac4) → [`00afcac8`](#insn-00afcac8)
- ブロック [`00afcac8`](#insn-00afcac8) 範囲 `[['00afcac8', '00afcacb']]`
  - `FALL_THROUGH` [`00afcac8`](#insn-00afcac8) → [`00afcacc`](#insn-00afcacc)
- ブロック [`00afcacc`](#insn-00afcacc) 範囲 `[['00afcacc', '00afcae7']]`
  - `FALL_THROUGH` [`00afcae4`](#insn-00afcae4) → [`00afcae8`](#insn-00afcae8)
- ブロック [`00afcae8`](#insn-00afcae8) 範囲 `[['00afcae8', '00afcaef']]`

## 命令位置別の参照

- [`00afcaa4`](#insn-00afcaa4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcaa8`](#insn-00afcaa8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcaac`](#insn-00afcaac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcac0`](#insn-00afcac0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00afcae0`](#insn-00afcae0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcae4`](#insn-00afcae4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcae8`](#insn-00afcae8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcaa4`](#insn-00afcaa4)

~~~json
{
  "source": "00afcaa4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcaa8`](#insn-00afcaa8)

~~~json
{
  "source": "00afcaa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcaac`](#insn-00afcaac)

~~~json
{
  "source": "00afcaac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcac0`](#insn-00afcac0)

~~~json
{
  "source": "00afcac0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcae0`](#insn-00afcae0)

~~~json
{
  "source": "00afcae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcae4`](#insn-00afcae4)

~~~json
{
  "source": "00afcae4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcae8`](#insn-00afcae8)

~~~json
{
  "source": "00afcae8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
