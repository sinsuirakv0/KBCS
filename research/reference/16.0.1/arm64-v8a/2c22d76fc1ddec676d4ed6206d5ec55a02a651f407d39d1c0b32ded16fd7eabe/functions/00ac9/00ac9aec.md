# 00ac9aec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ac98f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac98f0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-555cffcf06a270ccb80f0d65d90d620d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac9b5c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9b5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-781f0244f1fee5f00eb1d42368f9453d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac9aec",
  "name": "FUN_00ac9aec",
  "size": 996,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "362079c43759e15534431f383f3059d1b6fb256ee7449c2294c176ff771debc7",
  "source_text_sha256": "362079c43759e15534431f383f3059d1b6fb256ee7449c2294c176ff771debc7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac9aec",
        "00ac9ecb"
      ],
      [
        "00ac9f5c",
        "00ac9f5f"
      ]
    ],
    "bytes_sha256": "bd77b9b65ecd29133904ceddf9b5ce4ec619da9de47f95f010bf1b1a5421a4d4",
    "instruction_count": 249,
    "instruction_bytes": 996,
    "body_bytes": 996,
    "indirect": 10,
    "unresolved": 9
  }
}
~~~

## 呼び出し元

- [00788cac](../00788/00788cac.md)
- [0082ee20](../0082e/0082ee20.md)
- [008cabc0](../008ca/008cabc0.md)
- [008d1c40](../008d1/008d1c40.md)
- [008fe9e4](../008fe/008fe9e4.md)
- [00a3de58](../00a3d/00a3de58.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

- [0057bea8](../0057b/0057bea8.md)
- [005d8bc8](../005d8/005d8bc8.md)
- [008514f8](../00851/008514f8.md)
- [008b6f18](../008b6/008b6f18.md)
- [008b6f30](../008b6/008b6f30.md)
- [008b6fec](../008b6/008b6fec.md)
- [00a46784](../00a46/00a46784.md)
- [00a468c8](../00a46/00a468c8.md)
- [00a468d8](../00a46/00a468d8.md)
- [00a468fc](../00a46/00a468fc.md)
- [00ac871c](../00ac8/00ac871c.md)
- [00acb3e0](../00acb/00acb3e0.md)
- [00acb3e4](../00acb/00acb3e4.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6498 bytes

~~~c

void FUN_00ac9aec(long param_1,undefined8 param_2,undefined4 param_3,long *param_4)

{
  long lVar1;
  undefined *puVar2;
  undefined *puVar3;
  long *plVar4;
  long **pplVar5;
  undefined8 uVar6;
  undefined ***pppuVar7;
  long lVar8;
  long *plVar9;
  long *local_d0;
  long *local_c8;
  undefined **local_c0 [4];
  undefined ***local_a0;
  long *local_90 [4];
  long **local_70;
  long local_58;
  
                    /* catch() { ... } // from try @ 00ac96f4 with catch @ 00ac9af0 */
                    /* catch() { ... } // from try @ 00ac96e4 with catch @ 00ac9af4 */
                    /* catch() { ... } // from try @ 00ac99d0 with catch @ 00ac9afc */
                    /* catch() { ... } // from try @ 00ac95e0 with catch @ 00ac9b00
                       catch() { ... } // from try @ 00ac99c0 with catch @ 00ac9b00 */
                    /* catch() { ... } // from try @ 00ac9764 with catch @ 00ac9b08 */
  lVar1 = tpidr_el0;
                    /* catch() { ... } // from try @ 00ac959c with catch @ 00ac9b10 */
                    /* catch() { ... } // from try @ 00ac958c with catch @ 00ac9b14 */
  local_58 = *(long *)(lVar1 + 0x28);
                    /* catch() { ... } // from try @ 00ac96cc with catch @ 00ac9b1c */
  *(undefined4 *)(param_1 + 4) = param_3;
                    /* catch() { ... } // from try @ 00ac99b4 with catch @ 00ac9b20 */
  plVar4 = (long *)param_4[4];
                    /* catch() { ... } // from try @ 00ac9838 with catch @ 00ac9b24 */
  if (plVar4 == (long *)0x0) {
                    /* catch() { ... } // from try @ 00ac9530 with catch @ 00ac9b44 */
    local_70 = (long **)0x0;
                    /* catch() { ... } // from try @ 00ac9900 with catch @ 00ac9b48
                       catch() { ... } // from try @ 00ac9ae0 with catch @ 00ac9b48 */
  }
  else {
                    /* catch() { ... } // from try @ 00ac977c with catch @ 00ac9b28 */
                    /* catch() { ... } // from try @ 00ac9a10 with catch @ 00ac9b2c */
    if (plVar4 == param_4) {
      local_70 = local_90;
                    /* catch() { ... } // from try @ 00ac992c with catch @ 00ac9b50 */
                    /* catch() { ... } // from try @ 00ac985c with catch @ 00ac9b60
                       catch() { ... } // from try @ 00ac9ac8 with catch @ 00ac9b60 */
      (**(code **)(*param_4 + 0x18))(param_4,local_90);
    }
    else {
                    /* catch() { ... } // from try @ 00ac9978 with catch @ 00ac9b34 */
      local_70 = (long **)(**(code **)(*plVar4 + 0x10))();
                    /* catch() { ... } // from try @ 00ac9a28 with catch @ 00ac9b3c */
                    /* catch() { ... } // from try @ 00ac97b8 with catch @ 00ac9b40 */
    }
  }
                    /* catch() { ... } // from try @ 00ac98a4 with catch @ 00ac9b68 */
  FUN_0057bea8(local_90,param_1 + 0xb0);
  if (local_70 == local_90) {
    lVar8 = 0x20;
    pplVar5 = local_90;
LAB_00ac9b98:
    (**(code **)((long)*pplVar5 + lVar8))();
  }
  else if (local_70 != (long **)0x0) {
    lVar8 = 0x28;
    pplVar5 = local_70;
    goto LAB_00ac9b98;
  }
  FUN_00ac871c(param_1,4,0x21d,0x5f,0x5f);
  FUN_00a468fc(local_90,param_2,0x33,0x24c,9);
  (**(code **)(*local_90[0] + 0x10))(local_90[0],1);
  FUN_00a468c8(0x3f800000,0x3f800000);
  plVar4 = local_90[0];
  FUN_00a468fc(&local_d0,param_2,0xffffffff,0,3);
  local_c8 = local_d0;
  local_d0 = (long *)0x0;
  plVar4 = (long *)FUN_00a46784(plVar4,&local_c8);
  (**(code **)(*plVar4 + 0x10))(plVar4,1);
  plVar4 = local_c8;
  puVar2 = PTR_DAT_00c9b368;
  local_c8 = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    *plVar4 = (long)(PTR_DAT_00c9b368 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  plVar4 = local_d0;
  puVar3 = PTR_DAT_00c9b370;
  local_d0 = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    plVar9 = (long *)plVar4[0x16];
    *plVar4 = (long)(PTR_DAT_00c9b370 + 0x10);
    if ((plVar9 != (long *)0x0) && (lVar8 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), lVar8 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    *plVar4 = (long)(puVar2 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  plVar4 = local_90[0];
  FUN_00a468fc(&local_d0,param_2,0,0,0xc);
  local_c8 = local_d0;
  local_d0 = (long *)0x0;
  plVar4 = (long *)FUN_00a46784(plVar4,&local_c8);
  (**(code **)(*plVar4 + 0x10))(plVar4,1);
  uVar6 = FUN_00a468c8(0x40000000,0x40000000);
  FUN_00a468d8(uVar6,0);
  plVar4 = local_c8;
  local_c8 = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    *plVar4 = (long)(puVar2 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  plVar4 = local_d0;
  local_d0 = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    plVar9 = (long *)plVar4[0x16];
    *plVar4 = (long)(puVar3 + 0x10);
    if ((plVar9 != (long *)0x0) && (lVar8 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), lVar8 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    *plVar4 = (long)(puVar2 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  lVar8 = FUN_008514f8();
  local_c8 = local_90[0];
  local_a0 = local_c0;
  local_90[0] = (long *)0x0;
  local_c0[0] = &PTR_FUN_00c8d7c0;
  uVar6 = FUN_008b6fec(lVar8 + 0x2f38,*(undefined4 *)(param_1 + 4),4,0x21d,0x5f,0x5f,&local_c8,
                       local_c0);
  uVar6 = FUN_008b6f18(uVar6,0);
  FUN_008b6f30(uVar6,1);
  if (local_a0 == local_c0) {
    lVar8 = 0x20;
    pppuVar7 = local_c0;
  }
  else {
    if (local_a0 == (undefined ***)0x0) goto LAB_00ac9e20;
    lVar8 = 0x28;
    pppuVar7 = local_a0;
  }
  (**(code **)((long)*pppuVar7 + lVar8))();
LAB_00ac9e20:
  plVar4 = local_c8;
  local_c8 = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    *plVar4 = (long)(puVar2 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  plVar4 = local_90[0];
  local_90[0] = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    plVar9 = (long *)plVar4[0x16];
    *plVar4 = (long)(puVar3 + 0x10);
    if ((plVar9 != (long *)0x0) && (lVar8 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), lVar8 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    *plVar4 = (long)(puVar2 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
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
<a id="insn-00ac9aec"></a> `00ac9aec` | `ff 43 03 d1` | sub sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00ac9af0"></a> `00ac9af0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ac9af4"></a> `00ac9af4` | `f9 4b 00 f9` | str x25,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ac9af8"></a> `00ac9af8` | `f8 5f 0a a9` | stp x24,x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ac9afc"></a> `00ac9afc` | `f6 57 0b a9` | stp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00ac9b00"></a> `00ac9b00` | `f4 4f 0c a9` | stp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00ac9b04"></a> `00ac9b04` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00ac9b08"></a> `00ac9b08` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ac9b0c"></a> `00ac9b0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac9b10"></a> `00ac9b10` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00ac9b14"></a> `00ac9b14` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00ac9b18"></a> `00ac9b18` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac9b1c"></a> `00ac9b1c` | `02 04 00 b9` | str w2,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00ac9b20"></a> `00ac9b20` | `60 10 40 f9` | ldr x0,[x3, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9b24"></a> `00ac9b24` | `00 01 00 b4` | cbz x0,0x00ac9b44 | `CONDITIONAL_JUMP`
<a id="insn-00ac9b28"></a> `00ac9b28` | `1f 00 03 eb` | cmp x0,x3 | `FALL_THROUGH`
<a id="insn-00ac9b2c"></a> `00ac9b2c` | `00 01 00 54` | b.eq 0x00ac9b4c | `CONDITIONAL_JUMP`
<a id="insn-00ac9b30"></a> `00ac9b30` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ac9b34"></a> `00ac9b34` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9b38"></a> `00ac9b38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9b3c"></a> `00ac9b3c` | `e0 33 00 f9` | str x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ac9b40"></a> `00ac9b40` | `0a 00 00 14` | b 0x00ac9b68 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9b44"></a> `00ac9b44` | `ff 33 00 f9` | str xzr,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ac9b48"></a> `00ac9b48` | `08 00 00 14` | b 0x00ac9b68 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9b4c"></a> `00ac9b4c` | `e8 03 01 91` | add x8,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ac9b50"></a> `00ac9b50` | `69 00 40 f9` | ldr x9,[x3] | `FALL_THROUGH`
<a id="insn-00ac9b54"></a> `00ac9b54` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ac9b58"></a> `00ac9b58` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ac9b5c"></a> `00ac9b5c` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-00ac9b60"></a> `00ac9b60` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00ac9b64"></a> `00ac9b64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9b68"></a> `00ac9b68` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ac9b6c"></a> `00ac9b6c` | `61 c2 02 91` | add x1,x19,#0xb0 | `FALL_THROUGH`
<a id="insn-00ac9b70"></a> `00ac9b70` | `f5 03 01 91` | add x21,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ac9b74"></a> `00ac9b74` | `cd c8 ea 97` | bl 0x0057bea8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9b78"></a> `00ac9b78` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ac9b7c"></a> `00ac9b7c` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9b80"></a> `00ac9b80` | `80 00 00 54` | b.eq 0x00ac9b90 | `CONDITIONAL_JUMP`
<a id="insn-00ac9b84"></a> `00ac9b84` | `00 01 00 b4` | cbz x0,0x00ac9ba4 | `CONDITIONAL_JUMP`
<a id="insn-00ac9b88"></a> `00ac9b88` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ac9b8c"></a> `00ac9b8c` | `03 00 00 14` | b 0x00ac9b98 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9b90"></a> `00ac9b90` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ac9b94"></a> `00ac9b94` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ac9b98"></a> `00ac9b98` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ac9b9c"></a> `00ac9b9c` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac9ba0"></a> `00ac9ba0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9ba4"></a> `00ac9ba4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac9ba8"></a> `00ac9ba8` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00ac9bac"></a> `00ac9bac` | `a2 43 80 52` | mov w2,#0x21d | `FALL_THROUGH`
<a id="insn-00ac9bb0"></a> `00ac9bb0` | `e3 0b 80 52` | mov w3,#0x5f | `FALL_THROUGH`
<a id="insn-00ac9bb4"></a> `00ac9bb4` | `e4 0b 80 52` | mov w4,#0x5f | `FALL_THROUGH`
<a id="insn-00ac9bb8"></a> `00ac9bb8` | `d9 fa ff 97` | bl 0x00ac871c | `UNCONDITIONAL_CALL`
<a id="insn-00ac9bbc"></a> `00ac9bbc` | `e8 03 01 91` | add x8,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ac9bc0"></a> `00ac9bc0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9bc4"></a> `00ac9bc4` | `61 06 80 52` | mov w1,#0x33 | `FALL_THROUGH`
<a id="insn-00ac9bc8"></a> `00ac9bc8` | `82 49 80 52` | mov w2,#0x24c | `FALL_THROUGH`
<a id="insn-00ac9bcc"></a> `00ac9bcc` | `23 01 80 52` | mov w3,#0x9 | `FALL_THROUGH`
<a id="insn-00ac9bd0"></a> `00ac9bd0` | `4b f3 fd 97` | bl 0x00a468fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac9bd4"></a> `00ac9bd4` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9bd8"></a> `00ac9bd8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ac9bdc"></a> `00ac9bdc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9be0"></a> `00ac9be0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00ac9be4"></a> `00ac9be4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9be8"></a> `00ac9be8` | `00 10 2e 1e` | fmov s0,0x3f800000 | `FALL_THROUGH`
<a id="insn-00ac9bec"></a> `00ac9bec` | `01 10 2e 1e` | fmov s1,0x3f800000 | `FALL_THROUGH`
<a id="insn-00ac9bf0"></a> `00ac9bf0` | `36 f3 fd 97` | bl 0x00a468c8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9bf4"></a> `00ac9bf4` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9bf8"></a> `00ac9bf8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00ac9bfc"></a> `00ac9bfc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9c00"></a> `00ac9c00` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ac9c04"></a> `00ac9c04` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00ac9c08"></a> `00ac9c08` | `63 00 80 52` | mov w3,#0x3 | `FALL_THROUGH`
<a id="insn-00ac9c0c"></a> `00ac9c0c` | `3c f3 fd 97` | bl 0x00a468fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac9c10"></a> `00ac9c10` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ac9c14"></a> `00ac9c14` | `ff 23 00 a9` | stp xzr,x8,[sp] | `FALL_THROUGH`
<a id="insn-00ac9c18"></a> `00ac9c18` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ac9c1c"></a> `00ac9c1c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9c20"></a> `00ac9c20` | `d9 f2 fd 97` | bl 0x00a46784 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9c24"></a> `00ac9c24` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ac9c28"></a> `00ac9c28` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9c2c"></a> `00ac9c2c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00ac9c30"></a> `00ac9c30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9c34"></a> `00ac9c34` | `98 0e 00 d0` | adrp x24,0xc9b000 | `FALL_THROUGH`
<a id="insn-00ac9c38"></a> `00ac9c38` | `f5 07 40 f9` | ldr x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9c3c"></a> `00ac9c3c` | `18 b7 41 f9` | ldr x24,[x24, #0x368] | `FALL_THROUGH`
<a id="insn-00ac9c40"></a> `00ac9c40` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9c44"></a> `00ac9c44` | `f5 00 00 b4` | cbz x21,0x00ac9c60 | `CONDITIONAL_JUMP`
<a id="insn-00ac9c48"></a> `00ac9c48` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9c4c"></a> `00ac9c4c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9c50"></a> `00ac9c50` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00ac9c54"></a> `00ac9c54` | `dd 3b ec 97` | bl 0x005d8bc8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9c58"></a> `00ac9c58` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9c5c"></a> `00ac9c5c` | `95 38 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9c60"></a> `00ac9c60` | `99 0e 00 d0` | adrp x25,0xc9b000 | `FALL_THROUGH`
<a id="insn-00ac9c64"></a> `00ac9c64` | `f5 03 40 f9` | ldr x21,[sp] | `FALL_THROUGH`
<a id="insn-00ac9c68"></a> `00ac9c68` | `39 bb 41 f9` | ldr x25,[x25, #0x370] | `FALL_THROUGH`
<a id="insn-00ac9c6c"></a> `00ac9c6c` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00ac9c70"></a> `00ac9c70` | `b5 02 00 b4` | cbz x21,0x00ac9cc4 | `CONDITIONAL_JUMP`
<a id="insn-00ac9c74"></a> `00ac9c74` | `b6 5a 40 f9` | ldr x22,[x21, #0xb0] | `FALL_THROUGH`
<a id="insn-00ac9c78"></a> `00ac9c78` | `28 43 00 91` | add x8,x25,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9c7c"></a> `00ac9c7c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00ac9c80"></a> `00ac9c80` | `76 01 00 b4` | cbz x22,0x00ac9cac | `CONDITIONAL_JUMP`
<a id="insn-00ac9c84"></a> `00ac9c84` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00ac9c88"></a> `00ac9c88` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ac9c8c"></a> `00ac9c8c` | `1d 28 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9c90"></a> `00ac9c90` | `e0 00 00 b5` | cbnz x0,0x00ac9cac | `CONDITIONAL_JUMP`
<a id="insn-00ac9c94"></a> `00ac9c94` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00ac9c98"></a> `00ac9c98` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ac9c9c"></a> `00ac9c9c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9ca0"></a> `00ac9ca0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9ca4"></a> `00ac9ca4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ac9ca8"></a> `00ac9ca8` | `76 38 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9cac"></a> `00ac9cac` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9cb0"></a> `00ac9cb0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9cb4"></a> `00ac9cb4` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00ac9cb8"></a> `00ac9cb8` | `c4 3b ec 97` | bl 0x005d8bc8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9cbc"></a> `00ac9cbc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9cc0"></a> `00ac9cc0` | `7c 38 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9cc4"></a> `00ac9cc4` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9cc8"></a> `00ac9cc8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00ac9ccc"></a> `00ac9ccc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9cd0"></a> `00ac9cd0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ac9cd4"></a> `00ac9cd4` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00ac9cd8"></a> `00ac9cd8` | `83 01 80 52` | mov w3,#0xc | `FALL_THROUGH`
<a id="insn-00ac9cdc"></a> `00ac9cdc` | `08 f3 fd 97` | bl 0x00a468fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac9ce0"></a> `00ac9ce0` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ac9ce4"></a> `00ac9ce4` | `ff 23 00 a9` | stp xzr,x8,[sp] | `FALL_THROUGH`
<a id="insn-00ac9ce8"></a> `00ac9ce8` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ac9cec"></a> `00ac9cec` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9cf0"></a> `00ac9cf0` | `a5 f2 fd 97` | bl 0x00a46784 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9cf4"></a> `00ac9cf4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ac9cf8"></a> `00ac9cf8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9cfc"></a> `00ac9cfc` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00ac9d00"></a> `00ac9d00` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9d04"></a> `00ac9d04` | `00 10 20 1e` | fmov s0,0x40000000 | `FALL_THROUGH`
<a id="insn-00ac9d08"></a> `00ac9d08` | `01 10 20 1e` | fmov s1,0x40000000 | `FALL_THROUGH`
<a id="insn-00ac9d0c"></a> `00ac9d0c` | `ef f2 fd 97` | bl 0x00a468c8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9d10"></a> `00ac9d10` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ac9d14"></a> `00ac9d14` | `f1 f2 fd 97` | bl 0x00a468d8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9d18"></a> `00ac9d18` | `f4 07 40 f9` | ldr x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9d1c"></a> `00ac9d1c` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9d20"></a> `00ac9d20` | `f4 00 00 b4` | cbz x20,0x00ac9d3c | `CONDITIONAL_JUMP`
<a id="insn-00ac9d24"></a> `00ac9d24` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9d28"></a> `00ac9d28` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9d2c"></a> `00ac9d2c` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00ac9d30"></a> `00ac9d30` | `a6 3b ec 97` | bl 0x005d8bc8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9d34"></a> `00ac9d34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9d38"></a> `00ac9d38` | `5e 38 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9d3c"></a> `00ac9d3c` | `f4 03 40 f9` | ldr x20,[sp] | `FALL_THROUGH`
<a id="insn-00ac9d40"></a> `00ac9d40` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00ac9d44"></a> `00ac9d44` | `b4 02 00 b4` | cbz x20,0x00ac9d98 | `CONDITIONAL_JUMP`
<a id="insn-00ac9d48"></a> `00ac9d48` | `95 5a 40 f9` | ldr x21,[x20, #0xb0] | `FALL_THROUGH`
<a id="insn-00ac9d4c"></a> `00ac9d4c` | `28 43 00 91` | add x8,x25,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9d50"></a> `00ac9d50` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00ac9d54"></a> `00ac9d54` | `75 01 00 b4` | cbz x21,0x00ac9d80 | `CONDITIONAL_JUMP`
<a id="insn-00ac9d58"></a> `00ac9d58` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00ac9d5c"></a> `00ac9d5c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ac9d60"></a> `00ac9d60` | `e8 27 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9d64"></a> `00ac9d64` | `e0 00 00 b5` | cbnz x0,0x00ac9d80 | `CONDITIONAL_JUMP`
<a id="insn-00ac9d68"></a> `00ac9d68` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00ac9d6c"></a> `00ac9d6c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9d70"></a> `00ac9d70` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9d74"></a> `00ac9d74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9d78"></a> `00ac9d78` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9d7c"></a> `00ac9d7c` | `41 38 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9d80"></a> `00ac9d80` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9d84"></a> `00ac9d84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9d88"></a> `00ac9d88` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00ac9d8c"></a> `00ac9d8c` | `8f 3b ec 97` | bl 0x005d8bc8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9d90"></a> `00ac9d90` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9d94"></a> `00ac9d94` | `47 38 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9d98"></a> `00ac9d98` | `d8 1d f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9d9c"></a> `00ac9d9c` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9da0"></a> `00ac9da0` | `61 06 40 b9` | ldr w1,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00ac9da4"></a> `00ac9da4` | `29 0e 00 90` | adrp x9,0xc8d000 | `FALL_THROUGH`
<a id="insn-00ac9da8"></a> `00ac9da8` | `29 01 1f 91` | add x9,x9,#0x7c0 | `FALL_THROUGH`
<a id="insn-00ac9dac"></a> `00ac9dac` | `f3 43 00 91` | add x19,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9db0"></a> `00ac9db0` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9db4"></a> `00ac9db4` | `e8 a7 00 a9` | stp x8,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9db8"></a> `00ac9db8` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00ac9dbc"></a> `00ac9dbc` | `f3 1b 00 f9` | str x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ac9dc0"></a> `00ac9dc0` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00ac9dc4"></a> `00ac9dc4` | `e6 23 00 91` | add x6,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ac9dc8"></a> `00ac9dc8` | `e7 43 00 91` | add x7,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9dcc"></a> `00ac9dcc` | `82 00 80 52` | mov w2,#0x4 | `FALL_THROUGH`
<a id="insn-00ac9dd0"></a> `00ac9dd0` | `a3 43 80 52` | mov w3,#0x21d | `FALL_THROUGH`
<a id="insn-00ac9dd4"></a> `00ac9dd4` | `e4 0b 80 52` | mov w4,#0x5f | `FALL_THROUGH`
<a id="insn-00ac9dd8"></a> `00ac9dd8` | `e5 0b 80 52` | mov w5,#0x5f | `FALL_THROUGH`
<a id="insn-00ac9ddc"></a> `00ac9ddc` | `84 b4 f7 97` | bl 0x008b6fec | `UNCONDITIONAL_CALL`
<a id="insn-00ac9de0"></a> `00ac9de0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ac9de4"></a> `00ac9de4` | `4d b4 f7 97` | bl 0x008b6f18 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9de8"></a> `00ac9de8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00ac9dec"></a> `00ac9dec` | `51 b4 f7 97` | bl 0x008b6f30 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9df0"></a> `00ac9df0` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ac9df4"></a> `00ac9df4` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9df8"></a> `00ac9df8` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00ac9dfc"></a> `00ac9dfc` | `80 00 00 54` | b.eq 0x00ac9e0c | `CONDITIONAL_JUMP`
<a id="insn-00ac9e00"></a> `00ac9e00` | `00 01 00 b4` | cbz x0,0x00ac9e20 | `CONDITIONAL_JUMP`
<a id="insn-00ac9e04"></a> `00ac9e04` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ac9e08"></a> `00ac9e08` | `03 00 00 14` | b 0x00ac9e14 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9e0c"></a> `00ac9e0c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ac9e10"></a> `00ac9e10` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9e14"></a> `00ac9e14` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ac9e18"></a> `00ac9e18` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac9e1c"></a> `00ac9e1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9e20"></a> `00ac9e20` | `f3 07 40 f9` | ldr x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9e24"></a> `00ac9e24` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9e28"></a> `00ac9e28` | `f3 00 00 b4` | cbz x19,0x00ac9e44 | `CONDITIONAL_JUMP`
<a id="insn-00ac9e2c"></a> `00ac9e2c` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9e30"></a> `00ac9e30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac9e34"></a> `00ac9e34` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00ac9e38"></a> `00ac9e38` | `64 3b ec 97` | bl 0x005d8bc8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9e3c"></a> `00ac9e3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac9e40"></a> `00ac9e40` | `1c 38 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9e44"></a> `00ac9e44` | `f3 23 40 f9` | ldr x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9e48"></a> `00ac9e48` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9e4c"></a> `00ac9e4c` | `b3 02 00 b4` | cbz x19,0x00ac9ea0 | `CONDITIONAL_JUMP`
<a id="insn-00ac9e50"></a> `00ac9e50` | `74 5a 40 f9` | ldr x20,[x19, #0xb0] | `FALL_THROUGH`
<a id="insn-00ac9e54"></a> `00ac9e54` | `28 43 00 91` | add x8,x25,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9e58"></a> `00ac9e58` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00ac9e5c"></a> `00ac9e5c` | `74 01 00 b4` | cbz x20,0x00ac9e88 | `CONDITIONAL_JUMP`
<a id="insn-00ac9e60"></a> `00ac9e60` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ac9e64"></a> `00ac9e64` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ac9e68"></a> `00ac9e68` | `a6 27 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9e6c"></a> `00ac9e6c` | `e0 00 00 b5` | cbnz x0,0x00ac9e88 | `CONDITIONAL_JUMP`
<a id="insn-00ac9e70"></a> `00ac9e70` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ac9e74"></a> `00ac9e74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9e78"></a> `00ac9e78` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9e7c"></a> `00ac9e7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9e80"></a> `00ac9e80` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9e84"></a> `00ac9e84` | `ff 37 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9e88"></a> `00ac9e88` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00ac9e8c"></a> `00ac9e8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac9e90"></a> `00ac9e90` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00ac9e94"></a> `00ac9e94` | `4d 3b ec 97` | bl 0x005d8bc8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9e98"></a> `00ac9e98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac9e9c"></a> `00ac9e9c` | `05 38 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9ea0"></a> `00ac9ea0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00ac9ea4"></a> `00ac9ea4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac9ea8"></a> `00ac9ea8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ac9eac"></a> `00ac9eac` | `81 05 00 54` | b.ne 0x00ac9f5c | `CONDITIONAL_JUMP`
<a id="insn-00ac9eb0"></a> `00ac9eb0` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00ac9eb4"></a> `00ac9eb4` | `f9 4b 40 f9` | ldr x25,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ac9eb8"></a> `00ac9eb8` | `f6 57 4b a9` | ldp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00ac9ebc"></a> `00ac9ebc` | `f8 5f 4a a9` | ldp x24,x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ac9ec0"></a> `00ac9ec0` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ac9ec4"></a> `00ac9ec4` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00ac9ec8"></a> `00ac9ec8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ac9f5c"></a> `00ac9f5c` | `e1 37 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac9aec`](#insn-00ac9aec) 範囲 `[['00ac9aec', '00ac9aef']]`
  - `FALL_THROUGH` [`00ac9aec`](#insn-00ac9aec) → [`00ac9af0`](#insn-00ac9af0)
- ブロック [`00ac9af0`](#insn-00ac9af0) 範囲 `[['00ac9af0', '00ac9af3']]`
  - `FALL_THROUGH` [`00ac9af0`](#insn-00ac9af0) → [`00ac9af4`](#insn-00ac9af4)
- ブロック [`00ac9af4`](#insn-00ac9af4) 範囲 `[['00ac9af4', '00ac9afb']]`
  - `FALL_THROUGH` [`00ac9af8`](#insn-00ac9af8) → [`00ac9afc`](#insn-00ac9afc)
- ブロック [`00ac9afc`](#insn-00ac9afc) 範囲 `[['00ac9afc', '00ac9aff']]`
  - `FALL_THROUGH` [`00ac9afc`](#insn-00ac9afc) → [`00ac9b00`](#insn-00ac9b00)
- ブロック [`00ac9b00`](#insn-00ac9b00) 範囲 `[['00ac9b00', '00ac9b07']]`
  - `FALL_THROUGH` [`00ac9b04`](#insn-00ac9b04) → [`00ac9b08`](#insn-00ac9b08)
- ブロック [`00ac9b08`](#insn-00ac9b08) 範囲 `[['00ac9b08', '00ac9b0f']]`
  - `FALL_THROUGH` [`00ac9b0c`](#insn-00ac9b0c) → [`00ac9b10`](#insn-00ac9b10)
- ブロック [`00ac9b10`](#insn-00ac9b10) 範囲 `[['00ac9b10', '00ac9b13']]`
  - `FALL_THROUGH` [`00ac9b10`](#insn-00ac9b10) → [`00ac9b14`](#insn-00ac9b14)
- ブロック [`00ac9b14`](#insn-00ac9b14) 範囲 `[['00ac9b14', '00ac9b1b']]`
  - `FALL_THROUGH` [`00ac9b18`](#insn-00ac9b18) → [`00ac9b1c`](#insn-00ac9b1c)
- ブロック [`00ac9b1c`](#insn-00ac9b1c) 範囲 `[['00ac9b1c', '00ac9b1f']]`
  - `FALL_THROUGH` [`00ac9b1c`](#insn-00ac9b1c) → [`00ac9b20`](#insn-00ac9b20)
- ブロック [`00ac9b20`](#insn-00ac9b20) 範囲 `[['00ac9b20', '00ac9b23']]`
  - `FALL_THROUGH` [`00ac9b20`](#insn-00ac9b20) → [`00ac9b24`](#insn-00ac9b24)
- ブロック [`00ac9b24`](#insn-00ac9b24) 範囲 `[['00ac9b24', '00ac9b27']]`
  - `CONDITIONAL_JUMP` [`00ac9b24`](#insn-00ac9b24) → [`00ac9b44`](#insn-00ac9b44)
  - `FALL_THROUGH` [`00ac9b24`](#insn-00ac9b24) → [`00ac9b28`](#insn-00ac9b28)
- ブロック [`00ac9b28`](#insn-00ac9b28) 範囲 `[['00ac9b28', '00ac9b2b']]`
  - `FALL_THROUGH` [`00ac9b28`](#insn-00ac9b28) → [`00ac9b2c`](#insn-00ac9b2c)
- ブロック [`00ac9b2c`](#insn-00ac9b2c) 範囲 `[['00ac9b2c', '00ac9b2f']]`
  - `CONDITIONAL_JUMP` [`00ac9b2c`](#insn-00ac9b2c) → [`00ac9b4c`](#insn-00ac9b4c)
  - `FALL_THROUGH` [`00ac9b2c`](#insn-00ac9b2c) → [`00ac9b30`](#insn-00ac9b30)
- ブロック [`00ac9b30`](#insn-00ac9b30) 範囲 `[['00ac9b30', '00ac9b33']]`
  - `FALL_THROUGH` [`00ac9b30`](#insn-00ac9b30) → [`00ac9b34`](#insn-00ac9b34)
- ブロック [`00ac9b34`](#insn-00ac9b34) 範囲 `[['00ac9b34', '00ac9b3b']]`
  - `FALL_THROUGH` [`00ac9b38`](#insn-00ac9b38) → [`00ac9b3c`](#insn-00ac9b3c)
- ブロック [`00ac9b3c`](#insn-00ac9b3c) 範囲 `[['00ac9b3c', '00ac9b3f']]`
  - `FALL_THROUGH` [`00ac9b3c`](#insn-00ac9b3c) → [`00ac9b40`](#insn-00ac9b40)
- ブロック [`00ac9b40`](#insn-00ac9b40) 範囲 `[['00ac9b40', '00ac9b43']]`
  - `UNCONDITIONAL_JUMP` [`00ac9b40`](#insn-00ac9b40) → [`00ac9b68`](#insn-00ac9b68)
- ブロック [`00ac9b44`](#insn-00ac9b44) 範囲 `[['00ac9b44', '00ac9b47']]`
  - `FALL_THROUGH` [`00ac9b44`](#insn-00ac9b44) → [`00ac9b48`](#insn-00ac9b48)
- ブロック [`00ac9b48`](#insn-00ac9b48) 範囲 `[['00ac9b48', '00ac9b4b']]`
  - `UNCONDITIONAL_JUMP` [`00ac9b48`](#insn-00ac9b48) → [`00ac9b68`](#insn-00ac9b68)
- ブロック [`00ac9b4c`](#insn-00ac9b4c) 範囲 `[['00ac9b4c', '00ac9b4f']]`
  - `FALL_THROUGH` [`00ac9b4c`](#insn-00ac9b4c) → [`00ac9b50`](#insn-00ac9b50)
- ブロック [`00ac9b50`](#insn-00ac9b50) 範囲 `[['00ac9b50', '00ac9b5f']]`
  - `FALL_THROUGH` [`00ac9b5c`](#insn-00ac9b5c) → [`00ac9b60`](#insn-00ac9b60)
- ブロック [`00ac9b60`](#insn-00ac9b60) 範囲 `[['00ac9b60', '00ac9b67']]`
  - `FALL_THROUGH` [`00ac9b64`](#insn-00ac9b64) → [`00ac9b68`](#insn-00ac9b68)
- ブロック [`00ac9b68`](#insn-00ac9b68) 範囲 `[['00ac9b68', '00ac9b83']]`
  - `CONDITIONAL_JUMP` [`00ac9b80`](#insn-00ac9b80) → [`00ac9b90`](#insn-00ac9b90)
  - `FALL_THROUGH` [`00ac9b80`](#insn-00ac9b80) → [`00ac9b84`](#insn-00ac9b84)
- ブロック [`00ac9b84`](#insn-00ac9b84) 範囲 `[['00ac9b84', '00ac9b87']]`
  - `CONDITIONAL_JUMP` [`00ac9b84`](#insn-00ac9b84) → [`00ac9ba4`](#insn-00ac9ba4)
  - `FALL_THROUGH` [`00ac9b84`](#insn-00ac9b84) → [`00ac9b88`](#insn-00ac9b88)
- ブロック [`00ac9b88`](#insn-00ac9b88) 範囲 `[['00ac9b88', '00ac9b8f']]`
  - `UNCONDITIONAL_JUMP` [`00ac9b8c`](#insn-00ac9b8c) → [`00ac9b98`](#insn-00ac9b98)
- ブロック [`00ac9b90`](#insn-00ac9b90) 範囲 `[['00ac9b90', '00ac9b97']]`
  - `FALL_THROUGH` [`00ac9b94`](#insn-00ac9b94) → [`00ac9b98`](#insn-00ac9b98)
- ブロック [`00ac9b98`](#insn-00ac9b98) 範囲 `[['00ac9b98', '00ac9ba3']]`
  - `FALL_THROUGH` [`00ac9ba0`](#insn-00ac9ba0) → [`00ac9ba4`](#insn-00ac9ba4)
- ブロック [`00ac9ba4`](#insn-00ac9ba4) 範囲 `[['00ac9ba4', '00ac9c47']]`
  - `CONDITIONAL_JUMP` [`00ac9c44`](#insn-00ac9c44) → [`00ac9c60`](#insn-00ac9c60)
  - `FALL_THROUGH` [`00ac9c44`](#insn-00ac9c44) → [`00ac9c48`](#insn-00ac9c48)
- ブロック [`00ac9c48`](#insn-00ac9c48) 範囲 `[['00ac9c48', '00ac9c5f']]`
  - `FALL_THROUGH` [`00ac9c5c`](#insn-00ac9c5c) → [`00ac9c60`](#insn-00ac9c60)
- ブロック [`00ac9c60`](#insn-00ac9c60) 範囲 `[['00ac9c60', '00ac9c73']]`
  - `CONDITIONAL_JUMP` [`00ac9c70`](#insn-00ac9c70) → [`00ac9cc4`](#insn-00ac9cc4)
  - `FALL_THROUGH` [`00ac9c70`](#insn-00ac9c70) → [`00ac9c74`](#insn-00ac9c74)
- ブロック [`00ac9c74`](#insn-00ac9c74) 範囲 `[['00ac9c74', '00ac9c83']]`
  - `CONDITIONAL_JUMP` [`00ac9c80`](#insn-00ac9c80) → [`00ac9cac`](#insn-00ac9cac)
  - `FALL_THROUGH` [`00ac9c80`](#insn-00ac9c80) → [`00ac9c84`](#insn-00ac9c84)
- ブロック [`00ac9c84`](#insn-00ac9c84) 範囲 `[['00ac9c84', '00ac9c93']]`
  - `CONDITIONAL_JUMP` [`00ac9c90`](#insn-00ac9c90) → [`00ac9cac`](#insn-00ac9cac)
  - `FALL_THROUGH` [`00ac9c90`](#insn-00ac9c90) → [`00ac9c94`](#insn-00ac9c94)
- ブロック [`00ac9c94`](#insn-00ac9c94) 範囲 `[['00ac9c94', '00ac9cab']]`
  - `FALL_THROUGH` [`00ac9ca8`](#insn-00ac9ca8) → [`00ac9cac`](#insn-00ac9cac)
- ブロック [`00ac9cac`](#insn-00ac9cac) 範囲 `[['00ac9cac', '00ac9cc3']]`
  - `FALL_THROUGH` [`00ac9cc0`](#insn-00ac9cc0) → [`00ac9cc4`](#insn-00ac9cc4)
- ブロック [`00ac9cc4`](#insn-00ac9cc4) 範囲 `[['00ac9cc4', '00ac9d23']]`
  - `CONDITIONAL_JUMP` [`00ac9d20`](#insn-00ac9d20) → [`00ac9d3c`](#insn-00ac9d3c)
  - `FALL_THROUGH` [`00ac9d20`](#insn-00ac9d20) → [`00ac9d24`](#insn-00ac9d24)
- ブロック [`00ac9d24`](#insn-00ac9d24) 範囲 `[['00ac9d24', '00ac9d3b']]`
  - `FALL_THROUGH` [`00ac9d38`](#insn-00ac9d38) → [`00ac9d3c`](#insn-00ac9d3c)
- ブロック [`00ac9d3c`](#insn-00ac9d3c) 範囲 `[['00ac9d3c', '00ac9d47']]`
  - `CONDITIONAL_JUMP` [`00ac9d44`](#insn-00ac9d44) → [`00ac9d98`](#insn-00ac9d98)
  - `FALL_THROUGH` [`00ac9d44`](#insn-00ac9d44) → [`00ac9d48`](#insn-00ac9d48)
- ブロック [`00ac9d48`](#insn-00ac9d48) 範囲 `[['00ac9d48', '00ac9d57']]`
  - `CONDITIONAL_JUMP` [`00ac9d54`](#insn-00ac9d54) → [`00ac9d80`](#insn-00ac9d80)
  - `FALL_THROUGH` [`00ac9d54`](#insn-00ac9d54) → [`00ac9d58`](#insn-00ac9d58)
- ブロック [`00ac9d58`](#insn-00ac9d58) 範囲 `[['00ac9d58', '00ac9d67']]`
  - `CONDITIONAL_JUMP` [`00ac9d64`](#insn-00ac9d64) → [`00ac9d80`](#insn-00ac9d80)
  - `FALL_THROUGH` [`00ac9d64`](#insn-00ac9d64) → [`00ac9d68`](#insn-00ac9d68)
- ブロック [`00ac9d68`](#insn-00ac9d68) 範囲 `[['00ac9d68', '00ac9d7f']]`
  - `FALL_THROUGH` [`00ac9d7c`](#insn-00ac9d7c) → [`00ac9d80`](#insn-00ac9d80)
- ブロック [`00ac9d80`](#insn-00ac9d80) 範囲 `[['00ac9d80', '00ac9d97']]`
  - `FALL_THROUGH` [`00ac9d94`](#insn-00ac9d94) → [`00ac9d98`](#insn-00ac9d98)
- ブロック [`00ac9d98`](#insn-00ac9d98) 範囲 `[['00ac9d98', '00ac9dff']]`
  - `CONDITIONAL_JUMP` [`00ac9dfc`](#insn-00ac9dfc) → [`00ac9e0c`](#insn-00ac9e0c)
  - `FALL_THROUGH` [`00ac9dfc`](#insn-00ac9dfc) → [`00ac9e00`](#insn-00ac9e00)
- ブロック [`00ac9e00`](#insn-00ac9e00) 範囲 `[['00ac9e00', '00ac9e03']]`
  - `CONDITIONAL_JUMP` [`00ac9e00`](#insn-00ac9e00) → [`00ac9e20`](#insn-00ac9e20)
  - `FALL_THROUGH` [`00ac9e00`](#insn-00ac9e00) → [`00ac9e04`](#insn-00ac9e04)
- ブロック [`00ac9e04`](#insn-00ac9e04) 範囲 `[['00ac9e04', '00ac9e0b']]`
  - `UNCONDITIONAL_JUMP` [`00ac9e08`](#insn-00ac9e08) → [`00ac9e14`](#insn-00ac9e14)
- ブロック [`00ac9e0c`](#insn-00ac9e0c) 範囲 `[['00ac9e0c', '00ac9e13']]`
  - `FALL_THROUGH` [`00ac9e10`](#insn-00ac9e10) → [`00ac9e14`](#insn-00ac9e14)
- ブロック [`00ac9e14`](#insn-00ac9e14) 範囲 `[['00ac9e14', '00ac9e1f']]`
  - `FALL_THROUGH` [`00ac9e1c`](#insn-00ac9e1c) → [`00ac9e20`](#insn-00ac9e20)
- ブロック [`00ac9e20`](#insn-00ac9e20) 範囲 `[['00ac9e20', '00ac9e2b']]`
  - `CONDITIONAL_JUMP` [`00ac9e28`](#insn-00ac9e28) → [`00ac9e44`](#insn-00ac9e44)
  - `FALL_THROUGH` [`00ac9e28`](#insn-00ac9e28) → [`00ac9e2c`](#insn-00ac9e2c)
- ブロック [`00ac9e2c`](#insn-00ac9e2c) 範囲 `[['00ac9e2c', '00ac9e43']]`
  - `FALL_THROUGH` [`00ac9e40`](#insn-00ac9e40) → [`00ac9e44`](#insn-00ac9e44)
- ブロック [`00ac9e44`](#insn-00ac9e44) 範囲 `[['00ac9e44', '00ac9e4f']]`
  - `CONDITIONAL_JUMP` [`00ac9e4c`](#insn-00ac9e4c) → [`00ac9ea0`](#insn-00ac9ea0)
  - `FALL_THROUGH` [`00ac9e4c`](#insn-00ac9e4c) → [`00ac9e50`](#insn-00ac9e50)
- ブロック [`00ac9e50`](#insn-00ac9e50) 範囲 `[['00ac9e50', '00ac9e5f']]`
  - `CONDITIONAL_JUMP` [`00ac9e5c`](#insn-00ac9e5c) → [`00ac9e88`](#insn-00ac9e88)
  - `FALL_THROUGH` [`00ac9e5c`](#insn-00ac9e5c) → [`00ac9e60`](#insn-00ac9e60)
- ブロック [`00ac9e60`](#insn-00ac9e60) 範囲 `[['00ac9e60', '00ac9e6f']]`
  - `CONDITIONAL_JUMP` [`00ac9e6c`](#insn-00ac9e6c) → [`00ac9e88`](#insn-00ac9e88)
  - `FALL_THROUGH` [`00ac9e6c`](#insn-00ac9e6c) → [`00ac9e70`](#insn-00ac9e70)
- ブロック [`00ac9e70`](#insn-00ac9e70) 範囲 `[['00ac9e70', '00ac9e87']]`
  - `FALL_THROUGH` [`00ac9e84`](#insn-00ac9e84) → [`00ac9e88`](#insn-00ac9e88)
- ブロック [`00ac9e88`](#insn-00ac9e88) 範囲 `[['00ac9e88', '00ac9e9f']]`
  - `FALL_THROUGH` [`00ac9e9c`](#insn-00ac9e9c) → [`00ac9ea0`](#insn-00ac9ea0)
- ブロック [`00ac9ea0`](#insn-00ac9ea0) 範囲 `[['00ac9ea0', '00ac9eaf']]`
  - `CONDITIONAL_JUMP` [`00ac9eac`](#insn-00ac9eac) → [`00ac9f5c`](#insn-00ac9f5c)
  - `FALL_THROUGH` [`00ac9eac`](#insn-00ac9eac) → [`00ac9eb0`](#insn-00ac9eb0)
- ブロック [`00ac9eb0`](#insn-00ac9eb0) 範囲 `[['00ac9eb0', '00ac9ecb']]`
- ブロック [`00ac9f5c`](#insn-00ac9f5c) 範囲 `[['00ac9f5c', '00ac9f5f']]`

## 命令位置別の参照

- [`00ac9af0`](#insn-00ac9af0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9af4`](#insn-00ac9af4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9af8`](#insn-00ac9af8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9afc`](#insn-00ac9afc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b00`](#insn-00ac9b00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b18`](#insn-00ac9b18) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b24`](#insn-00ac9b24) → [`00ac9b44`](#insn-00ac9b44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b2c`](#insn-00ac9b2c) → [`00ac9b4c`](#insn-00ac9b4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b3c`](#insn-00ac9b3c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b40`](#insn-00ac9b40) → [`00ac9b68`](#insn-00ac9b68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b44`](#insn-00ac9b44) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b48`](#insn-00ac9b48) → [`00ac9b68`](#insn-00ac9b68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b58`](#insn-00ac9b58) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b74`](#insn-00ac9b74) → [`0057bea8`](../0057b/0057bea8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057bea8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b78`](#insn-00ac9b78) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b80`](#insn-00ac9b80) → [`00ac9b90`](#insn-00ac9b90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b84`](#insn-00ac9b84) → [`00ac9ba4`](#insn-00ac9ba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b8c`](#insn-00ac9b8c) → [`00ac9b98`](#insn-00ac9b98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9b98`](#insn-00ac9b98) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bb8`](#insn-00ac9bb8) → [`00ac871c`](../00ac8/00ac871c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac871c` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bd0`](#insn-00ac9bd0) → [`00a468fc`](../00a46/00a468fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a468fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bd4`](#insn-00ac9bd4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bf0`](#insn-00ac9bf0) → [`00a468c8`](../00a46/00a468c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a468c8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bf4`](#insn-00ac9bf4) → `Stack[-0x90]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c0c`](#insn-00ac9c0c) → [`00a468fc`](../00a46/00a468fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a468fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c10`](#insn-00ac9c10) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c14`](#insn-00ac9c14) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c20`](#insn-00ac9c20) → [`00a46784`](../00a46/00a46784.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a46784` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c38`](#insn-00ac9c38) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c3c`](#insn-00ac9c3c) → `00c9b368`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac9c40`](#insn-00ac9c40) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c44`](#insn-00ac9c44) → [`00ac9c60`](#insn-00ac9c60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c50`](#insn-00ac9c50) → `00c8b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9c54`](#insn-00ac9c54) → [`005d8bc8`](../005d8/005d8bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8bc8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c5c`](#insn-00ac9c5c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c64`](#insn-00ac9c64) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c68`](#insn-00ac9c68) → `00c9b370`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac9c6c`](#insn-00ac9c6c) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c70`](#insn-00ac9c70) → [`00ac9cc4`](#insn-00ac9cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c7c`](#insn-00ac9c7c) → `00c8b7b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9c80`](#insn-00ac9c80) → [`00ac9cac`](#insn-00ac9cac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c8c`](#insn-00ac9c8c) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c90`](#insn-00ac9c90) → [`00ac9cac`](#insn-00ac9cac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ca8`](#insn-00ac9ca8) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00ac9cb4`](#insn-00ac9cb4) → `00c8b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9cb8`](#insn-00ac9cb8) → [`005d8bc8`](../005d8/005d8bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8bc8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9cc0`](#insn-00ac9cc0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9cc4`](#insn-00ac9cc4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9cdc`](#insn-00ac9cdc) → [`00a468fc`](../00a46/00a468fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a468fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ce0`](#insn-00ac9ce0) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ce4`](#insn-00ac9ce4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9cf0`](#insn-00ac9cf0) → [`00a46784`](../00a46/00a46784.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a46784` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d0c`](#insn-00ac9d0c) → [`00a468c8`](../00a46/00a468c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a468c8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d14`](#insn-00ac9d14) → [`00a468d8`](../00a46/00a468d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a468d8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d18`](#insn-00ac9d18) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d1c`](#insn-00ac9d1c) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d20`](#insn-00ac9d20) → [`00ac9d3c`](#insn-00ac9d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d2c`](#insn-00ac9d2c) → `00c8b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9d30`](#insn-00ac9d30) → [`005d8bc8`](../005d8/005d8bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8bc8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d38`](#insn-00ac9d38) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d3c`](#insn-00ac9d3c) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d40`](#insn-00ac9d40) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d44`](#insn-00ac9d44) → [`00ac9d98`](#insn-00ac9d98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d50`](#insn-00ac9d50) → `00c8b7b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9d54`](#insn-00ac9d54) → [`00ac9d80`](#insn-00ac9d80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d60`](#insn-00ac9d60) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d64`](#insn-00ac9d64) → [`00ac9d80`](#insn-00ac9d80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d7c`](#insn-00ac9d7c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d88`](#insn-00ac9d88) → `00c8b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9d8c`](#insn-00ac9d8c) → [`005d8bc8`](../005d8/005d8bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8bc8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d94`](#insn-00ac9d94) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d98`](#insn-00ac9d98) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9d9c`](#insn-00ac9d9c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9db0`](#insn-00ac9db0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9db4`](#insn-00ac9db4) → `00c8d7c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9db4`](#insn-00ac9db4) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9dbc`](#insn-00ac9dbc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ddc`](#insn-00ac9ddc) → [`008b6fec`](../008b6/008b6fec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6fec` · 推定シンボル `None` · 推定型 `None`
- [`00ac9de4`](#insn-00ac9de4) → [`008b6f18`](../008b6/008b6f18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f18` · 推定シンボル `None` · 推定型 `None`
- [`00ac9dec`](#insn-00ac9dec) → [`008b6f30`](../008b6/008b6f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f30` · 推定シンボル `None` · 推定型 `None`
- [`00ac9df0`](#insn-00ac9df0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9dfc`](#insn-00ac9dfc) → [`00ac9e0c`](#insn-00ac9e0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e00`](#insn-00ac9e00) → [`00ac9e20`](#insn-00ac9e20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e08`](#insn-00ac9e08) → [`00ac9e14`](#insn-00ac9e14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e14`](#insn-00ac9e14) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e18`](#insn-00ac9e18) → `00c8d7e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac9e18`](#insn-00ac9e18) → `00c8d7e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9e1c`](#insn-00ac9e1c) → [`00acb3e0`](../00acb/00acb3e0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acb3e0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e1c`](#insn-00ac9e1c) → [`00acb3e4`](../00acb/00acb3e4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acb3e4` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e20`](#insn-00ac9e20) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e24`](#insn-00ac9e24) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e28`](#insn-00ac9e28) → [`00ac9e44`](#insn-00ac9e44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e34`](#insn-00ac9e34) → `00c8b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9e38`](#insn-00ac9e38) → [`005d8bc8`](../005d8/005d8bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8bc8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e40`](#insn-00ac9e40) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e44`](#insn-00ac9e44) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e48`](#insn-00ac9e48) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e4c`](#insn-00ac9e4c) → [`00ac9ea0`](#insn-00ac9ea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e58`](#insn-00ac9e58) → `00c8b7b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9e5c`](#insn-00ac9e5c) → [`00ac9e88`](#insn-00ac9e88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e68`](#insn-00ac9e68) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e6c`](#insn-00ac9e6c) → [`00ac9e88`](#insn-00ac9e88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e84`](#insn-00ac9e84) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e90`](#insn-00ac9e90) → `00c8b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ac9e94`](#insn-00ac9e94) → [`005d8bc8`](../005d8/005d8bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8bc8` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e9c`](#insn-00ac9e9c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ea4`](#insn-00ac9ea4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9eac`](#insn-00ac9eac) → [`00ac9f5c`](#insn-00ac9f5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9eb0`](#insn-00ac9eb0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9eb4`](#insn-00ac9eb4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9eb8`](#insn-00ac9eb8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ebc`](#insn-00ac9ebc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ec0`](#insn-00ac9ec0) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f5c`](#insn-00ac9f5c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac9af0`](#insn-00ac9af0)

~~~json
{
  "source": "00ac9af0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9af4`](#insn-00ac9af4)

~~~json
{
  "source": "00ac9af4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9af8`](#insn-00ac9af8)

~~~json
{
  "source": "00ac9af8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9afc`](#insn-00ac9afc)

~~~json
{
  "source": "00ac9afc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b00`](#insn-00ac9b00)

~~~json
{
  "source": "00ac9b00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b18`](#insn-00ac9b18)

~~~json
{
  "source": "00ac9b18",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b24`](#insn-00ac9b24)

~~~json
{
  "source": "00ac9b24",
  "target": "00ac9b44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b2c`](#insn-00ac9b2c)

~~~json
{
  "source": "00ac9b2c",
  "target": "00ac9b4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b3c`](#insn-00ac9b3c)

~~~json
{
  "source": "00ac9b3c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b40`](#insn-00ac9b40)

~~~json
{
  "source": "00ac9b40",
  "target": "00ac9b68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b44`](#insn-00ac9b44)

~~~json
{
  "source": "00ac9b44",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b48`](#insn-00ac9b48)

~~~json
{
  "source": "00ac9b48",
  "target": "00ac9b68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b58`](#insn-00ac9b58)

~~~json
{
  "source": "00ac9b58",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b74`](#insn-00ac9b74)

~~~json
{
  "source": "00ac9b74",
  "target": "0057bea8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9b78`](#insn-00ac9b78)

~~~json
{
  "source": "00ac9b78",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b80`](#insn-00ac9b80)

~~~json
{
  "source": "00ac9b80",
  "target": "00ac9b90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b84`](#insn-00ac9b84)

~~~json
{
  "source": "00ac9b84",
  "target": "00ac9ba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b8c`](#insn-00ac9b8c)

~~~json
{
  "source": "00ac9b8c",
  "target": "00ac9b98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9b98`](#insn-00ac9b98)

~~~json
{
  "source": "00ac9b98",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bb8`](#insn-00ac9bb8)

~~~json
{
  "source": "00ac9bb8",
  "target": "00ac871c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9bd0`](#insn-00ac9bd0)

~~~json
{
  "source": "00ac9bd0",
  "target": "00a468fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9bd4`](#insn-00ac9bd4)

~~~json
{
  "source": "00ac9bd4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bf0`](#insn-00ac9bf0)

~~~json
{
  "source": "00ac9bf0",
  "target": "00a468c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9bf4`](#insn-00ac9bf4)

~~~json
{
  "source": "00ac9bf4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c0c`](#insn-00ac9c0c)

~~~json
{
  "source": "00ac9c0c",
  "target": "00a468fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9c10`](#insn-00ac9c10)

~~~json
{
  "source": "00ac9c10",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c14`](#insn-00ac9c14)

~~~json
{
  "source": "00ac9c14",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c20`](#insn-00ac9c20)

~~~json
{
  "source": "00ac9c20",
  "target": "00a46784",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9c38`](#insn-00ac9c38)

~~~json
{
  "source": "00ac9c38",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c3c`](#insn-00ac9c3c)

~~~json
{
  "source": "00ac9c3c",
  "target": "00c9b368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b368",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9c40`](#insn-00ac9c40)

~~~json
{
  "source": "00ac9c40",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c44`](#insn-00ac9c44)

~~~json
{
  "source": "00ac9c44",
  "target": "00ac9c60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c50`](#insn-00ac9c50)

~~~json
{
  "source": "00ac9c50",
  "target": "00c8b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9c54`](#insn-00ac9c54)

~~~json
{
  "source": "00ac9c54",
  "target": "005d8bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9c5c`](#insn-00ac9c5c)

~~~json
{
  "source": "00ac9c5c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9c64`](#insn-00ac9c64)

~~~json
{
  "source": "00ac9c64",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c68`](#insn-00ac9c68)

~~~json
{
  "source": "00ac9c68",
  "target": "00c9b370",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b370",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9c6c`](#insn-00ac9c6c)

~~~json
{
  "source": "00ac9c6c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c70`](#insn-00ac9c70)

~~~json
{
  "source": "00ac9c70",
  "target": "00ac9cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c7c`](#insn-00ac9c7c)

~~~json
{
  "source": "00ac9c7c",
  "target": "00c8b7b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b7b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9c80`](#insn-00ac9c80)

~~~json
{
  "source": "00ac9c80",
  "target": "00ac9cac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c8c`](#insn-00ac9c8c)

~~~json
{
  "source": "00ac9c8c",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9c90`](#insn-00ac9c90)

~~~json
{
  "source": "00ac9c90",
  "target": "00ac9cac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ca8`](#insn-00ac9ca8)

~~~json
{
  "source": "00ac9ca8",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9cb4`](#insn-00ac9cb4)

~~~json
{
  "source": "00ac9cb4",
  "target": "00c8b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9cb8`](#insn-00ac9cb8)

~~~json
{
  "source": "00ac9cb8",
  "target": "005d8bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9cc0`](#insn-00ac9cc0)

~~~json
{
  "source": "00ac9cc0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9cc4`](#insn-00ac9cc4)

~~~json
{
  "source": "00ac9cc4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9cdc`](#insn-00ac9cdc)

~~~json
{
  "source": "00ac9cdc",
  "target": "00a468fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9ce0`](#insn-00ac9ce0)

~~~json
{
  "source": "00ac9ce0",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ce4`](#insn-00ac9ce4)

~~~json
{
  "source": "00ac9ce4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9cf0`](#insn-00ac9cf0)

~~~json
{
  "source": "00ac9cf0",
  "target": "00a46784",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9d0c`](#insn-00ac9d0c)

~~~json
{
  "source": "00ac9d0c",
  "target": "00a468c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9d14`](#insn-00ac9d14)

~~~json
{
  "source": "00ac9d14",
  "target": "00a468d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9d18`](#insn-00ac9d18)

~~~json
{
  "source": "00ac9d18",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9d1c`](#insn-00ac9d1c)

~~~json
{
  "source": "00ac9d1c",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9d20`](#insn-00ac9d20)

~~~json
{
  "source": "00ac9d20",
  "target": "00ac9d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9d2c`](#insn-00ac9d2c)

~~~json
{
  "source": "00ac9d2c",
  "target": "00c8b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9d30`](#insn-00ac9d30)

~~~json
{
  "source": "00ac9d30",
  "target": "005d8bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9d38`](#insn-00ac9d38)

~~~json
{
  "source": "00ac9d38",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9d3c`](#insn-00ac9d3c)

~~~json
{
  "source": "00ac9d3c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9d40`](#insn-00ac9d40)

~~~json
{
  "source": "00ac9d40",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9d44`](#insn-00ac9d44)

~~~json
{
  "source": "00ac9d44",
  "target": "00ac9d98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9d50`](#insn-00ac9d50)

~~~json
{
  "source": "00ac9d50",
  "target": "00c8b7b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b7b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9d54`](#insn-00ac9d54)

~~~json
{
  "source": "00ac9d54",
  "target": "00ac9d80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9d60`](#insn-00ac9d60)

~~~json
{
  "source": "00ac9d60",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9d64`](#insn-00ac9d64)

~~~json
{
  "source": "00ac9d64",
  "target": "00ac9d80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9d7c`](#insn-00ac9d7c)

~~~json
{
  "source": "00ac9d7c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9d88`](#insn-00ac9d88)

~~~json
{
  "source": "00ac9d88",
  "target": "00c8b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9d8c`](#insn-00ac9d8c)

~~~json
{
  "source": "00ac9d8c",
  "target": "005d8bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9d94`](#insn-00ac9d94)

~~~json
{
  "source": "00ac9d94",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9d98`](#insn-00ac9d98)

~~~json
{
  "source": "00ac9d98",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9d9c`](#insn-00ac9d9c)

~~~json
{
  "source": "00ac9d9c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9db0`](#insn-00ac9db0)

~~~json
{
  "source": "00ac9db0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9db4`](#insn-00ac9db4)

~~~json
{
  "source": "00ac9db4",
  "target": "00c8d7c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d7c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9db4`](#insn-00ac9db4)

~~~json
{
  "source": "00ac9db4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9dbc`](#insn-00ac9dbc)

~~~json
{
  "source": "00ac9dbc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ddc`](#insn-00ac9ddc)

~~~json
{
  "source": "00ac9ddc",
  "target": "008b6fec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9de4`](#insn-00ac9de4)

~~~json
{
  "source": "00ac9de4",
  "target": "008b6f18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9dec`](#insn-00ac9dec)

~~~json
{
  "source": "00ac9dec",
  "target": "008b6f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9df0`](#insn-00ac9df0)

~~~json
{
  "source": "00ac9df0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9dfc`](#insn-00ac9dfc)

~~~json
{
  "source": "00ac9dfc",
  "target": "00ac9e0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e00`](#insn-00ac9e00)

~~~json
{
  "source": "00ac9e00",
  "target": "00ac9e20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e08`](#insn-00ac9e08)

~~~json
{
  "source": "00ac9e08",
  "target": "00ac9e14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e14`](#insn-00ac9e14)

~~~json
{
  "source": "00ac9e14",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e18`](#insn-00ac9e18)

~~~json
{
  "source": "00ac9e18",
  "target": "00c8d7e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d7e0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9e18`](#insn-00ac9e18)

~~~json
{
  "source": "00ac9e18",
  "target": "00c8d7e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d7e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9e1c`](#insn-00ac9e1c)

~~~json
{
  "source": "00ac9e1c",
  "target": "00acb3e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9e1c`](#insn-00ac9e1c)

~~~json
{
  "source": "00ac9e1c",
  "target": "00acb3e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9e20`](#insn-00ac9e20)

~~~json
{
  "source": "00ac9e20",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e24`](#insn-00ac9e24)

~~~json
{
  "source": "00ac9e24",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e28`](#insn-00ac9e28)

~~~json
{
  "source": "00ac9e28",
  "target": "00ac9e44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e34`](#insn-00ac9e34)

~~~json
{
  "source": "00ac9e34",
  "target": "00c8b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9e38`](#insn-00ac9e38)

~~~json
{
  "source": "00ac9e38",
  "target": "005d8bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9e40`](#insn-00ac9e40)

~~~json
{
  "source": "00ac9e40",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9e44`](#insn-00ac9e44)

~~~json
{
  "source": "00ac9e44",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e48`](#insn-00ac9e48)

~~~json
{
  "source": "00ac9e48",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e4c`](#insn-00ac9e4c)

~~~json
{
  "source": "00ac9e4c",
  "target": "00ac9ea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e58`](#insn-00ac9e58)

~~~json
{
  "source": "00ac9e58",
  "target": "00c8b7b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b7b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9e5c`](#insn-00ac9e5c)

~~~json
{
  "source": "00ac9e5c",
  "target": "00ac9e88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e68`](#insn-00ac9e68)

~~~json
{
  "source": "00ac9e68",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9e6c`](#insn-00ac9e6c)

~~~json
{
  "source": "00ac9e6c",
  "target": "00ac9e88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e84`](#insn-00ac9e84)

~~~json
{
  "source": "00ac9e84",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9e90`](#insn-00ac9e90)

~~~json
{
  "source": "00ac9e90",
  "target": "00c8b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac9e94`](#insn-00ac9e94)

~~~json
{
  "source": "00ac9e94",
  "target": "005d8bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9e9c`](#insn-00ac9e9c)

~~~json
{
  "source": "00ac9e9c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9ea4`](#insn-00ac9ea4)

~~~json
{
  "source": "00ac9ea4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9eac`](#insn-00ac9eac)

~~~json
{
  "source": "00ac9eac",
  "target": "00ac9f5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9eb0`](#insn-00ac9eb0)

~~~json
{
  "source": "00ac9eb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9eb4`](#insn-00ac9eb4)

~~~json
{
  "source": "00ac9eb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9eb8`](#insn-00ac9eb8)

~~~json
{
  "source": "00ac9eb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ebc`](#insn-00ac9ebc)

~~~json
{
  "source": "00ac9ebc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ec0`](#insn-00ac9ec0)

~~~json
{
  "source": "00ac9ec0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f5c`](#insn-00ac9f5c)

~~~json
{
  "source": "00ac9f5c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
