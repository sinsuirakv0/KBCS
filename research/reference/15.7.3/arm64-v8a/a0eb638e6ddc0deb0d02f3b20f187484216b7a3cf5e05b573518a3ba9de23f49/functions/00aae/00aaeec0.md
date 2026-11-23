# 00aaeec0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aaedf8`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaedf8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-78dc7aba048dd086a81a7cabb1bf89c9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aaef04`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaef04.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-b56ddf43ab600f7399bac67172abbc41)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaeec0",
  "name": "FUN_00aaeec0",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d84d5260c3625f383cd0bf9e68ef8bc2f4aba9a6cf382e594f19625f0614dc56",
  "source_text_sha256": "d84d5260c3625f383cd0bf9e68ef8bc2f4aba9a6cf382e594f19625f0614dc56",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaeec0",
        "00aaefdf"
      ]
    ],
    "bytes_sha256": "b5eff5554e9f0e0a15323fb74a54b2148f156e15def2cb46288d48cf66eac68c",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009bd6b8](../009bd/009bd6b8.md)

## 呼び出し先

- [0045d420](../0045d/0045d420.md)
- [0045d518](../0045d/0045d518.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1132 bytes

~~~c

void FUN_00aaeec0(undefined4 *param_1,undefined8 param_2,uint param_3)

{
  byte bVar1;
  undefined4 uVar2;
  int iVar3;
  
  uVar2 = FUN_0045d518(param_2);
  *param_1 = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[3] = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[5] = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[4] = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[1] = uVar2;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)(param_1 + 7) = iVar3 != 0;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)((long)param_1 + 0x1d) = iVar3 != 0;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)((long)param_1 + 0x1e) = iVar3 != 0;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)((long)param_1 + 0x1f) = iVar3 != 0;
  uVar2 = FUN_0045d518(param_2);
  param_1[2] = uVar2;
  if (0x23 < (int)param_3) {
    iVar3 = FUN_0045d518(param_2);
    *(bool *)(param_1 + 8) = iVar3 != 0;
    if (0x9dc < param_3 >> 5) {
      iVar3 = FUN_0045d518(param_2);
      *(bool *)(param_1 + 9) = iVar3 != 0;
      if (0x18703 < param_3) {
        bVar1 = FUN_0045d420(param_2);
        *(byte *)(param_1 + 0xb) = bVar1 & 1;
      }
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaeec0"></a> `00aaeec0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aaeec4"></a> `00aaeec4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaeec8"></a> `00aaeec8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaeecc"></a> `00aaeecc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aaeed0"></a> `00aaeed0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaeed4"></a> `00aaeed4` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00aaeed8"></a> `00aaeed8` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00aaeedc"></a> `00aaeedc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00aaeee0"></a> `00aaeee0` | `8e b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeee4"></a> `00aaeee4` | `60 02 00 b9` | str w0,[x19] | `FALL_THROUGH`
<a id="insn-00aaeee8"></a> `00aaeee8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaeeec"></a> `00aaeeec` | `8b b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeef0"></a> `00aaeef0` | `60 0e 00 b9` | str w0,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00aaeef4"></a> `00aaeef4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaeef8"></a> `00aaeef8` | `88 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeefc"></a> `00aaeefc` | `60 16 00 b9` | str w0,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00aaef00"></a> `00aaef00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaef04"></a> `00aaef04` | `85 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaef08"></a> `00aaef08` | `60 12 00 b9` | str w0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aaef0c"></a> `00aaef0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaef10"></a> `00aaef10` | `82 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaef14"></a> `00aaef14` | `60 06 00 b9` | str w0,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00aaef18"></a> `00aaef18` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaef1c"></a> `00aaef1c` | `7f b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaef20"></a> `00aaef20` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaef24"></a> `00aaef24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaef28"></a> `00aaef28` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00aaef2c"></a> `00aaef2c` | `68 72 00 39` | strb w8,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00aaef30"></a> `00aaef30` | `7a b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaef34"></a> `00aaef34` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaef38"></a> `00aaef38` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaef3c"></a> `00aaef3c` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00aaef40"></a> `00aaef40` | `68 76 00 39` | strb w8,[x19, #0x1d] | `FALL_THROUGH`
<a id="insn-00aaef44"></a> `00aaef44` | `75 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaef48"></a> `00aaef48` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaef4c"></a> `00aaef4c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaef50"></a> `00aaef50` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00aaef54"></a> `00aaef54` | `68 7a 00 39` | strb w8,[x19, #0x1e] | `FALL_THROUGH`
<a id="insn-00aaef58"></a> `00aaef58` | `70 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaef5c"></a> `00aaef5c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaef60"></a> `00aaef60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaef64"></a> `00aaef64` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00aaef68"></a> `00aaef68` | `68 7e 00 39` | strb w8,[x19, #0x1f] | `FALL_THROUGH`
<a id="insn-00aaef6c"></a> `00aaef6c` | `6b b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaef70"></a> `00aaef70` | `bf 92 00 71` | cmp w21,#0x24 | `FALL_THROUGH`
<a id="insn-00aaef74"></a> `00aaef74` | `60 0a 00 b9` | str w0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aaef78"></a> `00aaef78` | `cb 02 00 54` | b.lt 0x00aaefd0 | `CONDITIONAL_JUMP`
<a id="insn-00aaef7c"></a> `00aaef7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaef80"></a> `00aaef80` | `66 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaef84"></a> `00aaef84` | `a8 7e 05 53` | lsr w8,w21,#0x5 | `FALL_THROUGH`
<a id="insn-00aaef88"></a> `00aaef88` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaef8c"></a> `00aaef8c` | `e9 07 9f 1a` | cset w9,ne | `FALL_THROUGH`
<a id="insn-00aaef90"></a> `00aaef90` | `1f 75 27 71` | cmp w8,#0x9dd | `FALL_THROUGH`
<a id="insn-00aaef94"></a> `00aaef94` | `69 82 00 39` | strb w9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00aaef98"></a> `00aaef98` | `c3 01 00 54` | b.cc 0x00aaefd0 | `CONDITIONAL_JUMP`
<a id="insn-00aaef9c"></a> `00aaef9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaefa0"></a> `00aaefa0` | `5e b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaefa4"></a> `00aaefa4` | `88 e0 90 52` | mov w8,#0x8704 | `FALL_THROUGH`
<a id="insn-00aaefa8"></a> `00aaefa8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaefac"></a> `00aaefac` | `28 00 a0 72` | movk w8,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-00aaefb0"></a> `00aaefb0` | `e9 07 9f 1a` | cset w9,ne | `FALL_THROUGH`
<a id="insn-00aaefb4"></a> `00aaefb4` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00aaefb8"></a> `00aaefb8` | `69 92 00 39` | strb w9,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00aaefbc"></a> `00aaefbc` | `a3 00 00 54` | b.cc 0x00aaefd0 | `CONDITIONAL_JUMP`
<a id="insn-00aaefc0"></a> `00aaefc0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaefc4"></a> `00aaefc4` | `17 b9 e6 97` | bl 0x0045d420 | `UNCONDITIONAL_CALL`
<a id="insn-00aaefc8"></a> `00aaefc8` | `08 00 00 12` | and w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aaefcc"></a> `00aaefcc` | `68 b2 00 39` | strb w8,[x19, #0x2c] | `FALL_THROUGH`
<a id="insn-00aaefd0"></a> `00aaefd0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaefd4"></a> `00aaefd4` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaefd8"></a> `00aaefd8` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aaefdc"></a> `00aaefdc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaeec0`](#insn-00aaeec0) 範囲 `[['00aaeec0', '00aaef7b']]`
  - `CONDITIONAL_JUMP` [`00aaef78`](#insn-00aaef78) → [`00aaefd0`](#insn-00aaefd0)
  - `FALL_THROUGH` [`00aaef78`](#insn-00aaef78) → [`00aaef7c`](#insn-00aaef7c)
- ブロック [`00aaef7c`](#insn-00aaef7c) 範囲 `[['00aaef7c', '00aaef9b']]`
  - `CONDITIONAL_JUMP` [`00aaef98`](#insn-00aaef98) → [`00aaefd0`](#insn-00aaefd0)
  - `FALL_THROUGH` [`00aaef98`](#insn-00aaef98) → [`00aaef9c`](#insn-00aaef9c)
- ブロック [`00aaef9c`](#insn-00aaef9c) 範囲 `[['00aaef9c', '00aaefbf']]`
  - `CONDITIONAL_JUMP` [`00aaefbc`](#insn-00aaefbc) → [`00aaefd0`](#insn-00aaefd0)
  - `FALL_THROUGH` [`00aaefbc`](#insn-00aaefbc) → [`00aaefc0`](#insn-00aaefc0)
- ブロック [`00aaefc0`](#insn-00aaefc0) 範囲 `[['00aaefc0', '00aaefcf']]`
  - `FALL_THROUGH` [`00aaefcc`](#insn-00aaefcc) → [`00aaefd0`](#insn-00aaefd0)
- ブロック [`00aaefd0`](#insn-00aaefd0) 範囲 `[['00aaefd0', '00aaefdf']]`

## 命令位置別の参照

- [`00aaeec0`](#insn-00aaeec0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeec4`](#insn-00aaeec4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeec8`](#insn-00aaeec8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeee0`](#insn-00aaeee0) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaeeec`](#insn-00aaeeec) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaeef8`](#insn-00aaeef8) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaef04`](#insn-00aaef04) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaef10`](#insn-00aaef10) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaef1c`](#insn-00aaef1c) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaef30`](#insn-00aaef30) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaef44`](#insn-00aaef44) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaef58`](#insn-00aaef58) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaef6c`](#insn-00aaef6c) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaef78`](#insn-00aaef78) → [`00aaefd0`](#insn-00aaefd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaef80`](#insn-00aaef80) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaef98`](#insn-00aaef98) → [`00aaefd0`](#insn-00aaefd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaefa0`](#insn-00aaefa0) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaefbc`](#insn-00aaefbc) → [`00aaefd0`](#insn-00aaefd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaefc4`](#insn-00aaefc4) → [`0045d420`](../0045d/0045d420.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d420` · 推定シンボル `None` · 推定型 `None`
- [`00aaefd0`](#insn-00aaefd0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaefd4`](#insn-00aaefd4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaefd8`](#insn-00aaefd8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaeec0`](#insn-00aaeec0)

~~~json
{
  "source": "00aaeec0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeec4`](#insn-00aaeec4)

~~~json
{
  "source": "00aaeec4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeec8`](#insn-00aaeec8)

~~~json
{
  "source": "00aaeec8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeee0`](#insn-00aaeee0)

~~~json
{
  "source": "00aaeee0",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeeec`](#insn-00aaeeec)

~~~json
{
  "source": "00aaeeec",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeef8`](#insn-00aaeef8)

~~~json
{
  "source": "00aaeef8",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaef04`](#insn-00aaef04)

~~~json
{
  "source": "00aaef04",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaef10`](#insn-00aaef10)

~~~json
{
  "source": "00aaef10",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaef1c`](#insn-00aaef1c)

~~~json
{
  "source": "00aaef1c",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaef30`](#insn-00aaef30)

~~~json
{
  "source": "00aaef30",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaef44`](#insn-00aaef44)

~~~json
{
  "source": "00aaef44",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaef58`](#insn-00aaef58)

~~~json
{
  "source": "00aaef58",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaef6c`](#insn-00aaef6c)

~~~json
{
  "source": "00aaef6c",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaef78`](#insn-00aaef78)

~~~json
{
  "source": "00aaef78",
  "target": "00aaefd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaef80`](#insn-00aaef80)

~~~json
{
  "source": "00aaef80",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaef98`](#insn-00aaef98)

~~~json
{
  "source": "00aaef98",
  "target": "00aaefd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaefa0`](#insn-00aaefa0)

~~~json
{
  "source": "00aaefa0",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaefbc`](#insn-00aaefbc)

~~~json
{
  "source": "00aaefbc",
  "target": "00aaefd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaefc4`](#insn-00aaefc4)

~~~json
{
  "source": "00aaefc4",
  "target": "0045d420",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaefd0`](#insn-00aaefd0)

~~~json
{
  "source": "00aaefd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaefd4`](#insn-00aaefd4)

~~~json
{
  "source": "00aaefd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaefd8`](#insn-00aaefd8)

~~~json
{
  "source": "00aaefd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
