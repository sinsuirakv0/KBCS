# 00aecc7c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aecbb4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-550da9837e690ec62ea00e7733ee8fa8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeccc0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccc0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-44b2fa4e078aba0e2970ee8054cb4908)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecc7c",
  "name": "_ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b9363002133eb015ecce41961113ad81b452e2df5fd1ed3b6c7969892508022",
  "source_text_sha256": "8b9363002133eb015ecce41961113ad81b452e2df5fd1ed3b6c7969892508022",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecc7c",
        "00aeccb7"
      ]
    ],
    "bytes_sha256": "5ccf1729cab887c5e351baa3861cac864b7cfeb761fb7f8a8dca0e3c8ee46ea4",
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
  return *(undefined8 *)(&DAT_010a0978 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecc7c"></a> `00aecc7c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecc80"></a> `00aecc80` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecc84"></a> `00aecc84` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecc88"></a> `00aecc88` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aecc8c"></a> `00aecc8c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aecc90"></a> `00aecc90` | `8b 00 00 54` | b.lt 0x00aecca0 | `CONDITIONAL_JUMP`
<a id="insn-00aecc94"></a> `00aecc94` | `60 bd ff 90` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00aecc98"></a> `00aecc98` | `00 50 17 91` | add x0,x0,#0x5d4 | `FALL_THROUGH`
<a id="insn-00aecc9c"></a> `00aecc9c` | `25 c5 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00aecca0"></a> `00aecca0` | `a8 2d 00 90` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecca4"></a> `00aecca4` | `08 e1 25 91` | add x8,x8,#0x978 | `FALL_THROUGH`
<a id="insn-00aecca8"></a> `00aecca8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aeccac"></a> `00aeccac` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeccb0"></a> `00aeccb0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeccb4"></a> `00aeccb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecc7c`](#insn-00aecc7c) 範囲 `[['00aecc7c', '00aecc93']]`
  - `CONDITIONAL_JUMP` [`00aecc90`](#insn-00aecc90) → [`00aecca0`](#insn-00aecca0)
  - `FALL_THROUGH` [`00aecc90`](#insn-00aecc90) → [`00aecc94`](#insn-00aecc94)
- ブロック [`00aecc94`](#insn-00aecc94) 範囲 `[['00aecc94', '00aecc9f']]`
  - `FALL_THROUGH` [`00aecc9c`](#insn-00aecc9c) → [`00aecca0`](#insn-00aecca0)
- ブロック [`00aecca0`](#insn-00aecca0) 範囲 `[['00aecca0', '00aeccb7']]`

## 命令位置別の参照

- [`00aecc7c`](#insn-00aecc7c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc80`](#insn-00aecc80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc90`](#insn-00aecc90) → [`00aecca0`](#insn-00aecca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc98`](#insn-00aecc98) → `002985d4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecc9c`](#insn-00aecc9c) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00aecca8`](#insn-00aecca8) → `010a0978`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccac`](#insn-00aeccac) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecc7c`](#insn-00aecc7c)

~~~json
{
  "source": "00aecc7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc80`](#insn-00aecc80)

~~~json
{
  "source": "00aecc80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc90`](#insn-00aecc90)

~~~json
{
  "source": "00aecc90",
  "target": "00aecca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc98`](#insn-00aecc98)

~~~json
{
  "source": "00aecc98",
  "target": "002985d4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002985d4",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002985d4",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecc9c`](#insn-00aecc9c)

~~~json
{
  "source": "00aecc9c",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecca8`](#insn-00aecca8)

~~~json
{
  "source": "00aecca8",
  "target": "010a0978",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccac`](#insn-00aeccac)

~~~json
{
  "source": "00aeccac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
