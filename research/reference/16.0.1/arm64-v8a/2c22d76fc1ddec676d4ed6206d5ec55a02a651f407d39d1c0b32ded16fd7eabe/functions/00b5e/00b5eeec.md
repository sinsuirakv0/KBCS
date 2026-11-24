# 00b5eeec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5eac4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5eac4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0008.md#compare-9cb15c4ce54e87be48a7860c3aa75b9a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b5ef88`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ef88.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0009.md#compare-4cc2bbfcd8cfe4b841d96d3dcfa950d2)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5eeec",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E",
  "size": 796,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f0d635067028b90e7d7377f8dfd9643c694de28f5e38c6e76b6b2396eda1ce46",
  "source_text_sha256": "f0d635067028b90e7d7377f8dfd9643c694de28f5e38c6e76b6b2396eda1ce46",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5eeec",
        "00b5f207"
      ]
    ],
    "bytes_sha256": "a5d9b260c82e3a2c57f4adf34b6a0d4bc7da78f6cf7719fa5a3f4dbf7ce50356",
    "instruction_count": 199,
    "instruction_bytes": 796,
    "body_bytes": 796,
    "indirect": 8,
    "unresolved": 8
  }
}
~~~

## 呼び出し元

- [00c5ae40](../00c5a/00c5ae40.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5aaa0](../00c5a/00c5aaa0.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac10](../00c5a/00c5ac10.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5b5e0](../00c5b/00c5b5e0.md)
- [00c5bc50](../00c5b/00c5bc50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4301 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
               (ulong *param_1,long *param_2,int param_3,undefined8 param_4,undefined8 param_5)

{
  long lVar1;
  undefined4 *puVar2;
  undefined8 *puVar3;
  long lVar4;
  ulong uVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  long *plVar9;
  undefined1 auStack_a8 [40];
  long *local_80;
  ulong uStack_78;
  long *local_70;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  puVar2 = (undefined4 *)_Znwm(0x70);
  *(undefined8 *)(puVar2 + 10) = param_4;
  *(undefined8 *)(puVar2 + 0xc) = param_5;
  *(undefined8 *)(puVar2 + 0xe) = 0;
  *(undefined8 *)(puVar2 + 0x10) = 0;
  *(undefined8 *)(puVar2 + 0x18) = 0;
  *(undefined8 *)(puVar2 + 0x1a) = 0;
  *puVar2 = 1;
  *(undefined8 *)(puVar2 + 3) = 0;
  *(undefined8 *)(puVar2 + 1) = 0;
  *(undefined8 *)(puVar2 + 7) = 0;
  *(undefined8 *)(puVar2 + 5) = 0;
  *(undefined8 *)(puVar2 + 0x12) = 0;
  *(undefined4 **)(puVar2 + 0x14) = puVar2 + 0x14;
  *(undefined4 **)(puVar2 + 0x16) = puVar2 + 0x14;
  _ZN8firebase5Mutex7AcquireEv(param_2 + 1);
  plVar6 = param_2 + 7;
  plVar7 = (long *)*plVar6;
  uVar5 = param_2[9];
  lVar4 = uVar5 + 1;
  if (uVar5 == 0xffffffffffffffff) {
    lVar4 = 1;
  }
  param_2[9] = lVar4;
  plVar9 = plVar6;
  if (plVar7 != (long *)0x0) {
    plVar6 = param_2 + 7;
    do {
      while (plVar8 = plVar7, plVar9 = plVar8, uVar5 < (ulong)plVar8[4]) {
        plVar6 = plVar8;
        plVar7 = (long *)*plVar8;
        if ((long *)*plVar8 == (long *)0x0) {
          lVar4 = *plVar8;
          goto joined_r0x00b5efd4;
        }
      }
      if (uVar5 <= (ulong)plVar8[4]) break;
      plVar6 = plVar8 + 1;
      plVar7 = (long *)*plVar6;
    } while ((long *)*plVar6 != (long *)0x0);
  }
  lVar4 = *plVar6;
  plVar8 = plVar6;
joined_r0x00b5efd4:
  if (lVar4 == 0) {
    puVar3 = (undefined8 *)_Znwm(0x30);
    puVar3[4] = uVar5;
    puVar3[5] = puVar2;
    *puVar3 = 0;
    puVar3[1] = 0;
    puVar3[2] = plVar9;
    *plVar8 = (long)puVar3;
    if (*(long *)param_2[6] != 0) {
      param_2[6] = *(long *)param_2[6];
      puVar3 = (undefined8 *)*plVar8;
    }
    _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_2[7],puVar3)
    ;
    param_2[8] = param_2[8] + 1;
    *param_1 = uVar5;
    param_1[1] = (ulong)param_2;
  }
  else {
    *param_1 = uVar5;
    param_1[1] = (ulong)param_2;
    if (param_2 == (long *)0x0) goto joined_r0x00b5f07c;
  }
  (**(code **)(*param_2 + 0x10))(param_2,param_1);
  _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E(param_1[1] + 200,param_1,FUN_00b60eac);
joined_r0x00b5f07c:
  if ((-1 < param_3) && (param_3 < (int)((ulong)(param_2[0xb] - param_2[10]) >> 6))) {
    _ZN8firebase5MutexC1ENS0_4ModeE(auStack_a8,0);
    uStack_78 = *param_1;
    local_70 = (long *)param_1[1];
    local_80 = param_2;
    if (local_70 != (long *)0x0) {
      (**(code **)(*local_70 + 0x10))(local_70,&uStack_78);
      _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E
                (local_70 + 0x19,&uStack_78,FUN_00b60eac);
    }
    (**(code **)(*local_80 + 0x10))(local_80,&uStack_78);
    if (local_70 != (long *)0x0) {
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(local_70 + 0x19,&uStack_78);
      (**(code **)(*local_70 + 0x18))(local_70,&uStack_78);
      local_70 = (long *)0x0;
    }
    if (local_80 != (long *)0x0) {
      (**(code **)(*local_80 + 0x58))(local_80,auStack_a8);
    }
    _ZN8firebase10FutureBaseaSEOS0_(param_2[10] + (long)param_3 * 0x40,auStack_a8);
    _ZN8firebase5Mutex7AcquireEv(auStack_a8);
    if (local_80 != (long *)0x0) {
      (**(code **)(*local_80 + 0x60))(local_80,auStack_a8);
      (**(code **)(*local_80 + 0x18))(local_80,&uStack_78);
      local_80 = (long *)0x0;
    }
    _ZN8firebase5Mutex7ReleaseEv(auStack_a8);
    if (local_70 != (long *)0x0) {
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(local_70 + 0x19,&uStack_78);
      plVar6 = local_70;
      local_70 = (long *)0x0;
      (**(code **)(*plVar6 + 0x18))(plVar6,&uStack_78);
    }
    _ZN8firebase5MutexD1Ev(auStack_a8);
  }
  _ZN8firebase5Mutex7ReleaseEv(param_2 + 1);
  if (*(long *)(lVar1 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5eeec"></a> `00b5eeec` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00b5eef0"></a> `00b5eef0` | `fb 2b 00 f9` | str x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b5eef4"></a> `00b5eef4` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b5eef8"></a> `00b5eef8` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b5eefc"></a> `00b5eefc` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b5ef00"></a> `00b5ef00` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b5ef04"></a> `00b5ef04` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b5ef08"></a> `00b5ef08` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b5ef0c"></a> `00b5ef0c` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b5ef10"></a> `00b5ef10` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00b5ef14"></a> `00b5ef14` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00b5ef18"></a> `00b5ef18` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b5ef1c"></a> `00b5ef1c` | `00 0e 80 52` | mov w0,#0x70 | `FALL_THROUGH`
<a id="insn-00b5ef20"></a> `00b5ef20` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-00b5ef24"></a> `00b5ef24` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00b5ef28"></a> `00b5ef28` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00b5ef2c"></a> `00b5ef2c` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00b5ef30"></a> `00b5ef30` | `d8 e3 03 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ef34"></a> `00b5ef34` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5ef38"></a> `00b5ef38` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00b5ef3c"></a> `00b5ef3c` | `18 cc 02 a9` | stp x24,x19,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00b5ef40"></a> `00b5ef40` | `09 40 01 91` | add x9,x0,#0x50 | `FALL_THROUGH`
<a id="insn-00b5ef44"></a> `00b5ef44` | `b3 22 00 91` | add x19,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00b5ef48"></a> `00b5ef48` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00b5ef4c"></a> `00b5ef4c` | `1f fc 03 a9` | stp xzr,xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00b5ef50"></a> `00b5ef50` | `1f 7c 06 a9` | stp xzr,xzr,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00b5ef54"></a> `00b5ef54` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00b5ef58"></a> `00b5ef58` | `00 40 80 3c` | stur q0,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00b5ef5c"></a> `00b5ef5c` | `00 40 81 3c` | stur q0,[x0, #0x14] | `FALL_THROUGH`
<a id="insn-00b5ef60"></a> `00b5ef60` | `1f a4 04 a9` | stp xzr,x9,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00b5ef64"></a> `00b5ef64` | `09 2c 00 f9` | str x9,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00b5ef68"></a> `00b5ef68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5ef6c"></a> `00b5ef6c` | `a5 ee 03 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ef70"></a> `00b5ef70` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00b5ef74"></a> `00b5ef74` | `5b 8f 43 f8` | ldr x27,[x26, #0x38]! | `FALL_THROUGH`
<a id="insn-00b5ef78"></a> `00b5ef78` | `58 0b 40 f9` | ldr x24,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ef7c"></a> `00b5ef7c` | `08 07 00 b1` | adds x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00b5ef80"></a> `00b5ef80` | `08 35 9f 9a` | csinc x8,x8,xzr,cc | `FALL_THROUGH`
<a id="insn-00b5ef84"></a> `00b5ef84` | `48 0b 00 f9` | str x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ef88"></a> `00b5ef88` | `3b 02 00 b4` | cbz x27,0x00b5efcc | `CONDITIONAL_JUMP`
<a id="insn-00b5ef8c"></a> `00b5ef8c` | `ba e2 00 91` | add x26,x21,#0x38 | `FALL_THROUGH`
<a id="insn-00b5ef90"></a> `00b5ef90` | `68 13 40 f9` | ldr x8,[x27, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ef94"></a> `00b5ef94` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00b5ef98"></a> `00b5ef98` | `c2 00 00 54` | b.cs 0x00b5efb0 | `CONDITIONAL_JUMP`
<a id="insn-00b5ef9c"></a> `00b5ef9c` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00b5efa0"></a> `00b5efa0` | `88 02 00 b4` | cbz x8,0x00b5eff0 | `CONDITIONAL_JUMP`
<a id="insn-00b5efa4"></a> `00b5efa4` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00b5efa8"></a> `00b5efa8` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00b5efac"></a> `00b5efac` | `f9 ff ff 17` | b 0x00b5ef90 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5efb0"></a> `00b5efb0` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00b5efb4"></a> `00b5efb4` | `e2 00 00 54` | b.cs 0x00b5efd0 | `CONDITIONAL_JUMP`
<a id="insn-00b5efb8"></a> `00b5efb8` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00b5efbc"></a> `00b5efbc` | `48 8f 40 f8` | ldr x8,[x26, #0x8]! | `FALL_THROUGH`
<a id="insn-00b5efc0"></a> `00b5efc0` | `88 00 00 b4` | cbz x8,0x00b5efd0 | `CONDITIONAL_JUMP`
<a id="insn-00b5efc4"></a> `00b5efc4` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00b5efc8"></a> `00b5efc8` | `f2 ff ff 17` | b 0x00b5ef90 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5efcc"></a> `00b5efcc` | `fb 03 1a aa` | mov x27,x26 | `FALL_THROUGH`
<a id="insn-00b5efd0"></a> `00b5efd0` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00b5efd4"></a> `00b5efd4` | `48 01 00 b4` | cbz x8,0x00b5effc | `CONDITIONAL_JUMP`
<a id="insn-00b5efd8"></a> `00b5efd8` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00b5efdc"></a> `00b5efdc` | `d8 02 00 f9` | str x24,[x22] | `FALL_THROUGH`
<a id="insn-00b5efe0"></a> `00b5efe0` | `f5 8e 00 f8` | str x21,[x23, #0x8]! | `FALL_THROUGH`
<a id="insn-00b5efe4"></a> `00b5efe4` | `75 03 00 b5` | cbnz x21,0x00b5f050 | `CONDITIONAL_JUMP`
<a id="insn-00b5efe8"></a> `00b5efe8` | `d4 04 f8 36` | tbz w20,#0x1f,0x00b5f080 | `CONDITIONAL_JUMP`
<a id="insn-00b5efec"></a> `00b5efec` | `78 00 00 14` | b 0x00b5f1cc | `UNCONDITIONAL_JUMP`
<a id="insn-00b5eff0"></a> `00b5eff0` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00b5eff4"></a> `00b5eff4` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00b5eff8"></a> `00b5eff8` | `08 ff ff b5` | cbnz x8,0x00b5efd8 | `CONDITIONAL_JUMP`
<a id="insn-00b5effc"></a> `00b5effc` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-00b5f000"></a> `00b5f000` | `a4 e3 03 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f004"></a> `00b5f004` | `18 5c 02 a9` | stp x24,x23,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b5f008"></a> `00b5f008` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b5f00c"></a> `00b5f00c` | `1b 08 00 f9` | str x27,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b5f010"></a> `00b5f010` | `40 03 00 f9` | str x0,[x26] | `FALL_THROUGH`
<a id="insn-00b5f014"></a> `00b5f014` | `a8 1a 40 f9` | ldr x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00b5f018"></a> `00b5f018` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00b5f01c"></a> `00b5f01c` | `88 00 00 b4` | cbz x8,0x00b5f02c | `CONDITIONAL_JUMP`
<a id="insn-00b5f020"></a> `00b5f020` | `a8 1a 00 f9` | str x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00b5f024"></a> `00b5f024` | `41 03 40 f9` | ldr x1,[x26] | `FALL_THROUGH`
<a id="insn-00b5f028"></a> `00b5f028` | `02 00 00 14` | b 0x00b5f030 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5f02c"></a> `00b5f02c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00b5f030"></a> `00b5f030` | `a0 1e 40 f9` | ldr x0,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00b5f034"></a> `00b5f034` | `6b f1 03 94` | bl 0x00c5b5e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f038"></a> `00b5f038` | `a8 22 40 f9` | ldr x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00b5f03c"></a> `00b5f03c` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00b5f040"></a> `00b5f040` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5f044"></a> `00b5f044` | `a8 22 00 f9` | str x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00b5f048"></a> `00b5f048` | `f8 86 00 f8` | str x24,[x23], #0x8 | `FALL_THROUGH`
<a id="insn-00b5f04c"></a> `00b5f04c` | `f5 02 00 f9` | str x21,[x23] | `FALL_THROUGH`
<a id="insn-00b5f050"></a> `00b5f050` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b5f054"></a> `00b5f054` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5f058"></a> `00b5f058` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5f05c"></a> `00b5f05c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b5f060"></a> `00b5f060` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5f064"></a> `00b5f064` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00b5f068"></a> `00b5f068` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00b5f06c"></a> `00b5f06c` | `02 f2 00 10` | adr x2,0xb60eac | `FALL_THROUGH`
<a id="insn-00b5f070"></a> `00b5f070` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5f074"></a> `00b5f074` | `00 21 03 91` | add x0,x8,#0xc8 | `FALL_THROUGH`
<a id="insn-00b5f078"></a> `00b5f078` | `e2 ee 03 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f07c"></a> `00b5f07c` | `94 0a f8 37` | tbnz w20,#0x1f,0x00b5f1cc | `CONDITIONAL_JUMP`
<a id="insn-00b5f080"></a> `00b5f080` | `a8 26 45 a9` | ldp x8,x9,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-00b5f084"></a> `00b5f084` | `28 01 08 cb` | sub x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00b5f088"></a> `00b5f088` | `08 fd 46 d3` | lsr x8,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00b5f08c"></a> `00b5f08c` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-00b5f090"></a> `00b5f090` | `ed 09 00 54` | b.le 0x00b5f1cc | `CONDITIONAL_JUMP`
<a id="insn-00b5f094"></a> `00b5f094` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5f098"></a> `00b5f098` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b5f09c"></a> `00b5f09c` | `f8 23 00 91` | add x24,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5f0a0"></a> `00b5f0a0` | `f4 ee 03 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f0a4"></a> `00b5f0a4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00b5f0a8"></a> `00b5f0a8` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00b5f0ac"></a> `00b5f0ac` | `16 c3 00 91` | add x22,x24,#0x30 | `FALL_THROUGH`
<a id="insn-00b5f0b0"></a> `00b5f0b0` | `f5 23 03 a9` | stp x21,x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5f0b4"></a> `00b5f0b4` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00b5f0b8"></a> `00b5f0b8` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5f0bc"></a> `00b5f0bc` | `80 01 00 b4` | cbz x0,0x00b5f0ec | `CONDITIONAL_JUMP`
<a id="insn-00b5f0c0"></a> `00b5f0c0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5f0c4"></a> `00b5f0c4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5f0c8"></a> `00b5f0c8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b5f0cc"></a> `00b5f0cc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5f0d0"></a> `00b5f0d0` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5f0d4"></a> `00b5f0d4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00b5f0d8"></a> `00b5f0d8` | `a2 ee 00 10` | adr x2,0xb60eac | `FALL_THROUGH`
<a id="insn-00b5f0dc"></a> `00b5f0dc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5f0e0"></a> `00b5f0e0` | `00 21 03 91` | add x0,x8,#0xc8 | `FALL_THROUGH`
<a id="insn-00b5f0e4"></a> `00b5f0e4` | `c7 ee 03 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f0e8"></a> `00b5f0e8` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5f0ec"></a> `00b5f0ec` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00b5f0f0"></a> `00b5f0f0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b5f0f4"></a> `00b5f0f4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5f0f8"></a> `00b5f0f8` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00b5f0fc"></a> `00b5f0fc` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00b5f100"></a> `00b5f100` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5f104"></a> `00b5f104` | `48 01 00 b4` | cbz x8,0x00b5f12c | `CONDITIONAL_JUMP`
<a id="insn-00b5f108"></a> `00b5f108` | `00 21 03 91` | add x0,x8,#0xc8 | `FALL_THROUGH`
<a id="insn-00b5f10c"></a> `00b5f10c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5f110"></a> `00b5f110` | `c0 ee 03 94` | bl 0x00c5ac10 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f114"></a> `00b5f114` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5f118"></a> `00b5f118` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5f11c"></a> `00b5f11c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5f120"></a> `00b5f120` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b5f124"></a> `00b5f124` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5f128"></a> `00b5f128` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5f12c"></a> `00b5f12c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5f130"></a> `00b5f130` | `a0 00 00 b4` | cbz x0,0x00b5f144 | `CONDITIONAL_JUMP`
<a id="insn-00b5f134"></a> `00b5f134` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5f138"></a> `00b5f138` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5f13c"></a> `00b5f13c` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00b5f140"></a> `00b5f140` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5f144"></a> `00b5f144` | `a8 2a 40 f9` | ldr x8,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-00b5f148"></a> `00b5f148` | `89 7e 40 93` | sxtw x9,w20 | `FALL_THROUGH`
<a id="insn-00b5f14c"></a> `00b5f14c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5f150"></a> `00b5f150` | `00 19 09 8b` | add x0,x8,x9, LSL #0x6 | `FALL_THROUGH`
<a id="insn-00b5f154"></a> `00b5f154` | `bf f2 03 94` | bl 0x00c5bc50 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f158"></a> `00b5f158` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5f15c"></a> `00b5f15c` | `29 ee 03 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f160"></a> `00b5f160` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5f164"></a> `00b5f164` | `60 01 00 b4` | cbz x0,0x00b5f190 | `CONDITIONAL_JUMP`
<a id="insn-00b5f168"></a> `00b5f168` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5f16c"></a> `00b5f16c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5f170"></a> `00b5f170` | `08 31 40 f9` | ldr x8,[x8, #0x60] | `FALL_THROUGH`
<a id="insn-00b5f174"></a> `00b5f174` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5f178"></a> `00b5f178` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5f17c"></a> `00b5f17c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5f180"></a> `00b5f180` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5f184"></a> `00b5f184` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b5f188"></a> `00b5f188` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5f18c"></a> `00b5f18c` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5f190"></a> `00b5f190` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5f194"></a> `00b5f194` | `1f ee 03 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f198"></a> `00b5f198` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5f19c"></a> `00b5f19c` | `48 01 00 b4` | cbz x8,0x00b5f1c4 | `CONDITIONAL_JUMP`
<a id="insn-00b5f1a0"></a> `00b5f1a0` | `00 21 03 91` | add x0,x8,#0xc8 | `FALL_THROUGH`
<a id="insn-00b5f1a4"></a> `00b5f1a4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5f1a8"></a> `00b5f1a8` | `9a ee 03 94` | bl 0x00c5ac10 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f1ac"></a> `00b5f1ac` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5f1b0"></a> `00b5f1b0` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5f1b4"></a> `00b5f1b4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5f1b8"></a> `00b5f1b8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5f1bc"></a> `00b5f1bc` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b5f1c0"></a> `00b5f1c0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5f1c4"></a> `00b5f1c4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5f1c8"></a> `00b5f1c8` | `36 ee 03 94` | bl 0x00c5aaa0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f1cc"></a> `00b5f1cc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5f1d0"></a> `00b5f1d0` | `10 ee 03 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00b5f1d4"></a> `00b5f1d4` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00b5f1d8"></a> `00b5f1d8` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00b5f1dc"></a> `00b5f1dc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b5f1e0"></a> `00b5f1e0` | `21 01 00 54` | b.ne 0x00b5f204 | `CONDITIONAL_JUMP`
<a id="insn-00b5f1e4"></a> `00b5f1e4` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b5f1e8"></a> `00b5f1e8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b5f1ec"></a> `00b5f1ec` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b5f1f0"></a> `00b5f1f0` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b5f1f4"></a> `00b5f1f4` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b5f1f8"></a> `00b5f1f8` | `fb 2b 40 f9` | ldr x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b5f1fc"></a> `00b5f1fc` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00b5f200"></a> `00b5f200` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5f204"></a> `00b5f204` | `37 e3 03 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5eeec`](#insn-00b5eeec) 範囲 `[['00b5eeec', '00b5ef8b']]`
  - `CONDITIONAL_JUMP` [`00b5ef88`](#insn-00b5ef88) → [`00b5efcc`](#insn-00b5efcc)
  - `FALL_THROUGH` [`00b5ef88`](#insn-00b5ef88) → [`00b5ef8c`](#insn-00b5ef8c)
- ブロック [`00b5ef8c`](#insn-00b5ef8c) 範囲 `[['00b5ef8c', '00b5ef8f']]`
  - `FALL_THROUGH` [`00b5ef8c`](#insn-00b5ef8c) → [`00b5ef90`](#insn-00b5ef90)
- ブロック [`00b5ef90`](#insn-00b5ef90) 範囲 `[['00b5ef90', '00b5ef9b']]`
  - `CONDITIONAL_JUMP` [`00b5ef98`](#insn-00b5ef98) → [`00b5efb0`](#insn-00b5efb0)
  - `FALL_THROUGH` [`00b5ef98`](#insn-00b5ef98) → [`00b5ef9c`](#insn-00b5ef9c)
- ブロック [`00b5ef9c`](#insn-00b5ef9c) 範囲 `[['00b5ef9c', '00b5efa3']]`
  - `CONDITIONAL_JUMP` [`00b5efa0`](#insn-00b5efa0) → [`00b5eff0`](#insn-00b5eff0)
  - `FALL_THROUGH` [`00b5efa0`](#insn-00b5efa0) → [`00b5efa4`](#insn-00b5efa4)
- ブロック [`00b5efa4`](#insn-00b5efa4) 範囲 `[['00b5efa4', '00b5efaf']]`
  - `UNCONDITIONAL_JUMP` [`00b5efac`](#insn-00b5efac) → [`00b5ef90`](#insn-00b5ef90)
- ブロック [`00b5efb0`](#insn-00b5efb0) 範囲 `[['00b5efb0', '00b5efb7']]`
  - `CONDITIONAL_JUMP` [`00b5efb4`](#insn-00b5efb4) → [`00b5efd0`](#insn-00b5efd0)
  - `FALL_THROUGH` [`00b5efb4`](#insn-00b5efb4) → [`00b5efb8`](#insn-00b5efb8)
- ブロック [`00b5efb8`](#insn-00b5efb8) 範囲 `[['00b5efb8', '00b5efc3']]`
  - `CONDITIONAL_JUMP` [`00b5efc0`](#insn-00b5efc0) → [`00b5efd0`](#insn-00b5efd0)
  - `FALL_THROUGH` [`00b5efc0`](#insn-00b5efc0) → [`00b5efc4`](#insn-00b5efc4)
- ブロック [`00b5efc4`](#insn-00b5efc4) 範囲 `[['00b5efc4', '00b5efcb']]`
  - `UNCONDITIONAL_JUMP` [`00b5efc8`](#insn-00b5efc8) → [`00b5ef90`](#insn-00b5ef90)
- ブロック [`00b5efcc`](#insn-00b5efcc) 範囲 `[['00b5efcc', '00b5efcf']]`
  - `FALL_THROUGH` [`00b5efcc`](#insn-00b5efcc) → [`00b5efd0`](#insn-00b5efd0)
- ブロック [`00b5efd0`](#insn-00b5efd0) 範囲 `[['00b5efd0', '00b5efd7']]`
  - `CONDITIONAL_JUMP` [`00b5efd4`](#insn-00b5efd4) → [`00b5effc`](#insn-00b5effc)
  - `FALL_THROUGH` [`00b5efd4`](#insn-00b5efd4) → [`00b5efd8`](#insn-00b5efd8)
- ブロック [`00b5efd8`](#insn-00b5efd8) 範囲 `[['00b5efd8', '00b5efe7']]`
  - `CONDITIONAL_JUMP` [`00b5efe4`](#insn-00b5efe4) → [`00b5f050`](#insn-00b5f050)
  - `FALL_THROUGH` [`00b5efe4`](#insn-00b5efe4) → [`00b5efe8`](#insn-00b5efe8)
- ブロック [`00b5efe8`](#insn-00b5efe8) 範囲 `[['00b5efe8', '00b5efeb']]`
  - `CONDITIONAL_JUMP` [`00b5efe8`](#insn-00b5efe8) → [`00b5f080`](#insn-00b5f080)
  - `FALL_THROUGH` [`00b5efe8`](#insn-00b5efe8) → [`00b5efec`](#insn-00b5efec)
- ブロック [`00b5efec`](#insn-00b5efec) 範囲 `[['00b5efec', '00b5efef']]`
  - `UNCONDITIONAL_JUMP` [`00b5efec`](#insn-00b5efec) → [`00b5f1cc`](#insn-00b5f1cc)
- ブロック [`00b5eff0`](#insn-00b5eff0) 範囲 `[['00b5eff0', '00b5effb']]`
  - `CONDITIONAL_JUMP` [`00b5eff8`](#insn-00b5eff8) → [`00b5efd8`](#insn-00b5efd8)
  - `FALL_THROUGH` [`00b5eff8`](#insn-00b5eff8) → [`00b5effc`](#insn-00b5effc)
- ブロック [`00b5effc`](#insn-00b5effc) 範囲 `[['00b5effc', '00b5f01f']]`
  - `CONDITIONAL_JUMP` [`00b5f01c`](#insn-00b5f01c) → [`00b5f02c`](#insn-00b5f02c)
  - `FALL_THROUGH` [`00b5f01c`](#insn-00b5f01c) → [`00b5f020`](#insn-00b5f020)
- ブロック [`00b5f020`](#insn-00b5f020) 範囲 `[['00b5f020', '00b5f02b']]`
  - `UNCONDITIONAL_JUMP` [`00b5f028`](#insn-00b5f028) → [`00b5f030`](#insn-00b5f030)
- ブロック [`00b5f02c`](#insn-00b5f02c) 範囲 `[['00b5f02c', '00b5f02f']]`
  - `FALL_THROUGH` [`00b5f02c`](#insn-00b5f02c) → [`00b5f030`](#insn-00b5f030)
- ブロック [`00b5f030`](#insn-00b5f030) 範囲 `[['00b5f030', '00b5f04f']]`
  - `FALL_THROUGH` [`00b5f04c`](#insn-00b5f04c) → [`00b5f050`](#insn-00b5f050)
- ブロック [`00b5f050`](#insn-00b5f050) 範囲 `[['00b5f050', '00b5f07f']]`
  - `CONDITIONAL_JUMP` [`00b5f07c`](#insn-00b5f07c) → [`00b5f1cc`](#insn-00b5f1cc)
  - `FALL_THROUGH` [`00b5f07c`](#insn-00b5f07c) → [`00b5f080`](#insn-00b5f080)
- ブロック [`00b5f080`](#insn-00b5f080) 範囲 `[['00b5f080', '00b5f093']]`
  - `CONDITIONAL_JUMP` [`00b5f090`](#insn-00b5f090) → [`00b5f1cc`](#insn-00b5f1cc)
  - `FALL_THROUGH` [`00b5f090`](#insn-00b5f090) → [`00b5f094`](#insn-00b5f094)
- ブロック [`00b5f094`](#insn-00b5f094) 範囲 `[['00b5f094', '00b5f0bf']]`
  - `CONDITIONAL_JUMP` [`00b5f0bc`](#insn-00b5f0bc) → [`00b5f0ec`](#insn-00b5f0ec)
  - `FALL_THROUGH` [`00b5f0bc`](#insn-00b5f0bc) → [`00b5f0c0`](#insn-00b5f0c0)
- ブロック [`00b5f0c0`](#insn-00b5f0c0) 範囲 `[['00b5f0c0', '00b5f0eb']]`
  - `FALL_THROUGH` [`00b5f0e8`](#insn-00b5f0e8) → [`00b5f0ec`](#insn-00b5f0ec)
- ブロック [`00b5f0ec`](#insn-00b5f0ec) 範囲 `[['00b5f0ec', '00b5f107']]`
  - `CONDITIONAL_JUMP` [`00b5f104`](#insn-00b5f104) → [`00b5f12c`](#insn-00b5f12c)
  - `FALL_THROUGH` [`00b5f104`](#insn-00b5f104) → [`00b5f108`](#insn-00b5f108)
- ブロック [`00b5f108`](#insn-00b5f108) 範囲 `[['00b5f108', '00b5f12b']]`
  - `FALL_THROUGH` [`00b5f128`](#insn-00b5f128) → [`00b5f12c`](#insn-00b5f12c)
- ブロック [`00b5f12c`](#insn-00b5f12c) 範囲 `[['00b5f12c', '00b5f133']]`
  - `CONDITIONAL_JUMP` [`00b5f130`](#insn-00b5f130) → [`00b5f144`](#insn-00b5f144)
  - `FALL_THROUGH` [`00b5f130`](#insn-00b5f130) → [`00b5f134`](#insn-00b5f134)
- ブロック [`00b5f134`](#insn-00b5f134) 範囲 `[['00b5f134', '00b5f143']]`
  - `FALL_THROUGH` [`00b5f140`](#insn-00b5f140) → [`00b5f144`](#insn-00b5f144)
- ブロック [`00b5f144`](#insn-00b5f144) 範囲 `[['00b5f144', '00b5f167']]`
  - `CONDITIONAL_JUMP` [`00b5f164`](#insn-00b5f164) → [`00b5f190`](#insn-00b5f190)
  - `FALL_THROUGH` [`00b5f164`](#insn-00b5f164) → [`00b5f168`](#insn-00b5f168)
- ブロック [`00b5f168`](#insn-00b5f168) 範囲 `[['00b5f168', '00b5f18f']]`
  - `FALL_THROUGH` [`00b5f18c`](#insn-00b5f18c) → [`00b5f190`](#insn-00b5f190)
- ブロック [`00b5f190`](#insn-00b5f190) 範囲 `[['00b5f190', '00b5f19f']]`
  - `CONDITIONAL_JUMP` [`00b5f19c`](#insn-00b5f19c) → [`00b5f1c4`](#insn-00b5f1c4)
  - `FALL_THROUGH` [`00b5f19c`](#insn-00b5f19c) → [`00b5f1a0`](#insn-00b5f1a0)
- ブロック [`00b5f1a0`](#insn-00b5f1a0) 範囲 `[['00b5f1a0', '00b5f1c3']]`
  - `FALL_THROUGH` [`00b5f1c0`](#insn-00b5f1c0) → [`00b5f1c4`](#insn-00b5f1c4)
- ブロック [`00b5f1c4`](#insn-00b5f1c4) 範囲 `[['00b5f1c4', '00b5f1cb']]`
  - `FALL_THROUGH` [`00b5f1c8`](#insn-00b5f1c8) → [`00b5f1cc`](#insn-00b5f1cc)
- ブロック [`00b5f1cc`](#insn-00b5f1cc) 範囲 `[['00b5f1cc', '00b5f1e3']]`
  - `CONDITIONAL_JUMP` [`00b5f1e0`](#insn-00b5f1e0) → [`00b5f204`](#insn-00b5f204)
  - `FALL_THROUGH` [`00b5f1e0`](#insn-00b5f1e0) → [`00b5f1e4`](#insn-00b5f1e4)
- ブロック [`00b5f1e4`](#insn-00b5f1e4) 範囲 `[['00b5f1e4', '00b5f203']]`
- ブロック [`00b5f204`](#insn-00b5f204) 範囲 `[['00b5f204', '00b5f207']]`

## 命令位置別の参照

- [`00b5eef0`](#insn-00b5eef0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5eef4`](#insn-00b5eef4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5eef8`](#insn-00b5eef8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5eefc`](#insn-00b5eefc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ef00`](#insn-00b5ef00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ef04`](#insn-00b5ef04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ef2c`](#insn-00b5ef2c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ef30`](#insn-00b5ef30) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00b5ef6c`](#insn-00b5ef6c) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00b5ef88`](#insn-00b5ef88) → [`00b5efcc`](#insn-00b5efcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ef98`](#insn-00b5ef98) → [`00b5efb0`](#insn-00b5efb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5efa0`](#insn-00b5efa0) → [`00b5eff0`](#insn-00b5eff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5efac`](#insn-00b5efac) → [`00b5ef90`](#insn-00b5ef90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5efb4`](#insn-00b5efb4) → [`00b5efd0`](#insn-00b5efd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5efc0`](#insn-00b5efc0) → [`00b5efd0`](#insn-00b5efd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5efc8`](#insn-00b5efc8) → [`00b5ef90`](#insn-00b5ef90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5efd4`](#insn-00b5efd4) → [`00b5effc`](#insn-00b5effc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5efe4`](#insn-00b5efe4) → [`00b5f050`](#insn-00b5f050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5efe8`](#insn-00b5efe8) → [`00b5f080`](#insn-00b5f080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5efec`](#insn-00b5efec) → [`00b5f1cc`](#insn-00b5f1cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5eff8`](#insn-00b5eff8) → [`00b5efd8`](#insn-00b5efd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f000`](#insn-00b5f000) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00b5f01c`](#insn-00b5f01c) → [`00b5f02c`](#insn-00b5f02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f028`](#insn-00b5f028) → [`00b5f030`](#insn-00b5f030) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f034`](#insn-00b5f034) → [`00c5b5e0`](../00c5b/00c5b5e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5e0` · 推定シンボル `None` · 推定型 `None`
- [`00b5f06c`](#insn-00b5f06c) → [`00b60eac`](../00b60/00b60eac.md) · `PARAM` · `ANALYSIS` · 関数 `00b60eac` · 推定シンボル `None` · 推定型 `None`
- [`00b5f078`](#insn-00b5f078) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00b5f07c`](#insn-00b5f07c) → [`00b5f1cc`](#insn-00b5f1cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f090`](#insn-00b5f090) → [`00b5f1cc`](#insn-00b5f1cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f0a0`](#insn-00b5f0a0) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00b5f0b0`](#insn-00b5f0b0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f0b8`](#insn-00b5f0b8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f0bc`](#insn-00b5f0bc) → [`00b5f0ec`](#insn-00b5f0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f0d0`](#insn-00b5f0d0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f0d8`](#insn-00b5f0d8) → [`00b60eac`](../00b60/00b60eac.md) · `PARAM` · `ANALYSIS` · 関数 `00b60eac` · 推定シンボル `None` · 推定型 `None`
- [`00b5f0e4`](#insn-00b5f0e4) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00b5f0e8`](#insn-00b5f0e8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f100`](#insn-00b5f100) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f104`](#insn-00b5f104) → [`00b5f12c`](#insn-00b5f12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f110`](#insn-00b5f110) → [`00c5ac10`](../00c5a/00c5ac10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac10` · 推定シンボル `None` · 推定型 `None`
- [`00b5f114`](#insn-00b5f114) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f128`](#insn-00b5f128) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f12c`](#insn-00b5f12c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f130`](#insn-00b5f130) → [`00b5f144`](#insn-00b5f144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f154`](#insn-00b5f154) → [`00c5bc50`](../00c5b/00c5bc50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc50` · 推定シンボル `None` · 推定型 `None`
- [`00b5f15c`](#insn-00b5f15c) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00b5f160`](#insn-00b5f160) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f164`](#insn-00b5f164) → [`00b5f190`](#insn-00b5f190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f178`](#insn-00b5f178) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f18c`](#insn-00b5f18c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f194`](#insn-00b5f194) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00b5f198`](#insn-00b5f198) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f19c`](#insn-00b5f19c) → [`00b5f1c4`](#insn-00b5f1c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1a8`](#insn-00b5f1a8) → [`00c5ac10`](../00c5a/00c5ac10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac10` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1ac`](#insn-00b5f1ac) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1b0`](#insn-00b5f1b0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1c8`](#insn-00b5f1c8) → [`00c5aaa0`](../00c5a/00c5aaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aaa0` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1d0`](#insn-00b5f1d0) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1d8`](#insn-00b5f1d8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1e0`](#insn-00b5f1e0) → [`00b5f204`](#insn-00b5f204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1e4`](#insn-00b5f1e4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1e8`](#insn-00b5f1e8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1ec`](#insn-00b5f1ec) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1f0`](#insn-00b5f1f0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1f4`](#insn-00b5f1f4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f1f8`](#insn-00b5f1f8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5f204`](#insn-00b5f204) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5eef0`](#insn-00b5eef0)

~~~json
{
  "source": "00b5eef0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5eef4`](#insn-00b5eef4)

~~~json
{
  "source": "00b5eef4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5eef8`](#insn-00b5eef8)

~~~json
{
  "source": "00b5eef8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5eefc`](#insn-00b5eefc)

~~~json
{
  "source": "00b5eefc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ef00`](#insn-00b5ef00)

~~~json
{
  "source": "00b5ef00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ef04`](#insn-00b5ef04)

~~~json
{
  "source": "00b5ef04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ef2c`](#insn-00b5ef2c)

~~~json
{
  "source": "00b5ef2c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ef30`](#insn-00b5ef30)

~~~json
{
  "source": "00b5ef30",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ef6c`](#insn-00b5ef6c)

~~~json
{
  "source": "00b5ef6c",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ef88`](#insn-00b5ef88)

~~~json
{
  "source": "00b5ef88",
  "target": "00b5efcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ef98`](#insn-00b5ef98)

~~~json
{
  "source": "00b5ef98",
  "target": "00b5efb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5efa0`](#insn-00b5efa0)

~~~json
{
  "source": "00b5efa0",
  "target": "00b5eff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5efac`](#insn-00b5efac)

~~~json
{
  "source": "00b5efac",
  "target": "00b5ef90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5efb4`](#insn-00b5efb4)

~~~json
{
  "source": "00b5efb4",
  "target": "00b5efd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5efc0`](#insn-00b5efc0)

~~~json
{
  "source": "00b5efc0",
  "target": "00b5efd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5efc8`](#insn-00b5efc8)

~~~json
{
  "source": "00b5efc8",
  "target": "00b5ef90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5efd4`](#insn-00b5efd4)

~~~json
{
  "source": "00b5efd4",
  "target": "00b5effc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5efe4`](#insn-00b5efe4)

~~~json
{
  "source": "00b5efe4",
  "target": "00b5f050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5efe8`](#insn-00b5efe8)

~~~json
{
  "source": "00b5efe8",
  "target": "00b5f080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5efec`](#insn-00b5efec)

~~~json
{
  "source": "00b5efec",
  "target": "00b5f1cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5eff8`](#insn-00b5eff8)

~~~json
{
  "source": "00b5eff8",
  "target": "00b5efd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f000`](#insn-00b5f000)

~~~json
{
  "source": "00b5f000",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f01c`](#insn-00b5f01c)

~~~json
{
  "source": "00b5f01c",
  "target": "00b5f02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f028`](#insn-00b5f028)

~~~json
{
  "source": "00b5f028",
  "target": "00b5f030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f034`](#insn-00b5f034)

~~~json
{
  "source": "00b5f034",
  "target": "00c5b5e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f06c`](#insn-00b5f06c)

~~~json
{
  "source": "00b5f06c",
  "target": "00b60eac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f078`](#insn-00b5f078)

~~~json
{
  "source": "00b5f078",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f07c`](#insn-00b5f07c)

~~~json
{
  "source": "00b5f07c",
  "target": "00b5f1cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f090`](#insn-00b5f090)

~~~json
{
  "source": "00b5f090",
  "target": "00b5f1cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f0a0`](#insn-00b5f0a0)

~~~json
{
  "source": "00b5f0a0",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f0b0`](#insn-00b5f0b0)

~~~json
{
  "source": "00b5f0b0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f0b8`](#insn-00b5f0b8)

~~~json
{
  "source": "00b5f0b8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f0bc`](#insn-00b5f0bc)

~~~json
{
  "source": "00b5f0bc",
  "target": "00b5f0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f0d0`](#insn-00b5f0d0)

~~~json
{
  "source": "00b5f0d0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f0d8`](#insn-00b5f0d8)

~~~json
{
  "source": "00b5f0d8",
  "target": "00b60eac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f0e4`](#insn-00b5f0e4)

~~~json
{
  "source": "00b5f0e4",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f0e8`](#insn-00b5f0e8)

~~~json
{
  "source": "00b5f0e8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f100`](#insn-00b5f100)

~~~json
{
  "source": "00b5f100",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f104`](#insn-00b5f104)

~~~json
{
  "source": "00b5f104",
  "target": "00b5f12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f110`](#insn-00b5f110)

~~~json
{
  "source": "00b5f110",
  "target": "00c5ac10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f114`](#insn-00b5f114)

~~~json
{
  "source": "00b5f114",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f128`](#insn-00b5f128)

~~~json
{
  "source": "00b5f128",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f12c`](#insn-00b5f12c)

~~~json
{
  "source": "00b5f12c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f130`](#insn-00b5f130)

~~~json
{
  "source": "00b5f130",
  "target": "00b5f144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f154`](#insn-00b5f154)

~~~json
{
  "source": "00b5f154",
  "target": "00c5bc50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f15c`](#insn-00b5f15c)

~~~json
{
  "source": "00b5f15c",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f160`](#insn-00b5f160)

~~~json
{
  "source": "00b5f160",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f164`](#insn-00b5f164)

~~~json
{
  "source": "00b5f164",
  "target": "00b5f190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f178`](#insn-00b5f178)

~~~json
{
  "source": "00b5f178",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f18c`](#insn-00b5f18c)

~~~json
{
  "source": "00b5f18c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f194`](#insn-00b5f194)

~~~json
{
  "source": "00b5f194",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f198`](#insn-00b5f198)

~~~json
{
  "source": "00b5f198",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f19c`](#insn-00b5f19c)

~~~json
{
  "source": "00b5f19c",
  "target": "00b5f1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f1a8`](#insn-00b5f1a8)

~~~json
{
  "source": "00b5f1a8",
  "target": "00c5ac10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f1ac`](#insn-00b5f1ac)

~~~json
{
  "source": "00b5f1ac",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f1b0`](#insn-00b5f1b0)

~~~json
{
  "source": "00b5f1b0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f1c8`](#insn-00b5f1c8)

~~~json
{
  "source": "00b5f1c8",
  "target": "00c5aaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f1d0`](#insn-00b5f1d0)

~~~json
{
  "source": "00b5f1d0",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5f1d8`](#insn-00b5f1d8)

~~~json
{
  "source": "00b5f1d8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f1e0`](#insn-00b5f1e0)

~~~json
{
  "source": "00b5f1e0",
  "target": "00b5f204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f1e4`](#insn-00b5f1e4)

~~~json
{
  "source": "00b5f1e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f1e8`](#insn-00b5f1e8)

~~~json
{
  "source": "00b5f1e8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f1ec`](#insn-00b5f1ec)

~~~json
{
  "source": "00b5f1ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f1f0`](#insn-00b5f1f0)

~~~json
{
  "source": "00b5f1f0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f1f4`](#insn-00b5f1f4)

~~~json
{
  "source": "00b5f1f4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f1f8`](#insn-00b5f1f8)

~~~json
{
  "source": "00b5f1f8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5f204`](#insn-00b5f204)

~~~json
{
  "source": "00b5f204",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
