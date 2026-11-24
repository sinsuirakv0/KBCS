# 00c0feac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b93464`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93464.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0073.md#compare-654041a77067543893d4136c6fc777bf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c102d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c102d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-a4f4e9ebf07849897b25ed09d2cf4a14)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c0feac",
  "name": "_ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwb",
  "size": 416,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20efaef8f39cd423b30662954889cb1028ca9b581d15a870efddf0bb30b06de9",
  "source_text_sha256": "20efaef8f39cd423b30662954889cb1028ca9b581d15a870efddf0bb30b06de9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c0feac",
        "00c1004b"
      ]
    ],
    "bytes_sha256": "93fb8b8cebe1e4f0ff3f2c70974f44730917b0d308c93d6acf2a0cbf0d167cfe",
    "instruction_count": 104,
    "instruction_bytes": 416,
    "body_bytes": 416,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c05b30](../00c05/00c05b30.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c5dae0](../00c5d/00c5dae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3048 bytes

~~~c

long * _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwb
                 (long *param_1,long *param_2,long param_3,undefined8 param_4,ulong param_5)

{
  long lVar1;
  ulong uVar2;
  int *piVar3;
  undefined *puVar4;
  bool bVar5;
  int iVar6;
  long *plVar7;
  int *piVar8;
  ulong uVar9;
  ulong uVar10;
  int *piVar11;
  undefined **local_60;
  ulong local_58;
  int *piStack_50;
  long local_48;
  undefined *local_40;
  undefined1 *local_38;
  
  if ((*(byte *)(param_3 + 8) & 1) == 0) {
                    /* WARNING: Could not recover jumptable at 0x00c0fef8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    plVar7 = (long *)(**(code **)(*param_1 + 0x30))(param_1,param_2,param_3,param_4,param_5 & 1);
    return plVar7;
  }
  _ZNKSt6__ndk18ios_base6getlocEv(&local_48,param_3);
  puVar4 = PTR__ZNSt6__ndk18numpunctIwE2idE_00c9b7c8;
  local_40 = PTR__ZNSt6__ndk18numpunctIwE2idE_00c9b7c8;
  if (*(long *)PTR__ZNSt6__ndk18numpunctIwE2idE_00c9b7c8 != -1) {
    local_60 = &local_40;
    local_38 = (undefined1 *)&local_60;
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk18numpunctIwE2idE_00c9b7c8,&local_38,FUN_00c35b90);
  }
  if (((long)*(int *)(puVar4 + 8) - 1U <
       (ulong)(*(long *)(local_48 + 0x18) - *(long *)(local_48 + 0x10) >> 3)) &&
     (plVar7 = *(long **)(*(long *)(local_48 + 0x10) + ((long)*(int *)(puVar4 + 8) - 1U) * 8),
     plVar7 != (long *)0x0)) {
    _ZNSt6__ndk16localeD1Ev(&local_48);
    lVar1 = 0x30;
    if ((param_5 & 1) == 0) {
      lVar1 = 0x38;
    }
    (**(code **)(*plVar7 + lVar1))(&local_60,plVar7);
    uVar9 = (ulong)local_60 & 0xff;
    bVar5 = ((ulong)local_60 & 1) != 0;
    uVar10 = (ulong)local_60 >> 1 & 0x7f;
    if (bVar5) {
      uVar10 = local_58;
    }
    piVar8 = piStack_50;
    if (uVar10 != 0) {
      uVar10 = local_58;
      plVar7 = param_2;
      piVar11 = (int *)((ulong)&local_60 | 4);
      if (bVar5) {
        piVar11 = piStack_50;
      }
      do {
        param_2 = plVar7;
        if (plVar7 != (long *)0x0) {
          piVar8 = (int *)plVar7[6];
          iVar6 = *piVar11;
          if (piVar8 == (int *)plVar7[7]) {
            iVar6 = (**(code **)(*plVar7 + 0x68))(plVar7);
          }
          else {
            *piVar8 = iVar6;
            plVar7[6] = (long)(piVar8 + 1);
          }
          uVar9 = (ulong)local_60 & 0xff;
          piVar8 = piStack_50;
          uVar10 = local_58;
          param_2 = (long *)0x0;
          if (iVar6 != -1) {
            param_2 = plVar7;
          }
        }
        piVar11 = piVar11 + 1;
        uVar2 = uVar9 >> 1;
        piVar3 = (int *)((ulong)&local_60 | 4);
        if ((uVar9 & 1) != 0) {
          uVar2 = uVar10;
          piVar3 = piVar8;
        }
        plVar7 = param_2;
      } while (piVar11 != piVar3 + uVar2);
    }
    if ((uVar9 & 1) != 0) {
      _ZdlPv(piVar8);
    }
    return param_2;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00c05b30();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c0feac"></a> `00c0feac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c0feb0"></a> `00c0feb0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00c0feb4"></a> `00c0feb4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c0feb8"></a> `00c0feb8` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c0febc"></a> `00c0febc` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c0fec0"></a> `00c0fec0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00c0fec4"></a> `00c0fec4` | `48 20 40 39` | ldrb w8,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00c0fec8"></a> `00c0fec8` | `f4 03 04 2a` | mov w20,w4 | `FALL_THROUGH`
<a id="insn-00c0fecc"></a> `00c0fecc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c0fed0"></a> `00c0fed0` | `68 01 00 37` | tbnz w8,#0x0,0x00c0fefc | `CONDITIONAL_JUMP`
<a id="insn-00c0fed4"></a> `00c0fed4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00c0fed8"></a> `00c0fed8` | `84 02 40 92` | and x4,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00c0fedc"></a> `00c0fedc` | `10 19 40 f9` | ldr x16,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00c0fee0"></a> `00c0fee0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c0fee4"></a> `00c0fee4` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c0fee8"></a> `00c0fee8` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c0feec"></a> `00c0feec` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c0fef0"></a> `00c0fef0` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00c0fef4"></a> `00c0fef4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c0fef8"></a> `00c0fef8` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00c0fefc"></a> `00c0fefc` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00c0ff00"></a> `00c0ff00` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00c0ff04"></a> `00c0ff04` | `db 1f 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00c0ff08"></a> `00c0ff08` | `76 04 00 90` | adrp x22,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c0ff0c"></a> `00c0ff0c` | `d6 e6 43 f9` | ldr x22,[x22, #0x7c8] | `FALL_THROUGH`
<a id="insn-00c0ff10"></a> `00c0ff10` | `f5 0f 40 f9` | ldr x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00c0ff14"></a> `00c0ff14` | `b6 03 1f f8` | stur x22,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00c0ff18"></a> `00c0ff18` | `c8 fe df c8` | ldar x8,[x22] | `FALL_THROUGH`
<a id="insn-00c0ff1c"></a> `00c0ff1c` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0ff20"></a> `00c0ff20` | `60 01 00 54` | b.eq 0x00c0ff4c | `CONDITIONAL_JUMP`
<a id="insn-00c0ff24"></a> `00c0ff24` | `a8 43 00 d1` | sub x8,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00c0ff28"></a> `00c0ff28` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00c0ff2c"></a> `00c0ff2c` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00c0ff30"></a> `00c0ff30` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00c0ff34"></a> `00c0ff34` | `60 04 00 90` | adrp x0,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c0ff38"></a> `00c0ff38` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c0ff3c"></a> `00c0ff3c` | `a2 e2 12 10` | adr x2,0xc35b90 | `FALL_THROUGH`
<a id="insn-00c0ff40"></a> `00c0ff40` | `00 e4 43 f9` | ldr x0,[x0, #0x7c8] | `FALL_THROUGH`
<a id="insn-00c0ff44"></a> `00c0ff44` | `a1 23 00 d1` | sub x1,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00c0ff48"></a> `00c0ff48` | `e6 36 01 94` | bl 0x00c5dae0 | `UNCONDITIONAL_CALL`
<a id="insn-00c0ff4c"></a> `00c0ff4c` | `a8 2a 41 a9` | ldp x8,x10,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00c0ff50"></a> `00c0ff50` | `c9 0a 80 b9` | ldrsw x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c0ff54"></a> `00c0ff54` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c0ff58"></a> `00c0ff58` | `4a 01 08 cb` | sub x10,x10,x8 | `FALL_THROUGH`
<a id="insn-00c0ff5c"></a> `00c0ff5c` | `3f 0d 8a eb` | cmp x9,x10, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00c0ff60"></a> `00c0ff60` | `42 07 00 54` | b.cs 0x00c10048 | `CONDITIONAL_JUMP`
<a id="insn-00c0ff64"></a> `00c0ff64` | `15 79 69 f8` | ldr x21,[x8, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c0ff68"></a> `00c0ff68` | `15 07 00 b4` | cbz x21,0x00c10048 | `CONDITIONAL_JUMP`
<a id="insn-00c0ff6c"></a> `00c0ff6c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00c0ff70"></a> `00c0ff70` | `c8 1f 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00c0ff74"></a> `00c0ff74` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0ff78"></a> `00c0ff78` | `9f 02 00 72` | tst w20,#0x1 | `FALL_THROUGH`
<a id="insn-00c0ff7c"></a> `00c0ff7c` | `09 07 80 52` | mov w9,#0x38 | `FALL_THROUGH`
<a id="insn-00c0ff80"></a> `00c0ff80` | `0a 06 80 52` | mov w10,#0x30 | `FALL_THROUGH`
<a id="insn-00c0ff84"></a> `00c0ff84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c0ff88"></a> `00c0ff88` | `f4 03 00 91` | mov x20,sp | `FALL_THROUGH`
<a id="insn-00c0ff8c"></a> `00c0ff8c` | `49 11 89 9a` | csel x9,x10,x9,ne | `FALL_THROUGH`
<a id="insn-00c0ff90"></a> `00c0ff90` | `09 69 69 f8` | ldr x9,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00c0ff94"></a> `00c0ff94` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00c0ff98"></a> `00c0ff98` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00c0ff9c"></a> `00c0ff9c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00c0ffa0"></a> `00c0ffa0` | `e9 83 40 a9` | ldp x9,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c0ffa4"></a> `00c0ffa4` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0ffa8"></a> `00c0ffa8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0ffac"></a> `00c0ffac` | `4a 01 89 9a` | csel x10,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00c0ffb0"></a> `00c0ffb0` | `aa 03 00 b4` | cbz x10,0x00c10024 | `CONDITIONAL_JUMP`
<a id="insn-00c0ffb4"></a> `00c0ffb4` | `94 02 7e b2` | orr x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00c0ffb8"></a> `00c0ffb8` | `95 02 80 9a` | csel x21,x20,x0,eq | `FALL_THROUGH`
<a id="insn-00c0ffbc"></a> `00c0ffbc` | `0f 00 00 14` | b 0x00c0fff8 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0ffc0"></a> `00c0ffc0` | `01 45 00 b8` | str w1,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00c0ffc4"></a> `00c0ffc4` | `68 1a 00 f9` | str x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00c0ffc8"></a> `00c0ffc8` | `e9 83 40 a9` | ldp x9,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c0ffcc"></a> `00c0ffcc` | `3f 04 00 31` | cmn w1,#0x1 | `FALL_THROUGH`
<a id="insn-00c0ffd0"></a> `00c0ffd0` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00c0ffd4"></a> `00c0ffd4` | `f3 03 93 9a` | csel x19,xzr,x19,eq | `FALL_THROUGH`
<a id="insn-00c0ffd8"></a> `00c0ffd8` | `0a 7d 01 53` | lsr w10,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0ffdc"></a> `00c0ffdc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0ffe0"></a> `00c0ffe0` | `b5 12 00 91` | add x21,x21,#0x4 | `FALL_THROUGH`
<a id="insn-00c0ffe4"></a> `00c0ffe4` | `8b 02 80 9a` | csel x11,x20,x0,eq | `FALL_THROUGH`
<a id="insn-00c0ffe8"></a> `00c0ffe8` | `4a 01 89 9a` | csel x10,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00c0ffec"></a> `00c0ffec` | `6a 09 0a 8b` | add x10,x11,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00c0fff0"></a> `00c0fff0` | `bf 02 0a eb` | cmp x21,x10 | `FALL_THROUGH`
<a id="insn-00c0fff4"></a> `00c0fff4` | `80 01 00 54` | b.eq 0x00c10024 | `CONDITIONAL_JUMP`
<a id="insn-00c0fff8"></a> `00c0fff8` | `13 ff ff b4` | cbz x19,0x00c0ffd8 | `CONDITIONAL_JUMP`
<a id="insn-00c0fffc"></a> `00c0fffc` | `68 26 43 a9` | ldp x8,x9,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00c10000"></a> `00c10000` | `a1 02 40 b9` | ldr w1,[x21] | `FALL_THROUGH`
<a id="insn-00c10004"></a> `00c10004` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c10008"></a> `00c10008` | `c1 fd ff 54` | b.ne 0x00c0ffc0 | `CONDITIONAL_JUMP`
<a id="insn-00c1000c"></a> `00c1000c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00c10010"></a> `00c10010` | `08 35 40 f9` | ldr x8,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-00c10014"></a> `00c10014` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c10018"></a> `00c10018` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c1001c"></a> `00c1001c` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00c10020"></a> `00c10020` | `ea ff ff 17` | b 0x00c0ffc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00c10024"></a> `00c10024` | `48 00 00 36` | tbz w8,#0x0,0x00c1002c | `CONDITIONAL_JUMP`
<a id="insn-00c10028"></a> `00c10028` | `a2 1e 01 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1002c"></a> `00c1002c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c10030"></a> `00c10030` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c10034"></a> `00c10034` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c10038"></a> `00c10038` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1003c"></a> `00c1003c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00c10040"></a> `00c10040` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c10044"></a> `00c10044` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c10048"></a> `00c10048` | `ba d6 ff 97` | bl 0x00c05b30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c0feac`](#insn-00c0feac) 範囲 `[['00c0feac', '00c0fed3']]`
  - `CONDITIONAL_JUMP` [`00c0fed0`](#insn-00c0fed0) → [`00c0fefc`](#insn-00c0fefc)
  - `FALL_THROUGH` [`00c0fed0`](#insn-00c0fed0) → [`00c0fed4`](#insn-00c0fed4)
- ブロック [`00c0fed4`](#insn-00c0fed4) 範囲 `[['00c0fed4', '00c0fefb']]`
- ブロック [`00c0fefc`](#insn-00c0fefc) 範囲 `[['00c0fefc', '00c0ff23']]`
  - `CONDITIONAL_JUMP` [`00c0ff20`](#insn-00c0ff20) → [`00c0ff4c`](#insn-00c0ff4c)
  - `FALL_THROUGH` [`00c0ff20`](#insn-00c0ff20) → [`00c0ff24`](#insn-00c0ff24)
- ブロック [`00c0ff24`](#insn-00c0ff24) 範囲 `[['00c0ff24', '00c0ff4b']]`
  - `FALL_THROUGH` [`00c0ff48`](#insn-00c0ff48) → [`00c0ff4c`](#insn-00c0ff4c)
- ブロック [`00c0ff4c`](#insn-00c0ff4c) 範囲 `[['00c0ff4c', '00c0ff63']]`
  - `CONDITIONAL_JUMP` [`00c0ff60`](#insn-00c0ff60) → [`00c10048`](#insn-00c10048)
  - `FALL_THROUGH` [`00c0ff60`](#insn-00c0ff60) → [`00c0ff64`](#insn-00c0ff64)
- ブロック [`00c0ff64`](#insn-00c0ff64) 範囲 `[['00c0ff64', '00c0ff6b']]`
  - `CONDITIONAL_JUMP` [`00c0ff68`](#insn-00c0ff68) → [`00c10048`](#insn-00c10048)
  - `FALL_THROUGH` [`00c0ff68`](#insn-00c0ff68) → [`00c0ff6c`](#insn-00c0ff6c)
- ブロック [`00c0ff6c`](#insn-00c0ff6c) 範囲 `[['00c0ff6c', '00c0ffb3']]`
  - `CONDITIONAL_JUMP` [`00c0ffb0`](#insn-00c0ffb0) → [`00c10024`](#insn-00c10024)
  - `FALL_THROUGH` [`00c0ffb0`](#insn-00c0ffb0) → [`00c0ffb4`](#insn-00c0ffb4)
- ブロック [`00c0ffb4`](#insn-00c0ffb4) 範囲 `[['00c0ffb4', '00c0ffbf']]`
  - `UNCONDITIONAL_JUMP` [`00c0ffbc`](#insn-00c0ffbc) → [`00c0fff8`](#insn-00c0fff8)
- ブロック [`00c0ffc0`](#insn-00c0ffc0) 範囲 `[['00c0ffc0', '00c0ffc7']]`
  - `FALL_THROUGH` [`00c0ffc4`](#insn-00c0ffc4) → [`00c0ffc8`](#insn-00c0ffc8)
- ブロック [`00c0ffc8`](#insn-00c0ffc8) 範囲 `[['00c0ffc8', '00c0ffd7']]`
  - `FALL_THROUGH` [`00c0ffd4`](#insn-00c0ffd4) → [`00c0ffd8`](#insn-00c0ffd8)
- ブロック [`00c0ffd8`](#insn-00c0ffd8) 範囲 `[['00c0ffd8', '00c0fff7']]`
  - `CONDITIONAL_JUMP` [`00c0fff4`](#insn-00c0fff4) → [`00c10024`](#insn-00c10024)
  - `FALL_THROUGH` [`00c0fff4`](#insn-00c0fff4) → [`00c0fff8`](#insn-00c0fff8)
- ブロック [`00c0fff8`](#insn-00c0fff8) 範囲 `[['00c0fff8', '00c0fffb']]`
  - `CONDITIONAL_JUMP` [`00c0fff8`](#insn-00c0fff8) → [`00c0ffd8`](#insn-00c0ffd8)
  - `FALL_THROUGH` [`00c0fff8`](#insn-00c0fff8) → [`00c0fffc`](#insn-00c0fffc)
- ブロック [`00c0fffc`](#insn-00c0fffc) 範囲 `[['00c0fffc', '00c1000b']]`
  - `CONDITIONAL_JUMP` [`00c10008`](#insn-00c10008) → [`00c0ffc0`](#insn-00c0ffc0)
  - `FALL_THROUGH` [`00c10008`](#insn-00c10008) → [`00c1000c`](#insn-00c1000c)
- ブロック [`00c1000c`](#insn-00c1000c) 範囲 `[['00c1000c', '00c10023']]`
  - `UNCONDITIONAL_JUMP` [`00c10020`](#insn-00c10020) → [`00c0ffc8`](#insn-00c0ffc8)
- ブロック [`00c10024`](#insn-00c10024) 範囲 `[['00c10024', '00c10027']]`
  - `CONDITIONAL_JUMP` [`00c10024`](#insn-00c10024) → [`00c1002c`](#insn-00c1002c)
  - `FALL_THROUGH` [`00c10024`](#insn-00c10024) → [`00c10028`](#insn-00c10028)
- ブロック [`00c10028`](#insn-00c10028) 範囲 `[['00c10028', '00c1002b']]`
  - `FALL_THROUGH` [`00c10028`](#insn-00c10028) → [`00c1002c`](#insn-00c1002c)
- ブロック [`00c1002c`](#insn-00c1002c) 範囲 `[['00c1002c', '00c10047']]`
- ブロック [`00c10048`](#insn-00c10048) 範囲 `[['00c10048', '00c1004b']]`

## 命令位置別の参照

- [`00c0feb4`](#insn-00c0feb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0feb8`](#insn-00c0feb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0febc`](#insn-00c0febc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0fed0`](#insn-00c0fed0) → [`00c0fefc`](#insn-00c0fefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0fee4`](#insn-00c0fee4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0fee8`](#insn-00c0fee8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0feec`](#insn-00c0feec) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff04`](#insn-00c0ff04) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff0c`](#insn-00c0ff0c) → `00c9b7c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c0ff10`](#insn-00c0ff10) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff14`](#insn-00c0ff14) → `01127a98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk18numpunctIwE2idE` · 推定型 `undefined8`
- [`00c0ff14`](#insn-00c0ff14) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff18`](#insn-00c0ff18) → `01127a98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk18numpunctIwE2idE` · 推定型 `undefined8`
- [`00c0ff20`](#insn-00c0ff20) → [`00c0ff4c`](#insn-00c0ff4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff2c`](#insn-00c0ff2c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff30`](#insn-00c0ff30) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff3c`](#insn-00c0ff3c) → [`00c35b90`](../00c35/00c35b90.md) · `PARAM` · `ANALYSIS` · 関数 `00c35b90` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff40`](#insn-00c0ff40) → `00c9b7c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c0ff40`](#insn-00c0ff40) → `01127a98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk18numpunctIwE2idE` · 推定型 `undefined8`
- [`00c0ff48`](#insn-00c0ff48) → [`00c5dae0`](../00c5d/00c5dae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dae0` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff50`](#insn-00c0ff50) → `01127aa0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c0ff60`](#insn-00c0ff60) → [`00c10048`](#insn-00c10048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff68`](#insn-00c0ff68) → [`00c10048`](#insn-00c10048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff70`](#insn-00c0ff70) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00c0ff9c`](#insn-00c0ff9c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ffa0`](#insn-00c0ffa0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ffb0`](#insn-00c0ffb0) → [`00c10024`](#insn-00c10024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ffbc`](#insn-00c0ffbc) → [`00c0fff8`](#insn-00c0fff8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ffc8`](#insn-00c0ffc8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ffd0`](#insn-00c0ffd0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0fff4`](#insn-00c0fff4) → [`00c10024`](#insn-00c10024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0fff8`](#insn-00c0fff8) → [`00c0ffd8`](#insn-00c0ffd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c10008`](#insn-00c10008) → [`00c0ffc0`](#insn-00c0ffc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c10020`](#insn-00c10020) → [`00c0ffc8`](#insn-00c0ffc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c10024`](#insn-00c10024) → [`00c1002c`](#insn-00c1002c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c10028`](#insn-00c10028) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00c10030`](#insn-00c10030) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c10034`](#insn-00c10034) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c10038`](#insn-00c10038) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c10048`](#insn-00c10048) → [`00c05b30`](../00c05/00c05b30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c05b30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c0feb4`](#insn-00c0feb4)

~~~json
{
  "source": "00c0feb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0feb8`](#insn-00c0feb8)

~~~json
{
  "source": "00c0feb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0febc`](#insn-00c0febc)

~~~json
{
  "source": "00c0febc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0fed0`](#insn-00c0fed0)

~~~json
{
  "source": "00c0fed0",
  "target": "00c0fefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0fee4`](#insn-00c0fee4)

~~~json
{
  "source": "00c0fee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0fee8`](#insn-00c0fee8)

~~~json
{
  "source": "00c0fee8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0feec`](#insn-00c0feec)

~~~json
{
  "source": "00c0feec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ff04`](#insn-00c0ff04)

~~~json
{
  "source": "00c0ff04",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0ff0c`](#insn-00c0ff0c)

~~~json
{
  "source": "00c0ff0c",
  "target": "00c9b7c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b7c8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c0ff10`](#insn-00c0ff10)

~~~json
{
  "source": "00c0ff10",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ff14`](#insn-00c0ff14)

~~~json
{
  "source": "00c0ff14",
  "target": "01127a98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0ff14`](#insn-00c0ff14)

~~~json
{
  "source": "00c0ff14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ff18`](#insn-00c0ff18)

~~~json
{
  "source": "00c0ff18",
  "target": "01127a98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0ff20`](#insn-00c0ff20)

~~~json
{
  "source": "00c0ff20",
  "target": "00c0ff4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ff2c`](#insn-00c0ff2c)

~~~json
{
  "source": "00c0ff2c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ff30`](#insn-00c0ff30)

~~~json
{
  "source": "00c0ff30",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ff3c`](#insn-00c0ff3c)

~~~json
{
  "source": "00c0ff3c",
  "target": "00c35b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0ff40`](#insn-00c0ff40)

~~~json
{
  "source": "00c0ff40",
  "target": "00c9b7c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b7c8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c0ff40`](#insn-00c0ff40)

~~~json
{
  "source": "00c0ff40",
  "target": "01127a98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0ff48`](#insn-00c0ff48)

~~~json
{
  "source": "00c0ff48",
  "target": "00c5dae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0ff50`](#insn-00c0ff50)

~~~json
{
  "source": "00c0ff50",
  "target": "01127aa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127aa0",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0ff60`](#insn-00c0ff60)

~~~json
{
  "source": "00c0ff60",
  "target": "00c10048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ff68`](#insn-00c0ff68)

~~~json
{
  "source": "00c0ff68",
  "target": "00c10048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ff70`](#insn-00c0ff70)

~~~json
{
  "source": "00c0ff70",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0ff9c`](#insn-00c0ff9c)

~~~json
{
  "source": "00c0ff9c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ffa0`](#insn-00c0ffa0)

~~~json
{
  "source": "00c0ffa0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ffb0`](#insn-00c0ffb0)

~~~json
{
  "source": "00c0ffb0",
  "target": "00c10024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ffbc`](#insn-00c0ffbc)

~~~json
{
  "source": "00c0ffbc",
  "target": "00c0fff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ffc8`](#insn-00c0ffc8)

~~~json
{
  "source": "00c0ffc8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ffd0`](#insn-00c0ffd0)

~~~json
{
  "source": "00c0ffd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0fff4`](#insn-00c0fff4)

~~~json
{
  "source": "00c0fff4",
  "target": "00c10024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0fff8`](#insn-00c0fff8)

~~~json
{
  "source": "00c0fff8",
  "target": "00c0ffd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c10008`](#insn-00c10008)

~~~json
{
  "source": "00c10008",
  "target": "00c0ffc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c10020`](#insn-00c10020)

~~~json
{
  "source": "00c10020",
  "target": "00c0ffc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c10024`](#insn-00c10024)

~~~json
{
  "source": "00c10024",
  "target": "00c1002c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c10028`](#insn-00c10028)

~~~json
{
  "source": "00c10028",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c10030`](#insn-00c10030)

~~~json
{
  "source": "00c10030",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c10034`](#insn-00c10034)

~~~json
{
  "source": "00c10034",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c10038`](#insn-00c10038)

~~~json
{
  "source": "00c10038",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c10048`](#insn-00c10048)

~~~json
{
  "source": "00c10048",
  "target": "00c05b30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
