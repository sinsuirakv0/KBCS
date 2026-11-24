# 00bcdc8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccc98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccc98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-1dacce06f1e26c489afb7b7262a8f411)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdc8c",
  "name": "_ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "de91190e4d79de5ad91e82de37934469bba60d1e046fc00546abbda034ea39a1",
  "source_text_sha256": "de91190e4d79de5ad91e82de37934469bba60d1e046fc00546abbda034ea39a1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdc8c",
        "00bcdcc7"
      ]
    ],
    "bytes_sha256": "1b2bc83b05f8c3bd8f8ceddb48feecfe5814256ba7582215f599d49de152464c",
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

- [00c5c0a0](../00c5c/00c5c0a0.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 406 bytes

~~~c

undefined8 _ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE(uint param_1)

{
                    /* try { // try from 00bcdc94 to 00ccdc9f has its CatchHandler @ 00bcf964 */
                    /* try { // try from 00bcdca0 to 00ccdd63 has its CatchHandler @ 00bcd634 */
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_011278c0)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdc8c"></a> `00bcdc8c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcdc90"></a> `00bcdc90` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdc94"></a> `00bcdc94` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdc98"></a> `00bcdc98` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bcdc9c"></a> `00bcdc9c` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bcdca0"></a> `00bcdca0` | `8b 00 00 54` | b.lt 0x00bcdcb0 | `CONDITIONAL_JUMP`
<a id="insn-00bcdca4"></a> `00bcdca4` | `c0 b6 ff f0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bcdca8"></a> `00bcdca8` | `00 8c 11 91` | add x0,x0,#0x463 | `FALL_THROUGH`
<a id="insn-00bcdcac"></a> `00bcdcac` | `fd 38 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcb0"></a> `00bcdcb0` | `c8 2a 00 d0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdcb4"></a> `00bcdcb4` | `08 01 23 91` | add x8,x8,#0x8c0 | `FALL_THROUGH`
<a id="insn-00bcdcb8"></a> `00bcdcb8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bcdcbc"></a> `00bcdcbc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdcc0"></a> `00bcdcc0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcdcc4"></a> `00bcdcc4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdc8c`](#insn-00bcdc8c) 範囲 `[['00bcdc8c', '00bcdc93']]`
  - `FALL_THROUGH` [`00bcdc90`](#insn-00bcdc90) → [`00bcdc94`](#insn-00bcdc94)
- ブロック [`00bcdc94`](#insn-00bcdc94) 範囲 `[['00bcdc94', '00bcdc9f']]`
  - `FALL_THROUGH` [`00bcdc9c`](#insn-00bcdc9c) → [`00bcdca0`](#insn-00bcdca0)
- ブロック [`00bcdca0`](#insn-00bcdca0) 範囲 `[['00bcdca0', '00bcdca3']]`
  - `CONDITIONAL_JUMP` [`00bcdca0`](#insn-00bcdca0) → [`00bcdcb0`](#insn-00bcdcb0)
  - `FALL_THROUGH` [`00bcdca0`](#insn-00bcdca0) → [`00bcdca4`](#insn-00bcdca4)
- ブロック [`00bcdca4`](#insn-00bcdca4) 範囲 `[['00bcdca4', '00bcdcaf']]`
  - `FALL_THROUGH` [`00bcdcac`](#insn-00bcdcac) → [`00bcdcb0`](#insn-00bcdcb0)
- ブロック [`00bcdcb0`](#insn-00bcdcb0) 範囲 `[['00bcdcb0', '00bcdcc7']]`

## 命令位置別の参照

- [`00bcdc8c`](#insn-00bcdc8c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc90`](#insn-00bcdc90) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdca0`](#insn-00bcdca0) → [`00bcdcb0`](#insn-00bcdcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdca8`](#insn-00bcdca8) → `002a8463`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcdcac`](#insn-00bcdcac) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcb8`](#insn-00bcdcb8) → `011278c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdcbc`](#insn-00bcdcbc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdc8c`](#insn-00bcdc8c)

~~~json
{
  "source": "00bcdc8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc90`](#insn-00bcdc90)

~~~json
{
  "source": "00bcdc90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdca0`](#insn-00bcdca0)

~~~json
{
  "source": "00bcdca0",
  "target": "00bcdcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdca8`](#insn-00bcdca8)

~~~json
{
  "source": "00bcdca8",
  "target": "002a8463",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8463",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002a8463",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcdcac`](#insn-00bcdcac)

~~~json
{
  "source": "00bcdcac",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcb8`](#insn-00bcdcb8)

~~~json
{
  "source": "00bcdcb8",
  "target": "011278c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdcbc`](#insn-00bcdcbc)

~~~json
{
  "source": "00bcdcbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
