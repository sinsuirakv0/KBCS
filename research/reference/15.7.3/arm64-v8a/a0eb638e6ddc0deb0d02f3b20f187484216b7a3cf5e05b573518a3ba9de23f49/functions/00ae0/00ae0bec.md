# 00ae0bec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae0b24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0b24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-8cc32d5480b680ffbfe1dcae7b514d0f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae0c30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0061.md#compare-54528382e4b630cde8b36109b01d4129)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae0bec",
  "name": "_ZN8firebase9analytics22analytics_consent_type10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3affa88cd48b769c2fb52692647d45213d034aed0e4b977110c949a8ee2385ab",
  "source_text_sha256": "3affa88cd48b769c2fb52692647d45213d034aed0e4b977110c949a8ee2385ab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae0bec",
        "00ae0c27"
      ]
    ],
    "bytes_sha256": "afb960e54be34b20cd2662b1c1e6fa447c7cd58e8d9ead63905271b957b54b53",
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

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 224 bytes

~~~c

undefined8 _ZN8firebase9analytics22analytics_consent_type10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (3 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return (&DAT_010a00b8)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae0bec"></a> `00ae0bec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae0bf0"></a> `00ae0bf0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0bf4"></a> `00ae0bf4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae0bf8"></a> `00ae0bf8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00ae0bfc"></a> `00ae0bfc` | `1f 10 00 71` | cmp w0,#0x4 | `FALL_THROUGH`
<a id="insn-00ae0c00"></a> `00ae0c00` | `8b 00 00 54` | b.lt 0x00ae0c10 | `CONDITIONAL_JUMP`
<a id="insn-00ae0c04"></a> `00ae0c04` | `c0 bd ff b0` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00ae0c08"></a> `00ae0c08` | `00 fc 19 91` | add x0,x0,#0x67f | `FALL_THROUGH`
<a id="insn-00ae0c0c"></a> `00ae0c0c` | `49 f5 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00ae0c10"></a> `00ae0c10` | `08 2e 00 90` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae0c14"></a> `00ae0c14` | `08 e1 02 91` | add x8,x8,#0xb8 | `FALL_THROUGH`
<a id="insn-00ae0c18"></a> `00ae0c18` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00ae0c1c"></a> `00ae0c1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0c20"></a> `00ae0c20` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae0c24"></a> `00ae0c24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae0bec`](#insn-00ae0bec) 範囲 `[['00ae0bec', '00ae0c03']]`
  - `CONDITIONAL_JUMP` [`00ae0c00`](#insn-00ae0c00) → [`00ae0c10`](#insn-00ae0c10)
  - `FALL_THROUGH` [`00ae0c00`](#insn-00ae0c00) → [`00ae0c04`](#insn-00ae0c04)
- ブロック [`00ae0c04`](#insn-00ae0c04) 範囲 `[['00ae0c04', '00ae0c0f']]`
  - `FALL_THROUGH` [`00ae0c0c`](#insn-00ae0c0c) → [`00ae0c10`](#insn-00ae0c10)
- ブロック [`00ae0c10`](#insn-00ae0c10) 範囲 `[['00ae0c10', '00ae0c27']]`

## 命令位置別の参照

- [`00ae0bec`](#insn-00ae0bec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0bf0`](#insn-00ae0bf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0c00`](#insn-00ae0c00) → [`00ae0c10`](#insn-00ae0c10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0c08`](#insn-00ae0c08) → `0029967f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae0c0c`](#insn-00ae0c0c) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00ae0c18`](#insn-00ae0c18) → `010a00b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0c1c`](#insn-00ae0c1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae0bec`](#insn-00ae0bec)

~~~json
{
  "source": "00ae0bec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0bf0`](#insn-00ae0bf0)

~~~json
{
  "source": "00ae0bf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0c00`](#insn-00ae0c00)

~~~json
{
  "source": "00ae0c00",
  "target": "00ae0c10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0c08`](#insn-00ae0c08)

~~~json
{
  "source": "00ae0c08",
  "target": "0029967f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029967f",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "0029967f",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae0c0c`](#insn-00ae0c0c)

~~~json
{
  "source": "00ae0c0c",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae0c18`](#insn-00ae0c18)

~~~json
{
  "source": "00ae0c18",
  "target": "010a00b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a00b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0c1c`](#insn-00ae0c1c)

~~~json
{
  "source": "00ae0c1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
