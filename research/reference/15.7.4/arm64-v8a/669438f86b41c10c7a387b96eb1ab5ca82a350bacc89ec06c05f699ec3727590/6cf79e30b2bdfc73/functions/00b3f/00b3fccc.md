# 00b3fccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00b3fccc.md)

## 関数情報

~~~json
{
  "address": "00b3fccc",
  "name": "FUN_00b3fccc",
  "size": 1696,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a50abb4dbabceb1853da8a7072900246e524e92d214af3510e2335e2b4bcc909",
  "source_text_sha256": "a50abb4dbabceb1853da8a7072900246e524e92d214af3510e2335e2b4bcc909"
}
~~~
## 呼び出し元

- [00b17160](../00b17/00b17160.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bdb200](../00bdb/00bdb200.md)
- [00bdb240](../00bdb/00bdb240.md)
- [00bdb260](../00bdb/00bdb260.md)
- [00bde2c0](../00bde/00bde2c0.md)
- [00bdec00](../00bde/00bdec00.md)
- [00bdec10](../00bde/00bdec10.md)
- [00bdf1b0](../00bdf/00bdf1b0.md)
- [00bdf390](../00bdf/00bdf390.md)
- [00bdf4e0](../00bdf/00bdf4e0.md)
- [00bdf7f0](../00bdf/00bdf7f0.md)
- [00bdf800](../00bdf/00bdf800.md)
- [00bdf900](../00bdf/00bdf900.md)
- [00bdf940](../00bdf/00bdf940.md)
- [00bdf950](../00bdf/00bdf950.md)
- [00bdf970](../00bdf/00bdf970.md)
- [00bdf9b0](../00bdf/00bdf9b0.md)
- [00bdf9d0](../00bdf/00bdf9d0.md)
- [00bdfb30](../00bdf/00bdfb30.md)
- [00bdfcc0](../00bdf/00bdfcc0.md)
- [00be00b0](../00be0/00be00b0.md)

## 関連文字列（未確認候補）

~~~text
"$schema"
"error: "
"field set more than once: "
"unknown field: "
~~~
## 疑似コード 1/1 / UTF-8 12640 bytes

~~~c

void FUN_00b3fccc(char *param_1,long *param_2,byte *param_3,long *param_4,long param_5)

{
  byte bVar1;
  uint uVar2;
  long lVar3;
  bool bVar4;
  int iVar5;
  long lVar6;
  void *pvVar7;
  char cVar8;
  byte *__s1;
  undefined1 *puVar9;
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
  void *local_140;
  void *pvStack_138;
  void *local_130;
  void *local_128;
  undefined8 local_120;
  ulong uStack_118;
  uint local_110;
  undefined4 uStack_10c;
  undefined2 uStack_108;
  undefined2 uStack_106;
  undefined8 *local_100;
  undefined8 local_f8;
  undefined8 local_f0;
  void **ppvStack_e8;
  undefined8 *local_e0;
  undefined8 local_d8;
  undefined8 local_d0;
  void **ppvStack_c8;
  void *local_c0;
  void *pvStack_b8;
  void *local_b0;
  void *pvStack_a8;
  undefined8 local_a0;
  ulong uStack_98;
  undefined1 *local_90;
  undefined2 local_88;
  long local_78;
  
  lVar3 = tpidr_el0;
  local_78 = *(long *)(lVar3 + 0x28);
  bVar1 = *param_3;
  lVar14 = *param_2;
  uVar18 = (ulong)(bVar1 >> 1);
  if ((bVar1 & 1) != 0) {
    uVar18 = *(ulong *)(param_3 + 8);
  }
  if (uVar18 == 7) {
    __s1 = *(byte **)(param_3 + 0x10);
    if ((bVar1 & 1) == 0) {
      __s1 = param_3 + 1;
    }
    iVar5 = memcmp(__s1,"$schema",7);
    if (iVar5 != 0) goto LAB_00b3fd48;
    _ZN11flatbuffers6Parser6ExpectEi(param_1,lVar14,0x101);
LAB_00b3fe2c:
    param_1[1] = '\x01';
    if (*param_1 != '\0') goto LAB_00b40324;
  }
  else {
LAB_00b3fd48:
    lVar6 = _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
                      (param_5 + 0x98,param_3);
    if ((param_5 + 0xa0 == lVar6) ||
       (puVar15 = *(undefined8 **)(lVar6 + 0x38), puVar15 == (undefined8 *)0x0)) {
      if (*(char *)(lVar14 + 0x2ed) == '\0') {
        _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
                  (&local_c0,"unknown field: ",param_3);
        _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
                  (&local_140,"error: ",&local_c0);
        _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
                  (lVar14,&local_140);
        if (((ulong)local_140 & 1) != 0) {
          _ZdlPv(local_130);
        }
        param_1[0] = '\x01';
        param_1[1] = '\0';
        if (((ulong)local_c0 & 1) != 0) {
          _ZdlPv(local_b0);
        }
        goto LAB_00b40324;
      }
      _ZN11flatbuffers6Parser16SkipAnyJsonValueEv(param_1,lVar14);
      goto LAB_00b3fe2c;
    }
    if (*(int *)(lVar14 + 0x14) == 0x104) {
      bVar1 = *(byte *)(lVar14 + 0x20);
      uVar18 = (ulong)(bVar1 >> 1);
      if ((bVar1 & 1) != 0) {
        uVar18 = *(ulong *)(lVar14 + 0x28);
      }
      if (uVar18 == 4) {
        piVar13 = *(int **)(lVar14 + 0x30);
        if ((bVar1 & 1) == 0) {
          piVar13 = (int *)(lVar14 + 0x21);
        }
        if ((*piVar13 == 0x6c6c756e) && (0xb < *(int *)(puVar15 + 0x13) - 1U)) {
          _ZN11flatbuffers6Parser4NextEv(param_1,lVar14);
          goto LAB_00b3fe2c;
        }
      }
    }
    pvStack_b8 = (void *)puVar15[0x14];
    local_c0 = (void *)puVar15[0x13];
    pvStack_a8 = (void *)puVar15[0x16];
    local_b0 = (void *)puVar15[0x15];
    uStack_98 = 0;
    local_90 = (undefined1 *)0x0;
    local_a0 = (void *)0x0;
    if ((puVar15[0x17] & 1) == 0) {
      local_90 = (undefined1 *)puVar15[0x19];
      uStack_98 = puVar15[0x18];
      local_a0 = (void *)puVar15[0x17];
    }
    else {
      uVar18 = puVar15[0x18];
      if (0xffffffffffffffef < uVar18) goto LAB_00b40368;
      pvVar7 = (void *)puVar15[0x19];
      if (uVar18 < 0x17) {
        puVar9 = (undefined1 *)((long)&local_a0 + 1);
        local_a0 = (void *)(ulong)(byte)((int)uVar18 << 1);
        if (uVar18 != 0) goto LAB_00b3ff04;
      }
      else {
        uVar10 = uVar18 + 0x10 & 0xfffffffffffffff0;
        puVar9 = (undefined1 *)_Znwm(uVar10);
        local_a0 = (void *)(uVar10 | 1);
        uStack_98 = uVar18;
        local_90 = puVar9;
LAB_00b3ff04:
        memcpy(puVar9,pvVar7,uVar18);
      }
      puVar9[uVar18] = 0;
    }
    local_88 = *(undefined2 *)(puVar15 + 0x1a);
    if (*(char *)((long)puVar15 + 0xdd) == '\0') {
      if (puVar15[0x1c] == 0) {
        if (*(int *)(lVar14 + 0x4b4) < 0x40) {
          *(int *)(lVar14 + 0x4b4) = *(int *)(lVar14 + 0x4b4) + 1;
          _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEjb
                    (&local_140,lVar14,&local_c0,puVar15,*param_4,param_5,0,0);
          *(int *)(lVar14 + 0x4b4) = *(int *)(lVar14 + 0x4b4) + -1;
          param_1[1] = '\0';
          *param_1 = (char)local_140;
          cVar8 = (char)local_140;
        }
        else {
          _ZN11flatbuffers6Parser12RecurseErrorEv(param_1,lVar14);
          cVar8 = *param_1;
        }
      }
      else {
        _ZN11flatbuffers6Parser21ParseNestedFlatbufferERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefE
                  (param_1,lVar14,&local_c0,puVar15,*param_4,param_5);
        cVar8 = *param_1;
      }
      bVar4 = true;
      param_1[1] = '\x01';
      if (cVar8 == '\0') goto LAB_00b40188;
    }
    else {
      pvVar7 = (void *)_Znwm(0x400);
      local_130 = (void *)((long)pvVar7 + 0x400);
      local_140 = pvVar7;
      memset(pvVar7,0,0x400);
      ppvStack_e8 = &local_140;
      local_100 = &local_f8;
      local_f8 = 0;
      local_e0 = &local_d8;
      local_d8 = 0;
      local_120 = (void *)0x0;
      uStack_118 = 0;
      local_110 = local_110 & 0xffffff00;
      local_f0 = 0;
      local_d0 = 0;
      uStack_10c = (undefined4)DAT_002b2b90;
      uStack_108 = (undefined2)((ulong)DAT_002b2b90 >> 0x20);
      uStack_106 = (undefined2)((ulong)DAT_002b2b90 >> 0x30);
      local_128 = (void *)0x0;
      pvStack_138 = pvVar7;
      ppvStack_c8 = ppvStack_e8;
      _ZN11flatbuffers6Parser20ParseFlexBufferValueEPN11flexbuffers7BuilderE
                (param_1,lVar14,&local_140);
      bVar4 = true;
      param_1[1] = '\x01';
      if (*param_1 == '\0') {
        _ZN11flexbuffers7Builder6FinishEv(&local_140);
        if (*(ulong *)(lVar14 + 0x198) < 8) {
          *(undefined8 *)(lVar14 + 0x198) = 8;
        }
        lVar6 = *(long *)(lVar14 + 0x180);
        uVar2 = -(((int)pvStack_138 - (int)local_140) +
                 (*(int *)(lVar14 + 0x170) - (int)lVar6) + *(int *)(lVar14 + 0x178));
        uVar18 = (ulong)uVar2 & 7;
        if ((ulong)(lVar6 - *(long *)(lVar14 + 0x188)) < uVar18) {
          _ZN11flatbuffers15vector_downward10reallocateEm(lVar14 + 0x150,uVar18);
          puVar9 = (undefined1 *)(*(long *)(lVar14 + 0x180) - uVar18);
          *(undefined1 **)(lVar14 + 0x180) = puVar9;
LAB_00b40070:
          *puVar9 = 0;
          if (uVar18 != 1) {
            uVar10 = 1;
            do {
              *(undefined1 *)(*(long *)(lVar14 + 0x180) + uVar10) = 0;
              uVar10 = uVar10 + 1;
            } while (uVar18 != uVar10);
          }
        }
        else {
          puVar9 = (undefined1 *)(lVar6 - uVar18);
          *(undefined1 **)(lVar14 + 0x180) = puVar9;
          if ((uVar2 & 7) != 0) goto LAB_00b40070;
        }
        _ZN11flatbuffers17FlatBufferBuilder12CreateVectorIhEENS_6OffsetINS_6VectorIT_EEEERKNSt6__ndk16vectorIS4_NS7_9allocatorIS4_EEEE
                  (lVar14 + 0x150,&local_140);
        _ZN11flatbuffers11NumToStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_
                  (&local_158);
        if (((ulong)local_a0 & 1) != 0) {
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
      if (local_140 != (void *)0x0) {
        pvStack_138 = local_140;
        _ZdlPv(local_140);
      }
      if (bVar4) {
LAB_00b40128:
        bVar4 = true;
      }
      else {
LAB_00b40188:
        puVar9 = local_90;
        uVar18 = uStack_98;
        lVar11 = *param_4;
        lVar16 = *(long *)(lVar14 + 0x4a0);
        lVar6 = lVar16;
        if (lVar11 != 0) {
          lVar12 = lVar11 * -0x48;
          lVar17 = lVar16;
          do {
            if (*(undefined8 **)(lVar17 + -8) == puVar15) {
                    /* try { // try from 00b4024c to 00c402f7 has its CatchHandler @ 00b40c78 */
              _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
                        (&local_158,"field set more than once: ",puVar15);
              _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
                        (&local_140,"error: ",&local_158);
              _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
                        (lVar14,&local_140);
              if (((ulong)local_140 & 1) != 0) {
                _ZdlPv(local_130);
              }
              param_1[0] = '\x01';
              param_1[1] = '\0';
              if ((local_158 & 1) != 0) {
                _ZdlPv(local_148);
              }
              goto LAB_00b40128;
            }
            lVar6 = lVar17;
          } while ((*(ushort *)(puVar15 + 0x1a) <= *(ushort *)(*(undefined8 **)(lVar17 + -8) + 0x1a)
                   ) && (lVar12 = lVar12 + 0x48, lVar6 = lVar16 + lVar11 * -0x48,
                        lVar17 = lVar17 + -0x48, lVar12 != 0));
        }
        local_120 = (void *)0x0;
        uStack_118 = 0;
        pvStack_138 = pvStack_b8;
        local_140 = local_c0;
        local_128 = pvStack_a8;
        local_130 = local_b0;
        local_110 = 0;
        uStack_10c = 0;
        if (((ulong)local_a0 & 1) == 0) {
          local_110 = (uint)local_90;
          uStack_10c = (undefined4)((ulong)local_90 >> 0x20);
          uStack_118 = uStack_98;
          local_120 = local_a0;
        }
        else {
          if (0xffffffffffffffef < uStack_98) {
LAB_00b40368:
                    /* WARNING: Subroutine does not return */
            abort();
          }
          if (uStack_98 < 0x17) {
            pvVar7 = (void *)((long)&local_120 + 1);
            local_120 = (void *)(ulong)(byte)((int)uStack_98 << 1);
            if (uStack_98 != 0) goto LAB_00b402bc;
          }
          else {
            uVar10 = uStack_98 + 0x10 & 0xfffffffffffffff0;
            pvVar7 = (void *)_Znwm(uVar10);
            local_120 = (void *)(uVar10 | 1);
            uStack_118 = uVar18;
            local_110 = (uint)pvVar7;
            uStack_10c = (undefined4)((ulong)pvVar7 >> 0x20);
LAB_00b402bc:
            memcpy(pvVar7,puVar9,uVar18);
          }
          *(undefined1 *)((long)pvVar7 + uVar18) = 0;
        }
        uStack_108 = local_88;
        local_100 = puVar15;
        _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE6insertENS_11__wrap_iterIPKS6_EEOS6_
                  (lVar14 + 0x498,lVar6,&local_140);
        if (((ulong)local_120 & 1) != 0) {
          _ZdlPv((void *)CONCAT44(uStack_10c,local_110));
        }
        bVar4 = false;
        *param_4 = *param_4 + 1;
      }
    }
                    /* try { // try from 00b40310 to 00c40317 has its CatchHandler @ 00b40c64 */
    if (((ulong)local_a0 & 1) != 0) {
                    /* try { // try from 00b40318 to 00c40343 has its CatchHandler @ 00b3e5f8 */
      _ZdlPv(local_90);
    }
    if (bVar4) goto LAB_00b40324;
  }
  param_1[0] = '\0';
  param_1[1] = '\0';
LAB_00b40324:
  if (*(long *)(lVar3 + 0x28) != local_78) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 00b40344 to 00c4035f has its CatchHandler @ 00b40c6c */
  return;
}

~~~
