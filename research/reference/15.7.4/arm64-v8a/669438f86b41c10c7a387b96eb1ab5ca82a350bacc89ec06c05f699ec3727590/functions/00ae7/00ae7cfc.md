# 00ae7cfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae7cb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0062.md#compare-95e705a4560733bd86fabdb72802e1e5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b47a80`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a80.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0057.md#compare-d87ee475194c3ae6f87bc9e20552e5b1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae7cfc",
  "name": "_ZN8firebase4util21asset_file_descriptor10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0fc5c95fd4f827ef9c5c44d013b64a76ad2414dff5ffa583bbcf24836b9a7b68",
  "source_text_sha256": "0fc5c95fd4f827ef9c5c44d013b64a76ad2414dff5ffa583bbcf24836b9a7b68",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae7cfc",
        "00ae7d37"
      ]
    ],
    "bytes_sha256": "1338a2d937a5dcb5cb8507269fc016c5a3be3b3858f56f557ae9b1213a4dc67b",
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

## 疑似コード / UTF-8 245 bytes

~~~c

undefined8 _ZN8firebase4util21asset_file_descriptor10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a05b8 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae7cfc"></a> `00ae7cfc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae7d00"></a> `00ae7d00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7d04"></a> `00ae7d04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae7d08"></a> `00ae7d08` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00ae7d0c"></a> `00ae7d0c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ae7d10"></a> `00ae7d10` | `8b 00 00 54` | b.lt 0x00ae7d20 | `CONDITIONAL_JUMP`
<a id="insn-00ae7d14"></a> `00ae7d14` | `80 bd ff d0` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00ae7d18"></a> `00ae7d18` | `00 c8 17 91` | add x0,x0,#0x5f2 | `FALL_THROUGH`
<a id="insn-00ae7d1c"></a> `00ae7d1c` | `19 d9 03 94` | bl 0x00bde180 | `UNCONDITIONAL_CALL`
<a id="insn-00ae7d20"></a> `00ae7d20` | `c8 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae7d24"></a> `00ae7d24` | `08 e1 16 91` | add x8,x8,#0x5b8 | `FALL_THROUGH`
<a id="insn-00ae7d28"></a> `00ae7d28` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00ae7d2c"></a> `00ae7d2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7d30"></a> `00ae7d30` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae7d34"></a> `00ae7d34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae7cfc`](#insn-00ae7cfc) 範囲 `[['00ae7cfc', '00ae7d13']]`
  - `CONDITIONAL_JUMP` [`00ae7d10`](#insn-00ae7d10) → [`00ae7d20`](#insn-00ae7d20)
  - `FALL_THROUGH` [`00ae7d10`](#insn-00ae7d10) → [`00ae7d14`](#insn-00ae7d14)
- ブロック [`00ae7d14`](#insn-00ae7d14) 範囲 `[['00ae7d14', '00ae7d1f']]`
  - `FALL_THROUGH` [`00ae7d1c`](#insn-00ae7d1c) → [`00ae7d20`](#insn-00ae7d20)
- ブロック [`00ae7d20`](#insn-00ae7d20) 範囲 `[['00ae7d20', '00ae7d37']]`

## 命令位置別の参照

- [`00ae7cfc`](#insn-00ae7cfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7d00`](#insn-00ae7d00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7d10`](#insn-00ae7d10) → [`00ae7d20`](#insn-00ae7d20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7d18`](#insn-00ae7d18) → `002995f2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae7d1c`](#insn-00ae7d1c) → [`00bde180`](../00bde/00bde180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde180` · 推定シンボル `None` · 推定型 `None`
- [`00ae7d28`](#insn-00ae7d28) → `010a05b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7d2c`](#insn-00ae7d2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae7cfc`](#insn-00ae7cfc)

~~~json
{
  "source": "00ae7cfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7d00`](#insn-00ae7d00)

~~~json
{
  "source": "00ae7d00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7d10`](#insn-00ae7d10)

~~~json
{
  "source": "00ae7d10",
  "target": "00ae7d20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7d18`](#insn-00ae7d18)

~~~json
{
  "source": "00ae7d18",
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
- 参照命令 [`00ae7d1c`](#insn-00ae7d1c)

~~~json
{
  "source": "00ae7d1c",
  "target": "00bde180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae7d28`](#insn-00ae7d28)

~~~json
{
  "source": "00ae7d28",
  "target": "010a05b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7d2c`](#insn-00ae7d2c)

~~~json
{
  "source": "00ae7d2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
