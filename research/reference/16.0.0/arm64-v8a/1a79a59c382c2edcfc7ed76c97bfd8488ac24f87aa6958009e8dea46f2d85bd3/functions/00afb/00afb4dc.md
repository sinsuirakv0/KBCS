# 00afb4dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0169.md#review-561e2992e8b88fcff55959f90ce9c861)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afb904`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afb/00afb904.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-61f66514710af8e9408c4c1628933214)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb4dc",
  "name": "FUN_00afb4dc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed5f1eb3c4adea43fc06bc09e94993e7e7ed0c7dbc0044a9253965ec22bbfd06",
  "source_text_sha256": "ed5f1eb3c4adea43fc06bc09e94993e7e7ed0c7dbc0044a9253965ec22bbfd06",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb4dc",
        "00afb527"
      ]
    ],
    "bytes_sha256": "9bf10a4784fc41d01c116e9e0381633b959bc79d7979060db8143df0ac058d3d",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)
- [00710298](../00710/00710298.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 403 bytes

~~~c

void FUN_00afb4dc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afb4f4 to 00bfb4ff has its CatchHandler @ 00afc9b4 */
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afb500 to 00bfb513 has its CatchHandler @ 00afc994 */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849b8) = param_3 & 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afb4dc"></a> `00afb4dc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afb4e0"></a> `00afb4e0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb4e4"></a> `00afb4e4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb4e8"></a> `00afb4e8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afb4ec"></a> `00afb4ec` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afb4f0"></a> `00afb4f0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afb4f4"></a> `00afb4f4` | `55 00 00 12` | and w21,w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afb4f8"></a> `00afb4f8` | `f0 57 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb4fc"></a> `00afb4fc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afb500"></a> `00afb500` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afb504"></a> `00afb504` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afb508"></a> `00afb508` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afb50c"></a> `00afb50c` | `09 37 89 52` | mov w9,#0x49b8 | `FALL_THROUGH`
<a id="insn-00afb510"></a> `00afb510` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb514"></a> `00afb514` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb518"></a> `00afb518` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb51c"></a> `00afb51c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb520"></a> `00afb520` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afb524"></a> `00afb524` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb4dc`](#insn-00afb4dc) 範囲 `[['00afb4dc', '00afb4f3']]`
  - `FALL_THROUGH` [`00afb4f0`](#insn-00afb4f0) → [`00afb4f4`](#insn-00afb4f4)
- ブロック [`00afb4f4`](#insn-00afb4f4) 範囲 `[['00afb4f4', '00afb4ff']]`
  - `FALL_THROUGH` [`00afb4fc`](#insn-00afb4fc) → [`00afb500`](#insn-00afb500)
- ブロック [`00afb500`](#insn-00afb500) 範囲 `[['00afb500', '00afb527']]`

## 命令位置別の参照

- [`00afb4dc`](#insn-00afb4dc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4e0`](#insn-00afb4e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4e4`](#insn-00afb4e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4f8`](#insn-00afb4f8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afb518`](#insn-00afb518) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb51c`](#insn-00afb51c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb520`](#insn-00afb520) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb4dc`](#insn-00afb4dc)

~~~json
{
  "source": "00afb4dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4e0`](#insn-00afb4e0)

~~~json
{
  "source": "00afb4e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4e4`](#insn-00afb4e4)

~~~json
{
  "source": "00afb4e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4f8`](#insn-00afb4f8)

~~~json
{
  "source": "00afb4f8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb518`](#insn-00afb518)

~~~json
{
  "source": "00afb518",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb51c`](#insn-00afb51c)

~~~json
{
  "source": "00afb51c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb520`](#insn-00afb520)

~~~json
{
  "source": "00afb520",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
