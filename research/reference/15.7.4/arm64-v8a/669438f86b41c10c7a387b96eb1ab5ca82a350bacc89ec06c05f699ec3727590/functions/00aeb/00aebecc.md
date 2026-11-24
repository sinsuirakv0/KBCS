# 00aebecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebe88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-a3149bd5520212d7f6b1c652d79cc1b2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4bc50`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bc50.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0015.md#compare-4e345ce983e7876916a5484aa191534d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebecc",
  "name": "_ZN8firebase4util8iterator10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0974070aed452fb6d81c634af49a74281d9715b88c255aa1fc7f1290a70c22f7",
  "source_text_sha256": "0974070aed452fb6d81c634af49a74281d9715b88c255aa1fc7f1290a70c22f7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebecc",
        "00aebf07"
      ]
    ],
    "bytes_sha256": "853508d1d290335e327ea8ba96a655b1e04a9c938730203f3f3f1ff7d2fd371f",
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

## 疑似コード / UTF-8 328 bytes

~~~c

undefined8 _ZN8firebase4util8iterator10GetFieldIdENS1_5FieldE(uint param_1)

{
                    /* try { // try from 00aebee0 to 00bebef3 has its CatchHandler @ 00af1c18 */
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a0918 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebecc"></a> `00aebecc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebed0"></a> `00aebed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebed4"></a> `00aebed4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebed8"></a> `00aebed8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aebedc"></a> `00aebedc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aebee0"></a> `00aebee0` | `8b 00 00 54` | b.lt 0x00aebef0 | `CONDITIONAL_JUMP`
<a id="insn-00aebee4"></a> `00aebee4` | `60 bd ff d0` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00aebee8"></a> `00aebee8` | `00 c8 17 91` | add x0,x0,#0x5f2 | `FALL_THROUGH`
<a id="insn-00aebeec"></a> `00aebeec` | `a5 c8 03 94` | bl 0x00bde180 | `UNCONDITIONAL_CALL`
<a id="insn-00aebef0"></a> `00aebef0` | `a8 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebef4"></a> `00aebef4` | `08 61 24 91` | add x8,x8,#0x918 | `FALL_THROUGH`
<a id="insn-00aebef8"></a> `00aebef8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aebefc"></a> `00aebefc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebf00"></a> `00aebf00` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebf04"></a> `00aebf04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebecc`](#insn-00aebecc) 範囲 `[['00aebecc', '00aebedf']]`
  - `FALL_THROUGH` [`00aebedc`](#insn-00aebedc) → [`00aebee0`](#insn-00aebee0)
- ブロック [`00aebee0`](#insn-00aebee0) 範囲 `[['00aebee0', '00aebee3']]`
  - `CONDITIONAL_JUMP` [`00aebee0`](#insn-00aebee0) → [`00aebef0`](#insn-00aebef0)
  - `FALL_THROUGH` [`00aebee0`](#insn-00aebee0) → [`00aebee4`](#insn-00aebee4)
- ブロック [`00aebee4`](#insn-00aebee4) 範囲 `[['00aebee4', '00aebeef']]`
  - `FALL_THROUGH` [`00aebeec`](#insn-00aebeec) → [`00aebef0`](#insn-00aebef0)
- ブロック [`00aebef0`](#insn-00aebef0) 範囲 `[['00aebef0', '00aebf07']]`

## 命令位置別の参照

- [`00aebecc`](#insn-00aebecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebed0`](#insn-00aebed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebee0`](#insn-00aebee0) → [`00aebef0`](#insn-00aebef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebee8`](#insn-00aebee8) → `002995f2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebeec`](#insn-00aebeec) → [`00bde180`](../00bde/00bde180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde180` · 推定シンボル `None` · 推定型 `None`
- [`00aebef8`](#insn-00aebef8) → `010a0918`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebefc`](#insn-00aebefc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebecc`](#insn-00aebecc)

~~~json
{
  "source": "00aebecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebed0`](#insn-00aebed0)

~~~json
{
  "source": "00aebed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebee0`](#insn-00aebee0)

~~~json
{
  "source": "00aebee0",
  "target": "00aebef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebee8`](#insn-00aebee8)

~~~json
{
  "source": "00aebee8",
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
- 参照命令 [`00aebeec`](#insn-00aebeec)

~~~json
{
  "source": "00aebeec",
  "target": "00bde180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebef8`](#insn-00aebef8)

~~~json
{
  "source": "00aebef8",
  "target": "010a0918",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebefc`](#insn-00aebefc)

~~~json
{
  "source": "00aebefc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
