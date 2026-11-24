# 00b4defc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4cf08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0075.md#compare-dff0deeaa5ebee87c402e9e39066c244)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4defc",
  "name": "_ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8617d7719cde405fdc6ff59b4b71efa230593e78b3de3c47e852ed7e6c81510f",
  "source_text_sha256": "8617d7719cde405fdc6ff59b4b71efa230593e78b3de3c47e852ed7e6c81510f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4defc",
        "00b4df37"
      ]
    ],
    "bytes_sha256": "e61f6d11e1ce417abbf874f4445537ec6014e0234d256d9326ff61e8b5b0e994",
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

## 疑似コード / UTF-8 250 bytes

~~~c

undefined8 _ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_01126d38 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4defc"></a> `00b4defc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4df00"></a> `00b4df00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4df04"></a> `00b4df04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4df08"></a> `00b4df08` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00b4df0c"></a> `00b4df0c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b4df10"></a> `00b4df10` | `8b 00 00 54` | b.lt 0x00b4df20 | `CONDITIONAL_JUMP`
<a id="insn-00b4df14"></a> `00b4df14` | `c0 ba ff f0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00b4df18"></a> `00b4df18` | `00 8c 11 91` | add x0,x0,#0x463 | `FALL_THROUGH`
<a id="insn-00b4df1c"></a> `00b4df1c` | `61 38 04 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4df20"></a> `00b4df20` | `c8 2e 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4df24"></a> `00b4df24` | `08 e1 34 91` | add x8,x8,#0xd38 | `FALL_THROUGH`
<a id="insn-00b4df28"></a> `00b4df28` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00b4df2c"></a> `00b4df2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4df30"></a> `00b4df30` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4df34"></a> `00b4df34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4defc`](#insn-00b4defc) 範囲 `[['00b4defc', '00b4df13']]`
  - `CONDITIONAL_JUMP` [`00b4df10`](#insn-00b4df10) → [`00b4df20`](#insn-00b4df20)
  - `FALL_THROUGH` [`00b4df10`](#insn-00b4df10) → [`00b4df14`](#insn-00b4df14)
- ブロック [`00b4df14`](#insn-00b4df14) 範囲 `[['00b4df14', '00b4df1f']]`
  - `FALL_THROUGH` [`00b4df1c`](#insn-00b4df1c) → [`00b4df20`](#insn-00b4df20)
- ブロック [`00b4df20`](#insn-00b4df20) 範囲 `[['00b4df20', '00b4df37']]`

## 命令位置別の参照

- [`00b4defc`](#insn-00b4defc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4df00`](#insn-00b4df00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4df10`](#insn-00b4df10) → [`00b4df20`](#insn-00b4df20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4df18`](#insn-00b4df18) → `002a8463`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4df1c`](#insn-00b4df1c) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00b4df28`](#insn-00b4df28) → `01126d38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4df2c`](#insn-00b4df2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4defc`](#insn-00b4defc)

~~~json
{
  "source": "00b4defc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4df00`](#insn-00b4df00)

~~~json
{
  "source": "00b4df00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4df10`](#insn-00b4df10)

~~~json
{
  "source": "00b4df10",
  "target": "00b4df20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4df18`](#insn-00b4df18)

~~~json
{
  "source": "00b4df18",
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
- 参照命令 [`00b4df1c`](#insn-00b4df1c)

~~~json
{
  "source": "00b4df1c",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4df28`](#insn-00b4df28)

~~~json
{
  "source": "00b4df28",
  "target": "01126d38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4df2c`](#insn-00b4df2c)

~~~json
{
  "source": "00b4df2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
