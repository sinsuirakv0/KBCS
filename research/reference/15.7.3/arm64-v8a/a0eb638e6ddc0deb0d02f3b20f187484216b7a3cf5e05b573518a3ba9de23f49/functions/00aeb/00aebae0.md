# 00aebae0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeba18`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba18.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-75611945275dec6e1d1e55387471579f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aebb24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb24.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-6bf185a5825308876958feb58796e87d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebae0",
  "name": "_ZN8firebase4util8iterable10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0fbea2796be3967af92b466f849b0d495125b109c82e016b446e37bfbbae001a",
  "source_text_sha256": "0fbea2796be3967af92b466f849b0d495125b109c82e016b446e37bfbbae001a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebae0",
        "00aebb1b"
      ]
    ],
    "bytes_sha256": "04035651bde5ea744473c225324ad2eba6609dedb701593d73e534ffb50397f9",
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

## 疑似コード / UTF-8 231 bytes

~~~c

undefined8 _ZN8firebase4util8iterable10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a08b0 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebae0"></a> `00aebae0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebae4"></a> `00aebae4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebae8"></a> `00aebae8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebaec"></a> `00aebaec` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aebaf0"></a> `00aebaf0` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aebaf4"></a> `00aebaf4` | `8b 00 00 54` | b.lt 0x00aebb04 | `CONDITIONAL_JUMP`
<a id="insn-00aebaf8"></a> `00aebaf8` | `60 bd ff d0` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00aebafc"></a> `00aebafc` | `00 fc 19 91` | add x0,x0,#0x67f | `FALL_THROUGH`
<a id="insn-00aebb00"></a> `00aebb00` | `8c c9 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00aebb04"></a> `00aebb04` | `a8 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebb08"></a> `00aebb08` | `08 c1 22 91` | add x8,x8,#0x8b0 | `FALL_THROUGH`
<a id="insn-00aebb0c"></a> `00aebb0c` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aebb10"></a> `00aebb10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebb14"></a> `00aebb14` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebb18"></a> `00aebb18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebae0`](#insn-00aebae0) 範囲 `[['00aebae0', '00aebaf7']]`
  - `CONDITIONAL_JUMP` [`00aebaf4`](#insn-00aebaf4) → [`00aebb04`](#insn-00aebb04)
  - `FALL_THROUGH` [`00aebaf4`](#insn-00aebaf4) → [`00aebaf8`](#insn-00aebaf8)
- ブロック [`00aebaf8`](#insn-00aebaf8) 範囲 `[['00aebaf8', '00aebb03']]`
  - `FALL_THROUGH` [`00aebb00`](#insn-00aebb00) → [`00aebb04`](#insn-00aebb04)
- ブロック [`00aebb04`](#insn-00aebb04) 範囲 `[['00aebb04', '00aebb1b']]`

## 命令位置別の参照

- [`00aebae0`](#insn-00aebae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebae4`](#insn-00aebae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebaf4`](#insn-00aebaf4) → [`00aebb04`](#insn-00aebb04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebafc`](#insn-00aebafc) → `0029967f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebb00`](#insn-00aebb00) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00aebb0c`](#insn-00aebb0c) → `010a08b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb10`](#insn-00aebb10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebae0`](#insn-00aebae0)

~~~json
{
  "source": "00aebae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebae4`](#insn-00aebae4)

~~~json
{
  "source": "00aebae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebaf4`](#insn-00aebaf4)

~~~json
{
  "source": "00aebaf4",
  "target": "00aebb04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebafc`](#insn-00aebafc)

~~~json
{
  "source": "00aebafc",
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
- 参照命令 [`00aebb00`](#insn-00aebb00)

~~~json
{
  "source": "00aebb00",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebb0c`](#insn-00aebb0c)

~~~json
{
  "source": "00aebb0c",
  "target": "010a08b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb10`](#insn-00aebb10)

~~~json
{
  "source": "00aebb10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
