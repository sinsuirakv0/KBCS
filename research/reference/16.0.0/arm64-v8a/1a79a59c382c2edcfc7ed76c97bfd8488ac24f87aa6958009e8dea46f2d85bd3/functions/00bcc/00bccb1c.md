# 00bccb1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5d61c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d61c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-e3b7ae26a7f282298e9878b0f5ff9d70)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bccf44`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf44.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-3d2d7f60777d2c314830aed7044c80d6)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccb1c",
  "name": "_ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef9fcdbad72f14d9140fd777c4e2c38a0e65f242e5a4449899385b298f3c44cb",
  "source_text_sha256": "ef9fcdbad72f14d9140fd777c4e2c38a0e65f242e5a4449899385b298f3c44cb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccb1c",
        "00bccb57"
      ]
    ],
    "bytes_sha256": "f04d9fa65fca3b2f7394faff7c6b43221add42066a81e89305cc248f1b6ed9f4",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ac00](../00c5a/00c5ac00.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 319 bytes

~~~c

undefined8 _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE(uint param_1)

{
                    /* try { // try from 00bccb1c to 00cccbcf has its CatchHandler @ 00bcc3d4 */
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_01126428)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccb1c"></a> `00bccb1c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccb20"></a> `00bccb20` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccb24"></a> `00bccb24` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccb28"></a> `00bccb28` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bccb2c"></a> `00bccb2c` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bccb30"></a> `00bccb30` | `8b 00 00 54` | b.lt 0x00bccb40 | `CONDITIONAL_JUMP`
<a id="insn-00bccb34"></a> `00bccb34` | `e0 b6 ff 90` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bccb38"></a> `00bccb38` | `00 68 0a 91` | add x0,x0,#0x29a | `FALL_THROUGH`
<a id="insn-00bccb3c"></a> `00bccb3c` | `31 38 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bccb40"></a> `00bccb40` | `c8 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccb44"></a> `00bccb44` | `08 a1 10 91` | add x8,x8,#0x428 | `FALL_THROUGH`
<a id="insn-00bccb48"></a> `00bccb48` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bccb4c"></a> `00bccb4c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccb50"></a> `00bccb50` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccb54"></a> `00bccb54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccb1c`](#insn-00bccb1c) 範囲 `[['00bccb1c', '00bccb33']]`
  - `CONDITIONAL_JUMP` [`00bccb30`](#insn-00bccb30) → [`00bccb40`](#insn-00bccb40)
  - `FALL_THROUGH` [`00bccb30`](#insn-00bccb30) → [`00bccb34`](#insn-00bccb34)
- ブロック [`00bccb34`](#insn-00bccb34) 範囲 `[['00bccb34', '00bccb3f']]`
  - `FALL_THROUGH` [`00bccb3c`](#insn-00bccb3c) → [`00bccb40`](#insn-00bccb40)
- ブロック [`00bccb40`](#insn-00bccb40) 範囲 `[['00bccb40', '00bccb57']]`

## 命令位置別の参照

- [`00bccb1c`](#insn-00bccb1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb20`](#insn-00bccb20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb30`](#insn-00bccb30) → [`00bccb40`](#insn-00bccb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb38`](#insn-00bccb38) → `002a829a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccb3c`](#insn-00bccb3c) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bccb48`](#insn-00bccb48) → `01126428`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccb4c`](#insn-00bccb4c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccb1c`](#insn-00bccb1c)

~~~json
{
  "source": "00bccb1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb20`](#insn-00bccb20)

~~~json
{
  "source": "00bccb20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb30`](#insn-00bccb30)

~~~json
{
  "source": "00bccb30",
  "target": "00bccb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb38`](#insn-00bccb38)

~~~json
{
  "source": "00bccb38",
  "target": "002a829a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a829a",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002a829a",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bccb3c`](#insn-00bccb3c)

~~~json
{
  "source": "00bccb3c",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccb48`](#insn-00bccb48)

~~~json
{
  "source": "00bccb48",
  "target": "01126428",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126428",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb4c`](#insn-00bccb4c)

~~~json
{
  "source": "00bccb4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
