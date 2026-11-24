# 00a7dfcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a2013c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a2013c.md) · 移動量 `+0x5de90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0013.md#compare-3caf7c352a8dab6aa3548d65d869bb4a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a7e1c4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e1c4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0061.md#compare-d2d33cab712b34d01db09d7acb9c6a37)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a7dfcc",
  "name": "FUN_00a7dfcc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e10ef441f62fa93006a341a6b733d14583824856e6476febff88f7e1218f124f",
  "source_text_sha256": "e10ef441f62fa93006a341a6b733d14583824856e6476febff88f7e1218f124f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a7dfcc",
        "00a7dfff"
      ]
    ],
    "bytes_sha256": "5320f7f62e97528059b570ed9f30a9f9a95785ad9877d0989135eaf28cf29310",
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

void FUN_00a7dfcc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c8bb20;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a7dfcc"></a> `00a7dfcc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a7dfd0"></a> `00a7dfd0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7dfd4"></a> `00a7dfd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a7dfd8"></a> `00a7dfd8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a7dfdc"></a> `00a7dfdc` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00a7dfe0"></a> `00a7dfe0` | `ac 66 07 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00a7dfe4"></a> `00a7dfe4` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a7dfe8"></a> `00a7dfe8` | `68 10 00 d0` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a7dfec"></a> `00a7dfec` | `08 81 2c 91` | add x8,x8,#0xb20 | `FALL_THROUGH`
<a id="insn-00a7dff0"></a> `00a7dff0` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00a7dff4"></a> `00a7dff4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7dff8"></a> `00a7dff8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a7dffc"></a> `00a7dffc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a7dfcc`](#insn-00a7dfcc) 範囲 `[['00a7dfcc', '00a7dfff']]`

## 命令位置別の参照

- [`00a7dfcc`](#insn-00a7dfcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dfd0`](#insn-00a7dfd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dfe0`](#insn-00a7dfe0) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00a7dff0`](#insn-00a7dff0) → `00c8bb20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a7dff4`](#insn-00a7dff4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dff8`](#insn-00a7dff8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a7dfcc`](#insn-00a7dfcc)

~~~json
{
  "source": "00a7dfcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dfd0`](#insn-00a7dfd0)

~~~json
{
  "source": "00a7dfd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dfe0`](#insn-00a7dfe0)

~~~json
{
  "source": "00a7dfe0",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7dff0`](#insn-00a7dff0)

~~~json
{
  "source": "00a7dff0",
  "target": "00c8bb20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bb20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a7dff4`](#insn-00a7dff4)

~~~json
{
  "source": "00a7dff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dff8`](#insn-00a7dff8)

~~~json
{
  "source": "00a7dff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
