# 00afaaf4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0168.md#review-2b7f2e766a254ab7d9647933c6e61a96)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afaf1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaf1c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-532cc50039a89d4165405ad259303c48)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaaf4",
  "name": "FUN_00afaaf4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35e2efa5d1d9d37a4f47b821ab51a3e86a6485294542108048c2c4465645a6ee",
  "source_text_sha256": "35e2efa5d1d9d37a4f47b821ab51a3e86a6485294542108048c2c4465645a6ee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaaf4",
        "00afab3f"
      ]
    ],
    "bytes_sha256": "62816ed209cacba1adf509bf13f1c681afbce38faddaed22601f58e395f794f7",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)
- [00a51dcc](../00a51/00a51dcc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_00afaaf4(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afab08 to 00bfab1f has its CatchHandler @ 00afb214 */
  lVar1 = FUN_008514b8();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a98) = param_3 & 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaaf4"></a> `00afaaf4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afaaf8"></a> `00afaaf8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaafc"></a> `00afaafc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afab00"></a> `00afab00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afab04"></a> `00afab04` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afab08"></a> `00afab08` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afab0c"></a> `00afab0c` | `55 00 00 12` | and w21,w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afab10"></a> `00afab10` | `6a 5a f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afab14"></a> `00afab14` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afab18"></a> `00afab18` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afab1c"></a> `00afab1c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afab20"></a> `00afab20` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afab24"></a> `00afab24` | `09 53 89 52` | mov w9,#0x4a98 | `FALL_THROUGH`
<a id="insn-00afab28"></a> `00afab28` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afab2c"></a> `00afab2c` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afab30"></a> `00afab30` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afab34"></a> `00afab34` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afab38"></a> `00afab38` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afab3c"></a> `00afab3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaaf4`](#insn-00afaaf4) 範囲 `[['00afaaf4', '00afab07']]`
  - `FALL_THROUGH` [`00afab04`](#insn-00afab04) → [`00afab08`](#insn-00afab08)
- ブロック [`00afab08`](#insn-00afab08) 範囲 `[['00afab08', '00afab3f']]`

## 命令位置別の参照

- [`00afaaf4`](#insn-00afaaf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaaf8`](#insn-00afaaf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaafc`](#insn-00afaafc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab10`](#insn-00afab10) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afab30`](#insn-00afab30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab34`](#insn-00afab34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab38`](#insn-00afab38) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaaf4`](#insn-00afaaf4)

~~~json
{
  "source": "00afaaf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaaf8`](#insn-00afaaf8)

~~~json
{
  "source": "00afaaf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaafc`](#insn-00afaafc)

~~~json
{
  "source": "00afaafc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab10`](#insn-00afab10)

~~~json
{
  "source": "00afab10",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afab30`](#insn-00afab30)

~~~json
{
  "source": "00afab30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab34`](#insn-00afab34)

~~~json
{
  "source": "00afab34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab38`](#insn-00afab38)

~~~json
{
  "source": "00afab38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
