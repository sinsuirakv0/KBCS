# 00a7bfdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a1e14c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e14c.md) · 移動量 `+0x5de90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0051.md#compare-db009b05ac7e8dde69e33ae377253b6a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a7c1d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c1d4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0061.md#compare-74ab69ff248eeb0a485f90ccf4c8cef9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a7bfdc",
  "name": "FUN_00a7bfdc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ccf3acc3402fe1513acbea2ea9dffc4275d0a20dae156acc82982e4c6517ff8f",
  "source_text_sha256": "ccf3acc3402fe1513acbea2ea9dffc4275d0a20dae156acc82982e4c6517ff8f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a7bfdc",
        "00a7c00f"
      ]
    ],
    "bytes_sha256": "33296a3db7af5e5861d88d28f365693c27c0a3755ab1675571b0bf7fbe5f06e0",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_00a7bfdc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c8b800;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a7bfdc"></a> `00a7bfdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a7bfe0"></a> `00a7bfe0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7bfe4"></a> `00a7bfe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a7bfe8"></a> `00a7bfe8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a7bfec"></a> `00a7bfec` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00a7bff0"></a> `00a7bff0` | `a8 6e 07 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00a7bff4"></a> `00a7bff4` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a7bff8"></a> `00a7bff8` | `88 10 00 90` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a7bffc"></a> `00a7bffc` | `08 01 20 91` | add x8,x8,#0x800 | `FALL_THROUGH`
<a id="insn-00a7c000"></a> `00a7c000` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00a7c004"></a> `00a7c004` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7c008"></a> `00a7c008` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a7c00c"></a> `00a7c00c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a7bfdc`](#insn-00a7bfdc) 範囲 `[['00a7bfdc', '00a7c00f']]`

## 命令位置別の参照

- [`00a7bfdc`](#insn-00a7bfdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bfe0`](#insn-00a7bfe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bff0`](#insn-00a7bff0) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00a7c000`](#insn-00a7c000) → `00c8b800`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a7c004`](#insn-00a7c004) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c008`](#insn-00a7c008) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a7bfdc`](#insn-00a7bfdc)

~~~json
{
  "source": "00a7bfdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bfe0`](#insn-00a7bfe0)

~~~json
{
  "source": "00a7bfe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bff0`](#insn-00a7bff0)

~~~json
{
  "source": "00a7bff0",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7c000`](#insn-00a7c000)

~~~json
{
  "source": "00a7c000",
  "target": "00c8b800",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b800",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a7c004`](#insn-00a7c004)

~~~json
{
  "source": "00a7c004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c008`](#insn-00a7c008)

~~~json
{
  "source": "00a7c008",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
