# 00bdda1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6e51c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e51c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-c0303d6aaf611a4b650a9ff152f20bda)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdde44`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde44.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-4acc31fe3d71d7a569afa22748957778)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdda1c",
  "name": "_ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "631378624b7b45511b355389dda1ae633eeafc6c9602ec076af19719edd48604",
  "source_text_sha256": "631378624b7b45511b355389dda1ae633eeafc6c9602ec076af19719edd48604",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdda1c",
        "00bdda57"
      ]
    ],
    "bytes_sha256": "f29e300e0759c5a20abcf96e0d3e7c3d665614df2a24bf158cf00be5f43180e5",
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

## 疑似コード / UTF-8 242 bytes

~~~c

undefined8 _ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01126a58 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdda1c"></a> `00bdda1c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdda20"></a> `00bdda20` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdda24"></a> `00bdda24` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdda28"></a> `00bdda28` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bdda2c"></a> `00bdda2c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdda30"></a> `00bdda30` | `8b 00 00 54` | b.lt 0x00bdda40 | `CONDITIONAL_JUMP`
<a id="insn-00bdda34"></a> `00bdda34` | `60 b6 ff 90` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdda38"></a> `00bdda38` | `00 44 11 91` | add x0,x0,#0x451 | `FALL_THROUGH`
<a id="insn-00bdda3c"></a> `00bdda3c` | `71 f4 01 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdda40"></a> `00bdda40` | `48 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdda44"></a> `00bdda44` | `08 61 29 91` | add x8,x8,#0xa58 | `FALL_THROUGH`
<a id="insn-00bdda48"></a> `00bdda48` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bdda4c"></a> `00bdda4c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdda50"></a> `00bdda50` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdda54"></a> `00bdda54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdda1c`](#insn-00bdda1c) 範囲 `[['00bdda1c', '00bdda33']]`
  - `CONDITIONAL_JUMP` [`00bdda30`](#insn-00bdda30) → [`00bdda40`](#insn-00bdda40)
  - `FALL_THROUGH` [`00bdda30`](#insn-00bdda30) → [`00bdda34`](#insn-00bdda34)
- ブロック [`00bdda34`](#insn-00bdda34) 範囲 `[['00bdda34', '00bdda3f']]`
  - `FALL_THROUGH` [`00bdda3c`](#insn-00bdda3c) → [`00bdda40`](#insn-00bdda40)
- ブロック [`00bdda40`](#insn-00bdda40) 範囲 `[['00bdda40', '00bdda57']]`

## 命令位置別の参照

- [`00bdda1c`](#insn-00bdda1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda20`](#insn-00bdda20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda30`](#insn-00bdda30) → [`00bdda40`](#insn-00bdda40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda38`](#insn-00bdda38) → `002a9451`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdda3c`](#insn-00bdda3c) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bdda48`](#insn-00bdda48) → `01126a58`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda4c`](#insn-00bdda4c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdda1c`](#insn-00bdda1c)

~~~json
{
  "source": "00bdda1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda20`](#insn-00bdda20)

~~~json
{
  "source": "00bdda20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda30`](#insn-00bdda30)

~~~json
{
  "source": "00bdda30",
  "target": "00bdda40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda38`](#insn-00bdda38)

~~~json
{
  "source": "00bdda38",
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
- 参照命令 [`00bdda3c`](#insn-00bdda3c)

~~~json
{
  "source": "00bdda3c",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdda48`](#insn-00bdda48)

~~~json
{
  "source": "00bdda48",
  "target": "01126a58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda4c`](#insn-00bdda4c)

~~~json
{
  "source": "00bdda4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
