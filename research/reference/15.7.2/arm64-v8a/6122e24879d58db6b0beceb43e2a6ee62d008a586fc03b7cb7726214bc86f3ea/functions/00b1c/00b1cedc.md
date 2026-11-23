# 00b1cedc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b1cfa4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cfa4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0064.md#compare-be56e2d0ef88185d1cab504876fffb09)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b1cedc",
  "name": "_ZN11flatbuffers6Parser21ParseNestedFlatbufferERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefE",
  "size": 1312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dadecdc388f8e8b2127509534af645a66b02a45c810ec41796a0c99c83faf239",
  "source_text_sha256": "dadecdc388f8e8b2127509534af645a66b02a45c810ec41796a0c99c83faf239",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b1cedc",
        "00b1d3fb"
      ]
    ],
    "bytes_sha256": "ee52231ad9519635b2a414a847c5563b68cf36dd57f26613f9d4d72cf47f67d9",
    "instruction_count": 328,
    "instruction_bytes": 1312,
    "body_bytes": 1312,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdf850](../00bdf/00bdf850.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bde1c0](../00bde/00bde1c0.md)
- [00bde910](../00bde/00bde910.md)
- [00bde970](../00bde/00bde970.md)
- [00bde980](../00bde/00bde980.md)
- [00bdeab0](../00bde/00bdeab0.md)
- [00bdef60](../00bde/00bdef60.md)
- [00bdf060](../00bdf/00bdf060.md)
- [00bdf0b0](../00bdf/00bdf0b0.md)
- [00bdf290](../00bdf/00bdf290.md)
- [00bdf380](../00bdf/00bdf380.md)
- [00bdf3c0](../00bdf/00bdf3c0.md)
- [00bdf700](../00bdf/00bdf700.md)
- [00bdf800](../00bdf/00bdf800.md)
- [00bdf8d0](../00bdf/00bdf8d0.md)
- [00bdfe60](../00bdf/00bdfe60.md)
- [00bdffc0](../00bdf/00bdffc0.md)

## 関連文字列（未確認候補）

~~~text
"_generated"
"error: "
"std::unique_ptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 11544 bytes

~~~c

void _ZN11flatbuffers6Parser21ParseNestedFlatbufferERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefE
               (char *param_1,long *param_2,long param_3,long param_4,undefined8 param_5,
               undefined8 param_6)

{
  long *plVar1;
  long lVar2;
  undefined8 *puVar3;
  bool bVar4;
  undefined1 *puVar5;
  undefined1 *puVar6;
  ulong uVar7;
  ulong uVar8;
  undefined8 *puVar9;
  undefined8 *puVar10;
  ulong uVar11;
  byte *pbVar12;
  undefined1 *puVar13;
  undefined1 *puVar14;
  undefined1 *puVar15;
  long lVar16;
  long lVar17;
  undefined8 uVar18;
  undefined8 uVar19;
  undefined8 uVar20;
  ulong local_6d8;
  ulong local_6d0;
  undefined1 *local_6c8;
  uint local_6c0;
  undefined2 uStack_6bc;
  undefined2 uStack_6ba;
  undefined8 uStack_6b8;
  void *local_6b0;
  undefined1 local_6a8;
  undefined1 local_6a0;
  char acStack_69f [7];
  char local_698;
  char acStack_697 [7];
  undefined8 local_690;
  undefined8 uStack_688;
  undefined8 local_680;
  undefined8 uStack_678;
  undefined4 local_670;
  undefined8 local_668;
  undefined8 uStack_660;
  undefined8 local_658;
  undefined8 uStack_650;
  undefined8 local_648;
  undefined8 uStack_640;
  undefined2 local_638;
  undefined1 local_636;
  undefined8 local_630;
  undefined8 uStack_628;
  undefined5 uStack_620;
  undefined3 local_61b;
  undefined5 uStack_618;
  undefined8 local_610;
  undefined8 uStack_608;
  undefined8 local_600;
  undefined8 uStack_5f8;
  undefined8 uStack_5f0;
  undefined8 uStack_5e8;
  undefined4 local_5e0;
  undefined8 local_5d8;
  undefined8 uStack_5d0;
  undefined7 local_5c8;
  undefined4 uStack_5c1;
  undefined8 local_5b8;
  undefined8 uStack_5b0;
  undefined8 uStack_5a8;
  undefined8 uStack_5a0;
  undefined8 local_598;
  undefined8 uStack_590;
  undefined8 uStack_588;
  undefined8 uStack_580;
  undefined8 local_578;
  undefined1 uStack_570;
  undefined7 uStack_56f;
  char cStack_568;
  undefined2 local_567;
  undefined1 local_565;
  undefined4 uStack_564;
  undefined8 uStack_560;
  undefined8 local_558;
  undefined8 local_550;
  undefined8 uStack_548;
  undefined8 local_540;
  undefined8 local_538;
  undefined2 local_530;
  long alStack_528 [22];
  undefined8 *local_478;
  undefined8 local_470;
  undefined8 local_468;
  undefined8 local_460;
  undefined8 local_458;
  undefined1 auStack_3f0 [56];
  uint local_3b8;
  uint local_3b0;
  int local_3a8;
  undefined4 uStack_3a4;
  ulong local_390;
  undefined8 local_2e8;
  undefined1 auStack_250 [408];
  undefined1 local_b8;
  long local_70;
  
  lVar2 = tpidr_el0;
  local_70 = *(long *)(lVar2 + 0x28);
  if (*(int *)((long)param_2 + 0x14) == 0x5b) {
    _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEjb
              (param_1,param_2,param_3,param_4,param_5,param_6,0,0);
    param_1[1] = '\x01';
    if (*param_1 != '\0') goto LAB_00b1d3c4;
  }
  else {
    lVar16 = *param_2;
    _ZN11flatbuffers6Parser16SkipAnyJsonValueEv(param_1,param_2);
    param_1[1] = '\x01';
    if (*param_1 != '\0') goto LAB_00b1d3c4;
    lVar17 = *param_2;
    puVar13 = (undefined1 *)(lVar16 + -1);
    local_6d0 = 0;
    local_6c8 = (undefined1 *)0x0;
    local_6d8 = 0;
    puVar15 = (undefined1 *)(lVar17 + -1);
    uVar11 = (long)puVar15 - (long)puVar13;
    if (0xffffffffffffffef < uVar11) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    if (uVar11 < 0x17) {
      local_6d8 = (ulong)(byte)((int)uVar11 << 1);
      puVar5 = (undefined1 *)((ulong)&local_6d8 | 1);
    }
    else {
      uVar7 = uVar11 + 0x10 & 0xfffffffffffffff0;
      puVar5 = (undefined1 *)_Znwm(uVar7);
      local_6d8 = uVar7 | 1;
      local_6d0 = uVar11;
      local_6c8 = puVar5;
    }
    if (lVar16 != lVar17) {
      uVar11 = lVar17 - lVar16;
      puVar6 = puVar5;
      if ((0x1f < uVar11) && ((puVar15 <= puVar5 || (puVar5 + uVar11 <= puVar13)))) {
        uVar8 = uVar11 & 0xffffffffffffffe0;
        puVar9 = (undefined8 *)(puVar5 + 0x10);
        puVar5 = puVar5 + uVar8;
        puVar10 = (undefined8 *)(lVar16 + 0xf);
        uVar7 = uVar8;
        do {
          puVar3 = puVar10 + -1;
          uVar18 = puVar10[-2];
          uVar20 = puVar10[1];
          uVar19 = *puVar10;
          uVar7 = uVar7 - 0x20;
          puVar10 = puVar10 + 4;
          puVar9[-1] = *puVar3;
          puVar9[-2] = uVar18;
          puVar9[1] = uVar20;
          *puVar9 = uVar19;
          puVar9 = puVar9 + 4;
        } while (uVar7 != 0);
        puVar6 = puVar5;
        puVar13 = puVar13 + uVar8;
        if (uVar11 == uVar8) goto LAB_00b1d044;
      }
      do {
        puVar14 = puVar13 + 1;
        puVar5 = puVar6 + 1;
        *puVar6 = *puVar13;
        puVar6 = puVar5;
        puVar13 = puVar14;
      } while (puVar15 != puVar14);
    }
LAB_00b1d044:
    local_540 = DAT_002b2820;
    uVar18 = s__generated_002ac2f1._0_8_;
    uStack_6b8 = 0x100010100000002;
    local_6b0 = (void *)0x0;
    local_6a0 = 0x1e;
    uStack_6bc = 0;
    acStack_69f[0] = s_std__unique_ptr_00298725[0];
    acStack_69f[1] = s_std__unique_ptr_00298725[1];
    acStack_69f[2] = s_std__unique_ptr_00298725[2];
    acStack_69f[3] = s_std__unique_ptr_00298725[3];
    acStack_69f[4] = s_std__unique_ptr_00298725[4];
    acStack_69f[5] = s_std__unique_ptr_00298725[5];
    acStack_69f[6] = s_std__unique_ptr_00298725[6];
    local_6c0 = 0;
    local_6a8 = 0;
    uStack_688 = 0;
    local_690 = 0;
    local_670 = 0;
    local_680 = 0;
    uStack_678 = 0;
    local_698 = s_std__unique_ptr_00298725[7];
    acStack_697[0] = s_std__unique_ptr_00298725[8];
    acStack_697[1] = s_std__unique_ptr_00298725[9];
    acStack_697[2] = s_std__unique_ptr_00298725[10];
    acStack_697[3] = s_std__unique_ptr_00298725[0xb];
    acStack_697[4] = s_std__unique_ptr_00298725[0xc];
    acStack_697[5] = s_std__unique_ptr_00298725[0xd];
    acStack_697[6] = s_std__unique_ptr_00298725[0xe];
    uStack_640 = 0;
    local_648 = 0;
    local_658 = 0;
    uStack_660 = 0;
    local_668 = 0;
    uStack_650 = 0x5402;
    local_638 = 1;
    local_636 = 0;
    local_630 = 0;
    uStack_628 = 0;
    uStack_618 = 0;
    uStack_620 = 0;
    local_61b = 0;
    uStack_5f8 = 0;
    local_600 = 0;
    uStack_5e8 = 0;
    uStack_5f0 = 0;
    uStack_608 = 0;
    local_610 = 0;
    local_5e0 = 1;
    local_5d8 = 0;
    uStack_5d0 = 0;
    local_5c8 = 0;
    uStack_5c1 = 0;
    local_578 = 0;
    uStack_560 = 0;
    uStack_564 = 0;
    uStack_590 = 0;
    local_598 = 0;
    uStack_580 = 0;
    uStack_588 = 0;
    uStack_5b0 = 0;
    local_5b8 = 0;
    uStack_5a0 = 0;
    uStack_5a8 = 0;
    uStack_570 = 0x14;
    local_567 = 0x6465;
    *puVar5 = 0;
    uStack_56f = (undefined7)uVar18;
    cStack_568 = SUB81(uVar18,7);
    local_565 = 0;
    local_550 = 0;
    uStack_548 = 0;
    local_558 = 0;
    local_538 = 0;
    local_530 = 0x101;
    _ZN11flatbuffers6ParserC2ERKNS_10IDLOptionsE(alStack_528,&local_6c0);
    _ZN11flatbuffers10IDLOptionsD2Ev(&local_6c0);
    local_2e8 = *(undefined8 *)(param_4 + 0xe0);
    if (alStack_528 != param_2) {
      _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE14__assign_multiINS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEEEEvT_SP_
                (&local_478,param_2[0x16],param_2 + 0x17);
      _ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA_
                (&local_460,param_2[0x19],param_2[0x1a]);
    }
    _ZN11flatbuffers10IDLOptionsaSERKS0_(auStack_250,param_2 + 0x5b);
    local_b8 = (undefined1)param_2[0x8e];
    puVar13 = (undefined1 *)((ulong)&local_6d8 | 1);
    if ((local_6d8 & 1) != 0) {
      puVar13 = local_6c8;
    }
    uVar11 = _ZN11flatbuffers6Parser5ParseEPKcPS2_S2_(alStack_528,puVar13,0,0);
    _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
              (&local_478,local_470);
    local_470 = 0;
    local_468 = 0;
    local_458 = local_460;
    local_478 = &local_470;
    if ((uVar11 & 1) == 0) {
      _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
                (&local_6c0,"error: ",auStack_3f0);
      _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
                (param_2,&local_6c0);
      if ((local_6c0 & 1) != 0) {
        _ZdlPv(local_6b0);
      }
      param_1[0] = '\x01';
      param_1[1] = '\x01';
      bVar4 = true;
    }
    else {
      plVar1 = param_2 + 0x2a;
      if ((ulong)param_2[0x33] < local_390) {
        param_2[0x33] = local_390;
      }
      lVar16 = param_2[0x30];
      uVar11 = local_390 - 1 &
               -((ulong)((local_3b8 - local_3a8) + local_3b0) +
                (ulong)(uint)(((int)param_2[0x2e] - (int)lVar16) + (int)param_2[0x2f]));
      if ((ulong)(lVar16 - param_2[0x31]) < uVar11) {
        _ZN11flatbuffers15vector_downward10reallocateEm(plVar1,uVar11);
        puVar13 = (undefined1 *)(param_2[0x30] - uVar11);
        param_2[0x30] = (long)puVar13;
LAB_00b1d2bc:
        *puVar13 = 0;
        if (uVar11 != 1) {
          uVar7 = 1;
          do {
            *(undefined1 *)(param_2[0x30] + uVar7) = 0;
            uVar7 = uVar7 + 1;
          } while (uVar11 != uVar7);
        }
      }
      else {
        puVar13 = (undefined1 *)(lVar16 - uVar11);
        param_2[0x30] = (long)puVar13;
        if (uVar11 != 0) goto LAB_00b1d2bc;
      }
      uVar11 = ((ulong)local_3b8 - (long)CONCAT44(uStack_3a4,local_3a8)) + (ulong)local_3b0;
      uVar7 = uVar11 & 0xffffffff;
      _ZN11flatbuffers17FlatBufferBuilder11StartVectorEmm(plVar1,uVar7,1);
      if (uVar7 != 0) {
        lVar16 = param_2[0x30];
        if ((ulong)(lVar16 - param_2[0x31]) < uVar7) {
          _ZN11flatbuffers15vector_downward10reallocateEm(plVar1,uVar7);
          lVar16 = param_2[0x30];
        }
        param_2[0x30] = (long)(lVar16 - uVar7);
        memcpy((void *)(lVar16 - uVar7),(void *)CONCAT44(uStack_3a4,local_3a8),uVar7);
      }
      *(undefined1 *)((long)param_2 + 0x196) = 0;
      _ZN11flatbuffers17FlatBufferBuilder11PushElementIjEEjT_(plVar1,uVar11 & 0xffffffff);
      _ZN11flatbuffers11NumToStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_
                (&local_6c0);
      pbVar12 = (byte *)(param_3 + 0x20);
      if ((*pbVar12 & 1) == 0) {
        pbVar12[0] = 0;
        pbVar12[1] = 0;
      }
      else {
        **(undefined1 **)(param_3 + 0x30) = 0;
        *(undefined8 *)(param_3 + 0x28) = 0;
        if ((*(byte *)(param_3 + 0x20) & 1) != 0) {
          _ZdlPv(*(void **)(param_3 + 0x30));
          *(undefined8 *)(param_3 + 0x20) = 0;
        }
      }
      bVar4 = false;
      *(void **)(param_3 + 0x30) = local_6b0;
      *(undefined8 *)(param_3 + 0x28) = uStack_6b8;
      *(ulong *)pbVar12 = CONCAT26(uStack_6ba,CONCAT24(uStack_6bc,local_6c0));
    }
    _ZN11flatbuffers6ParserD2Ev(alStack_528);
    if ((local_6d8 & 1) != 0) {
      _ZdlPv(local_6c8);
    }
    if (bVar4) goto LAB_00b1d3c4;
  }
  param_1[0] = '\0';
  param_1[1] = '\0';
LAB_00b1d3c4:
  if (*(long *)(lVar2 + 0x28) != local_70) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b1cedc"></a> `00b1cedc` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00b1cee0"></a> `00b1cee0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b1cee4"></a> `00b1cee4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b1cee8"></a> `00b1cee8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b1ceec"></a> `00b1ceec` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b1cef0"></a> `00b1cef0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b1cef4"></a> `00b1cef4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b1cef8"></a> `00b1cef8` | `ff 03 1a d1` | sub sp,sp,#0x680 | `FALL_THROUGH`
<a id="insn-00b1cefc"></a> `00b1cefc` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b1cf00"></a> `00b1cf00` | `49 17 40 f9` | ldr x9,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00b1cf04"></a> `00b1cf04` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00b1cf08"></a> `00b1cf08` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00b1cf0c"></a> `00b1cf0c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b1cf10"></a> `00b1cf10` | `a9 03 1a f8` | stur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b1cf14"></a> `00b1cf14` | `09 14 40 b9` | ldr w9,[x0, #0x14] | `FALL_THROUGH`
<a id="insn-00b1cf18"></a> `00b1cf18` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b1cf1c"></a> `00b1cf1c` | `3f 6d 01 71` | cmp w9,#0x5b | `FALL_THROUGH`
<a id="insn-00b1cf20"></a> `00b1cf20` | `a1 01 00 54` | b.ne 0x00b1cf54 | `CONDITIONAL_JUMP`
<a id="insn-00b1cf24"></a> `00b1cf24` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b1cf28"></a> `00b1cf28` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b1cf2c"></a> `00b1cf2c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b1cf30"></a> `00b1cf30` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b1cf34"></a> `00b1cf34` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00b1cf38"></a> `00b1cf38` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00b1cf3c"></a> `00b1cf3c` | `f1 09 03 94` | bl 0x00bdf700 | `UNCONDITIONAL_CALL`
<a id="insn-00b1cf40"></a> `00b1cf40` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00b1cf44"></a> `00b1cf44` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b1cf48"></a> `00b1cf48` | `69 06 00 39` | strb w9,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00b1cf4c"></a> `00b1cf4c` | `c8 23 00 35` | cbnz w8,0x00b1d3c4 | `CONDITIONAL_JUMP`
<a id="insn-00b1cf50"></a> `00b1cf50` | `1c 01 00 14` | b 0x00b1d3c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1cf54"></a> `00b1cf54` | `bb 02 40 f9` | ldr x27,[x21] | `FALL_THROUGH`
<a id="insn-00b1cf58"></a> `00b1cf58` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b1cf5c"></a> `00b1cf5c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b1cf60"></a> `00b1cf60` | `28 0a 03 94` | bl 0x00bdf800 | `UNCONDITIONAL_CALL`
<a id="insn-00b1cf64"></a> `00b1cf64` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00b1cf68"></a> `00b1cf68` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b1cf6c"></a> `00b1cf6c` | `69 06 00 39` | strb w9,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00b1cf70"></a> `00b1cf70` | `a8 22 00 35` | cbnz w8,0x00b1d3c4 | `CONDITIONAL_JUMP`
<a id="insn-00b1cf74"></a> `00b1cf74` | `bc 02 40 f9` | ldr x28,[x21] | `FALL_THROUGH`
<a id="insn-00b1cf78"></a> `00b1cf78` | `78 07 00 d1` | sub x24,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00b1cf7c"></a> `00b1cf7c` | `ff 7f 01 a9` | stp xzr,xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b1cf80"></a> `00b1cf80` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b1cf84"></a> `00b1cf84` | `99 07 00 d1` | sub x25,x28,#0x1 | `FALL_THROUGH`
<a id="insn-00b1cf88"></a> `00b1cf88` | `34 03 18 cb` | sub x20,x25,x24 | `FALL_THROUGH`
<a id="insn-00b1cf8c"></a> `00b1cf8c` | `9f 42 00 b1` | cmn x20,#0x10 | `FALL_THROUGH`
<a id="insn-00b1cf90"></a> `00b1cf90` | `42 23 00 54` | b.cs 0x00b1d3f8 | `CONDITIONAL_JUMP`
<a id="insn-00b1cf94"></a> `00b1cf94` | `9f 5a 00 f1` | cmp x20,#0x16 | `FALL_THROUGH`
<a id="insn-00b1cf98"></a> `00b1cf98` | `f7 03 00 f9` | str x23,[sp] | `FALL_THROUGH`
<a id="insn-00b1cf9c"></a> `00b1cf9c` | `c8 00 00 54` | b.hi 0x00b1cfb4 | `CONDITIONAL_JUMP`
<a id="insn-00b1cfa0"></a> `00b1cfa0` | `88 7a 1f 53` | lsl w8,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00b1cfa4"></a> `00b1cfa4` | `e9 23 00 91` | add x9,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b1cfa8"></a> `00b1cfa8` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b1cfac"></a> `00b1cfac` | `20 01 40 b2` | orr x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b1cfb0"></a> `00b1cfb0` | `08 00 00 14` | b 0x00b1cfd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1cfb4"></a> `00b1cfb4` | `88 42 00 91` | add x8,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00b1cfb8"></a> `00b1cfb8` | `17 ed 7c 92` | and x23,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00b1cfbc"></a> `00b1cfbc` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b1cfc0"></a> `00b1cfc0` | `e0 f7 02 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00b1cfc4"></a> `00b1cfc4` | `e8 02 40 b2` | orr x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00b1cfc8"></a> `00b1cfc8` | `e8 d3 00 a9` | stp x8,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b1cfcc"></a> `00b1cfcc` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b1cfd0"></a> `00b1cfd0` | `7f 03 1c eb` | cmp x27,x28 | `FALL_THROUGH`
<a id="insn-00b1cfd4"></a> `00b1cfd4` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b1cfd8"></a> `00b1cfd8` | `60 03 00 54` | b.eq 0x00b1d044 | `CONDITIONAL_JUMP`
<a id="insn-00b1cfdc"></a> `00b1cfdc` | `89 03 1b cb` | sub x9,x28,x27 | `FALL_THROUGH`
<a id="insn-00b1cfe0"></a> `00b1cfe0` | `3f 81 00 f1` | cmp x9,#0x20 | `FALL_THROUGH`
<a id="insn-00b1cfe4"></a> `00b1cfe4` | `83 02 00 54` | b.cc 0x00b1d034 | `CONDITIONAL_JUMP`
<a id="insn-00b1cfe8"></a> `00b1cfe8` | `1f 00 19 eb` | cmp x0,x25 | `FALL_THROUGH`
<a id="insn-00b1cfec"></a> `00b1cfec` | `82 00 00 54` | b.cs 0x00b1cffc | `CONDITIONAL_JUMP`
<a id="insn-00b1cff0"></a> `00b1cff0` | `0a 00 09 8b` | add x10,x0,x9 | `FALL_THROUGH`
<a id="insn-00b1cff4"></a> `00b1cff4` | `1f 03 0a eb` | cmp x24,x10 | `FALL_THROUGH`
<a id="insn-00b1cff8"></a> `00b1cff8` | `e3 01 00 54` | b.cc 0x00b1d034 | `CONDITIONAL_JUMP`
<a id="insn-00b1cffc"></a> `00b1cffc` | `2a e9 7b 92` | and x10,x9,#-0x20 | `FALL_THROUGH`
<a id="insn-00b1d000"></a> `00b1d000` | `0b 40 00 91` | add x11,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00b1d004"></a> `00b1d004` | `18 03 0a 8b` | add x24,x24,x10 | `FALL_THROUGH`
<a id="insn-00b1d008"></a> `00b1d008` | `00 00 0a 8b` | add x0,x0,x10 | `FALL_THROUGH`
<a id="insn-00b1d00c"></a> `00b1d00c` | `6c 3f 00 91` | add x12,x27,#0xf | `FALL_THROUGH`
<a id="insn-00b1d010"></a> `00b1d010` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00b1d014"></a> `00b1d014` | `80 85 7f ad` | ldp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00b1d018"></a> `00b1d018` | `ad 81 00 f1` | subs x13,x13,#0x20 | `FALL_THROUGH`
<a id="insn-00b1d01c"></a> `00b1d01c` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00b1d020"></a> `00b1d020` | `60 85 3f ad` | stp q0,q1,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00b1d024"></a> `00b1d024` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00b1d028"></a> `00b1d028` | `61 ff ff 54` | b.ne 0x00b1d014 | `CONDITIONAL_JUMP`
<a id="insn-00b1d02c"></a> `00b1d02c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00b1d030"></a> `00b1d030` | `a0 00 00 54` | b.eq 0x00b1d044 | `CONDITIONAL_JUMP`
<a id="insn-00b1d034"></a> `00b1d034` | `09 17 40 38` | ldrb w9,[x24], #0x1 | `FALL_THROUGH`
<a id="insn-00b1d038"></a> `00b1d038` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00b1d03c"></a> `00b1d03c` | `09 14 00 38` | strb w9,[x0], #0x1 | `FALL_THROUGH`
<a id="insn-00b1d040"></a> `00b1d040` | `a1 ff ff 54` | b.ne 0x00b1d034 | `CONDITIONAL_JUMP`
<a id="insn-00b1d044"></a> `00b1d044` | `49 00 80 d2` | mov x9,#0x2 | `FALL_THROUGH`
<a id="insn-00b1d048"></a> `00b1d048` | `29 20 c0 f2` | movk x9,#0x101, LSL #32 | `FALL_THROUGH`
<a id="insn-00b1d04c"></a> `00b1d04c` | `09 20 e0 f2` | movk x9,#0x100, LSL #48 | `FALL_THROUGH`
<a id="insn-00b1d050"></a> `00b1d050` | `e9 ff 02 a9` | stp x9,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b1d054"></a> `00b1d054` | `c9 bb ff f0` | adrp x9,0x298000 | `FALL_THROUGH`
<a id="insn-00b1d058"></a> `00b1d058` | `ca 03 80 52` | mov w10,#0x1e | `FALL_THROUGH`
<a id="insn-00b1d05c"></a> `00b1d05c` | `29 95 1c 91` | add x9,x9,#0x725 | `FALL_THROUGH`
<a id="insn-00b1d060"></a> `00b1d060` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b1d064"></a> `00b1d064` | `ea 03 01 39` | strb w10,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b1d068"></a> `00b1d068` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00b1d06c"></a> `00b1d06c` | `29 71 40 f8` | ldur x9,[x9, #0x7] | `FALL_THROUGH`
<a id="insn-00b1d070"></a> `00b1d070` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00b1d074"></a> `00b1d074` | `ff 4b 00 79` | strh wzr,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00b1d078"></a> `00b1d078` | `ea 13 04 f8` | stur x10,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00b1d07c"></a> `00b1d07c` | `4a 80 8a 52` | mov w10,#0x5402 | `FALL_THROUGH`
<a id="insn-00b1d080"></a> `00b1d080` | `ff 23 00 b9` | str wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b1d084"></a> `00b1d084` | `ff e3 00 39` | strb wzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b1d088"></a> `00b1d088` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b1d08c"></a> `00b1d08c` | `ff 43 01 39` | strb wzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b1d090"></a> `00b1d090` | `ff 73 00 b9` | str wzr,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b1d094"></a> `00b1d094` | `ff 7f 06 a9` | stp xzr,xzr,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b1d098"></a> `00b1d098` | `e9 27 00 f9` | str x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00b1d09c"></a> `00b1d09c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b1d0a0"></a> `00b1d0a0` | `00 81 87 3c` | stur q0,[x8, #0x78] | `FALL_THROUGH`
<a id="insn-00b1d0a4"></a> `00b1d0a4` | `00 81 86 3c` | stur q0,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-00b1d0a8"></a> `00b1d0a8` | `ea 23 01 79` | strh w10,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1d0ac"></a> `00b1d0ac` | `ea 83 00 91` | add x10,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b1d0b0"></a> `00b1d0b0` | `e0 83 87 3c` | stur q0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00b1d0b4"></a> `00b1d0b4` | `ff 4b 02 39` | strb wzr,[sp, #0x92] | `FALL_THROUGH`
<a id="insn-00b1d0b8"></a> `00b1d0b8` | `e9 53 01 79` | strh w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00b1d0bc"></a> `00b1d0bc` | `ff ab 02 39` | strb wzr,[sp, #0xaa] | `FALL_THROUGH`
<a id="insn-00b1d0c0"></a> `00b1d0c0` | `ff 7f 0b a9` | stp xzr,xzr,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00b1d0c4"></a> `00b1d0c4` | `1f 51 0a f8` | stur xzr,[x8, #0xa5] | `FALL_THROUGH`
<a id="insn-00b1d0c8"></a> `00b1d0c8` | `ff 63 00 f9` | str xzr,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b1d0cc"></a> `00b1d0cc` | `00 01 06 ad` | stp q0,q0,[x8, #0xc0] | `FALL_THROUGH`
<a id="insn-00b1d0d0"></a> `00b1d0d0` | `00 2d 80 3d` | str q0,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00b1d0d4"></a> `00b1d0d4` | `e9 03 01 b9` | str w9,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b1d0d8"></a> `00b1d0d8` | `89 02 80 52` | mov w9,#0x14 | `FALL_THROUGH`
<a id="insn-00b1d0dc"></a> `00b1d0dc` | `1f f1 0f b8` | stur wzr,[x8, #0xff] | `FALL_THROUGH`
<a id="insn-00b1d0e0"></a> `00b1d0e0` | `48 21 04 91` | add x8,x10,#0x108 | `FALL_THROUGH`
<a id="insn-00b1d0e4"></a> `00b1d0e4` | `ff ff 10 a9` | stp xzr,xzr,[sp, #0x108] | `FALL_THROUGH`
<a id="insn-00b1d0e8"></a> `00b1d0e8` | `ff 8f 00 f9` | str xzr,[sp, #0x118] | `FALL_THROUGH`
<a id="insn-00b1d0ec"></a> `00b1d0ec` | `00 01 02 ad` | stp q0,q0,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00b1d0f0"></a> `00b1d0f0` | `00 01 01 ad` | stp q0,q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b1d0f4"></a> `00b1d0f4` | `00 01 00 ad` | stp q0,q0,[x8] | `FALL_THROUGH`
<a id="insn-00b1d0f8"></a> `00b1d0f8` | `a8 8c 8c 52` | mov w8,#0x6465 | `FALL_THROUGH`
<a id="insn-00b1d0fc"></a> `00b1d0fc` | `e9 c3 05 39` | strb w9,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00b1d100"></a> `00b1d100` | `49 65 05 91` | add x9,x10,#0x159 | `FALL_THROUGH`
<a id="insn-00b1d104"></a> `00b1d104` | `28 01 00 79` | strh w8,[x9] | `FALL_THROUGH`
<a id="insn-00b1d108"></a> `00b1d108` | `68 bc ff f0` | adrp x8,0x2ac000 | `FALL_THROUGH`
<a id="insn-00b1d10c"></a> `00b1d10c` | `08 c5 0b 91` | add x8,x8,#0x2f1 | `FALL_THROUGH`
<a id="insn-00b1d110"></a> `00b1d110` | `a9 bc ff b0` | adrp x9,0x2b2000 | `FALL_THROUGH`
<a id="insn-00b1d114"></a> `00b1d114` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00b1d118"></a> `00b1d118` | `20 11 44 fd` | ldr d0,[x9, #0x820] | `FALL_THROUGH`
<a id="insn-00b1d11c"></a> `00b1d11c` | `1f 00 00 39` | strb wzr,[x0] | `FALL_THROUGH`
<a id="insn-00b1d120"></a> `00b1d120` | `29 20 80 52` | mov w9,#0x101 | `FALL_THROUGH`
<a id="insn-00b1d124"></a> `00b1d124` | `4a 45 05 91` | add x10,x10,#0x151 | `FALL_THROUGH`
<a id="insn-00b1d128"></a> `00b1d128` | `e0 e3 06 91` | add x0,sp,#0x1b8 | `FALL_THROUGH`
<a id="insn-00b1d12c"></a> `00b1d12c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b1d130"></a> `00b1d130` | `48 01 00 f9` | str x8,[x10] | `FALL_THROUGH`
<a id="insn-00b1d134"></a> `00b1d134` | `ff ef 05 39` | strb wzr,[sp, #0x17b] | `FALL_THROUGH`
<a id="insn-00b1d138"></a> `00b1d138` | `ff 7f 19 a9` | stp xzr,xzr,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00b1d13c"></a> `00b1d13c` | `ff c7 00 f9` | str xzr,[sp, #0x188] | `FALL_THROUGH`
<a id="insn-00b1d140"></a> `00b1d140` | `e0 d3 00 fd` | str d0,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00b1d144"></a> `00b1d144` | `ff d7 00 f9` | str xzr,[sp, #0x1a8] | `FALL_THROUGH`
<a id="insn-00b1d148"></a> `00b1d148` | `e9 63 03 79` | strh w9,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00b1d14c"></a> `00b1d14c` | `f8 e3 06 91` | add x24,sp,#0x1b8 | `FALL_THROUGH`
<a id="insn-00b1d150"></a> `00b1d150` | `08 06 03 94` | bl 0x00bde970 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d154"></a> `00b1d154` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b1d158"></a> `00b1d158` | `ee 05 03 94` | bl 0x00bde910 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d15c"></a> `00b1d15c` | `c8 72 40 f9` | ldr x8,[x22, #0xe0] | `FALL_THROUGH`
<a id="insn-00b1d160"></a> `00b1d160` | `1f 03 15 eb` | cmp x24,x21 | `FALL_THROUGH`
<a id="insn-00b1d164"></a> `00b1d164` | `16 c3 02 91` | add x22,x24,#0xb0 | `FALL_THROUGH`
<a id="insn-00b1d168"></a> `00b1d168` | `e8 ff 01 f9` | str x8,[sp, #0x3f8] | `FALL_THROUGH`
<a id="insn-00b1d16c"></a> `00b1d16c` | `00 01 00 54` | b.eq 0x00b1d18c | `CONDITIONAL_JUMP`
<a id="insn-00b1d170"></a> `00b1d170` | `a1 5a 40 f9` | ldr x1,[x21, #0xb0] | `FALL_THROUGH`
<a id="insn-00b1d174"></a> `00b1d174` | `a2 e2 02 91` | add x2,x21,#0xb8 | `FALL_THROUGH`
<a id="insn-00b1d178"></a> `00b1d178` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b1d17c"></a> `00b1d17c` | `39 0b 03 94` | bl 0x00bdfe60 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d180"></a> `00b1d180` | `a1 8a 4c a9` | ldp x1,x2,[x21, #0xc8] | `FALL_THROUGH`
<a id="insn-00b1d184"></a> `00b1d184` | `00 23 03 91` | add x0,x24,#0xc8 | `FALL_THROUGH`
<a id="insn-00b1d188"></a> `00b1d188` | `8e 0b 03 94` | bl 0x00bdffc0 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d18c"></a> `00b1d18c` | `a1 62 0b 91` | add x1,x21,#0x2d8 | `FALL_THROUGH`
<a id="insn-00b1d190"></a> `00b1d190` | `00 63 0b 91` | add x0,x24,#0x2d8 | `FALL_THROUGH`
<a id="insn-00b1d194"></a> `00b1d194` | `b3 07 03 94` | bl 0x00bdf060 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d198"></a> `00b1d198` | `e9 23 40 39` | ldrb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b1d19c"></a> `00b1d19c` | `ea 0f 40 f9` | ldr x10,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b1d1a0"></a> `00b1d1a0` | `a8 c2 51 39` | ldrb w8,[x21, #0x470] | `FALL_THROUGH`
<a id="insn-00b1d1a4"></a> `00b1d1a4` | `eb 23 00 91` | add x11,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b1d1a8"></a> `00b1d1a8` | `6b 01 40 b2` | orr x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b1d1ac"></a> `00b1d1ac` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b1d1b0"></a> `00b1d1b0` | `61 01 8a 9a` | csel x1,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00b1d1b4"></a> `00b1d1b4` | `e0 e3 06 91` | add x0,sp,#0x1b8 | `FALL_THROUGH`
<a id="insn-00b1d1b8"></a> `00b1d1b8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b1d1bc"></a> `00b1d1bc` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00b1d1c0"></a> `00b1d1c0` | `e8 a3 18 39` | strb w8,[sp, #0x628] | `FALL_THROUGH`
<a id="insn-00b1d1c4"></a> `00b1d1c4` | `67 07 03 94` | bl 0x00bdef60 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d1c8"></a> `00b1d1c8` | `e1 3b 41 f9` | ldr x1,[sp, #0x270] | `FALL_THROUGH`
<a id="insn-00b1d1cc"></a> `00b1d1cc` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00b1d1d0"></a> `00b1d1d0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b1d1d4"></a> `00b1d1d4` | `14 e3 02 91` | add x20,x24,#0xb8 | `FALL_THROUGH`
<a id="insn-00b1d1d8"></a> `00b1d1d8` | `36 06 03 94` | bl 0x00bdeab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d1dc"></a> `00b1d1dc` | `e8 43 41 f9` | ldr x8,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00b1d1e0"></a> `00b1d1e0` | `ff 3b 01 f9` | str xzr,[sp, #0x270] | `FALL_THROUGH`
<a id="insn-00b1d1e4"></a> `00b1d1e4` | `f4 37 01 f9` | str x20,[sp, #0x268] | `FALL_THROUGH`
<a id="insn-00b1d1e8"></a> `00b1d1e8` | `ff 3f 01 f9` | str xzr,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00b1d1ec"></a> `00b1d1ec` | `e8 47 01 f9` | str x8,[sp, #0x288] | `FALL_THROUGH`
<a id="insn-00b1d1f0"></a> `00b1d1f0` | `f7 03 00 36` | tbz w23,#0x0,0x00b1d26c | `CONDITIONAL_JUMP`
<a id="insn-00b1d1f4"></a> `00b1d1f4` | `e8 2b 43 b9` | ldr w8,[sp, #0x328] | `FALL_THROUGH`
<a id="insn-00b1d1f8"></a> `00b1d1f8` | `ea 3b 43 b9` | ldr w10,[sp, #0x338] | `FALL_THROUGH`
<a id="insn-00b1d1fc"></a> `00b1d1fc` | `e9 ab 41 f9` | ldr x9,[sp, #0x350] | `FALL_THROUGH`
<a id="insn-00b1d200"></a> `00b1d200` | `ab ce 40 f9` | ldr x11,[x21, #0x198] | `FALL_THROUGH`
<a id="insn-00b1d204"></a> `00b1d204` | `ec 33 43 b9` | ldr w12,[sp, #0x330] | `FALL_THROUGH`
<a id="insn-00b1d208"></a> `00b1d208` | `08 01 0a 4b` | sub w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00b1d20c"></a> `00b1d20c` | `b6 42 05 91` | add x22,x21,#0x150 | `FALL_THROUGH`
<a id="insn-00b1d210"></a> `00b1d210` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00b1d214"></a> `00b1d214` | `08 01 0c 0b` | add w8,w8,w12 | `FALL_THROUGH`
<a id="insn-00b1d218"></a> `00b1d218` | `42 00 00 54` | b.cs 0x00b1d220 | `CONDITIONAL_JUMP`
<a id="insn-00b1d21c"></a> `00b1d21c` | `a9 ce 00 f9` | str x9,[x21, #0x198] | `FALL_THROUGH`
<a id="insn-00b1d220"></a> `00b1d220` | `ab 72 41 b9` | ldr w11,[x21, #0x170] | `FALL_THROUGH`
<a id="insn-00b1d224"></a> `00b1d224` | `aa 36 58 a9` | ldp x10,x13,[x21, #0x180] | `FALL_THROUGH`
<a id="insn-00b1d228"></a> `00b1d228` | `ac 7a 41 b9` | ldr w12,[x21, #0x178] | `FALL_THROUGH`
<a id="insn-00b1d22c"></a> `00b1d22c` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b1d230"></a> `00b1d230` | `6b 01 0a 4b` | sub w11,w11,w10 | `FALL_THROUGH`
<a id="insn-00b1d234"></a> `00b1d234` | `6b 01 0c 0b` | add w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00b1d238"></a> `00b1d238` | `08 01 0b 8b` | add x8,x8,x11 | `FALL_THROUGH`
<a id="insn-00b1d23c"></a> `00b1d23c` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00b1d240"></a> `00b1d240` | `37 01 08 8a` | and x23,x9,x8 | `FALL_THROUGH`
<a id="insn-00b1d244"></a> `00b1d244` | `48 01 0d cb` | sub x8,x10,x13 | `FALL_THROUGH`
<a id="insn-00b1d248"></a> `00b1d248` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00b1d24c"></a> `00b1d24c` | `22 03 00 54` | b.cs 0x00b1d2b0 | `CONDITIONAL_JUMP`
<a id="insn-00b1d250"></a> `00b1d250` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b1d254"></a> `00b1d254` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b1d258"></a> `00b1d258` | `0e 08 03 94` | bl 0x00bdf290 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d25c"></a> `00b1d25c` | `a8 c2 40 f9` | ldr x8,[x21, #0x180] | `FALL_THROUGH`
<a id="insn-00b1d260"></a> `00b1d260` | `08 01 17 cb` | sub x8,x8,x23 | `FALL_THROUGH`
<a id="insn-00b1d264"></a> `00b1d264` | `a8 c2 00 f9` | str x8,[x21, #0x180] | `FALL_THROUGH`
<a id="insn-00b1d268"></a> `00b1d268` | `15 00 00 14` | b 0x00b1d2bc | `UNCONDITIONAL_JUMP`
<a id="insn-00b1d26c"></a> `00b1d26c` | `e8 e3 06 91` | add x8,sp,#0x1b8 | `FALL_THROUGH`
<a id="insn-00b1d270"></a> `00b1d270` | `a0 bb ff 90` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00b1d274"></a> `00b1d274` | `01 e1 04 91` | add x1,x8,#0x138 | `FALL_THROUGH`
<a id="insn-00b1d278"></a> `00b1d278` | `00 14 15 91` | add x0,x0,#0x545 | `FALL_THROUGH`
<a id="insn-00b1d27c"></a> `00b1d27c` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b1d280"></a> `00b1d280` | `b8 f7 02 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d284"></a> `00b1d284` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b1d288"></a> `00b1d288` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b1d28c"></a> `00b1d28c` | `91 09 03 94` | bl 0x00bdf8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d290"></a> `00b1d290` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b1d294"></a> `00b1d294` | `68 00 00 36` | tbz w8,#0x0,0x00b1d2a0 | `CONDITIONAL_JUMP`
<a id="insn-00b1d298"></a> `00b1d298` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b1d29c"></a> `00b1d29c` | `31 f7 02 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d2a0"></a> `00b1d2a0` | `28 20 80 52` | mov w8,#0x101 | `FALL_THROUGH`
<a id="insn-00b1d2a4"></a> `00b1d2a4` | `68 02 00 79` | strh w8,[x19] | `FALL_THROUGH`
<a id="insn-00b1d2a8"></a> `00b1d2a8` | `34 00 80 52` | mov w20,#0x1 | `FALL_THROUGH`
<a id="insn-00b1d2ac"></a> `00b1d2ac` | `3e 00 00 14` | b 0x00b1d3a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1d2b0"></a> `00b1d2b0` | `48 01 17 cb` | sub x8,x10,x23 | `FALL_THROUGH`
<a id="insn-00b1d2b4"></a> `00b1d2b4` | `a8 c2 00 f9` | str x8,[x21, #0x180] | `FALL_THROUGH`
<a id="insn-00b1d2b8"></a> `00b1d2b8` | `57 01 00 b4` | cbz x23,0x00b1d2e0 | `CONDITIONAL_JUMP`
<a id="insn-00b1d2bc"></a> `00b1d2bc` | `ff 06 00 f1` | cmp x23,#0x1 | `FALL_THROUGH`
<a id="insn-00b1d2c0"></a> `00b1d2c0` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00b1d2c4"></a> `00b1d2c4` | `e0 00 00 54` | b.eq 0x00b1d2e0 | `CONDITIONAL_JUMP`
<a id="insn-00b1d2c8"></a> `00b1d2c8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b1d2cc"></a> `00b1d2cc` | `a9 c2 40 f9` | ldr x9,[x21, #0x180] | `FALL_THROUGH`
<a id="insn-00b1d2d0"></a> `00b1d2d0` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00b1d2d4"></a> `00b1d2d4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b1d2d8"></a> `00b1d2d8` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00b1d2dc"></a> `00b1d2dc` | `81 ff ff 54` | b.ne 0x00b1d2cc | `CONDITIONAL_JUMP`
<a id="insn-00b1d2e0"></a> `00b1d2e0` | `e8 97 41 f9` | ldr x8,[sp, #0x328] | `FALL_THROUGH`
<a id="insn-00b1d2e4"></a> `00b1d2e4` | `f8 9f 41 f9` | ldr x24,[sp, #0x338] | `FALL_THROUGH`
<a id="insn-00b1d2e8"></a> `00b1d2e8` | `e9 9b 41 f9` | ldr x9,[sp, #0x330] | `FALL_THROUGH`
<a id="insn-00b1d2ec"></a> `00b1d2ec` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00b1d2f0"></a> `00b1d2f0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b1d2f4"></a> `00b1d2f4` | `08 01 18 cb` | sub x8,x8,x24 | `FALL_THROUGH`
<a id="insn-00b1d2f8"></a> `00b1d2f8` | `17 01 09 8b` | add x23,x8,x9 | `FALL_THROUGH`
<a id="insn-00b1d2fc"></a> `00b1d2fc` | `f9 7e 40 92` | and x25,x23,#0xffffffff | `FALL_THROUGH`
<a id="insn-00b1d300"></a> `00b1d300` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00b1d304"></a> `00b1d304` | `2f 08 03 94` | bl 0x00bdf3c0 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d308"></a> `00b1d308` | `d9 01 00 b4` | cbz x25,0x00b1d340 | `CONDITIONAL_JUMP`
<a id="insn-00b1d30c"></a> `00b1d30c` | `a8 26 58 a9` | ldp x8,x9,[x21, #0x180] | `FALL_THROUGH`
<a id="insn-00b1d310"></a> `00b1d310` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00b1d314"></a> `00b1d314` | `3f 01 19 eb` | cmp x9,x25 | `FALL_THROUGH`
<a id="insn-00b1d318"></a> `00b1d318` | `a2 00 00 54` | b.cs 0x00b1d32c | `CONDITIONAL_JUMP`
<a id="insn-00b1d31c"></a> `00b1d31c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b1d320"></a> `00b1d320` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00b1d324"></a> `00b1d324` | `db 07 03 94` | bl 0x00bdf290 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d328"></a> `00b1d328` | `a8 c2 40 f9` | ldr x8,[x21, #0x180] | `FALL_THROUGH`
<a id="insn-00b1d32c"></a> `00b1d32c` | `00 01 19 cb` | sub x0,x8,x25 | `FALL_THROUGH`
<a id="insn-00b1d330"></a> `00b1d330` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00b1d334"></a> `00b1d334` | `e2 03 19 aa` | mov x2,x25 | `FALL_THROUGH`
<a id="insn-00b1d338"></a> `00b1d338` | `a0 c2 00 f9` | str x0,[x21, #0x180] | `FALL_THROUGH`
<a id="insn-00b1d33c"></a> `00b1d33c` | `5d f7 02 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d340"></a> `00b1d340` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b1d344"></a> `00b1d344` | `e1 03 17 2a` | mov w1,w23 | `FALL_THROUGH`
<a id="insn-00b1d348"></a> `00b1d348` | `bf 5a 06 39` | strb wzr,[x21, #0x196] | `FALL_THROUGH`
<a id="insn-00b1d34c"></a> `00b1d34c` | `0d 08 03 94` | bl 0x00bdf380 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d350"></a> `00b1d350` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b1d354"></a> `00b1d354` | `57 07 03 94` | bl 0x00bdf0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d358"></a> `00b1d358` | `f4 03 40 f9` | ldr x20,[sp] | `FALL_THROUGH`
<a id="insn-00b1d35c"></a> `00b1d35c` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00b1d360"></a> `00b1d360` | `a8 0e 42 38` | ldrb w8,[x21, #0x20]! | `FALL_THROUGH`
<a id="insn-00b1d364"></a> `00b1d364` | `68 00 00 37` | tbnz w8,#0x0,0x00b1d370 | `CONDITIONAL_JUMP`
<a id="insn-00b1d368"></a> `00b1d368` | `bf 02 00 79` | strh wzr,[x21] | `FALL_THROUGH`
<a id="insn-00b1d36c"></a> `00b1d36c` | `09 00 00 14` | b 0x00b1d390 | `UNCONDITIONAL_JUMP`
<a id="insn-00b1d370"></a> `00b1d370` | `88 1a 40 f9` | ldr x8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00b1d374"></a> `00b1d374` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00b1d378"></a> `00b1d378` | `88 82 40 39` | ldrb w8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00b1d37c"></a> `00b1d37c` | `9f 16 00 f9` | str xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b1d380"></a> `00b1d380` | `88 00 00 36` | tbz w8,#0x0,0x00b1d390 | `CONDITIONAL_JUMP`
<a id="insn-00b1d384"></a> `00b1d384` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00b1d388"></a> `00b1d388` | `f6 f6 02 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d38c"></a> `00b1d38c` | `9f 12 00 f9` | str xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00b1d390"></a> `00b1d390` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b1d394"></a> `00b1d394` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b1d398"></a> `00b1d398` | `f4 03 1f 2a` | mov w20,wzr | `FALL_THROUGH`
<a id="insn-00b1d39c"></a> `00b1d39c` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00b1d3a0"></a> `00b1d3a0` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00b1d3a4"></a> `00b1d3a4` | `e0 e3 06 91` | add x0,sp,#0x1b8 | `FALL_THROUGH`
<a id="insn-00b1d3a8"></a> `00b1d3a8` | `76 05 03 94` | bl 0x00bde980 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d3ac"></a> `00b1d3ac` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b1d3b0"></a> `00b1d3b0` | `68 00 00 36` | tbz w8,#0x0,0x00b1d3bc | `CONDITIONAL_JUMP`
<a id="insn-00b1d3b4"></a> `00b1d3b4` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b1d3b8"></a> `00b1d3b8` | `ea f6 02 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b1d3bc"></a> `00b1d3bc` | `54 00 00 35` | cbnz w20,0x00b1d3c4 | `CONDITIONAL_JUMP`
<a id="insn-00b1d3c0"></a> `00b1d3c0` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-00b1d3c4"></a> `00b1d3c4` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00b1d3c8"></a> `00b1d3c8` | `a9 03 5a f8` | ldur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b1d3cc"></a> `00b1d3cc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b1d3d0"></a> `00b1d3d0` | `21 01 00 54` | b.ne 0x00b1d3f4 | `CONDITIONAL_JUMP`
<a id="insn-00b1d3d4"></a> `00b1d3d4` | `ff 03 1a 91` | add sp,sp,#0x680 | `FALL_THROUGH`
<a id="insn-00b1d3d8"></a> `00b1d3d8` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b1d3dc"></a> `00b1d3dc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b1d3e0"></a> `00b1d3e0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b1d3e4"></a> `00b1d3e4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b1d3e8"></a> `00b1d3e8` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b1d3ec"></a> `00b1d3ec` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00b1d3f0"></a> `00b1d3f0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b1d3f4"></a> `00b1d3f4` | `e7 f6 02 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`
<a id="insn-00b1d3f8"></a> `00b1d3f8` | `72 03 03 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b1cedc`](#insn-00b1cedc) 範囲 `[['00b1cedc', '00b1cf23']]`
  - `CONDITIONAL_JUMP` [`00b1cf20`](#insn-00b1cf20) → [`00b1cf54`](#insn-00b1cf54)
  - `FALL_THROUGH` [`00b1cf20`](#insn-00b1cf20) → [`00b1cf24`](#insn-00b1cf24)
- ブロック [`00b1cf24`](#insn-00b1cf24) 範囲 `[['00b1cf24', '00b1cf4f']]`
  - `CONDITIONAL_JUMP` [`00b1cf4c`](#insn-00b1cf4c) → [`00b1d3c4`](#insn-00b1d3c4)
  - `FALL_THROUGH` [`00b1cf4c`](#insn-00b1cf4c) → [`00b1cf50`](#insn-00b1cf50)
- ブロック [`00b1cf50`](#insn-00b1cf50) 範囲 `[['00b1cf50', '00b1cf53']]`
  - `UNCONDITIONAL_JUMP` [`00b1cf50`](#insn-00b1cf50) → [`00b1d3c0`](#insn-00b1d3c0)
- ブロック [`00b1cf54`](#insn-00b1cf54) 範囲 `[['00b1cf54', '00b1cf73']]`
  - `CONDITIONAL_JUMP` [`00b1cf70`](#insn-00b1cf70) → [`00b1d3c4`](#insn-00b1d3c4)
  - `FALL_THROUGH` [`00b1cf70`](#insn-00b1cf70) → [`00b1cf74`](#insn-00b1cf74)
- ブロック [`00b1cf74`](#insn-00b1cf74) 範囲 `[['00b1cf74', '00b1cf93']]`
  - `CONDITIONAL_JUMP` [`00b1cf90`](#insn-00b1cf90) → [`00b1d3f8`](#insn-00b1d3f8)
  - `FALL_THROUGH` [`00b1cf90`](#insn-00b1cf90) → [`00b1cf94`](#insn-00b1cf94)
- ブロック [`00b1cf94`](#insn-00b1cf94) 範囲 `[['00b1cf94', '00b1cf9f']]`
  - `CONDITIONAL_JUMP` [`00b1cf9c`](#insn-00b1cf9c) → [`00b1cfb4`](#insn-00b1cfb4)
  - `FALL_THROUGH` [`00b1cf9c`](#insn-00b1cf9c) → [`00b1cfa0`](#insn-00b1cfa0)
- ブロック [`00b1cfa0`](#insn-00b1cfa0) 範囲 `[['00b1cfa0', '00b1cfb3']]`
  - `UNCONDITIONAL_JUMP` [`00b1cfb0`](#insn-00b1cfb0) → [`00b1cfd0`](#insn-00b1cfd0)
- ブロック [`00b1cfb4`](#insn-00b1cfb4) 範囲 `[['00b1cfb4', '00b1cfcf']]`
  - `FALL_THROUGH` [`00b1cfcc`](#insn-00b1cfcc) → [`00b1cfd0`](#insn-00b1cfd0)
- ブロック [`00b1cfd0`](#insn-00b1cfd0) 範囲 `[['00b1cfd0', '00b1cfdb']]`
  - `CONDITIONAL_JUMP` [`00b1cfd8`](#insn-00b1cfd8) → [`00b1d044`](#insn-00b1d044)
  - `FALL_THROUGH` [`00b1cfd8`](#insn-00b1cfd8) → [`00b1cfdc`](#insn-00b1cfdc)
- ブロック [`00b1cfdc`](#insn-00b1cfdc) 範囲 `[['00b1cfdc', '00b1cfe7']]`
  - `CONDITIONAL_JUMP` [`00b1cfe4`](#insn-00b1cfe4) → [`00b1d034`](#insn-00b1d034)
  - `FALL_THROUGH` [`00b1cfe4`](#insn-00b1cfe4) → [`00b1cfe8`](#insn-00b1cfe8)
- ブロック [`00b1cfe8`](#insn-00b1cfe8) 範囲 `[['00b1cfe8', '00b1cfef']]`
  - `CONDITIONAL_JUMP` [`00b1cfec`](#insn-00b1cfec) → [`00b1cffc`](#insn-00b1cffc)
  - `FALL_THROUGH` [`00b1cfec`](#insn-00b1cfec) → [`00b1cff0`](#insn-00b1cff0)
- ブロック [`00b1cff0`](#insn-00b1cff0) 範囲 `[['00b1cff0', '00b1cffb']]`
  - `CONDITIONAL_JUMP` [`00b1cff8`](#insn-00b1cff8) → [`00b1d034`](#insn-00b1d034)
  - `FALL_THROUGH` [`00b1cff8`](#insn-00b1cff8) → [`00b1cffc`](#insn-00b1cffc)
- ブロック [`00b1cffc`](#insn-00b1cffc) 範囲 `[['00b1cffc', '00b1d013']]`
  - `FALL_THROUGH` [`00b1d010`](#insn-00b1d010) → [`00b1d014`](#insn-00b1d014)
- ブロック [`00b1d014`](#insn-00b1d014) 範囲 `[['00b1d014', '00b1d02b']]`
  - `CONDITIONAL_JUMP` [`00b1d028`](#insn-00b1d028) → [`00b1d014`](#insn-00b1d014)
  - `FALL_THROUGH` [`00b1d028`](#insn-00b1d028) → [`00b1d02c`](#insn-00b1d02c)
- ブロック [`00b1d02c`](#insn-00b1d02c) 範囲 `[['00b1d02c', '00b1d033']]`
  - `CONDITIONAL_JUMP` [`00b1d030`](#insn-00b1d030) → [`00b1d044`](#insn-00b1d044)
  - `FALL_THROUGH` [`00b1d030`](#insn-00b1d030) → [`00b1d034`](#insn-00b1d034)
- ブロック [`00b1d034`](#insn-00b1d034) 範囲 `[['00b1d034', '00b1d043']]`
  - `CONDITIONAL_JUMP` [`00b1d040`](#insn-00b1d040) → [`00b1d034`](#insn-00b1d034)
  - `FALL_THROUGH` [`00b1d040`](#insn-00b1d040) → [`00b1d044`](#insn-00b1d044)
- ブロック [`00b1d044`](#insn-00b1d044) 範囲 `[['00b1d044', '00b1d16f']]`
  - `CONDITIONAL_JUMP` [`00b1d16c`](#insn-00b1d16c) → [`00b1d18c`](#insn-00b1d18c)
  - `FALL_THROUGH` [`00b1d16c`](#insn-00b1d16c) → [`00b1d170`](#insn-00b1d170)
- ブロック [`00b1d170`](#insn-00b1d170) 範囲 `[['00b1d170', '00b1d18b']]`
  - `FALL_THROUGH` [`00b1d188`](#insn-00b1d188) → [`00b1d18c`](#insn-00b1d18c)
- ブロック [`00b1d18c`](#insn-00b1d18c) 範囲 `[['00b1d18c', '00b1d1f3']]`
  - `CONDITIONAL_JUMP` [`00b1d1f0`](#insn-00b1d1f0) → [`00b1d26c`](#insn-00b1d26c)
  - `FALL_THROUGH` [`00b1d1f0`](#insn-00b1d1f0) → [`00b1d1f4`](#insn-00b1d1f4)
- ブロック [`00b1d1f4`](#insn-00b1d1f4) 範囲 `[['00b1d1f4', '00b1d21b']]`
  - `CONDITIONAL_JUMP` [`00b1d218`](#insn-00b1d218) → [`00b1d220`](#insn-00b1d220)
  - `FALL_THROUGH` [`00b1d218`](#insn-00b1d218) → [`00b1d21c`](#insn-00b1d21c)
- ブロック [`00b1d21c`](#insn-00b1d21c) 範囲 `[['00b1d21c', '00b1d21f']]`
  - `FALL_THROUGH` [`00b1d21c`](#insn-00b1d21c) → [`00b1d220`](#insn-00b1d220)
- ブロック [`00b1d220`](#insn-00b1d220) 範囲 `[['00b1d220', '00b1d24f']]`
  - `CONDITIONAL_JUMP` [`00b1d24c`](#insn-00b1d24c) → [`00b1d2b0`](#insn-00b1d2b0)
  - `FALL_THROUGH` [`00b1d24c`](#insn-00b1d24c) → [`00b1d250`](#insn-00b1d250)
- ブロック [`00b1d250`](#insn-00b1d250) 範囲 `[['00b1d250', '00b1d26b']]`
  - `UNCONDITIONAL_JUMP` [`00b1d268`](#insn-00b1d268) → [`00b1d2bc`](#insn-00b1d2bc)
- ブロック [`00b1d26c`](#insn-00b1d26c) 範囲 `[['00b1d26c', '00b1d297']]`
  - `CONDITIONAL_JUMP` [`00b1d294`](#insn-00b1d294) → [`00b1d2a0`](#insn-00b1d2a0)
  - `FALL_THROUGH` [`00b1d294`](#insn-00b1d294) → [`00b1d298`](#insn-00b1d298)
- ブロック [`00b1d298`](#insn-00b1d298) 範囲 `[['00b1d298', '00b1d29f']]`
  - `FALL_THROUGH` [`00b1d29c`](#insn-00b1d29c) → [`00b1d2a0`](#insn-00b1d2a0)
- ブロック [`00b1d2a0`](#insn-00b1d2a0) 範囲 `[['00b1d2a0', '00b1d2af']]`
  - `UNCONDITIONAL_JUMP` [`00b1d2ac`](#insn-00b1d2ac) → [`00b1d3a4`](#insn-00b1d3a4)
- ブロック [`00b1d2b0`](#insn-00b1d2b0) 範囲 `[['00b1d2b0', '00b1d2bb']]`
  - `CONDITIONAL_JUMP` [`00b1d2b8`](#insn-00b1d2b8) → [`00b1d2e0`](#insn-00b1d2e0)
  - `FALL_THROUGH` [`00b1d2b8`](#insn-00b1d2b8) → [`00b1d2bc`](#insn-00b1d2bc)
- ブロック [`00b1d2bc`](#insn-00b1d2bc) 範囲 `[['00b1d2bc', '00b1d2c7']]`
  - `CONDITIONAL_JUMP` [`00b1d2c4`](#insn-00b1d2c4) → [`00b1d2e0`](#insn-00b1d2e0)
  - `FALL_THROUGH` [`00b1d2c4`](#insn-00b1d2c4) → [`00b1d2c8`](#insn-00b1d2c8)
- ブロック [`00b1d2c8`](#insn-00b1d2c8) 範囲 `[['00b1d2c8', '00b1d2cb']]`
  - `FALL_THROUGH` [`00b1d2c8`](#insn-00b1d2c8) → [`00b1d2cc`](#insn-00b1d2cc)
- ブロック [`00b1d2cc`](#insn-00b1d2cc) 範囲 `[['00b1d2cc', '00b1d2df']]`
  - `CONDITIONAL_JUMP` [`00b1d2dc`](#insn-00b1d2dc) → [`00b1d2cc`](#insn-00b1d2cc)
  - `FALL_THROUGH` [`00b1d2dc`](#insn-00b1d2dc) → [`00b1d2e0`](#insn-00b1d2e0)
- ブロック [`00b1d2e0`](#insn-00b1d2e0) 範囲 `[['00b1d2e0', '00b1d30b']]`
  - `CONDITIONAL_JUMP` [`00b1d308`](#insn-00b1d308) → [`00b1d340`](#insn-00b1d340)
  - `FALL_THROUGH` [`00b1d308`](#insn-00b1d308) → [`00b1d30c`](#insn-00b1d30c)
- ブロック [`00b1d30c`](#insn-00b1d30c) 範囲 `[['00b1d30c', '00b1d31b']]`
  - `CONDITIONAL_JUMP` [`00b1d318`](#insn-00b1d318) → [`00b1d32c`](#insn-00b1d32c)
  - `FALL_THROUGH` [`00b1d318`](#insn-00b1d318) → [`00b1d31c`](#insn-00b1d31c)
- ブロック [`00b1d31c`](#insn-00b1d31c) 範囲 `[['00b1d31c', '00b1d32b']]`
  - `FALL_THROUGH` [`00b1d328`](#insn-00b1d328) → [`00b1d32c`](#insn-00b1d32c)
- ブロック [`00b1d32c`](#insn-00b1d32c) 範囲 `[['00b1d32c', '00b1d33f']]`
  - `FALL_THROUGH` [`00b1d33c`](#insn-00b1d33c) → [`00b1d340`](#insn-00b1d340)
- ブロック [`00b1d340`](#insn-00b1d340) 範囲 `[['00b1d340', '00b1d367']]`
  - `CONDITIONAL_JUMP` [`00b1d364`](#insn-00b1d364) → [`00b1d370`](#insn-00b1d370)
  - `FALL_THROUGH` [`00b1d364`](#insn-00b1d364) → [`00b1d368`](#insn-00b1d368)
- ブロック [`00b1d368`](#insn-00b1d368) 範囲 `[['00b1d368', '00b1d36f']]`
  - `UNCONDITIONAL_JUMP` [`00b1d36c`](#insn-00b1d36c) → [`00b1d390`](#insn-00b1d390)
- ブロック [`00b1d370`](#insn-00b1d370) 範囲 `[['00b1d370', '00b1d383']]`
  - `CONDITIONAL_JUMP` [`00b1d380`](#insn-00b1d380) → [`00b1d390`](#insn-00b1d390)
  - `FALL_THROUGH` [`00b1d380`](#insn-00b1d380) → [`00b1d384`](#insn-00b1d384)
- ブロック [`00b1d384`](#insn-00b1d384) 範囲 `[['00b1d384', '00b1d38f']]`
  - `FALL_THROUGH` [`00b1d38c`](#insn-00b1d38c) → [`00b1d390`](#insn-00b1d390)
- ブロック [`00b1d390`](#insn-00b1d390) 範囲 `[['00b1d390', '00b1d3a3']]`
  - `FALL_THROUGH` [`00b1d3a0`](#insn-00b1d3a0) → [`00b1d3a4`](#insn-00b1d3a4)
- ブロック [`00b1d3a4`](#insn-00b1d3a4) 範囲 `[['00b1d3a4', '00b1d3b3']]`
  - `CONDITIONAL_JUMP` [`00b1d3b0`](#insn-00b1d3b0) → [`00b1d3bc`](#insn-00b1d3bc)
  - `FALL_THROUGH` [`00b1d3b0`](#insn-00b1d3b0) → [`00b1d3b4`](#insn-00b1d3b4)
- ブロック [`00b1d3b4`](#insn-00b1d3b4) 範囲 `[['00b1d3b4', '00b1d3bb']]`
  - `FALL_THROUGH` [`00b1d3b8`](#insn-00b1d3b8) → [`00b1d3bc`](#insn-00b1d3bc)
- ブロック [`00b1d3bc`](#insn-00b1d3bc) 範囲 `[['00b1d3bc', '00b1d3bf']]`
  - `CONDITIONAL_JUMP` [`00b1d3bc`](#insn-00b1d3bc) → [`00b1d3c4`](#insn-00b1d3c4)
  - `FALL_THROUGH` [`00b1d3bc`](#insn-00b1d3bc) → [`00b1d3c0`](#insn-00b1d3c0)
- ブロック [`00b1d3c0`](#insn-00b1d3c0) 範囲 `[['00b1d3c0', '00b1d3c3']]`
  - `FALL_THROUGH` [`00b1d3c0`](#insn-00b1d3c0) → [`00b1d3c4`](#insn-00b1d3c4)
- ブロック [`00b1d3c4`](#insn-00b1d3c4) 範囲 `[['00b1d3c4', '00b1d3d3']]`
  - `CONDITIONAL_JUMP` [`00b1d3d0`](#insn-00b1d3d0) → [`00b1d3f4`](#insn-00b1d3f4)
  - `FALL_THROUGH` [`00b1d3d0`](#insn-00b1d3d0) → [`00b1d3d4`](#insn-00b1d3d4)
- ブロック [`00b1d3d4`](#insn-00b1d3d4) 範囲 `[['00b1d3d4', '00b1d3f3']]`
- ブロック [`00b1d3f4`](#insn-00b1d3f4) 範囲 `[['00b1d3f4', '00b1d3f7']]`
- ブロック [`00b1d3f8`](#insn-00b1d3f8) 範囲 `[['00b1d3f8', '00b1d3fb']]`

## 命令位置別の参照

- [`00b1cedc`](#insn-00b1cedc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cee0`](#insn-00b1cee0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cee4`](#insn-00b1cee4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cee8`](#insn-00b1cee8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1ceec`](#insn-00b1ceec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cef0`](#insn-00b1cef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf10`](#insn-00b1cf10) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf20`](#insn-00b1cf20) → [`00b1cf54`](#insn-00b1cf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf3c`](#insn-00b1cf3c) → [`00bdf700`](../00bdf/00bdf700.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf700` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf4c`](#insn-00b1cf4c) → [`00b1d3c4`](#insn-00b1d3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf50`](#insn-00b1cf50) → [`00b1d3c0`](#insn-00b1d3c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf60`](#insn-00b1cf60) → [`00bdf800`](../00bdf/00bdf800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf800` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf70`](#insn-00b1cf70) → [`00b1d3c4`](#insn-00b1d3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf7c`](#insn-00b1cf7c) → `Stack[-0x6d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf80`](#insn-00b1cf80) → `Stack[-0x6d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf90`](#insn-00b1cf90) → [`00b1d3f8`](#insn-00b1d3f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf98`](#insn-00b1cf98) → `Stack[-0x6e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cf9c`](#insn-00b1cf9c) → [`00b1cfb4`](#insn-00b1cfb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cfa8`](#insn-00b1cfa8) → `Stack[-0x6d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cfb0`](#insn-00b1cfb0) → [`00b1cfd0`](#insn-00b1cfd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cfc0`](#insn-00b1cfc0) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00b1cfc8`](#insn-00b1cfc8) → `Stack[-0x6d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cfcc`](#insn-00b1cfcc) → `Stack[-0x6c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cfd8`](#insn-00b1cfd8) → [`00b1d044`](#insn-00b1d044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cfe4`](#insn-00b1cfe4) → [`00b1d034`](#insn-00b1d034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cfec`](#insn-00b1cfec) → [`00b1cffc`](#insn-00b1cffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1cff8`](#insn-00b1cff8) → [`00b1d034`](#insn-00b1d034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d028`](#insn-00b1d028) → [`00b1d014`](#insn-00b1d014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d030`](#insn-00b1d030) → [`00b1d044`](#insn-00b1d044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d040`](#insn-00b1d040) → [`00b1d034`](#insn-00b1d034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d050`](#insn-00b1d050) → `Stack[-0x6b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d060`](#insn-00b1d060) → `Stack[-0x6a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d064`](#insn-00b1d064) → `Stack[-0x6a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d068`](#insn-00b1d068) → `00298725`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1d06c`](#insn-00b1d06c) → `0029872c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1d074`](#insn-00b1d074) → `Stack[-0x6bc]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d078`](#insn-00b1d078) → `Stack[-0x69f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d080`](#insn-00b1d080) → `Stack[-0x6c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d084`](#insn-00b1d084) → `Stack[-0x6a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d088`](#insn-00b1d088) → `Stack[-0x690]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d08c`](#insn-00b1d08c) → `Stack[-0x690]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d090`](#insn-00b1d090) → `Stack[-0x670]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d094`](#insn-00b1d094) → `Stack[-0x680]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d098`](#insn-00b1d098) → `Stack[-0x698]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0a0`](#insn-00b1d0a0) → `Stack[-0x648]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0a4`](#insn-00b1d0a4) → `Stack[-0x658]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0a8`](#insn-00b1d0a8) → `Stack[-0x650]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0b0`](#insn-00b1d0b0) → `Stack[-0x668]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0b4`](#insn-00b1d0b4) → `Stack[-0x64e]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0b8`](#insn-00b1d0b8) → `Stack[-0x638]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0bc`](#insn-00b1d0bc) → `Stack[-0x636]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0c0`](#insn-00b1d0c0) → `Stack[-0x630]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0c4`](#insn-00b1d0c4) → `Stack[-0x61b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0c8`](#insn-00b1d0c8) → `Stack[-0x620]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0cc`](#insn-00b1d0cc) → `Stack[-0x600]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0d0`](#insn-00b1d0d0) → `Stack[-0x610]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0d4`](#insn-00b1d0d4) → `Stack[-0x5e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0dc`](#insn-00b1d0dc) → `Stack[-0x5c1]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0e4`](#insn-00b1d0e4) → `Stack[-0x5d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0e8`](#insn-00b1d0e8) → `Stack[-0x5c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0ec`](#insn-00b1d0ec) → `Stack[-0x578]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0f0`](#insn-00b1d0f0) → `Stack[-0x598]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0f4`](#insn-00b1d0f4) → `Stack[-0x5b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d0fc`](#insn-00b1d0fc) → `Stack[-0x570]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d104`](#insn-00b1d104) → `Stack[-0x567]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d114`](#insn-00b1d114) → `002ac2f1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1d118`](#insn-00b1d118) → `002b2820`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b1d130`](#insn-00b1d130) → `Stack[-0x56f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d134`](#insn-00b1d134) → `Stack[-0x565]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d138`](#insn-00b1d138) → `Stack[-0x550]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d13c`](#insn-00b1d13c) → `Stack[-0x558]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d140`](#insn-00b1d140) → `Stack[-0x540]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d144`](#insn-00b1d144) → `Stack[-0x538]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d148`](#insn-00b1d148) → `Stack[-0x530]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d150`](#insn-00b1d150) → [`00bde970`](../00bde/00bde970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde970` · 推定シンボル `None` · 推定型 `None`
- [`00b1d158`](#insn-00b1d158) → [`00bde910`](../00bde/00bde910.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde910` · 推定シンボル `None` · 推定型 `None`
- [`00b1d168`](#insn-00b1d168) → `Stack[-0x2e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d16c`](#insn-00b1d16c) → [`00b1d18c`](#insn-00b1d18c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d17c`](#insn-00b1d17c) → [`00bdfe60`](../00bdf/00bdfe60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdfe60` · 推定シンボル `None` · 推定型 `None`
- [`00b1d188`](#insn-00b1d188) → [`00bdffc0`](../00bdf/00bdffc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdffc0` · 推定シンボル `None` · 推定型 `None`
- [`00b1d194`](#insn-00b1d194) → [`00bdf060`](../00bdf/00bdf060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf060` · 推定シンボル `None` · 推定型 `None`
- [`00b1d198`](#insn-00b1d198) → `Stack[-0x6d8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d19c`](#insn-00b1d19c) → `Stack[-0x6c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1c0`](#insn-00b1d1c0) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1c4`](#insn-00b1d1c4) → [`00bdef60`](../00bde/00bdef60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdef60` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1c8`](#insn-00b1d1c8) → `Stack[-0x470]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1d8`](#insn-00b1d1d8) → [`00bdeab0`](../00bde/00bdeab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdeab0` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1dc`](#insn-00b1d1dc) → `Stack[-0x460]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1e0`](#insn-00b1d1e0) → `Stack[-0x470]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1e4`](#insn-00b1d1e4) → `Stack[-0x478]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1e8`](#insn-00b1d1e8) → `Stack[-0x468]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1ec`](#insn-00b1d1ec) → `Stack[-0x458]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1f0`](#insn-00b1d1f0) → [`00b1d26c`](#insn-00b1d26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1f4`](#insn-00b1d1f4) → `Stack[-0x3b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1f8`](#insn-00b1d1f8) → `Stack[-0x3a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d1fc`](#insn-00b1d1fc) → `Stack[-0x390]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d204`](#insn-00b1d204) → `Stack[-0x3b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d218`](#insn-00b1d218) → [`00b1d220`](#insn-00b1d220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d24c`](#insn-00b1d24c) → [`00b1d2b0`](#insn-00b1d2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d258`](#insn-00b1d258) → [`00bdf290`](../00bdf/00bdf290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf290` · 推定シンボル `None` · 推定型 `None`
- [`00b1d268`](#insn-00b1d268) → [`00b1d2bc`](#insn-00b1d2bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d278`](#insn-00b1d278) → `00291545`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b1d280`](#insn-00b1d280) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00b1d28c`](#insn-00b1d28c) → [`00bdf8d0`](../00bdf/00bdf8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf8d0` · 推定シンボル `None` · 推定型 `None`
- [`00b1d290`](#insn-00b1d290) → `Stack[-0x6c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d294`](#insn-00b1d294) → [`00b1d2a0`](#insn-00b1d2a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d298`](#insn-00b1d298) → `Stack[-0x6b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d29c`](#insn-00b1d29c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b1d2ac`](#insn-00b1d2ac) → [`00b1d3a4`](#insn-00b1d3a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d2b8`](#insn-00b1d2b8) → [`00b1d2e0`](#insn-00b1d2e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d2c4`](#insn-00b1d2c4) → [`00b1d2e0`](#insn-00b1d2e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d2dc`](#insn-00b1d2dc) → [`00b1d2cc`](#insn-00b1d2cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d2e0`](#insn-00b1d2e0) → `Stack[-0x3b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d2e4`](#insn-00b1d2e4) → `Stack[-0x3a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d2e8`](#insn-00b1d2e8) → `Stack[-0x3b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d304`](#insn-00b1d304) → [`00bdf3c0`](../00bdf/00bdf3c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf3c0` · 推定シンボル `None` · 推定型 `None`
- [`00b1d308`](#insn-00b1d308) → [`00b1d340`](#insn-00b1d340) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d318`](#insn-00b1d318) → [`00b1d32c`](#insn-00b1d32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d324`](#insn-00b1d324) → [`00bdf290`](../00bdf/00bdf290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf290` · 推定シンボル `None` · 推定型 `None`
- [`00b1d33c`](#insn-00b1d33c) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00b1d34c`](#insn-00b1d34c) → [`00bdf380`](../00bdf/00bdf380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf380` · 推定シンボル `None` · 推定型 `None`
- [`00b1d354`](#insn-00b1d354) → [`00bdf0b0`](../00bdf/00bdf0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf0b0` · 推定シンボル `None` · 推定型 `None`
- [`00b1d358`](#insn-00b1d358) → `Stack[-0x6e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d364`](#insn-00b1d364) → [`00b1d370`](#insn-00b1d370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d36c`](#insn-00b1d36c) → [`00b1d390`](#insn-00b1d390) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d380`](#insn-00b1d380) → [`00b1d390`](#insn-00b1d390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d388`](#insn-00b1d388) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b1d390`](#insn-00b1d390) → `Stack[-0x6b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d394`](#insn-00b1d394) → `Stack[-0x6c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3a8`](#insn-00b1d3a8) → [`00bde980`](../00bde/00bde980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde980` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3ac`](#insn-00b1d3ac) → `Stack[-0x6d8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3b0`](#insn-00b1d3b0) → [`00b1d3bc`](#insn-00b1d3bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3b4`](#insn-00b1d3b4) → `Stack[-0x6c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3b8`](#insn-00b1d3b8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3bc`](#insn-00b1d3bc) → [`00b1d3c4`](#insn-00b1d3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3c8`](#insn-00b1d3c8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3d0`](#insn-00b1d3d0) → [`00b1d3f4`](#insn-00b1d3f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3d8`](#insn-00b1d3d8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3dc`](#insn-00b1d3dc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3e0`](#insn-00b1d3e0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3e4`](#insn-00b1d3e4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3e8`](#insn-00b1d3e8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3f4`](#insn-00b1d3f4) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`00b1d3f8`](#insn-00b1d3f8) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b1cedc`](#insn-00b1cedc)

~~~json
{
  "source": "00b1cedc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cee0`](#insn-00b1cee0)

~~~json
{
  "source": "00b1cee0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cee4`](#insn-00b1cee4)

~~~json
{
  "source": "00b1cee4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cee8`](#insn-00b1cee8)

~~~json
{
  "source": "00b1cee8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1ceec`](#insn-00b1ceec)

~~~json
{
  "source": "00b1ceec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cef0`](#insn-00b1cef0)

~~~json
{
  "source": "00b1cef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cf10`](#insn-00b1cf10)

~~~json
{
  "source": "00b1cf10",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cf20`](#insn-00b1cf20)

~~~json
{
  "source": "00b1cf20",
  "target": "00b1cf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cf3c`](#insn-00b1cf3c)

~~~json
{
  "source": "00b1cf3c",
  "target": "00bdf700",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1cf4c`](#insn-00b1cf4c)

~~~json
{
  "source": "00b1cf4c",
  "target": "00b1d3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cf50`](#insn-00b1cf50)

~~~json
{
  "source": "00b1cf50",
  "target": "00b1d3c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cf60`](#insn-00b1cf60)

~~~json
{
  "source": "00b1cf60",
  "target": "00bdf800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1cf70`](#insn-00b1cf70)

~~~json
{
  "source": "00b1cf70",
  "target": "00b1d3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cf7c`](#insn-00b1cf7c)

~~~json
{
  "source": "00b1cf7c",
  "target": "Stack[-0x6d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cf80`](#insn-00b1cf80)

~~~json
{
  "source": "00b1cf80",
  "target": "Stack[-0x6d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cf90`](#insn-00b1cf90)

~~~json
{
  "source": "00b1cf90",
  "target": "00b1d3f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cf98`](#insn-00b1cf98)

~~~json
{
  "source": "00b1cf98",
  "target": "Stack[-0x6e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cf9c`](#insn-00b1cf9c)

~~~json
{
  "source": "00b1cf9c",
  "target": "00b1cfb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cfa8`](#insn-00b1cfa8)

~~~json
{
  "source": "00b1cfa8",
  "target": "Stack[-0x6d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cfb0`](#insn-00b1cfb0)

~~~json
{
  "source": "00b1cfb0",
  "target": "00b1cfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cfc0`](#insn-00b1cfc0)

~~~json
{
  "source": "00b1cfc0",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1cfc8`](#insn-00b1cfc8)

~~~json
{
  "source": "00b1cfc8",
  "target": "Stack[-0x6d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cfcc`](#insn-00b1cfcc)

~~~json
{
  "source": "00b1cfcc",
  "target": "Stack[-0x6c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cfd8`](#insn-00b1cfd8)

~~~json
{
  "source": "00b1cfd8",
  "target": "00b1d044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cfe4`](#insn-00b1cfe4)

~~~json
{
  "source": "00b1cfe4",
  "target": "00b1d034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cfec`](#insn-00b1cfec)

~~~json
{
  "source": "00b1cfec",
  "target": "00b1cffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1cff8`](#insn-00b1cff8)

~~~json
{
  "source": "00b1cff8",
  "target": "00b1d034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d028`](#insn-00b1d028)

~~~json
{
  "source": "00b1d028",
  "target": "00b1d014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d030`](#insn-00b1d030)

~~~json
{
  "source": "00b1d030",
  "target": "00b1d044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d040`](#insn-00b1d040)

~~~json
{
  "source": "00b1d040",
  "target": "00b1d034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d050`](#insn-00b1d050)

~~~json
{
  "source": "00b1d050",
  "target": "Stack[-0x6b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d060`](#insn-00b1d060)

~~~json
{
  "source": "00b1d060",
  "target": "Stack[-0x6a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d064`](#insn-00b1d064)

~~~json
{
  "source": "00b1d064",
  "target": "Stack[-0x6a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d068`](#insn-00b1d068)

~~~json
{
  "source": "00b1d068",
  "target": "00298725",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298725",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "7374643a3a756e697175655f70747200",
  "capture_start": "00298725",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1d06c`](#insn-00b1d06c)

~~~json
{
  "source": "00b1d06c",
  "target": "0029872c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298725",
  "offset": 7,
  "size": 16,
  "datatype": "string",
  "bytes": "7374643a3a756e697175655f70747200",
  "capture_start": "00298725",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1d074`](#insn-00b1d074)

~~~json
{
  "source": "00b1d074",
  "target": "Stack[-0x6bc]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d078`](#insn-00b1d078)

~~~json
{
  "source": "00b1d078",
  "target": "Stack[-0x69f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d080`](#insn-00b1d080)

~~~json
{
  "source": "00b1d080",
  "target": "Stack[-0x6c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d084`](#insn-00b1d084)

~~~json
{
  "source": "00b1d084",
  "target": "Stack[-0x6a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d088`](#insn-00b1d088)

~~~json
{
  "source": "00b1d088",
  "target": "Stack[-0x690]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d08c`](#insn-00b1d08c)

~~~json
{
  "source": "00b1d08c",
  "target": "Stack[-0x690]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d090`](#insn-00b1d090)

~~~json
{
  "source": "00b1d090",
  "target": "Stack[-0x670]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d094`](#insn-00b1d094)

~~~json
{
  "source": "00b1d094",
  "target": "Stack[-0x680]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d098`](#insn-00b1d098)

~~~json
{
  "source": "00b1d098",
  "target": "Stack[-0x698]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0a0`](#insn-00b1d0a0)

~~~json
{
  "source": "00b1d0a0",
  "target": "Stack[-0x648]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0a4`](#insn-00b1d0a4)

~~~json
{
  "source": "00b1d0a4",
  "target": "Stack[-0x658]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0a8`](#insn-00b1d0a8)

~~~json
{
  "source": "00b1d0a8",
  "target": "Stack[-0x650]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0b0`](#insn-00b1d0b0)

~~~json
{
  "source": "00b1d0b0",
  "target": "Stack[-0x668]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0b4`](#insn-00b1d0b4)

~~~json
{
  "source": "00b1d0b4",
  "target": "Stack[-0x64e]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0b8`](#insn-00b1d0b8)

~~~json
{
  "source": "00b1d0b8",
  "target": "Stack[-0x638]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0bc`](#insn-00b1d0bc)

~~~json
{
  "source": "00b1d0bc",
  "target": "Stack[-0x636]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0c0`](#insn-00b1d0c0)

~~~json
{
  "source": "00b1d0c0",
  "target": "Stack[-0x630]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0c4`](#insn-00b1d0c4)

~~~json
{
  "source": "00b1d0c4",
  "target": "Stack[-0x61b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0c8`](#insn-00b1d0c8)

~~~json
{
  "source": "00b1d0c8",
  "target": "Stack[-0x620]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0cc`](#insn-00b1d0cc)

~~~json
{
  "source": "00b1d0cc",
  "target": "Stack[-0x600]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0d0`](#insn-00b1d0d0)

~~~json
{
  "source": "00b1d0d0",
  "target": "Stack[-0x610]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0d4`](#insn-00b1d0d4)

~~~json
{
  "source": "00b1d0d4",
  "target": "Stack[-0x5e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0dc`](#insn-00b1d0dc)

~~~json
{
  "source": "00b1d0dc",
  "target": "Stack[-0x5c1]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0e4`](#insn-00b1d0e4)

~~~json
{
  "source": "00b1d0e4",
  "target": "Stack[-0x5d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0e8`](#insn-00b1d0e8)

~~~json
{
  "source": "00b1d0e8",
  "target": "Stack[-0x5c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0ec`](#insn-00b1d0ec)

~~~json
{
  "source": "00b1d0ec",
  "target": "Stack[-0x578]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0f0`](#insn-00b1d0f0)

~~~json
{
  "source": "00b1d0f0",
  "target": "Stack[-0x598]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0f4`](#insn-00b1d0f4)

~~~json
{
  "source": "00b1d0f4",
  "target": "Stack[-0x5b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d0fc`](#insn-00b1d0fc)

~~~json
{
  "source": "00b1d0fc",
  "target": "Stack[-0x570]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d104`](#insn-00b1d104)

~~~json
{
  "source": "00b1d104",
  "target": "Stack[-0x567]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d114`](#insn-00b1d114)

~~~json
{
  "source": "00b1d114",
  "target": "002ac2f1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac2f1",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "5f67656e65726174656400",
  "capture_start": "002ac2f1",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1d118`](#insn-00b1d118)

~~~json
{
  "source": "00b1d118",
  "target": "002b2820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0100000000000000",
  "capture_start": "002b2820",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1d130`](#insn-00b1d130)

~~~json
{
  "source": "00b1d130",
  "target": "Stack[-0x56f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d134`](#insn-00b1d134)

~~~json
{
  "source": "00b1d134",
  "target": "Stack[-0x565]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d138`](#insn-00b1d138)

~~~json
{
  "source": "00b1d138",
  "target": "Stack[-0x550]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d13c`](#insn-00b1d13c)

~~~json
{
  "source": "00b1d13c",
  "target": "Stack[-0x558]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d140`](#insn-00b1d140)

~~~json
{
  "source": "00b1d140",
  "target": "Stack[-0x540]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d144`](#insn-00b1d144)

~~~json
{
  "source": "00b1d144",
  "target": "Stack[-0x538]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d148`](#insn-00b1d148)

~~~json
{
  "source": "00b1d148",
  "target": "Stack[-0x530]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d150`](#insn-00b1d150)

~~~json
{
  "source": "00b1d150",
  "target": "00bde970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d158`](#insn-00b1d158)

~~~json
{
  "source": "00b1d158",
  "target": "00bde910",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d168`](#insn-00b1d168)

~~~json
{
  "source": "00b1d168",
  "target": "Stack[-0x2e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d16c`](#insn-00b1d16c)

~~~json
{
  "source": "00b1d16c",
  "target": "00b1d18c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d17c`](#insn-00b1d17c)

~~~json
{
  "source": "00b1d17c",
  "target": "00bdfe60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d188`](#insn-00b1d188)

~~~json
{
  "source": "00b1d188",
  "target": "00bdffc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d194`](#insn-00b1d194)

~~~json
{
  "source": "00b1d194",
  "target": "00bdf060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d198`](#insn-00b1d198)

~~~json
{
  "source": "00b1d198",
  "target": "Stack[-0x6d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d19c`](#insn-00b1d19c)

~~~json
{
  "source": "00b1d19c",
  "target": "Stack[-0x6c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1c0`](#insn-00b1d1c0)

~~~json
{
  "source": "00b1d1c0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1c4`](#insn-00b1d1c4)

~~~json
{
  "source": "00b1d1c4",
  "target": "00bdef60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d1c8`](#insn-00b1d1c8)

~~~json
{
  "source": "00b1d1c8",
  "target": "Stack[-0x470]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1d8`](#insn-00b1d1d8)

~~~json
{
  "source": "00b1d1d8",
  "target": "00bdeab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d1dc`](#insn-00b1d1dc)

~~~json
{
  "source": "00b1d1dc",
  "target": "Stack[-0x460]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1e0`](#insn-00b1d1e0)

~~~json
{
  "source": "00b1d1e0",
  "target": "Stack[-0x470]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1e4`](#insn-00b1d1e4)

~~~json
{
  "source": "00b1d1e4",
  "target": "Stack[-0x478]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1e8`](#insn-00b1d1e8)

~~~json
{
  "source": "00b1d1e8",
  "target": "Stack[-0x468]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1ec`](#insn-00b1d1ec)

~~~json
{
  "source": "00b1d1ec",
  "target": "Stack[-0x458]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1f0`](#insn-00b1d1f0)

~~~json
{
  "source": "00b1d1f0",
  "target": "00b1d26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1f4`](#insn-00b1d1f4)

~~~json
{
  "source": "00b1d1f4",
  "target": "Stack[-0x3b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1f8`](#insn-00b1d1f8)

~~~json
{
  "source": "00b1d1f8",
  "target": "Stack[-0x3a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d1fc`](#insn-00b1d1fc)

~~~json
{
  "source": "00b1d1fc",
  "target": "Stack[-0x390]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d204`](#insn-00b1d204)

~~~json
{
  "source": "00b1d204",
  "target": "Stack[-0x3b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d218`](#insn-00b1d218)

~~~json
{
  "source": "00b1d218",
  "target": "00b1d220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d24c`](#insn-00b1d24c)

~~~json
{
  "source": "00b1d24c",
  "target": "00b1d2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d258`](#insn-00b1d258)

~~~json
{
  "source": "00b1d258",
  "target": "00bdf290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d268`](#insn-00b1d268)

~~~json
{
  "source": "00b1d268",
  "target": "00b1d2bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d278`](#insn-00b1d278)

~~~json
{
  "source": "00b1d278",
  "target": "00291545",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00291545",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "6572726f723a2000",
  "capture_start": "00291545",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b1d280`](#insn-00b1d280)

~~~json
{
  "source": "00b1d280",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d28c`](#insn-00b1d28c)

~~~json
{
  "source": "00b1d28c",
  "target": "00bdf8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d290`](#insn-00b1d290)

~~~json
{
  "source": "00b1d290",
  "target": "Stack[-0x6c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d294`](#insn-00b1d294)

~~~json
{
  "source": "00b1d294",
  "target": "00b1d2a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d298`](#insn-00b1d298)

~~~json
{
  "source": "00b1d298",
  "target": "Stack[-0x6b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d29c`](#insn-00b1d29c)

~~~json
{
  "source": "00b1d29c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d2ac`](#insn-00b1d2ac)

~~~json
{
  "source": "00b1d2ac",
  "target": "00b1d3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d2b8`](#insn-00b1d2b8)

~~~json
{
  "source": "00b1d2b8",
  "target": "00b1d2e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d2c4`](#insn-00b1d2c4)

~~~json
{
  "source": "00b1d2c4",
  "target": "00b1d2e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d2dc`](#insn-00b1d2dc)

~~~json
{
  "source": "00b1d2dc",
  "target": "00b1d2cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d2e0`](#insn-00b1d2e0)

~~~json
{
  "source": "00b1d2e0",
  "target": "Stack[-0x3b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d2e4`](#insn-00b1d2e4)

~~~json
{
  "source": "00b1d2e4",
  "target": "Stack[-0x3a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d2e8`](#insn-00b1d2e8)

~~~json
{
  "source": "00b1d2e8",
  "target": "Stack[-0x3b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d304`](#insn-00b1d304)

~~~json
{
  "source": "00b1d304",
  "target": "00bdf3c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d308`](#insn-00b1d308)

~~~json
{
  "source": "00b1d308",
  "target": "00b1d340",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d318`](#insn-00b1d318)

~~~json
{
  "source": "00b1d318",
  "target": "00b1d32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d324`](#insn-00b1d324)

~~~json
{
  "source": "00b1d324",
  "target": "00bdf290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d33c`](#insn-00b1d33c)

~~~json
{
  "source": "00b1d33c",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d34c`](#insn-00b1d34c)

~~~json
{
  "source": "00b1d34c",
  "target": "00bdf380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d354`](#insn-00b1d354)

~~~json
{
  "source": "00b1d354",
  "target": "00bdf0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d358`](#insn-00b1d358)

~~~json
{
  "source": "00b1d358",
  "target": "Stack[-0x6e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d364`](#insn-00b1d364)

~~~json
{
  "source": "00b1d364",
  "target": "00b1d370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d36c`](#insn-00b1d36c)

~~~json
{
  "source": "00b1d36c",
  "target": "00b1d390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d380`](#insn-00b1d380)

~~~json
{
  "source": "00b1d380",
  "target": "00b1d390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d388`](#insn-00b1d388)

~~~json
{
  "source": "00b1d388",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d390`](#insn-00b1d390)

~~~json
{
  "source": "00b1d390",
  "target": "Stack[-0x6b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d394`](#insn-00b1d394)

~~~json
{
  "source": "00b1d394",
  "target": "Stack[-0x6c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3a8`](#insn-00b1d3a8)

~~~json
{
  "source": "00b1d3a8",
  "target": "00bde980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d3ac`](#insn-00b1d3ac)

~~~json
{
  "source": "00b1d3ac",
  "target": "Stack[-0x6d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3b0`](#insn-00b1d3b0)

~~~json
{
  "source": "00b1d3b0",
  "target": "00b1d3bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3b4`](#insn-00b1d3b4)

~~~json
{
  "source": "00b1d3b4",
  "target": "Stack[-0x6c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3b8`](#insn-00b1d3b8)

~~~json
{
  "source": "00b1d3b8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d3bc`](#insn-00b1d3bc)

~~~json
{
  "source": "00b1d3bc",
  "target": "00b1d3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3c8`](#insn-00b1d3c8)

~~~json
{
  "source": "00b1d3c8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3d0`](#insn-00b1d3d0)

~~~json
{
  "source": "00b1d3d0",
  "target": "00b1d3f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3d8`](#insn-00b1d3d8)

~~~json
{
  "source": "00b1d3d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3dc`](#insn-00b1d3dc)

~~~json
{
  "source": "00b1d3dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3e0`](#insn-00b1d3e0)

~~~json
{
  "source": "00b1d3e0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3e4`](#insn-00b1d3e4)

~~~json
{
  "source": "00b1d3e4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3e8`](#insn-00b1d3e8)

~~~json
{
  "source": "00b1d3e8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1d3f4`](#insn-00b1d3f4)

~~~json
{
  "source": "00b1d3f4",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1d3f8`](#insn-00b1d3f8)

~~~json
{
  "source": "00b1d3f8",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
