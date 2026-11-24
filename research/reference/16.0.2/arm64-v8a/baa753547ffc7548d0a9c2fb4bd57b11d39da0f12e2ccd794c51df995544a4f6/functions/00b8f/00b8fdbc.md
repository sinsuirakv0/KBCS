# 00b8fdbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b8fd20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8f/00b8fd20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0077.md#compare-ceb19efde9c5be6c0f5fe901e34f17f3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b90db0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b90/00b90db0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0008.md#compare-e5e49fc78b92e0e3290dbe1bddeb648c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b8fdbc",
  "name": "_ZN11flatbuffers21FlatBufferBuilderImplILb0EE26CreateVectorOfSortedTablesIN10reflection4EnumENSt6__ndk19allocatorINS_6OffsetIS4_EEEEEENS7_INS_6VectorINS7_IT_EEjEEEEPNS5_6vectorISC_T0_EE",
  "size": 472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4eea3dea745383cd53e694abdadd5af9d805ae12c5a004eb3cb6a27293965554",
  "source_text_sha256": "4eea3dea745383cd53e694abdadd5af9d805ae12c5a004eb3cb6a27293965554",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b8fdbc",
        "00b8ff93"
      ]
    ],
    "bytes_sha256": "a74bfcfe7e92e2691b4b267e78d399641dbefeec5913347b1142a3fb11c05345",
    "instruction_count": 118,
    "instruction_bytes": 472,
    "body_bytes": 472,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5c3b0](../00c5c/00c5c3b0.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5a920](../00c5a/00c5a920.md)
- [00c5c270](../00c5c/00c5c270.md)
- [00c5c320](../00c5c/00c5c320.md)
- [00c5c350](../00c5c/00c5c350.md)
- [00c5cbd0](../00c5c/00c5cbd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3870 bytes

~~~c

undefined4
_ZN11flatbuffers21FlatBufferBuilderImplILb0EE26CreateVectorOfSortedTablesIN10reflection4EnumENSt6__ndk19allocatorINS_6OffsetIS4_EEEEEENS7_INS_6VectorINS7_IT_EEjEEEEPNS5_6vectorISC_T0_EE
          (long param_1,long *param_2)

{
  uint uVar1;
  undefined *puVar2;
  undefined *puVar3;
  int iVar4;
  long lVar5;
  undefined *puVar6;
  undefined4 uVar7;
  void *__ptr;
  int iVar8;
  ulong uVar9;
  long lVar10;
  ulong uVar11;
  ulong uVar12;
  ulong uVar13;
  long local_70;
  long local_68;
  
  puVar6 = PTR__ZSt7nothrow_00c9b5f0;
  lVar5 = tpidr_el0;
  local_68 = *(long *)(lVar5 + 0x28);
  puVar3 = (undefined *)*param_2;
  uVar13 = param_2[1] - (long)puVar3;
  puVar2 = 
  PTR__ZZN11flatbuffers4dataINS_6OffsetIN10reflection4EnumEEENSt6__ndk19allocatorIS4_EEEEPT_RNS5_6vectorIS8_T0_EEE1t_00c9b928
  ;
  if (puVar3 != (undefined *)param_2[1]) {
    puVar2 = puVar3;
  }
  uVar11 = (long)uVar13 >> 2;
  local_70 = param_1;
  if (0x200 < (long)uVar13) {
    uVar12 = uVar11;
    if (0x1ffffffffffffffe < (long)uVar11) {
      uVar12 = 0x1fffffffffffffff;
    }
    do {
      __ptr = (void *)_ZnwmRKSt9nothrow_t(uVar12 << 2,puVar6);
      if (__ptr != (void *)0x0) {
                    /* try { // try from 00b8fe64 to 00c8fe6f has its CatchHandler @ 00b914f0 */
        _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl
                  (puVar2,puVar2 + uVar13,&local_70,uVar11,__ptr,uVar12);
                    /* try { // try from 00b8fe88 to 00c8fea3 has its CatchHandler @ 00b914d0 */
        _ZdlPv(__ptr);
        goto LAB_00b8fe8c;
      }
      uVar12 = uVar12 >> 1;
    } while (uVar12 != 0);
  }
  _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl
            (puVar2,puVar2 + uVar13,&local_70,uVar11,0,0);
LAB_00b8fe8c:
  _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm(param_1,uVar11,4,4);
  uVar12 = uVar13;
  while (uVar12 != 0) {
    uVar11 = uVar11 - 1;
    iVar4 = *(int *)(puVar2 + uVar11 * 4);
    if (*(ulong *)(param_1 + 0x68) < 4) {
      *(undefined8 *)(param_1 + 0x68) = 4;
    }
    iVar8 = *(int *)(param_1 + 0x30);
                    /* try { // try from 00b8fee0 to 00c8feeb has its CatchHandler @ 00b914c8 */
    uVar1 = -iVar8 & 3;
    uVar12 = (ulong)uVar1;
    if (uVar1 != 0) {
      lVar10 = *(long *)(param_1 + 0x40);
      if ((uint)((int)lVar10 - *(int *)(param_1 + 0x48)) < uVar12) {
                    /* try { // try from 00b8ff04 to 00c8ff27 has its CatchHandler @ 00b914f8 */
        _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar12);
        lVar10 = *(long *)(param_1 + 0x40);
        iVar8 = *(int *)(param_1 + 0x30);
      }
      *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar10 - uVar12);
      *(uint *)(param_1 + 0x30) = iVar8 + uVar1;
                    /* try { // try from 00b8ff28 to 00c9000b has its CatchHandler @ 00b8e624 */
      *(undefined1 *)(lVar10 - uVar12) = 0;
      if (uVar1 != 1) {
        uVar9 = 1;
        do {
          *(undefined1 *)(*(long *)(param_1 + 0x40) + uVar9) = 0;
          uVar9 = uVar9 + 1;
        } while (uVar12 != uVar9);
      }
    }
    _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIjjEET0_T_
              (param_1,(*(int *)(param_1 + 0x30) - iVar4) + 4);
    uVar12 = uVar11;
  }
  *(undefined1 *)(param_1 + 0x60) = 0;
  uVar7 = _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIjjEET0_T_(param_1,uVar13 >> 2);
  if (*(long *)(lVar5 + 0x28) == local_68) {
    return uVar7;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b8fdbc"></a> `00b8fdbc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b8fdc0"></a> `00b8fdc0` | `fb 0b 00 f9` | str x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b8fdc4"></a> `00b8fdc4` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b8fdc8"></a> `00b8fdc8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b8fdcc"></a> `00b8fdcc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b8fdd0"></a> `00b8fdd0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b8fdd4"></a> `00b8fdd4` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b8fdd8"></a> `00b8fdd8` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b8fddc"></a> `00b8fddc` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b8fde0"></a> `00b8fde0` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00b8fde4"></a> `00b8fde4` | `6a 08 00 90` | adrp x10,0xc9b000 | `FALL_THROUGH`
<a id="insn-00b8fde8"></a> `00b8fde8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b8fdec"></a> `00b8fdec` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b8fdf0"></a> `00b8fdf0` | `28 24 40 a9` | ldp x8,x9,[x1] | `FALL_THROUGH`
<a id="insn-00b8fdf4"></a> `00b8fdf4` | `4a 95 44 f9` | ldr x10,[x10, #0x928] | `FALL_THROUGH`
<a id="insn-00b8fdf8"></a> `00b8fdf8` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00b8fdfc"></a> `00b8fdfc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b8fe00"></a> `00b8fe00` | `3b 01 08 cb` | sub x27,x9,x8 | `FALL_THROUGH`
<a id="insn-00b8fe04"></a> `00b8fe04` | `54 01 88 9a` | csel x20,x10,x8,eq | `FALL_THROUGH`
<a id="insn-00b8fe08"></a> `00b8fe08` | `75 ff 42 93` | asr x21,x27,#0x2 | `FALL_THROUGH`
<a id="insn-00b8fe0c"></a> `00b8fe0c` | `7f 07 08 f1` | cmp x27,#0x201 | `FALL_THROUGH`
<a id="insn-00b8fe10"></a> `00b8fe10` | `96 02 1b 8b` | add x22,x20,x27 | `FALL_THROUGH`
<a id="insn-00b8fe14"></a> `00b8fe14` | `8b 01 00 54` | b.lt 0x00b8fe44 | `CONDITIONAL_JUMP`
<a id="insn-00b8fe18"></a> `00b8fe18` | `78 08 00 90` | adrp x24,0xc9b000 | `FALL_THROUGH`
<a id="insn-00b8fe1c"></a> `00b8fe1c` | `18 fb 42 f9` | ldr x24,[x24, #0x5f0] | `FALL_THROUGH`
<a id="insn-00b8fe20"></a> `00b8fe20` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00b8fe24"></a> `00b8fe24` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00b8fe28"></a> `00b8fe28` | `b7 b2 88 9a` | csel x23,x21,x8,lt | `FALL_THROUGH`
<a id="insn-00b8fe2c"></a> `00b8fe2c` | `e0 f6 7e d3` | lsl x0,x23,#0x2 | `FALL_THROUGH`
<a id="insn-00b8fe30"></a> `00b8fe30` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00b8fe34"></a> `00b8fe34` | `bb 2a 03 94` | bl 0x00c5a920 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fe38"></a> `00b8fe38` | `60 01 00 b5` | cbnz x0,0x00b8fe64 | `CONDITIONAL_JUMP`
<a id="insn-00b8fe3c"></a> `00b8fe3c` | `f7 fe 41 d3` | lsr x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fe40"></a> `00b8fe40` | `77 ff ff b5` | cbnz x23,0x00b8fe2c | `CONDITIONAL_JUMP`
<a id="insn-00b8fe44"></a> `00b8fe44` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00b8fe48"></a> `00b8fe48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b8fe4c"></a> `00b8fe4c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b8fe50"></a> `00b8fe50` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00b8fe54"></a> `00b8fe54` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00b8fe58"></a> `00b8fe58` | `e5 03 1f aa` | mov x5,xzr | `FALL_THROUGH`
<a id="insn-00b8fe5c"></a> `00b8fe5c` | `5d 33 03 94` | bl 0x00c5cbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fe60"></a> `00b8fe60` | `0b 00 00 14` | b 0x00b8fe8c | `UNCONDITIONAL_JUMP`
<a id="insn-00b8fe64"></a> `00b8fe64` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00b8fe68"></a> `00b8fe68` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00b8fe6c"></a> `00b8fe6c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b8fe70"></a> `00b8fe70` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b8fe74"></a> `00b8fe74` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00b8fe78"></a> `00b8fe78` | `e4 03 19 aa` | mov x4,x25 | `FALL_THROUGH`
<a id="insn-00b8fe7c"></a> `00b8fe7c` | `e5 03 17 aa` | mov x5,x23 | `FALL_THROUGH`
<a id="insn-00b8fe80"></a> `00b8fe80` | `54 33 03 94` | bl 0x00c5cbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fe84"></a> `00b8fe84` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00b8fe88"></a> `00b8fe88` | `3e 20 03 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fe8c"></a> `00b8fe8c` | `82 00 80 52` | mov w2,#0x4 | `FALL_THROUGH`
<a id="insn-00b8fe90"></a> `00b8fe90` | `83 00 80 52` | mov w3,#0x4 | `FALL_THROUGH`
<a id="insn-00b8fe94"></a> `00b8fe94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b8fe98"></a> `00b8fe98` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b8fe9c"></a> `00b8fe9c` | `2d 31 03 94` | bl 0x00c5c350 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fea0"></a> `00b8fea0` | `7b 05 00 b4` | cbz x27,0x00b8ff4c | `CONDITIONAL_JUMP`
<a id="insn-00b8fea4"></a> `00b8fea4` | `97 00 80 52` | mov w23,#0x4 | `FALL_THROUGH`
<a id="insn-00b8fea8"></a> `00b8fea8` | `07 00 00 14` | b 0x00b8fec4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8feac"></a> `00b8feac` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b8feb0"></a> `00b8feb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b8feb4"></a> `00b8feb4` | `08 01 18 4b` | sub w8,w8,w24 | `FALL_THROUGH`
<a id="insn-00b8feb8"></a> `00b8feb8` | `01 11 00 11` | add w1,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00b8febc"></a> `00b8febc` | `19 31 03 94` | bl 0x00c5c320 | `UNCONDITIONAL_CALL`
<a id="insn-00b8fec0"></a> `00b8fec0` | `75 04 00 b4` | cbz x21,0x00b8ff4c | `CONDITIONAL_JUMP`
<a id="insn-00b8fec4"></a> `00b8fec4` | `68 36 40 f9` | ldr x8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00b8fec8"></a> `00b8fec8` | `b5 06 00 d1` | sub x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00b8fecc"></a> `00b8fecc` | `98 7a 75 b8` | ldr w24,[x20, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00b8fed0"></a> `00b8fed0` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00b8fed4"></a> `00b8fed4` | `48 00 00 54` | b.hi 0x00b8fedc | `CONDITIONAL_JUMP`
<a id="insn-00b8fed8"></a> `00b8fed8` | `77 36 00 f9` | str x23,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00b8fedc"></a> `00b8fedc` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b8fee0"></a> `00b8fee0` | `e9 03 08 4b` | neg w9,w8 | `FALL_THROUGH`
<a id="insn-00b8fee4"></a> `00b8fee4` | `36 05 00 72` | ands w22,w9,#0x3 | `FALL_THROUGH`
<a id="insn-00b8fee8"></a> `00b8fee8` | `20 fe ff 54` | b.eq 0x00b8feac | `CONDITIONAL_JUMP`
<a id="insn-00b8feec"></a> `00b8feec` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b8fef0"></a> `00b8fef0` | `6a 4a 40 b9` | ldr w10,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b8fef4"></a> `00b8fef4` | `2a 01 0a 4b` | sub w10,w9,w10 | `FALL_THROUGH`
<a id="insn-00b8fef8"></a> `00b8fef8` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00b8fefc"></a> `00b8fefc` | `c2 00 00 54` | b.cs 0x00b8ff14 | `CONDITIONAL_JUMP`
<a id="insn-00b8ff00"></a> `00b8ff00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b8ff04"></a> `00b8ff04` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b8ff08"></a> `00b8ff08` | `da 30 03 94` | bl 0x00c5c270 | `UNCONDITIONAL_CALL`
<a id="insn-00b8ff0c"></a> `00b8ff0c` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b8ff10"></a> `00b8ff10` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b8ff14"></a> `00b8ff14` | `29 01 16 cb` | sub x9,x9,x22 | `FALL_THROUGH`
<a id="insn-00b8ff18"></a> `00b8ff18` | `08 01 16 0b` | add w8,w8,w22 | `FALL_THROUGH`
<a id="insn-00b8ff1c"></a> `00b8ff1c` | `df 06 00 71` | cmp w22,#0x1 | `FALL_THROUGH`
<a id="insn-00b8ff20"></a> `00b8ff20` | `69 22 00 f9` | str x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b8ff24"></a> `00b8ff24` | `68 32 00 b9` | str w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b8ff28"></a> `00b8ff28` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00b8ff2c"></a> `00b8ff2c` | `00 fc ff 54` | b.eq 0x00b8feac | `CONDITIONAL_JUMP`
<a id="insn-00b8ff30"></a> `00b8ff30` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8ff34"></a> `00b8ff34` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b8ff38"></a> `00b8ff38` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00b8ff3c"></a> `00b8ff3c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8ff40"></a> `00b8ff40` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00b8ff44"></a> `00b8ff44` | `81 ff ff 54` | b.ne 0x00b8ff34 | `CONDITIONAL_JUMP`
<a id="insn-00b8ff48"></a> `00b8ff48` | `d9 ff ff 17` | b 0x00b8feac | `UNCONDITIONAL_JUMP`
<a id="insn-00b8ff4c"></a> `00b8ff4c` | `61 ff 42 d3` | lsr x1,x27,#0x2 | `FALL_THROUGH`
<a id="insn-00b8ff50"></a> `00b8ff50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b8ff54"></a> `00b8ff54` | `7f 82 01 39` | strb wzr,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00b8ff58"></a> `00b8ff58` | `f2 30 03 94` | bl 0x00c5c320 | `UNCONDITIONAL_CALL`
<a id="insn-00b8ff5c"></a> `00b8ff5c` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00b8ff60"></a> `00b8ff60` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b8ff64"></a> `00b8ff64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b8ff68"></a> `00b8ff68` | `41 01 00 54` | b.ne 0x00b8ff90 | `CONDITIONAL_JUMP`
<a id="insn-00b8ff6c"></a> `00b8ff6c` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b8ff70"></a> `00b8ff70` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b8ff74"></a> `00b8ff74` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b8ff78"></a> `00b8ff78` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b8ff7c"></a> `00b8ff7c` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b8ff80"></a> `00b8ff80` | `fb 0b 40 f9` | ldr x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b8ff84"></a> `00b8ff84` | `e0 03 00 2a` | mov w0,w0 | `FALL_THROUGH`
<a id="insn-00b8ff88"></a> `00b8ff88` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b8ff8c"></a> `00b8ff8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b8ff90"></a> `00b8ff90` | `08 20 03 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b8fdbc`](#insn-00b8fdbc) 範囲 `[['00b8fdbc', '00b8fe17']]`
  - `CONDITIONAL_JUMP` [`00b8fe14`](#insn-00b8fe14) → [`00b8fe44`](#insn-00b8fe44)
  - `FALL_THROUGH` [`00b8fe14`](#insn-00b8fe14) → [`00b8fe18`](#insn-00b8fe18)
- ブロック [`00b8fe18`](#insn-00b8fe18) 範囲 `[['00b8fe18', '00b8fe2b']]`
  - `FALL_THROUGH` [`00b8fe28`](#insn-00b8fe28) → [`00b8fe2c`](#insn-00b8fe2c)
- ブロック [`00b8fe2c`](#insn-00b8fe2c) 範囲 `[['00b8fe2c', '00b8fe3b']]`
  - `CONDITIONAL_JUMP` [`00b8fe38`](#insn-00b8fe38) → [`00b8fe64`](#insn-00b8fe64)
  - `FALL_THROUGH` [`00b8fe38`](#insn-00b8fe38) → [`00b8fe3c`](#insn-00b8fe3c)
- ブロック [`00b8fe3c`](#insn-00b8fe3c) 範囲 `[['00b8fe3c', '00b8fe43']]`
  - `CONDITIONAL_JUMP` [`00b8fe40`](#insn-00b8fe40) → [`00b8fe2c`](#insn-00b8fe2c)
  - `FALL_THROUGH` [`00b8fe40`](#insn-00b8fe40) → [`00b8fe44`](#insn-00b8fe44)
- ブロック [`00b8fe44`](#insn-00b8fe44) 範囲 `[['00b8fe44', '00b8fe63']]`
  - `UNCONDITIONAL_JUMP` [`00b8fe60`](#insn-00b8fe60) → [`00b8fe8c`](#insn-00b8fe8c)
- ブロック [`00b8fe64`](#insn-00b8fe64) 範囲 `[['00b8fe64', '00b8fe87']]`
  - `FALL_THROUGH` [`00b8fe84`](#insn-00b8fe84) → [`00b8fe88`](#insn-00b8fe88)
- ブロック [`00b8fe88`](#insn-00b8fe88) 範囲 `[['00b8fe88', '00b8fe8b']]`
  - `FALL_THROUGH` [`00b8fe88`](#insn-00b8fe88) → [`00b8fe8c`](#insn-00b8fe8c)
- ブロック [`00b8fe8c`](#insn-00b8fe8c) 範囲 `[['00b8fe8c', '00b8fea3']]`
  - `CONDITIONAL_JUMP` [`00b8fea0`](#insn-00b8fea0) → [`00b8ff4c`](#insn-00b8ff4c)
  - `FALL_THROUGH` [`00b8fea0`](#insn-00b8fea0) → [`00b8fea4`](#insn-00b8fea4)
- ブロック [`00b8fea4`](#insn-00b8fea4) 範囲 `[['00b8fea4', '00b8feab']]`
  - `UNCONDITIONAL_JUMP` [`00b8fea8`](#insn-00b8fea8) → [`00b8fec4`](#insn-00b8fec4)
- ブロック [`00b8feac`](#insn-00b8feac) 範囲 `[['00b8feac', '00b8fec3']]`
  - `CONDITIONAL_JUMP` [`00b8fec0`](#insn-00b8fec0) → [`00b8ff4c`](#insn-00b8ff4c)
  - `FALL_THROUGH` [`00b8fec0`](#insn-00b8fec0) → [`00b8fec4`](#insn-00b8fec4)
- ブロック [`00b8fec4`](#insn-00b8fec4) 範囲 `[['00b8fec4', '00b8fed7']]`
  - `CONDITIONAL_JUMP` [`00b8fed4`](#insn-00b8fed4) → [`00b8fedc`](#insn-00b8fedc)
  - `FALL_THROUGH` [`00b8fed4`](#insn-00b8fed4) → [`00b8fed8`](#insn-00b8fed8)
- ブロック [`00b8fed8`](#insn-00b8fed8) 範囲 `[['00b8fed8', '00b8fedb']]`
  - `FALL_THROUGH` [`00b8fed8`](#insn-00b8fed8) → [`00b8fedc`](#insn-00b8fedc)
- ブロック [`00b8fedc`](#insn-00b8fedc) 範囲 `[['00b8fedc', '00b8fedf']]`
  - `FALL_THROUGH` [`00b8fedc`](#insn-00b8fedc) → [`00b8fee0`](#insn-00b8fee0)
- ブロック [`00b8fee0`](#insn-00b8fee0) 範囲 `[['00b8fee0', '00b8feeb']]`
  - `CONDITIONAL_JUMP` [`00b8fee8`](#insn-00b8fee8) → [`00b8feac`](#insn-00b8feac)
  - `FALL_THROUGH` [`00b8fee8`](#insn-00b8fee8) → [`00b8feec`](#insn-00b8feec)
- ブロック [`00b8feec`](#insn-00b8feec) 範囲 `[['00b8feec', '00b8feff']]`
  - `CONDITIONAL_JUMP` [`00b8fefc`](#insn-00b8fefc) → [`00b8ff14`](#insn-00b8ff14)
  - `FALL_THROUGH` [`00b8fefc`](#insn-00b8fefc) → [`00b8ff00`](#insn-00b8ff00)
- ブロック [`00b8ff00`](#insn-00b8ff00) 範囲 `[['00b8ff00', '00b8ff03']]`
  - `FALL_THROUGH` [`00b8ff00`](#insn-00b8ff00) → [`00b8ff04`](#insn-00b8ff04)
- ブロック [`00b8ff04`](#insn-00b8ff04) 範囲 `[['00b8ff04', '00b8ff13']]`
  - `FALL_THROUGH` [`00b8ff10`](#insn-00b8ff10) → [`00b8ff14`](#insn-00b8ff14)
- ブロック [`00b8ff14`](#insn-00b8ff14) 範囲 `[['00b8ff14', '00b8ff27']]`
  - `FALL_THROUGH` [`00b8ff24`](#insn-00b8ff24) → [`00b8ff28`](#insn-00b8ff28)
- ブロック [`00b8ff28`](#insn-00b8ff28) 範囲 `[['00b8ff28', '00b8ff2f']]`
  - `CONDITIONAL_JUMP` [`00b8ff2c`](#insn-00b8ff2c) → [`00b8feac`](#insn-00b8feac)
  - `FALL_THROUGH` [`00b8ff2c`](#insn-00b8ff2c) → [`00b8ff30`](#insn-00b8ff30)
- ブロック [`00b8ff30`](#insn-00b8ff30) 範囲 `[['00b8ff30', '00b8ff33']]`
  - `FALL_THROUGH` [`00b8ff30`](#insn-00b8ff30) → [`00b8ff34`](#insn-00b8ff34)
- ブロック [`00b8ff34`](#insn-00b8ff34) 範囲 `[['00b8ff34', '00b8ff47']]`
  - `CONDITIONAL_JUMP` [`00b8ff44`](#insn-00b8ff44) → [`00b8ff34`](#insn-00b8ff34)
  - `FALL_THROUGH` [`00b8ff44`](#insn-00b8ff44) → [`00b8ff48`](#insn-00b8ff48)
- ブロック [`00b8ff48`](#insn-00b8ff48) 範囲 `[['00b8ff48', '00b8ff4b']]`
  - `UNCONDITIONAL_JUMP` [`00b8ff48`](#insn-00b8ff48) → [`00b8feac`](#insn-00b8feac)
- ブロック [`00b8ff4c`](#insn-00b8ff4c) 範囲 `[['00b8ff4c', '00b8ff6b']]`
  - `CONDITIONAL_JUMP` [`00b8ff68`](#insn-00b8ff68) → [`00b8ff90`](#insn-00b8ff90)
  - `FALL_THROUGH` [`00b8ff68`](#insn-00b8ff68) → [`00b8ff6c`](#insn-00b8ff6c)
- ブロック [`00b8ff6c`](#insn-00b8ff6c) 範囲 `[['00b8ff6c', '00b8ff8f']]`
- ブロック [`00b8ff90`](#insn-00b8ff90) 範囲 `[['00b8ff90', '00b8ff93']]`

## 命令位置別の参照

- [`00b8fdc0`](#insn-00b8fdc0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdc4`](#insn-00b8fdc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdc8`](#insn-00b8fdc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdcc`](#insn-00b8fdcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdd0`](#insn-00b8fdd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdd4`](#insn-00b8fdd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdec`](#insn-00b8fdec) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fdf4`](#insn-00b8fdf4) → `00c9b928`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b8fdf8`](#insn-00b8fdf8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe14`](#insn-00b8fe14) → [`00b8fe44`](#insn-00b8fe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe1c`](#insn-00b8fe1c) → `00c9b5f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b8fe30`](#insn-00b8fe30) → `003104e1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZSt7nothrow` · 推定型 `undefined1`
- [`00b8fe34`](#insn-00b8fe34) → [`00c5a920`](../00c5a/00c5a920.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a920` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe38`](#insn-00b8fe38) → [`00b8fe64`](#insn-00b8fe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe40`](#insn-00b8fe40) → [`00b8fe2c`](#insn-00b8fe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe5c`](#insn-00b8fe5c) → [`00c5cbd0`](../00c5c/00c5cbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cbd0` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe60`](#insn-00b8fe60) → [`00b8fe8c`](#insn-00b8fe8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe80`](#insn-00b8fe80) → [`00c5cbd0`](../00c5c/00c5cbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cbd0` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe88`](#insn-00b8fe88) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b8fe9c`](#insn-00b8fe9c) → [`00c5c350`](../00c5c/00c5c350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c350` · 推定シンボル `None` · 推定型 `None`
- [`00b8fea0`](#insn-00b8fea0) → [`00b8ff4c`](#insn-00b8ff4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fea8`](#insn-00b8fea8) → [`00b8fec4`](#insn-00b8fec4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8febc`](#insn-00b8febc) → [`00c5c320`](../00c5c/00c5c320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c320` · 推定シンボル `None` · 推定型 `None`
- [`00b8fec0`](#insn-00b8fec0) → [`00b8ff4c`](#insn-00b8ff4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fed4`](#insn-00b8fed4) → [`00b8fedc`](#insn-00b8fedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fee8`](#insn-00b8fee8) → [`00b8feac`](#insn-00b8feac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8fefc`](#insn-00b8fefc) → [`00b8ff14`](#insn-00b8ff14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff08`](#insn-00b8ff08) → [`00c5c270`](../00c5c/00c5c270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c270` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff2c`](#insn-00b8ff2c) → [`00b8feac`](#insn-00b8feac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff44`](#insn-00b8ff44) → [`00b8ff34`](#insn-00b8ff34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff48`](#insn-00b8ff48) → [`00b8feac`](#insn-00b8feac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff58`](#insn-00b8ff58) → [`00c5c320`](../00c5c/00c5c320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c320` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff60`](#insn-00b8ff60) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff68`](#insn-00b8ff68) → [`00b8ff90`](#insn-00b8ff90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff6c`](#insn-00b8ff6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff70`](#insn-00b8ff70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff74`](#insn-00b8ff74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff78`](#insn-00b8ff78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff7c`](#insn-00b8ff7c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff80`](#insn-00b8ff80) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8ff90`](#insn-00b8ff90) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b8fdc0`](#insn-00b8fdc0)

~~~json
{
  "source": "00b8fdc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdc4`](#insn-00b8fdc4)

~~~json
{
  "source": "00b8fdc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdc8`](#insn-00b8fdc8)

~~~json
{
  "source": "00b8fdc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdcc`](#insn-00b8fdcc)

~~~json
{
  "source": "00b8fdcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdd0`](#insn-00b8fdd0)

~~~json
{
  "source": "00b8fdd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdd4`](#insn-00b8fdd4)

~~~json
{
  "source": "00b8fdd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdec`](#insn-00b8fdec)

~~~json
{
  "source": "00b8fdec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fdf4`](#insn-00b8fdf4)

~~~json
{
  "source": "00b8fdf4",
  "target": "00c9b928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b928",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b8fdf8`](#insn-00b8fdf8)

~~~json
{
  "source": "00b8fdf8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe14`](#insn-00b8fe14)

~~~json
{
  "source": "00b8fe14",
  "target": "00b8fe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe1c`](#insn-00b8fe1c)

~~~json
{
  "source": "00b8fe1c",
  "target": "00c9b5f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5f0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b8fe30`](#insn-00b8fe30)

~~~json
{
  "source": "00b8fe30",
  "target": "003104e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003104e1",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "003104e1",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b8fe34`](#insn-00b8fe34)

~~~json
{
  "source": "00b8fe34",
  "target": "00c5a920",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fe38`](#insn-00b8fe38)

~~~json
{
  "source": "00b8fe38",
  "target": "00b8fe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe40`](#insn-00b8fe40)

~~~json
{
  "source": "00b8fe40",
  "target": "00b8fe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe5c`](#insn-00b8fe5c)

~~~json
{
  "source": "00b8fe5c",
  "target": "00c5cbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fe60`](#insn-00b8fe60)

~~~json
{
  "source": "00b8fe60",
  "target": "00b8fe8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fe80`](#insn-00b8fe80)

~~~json
{
  "source": "00b8fe80",
  "target": "00c5cbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fe88`](#insn-00b8fe88)

~~~json
{
  "source": "00b8fe88",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fe9c`](#insn-00b8fe9c)

~~~json
{
  "source": "00b8fe9c",
  "target": "00c5c350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fea0`](#insn-00b8fea0)

~~~json
{
  "source": "00b8fea0",
  "target": "00b8ff4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fea8`](#insn-00b8fea8)

~~~json
{
  "source": "00b8fea8",
  "target": "00b8fec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8febc`](#insn-00b8febc)

~~~json
{
  "source": "00b8febc",
  "target": "00c5c320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8fec0`](#insn-00b8fec0)

~~~json
{
  "source": "00b8fec0",
  "target": "00b8ff4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fed4`](#insn-00b8fed4)

~~~json
{
  "source": "00b8fed4",
  "target": "00b8fedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fee8`](#insn-00b8fee8)

~~~json
{
  "source": "00b8fee8",
  "target": "00b8feac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8fefc`](#insn-00b8fefc)

~~~json
{
  "source": "00b8fefc",
  "target": "00b8ff14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff08`](#insn-00b8ff08)

~~~json
{
  "source": "00b8ff08",
  "target": "00c5c270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8ff2c`](#insn-00b8ff2c)

~~~json
{
  "source": "00b8ff2c",
  "target": "00b8feac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff44`](#insn-00b8ff44)

~~~json
{
  "source": "00b8ff44",
  "target": "00b8ff34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff48`](#insn-00b8ff48)

~~~json
{
  "source": "00b8ff48",
  "target": "00b8feac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff58`](#insn-00b8ff58)

~~~json
{
  "source": "00b8ff58",
  "target": "00c5c320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8ff60`](#insn-00b8ff60)

~~~json
{
  "source": "00b8ff60",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff68`](#insn-00b8ff68)

~~~json
{
  "source": "00b8ff68",
  "target": "00b8ff90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff6c`](#insn-00b8ff6c)

~~~json
{
  "source": "00b8ff6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff70`](#insn-00b8ff70)

~~~json
{
  "source": "00b8ff70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff74`](#insn-00b8ff74)

~~~json
{
  "source": "00b8ff74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff78`](#insn-00b8ff78)

~~~json
{
  "source": "00b8ff78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff7c`](#insn-00b8ff7c)

~~~json
{
  "source": "00b8ff7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff80`](#insn-00b8ff80)

~~~json
{
  "source": "00b8ff80",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8ff90`](#insn-00b8ff90)

~~~json
{
  "source": "00b8ff90",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
