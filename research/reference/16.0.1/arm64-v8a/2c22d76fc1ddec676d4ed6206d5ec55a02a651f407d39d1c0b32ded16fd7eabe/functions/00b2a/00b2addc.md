# 00b2addc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2a9b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a9b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-261f3a078a291aa438aaeaf58ddce345)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b2ae78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ae78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0037.md#compare-c0754a2be9b35a614cd559b2af860bd0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2addc",
  "name": "FUN_00b2addc",
  "size": 328,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "504eb618cec28585a19c58aeacc12d214216529572e51bb7ec42d28249f2521d",
  "source_text_sha256": "504eb618cec28585a19c58aeacc12d214216529572e51bb7ec42d28249f2521d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2addc",
        "00b2af1f"
      ],
      [
        "00b2af44",
        "00b2af47"
      ]
    ],
    "bytes_sha256": "76831844eefaca88ff15accb619a778e539baccddc1c9a0341c766695b479936",
    "instruction_count": 82,
    "instruction_bytes": 328,
    "body_bytes": 328,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b1f428](../00b1f/00b1f428.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [005e8198](../005e8/005e8198.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1743 bytes

~~~c

long * FUN_00b2addc(long *param_1,int *param_2,undefined8 param_3,undefined8 *param_4)

{
  undefined4 uVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  undefined8 uVar5;
  long lVar6;
  long *plVar7;
  long *plVar8;
  
  lVar2 = tpidr_el0;
  lVar6 = *(long *)(lVar2 + 0x28);
  plVar7 = param_1 + 1;
  plVar8 = plVar7;
  if ((long *)*plVar7 != (long *)0x0) {
    plVar3 = (long *)*plVar7;
    do {
      while (plVar4 = plVar3, plVar7 = plVar4, (int)plVar4[4] <= *param_2) {
        if (*param_2 <= (int)plVar4[4]) {
          uVar5 = 0;
          goto LAB_00b2aef0;
        }
        plVar3 = (long *)plVar4[1];
        if ((long *)plVar4[1] == (long *)0x0) {
          plVar8 = plVar4 + 1;
          goto LAB_00b2ae58;
        }
      }
      plVar3 = (long *)*plVar4;
      plVar8 = plVar4;
    } while ((long *)*plVar4 != (long *)0x0);
  }
LAB_00b2ae58:
  plVar4 = (long *)_Znwm(0x60);
  uVar1 = *(undefined4 *)*param_4;
  plVar4[0xb] = 0;
  *(undefined4 *)(plVar4 + 4) = uVar1;
  plVar4[10] = 0;
  plVar4[9] = 0;
  plVar4[8] = 0;
  plVar4[7] = 0;
  plVar4[6] = 0;
  plVar4[5] = 0;
  FUN_005e8198((long)plVar4 + 0x2c);
  *(undefined4 *)((long)plVar4 + 0x34) = 0;
  FUN_005e8198();
  plVar4[8] = 0;
  plVar4[9] = 0;
  plVar4[10] = 0;
  *plVar4 = 0;
  plVar4[1] = 0;
  plVar4[2] = (long)plVar7;
  *plVar8 = (long)plVar4;
  plVar7 = plVar4;
  if (*(long *)*param_1 != 0) {
    *param_1 = *(long *)*param_1;
    plVar7 = (long *)*plVar8;
  }
  plVar7 = (long *)FUN_0043bba4(param_1[1],plVar7);
  uVar5 = 1;
  param_1[2] = param_1[2] + 1;
  param_1 = plVar7;
LAB_00b2aef0:
  if (*(long *)(lVar2 + 0x28) == lVar6) {
    return plVar4;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(param_1,uVar5);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b2addc"></a> `00b2addc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b2ade0"></a> `00b2ade0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2ade4"></a> `00b2ade4` | `f9 1b 00 f9` | str x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2ade8"></a> `00b2ade8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2adec"></a> `00b2adec` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b2adf0"></a> `00b2adf0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b2adf4"></a> `00b2adf4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b2adf8"></a> `00b2adf8` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b2adfc"></a> `00b2adfc` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00b2ae00"></a> `00b2ae00` | `f6 03 03 aa` | mov x22,x3 | `FALL_THROUGH`
<a id="insn-00b2ae04"></a> `00b2ae04` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b2ae08"></a> `00b2ae08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b2ae0c"></a> `00b2ae0c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2ae10"></a> `00b2ae10` | `29 8f 40 f8` | ldr x9,[x25, #0x8]! | `FALL_THROUGH`
<a id="insn-00b2ae14"></a> `00b2ae14` | `f8 03 19 aa` | mov x24,x25 | `FALL_THROUGH`
<a id="insn-00b2ae18"></a> `00b2ae18` | `f4 03 19 aa` | mov x20,x25 | `FALL_THROUGH`
<a id="insn-00b2ae1c"></a> `00b2ae1c` | `e9 01 00 b4` | cbz x9,0x00b2ae58 | `CONDITIONAL_JUMP`
<a id="insn-00b2ae20"></a> `00b2ae20` | `28 00 40 b9` | ldr w8,[x1] | `FALL_THROUGH`
<a id="insn-00b2ae24"></a> `00b2ae24` | `04 00 00 14` | b 0x00b2ae34 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ae28"></a> `00b2ae28` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00b2ae2c"></a> `00b2ae2c` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00b2ae30"></a> `00b2ae30` | `49 01 00 b4` | cbz x9,0x00b2ae58 | `CONDITIONAL_JUMP`
<a id="insn-00b2ae34"></a> `00b2ae34` | `f4 03 09 aa` | mov x20,x9 | `FALL_THROUGH`
<a id="insn-00b2ae38"></a> `00b2ae38` | `29 21 40 b9` | ldr w9,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00b2ae3c"></a> `00b2ae3c` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00b2ae40"></a> `00b2ae40` | `4b ff ff 54` | b.lt 0x00b2ae28 | `CONDITIONAL_JUMP`
<a id="insn-00b2ae44"></a> `00b2ae44` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00b2ae48"></a> `00b2ae48` | `2a 05 00 54` | b.ge 0x00b2aeec | `CONDITIONAL_JUMP`
<a id="insn-00b2ae4c"></a> `00b2ae4c` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b2ae50"></a> `00b2ae50` | `29 ff ff b5` | cbnz x9,0x00b2ae34 | `CONDITIONAL_JUMP`
<a id="insn-00b2ae54"></a> `00b2ae54` | `98 22 00 91` | add x24,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00b2ae58"></a> `00b2ae58` | `00 0c 80 52` | mov w0,#0x60 | `FALL_THROUGH`
<a id="insn-00b2ae5c"></a> `00b2ae5c` | `0d b4 04 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ae60"></a> `00b2ae60` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00b2ae64"></a> `00b2ae64` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00b2ae68"></a> `00b2ae68` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b2ae6c"></a> `00b2ae6c` | `ff 43 00 39` | strb wzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ae70"></a> `00b2ae70` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-00b2ae74"></a> `00b2ae74` | `e0 67 00 a9` | stp x0,x25,[sp] | `FALL_THROUGH`
<a id="insn-00b2ae78"></a> `00b2ae78` | `1f 2c 00 f9` | str xzr,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00b2ae7c"></a> `00b2ae7c` | `08 20 00 b9` | str w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b2ae80"></a> `00b2ae80` | `00 80 84 3c` | stur q0,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00b2ae84"></a> `00b2ae84` | `00 80 83 3c` | stur q0,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00b2ae88"></a> `00b2ae88` | `00 80 82 3c` | stur q0,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00b2ae8c"></a> `00b2ae8c` | `00 b0 00 91` | add x0,x0,#0x2c | `FALL_THROUGH`
<a id="insn-00b2ae90"></a> `00b2ae90` | `c2 f4 ea 97` | bl 0x005e8198 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ae94"></a> `00b2ae94` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b2ae98"></a> `00b2ae98` | `1f 4c 03 b8` | str wzr,[x0, #0x34]! | `FALL_THROUGH`
<a id="insn-00b2ae9c"></a> `00b2ae9c` | `bf f4 ea 97` | bl 0x005e8198 | `UNCONDITIONAL_CALL`
<a id="insn-00b2aea0"></a> `00b2aea0` | `bf 7e 04 a9` | stp xzr,xzr,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00b2aea4"></a> `00b2aea4` | `bf 2a 00 f9` | str xzr,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-00b2aea8"></a> `00b2aea8` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-00b2aeac"></a> `00b2aeac` | `b4 0a 00 f9` | str x20,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00b2aeb0"></a> `00b2aeb0` | `15 03 00 f9` | str x21,[x24] | `FALL_THROUGH`
<a id="insn-00b2aeb4"></a> `00b2aeb4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b2aeb8"></a> `00b2aeb8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00b2aebc"></a> `00b2aebc` | `68 00 00 b4` | cbz x8,0x00b2aec8 | `CONDITIONAL_JUMP`
<a id="insn-00b2aec0"></a> `00b2aec0` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00b2aec4"></a> `00b2aec4` | `15 03 40 f9` | ldr x21,[x24] | `FALL_THROUGH`
<a id="insn-00b2aec8"></a> `00b2aec8` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2aecc"></a> `00b2aecc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b2aed0"></a> `00b2aed0` | `35 43 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00b2aed4"></a> `00b2aed4` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b2aed8"></a> `00b2aed8` | `f4 03 40 f9` | ldr x20,[sp] | `FALL_THROUGH`
<a id="insn-00b2aedc"></a> `00b2aedc` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00b2aee0"></a> `00b2aee0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b2aee4"></a> `00b2aee4` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b2aee8"></a> `00b2aee8` | `02 00 00 14` | b 0x00b2aef0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2aeec"></a> `00b2aeec` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b2aef0"></a> `00b2aef0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b2aef4"></a> `00b2aef4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2aef8"></a> `00b2aef8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b2aefc"></a> `00b2aefc` | `41 02 00 54` | b.ne 0x00b2af44 | `CONDITIONAL_JUMP`
<a id="insn-00b2af00"></a> `00b2af00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b2af04"></a> `00b2af04` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b2af08"></a> `00b2af08` | `f9 1b 40 f9` | ldr x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2af0c"></a> `00b2af0c` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b2af10"></a> `00b2af10` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2af14"></a> `00b2af14` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2af18"></a> `00b2af18` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b2af1c"></a> `00b2af1c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b2af44"></a> `00b2af44` | `e7 b3 04 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b2addc`](#insn-00b2addc) 範囲 `[['00b2addc', '00b2ae1f']]`
  - `CONDITIONAL_JUMP` [`00b2ae1c`](#insn-00b2ae1c) → [`00b2ae58`](#insn-00b2ae58)
  - `FALL_THROUGH` [`00b2ae1c`](#insn-00b2ae1c) → [`00b2ae20`](#insn-00b2ae20)
- ブロック [`00b2ae20`](#insn-00b2ae20) 範囲 `[['00b2ae20', '00b2ae27']]`
  - `UNCONDITIONAL_JUMP` [`00b2ae24`](#insn-00b2ae24) → [`00b2ae34`](#insn-00b2ae34)
- ブロック [`00b2ae28`](#insn-00b2ae28) 範囲 `[['00b2ae28', '00b2ae33']]`
  - `CONDITIONAL_JUMP` [`00b2ae30`](#insn-00b2ae30) → [`00b2ae58`](#insn-00b2ae58)
  - `FALL_THROUGH` [`00b2ae30`](#insn-00b2ae30) → [`00b2ae34`](#insn-00b2ae34)
- ブロック [`00b2ae34`](#insn-00b2ae34) 範囲 `[['00b2ae34', '00b2ae43']]`
  - `CONDITIONAL_JUMP` [`00b2ae40`](#insn-00b2ae40) → [`00b2ae28`](#insn-00b2ae28)
  - `FALL_THROUGH` [`00b2ae40`](#insn-00b2ae40) → [`00b2ae44`](#insn-00b2ae44)
- ブロック [`00b2ae44`](#insn-00b2ae44) 範囲 `[['00b2ae44', '00b2ae4b']]`
  - `CONDITIONAL_JUMP` [`00b2ae48`](#insn-00b2ae48) → [`00b2aeec`](#insn-00b2aeec)
  - `FALL_THROUGH` [`00b2ae48`](#insn-00b2ae48) → [`00b2ae4c`](#insn-00b2ae4c)
- ブロック [`00b2ae4c`](#insn-00b2ae4c) 範囲 `[['00b2ae4c', '00b2ae53']]`
  - `CONDITIONAL_JUMP` [`00b2ae50`](#insn-00b2ae50) → [`00b2ae34`](#insn-00b2ae34)
  - `FALL_THROUGH` [`00b2ae50`](#insn-00b2ae50) → [`00b2ae54`](#insn-00b2ae54)
- ブロック [`00b2ae54`](#insn-00b2ae54) 範囲 `[['00b2ae54', '00b2ae57']]`
  - `FALL_THROUGH` [`00b2ae54`](#insn-00b2ae54) → [`00b2ae58`](#insn-00b2ae58)
- ブロック [`00b2ae58`](#insn-00b2ae58) 範囲 `[['00b2ae58', '00b2aebf']]`
  - `CONDITIONAL_JUMP` [`00b2aebc`](#insn-00b2aebc) → [`00b2aec8`](#insn-00b2aec8)
  - `FALL_THROUGH` [`00b2aebc`](#insn-00b2aebc) → [`00b2aec0`](#insn-00b2aec0)
- ブロック [`00b2aec0`](#insn-00b2aec0) 範囲 `[['00b2aec0', '00b2aec7']]`
  - `FALL_THROUGH` [`00b2aec4`](#insn-00b2aec4) → [`00b2aec8`](#insn-00b2aec8)
- ブロック [`00b2aec8`](#insn-00b2aec8) 範囲 `[['00b2aec8', '00b2aeeb']]`
  - `UNCONDITIONAL_JUMP` [`00b2aee8`](#insn-00b2aee8) → [`00b2aef0`](#insn-00b2aef0)
- ブロック [`00b2aeec`](#insn-00b2aeec) 範囲 `[['00b2aeec', '00b2aeef']]`
  - `FALL_THROUGH` [`00b2aeec`](#insn-00b2aeec) → [`00b2aef0`](#insn-00b2aef0)
- ブロック [`00b2aef0`](#insn-00b2aef0) 範囲 `[['00b2aef0', '00b2aeff']]`
  - `CONDITIONAL_JUMP` [`00b2aefc`](#insn-00b2aefc) → [`00b2af44`](#insn-00b2af44)
  - `FALL_THROUGH` [`00b2aefc`](#insn-00b2aefc) → [`00b2af00`](#insn-00b2af00)
- ブロック [`00b2af00`](#insn-00b2af00) 範囲 `[['00b2af00', '00b2af1f']]`
- ブロック [`00b2af44`](#insn-00b2af44) 範囲 `[['00b2af44', '00b2af47']]`

## 命令位置別の参照

- [`00b2ade0`](#insn-00b2ade0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ade4`](#insn-00b2ade4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ade8`](#insn-00b2ade8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2adec`](#insn-00b2adec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2adf0`](#insn-00b2adf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae0c`](#insn-00b2ae0c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae1c`](#insn-00b2ae1c) → [`00b2ae58`](#insn-00b2ae58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae24`](#insn-00b2ae24) → [`00b2ae34`](#insn-00b2ae34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae30`](#insn-00b2ae30) → [`00b2ae58`](#insn-00b2ae58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae40`](#insn-00b2ae40) → [`00b2ae28`](#insn-00b2ae28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae48`](#insn-00b2ae48) → [`00b2aeec`](#insn-00b2aeec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae50`](#insn-00b2ae50) → [`00b2ae34`](#insn-00b2ae34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae5c`](#insn-00b2ae5c) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae6c`](#insn-00b2ae6c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae74`](#insn-00b2ae74) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae90`](#insn-00b2ae90) → [`005e8198`](../005e8/005e8198.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e8198` · 推定シンボル `None` · 推定型 `None`
- [`00b2ae9c`](#insn-00b2ae9c) → [`005e8198`](../005e8/005e8198.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e8198` · 推定シンボル `None` · 推定型 `None`
- [`00b2aebc`](#insn-00b2aebc) → [`00b2aec8`](#insn-00b2aec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aed0`](#insn-00b2aed0) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00b2aed8`](#insn-00b2aed8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aee8`](#insn-00b2aee8) → [`00b2aef0`](#insn-00b2aef0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aef4`](#insn-00b2aef4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aefc`](#insn-00b2aefc) → [`00b2af44`](#insn-00b2af44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af04`](#insn-00b2af04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af08`](#insn-00b2af08) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af0c`](#insn-00b2af0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af10`](#insn-00b2af10) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af14`](#insn-00b2af14) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af44`](#insn-00b2af44) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2ade0`](#insn-00b2ade0)

~~~json
{
  "source": "00b2ade0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ade4`](#insn-00b2ade4)

~~~json
{
  "source": "00b2ade4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ade8`](#insn-00b2ade8)

~~~json
{
  "source": "00b2ade8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2adec`](#insn-00b2adec)

~~~json
{
  "source": "00b2adec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2adf0`](#insn-00b2adf0)

~~~json
{
  "source": "00b2adf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ae0c`](#insn-00b2ae0c)

~~~json
{
  "source": "00b2ae0c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ae1c`](#insn-00b2ae1c)

~~~json
{
  "source": "00b2ae1c",
  "target": "00b2ae58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ae24`](#insn-00b2ae24)

~~~json
{
  "source": "00b2ae24",
  "target": "00b2ae34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ae30`](#insn-00b2ae30)

~~~json
{
  "source": "00b2ae30",
  "target": "00b2ae58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ae40`](#insn-00b2ae40)

~~~json
{
  "source": "00b2ae40",
  "target": "00b2ae28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ae48`](#insn-00b2ae48)

~~~json
{
  "source": "00b2ae48",
  "target": "00b2aeec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ae50`](#insn-00b2ae50)

~~~json
{
  "source": "00b2ae50",
  "target": "00b2ae34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ae5c`](#insn-00b2ae5c)

~~~json
{
  "source": "00b2ae5c",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ae6c`](#insn-00b2ae6c)

~~~json
{
  "source": "00b2ae6c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ae74`](#insn-00b2ae74)

~~~json
{
  "source": "00b2ae74",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ae90`](#insn-00b2ae90)

~~~json
{
  "source": "00b2ae90",
  "target": "005e8198",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ae9c`](#insn-00b2ae9c)

~~~json
{
  "source": "00b2ae9c",
  "target": "005e8198",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2aebc`](#insn-00b2aebc)

~~~json
{
  "source": "00b2aebc",
  "target": "00b2aec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aed0`](#insn-00b2aed0)

~~~json
{
  "source": "00b2aed0",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2aed8`](#insn-00b2aed8)

~~~json
{
  "source": "00b2aed8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aee8`](#insn-00b2aee8)

~~~json
{
  "source": "00b2aee8",
  "target": "00b2aef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aef4`](#insn-00b2aef4)

~~~json
{
  "source": "00b2aef4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aefc`](#insn-00b2aefc)

~~~json
{
  "source": "00b2aefc",
  "target": "00b2af44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af04`](#insn-00b2af04)

~~~json
{
  "source": "00b2af04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af08`](#insn-00b2af08)

~~~json
{
  "source": "00b2af08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af0c`](#insn-00b2af0c)

~~~json
{
  "source": "00b2af0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af10`](#insn-00b2af10)

~~~json
{
  "source": "00b2af10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af14`](#insn-00b2af14)

~~~json
{
  "source": "00b2af14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af44`](#insn-00b2af44)

~~~json
{
  "source": "00b2af44",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
