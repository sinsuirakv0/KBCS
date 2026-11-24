# 008daefc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008daea8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008daea8.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0029.md#compare-d63c7ac88469182a555812bbe73c1910)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `008dbea8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008db/008dbea8.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0022.md#compare-16781a8ddb08bedfca050b880658aa0e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008daefc",
  "name": "FUN_008daefc",
  "size": 628,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "85714ac848f44af08802d4f35383a538d8111db9ca8bd3468de05b9b9b86902b",
  "source_text_sha256": "85714ac848f44af08802d4f35383a538d8111db9ca8bd3468de05b9b9b86902b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008daefc",
        "008db16b"
      ],
      [
        "008db1a0",
        "008db1a3"
      ]
    ],
    "bytes_sha256": "014386ba51880cb6f75fd62cbcb0761eeaaaf23f2b904b398db4566c312ccbbf",
    "instruction_count": 157,
    "instruction_bytes": 628,
    "body_bytes": 628,
    "indirect": 10,
    "unresolved": 10
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00459db4](../00459/00459db4.md)
- [00596f6c](../00596/00596f6c.md)
- [00865b4c](../00865/00865b4c.md)
- [008d615c](../008d6/008d615c.md)
- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57fb0](../00c57/00c57fb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3826 bytes

~~~c

void FUN_008daefc(long param_1,undefined8 *param_2,ulong *param_3)

{
  long lVar1;
  int iVar2;
  int iVar3;
  undefined4 uVar4;
  long *plVar5;
  long lVar6;
  undefined4 *puVar7;
  ulong local_70;
  long *local_68;
  undefined4 local_5c;
  undefined4 local_58;
  undefined4 uStack_54;
  long *local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  puVar7 = *(undefined4 **)(param_1 + 0x10);
  *(undefined1 *)((long)puVar7 + 0x91) = 0;
  iVar2 = (*(code *)**(undefined8 **)*param_2)();
  iVar3 = (*(code *)**(undefined8 **)*param_2)((undefined8 *)*param_2);
  if (iVar2 == 0x199) {
    plVar5 = *(long **)(param_1 + 0x40);
    local_58 = 2;
    local_70 = CONCAT44(local_70._4_4_,iVar3);
joined_r0x008db0b0:
    if (plVar5 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
        FUN_00459db4();
      }
      goto LAB_008db1a0;
    }
    (**(code **)(*plVar5 + 0x30))(plVar5,&local_58,&local_70);
  }
  else {
    if (iVar3 != 200) {
      puVar7[1] = 0;
      puVar7[2] = 0;
      *(undefined1 *)(puVar7 + 0x1c) = 0;
      local_58 = 0;
      *(undefined8 *)(puVar7 + 6) = 0;
      *(undefined8 *)(puVar7 + 4) = 0;
      *(undefined8 *)(puVar7 + 10) = 0;
      *(undefined8 *)(puVar7 + 8) = 0;
      *(undefined8 *)(puVar7 + 0xe) = 0;
      *(undefined8 *)(puVar7 + 0xc) = 0;
      *(undefined8 *)(puVar7 + 0x12) = 0;
      *(undefined8 *)(puVar7 + 0x10) = 0;
      *(undefined8 *)(puVar7 + 0x16) = 0;
      *(undefined8 *)(puVar7 + 0x14) = 0;
      *(undefined8 *)(puVar7 + 0x1a) = 0;
      *(undefined8 *)(puVar7 + 0x18) = 0;
      FUN_00865b4c(&local_58);
      *(undefined1 *)(puVar7 + 0x24) = 0;
      *puVar7 = 0xffffffff;
      *(ulong *)(puVar7 + 0x1d) = CONCAT44(uStack_54,local_58);
      *(undefined1 *)(puVar7 + 0x1c) = 1;
      uVar4 = (*(code *)**(undefined8 **)*param_2)();
      plVar5 = *(long **)(param_1 + 0x40);
      local_58 = 1;
      local_70 = CONCAT44(local_70._4_4_,uVar4);
      goto joined_r0x008db0b0;
    }
    local_70 = *param_3;
    local_68 = (long *)param_3[1];
    if (local_68 != (long *)0x0) {
      FUN_00c53d70(1,local_68 + 1);
    }
    FUN_00596f6c(&local_58,&local_70);
    plVar5 = local_68;
    if ((local_68 == (long *)0x0) ||
       (lVar6 = FUN_00c53da0(0xffffffffffffffff,local_68 + 1), lVar6 != 0)) {
      if (CONCAT44(uStack_54,local_58) == 0) goto LAB_008db0e8;
LAB_008db004:
      FUN_008d615c(puVar7);
      puVar7[2] = 1;
      local_5c = (*(code *)**(undefined8 **)*param_2)();
      plVar5 = *(long **)(param_1 + 0x40);
      local_70 = local_70 & 0xffffffff00000000;
      if (plVar5 == (long *)0x0) {
LAB_008db158:
        if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
          FUN_00459db4();
        }
        goto LAB_008db1a0;
      }
      (**(code **)(*plVar5 + 0x30))(plVar5,&local_70,&local_5c);
    }
    else {
      (**(code **)(*plVar5 + 0x10))(plVar5);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
      if (CONCAT44(uStack_54,local_58) != 0) goto LAB_008db004;
LAB_008db0e8:
      local_5c = (*(code *)**(undefined8 **)*param_2)();
      plVar5 = *(long **)(param_1 + 0x40);
      local_70 = CONCAT44(local_70._4_4_,1);
      if (plVar5 == (long *)0x0) goto LAB_008db158;
      (**(code **)(*plVar5 + 0x30))(plVar5,&local_70,&local_5c);
    }
    if ((local_50 != (long *)0x0) &&
       (lVar6 = FUN_00c53da0(0xffffffffffffffff,local_50 + 1), lVar6 == 0)) {
      (**(code **)(*local_50 + 0x10))(local_50);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_50);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
LAB_008db1a0:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008daefc"></a> `008daefc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008daf00"></a> `008daf00` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008daf04"></a> `008daf04` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008daf08"></a> `008daf08` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008daf0c"></a> `008daf0c` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008daf10"></a> `008daf10` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-008daf14"></a> `008daf14` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-008daf18"></a> `008daf18` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008daf1c"></a> `008daf1c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-008daf20"></a> `008daf20` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-008daf24"></a> `008daf24` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-008daf28"></a> `008daf28` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008daf2c"></a> `008daf2c` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-008daf30"></a> `008daf30` | `bf 46 02 39` | strb wzr,[x21, #0x91] | `FALL_THROUGH`
<a id="insn-008daf34"></a> `008daf34` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-008daf38"></a> `008daf38` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-008daf3c"></a> `008daf3c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008daf40"></a> `008daf40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008daf44"></a> `008daf44` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-008daf48"></a> `008daf48` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-008daf4c"></a> `008daf4c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008daf50"></a> `008daf50` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-008daf54"></a> `008daf54` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-008daf58"></a> `008daf58` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-008daf5c"></a> `008daf5c` | `ff 66 06 71` | cmp w23,#0x199 | `FALL_THROUGH`
<a id="insn-008daf60"></a> `008daf60` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-008daf64"></a> `008daf64` | `a1 02 00 54` | b.ne 0x008dafb8 | `CONDITIONAL_JUMP`
<a id="insn-008daf68"></a> `008daf68` | `60 22 40 f9` | ldr x0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-008daf6c"></a> `008daf6c` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-008daf70"></a> `008daf70` | `e9 1b 00 b9` | str w9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008daf74"></a> `008daf74` | `e8 03 00 b9` | str w8,[sp] | `FALL_THROUGH`
<a id="insn-008daf78"></a> `008daf78` | `e0 09 00 b4` | cbz x0,0x008db0b4 | `CONDITIONAL_JUMP`
<a id="insn-008daf7c"></a> `008daf7c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-008daf80"></a> `008daf80` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-008daf84"></a> `008daf84` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-008daf88"></a> `008daf88` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-008daf8c"></a> `008daf8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008daf90"></a> `008daf90` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-008daf94"></a> `008daf94` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008daf98"></a> `008daf98` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008daf9c"></a> `008daf9c` | `21 10 00 54` | b.ne 0x008db1a0 | `CONDITIONAL_JUMP`
<a id="insn-008dafa0"></a> `008dafa0` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008dafa4"></a> `008dafa4` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008dafa8"></a> `008dafa8` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008dafac"></a> `008dafac` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008dafb0"></a> `008dafb0` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008dafb4"></a> `008dafb4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008dafb8"></a> `008dafb8` | `1f 21 03 71` | cmp w8,#0xc8 | `FALL_THROUGH`
<a id="insn-008dafbc"></a> `008dafbc` | `a1 04 00 54` | b.ne 0x008db050 | `CONDITIONAL_JUMP`
<a id="insn-008dafc0"></a> `008dafc0` | `c9 22 40 a9` | ldp x9,x8,[x22] | `FALL_THROUGH`
<a id="insn-008dafc4"></a> `008dafc4` | `e9 23 00 a9` | stp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-008dafc8"></a> `008dafc8` | `88 00 00 b4` | cbz x8,0x008dafd8 | `CONDITIONAL_JUMP`
<a id="insn-008dafcc"></a> `008dafcc` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-008dafd0"></a> `008dafd0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-008dafd4"></a> `008dafd4` | `67 e3 0d 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-008dafd8"></a> `008dafd8` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-008dafdc"></a> `008dafdc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-008dafe0"></a> `008dafe0` | `e3 ef f2 97` | bl 0x00596f6c | `UNCONDITIONAL_CALL`
<a id="insn-008dafe4"></a> `008dafe4` | `f6 07 40 f9` | ldr x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008dafe8"></a> `008dafe8` | `b6 00 00 b4` | cbz x22,0x008daffc | `CONDITIONAL_JUMP`
<a id="insn-008dafec"></a> `008dafec` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008daff0"></a> `008daff0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008daff4"></a> `008daff4` | `6b e3 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008daff8"></a> `008daff8` | `80 06 00 b4` | cbz x0,0x008db0c8 | `CONDITIONAL_JUMP`
<a id="insn-008daffc"></a> `008daffc` | `e1 0f 40 f9` | ldr x1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008db000"></a> `008db000` | `41 07 00 b4` | cbz x1,0x008db0e8 | `CONDITIONAL_JUMP`
<a id="insn-008db004"></a> `008db004` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008db008"></a> `008db008` | `55 ec ff 97` | bl 0x008d615c | `UNCONDITIONAL_CALL`
<a id="insn-008db00c"></a> `008db00c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-008db010"></a> `008db010` | `a8 0a 00 b9` | str w8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-008db014"></a> `008db014` | `80 02 40 f9` | ldr x0,[x20] | `FALL_THROUGH`
<a id="insn-008db018"></a> `008db018` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-008db01c"></a> `008db01c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008db020"></a> `008db020` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008db024"></a> `008db024` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-008db028"></a> `008db028` | `60 22 40 f9` | ldr x0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-008db02c"></a> `008db02c` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-008db030"></a> `008db030` | `e8 17 00 b9` | str w8,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-008db034"></a> `008db034` | `20 09 00 b4` | cbz x0,0x008db158 | `CONDITIONAL_JUMP`
<a id="insn-008db038"></a> `008db038` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-008db03c"></a> `008db03c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-008db040"></a> `008db040` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-008db044"></a> `008db044` | `e2 53 00 91` | add x2,sp,#0x14 | `FALL_THROUGH`
<a id="insn-008db048"></a> `008db048` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008db04c"></a> `008db04c` | `36 00 00 14` | b 0x008db124 | `UNCONDITIONAL_JUMP`
<a id="insn-008db050"></a> `008db050` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-008db054"></a> `008db054` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-008db058"></a> `008db058` | `bf fe 00 29` | stp wzr,wzr,[x21, #0x4] | `FALL_THROUGH`
<a id="insn-008db05c"></a> `008db05c` | `bf c2 01 39` | strb wzr,[x21, #0x70] | `FALL_THROUGH`
<a id="insn-008db060"></a> `008db060` | `ff 1b 00 b9` | str wzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008db064"></a> `008db064` | `a0 82 00 ad` | stp q0,q0,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008db068"></a> `008db068` | `a0 82 01 ad` | stp q0,q0,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-008db06c"></a> `008db06c` | `a0 82 02 ad` | stp q0,q0,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-008db070"></a> `008db070` | `b7 2a fe 97` | bl 0x00865b4c | `UNCONDITIONAL_CALL`
<a id="insn-008db074"></a> `008db074` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008db078"></a> `008db078` | `09 00 80 12` | mov w9,#0xffffffff | `FALL_THROUGH`
<a id="insn-008db07c"></a> `008db07c` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-008db080"></a> `008db080` | `bf 42 02 39` | strb wzr,[x21, #0x90] | `FALL_THROUGH`
<a id="insn-008db084"></a> `008db084` | `a9 02 00 b9` | str w9,[x21] | `FALL_THROUGH`
<a id="insn-008db088"></a> `008db088` | `a8 42 07 f8` | stur x8,[x21, #0x74] | `FALL_THROUGH`
<a id="insn-008db08c"></a> `008db08c` | `b6 c2 01 39` | strb w22,[x21, #0x70] | `FALL_THROUGH`
<a id="insn-008db090"></a> `008db090` | `80 02 40 f9` | ldr x0,[x20] | `FALL_THROUGH`
<a id="insn-008db094"></a> `008db094` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-008db098"></a> `008db098` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008db09c"></a> `008db09c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008db0a0"></a> `008db0a0` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-008db0a4"></a> `008db0a4` | `60 22 40 f9` | ldr x0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-008db0a8"></a> `008db0a8` | `f6 1b 00 b9` | str w22,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008db0ac"></a> `008db0ac` | `e8 03 00 b9` | str w8,[sp] | `FALL_THROUGH`
<a id="insn-008db0b0"></a> `008db0b0` | `60 f6 ff b5` | cbnz x0,0x008daf7c | `CONDITIONAL_JUMP`
<a id="insn-008db0b4"></a> `008db0b4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-008db0b8"></a> `008db0b8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008db0bc"></a> `008db0bc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008db0c0"></a> `008db0c0` | `01 07 00 54` | b.ne 0x008db1a0 | `CONDITIONAL_JUMP`
<a id="insn-008db0c4"></a> `008db0c4` | `3c fb ed 97` | bl 0x00459db4 | `CALL_TERMINATOR`
<a id="insn-008db0c8"></a> `008db0c8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008db0cc"></a> `008db0cc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008db0d0"></a> `008db0d0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008db0d4"></a> `008db0d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008db0d8"></a> `008db0d8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008db0dc"></a> `008db0dc` | `9d f3 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008db0e0"></a> `008db0e0` | `e1 0f 40 f9` | ldr x1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008db0e4"></a> `008db0e4` | `01 f9 ff b5` | cbnz x1,0x008db004 | `CONDITIONAL_JUMP`
<a id="insn-008db0e8"></a> `008db0e8` | `80 02 40 f9` | ldr x0,[x20] | `FALL_THROUGH`
<a id="insn-008db0ec"></a> `008db0ec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-008db0f0"></a> `008db0f0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008db0f4"></a> `008db0f4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008db0f8"></a> `008db0f8` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-008db0fc"></a> `008db0fc` | `60 22 40 f9` | ldr x0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-008db100"></a> `008db100` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-008db104"></a> `008db104` | `e9 03 00 b9` | str w9,[sp] | `FALL_THROUGH`
<a id="insn-008db108"></a> `008db108` | `e8 17 00 b9` | str w8,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-008db10c"></a> `008db10c` | `60 02 00 b4` | cbz x0,0x008db158 | `CONDITIONAL_JUMP`
<a id="insn-008db110"></a> `008db110` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-008db114"></a> `008db114` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-008db118"></a> `008db118` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-008db11c"></a> `008db11c` | `e2 53 00 91` | add x2,sp,#0x14 | `FALL_THROUGH`
<a id="insn-008db120"></a> `008db120` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008db124"></a> `008db124` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008db128"></a> `008db128` | `53 f3 ff b4` | cbz x19,0x008daf90 | `CONDITIONAL_JUMP`
<a id="insn-008db12c"></a> `008db12c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008db130"></a> `008db130` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008db134"></a> `008db134` | `1b e3 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008db138"></a> `008db138` | `c0 f2 ff b5` | cbnz x0,0x008daf90 | `CONDITIONAL_JUMP`
<a id="insn-008db13c"></a> `008db13c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-008db140"></a> `008db140` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008db144"></a> `008db144` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008db148"></a> `008db148` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008db14c"></a> `008db14c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008db150"></a> `008db150` | `80 f3 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008db154"></a> `008db154` | `8f ff ff 17` | b 0x008daf90 | `UNCONDITIONAL_JUMP`
<a id="insn-008db158"></a> `008db158` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-008db15c"></a> `008db15c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008db160"></a> `008db160` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008db164"></a> `008db164` | `e1 01 00 54` | b.ne 0x008db1a0 | `CONDITIONAL_JUMP`
<a id="insn-008db168"></a> `008db168` | `13 fb ed 97` | bl 0x00459db4 | `CALL_TERMINATOR`
<a id="insn-008db1a0"></a> `008db1a0` | `84 f3 0d 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008daefc`](#insn-008daefc) 範囲 `[['008daefc', '008daf67']]`
  - `CONDITIONAL_JUMP` [`008daf64`](#insn-008daf64) → [`008dafb8`](#insn-008dafb8)
  - `FALL_THROUGH` [`008daf64`](#insn-008daf64) → [`008daf68`](#insn-008daf68)
- ブロック [`008daf68`](#insn-008daf68) 範囲 `[['008daf68', '008daf7b']]`
  - `CONDITIONAL_JUMP` [`008daf78`](#insn-008daf78) → [`008db0b4`](#insn-008db0b4)
  - `FALL_THROUGH` [`008daf78`](#insn-008daf78) → [`008daf7c`](#insn-008daf7c)
- ブロック [`008daf7c`](#insn-008daf7c) 範囲 `[['008daf7c', '008daf8f']]`
  - `FALL_THROUGH` [`008daf8c`](#insn-008daf8c) → [`008daf90`](#insn-008daf90)
- ブロック [`008daf90`](#insn-008daf90) 範囲 `[['008daf90', '008daf9f']]`
  - `CONDITIONAL_JUMP` [`008daf9c`](#insn-008daf9c) → [`008db1a0`](#insn-008db1a0)
  - `FALL_THROUGH` [`008daf9c`](#insn-008daf9c) → [`008dafa0`](#insn-008dafa0)
- ブロック [`008dafa0`](#insn-008dafa0) 範囲 `[['008dafa0', '008dafb7']]`
- ブロック [`008dafb8`](#insn-008dafb8) 範囲 `[['008dafb8', '008dafbf']]`
  - `CONDITIONAL_JUMP` [`008dafbc`](#insn-008dafbc) → [`008db050`](#insn-008db050)
  - `FALL_THROUGH` [`008dafbc`](#insn-008dafbc) → [`008dafc0`](#insn-008dafc0)
- ブロック [`008dafc0`](#insn-008dafc0) 範囲 `[['008dafc0', '008dafcb']]`
  - `CONDITIONAL_JUMP` [`008dafc8`](#insn-008dafc8) → [`008dafd8`](#insn-008dafd8)
  - `FALL_THROUGH` [`008dafc8`](#insn-008dafc8) → [`008dafcc`](#insn-008dafcc)
- ブロック [`008dafcc`](#insn-008dafcc) 範囲 `[['008dafcc', '008dafd7']]`
  - `FALL_THROUGH` [`008dafd4`](#insn-008dafd4) → [`008dafd8`](#insn-008dafd8)
- ブロック [`008dafd8`](#insn-008dafd8) 範囲 `[['008dafd8', '008dafeb']]`
  - `CONDITIONAL_JUMP` [`008dafe8`](#insn-008dafe8) → [`008daffc`](#insn-008daffc)
  - `FALL_THROUGH` [`008dafe8`](#insn-008dafe8) → [`008dafec`](#insn-008dafec)
- ブロック [`008dafec`](#insn-008dafec) 範囲 `[['008dafec', '008daffb']]`
  - `CONDITIONAL_JUMP` [`008daff8`](#insn-008daff8) → [`008db0c8`](#insn-008db0c8)
  - `FALL_THROUGH` [`008daff8`](#insn-008daff8) → [`008daffc`](#insn-008daffc)
- ブロック [`008daffc`](#insn-008daffc) 範囲 `[['008daffc', '008db003']]`
  - `CONDITIONAL_JUMP` [`008db000`](#insn-008db000) → [`008db0e8`](#insn-008db0e8)
  - `FALL_THROUGH` [`008db000`](#insn-008db000) → [`008db004`](#insn-008db004)
- ブロック [`008db004`](#insn-008db004) 範囲 `[['008db004', '008db037']]`
  - `CONDITIONAL_JUMP` [`008db034`](#insn-008db034) → [`008db158`](#insn-008db158)
  - `FALL_THROUGH` [`008db034`](#insn-008db034) → [`008db038`](#insn-008db038)
- ブロック [`008db038`](#insn-008db038) 範囲 `[['008db038', '008db04f']]`
  - `UNCONDITIONAL_JUMP` [`008db04c`](#insn-008db04c) → [`008db124`](#insn-008db124)
- ブロック [`008db050`](#insn-008db050) 範囲 `[['008db050', '008db0b3']]`
  - `CONDITIONAL_JUMP` [`008db0b0`](#insn-008db0b0) → [`008daf7c`](#insn-008daf7c)
  - `FALL_THROUGH` [`008db0b0`](#insn-008db0b0) → [`008db0b4`](#insn-008db0b4)
- ブロック [`008db0b4`](#insn-008db0b4) 範囲 `[['008db0b4', '008db0c3']]`
  - `CONDITIONAL_JUMP` [`008db0c0`](#insn-008db0c0) → [`008db1a0`](#insn-008db1a0)
  - `FALL_THROUGH` [`008db0c0`](#insn-008db0c0) → [`008db0c4`](#insn-008db0c4)
- ブロック [`008db0c4`](#insn-008db0c4) 範囲 `[['008db0c4', '008db0c7']]`
- ブロック [`008db0c8`](#insn-008db0c8) 範囲 `[['008db0c8', '008db0e7']]`
  - `CONDITIONAL_JUMP` [`008db0e4`](#insn-008db0e4) → [`008db004`](#insn-008db004)
  - `FALL_THROUGH` [`008db0e4`](#insn-008db0e4) → [`008db0e8`](#insn-008db0e8)
- ブロック [`008db0e8`](#insn-008db0e8) 範囲 `[['008db0e8', '008db10f']]`
  - `CONDITIONAL_JUMP` [`008db10c`](#insn-008db10c) → [`008db158`](#insn-008db158)
  - `FALL_THROUGH` [`008db10c`](#insn-008db10c) → [`008db110`](#insn-008db110)
- ブロック [`008db110`](#insn-008db110) 範囲 `[['008db110', '008db123']]`
  - `FALL_THROUGH` [`008db120`](#insn-008db120) → [`008db124`](#insn-008db124)
- ブロック [`008db124`](#insn-008db124) 範囲 `[['008db124', '008db12b']]`
  - `CONDITIONAL_JUMP` [`008db128`](#insn-008db128) → [`008daf90`](#insn-008daf90)
  - `FALL_THROUGH` [`008db128`](#insn-008db128) → [`008db12c`](#insn-008db12c)
- ブロック [`008db12c`](#insn-008db12c) 範囲 `[['008db12c', '008db13b']]`
  - `CONDITIONAL_JUMP` [`008db138`](#insn-008db138) → [`008daf90`](#insn-008daf90)
  - `FALL_THROUGH` [`008db138`](#insn-008db138) → [`008db13c`](#insn-008db13c)
- ブロック [`008db13c`](#insn-008db13c) 範囲 `[['008db13c', '008db157']]`
  - `UNCONDITIONAL_JUMP` [`008db154`](#insn-008db154) → [`008daf90`](#insn-008daf90)
- ブロック [`008db158`](#insn-008db158) 範囲 `[['008db158', '008db167']]`
  - `CONDITIONAL_JUMP` [`008db164`](#insn-008db164) → [`008db1a0`](#insn-008db1a0)
  - `FALL_THROUGH` [`008db164`](#insn-008db164) → [`008db168`](#insn-008db168)
- ブロック [`008db168`](#insn-008db168) 範囲 `[['008db168', '008db16b']]`
- ブロック [`008db1a0`](#insn-008db1a0) 範囲 `[['008db1a0', '008db1a3']]`

## 命令位置別の参照

- [`008daf00`](#insn-008daf00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daf04`](#insn-008daf04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daf08`](#insn-008daf08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daf0c`](#insn-008daf0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daf28`](#insn-008daf28) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daf64`](#insn-008daf64) → [`008dafb8`](#insn-008dafb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daf70`](#insn-008daf70) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daf74`](#insn-008daf74) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daf78`](#insn-008daf78) → [`008db0b4`](#insn-008db0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daf94`](#insn-008daf94) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daf9c`](#insn-008daf9c) → [`008db1a0`](#insn-008db1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafa0`](#insn-008dafa0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafa4`](#insn-008dafa4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafa8`](#insn-008dafa8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafac`](#insn-008dafac) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafbc`](#insn-008dafbc) → [`008db050`](#insn-008db050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafc4`](#insn-008dafc4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafc8`](#insn-008dafc8) → [`008dafd8`](#insn-008dafd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafd4`](#insn-008dafd4) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`008dafe0`](#insn-008dafe0) → [`00596f6c`](../00596/00596f6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00596f6c` · 推定シンボル `None` · 推定型 `None`
- [`008dafe4`](#insn-008dafe4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafe8`](#insn-008dafe8) → [`008daffc`](#insn-008daffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daff4`](#insn-008daff4) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008daff8`](#insn-008daff8) → [`008db0c8`](#insn-008db0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008daffc`](#insn-008daffc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db000`](#insn-008db000) → [`008db0e8`](#insn-008db0e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db008`](#insn-008db008) → [`008d615c`](../008d6/008d615c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008d615c` · 推定シンボル `None` · 推定型 `None`
- [`008db02c`](#insn-008db02c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db030`](#insn-008db030) → `Stack[-0x5c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db034`](#insn-008db034) → [`008db158`](#insn-008db158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db04c`](#insn-008db04c) → [`008db124`](#insn-008db124) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db060`](#insn-008db060) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db070`](#insn-008db070) → [`00865b4c`](../00865/00865b4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00865b4c` · 推定シンボル `None` · 推定型 `None`
- [`008db074`](#insn-008db074) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0a8`](#insn-008db0a8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0ac`](#insn-008db0ac) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0b0`](#insn-008db0b0) → [`008daf7c`](#insn-008daf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0b8`](#insn-008db0b8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0c0`](#insn-008db0c0) → [`008db1a0`](#insn-008db1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0c4`](#insn-008db0c4) → [`00459db4`](../00459/00459db4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459db4` · 推定シンボル `None` · 推定型 `None`
- [`008db0dc`](#insn-008db0dc) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008db0e0`](#insn-008db0e0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0e4`](#insn-008db0e4) → [`008db004`](#insn-008db004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db104`](#insn-008db104) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db108`](#insn-008db108) → `Stack[-0x5c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db10c`](#insn-008db10c) → [`008db158`](#insn-008db158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db124`](#insn-008db124) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db128`](#insn-008db128) → [`008daf90`](#insn-008daf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db134`](#insn-008db134) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008db138`](#insn-008db138) → [`008daf90`](#insn-008daf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db150`](#insn-008db150) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008db154`](#insn-008db154) → [`008daf90`](#insn-008daf90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db15c`](#insn-008db15c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db164`](#insn-008db164) → [`008db1a0`](#insn-008db1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db168`](#insn-008db168) → [`00459db4`](../00459/00459db4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459db4` · 推定シンボル `None` · 推定型 `None`
- [`008db1a0`](#insn-008db1a0) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008daf00`](#insn-008daf00)

~~~json
{
  "source": "008daf00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daf04`](#insn-008daf04)

~~~json
{
  "source": "008daf04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daf08`](#insn-008daf08)

~~~json
{
  "source": "008daf08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daf0c`](#insn-008daf0c)

~~~json
{
  "source": "008daf0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daf28`](#insn-008daf28)

~~~json
{
  "source": "008daf28",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daf64`](#insn-008daf64)

~~~json
{
  "source": "008daf64",
  "target": "008dafb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daf70`](#insn-008daf70)

~~~json
{
  "source": "008daf70",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daf74`](#insn-008daf74)

~~~json
{
  "source": "008daf74",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daf78`](#insn-008daf78)

~~~json
{
  "source": "008daf78",
  "target": "008db0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daf94`](#insn-008daf94)

~~~json
{
  "source": "008daf94",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daf9c`](#insn-008daf9c)

~~~json
{
  "source": "008daf9c",
  "target": "008db1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafa0`](#insn-008dafa0)

~~~json
{
  "source": "008dafa0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafa4`](#insn-008dafa4)

~~~json
{
  "source": "008dafa4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafa8`](#insn-008dafa8)

~~~json
{
  "source": "008dafa8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafac`](#insn-008dafac)

~~~json
{
  "source": "008dafac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafbc`](#insn-008dafbc)

~~~json
{
  "source": "008dafbc",
  "target": "008db050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafc4`](#insn-008dafc4)

~~~json
{
  "source": "008dafc4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafc8`](#insn-008dafc8)

~~~json
{
  "source": "008dafc8",
  "target": "008dafd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafd4`](#insn-008dafd4)

~~~json
{
  "source": "008dafd4",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dafe0`](#insn-008dafe0)

~~~json
{
  "source": "008dafe0",
  "target": "00596f6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dafe4`](#insn-008dafe4)

~~~json
{
  "source": "008dafe4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafe8`](#insn-008dafe8)

~~~json
{
  "source": "008dafe8",
  "target": "008daffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daff4`](#insn-008daff4)

~~~json
{
  "source": "008daff4",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008daff8`](#insn-008daff8)

~~~json
{
  "source": "008daff8",
  "target": "008db0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008daffc`](#insn-008daffc)

~~~json
{
  "source": "008daffc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db000`](#insn-008db000)

~~~json
{
  "source": "008db000",
  "target": "008db0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db008`](#insn-008db008)

~~~json
{
  "source": "008db008",
  "target": "008d615c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db02c`](#insn-008db02c)

~~~json
{
  "source": "008db02c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db030`](#insn-008db030)

~~~json
{
  "source": "008db030",
  "target": "Stack[-0x5c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db034`](#insn-008db034)

~~~json
{
  "source": "008db034",
  "target": "008db158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db04c`](#insn-008db04c)

~~~json
{
  "source": "008db04c",
  "target": "008db124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db060`](#insn-008db060)

~~~json
{
  "source": "008db060",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db070`](#insn-008db070)

~~~json
{
  "source": "008db070",
  "target": "00865b4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db074`](#insn-008db074)

~~~json
{
  "source": "008db074",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0a8`](#insn-008db0a8)

~~~json
{
  "source": "008db0a8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0ac`](#insn-008db0ac)

~~~json
{
  "source": "008db0ac",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0b0`](#insn-008db0b0)

~~~json
{
  "source": "008db0b0",
  "target": "008daf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0b8`](#insn-008db0b8)

~~~json
{
  "source": "008db0b8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0c0`](#insn-008db0c0)

~~~json
{
  "source": "008db0c0",
  "target": "008db1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0c4`](#insn-008db0c4)

~~~json
{
  "source": "008db0c4",
  "target": "00459db4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db0dc`](#insn-008db0dc)

~~~json
{
  "source": "008db0dc",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db0e0`](#insn-008db0e0)

~~~json
{
  "source": "008db0e0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0e4`](#insn-008db0e4)

~~~json
{
  "source": "008db0e4",
  "target": "008db004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db104`](#insn-008db104)

~~~json
{
  "source": "008db104",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db108`](#insn-008db108)

~~~json
{
  "source": "008db108",
  "target": "Stack[-0x5c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db10c`](#insn-008db10c)

~~~json
{
  "source": "008db10c",
  "target": "008db158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db124`](#insn-008db124)

~~~json
{
  "source": "008db124",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db128`](#insn-008db128)

~~~json
{
  "source": "008db128",
  "target": "008daf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db134`](#insn-008db134)

~~~json
{
  "source": "008db134",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db138`](#insn-008db138)

~~~json
{
  "source": "008db138",
  "target": "008daf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db150`](#insn-008db150)

~~~json
{
  "source": "008db150",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db154`](#insn-008db154)

~~~json
{
  "source": "008db154",
  "target": "008daf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db15c`](#insn-008db15c)

~~~json
{
  "source": "008db15c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db164`](#insn-008db164)

~~~json
{
  "source": "008db164",
  "target": "008db1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db168`](#insn-008db168)

~~~json
{
  "source": "008db168",
  "target": "00459db4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db1a0`](#insn-008db1a0)

~~~json
{
  "source": "008db1a0",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
