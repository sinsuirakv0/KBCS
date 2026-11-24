# 00bfb1bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e774`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e774.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-db67c231f012208f8c2e58c858bc3edd)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb5e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb5e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-62e37bdcaef166ebe1c8d347e50b11ee)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb1bc",
  "name": "_ZNSt6__ndk18ios_base4initEPv",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acde8554ac3feef665b92a85df4419b1a07d924ab4dfc455ec64c78821db8f40",
  "source_text_sha256": "acde8554ac3feef665b92a85df4419b1a07d924ab4dfc455ec64c78821db8f40",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfb1bc",
        "00bfb207"
      ]
    ],
    "bytes_sha256": "62b793db518f122cb634ceabcc2af0c349b60ce0e3d7ee574feb374cebcff68d",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c57de0](../00c57/00c57de0.md)

## 呼び出し先

- [00c5a3a0](../00c5a/00c5a3a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 948 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void _ZNSt6__ndk18ios_base4initEPv(long param_1,long param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  uVar2 = _UNK_002c2ff8;
  uVar1 = _DAT_002c2ff0;
  *(long *)(param_1 + 0x28) = param_2;
  *(uint *)(param_1 + 0x20) = (uint)(param_2 == 0);
  *(undefined4 *)(param_1 + 0x24) = 0;
  *(undefined8 *)(param_1 + 0x18) = uVar2;
  *(undefined8 *)(param_1 + 0x10) = uVar1;
  *(undefined4 *)(param_1 + 8) = 0x1002;
  *(undefined8 *)(param_1 + 0x40) = 0;
  *(undefined8 *)(param_1 + 0x38) = 0;
  *(undefined8 *)(param_1 + 0x50) = 0;
  *(undefined8 *)(param_1 + 0x48) = 0;
  *(undefined8 *)(param_1 + 0x60) = 0;
  *(undefined8 *)(param_1 + 0x58) = 0;
  *(undefined8 *)(param_1 + 0x70) = 0;
  *(undefined8 *)(param_1 + 0x68) = 0;
  *(undefined8 *)(param_1 + 0x80) = 0;
  *(undefined8 *)(param_1 + 0x78) = 0;
  _ZNSt6__ndk16localeC2Ev(param_1 + 0x30);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfb1bc"></a> `00bfb1bc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfb1c0"></a> `00bfb1c0` | `29 b6 ff f0` | adrp x9,0x2c2000 | `FALL_THROUGH`
<a id="insn-00bfb1c4"></a> `00bfb1c4` | `3f 00 00 f1` | cmp x1,#0x0 | `FALL_THROUGH`
<a id="insn-00bfb1c8"></a> `00bfb1c8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bfb1cc"></a> `00bfb1cc` | `20 fd c3 3d` | ldr q0,[x9, #0xff0] | `FALL_THROUGH`
<a id="insn-00bfb1d0"></a> `00bfb1d0` | `e9 17 9f 1a` | cset w9,eq | `FALL_THROUGH`
<a id="insn-00bfb1d4"></a> `00bfb1d4` | `01 14 00 f9` | str x1,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00bfb1d8"></a> `00bfb1d8` | `09 7c 04 29` | stp w9,wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb1dc"></a> `00bfb1dc` | `49 00 82 52` | mov w9,#0x1002 | `FALL_THROUGH`
<a id="insn-00bfb1e0"></a> `00bfb1e0` | `00 04 80 3d` | str q0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb1e4"></a> `00bfb1e4` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bfb1e8"></a> `00bfb1e8` | `09 08 00 b9` | str w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfb1ec"></a> `00bfb1ec` | `00 80 83 3c` | stur q0,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00bfb1f0"></a> `00bfb1f0` | `00 80 84 3c` | stur q0,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00bfb1f4"></a> `00bfb1f4` | `00 80 85 3c` | stur q0,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb1f8"></a> `00bfb1f8` | `00 80 86 3c` | stur q0,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00bfb1fc"></a> `00bfb1fc` | `00 c0 00 91` | add x0,x0,#0x30 | `FALL_THROUGH`
<a id="insn-00bfb200"></a> `00bfb200` | `00 81 87 3c` | stur q0,[x8, #0x78] | `FALL_THROUGH`
<a id="insn-00bfb204"></a> `00bfb204` | `67 7c 01 14` | b 0x00c5a3a0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfb1bc`](#insn-00bfb1bc) 範囲 `[['00bfb1bc', '00bfb207']]`

## 命令位置別の参照

- [`00bfb1cc`](#insn-00bfb1cc) → `002c2ff0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb204`](#insn-00bfb204) → [`00c5a3a0`](../00c5a/00c5a3a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a3a0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfb1cc`](#insn-00bfb1cc)

~~~json
{
  "source": "00bfb1cc",
  "target": "002c2ff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb204`](#insn-00bfb204)

~~~json
{
  "source": "00bfb204",
  "target": "00c5a3a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
