# 00afaed8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0169.md#review-e0d5e71e95689b4a48c4483af2461ec3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afb300`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afb/00afb300.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-16b4be76bf3aadc618cd7807c1a5eb42)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaed8",
  "name": "FUN_00afaed8",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6404f5f907fc188b6cc40f80a73dfb348b173ba21005d2f43609bcd6a5f20f7c",
  "source_text_sha256": "6404f5f907fc188b6cc40f80a73dfb348b173ba21005d2f43609bcd6a5f20f7c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaed8",
        "00afaf23"
      ]
    ],
    "bytes_sha256": "553ea8044dc4a45cf1cfbc24281b7e8de8b08d7596695c3fc3f5dd8dcd6e8efd",
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

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 403 bytes

~~~c

void FUN_00afaed8(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afaeec to 00bfaf07 has its CatchHandler @ 00afb228 */
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afaf08 to 00bfaf97 has its CatchHandler @ 00afaa30 */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b90) = param_3 & 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaed8"></a> `00afaed8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afaedc"></a> `00afaedc` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaee0"></a> `00afaee0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaee4"></a> `00afaee4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afaee8"></a> `00afaee8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afaeec"></a> `00afaeec` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afaef0"></a> `00afaef0` | `55 00 00 12` | and w21,w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afaef4"></a> `00afaef4` | `71 59 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afaef8"></a> `00afaef8` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afaefc"></a> `00afaefc` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afaf00"></a> `00afaf00` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afaf04"></a> `00afaf04` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afaf08"></a> `00afaf08` | `09 72 89 52` | mov w9,#0x4b90 | `FALL_THROUGH`
<a id="insn-00afaf0c"></a> `00afaf0c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afaf10"></a> `00afaf10` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afaf14"></a> `00afaf14` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaf18"></a> `00afaf18` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaf1c"></a> `00afaf1c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afaf20"></a> `00afaf20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaed8`](#insn-00afaed8) 範囲 `[['00afaed8', '00afaeeb']]`
  - `FALL_THROUGH` [`00afaee8`](#insn-00afaee8) → [`00afaeec`](#insn-00afaeec)
- ブロック [`00afaeec`](#insn-00afaeec) 範囲 `[['00afaeec', '00afaf07']]`
  - `FALL_THROUGH` [`00afaf04`](#insn-00afaf04) → [`00afaf08`](#insn-00afaf08)
- ブロック [`00afaf08`](#insn-00afaf08) 範囲 `[['00afaf08', '00afaf23']]`

## 命令位置別の参照

- [`00afaed8`](#insn-00afaed8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaedc`](#insn-00afaedc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaee0`](#insn-00afaee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaef4`](#insn-00afaef4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afaf14`](#insn-00afaf14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf18`](#insn-00afaf18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf1c`](#insn-00afaf1c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaed8`](#insn-00afaed8)

~~~json
{
  "source": "00afaed8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaedc`](#insn-00afaedc)

~~~json
{
  "source": "00afaedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaee0`](#insn-00afaee0)

~~~json
{
  "source": "00afaee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaef4`](#insn-00afaef4)

~~~json
{
  "source": "00afaef4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf14`](#insn-00afaf14)

~~~json
{
  "source": "00afaf14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf18`](#insn-00afaf18)

~~~json
{
  "source": "00afaf18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf1c`](#insn-00afaf1c)

~~~json
{
  "source": "00afaf1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
