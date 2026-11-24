# 00bffd1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfed28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfed28.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-b8908d9209b31f8e6f8538d548677ef0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffd1c",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEx",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99efb7b31bb902d5c51a73635a323d5130e2ce01bfcb4a979d4a9e7d70086e49",
  "source_text_sha256": "99efb7b31bb902d5c51a73635a323d5130e2ce01bfcb4a979d4a9e7d70086e49",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffd1c",
        "00bffe47"
      ]
    ],
    "bytes_sha256": "9cb0840a5873079179d05dfea351071cf2973a0aa7a0527fb93eb09cbb32c8d7",
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

- [00c59300](../00c59/00c59300.md)
- [00c59310](../00c59/00c59310.md)
- [00c59320](../00c59/00c59320.md)
- [00c59330](../00c59/00c59330.md)
- [00c59340](../00c59/00c59340.md)
- [00c59350](../00c59/00c59350.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1629 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEx(long *param_1,undefined8 param_2)

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
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9c8d8
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_48);
    lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar1 = *(uint *)(lVar4 + 0x90);
    uVar5 = *(undefined8 *)(lVar4 + 0x28);
    if (uVar1 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,lVar4);
      plVar3 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_48,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9bcd0);
      uVar1 = (**(code **)(*plVar3 + 0x38))(plVar3,0x20);
      _ZNSt6__ndk16localeD1Ev(auStack_48);
      uVar1 = uVar1 & 0xff;
      *(uint *)(lVar4 + 0x90) = uVar1;
    }
    lVar4 = (**(code **)(*plVar2 + 0x28))(plVar2,uVar5,lVar4,uVar1,param_2);
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
<a id="insn-00bffd1c"></a> `00bffd1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffd20"></a> `00bffd20` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bffd24"></a> `00bffd24` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bffd28"></a> `00bffd28` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bffd2c"></a> `00bffd2c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bffd30"></a> `00bffd30` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bffd34"></a> `00bffd34` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bffd38"></a> `00bffd38` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bffd3c"></a> `00bffd3c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bffd40"></a> `00bffd40` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bffd44"></a> `00bffd44` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bffd48"></a> `00bffd48` | `6e 65 01 94` | bl 0x00c59300 | `UNCONDITIONAL_CALL`
<a id="insn-00bffd4c"></a> `00bffd4c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bffd50"></a> `00bffd50` | `88 06 00 34` | cbz w8,0x00bffe20 | `CONDITIONAL_JUMP`
<a id="insn-00bffd54"></a> `00bffd54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bffd58"></a> `00bffd58` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bffd5c"></a> `00bffd5c` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffd60"></a> `00bffd60` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bffd64"></a> `00bffd64` | `6b 65 01 94` | bl 0x00c59310 | `UNCONDITIONAL_CALL`
<a id="insn-00bffd68"></a> `00bffd68` | `e1 04 00 b0` | adrp x1,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bffd6c"></a> `00bffd6c` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffd70"></a> `00bffd70` | `21 6c 44 f9` | ldr x1,[x1, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bffd74"></a> `00bffd74` | `6b 65 01 94` | bl 0x00c59320 | `UNCONDITIONAL_CALL`
<a id="insn-00bffd78"></a> `00bffd78` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bffd7c"></a> `00bffd7c` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffd80"></a> `00bffd80` | `6c 65 01 94` | bl 0x00c59330 | `UNCONDITIONAL_CALL`
<a id="insn-00bffd84"></a> `00bffd84` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bffd88"></a> `00bffd88` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bffd8c"></a> `00bffd8c` | `62 02 08 8b` | add x2,x19,x8 | `FALL_THROUGH`
<a id="insn-00bffd90"></a> `00bffd90` | `43 90 40 b9` | ldr w3,[x2, #0x90] | `FALL_THROUGH`
<a id="insn-00bffd94"></a> `00bffd94` | `56 14 40 f9` | ldr x22,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bffd98"></a> `00bffd98` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bffd9c"></a> `00bffd9c` | `61 02 00 54` | b.ne 0x00bffde8 | `CONDITIONAL_JUMP`
<a id="insn-00bffda0"></a> `00bffda0` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffda4"></a> `00bffda4` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bffda8"></a> `00bffda8` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bffdac"></a> `00bffdac` | `59 65 01 94` | bl 0x00c59310 | `UNCONDITIONAL_CALL`
<a id="insn-00bffdb0"></a> `00bffdb0` | `e1 04 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bffdb4"></a> `00bffdb4` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffdb8"></a> `00bffdb8` | `21 68 46 f9` | ldr x1,[x1, #0xcd0] | `FALL_THROUGH`
<a id="insn-00bffdbc"></a> `00bffdbc` | `59 65 01 94` | bl 0x00c59320 | `UNCONDITIONAL_CALL`
<a id="insn-00bffdc0"></a> `00bffdc0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bffdc4"></a> `00bffdc4` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bffdc8"></a> `00bffdc8` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bffdcc"></a> `00bffdcc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bffdd0"></a> `00bffdd0` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bffdd4"></a> `00bffdd4` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffdd8"></a> `00bffdd8` | `56 65 01 94` | bl 0x00c59330 | `UNCONDITIONAL_CALL`
<a id="insn-00bffddc"></a> `00bffddc` | `e3 1e 00 12` | and w3,w23,#0xff | `FALL_THROUGH`
<a id="insn-00bffde0"></a> `00bffde0` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bffde4"></a> `00bffde4` | `03 93 00 b9` | str w3,[x24, #0x90] | `FALL_THROUGH`
<a id="insn-00bffde8"></a> `00bffde8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bffdec"></a> `00bffdec` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bffdf0"></a> `00bffdf0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bffdf4"></a> `00bffdf4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bffdf8"></a> `00bffdf8` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00bffdfc"></a> `00bffdfc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bffe00"></a> `00bffe00` | `00 01 00 b5` | cbnz x0,0x00bffe20 | `CONDITIONAL_JUMP`
<a id="insn-00bffe04"></a> `00bffe04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bffe08"></a> `00bffe08` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bffe0c"></a> `00bffe0c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bffe10"></a> `00bffe10` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bffe14"></a> `00bffe14` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bffe18"></a> `00bffe18` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bffe1c"></a> `00bffe1c` | `49 65 01 94` | bl 0x00c59340 | `UNCONDITIONAL_CALL`
<a id="insn-00bffe20"></a> `00bffe20` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bffe24"></a> `00bffe24` | `4b 65 01 94` | bl 0x00c59350 | `UNCONDITIONAL_CALL`
<a id="insn-00bffe28"></a> `00bffe28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bffe2c"></a> `00bffe2c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bffe30"></a> `00bffe30` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bffe34"></a> `00bffe34` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bffe38"></a> `00bffe38` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bffe3c"></a> `00bffe3c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bffe40"></a> `00bffe40` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffe44"></a> `00bffe44` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffd1c`](#insn-00bffd1c) 範囲 `[['00bffd1c', '00bffd53']]`
  - `CONDITIONAL_JUMP` [`00bffd50`](#insn-00bffd50) → [`00bffe20`](#insn-00bffe20)
  - `FALL_THROUGH` [`00bffd50`](#insn-00bffd50) → [`00bffd54`](#insn-00bffd54)
- ブロック [`00bffd54`](#insn-00bffd54) 範囲 `[['00bffd54', '00bffd9f']]`
  - `CONDITIONAL_JUMP` [`00bffd9c`](#insn-00bffd9c) → [`00bffde8`](#insn-00bffde8)
  - `FALL_THROUGH` [`00bffd9c`](#insn-00bffd9c) → [`00bffda0`](#insn-00bffda0)
- ブロック [`00bffda0`](#insn-00bffda0) 範囲 `[['00bffda0', '00bffde7']]`
  - `FALL_THROUGH` [`00bffde4`](#insn-00bffde4) → [`00bffde8`](#insn-00bffde8)
- ブロック [`00bffde8`](#insn-00bffde8) 範囲 `[['00bffde8', '00bffe03']]`
  - `CONDITIONAL_JUMP` [`00bffe00`](#insn-00bffe00) → [`00bffe20`](#insn-00bffe20)
  - `FALL_THROUGH` [`00bffe00`](#insn-00bffe00) → [`00bffe04`](#insn-00bffe04)
- ブロック [`00bffe04`](#insn-00bffe04) 範囲 `[['00bffe04', '00bffe1f']]`
  - `FALL_THROUGH` [`00bffe1c`](#insn-00bffe1c) → [`00bffe20`](#insn-00bffe20)
- ブロック [`00bffe20`](#insn-00bffe20) 範囲 `[['00bffe20', '00bffe47']]`

## 命令位置別の参照

- [`00bffd24`](#insn-00bffd24) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffd28`](#insn-00bffd28) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffd2c`](#insn-00bffd2c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffd30`](#insn-00bffd30) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffd48`](#insn-00bffd48) → [`00c59300`](../00c59/00c59300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59300` · 推定シンボル `None` · 推定型 `None`
- [`00bffd4c`](#insn-00bffd4c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffd50`](#insn-00bffd50) → [`00bffe20`](#insn-00bffe20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffd64`](#insn-00bffd64) → [`00c59310`](../00c59/00c59310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59310` · 推定シンボル `None` · 推定型 `None`
- [`00bffd70`](#insn-00bffd70) → `00c9c8d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bffd70`](#insn-00bffd70) → `01128c58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bffd74`](#insn-00bffd74) → [`00c59320`](../00c59/00c59320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59320` · 推定シンボル `None` · 推定型 `None`
- [`00bffd80`](#insn-00bffd80) → [`00c59330`](../00c59/00c59330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59330` · 推定シンボル `None` · 推定型 `None`
- [`00bffd9c`](#insn-00bffd9c) → [`00bffde8`](#insn-00bffde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffdac`](#insn-00bffdac) → [`00c59310`](../00c59/00c59310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59310` · 推定シンボル `None` · 推定型 `None`
- [`00bffdb8`](#insn-00bffdb8) → `00c9bcd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bffdb8`](#insn-00bffdb8) → `01128ed8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bffdbc`](#insn-00bffdbc) → [`00c59320`](../00c59/00c59320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59320` · 推定シンボル `None` · 推定型 `None`
- [`00bffdd8`](#insn-00bffdd8) → [`00c59330`](../00c59/00c59330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59330` · 推定シンボル `None` · 推定型 `None`
- [`00bffe00`](#insn-00bffe00) → [`00bffe20`](#insn-00bffe20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffe1c`](#insn-00bffe1c) → [`00c59340`](../00c59/00c59340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59340` · 推定シンボル `None` · 推定型 `None`
- [`00bffe24`](#insn-00bffe24) → [`00c59350`](../00c59/00c59350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59350` · 推定シンボル `None` · 推定型 `None`
- [`00bffe2c`](#insn-00bffe2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffe30`](#insn-00bffe30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffe34`](#insn-00bffe34) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffe38`](#insn-00bffe38) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffd24`](#insn-00bffd24)

~~~json
{
  "source": "00bffd24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffd28`](#insn-00bffd28)

~~~json
{
  "source": "00bffd28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffd2c`](#insn-00bffd2c)

~~~json
{
  "source": "00bffd2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffd30`](#insn-00bffd30)

~~~json
{
  "source": "00bffd30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffd48`](#insn-00bffd48)

~~~json
{
  "source": "00bffd48",
  "target": "00c59300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffd4c`](#insn-00bffd4c)

~~~json
{
  "source": "00bffd4c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffd50`](#insn-00bffd50)

~~~json
{
  "source": "00bffd50",
  "target": "00bffe20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffd64`](#insn-00bffd64)

~~~json
{
  "source": "00bffd64",
  "target": "00c59310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffd70`](#insn-00bffd70)

~~~json
{
  "source": "00bffd70",
  "target": "00c9c8d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bffd70`](#insn-00bffd70)

~~~json
{
  "source": "00bffd70",
  "target": "01128c58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128c58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bffd74`](#insn-00bffd74)

~~~json
{
  "source": "00bffd74",
  "target": "00c59320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffd80`](#insn-00bffd80)

~~~json
{
  "source": "00bffd80",
  "target": "00c59330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffd9c`](#insn-00bffd9c)

~~~json
{
  "source": "00bffd9c",
  "target": "00bffde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffdac`](#insn-00bffdac)

~~~json
{
  "source": "00bffdac",
  "target": "00c59310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffdb8`](#insn-00bffdb8)

~~~json
{
  "source": "00bffdb8",
  "target": "00c9bcd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bcd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bffdb8`](#insn-00bffdb8)

~~~json
{
  "source": "00bffdb8",
  "target": "01128ed8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128ed8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bffdbc`](#insn-00bffdbc)

~~~json
{
  "source": "00bffdbc",
  "target": "00c59320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffdd8`](#insn-00bffdd8)

~~~json
{
  "source": "00bffdd8",
  "target": "00c59330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffe00`](#insn-00bffe00)

~~~json
{
  "source": "00bffe00",
  "target": "00bffe20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffe1c`](#insn-00bffe1c)

~~~json
{
  "source": "00bffe1c",
  "target": "00c59340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffe24`](#insn-00bffe24)

~~~json
{
  "source": "00bffe24",
  "target": "00c59350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffe2c`](#insn-00bffe2c)

~~~json
{
  "source": "00bffe2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffe30`](#insn-00bffe30)

~~~json
{
  "source": "00bffe30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffe34`](#insn-00bffe34)

~~~json
{
  "source": "00bffe34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffe38`](#insn-00bffe38)

~~~json
{
  "source": "00bffe38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
