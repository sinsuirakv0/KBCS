# 00bfeeac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b82464`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82464.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-5fe2bcbde73165bcebf0d4ea51b9b668)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bff2d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff2d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-f7596fafbe0484297dbf13d53c28cfa9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfeeac",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPKv",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7624881bee14475374801c38b0042b4163fa9ee7871a558f113f49096502e6ce",
  "source_text_sha256": "7624881bee14475374801c38b0042b4163fa9ee7871a558f113f49096502e6ce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfeeac",
        "00bfefd7"
      ]
    ],
    "bytes_sha256": "4d498eaed30150e24d2b84e69e081979f1861a1c64ebddcb410a8c3f5338c5ac",
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

- [00c57e60](../00c57/00c57e60.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ea0](../00c57/00c57ea0.md)
- [00c57eb0](../00c57/00c57eb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1631 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPKv(long *param_1,undefined8 param_2)

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
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b438
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_48);
    lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar1 = *(uint *)(lVar4 + 0x90);
    uVar5 = *(undefined8 *)(lVar4 + 0x28);
    if (uVar1 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,lVar4);
      plVar3 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_48,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9a830);
      uVar1 = (**(code **)(*plVar3 + 0x38))(plVar3,0x20);
      _ZNSt6__ndk16localeD1Ev(auStack_48);
      uVar1 = uVar1 & 0xff;
      *(uint *)(lVar4 + 0x90) = uVar1;
    }
    lVar4 = (**(code **)(*plVar2 + 0x50))(plVar2,uVar5,lVar4,uVar1,param_2);
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
<a id="insn-00bfeeac"></a> `00bfeeac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfeeb0"></a> `00bfeeb0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfeeb4"></a> `00bfeeb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfeeb8"></a> `00bfeeb8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfeebc"></a> `00bfeebc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfeec0"></a> `00bfeec0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfeec4"></a> `00bfeec4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfeec8"></a> `00bfeec8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfeecc"></a> `00bfeecc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfeed0"></a> `00bfeed0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeed4"></a> `00bfeed4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfeed8"></a> `00bfeed8` | `e2 63 01 94` | bl 0x00c57e60 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeedc"></a> `00bfeedc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfeee0"></a> `00bfeee0` | `88 06 00 34` | cbz w8,0x00bfefb0 | `CONDITIONAL_JUMP`
<a id="insn-00bfeee4"></a> `00bfeee4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfeee8"></a> `00bfeee8` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfeeec"></a> `00bfeeec` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeef0"></a> `00bfeef0` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfeef4"></a> `00bfeef4` | `df 63 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeef8"></a> `00bfeef8` | `e1 04 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfeefc"></a> `00bfeefc` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef00"></a> `00bfef00` | `21 1c 42 f9` | ldr x1,[x1, #0x438] | `FALL_THROUGH`
<a id="insn-00bfef04"></a> `00bfef04` | `df 63 01 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef08"></a> `00bfef08` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bfef0c"></a> `00bfef0c` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef10"></a> `00bfef10` | `e0 63 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef14"></a> `00bfef14` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfef18"></a> `00bfef18` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfef1c"></a> `00bfef1c` | `62 02 08 8b` | add x2,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfef20"></a> `00bfef20` | `43 90 40 b9` | ldr w3,[x2, #0x90] | `FALL_THROUGH`
<a id="insn-00bfef24"></a> `00bfef24` | `56 14 40 f9` | ldr x22,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bfef28"></a> `00bfef28` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bfef2c"></a> `00bfef2c` | `61 02 00 54` | b.ne 0x00bfef78 | `CONDITIONAL_JUMP`
<a id="insn-00bfef30"></a> `00bfef30` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef34"></a> `00bfef34` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bfef38"></a> `00bfef38` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bfef3c"></a> `00bfef3c` | `cd 63 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef40"></a> `00bfef40` | `e1 04 00 90` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bfef44"></a> `00bfef44` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef48"></a> `00bfef48` | `21 18 44 f9` | ldr x1,[x1, #0x830] | `FALL_THROUGH`
<a id="insn-00bfef4c"></a> `00bfef4c` | `cd 63 01 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef50"></a> `00bfef50` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfef54"></a> `00bfef54` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfef58"></a> `00bfef58` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bfef5c"></a> `00bfef5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfef60"></a> `00bfef60` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bfef64"></a> `00bfef64` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef68"></a> `00bfef68` | `ca 63 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef6c"></a> `00bfef6c` | `e3 1e 00 12` | and w3,w23,#0xff | `FALL_THROUGH`
<a id="insn-00bfef70"></a> `00bfef70` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bfef74"></a> `00bfef74` | `03 93 00 b9` | str w3,[x24, #0x90] | `FALL_THROUGH`
<a id="insn-00bfef78"></a> `00bfef78` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bfef7c"></a> `00bfef7c` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfef80"></a> `00bfef80` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfef84"></a> `00bfef84` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bfef88"></a> `00bfef88` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00bfef8c"></a> `00bfef8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfef90"></a> `00bfef90` | `00 01 00 b5` | cbnz x0,0x00bfefb0 | `CONDITIONAL_JUMP`
<a id="insn-00bfef94"></a> `00bfef94` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfef98"></a> `00bfef98` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bfef9c"></a> `00bfef9c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfefa0"></a> `00bfefa0` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfefa4"></a> `00bfefa4` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfefa8"></a> `00bfefa8` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bfefac"></a> `00bfefac` | `bd 63 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfefb0"></a> `00bfefb0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfefb4"></a> `00bfefb4` | `bf 63 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfefb8"></a> `00bfefb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfefbc"></a> `00bfefbc` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfefc0"></a> `00bfefc0` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfefc4"></a> `00bfefc4` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfefc8"></a> `00bfefc8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfefcc"></a> `00bfefcc` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfefd0"></a> `00bfefd0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfefd4"></a> `00bfefd4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfeeac`](#insn-00bfeeac) 範囲 `[['00bfeeac', '00bfeee3']]`
  - `CONDITIONAL_JUMP` [`00bfeee0`](#insn-00bfeee0) → [`00bfefb0`](#insn-00bfefb0)
  - `FALL_THROUGH` [`00bfeee0`](#insn-00bfeee0) → [`00bfeee4`](#insn-00bfeee4)
- ブロック [`00bfeee4`](#insn-00bfeee4) 範囲 `[['00bfeee4', '00bfef2f']]`
  - `CONDITIONAL_JUMP` [`00bfef2c`](#insn-00bfef2c) → [`00bfef78`](#insn-00bfef78)
  - `FALL_THROUGH` [`00bfef2c`](#insn-00bfef2c) → [`00bfef30`](#insn-00bfef30)
- ブロック [`00bfef30`](#insn-00bfef30) 範囲 `[['00bfef30', '00bfef77']]`
  - `FALL_THROUGH` [`00bfef74`](#insn-00bfef74) → [`00bfef78`](#insn-00bfef78)
- ブロック [`00bfef78`](#insn-00bfef78) 範囲 `[['00bfef78', '00bfef93']]`
  - `CONDITIONAL_JUMP` [`00bfef90`](#insn-00bfef90) → [`00bfefb0`](#insn-00bfefb0)
  - `FALL_THROUGH` [`00bfef90`](#insn-00bfef90) → [`00bfef94`](#insn-00bfef94)
- ブロック [`00bfef94`](#insn-00bfef94) 範囲 `[['00bfef94', '00bfefaf']]`
  - `FALL_THROUGH` [`00bfefac`](#insn-00bfefac) → [`00bfefb0`](#insn-00bfefb0)
- ブロック [`00bfefb0`](#insn-00bfefb0) 範囲 `[['00bfefb0', '00bfefd7']]`

## 命令位置別の参照

- [`00bfeeb4`](#insn-00bfeeb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeeb8`](#insn-00bfeeb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeebc`](#insn-00bfeebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeec0`](#insn-00bfeec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeed8`](#insn-00bfeed8) → [`00c57e60`](../00c57/00c57e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e60` · 推定シンボル `None` · 推定型 `None`
- [`00bfeedc`](#insn-00bfeedc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeee0`](#insn-00bfeee0) → [`00bfefb0`](#insn-00bfefb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeef4`](#insn-00bfeef4) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfef00`](#insn-00bfef00) → `00c9b438`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfef00`](#insn-00bfef00) → `01127798`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfef04`](#insn-00bfef04) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bfef10`](#insn-00bfef10) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfef2c`](#insn-00bfef2c) → [`00bfef78`](#insn-00bfef78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfef3c`](#insn-00bfef3c) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfef48`](#insn-00bfef48) → `00c9a830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfef48`](#insn-00bfef48) → `01127a18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bfef4c`](#insn-00bfef4c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bfef68`](#insn-00bfef68) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfef90`](#insn-00bfef90) → [`00bfefb0`](#insn-00bfefb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefac`](#insn-00bfefac) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfefb4`](#insn-00bfefb4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bfefbc`](#insn-00bfefbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefc0`](#insn-00bfefc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefc4`](#insn-00bfefc4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefc8`](#insn-00bfefc8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfeeb4`](#insn-00bfeeb4)

~~~json
{
  "source": "00bfeeb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeeb8`](#insn-00bfeeb8)

~~~json
{
  "source": "00bfeeb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeebc`](#insn-00bfeebc)

~~~json
{
  "source": "00bfeebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeec0`](#insn-00bfeec0)

~~~json
{
  "source": "00bfeec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeed8`](#insn-00bfeed8)

~~~json
{
  "source": "00bfeed8",
  "target": "00c57e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeedc`](#insn-00bfeedc)

~~~json
{
  "source": "00bfeedc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeee0`](#insn-00bfeee0)

~~~json
{
  "source": "00bfeee0",
  "target": "00bfefb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeef4`](#insn-00bfeef4)

~~~json
{
  "source": "00bfeef4",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef00`](#insn-00bfef00)

~~~json
{
  "source": "00bfef00",
  "target": "00c9b438",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b438",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfef00`](#insn-00bfef00)

~~~json
{
  "source": "00bfef00",
  "target": "01127798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127798",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfef04`](#insn-00bfef04)

~~~json
{
  "source": "00bfef04",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef10`](#insn-00bfef10)

~~~json
{
  "source": "00bfef10",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef2c`](#insn-00bfef2c)

~~~json
{
  "source": "00bfef2c",
  "target": "00bfef78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfef3c`](#insn-00bfef3c)

~~~json
{
  "source": "00bfef3c",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef48`](#insn-00bfef48)

~~~json
{
  "source": "00bfef48",
  "target": "00c9a830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfef48`](#insn-00bfef48)

~~~json
{
  "source": "00bfef48",
  "target": "01127a18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfef4c`](#insn-00bfef4c)

~~~json
{
  "source": "00bfef4c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef68`](#insn-00bfef68)

~~~json
{
  "source": "00bfef68",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef90`](#insn-00bfef90)

~~~json
{
  "source": "00bfef90",
  "target": "00bfefb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefac`](#insn-00bfefac)

~~~json
{
  "source": "00bfefac",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfefb4`](#insn-00bfefb4)

~~~json
{
  "source": "00bfefb4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfefbc`](#insn-00bfefbc)

~~~json
{
  "source": "00bfefbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefc0`](#insn-00bfefc0)

~~~json
{
  "source": "00bfefc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefc4`](#insn-00bfefc4)

~~~json
{
  "source": "00bfefc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefc8`](#insn-00bfefc8)

~~~json
{
  "source": "00bfefc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
