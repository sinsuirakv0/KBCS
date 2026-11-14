# 00baadcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

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
  "source_text_sha256": "5fbd3a2ed4ca07078cddca3991cd2bc47676725db72a47742fbb6cdffb2df5a1"
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
