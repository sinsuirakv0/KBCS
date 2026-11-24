# 00a6abac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a69bb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a69/00a69bb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0063.md#compare-071bde8df828d5ecd6f7377184a3739f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6abac",
  "name": "FUN_00a6abac",
  "size": 560,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a2a70b6e12e66984c3afbbfafafff76165e920637ea8c93b7c2a4e314ede6f9f",
  "source_text_sha256": "a2a70b6e12e66984c3afbbfafafff76165e920637ea8c93b7c2a4e314ede6f9f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6abac",
        "00a6add7"
      ],
      [
        "00a6adfc",
        "00a6adff"
      ]
    ],
    "bytes_sha256": "6ac65566422aed77acc042c47200b4fead939e8923b2fa0734fad9a47770afd1",
    "instruction_count": 140,
    "instruction_bytes": 560,
    "body_bytes": 560,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00a6bf90](../00a6b/00a6bf90.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [00442c90](../00442/00442c90.md)
- [00a69d4c](../00a69/00a69d4c.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2721 bytes

~~~c

/* WARNING: Removing unreachable block (ram,0x00a6ad28) */
/* WARNING: Removing unreachable block (ram,0x00a6ad38) */

void FUN_00a6abac(long *param_1,int param_2,undefined4 param_3,undefined4 param_4,undefined4 param_5
                 )

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  long lVar4;
  long lVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  long *plVar9;
  
  lVar1 = tpidr_el0;
  lVar5 = *(long *)(lVar1 + 0x28);
  plVar8 = param_1 + 1;
  plVar7 = (long *)*plVar8;
  for (plVar6 = plVar7; plVar6 != (long *)0x0; plVar6 = (long *)*plVar6) {
    if ((int)plVar6[4] <= param_2) {
      if (param_2 <= (int)plVar6[4]) goto joined_r0x00a6ad54;
      plVar6 = plVar6 + 1;
    }
  }
  puVar2 = (undefined8 *)_Znwm(0x38);
  *puVar2 = &PTR_FUN_00c8c9a0;
  puVar2[1] = 0;
  puVar2[2] = 0;
  puVar2[4] = 0;
  puVar2[3] = 0;
  puVar2[6] = 0;
  puVar2[5] = 0;
  puVar2[4] = puVar2 + 5;
  plVar6 = plVar8;
  while (plVar9 = plVar6, plVar7 != (long *)0x0) {
    while (plVar3 = plVar7, plVar6 = plVar3, (int)plVar3[4] <= param_2) {
      if (param_2 <= (int)plVar3[4]) goto LAB_00a6ace8;
      plVar7 = (long *)plVar3[1];
      if ((long *)plVar3[1] == (long *)0x0) {
        plVar9 = plVar3 + 1;
        goto LAB_00a6ac90;
      }
    }
    plVar7 = (long *)*plVar3;
  }
LAB_00a6ac90:
  plVar3 = (long *)_Znwm(0x38);
  plVar3[5] = 0;
  plVar3[6] = 0;
  *plVar3 = 0;
  plVar3[1] = 0;
  plVar3[2] = (long)plVar6;
  *plVar9 = (long)plVar3;
  plVar7 = (long *)*param_1;
  *(int *)(plVar3 + 4) = param_2;
  plVar6 = plVar3;
  if (*plVar7 != 0) {
    *param_1 = *plVar7;
    plVar6 = (long *)*plVar9;
  }
  FUN_0043bf04(param_1[1],plVar6);
  param_1[2] = param_1[2] + 1;
LAB_00a6ace8:
  plVar6 = (long *)plVar3[6];
  plVar3[5] = (long)(puVar2 + 3);
  plVar3[6] = (long)puVar2;
  if ((plVar6 != (long *)0x0) && (lVar4 = FUN_00c54d90(0xffffffffffffffff,plVar6 + 1), lVar4 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = (long *)*plVar8;
joined_r0x00a6ad54:
  do {
    if (plVar7 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == lVar5) {
                    /* WARNING: Subroutine does not return */
        FUN_00442c90("map::at:  key not found");
      }
LAB_00a6adfc:
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    if (param_2 < (int)plVar7[4]) {
      plVar7 = (long *)*plVar7;
      goto joined_r0x00a6ad54;
    }
    if (param_2 <= (int)plVar7[4]) {
      if (*(long *)(lVar1 + 0x28) == lVar5) {
        FUN_00a69d4c(plVar7[5],param_3,param_4,param_5);
        return;
      }
      goto LAB_00a6adfc;
    }
    plVar7 = (long *)plVar7[1];
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a6abac"></a> `00a6abac` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00a6abb0"></a> `00a6abb0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6abb4"></a> `00a6abb4` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6abb8"></a> `00a6abb8` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6abbc"></a> `00a6abbc` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a6abc0"></a> `00a6abc0` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a6abc4"></a> `00a6abc4` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a6abc8"></a> `00a6abc8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00a6abcc"></a> `00a6abcc` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a6abd0"></a> `00a6abd0` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00a6abd4"></a> `00a6abd4` | `f3 03 04 2a` | mov w19,w4 | `FALL_THROUGH`
<a id="insn-00a6abd8"></a> `00a6abd8` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00a6abdc"></a> `00a6abdc` | `f4 03 03 2a` | mov w20,w3 | `FALL_THROUGH`
<a id="insn-00a6abe0"></a> `00a6abe0` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00a6abe4"></a> `00a6abe4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00a6abe8"></a> `00a6abe8` | `f6 03 01 2a` | mov w22,w1 | `FALL_THROUGH`
<a id="insn-00a6abec"></a> `00a6abec` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a6abf0"></a> `00a6abf0` | `58 8f 40 f8` | ldr x24,[x26, #0x8]! | `FALL_THROUGH`
<a id="insn-00a6abf4"></a> `00a6abf4` | `78 01 00 b4` | cbz x24,0x00a6ac20 | `CONDITIONAL_JUMP`
<a id="insn-00a6abf8"></a> `00a6abf8` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00a6abfc"></a> `00a6abfc` | `03 00 00 14` | b 0x00a6ac08 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6ac00"></a> `00a6ac00` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a6ac04"></a> `00a6ac04` | `e8 00 00 b4` | cbz x8,0x00a6ac20 | `CONDITIONAL_JUMP`
<a id="insn-00a6ac08"></a> `00a6ac08` | `09 21 40 b9` | ldr w9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00a6ac0c"></a> `00a6ac0c` | `3f 01 16 6b` | cmp w9,w22 | `FALL_THROUGH`
<a id="insn-00a6ac10"></a> `00a6ac10` | `8c ff ff 54` | b.gt 0x00a6ac00 | `CONDITIONAL_JUMP`
<a id="insn-00a6ac14"></a> `00a6ac14` | `0a 0a 00 54` | b.ge 0x00a6ad54 | `CONDITIONAL_JUMP`
<a id="insn-00a6ac18"></a> `00a6ac18` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00a6ac1c"></a> `00a6ac1c` | `f9 ff ff 17` | b 0x00a6ac00 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6ac20"></a> `00a6ac20` | `00 07 80 52` | mov w0,#0x38 | `FALL_THROUGH`
<a id="insn-00a6ac24"></a> `00a6ac24` | `c3 b8 07 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ac28"></a> `00a6ac28` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00a6ac2c"></a> `00a6ac2c` | `08 11 00 d0` | adrp x8,0xc8c000 | `FALL_THROUGH`
<a id="insn-00a6ac30"></a> `00a6ac30` | `08 81 26 91` | add x8,x8,#0x9a0 | `FALL_THROUGH`
<a id="insn-00a6ac34"></a> `00a6ac34` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00a6ac38"></a> `00a6ac38` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00a6ac3c"></a> `00a6ac3c` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00a6ac40"></a> `00a6ac40` | `fc 03 1a aa` | mov x28,x26 | `FALL_THROUGH`
<a id="insn-00a6ac44"></a> `00a6ac44` | `fb 03 1a aa` | mov x27,x26 | `FALL_THROUGH`
<a id="insn-00a6ac48"></a> `00a6ac48` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a6ac4c"></a> `00a6ac4c` | `00 8d 81 3c` | str q0,[x8, #0x18]! | `FALL_THROUGH`
<a id="insn-00a6ac50"></a> `00a6ac50` | `20 8d 82 3c` | str q0,[x9, #0x28]! | `FALL_THROUGH`
<a id="insn-00a6ac54"></a> `00a6ac54` | `09 10 00 f9` | str x9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00a6ac58"></a> `00a6ac58` | `e8 83 00 a9` | stp x8,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6ac5c"></a> `00a6ac5c` | `b8 00 00 b5` | cbnz x24,0x00a6ac70 | `CONDITIONAL_JUMP`
<a id="insn-00a6ac60"></a> `00a6ac60` | `0c 00 00 14` | b 0x00a6ac90 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6ac64"></a> `00a6ac64` | `78 03 40 f9` | ldr x24,[x27] | `FALL_THROUGH`
<a id="insn-00a6ac68"></a> `00a6ac68` | `fc 03 1b aa` | mov x28,x27 | `FALL_THROUGH`
<a id="insn-00a6ac6c"></a> `00a6ac6c` | `38 01 00 b4` | cbz x24,0x00a6ac90 | `CONDITIONAL_JUMP`
<a id="insn-00a6ac70"></a> `00a6ac70` | `09 23 40 b9` | ldr w9,[x24, #0x20] | `FALL_THROUGH`
<a id="insn-00a6ac74"></a> `00a6ac74` | `fb 03 18 aa` | mov x27,x24 | `FALL_THROUGH`
<a id="insn-00a6ac78"></a> `00a6ac78` | `3f 01 16 6b` | cmp w9,w22 | `FALL_THROUGH`
<a id="insn-00a6ac7c"></a> `00a6ac7c` | `4c ff ff 54` | b.gt 0x00a6ac64 | `CONDITIONAL_JUMP`
<a id="insn-00a6ac80"></a> `00a6ac80` | `2a 03 00 54` | b.ge 0x00a6ace4 | `CONDITIONAL_JUMP`
<a id="insn-00a6ac84"></a> `00a6ac84` | `78 07 40 f9` | ldr x24,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00a6ac88"></a> `00a6ac88` | `58 ff ff b5` | cbnz x24,0x00a6ac70 | `CONDITIONAL_JUMP`
<a id="insn-00a6ac8c"></a> `00a6ac8c` | `7c 23 00 91` | add x28,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00a6ac90"></a> `00a6ac90` | `00 07 80 52` | mov w0,#0x38 | `FALL_THROUGH`
<a id="insn-00a6ac94"></a> `00a6ac94` | `a7 b8 07 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ac98"></a> `00a6ac98` | `1f fc 02 a9` | stp xzr,xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00a6ac9c"></a> `00a6ac9c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00a6aca0"></a> `00a6aca0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00a6aca4"></a> `00a6aca4` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00a6aca8"></a> `00a6aca8` | `1b 08 00 f9` | str x27,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a6acac"></a> `00a6acac` | `80 03 00 f9` | str x0,[x28] | `FALL_THROUGH`
<a id="insn-00a6acb0"></a> `00a6acb0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00a6acb4"></a> `00a6acb4` | `16 20 00 b9` | str w22,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00a6acb8"></a> `00a6acb8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a6acbc"></a> `00a6acbc` | `68 00 00 b4` | cbz x8,0x00a6acc8 | `CONDITIONAL_JUMP`
<a id="insn-00a6acc0"></a> `00a6acc0` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00a6acc4"></a> `00a6acc4` | `81 03 40 f9` | ldr x1,[x28] | `FALL_THROUGH`
<a id="insn-00a6acc8"></a> `00a6acc8` | `e0 06 40 f9` | ldr x0,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a6accc"></a> `00a6accc` | `8e 44 e7 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-00a6acd0"></a> `00a6acd0` | `e8 0a 40 f9` | ldr x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00a6acd4"></a> `00a6acd4` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00a6acd8"></a> `00a6acd8` | `e8 83 40 a9` | ldp x8,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6acdc"></a> `00a6acdc` | `e9 0a 00 f9` | str x9,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ace0"></a> `00a6ace0` | `02 00 00 14` | b 0x00a6ace8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6ace4"></a> `00a6ace4` | `f8 03 1b aa` | mov x24,x27 | `FALL_THROUGH`
<a id="insn-00a6ace8"></a> `00a6ace8` | `17 1b 40 f9` | ldr x23,[x24, #0x30] | `FALL_THROUGH`
<a id="insn-00a6acec"></a> `00a6acec` | `ff ff 00 a9` | stp xzr,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6acf0"></a> `00a6acf0` | `08 83 02 a9` | stp x8,x0,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00a6acf4"></a> `00a6acf4` | `77 01 00 b4` | cbz x23,0x00a6ad20 | `CONDITIONAL_JUMP`
<a id="insn-00a6acf8"></a> `00a6acf8` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00a6acfc"></a> `00a6acfc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6ad00"></a> `00a6ad00` | `24 a8 07 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad04"></a> `00a6ad04` | `e0 00 00 b5` | cbnz x0,0x00a6ad20 | `CONDITIONAL_JUMP`
<a id="insn-00a6ad08"></a> `00a6ad08` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00a6ad0c"></a> `00a6ad0c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00a6ad10"></a> `00a6ad10` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ad14"></a> `00a6ad14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6ad18"></a> `00a6ad18` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00a6ad1c"></a> `00a6ad1c` | `81 b8 07 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad20"></a> `00a6ad20` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ad24"></a> `00a6ad24` | `77 01 00 b4` | cbz x23,0x00a6ad50 | `CONDITIONAL_JUMP`
<a id="insn-00a6ad28"></a> `00a6ad28` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00a6ad2c"></a> `00a6ad2c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6ad30"></a> `00a6ad30` | `18 a8 07 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad34"></a> `00a6ad34` | `e0 00 00 b5` | cbnz x0,0x00a6ad50 | `CONDITIONAL_JUMP`
<a id="insn-00a6ad38"></a> `00a6ad38` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00a6ad3c"></a> `00a6ad3c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00a6ad40"></a> `00a6ad40` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ad44"></a> `00a6ad44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6ad48"></a> `00a6ad48` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00a6ad4c"></a> `00a6ad4c` | `75 b8 07 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ad50"></a> `00a6ad50` | `58 03 40 f9` | ldr x24,[x26] | `FALL_THROUGH`
<a id="insn-00a6ad54"></a> `00a6ad54` | `98 00 00 b5` | cbnz x24,0x00a6ad64 | `CONDITIONAL_JUMP`
<a id="insn-00a6ad58"></a> `00a6ad58` | `09 00 00 14` | b 0x00a6ad7c | `UNCONDITIONAL_JUMP`
<a id="insn-00a6ad5c"></a> `00a6ad5c` | `18 03 40 f9` | ldr x24,[x24] | `FALL_THROUGH`
<a id="insn-00a6ad60"></a> `00a6ad60` | `f8 00 00 b4` | cbz x24,0x00a6ad7c | `CONDITIONAL_JUMP`
<a id="insn-00a6ad64"></a> `00a6ad64` | `08 23 40 b9` | ldr w8,[x24, #0x20] | `FALL_THROUGH`
<a id="insn-00a6ad68"></a> `00a6ad68` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00a6ad6c"></a> `00a6ad6c` | `8c ff ff 54` | b.gt 0x00a6ad5c | `CONDITIONAL_JUMP`
<a id="insn-00a6ad70"></a> `00a6ad70` | `4a 01 00 54` | b.ge 0x00a6ad98 | `CONDITIONAL_JUMP`
<a id="insn-00a6ad74"></a> `00a6ad74` | `18 07 40 f9` | ldr x24,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00a6ad78"></a> `00a6ad78` | `78 ff ff b5` | cbnz x24,0x00a6ad64 | `CONDITIONAL_JUMP`
<a id="insn-00a6ad7c"></a> `00a6ad7c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00a6ad80"></a> `00a6ad80` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a6ad84"></a> `00a6ad84` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a6ad88"></a> `00a6ad88` | `a1 03 00 54` | b.ne 0x00a6adfc | `CONDITIONAL_JUMP`
<a id="insn-00a6ad8c"></a> `00a6ad8c` | `a0 c1 ff d0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00a6ad90"></a> `00a6ad90` | `00 c0 06 91` | add x0,x0,#0x1b0 | `FALL_THROUGH`
<a id="insn-00a6ad94"></a> `00a6ad94` | `bf 5f e7 97` | bl 0x00442c90 | `CALL_TERMINATOR`
<a id="insn-00a6ad98"></a> `00a6ad98` | `00 17 40 f9` | ldr x0,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00a6ad9c"></a> `00a6ad9c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00a6ada0"></a> `00a6ada0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a6ada4"></a> `00a6ada4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a6ada8"></a> `00a6ada8` | `a1 02 00 54` | b.ne 0x00a6adfc | `CONDITIONAL_JUMP`
<a id="insn-00a6adac"></a> `00a6adac` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00a6adb0"></a> `00a6adb0` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00a6adb4"></a> `00a6adb4` | `e3 03 13 2a` | mov w3,w19 | `FALL_THROUGH`
<a id="insn-00a6adb8"></a> `00a6adb8` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a6adbc"></a> `00a6adbc` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a6adc0"></a> `00a6adc0` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a6adc4"></a> `00a6adc4` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6adc8"></a> `00a6adc8` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6adcc"></a> `00a6adcc` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6add0"></a> `00a6add0` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00a6add4"></a> `00a6add4` | `de fb ff 17` | b 0x00a69d4c | `CALL_TERMINATOR`
<a id="insn-00a6adfc"></a> `00a6adfc` | `61 b8 07 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6abac`](#insn-00a6abac) 範囲 `[['00a6abac', '00a6abf7']]`
  - `CONDITIONAL_JUMP` [`00a6abf4`](#insn-00a6abf4) → [`00a6ac20`](#insn-00a6ac20)
  - `FALL_THROUGH` [`00a6abf4`](#insn-00a6abf4) → [`00a6abf8`](#insn-00a6abf8)
- ブロック [`00a6abf8`](#insn-00a6abf8) 範囲 `[['00a6abf8', '00a6abff']]`
  - `UNCONDITIONAL_JUMP` [`00a6abfc`](#insn-00a6abfc) → [`00a6ac08`](#insn-00a6ac08)
- ブロック [`00a6ac00`](#insn-00a6ac00) 範囲 `[['00a6ac00', '00a6ac07']]`
  - `CONDITIONAL_JUMP` [`00a6ac04`](#insn-00a6ac04) → [`00a6ac20`](#insn-00a6ac20)
  - `FALL_THROUGH` [`00a6ac04`](#insn-00a6ac04) → [`00a6ac08`](#insn-00a6ac08)
- ブロック [`00a6ac08`](#insn-00a6ac08) 範囲 `[['00a6ac08', '00a6ac13']]`
  - `CONDITIONAL_JUMP` [`00a6ac10`](#insn-00a6ac10) → [`00a6ac00`](#insn-00a6ac00)
  - `FALL_THROUGH` [`00a6ac10`](#insn-00a6ac10) → [`00a6ac14`](#insn-00a6ac14)
- ブロック [`00a6ac14`](#insn-00a6ac14) 範囲 `[['00a6ac14', '00a6ac17']]`
  - `CONDITIONAL_JUMP` [`00a6ac14`](#insn-00a6ac14) → [`00a6ad54`](#insn-00a6ad54)
  - `FALL_THROUGH` [`00a6ac14`](#insn-00a6ac14) → [`00a6ac18`](#insn-00a6ac18)
- ブロック [`00a6ac18`](#insn-00a6ac18) 範囲 `[['00a6ac18', '00a6ac1f']]`
  - `UNCONDITIONAL_JUMP` [`00a6ac1c`](#insn-00a6ac1c) → [`00a6ac00`](#insn-00a6ac00)
- ブロック [`00a6ac20`](#insn-00a6ac20) 範囲 `[['00a6ac20', '00a6ac5f']]`
  - `CONDITIONAL_JUMP` [`00a6ac5c`](#insn-00a6ac5c) → [`00a6ac70`](#insn-00a6ac70)
  - `FALL_THROUGH` [`00a6ac5c`](#insn-00a6ac5c) → [`00a6ac60`](#insn-00a6ac60)
- ブロック [`00a6ac60`](#insn-00a6ac60) 範囲 `[['00a6ac60', '00a6ac63']]`
  - `UNCONDITIONAL_JUMP` [`00a6ac60`](#insn-00a6ac60) → [`00a6ac90`](#insn-00a6ac90)
- ブロック [`00a6ac64`](#insn-00a6ac64) 範囲 `[['00a6ac64', '00a6ac6f']]`
  - `CONDITIONAL_JUMP` [`00a6ac6c`](#insn-00a6ac6c) → [`00a6ac90`](#insn-00a6ac90)
  - `FALL_THROUGH` [`00a6ac6c`](#insn-00a6ac6c) → [`00a6ac70`](#insn-00a6ac70)
- ブロック [`00a6ac70`](#insn-00a6ac70) 範囲 `[['00a6ac70', '00a6ac7f']]`
  - `CONDITIONAL_JUMP` [`00a6ac7c`](#insn-00a6ac7c) → [`00a6ac64`](#insn-00a6ac64)
  - `FALL_THROUGH` [`00a6ac7c`](#insn-00a6ac7c) → [`00a6ac80`](#insn-00a6ac80)
- ブロック [`00a6ac80`](#insn-00a6ac80) 範囲 `[['00a6ac80', '00a6ac83']]`
  - `CONDITIONAL_JUMP` [`00a6ac80`](#insn-00a6ac80) → [`00a6ace4`](#insn-00a6ace4)
  - `FALL_THROUGH` [`00a6ac80`](#insn-00a6ac80) → [`00a6ac84`](#insn-00a6ac84)
- ブロック [`00a6ac84`](#insn-00a6ac84) 範囲 `[['00a6ac84', '00a6ac8b']]`
  - `CONDITIONAL_JUMP` [`00a6ac88`](#insn-00a6ac88) → [`00a6ac70`](#insn-00a6ac70)
  - `FALL_THROUGH` [`00a6ac88`](#insn-00a6ac88) → [`00a6ac8c`](#insn-00a6ac8c)
- ブロック [`00a6ac8c`](#insn-00a6ac8c) 範囲 `[['00a6ac8c', '00a6ac8f']]`
  - `FALL_THROUGH` [`00a6ac8c`](#insn-00a6ac8c) → [`00a6ac90`](#insn-00a6ac90)
- ブロック [`00a6ac90`](#insn-00a6ac90) 範囲 `[['00a6ac90', '00a6acbf']]`
  - `CONDITIONAL_JUMP` [`00a6acbc`](#insn-00a6acbc) → [`00a6acc8`](#insn-00a6acc8)
  - `FALL_THROUGH` [`00a6acbc`](#insn-00a6acbc) → [`00a6acc0`](#insn-00a6acc0)
- ブロック [`00a6acc0`](#insn-00a6acc0) 範囲 `[['00a6acc0', '00a6acc7']]`
  - `FALL_THROUGH` [`00a6acc4`](#insn-00a6acc4) → [`00a6acc8`](#insn-00a6acc8)
- ブロック [`00a6acc8`](#insn-00a6acc8) 範囲 `[['00a6acc8', '00a6ace3']]`
  - `UNCONDITIONAL_JUMP` [`00a6ace0`](#insn-00a6ace0) → [`00a6ace8`](#insn-00a6ace8)
- ブロック [`00a6ace4`](#insn-00a6ace4) 範囲 `[['00a6ace4', '00a6ace7']]`
  - `FALL_THROUGH` [`00a6ace4`](#insn-00a6ace4) → [`00a6ace8`](#insn-00a6ace8)
- ブロック [`00a6ace8`](#insn-00a6ace8) 範囲 `[['00a6ace8', '00a6acf7']]`
  - `CONDITIONAL_JUMP` [`00a6acf4`](#insn-00a6acf4) → [`00a6ad20`](#insn-00a6ad20)
  - `FALL_THROUGH` [`00a6acf4`](#insn-00a6acf4) → [`00a6acf8`](#insn-00a6acf8)
- ブロック [`00a6acf8`](#insn-00a6acf8) 範囲 `[['00a6acf8', '00a6ad07']]`
  - `CONDITIONAL_JUMP` [`00a6ad04`](#insn-00a6ad04) → [`00a6ad20`](#insn-00a6ad20)
  - `FALL_THROUGH` [`00a6ad04`](#insn-00a6ad04) → [`00a6ad08`](#insn-00a6ad08)
- ブロック [`00a6ad08`](#insn-00a6ad08) 範囲 `[['00a6ad08', '00a6ad1f']]`
  - `FALL_THROUGH` [`00a6ad1c`](#insn-00a6ad1c) → [`00a6ad20`](#insn-00a6ad20)
- ブロック [`00a6ad20`](#insn-00a6ad20) 範囲 `[['00a6ad20', '00a6ad27']]`
  - `CONDITIONAL_JUMP` [`00a6ad24`](#insn-00a6ad24) → [`00a6ad50`](#insn-00a6ad50)
  - `FALL_THROUGH` [`00a6ad24`](#insn-00a6ad24) → [`00a6ad28`](#insn-00a6ad28)
- ブロック [`00a6ad28`](#insn-00a6ad28) 範囲 `[['00a6ad28', '00a6ad37']]`
  - `CONDITIONAL_JUMP` [`00a6ad34`](#insn-00a6ad34) → [`00a6ad50`](#insn-00a6ad50)
  - `FALL_THROUGH` [`00a6ad34`](#insn-00a6ad34) → [`00a6ad38`](#insn-00a6ad38)
- ブロック [`00a6ad38`](#insn-00a6ad38) 範囲 `[['00a6ad38', '00a6ad4f']]`
  - `FALL_THROUGH` [`00a6ad4c`](#insn-00a6ad4c) → [`00a6ad50`](#insn-00a6ad50)
- ブロック [`00a6ad50`](#insn-00a6ad50) 範囲 `[['00a6ad50', '00a6ad53']]`
  - `FALL_THROUGH` [`00a6ad50`](#insn-00a6ad50) → [`00a6ad54`](#insn-00a6ad54)
- ブロック [`00a6ad54`](#insn-00a6ad54) 範囲 `[['00a6ad54', '00a6ad57']]`
  - `CONDITIONAL_JUMP` [`00a6ad54`](#insn-00a6ad54) → [`00a6ad64`](#insn-00a6ad64)
  - `FALL_THROUGH` [`00a6ad54`](#insn-00a6ad54) → [`00a6ad58`](#insn-00a6ad58)
- ブロック [`00a6ad58`](#insn-00a6ad58) 範囲 `[['00a6ad58', '00a6ad5b']]`
  - `UNCONDITIONAL_JUMP` [`00a6ad58`](#insn-00a6ad58) → [`00a6ad7c`](#insn-00a6ad7c)
- ブロック [`00a6ad5c`](#insn-00a6ad5c) 範囲 `[['00a6ad5c', '00a6ad63']]`
  - `CONDITIONAL_JUMP` [`00a6ad60`](#insn-00a6ad60) → [`00a6ad7c`](#insn-00a6ad7c)
  - `FALL_THROUGH` [`00a6ad60`](#insn-00a6ad60) → [`00a6ad64`](#insn-00a6ad64)
- ブロック [`00a6ad64`](#insn-00a6ad64) 範囲 `[['00a6ad64', '00a6ad6f']]`
  - `CONDITIONAL_JUMP` [`00a6ad6c`](#insn-00a6ad6c) → [`00a6ad5c`](#insn-00a6ad5c)
  - `FALL_THROUGH` [`00a6ad6c`](#insn-00a6ad6c) → [`00a6ad70`](#insn-00a6ad70)
- ブロック [`00a6ad70`](#insn-00a6ad70) 範囲 `[['00a6ad70', '00a6ad73']]`
  - `CONDITIONAL_JUMP` [`00a6ad70`](#insn-00a6ad70) → [`00a6ad98`](#insn-00a6ad98)
  - `FALL_THROUGH` [`00a6ad70`](#insn-00a6ad70) → [`00a6ad74`](#insn-00a6ad74)
- ブロック [`00a6ad74`](#insn-00a6ad74) 範囲 `[['00a6ad74', '00a6ad7b']]`
  - `CONDITIONAL_JUMP` [`00a6ad78`](#insn-00a6ad78) → [`00a6ad64`](#insn-00a6ad64)
  - `FALL_THROUGH` [`00a6ad78`](#insn-00a6ad78) → [`00a6ad7c`](#insn-00a6ad7c)
- ブロック [`00a6ad7c`](#insn-00a6ad7c) 範囲 `[['00a6ad7c', '00a6ad8b']]`
  - `CONDITIONAL_JUMP` [`00a6ad88`](#insn-00a6ad88) → [`00a6adfc`](#insn-00a6adfc)
  - `FALL_THROUGH` [`00a6ad88`](#insn-00a6ad88) → [`00a6ad8c`](#insn-00a6ad8c)
- ブロック [`00a6ad8c`](#insn-00a6ad8c) 範囲 `[['00a6ad8c', '00a6ad97']]`
- ブロック [`00a6ad98`](#insn-00a6ad98) 範囲 `[['00a6ad98', '00a6adab']]`
  - `CONDITIONAL_JUMP` [`00a6ada8`](#insn-00a6ada8) → [`00a6adfc`](#insn-00a6adfc)
  - `FALL_THROUGH` [`00a6ada8`](#insn-00a6ada8) → [`00a6adac`](#insn-00a6adac)
- ブロック [`00a6adac`](#insn-00a6adac) 範囲 `[['00a6adac', '00a6add7']]`
- ブロック [`00a6adfc`](#insn-00a6adfc) 範囲 `[['00a6adfc', '00a6adff']]`

## 命令位置別の参照

- [`00a6abb0`](#insn-00a6abb0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abb4`](#insn-00a6abb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abb8`](#insn-00a6abb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abbc`](#insn-00a6abbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abc0`](#insn-00a6abc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abc4`](#insn-00a6abc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abec`](#insn-00a6abec) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abf4`](#insn-00a6abf4) → [`00a6ac20`](#insn-00a6ac20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abfc`](#insn-00a6abfc) → [`00a6ac08`](#insn-00a6ac08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac04`](#insn-00a6ac04) → [`00a6ac20`](#insn-00a6ac20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac10`](#insn-00a6ac10) → [`00a6ac00`](#insn-00a6ac00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac14`](#insn-00a6ac14) → [`00a6ad54`](#insn-00a6ad54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac1c`](#insn-00a6ac1c) → [`00a6ac00`](#insn-00a6ac00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac24`](#insn-00a6ac24) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac34`](#insn-00a6ac34) → `00c8c9a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6ac58`](#insn-00a6ac58) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac5c`](#insn-00a6ac5c) → [`00a6ac70`](#insn-00a6ac70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac60`](#insn-00a6ac60) → [`00a6ac90`](#insn-00a6ac90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac6c`](#insn-00a6ac6c) → [`00a6ac90`](#insn-00a6ac90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac7c`](#insn-00a6ac7c) → [`00a6ac64`](#insn-00a6ac64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac80`](#insn-00a6ac80) → [`00a6ace4`](#insn-00a6ace4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac88`](#insn-00a6ac88) → [`00a6ac70`](#insn-00a6ac70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac94`](#insn-00a6ac94) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00a6acbc`](#insn-00a6acbc) → [`00a6acc8`](#insn-00a6acc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6accc`](#insn-00a6accc) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`00a6acd8`](#insn-00a6acd8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ace0`](#insn-00a6ace0) → [`00a6ace8`](#insn-00a6ace8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6acec`](#insn-00a6acec) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6acf4`](#insn-00a6acf4) → [`00a6ad20`](#insn-00a6ad20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad00`](#insn-00a6ad00) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad04`](#insn-00a6ad04) → [`00a6ad20`](#insn-00a6ad20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad1c`](#insn-00a6ad1c) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad20`](#insn-00a6ad20) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad24`](#insn-00a6ad24) → [`00a6ad50`](#insn-00a6ad50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad30`](#insn-00a6ad30) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad34`](#insn-00a6ad34) → [`00a6ad50`](#insn-00a6ad50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad4c`](#insn-00a6ad4c) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad54`](#insn-00a6ad54) → [`00a6ad64`](#insn-00a6ad64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad58`](#insn-00a6ad58) → [`00a6ad7c`](#insn-00a6ad7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad60`](#insn-00a6ad60) → [`00a6ad7c`](#insn-00a6ad7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad6c`](#insn-00a6ad6c) → [`00a6ad5c`](#insn-00a6ad5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad70`](#insn-00a6ad70) → [`00a6ad98`](#insn-00a6ad98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad78`](#insn-00a6ad78) → [`00a6ad64`](#insn-00a6ad64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad80`](#insn-00a6ad80) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad88`](#insn-00a6ad88) → [`00a6adfc`](#insn-00a6adfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ad90`](#insn-00a6ad90) → `002a01b0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a6ad94`](#insn-00a6ad94) → [`00442c90`](../00442/00442c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00442c90` · 推定シンボル `None` · 推定型 `None`
- [`00a6ada0`](#insn-00a6ada0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ada8`](#insn-00a6ada8) → [`00a6adfc`](#insn-00a6adfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adb8`](#insn-00a6adb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adbc`](#insn-00a6adbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adc0`](#insn-00a6adc0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adc4`](#insn-00a6adc4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adc8`](#insn-00a6adc8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adcc`](#insn-00a6adcc) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6add4`](#insn-00a6add4) → [`00a69d4c`](../00a69/00a69d4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a69d4c` · 推定シンボル `None` · 推定型 `None`
- [`00a6adfc`](#insn-00a6adfc) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6abb0`](#insn-00a6abb0)

~~~json
{
  "source": "00a6abb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abb4`](#insn-00a6abb4)

~~~json
{
  "source": "00a6abb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abb8`](#insn-00a6abb8)

~~~json
{
  "source": "00a6abb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abbc`](#insn-00a6abbc)

~~~json
{
  "source": "00a6abbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abc0`](#insn-00a6abc0)

~~~json
{
  "source": "00a6abc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abc4`](#insn-00a6abc4)

~~~json
{
  "source": "00a6abc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abec`](#insn-00a6abec)

~~~json
{
  "source": "00a6abec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abf4`](#insn-00a6abf4)

~~~json
{
  "source": "00a6abf4",
  "target": "00a6ac20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abfc`](#insn-00a6abfc)

~~~json
{
  "source": "00a6abfc",
  "target": "00a6ac08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac04`](#insn-00a6ac04)

~~~json
{
  "source": "00a6ac04",
  "target": "00a6ac20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac10`](#insn-00a6ac10)

~~~json
{
  "source": "00a6ac10",
  "target": "00a6ac00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac14`](#insn-00a6ac14)

~~~json
{
  "source": "00a6ac14",
  "target": "00a6ad54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac1c`](#insn-00a6ac1c)

~~~json
{
  "source": "00a6ac1c",
  "target": "00a6ac00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac24`](#insn-00a6ac24)

~~~json
{
  "source": "00a6ac24",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ac34`](#insn-00a6ac34)

~~~json
{
  "source": "00a6ac34",
  "target": "00c8c9a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c9a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6ac58`](#insn-00a6ac58)

~~~json
{
  "source": "00a6ac58",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac5c`](#insn-00a6ac5c)

~~~json
{
  "source": "00a6ac5c",
  "target": "00a6ac70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac60`](#insn-00a6ac60)

~~~json
{
  "source": "00a6ac60",
  "target": "00a6ac90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac6c`](#insn-00a6ac6c)

~~~json
{
  "source": "00a6ac6c",
  "target": "00a6ac90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac7c`](#insn-00a6ac7c)

~~~json
{
  "source": "00a6ac7c",
  "target": "00a6ac64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac80`](#insn-00a6ac80)

~~~json
{
  "source": "00a6ac80",
  "target": "00a6ace4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac88`](#insn-00a6ac88)

~~~json
{
  "source": "00a6ac88",
  "target": "00a6ac70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac94`](#insn-00a6ac94)

~~~json
{
  "source": "00a6ac94",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6acbc`](#insn-00a6acbc)

~~~json
{
  "source": "00a6acbc",
  "target": "00a6acc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6accc`](#insn-00a6accc)

~~~json
{
  "source": "00a6accc",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6acd8`](#insn-00a6acd8)

~~~json
{
  "source": "00a6acd8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ace0`](#insn-00a6ace0)

~~~json
{
  "source": "00a6ace0",
  "target": "00a6ace8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6acec`](#insn-00a6acec)

~~~json
{
  "source": "00a6acec",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6acf4`](#insn-00a6acf4)

~~~json
{
  "source": "00a6acf4",
  "target": "00a6ad20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad00`](#insn-00a6ad00)

~~~json
{
  "source": "00a6ad00",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad04`](#insn-00a6ad04)

~~~json
{
  "source": "00a6ad04",
  "target": "00a6ad20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad1c`](#insn-00a6ad1c)

~~~json
{
  "source": "00a6ad1c",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad20`](#insn-00a6ad20)

~~~json
{
  "source": "00a6ad20",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad24`](#insn-00a6ad24)

~~~json
{
  "source": "00a6ad24",
  "target": "00a6ad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad30`](#insn-00a6ad30)

~~~json
{
  "source": "00a6ad30",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad34`](#insn-00a6ad34)

~~~json
{
  "source": "00a6ad34",
  "target": "00a6ad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad4c`](#insn-00a6ad4c)

~~~json
{
  "source": "00a6ad4c",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ad54`](#insn-00a6ad54)

~~~json
{
  "source": "00a6ad54",
  "target": "00a6ad64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad58`](#insn-00a6ad58)

~~~json
{
  "source": "00a6ad58",
  "target": "00a6ad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad60`](#insn-00a6ad60)

~~~json
{
  "source": "00a6ad60",
  "target": "00a6ad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad6c`](#insn-00a6ad6c)

~~~json
{
  "source": "00a6ad6c",
  "target": "00a6ad5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad70`](#insn-00a6ad70)

~~~json
{
  "source": "00a6ad70",
  "target": "00a6ad98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad78`](#insn-00a6ad78)

~~~json
{
  "source": "00a6ad78",
  "target": "00a6ad64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad80`](#insn-00a6ad80)

~~~json
{
  "source": "00a6ad80",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad88`](#insn-00a6ad88)

~~~json
{
  "source": "00a6ad88",
  "target": "00a6adfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ad90`](#insn-00a6ad90)

~~~json
{
  "source": "00a6ad90",
  "target": "002a01b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a01b0",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "6d61703a3a61743a20206b6579206e6f7420666f756e6400",
  "capture_start": "002a01b0",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6ad94`](#insn-00a6ad94)

~~~json
{
  "source": "00a6ad94",
  "target": "00442c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ada0`](#insn-00a6ada0)

~~~json
{
  "source": "00a6ada0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ada8`](#insn-00a6ada8)

~~~json
{
  "source": "00a6ada8",
  "target": "00a6adfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adb8`](#insn-00a6adb8)

~~~json
{
  "source": "00a6adb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adbc`](#insn-00a6adbc)

~~~json
{
  "source": "00a6adbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adc0`](#insn-00a6adc0)

~~~json
{
  "source": "00a6adc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adc4`](#insn-00a6adc4)

~~~json
{
  "source": "00a6adc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adc8`](#insn-00a6adc8)

~~~json
{
  "source": "00a6adc8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adcc`](#insn-00a6adcc)

~~~json
{
  "source": "00a6adcc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6add4`](#insn-00a6add4)

~~~json
{
  "source": "00a6add4",
  "target": "00a69d4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6adfc`](#insn-00a6adfc)

~~~json
{
  "source": "00a6adfc",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
