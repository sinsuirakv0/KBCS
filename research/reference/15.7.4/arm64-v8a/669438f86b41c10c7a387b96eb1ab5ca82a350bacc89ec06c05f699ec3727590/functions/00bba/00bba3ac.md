# 00bba3ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bba368`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba368.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-be7aa6ee6ac7b3e80ed1129f1a8c21ef)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c36df4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36df4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-eac74684ee44b9b5c57ab006db60f017)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba3ac",
  "name": "_ZNSt6__ndk111regex_errorC2ENS_15regex_constants10error_typeE",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4e0b489b4b32b40d0144fb7a65e828ca671d0b2af291a2ac6b2573bce4ff940d",
  "source_text_sha256": "4e0b489b4b32b40d0144fb7a65e828ca671d0b2af291a2ac6b2573bce4ff940d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bba3ac",
        "00bba417"
      ]
    ],
    "bytes_sha256": "fef95358f1131ec4703e2c0fb9c7b83738ea550325ac9724fc2030316f9ac691",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdd960](../00bdd/00bdd960.md)

## 呼び出し先

- [00bdda80](../00bdd/00bdda80.md)

## 関連文字列（未確認候補）

~~~text
"Unknown error type"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 930 bytes

~~~c

void _ZNSt6__ndk111regex_errorC2ENS_15regex_constants10error_typeE(long *param_1,int param_2)

{
  char *pcVar1;
  
                    /* try { // try from 00bba3b4 to 00cba3b7 has its CatchHandler @ 00bbad64 */
                    /* try { // try from 00bba3cc to 00cba3cf has its CatchHandler @ 00bbad60 */
  if (param_2 - 1U < 0x11) {
    pcVar1 = &DAT_002fc770 + *(int *)(&DAT_002fc770 + (ulong)(param_2 - 1U) * 4);
  }
  else {
                    /* try { // try from 00bba3e4 to 00cba3e7 has its CatchHandler @ 00bbad5c */
    pcVar1 = "Unknown error type";
  }
  _ZNSt13runtime_errorC2EPKc(param_1,pcVar1);
                    /* try { // try from 00bba3fc to 00cba3ff has its CatchHandler @ 00bbad58 */
  *param_1 = (long)(PTR__ZTVNSt6__ndk111regex_errorE_00c1bfe0 + 0x10);
  *(int *)(param_1 + 2) = param_2;
                    /* try { // try from 00bba414 to 00cba417 has its CatchHandler @ 00bbad54 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bba3ac"></a> `00bba3ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bba3b0"></a> `00bba3b0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bba3b4"></a> `00bba3b4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba3b8"></a> `00bba3b8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bba3bc"></a> `00bba3bc` | `28 04 00 51` | sub w8,w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bba3c0"></a> `00bba3c0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00bba3c4"></a> `00bba3c4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bba3c8"></a> `00bba3c8` | `1f 41 00 71` | cmp w8,#0x10 | `FALL_THROUGH`
<a id="insn-00bba3cc"></a> `00bba3cc` | `c8 00 00 54` | b.hi 0x00bba3e4 | `CONDITIONAL_JUMP`
<a id="insn-00bba3d0"></a> `00bba3d0` | `09 ba ff d0` | adrp x9,0x2fc000 | `FALL_THROUGH`
<a id="insn-00bba3d4"></a> `00bba3d4` | `29 c1 1d 91` | add x9,x9,#0x770 | `FALL_THROUGH`
<a id="insn-00bba3d8"></a> `00bba3d8` | `28 59 a8 b8` | ldrsw x8,[x9, w8, UXTW #0x2] | `FALL_THROUGH`
<a id="insn-00bba3dc"></a> `00bba3dc` | `21 01 08 8b` | add x1,x9,x8 | `FALL_THROUGH`
<a id="insn-00bba3e0"></a> `00bba3e0` | `03 00 00 14` | b 0x00bba3ec | `UNCONDITIONAL_JUMP`
<a id="insn-00bba3e4"></a> `00bba3e4` | `41 b7 ff 90` | adrp x1,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bba3e8"></a> `00bba3e8` | `21 a0 05 91` | add x1,x1,#0x168 | `FALL_THROUGH`
<a id="insn-00bba3ec"></a> `00bba3ec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bba3f0"></a> `00bba3f0` | `a4 8d 00 94` | bl 0x00bdda80 | `UNCONDITIONAL_CALL`
<a id="insn-00bba3f4"></a> `00bba3f4` | `08 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bba3f8"></a> `00bba3f8` | `08 f1 47 f9` | ldr x8,[x8, #0xfe0] | `FALL_THROUGH`
<a id="insn-00bba3fc"></a> `00bba3fc` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bba400"></a> `00bba400` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bba404"></a> `00bba404` | `93 12 00 b9` | str w19,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bba408"></a> `00bba408` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba40c"></a> `00bba40c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bba410"></a> `00bba410` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bba414"></a> `00bba414` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bba3ac`](#insn-00bba3ac) 範囲 `[['00bba3ac', '00bba3b3']]`
  - `FALL_THROUGH` [`00bba3b0`](#insn-00bba3b0) → [`00bba3b4`](#insn-00bba3b4)
- ブロック [`00bba3b4`](#insn-00bba3b4) 範囲 `[['00bba3b4', '00bba3cb']]`
  - `FALL_THROUGH` [`00bba3c8`](#insn-00bba3c8) → [`00bba3cc`](#insn-00bba3cc)
- ブロック [`00bba3cc`](#insn-00bba3cc) 範囲 `[['00bba3cc', '00bba3cf']]`
  - `CONDITIONAL_JUMP` [`00bba3cc`](#insn-00bba3cc) → [`00bba3e4`](#insn-00bba3e4)
  - `FALL_THROUGH` [`00bba3cc`](#insn-00bba3cc) → [`00bba3d0`](#insn-00bba3d0)
- ブロック [`00bba3d0`](#insn-00bba3d0) 範囲 `[['00bba3d0', '00bba3e3']]`
  - `UNCONDITIONAL_JUMP` [`00bba3e0`](#insn-00bba3e0) → [`00bba3ec`](#insn-00bba3ec)
- ブロック [`00bba3e4`](#insn-00bba3e4) 範囲 `[['00bba3e4', '00bba3eb']]`
  - `FALL_THROUGH` [`00bba3e8`](#insn-00bba3e8) → [`00bba3ec`](#insn-00bba3ec)
- ブロック [`00bba3ec`](#insn-00bba3ec) 範囲 `[['00bba3ec', '00bba3fb']]`
  - `FALL_THROUGH` [`00bba3f8`](#insn-00bba3f8) → [`00bba3fc`](#insn-00bba3fc)
- ブロック [`00bba3fc`](#insn-00bba3fc) 範囲 `[['00bba3fc', '00bba413']]`
  - `FALL_THROUGH` [`00bba410`](#insn-00bba410) → [`00bba414`](#insn-00bba414)
- ブロック [`00bba414`](#insn-00bba414) 範囲 `[['00bba414', '00bba417']]`

## 命令位置別の参照

- [`00bba3b0`](#insn-00bba3b0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba3b4`](#insn-00bba3b4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba3cc`](#insn-00bba3cc) → [`00bba3e4`](#insn-00bba3e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba3d8`](#insn-00bba3d8) → `002fc770`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba3e0`](#insn-00bba3e0) → [`00bba3ec`](#insn-00bba3ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba3e8`](#insn-00bba3e8) → `002a2168`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bba3f0`](#insn-00bba3f0) → [`00bdda80`](../00bdd/00bdda80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdda80` · 推定シンボル `None` · 推定型 `None`
- [`00bba3f8`](#insn-00bba3f8) → `00c1bfe0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bba400`](#insn-00bba400) → `00c16018`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bba408`](#insn-00bba408) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba40c`](#insn-00bba40c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bba3b0`](#insn-00bba3b0)

~~~json
{
  "source": "00bba3b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba3b4`](#insn-00bba3b4)

~~~json
{
  "source": "00bba3b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba3cc`](#insn-00bba3cc)

~~~json
{
  "source": "00bba3cc",
  "target": "00bba3e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba3d8`](#insn-00bba3d8)

~~~json
{
  "source": "00bba3d8",
  "target": "002fc770",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba3e0`](#insn-00bba3e0)

~~~json
{
  "source": "00bba3e0",
  "target": "00bba3ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba3e8`](#insn-00bba3e8)

~~~json
{
  "source": "00bba3e8",
  "target": "002a2168",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2168",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "556e6b6e6f776e206572726f72207479706500",
  "capture_start": "002a2168",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bba3f0`](#insn-00bba3f0)

~~~json
{
  "source": "00bba3f0",
  "target": "00bdda80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba3f8`](#insn-00bba3f8)

~~~json
{
  "source": "00bba3f8",
  "target": "00c1bfe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bfe0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bba400`](#insn-00bba400)

~~~json
{
  "source": "00bba400",
  "target": "00c16018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16008",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bba408`](#insn-00bba408)

~~~json
{
  "source": "00bba408",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba40c`](#insn-00bba40c)

~~~json
{
  "source": "00bba40c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
