# 009dbcac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `009a5f4c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a5/009a5f4c.md) · 移動量 `+0x35d60`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0048.md#compare-38c08d41cd27acd1708c6646d3af4744)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `009dbe48`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbe48.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0032.md#compare-efa1e98d3b5ee5c45faaa245f6741709)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009dbcac",
  "name": "FUN_009dbcac",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8214ba32b92d57f6de53f8502d5ed4e079ede746ac6efcce2c2dde80b085a88",
  "source_text_sha256": "b8214ba32b92d57f6de53f8502d5ed4e079ede746ac6efcce2c2dde80b085a88",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009dbcac",
        "009dbd23"
      ]
    ],
    "bytes_sha256": "c30dc1b2a123135a7abeb1cb7e3ca97f6f98afd957ae19f21990f6a4e5a4d448",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00707ea0](../00707/00707ea0.md)

## 呼び出し先

- [0046bd14](../0046b/0046bd14.md)
- [00470074](../00470/00470074.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 546 bytes

~~~c

void FUN_009dbcac(undefined8 param_1,long param_2,undefined8 param_3,undefined4 param_4,
                 undefined4 param_5,undefined4 param_6,int param_7)

{
  long lVar1;
  long lVar2;
  
                    /* try { // try from 009dbcb0 to 00adbd83 has its CatchHandler @ 009db558 */
  lVar1 = 0x1560;
  if (param_7 != 0) {
    lVar1 = 0x1b80;
  }
  lVar2 = 0x1608;
  if (param_7 != 0) {
    lVar2 = 0x1c28;
  }
  FUN_00470074(param_2 + lVar1,param_2 + lVar2,param_6,0);
  FUN_0046bd14(param_3,param_2 + lVar1,param_4,param_5);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009dbcac"></a> `009dbcac` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-009dbcb0"></a> `009dbcb0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009dbcb4"></a> `009dbcb4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dbcb8"></a> `009dbcb8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dbcbc"></a> `009dbcbc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009dbcc0"></a> `009dbcc0` | `df 00 00 71` | cmp w6,#0x0 | `FALL_THROUGH`
<a id="insn-009dbcc4"></a> `009dbcc4` | `08 70 83 52` | mov w8,#0x1b80 | `FALL_THROUGH`
<a id="insn-009dbcc8"></a> `009dbcc8` | `09 ac 82 52` | mov w9,#0x1560 | `FALL_THROUGH`
<a id="insn-009dbccc"></a> `009dbccc` | `0a 85 83 52` | mov w10,#0x1c28 | `FALL_THROUGH`
<a id="insn-009dbcd0"></a> `009dbcd0` | `0b c1 82 52` | mov w11,#0x1608 | `FALL_THROUGH`
<a id="insn-009dbcd4"></a> `009dbcd4` | `37 01 88 9a` | csel x23,x9,x8,eq | `FALL_THROUGH`
<a id="insn-009dbcd8"></a> `009dbcd8` | `68 01 8a 9a` | csel x8,x11,x10,eq | `FALL_THROUGH`
<a id="insn-009dbcdc"></a> `009dbcdc` | `f4 03 03 2a` | mov w20,w3 | `FALL_THROUGH`
<a id="insn-009dbce0"></a> `009dbce0` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-009dbce4"></a> `009dbce4` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-009dbce8"></a> `009dbce8` | `20 00 17 8b` | add x0,x1,x23 | `FALL_THROUGH`
<a id="insn-009dbcec"></a> `009dbcec` | `21 00 08 8b` | add x1,x1,x8 | `FALL_THROUGH`
<a id="insn-009dbcf0"></a> `009dbcf0` | `e2 03 05 2a` | mov w2,w5 | `FALL_THROUGH`
<a id="insn-009dbcf4"></a> `009dbcf4` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009dbcf8"></a> `009dbcf8` | `f3 03 04 2a` | mov w19,w4 | `FALL_THROUGH`
<a id="insn-009dbcfc"></a> `009dbcfc` | `de 50 ea 97` | bl 0x00470074 | `UNCONDITIONAL_CALL`
<a id="insn-009dbd00"></a> `009dbd00` | `c1 02 17 8b` | add x1,x22,x23 | `FALL_THROUGH`
<a id="insn-009dbd04"></a> `009dbd04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009dbd08"></a> `009dbd08` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-009dbd0c"></a> `009dbd0c` | `e3 03 13 2a` | mov w3,w19 | `FALL_THROUGH`
<a id="insn-009dbd10"></a> `009dbd10` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dbd14"></a> `009dbd14` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009dbd18"></a> `009dbd18` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dbd1c"></a> `009dbd1c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-009dbd20"></a> `009dbd20` | `fd 3f ea 17` | b 0x0046bd14 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009dbcac`](#insn-009dbcac) 範囲 `[['009dbcac', '009dbcaf']]`
  - `FALL_THROUGH` [`009dbcac`](#insn-009dbcac) → [`009dbcb0`](#insn-009dbcb0)
- ブロック [`009dbcb0`](#insn-009dbcb0) 範囲 `[['009dbcb0', '009dbd23']]`

## 命令位置別の参照

- [`009dbcac`](#insn-009dbcac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbcb0`](#insn-009dbcb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbcb4`](#insn-009dbcb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbcb8`](#insn-009dbcb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbcfc`](#insn-009dbcfc) → [`00470074`](../00470/00470074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470074` · 推定シンボル `None` · 推定型 `None`
- [`009dbd10`](#insn-009dbd10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbd14`](#insn-009dbd14) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbd18`](#insn-009dbd18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbd1c`](#insn-009dbd1c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbd20`](#insn-009dbd20) → [`0046bd14`](../0046b/0046bd14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046bd14` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009dbcac`](#insn-009dbcac)

~~~json
{
  "source": "009dbcac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbcb0`](#insn-009dbcb0)

~~~json
{
  "source": "009dbcb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbcb4`](#insn-009dbcb4)

~~~json
{
  "source": "009dbcb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbcb8`](#insn-009dbcb8)

~~~json
{
  "source": "009dbcb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbcfc`](#insn-009dbcfc)

~~~json
{
  "source": "009dbcfc",
  "target": "00470074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dbd10`](#insn-009dbd10)

~~~json
{
  "source": "009dbd10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbd14`](#insn-009dbd14)

~~~json
{
  "source": "009dbd14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbd18`](#insn-009dbd18)

~~~json
{
  "source": "009dbd18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbd1c`](#insn-009dbd1c)

~~~json
{
  "source": "009dbd1c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbd20`](#insn-009dbd20)

~~~json
{
  "source": "009dbd20",
  "target": "0046bd14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
