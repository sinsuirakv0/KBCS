# 00afaaac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0168.md#review-eeba5e23c83d51395a37e825499cb6f7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afaed4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaed4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-78824f1b1ad12f43d83dbb5f8dca1507)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaaac",
  "name": "FUN_00afaaac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "68231e94d94b7338fdbc373d4bae2a219ec77b92280f9f77904d4ae7019cf451",
  "source_text_sha256": "68231e94d94b7338fdbc373d4bae2a219ec77b92280f9f77904d4ae7019cf451",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaaac",
        "00afaaf3"
      ]
    ],
    "bytes_sha256": "51c5dcf186c46aca5bce44abee3f032bab8a9ffcb450e0a7b90301fb94616ae5",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 377 bytes

~~~c

bool FUN_00afaaac(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afaacc to 00bfaae3 has its CatchHandler @ 00afb218 */
                    /* try { // try from 00afaae4 to 00bfab07 has its CatchHandler @ 00afaa30 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a98) != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaaac"></a> `00afaaac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afaab0"></a> `00afaab0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaab4"></a> `00afaab4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afaab8"></a> `00afaab8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afaabc"></a> `00afaabc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afaac0"></a> `00afaac0` | `7e 5a f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afaac4"></a> `00afaac4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afaac8"></a> `00afaac8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afaacc"></a> `00afaacc` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afaad0"></a> `00afaad0` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afaad4"></a> `00afaad4` | `09 53 89 52` | mov w9,#0x4a98 | `FALL_THROUGH`
<a id="insn-00afaad8"></a> `00afaad8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afaadc"></a> `00afaadc` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afaae0"></a> `00afaae0` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afaae4"></a> `00afaae4` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afaae8"></a> `00afaae8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaaec"></a> `00afaaec` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afaaf0"></a> `00afaaf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaaac`](#insn-00afaaac) 範囲 `[['00afaaac', '00afaacb']]`
  - `FALL_THROUGH` [`00afaac8`](#insn-00afaac8) → [`00afaacc`](#insn-00afaacc)
- ブロック [`00afaacc`](#insn-00afaacc) 範囲 `[['00afaacc', '00afaae3']]`
  - `FALL_THROUGH` [`00afaae0`](#insn-00afaae0) → [`00afaae4`](#insn-00afaae4)
- ブロック [`00afaae4`](#insn-00afaae4) 範囲 `[['00afaae4', '00afaaf3']]`

## 命令位置別の参照

- [`00afaaac`](#insn-00afaaac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaab0`](#insn-00afaab0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaac0`](#insn-00afaac0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afaae8`](#insn-00afaae8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaaec`](#insn-00afaaec) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaaac`](#insn-00afaaac)

~~~json
{
  "source": "00afaaac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaab0`](#insn-00afaab0)

~~~json
{
  "source": "00afaab0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaac0`](#insn-00afaac0)

~~~json
{
  "source": "00afaac0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaae8`](#insn-00afaae8)

~~~json
{
  "source": "00afaae8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaaec`](#insn-00afaaec)

~~~json
{
  "source": "00afaaec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
