# 00c0eabc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c0ea20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0ea20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0087.md#compare-eceaa09ff306fe76365f35b9ec765452)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c0fab0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0f/00c0fab0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-e41211d49bc4ea3222260ea14ed20986)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c0eabc",
  "name": "_ZNSt6__ndk19__num_getIwE17__stage2_int_prepERNS_8ios_baseEPwRw",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b153d2f8b5ecb282f9b0ac4293618f3584dbb0d65815fa0f86572aacf2dc232b",
  "source_text_sha256": "b153d2f8b5ecb282f9b0ac4293618f3584dbb0d65815fa0f86572aacf2dc232b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c0eabc",
        "00c0ec23"
      ]
    ],
    "bytes_sha256": "c577f49a4ca3a92122b2fbd1de062e20b1b79db48080ba1d82008088a75e06fd",
    "instruction_count": 90,
    "instruction_bytes": 360,
    "body_bytes": 360,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5e660](../00c5e/00c5e660.md)

## 呼び出し先

- [00c05ff4](../00c05/00c05ff4.md)
- [00c58340](../00c58/00c58340.md)
- [00c58360](../00c58/00c58360.md)
- [00c5dfb0](../00c5d/00c5dfb0.md)

## 関連文字列（未確認候補）

~~~text
"0123456789abcdefABCDEFxX+-pPiInN"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3115 bytes

~~~c

void _ZNSt6__ndk19__num_getIwE17__stage2_int_prepERNS_8ios_baseEPwRw
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined4 *param_4)

{
  long lVar1;
  undefined *puVar2;
  long lVar3;
  undefined4 uVar4;
  long *plVar5;
  long local_58;
  undefined *local_50;
  undefined8 **local_48;
  undefined **local_28;
  
                    /* catch() { ... } // from try @ 00c0ea34 with catch @ 00c0eac8 */
                    /* catch() { ... } // from try @ 00c0ea64 with catch @ 00c0ead0 */
                    /* catch() { ... } // from try @ 00c0ea78 with catch @ 00c0ead8 */
  _ZNKSt6__ndk18ios_base6getlocEv(&local_58);
  lVar3 = local_58;
  puVar2 = PTR__ZNSt6__ndk15ctypeIwE2idE_00c9bc10;
  local_50 = PTR__ZNSt6__ndk15ctypeIwE2idE_00c9bc10;
  if (*(long *)PTR__ZNSt6__ndk15ctypeIwE2idE_00c9bc10 != -1) {
    local_28 = &local_50;
    local_48 = &local_28;
                    /* try { // try from 00c0eb18 to 00d0eb93 has its CatchHandler @ 00c0eb18
                       catch() { ... } // from try @ 00c0eb18 with catch @ 00c0eb18
                       catch() { ... } // from try @ 00c0ebe0 with catch @ 00c0eb18
                       catch() { ... } // from try @ 00c0ecd0 with catch @ 00c0eb18 */
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk15ctypeIwE2idE_00c9bc10,&local_48,FUN_00c36054);
  }
  lVar1 = *(long *)(lVar3 + 0x10);
  if (((ulong)(*(long *)(lVar3 + 0x18) - lVar1 >> 3) <= (long)*(int *)(puVar2 + 8) - 1U) ||
     (plVar5 = *(long **)(lVar1 + ((long)*(int *)(puVar2 + 8) - 1U) * 8), plVar5 == (long *)0x0)) {
                    /* WARNING: Subroutine does not return */
    FUN_00c05ff4();
  }
  (**(code **)(*plVar5 + 0x60))
            (plVar5,PTR__ZNSt6__ndk114__num_get_base5__srcE_00c9bc90,
             PTR__ZNSt6__ndk114__num_get_base5__srcE_00c9bc90 + 0x1a,param_3);
  puVar2 = PTR__ZNSt6__ndk18numpunctIwE2idE_00c9bc98;
  local_50 = PTR__ZNSt6__ndk18numpunctIwE2idE_00c9bc98;
  if (*(long *)PTR__ZNSt6__ndk18numpunctIwE2idE_00c9bc98 != -1) {
    local_28 = &local_50;
    local_48 = &local_28;
                    /* try { // try from 00c0eb94 to 00d0eb9b has its CatchHandler @ 00c0edf0 */
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk18numpunctIwE2idE_00c9bc98,&local_48,FUN_00c36054);
  }
                    /* try { // try from 00c0ebc8 to 00d0ebcf has its CatchHandler @ 00c0eddc */
  if (((long)*(int *)(puVar2 + 8) - 1U <
       (ulong)(*(long *)(local_58 + 0x18) - *(long *)(local_58 + 0x10) >> 3)) &&
     (plVar5 = *(long **)(*(long *)(local_58 + 0x10) + ((long)*(int *)(puVar2 + 8) - 1U) * 8),
     plVar5 != (long *)0x0)) {
                    /* try { // try from 00c0ebd4 to 00d0ebdf has its CatchHandler @ 00c0edf8 */
    uVar4 = (**(code **)(*plVar5 + 0x20))(plVar5);
                    /* try { // try from 00c0ebe0 to 00d0ec37 has its CatchHandler @ 00c0eb18 */
    *param_4 = uVar4;
    (**(code **)(*plVar5 + 0x28))(param_1,plVar5);
    _ZNSt6__ndk16localeD1Ev(&local_58);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00c05ff4();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c0eabc"></a> `00c0eabc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c0eac0"></a> `00c0eac0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00c0eac4"></a> `00c0eac4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c0eac8"></a> `00c0eac8` | `f7 1b 00 f9` | str x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c0eacc"></a> `00c0eacc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c0ead0"></a> `00c0ead0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c0ead4"></a> `00c0ead4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00c0ead8"></a> `00c0ead8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00c0eadc"></a> `00c0eadc` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00c0eae0"></a> `00c0eae0` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00c0eae4"></a> `00c0eae4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00c0eae8"></a> `00c0eae8` | `16 26 01 94` | bl 0x00c58340 | `UNCONDITIONAL_CALL`
<a id="insn-00c0eaec"></a> `00c0eaec` | `77 04 00 b0` | adrp x23,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c0eaf0"></a> `00c0eaf0` | `f7 0a 46 f9` | ldr x23,[x23, #0xc10] | `FALL_THROUGH`
<a id="insn-00c0eaf4"></a> `00c0eaf4` | `f6 07 40 f9` | ldr x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c0eaf8"></a> `00c0eaf8` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c0eafc"></a> `00c0eafc` | `e8 fe df c8` | ldar x8,[x23] | `FALL_THROUGH`
<a id="insn-00c0eb00"></a> `00c0eb00` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0eb04"></a> `00c0eb04` | `60 01 00 54` | b.eq 0x00c0eb30 | `CONDITIONAL_JUMP`
<a id="insn-00c0eb08"></a> `00c0eb08` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00c0eb0c"></a> `00c0eb0c` | `a9 63 00 91` | add x9,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0eb10"></a> `00c0eb10` | `a8 0f 00 f9` | str x8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00c0eb14"></a> `00c0eb14` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00c0eb18"></a> `00c0eb18` | `60 04 00 b0` | adrp x0,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c0eb1c"></a> `00c0eb1c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c0eb20"></a> `00c0eb20` | `a2 a9 13 10` | adr x2,0xc36054 | `FALL_THROUGH`
<a id="insn-00c0eb24"></a> `00c0eb24` | `00 08 46 f9` | ldr x0,[x0, #0xc10] | `FALL_THROUGH`
<a id="insn-00c0eb28"></a> `00c0eb28` | `a1 23 00 d1` | sub x1,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00c0eb2c"></a> `00c0eb2c` | `21 3d 01 94` | bl 0x00c5dfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00c0eb30"></a> `00c0eb30` | `c8 2a 41 a9` | ldp x8,x10,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00c0eb34"></a> `00c0eb34` | `e9 0a 80 b9` | ldrsw x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00c0eb38"></a> `00c0eb38` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c0eb3c"></a> `00c0eb3c` | `4a 01 08 cb` | sub x10,x10,x8 | `FALL_THROUGH`
<a id="insn-00c0eb40"></a> `00c0eb40` | `3f 0d 8a eb` | cmp x9,x10, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00c0eb44"></a> `00c0eb44` | `c2 06 00 54` | b.cs 0x00c0ec1c | `CONDITIONAL_JUMP`
<a id="insn-00c0eb48"></a> `00c0eb48` | `00 79 69 f8` | ldr x0,[x8, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c0eb4c"></a> `00c0eb4c` | `80 06 00 b4` | cbz x0,0x00c0ec1c | `CONDITIONAL_JUMP`
<a id="insn-00c0eb50"></a> `00c0eb50` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00c0eb54"></a> `00c0eb54` | `08 31 40 f9` | ldr x8,[x8, #0x60] | `FALL_THROUGH`
<a id="insn-00c0eb58"></a> `00c0eb58` | `61 04 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c0eb5c"></a> `00c0eb5c` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00c0eb60"></a> `00c0eb60` | `21 48 46 f9` | ldr x1,[x1, #0xc90] | `FALL_THROUGH`
<a id="insn-00c0eb64"></a> `00c0eb64` | `22 68 00 91` | add x2,x1,#0x1a | `FALL_THROUGH`
<a id="insn-00c0eb68"></a> `00c0eb68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c0eb6c"></a> `00c0eb6c` | `76 04 00 b0` | adrp x22,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c0eb70"></a> `00c0eb70` | `d6 4e 46 f9` | ldr x22,[x22, #0xc98] | `FALL_THROUGH`
<a id="insn-00c0eb74"></a> `00c0eb74` | `f5 07 40 f9` | ldr x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c0eb78"></a> `00c0eb78` | `f6 0b 00 f9` | str x22,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c0eb7c"></a> `00c0eb7c` | `c8 fe df c8` | ldar x8,[x22] | `FALL_THROUGH`
<a id="insn-00c0eb80"></a> `00c0eb80` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0eb84"></a> `00c0eb84` | `60 01 00 54` | b.eq 0x00c0ebb0 | `CONDITIONAL_JUMP`
<a id="insn-00c0eb88"></a> `00c0eb88` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00c0eb8c"></a> `00c0eb8c` | `a9 63 00 91` | add x9,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0eb90"></a> `00c0eb90` | `a8 0f 00 f9` | str x8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00c0eb94"></a> `00c0eb94` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00c0eb98"></a> `00c0eb98` | `60 04 00 b0` | adrp x0,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c0eb9c"></a> `00c0eb9c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c0eba0"></a> `00c0eba0` | `a2 a5 13 10` | adr x2,0xc36054 | `FALL_THROUGH`
<a id="insn-00c0eba4"></a> `00c0eba4` | `00 4c 46 f9` | ldr x0,[x0, #0xc98] | `FALL_THROUGH`
<a id="insn-00c0eba8"></a> `00c0eba8` | `a1 23 00 d1` | sub x1,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00c0ebac"></a> `00c0ebac` | `01 3d 01 94` | bl 0x00c5dfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00c0ebb0"></a> `00c0ebb0` | `a8 2a 41 a9` | ldp x8,x10,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00c0ebb4"></a> `00c0ebb4` | `c9 0a 80 b9` | ldrsw x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c0ebb8"></a> `00c0ebb8` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c0ebbc"></a> `00c0ebbc` | `4a 01 08 cb` | sub x10,x10,x8 | `FALL_THROUGH`
<a id="insn-00c0ebc0"></a> `00c0ebc0` | `3f 0d 8a eb` | cmp x9,x10, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00c0ebc4"></a> `00c0ebc4` | `e2 02 00 54` | b.cs 0x00c0ec20 | `CONDITIONAL_JUMP`
<a id="insn-00c0ebc8"></a> `00c0ebc8` | `15 79 69 f8` | ldr x21,[x8, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c0ebcc"></a> `00c0ebcc` | `b5 02 00 b4` | cbz x21,0x00c0ec20 | `CONDITIONAL_JUMP`
<a id="insn-00c0ebd0"></a> `00c0ebd0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0ebd4"></a> `00c0ebd4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c0ebd8"></a> `00c0ebd8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c0ebdc"></a> `00c0ebdc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c0ebe0"></a> `00c0ebe0` | `80 02 00 b9` | str w0,[x20] | `FALL_THROUGH`
<a id="insn-00c0ebe4"></a> `00c0ebe4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0ebe8"></a> `00c0ebe8` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c0ebec"></a> `00c0ebec` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00c0ebf0"></a> `00c0ebf0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c0ebf4"></a> `00c0ebf4` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00c0ebf8"></a> `00c0ebf8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00c0ebfc"></a> `00c0ebfc` | `d9 25 01 94` | bl 0x00c58360 | `UNCONDITIONAL_CALL`
<a id="insn-00c0ec00"></a> `00c0ec00` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c0ec04"></a> `00c0ec04` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c0ec08"></a> `00c0ec08` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c0ec0c"></a> `00c0ec0c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c0ec10"></a> `00c0ec10` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00c0ec14"></a> `00c0ec14` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c0ec18"></a> `00c0ec18` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c0ec1c"></a> `00c0ec1c` | `f6 dc ff 97` | bl 0x00c05ff4 | `CALL_TERMINATOR`
<a id="insn-00c0ec20"></a> `00c0ec20` | `f5 dc ff 97` | bl 0x00c05ff4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c0eabc`](#insn-00c0eabc) 範囲 `[['00c0eabc', '00c0eac7']]`
  - `FALL_THROUGH` [`00c0eac4`](#insn-00c0eac4) → [`00c0eac8`](#insn-00c0eac8)
- ブロック [`00c0eac8`](#insn-00c0eac8) 範囲 `[['00c0eac8', '00c0eacf']]`
  - `FALL_THROUGH` [`00c0eacc`](#insn-00c0eacc) → [`00c0ead0`](#insn-00c0ead0)
- ブロック [`00c0ead0`](#insn-00c0ead0) 範囲 `[['00c0ead0', '00c0ead7']]`
  - `FALL_THROUGH` [`00c0ead4`](#insn-00c0ead4) → [`00c0ead8`](#insn-00c0ead8)
- ブロック [`00c0ead8`](#insn-00c0ead8) 範囲 `[['00c0ead8', '00c0eb07']]`
  - `CONDITIONAL_JUMP` [`00c0eb04`](#insn-00c0eb04) → [`00c0eb30`](#insn-00c0eb30)
  - `FALL_THROUGH` [`00c0eb04`](#insn-00c0eb04) → [`00c0eb08`](#insn-00c0eb08)
- ブロック [`00c0eb08`](#insn-00c0eb08) 範囲 `[['00c0eb08', '00c0eb17']]`
  - `FALL_THROUGH` [`00c0eb14`](#insn-00c0eb14) → [`00c0eb18`](#insn-00c0eb18)
- ブロック [`00c0eb18`](#insn-00c0eb18) 範囲 `[['00c0eb18', '00c0eb2f']]`
  - `FALL_THROUGH` [`00c0eb2c`](#insn-00c0eb2c) → [`00c0eb30`](#insn-00c0eb30)
- ブロック [`00c0eb30`](#insn-00c0eb30) 範囲 `[['00c0eb30', '00c0eb47']]`
  - `CONDITIONAL_JUMP` [`00c0eb44`](#insn-00c0eb44) → [`00c0ec1c`](#insn-00c0ec1c)
  - `FALL_THROUGH` [`00c0eb44`](#insn-00c0eb44) → [`00c0eb48`](#insn-00c0eb48)
- ブロック [`00c0eb48`](#insn-00c0eb48) 範囲 `[['00c0eb48', '00c0eb4f']]`
  - `CONDITIONAL_JUMP` [`00c0eb4c`](#insn-00c0eb4c) → [`00c0ec1c`](#insn-00c0ec1c)
  - `FALL_THROUGH` [`00c0eb4c`](#insn-00c0eb4c) → [`00c0eb50`](#insn-00c0eb50)
- ブロック [`00c0eb50`](#insn-00c0eb50) 範囲 `[['00c0eb50', '00c0eb87']]`
  - `CONDITIONAL_JUMP` [`00c0eb84`](#insn-00c0eb84) → [`00c0ebb0`](#insn-00c0ebb0)
  - `FALL_THROUGH` [`00c0eb84`](#insn-00c0eb84) → [`00c0eb88`](#insn-00c0eb88)
- ブロック [`00c0eb88`](#insn-00c0eb88) 範囲 `[['00c0eb88', '00c0eb93']]`
  - `FALL_THROUGH` [`00c0eb90`](#insn-00c0eb90) → [`00c0eb94`](#insn-00c0eb94)
- ブロック [`00c0eb94`](#insn-00c0eb94) 範囲 `[['00c0eb94', '00c0ebaf']]`
  - `FALL_THROUGH` [`00c0ebac`](#insn-00c0ebac) → [`00c0ebb0`](#insn-00c0ebb0)
- ブロック [`00c0ebb0`](#insn-00c0ebb0) 範囲 `[['00c0ebb0', '00c0ebc7']]`
  - `CONDITIONAL_JUMP` [`00c0ebc4`](#insn-00c0ebc4) → [`00c0ec20`](#insn-00c0ec20)
  - `FALL_THROUGH` [`00c0ebc4`](#insn-00c0ebc4) → [`00c0ebc8`](#insn-00c0ebc8)
- ブロック [`00c0ebc8`](#insn-00c0ebc8) 範囲 `[['00c0ebc8', '00c0ebcf']]`
  - `CONDITIONAL_JUMP` [`00c0ebcc`](#insn-00c0ebcc) → [`00c0ec20`](#insn-00c0ec20)
  - `FALL_THROUGH` [`00c0ebcc`](#insn-00c0ebcc) → [`00c0ebd0`](#insn-00c0ebd0)
- ブロック [`00c0ebd0`](#insn-00c0ebd0) 範囲 `[['00c0ebd0', '00c0ebd3']]`
  - `FALL_THROUGH` [`00c0ebd0`](#insn-00c0ebd0) → [`00c0ebd4`](#insn-00c0ebd4)
- ブロック [`00c0ebd4`](#insn-00c0ebd4) 範囲 `[['00c0ebd4', '00c0ebdf']]`
  - `FALL_THROUGH` [`00c0ebdc`](#insn-00c0ebdc) → [`00c0ebe0`](#insn-00c0ebe0)
- ブロック [`00c0ebe0`](#insn-00c0ebe0) 範囲 `[['00c0ebe0', '00c0ec1b']]`
- ブロック [`00c0ec1c`](#insn-00c0ec1c) 範囲 `[['00c0ec1c', '00c0ec1f']]`
- ブロック [`00c0ec20`](#insn-00c0ec20) 範囲 `[['00c0ec20', '00c0ec23']]`

## 命令位置別の参照

- [`00c0eac4`](#insn-00c0eac4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eac8`](#insn-00c0eac8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eacc`](#insn-00c0eacc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ead0`](#insn-00c0ead0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eae8`](#insn-00c0eae8) → [`00c58340`](../00c58/00c58340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58340` · 推定シンボル `None` · 推定型 `None`
- [`00c0eaf0`](#insn-00c0eaf0) → `00c9bc10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c0eaf4`](#insn-00c0eaf4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eaf8`](#insn-00c0eaf8) → `01127f08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIwE2idE` · 推定型 `undefined8`
- [`00c0eaf8`](#insn-00c0eaf8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eafc`](#insn-00c0eafc) → `01127f08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIwE2idE` · 推定型 `undefined8`
- [`00c0eb04`](#insn-00c0eb04) → [`00c0eb30`](#insn-00c0eb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb10`](#insn-00c0eb10) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb14`](#insn-00c0eb14) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb20`](#insn-00c0eb20) → [`00c36054`](../00c36/00c36054.md) · `PARAM` · `ANALYSIS` · 関数 `00c36054` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb24`](#insn-00c0eb24) → `00c9bc10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c0eb24`](#insn-00c0eb24) → `01127f08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIwE2idE` · 推定型 `undefined8`
- [`00c0eb2c`](#insn-00c0eb2c) → [`00c5dfb0`](../00c5d/00c5dfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dfb0` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb34`](#insn-00c0eb34) → `01127f10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c0eb44`](#insn-00c0eb44) → [`00c0ec1c`](#insn-00c0ec1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb4c`](#insn-00c0eb4c) → [`00c0ec1c`](#insn-00c0ec1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb60`](#insn-00c0eb60) → `00c9bc90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c0eb60`](#insn-00c0eb60) → `00310ede`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk114__num_get_base5__srcE` · 推定型 `string`
- [`00c0eb64`](#insn-00c0eb64) → `00310ef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00c0eb70`](#insn-00c0eb70) → `00c9bc98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c0eb74`](#insn-00c0eb74) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb78`](#insn-00c0eb78) → `01127f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk18numpunctIwE2idE` · 推定型 `undefined8`
- [`00c0eb78`](#insn-00c0eb78) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb7c`](#insn-00c0eb7c) → `01127f98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk18numpunctIwE2idE` · 推定型 `undefined8`
- [`00c0eb84`](#insn-00c0eb84) → [`00c0ebb0`](#insn-00c0ebb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb90`](#insn-00c0eb90) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eb94`](#insn-00c0eb94) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0eba0`](#insn-00c0eba0) → [`00c36054`](../00c36/00c36054.md) · `PARAM` · `ANALYSIS` · 関数 `00c36054` · 推定シンボル `None` · 推定型 `None`
- [`00c0eba4`](#insn-00c0eba4) → `00c9bc98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c0eba4`](#insn-00c0eba4) → `01127f98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk18numpunctIwE2idE` · 推定型 `undefined8`
- [`00c0ebac`](#insn-00c0ebac) → [`00c5dfb0`](../00c5d/00c5dfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dfb0` · 推定シンボル `None` · 推定型 `None`
- [`00c0ebb4`](#insn-00c0ebb4) → `01127fa0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c0ebc4`](#insn-00c0ebc4) → [`00c0ec20`](#insn-00c0ec20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ebcc`](#insn-00c0ebcc) → [`00c0ec20`](#insn-00c0ec20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ebfc`](#insn-00c0ebfc) → [`00c58360`](../00c58/00c58360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58360` · 推定シンボル `None` · 推定型 `None`
- [`00c0ec00`](#insn-00c0ec00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ec04`](#insn-00c0ec04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ec08`](#insn-00c0ec08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ec0c`](#insn-00c0ec0c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ec1c`](#insn-00c0ec1c) → [`00c05ff4`](../00c05/00c05ff4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c05ff4` · 推定シンボル `None` · 推定型 `None`
- [`00c0ec20`](#insn-00c0ec20) → [`00c05ff4`](../00c05/00c05ff4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c05ff4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c0eac4`](#insn-00c0eac4)

~~~json
{
  "source": "00c0eac4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eac8`](#insn-00c0eac8)

~~~json
{
  "source": "00c0eac8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eacc`](#insn-00c0eacc)

~~~json
{
  "source": "00c0eacc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ead0`](#insn-00c0ead0)

~~~json
{
  "source": "00c0ead0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eae8`](#insn-00c0eae8)

~~~json
{
  "source": "00c0eae8",
  "target": "00c58340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0eaf0`](#insn-00c0eaf0)

~~~json
{
  "source": "00c0eaf0",
  "target": "00c9bc10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c0eaf4`](#insn-00c0eaf4)

~~~json
{
  "source": "00c0eaf4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eaf8`](#insn-00c0eaf8)

~~~json
{
  "source": "00c0eaf8",
  "target": "01127f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0eaf8`](#insn-00c0eaf8)

~~~json
{
  "source": "00c0eaf8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eafc`](#insn-00c0eafc)

~~~json
{
  "source": "00c0eafc",
  "target": "01127f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0eb04`](#insn-00c0eb04)

~~~json
{
  "source": "00c0eb04",
  "target": "00c0eb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eb10`](#insn-00c0eb10)

~~~json
{
  "source": "00c0eb10",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eb14`](#insn-00c0eb14)

~~~json
{
  "source": "00c0eb14",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eb20`](#insn-00c0eb20)

~~~json
{
  "source": "00c0eb20",
  "target": "00c36054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0eb24`](#insn-00c0eb24)

~~~json
{
  "source": "00c0eb24",
  "target": "00c9bc10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c0eb24`](#insn-00c0eb24)

~~~json
{
  "source": "00c0eb24",
  "target": "01127f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0eb2c`](#insn-00c0eb2c)

~~~json
{
  "source": "00c0eb2c",
  "target": "00c5dfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0eb34`](#insn-00c0eb34)

~~~json
{
  "source": "00c0eb34",
  "target": "01127f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127f10",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0eb44`](#insn-00c0eb44)

~~~json
{
  "source": "00c0eb44",
  "target": "00c0ec1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eb4c`](#insn-00c0eb4c)

~~~json
{
  "source": "00c0eb4c",
  "target": "00c0ec1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eb60`](#insn-00c0eb60)

~~~json
{
  "source": "00c0eb60",
  "target": "00c9bc90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c0eb60`](#insn-00c0eb60)

~~~json
{
  "source": "00c0eb60",
  "target": "00310ede",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00310ede",
  "offset": 0,
  "size": 33,
  "datatype": "string",
  "bytes": "3031323334353637383961626364656641424344454678582b2d705069496e4e",
  "capture_start": "00310ede",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00c0eb64`](#insn-00c0eb64)

~~~json
{
  "source": "00c0eb64",
  "target": "00310ef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00310ede",
  "offset": 26,
  "size": 33,
  "datatype": "string",
  "bytes": "3031323334353637383961626364656641424344454678582b2d705069496e4e",
  "capture_start": "00310ede",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00c0eb70`](#insn-00c0eb70)

~~~json
{
  "source": "00c0eb70",
  "target": "00c9bc98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c0eb74`](#insn-00c0eb74)

~~~json
{
  "source": "00c0eb74",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eb78`](#insn-00c0eb78)

~~~json
{
  "source": "00c0eb78",
  "target": "01127f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127f98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0eb78`](#insn-00c0eb78)

~~~json
{
  "source": "00c0eb78",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eb7c`](#insn-00c0eb7c)

~~~json
{
  "source": "00c0eb7c",
  "target": "01127f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127f98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0eb84`](#insn-00c0eb84)

~~~json
{
  "source": "00c0eb84",
  "target": "00c0ebb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eb90`](#insn-00c0eb90)

~~~json
{
  "source": "00c0eb90",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eb94`](#insn-00c0eb94)

~~~json
{
  "source": "00c0eb94",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0eba0`](#insn-00c0eba0)

~~~json
{
  "source": "00c0eba0",
  "target": "00c36054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0eba4`](#insn-00c0eba4)

~~~json
{
  "source": "00c0eba4",
  "target": "00c9bc98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c0eba4`](#insn-00c0eba4)

~~~json
{
  "source": "00c0eba4",
  "target": "01127f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127f98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0ebac`](#insn-00c0ebac)

~~~json
{
  "source": "00c0ebac",
  "target": "00c5dfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0ebb4`](#insn-00c0ebb4)

~~~json
{
  "source": "00c0ebb4",
  "target": "01127fa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127fa0",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0ebc4`](#insn-00c0ebc4)

~~~json
{
  "source": "00c0ebc4",
  "target": "00c0ec20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ebcc`](#insn-00c0ebcc)

~~~json
{
  "source": "00c0ebcc",
  "target": "00c0ec20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ebfc`](#insn-00c0ebfc)

~~~json
{
  "source": "00c0ebfc",
  "target": "00c58360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0ec00`](#insn-00c0ec00)

~~~json
{
  "source": "00c0ec00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ec04`](#insn-00c0ec04)

~~~json
{
  "source": "00c0ec04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ec08`](#insn-00c0ec08)

~~~json
{
  "source": "00c0ec08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ec0c`](#insn-00c0ec0c)

~~~json
{
  "source": "00c0ec0c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ec1c`](#insn-00c0ec1c)

~~~json
{
  "source": "00c0ec1c",
  "target": "00c05ff4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0ec20`](#insn-00c0ec20)

~~~json
{
  "source": "00c0ec20",
  "target": "00c05ff4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
