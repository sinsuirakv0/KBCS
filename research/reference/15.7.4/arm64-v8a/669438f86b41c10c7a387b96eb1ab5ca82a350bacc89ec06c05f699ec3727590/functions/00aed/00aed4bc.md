# 00aed4bc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aed478`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed478.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-4ea82cb0ccc4965863d30a453481824c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4d240`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d240.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-dbb1ce9ba1a101e0733a5d361483bdc0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed4bc",
  "name": "_ZN8firebase4util11short_class10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae14411aed7d839873859c3fd5b6ad94d5faea0325e40b8f34b65a410d3e6edb",
  "source_text_sha256": "ae14411aed7d839873859c3fd5b6ad94d5faea0325e40b8f34b65a410d3e6edb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aed4bc",
        "00aed4f7"
      ]
    ],
    "bytes_sha256": "46423f2ca3c082d5ce34efcd868fa95bc4a3b594dbd06c52c60e94a34496abc8",
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

## 疑似コード / UTF-8 235 bytes

~~~c

undefined8 _ZN8firebase4util11short_class10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a0a08 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aed4bc"></a> `00aed4bc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aed4c0"></a> `00aed4c0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed4c4"></a> `00aed4c4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aed4c8"></a> `00aed4c8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aed4cc"></a> `00aed4cc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aed4d0"></a> `00aed4d0` | `8b 00 00 54` | b.lt 0x00aed4e0 | `CONDITIONAL_JUMP`
<a id="insn-00aed4d4"></a> `00aed4d4` | `60 bd ff 90` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00aed4d8"></a> `00aed4d8` | `00 c8 17 91` | add x0,x0,#0x5f2 | `FALL_THROUGH`
<a id="insn-00aed4dc"></a> `00aed4dc` | `29 c3 03 94` | bl 0x00bde180 | `UNCONDITIONAL_CALL`
<a id="insn-00aed4e0"></a> `00aed4e0` | `88 2d 00 f0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aed4e4"></a> `00aed4e4` | `08 21 28 91` | add x8,x8,#0xa08 | `FALL_THROUGH`
<a id="insn-00aed4e8"></a> `00aed4e8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aed4ec"></a> `00aed4ec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed4f0"></a> `00aed4f0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aed4f4"></a> `00aed4f4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aed4bc`](#insn-00aed4bc) 範囲 `[['00aed4bc', '00aed4d3']]`
  - `CONDITIONAL_JUMP` [`00aed4d0`](#insn-00aed4d0) → [`00aed4e0`](#insn-00aed4e0)
  - `FALL_THROUGH` [`00aed4d0`](#insn-00aed4d0) → [`00aed4d4`](#insn-00aed4d4)
- ブロック [`00aed4d4`](#insn-00aed4d4) 範囲 `[['00aed4d4', '00aed4df']]`
  - `FALL_THROUGH` [`00aed4dc`](#insn-00aed4dc) → [`00aed4e0`](#insn-00aed4e0)
- ブロック [`00aed4e0`](#insn-00aed4e0) 範囲 `[['00aed4e0', '00aed4f7']]`

## 命令位置別の参照

- [`00aed4bc`](#insn-00aed4bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4c0`](#insn-00aed4c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4d0`](#insn-00aed4d0) → [`00aed4e0`](#insn-00aed4e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4d8`](#insn-00aed4d8) → `002995f2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aed4dc`](#insn-00aed4dc) → [`00bde180`](../00bde/00bde180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde180` · 推定シンボル `None` · 推定型 `None`
- [`00aed4e8`](#insn-00aed4e8) → `010a0a08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed4ec`](#insn-00aed4ec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aed4bc`](#insn-00aed4bc)

~~~json
{
  "source": "00aed4bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4c0`](#insn-00aed4c0)

~~~json
{
  "source": "00aed4c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4d0`](#insn-00aed4d0)

~~~json
{
  "source": "00aed4d0",
  "target": "00aed4e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4d8`](#insn-00aed4d8)

~~~json
{
  "source": "00aed4d8",
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
- 参照命令 [`00aed4dc`](#insn-00aed4dc)

~~~json
{
  "source": "00aed4dc",
  "target": "00bde180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed4e8`](#insn-00aed4e8)

~~~json
{
  "source": "00aed4e8",
  "target": "010a0a08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed4ec`](#insn-00aed4ec)

~~~json
{
  "source": "00aed4ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
