# 00bd1adc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd1a40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1a40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-691a061dc4af4065628daf316130f504)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd2ad0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd2/00bd2ad0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0082.md#compare-7cbc5703485364085435bfb16402215e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1adc",
  "name": "_ZN8firebase4auth23weak_password_exception10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ffad6ce43be75d36c0cfa05812371c45998902b2e0b9c99fab048e5b69f039d",
  "source_text_sha256": "2ffad6ce43be75d36c0cfa05812371c45998902b2e0b9c99fab048e5b69f039d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1adc",
        "00bd1b17"
      ]
    ],
    "bytes_sha256": "9810d98a080237b256c4dc611f66db697c76433c44b692cc4b66d2cb823faf46",
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

- [00c5b0d0](../00c5b/00c5b0d0.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 247 bytes

~~~c

undefined8 _ZN8firebase4auth23weak_password_exception10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01126a20 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1adc"></a> `00bd1adc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd1ae0"></a> `00bd1ae0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1ae4"></a> `00bd1ae4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd1ae8"></a> `00bd1ae8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bd1aec"></a> `00bd1aec` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bd1af0"></a> `00bd1af0` | `8b 00 00 54` | b.lt 0x00bd1b00 | `CONDITIONAL_JUMP`
<a id="insn-00bd1af4"></a> `00bd1af4` | `c0 b6 ff 90` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bd1af8"></a> `00bd1af8` | `00 34 15 91` | add x0,x0,#0x54d | `FALL_THROUGH`
<a id="insn-00bd1afc"></a> `00bd1afc` | `75 25 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1b00"></a> `00bd1b00` | `a8 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd1b04"></a> `00bd1b04` | `08 81 28 91` | add x8,x8,#0xa20 | `FALL_THROUGH`
<a id="insn-00bd1b08"></a> `00bd1b08` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bd1b0c"></a> `00bd1b0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1b10"></a> `00bd1b10` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd1b14"></a> `00bd1b14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1adc`](#insn-00bd1adc) 範囲 `[['00bd1adc', '00bd1af3']]`
  - `CONDITIONAL_JUMP` [`00bd1af0`](#insn-00bd1af0) → [`00bd1b00`](#insn-00bd1b00)
  - `FALL_THROUGH` [`00bd1af0`](#insn-00bd1af0) → [`00bd1af4`](#insn-00bd1af4)
- ブロック [`00bd1af4`](#insn-00bd1af4) 範囲 `[['00bd1af4', '00bd1aff']]`
  - `FALL_THROUGH` [`00bd1afc`](#insn-00bd1afc) → [`00bd1b00`](#insn-00bd1b00)
- ブロック [`00bd1b00`](#insn-00bd1b00) 範囲 `[['00bd1b00', '00bd1b17']]`

## 命令位置別の参照

- [`00bd1adc`](#insn-00bd1adc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1ae0`](#insn-00bd1ae0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1af0`](#insn-00bd1af0) → [`00bd1b00`](#insn-00bd1b00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1af8`](#insn-00bd1af8) → `002a954d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd1afc`](#insn-00bd1afc) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bd1b08`](#insn-00bd1b08) → `01126a20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1b0c`](#insn-00bd1b0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1adc`](#insn-00bd1adc)

~~~json
{
  "source": "00bd1adc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1ae0`](#insn-00bd1ae0)

~~~json
{
  "source": "00bd1ae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1af0`](#insn-00bd1af0)

~~~json
{
  "source": "00bd1af0",
  "target": "00bd1b00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1af8`](#insn-00bd1af8)

~~~json
{
  "source": "00bd1af8",
  "target": "002a954d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a954d",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002a954d",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd1afc`](#insn-00bd1afc)

~~~json
{
  "source": "00bd1afc",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1b08`](#insn-00bd1b08)

~~~json
{
  "source": "00bd1b08",
  "target": "01126a20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1b0c`](#insn-00bd1b0c)

~~~json
{
  "source": "00bd1b0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
