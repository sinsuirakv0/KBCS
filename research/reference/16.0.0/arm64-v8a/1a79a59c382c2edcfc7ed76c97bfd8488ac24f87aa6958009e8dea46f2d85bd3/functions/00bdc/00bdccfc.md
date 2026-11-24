# 00bdccfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6d7fc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d7fc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-6c0813f76a8b7ed3c69311e672fa80fc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd124`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd124.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-0b56787f738c0024deedc614968469a7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdccfc",
  "name": "_ZN8firebase4auth11tokenresult10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5ae609bc569c3658400ab0865f6f816ca8aa6383c5d182c2667e11c8f775d042",
  "source_text_sha256": "5ae609bc569c3658400ab0865f6f816ca8aa6383c5d182c2667e11c8f775d042",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdccfc",
        "00bdcd37"
      ]
    ],
    "bytes_sha256": "731f910465a2941103056e5fd97376cb7c34b6e7087ef597fcca2dcabff47733",
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

- [00c5ac00](../00c5a/00c5ac00.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 235 bytes

~~~c

undefined8 _ZN8firebase4auth11tokenresult10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01126918 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdccfc"></a> `00bdccfc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdcd00"></a> `00bdcd00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcd04"></a> `00bdcd04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcd08"></a> `00bdcd08` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bdcd0c"></a> `00bdcd0c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdcd10"></a> `00bdcd10` | `8b 00 00 54` | b.lt 0x00bdcd20 | `CONDITIONAL_JUMP`
<a id="insn-00bdcd14"></a> `00bdcd14` | `60 b6 ff b0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdcd18"></a> `00bdcd18` | `00 44 11 91` | add x0,x0,#0x451 | `FALL_THROUGH`
<a id="insn-00bdcd1c"></a> `00bdcd1c` | `b9 f7 01 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcd20"></a> `00bdcd20` | `48 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcd24"></a> `00bdcd24` | `08 61 24 91` | add x8,x8,#0x918 | `FALL_THROUGH`
<a id="insn-00bdcd28"></a> `00bdcd28` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bdcd2c"></a> `00bdcd2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcd30"></a> `00bdcd30` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdcd34"></a> `00bdcd34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdccfc`](#insn-00bdccfc) 範囲 `[['00bdccfc', '00bdcd13']]`
  - `CONDITIONAL_JUMP` [`00bdcd10`](#insn-00bdcd10) → [`00bdcd20`](#insn-00bdcd20)
  - `FALL_THROUGH` [`00bdcd10`](#insn-00bdcd10) → [`00bdcd14`](#insn-00bdcd14)
- ブロック [`00bdcd14`](#insn-00bdcd14) 範囲 `[['00bdcd14', '00bdcd1f']]`
  - `FALL_THROUGH` [`00bdcd1c`](#insn-00bdcd1c) → [`00bdcd20`](#insn-00bdcd20)
- ブロック [`00bdcd20`](#insn-00bdcd20) 範囲 `[['00bdcd20', '00bdcd37']]`

## 命令位置別の参照

- [`00bdccfc`](#insn-00bdccfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd00`](#insn-00bdcd00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd10`](#insn-00bdcd10) → [`00bdcd20`](#insn-00bdcd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd18`](#insn-00bdcd18) → `002a9451`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdcd1c`](#insn-00bdcd1c) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd28`](#insn-00bdcd28) → `01126918`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd2c`](#insn-00bdcd2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdccfc`](#insn-00bdccfc)

~~~json
{
  "source": "00bdccfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd00`](#insn-00bdcd00)

~~~json
{
  "source": "00bdcd00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd10`](#insn-00bdcd10)

~~~json
{
  "source": "00bdcd10",
  "target": "00bdcd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd18`](#insn-00bdcd18)

~~~json
{
  "source": "00bdcd18",
  "target": "002a9451",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9451",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002a9451",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdcd1c`](#insn-00bdcd1c)

~~~json
{
  "source": "00bdcd1c",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcd28`](#insn-00bdcd28)

~~~json
{
  "source": "00bdcd28",
  "target": "01126918",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd2c`](#insn-00bdcd2c)

~~~json
{
  "source": "00bdcd2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
