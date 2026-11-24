# 00b6fafc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b6eb08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6eb08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0078.md#compare-3f72a945342ff3e7c6eb80cf52df220e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6fafc",
  "name": "_ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 652,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "881e031e4b9d3b940aff366a9057494a1afd1ca8bcbae5afc4c2a59a6715a626",
  "source_text_sha256": "881e031e4b9d3b940aff366a9057494a1afd1ca8bcbae5afc4c2a59a6715a626",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6fafc",
        "00b6fd87"
      ]
    ],
    "bytes_sha256": "de45e2ba97772173d2df4d6fde830ef76b6cadc51968ff77029d7a49092321a4",
    "instruction_count": 163,
    "instruction_bytes": 652,
    "body_bytes": 652,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d810](../00c5d/00c5d810.md)

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59020](../00c59/00c59020.md)
- [00c59150](../00c59/00c59150.md)
- [00c5d080](../00c5d/00c5d080.md)
- [00c5d0a0](../00c5d/00c5d0a0.md)
- [00c5d7c0](../00c5d/00c5d7c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4173 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (long param_1,undefined8 param_2)

{
  long lVar1;
  ulong uVar2;
  long lVar3;
  void *pvVar4;
  ulong *puVar5;
  ulong uVar6;
  byte local_b0 [8];
  ulong local_a8;
  void *local_a0;
  byte local_98 [16];
  void *local_88;
  ulong local_80;
  ulong uStack_78;
  void *local_70;
  ulong local_60;
  ulong uStack_58;
  void *local_50;
  long local_48;
  
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  lVar1 = param_1 + 0x140;
  if ((*(byte *)(param_1 + 0x140) & 1) == 0) {
    if (*(byte *)(param_1 + 0x140) >> 1 != 0) {
LAB_00b6fb48:
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                (lVar1,&DAT_002b4cef,1);
    }
  }
  else if (*(long *)(param_1 + 0x148) != 0) goto LAB_00b6fb48;
  if ((*(byte *)(param_1 + 0x590) & 1) == 0) {
    if (*(byte *)(param_1 + 0x590) >> 1 != 0) goto LAB_00b6fb70;
LAB_00b6fb94:
    uVar6 = 0;
    uStack_58 = 0;
    local_50 = (void *)0x0;
    local_60 = 0;
  }
  else {
    if (*(long *)(param_1 + 0x598) == 0) goto LAB_00b6fb94;
LAB_00b6fb70:
    _ZN11flatbuffers12AbsolutePathERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
              (&local_60,param_1 + 0x590);
    uVar6 = local_60 & 0xff;
  }
  uVar2 = uVar6 >> 1;
  pvVar4 = (void *)((ulong)&local_60 | 1);
  if ((uVar6 & 1) != 0) {
    uVar2 = uStack_58;
    pvVar4 = local_50;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm(lVar1,pvVar4,uVar2)
  ;
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if ((*(byte *)(param_1 + 0x590) & 1) == 0) {
    if (*(byte *)(param_1 + 0x590) >> 1 == 0) goto LAB_00b6fc04;
  }
  else if (*(long *)(param_1 + 0x598) == 0) goto LAB_00b6fc04;
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
            (lVar1,&DAT_002b0a42,1);
LAB_00b6fc04:
  _ZN11flatbuffers11NumToStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_
            (local_98,*(undefined4 *)(param_1 + 0x18));
  puVar5 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                              (local_98,&DAT_002bd7f8,2);
  uStack_78 = puVar5[1];
  local_80 = *puVar5;
  local_70 = (void *)puVar5[2];
  *puVar5 = 0;
  puVar5[1] = 0;
  puVar5[2] = 0;
  _ZN11flatbuffers11NumToStringIlEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_
            (local_b0,*(long *)(param_1 + 8) - *(long *)(param_1 + 0x10));
  uVar6 = (ulong)(local_b0[0] >> 1);
  pvVar4 = (void *)((ulong)local_b0 | 1);
  if ((local_b0[0] & 1) != 0) {
    uVar6 = local_a8;
    pvVar4 = local_a0;
  }
  puVar5 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                              (&local_80,pvVar4,uVar6);
  uStack_58 = puVar5[1];
  local_60 = *puVar5;
  local_50 = (void *)puVar5[2];
  puVar5[1] = 0;
  puVar5[2] = 0;
  *puVar5 = 0;
  uVar6 = local_60 >> 1 & 0x7f;
  pvVar4 = (void *)((ulong)&local_60 | 1);
  if ((local_60 & 1) != 0) {
    uVar6 = uStack_58;
    pvVar4 = local_50;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm(lVar1,pvVar4,uVar6)
  ;
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if ((local_b0[0] & 1) != 0) {
    _ZdlPv(local_a0);
  }
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  if ((local_98[0] & 1) != 0) {
    _ZdlPv(local_88);
  }
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_60,&DAT_002bd7f8,param_2);
  uVar6 = local_60 >> 1 & 0x7f;
  pvVar4 = (void *)((ulong)&local_60 | 1);
  if ((local_60 & 1) != 0) {
    uVar6 = uStack_58;
    pvVar4 = local_50;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm(lVar1,pvVar4,uVar6)
  ;
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if (*(long *)(lVar3 + 0x28) == local_48) {
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
<a id="insn-00b6fafc"></a> `00b6fafc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00b6fb00"></a> `00b6fb00` | `f7 3b 00 f9` | str x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b6fb04"></a> `00b6fb04` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b6fb08"></a> `00b6fb08` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b6fb0c"></a> `00b6fb0c` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b6fb10"></a> `00b6fb10` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b6fb14"></a> `00b6fb14` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b6fb18"></a> `00b6fb18` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b6fb1c"></a> `00b6fb1c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b6fb20"></a> `00b6fb20` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6fb24"></a> `00b6fb24` | `13 00 05 91` | add x19,x0,#0x140 | `FALL_THROUGH`
<a id="insn-00b6fb28"></a> `00b6fb28` | `a8 83 1c f8` | stur x8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00b6fb2c"></a> `00b6fb2c` | `08 00 45 39` | ldrb w8,[x0, #0x140] | `FALL_THROUGH`
<a id="insn-00b6fb30"></a> `00b6fb30` | `88 00 00 37` | tbnz w8,#0x0,0x00b6fb40 | `CONDITIONAL_JUMP`
<a id="insn-00b6fb34"></a> `00b6fb34` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fb38"></a> `00b6fb38` | `88 00 00 b5` | cbnz x8,0x00b6fb48 | `CONDITIONAL_JUMP`
<a id="insn-00b6fb3c"></a> `00b6fb3c` | `08 00 00 14` | b 0x00b6fb5c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6fb40"></a> `00b6fb40` | `a8 a6 40 f9` | ldr x8,[x21, #0x148] | `FALL_THROUGH`
<a id="insn-00b6fb44"></a> `00b6fb44` | `c8 00 00 b4` | cbz x8,0x00b6fb5c | `CONDITIONAL_JUMP`
<a id="insn-00b6fb48"></a> `00b6fb48` | `21 ba ff b0` | adrp x1,0x2b4000 | `FALL_THROUGH`
<a id="insn-00b6fb4c"></a> `00b6fb4c` | `21 bc 33 91` | add x1,x1,#0xcef | `FALL_THROUGH`
<a id="insn-00b6fb50"></a> `00b6fb50` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fb54"></a> `00b6fb54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6fb58"></a> `00b6fb58` | `32 a5 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fb5c"></a> `00b6fb5c` | `a8 42 56 39` | ldrb w8,[x21, #0x590] | `FALL_THROUGH`
<a id="insn-00b6fb60"></a> `00b6fb60` | `48 01 00 37` | tbnz w8,#0x0,0x00b6fb88 | `CONDITIONAL_JUMP`
<a id="insn-00b6fb64"></a> `00b6fb64` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fb68"></a> `00b6fb68` | `b6 42 16 91` | add x22,x21,#0x590 | `FALL_THROUGH`
<a id="insn-00b6fb6c"></a> `00b6fb6c` | `48 01 00 b4` | cbz x8,0x00b6fb94 | `CONDITIONAL_JUMP`
<a id="insn-00b6fb70"></a> `00b6fb70` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b6fb74"></a> `00b6fb74` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b6fb78"></a> `00b6fb78` | `12 b7 03 94` | bl 0x00c5d7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fb7c"></a> `00b6fb7c` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6fb80"></a> `00b6fb80` | `ea a7 45 a9` | ldp x10,x9,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00b6fb84"></a> `00b6fb84` | `08 00 00 14` | b 0x00b6fba4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6fb88"></a> `00b6fb88` | `a8 ce 42 f9` | ldr x8,[x21, #0x598] | `FALL_THROUGH`
<a id="insn-00b6fb8c"></a> `00b6fb8c` | `b6 42 16 91` | add x22,x21,#0x590 | `FALL_THROUGH`
<a id="insn-00b6fb90"></a> `00b6fb90` | `08 ff ff b5` | cbnz x8,0x00b6fb70 | `CONDITIONAL_JUMP`
<a id="insn-00b6fb94"></a> `00b6fb94` | `ea 03 1f aa` | mov x10,xzr | `FALL_THROUGH`
<a id="insn-00b6fb98"></a> `00b6fb98` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00b6fb9c"></a> `00b6fb9c` | `ff ff 05 a9` | stp xzr,xzr,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00b6fba0"></a> `00b6fba0` | `ff 2b 00 f9` | str xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6fba4"></a> `00b6fba4` | `eb 43 01 91` | add x11,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b6fba8"></a> `00b6fba8` | `0c 7d 01 53` | lsr w12,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fbac"></a> `00b6fbac` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fbb0"></a> `00b6fbb0` | `68 01 40 b2` | orr x8,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fbb4"></a> `00b6fbb4` | `01 01 89 9a` | csel x1,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00b6fbb8"></a> `00b6fbb8` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00b6fbbc"></a> `00b6fbbc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6fbc0"></a> `00b6fbc0` | `18 a5 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fbc4"></a> `00b6fbc4` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6fbc8"></a> `00b6fbc8` | `68 00 00 36` | tbz w8,#0x0,0x00b6fbd4 | `CONDITIONAL_JUMP`
<a id="insn-00b6fbcc"></a> `00b6fbcc` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b6fbd0"></a> `00b6fbd0` | `e0 a4 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fbd4"></a> `00b6fbd4` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00b6fbd8"></a> `00b6fbd8` | `88 00 00 37` | tbnz w8,#0x0,0x00b6fbe8 | `CONDITIONAL_JUMP`
<a id="insn-00b6fbdc"></a> `00b6fbdc` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fbe0"></a> `00b6fbe0` | `88 00 00 b5` | cbnz x8,0x00b6fbf0 | `CONDITIONAL_JUMP`
<a id="insn-00b6fbe4"></a> `00b6fbe4` | `08 00 00 14` | b 0x00b6fc04 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6fbe8"></a> `00b6fbe8` | `a8 ce 42 f9` | ldr x8,[x21, #0x598] | `FALL_THROUGH`
<a id="insn-00b6fbec"></a> `00b6fbec` | `c8 00 00 b4` | cbz x8,0x00b6fc04 | `CONDITIONAL_JUMP`
<a id="insn-00b6fbf0"></a> `00b6fbf0` | `01 ba ff b0` | adrp x1,0x2b0000 | `FALL_THROUGH`
<a id="insn-00b6fbf4"></a> `00b6fbf4` | `21 08 29 91` | add x1,x1,#0xa42 | `FALL_THROUGH`
<a id="insn-00b6fbf8"></a> `00b6fbf8` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fbfc"></a> `00b6fbfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6fc00"></a> `00b6fc00` | `08 a5 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fc04"></a> `00b6fc04` | `a0 1a 40 b9` | ldr w0,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00b6fc08"></a> `00b6fc08` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b6fc0c"></a> `00b6fc0c` | `1d b5 03 94` | bl 0x00c5d080 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fc10"></a> `00b6fc10` | `61 ba ff d0` | adrp x1,0x2bd000 | `FALL_THROUGH`
<a id="insn-00b6fc14"></a> `00b6fc14` | `21 e0 1f 91` | add x1,x1,#0x7f8 | `FALL_THROUGH`
<a id="insn-00b6fc18"></a> `00b6fc18` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b6fc1c"></a> `00b6fc1c` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00b6fc20"></a> `00b6fc20` | `00 a5 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fc24"></a> `00b6fc24` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00b6fc28"></a> `00b6fc28` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fc2c"></a> `00b6fc2c` | `e0 0f 80 3d` | str q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6fc30"></a> `00b6fc30` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b6fc34"></a> `00b6fc34` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b6fc38"></a> `00b6fc38` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fc3c"></a> `00b6fc3c` | `a8 a6 40 a9` | ldp x8,x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00b6fc40"></a> `00b6fc40` | `f5 03 00 91` | mov x21,sp | `FALL_THROUGH`
<a id="insn-00b6fc44"></a> `00b6fc44` | `00 01 09 cb` | sub x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00b6fc48"></a> `00b6fc48` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b6fc4c"></a> `00b6fc4c` | `15 b5 03 94` | bl 0x00c5d0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fc50"></a> `00b6fc50` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b6fc54"></a> `00b6fc54` | `ea a7 40 a9` | ldp x10,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b6fc58"></a> `00b6fc58` | `ab 02 40 b2` | orr x11,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fc5c"></a> `00b6fc5c` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b6fc60"></a> `00b6fc60` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fc64"></a> `00b6fc64` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fc68"></a> `00b6fc68` | `61 01 89 9a` | csel x1,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00b6fc6c"></a> `00b6fc6c` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00b6fc70"></a> `00b6fc70` | `ec a4 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fc74"></a> `00b6fc74` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00b6fc78"></a> `00b6fc78` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fc7c"></a> `00b6fc7c` | `e9 43 01 91` | add x9,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b6fc80"></a> `00b6fc80` | `29 01 40 b2` | orr x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fc84"></a> `00b6fc84` | `e0 17 80 3d` | str q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6fc88"></a> `00b6fc88` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b6fc8c"></a> `00b6fc8c` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00b6fc90"></a> `00b6fc90` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b6fc94"></a> `00b6fc94` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6fc98"></a> `00b6fc98` | `eb ab 45 a9` | ldp x11,x10,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00b6fc9c"></a> `00b6fc9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6fca0"></a> `00b6fca0` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fca4"></a> `00b6fca4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fca8"></a> `00b6fca8` | `21 01 8a 9a` | csel x1,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00b6fcac"></a> `00b6fcac` | `82 01 8b 9a` | csel x2,x12,x11,eq | `FALL_THROUGH`
<a id="insn-00b6fcb0"></a> `00b6fcb0` | `dc a4 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fcb4"></a> `00b6fcb4` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6fcb8"></a> `00b6fcb8` | `c8 04 00 37` | tbnz w8,#0x0,0x00b6fd50 | `CONDITIONAL_JUMP`
<a id="insn-00b6fcbc"></a> `00b6fcbc` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b6fcc0"></a> `00b6fcc0` | `08 05 00 37` | tbnz w8,#0x0,0x00b6fd60 | `CONDITIONAL_JUMP`
<a id="insn-00b6fcc4"></a> `00b6fcc4` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6fcc8"></a> `00b6fcc8` | `48 05 00 37` | tbnz w8,#0x0,0x00b6fd70 | `CONDITIONAL_JUMP`
<a id="insn-00b6fccc"></a> `00b6fccc` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b6fcd0"></a> `00b6fcd0` | `68 00 00 36` | tbz w8,#0x0,0x00b6fcdc | `CONDITIONAL_JUMP`
<a id="insn-00b6fcd4"></a> `00b6fcd4` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b6fcd8"></a> `00b6fcd8` | `9e a4 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fcdc"></a> `00b6fcdc` | `60 ba ff d0` | adrp x0,0x2bd000 | `FALL_THROUGH`
<a id="insn-00b6fce0"></a> `00b6fce0` | `00 e0 1f 91` | add x0,x0,#0x7f8 | `FALL_THROUGH`
<a id="insn-00b6fce4"></a> `00b6fce4` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b6fce8"></a> `00b6fce8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b6fcec"></a> `00b6fcec` | `f5 43 01 91` | add x21,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b6fcf0"></a> `00b6fcf0` | `18 a5 03 94` | bl 0x00c59150 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fcf4"></a> `00b6fcf4` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6fcf8"></a> `00b6fcf8` | `ea a7 45 a9` | ldp x10,x9,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00b6fcfc"></a> `00b6fcfc` | `ab 02 40 b2` | orr x11,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fd00"></a> `00b6fd00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6fd04"></a> `00b6fd04` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fd08"></a> `00b6fd08` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6fd0c"></a> `00b6fd0c` | `61 01 89 9a` | csel x1,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00b6fd10"></a> `00b6fd10` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00b6fd14"></a> `00b6fd14` | `c3 a4 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fd18"></a> `00b6fd18` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6fd1c"></a> `00b6fd1c` | `68 00 00 36` | tbz w8,#0x0,0x00b6fd28 | `CONDITIONAL_JUMP`
<a id="insn-00b6fd20"></a> `00b6fd20` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b6fd24"></a> `00b6fd24` | `8b a4 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fd28"></a> `00b6fd28` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b6fd2c"></a> `00b6fd2c` | `a9 83 5c f8` | ldur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00b6fd30"></a> `00b6fd30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b6fd34"></a> `00b6fd34` | `81 02 00 54` | b.ne 0x00b6fd84 | `CONDITIONAL_JUMP`
<a id="insn-00b6fd38"></a> `00b6fd38` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b6fd3c"></a> `00b6fd3c` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b6fd40"></a> `00b6fd40` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b6fd44"></a> `00b6fd44` | `f7 3b 40 f9` | ldr x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b6fd48"></a> `00b6fd48` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00b6fd4c"></a> `00b6fd4c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b6fd50"></a> `00b6fd50` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b6fd54"></a> `00b6fd54` | `7f a4 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fd58"></a> `00b6fd58` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b6fd5c"></a> `00b6fd5c` | `48 fb 07 36` | tbz w8,#0x0,0x00b6fcc4 | `CONDITIONAL_JUMP`
<a id="insn-00b6fd60"></a> `00b6fd60` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fd64"></a> `00b6fd64` | `7b a4 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fd68"></a> `00b6fd68` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6fd6c"></a> `00b6fd6c` | `08 fb 07 36` | tbz w8,#0x0,0x00b6fccc | `CONDITIONAL_JUMP`
<a id="insn-00b6fd70"></a> `00b6fd70` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b6fd74"></a> `00b6fd74` | `77 a4 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fd78"></a> `00b6fd78` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b6fd7c"></a> `00b6fd7c` | `c8 fa 07 37` | tbnz w8,#0x0,0x00b6fcd4 | `CONDITIONAL_JUMP`
<a id="insn-00b6fd80"></a> `00b6fd80` | `d7 ff ff 17` | b 0x00b6fcdc | `UNCONDITIONAL_JUMP`
<a id="insn-00b6fd84"></a> `00b6fd84` | `7f a4 03 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6fafc`](#insn-00b6fafc) 範囲 `[['00b6fafc', '00b6fb33']]`
  - `CONDITIONAL_JUMP` [`00b6fb30`](#insn-00b6fb30) → [`00b6fb40`](#insn-00b6fb40)
  - `FALL_THROUGH` [`00b6fb30`](#insn-00b6fb30) → [`00b6fb34`](#insn-00b6fb34)
- ブロック [`00b6fb34`](#insn-00b6fb34) 範囲 `[['00b6fb34', '00b6fb3b']]`
  - `CONDITIONAL_JUMP` [`00b6fb38`](#insn-00b6fb38) → [`00b6fb48`](#insn-00b6fb48)
  - `FALL_THROUGH` [`00b6fb38`](#insn-00b6fb38) → [`00b6fb3c`](#insn-00b6fb3c)
- ブロック [`00b6fb3c`](#insn-00b6fb3c) 範囲 `[['00b6fb3c', '00b6fb3f']]`
  - `UNCONDITIONAL_JUMP` [`00b6fb3c`](#insn-00b6fb3c) → [`00b6fb5c`](#insn-00b6fb5c)
- ブロック [`00b6fb40`](#insn-00b6fb40) 範囲 `[['00b6fb40', '00b6fb47']]`
  - `CONDITIONAL_JUMP` [`00b6fb44`](#insn-00b6fb44) → [`00b6fb5c`](#insn-00b6fb5c)
  - `FALL_THROUGH` [`00b6fb44`](#insn-00b6fb44) → [`00b6fb48`](#insn-00b6fb48)
- ブロック [`00b6fb48`](#insn-00b6fb48) 範囲 `[['00b6fb48', '00b6fb5b']]`
  - `FALL_THROUGH` [`00b6fb58`](#insn-00b6fb58) → [`00b6fb5c`](#insn-00b6fb5c)
- ブロック [`00b6fb5c`](#insn-00b6fb5c) 範囲 `[['00b6fb5c', '00b6fb63']]`
  - `CONDITIONAL_JUMP` [`00b6fb60`](#insn-00b6fb60) → [`00b6fb88`](#insn-00b6fb88)
  - `FALL_THROUGH` [`00b6fb60`](#insn-00b6fb60) → [`00b6fb64`](#insn-00b6fb64)
- ブロック [`00b6fb64`](#insn-00b6fb64) 範囲 `[['00b6fb64', '00b6fb6f']]`
  - `CONDITIONAL_JUMP` [`00b6fb6c`](#insn-00b6fb6c) → [`00b6fb94`](#insn-00b6fb94)
  - `FALL_THROUGH` [`00b6fb6c`](#insn-00b6fb6c) → [`00b6fb70`](#insn-00b6fb70)
- ブロック [`00b6fb70`](#insn-00b6fb70) 範囲 `[['00b6fb70', '00b6fb87']]`
  - `UNCONDITIONAL_JUMP` [`00b6fb84`](#insn-00b6fb84) → [`00b6fba4`](#insn-00b6fba4)
- ブロック [`00b6fb88`](#insn-00b6fb88) 範囲 `[['00b6fb88', '00b6fb93']]`
  - `CONDITIONAL_JUMP` [`00b6fb90`](#insn-00b6fb90) → [`00b6fb70`](#insn-00b6fb70)
  - `FALL_THROUGH` [`00b6fb90`](#insn-00b6fb90) → [`00b6fb94`](#insn-00b6fb94)
- ブロック [`00b6fb94`](#insn-00b6fb94) 範囲 `[['00b6fb94', '00b6fba3']]`
  - `FALL_THROUGH` [`00b6fba0`](#insn-00b6fba0) → [`00b6fba4`](#insn-00b6fba4)
- ブロック [`00b6fba4`](#insn-00b6fba4) 範囲 `[['00b6fba4', '00b6fbcb']]`
  - `CONDITIONAL_JUMP` [`00b6fbc8`](#insn-00b6fbc8) → [`00b6fbd4`](#insn-00b6fbd4)
  - `FALL_THROUGH` [`00b6fbc8`](#insn-00b6fbc8) → [`00b6fbcc`](#insn-00b6fbcc)
- ブロック [`00b6fbcc`](#insn-00b6fbcc) 範囲 `[['00b6fbcc', '00b6fbd3']]`
  - `FALL_THROUGH` [`00b6fbd0`](#insn-00b6fbd0) → [`00b6fbd4`](#insn-00b6fbd4)
- ブロック [`00b6fbd4`](#insn-00b6fbd4) 範囲 `[['00b6fbd4', '00b6fbdb']]`
  - `CONDITIONAL_JUMP` [`00b6fbd8`](#insn-00b6fbd8) → [`00b6fbe8`](#insn-00b6fbe8)
  - `FALL_THROUGH` [`00b6fbd8`](#insn-00b6fbd8) → [`00b6fbdc`](#insn-00b6fbdc)
- ブロック [`00b6fbdc`](#insn-00b6fbdc) 範囲 `[['00b6fbdc', '00b6fbe3']]`
  - `CONDITIONAL_JUMP` [`00b6fbe0`](#insn-00b6fbe0) → [`00b6fbf0`](#insn-00b6fbf0)
  - `FALL_THROUGH` [`00b6fbe0`](#insn-00b6fbe0) → [`00b6fbe4`](#insn-00b6fbe4)
- ブロック [`00b6fbe4`](#insn-00b6fbe4) 範囲 `[['00b6fbe4', '00b6fbe7']]`
  - `UNCONDITIONAL_JUMP` [`00b6fbe4`](#insn-00b6fbe4) → [`00b6fc04`](#insn-00b6fc04)
- ブロック [`00b6fbe8`](#insn-00b6fbe8) 範囲 `[['00b6fbe8', '00b6fbef']]`
  - `CONDITIONAL_JUMP` [`00b6fbec`](#insn-00b6fbec) → [`00b6fc04`](#insn-00b6fc04)
  - `FALL_THROUGH` [`00b6fbec`](#insn-00b6fbec) → [`00b6fbf0`](#insn-00b6fbf0)
- ブロック [`00b6fbf0`](#insn-00b6fbf0) 範囲 `[['00b6fbf0', '00b6fc03']]`
  - `FALL_THROUGH` [`00b6fc00`](#insn-00b6fc00) → [`00b6fc04`](#insn-00b6fc04)
- ブロック [`00b6fc04`](#insn-00b6fc04) 範囲 `[['00b6fc04', '00b6fcbb']]`
  - `CONDITIONAL_JUMP` [`00b6fcb8`](#insn-00b6fcb8) → [`00b6fd50`](#insn-00b6fd50)
  - `FALL_THROUGH` [`00b6fcb8`](#insn-00b6fcb8) → [`00b6fcbc`](#insn-00b6fcbc)
- ブロック [`00b6fcbc`](#insn-00b6fcbc) 範囲 `[['00b6fcbc', '00b6fcc3']]`
  - `CONDITIONAL_JUMP` [`00b6fcc0`](#insn-00b6fcc0) → [`00b6fd60`](#insn-00b6fd60)
  - `FALL_THROUGH` [`00b6fcc0`](#insn-00b6fcc0) → [`00b6fcc4`](#insn-00b6fcc4)
- ブロック [`00b6fcc4`](#insn-00b6fcc4) 範囲 `[['00b6fcc4', '00b6fccb']]`
  - `CONDITIONAL_JUMP` [`00b6fcc8`](#insn-00b6fcc8) → [`00b6fd70`](#insn-00b6fd70)
  - `FALL_THROUGH` [`00b6fcc8`](#insn-00b6fcc8) → [`00b6fccc`](#insn-00b6fccc)
- ブロック [`00b6fccc`](#insn-00b6fccc) 範囲 `[['00b6fccc', '00b6fcd3']]`
  - `CONDITIONAL_JUMP` [`00b6fcd0`](#insn-00b6fcd0) → [`00b6fcdc`](#insn-00b6fcdc)
  - `FALL_THROUGH` [`00b6fcd0`](#insn-00b6fcd0) → [`00b6fcd4`](#insn-00b6fcd4)
- ブロック [`00b6fcd4`](#insn-00b6fcd4) 範囲 `[['00b6fcd4', '00b6fcdb']]`
  - `FALL_THROUGH` [`00b6fcd8`](#insn-00b6fcd8) → [`00b6fcdc`](#insn-00b6fcdc)
- ブロック [`00b6fcdc`](#insn-00b6fcdc) 範囲 `[['00b6fcdc', '00b6fd1f']]`
  - `CONDITIONAL_JUMP` [`00b6fd1c`](#insn-00b6fd1c) → [`00b6fd28`](#insn-00b6fd28)
  - `FALL_THROUGH` [`00b6fd1c`](#insn-00b6fd1c) → [`00b6fd20`](#insn-00b6fd20)
- ブロック [`00b6fd20`](#insn-00b6fd20) 範囲 `[['00b6fd20', '00b6fd27']]`
  - `FALL_THROUGH` [`00b6fd24`](#insn-00b6fd24) → [`00b6fd28`](#insn-00b6fd28)
- ブロック [`00b6fd28`](#insn-00b6fd28) 範囲 `[['00b6fd28', '00b6fd37']]`
  - `CONDITIONAL_JUMP` [`00b6fd34`](#insn-00b6fd34) → [`00b6fd84`](#insn-00b6fd84)
  - `FALL_THROUGH` [`00b6fd34`](#insn-00b6fd34) → [`00b6fd38`](#insn-00b6fd38)
- ブロック [`00b6fd38`](#insn-00b6fd38) 範囲 `[['00b6fd38', '00b6fd4f']]`
- ブロック [`00b6fd50`](#insn-00b6fd50) 範囲 `[['00b6fd50', '00b6fd5f']]`
  - `CONDITIONAL_JUMP` [`00b6fd5c`](#insn-00b6fd5c) → [`00b6fcc4`](#insn-00b6fcc4)
  - `FALL_THROUGH` [`00b6fd5c`](#insn-00b6fd5c) → [`00b6fd60`](#insn-00b6fd60)
- ブロック [`00b6fd60`](#insn-00b6fd60) 範囲 `[['00b6fd60', '00b6fd6f']]`
  - `CONDITIONAL_JUMP` [`00b6fd6c`](#insn-00b6fd6c) → [`00b6fccc`](#insn-00b6fccc)
  - `FALL_THROUGH` [`00b6fd6c`](#insn-00b6fd6c) → [`00b6fd70`](#insn-00b6fd70)
- ブロック [`00b6fd70`](#insn-00b6fd70) 範囲 `[['00b6fd70', '00b6fd7f']]`
  - `CONDITIONAL_JUMP` [`00b6fd7c`](#insn-00b6fd7c) → [`00b6fcd4`](#insn-00b6fcd4)
  - `FALL_THROUGH` [`00b6fd7c`](#insn-00b6fd7c) → [`00b6fd80`](#insn-00b6fd80)
- ブロック [`00b6fd80`](#insn-00b6fd80) 範囲 `[['00b6fd80', '00b6fd83']]`
  - `UNCONDITIONAL_JUMP` [`00b6fd80`](#insn-00b6fd80) → [`00b6fcdc`](#insn-00b6fcdc)
- ブロック [`00b6fd84`](#insn-00b6fd84) 範囲 `[['00b6fd84', '00b6fd87']]`

## 命令位置別の参照

- [`00b6fb00`](#insn-00b6fb00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb04`](#insn-00b6fb04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb08`](#insn-00b6fb08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb0c`](#insn-00b6fb0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb28`](#insn-00b6fb28) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb30`](#insn-00b6fb30) → [`00b6fb40`](#insn-00b6fb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb38`](#insn-00b6fb38) → [`00b6fb48`](#insn-00b6fb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb3c`](#insn-00b6fb3c) → [`00b6fb5c`](#insn-00b6fb5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb44`](#insn-00b6fb44) → [`00b6fb5c`](#insn-00b6fb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb4c`](#insn-00b6fb4c) → `002b4cef`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb58`](#insn-00b6fb58) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb60`](#insn-00b6fb60) → [`00b6fb88`](#insn-00b6fb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb6c`](#insn-00b6fb6c) → [`00b6fb94`](#insn-00b6fb94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb78`](#insn-00b6fb78) → [`00c5d7c0`](../00c5d/00c5d7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d7c0` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb7c`](#insn-00b6fb7c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb80`](#insn-00b6fb80) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb84`](#insn-00b6fb84) → [`00b6fba4`](#insn-00b6fba4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb90`](#insn-00b6fb90) → [`00b6fb70`](#insn-00b6fb70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb9c`](#insn-00b6fb9c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fba0`](#insn-00b6fba0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fbc0`](#insn-00b6fbc0) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b6fbc4`](#insn-00b6fbc4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fbc8`](#insn-00b6fbc8) → [`00b6fbd4`](#insn-00b6fbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fbcc`](#insn-00b6fbcc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fbd0`](#insn-00b6fbd0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b6fbd8`](#insn-00b6fbd8) → [`00b6fbe8`](#insn-00b6fbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fbe0`](#insn-00b6fbe0) → [`00b6fbf0`](#insn-00b6fbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fbe4`](#insn-00b6fbe4) → [`00b6fc04`](#insn-00b6fc04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fbec`](#insn-00b6fbec) → [`00b6fc04`](#insn-00b6fc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fbf4`](#insn-00b6fbf4) → `002b0a42`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc00`](#insn-00b6fc00) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc0c`](#insn-00b6fc0c) → [`00c5d080`](../00c5d/00c5d080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d080` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc14`](#insn-00b6fc14) → `002bd7f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc20`](#insn-00b6fc20) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc2c`](#insn-00b6fc2c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc30`](#insn-00b6fc30) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc4c`](#insn-00b6fc4c) → [`00c5d0a0`](../00c5d/00c5d0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d0a0` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc50`](#insn-00b6fc50) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc54`](#insn-00b6fc54) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc70`](#insn-00b6fc70) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc84`](#insn-00b6fc84) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc88`](#insn-00b6fc88) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc94`](#insn-00b6fc94) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fc98`](#insn-00b6fc98) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcb0`](#insn-00b6fcb0) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcb4`](#insn-00b6fcb4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcb8`](#insn-00b6fcb8) → [`00b6fd50`](#insn-00b6fd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcbc`](#insn-00b6fcbc) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcc0`](#insn-00b6fcc0) → [`00b6fd60`](#insn-00b6fd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcc4`](#insn-00b6fcc4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcc8`](#insn-00b6fcc8) → [`00b6fd70`](#insn-00b6fd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fccc`](#insn-00b6fccc) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcd0`](#insn-00b6fcd0) → [`00b6fcdc`](#insn-00b6fcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcd4`](#insn-00b6fcd4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcd8`](#insn-00b6fcd8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b6fce0`](#insn-00b6fce0) → `002bd7f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcf0`](#insn-00b6fcf0) → [`00c59150`](../00c59/00c59150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59150` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcf4`](#insn-00b6fcf4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcf8`](#insn-00b6fcf8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd14`](#insn-00b6fd14) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd18`](#insn-00b6fd18) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd1c`](#insn-00b6fd1c) → [`00b6fd28`](#insn-00b6fd28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd20`](#insn-00b6fd20) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd24`](#insn-00b6fd24) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd2c`](#insn-00b6fd2c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd34`](#insn-00b6fd34) → [`00b6fd84`](#insn-00b6fd84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd38`](#insn-00b6fd38) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd3c`](#insn-00b6fd3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd40`](#insn-00b6fd40) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd44`](#insn-00b6fd44) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd50`](#insn-00b6fd50) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd54`](#insn-00b6fd54) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd58`](#insn-00b6fd58) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd5c`](#insn-00b6fd5c) → [`00b6fcc4`](#insn-00b6fcc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd60`](#insn-00b6fd60) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd64`](#insn-00b6fd64) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd68`](#insn-00b6fd68) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd6c`](#insn-00b6fd6c) → [`00b6fccc`](#insn-00b6fccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd70`](#insn-00b6fd70) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd74`](#insn-00b6fd74) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd78`](#insn-00b6fd78) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd7c`](#insn-00b6fd7c) → [`00b6fcd4`](#insn-00b6fcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd80`](#insn-00b6fd80) → [`00b6fcdc`](#insn-00b6fcdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd84`](#insn-00b6fd84) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6fb00`](#insn-00b6fb00)

~~~json
{
  "source": "00b6fb00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb04`](#insn-00b6fb04)

~~~json
{
  "source": "00b6fb04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb08`](#insn-00b6fb08)

~~~json
{
  "source": "00b6fb08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb0c`](#insn-00b6fb0c)

~~~json
{
  "source": "00b6fb0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb28`](#insn-00b6fb28)

~~~json
{
  "source": "00b6fb28",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb30`](#insn-00b6fb30)

~~~json
{
  "source": "00b6fb30",
  "target": "00b6fb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb38`](#insn-00b6fb38)

~~~json
{
  "source": "00b6fb38",
  "target": "00b6fb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb3c`](#insn-00b6fb3c)

~~~json
{
  "source": "00b6fb3c",
  "target": "00b6fb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb44`](#insn-00b6fb44)

~~~json
{
  "source": "00b6fb44",
  "target": "00b6fb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb4c`](#insn-00b6fb4c)

~~~json
{
  "source": "00b6fb4c",
  "target": "002b4cef",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb58`](#insn-00b6fb58)

~~~json
{
  "source": "00b6fb58",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fb60`](#insn-00b6fb60)

~~~json
{
  "source": "00b6fb60",
  "target": "00b6fb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb6c`](#insn-00b6fb6c)

~~~json
{
  "source": "00b6fb6c",
  "target": "00b6fb94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb78`](#insn-00b6fb78)

~~~json
{
  "source": "00b6fb78",
  "target": "00c5d7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fb7c`](#insn-00b6fb7c)

~~~json
{
  "source": "00b6fb7c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb80`](#insn-00b6fb80)

~~~json
{
  "source": "00b6fb80",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb84`](#insn-00b6fb84)

~~~json
{
  "source": "00b6fb84",
  "target": "00b6fba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb90`](#insn-00b6fb90)

~~~json
{
  "source": "00b6fb90",
  "target": "00b6fb70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb9c`](#insn-00b6fb9c)

~~~json
{
  "source": "00b6fb9c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fba0`](#insn-00b6fba0)

~~~json
{
  "source": "00b6fba0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fbc0`](#insn-00b6fbc0)

~~~json
{
  "source": "00b6fbc0",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fbc4`](#insn-00b6fbc4)

~~~json
{
  "source": "00b6fbc4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fbc8`](#insn-00b6fbc8)

~~~json
{
  "source": "00b6fbc8",
  "target": "00b6fbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fbcc`](#insn-00b6fbcc)

~~~json
{
  "source": "00b6fbcc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fbd0`](#insn-00b6fbd0)

~~~json
{
  "source": "00b6fbd0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fbd8`](#insn-00b6fbd8)

~~~json
{
  "source": "00b6fbd8",
  "target": "00b6fbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fbe0`](#insn-00b6fbe0)

~~~json
{
  "source": "00b6fbe0",
  "target": "00b6fbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fbe4`](#insn-00b6fbe4)

~~~json
{
  "source": "00b6fbe4",
  "target": "00b6fc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fbec`](#insn-00b6fbec)

~~~json
{
  "source": "00b6fbec",
  "target": "00b6fc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fbf4`](#insn-00b6fbf4)

~~~json
{
  "source": "00b6fbf4",
  "target": "002b0a42",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fc00`](#insn-00b6fc00)

~~~json
{
  "source": "00b6fc00",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fc0c`](#insn-00b6fc0c)

~~~json
{
  "source": "00b6fc0c",
  "target": "00c5d080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fc14`](#insn-00b6fc14)

~~~json
{
  "source": "00b6fc14",
  "target": "002bd7f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fc20`](#insn-00b6fc20)

~~~json
{
  "source": "00b6fc20",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fc2c`](#insn-00b6fc2c)

~~~json
{
  "source": "00b6fc2c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fc30`](#insn-00b6fc30)

~~~json
{
  "source": "00b6fc30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fc4c`](#insn-00b6fc4c)

~~~json
{
  "source": "00b6fc4c",
  "target": "00c5d0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fc50`](#insn-00b6fc50)

~~~json
{
  "source": "00b6fc50",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fc54`](#insn-00b6fc54)

~~~json
{
  "source": "00b6fc54",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fc70`](#insn-00b6fc70)

~~~json
{
  "source": "00b6fc70",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fc84`](#insn-00b6fc84)

~~~json
{
  "source": "00b6fc84",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fc88`](#insn-00b6fc88)

~~~json
{
  "source": "00b6fc88",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fc94`](#insn-00b6fc94)

~~~json
{
  "source": "00b6fc94",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fc98`](#insn-00b6fc98)

~~~json
{
  "source": "00b6fc98",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcb0`](#insn-00b6fcb0)

~~~json
{
  "source": "00b6fcb0",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fcb4`](#insn-00b6fcb4)

~~~json
{
  "source": "00b6fcb4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcb8`](#insn-00b6fcb8)

~~~json
{
  "source": "00b6fcb8",
  "target": "00b6fd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcbc`](#insn-00b6fcbc)

~~~json
{
  "source": "00b6fcbc",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcc0`](#insn-00b6fcc0)

~~~json
{
  "source": "00b6fcc0",
  "target": "00b6fd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcc4`](#insn-00b6fcc4)

~~~json
{
  "source": "00b6fcc4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcc8`](#insn-00b6fcc8)

~~~json
{
  "source": "00b6fcc8",
  "target": "00b6fd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fccc`](#insn-00b6fccc)

~~~json
{
  "source": "00b6fccc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcd0`](#insn-00b6fcd0)

~~~json
{
  "source": "00b6fcd0",
  "target": "00b6fcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcd4`](#insn-00b6fcd4)

~~~json
{
  "source": "00b6fcd4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcd8`](#insn-00b6fcd8)

~~~json
{
  "source": "00b6fcd8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fce0`](#insn-00b6fce0)

~~~json
{
  "source": "00b6fce0",
  "target": "002bd7f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcf0`](#insn-00b6fcf0)

~~~json
{
  "source": "00b6fcf0",
  "target": "00c59150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fcf4`](#insn-00b6fcf4)

~~~json
{
  "source": "00b6fcf4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcf8`](#insn-00b6fcf8)

~~~json
{
  "source": "00b6fcf8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd14`](#insn-00b6fd14)

~~~json
{
  "source": "00b6fd14",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd18`](#insn-00b6fd18)

~~~json
{
  "source": "00b6fd18",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd1c`](#insn-00b6fd1c)

~~~json
{
  "source": "00b6fd1c",
  "target": "00b6fd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd20`](#insn-00b6fd20)

~~~json
{
  "source": "00b6fd20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd24`](#insn-00b6fd24)

~~~json
{
  "source": "00b6fd24",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd2c`](#insn-00b6fd2c)

~~~json
{
  "source": "00b6fd2c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd34`](#insn-00b6fd34)

~~~json
{
  "source": "00b6fd34",
  "target": "00b6fd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd38`](#insn-00b6fd38)

~~~json
{
  "source": "00b6fd38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd3c`](#insn-00b6fd3c)

~~~json
{
  "source": "00b6fd3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd40`](#insn-00b6fd40)

~~~json
{
  "source": "00b6fd40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd44`](#insn-00b6fd44)

~~~json
{
  "source": "00b6fd44",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd50`](#insn-00b6fd50)

~~~json
{
  "source": "00b6fd50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd54`](#insn-00b6fd54)

~~~json
{
  "source": "00b6fd54",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd58`](#insn-00b6fd58)

~~~json
{
  "source": "00b6fd58",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd5c`](#insn-00b6fd5c)

~~~json
{
  "source": "00b6fd5c",
  "target": "00b6fcc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd60`](#insn-00b6fd60)

~~~json
{
  "source": "00b6fd60",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd64`](#insn-00b6fd64)

~~~json
{
  "source": "00b6fd64",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd68`](#insn-00b6fd68)

~~~json
{
  "source": "00b6fd68",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd6c`](#insn-00b6fd6c)

~~~json
{
  "source": "00b6fd6c",
  "target": "00b6fccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd70`](#insn-00b6fd70)

~~~json
{
  "source": "00b6fd70",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd74`](#insn-00b6fd74)

~~~json
{
  "source": "00b6fd74",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd78`](#insn-00b6fd78)

~~~json
{
  "source": "00b6fd78",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd7c`](#insn-00b6fd7c)

~~~json
{
  "source": "00b6fd7c",
  "target": "00b6fcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd80`](#insn-00b6fd80)

~~~json
{
  "source": "00b6fd80",
  "target": "00b6fcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd84`](#insn-00b6fd84)

~~~json
{
  "source": "00b6fd84",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
