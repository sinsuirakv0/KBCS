# 009dbbbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `009a5e5c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a5/009a5e5c.md) · 移動量 `+0x35d60`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0048.md#compare-9ce5a6a4afb4fa90c6096e3513946fac)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `009dbd58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbd58.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0032.md#compare-bd1d3b4113e836db38962086ef426176)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009dbbbc",
  "name": "FUN_009dbbbc",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a57cd388689d2c07aecf392818f884a1a9b77722938eda515f038e1a5458f34b",
  "source_text_sha256": "a57cd388689d2c07aecf392818f884a1a9b77722938eda515f038e1a5458f34b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009dbbbc",
        "009dbc33"
      ]
    ],
    "bytes_sha256": "1fc478dd8784effe430fcdf4317d2ad0f341db37899f61d7e5860910c4650d30",
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

## 疑似コード / UTF-8 643 bytes

~~~c

void FUN_009dbbbc(undefined8 param_1,long param_2,undefined8 param_3,undefined4 param_4,
                 undefined4 param_5,undefined4 param_6,int param_7)

{
  long lVar1;
  long lVar2;
  
  lVar1 = 0x1480;
  if (param_7 != 0) {
    lVar1 = 0x1aa0;
  }
  lVar2 = 0x1528;
  if (param_7 != 0) {
    lVar2 = 0x1b48;
  }
  FUN_00470074(param_2 + lVar1,param_2 + lVar2,param_6,0);
                    /* try { // try from 009dbc14 to 00adbc1f has its CatchHandler @ 009dbf28 */
                    /* try { // try from 009dbc20 to 00adbc27 has its CatchHandler @ 009dbf20 */
  FUN_0046bd14(param_3,param_2 + lVar1,param_4,param_5);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009dbbbc"></a> `009dbbbc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-009dbbc0"></a> `009dbbc0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009dbbc4"></a> `009dbbc4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dbbc8"></a> `009dbbc8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dbbcc"></a> `009dbbcc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009dbbd0"></a> `009dbbd0` | `df 00 00 71` | cmp w6,#0x0 | `FALL_THROUGH`
<a id="insn-009dbbd4"></a> `009dbbd4` | `08 54 83 52` | mov w8,#0x1aa0 | `FALL_THROUGH`
<a id="insn-009dbbd8"></a> `009dbbd8` | `09 90 82 52` | mov w9,#0x1480 | `FALL_THROUGH`
<a id="insn-009dbbdc"></a> `009dbbdc` | `0a 69 83 52` | mov w10,#0x1b48 | `FALL_THROUGH`
<a id="insn-009dbbe0"></a> `009dbbe0` | `0b a5 82 52` | mov w11,#0x1528 | `FALL_THROUGH`
<a id="insn-009dbbe4"></a> `009dbbe4` | `37 01 88 9a` | csel x23,x9,x8,eq | `FALL_THROUGH`
<a id="insn-009dbbe8"></a> `009dbbe8` | `68 01 8a 9a` | csel x8,x11,x10,eq | `FALL_THROUGH`
<a id="insn-009dbbec"></a> `009dbbec` | `f4 03 03 2a` | mov w20,w3 | `FALL_THROUGH`
<a id="insn-009dbbf0"></a> `009dbbf0` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-009dbbf4"></a> `009dbbf4` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-009dbbf8"></a> `009dbbf8` | `20 00 17 8b` | add x0,x1,x23 | `FALL_THROUGH`
<a id="insn-009dbbfc"></a> `009dbbfc` | `21 00 08 8b` | add x1,x1,x8 | `FALL_THROUGH`
<a id="insn-009dbc00"></a> `009dbc00` | `e2 03 05 2a` | mov w2,w5 | `FALL_THROUGH`
<a id="insn-009dbc04"></a> `009dbc04` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009dbc08"></a> `009dbc08` | `f3 03 04 2a` | mov w19,w4 | `FALL_THROUGH`
<a id="insn-009dbc0c"></a> `009dbc0c` | `1a 51 ea 97` | bl 0x00470074 | `UNCONDITIONAL_CALL`
<a id="insn-009dbc10"></a> `009dbc10` | `c1 02 17 8b` | add x1,x22,x23 | `FALL_THROUGH`
<a id="insn-009dbc14"></a> `009dbc14` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009dbc18"></a> `009dbc18` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-009dbc1c"></a> `009dbc1c` | `e3 03 13 2a` | mov w3,w19 | `FALL_THROUGH`
<a id="insn-009dbc20"></a> `009dbc20` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dbc24"></a> `009dbc24` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009dbc28"></a> `009dbc28` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dbc2c"></a> `009dbc2c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-009dbc30"></a> `009dbc30` | `39 40 ea 17` | b 0x0046bd14 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009dbbbc`](#insn-009dbbbc) 範囲 `[['009dbbbc', '009dbc13']]`
  - `FALL_THROUGH` [`009dbc10`](#insn-009dbc10) → [`009dbc14`](#insn-009dbc14)
- ブロック [`009dbc14`](#insn-009dbc14) 範囲 `[['009dbc14', '009dbc1f']]`
  - `FALL_THROUGH` [`009dbc1c`](#insn-009dbc1c) → [`009dbc20`](#insn-009dbc20)
- ブロック [`009dbc20`](#insn-009dbc20) 範囲 `[['009dbc20', '009dbc33']]`

## 命令位置別の参照

- [`009dbbbc`](#insn-009dbbbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbbc0`](#insn-009dbbc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbbc4`](#insn-009dbbc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbbc8`](#insn-009dbbc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbc0c`](#insn-009dbc0c) → [`00470074`](../00470/00470074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470074` · 推定シンボル `None` · 推定型 `None`
- [`009dbc20`](#insn-009dbc20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbc24`](#insn-009dbc24) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbc28`](#insn-009dbc28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbc2c`](#insn-009dbc2c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbc30`](#insn-009dbc30) → [`0046bd14`](../0046b/0046bd14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046bd14` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009dbbbc`](#insn-009dbbbc)

~~~json
{
  "source": "009dbbbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbbc0`](#insn-009dbbc0)

~~~json
{
  "source": "009dbbc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbbc4`](#insn-009dbbc4)

~~~json
{
  "source": "009dbbc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbbc8`](#insn-009dbbc8)

~~~json
{
  "source": "009dbbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbc0c`](#insn-009dbc0c)

~~~json
{
  "source": "009dbc0c",
  "target": "00470074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dbc20`](#insn-009dbc20)

~~~json
{
  "source": "009dbc20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbc24`](#insn-009dbc24)

~~~json
{
  "source": "009dbc24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbc28`](#insn-009dbc28)

~~~json
{
  "source": "009dbc28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbc2c`](#insn-009dbc2c)

~~~json
{
  "source": "009dbc2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbc30`](#insn-009dbc30)

~~~json
{
  "source": "009dbc30",
  "target": "0046bd14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
