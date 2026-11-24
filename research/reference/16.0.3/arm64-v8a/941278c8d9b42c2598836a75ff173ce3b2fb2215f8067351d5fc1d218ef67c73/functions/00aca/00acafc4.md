# 00acafc4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac9fd0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9fd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-179134abf8b4245bde1709ccba9618ed)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acafc4",
  "name": "FUN_00acafc4",
  "size": 656,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8891e93fac1ef4c78ddad3caf4e8b602c0f6341fea7766c101f9b1c8b7f74089",
  "source_text_sha256": "8891e93fac1ef4c78ddad3caf4e8b602c0f6341fea7766c101f9b1c8b7f74089",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acafc4",
        "00acb24f"
      ],
      [
        "00acb2d0",
        "00acb2d3"
      ]
    ],
    "bytes_sha256": "b2a0373cb2119a1d522e245ab34eeace273318c9916c5da6456b632949382ba7",
    "instruction_count": 164,
    "instruction_bytes": 656,
    "body_bytes": 656,
    "indirect": 5,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [007890e0](../00789/007890e0.md)
- [0082fe24](../0082f/0082fe24.md)
- [008cbbc0](../008cb/008cbbc0.md)
- [008ff9e4](../008ff/008ff9e4.md)
- [00a3eea0](../00a3e/00a3eea0.md)
- [00ac14b8](../00ac1/00ac14b8.md)

## 呼び出し先

- [0046cd24](../0046c/0046cd24.md)
- [0048a2ac](../0048a/0048a2ac.md)
- [005d8fb8](../005d8/005d8fb8.md)
- [008524fc](../00852/008524fc.md)
- [008b7f1c](../008b7/008b7f1c.md)
- [008b7ff0](../008b7/008b7ff0.md)
- [00a477cc](../00a47/00a477cc.md)
- [00a47910](../00a47/00a47910.md)
- [00a47944](../00a47/00a47944.md)
- [00acc5a8](../00acc/00acc5a8.md)
- [00acc5ac](../00acc/00acc5ac.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3023 bytes

~~~c

void FUN_00acafc4(long param_1,undefined8 param_2,undefined8 param_3,undefined4 param_4)

{
  long lVar1;
  undefined *puVar2;
  undefined *puVar3;
  int iVar4;
  long lVar5;
  long *plVar6;
  undefined8 uVar7;
  undefined ***pppuVar8;
  long *plVar9;
  long *local_a8;
  long *local_a0;
  long *local_98;
  undefined **local_90 [4];
  undefined ***local_70;
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  *(undefined4 *)(param_1 + 8) = param_4;
  FUN_008524fc();
  iVar4 = FUN_0046cd24();
  lVar5 = FUN_0048a2ac(param_3,0xb);
  iVar4 = iVar4 - *(int *)(lVar5 + 8);
  FUN_00a47944(&local_98,param_2,iVar4 + 0x2d,0x261,0x15);
  (**(code **)(*local_98 + 0x10))(local_98,1);
  FUN_00a47910(0x3f800000,0x3f800000);
  plVar6 = local_98;
  FUN_00a47944(&local_a8,param_2,0x1c,0xfffffff8,0x12);
  local_a0 = local_a8;
  local_a8 = (long *)0x0;
  plVar6 = (long *)FUN_00a477cc(plVar6,&local_a0);
  (**(code **)(*plVar6 + 0x10))(plVar6,1);
  plVar6 = local_a0;
  puVar2 = PTR_DAT_00c9c408;
  local_a0 = (long *)0x0;
  if (plVar6 != (long *)0x0) {
    *plVar6 = (long)(PTR_DAT_00c9c408 + 0x10);
    FUN_005d8fb8(plVar6 + 10);
    _ZdlPv(plVar6);
  }
  plVar6 = local_a8;
  puVar3 = PTR_DAT_00c9c410;
  local_a8 = (long *)0x0;
  if (plVar6 != (long *)0x0) {
    plVar9 = (long *)plVar6[0x16];
    *plVar6 = (long)(PTR_DAT_00c9c410 + 0x10);
    if ((plVar9 != (long *)0x0) && (lVar5 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    *plVar6 = (long)(puVar2 + 0x10);
    FUN_005d8fb8(plVar6 + 10);
    _ZdlPv(plVar6);
  }
  lVar5 = FUN_008524fc();
  local_70 = local_90;
  local_a0 = local_98;
  local_98 = (long *)0x0;
  local_90[0] = &PTR_FUN_00c8e8e0;
  uVar7 = FUN_008b7ff0(lVar5 + 0x2f38,*(undefined4 *)(param_1 + 8),iVar4 + -2,0x238,0x4b,0x52,
                       &local_a0,local_90);
  FUN_008b7f1c(uVar7,0);
  if (local_70 == local_90) {
    lVar5 = 0x20;
    pppuVar8 = local_90;
  }
  else {
    if (local_70 == (undefined ***)0x0) goto LAB_00acb1a4;
    lVar5 = 0x28;
    pppuVar8 = local_70;
  }
  (**(code **)((long)*pppuVar8 + lVar5))();
LAB_00acb1a4:
  plVar6 = local_a0;
  local_a0 = (long *)0x0;
  if (plVar6 != (long *)0x0) {
    *plVar6 = (long)(puVar2 + 0x10);
    FUN_005d8fb8(plVar6 + 10);
    _ZdlPv(plVar6);
  }
  plVar6 = local_98;
  local_98 = (long *)0x0;
  if (plVar6 != (long *)0x0) {
    plVar9 = (long *)plVar6[0x16];
    *plVar6 = (long)(puVar3 + 0x10);
    if ((plVar9 != (long *)0x0) && (lVar5 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    *plVar6 = (long)(puVar2 + 0x10);
    FUN_005d8fb8(plVar6 + 10);
    _ZdlPv(plVar6);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
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
<a id="insn-00acafc4"></a> `00acafc4` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00acafc8"></a> `00acafc8` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acafcc"></a> `00acafcc` | `f9 3b 00 f9` | str x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acafd0"></a> `00acafd0` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acafd4"></a> `00acafd4` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acafd8"></a> `00acafd8` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acafdc"></a> `00acafdc` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acafe0"></a> `00acafe0` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acafe4"></a> `00acafe4` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00acafe8"></a> `00acafe8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00acafec"></a> `00acafec` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00acaff0"></a> `00acaff0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acaff4"></a> `00acaff4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acaff8"></a> `00acaff8` | `03 08 00 b9` | str w3,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acaffc"></a> `00acaffc` | `40 1d f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00acb000"></a> `00acb000` | `49 87 e6 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-00acb004"></a> `00acb004` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00acb008"></a> `00acb008` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acb00c"></a> `00acb00c` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00acb010"></a> `00acb010` | `a7 fc e6 97` | bl 0x0048a2ac | `UNCONDITIONAL_CALL`
<a id="insn-00acb014"></a> `00acb014` | `08 08 40 b9` | ldr w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acb018"></a> `00acb018` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb01c"></a> `00acb01c` | `22 4c 80 52` | mov w2,#0x261 | `FALL_THROUGH`
<a id="insn-00acb020"></a> `00acb020` | `a3 02 80 52` | mov w3,#0x15 | `FALL_THROUGH`
<a id="insn-00acb024"></a> `00acb024` | `d8 02 08 4b` | sub w24,w22,w8 | `FALL_THROUGH`
<a id="insn-00acb028"></a> `00acb028` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00acb02c"></a> `00acb02c` | `01 b7 00 11` | add w1,w24,#0x2d | `FALL_THROUGH`
<a id="insn-00acb030"></a> `00acb030` | `45 f2 fd 97` | bl 0x00a47944 | `UNCONDITIONAL_CALL`
<a id="insn-00acb034"></a> `00acb034` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acb038"></a> `00acb038` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acb03c"></a> `00acb03c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acb040"></a> `00acb040` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acb044"></a> `00acb044` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acb048"></a> `00acb048` | `00 10 2e 1e` | fmov s0,0x3f800000 | `FALL_THROUGH`
<a id="insn-00acb04c"></a> `00acb04c` | `01 10 2e 1e` | fmov s1,0x3f800000 | `FALL_THROUGH`
<a id="insn-00acb050"></a> `00acb050` | `30 f2 fd 97` | bl 0x00a47910 | `UNCONDITIONAL_CALL`
<a id="insn-00acb054"></a> `00acb054` | `f5 0f 40 f9` | ldr x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acb058"></a> `00acb058` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acb05c"></a> `00acb05c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb060"></a> `00acb060` | `81 03 80 52` | mov w1,#0x1c | `FALL_THROUGH`
<a id="insn-00acb064"></a> `00acb064` | `e2 00 80 12` | mov w2,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00acb068"></a> `00acb068` | `43 02 80 52` | mov w3,#0x12 | `FALL_THROUGH`
<a id="insn-00acb06c"></a> `00acb06c` | `36 f2 fd 97` | bl 0x00a47944 | `UNCONDITIONAL_CALL`
<a id="insn-00acb070"></a> `00acb070` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acb074"></a> `00acb074` | `ff a3 00 a9` | stp xzr,x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acb078"></a> `00acb078` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acb07c"></a> `00acb07c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acb080"></a> `00acb080` | `d3 f1 fd 97` | bl 0x00a477cc | `UNCONDITIONAL_CALL`
<a id="insn-00acb084"></a> `00acb084` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acb088"></a> `00acb088` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acb08c"></a> `00acb08c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acb090"></a> `00acb090` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acb094"></a> `00acb094` | `96 0e 00 b0` | adrp x22,0xc9c000 | `FALL_THROUGH`
<a id="insn-00acb098"></a> `00acb098` | `f4 0b 40 f9` | ldr x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb09c"></a> `00acb09c` | `d6 06 42 f9` | ldr x22,[x22, #0x408] | `FALL_THROUGH`
<a id="insn-00acb0a0"></a> `00acb0a0` | `ff 0b 00 f9` | str xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb0a4"></a> `00acb0a4` | `f4 00 00 b4` | cbz x20,0x00acb0c0 | `CONDITIONAL_JUMP`
<a id="insn-00acb0a8"></a> `00acb0a8` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00acb0ac"></a> `00acb0ac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb0b0"></a> `00acb0b0` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00acb0b4"></a> `00acb0b4` | `c1 37 ec 97` | bl 0x005d8fb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb0b8"></a> `00acb0b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb0bc"></a> `00acb0bc` | `a5 37 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acb0c0"></a> `00acb0c0` | `99 0e 00 b0` | adrp x25,0xc9c000 | `FALL_THROUGH`
<a id="insn-00acb0c4"></a> `00acb0c4` | `f4 07 40 f9` | ldr x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acb0c8"></a> `00acb0c8` | `39 0b 42 f9` | ldr x25,[x25, #0x410] | `FALL_THROUGH`
<a id="insn-00acb0cc"></a> `00acb0cc` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acb0d0"></a> `00acb0d0` | `b4 02 00 b4` | cbz x20,0x00acb124 | `CONDITIONAL_JUMP`
<a id="insn-00acb0d4"></a> `00acb0d4` | `95 5a 40 f9` | ldr x21,[x20, #0xb0] | `FALL_THROUGH`
<a id="insn-00acb0d8"></a> `00acb0d8` | `28 43 00 91` | add x8,x25,#0x10 | `FALL_THROUGH`
<a id="insn-00acb0dc"></a> `00acb0dc` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00acb0e0"></a> `00acb0e0` | `75 01 00 b4` | cbz x21,0x00acb10c | `CONDITIONAL_JUMP`
<a id="insn-00acb0e4"></a> `00acb0e4` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00acb0e8"></a> `00acb0e8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acb0ec"></a> `00acb0ec` | `29 27 06 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00acb0f0"></a> `00acb0f0` | `e0 00 00 b5` | cbnz x0,0x00acb10c | `CONDITIONAL_JUMP`
<a id="insn-00acb0f4"></a> `00acb0f4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00acb0f8"></a> `00acb0f8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acb0fc"></a> `00acb0fc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acb100"></a> `00acb100` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acb104"></a> `00acb104` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acb108"></a> `00acb108` | `86 37 06 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00acb10c"></a> `00acb10c` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00acb110"></a> `00acb110` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb114"></a> `00acb114` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00acb118"></a> `00acb118` | `a8 37 ec 97` | bl 0x005d8fb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb11c"></a> `00acb11c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb120"></a> `00acb120` | `8c 37 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acb124"></a> `00acb124` | `f6 1c f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00acb128"></a> `00acb128` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acb12c"></a> `00acb12c` | `61 0a 40 b9` | ldr w1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00acb130"></a> `00acb130` | `09 0e 00 f0` | adrp x9,0xc8e000 | `FALL_THROUGH`
<a id="insn-00acb134"></a> `00acb134` | `29 81 23 91` | add x9,x9,#0x8e0 | `FALL_THROUGH`
<a id="insn-00acb138"></a> `00acb138` | `f3 83 00 91` | add x19,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acb13c"></a> `00acb13c` | `02 0b 00 51` | sub w2,w24,#0x2 | `FALL_THROUGH`
<a id="insn-00acb140"></a> `00acb140` | `e8 7f 01 a9` | stp x8,xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb144"></a> `00acb144` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00acb148"></a> `00acb148` | `e9 13 00 f9` | str x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acb14c"></a> `00acb14c` | `f3 23 00 f9` | str x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acb150"></a> `00acb150` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00acb154"></a> `00acb154` | `e6 43 00 91` | add x6,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acb158"></a> `00acb158` | `e7 83 00 91` | add x7,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acb15c"></a> `00acb15c` | `03 47 80 52` | mov w3,#0x238 | `FALL_THROUGH`
<a id="insn-00acb160"></a> `00acb160` | `64 09 80 52` | mov w4,#0x4b | `FALL_THROUGH`
<a id="insn-00acb164"></a> `00acb164` | `45 0a 80 52` | mov w5,#0x52 | `FALL_THROUGH`
<a id="insn-00acb168"></a> `00acb168` | `a2 b3 f7 97` | bl 0x008b7ff0 | `UNCONDITIONAL_CALL`
<a id="insn-00acb16c"></a> `00acb16c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acb170"></a> `00acb170` | `6b b3 f7 97` | bl 0x008b7f1c | `UNCONDITIONAL_CALL`
<a id="insn-00acb174"></a> `00acb174` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acb178"></a> `00acb178` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acb17c"></a> `00acb17c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00acb180"></a> `00acb180` | `80 00 00 54` | b.eq 0x00acb190 | `CONDITIONAL_JUMP`
<a id="insn-00acb184"></a> `00acb184` | `00 01 00 b4` | cbz x0,0x00acb1a4 | `CONDITIONAL_JUMP`
<a id="insn-00acb188"></a> `00acb188` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00acb18c"></a> `00acb18c` | `03 00 00 14` | b 0x00acb198 | `UNCONDITIONAL_JUMP`
<a id="insn-00acb190"></a> `00acb190` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00acb194"></a> `00acb194` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acb198"></a> `00acb198` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00acb19c"></a> `00acb19c` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acb1a0"></a> `00acb1a0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acb1a4"></a> `00acb1a4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb1a8"></a> `00acb1a8` | `ff 0b 00 f9` | str xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb1ac"></a> `00acb1ac` | `f3 00 00 b4` | cbz x19,0x00acb1c8 | `CONDITIONAL_JUMP`
<a id="insn-00acb1b0"></a> `00acb1b0` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00acb1b4"></a> `00acb1b4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb1b8"></a> `00acb1b8` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00acb1bc"></a> `00acb1bc` | `7f 37 ec 97` | bl 0x005d8fb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb1c0"></a> `00acb1c0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb1c4"></a> `00acb1c4` | `63 37 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acb1c8"></a> `00acb1c8` | `f3 0f 40 f9` | ldr x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acb1cc"></a> `00acb1cc` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acb1d0"></a> `00acb1d0` | `b3 02 00 b4` | cbz x19,0x00acb224 | `CONDITIONAL_JUMP`
<a id="insn-00acb1d4"></a> `00acb1d4` | `74 5a 40 f9` | ldr x20,[x19, #0xb0] | `FALL_THROUGH`
<a id="insn-00acb1d8"></a> `00acb1d8` | `28 43 00 91` | add x8,x25,#0x10 | `FALL_THROUGH`
<a id="insn-00acb1dc"></a> `00acb1dc` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00acb1e0"></a> `00acb1e0` | `74 01 00 b4` | cbz x20,0x00acb20c | `CONDITIONAL_JUMP`
<a id="insn-00acb1e4"></a> `00acb1e4` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acb1e8"></a> `00acb1e8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acb1ec"></a> `00acb1ec` | `e9 26 06 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00acb1f0"></a> `00acb1f0` | `e0 00 00 b5` | cbnz x0,0x00acb20c | `CONDITIONAL_JUMP`
<a id="insn-00acb1f4"></a> `00acb1f4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acb1f8"></a> `00acb1f8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb1fc"></a> `00acb1fc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acb200"></a> `00acb200` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acb204"></a> `00acb204` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb208"></a> `00acb208` | `46 37 06 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00acb20c"></a> `00acb20c` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00acb210"></a> `00acb210` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb214"></a> `00acb214` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00acb218"></a> `00acb218` | `68 37 ec 97` | bl 0x005d8fb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb21c"></a> `00acb21c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb220"></a> `00acb220` | `4c 37 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acb224"></a> `00acb224` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00acb228"></a> `00acb228` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acb22c"></a> `00acb22c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acb230"></a> `00acb230` | `01 05 00 54` | b.ne 0x00acb2d0 | `CONDITIONAL_JUMP`
<a id="insn-00acb234"></a> `00acb234` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acb238"></a> `00acb238` | `f9 3b 40 f9` | ldr x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acb23c"></a> `00acb23c` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acb240"></a> `00acb240` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acb244"></a> `00acb244` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acb248"></a> `00acb248` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00acb24c"></a> `00acb24c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acb2d0"></a> `00acb2d0` | `2c 37 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acafc4`](#insn-00acafc4) 範囲 `[['00acafc4', '00acb0a7']]`
  - `CONDITIONAL_JUMP` [`00acb0a4`](#insn-00acb0a4) → [`00acb0c0`](#insn-00acb0c0)
  - `FALL_THROUGH` [`00acb0a4`](#insn-00acb0a4) → [`00acb0a8`](#insn-00acb0a8)
- ブロック [`00acb0a8`](#insn-00acb0a8) 範囲 `[['00acb0a8', '00acb0bf']]`
  - `FALL_THROUGH` [`00acb0bc`](#insn-00acb0bc) → [`00acb0c0`](#insn-00acb0c0)
- ブロック [`00acb0c0`](#insn-00acb0c0) 範囲 `[['00acb0c0', '00acb0d3']]`
  - `CONDITIONAL_JUMP` [`00acb0d0`](#insn-00acb0d0) → [`00acb124`](#insn-00acb124)
  - `FALL_THROUGH` [`00acb0d0`](#insn-00acb0d0) → [`00acb0d4`](#insn-00acb0d4)
- ブロック [`00acb0d4`](#insn-00acb0d4) 範囲 `[['00acb0d4', '00acb0e3']]`
  - `CONDITIONAL_JUMP` [`00acb0e0`](#insn-00acb0e0) → [`00acb10c`](#insn-00acb10c)
  - `FALL_THROUGH` [`00acb0e0`](#insn-00acb0e0) → [`00acb0e4`](#insn-00acb0e4)
- ブロック [`00acb0e4`](#insn-00acb0e4) 範囲 `[['00acb0e4', '00acb0f3']]`
  - `CONDITIONAL_JUMP` [`00acb0f0`](#insn-00acb0f0) → [`00acb10c`](#insn-00acb10c)
  - `FALL_THROUGH` [`00acb0f0`](#insn-00acb0f0) → [`00acb0f4`](#insn-00acb0f4)
- ブロック [`00acb0f4`](#insn-00acb0f4) 範囲 `[['00acb0f4', '00acb10b']]`
  - `FALL_THROUGH` [`00acb108`](#insn-00acb108) → [`00acb10c`](#insn-00acb10c)
- ブロック [`00acb10c`](#insn-00acb10c) 範囲 `[['00acb10c', '00acb123']]`
  - `FALL_THROUGH` [`00acb120`](#insn-00acb120) → [`00acb124`](#insn-00acb124)
- ブロック [`00acb124`](#insn-00acb124) 範囲 `[['00acb124', '00acb183']]`
  - `CONDITIONAL_JUMP` [`00acb180`](#insn-00acb180) → [`00acb190`](#insn-00acb190)
  - `FALL_THROUGH` [`00acb180`](#insn-00acb180) → [`00acb184`](#insn-00acb184)
- ブロック [`00acb184`](#insn-00acb184) 範囲 `[['00acb184', '00acb187']]`
  - `CONDITIONAL_JUMP` [`00acb184`](#insn-00acb184) → [`00acb1a4`](#insn-00acb1a4)
  - `FALL_THROUGH` [`00acb184`](#insn-00acb184) → [`00acb188`](#insn-00acb188)
- ブロック [`00acb188`](#insn-00acb188) 範囲 `[['00acb188', '00acb18f']]`
  - `UNCONDITIONAL_JUMP` [`00acb18c`](#insn-00acb18c) → [`00acb198`](#insn-00acb198)
- ブロック [`00acb190`](#insn-00acb190) 範囲 `[['00acb190', '00acb197']]`
  - `FALL_THROUGH` [`00acb194`](#insn-00acb194) → [`00acb198`](#insn-00acb198)
- ブロック [`00acb198`](#insn-00acb198) 範囲 `[['00acb198', '00acb1a3']]`
  - `FALL_THROUGH` [`00acb1a0`](#insn-00acb1a0) → [`00acb1a4`](#insn-00acb1a4)
- ブロック [`00acb1a4`](#insn-00acb1a4) 範囲 `[['00acb1a4', '00acb1af']]`
  - `CONDITIONAL_JUMP` [`00acb1ac`](#insn-00acb1ac) → [`00acb1c8`](#insn-00acb1c8)
  - `FALL_THROUGH` [`00acb1ac`](#insn-00acb1ac) → [`00acb1b0`](#insn-00acb1b0)
- ブロック [`00acb1b0`](#insn-00acb1b0) 範囲 `[['00acb1b0', '00acb1c7']]`
  - `FALL_THROUGH` [`00acb1c4`](#insn-00acb1c4) → [`00acb1c8`](#insn-00acb1c8)
- ブロック [`00acb1c8`](#insn-00acb1c8) 範囲 `[['00acb1c8', '00acb1d3']]`
  - `CONDITIONAL_JUMP` [`00acb1d0`](#insn-00acb1d0) → [`00acb224`](#insn-00acb224)
  - `FALL_THROUGH` [`00acb1d0`](#insn-00acb1d0) → [`00acb1d4`](#insn-00acb1d4)
- ブロック [`00acb1d4`](#insn-00acb1d4) 範囲 `[['00acb1d4', '00acb1e3']]`
  - `CONDITIONAL_JUMP` [`00acb1e0`](#insn-00acb1e0) → [`00acb20c`](#insn-00acb20c)
  - `FALL_THROUGH` [`00acb1e0`](#insn-00acb1e0) → [`00acb1e4`](#insn-00acb1e4)
- ブロック [`00acb1e4`](#insn-00acb1e4) 範囲 `[['00acb1e4', '00acb1f3']]`
  - `CONDITIONAL_JUMP` [`00acb1f0`](#insn-00acb1f0) → [`00acb20c`](#insn-00acb20c)
  - `FALL_THROUGH` [`00acb1f0`](#insn-00acb1f0) → [`00acb1f4`](#insn-00acb1f4)
- ブロック [`00acb1f4`](#insn-00acb1f4) 範囲 `[['00acb1f4', '00acb20b']]`
  - `FALL_THROUGH` [`00acb208`](#insn-00acb208) → [`00acb20c`](#insn-00acb20c)
- ブロック [`00acb20c`](#insn-00acb20c) 範囲 `[['00acb20c', '00acb223']]`
  - `FALL_THROUGH` [`00acb220`](#insn-00acb220) → [`00acb224`](#insn-00acb224)
- ブロック [`00acb224`](#insn-00acb224) 範囲 `[['00acb224', '00acb233']]`
  - `CONDITIONAL_JUMP` [`00acb230`](#insn-00acb230) → [`00acb2d0`](#insn-00acb2d0)
  - `FALL_THROUGH` [`00acb230`](#insn-00acb230) → [`00acb234`](#insn-00acb234)
- ブロック [`00acb234`](#insn-00acb234) 範囲 `[['00acb234', '00acb24f']]`
- ブロック [`00acb2d0`](#insn-00acb2d0) 範囲 `[['00acb2d0', '00acb2d3']]`

## 命令位置別の参照

- [`00acafc8`](#insn-00acafc8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafcc`](#insn-00acafcc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafd0`](#insn-00acafd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafd4`](#insn-00acafd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafd8`](#insn-00acafd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaff4`](#insn-00acaff4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaffc`](#insn-00acaffc) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00acb000`](#insn-00acb000) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`00acb010`](#insn-00acb010) → [`0048a2ac`](../0048a/0048a2ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048a2ac` · 推定シンボル `None` · 推定型 `None`
- [`00acb030`](#insn-00acb030) → [`00a47944`](../00a47/00a47944.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a47944` · 推定シンボル `None` · 推定型 `None`
- [`00acb034`](#insn-00acb034) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb050`](#insn-00acb050) → [`00a47910`](../00a47/00a47910.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a47910` · 推定シンボル `None` · 推定型 `None`
- [`00acb054`](#insn-00acb054) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb06c`](#insn-00acb06c) → [`00a47944`](../00a47/00a47944.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a47944` · 推定シンボル `None` · 推定型 `None`
- [`00acb070`](#insn-00acb070) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb074`](#insn-00acb074) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb080`](#insn-00acb080) → [`00a477cc`](../00a47/00a477cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a477cc` · 推定シンボル `None` · 推定型 `None`
- [`00acb098`](#insn-00acb098) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb09c`](#insn-00acb09c) → `00c9c408`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acb0a0`](#insn-00acb0a0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0a4`](#insn-00acb0a4) → [`00acb0c0`](#insn-00acb0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0b0`](#insn-00acb0b0) → `00c8c7f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acb0b4`](#insn-00acb0b4) → [`005d8fb8`](../005d8/005d8fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8fb8` · 推定シンボル `None` · 推定型 `None`
- [`00acb0bc`](#insn-00acb0bc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00acb0c4`](#insn-00acb0c4) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0c8`](#insn-00acb0c8) → `00c9c410`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acb0cc`](#insn-00acb0cc) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0d0`](#insn-00acb0d0) → [`00acb124`](#insn-00acb124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0dc`](#insn-00acb0dc) → `00c8c850`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acb0e0`](#insn-00acb0e0) → [`00acb10c`](#insn-00acb10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0ec`](#insn-00acb0ec) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00acb0f0`](#insn-00acb0f0) → [`00acb10c`](#insn-00acb10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb108`](#insn-00acb108) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00acb114`](#insn-00acb114) → `00c8c7f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acb118`](#insn-00acb118) → [`005d8fb8`](../005d8/005d8fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8fb8` · 推定シンボル `None` · 推定型 `None`
- [`00acb120`](#insn-00acb120) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00acb124`](#insn-00acb124) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00acb128`](#insn-00acb128) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb140`](#insn-00acb140) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb148`](#insn-00acb148) → `00c8e8e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acb148`](#insn-00acb148) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb14c`](#insn-00acb14c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb168`](#insn-00acb168) → [`008b7ff0`](../008b7/008b7ff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7ff0` · 推定シンボル `None` · 推定型 `None`
- [`00acb170`](#insn-00acb170) → [`008b7f1c`](../008b7/008b7f1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7f1c` · 推定シンボル `None` · 推定型 `None`
- [`00acb174`](#insn-00acb174) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb180`](#insn-00acb180) → [`00acb190`](#insn-00acb190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb184`](#insn-00acb184) → [`00acb1a4`](#insn-00acb1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb18c`](#insn-00acb18c) → [`00acb198`](#insn-00acb198) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb198`](#insn-00acb198) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb19c`](#insn-00acb19c) → `00c8e900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acb19c`](#insn-00acb19c) → `00c8e908`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acb1a0`](#insn-00acb1a0) → [`00acc5a8`](../00acc/00acc5a8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acc5a8` · 推定シンボル `None` · 推定型 `None`
- [`00acb1a0`](#insn-00acb1a0) → [`00acc5ac`](../00acc/00acc5ac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acc5ac` · 推定シンボル `None` · 推定型 `None`
- [`00acb1a4`](#insn-00acb1a4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1a8`](#insn-00acb1a8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1ac`](#insn-00acb1ac) → [`00acb1c8`](#insn-00acb1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1b8`](#insn-00acb1b8) → `00c8c7f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acb1bc`](#insn-00acb1bc) → [`005d8fb8`](../005d8/005d8fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8fb8` · 推定シンボル `None` · 推定型 `None`
- [`00acb1c4`](#insn-00acb1c4) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00acb1c8`](#insn-00acb1c8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1cc`](#insn-00acb1cc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1d0`](#insn-00acb1d0) → [`00acb224`](#insn-00acb224) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1dc`](#insn-00acb1dc) → `00c8c850`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acb1e0`](#insn-00acb1e0) → [`00acb20c`](#insn-00acb20c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1ec`](#insn-00acb1ec) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00acb1f0`](#insn-00acb1f0) → [`00acb20c`](#insn-00acb20c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb208`](#insn-00acb208) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00acb214`](#insn-00acb214) → `00c8c7f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acb218`](#insn-00acb218) → [`005d8fb8`](../005d8/005d8fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8fb8` · 推定シンボル `None` · 推定型 `None`
- [`00acb220`](#insn-00acb220) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00acb228`](#insn-00acb228) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb230`](#insn-00acb230) → [`00acb2d0`](#insn-00acb2d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb234`](#insn-00acb234) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb238`](#insn-00acb238) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb23c`](#insn-00acb23c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb240`](#insn-00acb240) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb244`](#insn-00acb244) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2d0`](#insn-00acb2d0) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acafc8`](#insn-00acafc8)

~~~json
{
  "source": "00acafc8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafcc`](#insn-00acafcc)

~~~json
{
  "source": "00acafcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafd0`](#insn-00acafd0)

~~~json
{
  "source": "00acafd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafd4`](#insn-00acafd4)

~~~json
{
  "source": "00acafd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafd8`](#insn-00acafd8)

~~~json
{
  "source": "00acafd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaff4`](#insn-00acaff4)

~~~json
{
  "source": "00acaff4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaffc`](#insn-00acaffc)

~~~json
{
  "source": "00acaffc",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb000`](#insn-00acb000)

~~~json
{
  "source": "00acb000",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb010`](#insn-00acb010)

~~~json
{
  "source": "00acb010",
  "target": "0048a2ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb030`](#insn-00acb030)

~~~json
{
  "source": "00acb030",
  "target": "00a47944",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb034`](#insn-00acb034)

~~~json
{
  "source": "00acb034",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb050`](#insn-00acb050)

~~~json
{
  "source": "00acb050",
  "target": "00a47910",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb054`](#insn-00acb054)

~~~json
{
  "source": "00acb054",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb06c`](#insn-00acb06c)

~~~json
{
  "source": "00acb06c",
  "target": "00a47944",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb070`](#insn-00acb070)

~~~json
{
  "source": "00acb070",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb074`](#insn-00acb074)

~~~json
{
  "source": "00acb074",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb080`](#insn-00acb080)

~~~json
{
  "source": "00acb080",
  "target": "00a477cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb098`](#insn-00acb098)

~~~json
{
  "source": "00acb098",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb09c`](#insn-00acb09c)

~~~json
{
  "source": "00acb09c",
  "target": "00c9c408",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c408",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb0a0`](#insn-00acb0a0)

~~~json
{
  "source": "00acb0a0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0a4`](#insn-00acb0a4)

~~~json
{
  "source": "00acb0a4",
  "target": "00acb0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0b0`](#insn-00acb0b0)

~~~json
{
  "source": "00acb0b0",
  "target": "00c8c7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c7f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb0b4`](#insn-00acb0b4)

~~~json
{
  "source": "00acb0b4",
  "target": "005d8fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb0bc`](#insn-00acb0bc)

~~~json
{
  "source": "00acb0bc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb0c4`](#insn-00acb0c4)

~~~json
{
  "source": "00acb0c4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0c8`](#insn-00acb0c8)

~~~json
{
  "source": "00acb0c8",
  "target": "00c9c410",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c410",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb0cc`](#insn-00acb0cc)

~~~json
{
  "source": "00acb0cc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0d0`](#insn-00acb0d0)

~~~json
{
  "source": "00acb0d0",
  "target": "00acb124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0dc`](#insn-00acb0dc)

~~~json
{
  "source": "00acb0dc",
  "target": "00c8c850",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c850",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb0e0`](#insn-00acb0e0)

~~~json
{
  "source": "00acb0e0",
  "target": "00acb10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0ec`](#insn-00acb0ec)

~~~json
{
  "source": "00acb0ec",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb0f0`](#insn-00acb0f0)

~~~json
{
  "source": "00acb0f0",
  "target": "00acb10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb108`](#insn-00acb108)

~~~json
{
  "source": "00acb108",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb114`](#insn-00acb114)

~~~json
{
  "source": "00acb114",
  "target": "00c8c7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c7f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb118`](#insn-00acb118)

~~~json
{
  "source": "00acb118",
  "target": "005d8fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb120`](#insn-00acb120)

~~~json
{
  "source": "00acb120",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb124`](#insn-00acb124)

~~~json
{
  "source": "00acb124",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb128`](#insn-00acb128)

~~~json
{
  "source": "00acb128",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb140`](#insn-00acb140)

~~~json
{
  "source": "00acb140",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb148`](#insn-00acb148)

~~~json
{
  "source": "00acb148",
  "target": "00c8e8e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e8e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb148`](#insn-00acb148)

~~~json
{
  "source": "00acb148",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb14c`](#insn-00acb14c)

~~~json
{
  "source": "00acb14c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb168`](#insn-00acb168)

~~~json
{
  "source": "00acb168",
  "target": "008b7ff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb170`](#insn-00acb170)

~~~json
{
  "source": "00acb170",
  "target": "008b7f1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb174`](#insn-00acb174)

~~~json
{
  "source": "00acb174",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb180`](#insn-00acb180)

~~~json
{
  "source": "00acb180",
  "target": "00acb190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb184`](#insn-00acb184)

~~~json
{
  "source": "00acb184",
  "target": "00acb1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb18c`](#insn-00acb18c)

~~~json
{
  "source": "00acb18c",
  "target": "00acb198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb198`](#insn-00acb198)

~~~json
{
  "source": "00acb198",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb19c`](#insn-00acb19c)

~~~json
{
  "source": "00acb19c",
  "target": "00c8e900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb19c`](#insn-00acb19c)

~~~json
{
  "source": "00acb19c",
  "target": "00c8e908",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e908",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb1a0`](#insn-00acb1a0)

~~~json
{
  "source": "00acb1a0",
  "target": "00acc5a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb1a0`](#insn-00acb1a0)

~~~json
{
  "source": "00acb1a0",
  "target": "00acc5ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb1a4`](#insn-00acb1a4)

~~~json
{
  "source": "00acb1a4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1a8`](#insn-00acb1a8)

~~~json
{
  "source": "00acb1a8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1ac`](#insn-00acb1ac)

~~~json
{
  "source": "00acb1ac",
  "target": "00acb1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1b8`](#insn-00acb1b8)

~~~json
{
  "source": "00acb1b8",
  "target": "00c8c7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c7f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb1bc`](#insn-00acb1bc)

~~~json
{
  "source": "00acb1bc",
  "target": "005d8fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb1c4`](#insn-00acb1c4)

~~~json
{
  "source": "00acb1c4",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb1c8`](#insn-00acb1c8)

~~~json
{
  "source": "00acb1c8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1cc`](#insn-00acb1cc)

~~~json
{
  "source": "00acb1cc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1d0`](#insn-00acb1d0)

~~~json
{
  "source": "00acb1d0",
  "target": "00acb224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1dc`](#insn-00acb1dc)

~~~json
{
  "source": "00acb1dc",
  "target": "00c8c850",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c850",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb1e0`](#insn-00acb1e0)

~~~json
{
  "source": "00acb1e0",
  "target": "00acb20c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1ec`](#insn-00acb1ec)

~~~json
{
  "source": "00acb1ec",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb1f0`](#insn-00acb1f0)

~~~json
{
  "source": "00acb1f0",
  "target": "00acb20c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb208`](#insn-00acb208)

~~~json
{
  "source": "00acb208",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb214`](#insn-00acb214)

~~~json
{
  "source": "00acb214",
  "target": "00c8c7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c7f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb218`](#insn-00acb218)

~~~json
{
  "source": "00acb218",
  "target": "005d8fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb220`](#insn-00acb220)

~~~json
{
  "source": "00acb220",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb228`](#insn-00acb228)

~~~json
{
  "source": "00acb228",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb230`](#insn-00acb230)

~~~json
{
  "source": "00acb230",
  "target": "00acb2d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb234`](#insn-00acb234)

~~~json
{
  "source": "00acb234",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb238`](#insn-00acb238)

~~~json
{
  "source": "00acb238",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb23c`](#insn-00acb23c)

~~~json
{
  "source": "00acb23c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb240`](#insn-00acb240)

~~~json
{
  "source": "00acb240",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb244`](#insn-00acb244)

~~~json
{
  "source": "00acb244",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2d0`](#insn-00acb2d0)

~~~json
{
  "source": "00acb2d0",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
