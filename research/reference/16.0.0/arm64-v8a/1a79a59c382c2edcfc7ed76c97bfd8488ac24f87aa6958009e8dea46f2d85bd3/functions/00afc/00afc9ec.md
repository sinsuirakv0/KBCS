# 00afc9ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0169.md#review-29d49a77c076ddda1a73db223eeadd22)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afce14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afce14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0007.md#compare-e649cb623343cd4e862e8cadb916e9b4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afc9ec",
  "name": "FUN_00afc9ec",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26e1a7652d72235f75318227b7fd661a4596155383bcb5580f50e530cd8ef7de",
  "source_text_sha256": "26e1a7652d72235f75318227b7fd661a4596155383bcb5580f50e530cd8ef7de",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afc9ec",
        "00afca3f"
      ]
    ],
    "bytes_sha256": "db470d61e4524e5dbd8cd28ba933d4b667c5c1555d107a90d1b6ca4c6406c3bc",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1109 bytes

~~~c

void FUN_00afc9ec(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00afbec8 with catch @ 00afca0c */
                    /* catch() { ... } // from try @ 00afbe98 with catch @ 00afca10
                       catch() { ... } // from try @ 00afbf74 with catch @ 00afca10 */
                    /* catch() { ... } // from try @ 00afbd54 with catch @ 00afca14 */
                    /* catch() { ... } // from try @ 00afc580 with catch @ 00afca18 */
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
                    /* catch() { ... } // from try @ 00afc544 with catch @ 00afca1c
                       catch() { ... } // from try @ 00afc628 with catch @ 00afca1c */
                    /* catch() { ... } // from try @ 00afc300 with catch @ 00afca20 */
  *(int *)(lVar1 + 0x84c70) = *(int *)(lVar1 + 0x84c70) + param_3;
                    /* catch() { ... } // from try @ 00afc2c4 with catch @ 00afca38
                       catch() { ... } // from try @ 00afc3a8 with catch @ 00afca38 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afc9ec"></a> `00afc9ec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afc9f0"></a> `00afc9f0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc9f4"></a> `00afc9f4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afc9f8"></a> `00afc9f8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afc9fc"></a> `00afc9fc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afca00"></a> `00afca00` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afca04"></a> `00afca04` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afca08"></a> `00afca08` | `ac 52 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afca0c"></a> `00afca0c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afca10"></a> `00afca10` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afca14"></a> `00afca14` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afca18"></a> `00afca18` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afca1c"></a> `00afca1c` | `09 8e 89 52` | mov w9,#0x4c70 | `FALL_THROUGH`
<a id="insn-00afca20"></a> `00afca20` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afca24"></a> `00afca24` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afca28"></a> `00afca28` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00afca2c"></a> `00afca2c` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afca30"></a> `00afca30` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afca34"></a> `00afca34` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afca38"></a> `00afca38` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afca3c"></a> `00afca3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afc9ec`](#insn-00afc9ec) 範囲 `[['00afc9ec', '00afca0b']]`
  - `FALL_THROUGH` [`00afca08`](#insn-00afca08) → [`00afca0c`](#insn-00afca0c)
- ブロック [`00afca0c`](#insn-00afca0c) 範囲 `[['00afca0c', '00afca0f']]`
  - `FALL_THROUGH` [`00afca0c`](#insn-00afca0c) → [`00afca10`](#insn-00afca10)
- ブロック [`00afca10`](#insn-00afca10) 範囲 `[['00afca10', '00afca13']]`
  - `FALL_THROUGH` [`00afca10`](#insn-00afca10) → [`00afca14`](#insn-00afca14)
- ブロック [`00afca14`](#insn-00afca14) 範囲 `[['00afca14', '00afca17']]`
  - `FALL_THROUGH` [`00afca14`](#insn-00afca14) → [`00afca18`](#insn-00afca18)
- ブロック [`00afca18`](#insn-00afca18) 範囲 `[['00afca18', '00afca1b']]`
  - `FALL_THROUGH` [`00afca18`](#insn-00afca18) → [`00afca1c`](#insn-00afca1c)
- ブロック [`00afca1c`](#insn-00afca1c) 範囲 `[['00afca1c', '00afca1f']]`
  - `FALL_THROUGH` [`00afca1c`](#insn-00afca1c) → [`00afca20`](#insn-00afca20)
- ブロック [`00afca20`](#insn-00afca20) 範囲 `[['00afca20', '00afca37']]`
  - `FALL_THROUGH` [`00afca34`](#insn-00afca34) → [`00afca38`](#insn-00afca38)
- ブロック [`00afca38`](#insn-00afca38) 範囲 `[['00afca38', '00afca3f']]`

## 命令位置別の参照

- [`00afc9ec`](#insn-00afc9ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc9f0`](#insn-00afc9f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc9f4`](#insn-00afc9f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afca08`](#insn-00afca08) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afca30`](#insn-00afca30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afca34`](#insn-00afca34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afca38`](#insn-00afca38) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afc9ec`](#insn-00afc9ec)

~~~json
{
  "source": "00afc9ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc9f0`](#insn-00afc9f0)

~~~json
{
  "source": "00afc9f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc9f4`](#insn-00afc9f4)

~~~json
{
  "source": "00afc9f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afca08`](#insn-00afca08)

~~~json
{
  "source": "00afca08",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afca30`](#insn-00afca30)

~~~json
{
  "source": "00afca30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afca34`](#insn-00afca34)

~~~json
{
  "source": "00afca34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afca38`](#insn-00afca38)

~~~json
{
  "source": "00afca38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
