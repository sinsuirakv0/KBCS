# 00bfeafc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfe6d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe6d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-f935e25207e7e6e2175b6b2825b57704)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfeb98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfeb98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0087.md#compare-5b686c5e65f19d7d579faa2ab51e7928)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfeafc",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEb",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3182d4ec74c8095e6a3e04ac4549170e5ffe1c5de041e7296ac1763f6bc501a4",
  "source_text_sha256": "3182d4ec74c8095e6a3e04ac4549170e5ffe1c5de041e7296ac1763f6bc501a4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfeafc",
        "00bfec27"
      ]
    ],
    "bytes_sha256": "0f37a88357304a044cd4a73fc889bab88088703efe3830c9f1a1adc3fd6e678a",
    "instruction_count": 75,
    "instruction_bytes": 300,
    "body_bytes": 300,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58260](../00c58/00c58260.md)
- [00c58270](../00c58/00c58270.md)
- [00c58280](../00c58/00c58280.md)
- [00c58290](../00c58/00c58290.md)
- [00c582a0](../00c58/00c582a0.md)
- [00c582b0](../00c58/00c582b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1627 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEb(long *param_1,uint param_2)

{
  uint uVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  undefined8 uVar5;
  char local_58 [16];
  undefined1 auStack_48 [8];
  
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_(local_58,param_1);
  if (local_58[0] != '\0') {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,(long)param_1 + *(long *)(*param_1 + -0x18));
    plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_48,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b838
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_48);
    lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar1 = *(uint *)(lVar4 + 0x90);
    uVar5 = *(undefined8 *)(lVar4 + 0x28);
    if (uVar1 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,lVar4);
      plVar3 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_48,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
      uVar1 = (**(code **)(*plVar3 + 0x38))(plVar3,0x20);
      _ZNSt6__ndk16localeD1Ev(auStack_48);
      uVar1 = uVar1 & 0xff;
      *(uint *)(lVar4 + 0x90) = uVar1;
    }
    lVar4 = (**(code **)(*plVar2 + 0x18))(plVar2,uVar5,lVar4,uVar1,param_2 & 1);
    if (lVar4 == 0) {
      lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
      _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | 5);
    }
  }
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD2Ev(local_58);
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfeafc"></a> `00bfeafc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfeb00"></a> `00bfeb00` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfeb04"></a> `00bfeb04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfeb08"></a> `00bfeb08` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfeb0c"></a> `00bfeb0c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfeb10"></a> `00bfeb10` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfeb14"></a> `00bfeb14` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfeb18"></a> `00bfeb18` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00bfeb1c"></a> `00bfeb1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfeb20"></a> `00bfeb20` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeb24"></a> `00bfeb24` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfeb28"></a> `00bfeb28` | `ce 65 01 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeb2c"></a> `00bfeb2c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfeb30"></a> `00bfeb30` | `88 06 00 34` | cbz w8,0x00bfec00 | `CONDITIONAL_JUMP`
<a id="insn-00bfeb34"></a> `00bfeb34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfeb38"></a> `00bfeb38` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfeb3c"></a> `00bfeb3c` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeb40"></a> `00bfeb40` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfeb44"></a> `00bfeb44` | `cb 65 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeb48"></a> `00bfeb48` | `e1 04 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfeb4c"></a> `00bfeb4c` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeb50"></a> `00bfeb50` | `21 1c 44 f9` | ldr x1,[x1, #0x838] | `FALL_THROUGH`
<a id="insn-00bfeb54"></a> `00bfeb54` | `cb 65 01 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeb58"></a> `00bfeb58` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bfeb5c"></a> `00bfeb5c` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeb60"></a> `00bfeb60` | `cc 65 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeb64"></a> `00bfeb64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfeb68"></a> `00bfeb68` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfeb6c"></a> `00bfeb6c` | `62 02 08 8b` | add x2,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfeb70"></a> `00bfeb70` | `43 90 40 b9` | ldr w3,[x2, #0x90] | `FALL_THROUGH`
<a id="insn-00bfeb74"></a> `00bfeb74` | `56 14 40 f9` | ldr x22,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bfeb78"></a> `00bfeb78` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bfeb7c"></a> `00bfeb7c` | `61 02 00 54` | b.ne 0x00bfebc8 | `CONDITIONAL_JUMP`
<a id="insn-00bfeb80"></a> `00bfeb80` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeb84"></a> `00bfeb84` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bfeb88"></a> `00bfeb88` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bfeb8c"></a> `00bfeb8c` | `b9 65 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeb90"></a> `00bfeb90` | `e1 04 00 90` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bfeb94"></a> `00bfeb94` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeb98"></a> `00bfeb98` | `21 18 46 f9` | ldr x1,[x1, #0xc30] | `FALL_THROUGH`
<a id="insn-00bfeb9c"></a> `00bfeb9c` | `b9 65 01 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeba0"></a> `00bfeba0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfeba4"></a> `00bfeba4` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfeba8"></a> `00bfeba8` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bfebac"></a> `00bfebac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfebb0"></a> `00bfebb0` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bfebb4"></a> `00bfebb4` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfebb8"></a> `00bfebb8` | `b6 65 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bfebbc"></a> `00bfebbc` | `e3 1e 00 12` | and w3,w23,#0xff | `FALL_THROUGH`
<a id="insn-00bfebc0"></a> `00bfebc0` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bfebc4"></a> `00bfebc4` | `03 93 00 b9` | str w3,[x24, #0x90] | `FALL_THROUGH`
<a id="insn-00bfebc8"></a> `00bfebc8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bfebcc"></a> `00bfebcc` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bfebd0"></a> `00bfebd0` | `84 02 00 12` | and w4,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfebd4"></a> `00bfebd4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfebd8"></a> `00bfebd8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bfebdc"></a> `00bfebdc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfebe0"></a> `00bfebe0` | `00 01 00 b5` | cbnz x0,0x00bfec00 | `CONDITIONAL_JUMP`
<a id="insn-00bfebe4"></a> `00bfebe4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfebe8"></a> `00bfebe8` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bfebec"></a> `00bfebec` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfebf0"></a> `00bfebf0` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfebf4"></a> `00bfebf4` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfebf8"></a> `00bfebf8` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bfebfc"></a> `00bfebfc` | `a9 65 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfec00"></a> `00bfec00` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfec04"></a> `00bfec04` | `ab 65 01 94` | bl 0x00c582b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfec08"></a> `00bfec08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfec0c"></a> `00bfec0c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfec10"></a> `00bfec10` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfec14"></a> `00bfec14` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfec18"></a> `00bfec18` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfec1c"></a> `00bfec1c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfec20"></a> `00bfec20` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfec24"></a> `00bfec24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfeafc`](#insn-00bfeafc) 範囲 `[['00bfeafc', '00bfeb33']]`
  - `CONDITIONAL_JUMP` [`00bfeb30`](#insn-00bfeb30) → [`00bfec00`](#insn-00bfec00)
  - `FALL_THROUGH` [`00bfeb30`](#insn-00bfeb30) → [`00bfeb34`](#insn-00bfeb34)
- ブロック [`00bfeb34`](#insn-00bfeb34) 範囲 `[['00bfeb34', '00bfeb7f']]`
  - `CONDITIONAL_JUMP` [`00bfeb7c`](#insn-00bfeb7c) → [`00bfebc8`](#insn-00bfebc8)
  - `FALL_THROUGH` [`00bfeb7c`](#insn-00bfeb7c) → [`00bfeb80`](#insn-00bfeb80)
- ブロック [`00bfeb80`](#insn-00bfeb80) 範囲 `[['00bfeb80', '00bfebc7']]`
  - `FALL_THROUGH` [`00bfebc4`](#insn-00bfebc4) → [`00bfebc8`](#insn-00bfebc8)
- ブロック [`00bfebc8`](#insn-00bfebc8) 範囲 `[['00bfebc8', '00bfebe3']]`
  - `CONDITIONAL_JUMP` [`00bfebe0`](#insn-00bfebe0) → [`00bfec00`](#insn-00bfec00)
  - `FALL_THROUGH` [`00bfebe0`](#insn-00bfebe0) → [`00bfebe4`](#insn-00bfebe4)
- ブロック [`00bfebe4`](#insn-00bfebe4) 範囲 `[['00bfebe4', '00bfebff']]`
  - `FALL_THROUGH` [`00bfebfc`](#insn-00bfebfc) → [`00bfec00`](#insn-00bfec00)
- ブロック [`00bfec00`](#insn-00bfec00) 範囲 `[['00bfec00', '00bfec27']]`

## 命令位置別の参照

- [`00bfeb04`](#insn-00bfeb04) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb08`](#insn-00bfeb08) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb0c`](#insn-00bfeb0c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb10`](#insn-00bfeb10) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb28`](#insn-00bfeb28) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb2c`](#insn-00bfeb2c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb30`](#insn-00bfeb30) → [`00bfec00`](#insn-00bfec00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb44`](#insn-00bfeb44) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb50`](#insn-00bfeb50) → `00c9b838`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfeb50`](#insn-00bfeb50) → `01127b98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfeb54`](#insn-00bfeb54) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb60`](#insn-00bfeb60) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb7c`](#insn-00bfeb7c) → [`00bfebc8`](#insn-00bfebc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb8c`](#insn-00bfeb8c) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb98`](#insn-00bfeb98) → `00c9ac30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfeb98`](#insn-00bfeb98) → `01127e18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bfeb9c`](#insn-00bfeb9c) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00bfebb8`](#insn-00bfebb8) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bfebe0`](#insn-00bfebe0) → [`00bfec00`](#insn-00bfec00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfebfc`](#insn-00bfebfc) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfec04`](#insn-00bfec04) → [`00c582b0`](../00c58/00c582b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582b0` · 推定シンボル `None` · 推定型 `None`
- [`00bfec0c`](#insn-00bfec0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec10`](#insn-00bfec10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec14`](#insn-00bfec14) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec18`](#insn-00bfec18) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfeb04`](#insn-00bfeb04)

~~~json
{
  "source": "00bfeb04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb08`](#insn-00bfeb08)

~~~json
{
  "source": "00bfeb08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb0c`](#insn-00bfeb0c)

~~~json
{
  "source": "00bfeb0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb10`](#insn-00bfeb10)

~~~json
{
  "source": "00bfeb10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb28`](#insn-00bfeb28)

~~~json
{
  "source": "00bfeb28",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeb2c`](#insn-00bfeb2c)

~~~json
{
  "source": "00bfeb2c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb30`](#insn-00bfeb30)

~~~json
{
  "source": "00bfeb30",
  "target": "00bfec00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb44`](#insn-00bfeb44)

~~~json
{
  "source": "00bfeb44",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeb50`](#insn-00bfeb50)

~~~json
{
  "source": "00bfeb50",
  "target": "00c9b838",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b838",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfeb50`](#insn-00bfeb50)

~~~json
{
  "source": "00bfeb50",
  "target": "01127b98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfeb54`](#insn-00bfeb54)

~~~json
{
  "source": "00bfeb54",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeb60`](#insn-00bfeb60)

~~~json
{
  "source": "00bfeb60",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeb7c`](#insn-00bfeb7c)

~~~json
{
  "source": "00bfeb7c",
  "target": "00bfebc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb8c`](#insn-00bfeb8c)

~~~json
{
  "source": "00bfeb8c",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeb98`](#insn-00bfeb98)

~~~json
{
  "source": "00bfeb98",
  "target": "00c9ac30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac30",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfeb98`](#insn-00bfeb98)

~~~json
{
  "source": "00bfeb98",
  "target": "01127e18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfeb9c`](#insn-00bfeb9c)

~~~json
{
  "source": "00bfeb9c",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfebb8`](#insn-00bfebb8)

~~~json
{
  "source": "00bfebb8",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfebe0`](#insn-00bfebe0)

~~~json
{
  "source": "00bfebe0",
  "target": "00bfec00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfebfc`](#insn-00bfebfc)

~~~json
{
  "source": "00bfebfc",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfec04`](#insn-00bfec04)

~~~json
{
  "source": "00bfec04",
  "target": "00c582b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfec0c`](#insn-00bfec0c)

~~~json
{
  "source": "00bfec0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec10`](#insn-00bfec10)

~~~json
{
  "source": "00bfec10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec14`](#insn-00bfec14)

~~~json
{
  "source": "00bfec14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec18`](#insn-00bfec18)

~~~json
{
  "source": "00bfec18",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
