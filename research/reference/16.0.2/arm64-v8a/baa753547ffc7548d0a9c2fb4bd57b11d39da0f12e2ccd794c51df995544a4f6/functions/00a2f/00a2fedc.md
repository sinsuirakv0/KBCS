# 00a2fedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a2fe88`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2fe88.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0061.md#compare-b7324dbf7cce9defc1417593266d35c7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00a30ed0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a30/00a30ed0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0062.md#compare-e8be8595adc5d71f4d390e9d821987c7)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a2fedc",
  "name": "FUN_00a2fedc",
  "size": 664,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0393a0952242a791dad232b3511da998761d067aebbce1ce9a700ba571033048",
  "source_text_sha256": "0393a0952242a791dad232b3511da998761d067aebbce1ce9a700ba571033048",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a2fedc",
        "00a30123"
      ],
      [
        "00a30130",
        "00a30143"
      ],
      [
        "00a30150",
        "00a3015f"
      ],
      [
        "00a30168",
        "00a3016f"
      ],
      [
        "00a30184",
        "00a301a7"
      ]
    ],
    "bytes_sha256": "7bc4b70ce67880f9e8c775c06c07dcec56acf03cf1d1ba1a60e01e340cee2e0a",
    "instruction_count": 166,
    "instruction_bytes": 664,
    "body_bytes": 664,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b2c4ec](../00b2c/00b2c4ec.md)

## 呼び出し先

- [0048ce94](../0048c/0048ce94.md)
- [004939d8](../00493/004939d8.md)
- [0077c8a4](../0077c/0077c8a4.md)
- [00c53ffc](../00c53/00c53ffc.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58020](../00c58/00c58020.md)
- [00c58030](../00c58/00c58030.md)
- [00c580d0](../00c58/00c580d0.md)

## 関連文字列（未確認候補）

~~~text
"scheme_item_param_"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3585 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

uint FUN_00a2fedc(undefined8 *param_1,undefined8 param_2)

{
  void *__src;
  undefined4 uVar1;
  int iVar2;
  size_t __n;
  long lVar3;
  long *plVar4;
  bool bVar5;
  uint uVar6;
  ulong *puVar7;
  undefined8 uVar8;
  void *unaff_x22;
  long *plVar9;
  long *plVar10;
  byte local_d8 [16];
  void *local_c8;
  ulong local_c0;
  ulong uStack_b8;
  void *local_b0;
  byte local_a8 [16];
  void *local_98;
  undefined4 local_90;
  int local_88;
  void *local_80;
  void *pvStack_78;
  undefined8 local_70;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  plVar9 = (long *)*param_1;
  if (plVar9 == param_1 + 1) {
    uVar6 = 0;
  }
  else {
    do {
      __src = (void *)plVar9[6];
      uVar1 = (undefined4)plVar9[4];
      iVar2 = (int)plVar9[5];
      local_80 = (void *)0x0;
      pvStack_78 = (void *)0x0;
      __n = plVar9[7] - (long)__src;
      local_70 = 0;
      local_90 = uVar1;
      local_88 = iVar2;
      if (__n == 0) {
        unaff_x22 = (void *)0x0;
        if (iVar2 != 0) goto LAB_00a2ff9c;
LAB_00a2ffb0:
        _ZNSt6__ndk19to_stringEi(local_d8,uVar1);
        puVar7 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
                                    (local_d8,0,"scheme_item_param_");
        local_b0 = (void *)puVar7[2];
        uStack_b8 = puVar7[1];
        local_c0 = *puVar7;
        puVar7[1] = 0;
        puVar7[2] = 0;
        *puVar7 = 0;
        FUN_0048ce94(local_a8,&local_c0);
        uVar6 = FUN_004939d8(param_2,local_a8);
        if ((local_a8[0] & 1) != 0) {
          _ZdlPv(local_98);
        }
        if ((local_c0 & 1) != 0) {
          _ZdlPv(local_b0);
        }
        if ((local_d8[0] & 1) != 0) {
          _ZdlPv(local_c8);
        }
      }
      else {
        if (0x1555555555555555 < (ulong)(((long)__n >> 2) * -0x5555555555555555)) {
          if (*(long *)(lVar3 + 0x28) == local_68) {
            uVar8 = FUN_0077c8a4(&local_80);
            if ((local_a8[0] & 1) != 0) {
              _ZdlPv(local_98);
            }
            if ((local_c0 & 1) != 0) {
              _ZdlPv(local_b0);
            }
            if ((local_d8[0] & 1) != 0) {
              _ZdlPv(local_c8);
            }
            if (unaff_x22 != (void *)0x0) {
              _ZdlPv(unaff_x22);
            }
            if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_00c53ffc(uVar8);
            }
          }
          goto LAB_00a301a4;
        }
        unaff_x22 = (void *)_Znwm(__n);
        local_80 = unaff_x22;
        pvStack_78 = unaff_x22;
        memcpy(unaff_x22,__src,__n);
        if (iVar2 == 0) goto LAB_00a2ffb0;
LAB_00a2ff9c:
        uVar6 = 0;
      }
      if (unaff_x22 != (void *)0x0) {
        _ZdlPv(unaff_x22);
      }
      if ((uVar6 & 1) != 0) {
        uVar6 = 1;
        break;
      }
      plVar4 = (long *)plVar9[1];
      plVar10 = plVar9;
      if ((long *)plVar9[1] == (long *)0x0) {
        do {
          plVar9 = (long *)plVar10[2];
          bVar5 = (long *)*plVar9 != plVar10;
          plVar10 = plVar9;
        } while (bVar5);
      }
      else {
        do {
          plVar9 = plVar4;
          plVar4 = (long *)*plVar9;
        } while ((long *)*plVar9 != (long *)0x0);
      }
    } while (plVar9 != param_1 + 1);
  }
  if (*(long *)(lVar3 + 0x28) == local_68) {
    return uVar6 & 1;
  }
LAB_00a301a4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a2fedc"></a> `00a2fedc` | `ff 83 03 d1` | sub sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00a2fee0"></a> `00a2fee0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a2fee4"></a> `00a2fee4` | `fc 6f 09 a9` | stp x28,x27,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a2fee8"></a> `00a2fee8` | `fa 67 0a a9` | stp x26,x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00a2feec"></a> `00a2feec` | `f8 5f 0b a9` | stp x24,x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a2fef0"></a> `00a2fef0` | `f6 57 0c a9` | stp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00a2fef4"></a> `00a2fef4` | `f4 4f 0d a9` | stp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00a2fef8"></a> `00a2fef8` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00a2fefc"></a> `00a2fefc` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a2ff00"></a> `00a2ff00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a2ff04"></a> `00a2ff04` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00a2ff08"></a> `00a2ff08` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00a2ff0c"></a> `00a2ff0c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a2ff10"></a> `00a2ff10` | `7a 86 40 f8` | ldr x26,[x19], #0x8 | `FALL_THROUGH`
<a id="insn-00a2ff14"></a> `00a2ff14` | `5f 03 13 eb` | cmp x26,x19 | `FALL_THROUGH`
<a id="insn-00a2ff18"></a> `00a2ff18` | `a0 0b 00 54` | b.eq 0x00a3008c | `CONDITIONAL_JUMP`
<a id="insn-00a2ff1c"></a> `00a2ff1c` | `f5 f3 00 b2` | orr x21,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00a2ff20"></a> `00a2ff20` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00a2ff24"></a> `00a2ff24` | `bb c3 00 d1` | sub x27,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00a2ff28"></a> `00a2ff28` | `d5 aa 8a f2` | movk x21,#0x5556 | `FALL_THROUGH`
<a id="insn-00a2ff2c"></a> `00a2ff2c` | `b5 aa e2 f2` | movk x21,#0x1555, LSL #48 | `FALL_THROUGH`
<a id="insn-00a2ff30"></a> `00a2ff30` | `04 00 00 14` | b 0x00a2ff40 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2ff34"></a> `00a2ff34` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00a2ff38"></a> `00a2ff38` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00a2ff3c"></a> `00a2ff3c` | `e0 0a 00 54` | b.eq 0x00a30098 | `CONDITIONAL_JUMP`
<a id="insn-00a2ff40"></a> `00a2ff40` | `58 23 43 a9` | ldp x24,x8,[x26, #0x30] | `FALL_THROUGH`
<a id="insn-00a2ff44"></a> `00a2ff44` | `57 23 40 b9` | ldr w23,[x26, #0x20] | `FALL_THROUGH`
<a id="insn-00a2ff48"></a> `00a2ff48` | `5c 2b 40 b9` | ldr w28,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00a2ff4c"></a> `00a2ff4c` | `7f 7f 01 a9` | stp xzr,xzr,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00a2ff50"></a> `00a2ff50` | `b7 03 1d b8` | stur w23,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00a2ff54"></a> `00a2ff54` | `19 01 18 eb` | subs x25,x8,x24 | `FALL_THROUGH`
<a id="insn-00a2ff58"></a> `00a2ff58` | `bc 83 1d b8` | stur w28,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00a2ff5c"></a> `00a2ff5c` | `7f 03 02 f8` | stur xzr,[x27, #0x20] | `FALL_THROUGH`
<a id="insn-00a2ff60"></a> `00a2ff60` | `40 02 00 54` | b.eq 0x00a2ffa8 | `CONDITIONAL_JUMP`
<a id="insn-00a2ff64"></a> `00a2ff64` | `28 ff 42 93` | asr x8,x25,#0x2 | `FALL_THROUGH`
<a id="insn-00a2ff68"></a> `00a2ff68` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00a2ff6c"></a> `00a2ff6c` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00a2ff70"></a> `00a2ff70` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00a2ff74"></a> `00a2ff74` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00a2ff78"></a> `00a2ff78` | `c2 0a 00 54` | b.cs 0x00a300d0 | `CONDITIONAL_JUMP`
<a id="insn-00a2ff7c"></a> `00a2ff7c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00a2ff80"></a> `00a2ff80` | `f8 9f 08 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00a2ff84"></a> `00a2ff84` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00a2ff88"></a> `00a2ff88` | `e2 03 19 aa` | mov x2,x25 | `FALL_THROUGH`
<a id="insn-00a2ff8c"></a> `00a2ff8c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00a2ff90"></a> `00a2ff90` | `a0 03 3e a9` | stp x0,x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00a2ff94"></a> `00a2ff94` | `4f a0 08 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00a2ff98"></a> `00a2ff98` | `dc 00 00 34` | cbz w28,0x00a2ffb0 | `CONDITIONAL_JUMP`
<a id="insn-00a2ff9c"></a> `00a2ff9c` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00a2ffa0"></a> `00a2ffa0` | `16 04 00 b5` | cbnz x22,0x00a30020 | `CONDITIONAL_JUMP`
<a id="insn-00a2ffa4"></a> `00a2ffa4` | `21 00 00 14` | b 0x00a30028 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2ffa8"></a> `00a2ffa8` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00a2ffac"></a> `00a2ffac` | `9c ff ff 35` | cbnz w28,0x00a2ff9c | `CONDITIONAL_JUMP`
<a id="insn-00a2ffb0"></a> `00a2ffb0` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a2ffb4"></a> `00a2ffb4` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00a2ffb8"></a> `00a2ffb8` | `1a a0 08 94` | bl 0x00c58020 | `UNCONDITIONAL_CALL`
<a id="insn-00a2ffbc"></a> `00a2ffbc` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a2ffc0"></a> `00a2ffc0` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00a2ffc4"></a> `00a2ffc4` | `62 c4 ff 90` | adrp x2,0x2bb000 | `FALL_THROUGH`
<a id="insn-00a2ffc8"></a> `00a2ffc8` | `42 74 1d 91` | add x2,x2,#0x75d | `FALL_THROUGH`
<a id="insn-00a2ffcc"></a> `00a2ffcc` | `19 a0 08 94` | bl 0x00c58030 | `UNCONDITIONAL_CALL`
<a id="insn-00a2ffd0"></a> `00a2ffd0` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a2ffd4"></a> `00a2ffd4` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00a2ffd8"></a> `00a2ffd8` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a2ffdc"></a> `00a2ffdc` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a2ffe0"></a> `00a2ffe0` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a2ffe4"></a> `00a2ffe4` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00a2ffe8"></a> `00a2ffe8` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00a2ffec"></a> `00a2ffec` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00a2fff0"></a> `00a2fff0` | `a9 73 e9 97` | bl 0x0048ce94 | `UNCONDITIONAL_CALL`
<a id="insn-00a2fff4"></a> `00a2fff4` | `e1 e3 00 91` | add x1,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00a2fff8"></a> `00a2fff8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a2fffc"></a> `00a2fffc` | `77 8e e9 97` | bl 0x004939d8 | `UNCONDITIONAL_CALL`
<a id="insn-00a30000"></a> `00a30000` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00a30004"></a> `00a30004` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00a30008"></a> `00a30008` | `a8 02 00 37` | tbnz w8,#0x0,0x00a3005c | `CONDITIONAL_JUMP`
<a id="insn-00a3000c"></a> `00a3000c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a30010"></a> `00a30010` | `e8 02 00 37` | tbnz w8,#0x0,0x00a3006c | `CONDITIONAL_JUMP`
<a id="insn-00a30014"></a> `00a30014` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a30018"></a> `00a30018` | `28 03 00 37` | tbnz w8,#0x0,0x00a3007c | `CONDITIONAL_JUMP`
<a id="insn-00a3001c"></a> `00a3001c` | `76 00 00 b4` | cbz x22,0x00a30028 | `CONDITIONAL_JUMP`
<a id="insn-00a30020"></a> `00a30020` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00a30024"></a> `00a30024` | `d7 9f 08 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a30028"></a> `00a30028` | `77 03 00 37` | tbnz w23,#0x0,0x00a30094 | `CONDITIONAL_JUMP`
<a id="insn-00a3002c"></a> `00a3002c` | `49 07 40 f9` | ldr x9,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00a30030"></a> `00a30030` | `a9 00 00 b4` | cbz x9,0x00a30044 | `CONDITIONAL_JUMP`
<a id="insn-00a30034"></a> `00a30034` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00a30038"></a> `00a30038` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a3003c"></a> `00a3003c` | `c9 ff ff b5` | cbnz x9,0x00a30034 | `CONDITIONAL_JUMP`
<a id="insn-00a30040"></a> `00a30040` | `bd ff ff 17` | b 0x00a2ff34 | `UNCONDITIONAL_JUMP`
<a id="insn-00a30044"></a> `00a30044` | `48 0b 40 f9` | ldr x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00a30048"></a> `00a30048` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00a3004c"></a> `00a3004c` | `3f 01 1a eb` | cmp x9,x26 | `FALL_THROUGH`
<a id="insn-00a30050"></a> `00a30050` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00a30054"></a> `00a30054` | `81 ff ff 54` | b.ne 0x00a30044 | `CONDITIONAL_JUMP`
<a id="insn-00a30058"></a> `00a30058` | `b7 ff ff 17` | b 0x00a2ff34 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3005c"></a> `00a3005c` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00a30060"></a> `00a30060` | `c8 9f 08 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a30064"></a> `00a30064` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a30068"></a> `00a30068` | `68 fd 07 36` | tbz w8,#0x0,0x00a30014 | `CONDITIONAL_JUMP`
<a id="insn-00a3006c"></a> `00a3006c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a30070"></a> `00a30070` | `c4 9f 08 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a30074"></a> `00a30074` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a30078"></a> `00a30078` | `28 fd 07 36` | tbz w8,#0x0,0x00a3001c | `CONDITIONAL_JUMP`
<a id="insn-00a3007c"></a> `00a3007c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a30080"></a> `00a30080` | `c0 9f 08 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a30084"></a> `00a30084` | `f6 fc ff b5` | cbnz x22,0x00a30020 | `CONDITIONAL_JUMP`
<a id="insn-00a30088"></a> `00a30088` | `e8 ff ff 17` | b 0x00a30028 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3008c"></a> `00a3008c` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00a30090"></a> `00a30090` | `02 00 00 14` | b 0x00a30098 | `UNCONDITIONAL_JUMP`
<a id="insn-00a30094"></a> `00a30094` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00a30098"></a> `00a30098` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00a3009c"></a> `00a3009c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00a300a0"></a> `00a300a0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a300a4"></a> `00a300a4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a300a8"></a> `00a300a8` | `e1 07 00 54` | b.ne 0x00a301a4 | `CONDITIONAL_JUMP`
<a id="insn-00a300ac"></a> `00a300ac` | `e0 02 00 12` | and w0,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00a300b0"></a> `00a300b0` | `f4 4f 4d a9` | ldp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00a300b4"></a> `00a300b4` | `f6 57 4c a9` | ldp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00a300b8"></a> `00a300b8` | `f8 5f 4b a9` | ldp x24,x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a300bc"></a> `00a300bc` | `fa 67 4a a9` | ldp x26,x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00a300c0"></a> `00a300c0` | `fc 6f 49 a9` | ldp x28,x27,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a300c4"></a> `00a300c4` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a300c8"></a> `00a300c8` | `ff 83 03 91` | add sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00a300cc"></a> `00a300cc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a300d0"></a> `00a300d0` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00a300d4"></a> `00a300d4` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00a300d8"></a> `00a300d8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a300dc"></a> `00a300dc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a300e0"></a> `00a300e0` | `21 06 00 54` | b.ne 0x00a301a4 | `CONDITIONAL_JUMP`
<a id="insn-00a300e4"></a> `00a300e4` | `60 43 00 91` | add x0,x27,#0x10 | `FALL_THROUGH`
<a id="insn-00a300e8"></a> `00a300e8` | `ef 31 f5 97` | bl 0x0077c8a4 | `UNCONDITIONAL_CALL`
<a id="insn-00a300ec"></a> `00a300ec` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00a300f0"></a> `00a300f0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a300f4"></a> `00a300f4` | `e8 00 00 37` | tbnz w8,#0x0,0x00a30110 | `CONDITIONAL_JUMP`
<a id="insn-00a300f8"></a> `00a300f8` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a300fc"></a> `00a300fc` | `a8 01 00 37` | tbnz w8,#0x0,0x00a30130 | `CONDITIONAL_JUMP`
<a id="insn-00a30100"></a> `00a30100` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a30104"></a> `00a30104` | `68 02 00 37` | tbnz w8,#0x0,0x00a30150 | `CONDITIONAL_JUMP`
<a id="insn-00a30108"></a> `00a30108` | `16 03 00 b5` | cbnz x22,0x00a30168 | `CONDITIONAL_JUMP`
<a id="insn-00a3010c"></a> `00a3010c` | `1f 00 00 14` | b 0x00a30188 | `UNCONDITIONAL_JUMP`
<a id="insn-00a30110"></a> `00a30110` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00a30114"></a> `00a30114` | `9b 9f 08 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a30118"></a> `00a30118` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3011c"></a> `00a3011c` | `28 ff 07 36` | tbz w8,#0x0,0x00a30100 | `CONDITIONAL_JUMP`
<a id="insn-00a30120"></a> `00a30120` | `04 00 00 14` | b 0x00a30130 | `UNCONDITIONAL_JUMP`
<a id="insn-00a30130"></a> `00a30130` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a30134"></a> `00a30134` | `93 9f 08 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a30138"></a> `00a30138` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a3013c"></a> `00a3013c` | `68 fe 07 36` | tbz w8,#0x0,0x00a30108 | `CONDITIONAL_JUMP`
<a id="insn-00a30140"></a> `00a30140` | `04 00 00 14` | b 0x00a30150 | `UNCONDITIONAL_JUMP`
<a id="insn-00a30150"></a> `00a30150` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a30154"></a> `00a30154` | `8b 9f 08 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a30158"></a> `00a30158` | `96 00 00 b5` | cbnz x22,0x00a30168 | `CONDITIONAL_JUMP`
<a id="insn-00a3015c"></a> `00a3015c` | `0b 00 00 14` | b 0x00a30188 | `UNCONDITIONAL_JUMP`
<a id="insn-00a30168"></a> `00a30168` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00a3016c"></a> `00a3016c` | `06 00 00 14` | b 0x00a30184 | `UNCONDITIONAL_JUMP`
<a id="insn-00a30184"></a> `00a30184` | `7f 9f 08 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a30188"></a> `00a30188` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00a3018c"></a> `00a3018c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00a30190"></a> `00a30190` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a30194"></a> `00a30194` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a30198"></a> `00a30198` | `61 00 00 54` | b.ne 0x00a301a4 | `CONDITIONAL_JUMP`
<a id="insn-00a3019c"></a> `00a3019c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a301a0"></a> `00a301a0` | `97 8f 08 94` | bl 0x00c53ffc | `CALL_TERMINATOR`
<a id="insn-00a301a4"></a> `00a301a4` | `83 9f 08 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a2fedc`](#insn-00a2fedc) 範囲 `[['00a2fedc', '00a2ff1b']]`
  - `CONDITIONAL_JUMP` [`00a2ff18`](#insn-00a2ff18) → [`00a3008c`](#insn-00a3008c)
  - `FALL_THROUGH` [`00a2ff18`](#insn-00a2ff18) → [`00a2ff1c`](#insn-00a2ff1c)
- ブロック [`00a2ff1c`](#insn-00a2ff1c) 範囲 `[['00a2ff1c', '00a2ff33']]`
  - `UNCONDITIONAL_JUMP` [`00a2ff30`](#insn-00a2ff30) → [`00a2ff40`](#insn-00a2ff40)
- ブロック [`00a2ff34`](#insn-00a2ff34) 範囲 `[['00a2ff34', '00a2ff3f']]`
  - `CONDITIONAL_JUMP` [`00a2ff3c`](#insn-00a2ff3c) → [`00a30098`](#insn-00a30098)
  - `FALL_THROUGH` [`00a2ff3c`](#insn-00a2ff3c) → [`00a2ff40`](#insn-00a2ff40)
- ブロック [`00a2ff40`](#insn-00a2ff40) 範囲 `[['00a2ff40', '00a2ff63']]`
  - `CONDITIONAL_JUMP` [`00a2ff60`](#insn-00a2ff60) → [`00a2ffa8`](#insn-00a2ffa8)
  - `FALL_THROUGH` [`00a2ff60`](#insn-00a2ff60) → [`00a2ff64`](#insn-00a2ff64)
- ブロック [`00a2ff64`](#insn-00a2ff64) 範囲 `[['00a2ff64', '00a2ff7b']]`
  - `CONDITIONAL_JUMP` [`00a2ff78`](#insn-00a2ff78) → [`00a300d0`](#insn-00a300d0)
  - `FALL_THROUGH` [`00a2ff78`](#insn-00a2ff78) → [`00a2ff7c`](#insn-00a2ff7c)
- ブロック [`00a2ff7c`](#insn-00a2ff7c) 範囲 `[['00a2ff7c', '00a2ff9b']]`
  - `CONDITIONAL_JUMP` [`00a2ff98`](#insn-00a2ff98) → [`00a2ffb0`](#insn-00a2ffb0)
  - `FALL_THROUGH` [`00a2ff98`](#insn-00a2ff98) → [`00a2ff9c`](#insn-00a2ff9c)
- ブロック [`00a2ff9c`](#insn-00a2ff9c) 範囲 `[['00a2ff9c', '00a2ffa3']]`
  - `CONDITIONAL_JUMP` [`00a2ffa0`](#insn-00a2ffa0) → [`00a30020`](#insn-00a30020)
  - `FALL_THROUGH` [`00a2ffa0`](#insn-00a2ffa0) → [`00a2ffa4`](#insn-00a2ffa4)
- ブロック [`00a2ffa4`](#insn-00a2ffa4) 範囲 `[['00a2ffa4', '00a2ffa7']]`
  - `UNCONDITIONAL_JUMP` [`00a2ffa4`](#insn-00a2ffa4) → [`00a30028`](#insn-00a30028)
- ブロック [`00a2ffa8`](#insn-00a2ffa8) 範囲 `[['00a2ffa8', '00a2ffaf']]`
  - `CONDITIONAL_JUMP` [`00a2ffac`](#insn-00a2ffac) → [`00a2ff9c`](#insn-00a2ff9c)
  - `FALL_THROUGH` [`00a2ffac`](#insn-00a2ffac) → [`00a2ffb0`](#insn-00a2ffb0)
- ブロック [`00a2ffb0`](#insn-00a2ffb0) 範囲 `[['00a2ffb0', '00a3000b']]`
  - `CONDITIONAL_JUMP` [`00a30008`](#insn-00a30008) → [`00a3005c`](#insn-00a3005c)
  - `FALL_THROUGH` [`00a30008`](#insn-00a30008) → [`00a3000c`](#insn-00a3000c)
- ブロック [`00a3000c`](#insn-00a3000c) 範囲 `[['00a3000c', '00a30013']]`
  - `CONDITIONAL_JUMP` [`00a30010`](#insn-00a30010) → [`00a3006c`](#insn-00a3006c)
  - `FALL_THROUGH` [`00a30010`](#insn-00a30010) → [`00a30014`](#insn-00a30014)
- ブロック [`00a30014`](#insn-00a30014) 範囲 `[['00a30014', '00a3001b']]`
  - `CONDITIONAL_JUMP` [`00a30018`](#insn-00a30018) → [`00a3007c`](#insn-00a3007c)
  - `FALL_THROUGH` [`00a30018`](#insn-00a30018) → [`00a3001c`](#insn-00a3001c)
- ブロック [`00a3001c`](#insn-00a3001c) 範囲 `[['00a3001c', '00a3001f']]`
  - `CONDITIONAL_JUMP` [`00a3001c`](#insn-00a3001c) → [`00a30028`](#insn-00a30028)
  - `FALL_THROUGH` [`00a3001c`](#insn-00a3001c) → [`00a30020`](#insn-00a30020)
- ブロック [`00a30020`](#insn-00a30020) 範囲 `[['00a30020', '00a30027']]`
  - `FALL_THROUGH` [`00a30024`](#insn-00a30024) → [`00a30028`](#insn-00a30028)
- ブロック [`00a30028`](#insn-00a30028) 範囲 `[['00a30028', '00a3002b']]`
  - `CONDITIONAL_JUMP` [`00a30028`](#insn-00a30028) → [`00a30094`](#insn-00a30094)
  - `FALL_THROUGH` [`00a30028`](#insn-00a30028) → [`00a3002c`](#insn-00a3002c)
- ブロック [`00a3002c`](#insn-00a3002c) 範囲 `[['00a3002c', '00a30033']]`
  - `CONDITIONAL_JUMP` [`00a30030`](#insn-00a30030) → [`00a30044`](#insn-00a30044)
  - `FALL_THROUGH` [`00a30030`](#insn-00a30030) → [`00a30034`](#insn-00a30034)
- ブロック [`00a30034`](#insn-00a30034) 範囲 `[['00a30034', '00a3003f']]`
  - `CONDITIONAL_JUMP` [`00a3003c`](#insn-00a3003c) → [`00a30034`](#insn-00a30034)
  - `FALL_THROUGH` [`00a3003c`](#insn-00a3003c) → [`00a30040`](#insn-00a30040)
- ブロック [`00a30040`](#insn-00a30040) 範囲 `[['00a30040', '00a30043']]`
  - `UNCONDITIONAL_JUMP` [`00a30040`](#insn-00a30040) → [`00a2ff34`](#insn-00a2ff34)
- ブロック [`00a30044`](#insn-00a30044) 範囲 `[['00a30044', '00a30057']]`
  - `CONDITIONAL_JUMP` [`00a30054`](#insn-00a30054) → [`00a30044`](#insn-00a30044)
  - `FALL_THROUGH` [`00a30054`](#insn-00a30054) → [`00a30058`](#insn-00a30058)
- ブロック [`00a30058`](#insn-00a30058) 範囲 `[['00a30058', '00a3005b']]`
  - `UNCONDITIONAL_JUMP` [`00a30058`](#insn-00a30058) → [`00a2ff34`](#insn-00a2ff34)
- ブロック [`00a3005c`](#insn-00a3005c) 範囲 `[['00a3005c', '00a3006b']]`
  - `CONDITIONAL_JUMP` [`00a30068`](#insn-00a30068) → [`00a30014`](#insn-00a30014)
  - `FALL_THROUGH` [`00a30068`](#insn-00a30068) → [`00a3006c`](#insn-00a3006c)
- ブロック [`00a3006c`](#insn-00a3006c) 範囲 `[['00a3006c', '00a3007b']]`
  - `CONDITIONAL_JUMP` [`00a30078`](#insn-00a30078) → [`00a3001c`](#insn-00a3001c)
  - `FALL_THROUGH` [`00a30078`](#insn-00a30078) → [`00a3007c`](#insn-00a3007c)
- ブロック [`00a3007c`](#insn-00a3007c) 範囲 `[['00a3007c', '00a30087']]`
  - `CONDITIONAL_JUMP` [`00a30084`](#insn-00a30084) → [`00a30020`](#insn-00a30020)
  - `FALL_THROUGH` [`00a30084`](#insn-00a30084) → [`00a30088`](#insn-00a30088)
- ブロック [`00a30088`](#insn-00a30088) 範囲 `[['00a30088', '00a3008b']]`
  - `UNCONDITIONAL_JUMP` [`00a30088`](#insn-00a30088) → [`00a30028`](#insn-00a30028)
- ブロック [`00a3008c`](#insn-00a3008c) 範囲 `[['00a3008c', '00a30093']]`
  - `UNCONDITIONAL_JUMP` [`00a30090`](#insn-00a30090) → [`00a30098`](#insn-00a30098)
- ブロック [`00a30094`](#insn-00a30094) 範囲 `[['00a30094', '00a30097']]`
  - `FALL_THROUGH` [`00a30094`](#insn-00a30094) → [`00a30098`](#insn-00a30098)
- ブロック [`00a30098`](#insn-00a30098) 範囲 `[['00a30098', '00a300ab']]`
  - `CONDITIONAL_JUMP` [`00a300a8`](#insn-00a300a8) → [`00a301a4`](#insn-00a301a4)
  - `FALL_THROUGH` [`00a300a8`](#insn-00a300a8) → [`00a300ac`](#insn-00a300ac)
- ブロック [`00a300ac`](#insn-00a300ac) 範囲 `[['00a300ac', '00a300cf']]`
- ブロック [`00a300d0`](#insn-00a300d0) 範囲 `[['00a300d0', '00a300e3']]`
  - `CONDITIONAL_JUMP` [`00a300e0`](#insn-00a300e0) → [`00a301a4`](#insn-00a301a4)
  - `FALL_THROUGH` [`00a300e0`](#insn-00a300e0) → [`00a300e4`](#insn-00a300e4)
- ブロック [`00a300e4`](#insn-00a300e4) 範囲 `[['00a300e4', '00a300f7']]`
  - `CONDITIONAL_JUMP` [`00a300f4`](#insn-00a300f4) → [`00a30110`](#insn-00a30110)
  - `FALL_THROUGH` [`00a300f4`](#insn-00a300f4) → [`00a300f8`](#insn-00a300f8)
- ブロック [`00a300f8`](#insn-00a300f8) 範囲 `[['00a300f8', '00a300ff']]`
  - `CONDITIONAL_JUMP` [`00a300fc`](#insn-00a300fc) → [`00a30130`](#insn-00a30130)
  - `FALL_THROUGH` [`00a300fc`](#insn-00a300fc) → [`00a30100`](#insn-00a30100)
- ブロック [`00a30100`](#insn-00a30100) 範囲 `[['00a30100', '00a30107']]`
  - `CONDITIONAL_JUMP` [`00a30104`](#insn-00a30104) → [`00a30150`](#insn-00a30150)
  - `FALL_THROUGH` [`00a30104`](#insn-00a30104) → [`00a30108`](#insn-00a30108)
- ブロック [`00a30108`](#insn-00a30108) 範囲 `[['00a30108', '00a3010b']]`
  - `CONDITIONAL_JUMP` [`00a30108`](#insn-00a30108) → [`00a30168`](#insn-00a30168)
  - `FALL_THROUGH` [`00a30108`](#insn-00a30108) → [`00a3010c`](#insn-00a3010c)
- ブロック [`00a3010c`](#insn-00a3010c) 範囲 `[['00a3010c', '00a3010f']]`
  - `UNCONDITIONAL_JUMP` [`00a3010c`](#insn-00a3010c) → [`00a30188`](#insn-00a30188)
- ブロック [`00a30110`](#insn-00a30110) 範囲 `[['00a30110', '00a3011f']]`
  - `CONDITIONAL_JUMP` [`00a3011c`](#insn-00a3011c) → [`00a30100`](#insn-00a30100)
  - `FALL_THROUGH` [`00a3011c`](#insn-00a3011c) → [`00a30120`](#insn-00a30120)
- ブロック [`00a30120`](#insn-00a30120) 範囲 `[['00a30120', '00a30123']]`
  - `UNCONDITIONAL_JUMP` [`00a30120`](#insn-00a30120) → [`00a30130`](#insn-00a30130)
- ブロック [`00a30130`](#insn-00a30130) 範囲 `[['00a30130', '00a3013f']]`
  - `CONDITIONAL_JUMP` [`00a3013c`](#insn-00a3013c) → [`00a30108`](#insn-00a30108)
  - `FALL_THROUGH` [`00a3013c`](#insn-00a3013c) → [`00a30140`](#insn-00a30140)
- ブロック [`00a30140`](#insn-00a30140) 範囲 `[['00a30140', '00a30143']]`
  - `UNCONDITIONAL_JUMP` [`00a30140`](#insn-00a30140) → [`00a30150`](#insn-00a30150)
- ブロック [`00a30150`](#insn-00a30150) 範囲 `[['00a30150', '00a3015b']]`
  - `CONDITIONAL_JUMP` [`00a30158`](#insn-00a30158) → [`00a30168`](#insn-00a30168)
  - `FALL_THROUGH` [`00a30158`](#insn-00a30158) → [`00a3015c`](#insn-00a3015c)
- ブロック [`00a3015c`](#insn-00a3015c) 範囲 `[['00a3015c', '00a3015f']]`
  - `UNCONDITIONAL_JUMP` [`00a3015c`](#insn-00a3015c) → [`00a30188`](#insn-00a30188)
- ブロック [`00a30168`](#insn-00a30168) 範囲 `[['00a30168', '00a3016f']]`
  - `UNCONDITIONAL_JUMP` [`00a3016c`](#insn-00a3016c) → [`00a30184`](#insn-00a30184)
- ブロック [`00a30184`](#insn-00a30184) 範囲 `[['00a30184', '00a30187']]`
  - `FALL_THROUGH` [`00a30184`](#insn-00a30184) → [`00a30188`](#insn-00a30188)
- ブロック [`00a30188`](#insn-00a30188) 範囲 `[['00a30188', '00a3019b']]`
  - `CONDITIONAL_JUMP` [`00a30198`](#insn-00a30198) → [`00a301a4`](#insn-00a301a4)
  - `FALL_THROUGH` [`00a30198`](#insn-00a30198) → [`00a3019c`](#insn-00a3019c)
- ブロック [`00a3019c`](#insn-00a3019c) 範囲 `[['00a3019c', '00a301a3']]`
- ブロック [`00a301a4`](#insn-00a301a4) 範囲 `[['00a301a4', '00a301a7']]`

## 命令位置別の参照

- [`00a2fee0`](#insn-00a2fee0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2fee4`](#insn-00a2fee4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2fee8`](#insn-00a2fee8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2feec`](#insn-00a2feec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2fef0`](#insn-00a2fef0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2fef4`](#insn-00a2fef4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff04`](#insn-00a2ff04) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff0c`](#insn-00a2ff0c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff18`](#insn-00a2ff18) → [`00a3008c`](#insn-00a3008c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff30`](#insn-00a2ff30) → [`00a2ff40`](#insn-00a2ff40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff3c`](#insn-00a2ff3c) → [`00a30098`](#insn-00a30098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff4c`](#insn-00a2ff4c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff50`](#insn-00a2ff50) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff58`](#insn-00a2ff58) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff5c`](#insn-00a2ff5c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff60`](#insn-00a2ff60) → [`00a2ffa8`](#insn-00a2ffa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff78`](#insn-00a2ff78) → [`00a300d0`](#insn-00a300d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff80`](#insn-00a2ff80) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff90`](#insn-00a2ff90) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff94`](#insn-00a2ff94) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00a2ff98`](#insn-00a2ff98) → [`00a2ffb0`](#insn-00a2ffb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ffa0`](#insn-00a2ffa0) → [`00a30020`](#insn-00a30020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ffa4`](#insn-00a2ffa4) → [`00a30028`](#insn-00a30028) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ffac`](#insn-00a2ffac) → [`00a2ff9c`](#insn-00a2ff9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ffb8`](#insn-00a2ffb8) → [`00c58020`](../00c58/00c58020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58020` · 推定シンボル `None` · 推定型 `None`
- [`00a2ffc8`](#insn-00a2ffc8) → `002bb75d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a2ffcc`](#insn-00a2ffcc) → [`00c58030`](../00c58/00c58030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58030` · 推定シンボル `None` · 推定型 `None`
- [`00a2ffd8`](#insn-00a2ffd8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ffdc`](#insn-00a2ffdc) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2fff0`](#insn-00a2fff0) → [`0048ce94`](../0048c/0048ce94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce94` · 推定シンボル `None` · 推定型 `None`
- [`00a2fffc`](#insn-00a2fffc) → [`004939d8`](../00493/004939d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004939d8` · 推定シンボル `None` · 推定型 `None`
- [`00a30000`](#insn-00a30000) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30008`](#insn-00a30008) → [`00a3005c`](#insn-00a3005c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3000c`](#insn-00a3000c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30010`](#insn-00a30010) → [`00a3006c`](#insn-00a3006c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30014`](#insn-00a30014) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30018`](#insn-00a30018) → [`00a3007c`](#insn-00a3007c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3001c`](#insn-00a3001c) → [`00a30028`](#insn-00a30028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30024`](#insn-00a30024) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a30028`](#insn-00a30028) → [`00a30094`](#insn-00a30094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30030`](#insn-00a30030) → [`00a30044`](#insn-00a30044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3003c`](#insn-00a3003c) → [`00a30034`](#insn-00a30034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30040`](#insn-00a30040) → [`00a2ff34`](#insn-00a2ff34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30054`](#insn-00a30054) → [`00a30044`](#insn-00a30044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30058`](#insn-00a30058) → [`00a2ff34`](#insn-00a2ff34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3005c`](#insn-00a3005c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30060`](#insn-00a30060) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a30064`](#insn-00a30064) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30068`](#insn-00a30068) → [`00a30014`](#insn-00a30014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3006c`](#insn-00a3006c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30070`](#insn-00a30070) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a30074`](#insn-00a30074) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30078`](#insn-00a30078) → [`00a3001c`](#insn-00a3001c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3007c`](#insn-00a3007c) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30080`](#insn-00a30080) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a30084`](#insn-00a30084) → [`00a30020`](#insn-00a30020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30088`](#insn-00a30088) → [`00a30028`](#insn-00a30028) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30090`](#insn-00a30090) → [`00a30098`](#insn-00a30098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30098`](#insn-00a30098) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300a0`](#insn-00a300a0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300a8`](#insn-00a300a8) → [`00a301a4`](#insn-00a301a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300b0`](#insn-00a300b0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300b4`](#insn-00a300b4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300b8`](#insn-00a300b8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300bc`](#insn-00a300bc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300c0`](#insn-00a300c0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300c4`](#insn-00a300c4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300d0`](#insn-00a300d0) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300d8`](#insn-00a300d8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300e0`](#insn-00a300e0) → [`00a301a4`](#insn-00a301a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300e8`](#insn-00a300e8) → [`0077c8a4`](../0077c/0077c8a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0077c8a4` · 推定シンボル `None` · 推定型 `None`
- [`00a300ec`](#insn-00a300ec) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300f4`](#insn-00a300f4) → [`00a30110`](#insn-00a30110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300f8`](#insn-00a300f8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a300fc`](#insn-00a300fc) → [`00a30130`](#insn-00a30130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30100`](#insn-00a30100) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30104`](#insn-00a30104) → [`00a30150`](#insn-00a30150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30108`](#insn-00a30108) → [`00a30168`](#insn-00a30168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3010c`](#insn-00a3010c) → [`00a30188`](#insn-00a30188) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30110`](#insn-00a30110) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30114`](#insn-00a30114) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a30118`](#insn-00a30118) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3011c`](#insn-00a3011c) → [`00a30100`](#insn-00a30100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30120`](#insn-00a30120) → [`00a30130`](#insn-00a30130) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30130`](#insn-00a30130) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30134`](#insn-00a30134) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a30138`](#insn-00a30138) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3013c`](#insn-00a3013c) → [`00a30108`](#insn-00a30108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30140`](#insn-00a30140) → [`00a30150`](#insn-00a30150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30150`](#insn-00a30150) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30154`](#insn-00a30154) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a30158`](#insn-00a30158) → [`00a30168`](#insn-00a30168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3015c`](#insn-00a3015c) → [`00a30188`](#insn-00a30188) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3016c`](#insn-00a3016c) → [`00a30184`](#insn-00a30184) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30184`](#insn-00a30184) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a30188`](#insn-00a30188) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30190`](#insn-00a30190) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a30198`](#insn-00a30198) → [`00a301a4`](#insn-00a301a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a301a0`](#insn-00a301a0) → [`00c53ffc`](../00c53/00c53ffc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53ffc` · 推定シンボル `None` · 推定型 `None`
- [`00a301a4`](#insn-00a301a4) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a2fee0`](#insn-00a2fee0)

~~~json
{
  "source": "00a2fee0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2fee4`](#insn-00a2fee4)

~~~json
{
  "source": "00a2fee4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2fee8`](#insn-00a2fee8)

~~~json
{
  "source": "00a2fee8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2feec`](#insn-00a2feec)

~~~json
{
  "source": "00a2feec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2fef0`](#insn-00a2fef0)

~~~json
{
  "source": "00a2fef0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2fef4`](#insn-00a2fef4)

~~~json
{
  "source": "00a2fef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff04`](#insn-00a2ff04)

~~~json
{
  "source": "00a2ff04",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff0c`](#insn-00a2ff0c)

~~~json
{
  "source": "00a2ff0c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff18`](#insn-00a2ff18)

~~~json
{
  "source": "00a2ff18",
  "target": "00a3008c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff30`](#insn-00a2ff30)

~~~json
{
  "source": "00a2ff30",
  "target": "00a2ff40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff3c`](#insn-00a2ff3c)

~~~json
{
  "source": "00a2ff3c",
  "target": "00a30098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff4c`](#insn-00a2ff4c)

~~~json
{
  "source": "00a2ff4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff50`](#insn-00a2ff50)

~~~json
{
  "source": "00a2ff50",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff58`](#insn-00a2ff58)

~~~json
{
  "source": "00a2ff58",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff5c`](#insn-00a2ff5c)

~~~json
{
  "source": "00a2ff5c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff60`](#insn-00a2ff60)

~~~json
{
  "source": "00a2ff60",
  "target": "00a2ffa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff78`](#insn-00a2ff78)

~~~json
{
  "source": "00a2ff78",
  "target": "00a300d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff80`](#insn-00a2ff80)

~~~json
{
  "source": "00a2ff80",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2ff90`](#insn-00a2ff90)

~~~json
{
  "source": "00a2ff90",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ff94`](#insn-00a2ff94)

~~~json
{
  "source": "00a2ff94",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2ff98`](#insn-00a2ff98)

~~~json
{
  "source": "00a2ff98",
  "target": "00a2ffb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ffa0`](#insn-00a2ffa0)

~~~json
{
  "source": "00a2ffa0",
  "target": "00a30020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ffa4`](#insn-00a2ffa4)

~~~json
{
  "source": "00a2ffa4",
  "target": "00a30028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ffac`](#insn-00a2ffac)

~~~json
{
  "source": "00a2ffac",
  "target": "00a2ff9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ffb8`](#insn-00a2ffb8)

~~~json
{
  "source": "00a2ffb8",
  "target": "00c58020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2ffc8`](#insn-00a2ffc8)

~~~json
{
  "source": "00a2ffc8",
  "target": "002bb75d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb75d",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "736368656d655f6974656d5f706172616d5f00",
  "capture_start": "002bb75d",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a2ffcc`](#insn-00a2ffcc)

~~~json
{
  "source": "00a2ffcc",
  "target": "00c58030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2ffd8`](#insn-00a2ffd8)

~~~json
{
  "source": "00a2ffd8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ffdc`](#insn-00a2ffdc)

~~~json
{
  "source": "00a2ffdc",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2fff0`](#insn-00a2fff0)

~~~json
{
  "source": "00a2fff0",
  "target": "0048ce94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2fffc`](#insn-00a2fffc)

~~~json
{
  "source": "00a2fffc",
  "target": "004939d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a30000`](#insn-00a30000)

~~~json
{
  "source": "00a30000",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30008`](#insn-00a30008)

~~~json
{
  "source": "00a30008",
  "target": "00a3005c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3000c`](#insn-00a3000c)

~~~json
{
  "source": "00a3000c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30010`](#insn-00a30010)

~~~json
{
  "source": "00a30010",
  "target": "00a3006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30014`](#insn-00a30014)

~~~json
{
  "source": "00a30014",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30018`](#insn-00a30018)

~~~json
{
  "source": "00a30018",
  "target": "00a3007c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3001c`](#insn-00a3001c)

~~~json
{
  "source": "00a3001c",
  "target": "00a30028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30024`](#insn-00a30024)

~~~json
{
  "source": "00a30024",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a30028`](#insn-00a30028)

~~~json
{
  "source": "00a30028",
  "target": "00a30094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30030`](#insn-00a30030)

~~~json
{
  "source": "00a30030",
  "target": "00a30044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3003c`](#insn-00a3003c)

~~~json
{
  "source": "00a3003c",
  "target": "00a30034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30040`](#insn-00a30040)

~~~json
{
  "source": "00a30040",
  "target": "00a2ff34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30054`](#insn-00a30054)

~~~json
{
  "source": "00a30054",
  "target": "00a30044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30058`](#insn-00a30058)

~~~json
{
  "source": "00a30058",
  "target": "00a2ff34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3005c`](#insn-00a3005c)

~~~json
{
  "source": "00a3005c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30060`](#insn-00a30060)

~~~json
{
  "source": "00a30060",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a30064`](#insn-00a30064)

~~~json
{
  "source": "00a30064",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30068`](#insn-00a30068)

~~~json
{
  "source": "00a30068",
  "target": "00a30014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3006c`](#insn-00a3006c)

~~~json
{
  "source": "00a3006c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30070`](#insn-00a30070)

~~~json
{
  "source": "00a30070",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a30074`](#insn-00a30074)

~~~json
{
  "source": "00a30074",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30078`](#insn-00a30078)

~~~json
{
  "source": "00a30078",
  "target": "00a3001c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3007c`](#insn-00a3007c)

~~~json
{
  "source": "00a3007c",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30080`](#insn-00a30080)

~~~json
{
  "source": "00a30080",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a30084`](#insn-00a30084)

~~~json
{
  "source": "00a30084",
  "target": "00a30020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30088`](#insn-00a30088)

~~~json
{
  "source": "00a30088",
  "target": "00a30028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30090`](#insn-00a30090)

~~~json
{
  "source": "00a30090",
  "target": "00a30098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30098`](#insn-00a30098)

~~~json
{
  "source": "00a30098",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300a0`](#insn-00a300a0)

~~~json
{
  "source": "00a300a0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300a8`](#insn-00a300a8)

~~~json
{
  "source": "00a300a8",
  "target": "00a301a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300b0`](#insn-00a300b0)

~~~json
{
  "source": "00a300b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300b4`](#insn-00a300b4)

~~~json
{
  "source": "00a300b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300b8`](#insn-00a300b8)

~~~json
{
  "source": "00a300b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300bc`](#insn-00a300bc)

~~~json
{
  "source": "00a300bc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300c0`](#insn-00a300c0)

~~~json
{
  "source": "00a300c0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300c4`](#insn-00a300c4)

~~~json
{
  "source": "00a300c4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300d0`](#insn-00a300d0)

~~~json
{
  "source": "00a300d0",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300d8`](#insn-00a300d8)

~~~json
{
  "source": "00a300d8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300e0`](#insn-00a300e0)

~~~json
{
  "source": "00a300e0",
  "target": "00a301a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300e8`](#insn-00a300e8)

~~~json
{
  "source": "00a300e8",
  "target": "0077c8a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a300ec`](#insn-00a300ec)

~~~json
{
  "source": "00a300ec",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300f4`](#insn-00a300f4)

~~~json
{
  "source": "00a300f4",
  "target": "00a30110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300f8`](#insn-00a300f8)

~~~json
{
  "source": "00a300f8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a300fc`](#insn-00a300fc)

~~~json
{
  "source": "00a300fc",
  "target": "00a30130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30100`](#insn-00a30100)

~~~json
{
  "source": "00a30100",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30104`](#insn-00a30104)

~~~json
{
  "source": "00a30104",
  "target": "00a30150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30108`](#insn-00a30108)

~~~json
{
  "source": "00a30108",
  "target": "00a30168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3010c`](#insn-00a3010c)

~~~json
{
  "source": "00a3010c",
  "target": "00a30188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30110`](#insn-00a30110)

~~~json
{
  "source": "00a30110",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30114`](#insn-00a30114)

~~~json
{
  "source": "00a30114",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a30118`](#insn-00a30118)

~~~json
{
  "source": "00a30118",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3011c`](#insn-00a3011c)

~~~json
{
  "source": "00a3011c",
  "target": "00a30100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30120`](#insn-00a30120)

~~~json
{
  "source": "00a30120",
  "target": "00a30130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30130`](#insn-00a30130)

~~~json
{
  "source": "00a30130",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30134`](#insn-00a30134)

~~~json
{
  "source": "00a30134",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a30138`](#insn-00a30138)

~~~json
{
  "source": "00a30138",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3013c`](#insn-00a3013c)

~~~json
{
  "source": "00a3013c",
  "target": "00a30108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30140`](#insn-00a30140)

~~~json
{
  "source": "00a30140",
  "target": "00a30150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30150`](#insn-00a30150)

~~~json
{
  "source": "00a30150",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30154`](#insn-00a30154)

~~~json
{
  "source": "00a30154",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a30158`](#insn-00a30158)

~~~json
{
  "source": "00a30158",
  "target": "00a30168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3015c`](#insn-00a3015c)

~~~json
{
  "source": "00a3015c",
  "target": "00a30188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3016c`](#insn-00a3016c)

~~~json
{
  "source": "00a3016c",
  "target": "00a30184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30184`](#insn-00a30184)

~~~json
{
  "source": "00a30184",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a30188`](#insn-00a30188)

~~~json
{
  "source": "00a30188",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30190`](#insn-00a30190)

~~~json
{
  "source": "00a30190",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a30198`](#insn-00a30198)

~~~json
{
  "source": "00a30198",
  "target": "00a301a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a301a0`](#insn-00a301a0)

~~~json
{
  "source": "00a301a0",
  "target": "00c53ffc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a301a4`](#insn-00a301a4)

~~~json
{
  "source": "00a301a4",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
