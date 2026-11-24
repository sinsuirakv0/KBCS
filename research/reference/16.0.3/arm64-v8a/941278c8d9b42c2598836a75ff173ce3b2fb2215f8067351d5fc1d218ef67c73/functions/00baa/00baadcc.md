# 00baadcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ba9dd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9dd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-7f31c73cdcc3242627aeb81c6ce46678)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baadcc",
  "name": "FUN_00baadcc",
  "size": 1652,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fbd3a2ed4ca07078cddca3991cd2bc47676725db72a47742fbb6cdffb2df5a1",
  "source_text_sha256": "5fbd3a2ed4ca07078cddca3991cd2bc47676725db72a47742fbb6cdffb2df5a1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baadcc",
        "00bab43f"
      ]
    ],
    "bytes_sha256": "526d0d2f19d175cbe0fc1c07f75ce98db01cccd1ce770ee4a19d1f4d0fbdbe7c",
    "instruction_count": 413,
    "instruction_bytes": 1652,
    "body_bytes": 1652,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b79e94](../00b79/00b79e94.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c590a0](../00c59/00c590a0.md)
- [00c590f0](../00c59/00c590f0.md)
- [00c59130](../00c59/00c59130.md)
- [00c59150](../00c59/00c59150.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)
- [00c5cb60](../00c5c/00c5cb60.md)
- [00c5cb70](../00c5c/00c5cb70.md)
- [00c5d090](../00c5d/00c5d090.md)
- [00c5d240](../00c5d/00c5d240.md)
- [00c5d330](../00c5d/00c5d330.md)
- [00c5d5d0](../00c5d/00c5d5d0.md)
- [00c5d6e0](../00c5d/00c5d6e0.md)
- [00c5d740](../00c5d/00c5d740.md)
- [00c5d750](../00c5d/00c5d750.md)
- [00c5d790](../00c5d/00c5d790.md)
- [00c5d7f0](../00c5d/00c5d7f0.md)
- [00c5d810](../00c5d/00c5d810.md)
- [00c5d980](../00c5d/00c5d980.md)
- [00c5db40](../00c5d/00c5db40.md)
- [00c5e0f0](../00c5e/00c5e0f0.md)

## 関連文字列（未確認候補）

~~~text
"$schema"
"error: "
"field set more than once: "
"unknown field: "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 16086 bytes

~~~c

void FUN_00baadcc(char *param_1,long *param_2,byte *param_3,long *param_4,long param_5)

{
  byte bVar1;
  uint uVar2;
  long lVar3;
  bool bVar4;
  int iVar5;
  long lVar6;
  undefined1 *puVar7;
  undefined *puVar8;
  void *pvVar9;
  byte *__s1;
  ulong uVar10;
  long lVar11;
  long lVar12;
  int *piVar13;
  long lVar14;
  undefined8 *puVar15;
  long lVar16;
  long lVar17;
  ulong uVar18;
  byte local_158;
  undefined7 uStack_157;
  ulong uStack_150;
  undefined1 *local_148;
  undefined *local_140;
  undefined *puStack_138;
  undefined *local_130;
  void *local_128;
  undefined8 local_120;
  ulong uStack_118;
  undefined2 local_110;
  undefined2 uStack_10e;
  undefined4 uStack_10c;
  undefined2 uStack_108;
  undefined2 uStack_106;
  undefined8 *local_100;
  undefined8 local_f8;
  undefined8 local_f0;
  undefined **ppuStack_e8;
  undefined8 *local_e0;
  undefined8 local_d8;
  undefined8 local_d0;
  undefined **ppuStack_c8;
  undefined *local_c0;
  undefined *puStack_b8;
  undefined *local_b0;
  void *pvStack_a8;
  undefined8 local_a0;
  ulong uStack_98;
  undefined1 *local_90;
  undefined2 local_88;
  long local_78;
  
                    /* try { // try from 00baadcc to 00caadcf has its CatchHandler @ 00bad040 */
                    /* try { // try from 00baadec to 00caadf7 has its CatchHandler @ 00bacff0 */
  lVar3 = tpidr_el0;
  local_78 = *(long *)(lVar3 + 0x28);
  bVar1 = *param_3;
                    /* try { // try from 00baae0c to 00caae17 has its CatchHandler @ 00bacfbc */
  lVar14 = *param_2;
  uVar18 = (ulong)(bVar1 >> 1);
  if ((bVar1 & 1) != 0) {
    uVar18 = *(ulong *)(param_3 + 8);
  }
  if (uVar18 == 7) {
    __s1 = *(byte **)(param_3 + 0x10);
                    /* try { // try from 00baae38 to 00caae43 has its CatchHandler @ 00bacfa0 */
    if ((bVar1 & 1) == 0) {
      __s1 = param_3 + 1;
    }
    iVar5 = memcmp(__s1,"$schema",7);
    if (iVar5 != 0) goto LAB_00baae48;
    _ZN11flatbuffers6Parser6ExpectEi(param_1,lVar14,0x101);
LAB_00baaf28:
    param_1[1] = '\x01';
    if (*param_1 != '\0') goto LAB_00bab25c;
  }
  else {
LAB_00baae48:
    lVar6 = _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
                      (param_5 + 0xa0,param_3);
                    /* try { // try from 00baae5c to 00caae67 has its CatchHandler @ 00bacf6c */
    if ((param_5 + 0xa8 == lVar6) ||
       (puVar15 = *(undefined8 **)(lVar6 + 0x38), puVar15 == (undefined8 *)0x0)) {
      if (*(char *)(lVar14 + 0x314) == '\0') {
        _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
                  (&local_c0,"unknown field: ",param_3);
                    /* try { // try from 00baaf5c to 00caaf67 has its CatchHandler @ 00bace38 */
        _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
                  (&local_140,"error: ",&local_c0);
        _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
                  (lVar14,&local_140);
        if (((ulong)local_140 & 1) != 0) {
          _ZdlPv(local_130);
        }
                    /* try { // try from 00baaf80 to 00caaf8b has its CatchHandler @ 00bace1c */
        param_1[0] = '\x01';
        param_1[1] = '\0';
        if (((ulong)local_c0 & 1) != 0) {
                    /* try { // try from 00baaf94 to 00caaf97 has its CatchHandler @ 00bacdfc */
          _ZdlPv(local_b0);
        }
        goto LAB_00bab25c;
      }
      _ZN11flatbuffers6Parser16SkipAnyJsonValueEv(param_1,lVar14);
      goto LAB_00baaf28;
    }
    if (*(int *)(lVar14 + 0x1c) == 0x104) {
      bVar1 = *(byte *)(lVar14 + 0x28);
      uVar18 = (ulong)(bVar1 >> 1);
                    /* try { // try from 00baae88 to 00caae93 has its CatchHandler @ 00bacf50 */
      if ((bVar1 & 1) != 0) {
        uVar18 = *(ulong *)(lVar14 + 0x30);
      }
      if (uVar18 == 4) {
        piVar13 = *(int **)(lVar14 + 0x38);
        if ((bVar1 & 1) == 0) {
          piVar13 = (int *)(lVar14 + 0x29);
        }
                    /* try { // try from 00baaea8 to 00caaeb3 has its CatchHandler @ 00bacf1c */
                    /* try { // try from 00baaeb4 to 00caaed3 has its CatchHandler @ 00bad0c8 */
        if ((*piVar13 == 0x6c6c756e) && (0xb < *(int *)(puVar15 + 0x14) - 1U)) {
          _ZN11flatbuffers6Parser4NextEv(param_1,lVar14);
          goto LAB_00baaf28;
        }
      }
    }
    puStack_b8 = (undefined *)puVar15[0x15];
    local_c0 = (undefined *)puVar15[0x14];
    pvStack_a8 = (void *)puVar15[0x17];
    local_b0 = (undefined *)puVar15[0x16];
                    /* try { // try from 00baaed4 to 00caaf0b has its CatchHandler @ 00bad138 */
    uStack_98 = 0;
    local_90 = (undefined1 *)0x0;
    local_a0 = (void *)0x0;
    if ((puVar15[0x18] & 1) == 0) {
      local_90 = (undefined1 *)puVar15[0x1a];
      uStack_98 = puVar15[0x19];
      local_a0 = (void *)puVar15[0x18];
    }
    else {
      uVar18 = puVar15[0x19];
      if (0xffffffffffffffef < uVar18) goto LAB_00bab43c;
      pvVar9 = (void *)puVar15[0x1a];
      if (uVar18 < 0x17) {
                    /* try { // try from 00baafb4 to 00caafbf has its CatchHandler @ 00bacd80 */
        puVar7 = (undefined1 *)((long)&local_a0 + 1);
        local_a0 = (void *)(ulong)(byte)((int)uVar18 << 1);
        if (uVar18 != 0) goto LAB_00bab000;
      }
      else {
                    /* try { // try from 00baafd4 to 00caafdf has its CatchHandler @ 00bacd7c */
        uVar10 = uVar18 + 0x10 & 0xfffffffffffffff0;
        puVar7 = (undefined1 *)_Znwm(uVar10);
        local_a0 = (void *)(uVar10 | 1);
        uStack_98 = uVar18;
        local_90 = puVar7;
LAB_00bab000:
                    /* try { // try from 00bab000 to 00cab00b has its CatchHandler @ 00bacd30 */
        memcpy(puVar7,pvVar9,uVar18);
      }
      puVar7[uVar18] = 0;
    }
    local_88 = *(undefined2 *)(puVar15 + 0x1b);
                    /* try { // try from 00bab024 to 00cab02f has its CatchHandler @ 00baccfc */
    if (*(char *)((long)puVar15 + 0xe4) == '\0') {
                    /* try { // try from 00bab184 to 00cab18f has its CatchHandler @ 00bacba0 */
      if (puVar15[0x1e] == 0) {
                    /* try { // try from 00bab1a4 to 00cab1af has its CatchHandler @ 00bacb9c */
                    /* try { // try from 00bab1b0 to 00cab1cf has its CatchHandler @ 00bacecc */
        _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEmb
                  (param_1,lVar14,&local_c0,puVar15,*param_4,param_5,0,0);
      }
      else {
        _ZN11flatbuffers6Parser21ParseNestedFlatbufferERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefE
                  (param_1,lVar14,&local_c0,puVar15,*param_4,param_5);
      }
      param_1[1] = '\x01';
      if (*param_1 == '\0') goto LAB_00bab28c;
LAB_00bab244:
      bVar4 = true;
    }
    else {
      puVar8 = (undefined *)_Znwm(0x400);
      local_130 = puVar8 + 0x400;
      local_140 = puVar8;
      memset(puVar8,0,0x400);
                    /* try { // try from 00bab050 to 00cab05b has its CatchHandler @ 00baccec */
      ppuStack_e8 = &local_140;
      local_100 = &local_f8;
      local_f8 = 0;
      local_e0 = &local_d8;
      local_d8 = 0;
                    /* try { // try from 00bab070 to 00cab07b has its CatchHandler @ 00baccac */
      local_120 = (void *)0x0;
      uStack_118 = 0;
      local_110 = 0;
      local_f0 = 0;
      local_d0 = 0;
      uStack_10c = (undefined4)DAT_002c4370;
      uStack_108 = (undefined2)((ulong)DAT_002c4370 >> 0x20);
      uStack_106 = (undefined2)((ulong)DAT_002c4370 >> 0x30);
      local_128 = (void *)0x0;
      puStack_138 = puVar8;
      ppuStack_c8 = ppuStack_e8;
      _ZN11flatbuffers6Parser20ParseFlexBufferValueEPN11flexbuffers7BuilderE
                (param_1,lVar14,&local_140);
      bVar4 = true;
                    /* try { // try from 00bab09c to 00cab0a7 has its CatchHandler @ 00bacc9c */
      param_1[1] = '\x01';
      if (*param_1 == '\0') {
        _ZN11flexbuffers7Builder6FinishEv(&local_140);
        if ((long)puStack_138 - (long)local_140 != 0) {
                    /* try { // try from 00bab0c0 to 00cab0cb has its CatchHandler @ 00bacc5c */
          if (*(ulong *)(lVar14 + 0x1c0) < 8) {
            *(undefined8 *)(lVar14 + 0x1c0) = 8;
          }
          iVar5 = *(int *)(lVar14 + 0x188);
          uVar2 = -((int)((long)puStack_138 - (long)local_140) + iVar5);
          uVar18 = (ulong)uVar2 & 7;
          if ((uVar2 & 7) != 0) {
            lVar6 = *(long *)(lVar14 + 0x198);
                    /* try { // try from 00bab0ec to 00cab0f7 has its CatchHandler @ 00bacc40 */
            if ((uint)((int)lVar6 - *(int *)(lVar14 + 0x1a0)) < uVar18) {
              _ZN11flatbuffers15vector_downwardIjE10reallocateEm(lVar14 + 0x158,uVar18);
              lVar6 = *(long *)(lVar14 + 0x198);
                    /* try { // try from 00bab108 to 00cab113 has its CatchHandler @ 00bacc3c */
              iVar5 = *(int *)(lVar14 + 0x188);
            }
            *(undefined1 **)(lVar14 + 0x198) = (undefined1 *)(lVar6 - uVar18);
            *(int *)(lVar14 + 0x188) = iVar5 + (int)uVar18;
            *(undefined1 *)(lVar6 - uVar18) = 0;
            if (uVar18 != 1) {
              uVar10 = 1;
              do {
                *(undefined1 *)(*(long *)(lVar14 + 0x198) + uVar10) = 0;
                    /* try { // try from 00bab134 to 00cab13f has its CatchHandler @ 00bacbf0 */
                uVar10 = uVar10 + 1;
              } while (uVar18 != uVar10);
            }
          }
        }
        puVar8 = 
        PTR__ZZN11flatbuffers4dataIhNSt6__ndk19allocatorIhEEEEPKT_RKNS1_6vectorIS4_T0_EEE1t_00c9c938
        ;
                    /* try { // try from 00bab158 to 00cab163 has its CatchHandler @ 00bacbec */
        if (local_140 != puStack_138) {
          puVar8 = local_140;
        }
        _ZN11flatbuffers21FlatBufferBuilderImplILb0EE12CreateVectorIhNS_6OffsetENS_6VectorEEET0_IJT1_IJT_EEEEPKS7_m
                  (lVar14 + 0x158,puVar8,(long)puStack_138 - (long)local_140);
        _ZN11flatbuffers11NumToStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_
                  (&local_158);
        if (((ulong)local_a0 & 1) != 0) {
                    /* try { // try from 00bab1d0 to 00cab23f has its CatchHandler @ 00bad0a0 */
          *local_90 = 0;
          uStack_98 = 0;
          if (((ulong)local_a0 & 1) != 0) {
            _ZdlPv(local_90);
          }
        }
        local_a0 = (void *)CONCAT71(uStack_157,local_158);
        bVar4 = false;
        local_90 = local_148;
        uStack_98 = uStack_150;
      }
      _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
                (&local_e0,local_d8);
      _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE7destroyEPNS_11__tree_nodeImPvEE
                (&local_100,local_f8);
      if (local_128 != (void *)0x0) {
        local_120 = local_128;
        _ZdlPv(local_128);
      }
      if (local_140 != (undefined *)0x0) {
        puStack_138 = local_140;
        _ZdlPv(local_140);
      }
      if (bVar4) goto LAB_00bab244;
LAB_00bab28c:
      puVar7 = local_90;
      uVar18 = uStack_98;
      lVar11 = *param_4;
      lVar16 = *(long *)(lVar14 + 0x5b8);
      lVar6 = lVar16;
      if (lVar11 != 0) {
                    /* try { // try from 00bab298 to 00cab2a3 has its CatchHandler @ 00bacdf8 */
        lVar12 = lVar11 * -0x48;
        lVar17 = lVar16;
                    /* try { // try from 00bab2ac to 00cab2af has its CatchHandler @ 00bacdd8 */
        do {
          if (*(undefined8 **)(lVar17 + -8) == puVar15) {
            _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
                      (&local_158,"field set more than once: ",puVar15);
            _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
                      (&local_140,"error: ",&local_158);
                    /* try { // try from 00bab368 to 00cab373 has its CatchHandler @ 00baccd8 */
            _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
                      (lVar14,&local_140);
            if (((ulong)local_140 & 1) != 0) {
              _ZdlPv(local_130);
            }
                    /* try { // try from 00bab388 to 00cab393 has its CatchHandler @ 00bacc98 */
            param_1[0] = '\x01';
            param_1[1] = '\0';
            if ((local_158 & 1) != 0) {
              _ZdlPv(local_148);
            }
            bVar4 = true;
            goto joined_r0x00bab3a4;
          }
          lVar6 = lVar17;
        } while ((*(ushort *)(puVar15 + 0x1b) <= *(ushort *)(*(undefined8 **)(lVar17 + -8) + 0x1b))
                && (lVar12 = lVar12 + 0x48, lVar6 = lVar16 + lVar11 * -0x48, lVar17 = lVar17 + -0x48
                   , lVar12 != 0
                    /* try { // try from 00bab2cc to 00cab2d7 has its CatchHandler @ 00bacd6c */));
      }
                    /* try { // try from 00bab2ec to 00cab2f7 has its CatchHandler @ 00bacd68 */
      local_120 = (void *)0x0;
      uStack_118 = 0;
      puStack_138 = puStack_b8;
      local_140 = local_c0;
      local_128 = pvStack_a8;
      local_130 = local_b0;
      local_110 = 0;
      uStack_10e = 0;
      uStack_10c = 0;
      if (((ulong)local_a0 & 1) == 0) {
        local_110 = SUB82(local_90,0);
        uStack_10e = (undefined2)((ulong)local_90 >> 0x10);
        uStack_10c = (undefined4)((ulong)local_90 >> 0x20);
        uStack_118 = uStack_98;
        local_120 = local_a0;
      }
      else {
                    /* try { // try from 00bab318 to 00cab323 has its CatchHandler @ 00bacd20 */
        if (0xffffffffffffffef < uStack_98) {
LAB_00bab43c:
                    /* WARNING: Subroutine does not return */
          abort();
        }
        if (uStack_98 < 0x17) {
          pvVar9 = (void *)((long)&local_120 + 1);
          local_120 = (void *)(ulong)(byte)((int)uStack_98 << 1);
          if (uStack_98 != 0) goto LAB_00bab3cc;
        }
        else {
          uVar10 = uStack_98 + 0x10 & 0xfffffffffffffff0;
                    /* try { // try from 00bab3b4 to 00cab3bf has its CatchHandler @ 00bacc88 */
          pvVar9 = (void *)_Znwm(uVar10);
          local_120 = (void *)(uVar10 | 1);
          uStack_118 = uVar18;
          local_110 = SUB82(pvVar9,0);
          uStack_10e = (undefined2)((ulong)pvVar9 >> 0x10);
          uStack_10c = (undefined4)((ulong)pvVar9 >> 0x20);
LAB_00bab3cc:
                    /* try { // try from 00bab3d8 to 00cab3e3 has its CatchHandler @ 00bacc58 */
          memcpy(pvVar9,puVar7,uVar18);
        }
        *(undefined1 *)((long)pvVar9 + uVar18) = 0;
      }
      uStack_108 = local_88;
      local_100 = puVar15;
      _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE6insertENS_11__wrap_iterIPKS6_EEOS6_
                (lVar14 + 0x5b0,lVar6,&local_140);
      if (((ulong)local_120 & 1) != 0) {
                    /* try { // try from 00bab404 to 00cab40f has its CatchHandler @ 00bacc2c */
        _ZdlPv((void *)CONCAT44(uStack_10c,CONCAT22(uStack_10e,local_110)));
      }
      bVar4 = false;
      *param_4 = *param_4 + 1;
                    /* try { // try from 00bab420 to 00cab42b has its CatchHandler @ 00bacc28 */
    }
joined_r0x00bab3a4:
    if (((ulong)local_a0 & 1) != 0) {
      _ZdlPv(local_90);
    }
    if (bVar4) goto LAB_00bab25c;
  }
  param_1[0] = '\0';
  param_1[1] = '\0';
LAB_00bab25c:
  if (*(long *)(lVar3 + 0x28) == local_78) {
                    /* try { // try from 00bab274 to 00cab27f has its CatchHandler @ 00bace34 */
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
<a id="insn-00baadcc"></a> `00baadcc` | `ff 83 05 d1` | sub sp,sp,#0x160 | `FALL_THROUGH`
<a id="insn-00baadd0"></a> `00baadd0` | `fc 6f 10 a9` | stp x28,x27,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00baadd4"></a> `00baadd4` | `fa 67 11 a9` | stp x26,x25,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00baadd8"></a> `00baadd8` | `f8 5f 12 a9` | stp x24,x23,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00baaddc"></a> `00baaddc` | `f6 57 13 a9` | stp x22,x21,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00baade0"></a> `00baade0` | `f4 4f 14 a9` | stp x20,x19,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00baade4"></a> `00baade4` | `fd 7b 15 a9` | stp x29,x30,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00baade8"></a> `00baade8` | `fd 43 05 91` | add x29,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00baadec"></a> `00baadec` | `5c d0 3b d5` | mrs x28,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00baadf0"></a> `00baadf0` | `89 17 40 f9` | ldr x9,[x28, #0x28] | `FALL_THROUGH`
<a id="insn-00baadf4"></a> `00baadf4` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00baadf8"></a> `00baadf8` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00baadfc"></a> `00baadfc` | `f8 03 01 aa` | mov x24,x1 | `FALL_THROUGH`
<a id="insn-00baae00"></a> `00baae00` | `a9 83 19 f8` | stur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00baae04"></a> `00baae04` | `29 00 40 39` | ldrb w9,[x1] | `FALL_THROUGH`
<a id="insn-00baae08"></a> `00baae08` | `2a 04 40 f9` | ldr x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00baae0c"></a> `00baae0c` | `14 00 40 f9` | ldr x20,[x0] | `FALL_THROUGH`
<a id="insn-00baae10"></a> `00baae10` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00baae14"></a> `00baae14` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baae18"></a> `00baae18` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baae1c"></a> `00baae1c` | `6a 01 8a 9a` | csel x10,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baae20"></a> `00baae20` | `5f 1d 00 f1` | cmp x10,#0x7 | `FALL_THROUGH`
<a id="insn-00baae24"></a> `00baae24` | `21 01 00 54` | b.ne 0x00baae48 | `CONDITIONAL_JUMP`
<a id="insn-00baae28"></a> `00baae28` | `08 0b 40 f9` | ldr x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00baae2c"></a> `00baae2c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baae30"></a> `00baae30` | `21 b8 ff b0` | adrp x1,0x2af000 | `FALL_THROUGH`
<a id="insn-00baae34"></a> `00baae34` | `21 94 15 91` | add x1,x1,#0x565 | `FALL_THROUGH`
<a id="insn-00baae38"></a> `00baae38` | `00 15 98 9a` | csinc x0,x8,x24,ne | `FALL_THROUGH`
<a id="insn-00baae3c"></a> `00baae3c` | `e2 00 80 52` | mov w2,#0x7 | `FALL_THROUGH`
<a id="insn-00baae40"></a> `00baae40` | `ac b8 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00baae44"></a> `00baae44` | `a0 06 00 34` | cbz w0,0x00baaf18 | `CONDITIONAL_JUMP`
<a id="insn-00baae48"></a> `00baae48` | `e0 82 02 91` | add x0,x23,#0xa0 | `FALL_THROUGH`
<a id="insn-00baae4c"></a> `00baae4c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00baae50"></a> `00baae50` | `3c cb 02 94` | bl 0x00c5db40 | `UNCONDITIONAL_CALL`
<a id="insn-00baae54"></a> `00baae54` | `e8 a2 02 91` | add x8,x23,#0xa8 | `FALL_THROUGH`
<a id="insn-00baae58"></a> `00baae58` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00baae5c"></a> `00baae5c` | `20 05 00 54` | b.eq 0x00baaf00 | `CONDITIONAL_JUMP`
<a id="insn-00baae60"></a> `00baae60` | `16 1c 40 f9` | ldr x22,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00baae64"></a> `00baae64` | `f6 04 00 b4` | cbz x22,0x00baaf00 | `CONDITIONAL_JUMP`
<a id="insn-00baae68"></a> `00baae68` | `88 1e 40 b9` | ldr w8,[x20, #0x1c] | `FALL_THROUGH`
<a id="insn-00baae6c"></a> `00baae6c` | `1f 11 04 71` | cmp w8,#0x104 | `FALL_THROUGH`
<a id="insn-00baae70"></a> `00baae70` | `a1 02 00 54` | b.ne 0x00baaec4 | `CONDITIONAL_JUMP`
<a id="insn-00baae74"></a> `00baae74` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00baae78"></a> `00baae78` | `09 8d 42 38` | ldrb w9,[x8, #0x28]! | `FALL_THROUGH`
<a id="insn-00baae7c"></a> `00baae7c` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baae80"></a> `00baae80` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baae84"></a> `00baae84` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baae88"></a> `00baae88` | `6a 01 8a 9a` | csel x10,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baae8c"></a> `00baae8c` | `5f 11 00 f1` | cmp x10,#0x4 | `FALL_THROUGH`
<a id="insn-00baae90"></a> `00baae90` | `a1 01 00 54` | b.ne 0x00baaec4 | `CONDITIONAL_JUMP`
<a id="insn-00baae94"></a> `00baae94` | `8a 1e 40 f9` | ldr x10,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00baae98"></a> `00baae98` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baae9c"></a> `00baae9c` | `c9 ad 8e 52` | mov w9,#0x756e | `FALL_THROUGH`
<a id="insn-00baaea0"></a> `00baaea0` | `89 8d ad 72` | movk w9,#0x6c6c, LSL #16 | `FALL_THROUGH`
<a id="insn-00baaea4"></a> `00baaea4` | `48 15 88 9a` | csinc x8,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baaea8"></a> `00baaea8` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-00baaeac"></a> `00baaeac` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00baaeb0"></a> `00baaeb0` | `a1 00 00 54` | b.ne 0x00baaec4 | `CONDITIONAL_JUMP`
<a id="insn-00baaeb4"></a> `00baaeb4` | `c8 a2 40 b9` | ldr w8,[x22, #0xa0] | `FALL_THROUGH`
<a id="insn-00baaeb8"></a> `00baaeb8` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baaebc"></a> `00baaebc` | `1f 31 00 71` | cmp w8,#0xc | `FALL_THROUGH`
<a id="insn-00baaec0"></a> `00baaec0` | `42 2b 00 54` | b.cs 0x00bab428 | `CONDITIONAL_JUMP`
<a id="insn-00baaec4"></a> `00baaec4` | `c0 06 45 ad` | ldp q0,q1,[x22, #0xa0] | `FALL_THROUGH`
<a id="insn-00baaec8"></a> `00baaec8` | `fa 83 02 91` | add x26,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00baaecc"></a> `00baaecc` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00baaed0"></a> `00baaed0` | `ea 83 02 91` | add x10,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00baaed4"></a> `00baaed4` | `40 07 00 ad` | stp q0,q1,[x26] | `FALL_THROUGH`
<a id="insn-00baaed8"></a> `00baaed8` | `ff ff 0c a9` | stp xzr,xzr,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00baaedc"></a> `00baaedc` | `ff 63 00 f9` | str xzr,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baaee0"></a> `00baaee0` | `09 0d 4c 38` | ldrb w9,[x8, #0xc0]! | `FALL_THROUGH`
<a id="insn-00baaee4"></a> `00baaee4` | `5b 81 00 91` | add x27,x10,#0x20 | `FALL_THROUGH`
<a id="insn-00baaee8"></a> `00baaee8` | `a9 05 00 37` | tbnz w9,#0x0,0x00baaf9c | `CONDITIONAL_JUMP`
<a id="insn-00baaeec"></a> `00baaeec` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00baaef0"></a> `00baaef0` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00baaef4"></a> `00baaef4` | `69 0b 00 f9` | str x9,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00baaef8"></a> `00baaef8` | `60 03 80 3d` | str q0,[x27] | `FALL_THROUGH`
<a id="insn-00baaefc"></a> `00baaefc` | `47 00 00 14` | b 0x00bab018 | `UNCONDITIONAL_JUMP`
<a id="insn-00baaf00"></a> `00baaf00` | `88 52 4c 39` | ldrb w8,[x20, #0x314] | `FALL_THROUGH`
<a id="insn-00baaf04"></a> `00baaf04` | `c8 01 00 34` | cbz w8,0x00baaf3c | `CONDITIONAL_JUMP`
<a id="insn-00baaf08"></a> `00baaf08` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00baaf0c"></a> `00baaf0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baaf10"></a> `00baaf10` | `f4 c9 02 94` | bl 0x00c5d6e0 | `UNCONDITIONAL_CALL`
<a id="insn-00baaf14"></a> `00baaf14` | `05 00 00 14` | b 0x00baaf28 | `UNCONDITIONAL_JUMP`
<a id="insn-00baaf18"></a> `00baaf18` | `21 20 80 52` | mov w1,#0x101 | `FALL_THROUGH`
<a id="insn-00baaf1c"></a> `00baaf1c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00baaf20"></a> `00baaf20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baaf24"></a> `00baaf24` | `33 ca 02 94` | bl 0x00c5d7f0 | `UNCONDITIONAL_CALL`
<a id="insn-00baaf28"></a> `00baaf28` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00baaf2c"></a> `00baaf2c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baaf30"></a> `00baaf30` | `69 06 00 39` | strb w9,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00baaf34"></a> `00baaf34` | `48 19 00 35` | cbnz w8,0x00bab25c | `CONDITIONAL_JUMP`
<a id="insn-00baaf38"></a> `00baaf38` | `c8 00 00 14` | b 0x00bab258 | `UNCONDITIONAL_JUMP`
<a id="insn-00baaf3c"></a> `00baaf3c` | `a0 b8 ff f0` | adrp x0,0x2c1000 | `FALL_THROUGH`
<a id="insn-00baaf40"></a> `00baaf40` | `00 44 34 91` | add x0,x0,#0xd11 | `FALL_THROUGH`
<a id="insn-00baaf44"></a> `00baaf44` | `e8 83 02 91` | add x8,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00baaf48"></a> `00baaf48` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00baaf4c"></a> `00baaf4c` | `81 b8 02 94` | bl 0x00c59150 | `UNCONDITIONAL_CALL`
<a id="insn-00baaf50"></a> `00baaf50` | `a0 b7 ff d0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00baaf54"></a> `00baaf54` | `00 a4 2e 91` | add x0,x0,#0xba9 | `FALL_THROUGH`
<a id="insn-00baaf58"></a> `00baaf58` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00baaf5c"></a> `00baaf5c` | `e1 83 02 91` | add x1,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00baaf60"></a> `00baaf60` | `7c b8 02 94` | bl 0x00c59150 | `UNCONDITIONAL_CALL`
<a id="insn-00baaf64"></a> `00baaf64` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00baaf68"></a> `00baaf68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baaf6c"></a> `00baaf6c` | `29 ca 02 94` | bl 0x00c5d810 | `UNCONDITIONAL_CALL`
<a id="insn-00baaf70"></a> `00baaf70` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaf74"></a> `00baaf74` | `68 00 00 36` | tbz w8,#0x0,0x00baaf80 | `CONDITIONAL_JUMP`
<a id="insn-00baaf78"></a> `00baaf78` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baaf7c"></a> `00baaf7c` | `f5 b7 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00baaf80"></a> `00baaf80` | `e8 83 42 39` | ldrb w8,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00baaf84"></a> `00baaf84` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baaf88"></a> `00baaf88` | `69 02 00 79` | strh w9,[x19] | `FALL_THROUGH`
<a id="insn-00baaf8c"></a> `00baaf8c` | `88 16 00 36` | tbz w8,#0x0,0x00bab25c | `CONDITIONAL_JUMP`
<a id="insn-00baaf90"></a> `00baaf90` | `e0 5b 40 f9` | ldr x0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00baaf94"></a> `00baaf94` | `ef b7 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00baaf98"></a> `00baaf98` | `b1 00 00 14` | b 0x00bab25c | `UNCONDITIONAL_JUMP`
<a id="insn-00baaf9c"></a> `00baaf9c` | `d8 66 40 f9` | ldr x24,[x22, #0xc8] | `FALL_THROUGH`
<a id="insn-00baafa0"></a> `00baafa0` | `1f 43 00 b1` | cmn x24,#0x10 | `FALL_THROUGH`
<a id="insn-00baafa4"></a> `00baafa4` | `c2 24 00 54` | b.cs 0x00bab43c | `CONDITIONAL_JUMP`
<a id="insn-00baafa8"></a> `00baafa8` | `d9 6a 40 f9` | ldr x25,[x22, #0xd0] | `FALL_THROUGH`
<a id="insn-00baafac"></a> `00baafac` | `1f 5f 00 f1` | cmp x24,#0x17 | `FALL_THROUGH`
<a id="insn-00baafb0"></a> `00baafb0` | `c2 00 00 54` | b.cs 0x00baafc8 | `CONDITIONAL_JUMP`
<a id="insn-00baafb4"></a> `00baafb4` | `08 7b 1f 53` | lsl w8,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00baafb8"></a> `00baafb8` | `7a 07 00 91` | add x26,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00baafbc"></a> `00baafbc` | `e8 03 03 39` | strb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baafc0"></a> `00baafc0` | `18 02 00 b5` | cbnz x24,0x00bab000 | `CONDITIONAL_JUMP`
<a id="insn-00baafc4"></a> `00baafc4` | `13 00 00 14` | b 0x00bab010 | `UNCONDITIONAL_JUMP`
<a id="insn-00baafc8"></a> `00baafc8` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00baafcc"></a> `00baafcc` | `fc 03 00 f9` | str x28,[sp] | `FALL_THROUGH`
<a id="insn-00baafd0"></a> `00baafd0` | `fc 03 15 aa` | mov x28,x21 | `FALL_THROUGH`
<a id="insn-00baafd4"></a> `00baafd4` | `f5 03 1b aa` | mov x21,x27 | `FALL_THROUGH`
<a id="insn-00baafd8"></a> `00baafd8` | `1b ed 7c 92` | and x27,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00baafdc"></a> `00baafdc` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00baafe0"></a> `00baafe0` | `d4 b7 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00baafe4"></a> `00baafe4` | `68 03 40 b2` | orr x8,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00baafe8"></a> `00baafe8` | `fb 03 15 aa` | mov x27,x21 | `FALL_THROUGH`
<a id="insn-00baafec"></a> `00baafec` | `f5 03 1c aa` | mov x21,x28 | `FALL_THROUGH`
<a id="insn-00baaff0"></a> `00baaff0` | `fc 03 40 f9` | ldr x28,[sp] | `FALL_THROUGH`
<a id="insn-00baaff4"></a> `00baaff4` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00baaff8"></a> `00baaff8` | `e8 63 0c a9` | stp x8,x24,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baaffc"></a> `00baaffc` | `e0 6b 00 f9` | str x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab000"></a> `00bab000` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00bab004"></a> `00bab004` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bab008"></a> `00bab008` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bab00c"></a> `00bab00c` | `25 b8 02 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab010"></a> `00bab010` | `5f 6b 38 38` | strb wzr,[x26, x24, LSL ] | `FALL_THROUGH`
<a id="insn-00bab014"></a> `00bab014` | `fa 83 02 91` | add x26,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bab018"></a> `00bab018` | `c8 b2 41 79` | ldrh w8,[x22, #0xd8] | `FALL_THROUGH`
<a id="insn-00bab01c"></a> `00bab01c` | `e8 b3 01 79` | strh w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00bab020"></a> `00bab020` | `c8 92 43 39` | ldrb w8,[x22, #0xe4] | `FALL_THROUGH`
<a id="insn-00bab024"></a> `00bab024` | `a8 0a 00 34` | cbz w8,0x00bab178 | `CONDITIONAL_JUMP`
<a id="insn-00bab028"></a> `00bab028` | `00 80 80 52` | mov w0,#0x400 | `FALL_THROUGH`
<a id="insn-00bab02c"></a> `00bab02c` | `c1 b7 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bab030"></a> `00bab030` | `08 00 10 91` | add x8,x0,#0x400 | `FALL_THROUGH`
<a id="insn-00bab034"></a> `00bab034` | `02 80 80 52` | mov w2,#0x400 | `FALL_THROUGH`
<a id="insn-00bab038"></a> `00bab038` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bab03c"></a> `00bab03c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bab040"></a> `00bab040` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab044"></a> `00bab044` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab048"></a> `00bab048` | `3a b8 02 94` | bl 0x00c59130 | `UNCONDITIONAL_CALL`
<a id="insn-00bab04c"></a> `00bab04c` | `c8 b8 ff b0` | adrp x8,0x2c4000 | `FALL_THROUGH`
<a id="insn-00bab050"></a> `00bab050` | `f9 83 00 91` | add x25,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bab054"></a> `00bab054` | `00 b9 41 fd` | ldr d0,[x8, #0x370] | `FALL_THROUGH`
<a id="insn-00bab058"></a> `00bab058` | `28 23 01 91` | add x8,x25,#0x48 | `FALL_THROUGH`
<a id="insn-00bab05c"></a> `00bab05c` | `e8 7f 06 a9` | stp x8,xzr,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bab060"></a> `00bab060` | `28 a3 01 91` | add x8,x25,#0x68 | `FALL_THROUGH`
<a id="insn-00bab064"></a> `00bab064` | `e8 7f 08 a9` | stp x8,xzr,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bab068"></a> `00bab068` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bab06c"></a> `00bab06c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bab070"></a> `00bab070` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bab074"></a> `00bab074` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab078"></a> `00bab078` | `ff a3 00 79` | strh wzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bab07c"></a> `00bab07c` | `ff 67 07 a9` | stp xzr,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bab080"></a> `00bab080` | `ff 67 09 a9` | stp xzr,x25,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bab084"></a> `00bab084` | `e0 43 05 fc` | stur d0,[sp, #0x54] | `FALL_THROUGH`
<a id="insn-00bab088"></a> `00bab088` | `ff 1f 00 f9` | str xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bab08c"></a> `00bab08c` | `f7 17 00 f9` | str x23,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bab090"></a> `00bab090` | `ac c9 02 94` | bl 0x00c5d740 | `UNCONDITIONAL_CALL`
<a id="insn-00bab094"></a> `00bab094` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab098"></a> `00bab098` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bab09c"></a> `00bab09c` | `77 06 00 39` | strb w23,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bab0a0"></a> `00bab0a0` | `28 0b 00 35` | cbnz w8,0x00bab204 | `CONDITIONAL_JUMP`
<a id="insn-00bab0a4"></a> `00bab0a4` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bab0a8"></a> `00bab0a8` | `36 ca 02 94` | bl 0x00c5d980 | `UNCONDITIONAL_CALL`
<a id="insn-00bab0ac"></a> `00bab0ac` | `e9 23 42 a9` | ldp x9,x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab0b0"></a> `00bab0b0` | `97 62 05 91` | add x23,x20,#0x158 | `FALL_THROUGH`
<a id="insn-00bab0b4"></a> `00bab0b4` | `09 01 09 eb` | subs x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00bab0b8"></a> `00bab0b8` | `40 04 00 54` | b.eq 0x00bab140 | `CONDITIONAL_JUMP`
<a id="insn-00bab0bc"></a> `00bab0bc` | `88 e2 40 f9` | ldr x8,[x20, #0x1c0] | `FALL_THROUGH`
<a id="insn-00bab0c0"></a> `00bab0c0` | `1f 1d 00 f1` | cmp x8,#0x7 | `FALL_THROUGH`
<a id="insn-00bab0c4"></a> `00bab0c4` | `68 00 00 54` | b.hi 0x00bab0d0 | `CONDITIONAL_JUMP`
<a id="insn-00bab0c8"></a> `00bab0c8` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bab0cc"></a> `00bab0cc` | `88 e2 00 f9` | str x8,[x20, #0x1c0] | `FALL_THROUGH`
<a id="insn-00bab0d0"></a> `00bab0d0` | `88 8a 41 b9` | ldr w8,[x20, #0x188] | `FALL_THROUGH`
<a id="insn-00bab0d4"></a> `00bab0d4` | `29 01 08 0b` | add w9,w9,w8 | `FALL_THROUGH`
<a id="insn-00bab0d8"></a> `00bab0d8` | `e9 03 09 4b` | neg w9,w9 | `FALL_THROUGH`
<a id="insn-00bab0dc"></a> `00bab0dc` | `38 09 40 f2` | ands x24,x9,#0x7 | `FALL_THROUGH`
<a id="insn-00bab0e0"></a> `00bab0e0` | `00 03 00 54` | b.eq 0x00bab140 | `CONDITIONAL_JUMP`
<a id="insn-00bab0e4"></a> `00bab0e4` | `89 ce 40 f9` | ldr x9,[x20, #0x198] | `FALL_THROUGH`
<a id="insn-00bab0e8"></a> `00bab0e8` | `8a a2 41 b9` | ldr w10,[x20, #0x1a0] | `FALL_THROUGH`
<a id="insn-00bab0ec"></a> `00bab0ec` | `2a 01 0a 4b` | sub w10,w9,w10 | `FALL_THROUGH`
<a id="insn-00bab0f0"></a> `00bab0f0` | `5f 01 18 eb` | cmp x10,x24 | `FALL_THROUGH`
<a id="insn-00bab0f4"></a> `00bab0f4` | `c2 00 00 54` | b.cs 0x00bab10c | `CONDITIONAL_JUMP`
<a id="insn-00bab0f8"></a> `00bab0f8` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bab0fc"></a> `00bab0fc` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bab100"></a> `00bab100` | `50 c8 02 94` | bl 0x00c5d240 | `UNCONDITIONAL_CALL`
<a id="insn-00bab104"></a> `00bab104` | `89 ce 40 f9` | ldr x9,[x20, #0x198] | `FALL_THROUGH`
<a id="insn-00bab108"></a> `00bab108` | `88 8a 41 b9` | ldr w8,[x20, #0x188] | `FALL_THROUGH`
<a id="insn-00bab10c"></a> `00bab10c` | `29 01 18 cb` | sub x9,x9,x24 | `FALL_THROUGH`
<a id="insn-00bab110"></a> `00bab110` | `08 01 18 0b` | add w8,w8,w24 | `FALL_THROUGH`
<a id="insn-00bab114"></a> `00bab114` | `1f 07 00 f1` | cmp x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bab118"></a> `00bab118` | `89 ce 00 f9` | str x9,[x20, #0x198] | `FALL_THROUGH`
<a id="insn-00bab11c"></a> `00bab11c` | `88 8a 01 b9` | str w8,[x20, #0x188] | `FALL_THROUGH`
<a id="insn-00bab120"></a> `00bab120` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00bab124"></a> `00bab124` | `e0 00 00 54` | b.eq 0x00bab140 | `CONDITIONAL_JUMP`
<a id="insn-00bab128"></a> `00bab128` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab12c"></a> `00bab12c` | `89 ce 40 f9` | ldr x9,[x20, #0x198] | `FALL_THROUGH`
<a id="insn-00bab130"></a> `00bab130` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab134"></a> `00bab134` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab138"></a> `00bab138` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00bab13c"></a> `00bab13c` | `81 ff ff 54` | b.ne 0x00bab12c | `CONDITIONAL_JUMP`
<a id="insn-00bab140"></a> `00bab140` | `e9 23 42 a9` | ldp x9,x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab144"></a> `00bab144` | `8a 07 00 b0` | adrp x10,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bab148"></a> `00bab148` | `4a 9d 44 f9` | ldr x10,[x10, #0x938] | `FALL_THROUGH`
<a id="insn-00bab14c"></a> `00bab14c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bab150"></a> `00bab150` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bab154"></a> `00bab154` | `02 01 09 cb` | sub x2,x8,x9 | `FALL_THROUGH`
<a id="insn-00bab158"></a> `00bab158` | `41 01 89 9a` | csel x1,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab15c"></a> `00bab15c` | `75 c8 02 94` | bl 0x00c5d330 | `UNCONDITIONAL_CALL`
<a id="insn-00bab160"></a> `00bab160` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bab164"></a> `00bab164` | `cb c7 02 94` | bl 0x00c5d090 | `UNCONDITIONAL_CALL`
<a id="insn-00bab168"></a> `00bab168` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab16c"></a> `00bab16c` | `28 03 00 37` | tbnz w8,#0x0,0x00bab1d0 | `CONDITIONAL_JUMP`
<a id="insn-00bab170"></a> `00bab170` | `ff 83 01 79` | strh wzr,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab174"></a> `00bab174` | `1f 00 00 14` | b 0x00bab1f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab178"></a> `00bab178` | `c8 7a 40 f9` | ldr x8,[x22, #0xf0] | `FALL_THROUGH`
<a id="insn-00bab17c"></a> `00bab17c` | `a3 02 40 f9` | ldr x3,[x21] | `FALL_THROUGH`
<a id="insn-00bab180"></a> `00bab180` | `e1 83 02 91` | add x1,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bab184"></a> `00bab184` | `e8 00 00 b4` | cbz x8,0x00bab1a0 | `CONDITIONAL_JUMP`
<a id="insn-00bab188"></a> `00bab188` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bab18c"></a> `00bab18c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bab190"></a> `00bab190` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bab194"></a> `00bab194` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00bab198"></a> `00bab198` | `6e c9 02 94` | bl 0x00c5d750 | `UNCONDITIONAL_CALL`
<a id="insn-00bab19c"></a> `00bab19c` | `08 00 00 14` | b 0x00bab1bc | `UNCONDITIONAL_JUMP`
<a id="insn-00bab1a0"></a> `00bab1a0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bab1a4"></a> `00bab1a4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bab1a8"></a> `00bab1a8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bab1ac"></a> `00bab1ac` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00bab1b0"></a> `00bab1b0` | `e5 03 1f aa` | mov x5,xzr | `FALL_THROUGH`
<a id="insn-00bab1b4"></a> `00bab1b4` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00bab1b8"></a> `00bab1b8` | `06 c9 02 94` | bl 0x00c5d5d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab1bc"></a> `00bab1bc` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab1c0"></a> `00bab1c0` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bab1c4"></a> `00bab1c4` | `77 06 00 39` | strb w23,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bab1c8"></a> `00bab1c8` | `e8 03 00 35` | cbnz w8,0x00bab244 | `CONDITIONAL_JUMP`
<a id="insn-00bab1cc"></a> `00bab1cc` | `30 00 00 14` | b 0x00bab28c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab1d0"></a> `00bab1d0` | `e8 6b 40 f9` | ldr x8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab1d4"></a> `00bab1d4` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bab1d8"></a> `00bab1d8` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab1dc"></a> `00bab1dc` | `ff 67 00 f9` | str xzr,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00bab1e0"></a> `00bab1e0` | `88 00 00 36` | tbz w8,#0x0,0x00bab1f0 | `CONDITIONAL_JUMP`
<a id="insn-00bab1e4"></a> `00bab1e4` | `e0 6b 40 f9` | ldr x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab1e8"></a> `00bab1e8` | `5a b7 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab1ec"></a> `00bab1ec` | `ff 63 00 f9` | str xzr,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab1f0"></a> `00bab1f0` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bab1f4"></a> `00bab1f4` | `e0 83 c0 3c` | ldur q0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab1f8"></a> `00bab1f8` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00bab1fc"></a> `00bab1fc` | `68 0b 00 f9` | str x8,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bab200"></a> `00bab200` | `60 03 80 3d` | str q0,[x27] | `FALL_THROUGH`
<a id="insn-00bab204"></a> `00bab204` | `e1 47 40 f9` | ldr x1,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00bab208"></a> `00bab208` | `20 83 01 91` | add x0,x25,#0x60 | `FALL_THROUGH`
<a id="insn-00bab20c"></a> `00bab20c` | `55 c6 02 94` | bl 0x00c5cb60 | `UNCONDITIONAL_CALL`
<a id="insn-00bab210"></a> `00bab210` | `e1 37 40 f9` | ldr x1,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bab214"></a> `00bab214` | `20 03 01 91` | add x0,x25,#0x40 | `FALL_THROUGH`
<a id="insn-00bab218"></a> `00bab218` | `56 c6 02 94` | bl 0x00c5cb70 | `UNCONDITIONAL_CALL`
<a id="insn-00bab21c"></a> `00bab21c` | `e0 1f 40 f9` | ldr x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bab220"></a> `00bab220` | `60 00 00 b4` | cbz x0,0x00bab22c | `CONDITIONAL_JUMP`
<a id="insn-00bab224"></a> `00bab224` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab228"></a> `00bab228` | `4a b7 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab22c"></a> `00bab22c` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab230"></a> `00bab230` | `60 00 00 b4` | cbz x0,0x00bab23c | `CONDITIONAL_JUMP`
<a id="insn-00bab234"></a> `00bab234` | `e0 17 00 f9` | str x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bab238"></a> `00bab238` | `46 b7 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab23c"></a> `00bab23c` | `97 02 00 34` | cbz w23,0x00bab28c | `CONDITIONAL_JUMP`
<a id="insn-00bab240"></a> `00bab240` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bab244"></a> `00bab244` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab248"></a> `00bab248` | `68 00 00 36` | tbz w8,#0x0,0x00bab254 | `CONDITIONAL_JUMP`
<a id="insn-00bab24c"></a> `00bab24c` | `e0 6b 40 f9` | ldr x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab250"></a> `00bab250` | `40 b7 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab254"></a> `00bab254` | `57 00 00 35` | cbnz w23,0x00bab25c | `CONDITIONAL_JUMP`
<a id="insn-00bab258"></a> `00bab258` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-00bab25c"></a> `00bab25c` | `88 17 40 f9` | ldr x8,[x28, #0x28] | `FALL_THROUGH`
<a id="insn-00bab260"></a> `00bab260` | `a9 83 59 f8` | ldur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00bab264"></a> `00bab264` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bab268"></a> `00bab268` | `81 0e 00 54` | b.ne 0x00bab438 | `CONDITIONAL_JUMP`
<a id="insn-00bab26c"></a> `00bab26c` | `fd 7b 55 a9` | ldp x29,x30,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bab270"></a> `00bab270` | `f4 4f 54 a9` | ldp x20,x19,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00bab274"></a> `00bab274` | `f6 57 53 a9` | ldp x22,x21,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bab278"></a> `00bab278` | `f8 5f 52 a9` | ldp x24,x23,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bab27c"></a> `00bab27c` | `fa 67 51 a9` | ldp x26,x25,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00bab280"></a> `00bab280` | `fc 6f 50 a9` | ldp x28,x27,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00bab284"></a> `00bab284` | `ff 83 05 91` | add sp,sp,#0x160 | `FALL_THROUGH`
<a id="insn-00bab288"></a> `00bab288` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bab28c"></a> `00bab28c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bab290"></a> `00bab290` | `97 de 42 f9` | ldr x23,[x20, #0x5b8] | `FALL_THROUGH`
<a id="insn-00bab294"></a> `00bab294` | `68 02 00 b4` | cbz x8,0x00bab2e0 | `CONDITIONAL_JUMP`
<a id="insn-00bab298"></a> `00bab298` | `09 09 80 52` | mov w9,#0x48 | `FALL_THROUGH`
<a id="insn-00bab29c"></a> `00bab29c` | `ea 08 80 92` | mov x10,#-0x48 | `FALL_THROUGH`
<a id="insn-00bab2a0"></a> `00bab2a0` | `0b fd 09 9b` | mneg x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00bab2a4"></a> `00bab2a4` | `09 7d 0a 9b` | mul x9,x8,x10 | `FALL_THROUGH`
<a id="insn-00bab2a8"></a> `00bab2a8` | `e8 02 0b 8b` | add x8,x23,x11 | `FALL_THROUGH`
<a id="insn-00bab2ac"></a> `00bab2ac` | `ea 22 01 d1` | sub x10,x23,#0x48 | `FALL_THROUGH`
<a id="insn-00bab2b0"></a> `00bab2b0` | `4b 21 40 f9` | ldr x11,[x10, #0x40] | `FALL_THROUGH`
<a id="insn-00bab2b4"></a> `00bab2b4` | `7f 01 16 eb` | cmp x11,x22 | `FALL_THROUGH`
<a id="insn-00bab2b8"></a> `00bab2b8` | `40 04 00 54` | b.eq 0x00bab340 | `CONDITIONAL_JUMP`
<a id="insn-00bab2bc"></a> `00bab2bc` | `6b b1 41 79` | ldrh w11,[x11, #0xd8] | `FALL_THROUGH`
<a id="insn-00bab2c0"></a> `00bab2c0` | `cc b2 41 79` | ldrh w12,[x22, #0xd8] | `FALL_THROUGH`
<a id="insn-00bab2c4"></a> `00bab2c4` | `7f 01 0c 6b` | cmp w11,w12 | `FALL_THROUGH`
<a id="insn-00bab2c8"></a> `00bab2c8` | `c3 00 00 54` | b.cc 0x00bab2e0 | `CONDITIONAL_JUMP`
<a id="insn-00bab2cc"></a> `00bab2cc` | `f7 03 0a aa` | mov x23,x10 | `FALL_THROUGH`
<a id="insn-00bab2d0"></a> `00bab2d0` | `29 21 01 91` | add x9,x9,#0x48 | `FALL_THROUGH`
<a id="insn-00bab2d4"></a> `00bab2d4` | `4a 21 01 d1` | sub x10,x10,#0x48 | `FALL_THROUGH`
<a id="insn-00bab2d8"></a> `00bab2d8` | `c9 fe ff b5` | cbnz x9,0x00bab2b0 | `CONDITIONAL_JUMP`
<a id="insn-00bab2dc"></a> `00bab2dc` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00bab2e0"></a> `00bab2e0` | `40 07 40 ad` | ldp q0,q1,[x26] | `FALL_THROUGH`
<a id="insn-00bab2e4"></a> `00bab2e4` | `e9 03 43 39` | ldrb w9,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab2e8"></a> `00bab2e8` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bab2ec"></a> `00bab2ec` | `08 81 00 91` | add x8,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bab2f0"></a> `00bab2f0` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab2f4"></a> `00bab2f4` | `e0 07 01 ad` | stp q0,q1,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab2f8"></a> `00bab2f8` | `ff 2b 00 f9` | str xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bab2fc"></a> `00bab2fc` | `c9 00 00 37` | tbnz w9,#0x0,0x00bab314 | `CONDITIONAL_JUMP`
<a id="insn-00bab300"></a> `00bab300` | `69 0b 40 f9` | ldr x9,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bab304"></a> `00bab304` | `60 03 c0 3d` | ldr q0,[x27] | `FALL_THROUGH`
<a id="insn-00bab308"></a> `00bab308` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bab30c"></a> `00bab30c` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00bab310"></a> `00bab310` | `34 00 00 14` | b 0x00bab3e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab314"></a> `00bab314` | `f8 67 40 f9` | ldr x24,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00bab318"></a> `00bab318` | `1f 43 00 b1` | cmn x24,#0x10 | `FALL_THROUGH`
<a id="insn-00bab31c"></a> `00bab31c` | `02 09 00 54` | b.cs 0x00bab43c | `CONDITIONAL_JUMP`
<a id="insn-00bab320"></a> `00bab320` | `f9 6b 40 f9` | ldr x25,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab324"></a> `00bab324` | `1f 5f 00 f1` | cmp x24,#0x17 | `FALL_THROUGH`
<a id="insn-00bab328"></a> `00bab328` | `22 04 00 54` | b.cs 0x00bab3ac | `CONDITIONAL_JUMP`
<a id="insn-00bab32c"></a> `00bab32c` | `09 7b 1f 53` | lsl w9,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00bab330"></a> `00bab330` | `1a 05 00 91` | add x26,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab334"></a> `00bab334` | `e9 03 01 39` | strb w9,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab338"></a> `00bab338` | `b8 04 00 b5` | cbnz x24,0x00bab3cc | `CONDITIONAL_JUMP`
<a id="insn-00bab33c"></a> `00bab33c` | `28 00 00 14` | b 0x00bab3dc | `UNCONDITIONAL_JUMP`
<a id="insn-00bab340"></a> `00bab340` | `a0 b8 ff b0` | adrp x0,0x2c0000 | `FALL_THROUGH`
<a id="insn-00bab344"></a> `00bab344` | `00 08 30 91` | add x0,x0,#0xc02 | `FALL_THROUGH`
<a id="insn-00bab348"></a> `00bab348` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bab34c"></a> `00bab34c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bab350"></a> `00bab350` | `80 b7 02 94` | bl 0x00c59150 | `UNCONDITIONAL_CALL`
<a id="insn-00bab354"></a> `00bab354` | `a0 b7 ff b0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00bab358"></a> `00bab358` | `00 a4 2e 91` | add x0,x0,#0xba9 | `FALL_THROUGH`
<a id="insn-00bab35c"></a> `00bab35c` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bab360"></a> `00bab360` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bab364"></a> `00bab364` | `7b b7 02 94` | bl 0x00c59150 | `UNCONDITIONAL_CALL`
<a id="insn-00bab368"></a> `00bab368` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bab36c"></a> `00bab36c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bab370"></a> `00bab370` | `28 c9 02 94` | bl 0x00c5d810 | `UNCONDITIONAL_CALL`
<a id="insn-00bab374"></a> `00bab374` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab378"></a> `00bab378` | `68 00 00 36` | tbz w8,#0x0,0x00bab384 | `CONDITIONAL_JUMP`
<a id="insn-00bab37c"></a> `00bab37c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab380"></a> `00bab380` | `f4 b6 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab384"></a> `00bab384` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab388"></a> `00bab388` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bab38c"></a> `00bab38c` | `69 02 00 79` | strh w9,[x19] | `FALL_THROUGH`
<a id="insn-00bab390"></a> `00bab390` | `68 00 00 36` | tbz w8,#0x0,0x00bab39c | `CONDITIONAL_JUMP`
<a id="insn-00bab394"></a> `00bab394` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bab398"></a> `00bab398` | `ee b6 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab39c"></a> `00bab39c` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bab3a0"></a> `00bab3a0` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab3a4"></a> `00bab3a4` | `48 f5 07 37` | tbnz w8,#0x0,0x00bab24c | `CONDITIONAL_JUMP`
<a id="insn-00bab3a8"></a> `00bab3a8` | `ab ff ff 17` | b 0x00bab254 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab3ac"></a> `00bab3ac` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00bab3b0"></a> `00bab3b0` | `1b ed 7c 92` | and x27,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00bab3b4"></a> `00bab3b4` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bab3b8"></a> `00bab3b8` | `de b6 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bab3bc"></a> `00bab3bc` | `68 03 40 b2` | orr x8,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bab3c0"></a> `00bab3c0` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bab3c4"></a> `00bab3c4` | `e8 63 04 a9` | stp x8,x24,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab3c8"></a> `00bab3c8` | `e0 2b 00 f9` | str x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bab3cc"></a> `00bab3cc` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00bab3d0"></a> `00bab3d0` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bab3d4"></a> `00bab3d4` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bab3d8"></a> `00bab3d8` | `32 b7 02 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab3dc"></a> `00bab3dc` | `5f 6b 38 38` | strb wzr,[x26, x24, LSL ] | `FALL_THROUGH`
<a id="insn-00bab3e0"></a> `00bab3e0` | `e8 b3 41 79` | ldrh w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00bab3e4"></a> `00bab3e4` | `80 c2 16 91` | add x0,x20,#0x5b0 | `FALL_THROUGH`
<a id="insn-00bab3e8"></a> `00bab3e8` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bab3ec"></a> `00bab3ec` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bab3f0"></a> `00bab3f0` | `e8 b3 00 79` | strh w8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bab3f4"></a> `00bab3f4` | `f6 33 00 f9` | str x22,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bab3f8"></a> `00bab3f8` | `3e cb 02 94` | bl 0x00c5e0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab3fc"></a> `00bab3fc` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab400"></a> `00bab400` | `68 00 00 36` | tbz w8,#0x0,0x00bab40c | `CONDITIONAL_JUMP`
<a id="insn-00bab404"></a> `00bab404` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bab408"></a> `00bab408` | `d2 b6 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab40c"></a> `00bab40c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bab410"></a> `00bab410` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00bab414"></a> `00bab414` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab418"></a> `00bab418` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00bab41c"></a> `00bab41c` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab420"></a> `00bab420` | `68 f1 07 37` | tbnz w8,#0x0,0x00bab24c | `CONDITIONAL_JUMP`
<a id="insn-00bab424"></a> `00bab424` | `8c ff ff 17` | b 0x00bab254 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab428"></a> `00bab428` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bab42c"></a> `00bab42c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bab430"></a> `00bab430` | `d8 c8 02 94` | bl 0x00c5d790 | `UNCONDITIONAL_CALL`
<a id="insn-00bab434"></a> `00bab434` | `bd fe ff 17` | b 0x00baaf28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab438"></a> `00bab438` | `d2 b6 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`
<a id="insn-00bab43c"></a> `00bab43c` | `69 c3 02 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baadcc`](#insn-00baadcc) 範囲 `[['00baadcc', '00baadeb']]`
  - `FALL_THROUGH` [`00baade8`](#insn-00baade8) → [`00baadec`](#insn-00baadec)
- ブロック [`00baadec`](#insn-00baadec) 範囲 `[['00baadec', '00baae0b']]`
  - `FALL_THROUGH` [`00baae08`](#insn-00baae08) → [`00baae0c`](#insn-00baae0c)
- ブロック [`00baae0c`](#insn-00baae0c) 範囲 `[['00baae0c', '00baae27']]`
  - `CONDITIONAL_JUMP` [`00baae24`](#insn-00baae24) → [`00baae48`](#insn-00baae48)
  - `FALL_THROUGH` [`00baae24`](#insn-00baae24) → [`00baae28`](#insn-00baae28)
- ブロック [`00baae28`](#insn-00baae28) 範囲 `[['00baae28', '00baae37']]`
  - `FALL_THROUGH` [`00baae34`](#insn-00baae34) → [`00baae38`](#insn-00baae38)
- ブロック [`00baae38`](#insn-00baae38) 範囲 `[['00baae38', '00baae47']]`
  - `CONDITIONAL_JUMP` [`00baae44`](#insn-00baae44) → [`00baaf18`](#insn-00baaf18)
  - `FALL_THROUGH` [`00baae44`](#insn-00baae44) → [`00baae48`](#insn-00baae48)
- ブロック [`00baae48`](#insn-00baae48) 範囲 `[['00baae48', '00baae5b']]`
  - `FALL_THROUGH` [`00baae58`](#insn-00baae58) → [`00baae5c`](#insn-00baae5c)
- ブロック [`00baae5c`](#insn-00baae5c) 範囲 `[['00baae5c', '00baae5f']]`
  - `CONDITIONAL_JUMP` [`00baae5c`](#insn-00baae5c) → [`00baaf00`](#insn-00baaf00)
  - `FALL_THROUGH` [`00baae5c`](#insn-00baae5c) → [`00baae60`](#insn-00baae60)
- ブロック [`00baae60`](#insn-00baae60) 範囲 `[['00baae60', '00baae67']]`
  - `CONDITIONAL_JUMP` [`00baae64`](#insn-00baae64) → [`00baaf00`](#insn-00baaf00)
  - `FALL_THROUGH` [`00baae64`](#insn-00baae64) → [`00baae68`](#insn-00baae68)
- ブロック [`00baae68`](#insn-00baae68) 範囲 `[['00baae68', '00baae73']]`
  - `CONDITIONAL_JUMP` [`00baae70`](#insn-00baae70) → [`00baaec4`](#insn-00baaec4)
  - `FALL_THROUGH` [`00baae70`](#insn-00baae70) → [`00baae74`](#insn-00baae74)
- ブロック [`00baae74`](#insn-00baae74) 範囲 `[['00baae74', '00baae87']]`
  - `FALL_THROUGH` [`00baae84`](#insn-00baae84) → [`00baae88`](#insn-00baae88)
- ブロック [`00baae88`](#insn-00baae88) 範囲 `[['00baae88', '00baae93']]`
  - `CONDITIONAL_JUMP` [`00baae90`](#insn-00baae90) → [`00baaec4`](#insn-00baaec4)
  - `FALL_THROUGH` [`00baae90`](#insn-00baae90) → [`00baae94`](#insn-00baae94)
- ブロック [`00baae94`](#insn-00baae94) 範囲 `[['00baae94', '00baaea7']]`
  - `FALL_THROUGH` [`00baaea4`](#insn-00baaea4) → [`00baaea8`](#insn-00baaea8)
- ブロック [`00baaea8`](#insn-00baaea8) 範囲 `[['00baaea8', '00baaeb3']]`
  - `CONDITIONAL_JUMP` [`00baaeb0`](#insn-00baaeb0) → [`00baaec4`](#insn-00baaec4)
  - `FALL_THROUGH` [`00baaeb0`](#insn-00baaeb0) → [`00baaeb4`](#insn-00baaeb4)
- ブロック [`00baaeb4`](#insn-00baaeb4) 範囲 `[['00baaeb4', '00baaec3']]`
  - `CONDITIONAL_JUMP` [`00baaec0`](#insn-00baaec0) → [`00bab428`](#insn-00bab428)
  - `FALL_THROUGH` [`00baaec0`](#insn-00baaec0) → [`00baaec4`](#insn-00baaec4)
- ブロック [`00baaec4`](#insn-00baaec4) 範囲 `[['00baaec4', '00baaed3']]`
  - `FALL_THROUGH` [`00baaed0`](#insn-00baaed0) → [`00baaed4`](#insn-00baaed4)
- ブロック [`00baaed4`](#insn-00baaed4) 範囲 `[['00baaed4', '00baaeeb']]`
  - `CONDITIONAL_JUMP` [`00baaee8`](#insn-00baaee8) → [`00baaf9c`](#insn-00baaf9c)
  - `FALL_THROUGH` [`00baaee8`](#insn-00baaee8) → [`00baaeec`](#insn-00baaeec)
- ブロック [`00baaeec`](#insn-00baaeec) 範囲 `[['00baaeec', '00baaeff']]`
  - `UNCONDITIONAL_JUMP` [`00baaefc`](#insn-00baaefc) → [`00bab018`](#insn-00bab018)
- ブロック [`00baaf00`](#insn-00baaf00) 範囲 `[['00baaf00', '00baaf07']]`
  - `CONDITIONAL_JUMP` [`00baaf04`](#insn-00baaf04) → [`00baaf3c`](#insn-00baaf3c)
  - `FALL_THROUGH` [`00baaf04`](#insn-00baaf04) → [`00baaf08`](#insn-00baaf08)
- ブロック [`00baaf08`](#insn-00baaf08) 範囲 `[['00baaf08', '00baaf17']]`
  - `UNCONDITIONAL_JUMP` [`00baaf14`](#insn-00baaf14) → [`00baaf28`](#insn-00baaf28)
- ブロック [`00baaf18`](#insn-00baaf18) 範囲 `[['00baaf18', '00baaf27']]`
  - `FALL_THROUGH` [`00baaf24`](#insn-00baaf24) → [`00baaf28`](#insn-00baaf28)
- ブロック [`00baaf28`](#insn-00baaf28) 範囲 `[['00baaf28', '00baaf37']]`
  - `CONDITIONAL_JUMP` [`00baaf34`](#insn-00baaf34) → [`00bab25c`](#insn-00bab25c)
  - `FALL_THROUGH` [`00baaf34`](#insn-00baaf34) → [`00baaf38`](#insn-00baaf38)
- ブロック [`00baaf38`](#insn-00baaf38) 範囲 `[['00baaf38', '00baaf3b']]`
  - `UNCONDITIONAL_JUMP` [`00baaf38`](#insn-00baaf38) → [`00bab258`](#insn-00bab258)
- ブロック [`00baaf3c`](#insn-00baaf3c) 範囲 `[['00baaf3c', '00baaf5b']]`
  - `FALL_THROUGH` [`00baaf58`](#insn-00baaf58) → [`00baaf5c`](#insn-00baaf5c)
- ブロック [`00baaf5c`](#insn-00baaf5c) 範囲 `[['00baaf5c', '00baaf77']]`
  - `CONDITIONAL_JUMP` [`00baaf74`](#insn-00baaf74) → [`00baaf80`](#insn-00baaf80)
  - `FALL_THROUGH` [`00baaf74`](#insn-00baaf74) → [`00baaf78`](#insn-00baaf78)
- ブロック [`00baaf78`](#insn-00baaf78) 範囲 `[['00baaf78', '00baaf7f']]`
  - `FALL_THROUGH` [`00baaf7c`](#insn-00baaf7c) → [`00baaf80`](#insn-00baaf80)
- ブロック [`00baaf80`](#insn-00baaf80) 範囲 `[['00baaf80', '00baaf8f']]`
  - `CONDITIONAL_JUMP` [`00baaf8c`](#insn-00baaf8c) → [`00bab25c`](#insn-00bab25c)
  - `FALL_THROUGH` [`00baaf8c`](#insn-00baaf8c) → [`00baaf90`](#insn-00baaf90)
- ブロック [`00baaf90`](#insn-00baaf90) 範囲 `[['00baaf90', '00baaf93']]`
  - `FALL_THROUGH` [`00baaf90`](#insn-00baaf90) → [`00baaf94`](#insn-00baaf94)
- ブロック [`00baaf94`](#insn-00baaf94) 範囲 `[['00baaf94', '00baaf9b']]`
  - `UNCONDITIONAL_JUMP` [`00baaf98`](#insn-00baaf98) → [`00bab25c`](#insn-00bab25c)
- ブロック [`00baaf9c`](#insn-00baaf9c) 範囲 `[['00baaf9c', '00baafa7']]`
  - `CONDITIONAL_JUMP` [`00baafa4`](#insn-00baafa4) → [`00bab43c`](#insn-00bab43c)
  - `FALL_THROUGH` [`00baafa4`](#insn-00baafa4) → [`00baafa8`](#insn-00baafa8)
- ブロック [`00baafa8`](#insn-00baafa8) 範囲 `[['00baafa8', '00baafb3']]`
  - `CONDITIONAL_JUMP` [`00baafb0`](#insn-00baafb0) → [`00baafc8`](#insn-00baafc8)
  - `FALL_THROUGH` [`00baafb0`](#insn-00baafb0) → [`00baafb4`](#insn-00baafb4)
- ブロック [`00baafb4`](#insn-00baafb4) 範囲 `[['00baafb4', '00baafc3']]`
  - `CONDITIONAL_JUMP` [`00baafc0`](#insn-00baafc0) → [`00bab000`](#insn-00bab000)
  - `FALL_THROUGH` [`00baafc0`](#insn-00baafc0) → [`00baafc4`](#insn-00baafc4)
- ブロック [`00baafc4`](#insn-00baafc4) 範囲 `[['00baafc4', '00baafc7']]`
  - `UNCONDITIONAL_JUMP` [`00baafc4`](#insn-00baafc4) → [`00bab010`](#insn-00bab010)
- ブロック [`00baafc8`](#insn-00baafc8) 範囲 `[['00baafc8', '00baafd3']]`
  - `FALL_THROUGH` [`00baafd0`](#insn-00baafd0) → [`00baafd4`](#insn-00baafd4)
- ブロック [`00baafd4`](#insn-00baafd4) 範囲 `[['00baafd4', '00baafff']]`
  - `FALL_THROUGH` [`00baaffc`](#insn-00baaffc) → [`00bab000`](#insn-00bab000)
- ブロック [`00bab000`](#insn-00bab000) 範囲 `[['00bab000', '00bab00f']]`
  - `FALL_THROUGH` [`00bab00c`](#insn-00bab00c) → [`00bab010`](#insn-00bab010)
- ブロック [`00bab010`](#insn-00bab010) 範囲 `[['00bab010', '00bab017']]`
  - `FALL_THROUGH` [`00bab014`](#insn-00bab014) → [`00bab018`](#insn-00bab018)
- ブロック [`00bab018`](#insn-00bab018) 範囲 `[['00bab018', '00bab023']]`
  - `FALL_THROUGH` [`00bab020`](#insn-00bab020) → [`00bab024`](#insn-00bab024)
- ブロック [`00bab024`](#insn-00bab024) 範囲 `[['00bab024', '00bab027']]`
  - `CONDITIONAL_JUMP` [`00bab024`](#insn-00bab024) → [`00bab178`](#insn-00bab178)
  - `FALL_THROUGH` [`00bab024`](#insn-00bab024) → [`00bab028`](#insn-00bab028)
- ブロック [`00bab028`](#insn-00bab028) 範囲 `[['00bab028', '00bab04f']]`
  - `FALL_THROUGH` [`00bab04c`](#insn-00bab04c) → [`00bab050`](#insn-00bab050)
- ブロック [`00bab050`](#insn-00bab050) 範囲 `[['00bab050', '00bab06f']]`
  - `FALL_THROUGH` [`00bab06c`](#insn-00bab06c) → [`00bab070`](#insn-00bab070)
- ブロック [`00bab070`](#insn-00bab070) 範囲 `[['00bab070', '00bab09b']]`
  - `FALL_THROUGH` [`00bab098`](#insn-00bab098) → [`00bab09c`](#insn-00bab09c)
- ブロック [`00bab09c`](#insn-00bab09c) 範囲 `[['00bab09c', '00bab0a3']]`
  - `CONDITIONAL_JUMP` [`00bab0a0`](#insn-00bab0a0) → [`00bab204`](#insn-00bab204)
  - `FALL_THROUGH` [`00bab0a0`](#insn-00bab0a0) → [`00bab0a4`](#insn-00bab0a4)
- ブロック [`00bab0a4`](#insn-00bab0a4) 範囲 `[['00bab0a4', '00bab0bb']]`
  - `CONDITIONAL_JUMP` [`00bab0b8`](#insn-00bab0b8) → [`00bab140`](#insn-00bab140)
  - `FALL_THROUGH` [`00bab0b8`](#insn-00bab0b8) → [`00bab0bc`](#insn-00bab0bc)
- ブロック [`00bab0bc`](#insn-00bab0bc) 範囲 `[['00bab0bc', '00bab0bf']]`
  - `FALL_THROUGH` [`00bab0bc`](#insn-00bab0bc) → [`00bab0c0`](#insn-00bab0c0)
- ブロック [`00bab0c0`](#insn-00bab0c0) 範囲 `[['00bab0c0', '00bab0c7']]`
  - `CONDITIONAL_JUMP` [`00bab0c4`](#insn-00bab0c4) → [`00bab0d0`](#insn-00bab0d0)
  - `FALL_THROUGH` [`00bab0c4`](#insn-00bab0c4) → [`00bab0c8`](#insn-00bab0c8)
- ブロック [`00bab0c8`](#insn-00bab0c8) 範囲 `[['00bab0c8', '00bab0cf']]`
  - `FALL_THROUGH` [`00bab0cc`](#insn-00bab0cc) → [`00bab0d0`](#insn-00bab0d0)
- ブロック [`00bab0d0`](#insn-00bab0d0) 範囲 `[['00bab0d0', '00bab0e3']]`
  - `CONDITIONAL_JUMP` [`00bab0e0`](#insn-00bab0e0) → [`00bab140`](#insn-00bab140)
  - `FALL_THROUGH` [`00bab0e0`](#insn-00bab0e0) → [`00bab0e4`](#insn-00bab0e4)
- ブロック [`00bab0e4`](#insn-00bab0e4) 範囲 `[['00bab0e4', '00bab0eb']]`
  - `FALL_THROUGH` [`00bab0e8`](#insn-00bab0e8) → [`00bab0ec`](#insn-00bab0ec)
- ブロック [`00bab0ec`](#insn-00bab0ec) 範囲 `[['00bab0ec', '00bab0f7']]`
  - `CONDITIONAL_JUMP` [`00bab0f4`](#insn-00bab0f4) → [`00bab10c`](#insn-00bab10c)
  - `FALL_THROUGH` [`00bab0f4`](#insn-00bab0f4) → [`00bab0f8`](#insn-00bab0f8)
- ブロック [`00bab0f8`](#insn-00bab0f8) 範囲 `[['00bab0f8', '00bab107']]`
  - `FALL_THROUGH` [`00bab104`](#insn-00bab104) → [`00bab108`](#insn-00bab108)
- ブロック [`00bab108`](#insn-00bab108) 範囲 `[['00bab108', '00bab10b']]`
  - `FALL_THROUGH` [`00bab108`](#insn-00bab108) → [`00bab10c`](#insn-00bab10c)
- ブロック [`00bab10c`](#insn-00bab10c) 範囲 `[['00bab10c', '00bab127']]`
  - `CONDITIONAL_JUMP` [`00bab124`](#insn-00bab124) → [`00bab140`](#insn-00bab140)
  - `FALL_THROUGH` [`00bab124`](#insn-00bab124) → [`00bab128`](#insn-00bab128)
- ブロック [`00bab128`](#insn-00bab128) 範囲 `[['00bab128', '00bab12b']]`
  - `FALL_THROUGH` [`00bab128`](#insn-00bab128) → [`00bab12c`](#insn-00bab12c)
- ブロック [`00bab12c`](#insn-00bab12c) 範囲 `[['00bab12c', '00bab133']]`
  - `FALL_THROUGH` [`00bab130`](#insn-00bab130) → [`00bab134`](#insn-00bab134)
- ブロック [`00bab134`](#insn-00bab134) 範囲 `[['00bab134', '00bab13f']]`
  - `CONDITIONAL_JUMP` [`00bab13c`](#insn-00bab13c) → [`00bab12c`](#insn-00bab12c)
  - `FALL_THROUGH` [`00bab13c`](#insn-00bab13c) → [`00bab140`](#insn-00bab140)
- ブロック [`00bab140`](#insn-00bab140) 範囲 `[['00bab140', '00bab157']]`
  - `FALL_THROUGH` [`00bab154`](#insn-00bab154) → [`00bab158`](#insn-00bab158)
- ブロック [`00bab158`](#insn-00bab158) 範囲 `[['00bab158', '00bab16f']]`
  - `CONDITIONAL_JUMP` [`00bab16c`](#insn-00bab16c) → [`00bab1d0`](#insn-00bab1d0)
  - `FALL_THROUGH` [`00bab16c`](#insn-00bab16c) → [`00bab170`](#insn-00bab170)
- ブロック [`00bab170`](#insn-00bab170) 範囲 `[['00bab170', '00bab177']]`
  - `UNCONDITIONAL_JUMP` [`00bab174`](#insn-00bab174) → [`00bab1f0`](#insn-00bab1f0)
- ブロック [`00bab178`](#insn-00bab178) 範囲 `[['00bab178', '00bab183']]`
  - `FALL_THROUGH` [`00bab180`](#insn-00bab180) → [`00bab184`](#insn-00bab184)
- ブロック [`00bab184`](#insn-00bab184) 範囲 `[['00bab184', '00bab187']]`
  - `CONDITIONAL_JUMP` [`00bab184`](#insn-00bab184) → [`00bab1a0`](#insn-00bab1a0)
  - `FALL_THROUGH` [`00bab184`](#insn-00bab184) → [`00bab188`](#insn-00bab188)
- ブロック [`00bab188`](#insn-00bab188) 範囲 `[['00bab188', '00bab19f']]`
  - `UNCONDITIONAL_JUMP` [`00bab19c`](#insn-00bab19c) → [`00bab1bc`](#insn-00bab1bc)
- ブロック [`00bab1a0`](#insn-00bab1a0) 範囲 `[['00bab1a0', '00bab1a3']]`
  - `FALL_THROUGH` [`00bab1a0`](#insn-00bab1a0) → [`00bab1a4`](#insn-00bab1a4)
- ブロック [`00bab1a4`](#insn-00bab1a4) 範囲 `[['00bab1a4', '00bab1af']]`
  - `FALL_THROUGH` [`00bab1ac`](#insn-00bab1ac) → [`00bab1b0`](#insn-00bab1b0)
- ブロック [`00bab1b0`](#insn-00bab1b0) 範囲 `[['00bab1b0', '00bab1bb']]`
  - `FALL_THROUGH` [`00bab1b8`](#insn-00bab1b8) → [`00bab1bc`](#insn-00bab1bc)
- ブロック [`00bab1bc`](#insn-00bab1bc) 範囲 `[['00bab1bc', '00bab1cb']]`
  - `CONDITIONAL_JUMP` [`00bab1c8`](#insn-00bab1c8) → [`00bab244`](#insn-00bab244)
  - `FALL_THROUGH` [`00bab1c8`](#insn-00bab1c8) → [`00bab1cc`](#insn-00bab1cc)
- ブロック [`00bab1cc`](#insn-00bab1cc) 範囲 `[['00bab1cc', '00bab1cf']]`
  - `UNCONDITIONAL_JUMP` [`00bab1cc`](#insn-00bab1cc) → [`00bab28c`](#insn-00bab28c)
- ブロック [`00bab1d0`](#insn-00bab1d0) 範囲 `[['00bab1d0', '00bab1e3']]`
  - `CONDITIONAL_JUMP` [`00bab1e0`](#insn-00bab1e0) → [`00bab1f0`](#insn-00bab1f0)
  - `FALL_THROUGH` [`00bab1e0`](#insn-00bab1e0) → [`00bab1e4`](#insn-00bab1e4)
- ブロック [`00bab1e4`](#insn-00bab1e4) 範囲 `[['00bab1e4', '00bab1ef']]`
  - `FALL_THROUGH` [`00bab1ec`](#insn-00bab1ec) → [`00bab1f0`](#insn-00bab1f0)
- ブロック [`00bab1f0`](#insn-00bab1f0) 範囲 `[['00bab1f0', '00bab203']]`
  - `FALL_THROUGH` [`00bab200`](#insn-00bab200) → [`00bab204`](#insn-00bab204)
- ブロック [`00bab204`](#insn-00bab204) 範囲 `[['00bab204', '00bab223']]`
  - `CONDITIONAL_JUMP` [`00bab220`](#insn-00bab220) → [`00bab22c`](#insn-00bab22c)
  - `FALL_THROUGH` [`00bab220`](#insn-00bab220) → [`00bab224`](#insn-00bab224)
- ブロック [`00bab224`](#insn-00bab224) 範囲 `[['00bab224', '00bab22b']]`
  - `FALL_THROUGH` [`00bab228`](#insn-00bab228) → [`00bab22c`](#insn-00bab22c)
- ブロック [`00bab22c`](#insn-00bab22c) 範囲 `[['00bab22c', '00bab233']]`
  - `CONDITIONAL_JUMP` [`00bab230`](#insn-00bab230) → [`00bab23c`](#insn-00bab23c)
  - `FALL_THROUGH` [`00bab230`](#insn-00bab230) → [`00bab234`](#insn-00bab234)
- ブロック [`00bab234`](#insn-00bab234) 範囲 `[['00bab234', '00bab23b']]`
  - `FALL_THROUGH` [`00bab238`](#insn-00bab238) → [`00bab23c`](#insn-00bab23c)
- ブロック [`00bab23c`](#insn-00bab23c) 範囲 `[['00bab23c', '00bab23f']]`
  - `CONDITIONAL_JUMP` [`00bab23c`](#insn-00bab23c) → [`00bab28c`](#insn-00bab28c)
  - `FALL_THROUGH` [`00bab23c`](#insn-00bab23c) → [`00bab240`](#insn-00bab240)
- ブロック [`00bab240`](#insn-00bab240) 範囲 `[['00bab240', '00bab243']]`
  - `FALL_THROUGH` [`00bab240`](#insn-00bab240) → [`00bab244`](#insn-00bab244)
- ブロック [`00bab244`](#insn-00bab244) 範囲 `[['00bab244', '00bab24b']]`
  - `CONDITIONAL_JUMP` [`00bab248`](#insn-00bab248) → [`00bab254`](#insn-00bab254)
  - `FALL_THROUGH` [`00bab248`](#insn-00bab248) → [`00bab24c`](#insn-00bab24c)
- ブロック [`00bab24c`](#insn-00bab24c) 範囲 `[['00bab24c', '00bab253']]`
  - `FALL_THROUGH` [`00bab250`](#insn-00bab250) → [`00bab254`](#insn-00bab254)
- ブロック [`00bab254`](#insn-00bab254) 範囲 `[['00bab254', '00bab257']]`
  - `CONDITIONAL_JUMP` [`00bab254`](#insn-00bab254) → [`00bab25c`](#insn-00bab25c)
  - `FALL_THROUGH` [`00bab254`](#insn-00bab254) → [`00bab258`](#insn-00bab258)
- ブロック [`00bab258`](#insn-00bab258) 範囲 `[['00bab258', '00bab25b']]`
  - `FALL_THROUGH` [`00bab258`](#insn-00bab258) → [`00bab25c`](#insn-00bab25c)
- ブロック [`00bab25c`](#insn-00bab25c) 範囲 `[['00bab25c', '00bab26b']]`
  - `CONDITIONAL_JUMP` [`00bab268`](#insn-00bab268) → [`00bab438`](#insn-00bab438)
  - `FALL_THROUGH` [`00bab268`](#insn-00bab268) → [`00bab26c`](#insn-00bab26c)
- ブロック [`00bab26c`](#insn-00bab26c) 範囲 `[['00bab26c', '00bab273']]`
  - `FALL_THROUGH` [`00bab270`](#insn-00bab270) → [`00bab274`](#insn-00bab274)
- ブロック [`00bab274`](#insn-00bab274) 範囲 `[['00bab274', '00bab28b']]`
- ブロック [`00bab28c`](#insn-00bab28c) 範囲 `[['00bab28c', '00bab297']]`
  - `CONDITIONAL_JUMP` [`00bab294`](#insn-00bab294) → [`00bab2e0`](#insn-00bab2e0)
  - `FALL_THROUGH` [`00bab294`](#insn-00bab294) → [`00bab298`](#insn-00bab298)
- ブロック [`00bab298`](#insn-00bab298) 範囲 `[['00bab298', '00bab2ab']]`
  - `FALL_THROUGH` [`00bab2a8`](#insn-00bab2a8) → [`00bab2ac`](#insn-00bab2ac)
- ブロック [`00bab2ac`](#insn-00bab2ac) 範囲 `[['00bab2ac', '00bab2af']]`
  - `FALL_THROUGH` [`00bab2ac`](#insn-00bab2ac) → [`00bab2b0`](#insn-00bab2b0)
- ブロック [`00bab2b0`](#insn-00bab2b0) 範囲 `[['00bab2b0', '00bab2bb']]`
  - `CONDITIONAL_JUMP` [`00bab2b8`](#insn-00bab2b8) → [`00bab340`](#insn-00bab340)
  - `FALL_THROUGH` [`00bab2b8`](#insn-00bab2b8) → [`00bab2bc`](#insn-00bab2bc)
- ブロック [`00bab2bc`](#insn-00bab2bc) 範囲 `[['00bab2bc', '00bab2cb']]`
  - `CONDITIONAL_JUMP` [`00bab2c8`](#insn-00bab2c8) → [`00bab2e0`](#insn-00bab2e0)
  - `FALL_THROUGH` [`00bab2c8`](#insn-00bab2c8) → [`00bab2cc`](#insn-00bab2cc)
- ブロック [`00bab2cc`](#insn-00bab2cc) 範囲 `[['00bab2cc', '00bab2db']]`
  - `CONDITIONAL_JUMP` [`00bab2d8`](#insn-00bab2d8) → [`00bab2b0`](#insn-00bab2b0)
  - `FALL_THROUGH` [`00bab2d8`](#insn-00bab2d8) → [`00bab2dc`](#insn-00bab2dc)
- ブロック [`00bab2dc`](#insn-00bab2dc) 範囲 `[['00bab2dc', '00bab2df']]`
  - `FALL_THROUGH` [`00bab2dc`](#insn-00bab2dc) → [`00bab2e0`](#insn-00bab2e0)
- ブロック [`00bab2e0`](#insn-00bab2e0) 範囲 `[['00bab2e0', '00bab2eb']]`
  - `FALL_THROUGH` [`00bab2e8`](#insn-00bab2e8) → [`00bab2ec`](#insn-00bab2ec)
- ブロック [`00bab2ec`](#insn-00bab2ec) 範囲 `[['00bab2ec', '00bab2ff']]`
  - `CONDITIONAL_JUMP` [`00bab2fc`](#insn-00bab2fc) → [`00bab314`](#insn-00bab314)
  - `FALL_THROUGH` [`00bab2fc`](#insn-00bab2fc) → [`00bab300`](#insn-00bab300)
- ブロック [`00bab300`](#insn-00bab300) 範囲 `[['00bab300', '00bab313']]`
  - `UNCONDITIONAL_JUMP` [`00bab310`](#insn-00bab310) → [`00bab3e0`](#insn-00bab3e0)
- ブロック [`00bab314`](#insn-00bab314) 範囲 `[['00bab314', '00bab317']]`
  - `FALL_THROUGH` [`00bab314`](#insn-00bab314) → [`00bab318`](#insn-00bab318)
- ブロック [`00bab318`](#insn-00bab318) 範囲 `[['00bab318', '00bab31f']]`
  - `CONDITIONAL_JUMP` [`00bab31c`](#insn-00bab31c) → [`00bab43c`](#insn-00bab43c)
  - `FALL_THROUGH` [`00bab31c`](#insn-00bab31c) → [`00bab320`](#insn-00bab320)
- ブロック [`00bab320`](#insn-00bab320) 範囲 `[['00bab320', '00bab32b']]`
  - `CONDITIONAL_JUMP` [`00bab328`](#insn-00bab328) → [`00bab3ac`](#insn-00bab3ac)
  - `FALL_THROUGH` [`00bab328`](#insn-00bab328) → [`00bab32c`](#insn-00bab32c)
- ブロック [`00bab32c`](#insn-00bab32c) 範囲 `[['00bab32c', '00bab33b']]`
  - `CONDITIONAL_JUMP` [`00bab338`](#insn-00bab338) → [`00bab3cc`](#insn-00bab3cc)
  - `FALL_THROUGH` [`00bab338`](#insn-00bab338) → [`00bab33c`](#insn-00bab33c)
- ブロック [`00bab33c`](#insn-00bab33c) 範囲 `[['00bab33c', '00bab33f']]`
  - `UNCONDITIONAL_JUMP` [`00bab33c`](#insn-00bab33c) → [`00bab3dc`](#insn-00bab3dc)
- ブロック [`00bab340`](#insn-00bab340) 範囲 `[['00bab340', '00bab367']]`
  - `FALL_THROUGH` [`00bab364`](#insn-00bab364) → [`00bab368`](#insn-00bab368)
- ブロック [`00bab368`](#insn-00bab368) 範囲 `[['00bab368', '00bab37b']]`
  - `CONDITIONAL_JUMP` [`00bab378`](#insn-00bab378) → [`00bab384`](#insn-00bab384)
  - `FALL_THROUGH` [`00bab378`](#insn-00bab378) → [`00bab37c`](#insn-00bab37c)
- ブロック [`00bab37c`](#insn-00bab37c) 範囲 `[['00bab37c', '00bab383']]`
  - `FALL_THROUGH` [`00bab380`](#insn-00bab380) → [`00bab384`](#insn-00bab384)
- ブロック [`00bab384`](#insn-00bab384) 範囲 `[['00bab384', '00bab387']]`
  - `FALL_THROUGH` [`00bab384`](#insn-00bab384) → [`00bab388`](#insn-00bab388)
- ブロック [`00bab388`](#insn-00bab388) 範囲 `[['00bab388', '00bab393']]`
  - `CONDITIONAL_JUMP` [`00bab390`](#insn-00bab390) → [`00bab39c`](#insn-00bab39c)
  - `FALL_THROUGH` [`00bab390`](#insn-00bab390) → [`00bab394`](#insn-00bab394)
- ブロック [`00bab394`](#insn-00bab394) 範囲 `[['00bab394', '00bab39b']]`
  - `FALL_THROUGH` [`00bab398`](#insn-00bab398) → [`00bab39c`](#insn-00bab39c)
- ブロック [`00bab39c`](#insn-00bab39c) 範囲 `[['00bab39c', '00bab3a7']]`
  - `CONDITIONAL_JUMP` [`00bab3a4`](#insn-00bab3a4) → [`00bab24c`](#insn-00bab24c)
  - `FALL_THROUGH` [`00bab3a4`](#insn-00bab3a4) → [`00bab3a8`](#insn-00bab3a8)
- ブロック [`00bab3a8`](#insn-00bab3a8) 範囲 `[['00bab3a8', '00bab3ab']]`
  - `UNCONDITIONAL_JUMP` [`00bab3a8`](#insn-00bab3a8) → [`00bab254`](#insn-00bab254)
- ブロック [`00bab3ac`](#insn-00bab3ac) 範囲 `[['00bab3ac', '00bab3b3']]`
  - `FALL_THROUGH` [`00bab3b0`](#insn-00bab3b0) → [`00bab3b4`](#insn-00bab3b4)
- ブロック [`00bab3b4`](#insn-00bab3b4) 範囲 `[['00bab3b4', '00bab3cb']]`
  - `FALL_THROUGH` [`00bab3c8`](#insn-00bab3c8) → [`00bab3cc`](#insn-00bab3cc)
- ブロック [`00bab3cc`](#insn-00bab3cc) 範囲 `[['00bab3cc', '00bab3d7']]`
  - `FALL_THROUGH` [`00bab3d4`](#insn-00bab3d4) → [`00bab3d8`](#insn-00bab3d8)
- ブロック [`00bab3d8`](#insn-00bab3d8) 範囲 `[['00bab3d8', '00bab3db']]`
  - `FALL_THROUGH` [`00bab3d8`](#insn-00bab3d8) → [`00bab3dc`](#insn-00bab3dc)
- ブロック [`00bab3dc`](#insn-00bab3dc) 範囲 `[['00bab3dc', '00bab3df']]`
  - `FALL_THROUGH` [`00bab3dc`](#insn-00bab3dc) → [`00bab3e0`](#insn-00bab3e0)
- ブロック [`00bab3e0`](#insn-00bab3e0) 範囲 `[['00bab3e0', '00bab403']]`
  - `CONDITIONAL_JUMP` [`00bab400`](#insn-00bab400) → [`00bab40c`](#insn-00bab40c)
  - `FALL_THROUGH` [`00bab400`](#insn-00bab400) → [`00bab404`](#insn-00bab404)
- ブロック [`00bab404`](#insn-00bab404) 範囲 `[['00bab404', '00bab40b']]`
  - `FALL_THROUGH` [`00bab408`](#insn-00bab408) → [`00bab40c`](#insn-00bab40c)
- ブロック [`00bab40c`](#insn-00bab40c) 範囲 `[['00bab40c', '00bab41f']]`
  - `FALL_THROUGH` [`00bab41c`](#insn-00bab41c) → [`00bab420`](#insn-00bab420)
- ブロック [`00bab420`](#insn-00bab420) 範囲 `[['00bab420', '00bab423']]`
  - `CONDITIONAL_JUMP` [`00bab420`](#insn-00bab420) → [`00bab24c`](#insn-00bab24c)
  - `FALL_THROUGH` [`00bab420`](#insn-00bab420) → [`00bab424`](#insn-00bab424)
- ブロック [`00bab424`](#insn-00bab424) 範囲 `[['00bab424', '00bab427']]`
  - `UNCONDITIONAL_JUMP` [`00bab424`](#insn-00bab424) → [`00bab254`](#insn-00bab254)
- ブロック [`00bab428`](#insn-00bab428) 範囲 `[['00bab428', '00bab437']]`
  - `UNCONDITIONAL_JUMP` [`00bab434`](#insn-00bab434) → [`00baaf28`](#insn-00baaf28)
- ブロック [`00bab438`](#insn-00bab438) 範囲 `[['00bab438', '00bab43b']]`
- ブロック [`00bab43c`](#insn-00bab43c) 範囲 `[['00bab43c', '00bab43f']]`

## 命令位置別の参照

- [`00baadd0`](#insn-00baadd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadd4`](#insn-00baadd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadd8`](#insn-00baadd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaddc`](#insn-00baaddc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baade0`](#insn-00baade0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baade4`](#insn-00baade4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae00`](#insn-00baae00) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae24`](#insn-00baae24) → [`00baae48`](#insn-00baae48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae34`](#insn-00baae34) → `002af565`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00baae40`](#insn-00baae40) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00baae44`](#insn-00baae44) → [`00baaf18`](#insn-00baaf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae50`](#insn-00baae50) → [`00c5db40`](../00c5d/00c5db40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db40` · 推定シンボル `None` · 推定型 `None`
- [`00baae5c`](#insn-00baae5c) → [`00baaf00`](#insn-00baaf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae64`](#insn-00baae64) → [`00baaf00`](#insn-00baaf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae70`](#insn-00baae70) → [`00baaec4`](#insn-00baaec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae90`](#insn-00baae90) → [`00baaec4`](#insn-00baaec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaeb0`](#insn-00baaeb0) → [`00baaec4`](#insn-00baaec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaec0`](#insn-00baaec0) → [`00bab428`](#insn-00bab428) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaed4`](#insn-00baaed4) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaed8`](#insn-00baaed8) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaedc`](#insn-00baaedc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaee8`](#insn-00baaee8) → [`00baaf9c`](#insn-00baaf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaef4`](#insn-00baaef4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaef8`](#insn-00baaef8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaefc`](#insn-00baaefc) → [`00bab018`](#insn-00bab018) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf04`](#insn-00baaf04) → [`00baaf3c`](#insn-00baaf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf10`](#insn-00baaf10) → [`00c5d6e0`](../00c5d/00c5d6e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d6e0` · 推定シンボル `None` · 推定型 `None`
- [`00baaf14`](#insn-00baaf14) → [`00baaf28`](#insn-00baaf28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf24`](#insn-00baaf24) → [`00c5d7f0`](../00c5d/00c5d7f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d7f0` · 推定シンボル `None` · 推定型 `None`
- [`00baaf34`](#insn-00baaf34) → [`00bab25c`](#insn-00bab25c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf38`](#insn-00baaf38) → [`00bab258`](#insn-00bab258) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf40`](#insn-00baaf40) → `002c1d11`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00baaf4c`](#insn-00baaf4c) → [`00c59150`](../00c59/00c59150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59150` · 推定シンボル `None` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → `002a0ba9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00baaf60`](#insn-00baaf60) → [`00c59150`](../00c59/00c59150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59150` · 推定シンボル `None` · 推定型 `None`
- [`00baaf6c`](#insn-00baaf6c) → [`00c5d810`](../00c5d/00c5d810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d810` · 推定シンボル `None` · 推定型 `None`
- [`00baaf70`](#insn-00baaf70) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf74`](#insn-00baaf74) → [`00baaf80`](#insn-00baaf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf78`](#insn-00baaf78) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf7c`](#insn-00baaf7c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00baaf80`](#insn-00baaf80) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf8c`](#insn-00baaf8c) → [`00bab25c`](#insn-00bab25c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf90`](#insn-00baaf90) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf94`](#insn-00baaf94) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00baaf98`](#insn-00baaf98) → [`00bab25c`](#insn-00bab25c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafa4`](#insn-00baafa4) → [`00bab43c`](#insn-00bab43c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafb0`](#insn-00baafb0) → [`00baafc8`](#insn-00baafc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafbc`](#insn-00baafbc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafc0`](#insn-00baafc0) → [`00bab000`](#insn-00bab000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafc4`](#insn-00baafc4) → [`00bab010`](#insn-00bab010) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafcc`](#insn-00baafcc) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafe0`](#insn-00baafe0) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaff8`](#insn-00baaff8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaffc`](#insn-00baaffc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab00c`](#insn-00bab00c) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00bab01c`](#insn-00bab01c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab024`](#insn-00bab024) → [`00bab178`](#insn-00bab178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab02c`](#insn-00bab02c) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bab040`](#insn-00bab040) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab044`](#insn-00bab044) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab048`](#insn-00bab048) → [`00c59130`](../00c59/00c59130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59130` · 推定シンボル `None` · 推定型 `None`
- [`00bab054`](#insn-00bab054) → `002c4370`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bab05c`](#insn-00bab05c) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab05c`](#insn-00bab05c) → `Stack[-0xf8]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab064`](#insn-00bab064) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab064`](#insn-00bab064) → `Stack[-0xd8]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab074`](#insn-00bab074) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab078`](#insn-00bab078) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab07c`](#insn-00bab07c) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab080`](#insn-00bab080) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab084`](#insn-00bab084) → `Stack[-0x10c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab088`](#insn-00bab088) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab08c`](#insn-00bab08c) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab090`](#insn-00bab090) → [`00c5d740`](../00c5d/00c5d740.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d740` · 推定シンボル `None` · 推定型 `None`
- [`00bab0a0`](#insn-00bab0a0) → [`00bab204`](#insn-00bab204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0a8`](#insn-00bab0a8) → [`00c5d980`](../00c5d/00c5d980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d980` · 推定シンボル `None` · 推定型 `None`
- [`00bab0ac`](#insn-00bab0ac) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0b8`](#insn-00bab0b8) → [`00bab140`](#insn-00bab140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0c4`](#insn-00bab0c4) → [`00bab0d0`](#insn-00bab0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0e0`](#insn-00bab0e0) → [`00bab140`](#insn-00bab140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0f4`](#insn-00bab0f4) → [`00bab10c`](#insn-00bab10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab100`](#insn-00bab100) → [`00c5d240`](../00c5d/00c5d240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d240` · 推定シンボル `None` · 推定型 `None`
- [`00bab124`](#insn-00bab124) → [`00bab140`](#insn-00bab140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab13c`](#insn-00bab13c) → [`00bab12c`](#insn-00bab12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab140`](#insn-00bab140) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab148`](#insn-00bab148) → `00c9c938`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab158`](#insn-00bab158) → `01127298`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZZN11flatbuffers4dataIhNSt6__ndk19allocatorIhEEEEPKT_RKNS1_6vectorIS4_T0_EEE1t` · 推定型 `undefined1`
- [`00bab15c`](#insn-00bab15c) → [`00c5d330`](../00c5d/00c5d330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d330` · 推定シンボル `None` · 推定型 `None`
- [`00bab164`](#insn-00bab164) → [`00c5d090`](../00c5d/00c5d090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d090` · 推定シンボル `None` · 推定型 `None`
- [`00bab168`](#insn-00bab168) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab16c`](#insn-00bab16c) → [`00bab1d0`](#insn-00bab1d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab170`](#insn-00bab170) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab174`](#insn-00bab174) → [`00bab1f0`](#insn-00bab1f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab184`](#insn-00bab184) → [`00bab1a0`](#insn-00bab1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab198`](#insn-00bab198) → [`00c5d750`](../00c5d/00c5d750.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d750` · 推定シンボル `None` · 推定型 `None`
- [`00bab19c`](#insn-00bab19c) → [`00bab1bc`](#insn-00bab1bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1b8`](#insn-00bab1b8) → [`00c5d5d0`](../00c5d/00c5d5d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5d0` · 推定シンボル `None` · 推定型 `None`
- [`00bab1c8`](#insn-00bab1c8) → [`00bab244`](#insn-00bab244) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1cc`](#insn-00bab1cc) → [`00bab28c`](#insn-00bab28c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1d0`](#insn-00bab1d0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1d8`](#insn-00bab1d8) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1dc`](#insn-00bab1dc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1e0`](#insn-00bab1e0) → [`00bab1f0`](#insn-00bab1f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1e4`](#insn-00bab1e4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1e8`](#insn-00bab1e8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bab1ec`](#insn-00bab1ec) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1f0`](#insn-00bab1f0) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1f4`](#insn-00bab1f4) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1fc`](#insn-00bab1fc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab200`](#insn-00bab200) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab204`](#insn-00bab204) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab20c`](#insn-00bab20c) → [`00c5cb60`](../00c5c/00c5cb60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cb60` · 推定シンボル `None` · 推定型 `None`
- [`00bab210`](#insn-00bab210) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab218`](#insn-00bab218) → [`00c5cb70`](../00c5c/00c5cb70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cb70` · 推定シンボル `None` · 推定型 `None`
- [`00bab21c`](#insn-00bab21c) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab220`](#insn-00bab220) → [`00bab22c`](#insn-00bab22c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab224`](#insn-00bab224) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab228`](#insn-00bab228) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bab22c`](#insn-00bab22c) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab230`](#insn-00bab230) → [`00bab23c`](#insn-00bab23c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab234`](#insn-00bab234) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab238`](#insn-00bab238) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bab23c`](#insn-00bab23c) → [`00bab28c`](#insn-00bab28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab244`](#insn-00bab244) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab248`](#insn-00bab248) → [`00bab254`](#insn-00bab254) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab24c`](#insn-00bab24c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab250`](#insn-00bab250) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bab254`](#insn-00bab254) → [`00bab25c`](#insn-00bab25c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab260`](#insn-00bab260) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab268`](#insn-00bab268) → [`00bab438`](#insn-00bab438) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab26c`](#insn-00bab26c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab270`](#insn-00bab270) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab274`](#insn-00bab274) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab278`](#insn-00bab278) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab27c`](#insn-00bab27c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab280`](#insn-00bab280) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab294`](#insn-00bab294) → [`00bab2e0`](#insn-00bab2e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2b8`](#insn-00bab2b8) → [`00bab340`](#insn-00bab340) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2c8`](#insn-00bab2c8) → [`00bab2e0`](#insn-00bab2e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2d8`](#insn-00bab2d8) → [`00bab2b0`](#insn-00bab2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2e0`](#insn-00bab2e0) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2e4`](#insn-00bab2e4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2f0`](#insn-00bab2f0) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2f4`](#insn-00bab2f4) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2f8`](#insn-00bab2f8) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2fc`](#insn-00bab2fc) → [`00bab314`](#insn-00bab314) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab300`](#insn-00bab300) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab304`](#insn-00bab304) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab308`](#insn-00bab308) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab30c`](#insn-00bab30c) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab310`](#insn-00bab310) → [`00bab3e0`](#insn-00bab3e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab314`](#insn-00bab314) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab31c`](#insn-00bab31c) → [`00bab43c`](#insn-00bab43c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab320`](#insn-00bab320) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab328`](#insn-00bab328) → [`00bab3ac`](#insn-00bab3ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab334`](#insn-00bab334) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab338`](#insn-00bab338) → [`00bab3cc`](#insn-00bab3cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab33c`](#insn-00bab33c) → [`00bab3dc`](#insn-00bab3dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab344`](#insn-00bab344) → `002c0c02`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bab350`](#insn-00bab350) → [`00c59150`](../00c59/00c59150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59150` · 推定シンボル `None` · 推定型 `None`
- [`00bab358`](#insn-00bab358) → `002a0ba9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bab364`](#insn-00bab364) → [`00c59150`](../00c59/00c59150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59150` · 推定シンボル `None` · 推定型 `None`
- [`00bab370`](#insn-00bab370) → [`00c5d810`](../00c5d/00c5d810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d810` · 推定シンボル `None` · 推定型 `None`
- [`00bab374`](#insn-00bab374) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab378`](#insn-00bab378) → [`00bab384`](#insn-00bab384) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab37c`](#insn-00bab37c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab380`](#insn-00bab380) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bab384`](#insn-00bab384) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab390`](#insn-00bab390) → [`00bab39c`](#insn-00bab39c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab394`](#insn-00bab394) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab398`](#insn-00bab398) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bab3a0`](#insn-00bab3a0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3a4`](#insn-00bab3a4) → [`00bab24c`](#insn-00bab24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3a8`](#insn-00bab3a8) → [`00bab254`](#insn-00bab254) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3b8`](#insn-00bab3b8) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bab3c4`](#insn-00bab3c4) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3c8`](#insn-00bab3c8) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3d8`](#insn-00bab3d8) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00bab3e0`](#insn-00bab3e0) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3f0`](#insn-00bab3f0) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3f4`](#insn-00bab3f4) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3f8`](#insn-00bab3f8) → [`00c5e0f0`](../00c5e/00c5e0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bab3fc`](#insn-00bab3fc) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab400`](#insn-00bab400) → [`00bab40c`](#insn-00bab40c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab404`](#insn-00bab404) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab408`](#insn-00bab408) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bab41c`](#insn-00bab41c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab420`](#insn-00bab420) → [`00bab24c`](#insn-00bab24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab424`](#insn-00bab424) → [`00bab254`](#insn-00bab254) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab430`](#insn-00bab430) → [`00c5d790`](../00c5d/00c5d790.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d790` · 推定シンボル `None` · 推定型 `None`
- [`00bab434`](#insn-00bab434) → [`00baaf28`](#insn-00baaf28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab438`](#insn-00bab438) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`
- [`00bab43c`](#insn-00bab43c) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baadd0`](#insn-00baadd0)

~~~json
{
  "source": "00baadd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadd4`](#insn-00baadd4)

~~~json
{
  "source": "00baadd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadd8`](#insn-00baadd8)

~~~json
{
  "source": "00baadd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaddc`](#insn-00baaddc)

~~~json
{
  "source": "00baaddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baade0`](#insn-00baade0)

~~~json
{
  "source": "00baade0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baade4`](#insn-00baade4)

~~~json
{
  "source": "00baade4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae00`](#insn-00baae00)

~~~json
{
  "source": "00baae00",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae24`](#insn-00baae24)

~~~json
{
  "source": "00baae24",
  "target": "00baae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae34`](#insn-00baae34)

~~~json
{
  "source": "00baae34",
  "target": "002af565",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af565",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "24736368656d6100",
  "capture_start": "002af565",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00baae40`](#insn-00baae40)

~~~json
{
  "source": "00baae40",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae44`](#insn-00baae44)

~~~json
{
  "source": "00baae44",
  "target": "00baaf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae50`](#insn-00baae50)

~~~json
{
  "source": "00baae50",
  "target": "00c5db40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae5c`](#insn-00baae5c)

~~~json
{
  "source": "00baae5c",
  "target": "00baaf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae64`](#insn-00baae64)

~~~json
{
  "source": "00baae64",
  "target": "00baaf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae70`](#insn-00baae70)

~~~json
{
  "source": "00baae70",
  "target": "00baaec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae90`](#insn-00baae90)

~~~json
{
  "source": "00baae90",
  "target": "00baaec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaeb0`](#insn-00baaeb0)

~~~json
{
  "source": "00baaeb0",
  "target": "00baaec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaec0`](#insn-00baaec0)

~~~json
{
  "source": "00baaec0",
  "target": "00bab428",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaed4`](#insn-00baaed4)

~~~json
{
  "source": "00baaed4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaed8`](#insn-00baaed8)

~~~json
{
  "source": "00baaed8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaedc`](#insn-00baaedc)

~~~json
{
  "source": "00baaedc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaee8`](#insn-00baaee8)

~~~json
{
  "source": "00baaee8",
  "target": "00baaf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaef4`](#insn-00baaef4)

~~~json
{
  "source": "00baaef4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaef8`](#insn-00baaef8)

~~~json
{
  "source": "00baaef8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaefc`](#insn-00baaefc)

~~~json
{
  "source": "00baaefc",
  "target": "00bab018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf04`](#insn-00baaf04)

~~~json
{
  "source": "00baaf04",
  "target": "00baaf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf10`](#insn-00baaf10)

~~~json
{
  "source": "00baaf10",
  "target": "00c5d6e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaf14`](#insn-00baaf14)

~~~json
{
  "source": "00baaf14",
  "target": "00baaf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf24`](#insn-00baaf24)

~~~json
{
  "source": "00baaf24",
  "target": "00c5d7f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaf34`](#insn-00baaf34)

~~~json
{
  "source": "00baaf34",
  "target": "00bab25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf38`](#insn-00baaf38)

~~~json
{
  "source": "00baaf38",
  "target": "00bab258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf40`](#insn-00baaf40)

~~~json
{
  "source": "00baaf40",
  "target": "002c1d11",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c1d11",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "756e6b6e6f776e206669656c643a2000",
  "capture_start": "002c1d11",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00baaf4c`](#insn-00baaf4c)

~~~json
{
  "source": "00baaf4c",
  "target": "00c59150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "002a0ba9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0ba9",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "6572726f723a2000",
  "capture_start": "002a0ba9",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00baaf60`](#insn-00baaf60)

~~~json
{
  "source": "00baaf60",
  "target": "00c59150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaf6c`](#insn-00baaf6c)

~~~json
{
  "source": "00baaf6c",
  "target": "00c5d810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaf70`](#insn-00baaf70)

~~~json
{
  "source": "00baaf70",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf74`](#insn-00baaf74)

~~~json
{
  "source": "00baaf74",
  "target": "00baaf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf78`](#insn-00baaf78)

~~~json
{
  "source": "00baaf78",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf7c`](#insn-00baaf7c)

~~~json
{
  "source": "00baaf7c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaf80`](#insn-00baaf80)

~~~json
{
  "source": "00baaf80",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf8c`](#insn-00baaf8c)

~~~json
{
  "source": "00baaf8c",
  "target": "00bab25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf90`](#insn-00baaf90)

~~~json
{
  "source": "00baaf90",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf94`](#insn-00baaf94)

~~~json
{
  "source": "00baaf94",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaf98`](#insn-00baaf98)

~~~json
{
  "source": "00baaf98",
  "target": "00bab25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafa4`](#insn-00baafa4)

~~~json
{
  "source": "00baafa4",
  "target": "00bab43c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafb0`](#insn-00baafb0)

~~~json
{
  "source": "00baafb0",
  "target": "00baafc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafbc`](#insn-00baafbc)

~~~json
{
  "source": "00baafbc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafc0`](#insn-00baafc0)

~~~json
{
  "source": "00baafc0",
  "target": "00bab000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafc4`](#insn-00baafc4)

~~~json
{
  "source": "00baafc4",
  "target": "00bab010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafcc`](#insn-00baafcc)

~~~json
{
  "source": "00baafcc",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafe0`](#insn-00baafe0)

~~~json
{
  "source": "00baafe0",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff8`](#insn-00baaff8)

~~~json
{
  "source": "00baaff8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaffc`](#insn-00baaffc)

~~~json
{
  "source": "00baaffc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab00c`](#insn-00bab00c)

~~~json
{
  "source": "00bab00c",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab01c`](#insn-00bab01c)

~~~json
{
  "source": "00bab01c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab024`](#insn-00bab024)

~~~json
{
  "source": "00bab024",
  "target": "00bab178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab02c`](#insn-00bab02c)

~~~json
{
  "source": "00bab02c",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab040`](#insn-00bab040)

~~~json
{
  "source": "00bab040",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab044`](#insn-00bab044)

~~~json
{
  "source": "00bab044",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab048`](#insn-00bab048)

~~~json
{
  "source": "00bab048",
  "target": "00c59130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab054`](#insn-00bab054)

~~~json
{
  "source": "00bab054",
  "target": "002c4370",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4370",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0700000000000000",
  "capture_start": "002c4370",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bab05c`](#insn-00bab05c)

~~~json
{
  "source": "00bab05c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab05c`](#insn-00bab05c)

~~~json
{
  "source": "00bab05c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab064`](#insn-00bab064)

~~~json
{
  "source": "00bab064",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab064`](#insn-00bab064)

~~~json
{
  "source": "00bab064",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab074`](#insn-00bab074)

~~~json
{
  "source": "00bab074",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab078`](#insn-00bab078)

~~~json
{
  "source": "00bab078",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab07c`](#insn-00bab07c)

~~~json
{
  "source": "00bab07c",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab080`](#insn-00bab080)

~~~json
{
  "source": "00bab080",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab084`](#insn-00bab084)

~~~json
{
  "source": "00bab084",
  "target": "Stack[-0x10c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab088`](#insn-00bab088)

~~~json
{
  "source": "00bab088",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab08c`](#insn-00bab08c)

~~~json
{
  "source": "00bab08c",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab090`](#insn-00bab090)

~~~json
{
  "source": "00bab090",
  "target": "00c5d740",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab0a0`](#insn-00bab0a0)

~~~json
{
  "source": "00bab0a0",
  "target": "00bab204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0a8`](#insn-00bab0a8)

~~~json
{
  "source": "00bab0a8",
  "target": "00c5d980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab0ac`](#insn-00bab0ac)

~~~json
{
  "source": "00bab0ac",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0b8`](#insn-00bab0b8)

~~~json
{
  "source": "00bab0b8",
  "target": "00bab140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0c4`](#insn-00bab0c4)

~~~json
{
  "source": "00bab0c4",
  "target": "00bab0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0e0`](#insn-00bab0e0)

~~~json
{
  "source": "00bab0e0",
  "target": "00bab140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0f4`](#insn-00bab0f4)

~~~json
{
  "source": "00bab0f4",
  "target": "00bab10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab100`](#insn-00bab100)

~~~json
{
  "source": "00bab100",
  "target": "00c5d240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab124`](#insn-00bab124)

~~~json
{
  "source": "00bab124",
  "target": "00bab140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab13c`](#insn-00bab13c)

~~~json
{
  "source": "00bab13c",
  "target": "00bab12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab140`](#insn-00bab140)

~~~json
{
  "source": "00bab140",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab148`](#insn-00bab148)

~~~json
{
  "source": "00bab148",
  "target": "00c9c938",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c938",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab158`](#insn-00bab158)

~~~json
{
  "source": "00bab158",
  "target": "01127298",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127298",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab15c`](#insn-00bab15c)

~~~json
{
  "source": "00bab15c",
  "target": "00c5d330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab164`](#insn-00bab164)

~~~json
{
  "source": "00bab164",
  "target": "00c5d090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab168`](#insn-00bab168)

~~~json
{
  "source": "00bab168",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab16c`](#insn-00bab16c)

~~~json
{
  "source": "00bab16c",
  "target": "00bab1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab170`](#insn-00bab170)

~~~json
{
  "source": "00bab170",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab174`](#insn-00bab174)

~~~json
{
  "source": "00bab174",
  "target": "00bab1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab184`](#insn-00bab184)

~~~json
{
  "source": "00bab184",
  "target": "00bab1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab198`](#insn-00bab198)

~~~json
{
  "source": "00bab198",
  "target": "00c5d750",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab19c`](#insn-00bab19c)

~~~json
{
  "source": "00bab19c",
  "target": "00bab1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1b8`](#insn-00bab1b8)

~~~json
{
  "source": "00bab1b8",
  "target": "00c5d5d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab1c8`](#insn-00bab1c8)

~~~json
{
  "source": "00bab1c8",
  "target": "00bab244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1cc`](#insn-00bab1cc)

~~~json
{
  "source": "00bab1cc",
  "target": "00bab28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1d0`](#insn-00bab1d0)

~~~json
{
  "source": "00bab1d0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1d8`](#insn-00bab1d8)

~~~json
{
  "source": "00bab1d8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1dc`](#insn-00bab1dc)

~~~json
{
  "source": "00bab1dc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1e0`](#insn-00bab1e0)

~~~json
{
  "source": "00bab1e0",
  "target": "00bab1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1e4`](#insn-00bab1e4)

~~~json
{
  "source": "00bab1e4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1e8`](#insn-00bab1e8)

~~~json
{
  "source": "00bab1e8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab1ec`](#insn-00bab1ec)

~~~json
{
  "source": "00bab1ec",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1f0`](#insn-00bab1f0)

~~~json
{
  "source": "00bab1f0",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1f4`](#insn-00bab1f4)

~~~json
{
  "source": "00bab1f4",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1fc`](#insn-00bab1fc)

~~~json
{
  "source": "00bab1fc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab200`](#insn-00bab200)

~~~json
{
  "source": "00bab200",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab204`](#insn-00bab204)

~~~json
{
  "source": "00bab204",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab20c`](#insn-00bab20c)

~~~json
{
  "source": "00bab20c",
  "target": "00c5cb60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab210`](#insn-00bab210)

~~~json
{
  "source": "00bab210",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab218`](#insn-00bab218)

~~~json
{
  "source": "00bab218",
  "target": "00c5cb70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab21c`](#insn-00bab21c)

~~~json
{
  "source": "00bab21c",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab220`](#insn-00bab220)

~~~json
{
  "source": "00bab220",
  "target": "00bab22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab224`](#insn-00bab224)

~~~json
{
  "source": "00bab224",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab228`](#insn-00bab228)

~~~json
{
  "source": "00bab228",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab22c`](#insn-00bab22c)

~~~json
{
  "source": "00bab22c",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab230`](#insn-00bab230)

~~~json
{
  "source": "00bab230",
  "target": "00bab23c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab234`](#insn-00bab234)

~~~json
{
  "source": "00bab234",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab238`](#insn-00bab238)

~~~json
{
  "source": "00bab238",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab23c`](#insn-00bab23c)

~~~json
{
  "source": "00bab23c",
  "target": "00bab28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab244`](#insn-00bab244)

~~~json
{
  "source": "00bab244",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab248`](#insn-00bab248)

~~~json
{
  "source": "00bab248",
  "target": "00bab254",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab24c`](#insn-00bab24c)

~~~json
{
  "source": "00bab24c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab250`](#insn-00bab250)

~~~json
{
  "source": "00bab250",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab254`](#insn-00bab254)

~~~json
{
  "source": "00bab254",
  "target": "00bab25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab260`](#insn-00bab260)

~~~json
{
  "source": "00bab260",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab268`](#insn-00bab268)

~~~json
{
  "source": "00bab268",
  "target": "00bab438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab26c`](#insn-00bab26c)

~~~json
{
  "source": "00bab26c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab270`](#insn-00bab270)

~~~json
{
  "source": "00bab270",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab274`](#insn-00bab274)

~~~json
{
  "source": "00bab274",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab278`](#insn-00bab278)

~~~json
{
  "source": "00bab278",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab27c`](#insn-00bab27c)

~~~json
{
  "source": "00bab27c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab280`](#insn-00bab280)

~~~json
{
  "source": "00bab280",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab294`](#insn-00bab294)

~~~json
{
  "source": "00bab294",
  "target": "00bab2e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2b8`](#insn-00bab2b8)

~~~json
{
  "source": "00bab2b8",
  "target": "00bab340",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2c8`](#insn-00bab2c8)

~~~json
{
  "source": "00bab2c8",
  "target": "00bab2e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2d8`](#insn-00bab2d8)

~~~json
{
  "source": "00bab2d8",
  "target": "00bab2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2e0`](#insn-00bab2e0)

~~~json
{
  "source": "00bab2e0",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2e4`](#insn-00bab2e4)

~~~json
{
  "source": "00bab2e4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2f0`](#insn-00bab2f0)

~~~json
{
  "source": "00bab2f0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2f4`](#insn-00bab2f4)

~~~json
{
  "source": "00bab2f4",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2f8`](#insn-00bab2f8)

~~~json
{
  "source": "00bab2f8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2fc`](#insn-00bab2fc)

~~~json
{
  "source": "00bab2fc",
  "target": "00bab314",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab300`](#insn-00bab300)

~~~json
{
  "source": "00bab300",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab304`](#insn-00bab304)

~~~json
{
  "source": "00bab304",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab308`](#insn-00bab308)

~~~json
{
  "source": "00bab308",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab30c`](#insn-00bab30c)

~~~json
{
  "source": "00bab30c",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab310`](#insn-00bab310)

~~~json
{
  "source": "00bab310",
  "target": "00bab3e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab314`](#insn-00bab314)

~~~json
{
  "source": "00bab314",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab31c`](#insn-00bab31c)

~~~json
{
  "source": "00bab31c",
  "target": "00bab43c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab320`](#insn-00bab320)

~~~json
{
  "source": "00bab320",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab328`](#insn-00bab328)

~~~json
{
  "source": "00bab328",
  "target": "00bab3ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab334`](#insn-00bab334)

~~~json
{
  "source": "00bab334",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab338`](#insn-00bab338)

~~~json
{
  "source": "00bab338",
  "target": "00bab3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab33c`](#insn-00bab33c)

~~~json
{
  "source": "00bab33c",
  "target": "00bab3dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab344`](#insn-00bab344)

~~~json
{
  "source": "00bab344",
  "target": "002c0c02",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c0c02",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "6669656c6420736574206d6f7265207468616e206f6e63653a2000",
  "capture_start": "002c0c02",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bab350`](#insn-00bab350)

~~~json
{
  "source": "00bab350",
  "target": "00c59150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab358`](#insn-00bab358)

~~~json
{
  "source": "00bab358",
  "target": "002a0ba9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0ba9",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "6572726f723a2000",
  "capture_start": "002a0ba9",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bab364`](#insn-00bab364)

~~~json
{
  "source": "00bab364",
  "target": "00c59150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab370`](#insn-00bab370)

~~~json
{
  "source": "00bab370",
  "target": "00c5d810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab374`](#insn-00bab374)

~~~json
{
  "source": "00bab374",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab378`](#insn-00bab378)

~~~json
{
  "source": "00bab378",
  "target": "00bab384",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab37c`](#insn-00bab37c)

~~~json
{
  "source": "00bab37c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab380`](#insn-00bab380)

~~~json
{
  "source": "00bab380",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab384`](#insn-00bab384)

~~~json
{
  "source": "00bab384",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab390`](#insn-00bab390)

~~~json
{
  "source": "00bab390",
  "target": "00bab39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab394`](#insn-00bab394)

~~~json
{
  "source": "00bab394",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab398`](#insn-00bab398)

~~~json
{
  "source": "00bab398",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab3a0`](#insn-00bab3a0)

~~~json
{
  "source": "00bab3a0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3a4`](#insn-00bab3a4)

~~~json
{
  "source": "00bab3a4",
  "target": "00bab24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3a8`](#insn-00bab3a8)

~~~json
{
  "source": "00bab3a8",
  "target": "00bab254",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3b8`](#insn-00bab3b8)

~~~json
{
  "source": "00bab3b8",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab3c4`](#insn-00bab3c4)

~~~json
{
  "source": "00bab3c4",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3c8`](#insn-00bab3c8)

~~~json
{
  "source": "00bab3c8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3d8`](#insn-00bab3d8)

~~~json
{
  "source": "00bab3d8",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab3e0`](#insn-00bab3e0)

~~~json
{
  "source": "00bab3e0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3f0`](#insn-00bab3f0)

~~~json
{
  "source": "00bab3f0",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3f4`](#insn-00bab3f4)

~~~json
{
  "source": "00bab3f4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3f8`](#insn-00bab3f8)

~~~json
{
  "source": "00bab3f8",
  "target": "00c5e0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab3fc`](#insn-00bab3fc)

~~~json
{
  "source": "00bab3fc",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab400`](#insn-00bab400)

~~~json
{
  "source": "00bab400",
  "target": "00bab40c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab404`](#insn-00bab404)

~~~json
{
  "source": "00bab404",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab408`](#insn-00bab408)

~~~json
{
  "source": "00bab408",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab41c`](#insn-00bab41c)

~~~json
{
  "source": "00bab41c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab420`](#insn-00bab420)

~~~json
{
  "source": "00bab420",
  "target": "00bab24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab424`](#insn-00bab424)

~~~json
{
  "source": "00bab424",
  "target": "00bab254",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab430`](#insn-00bab430)

~~~json
{
  "source": "00bab430",
  "target": "00c5d790",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab434`](#insn-00bab434)

~~~json
{
  "source": "00bab434",
  "target": "00baaf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab438`](#insn-00bab438)

~~~json
{
  "source": "00bab438",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab43c`](#insn-00bab43c)

~~~json
{
  "source": "00bab43c",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
