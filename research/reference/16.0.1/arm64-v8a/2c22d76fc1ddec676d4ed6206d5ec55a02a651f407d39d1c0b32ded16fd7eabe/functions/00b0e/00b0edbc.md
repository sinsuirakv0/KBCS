# 00b0edbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0e994`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e994.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-dff6e0d364b07790fc605fa3efd56e2d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b0ee58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0ee58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0037.md#compare-0d8233a1056290d8f956f5e9bef4dbab)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0edbc",
  "name": "FUN_00b0edbc",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3c8bab51d6d15fa17081a7c27e509f5667d1843abf841ef99d13eb01e4655f5f",
  "source_text_sha256": "3c8bab51d6d15fa17081a7c27e509f5667d1843abf841ef99d13eb01e4655f5f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0edbc",
        "00b0eedb"
      ]
    ],
    "bytes_sha256": "a38180ec75d4a9d0f6369bac3587fa681b009adabcc8d104be844eed634ba38b",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a1a750](../00a1a/00a1a750.md)

## 呼び出し先

- [004802f8](../00480/004802f8.md)
- [004803f0](../00480/004803f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1132 bytes

~~~c

void FUN_00b0edbc(undefined4 *param_1,undefined8 param_2,uint param_3)

{
  byte bVar1;
  undefined4 uVar2;
  int iVar3;
  
  uVar2 = FUN_004803f0(param_2);
  *param_1 = uVar2;
  uVar2 = FUN_004803f0(param_2);
  param_1[3] = uVar2;
  uVar2 = FUN_004803f0(param_2);
  param_1[5] = uVar2;
  uVar2 = FUN_004803f0(param_2);
  param_1[4] = uVar2;
  uVar2 = FUN_004803f0(param_2);
  param_1[1] = uVar2;
  iVar3 = FUN_004803f0(param_2);
  *(bool *)(param_1 + 7) = iVar3 != 0;
  iVar3 = FUN_004803f0(param_2);
  *(bool *)((long)param_1 + 0x1d) = iVar3 != 0;
  iVar3 = FUN_004803f0(param_2);
  *(bool *)((long)param_1 + 0x1e) = iVar3 != 0;
  iVar3 = FUN_004803f0(param_2);
  *(bool *)((long)param_1 + 0x1f) = iVar3 != 0;
  uVar2 = FUN_004803f0(param_2);
  param_1[2] = uVar2;
  if (0x23 < (int)param_3) {
    iVar3 = FUN_004803f0(param_2);
    *(bool *)(param_1 + 8) = iVar3 != 0;
    if (0x9dc < param_3 >> 5) {
      iVar3 = FUN_004803f0(param_2);
      *(bool *)(param_1 + 9) = iVar3 != 0;
      if (0x18703 < param_3) {
        bVar1 = FUN_004802f8(param_2);
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
<a id="insn-00b0edbc"></a> `00b0edbc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b0edc0"></a> `00b0edc0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0edc4"></a> `00b0edc4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0edc8"></a> `00b0edc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b0edcc"></a> `00b0edcc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b0edd0"></a> `00b0edd0` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00b0edd4"></a> `00b0edd4` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00b0edd8"></a> `00b0edd8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b0eddc"></a> `00b0eddc` | `85 c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ede0"></a> `00b0ede0` | `60 02 00 b9` | str w0,[x19] | `FALL_THROUGH`
<a id="insn-00b0ede4"></a> `00b0ede4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ede8"></a> `00b0ede8` | `82 c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0edec"></a> `00b0edec` | `60 0e 00 b9` | str w0,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00b0edf0"></a> `00b0edf0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0edf4"></a> `00b0edf4` | `7f c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0edf8"></a> `00b0edf8` | `60 16 00 b9` | str w0,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00b0edfc"></a> `00b0edfc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ee00"></a> `00b0ee00` | `7c c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ee04"></a> `00b0ee04` | `60 12 00 b9` | str w0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ee08"></a> `00b0ee08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ee0c"></a> `00b0ee0c` | `79 c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ee10"></a> `00b0ee10` | `60 06 00 b9` | str w0,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00b0ee14"></a> `00b0ee14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ee18"></a> `00b0ee18` | `76 c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ee1c"></a> `00b0ee1c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b0ee20"></a> `00b0ee20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ee24"></a> `00b0ee24` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00b0ee28"></a> `00b0ee28` | `68 72 00 39` | strb w8,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00b0ee2c"></a> `00b0ee2c` | `71 c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ee30"></a> `00b0ee30` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b0ee34"></a> `00b0ee34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ee38"></a> `00b0ee38` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00b0ee3c"></a> `00b0ee3c` | `68 76 00 39` | strb w8,[x19, #0x1d] | `FALL_THROUGH`
<a id="insn-00b0ee40"></a> `00b0ee40` | `6c c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ee44"></a> `00b0ee44` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b0ee48"></a> `00b0ee48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ee4c"></a> `00b0ee4c` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00b0ee50"></a> `00b0ee50` | `68 7a 00 39` | strb w8,[x19, #0x1e] | `FALL_THROUGH`
<a id="insn-00b0ee54"></a> `00b0ee54` | `67 c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ee58"></a> `00b0ee58` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b0ee5c"></a> `00b0ee5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ee60"></a> `00b0ee60` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00b0ee64"></a> `00b0ee64` | `68 7e 00 39` | strb w8,[x19, #0x1f] | `FALL_THROUGH`
<a id="insn-00b0ee68"></a> `00b0ee68` | `62 c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ee6c"></a> `00b0ee6c` | `bf 92 00 71` | cmp w21,#0x24 | `FALL_THROUGH`
<a id="insn-00b0ee70"></a> `00b0ee70` | `60 0a 00 b9` | str w0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b0ee74"></a> `00b0ee74` | `cb 02 00 54` | b.lt 0x00b0eecc | `CONDITIONAL_JUMP`
<a id="insn-00b0ee78"></a> `00b0ee78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ee7c"></a> `00b0ee7c` | `5d c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ee80"></a> `00b0ee80` | `a8 7e 05 53` | lsr w8,w21,#0x5 | `FALL_THROUGH`
<a id="insn-00b0ee84"></a> `00b0ee84` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b0ee88"></a> `00b0ee88` | `e9 07 9f 1a` | cset w9,ne | `FALL_THROUGH`
<a id="insn-00b0ee8c"></a> `00b0ee8c` | `1f 75 27 71` | cmp w8,#0x9dd | `FALL_THROUGH`
<a id="insn-00b0ee90"></a> `00b0ee90` | `69 82 00 39` | strb w9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b0ee94"></a> `00b0ee94` | `c3 01 00 54` | b.cc 0x00b0eecc | `CONDITIONAL_JUMP`
<a id="insn-00b0ee98"></a> `00b0ee98` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ee9c"></a> `00b0ee9c` | `55 c5 e5 97` | bl 0x004803f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0eea0"></a> `00b0eea0` | `88 e0 90 52` | mov w8,#0x8704 | `FALL_THROUGH`
<a id="insn-00b0eea4"></a> `00b0eea4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b0eea8"></a> `00b0eea8` | `28 00 a0 72` | movk w8,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-00b0eeac"></a> `00b0eeac` | `e9 07 9f 1a` | cset w9,ne | `FALL_THROUGH`
<a id="insn-00b0eeb0"></a> `00b0eeb0` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00b0eeb4"></a> `00b0eeb4` | `69 92 00 39` | strb w9,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00b0eeb8"></a> `00b0eeb8` | `a3 00 00 54` | b.cc 0x00b0eecc | `CONDITIONAL_JUMP`
<a id="insn-00b0eebc"></a> `00b0eebc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0eec0"></a> `00b0eec0` | `0e c5 e5 97` | bl 0x004802f8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0eec4"></a> `00b0eec4` | `08 00 00 12` | and w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b0eec8"></a> `00b0eec8` | `68 b2 00 39` | strb w8,[x19, #0x2c] | `FALL_THROUGH`
<a id="insn-00b0eecc"></a> `00b0eecc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0eed0"></a> `00b0eed0` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0eed4"></a> `00b0eed4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b0eed8"></a> `00b0eed8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0edbc`](#insn-00b0edbc) 範囲 `[['00b0edbc', '00b0ee77']]`
  - `CONDITIONAL_JUMP` [`00b0ee74`](#insn-00b0ee74) → [`00b0eecc`](#insn-00b0eecc)
  - `FALL_THROUGH` [`00b0ee74`](#insn-00b0ee74) → [`00b0ee78`](#insn-00b0ee78)
- ブロック [`00b0ee78`](#insn-00b0ee78) 範囲 `[['00b0ee78', '00b0ee97']]`
  - `CONDITIONAL_JUMP` [`00b0ee94`](#insn-00b0ee94) → [`00b0eecc`](#insn-00b0eecc)
  - `FALL_THROUGH` [`00b0ee94`](#insn-00b0ee94) → [`00b0ee98`](#insn-00b0ee98)
- ブロック [`00b0ee98`](#insn-00b0ee98) 範囲 `[['00b0ee98', '00b0eebb']]`
  - `CONDITIONAL_JUMP` [`00b0eeb8`](#insn-00b0eeb8) → [`00b0eecc`](#insn-00b0eecc)
  - `FALL_THROUGH` [`00b0eeb8`](#insn-00b0eeb8) → [`00b0eebc`](#insn-00b0eebc)
- ブロック [`00b0eebc`](#insn-00b0eebc) 範囲 `[['00b0eebc', '00b0eecb']]`
  - `FALL_THROUGH` [`00b0eec8`](#insn-00b0eec8) → [`00b0eecc`](#insn-00b0eecc)
- ブロック [`00b0eecc`](#insn-00b0eecc) 範囲 `[['00b0eecc', '00b0eedb']]`

## 命令位置別の参照

- [`00b0edbc`](#insn-00b0edbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0edc0`](#insn-00b0edc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0edc4`](#insn-00b0edc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0eddc`](#insn-00b0eddc) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0ede8`](#insn-00b0ede8) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0edf4`](#insn-00b0edf4) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee00`](#insn-00b0ee00) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee0c`](#insn-00b0ee0c) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee18`](#insn-00b0ee18) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee2c`](#insn-00b0ee2c) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee40`](#insn-00b0ee40) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee54`](#insn-00b0ee54) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee68`](#insn-00b0ee68) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee74`](#insn-00b0ee74) → [`00b0eecc`](#insn-00b0eecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee7c`](#insn-00b0ee7c) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee94`](#insn-00b0ee94) → [`00b0eecc`](#insn-00b0eecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee9c`](#insn-00b0ee9c) → [`004803f0`](../00480/004803f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0eeb8`](#insn-00b0eeb8) → [`00b0eecc`](#insn-00b0eecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0eec0`](#insn-00b0eec0) → [`004802f8`](../00480/004802f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004802f8` · 推定シンボル `None` · 推定型 `None`
- [`00b0eecc`](#insn-00b0eecc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0eed0`](#insn-00b0eed0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0eed4`](#insn-00b0eed4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0edbc`](#insn-00b0edbc)

~~~json
{
  "source": "00b0edbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0edc0`](#insn-00b0edc0)

~~~json
{
  "source": "00b0edc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0edc4`](#insn-00b0edc4)

~~~json
{
  "source": "00b0edc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0eddc`](#insn-00b0eddc)

~~~json
{
  "source": "00b0eddc",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ede8`](#insn-00b0ede8)

~~~json
{
  "source": "00b0ede8",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0edf4`](#insn-00b0edf4)

~~~json
{
  "source": "00b0edf4",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ee00`](#insn-00b0ee00)

~~~json
{
  "source": "00b0ee00",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ee0c`](#insn-00b0ee0c)

~~~json
{
  "source": "00b0ee0c",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ee18`](#insn-00b0ee18)

~~~json
{
  "source": "00b0ee18",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ee2c`](#insn-00b0ee2c)

~~~json
{
  "source": "00b0ee2c",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ee40`](#insn-00b0ee40)

~~~json
{
  "source": "00b0ee40",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ee54`](#insn-00b0ee54)

~~~json
{
  "source": "00b0ee54",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ee68`](#insn-00b0ee68)

~~~json
{
  "source": "00b0ee68",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ee74`](#insn-00b0ee74)

~~~json
{
  "source": "00b0ee74",
  "target": "00b0eecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ee7c`](#insn-00b0ee7c)

~~~json
{
  "source": "00b0ee7c",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ee94`](#insn-00b0ee94)

~~~json
{
  "source": "00b0ee94",
  "target": "00b0eecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ee9c`](#insn-00b0ee9c)

~~~json
{
  "source": "00b0ee9c",
  "target": "004803f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0eeb8`](#insn-00b0eeb8)

~~~json
{
  "source": "00b0eeb8",
  "target": "00b0eecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0eec0`](#insn-00b0eec0)

~~~json
{
  "source": "00b0eec0",
  "target": "004802f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0eecc`](#insn-00b0eecc)

~~~json
{
  "source": "00b0eecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0eed0`](#insn-00b0eed0)

~~~json
{
  "source": "00b0eed0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0eed4`](#insn-00b0eed4)

~~~json
{
  "source": "00b0eed4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
