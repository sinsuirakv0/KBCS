# 00aedfb4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aedf70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-635aad5bf821325ab941ae7e651f06ec)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4dd38`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd38.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-9c44f014c1f5f7015ecdbed7cd4b602e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedfb4",
  "name": "_ZN8firebase4util3uri10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e63af509c1cb48af34c70bba8a4c9f94b83c68af2008be84c080dfd8e7f683e8",
  "source_text_sha256": "e63af509c1cb48af34c70bba8a4c9f94b83c68af2008be84c080dfd8e7f683e8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedfb4",
        "00aedfef"
      ]
    ],
    "bytes_sha256": "b03b4a790c15454efc7bbcd43029f40a1c6a24408be5050b7e4cd54393e5c589",
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

- [00bde180](../00bde/00bde180.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 226 bytes

~~~c

undefined8 _ZN8firebase4util3uri10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a0a80 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedfb4"></a> `00aedfb4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedfb8"></a> `00aedfb8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedfbc"></a> `00aedfbc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedfc0"></a> `00aedfc0` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aedfc4"></a> `00aedfc4` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aedfc8"></a> `00aedfc8` | `8b 00 00 54` | b.lt 0x00aedfd8 | `CONDITIONAL_JUMP`
<a id="insn-00aedfcc"></a> `00aedfcc` | `60 bd ff 90` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00aedfd0"></a> `00aedfd0` | `00 c8 17 91` | add x0,x0,#0x5f2 | `FALL_THROUGH`
<a id="insn-00aedfd4"></a> `00aedfd4` | `6b c0 03 94` | bl 0x00bde180 | `UNCONDITIONAL_CALL`
<a id="insn-00aedfd8"></a> `00aedfd8` | `88 2d 00 f0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedfdc"></a> `00aedfdc` | `08 01 2a 91` | add x8,x8,#0xa80 | `FALL_THROUGH`
<a id="insn-00aedfe0"></a> `00aedfe0` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aedfe4"></a> `00aedfe4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedfe8"></a> `00aedfe8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedfec"></a> `00aedfec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedfb4`](#insn-00aedfb4) 範囲 `[['00aedfb4', '00aedfcb']]`
  - `CONDITIONAL_JUMP` [`00aedfc8`](#insn-00aedfc8) → [`00aedfd8`](#insn-00aedfd8)
  - `FALL_THROUGH` [`00aedfc8`](#insn-00aedfc8) → [`00aedfcc`](#insn-00aedfcc)
- ブロック [`00aedfcc`](#insn-00aedfcc) 範囲 `[['00aedfcc', '00aedfd7']]`
  - `FALL_THROUGH` [`00aedfd4`](#insn-00aedfd4) → [`00aedfd8`](#insn-00aedfd8)
- ブロック [`00aedfd8`](#insn-00aedfd8) 範囲 `[['00aedfd8', '00aedfef']]`

## 命令位置別の参照

- [`00aedfb4`](#insn-00aedfb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedfb8`](#insn-00aedfb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedfc8`](#insn-00aedfc8) → [`00aedfd8`](#insn-00aedfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedfd0`](#insn-00aedfd0) → `002995f2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedfd4`](#insn-00aedfd4) → [`00bde180`](../00bde/00bde180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde180` · 推定シンボル `None` · 推定型 `None`
- [`00aedfe0`](#insn-00aedfe0) → `010a0a80`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedfe4`](#insn-00aedfe4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedfb4`](#insn-00aedfb4)

~~~json
{
  "source": "00aedfb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedfb8`](#insn-00aedfb8)

~~~json
{
  "source": "00aedfb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedfc8`](#insn-00aedfc8)

~~~json
{
  "source": "00aedfc8",
  "target": "00aedfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedfd0`](#insn-00aedfd0)

~~~json
{
  "source": "00aedfd0",
  "target": "002995f2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002995f2",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002995f2",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedfd4`](#insn-00aedfd4)

~~~json
{
  "source": "00aedfd4",
  "target": "00bde180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedfe0`](#insn-00aedfe0)

~~~json
{
  "source": "00aedfe0",
  "target": "010a0a80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedfe4`](#insn-00aedfe4)

~~~json
{
  "source": "00aedfe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
