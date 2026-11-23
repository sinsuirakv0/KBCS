# 00aedbc8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aedb00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb00.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-a9a3e2aa5cd81d5f0d84e33c1652b01a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aedc0c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedc0c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-957065c961b8e5c86041ab5683787492)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedbc8",
  "name": "_ZN8firebase4util9throwable10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7f4721d99769ca5d9bb6f7ce16644374d43d1a54f63a4f9a9ada16c14a3498a",
  "source_text_sha256": "f7f4721d99769ca5d9bb6f7ce16644374d43d1a54f63a4f9a9ada16c14a3498a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedbc8",
        "00aedc03"
      ]
    ],
    "bytes_sha256": "bad1060d78be6bce8e2cbfedd94414c9ef0ff1af263211517152f38ae3a2f0d6",
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

## 疑似コード / UTF-8 232 bytes

~~~c

undefined8 _ZN8firebase4util9throwable10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a0a18 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedbc8"></a> `00aedbc8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedbcc"></a> `00aedbcc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedbd0"></a> `00aedbd0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedbd4"></a> `00aedbd4` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aedbd8"></a> `00aedbd8` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aedbdc"></a> `00aedbdc` | `8b 00 00 54` | b.lt 0x00aedbec | `CONDITIONAL_JUMP`
<a id="insn-00aedbe0"></a> `00aedbe0` | `60 bd ff 90` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00aedbe4"></a> `00aedbe4` | `00 fc 19 91` | add x0,x0,#0x67f | `FALL_THROUGH`
<a id="insn-00aedbe8"></a> `00aedbe8` | `52 c1 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00aedbec"></a> `00aedbec` | `88 2d 00 f0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedbf0"></a> `00aedbf0` | `08 61 28 91` | add x8,x8,#0xa18 | `FALL_THROUGH`
<a id="insn-00aedbf4"></a> `00aedbf4` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aedbf8"></a> `00aedbf8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedbfc"></a> `00aedbfc` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedc00"></a> `00aedc00` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedbc8`](#insn-00aedbc8) 範囲 `[['00aedbc8', '00aedbdf']]`
  - `CONDITIONAL_JUMP` [`00aedbdc`](#insn-00aedbdc) → [`00aedbec`](#insn-00aedbec)
  - `FALL_THROUGH` [`00aedbdc`](#insn-00aedbdc) → [`00aedbe0`](#insn-00aedbe0)
- ブロック [`00aedbe0`](#insn-00aedbe0) 範囲 `[['00aedbe0', '00aedbeb']]`
  - `FALL_THROUGH` [`00aedbe8`](#insn-00aedbe8) → [`00aedbec`](#insn-00aedbec)
- ブロック [`00aedbec`](#insn-00aedbec) 範囲 `[['00aedbec', '00aedc03']]`

## 命令位置別の参照

- [`00aedbc8`](#insn-00aedbc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbcc`](#insn-00aedbcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbdc`](#insn-00aedbdc) → [`00aedbec`](#insn-00aedbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbe4`](#insn-00aedbe4) → `0029967f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedbe8`](#insn-00aedbe8) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00aedbf4`](#insn-00aedbf4) → `010a0a18`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbf8`](#insn-00aedbf8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedbc8`](#insn-00aedbc8)

~~~json
{
  "source": "00aedbc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbcc`](#insn-00aedbcc)

~~~json
{
  "source": "00aedbcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbdc`](#insn-00aedbdc)

~~~json
{
  "source": "00aedbdc",
  "target": "00aedbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbe4`](#insn-00aedbe4)

~~~json
{
  "source": "00aedbe4",
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
- 参照命令 [`00aedbe8`](#insn-00aedbe8)

~~~json
{
  "source": "00aedbe8",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedbf4`](#insn-00aedbf4)

~~~json
{
  "source": "00aedbf4",
  "target": "010a0a18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbf8`](#insn-00aedbf8)

~~~json
{
  "source": "00aedbf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
