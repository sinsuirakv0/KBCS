# 00afcacc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0019.md#review-274fb34c805c61a49aef898046446ac5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afcef4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcef4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0007.md#compare-d01af399dc933960bf12a86d02f61192)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcacc",
  "name": "FUN_00afcacc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "32b9d613465bec2e58f55d712010ef5a96996ef9cdb1127621fb173f7348e4ce",
  "source_text_sha256": "32b9d613465bec2e58f55d712010ef5a96996ef9cdb1127621fb173f7348e4ce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcacc",
        "00afcb1f"
      ]
    ],
    "bytes_sha256": "9fd6848fc6cba1bcb2f6e3772c1d61ebe2301de07db7dc618b4f5b4e5dcb8332",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00710298](../00710/00710298.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 509 bytes

~~~c

void FUN_00afcacc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afbcd8 with catch @ 00afcadc */
  lVar1 = FUN_008514b8();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
                    /* catch() { ... } // from try @ 00afc778 with catch @ 00afcafc */
  *(int *)(lVar1 + 0x84ca8) = *(int *)(lVar1 + 0x84ca8) + param_3;
                    /* catch() { ... } // from try @ 00afba10 with catch @ 00afcb14 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcacc"></a> `00afcacc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afcad0"></a> `00afcad0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcad4"></a> `00afcad4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcad8"></a> `00afcad8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcadc"></a> `00afcadc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afcae0"></a> `00afcae0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afcae4"></a> `00afcae4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afcae8"></a> `00afcae8` | `74 52 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcaec"></a> `00afcaec` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcaf0"></a> `00afcaf0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcaf4"></a> `00afcaf4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcaf8"></a> `00afcaf8` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afcafc"></a> `00afcafc` | `09 95 89 52` | mov w9,#0x4ca8 | `FALL_THROUGH`
<a id="insn-00afcb00"></a> `00afcb00` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afcb04"></a> `00afcb04` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcb08"></a> `00afcb08` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00afcb0c"></a> `00afcb0c` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcb10"></a> `00afcb10` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcb14"></a> `00afcb14` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcb18"></a> `00afcb18` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afcb1c"></a> `00afcb1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcacc`](#insn-00afcacc) 範囲 `[['00afcacc', '00afcadb']]`
  - `FALL_THROUGH` [`00afcad8`](#insn-00afcad8) → [`00afcadc`](#insn-00afcadc)
- ブロック [`00afcadc`](#insn-00afcadc) 範囲 `[['00afcadc', '00afcafb']]`
  - `FALL_THROUGH` [`00afcaf8`](#insn-00afcaf8) → [`00afcafc`](#insn-00afcafc)
- ブロック [`00afcafc`](#insn-00afcafc) 範囲 `[['00afcafc', '00afcb13']]`
  - `FALL_THROUGH` [`00afcb10`](#insn-00afcb10) → [`00afcb14`](#insn-00afcb14)
- ブロック [`00afcb14`](#insn-00afcb14) 範囲 `[['00afcb14', '00afcb1f']]`

## 命令位置別の参照

- [`00afcacc`](#insn-00afcacc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcad0`](#insn-00afcad0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcad4`](#insn-00afcad4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcae8`](#insn-00afcae8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afcb10`](#insn-00afcb10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcb14`](#insn-00afcb14) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcb18`](#insn-00afcb18) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcacc`](#insn-00afcacc)

~~~json
{
  "source": "00afcacc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcad0`](#insn-00afcad0)

~~~json
{
  "source": "00afcad0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcad4`](#insn-00afcad4)

~~~json
{
  "source": "00afcad4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcae8`](#insn-00afcae8)

~~~json
{
  "source": "00afcae8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcb10`](#insn-00afcb10)

~~~json
{
  "source": "00afcb10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcb14`](#insn-00afcb14)

~~~json
{
  "source": "00afcb14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcb18`](#insn-00afcb18)

~~~json
{
  "source": "00afcb18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
