# 005afdbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `005afdbc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afdbc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0004.md#compare-24e4750a3fa15dfc5596c12337f04e8a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `005afdbc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afdbc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0004.md#compare-2c960685ab75731d425f94a43a676675)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005afdbc",
  "name": "FUN_005afdbc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7b988fcae7e4a734f0967486c46ecd0e7829626c3e85f4a017643f993d327d3",
  "source_text_sha256": "f7b988fcae7e4a734f0967486c46ecd0e7829626c3e85f4a017643f993d327d3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005afdbc",
        "005afe03"
      ]
    ],
    "bytes_sha256": "9318425a64162d2ba4dd0376be33089d5f109c72eac1656844aad3f8ba2c7a21",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 273 bytes

~~~c

void FUN_005afdbc(long *param_1)

{
  long *plVar1;
  
  plVar1 = (long *)param_1[1];
  *param_1 = (long)(PTR__ZTVNSt6__ndk116__owns_one_stateIcEE_00c1b560 + 0x10);
  if (plVar1 != (long *)0x0) {
    (**(code **)(*plVar1 + 8))(plVar1);
  }
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005afdbc"></a> `005afdbc` | `69 33 00 90` | adrp x9,0xc1b000 | `FALL_THROUGH`
<a id="insn-005afdc0"></a> `005afdc0` | `29 b1 42 f9` | ldr x9,[x9, #0x560] | `FALL_THROUGH`
<a id="insn-005afdc4"></a> `005afdc4` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-005afdc8"></a> `005afdc8` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-005afdcc"></a> `005afdcc` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-005afdd0"></a> `005afdd0` | `88 01 00 b4` | cbz x8,0x005afe00 | `CONDITIONAL_JUMP`
<a id="insn-005afdd4"></a> `005afdd4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-005afdd8"></a> `005afdd8` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005afddc"></a> `005afddc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005afde0"></a> `005afde0` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-005afde4"></a> `005afde4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005afde8"></a> `005afde8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-005afdec"></a> `005afdec` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-005afdf0"></a> `005afdf0` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-005afdf4"></a> `005afdf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005afdf8"></a> `005afdf8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005afdfc"></a> `005afdfc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-005afe00"></a> `005afe00` | `84 ac 18 14` | b 0x00bdb010 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005afdbc`](#insn-005afdbc) 範囲 `[['005afdbc', '005afdd3']]`
  - `CONDITIONAL_JUMP` [`005afdd0`](#insn-005afdd0) → [`005afe00`](#insn-005afe00)
  - `FALL_THROUGH` [`005afdd0`](#insn-005afdd0) → [`005afdd4`](#insn-005afdd4)
- ブロック [`005afdd4`](#insn-005afdd4) 範囲 `[['005afdd4', '005afdff']]`
  - `FALL_THROUGH` [`005afdfc`](#insn-005afdfc) → [`005afe00`](#insn-005afe00)
- ブロック [`005afe00`](#insn-005afe00) 範囲 `[['005afe00', '005afe03']]`

## 命令位置別の参照

- [`005afdc0`](#insn-005afdc0) → `00c1b560`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005afdcc`](#insn-005afdcc) → `00bf3740`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`005afdd0`](#insn-005afdd0) → [`005afe00`](#insn-005afe00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005afdd4`](#insn-005afdd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005afdd8`](#insn-005afdd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005afdf8`](#insn-005afdf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005afdfc`](#insn-005afdfc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005afe00`](#insn-005afe00) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005afdc0`](#insn-005afdc0)

~~~json
{
  "source": "005afdc0",
  "target": "00c1b560",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b560",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005afdcc`](#insn-005afdcc)

~~~json
{
  "source": "005afdcc",
  "target": "00bf3740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf3730",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`005afdd0`](#insn-005afdd0)

~~~json
{
  "source": "005afdd0",
  "target": "005afe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005afdd4`](#insn-005afdd4)

~~~json
{
  "source": "005afdd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005afdd8`](#insn-005afdd8)

~~~json
{
  "source": "005afdd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005afdf8`](#insn-005afdf8)

~~~json
{
  "source": "005afdf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005afdfc`](#insn-005afdfc)

~~~json
{
  "source": "005afdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005afe00`](#insn-005afe00)

~~~json
{
  "source": "005afe00",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
