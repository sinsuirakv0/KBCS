# 00bbaea8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbade0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbade0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-bb98261b804f750f910449dea5e848cb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbaeec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeec.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-1d802bfb403122a36c84e212e615ae07)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaea8",
  "name": "_ZNSt14overflow_errorD1Ev",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c1c1b207874b7a02478d51f6ed2561bd12c44e46c57bbcb19c27f331c911174",
  "source_text_sha256": "7c1c1b207874b7a02478d51f6ed2561bd12c44e46c57bbcb19c27f331c911174",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaea8",
        "00bbaeff"
      ]
    ],
    "bytes_sha256": "34116736e7de14d48814f874ae5b5de45277250831d3e81eb04cf1f2134005fa",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdda20](../00bdd/00bdda20.md)
- [00be0f20](../00be0/00be0f20.md)
- [00be0f80](../00be0/00be0f80.md)
- [00be1150](../00be1/00be1150.md)
- [00be1e30](../00be1/00be1e30.md)

## 呼び出し先

- [00bd6df0](../00bd6/00bd6df0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb440](../00bdb/00bdb440.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt14overflow_errorD1Ev(long *param_1)

{
  int iVar1;
  long lVar2;
  
  lVar2 = param_1[1];
  *param_1 = (long)(PTR__ZTVSt13runtime_error_00c1bc18 + 0x10);
  iVar1 = FUN_00bd6df0(0xffffffff,lVar2 + -8);
  if (iVar1 + -1 < 0) {
    _ZdlPv((void *)(lVar2 + -0x18));
  }
  _ZNSt20bad_array_new_lengthD1Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaea8"></a> `00bbaea8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaeac"></a> `00bbaeac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbaeb0"></a> `00bbaeb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaeb4"></a> `00bbaeb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbaeb8"></a> `00bbaeb8` | `08 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbaebc"></a> `00bbaebc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbaec0"></a> `00bbaec0` | `08 0d 46 f9` | ldr x8,[x8, #0xc18] | `FALL_THROUGH`
<a id="insn-00bbaec4"></a> `00bbaec4` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbaec8"></a> `00bbaec8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbaecc"></a> `00bbaecc` | `81 22 00 d1` | sub x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bbaed0"></a> `00bbaed0` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbaed4"></a> `00bbaed4` | `00 00 80 12` | mov w0,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bbaed8"></a> `00bbaed8` | `c6 6f 00 94` | bl 0x00bd6df0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaedc"></a> `00bbaedc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbaee0"></a> `00bbaee0` | `65 00 00 54` | b.pl 0x00bbaeec | `CONDITIONAL_JUMP`
<a id="insn-00bbaee4"></a> `00bbaee4` | `80 62 00 d1` | sub x0,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00bbaee8"></a> `00bbaee8` | `4a 80 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaeec"></a> `00bbaeec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaef0"></a> `00bbaef0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaef4"></a> `00bbaef4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbaef8"></a> `00bbaef8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbaefc"></a> `00bbaefc` | `51 81 00 14` | b 0x00bdb440 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaea8`](#insn-00bbaea8) 範囲 `[['00bbaea8', '00bbaee3']]`
  - `CONDITIONAL_JUMP` [`00bbaee0`](#insn-00bbaee0) → [`00bbaeec`](#insn-00bbaeec)
  - `FALL_THROUGH` [`00bbaee0`](#insn-00bbaee0) → [`00bbaee4`](#insn-00bbaee4)
- ブロック [`00bbaee4`](#insn-00bbaee4) 範囲 `[['00bbaee4', '00bbaeeb']]`
  - `FALL_THROUGH` [`00bbaee8`](#insn-00bbaee8) → [`00bbaeec`](#insn-00bbaeec)
- ブロック [`00bbaeec`](#insn-00bbaeec) 範囲 `[['00bbaeec', '00bbaeff']]`

## 命令位置別の参照

- [`00bbaeac`](#insn-00bbaeac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaeb0`](#insn-00bbaeb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaec0`](#insn-00bbaec0) → `00c1bc18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbaed0`](#insn-00bbaed0) → `00c16908`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bbaed8`](#insn-00bbaed8) → [`00bd6df0`](../00bd6/00bd6df0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6df0` · 推定シンボル `None` · 推定型 `None`
- [`00bbaee0`](#insn-00bbaee0) → [`00bbaeec`](#insn-00bbaeec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaee8`](#insn-00bbaee8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bbaef0`](#insn-00bbaef0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaef4`](#insn-00bbaef4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaefc`](#insn-00bbaefc) → [`00bdb440`](../00bdb/00bdb440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb440` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaeac`](#insn-00bbaeac)

~~~json
{
  "source": "00bbaeac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaeb0`](#insn-00bbaeb0)

~~~json
{
  "source": "00bbaeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaec0`](#insn-00bbaec0)

~~~json
{
  "source": "00bbaec0",
  "target": "00c1bc18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bc18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbaed0`](#insn-00bbaed0)

~~~json
{
  "source": "00bbaed0",
  "target": "00c16908",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c168f8",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bbaed8`](#insn-00bbaed8)

~~~json
{
  "source": "00bbaed8",
  "target": "00bd6df0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaee0`](#insn-00bbaee0)

~~~json
{
  "source": "00bbaee0",
  "target": "00bbaeec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaee8`](#insn-00bbaee8)

~~~json
{
  "source": "00bbaee8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaef0`](#insn-00bbaef0)

~~~json
{
  "source": "00bbaef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaef4`](#insn-00bbaef4)

~~~json
{
  "source": "00bbaef4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaefc`](#insn-00bbaefc)

~~~json
{
  "source": "00bbaefc",
  "target": "00bdb440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
