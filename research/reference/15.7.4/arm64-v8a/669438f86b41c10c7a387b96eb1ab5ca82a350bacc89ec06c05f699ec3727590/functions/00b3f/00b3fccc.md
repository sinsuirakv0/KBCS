# 00b3fccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b3fc88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3fc88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0009.md#compare-0962ad251cac350dcf2ef9b54a5ba589)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0091.md#review-3ac7e47cd8135bc8bff2402989f869a3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "a50abb4dbabceb1853da8a7072900246e524e92d214af3510e2335e2b4bcc909",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3fccc",
        "00b4036b"
      ]
    ],
    "bytes_sha256": "96db50ede81146f6353f04a21ec37fa4d02d102506c21d7b33b48651d28bd954",
    "instruction_count": 424,
    "instruction_bytes": 1696,
    "body_bytes": 1696,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 12640 bytes

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b3fccc"></a> `00b3fccc` | `ff 83 05 d1` | sub sp,sp,#0x160 | `FALL_THROUGH`
<a id="insn-00b3fcd0"></a> `00b3fcd0` | `fc 6f 10 a9` | stp x28,x27,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b3fcd4"></a> `00b3fcd4` | `fa 67 11 a9` | stp x26,x25,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b3fcd8"></a> `00b3fcd8` | `f8 5f 12 a9` | stp x24,x23,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00b3fcdc"></a> `00b3fcdc` | `f6 57 13 a9` | stp x22,x21,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00b3fce0"></a> `00b3fce0` | `f4 4f 14 a9` | stp x20,x19,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00b3fce4"></a> `00b3fce4` | `fd 7b 15 a9` | stp x29,x30,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00b3fce8"></a> `00b3fce8` | `fd 43 05 91` | add x29,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00b3fcec"></a> `00b3fcec` | `5c d0 3b d5` | mrs x28,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b3fcf0"></a> `00b3fcf0` | `89 17 40 f9` | ldr x9,[x28, #0x28] | `FALL_THROUGH`
<a id="insn-00b3fcf4"></a> `00b3fcf4` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00b3fcf8"></a> `00b3fcf8` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00b3fcfc"></a> `00b3fcfc` | `f8 03 01 aa` | mov x24,x1 | `FALL_THROUGH`
<a id="insn-00b3fd00"></a> `00b3fd00` | `a9 83 19 f8` | stur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00b3fd04"></a> `00b3fd04` | `29 00 40 39` | ldrb w9,[x1] | `FALL_THROUGH`
<a id="insn-00b3fd08"></a> `00b3fd08` | `2a 04 40 f9` | ldr x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00b3fd0c"></a> `00b3fd0c` | `14 00 40 f9` | ldr x20,[x0] | `FALL_THROUGH`
<a id="insn-00b3fd10"></a> `00b3fd10` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b3fd14"></a> `00b3fd14` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fd18"></a> `00b3fd18` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fd1c"></a> `00b3fd1c` | `6a 01 8a 9a` | csel x10,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00b3fd20"></a> `00b3fd20` | `5f 1d 00 f1` | cmp x10,#0x7 | `FALL_THROUGH`
<a id="insn-00b3fd24"></a> `00b3fd24` | `21 01 00 54` | b.ne 0x00b3fd48 | `CONDITIONAL_JUMP`
<a id="insn-00b3fd28"></a> `00b3fd28` | `08 0b 40 f9` | ldr x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b3fd2c"></a> `00b3fd2c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fd30"></a> `00b3fd30` | `01 bb ff 90` | adrp x1,0x29f000 | `FALL_THROUGH`
<a id="insn-00b3fd34"></a> `00b3fd34` | `21 5c 02 91` | add x1,x1,#0x97 | `FALL_THROUGH`
<a id="insn-00b3fd38"></a> `00b3fd38` | `00 15 98 9a` | csinc x0,x8,x24,ne | `FALL_THROUGH`
<a id="insn-00b3fd3c"></a> `00b3fd3c` | `e2 00 80 52` | mov w2,#0x7 | `FALL_THROUGH`
<a id="insn-00b3fd40"></a> `00b3fd40` | `30 6d 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fd44"></a> `00b3fd44` | `c0 06 00 34` | cbz w0,0x00b3fe1c | `CONDITIONAL_JUMP`
<a id="insn-00b3fd48"></a> `00b3fd48` | `e0 62 02 91` | add x0,x23,#0x98 | `FALL_THROUGH`
<a id="insn-00b3fd4c"></a> `00b3fd4c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00b3fd50"></a> `00b3fd50` | `dc 7f 02 94` | bl 0x00bdfcc0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fd54"></a> `00b3fd54` | `e8 82 02 91` | add x8,x23,#0xa0 | `FALL_THROUGH`
<a id="insn-00b3fd58"></a> `00b3fd58` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00b3fd5c"></a> `00b3fd5c` | `40 05 00 54` | b.eq 0x00b3fe04 | `CONDITIONAL_JUMP`
<a id="insn-00b3fd60"></a> `00b3fd60` | `16 1c 40 f9` | ldr x22,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00b3fd64"></a> `00b3fd64` | `16 05 00 b4` | cbz x22,0x00b3fe04 | `CONDITIONAL_JUMP`
<a id="insn-00b3fd68"></a> `00b3fd68` | `88 16 40 b9` | ldr w8,[x20, #0x14] | `FALL_THROUGH`
<a id="insn-00b3fd6c"></a> `00b3fd6c` | `1f 11 04 71` | cmp w8,#0x104 | `FALL_THROUGH`
<a id="insn-00b3fd70"></a> `00b3fd70` | `a1 02 00 54` | b.ne 0x00b3fdc4 | `CONDITIONAL_JUMP`
<a id="insn-00b3fd74"></a> `00b3fd74` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00b3fd78"></a> `00b3fd78` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00b3fd7c"></a> `00b3fd7c` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b3fd80"></a> `00b3fd80` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fd84"></a> `00b3fd84` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fd88"></a> `00b3fd88` | `6a 01 8a 9a` | csel x10,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00b3fd8c"></a> `00b3fd8c` | `5f 11 00 f1` | cmp x10,#0x4 | `FALL_THROUGH`
<a id="insn-00b3fd90"></a> `00b3fd90` | `a1 01 00 54` | b.ne 0x00b3fdc4 | `CONDITIONAL_JUMP`
<a id="insn-00b3fd94"></a> `00b3fd94` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00b3fd98"></a> `00b3fd98` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fd9c"></a> `00b3fd9c` | `c9 ad 8e 52` | mov w9,#0x756e | `FALL_THROUGH`
<a id="insn-00b3fda0"></a> `00b3fda0` | `89 8d ad 72` | movk w9,#0x6c6c, LSL #16 | `FALL_THROUGH`
<a id="insn-00b3fda4"></a> `00b3fda4` | `48 15 88 9a` | csinc x8,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00b3fda8"></a> `00b3fda8` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-00b3fdac"></a> `00b3fdac` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00b3fdb0"></a> `00b3fdb0` | `a1 00 00 54` | b.ne 0x00b3fdc4 | `CONDITIONAL_JUMP`
<a id="insn-00b3fdb4"></a> `00b3fdb4` | `c8 9a 40 b9` | ldr w8,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00b3fdb8"></a> `00b3fdb8` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fdbc"></a> `00b3fdbc` | `1f 31 00 71` | cmp w8,#0xc | `FALL_THROUGH`
<a id="insn-00b3fdc0"></a> `00b3fdc0` | `a2 2c 00 54` | b.cs 0x00b40354 | `CONDITIONAL_JUMP`
<a id="insn-00b3fdc4"></a> `00b3fdc4` | `c0 82 c9 3c` | ldur q0,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00b3fdc8"></a> `00b3fdc8` | `c1 82 ca 3c` | ldur q1,[x22, #0xa8] | `FALL_THROUGH`
<a id="insn-00b3fdcc"></a> `00b3fdcc` | `fa 83 02 91` | add x26,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b3fdd0"></a> `00b3fdd0` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00b3fdd4"></a> `00b3fdd4` | `ea 83 02 91` | add x10,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b3fdd8"></a> `00b3fdd8` | `40 07 00 ad` | stp q0,q1,[x26] | `FALL_THROUGH`
<a id="insn-00b3fddc"></a> `00b3fddc` | `ff ff 0c a9` | stp xzr,xzr,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00b3fde0"></a> `00b3fde0` | `ff 63 00 f9` | str xzr,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b3fde4"></a> `00b3fde4` | `09 8d 4b 38` | ldrb w9,[x8, #0xb8]! | `FALL_THROUGH`
<a id="insn-00b3fde8"></a> `00b3fde8` | `5b 81 00 91` | add x27,x10,#0x20 | `FALL_THROUGH`
<a id="insn-00b3fdec"></a> `00b3fdec` | `a9 05 00 37` | tbnz w9,#0x0,0x00b3fea0 | `CONDITIONAL_JUMP`
<a id="insn-00b3fdf0"></a> `00b3fdf0` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b3fdf4"></a> `00b3fdf4` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00b3fdf8"></a> `00b3fdf8` | `69 0b 00 f9` | str x9,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00b3fdfc"></a> `00b3fdfc` | `60 03 80 3d` | str q0,[x27] | `FALL_THROUGH`
<a id="insn-00b3fe00"></a> `00b3fe00` | `47 00 00 14` | b 0x00b3ff1c | `UNCONDITIONAL_JUMP`
<a id="insn-00b3fe04"></a> `00b3fe04` | `88 b6 4b 39` | ldrb w8,[x20, #0x2ed] | `FALL_THROUGH`
<a id="insn-00b3fe08"></a> `00b3fe08` | `c8 01 00 34` | cbz w8,0x00b3fe40 | `CONDITIONAL_JUMP`
<a id="insn-00b3fe0c"></a> `00b3fe0c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b3fe10"></a> `00b3fe10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3fe14"></a> `00b3fe14` | `bb 7e 02 94` | bl 0x00bdf900 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fe18"></a> `00b3fe18` | `05 00 00 14` | b 0x00b3fe2c | `UNCONDITIONAL_JUMP`
<a id="insn-00b3fe1c"></a> `00b3fe1c` | `21 20 80 52` | mov w1,#0x101 | `FALL_THROUGH`
<a id="insn-00b3fe20"></a> `00b3fe20` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b3fe24"></a> `00b3fe24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3fe28"></a> `00b3fe28` | `e2 7e 02 94` | bl 0x00bdf9b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fe2c"></a> `00b3fe2c` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00b3fe30"></a> `00b3fe30` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fe34"></a> `00b3fe34` | `69 06 00 39` | strb w9,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00b3fe38"></a> `00b3fe38` | `68 27 00 35` | cbnz w8,0x00b40324 | `CONDITIONAL_JUMP`
<a id="insn-00b3fe3c"></a> `00b3fe3c` | `39 01 00 14` | b 0x00b40320 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3fe40"></a> `00b3fe40` | `80 bb ff b0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00b3fe44"></a> `00b3fe44` | `00 78 1a 91` | add x0,x0,#0x69e | `FALL_THROUGH`
<a id="insn-00b3fe48"></a> `00b3fe48` | `e8 83 02 91` | add x8,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b3fe4c"></a> `00b3fe4c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00b3fe50"></a> `00b3fe50` | `04 6d 02 94` | bl 0x00bdb260 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fe54"></a> `00b3fe54` | `80 ba ff d0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00b3fe58"></a> `00b3fe58` | `00 14 15 91` | add x0,x0,#0x545 | `FALL_THROUGH`
<a id="insn-00b3fe5c"></a> `00b3fe5c` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b3fe60"></a> `00b3fe60` | `e1 83 02 91` | add x1,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b3fe64"></a> `00b3fe64` | `ff 6c 02 94` | bl 0x00bdb260 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fe68"></a> `00b3fe68` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b3fe6c"></a> `00b3fe6c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3fe70"></a> `00b3fe70` | `d8 7e 02 94` | bl 0x00bdf9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fe74"></a> `00b3fe74` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3fe78"></a> `00b3fe78` | `68 00 00 36` | tbz w8,#0x0,0x00b3fe84 | `CONDITIONAL_JUMP`
<a id="insn-00b3fe7c"></a> `00b3fe7c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3fe80"></a> `00b3fe80` | `78 6c 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fe84"></a> `00b3fe84` | `e8 83 42 39` | ldrb w8,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b3fe88"></a> `00b3fe88` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fe8c"></a> `00b3fe8c` | `69 02 00 79` | strh w9,[x19] | `FALL_THROUGH`
<a id="insn-00b3fe90"></a> `00b3fe90` | `a8 24 00 36` | tbz w8,#0x0,0x00b40324 | `CONDITIONAL_JUMP`
<a id="insn-00b3fe94"></a> `00b3fe94` | `e0 5b 40 f9` | ldr x0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00b3fe98"></a> `00b3fe98` | `72 6c 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fe9c"></a> `00b3fe9c` | `22 01 00 14` | b 0x00b40324 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3fea0"></a> `00b3fea0` | `d8 62 40 f9` | ldr x24,[x22, #0xc0] | `FALL_THROUGH`
<a id="insn-00b3fea4"></a> `00b3fea4` | `1f 43 00 b1` | cmn x24,#0x10 | `FALL_THROUGH`
<a id="insn-00b3fea8"></a> `00b3fea8` | `02 26 00 54` | b.cs 0x00b40368 | `CONDITIONAL_JUMP`
<a id="insn-00b3feac"></a> `00b3feac` | `d9 66 40 f9` | ldr x25,[x22, #0xc8] | `FALL_THROUGH`
<a id="insn-00b3feb0"></a> `00b3feb0` | `1f 5f 00 f1` | cmp x24,#0x17 | `FALL_THROUGH`
<a id="insn-00b3feb4"></a> `00b3feb4` | `c2 00 00 54` | b.cs 0x00b3fecc | `CONDITIONAL_JUMP`
<a id="insn-00b3feb8"></a> `00b3feb8` | `08 7b 1f 53` | lsl w8,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00b3febc"></a> `00b3febc` | `7a 07 00 91` | add x26,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fec0"></a> `00b3fec0` | `e8 03 03 39` | strb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b3fec4"></a> `00b3fec4` | `18 02 00 b5` | cbnz x24,0x00b3ff04 | `CONDITIONAL_JUMP`
<a id="insn-00b3fec8"></a> `00b3fec8` | `13 00 00 14` | b 0x00b3ff14 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3fecc"></a> `00b3fecc` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00b3fed0"></a> `00b3fed0` | `fc 03 00 f9` | str x28,[sp] | `FALL_THROUGH`
<a id="insn-00b3fed4"></a> `00b3fed4` | `fc 03 15 aa` | mov x28,x21 | `FALL_THROUGH`
<a id="insn-00b3fed8"></a> `00b3fed8` | `f5 03 1b aa` | mov x21,x27 | `FALL_THROUGH`
<a id="insn-00b3fedc"></a> `00b3fedc` | `1b ed 7c 92` | and x27,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00b3fee0"></a> `00b3fee0` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00b3fee4"></a> `00b3fee4` | `57 6c 02 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fee8"></a> `00b3fee8` | `68 03 40 b2` | orr x8,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00b3feec"></a> `00b3feec` | `fb 03 15 aa` | mov x27,x21 | `FALL_THROUGH`
<a id="insn-00b3fef0"></a> `00b3fef0` | `f5 03 1c aa` | mov x21,x28 | `FALL_THROUGH`
<a id="insn-00b3fef4"></a> `00b3fef4` | `fc 03 40 f9` | ldr x28,[sp] | `FALL_THROUGH`
<a id="insn-00b3fef8"></a> `00b3fef8` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00b3fefc"></a> `00b3fefc` | `e8 63 0c a9` | stp x8,x24,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b3ff00"></a> `00b3ff00` | `e0 6b 00 f9` | str x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b3ff04"></a> `00b3ff04` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00b3ff08"></a> `00b3ff08` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00b3ff0c"></a> `00b3ff0c` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00b3ff10"></a> `00b3ff10` | `a8 6c 02 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ff14"></a> `00b3ff14` | `5f 6b 38 38` | strb wzr,[x26, x24, LSL ] | `FALL_THROUGH`
<a id="insn-00b3ff18"></a> `00b3ff18` | `fa 83 02 91` | add x26,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b3ff1c"></a> `00b3ff1c` | `c8 a2 41 79` | ldrh w8,[x22, #0xd0] | `FALL_THROUGH`
<a id="insn-00b3ff20"></a> `00b3ff20` | `e8 b3 01 79` | strh w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00b3ff24"></a> `00b3ff24` | `c8 76 43 39` | ldrb w8,[x22, #0xdd] | `FALL_THROUGH`
<a id="insn-00b3ff28"></a> `00b3ff28` | `88 07 00 34` | cbz w8,0x00b40018 | `CONDITIONAL_JUMP`
<a id="insn-00b3ff2c"></a> `00b3ff2c` | `00 80 80 52` | mov w0,#0x400 | `FALL_THROUGH`
<a id="insn-00b3ff30"></a> `00b3ff30` | `44 6c 02 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ff34"></a> `00b3ff34` | `08 00 10 91` | add x8,x0,#0x400 | `FALL_THROUGH`
<a id="insn-00b3ff38"></a> `00b3ff38` | `02 80 80 52` | mov w2,#0x400 | `FALL_THROUGH`
<a id="insn-00b3ff3c"></a> `00b3ff3c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b3ff40"></a> `00b3ff40` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00b3ff44"></a> `00b3ff44` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3ff48"></a> `00b3ff48` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3ff4c"></a> `00b3ff4c` | `bd 6c 02 94` | bl 0x00bdb240 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ff50"></a> `00b3ff50` | `88 bb ff f0` | adrp x8,0x2b2000 | `FALL_THROUGH`
<a id="insn-00b3ff54"></a> `00b3ff54` | `f9 83 00 91` | add x25,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b3ff58"></a> `00b3ff58` | `00 c9 45 fd` | ldr d0,[x8, #0xb90] | `FALL_THROUGH`
<a id="insn-00b3ff5c"></a> `00b3ff5c` | `28 23 01 91` | add x8,x25,#0x48 | `FALL_THROUGH`
<a id="insn-00b3ff60"></a> `00b3ff60` | `e8 7f 06 a9` | stp x8,xzr,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b3ff64"></a> `00b3ff64` | `28 a3 01 91` | add x8,x25,#0x68 | `FALL_THROUGH`
<a id="insn-00b3ff68"></a> `00b3ff68` | `e8 7f 08 a9` | stp x8,xzr,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b3ff6c"></a> `00b3ff6c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b3ff70"></a> `00b3ff70` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b3ff74"></a> `00b3ff74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3ff78"></a> `00b3ff78` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3ff7c"></a> `00b3ff7c` | `ff 43 01 39` | strb wzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3ff80"></a> `00b3ff80` | `ff 67 07 a9` | stp xzr,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b3ff84"></a> `00b3ff84` | `ff 67 09 a9` | stp xzr,x25,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b3ff88"></a> `00b3ff88` | `e0 43 05 fc` | stur d0,[sp, #0x54] | `FALL_THROUGH`
<a id="insn-00b3ff8c"></a> `00b3ff8c` | `ff 1f 00 f9` | str xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b3ff90"></a> `00b3ff90` | `f7 17 00 f9` | str x23,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b3ff94"></a> `00b3ff94` | `6b 7e 02 94` | bl 0x00bdf940 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ff98"></a> `00b3ff98` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00b3ff9c"></a> `00b3ff9c` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ffa0"></a> `00b3ffa0` | `77 06 00 39` | strb w23,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00b3ffa4"></a> `00b3ffa4` | `48 0a 00 35` | cbnz w8,0x00b400ec | `CONDITIONAL_JUMP`
<a id="insn-00b3ffa8"></a> `00b3ffa8` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b3ffac"></a> `00b3ffac` | `e1 7e 02 94` | bl 0x00bdfb30 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ffb0"></a> `00b3ffb0` | `88 ce 40 f9` | ldr x8,[x20, #0x198] | `FALL_THROUGH`
<a id="insn-00b3ffb4"></a> `00b3ffb4` | `ea 27 42 a9` | ldp x10,x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3ffb8"></a> `00b3ffb8` | `97 42 05 91` | add x23,x20,#0x150 | `FALL_THROUGH`
<a id="insn-00b3ffbc"></a> `00b3ffbc` | `1f 1d 00 f1` | cmp x8,#0x7 | `FALL_THROUGH`
<a id="insn-00b3ffc0"></a> `00b3ffc0` | `28 01 0a cb` | sub x8,x9,x10 | `FALL_THROUGH`
<a id="insn-00b3ffc4"></a> `00b3ffc4` | `68 00 00 54` | b.hi 0x00b3ffd0 | `CONDITIONAL_JUMP`
<a id="insn-00b3ffc8"></a> `00b3ffc8` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00b3ffcc"></a> `00b3ffcc` | `89 ce 00 f9` | str x9,[x20, #0x198] | `FALL_THROUGH`
<a id="insn-00b3ffd0"></a> `00b3ffd0` | `8a 72 41 b9` | ldr w10,[x20, #0x170] | `FALL_THROUGH`
<a id="insn-00b3ffd4"></a> `00b3ffd4` | `89 32 58 a9` | ldp x9,x12,[x20, #0x180] | `FALL_THROUGH`
<a id="insn-00b3ffd8"></a> `00b3ffd8` | `8b 7a 41 b9` | ldr w11,[x20, #0x178] | `FALL_THROUGH`
<a id="insn-00b3ffdc"></a> `00b3ffdc` | `4a 01 09 4b` | sub w10,w10,w9 | `FALL_THROUGH`
<a id="insn-00b3ffe0"></a> `00b3ffe0` | `4a 01 0b 0b` | add w10,w10,w11 | `FALL_THROUGH`
<a id="insn-00b3ffe4"></a> `00b3ffe4` | `08 01 0a 0b` | add w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00b3ffe8"></a> `00b3ffe8` | `e8 03 08 4b` | neg w8,w8 | `FALL_THROUGH`
<a id="insn-00b3ffec"></a> `00b3ffec` | `18 09 40 92` | and x24,x8,#0x7 | `FALL_THROUGH`
<a id="insn-00b3fff0"></a> `00b3fff0` | `28 01 0c cb` | sub x8,x9,x12 | `FALL_THROUGH`
<a id="insn-00b3fff4"></a> `00b3fff4` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00b3fff8"></a> `00b3fff8` | `62 03 00 54` | b.cs 0x00b40064 | `CONDITIONAL_JUMP`
<a id="insn-00b3fffc"></a> `00b3fffc` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b40000"></a> `00b40000` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00b40004"></a> `00b40004` | `e3 7c 02 94` | bl 0x00bdf390 | `UNCONDITIONAL_CALL`
<a id="insn-00b40008"></a> `00b40008` | `88 c2 40 f9` | ldr x8,[x20, #0x180] | `FALL_THROUGH`
<a id="insn-00b4000c"></a> `00b4000c` | `08 01 18 cb` | sub x8,x8,x24 | `FALL_THROUGH`
<a id="insn-00b40010"></a> `00b40010` | `88 c2 00 f9` | str x8,[x20, #0x180] | `FALL_THROUGH`
<a id="insn-00b40014"></a> `00b40014` | `17 00 00 14` | b 0x00b40070 | `UNCONDITIONAL_JUMP`
<a id="insn-00b40018"></a> `00b40018` | `c8 72 40 f9` | ldr x8,[x22, #0xe0] | `FALL_THROUGH`
<a id="insn-00b4001c"></a> `00b4001c` | `48 01 00 b4` | cbz x8,0x00b40044 | `CONDITIONAL_JUMP`
<a id="insn-00b40020"></a> `00b40020` | `a3 02 40 f9` | ldr x3,[x21] | `FALL_THROUGH`
<a id="insn-00b40024"></a> `00b40024` | `e1 83 02 91` | add x1,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b40028"></a> `00b40028` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b4002c"></a> `00b4002c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b40030"></a> `00b40030` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b40034"></a> `00b40034` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00b40038"></a> `00b40038` | `46 7e 02 94` | bl 0x00bdf950 | `UNCONDITIONAL_CALL`
<a id="insn-00b4003c"></a> `00b4003c` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00b40040"></a> `00b40040` | `4f 00 00 14` | b 0x00b4017c | `UNCONDITIONAL_JUMP`
<a id="insn-00b40044"></a> `00b40044` | `88 b6 44 b9` | ldr w8,[x20, #0x4b4] | `FALL_THROUGH`
<a id="insn-00b40048"></a> `00b40048` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00b4004c"></a> `00b4004c` | `6b 07 00 54` | b.lt 0x00b40138 | `CONDITIONAL_JUMP`
<a id="insn-00b40050"></a> `00b40050` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b40054"></a> `00b40054` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b40058"></a> `00b40058` | `e6 7d 02 94` | bl 0x00bdf7f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4005c"></a> `00b4005c` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00b40060"></a> `00b40060` | `47 00 00 14` | b 0x00b4017c | `UNCONDITIONAL_JUMP`
<a id="insn-00b40064"></a> `00b40064` | `28 01 18 cb` | sub x8,x9,x24 | `FALL_THROUGH`
<a id="insn-00b40068"></a> `00b40068` | `88 c2 00 f9` | str x8,[x20, #0x180] | `FALL_THROUGH`
<a id="insn-00b4006c"></a> `00b4006c` | `58 01 00 b4` | cbz x24,0x00b40094 | `CONDITIONAL_JUMP`
<a id="insn-00b40070"></a> `00b40070` | `1f 07 00 f1` | cmp x24,#0x1 | `FALL_THROUGH`
<a id="insn-00b40074"></a> `00b40074` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00b40078"></a> `00b40078` | `e0 00 00 54` | b.eq 0x00b40094 | `CONDITIONAL_JUMP`
<a id="insn-00b4007c"></a> `00b4007c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b40080"></a> `00b40080` | `89 c2 40 f9` | ldr x9,[x20, #0x180] | `FALL_THROUGH`
<a id="insn-00b40084"></a> `00b40084` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00b40088"></a> `00b40088` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b4008c"></a> `00b4008c` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00b40090"></a> `00b40090` | `81 ff ff 54` | b.ne 0x00b40080 | `CONDITIONAL_JUMP`
<a id="insn-00b40094"></a> `00b40094` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b40098"></a> `00b40098` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b4009c"></a> `00b4009c` | `11 7d 02 94` | bl 0x00bdf4e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b400a0"></a> `00b400a0` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b400a4"></a> `00b400a4` | `43 7c 02 94` | bl 0x00bdf1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b400a8"></a> `00b400a8` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b400ac"></a> `00b400ac` | `68 00 00 37` | tbnz w8,#0x0,0x00b400b8 | `CONDITIONAL_JUMP`
<a id="insn-00b400b0"></a> `00b400b0` | `ff 83 01 79` | strh wzr,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b400b4"></a> `00b400b4` | `09 00 00 14` | b 0x00b400d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b400b8"></a> `00b400b8` | `e8 6b 40 f9` | ldr x8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b400bc"></a> `00b400bc` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00b400c0"></a> `00b400c0` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b400c4"></a> `00b400c4` | `ff 67 00 f9` | str xzr,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00b400c8"></a> `00b400c8` | `88 00 00 36` | tbz w8,#0x0,0x00b400d8 | `CONDITIONAL_JUMP`
<a id="insn-00b400cc"></a> `00b400cc` | `e0 6b 40 f9` | ldr x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b400d0"></a> `00b400d0` | `e4 6b 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b400d4"></a> `00b400d4` | `ff 63 00 f9` | str xzr,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b400d8"></a> `00b400d8` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b400dc"></a> `00b400dc` | `e0 83 c0 3c` | ldur q0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b400e0"></a> `00b400e0` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00b400e4"></a> `00b400e4` | `68 0b 00 f9` | str x8,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00b400e8"></a> `00b400e8` | `60 03 80 3d` | str q0,[x27] | `FALL_THROUGH`
<a id="insn-00b400ec"></a> `00b400ec` | `e1 47 40 f9` | ldr x1,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00b400f0"></a> `00b400f0` | `20 83 01 91` | add x0,x25,#0x60 | `FALL_THROUGH`
<a id="insn-00b400f4"></a> `00b400f4` | `c3 7a 02 94` | bl 0x00bdec00 | `UNCONDITIONAL_CALL`
<a id="insn-00b400f8"></a> `00b400f8` | `e1 37 40 f9` | ldr x1,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00b400fc"></a> `00b400fc` | `20 03 01 91` | add x0,x25,#0x40 | `FALL_THROUGH`
<a id="insn-00b40100"></a> `00b40100` | `c4 7a 02 94` | bl 0x00bdec10 | `UNCONDITIONAL_CALL`
<a id="insn-00b40104"></a> `00b40104` | `e0 1f 40 f9` | ldr x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b40108"></a> `00b40108` | `60 00 00 b4` | cbz x0,0x00b40114 | `CONDITIONAL_JUMP`
<a id="insn-00b4010c"></a> `00b4010c` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b40110"></a> `00b40110` | `d4 6b 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b40114"></a> `00b40114` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b40118"></a> `00b40118` | `60 00 00 b4` | cbz x0,0x00b40124 | `CONDITIONAL_JUMP`
<a id="insn-00b4011c"></a> `00b4011c` | `e0 17 00 f9` | str x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b40120"></a> `00b40120` | `d0 6b 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b40124"></a> `00b40124` | `37 03 00 34` | cbz w23,0x00b40188 | `CONDITIONAL_JUMP`
<a id="insn-00b40128"></a> `00b40128` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00b4012c"></a> `00b4012c` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b40130"></a> `00b40130` | `28 0f 00 37` | tbnz w8,#0x0,0x00b40314 | `CONDITIONAL_JUMP`
<a id="insn-00b40134"></a> `00b40134` | `7a 00 00 14` | b 0x00b4031c | `UNCONDITIONAL_JUMP`
<a id="insn-00b40138"></a> `00b40138` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b4013c"></a> `00b4013c` | `88 b6 04 b9` | str w8,[x20, #0x4b4] | `FALL_THROUGH`
<a id="insn-00b40140"></a> `00b40140` | `a3 02 40 f9` | ldr x3,[x21] | `FALL_THROUGH`
<a id="insn-00b40144"></a> `00b40144` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b40148"></a> `00b40148` | `e1 83 02 91` | add x1,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b4014c"></a> `00b4014c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b40150"></a> `00b40150` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b40154"></a> `00b40154` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00b40158"></a> `00b40158` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00b4015c"></a> `00b4015c` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00b40160"></a> `00b40160` | `a8 7d 02 94` | bl 0x00bdf800 | `UNCONDITIONAL_CALL`
<a id="insn-00b40164"></a> `00b40164` | `88 b6 44 b9` | ldr w8,[x20, #0x4b4] | `FALL_THROUGH`
<a id="insn-00b40168"></a> `00b40168` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b4016c"></a> `00b4016c` | `88 b6 04 b9` | str w8,[x20, #0x4b4] | `FALL_THROUGH`
<a id="insn-00b40170"></a> `00b40170` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b40174"></a> `00b40174` | `7f 06 00 39` | strb wzr,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00b40178"></a> `00b40178` | `68 02 00 39` | strb w8,[x19] | `FALL_THROUGH`
<a id="insn-00b4017c"></a> `00b4017c` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00b40180"></a> `00b40180` | `77 06 00 39` | strb w23,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00b40184"></a> `00b40184` | `48 0c 00 35` | cbnz w8,0x00b4030c | `CONDITIONAL_JUMP`
<a id="insn-00b40188"></a> `00b40188` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b4018c"></a> `00b4018c` | `97 52 42 f9` | ldr x23,[x20, #0x4a0] | `FALL_THROUGH`
<a id="insn-00b40190"></a> `00b40190` | `68 02 00 b4` | cbz x8,0x00b401dc | `CONDITIONAL_JUMP`
<a id="insn-00b40194"></a> `00b40194` | `09 09 80 52` | mov w9,#0x48 | `FALL_THROUGH`
<a id="insn-00b40198"></a> `00b40198` | `ea 08 80 92` | mov x10,#-0x48 | `FALL_THROUGH`
<a id="insn-00b4019c"></a> `00b4019c` | `0b fd 09 9b` | mneg x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00b401a0"></a> `00b401a0` | `09 7d 0a 9b` | mul x9,x8,x10 | `FALL_THROUGH`
<a id="insn-00b401a4"></a> `00b401a4` | `e8 02 0b 8b` | add x8,x23,x11 | `FALL_THROUGH`
<a id="insn-00b401a8"></a> `00b401a8` | `ea 22 01 d1` | sub x10,x23,#0x48 | `FALL_THROUGH`
<a id="insn-00b401ac"></a> `00b401ac` | `4b 21 40 f9` | ldr x11,[x10, #0x40] | `FALL_THROUGH`
<a id="insn-00b401b0"></a> `00b401b0` | `7f 01 16 eb` | cmp x11,x22 | `FALL_THROUGH`
<a id="insn-00b401b4"></a> `00b401b4` | `40 04 00 54` | b.eq 0x00b4023c | `CONDITIONAL_JUMP`
<a id="insn-00b401b8"></a> `00b401b8` | `6b a1 41 79` | ldrh w11,[x11, #0xd0] | `FALL_THROUGH`
<a id="insn-00b401bc"></a> `00b401bc` | `cc a2 41 79` | ldrh w12,[x22, #0xd0] | `FALL_THROUGH`
<a id="insn-00b401c0"></a> `00b401c0` | `7f 01 0c 6b` | cmp w11,w12 | `FALL_THROUGH`
<a id="insn-00b401c4"></a> `00b401c4` | `c3 00 00 54` | b.cc 0x00b401dc | `CONDITIONAL_JUMP`
<a id="insn-00b401c8"></a> `00b401c8` | `f7 03 0a aa` | mov x23,x10 | `FALL_THROUGH`
<a id="insn-00b401cc"></a> `00b401cc` | `29 21 01 91` | add x9,x9,#0x48 | `FALL_THROUGH`
<a id="insn-00b401d0"></a> `00b401d0` | `4a 21 01 d1` | sub x10,x10,#0x48 | `FALL_THROUGH`
<a id="insn-00b401d4"></a> `00b401d4` | `c9 fe ff b5` | cbnz x9,0x00b401ac | `CONDITIONAL_JUMP`
<a id="insn-00b401d8"></a> `00b401d8` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00b401dc"></a> `00b401dc` | `40 07 40 ad` | ldp q0,q1,[x26] | `FALL_THROUGH`
<a id="insn-00b401e0"></a> `00b401e0` | `e9 03 43 39` | ldrb w9,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b401e4"></a> `00b401e4` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b401e8"></a> `00b401e8` | `08 81 00 91` | add x8,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00b401ec"></a> `00b401ec` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b401f0"></a> `00b401f0` | `e0 07 01 ad` | stp q0,q1,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b401f4"></a> `00b401f4` | `ff 2b 00 f9` | str xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b401f8"></a> `00b401f8` | `c9 00 00 37` | tbnz w9,#0x0,0x00b40210 | `CONDITIONAL_JUMP`
<a id="insn-00b401fc"></a> `00b401fc` | `69 0b 40 f9` | ldr x9,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00b40200"></a> `00b40200` | `60 03 c0 3d` | ldr q0,[x27] | `FALL_THROUGH`
<a id="insn-00b40204"></a> `00b40204` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b40208"></a> `00b40208` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00b4020c"></a> `00b4020c` | `31 00 00 14` | b 0x00b402d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b40210"></a> `00b40210` | `f8 67 40 f9` | ldr x24,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00b40214"></a> `00b40214` | `1f 43 00 b1` | cmn x24,#0x10 | `FALL_THROUGH`
<a id="insn-00b40218"></a> `00b40218` | `82 0a 00 54` | b.cs 0x00b40368 | `CONDITIONAL_JUMP`
<a id="insn-00b4021c"></a> `00b4021c` | `f9 6b 40 f9` | ldr x25,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b40220"></a> `00b40220` | `1f 5f 00 f1` | cmp x24,#0x17 | `FALL_THROUGH`
<a id="insn-00b40224"></a> `00b40224` | `c2 03 00 54` | b.cs 0x00b4029c | `CONDITIONAL_JUMP`
<a id="insn-00b40228"></a> `00b40228` | `09 7b 1f 53` | lsl w9,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00b4022c"></a> `00b4022c` | `1a 05 00 91` | add x26,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b40230"></a> `00b40230` | `e9 03 01 39` | strb w9,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b40234"></a> `00b40234` | `58 04 00 b5` | cbnz x24,0x00b402bc | `CONDITIONAL_JUMP`
<a id="insn-00b40238"></a> `00b40238` | `25 00 00 14` | b 0x00b402cc | `UNCONDITIONAL_JUMP`
<a id="insn-00b4023c"></a> `00b4023c` | `60 bb ff f0` | adrp x0,0x2af000 | `FALL_THROUGH`
<a id="insn-00b40240"></a> `00b40240` | `00 08 15 91` | add x0,x0,#0x542 | `FALL_THROUGH`
<a id="insn-00b40244"></a> `00b40244` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b40248"></a> `00b40248` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4024c"></a> `00b4024c` | `05 6c 02 94` | bl 0x00bdb260 | `UNCONDITIONAL_CALL`
<a id="insn-00b40250"></a> `00b40250` | `80 ba ff b0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00b40254"></a> `00b40254` | `00 14 15 91` | add x0,x0,#0x545 | `FALL_THROUGH`
<a id="insn-00b40258"></a> `00b40258` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4025c"></a> `00b4025c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b40260"></a> `00b40260` | `00 6c 02 94` | bl 0x00bdb260 | `UNCONDITIONAL_CALL`
<a id="insn-00b40264"></a> `00b40264` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b40268"></a> `00b40268` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b4026c"></a> `00b4026c` | `d9 7d 02 94` | bl 0x00bdf9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00b40270"></a> `00b40270` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b40274"></a> `00b40274` | `68 00 00 36` | tbz w8,#0x0,0x00b40280 | `CONDITIONAL_JUMP`
<a id="insn-00b40278"></a> `00b40278` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b4027c"></a> `00b4027c` | `79 6b 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b40280"></a> `00b40280` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b40284"></a> `00b40284` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b40288"></a> `00b40288` | `69 02 00 79` | strh w9,[x19] | `FALL_THROUGH`
<a id="insn-00b4028c"></a> `00b4028c` | `e8 f4 07 36` | tbz w8,#0x0,0x00b40128 | `CONDITIONAL_JUMP`
<a id="insn-00b40290"></a> `00b40290` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b40294"></a> `00b40294` | `73 6b 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b40298"></a> `00b40298` | `a4 ff ff 17` | b 0x00b40128 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4029c"></a> `00b4029c` | `08 43 00 91` | add x8,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00b402a0"></a> `00b402a0` | `1b ed 7c 92` | and x27,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00b402a4"></a> `00b402a4` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00b402a8"></a> `00b402a8` | `66 6b 02 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00b402ac"></a> `00b402ac` | `68 03 40 b2` | orr x8,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00b402b0"></a> `00b402b0` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00b402b4"></a> `00b402b4` | `e8 63 04 a9` | stp x8,x24,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b402b8"></a> `00b402b8` | `e0 2b 00 f9` | str x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b402bc"></a> `00b402bc` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00b402c0"></a> `00b402c0` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00b402c4"></a> `00b402c4` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00b402c8"></a> `00b402c8` | `ba 6b 02 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b402cc"></a> `00b402cc` | `5f 6b 38 38` | strb wzr,[x26, x24, LSL ] | `FALL_THROUGH`
<a id="insn-00b402d0"></a> `00b402d0` | `e8 b3 41 79` | ldrh w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00b402d4"></a> `00b402d4` | `80 62 12 91` | add x0,x20,#0x498 | `FALL_THROUGH`
<a id="insn-00b402d8"></a> `00b402d8` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b402dc"></a> `00b402dc` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b402e0"></a> `00b402e0` | `e8 b3 00 79` | strh w8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00b402e4"></a> `00b402e4` | `f6 33 00 f9` | str x22,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b402e8"></a> `00b402e8` | `72 7f 02 94` | bl 0x00be00b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b402ec"></a> `00b402ec` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b402f0"></a> `00b402f0` | `68 00 00 36` | tbz w8,#0x0,0x00b402fc | `CONDITIONAL_JUMP`
<a id="insn-00b402f4"></a> `00b402f4` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b402f8"></a> `00b402f8` | `5a 6b 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b402fc"></a> `00b402fc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b40300"></a> `00b40300` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00b40304"></a> `00b40304` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b40308"></a> `00b40308` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00b4030c"></a> `00b4030c` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b40310"></a> `00b40310` | `68 00 00 36` | tbz w8,#0x0,0x00b4031c | `CONDITIONAL_JUMP`
<a id="insn-00b40314"></a> `00b40314` | `e0 6b 40 f9` | ldr x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b40318"></a> `00b40318` | `52 6b 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b4031c"></a> `00b4031c` | `57 00 00 35` | cbnz w23,0x00b40324 | `CONDITIONAL_JUMP`
<a id="insn-00b40320"></a> `00b40320` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-00b40324"></a> `00b40324` | `88 17 40 f9` | ldr x8,[x28, #0x28] | `FALL_THROUGH`
<a id="insn-00b40328"></a> `00b40328` | `a9 83 59 f8` | ldur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00b4032c"></a> `00b4032c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b40330"></a> `00b40330` | `a1 01 00 54` | b.ne 0x00b40364 | `CONDITIONAL_JUMP`
<a id="insn-00b40334"></a> `00b40334` | `fd 7b 55 a9` | ldp x29,x30,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00b40338"></a> `00b40338` | `f4 4f 54 a9` | ldp x20,x19,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00b4033c"></a> `00b4033c` | `f6 57 53 a9` | ldp x22,x21,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00b40340"></a> `00b40340` | `f8 5f 52 a9` | ldp x24,x23,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00b40344"></a> `00b40344` | `fa 67 51 a9` | ldp x26,x25,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b40348"></a> `00b40348` | `fc 6f 50 a9` | ldp x28,x27,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b4034c"></a> `00b4034c` | `ff 83 05 91` | add sp,sp,#0x160 | `FALL_THROUGH`
<a id="insn-00b40350"></a> `00b40350` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b40354"></a> `00b40354` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b40358"></a> `00b40358` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b4035c"></a> `00b4035c` | `85 7d 02 94` | bl 0x00bdf970 | `UNCONDITIONAL_CALL`
<a id="insn-00b40360"></a> `00b40360` | `b3 fe ff 17` | b 0x00b3fe2c | `UNCONDITIONAL_JUMP`
<a id="insn-00b40364"></a> `00b40364` | `4b 6b 02 94` | bl 0x00bdb090 | `CALL_TERMINATOR`
<a id="insn-00b40368"></a> `00b40368` | `d6 77 02 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3fccc`](#insn-00b3fccc) 範囲 `[['00b3fccc', '00b3fd27']]`
  - `CONDITIONAL_JUMP` [`00b3fd24`](#insn-00b3fd24) → [`00b3fd48`](#insn-00b3fd48)
  - `FALL_THROUGH` [`00b3fd24`](#insn-00b3fd24) → [`00b3fd28`](#insn-00b3fd28)
- ブロック [`00b3fd28`](#insn-00b3fd28) 範囲 `[['00b3fd28', '00b3fd47']]`
  - `CONDITIONAL_JUMP` [`00b3fd44`](#insn-00b3fd44) → [`00b3fe1c`](#insn-00b3fe1c)
  - `FALL_THROUGH` [`00b3fd44`](#insn-00b3fd44) → [`00b3fd48`](#insn-00b3fd48)
- ブロック [`00b3fd48`](#insn-00b3fd48) 範囲 `[['00b3fd48', '00b3fd5f']]`
  - `CONDITIONAL_JUMP` [`00b3fd5c`](#insn-00b3fd5c) → [`00b3fe04`](#insn-00b3fe04)
  - `FALL_THROUGH` [`00b3fd5c`](#insn-00b3fd5c) → [`00b3fd60`](#insn-00b3fd60)
- ブロック [`00b3fd60`](#insn-00b3fd60) 範囲 `[['00b3fd60', '00b3fd67']]`
  - `CONDITIONAL_JUMP` [`00b3fd64`](#insn-00b3fd64) → [`00b3fe04`](#insn-00b3fe04)
  - `FALL_THROUGH` [`00b3fd64`](#insn-00b3fd64) → [`00b3fd68`](#insn-00b3fd68)
- ブロック [`00b3fd68`](#insn-00b3fd68) 範囲 `[['00b3fd68', '00b3fd73']]`
  - `CONDITIONAL_JUMP` [`00b3fd70`](#insn-00b3fd70) → [`00b3fdc4`](#insn-00b3fdc4)
  - `FALL_THROUGH` [`00b3fd70`](#insn-00b3fd70) → [`00b3fd74`](#insn-00b3fd74)
- ブロック [`00b3fd74`](#insn-00b3fd74) 範囲 `[['00b3fd74', '00b3fd93']]`
  - `CONDITIONAL_JUMP` [`00b3fd90`](#insn-00b3fd90) → [`00b3fdc4`](#insn-00b3fdc4)
  - `FALL_THROUGH` [`00b3fd90`](#insn-00b3fd90) → [`00b3fd94`](#insn-00b3fd94)
- ブロック [`00b3fd94`](#insn-00b3fd94) 範囲 `[['00b3fd94', '00b3fdb3']]`
  - `CONDITIONAL_JUMP` [`00b3fdb0`](#insn-00b3fdb0) → [`00b3fdc4`](#insn-00b3fdc4)
  - `FALL_THROUGH` [`00b3fdb0`](#insn-00b3fdb0) → [`00b3fdb4`](#insn-00b3fdb4)
- ブロック [`00b3fdb4`](#insn-00b3fdb4) 範囲 `[['00b3fdb4', '00b3fdc3']]`
  - `CONDITIONAL_JUMP` [`00b3fdc0`](#insn-00b3fdc0) → [`00b40354`](#insn-00b40354)
  - `FALL_THROUGH` [`00b3fdc0`](#insn-00b3fdc0) → [`00b3fdc4`](#insn-00b3fdc4)
- ブロック [`00b3fdc4`](#insn-00b3fdc4) 範囲 `[['00b3fdc4', '00b3fdef']]`
  - `CONDITIONAL_JUMP` [`00b3fdec`](#insn-00b3fdec) → [`00b3fea0`](#insn-00b3fea0)
  - `FALL_THROUGH` [`00b3fdec`](#insn-00b3fdec) → [`00b3fdf0`](#insn-00b3fdf0)
- ブロック [`00b3fdf0`](#insn-00b3fdf0) 範囲 `[['00b3fdf0', '00b3fe03']]`
  - `UNCONDITIONAL_JUMP` [`00b3fe00`](#insn-00b3fe00) → [`00b3ff1c`](#insn-00b3ff1c)
- ブロック [`00b3fe04`](#insn-00b3fe04) 範囲 `[['00b3fe04', '00b3fe0b']]`
  - `CONDITIONAL_JUMP` [`00b3fe08`](#insn-00b3fe08) → [`00b3fe40`](#insn-00b3fe40)
  - `FALL_THROUGH` [`00b3fe08`](#insn-00b3fe08) → [`00b3fe0c`](#insn-00b3fe0c)
- ブロック [`00b3fe0c`](#insn-00b3fe0c) 範囲 `[['00b3fe0c', '00b3fe1b']]`
  - `UNCONDITIONAL_JUMP` [`00b3fe18`](#insn-00b3fe18) → [`00b3fe2c`](#insn-00b3fe2c)
- ブロック [`00b3fe1c`](#insn-00b3fe1c) 範囲 `[['00b3fe1c', '00b3fe2b']]`
  - `FALL_THROUGH` [`00b3fe28`](#insn-00b3fe28) → [`00b3fe2c`](#insn-00b3fe2c)
- ブロック [`00b3fe2c`](#insn-00b3fe2c) 範囲 `[['00b3fe2c', '00b3fe3b']]`
  - `CONDITIONAL_JUMP` [`00b3fe38`](#insn-00b3fe38) → [`00b40324`](#insn-00b40324)
  - `FALL_THROUGH` [`00b3fe38`](#insn-00b3fe38) → [`00b3fe3c`](#insn-00b3fe3c)
- ブロック [`00b3fe3c`](#insn-00b3fe3c) 範囲 `[['00b3fe3c', '00b3fe3f']]`
  - `UNCONDITIONAL_JUMP` [`00b3fe3c`](#insn-00b3fe3c) → [`00b40320`](#insn-00b40320)
- ブロック [`00b3fe40`](#insn-00b3fe40) 範囲 `[['00b3fe40', '00b3fe7b']]`
  - `CONDITIONAL_JUMP` [`00b3fe78`](#insn-00b3fe78) → [`00b3fe84`](#insn-00b3fe84)
  - `FALL_THROUGH` [`00b3fe78`](#insn-00b3fe78) → [`00b3fe7c`](#insn-00b3fe7c)
- ブロック [`00b3fe7c`](#insn-00b3fe7c) 範囲 `[['00b3fe7c', '00b3fe83']]`
  - `FALL_THROUGH` [`00b3fe80`](#insn-00b3fe80) → [`00b3fe84`](#insn-00b3fe84)
- ブロック [`00b3fe84`](#insn-00b3fe84) 範囲 `[['00b3fe84', '00b3fe93']]`
  - `CONDITIONAL_JUMP` [`00b3fe90`](#insn-00b3fe90) → [`00b40324`](#insn-00b40324)
  - `FALL_THROUGH` [`00b3fe90`](#insn-00b3fe90) → [`00b3fe94`](#insn-00b3fe94)
- ブロック [`00b3fe94`](#insn-00b3fe94) 範囲 `[['00b3fe94', '00b3fe9f']]`
  - `UNCONDITIONAL_JUMP` [`00b3fe9c`](#insn-00b3fe9c) → [`00b40324`](#insn-00b40324)
- ブロック [`00b3fea0`](#insn-00b3fea0) 範囲 `[['00b3fea0', '00b3feab']]`
  - `CONDITIONAL_JUMP` [`00b3fea8`](#insn-00b3fea8) → [`00b40368`](#insn-00b40368)
  - `FALL_THROUGH` [`00b3fea8`](#insn-00b3fea8) → [`00b3feac`](#insn-00b3feac)
- ブロック [`00b3feac`](#insn-00b3feac) 範囲 `[['00b3feac', '00b3feb7']]`
  - `CONDITIONAL_JUMP` [`00b3feb4`](#insn-00b3feb4) → [`00b3fecc`](#insn-00b3fecc)
  - `FALL_THROUGH` [`00b3feb4`](#insn-00b3feb4) → [`00b3feb8`](#insn-00b3feb8)
- ブロック [`00b3feb8`](#insn-00b3feb8) 範囲 `[['00b3feb8', '00b3fec7']]`
  - `CONDITIONAL_JUMP` [`00b3fec4`](#insn-00b3fec4) → [`00b3ff04`](#insn-00b3ff04)
  - `FALL_THROUGH` [`00b3fec4`](#insn-00b3fec4) → [`00b3fec8`](#insn-00b3fec8)
- ブロック [`00b3fec8`](#insn-00b3fec8) 範囲 `[['00b3fec8', '00b3fecb']]`
  - `UNCONDITIONAL_JUMP` [`00b3fec8`](#insn-00b3fec8) → [`00b3ff14`](#insn-00b3ff14)
- ブロック [`00b3fecc`](#insn-00b3fecc) 範囲 `[['00b3fecc', '00b3ff03']]`
  - `FALL_THROUGH` [`00b3ff00`](#insn-00b3ff00) → [`00b3ff04`](#insn-00b3ff04)
- ブロック [`00b3ff04`](#insn-00b3ff04) 範囲 `[['00b3ff04', '00b3ff13']]`
  - `FALL_THROUGH` [`00b3ff10`](#insn-00b3ff10) → [`00b3ff14`](#insn-00b3ff14)
- ブロック [`00b3ff14`](#insn-00b3ff14) 範囲 `[['00b3ff14', '00b3ff1b']]`
  - `FALL_THROUGH` [`00b3ff18`](#insn-00b3ff18) → [`00b3ff1c`](#insn-00b3ff1c)
- ブロック [`00b3ff1c`](#insn-00b3ff1c) 範囲 `[['00b3ff1c', '00b3ff2b']]`
  - `CONDITIONAL_JUMP` [`00b3ff28`](#insn-00b3ff28) → [`00b40018`](#insn-00b40018)
  - `FALL_THROUGH` [`00b3ff28`](#insn-00b3ff28) → [`00b3ff2c`](#insn-00b3ff2c)
- ブロック [`00b3ff2c`](#insn-00b3ff2c) 範囲 `[['00b3ff2c', '00b3ffa7']]`
  - `CONDITIONAL_JUMP` [`00b3ffa4`](#insn-00b3ffa4) → [`00b400ec`](#insn-00b400ec)
  - `FALL_THROUGH` [`00b3ffa4`](#insn-00b3ffa4) → [`00b3ffa8`](#insn-00b3ffa8)
- ブロック [`00b3ffa8`](#insn-00b3ffa8) 範囲 `[['00b3ffa8', '00b3ffc7']]`
  - `CONDITIONAL_JUMP` [`00b3ffc4`](#insn-00b3ffc4) → [`00b3ffd0`](#insn-00b3ffd0)
  - `FALL_THROUGH` [`00b3ffc4`](#insn-00b3ffc4) → [`00b3ffc8`](#insn-00b3ffc8)
- ブロック [`00b3ffc8`](#insn-00b3ffc8) 範囲 `[['00b3ffc8', '00b3ffcf']]`
  - `FALL_THROUGH` [`00b3ffcc`](#insn-00b3ffcc) → [`00b3ffd0`](#insn-00b3ffd0)
- ブロック [`00b3ffd0`](#insn-00b3ffd0) 範囲 `[['00b3ffd0', '00b3fffb']]`
  - `CONDITIONAL_JUMP` [`00b3fff8`](#insn-00b3fff8) → [`00b40064`](#insn-00b40064)
  - `FALL_THROUGH` [`00b3fff8`](#insn-00b3fff8) → [`00b3fffc`](#insn-00b3fffc)
- ブロック [`00b3fffc`](#insn-00b3fffc) 範囲 `[['00b3fffc', '00b40017']]`
  - `UNCONDITIONAL_JUMP` [`00b40014`](#insn-00b40014) → [`00b40070`](#insn-00b40070)
- ブロック [`00b40018`](#insn-00b40018) 範囲 `[['00b40018', '00b4001f']]`
  - `CONDITIONAL_JUMP` [`00b4001c`](#insn-00b4001c) → [`00b40044`](#insn-00b40044)
  - `FALL_THROUGH` [`00b4001c`](#insn-00b4001c) → [`00b40020`](#insn-00b40020)
- ブロック [`00b40020`](#insn-00b40020) 範囲 `[['00b40020', '00b40043']]`
  - `UNCONDITIONAL_JUMP` [`00b40040`](#insn-00b40040) → [`00b4017c`](#insn-00b4017c)
- ブロック [`00b40044`](#insn-00b40044) 範囲 `[['00b40044', '00b4004f']]`
  - `CONDITIONAL_JUMP` [`00b4004c`](#insn-00b4004c) → [`00b40138`](#insn-00b40138)
  - `FALL_THROUGH` [`00b4004c`](#insn-00b4004c) → [`00b40050`](#insn-00b40050)
- ブロック [`00b40050`](#insn-00b40050) 範囲 `[['00b40050', '00b40063']]`
  - `UNCONDITIONAL_JUMP` [`00b40060`](#insn-00b40060) → [`00b4017c`](#insn-00b4017c)
- ブロック [`00b40064`](#insn-00b40064) 範囲 `[['00b40064', '00b4006f']]`
  - `CONDITIONAL_JUMP` [`00b4006c`](#insn-00b4006c) → [`00b40094`](#insn-00b40094)
  - `FALL_THROUGH` [`00b4006c`](#insn-00b4006c) → [`00b40070`](#insn-00b40070)
- ブロック [`00b40070`](#insn-00b40070) 範囲 `[['00b40070', '00b4007b']]`
  - `CONDITIONAL_JUMP` [`00b40078`](#insn-00b40078) → [`00b40094`](#insn-00b40094)
  - `FALL_THROUGH` [`00b40078`](#insn-00b40078) → [`00b4007c`](#insn-00b4007c)
- ブロック [`00b4007c`](#insn-00b4007c) 範囲 `[['00b4007c', '00b4007f']]`
  - `FALL_THROUGH` [`00b4007c`](#insn-00b4007c) → [`00b40080`](#insn-00b40080)
- ブロック [`00b40080`](#insn-00b40080) 範囲 `[['00b40080', '00b40093']]`
  - `CONDITIONAL_JUMP` [`00b40090`](#insn-00b40090) → [`00b40080`](#insn-00b40080)
  - `FALL_THROUGH` [`00b40090`](#insn-00b40090) → [`00b40094`](#insn-00b40094)
- ブロック [`00b40094`](#insn-00b40094) 範囲 `[['00b40094', '00b400af']]`
  - `CONDITIONAL_JUMP` [`00b400ac`](#insn-00b400ac) → [`00b400b8`](#insn-00b400b8)
  - `FALL_THROUGH` [`00b400ac`](#insn-00b400ac) → [`00b400b0`](#insn-00b400b0)
- ブロック [`00b400b0`](#insn-00b400b0) 範囲 `[['00b400b0', '00b400b7']]`
  - `UNCONDITIONAL_JUMP` [`00b400b4`](#insn-00b400b4) → [`00b400d8`](#insn-00b400d8)
- ブロック [`00b400b8`](#insn-00b400b8) 範囲 `[['00b400b8', '00b400cb']]`
  - `CONDITIONAL_JUMP` [`00b400c8`](#insn-00b400c8) → [`00b400d8`](#insn-00b400d8)
  - `FALL_THROUGH` [`00b400c8`](#insn-00b400c8) → [`00b400cc`](#insn-00b400cc)
- ブロック [`00b400cc`](#insn-00b400cc) 範囲 `[['00b400cc', '00b400d7']]`
  - `FALL_THROUGH` [`00b400d4`](#insn-00b400d4) → [`00b400d8`](#insn-00b400d8)
- ブロック [`00b400d8`](#insn-00b400d8) 範囲 `[['00b400d8', '00b400eb']]`
  - `FALL_THROUGH` [`00b400e8`](#insn-00b400e8) → [`00b400ec`](#insn-00b400ec)
- ブロック [`00b400ec`](#insn-00b400ec) 範囲 `[['00b400ec', '00b4010b']]`
  - `CONDITIONAL_JUMP` [`00b40108`](#insn-00b40108) → [`00b40114`](#insn-00b40114)
  - `FALL_THROUGH` [`00b40108`](#insn-00b40108) → [`00b4010c`](#insn-00b4010c)
- ブロック [`00b4010c`](#insn-00b4010c) 範囲 `[['00b4010c', '00b40113']]`
  - `FALL_THROUGH` [`00b40110`](#insn-00b40110) → [`00b40114`](#insn-00b40114)
- ブロック [`00b40114`](#insn-00b40114) 範囲 `[['00b40114', '00b4011b']]`
  - `CONDITIONAL_JUMP` [`00b40118`](#insn-00b40118) → [`00b40124`](#insn-00b40124)
  - `FALL_THROUGH` [`00b40118`](#insn-00b40118) → [`00b4011c`](#insn-00b4011c)
- ブロック [`00b4011c`](#insn-00b4011c) 範囲 `[['00b4011c', '00b40123']]`
  - `FALL_THROUGH` [`00b40120`](#insn-00b40120) → [`00b40124`](#insn-00b40124)
- ブロック [`00b40124`](#insn-00b40124) 範囲 `[['00b40124', '00b40127']]`
  - `CONDITIONAL_JUMP` [`00b40124`](#insn-00b40124) → [`00b40188`](#insn-00b40188)
  - `FALL_THROUGH` [`00b40124`](#insn-00b40124) → [`00b40128`](#insn-00b40128)
- ブロック [`00b40128`](#insn-00b40128) 範囲 `[['00b40128', '00b40133']]`
  - `CONDITIONAL_JUMP` [`00b40130`](#insn-00b40130) → [`00b40314`](#insn-00b40314)
  - `FALL_THROUGH` [`00b40130`](#insn-00b40130) → [`00b40134`](#insn-00b40134)
- ブロック [`00b40134`](#insn-00b40134) 範囲 `[['00b40134', '00b40137']]`
  - `UNCONDITIONAL_JUMP` [`00b40134`](#insn-00b40134) → [`00b4031c`](#insn-00b4031c)
- ブロック [`00b40138`](#insn-00b40138) 範囲 `[['00b40138', '00b4017b']]`
  - `FALL_THROUGH` [`00b40178`](#insn-00b40178) → [`00b4017c`](#insn-00b4017c)
- ブロック [`00b4017c`](#insn-00b4017c) 範囲 `[['00b4017c', '00b40187']]`
  - `CONDITIONAL_JUMP` [`00b40184`](#insn-00b40184) → [`00b4030c`](#insn-00b4030c)
  - `FALL_THROUGH` [`00b40184`](#insn-00b40184) → [`00b40188`](#insn-00b40188)
- ブロック [`00b40188`](#insn-00b40188) 範囲 `[['00b40188', '00b40193']]`
  - `CONDITIONAL_JUMP` [`00b40190`](#insn-00b40190) → [`00b401dc`](#insn-00b401dc)
  - `FALL_THROUGH` [`00b40190`](#insn-00b40190) → [`00b40194`](#insn-00b40194)
- ブロック [`00b40194`](#insn-00b40194) 範囲 `[['00b40194', '00b401ab']]`
  - `FALL_THROUGH` [`00b401a8`](#insn-00b401a8) → [`00b401ac`](#insn-00b401ac)
- ブロック [`00b401ac`](#insn-00b401ac) 範囲 `[['00b401ac', '00b401b7']]`
  - `CONDITIONAL_JUMP` [`00b401b4`](#insn-00b401b4) → [`00b4023c`](#insn-00b4023c)
  - `FALL_THROUGH` [`00b401b4`](#insn-00b401b4) → [`00b401b8`](#insn-00b401b8)
- ブロック [`00b401b8`](#insn-00b401b8) 範囲 `[['00b401b8', '00b401c7']]`
  - `CONDITIONAL_JUMP` [`00b401c4`](#insn-00b401c4) → [`00b401dc`](#insn-00b401dc)
  - `FALL_THROUGH` [`00b401c4`](#insn-00b401c4) → [`00b401c8`](#insn-00b401c8)
- ブロック [`00b401c8`](#insn-00b401c8) 範囲 `[['00b401c8', '00b401d7']]`
  - `CONDITIONAL_JUMP` [`00b401d4`](#insn-00b401d4) → [`00b401ac`](#insn-00b401ac)
  - `FALL_THROUGH` [`00b401d4`](#insn-00b401d4) → [`00b401d8`](#insn-00b401d8)
- ブロック [`00b401d8`](#insn-00b401d8) 範囲 `[['00b401d8', '00b401db']]`
  - `FALL_THROUGH` [`00b401d8`](#insn-00b401d8) → [`00b401dc`](#insn-00b401dc)
- ブロック [`00b401dc`](#insn-00b401dc) 範囲 `[['00b401dc', '00b401fb']]`
  - `CONDITIONAL_JUMP` [`00b401f8`](#insn-00b401f8) → [`00b40210`](#insn-00b40210)
  - `FALL_THROUGH` [`00b401f8`](#insn-00b401f8) → [`00b401fc`](#insn-00b401fc)
- ブロック [`00b401fc`](#insn-00b401fc) 範囲 `[['00b401fc', '00b4020f']]`
  - `UNCONDITIONAL_JUMP` [`00b4020c`](#insn-00b4020c) → [`00b402d0`](#insn-00b402d0)
- ブロック [`00b40210`](#insn-00b40210) 範囲 `[['00b40210', '00b4021b']]`
  - `CONDITIONAL_JUMP` [`00b40218`](#insn-00b40218) → [`00b40368`](#insn-00b40368)
  - `FALL_THROUGH` [`00b40218`](#insn-00b40218) → [`00b4021c`](#insn-00b4021c)
- ブロック [`00b4021c`](#insn-00b4021c) 範囲 `[['00b4021c', '00b40227']]`
  - `CONDITIONAL_JUMP` [`00b40224`](#insn-00b40224) → [`00b4029c`](#insn-00b4029c)
  - `FALL_THROUGH` [`00b40224`](#insn-00b40224) → [`00b40228`](#insn-00b40228)
- ブロック [`00b40228`](#insn-00b40228) 範囲 `[['00b40228', '00b40237']]`
  - `CONDITIONAL_JUMP` [`00b40234`](#insn-00b40234) → [`00b402bc`](#insn-00b402bc)
  - `FALL_THROUGH` [`00b40234`](#insn-00b40234) → [`00b40238`](#insn-00b40238)
- ブロック [`00b40238`](#insn-00b40238) 範囲 `[['00b40238', '00b4023b']]`
  - `UNCONDITIONAL_JUMP` [`00b40238`](#insn-00b40238) → [`00b402cc`](#insn-00b402cc)
- ブロック [`00b4023c`](#insn-00b4023c) 範囲 `[['00b4023c', '00b4024b']]`
  - `FALL_THROUGH` [`00b40248`](#insn-00b40248) → [`00b4024c`](#insn-00b4024c)
- ブロック [`00b4024c`](#insn-00b4024c) 範囲 `[['00b4024c', '00b40277']]`
  - `CONDITIONAL_JUMP` [`00b40274`](#insn-00b40274) → [`00b40280`](#insn-00b40280)
  - `FALL_THROUGH` [`00b40274`](#insn-00b40274) → [`00b40278`](#insn-00b40278)
- ブロック [`00b40278`](#insn-00b40278) 範囲 `[['00b40278', '00b4027f']]`
  - `FALL_THROUGH` [`00b4027c`](#insn-00b4027c) → [`00b40280`](#insn-00b40280)
- ブロック [`00b40280`](#insn-00b40280) 範囲 `[['00b40280', '00b4028f']]`
  - `CONDITIONAL_JUMP` [`00b4028c`](#insn-00b4028c) → [`00b40128`](#insn-00b40128)
  - `FALL_THROUGH` [`00b4028c`](#insn-00b4028c) → [`00b40290`](#insn-00b40290)
- ブロック [`00b40290`](#insn-00b40290) 範囲 `[['00b40290', '00b4029b']]`
  - `UNCONDITIONAL_JUMP` [`00b40298`](#insn-00b40298) → [`00b40128`](#insn-00b40128)
- ブロック [`00b4029c`](#insn-00b4029c) 範囲 `[['00b4029c', '00b402bb']]`
  - `FALL_THROUGH` [`00b402b8`](#insn-00b402b8) → [`00b402bc`](#insn-00b402bc)
- ブロック [`00b402bc`](#insn-00b402bc) 範囲 `[['00b402bc', '00b402cb']]`
  - `FALL_THROUGH` [`00b402c8`](#insn-00b402c8) → [`00b402cc`](#insn-00b402cc)
- ブロック [`00b402cc`](#insn-00b402cc) 範囲 `[['00b402cc', '00b402cf']]`
  - `FALL_THROUGH` [`00b402cc`](#insn-00b402cc) → [`00b402d0`](#insn-00b402d0)
- ブロック [`00b402d0`](#insn-00b402d0) 範囲 `[['00b402d0', '00b402f3']]`
  - `CONDITIONAL_JUMP` [`00b402f0`](#insn-00b402f0) → [`00b402fc`](#insn-00b402fc)
  - `FALL_THROUGH` [`00b402f0`](#insn-00b402f0) → [`00b402f4`](#insn-00b402f4)
- ブロック [`00b402f4`](#insn-00b402f4) 範囲 `[['00b402f4', '00b402fb']]`
  - `FALL_THROUGH` [`00b402f8`](#insn-00b402f8) → [`00b402fc`](#insn-00b402fc)
- ブロック [`00b402fc`](#insn-00b402fc) 範囲 `[['00b402fc', '00b4030b']]`
  - `FALL_THROUGH` [`00b40308`](#insn-00b40308) → [`00b4030c`](#insn-00b4030c)
- ブロック [`00b4030c`](#insn-00b4030c) 範囲 `[['00b4030c', '00b4030f']]`
  - `FALL_THROUGH` [`00b4030c`](#insn-00b4030c) → [`00b40310`](#insn-00b40310)
- ブロック [`00b40310`](#insn-00b40310) 範囲 `[['00b40310', '00b40313']]`
  - `CONDITIONAL_JUMP` [`00b40310`](#insn-00b40310) → [`00b4031c`](#insn-00b4031c)
  - `FALL_THROUGH` [`00b40310`](#insn-00b40310) → [`00b40314`](#insn-00b40314)
- ブロック [`00b40314`](#insn-00b40314) 範囲 `[['00b40314', '00b40317']]`
  - `FALL_THROUGH` [`00b40314`](#insn-00b40314) → [`00b40318`](#insn-00b40318)
- ブロック [`00b40318`](#insn-00b40318) 範囲 `[['00b40318', '00b4031b']]`
  - `FALL_THROUGH` [`00b40318`](#insn-00b40318) → [`00b4031c`](#insn-00b4031c)
- ブロック [`00b4031c`](#insn-00b4031c) 範囲 `[['00b4031c', '00b4031f']]`
  - `CONDITIONAL_JUMP` [`00b4031c`](#insn-00b4031c) → [`00b40324`](#insn-00b40324)
  - `FALL_THROUGH` [`00b4031c`](#insn-00b4031c) → [`00b40320`](#insn-00b40320)
- ブロック [`00b40320`](#insn-00b40320) 範囲 `[['00b40320', '00b40323']]`
  - `FALL_THROUGH` [`00b40320`](#insn-00b40320) → [`00b40324`](#insn-00b40324)
- ブロック [`00b40324`](#insn-00b40324) 範囲 `[['00b40324', '00b40333']]`
  - `CONDITIONAL_JUMP` [`00b40330`](#insn-00b40330) → [`00b40364`](#insn-00b40364)
  - `FALL_THROUGH` [`00b40330`](#insn-00b40330) → [`00b40334`](#insn-00b40334)
- ブロック [`00b40334`](#insn-00b40334) 範囲 `[['00b40334', '00b40343']]`
  - `FALL_THROUGH` [`00b40340`](#insn-00b40340) → [`00b40344`](#insn-00b40344)
- ブロック [`00b40344`](#insn-00b40344) 範囲 `[['00b40344', '00b40353']]`
- ブロック [`00b40354`](#insn-00b40354) 範囲 `[['00b40354', '00b40363']]`
  - `UNCONDITIONAL_JUMP` [`00b40360`](#insn-00b40360) → [`00b3fe2c`](#insn-00b3fe2c)
- ブロック [`00b40364`](#insn-00b40364) 範囲 `[['00b40364', '00b40367']]`
- ブロック [`00b40368`](#insn-00b40368) 範囲 `[['00b40368', '00b4036b']]`

## 命令位置別の参照

- [`00b3fcd0`](#insn-00b3fcd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fcd4`](#insn-00b3fcd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fcd8`](#insn-00b3fcd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fcdc`](#insn-00b3fcdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fce0`](#insn-00b3fce0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fce4`](#insn-00b3fce4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fd00`](#insn-00b3fd00) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fd24`](#insn-00b3fd24) → [`00b3fd48`](#insn-00b3fd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fd34`](#insn-00b3fd34) → `0029f097`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b3fd40`](#insn-00b3fd40) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3fd44`](#insn-00b3fd44) → [`00b3fe1c`](#insn-00b3fe1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fd50`](#insn-00b3fd50) → [`00bdfcc0`](../00bdf/00bdfcc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdfcc0` · 推定シンボル `None` · 推定型 `None`
- [`00b3fd5c`](#insn-00b3fd5c) → [`00b3fe04`](#insn-00b3fe04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fd64`](#insn-00b3fd64) → [`00b3fe04`](#insn-00b3fe04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fd70`](#insn-00b3fd70) → [`00b3fdc4`](#insn-00b3fdc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fd90`](#insn-00b3fd90) → [`00b3fdc4`](#insn-00b3fdc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fdb0`](#insn-00b3fdb0) → [`00b3fdc4`](#insn-00b3fdc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fdc0`](#insn-00b3fdc0) → [`00b40354`](#insn-00b40354) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fdd8`](#insn-00b3fdd8) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fddc`](#insn-00b3fddc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fde0`](#insn-00b3fde0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fdec`](#insn-00b3fdec) → [`00b3fea0`](#insn-00b3fea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fdf8`](#insn-00b3fdf8) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fdfc`](#insn-00b3fdfc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe00`](#insn-00b3fe00) → [`00b3ff1c`](#insn-00b3ff1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe08`](#insn-00b3fe08) → [`00b3fe40`](#insn-00b3fe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe14`](#insn-00b3fe14) → [`00bdf900`](../00bdf/00bdf900.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf900` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe18`](#insn-00b3fe18) → [`00b3fe2c`](#insn-00b3fe2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe28`](#insn-00b3fe28) → [`00bdf9b0`](../00bdf/00bdf9b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf9b0` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe38`](#insn-00b3fe38) → [`00b40324`](#insn-00b40324) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe3c`](#insn-00b3fe3c) → [`00b40320`](#insn-00b40320) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe44`](#insn-00b3fe44) → `002b069e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b3fe50`](#insn-00b3fe50) → [`00bdb260`](../00bdb/00bdb260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb260` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe58`](#insn-00b3fe58) → `00291545`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b3fe64`](#insn-00b3fe64) → [`00bdb260`](../00bdb/00bdb260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb260` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe70`](#insn-00b3fe70) → [`00bdf9d0`](../00bdf/00bdf9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf9d0` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe74`](#insn-00b3fe74) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe78`](#insn-00b3fe78) → [`00b3fe84`](#insn-00b3fe84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe7c`](#insn-00b3fe7c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe80`](#insn-00b3fe80) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe84`](#insn-00b3fe84) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe90`](#insn-00b3fe90) → [`00b40324`](#insn-00b40324) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe94`](#insn-00b3fe94) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe98`](#insn-00b3fe98) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b3fe9c`](#insn-00b3fe9c) → [`00b40324`](#insn-00b40324) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fea8`](#insn-00b3fea8) → [`00b40368`](#insn-00b40368) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3feb4`](#insn-00b3feb4) → [`00b3fecc`](#insn-00b3fecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fec0`](#insn-00b3fec0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fec4`](#insn-00b3fec4) → [`00b3ff04`](#insn-00b3ff04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fec8`](#insn-00b3fec8) → [`00b3ff14`](#insn-00b3ff14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fed0`](#insn-00b3fed0) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fee4`](#insn-00b3fee4) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00b3fef4`](#insn-00b3fef4) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fefc`](#insn-00b3fefc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff00`](#insn-00b3ff00) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff10`](#insn-00b3ff10) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff20`](#insn-00b3ff20) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff28`](#insn-00b3ff28) → [`00b40018`](#insn-00b40018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff30`](#insn-00b3ff30) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff44`](#insn-00b3ff44) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff48`](#insn-00b3ff48) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff4c`](#insn-00b3ff4c) → [`00bdb240`](../00bdb/00bdb240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb240` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff58`](#insn-00b3ff58) → `002b2b90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3ff60`](#insn-00b3ff60) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff60`](#insn-00b3ff60) → `Stack[-0xf8]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff68`](#insn-00b3ff68) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff68`](#insn-00b3ff68) → `Stack[-0xd8]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff78`](#insn-00b3ff78) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff7c`](#insn-00b3ff7c) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff80`](#insn-00b3ff80) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff84`](#insn-00b3ff84) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff88`](#insn-00b3ff88) → `Stack[-0x10c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff8c`](#insn-00b3ff8c) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff90`](#insn-00b3ff90) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ff94`](#insn-00b3ff94) → [`00bdf940`](../00bdf/00bdf940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf940` · 推定シンボル `None` · 推定型 `None`
- [`00b3ffa4`](#insn-00b3ffa4) → [`00b400ec`](#insn-00b400ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ffac`](#insn-00b3ffac) → [`00bdfb30`](../00bdf/00bdfb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdfb30` · 推定シンボル `None` · 推定型 `None`
- [`00b3ffb4`](#insn-00b3ffb4) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ffc4`](#insn-00b3ffc4) → [`00b3ffd0`](#insn-00b3ffd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fff8`](#insn-00b3fff8) → [`00b40064`](#insn-00b40064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40004`](#insn-00b40004) → [`00bdf390`](../00bdf/00bdf390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf390` · 推定シンボル `None` · 推定型 `None`
- [`00b40014`](#insn-00b40014) → [`00b40070`](#insn-00b40070) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4001c`](#insn-00b4001c) → [`00b40044`](#insn-00b40044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40038`](#insn-00b40038) → [`00bdf950`](../00bdf/00bdf950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf950` · 推定シンボル `None` · 推定型 `None`
- [`00b40040`](#insn-00b40040) → [`00b4017c`](#insn-00b4017c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4004c`](#insn-00b4004c) → [`00b40138`](#insn-00b40138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40058`](#insn-00b40058) → [`00bdf7f0`](../00bdf/00bdf7f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf7f0` · 推定シンボル `None` · 推定型 `None`
- [`00b40060`](#insn-00b40060) → [`00b4017c`](#insn-00b4017c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4006c`](#insn-00b4006c) → [`00b40094`](#insn-00b40094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40078`](#insn-00b40078) → [`00b40094`](#insn-00b40094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40090`](#insn-00b40090) → [`00b40080`](#insn-00b40080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4009c`](#insn-00b4009c) → [`00bdf4e0`](../00bdf/00bdf4e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf4e0` · 推定シンボル `None` · 推定型 `None`
- [`00b400a4`](#insn-00b400a4) → [`00bdf1b0`](../00bdf/00bdf1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b400a8`](#insn-00b400a8) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400ac`](#insn-00b400ac) → [`00b400b8`](#insn-00b400b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400b0`](#insn-00b400b0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400b4`](#insn-00b400b4) → [`00b400d8`](#insn-00b400d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400b8`](#insn-00b400b8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400c0`](#insn-00b400c0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400c4`](#insn-00b400c4) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400c8`](#insn-00b400c8) → [`00b400d8`](#insn-00b400d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400cc`](#insn-00b400cc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400d0`](#insn-00b400d0) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b400d4`](#insn-00b400d4) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400d8`](#insn-00b400d8) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400dc`](#insn-00b400dc) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400e4`](#insn-00b400e4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400e8`](#insn-00b400e8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400ec`](#insn-00b400ec) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b400f4`](#insn-00b400f4) → [`00bdec00`](../00bde/00bdec00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec00` · 推定シンボル `None` · 推定型 `None`
- [`00b400f8`](#insn-00b400f8) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40100`](#insn-00b40100) → [`00bdec10`](../00bde/00bdec10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec10` · 推定シンボル `None` · 推定型 `None`
- [`00b40104`](#insn-00b40104) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40108`](#insn-00b40108) → [`00b40114`](#insn-00b40114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4010c`](#insn-00b4010c) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40110`](#insn-00b40110) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b40114`](#insn-00b40114) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40118`](#insn-00b40118) → [`00b40124`](#insn-00b40124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4011c`](#insn-00b4011c) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40120`](#insn-00b40120) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b40124`](#insn-00b40124) → [`00b40188`](#insn-00b40188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4012c`](#insn-00b4012c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40130`](#insn-00b40130) → [`00b40314`](#insn-00b40314) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40134`](#insn-00b40134) → [`00b4031c`](#insn-00b4031c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40160`](#insn-00b40160) → [`00bdf800`](../00bdf/00bdf800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf800` · 推定シンボル `None` · 推定型 `None`
- [`00b40170`](#insn-00b40170) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40184`](#insn-00b40184) → [`00b4030c`](#insn-00b4030c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40190`](#insn-00b40190) → [`00b401dc`](#insn-00b401dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b401b4`](#insn-00b401b4) → [`00b4023c`](#insn-00b4023c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b401c4`](#insn-00b401c4) → [`00b401dc`](#insn-00b401dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b401d4`](#insn-00b401d4) → [`00b401ac`](#insn-00b401ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b401dc`](#insn-00b401dc) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b401e0`](#insn-00b401e0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b401ec`](#insn-00b401ec) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b401f0`](#insn-00b401f0) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b401f4`](#insn-00b401f4) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b401f8`](#insn-00b401f8) → [`00b40210`](#insn-00b40210) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b401fc`](#insn-00b401fc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40200`](#insn-00b40200) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40204`](#insn-00b40204) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40208`](#insn-00b40208) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4020c`](#insn-00b4020c) → [`00b402d0`](#insn-00b402d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40210`](#insn-00b40210) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40218`](#insn-00b40218) → [`00b40368`](#insn-00b40368) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4021c`](#insn-00b4021c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40224`](#insn-00b40224) → [`00b4029c`](#insn-00b4029c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40230`](#insn-00b40230) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40234`](#insn-00b40234) → [`00b402bc`](#insn-00b402bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40238`](#insn-00b40238) → [`00b402cc`](#insn-00b402cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40240`](#insn-00b40240) → `002af542`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4024c`](#insn-00b4024c) → [`00bdb260`](../00bdb/00bdb260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb260` · 推定シンボル `None` · 推定型 `None`
- [`00b40254`](#insn-00b40254) → `00291545`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b40260`](#insn-00b40260) → [`00bdb260`](../00bdb/00bdb260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb260` · 推定シンボル `None` · 推定型 `None`
- [`00b4026c`](#insn-00b4026c) → [`00bdf9d0`](../00bdf/00bdf9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf9d0` · 推定シンボル `None` · 推定型 `None`
- [`00b40270`](#insn-00b40270) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40274`](#insn-00b40274) → [`00b40280`](#insn-00b40280) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40278`](#insn-00b40278) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4027c`](#insn-00b4027c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b40280`](#insn-00b40280) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4028c`](#insn-00b4028c) → [`00b40128`](#insn-00b40128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40290`](#insn-00b40290) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40294`](#insn-00b40294) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b40298`](#insn-00b40298) → [`00b40128`](#insn-00b40128) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b402a8`](#insn-00b402a8) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00b402b4`](#insn-00b402b4) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b402b8`](#insn-00b402b8) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b402c8`](#insn-00b402c8) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b402d0`](#insn-00b402d0) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b402e0`](#insn-00b402e0) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b402e4`](#insn-00b402e4) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b402e8`](#insn-00b402e8) → [`00be00b0`](../00be0/00be00b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be00b0` · 推定シンボル `None` · 推定型 `None`
- [`00b402ec`](#insn-00b402ec) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b402f0`](#insn-00b402f0) → [`00b402fc`](#insn-00b402fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b402f4`](#insn-00b402f4) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b402f8`](#insn-00b402f8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b4030c`](#insn-00b4030c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40310`](#insn-00b40310) → [`00b4031c`](#insn-00b4031c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40314`](#insn-00b40314) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40318`](#insn-00b40318) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b4031c`](#insn-00b4031c) → [`00b40324`](#insn-00b40324) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40328`](#insn-00b40328) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40330`](#insn-00b40330) → [`00b40364`](#insn-00b40364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40334`](#insn-00b40334) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40338`](#insn-00b40338) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4033c`](#insn-00b4033c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40340`](#insn-00b40340) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40344`](#insn-00b40344) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40348`](#insn-00b40348) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4035c`](#insn-00b4035c) → [`00bdf970`](../00bdf/00bdf970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf970` · 推定シンボル `None` · 推定型 `None`
- [`00b40360`](#insn-00b40360) → [`00b3fe2c`](#insn-00b3fe2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b40364`](#insn-00b40364) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b40368`](#insn-00b40368) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3fcd0`](#insn-00b3fcd0)

~~~json
{
  "source": "00b3fcd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fcd4`](#insn-00b3fcd4)

~~~json
{
  "source": "00b3fcd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fcd8`](#insn-00b3fcd8)

~~~json
{
  "source": "00b3fcd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fcdc`](#insn-00b3fcdc)

~~~json
{
  "source": "00b3fcdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fce0`](#insn-00b3fce0)

~~~json
{
  "source": "00b3fce0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fce4`](#insn-00b3fce4)

~~~json
{
  "source": "00b3fce4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fd00`](#insn-00b3fd00)

~~~json
{
  "source": "00b3fd00",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fd24`](#insn-00b3fd24)

~~~json
{
  "source": "00b3fd24",
  "target": "00b3fd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fd34`](#insn-00b3fd34)

~~~json
{
  "source": "00b3fd34",
  "target": "0029f097",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f097",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "24736368656d6100",
  "capture_start": "0029f097",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b3fd40`](#insn-00b3fd40)

~~~json
{
  "source": "00b3fd40",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fd44`](#insn-00b3fd44)

~~~json
{
  "source": "00b3fd44",
  "target": "00b3fe1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fd50`](#insn-00b3fd50)

~~~json
{
  "source": "00b3fd50",
  "target": "00bdfcc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fd5c`](#insn-00b3fd5c)

~~~json
{
  "source": "00b3fd5c",
  "target": "00b3fe04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fd64`](#insn-00b3fd64)

~~~json
{
  "source": "00b3fd64",
  "target": "00b3fe04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fd70`](#insn-00b3fd70)

~~~json
{
  "source": "00b3fd70",
  "target": "00b3fdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fd90`](#insn-00b3fd90)

~~~json
{
  "source": "00b3fd90",
  "target": "00b3fdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fdb0`](#insn-00b3fdb0)

~~~json
{
  "source": "00b3fdb0",
  "target": "00b3fdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fdc0`](#insn-00b3fdc0)

~~~json
{
  "source": "00b3fdc0",
  "target": "00b40354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fdd8`](#insn-00b3fdd8)

~~~json
{
  "source": "00b3fdd8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fddc`](#insn-00b3fddc)

~~~json
{
  "source": "00b3fddc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fde0`](#insn-00b3fde0)

~~~json
{
  "source": "00b3fde0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fdec`](#insn-00b3fdec)

~~~json
{
  "source": "00b3fdec",
  "target": "00b3fea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fdf8`](#insn-00b3fdf8)

~~~json
{
  "source": "00b3fdf8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fdfc`](#insn-00b3fdfc)

~~~json
{
  "source": "00b3fdfc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe00`](#insn-00b3fe00)

~~~json
{
  "source": "00b3fe00",
  "target": "00b3ff1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe08`](#insn-00b3fe08)

~~~json
{
  "source": "00b3fe08",
  "target": "00b3fe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe14`](#insn-00b3fe14)

~~~json
{
  "source": "00b3fe14",
  "target": "00bdf900",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fe18`](#insn-00b3fe18)

~~~json
{
  "source": "00b3fe18",
  "target": "00b3fe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe28`](#insn-00b3fe28)

~~~json
{
  "source": "00b3fe28",
  "target": "00bdf9b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fe38`](#insn-00b3fe38)

~~~json
{
  "source": "00b3fe38",
  "target": "00b40324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe3c`](#insn-00b3fe3c)

~~~json
{
  "source": "00b3fe3c",
  "target": "00b40320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe44`](#insn-00b3fe44)

~~~json
{
  "source": "00b3fe44",
  "target": "002b069e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b069e",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "756e6b6e6f776e206669656c643a2000",
  "capture_start": "002b069e",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b3fe50`](#insn-00b3fe50)

~~~json
{
  "source": "00b3fe50",
  "target": "00bdb260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fe58`](#insn-00b3fe58)

~~~json
{
  "source": "00b3fe58",
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
- 参照命令 [`00b3fe64`](#insn-00b3fe64)

~~~json
{
  "source": "00b3fe64",
  "target": "00bdb260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fe70`](#insn-00b3fe70)

~~~json
{
  "source": "00b3fe70",
  "target": "00bdf9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fe74`](#insn-00b3fe74)

~~~json
{
  "source": "00b3fe74",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe78`](#insn-00b3fe78)

~~~json
{
  "source": "00b3fe78",
  "target": "00b3fe84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe7c`](#insn-00b3fe7c)

~~~json
{
  "source": "00b3fe7c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe80`](#insn-00b3fe80)

~~~json
{
  "source": "00b3fe80",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fe84`](#insn-00b3fe84)

~~~json
{
  "source": "00b3fe84",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe90`](#insn-00b3fe90)

~~~json
{
  "source": "00b3fe90",
  "target": "00b40324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe94`](#insn-00b3fe94)

~~~json
{
  "source": "00b3fe94",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fe98`](#insn-00b3fe98)

~~~json
{
  "source": "00b3fe98",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fe9c`](#insn-00b3fe9c)

~~~json
{
  "source": "00b3fe9c",
  "target": "00b40324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fea8`](#insn-00b3fea8)

~~~json
{
  "source": "00b3fea8",
  "target": "00b40368",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3feb4`](#insn-00b3feb4)

~~~json
{
  "source": "00b3feb4",
  "target": "00b3fecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fec0`](#insn-00b3fec0)

~~~json
{
  "source": "00b3fec0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fec4`](#insn-00b3fec4)

~~~json
{
  "source": "00b3fec4",
  "target": "00b3ff04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fec8`](#insn-00b3fec8)

~~~json
{
  "source": "00b3fec8",
  "target": "00b3ff14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fed0`](#insn-00b3fed0)

~~~json
{
  "source": "00b3fed0",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fee4`](#insn-00b3fee4)

~~~json
{
  "source": "00b3fee4",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fef4`](#insn-00b3fef4)

~~~json
{
  "source": "00b3fef4",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fefc`](#insn-00b3fefc)

~~~json
{
  "source": "00b3fefc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff00`](#insn-00b3ff00)

~~~json
{
  "source": "00b3ff00",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff10`](#insn-00b3ff10)

~~~json
{
  "source": "00b3ff10",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ff20`](#insn-00b3ff20)

~~~json
{
  "source": "00b3ff20",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff28`](#insn-00b3ff28)

~~~json
{
  "source": "00b3ff28",
  "target": "00b40018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff30`](#insn-00b3ff30)

~~~json
{
  "source": "00b3ff30",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ff44`](#insn-00b3ff44)

~~~json
{
  "source": "00b3ff44",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff48`](#insn-00b3ff48)

~~~json
{
  "source": "00b3ff48",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff4c`](#insn-00b3ff4c)

~~~json
{
  "source": "00b3ff4c",
  "target": "00bdb240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ff58`](#insn-00b3ff58)

~~~json
{
  "source": "00b3ff58",
  "target": "002b2b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2b90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0700000000000000",
  "capture_start": "002b2b90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b3ff60`](#insn-00b3ff60)

~~~json
{
  "source": "00b3ff60",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff60`](#insn-00b3ff60)

~~~json
{
  "source": "00b3ff60",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff68`](#insn-00b3ff68)

~~~json
{
  "source": "00b3ff68",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff68`](#insn-00b3ff68)

~~~json
{
  "source": "00b3ff68",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff78`](#insn-00b3ff78)

~~~json
{
  "source": "00b3ff78",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff7c`](#insn-00b3ff7c)

~~~json
{
  "source": "00b3ff7c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff80`](#insn-00b3ff80)

~~~json
{
  "source": "00b3ff80",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff84`](#insn-00b3ff84)

~~~json
{
  "source": "00b3ff84",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff88`](#insn-00b3ff88)

~~~json
{
  "source": "00b3ff88",
  "target": "Stack[-0x10c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff8c`](#insn-00b3ff8c)

~~~json
{
  "source": "00b3ff8c",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff90`](#insn-00b3ff90)

~~~json
{
  "source": "00b3ff90",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ff94`](#insn-00b3ff94)

~~~json
{
  "source": "00b3ff94",
  "target": "00bdf940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ffa4`](#insn-00b3ffa4)

~~~json
{
  "source": "00b3ffa4",
  "target": "00b400ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ffac`](#insn-00b3ffac)

~~~json
{
  "source": "00b3ffac",
  "target": "00bdfb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ffb4`](#insn-00b3ffb4)

~~~json
{
  "source": "00b3ffb4",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ffc4`](#insn-00b3ffc4)

~~~json
{
  "source": "00b3ffc4",
  "target": "00b3ffd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fff8`](#insn-00b3fff8)

~~~json
{
  "source": "00b3fff8",
  "target": "00b40064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40004`](#insn-00b40004)

~~~json
{
  "source": "00b40004",
  "target": "00bdf390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40014`](#insn-00b40014)

~~~json
{
  "source": "00b40014",
  "target": "00b40070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4001c`](#insn-00b4001c)

~~~json
{
  "source": "00b4001c",
  "target": "00b40044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40038`](#insn-00b40038)

~~~json
{
  "source": "00b40038",
  "target": "00bdf950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40040`](#insn-00b40040)

~~~json
{
  "source": "00b40040",
  "target": "00b4017c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4004c`](#insn-00b4004c)

~~~json
{
  "source": "00b4004c",
  "target": "00b40138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40058`](#insn-00b40058)

~~~json
{
  "source": "00b40058",
  "target": "00bdf7f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40060`](#insn-00b40060)

~~~json
{
  "source": "00b40060",
  "target": "00b4017c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4006c`](#insn-00b4006c)

~~~json
{
  "source": "00b4006c",
  "target": "00b40094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40078`](#insn-00b40078)

~~~json
{
  "source": "00b40078",
  "target": "00b40094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40090`](#insn-00b40090)

~~~json
{
  "source": "00b40090",
  "target": "00b40080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4009c`](#insn-00b4009c)

~~~json
{
  "source": "00b4009c",
  "target": "00bdf4e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b400a4`](#insn-00b400a4)

~~~json
{
  "source": "00b400a4",
  "target": "00bdf1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b400a8`](#insn-00b400a8)

~~~json
{
  "source": "00b400a8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400ac`](#insn-00b400ac)

~~~json
{
  "source": "00b400ac",
  "target": "00b400b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400b0`](#insn-00b400b0)

~~~json
{
  "source": "00b400b0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400b4`](#insn-00b400b4)

~~~json
{
  "source": "00b400b4",
  "target": "00b400d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400b8`](#insn-00b400b8)

~~~json
{
  "source": "00b400b8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400c0`](#insn-00b400c0)

~~~json
{
  "source": "00b400c0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400c4`](#insn-00b400c4)

~~~json
{
  "source": "00b400c4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400c8`](#insn-00b400c8)

~~~json
{
  "source": "00b400c8",
  "target": "00b400d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400cc`](#insn-00b400cc)

~~~json
{
  "source": "00b400cc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400d0`](#insn-00b400d0)

~~~json
{
  "source": "00b400d0",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b400d4`](#insn-00b400d4)

~~~json
{
  "source": "00b400d4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400d8`](#insn-00b400d8)

~~~json
{
  "source": "00b400d8",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400dc`](#insn-00b400dc)

~~~json
{
  "source": "00b400dc",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400e4`](#insn-00b400e4)

~~~json
{
  "source": "00b400e4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400e8`](#insn-00b400e8)

~~~json
{
  "source": "00b400e8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400ec`](#insn-00b400ec)

~~~json
{
  "source": "00b400ec",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b400f4`](#insn-00b400f4)

~~~json
{
  "source": "00b400f4",
  "target": "00bdec00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b400f8`](#insn-00b400f8)

~~~json
{
  "source": "00b400f8",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40100`](#insn-00b40100)

~~~json
{
  "source": "00b40100",
  "target": "00bdec10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40104`](#insn-00b40104)

~~~json
{
  "source": "00b40104",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40108`](#insn-00b40108)

~~~json
{
  "source": "00b40108",
  "target": "00b40114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4010c`](#insn-00b4010c)

~~~json
{
  "source": "00b4010c",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40110`](#insn-00b40110)

~~~json
{
  "source": "00b40110",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40114`](#insn-00b40114)

~~~json
{
  "source": "00b40114",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40118`](#insn-00b40118)

~~~json
{
  "source": "00b40118",
  "target": "00b40124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4011c`](#insn-00b4011c)

~~~json
{
  "source": "00b4011c",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40120`](#insn-00b40120)

~~~json
{
  "source": "00b40120",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40124`](#insn-00b40124)

~~~json
{
  "source": "00b40124",
  "target": "00b40188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4012c`](#insn-00b4012c)

~~~json
{
  "source": "00b4012c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40130`](#insn-00b40130)

~~~json
{
  "source": "00b40130",
  "target": "00b40314",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40134`](#insn-00b40134)

~~~json
{
  "source": "00b40134",
  "target": "00b4031c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40160`](#insn-00b40160)

~~~json
{
  "source": "00b40160",
  "target": "00bdf800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40170`](#insn-00b40170)

~~~json
{
  "source": "00b40170",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40184`](#insn-00b40184)

~~~json
{
  "source": "00b40184",
  "target": "00b4030c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40190`](#insn-00b40190)

~~~json
{
  "source": "00b40190",
  "target": "00b401dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b401b4`](#insn-00b401b4)

~~~json
{
  "source": "00b401b4",
  "target": "00b4023c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b401c4`](#insn-00b401c4)

~~~json
{
  "source": "00b401c4",
  "target": "00b401dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b401d4`](#insn-00b401d4)

~~~json
{
  "source": "00b401d4",
  "target": "00b401ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b401dc`](#insn-00b401dc)

~~~json
{
  "source": "00b401dc",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b401e0`](#insn-00b401e0)

~~~json
{
  "source": "00b401e0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b401ec`](#insn-00b401ec)

~~~json
{
  "source": "00b401ec",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b401f0`](#insn-00b401f0)

~~~json
{
  "source": "00b401f0",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b401f4`](#insn-00b401f4)

~~~json
{
  "source": "00b401f4",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b401f8`](#insn-00b401f8)

~~~json
{
  "source": "00b401f8",
  "target": "00b40210",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b401fc`](#insn-00b401fc)

~~~json
{
  "source": "00b401fc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40200`](#insn-00b40200)

~~~json
{
  "source": "00b40200",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40204`](#insn-00b40204)

~~~json
{
  "source": "00b40204",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40208`](#insn-00b40208)

~~~json
{
  "source": "00b40208",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4020c`](#insn-00b4020c)

~~~json
{
  "source": "00b4020c",
  "target": "00b402d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40210`](#insn-00b40210)

~~~json
{
  "source": "00b40210",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40218`](#insn-00b40218)

~~~json
{
  "source": "00b40218",
  "target": "00b40368",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4021c`](#insn-00b4021c)

~~~json
{
  "source": "00b4021c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40224`](#insn-00b40224)

~~~json
{
  "source": "00b40224",
  "target": "00b4029c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40230`](#insn-00b40230)

~~~json
{
  "source": "00b40230",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40234`](#insn-00b40234)

~~~json
{
  "source": "00b40234",
  "target": "00b402bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40238`](#insn-00b40238)

~~~json
{
  "source": "00b40238",
  "target": "00b402cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40240`](#insn-00b40240)

~~~json
{
  "source": "00b40240",
  "target": "002af542",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af542",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "6669656c6420736574206d6f7265207468616e206f6e63653a2000",
  "capture_start": "002af542",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4024c`](#insn-00b4024c)

~~~json
{
  "source": "00b4024c",
  "target": "00bdb260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40254`](#insn-00b40254)

~~~json
{
  "source": "00b40254",
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
- 参照命令 [`00b40260`](#insn-00b40260)

~~~json
{
  "source": "00b40260",
  "target": "00bdb260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4026c`](#insn-00b4026c)

~~~json
{
  "source": "00b4026c",
  "target": "00bdf9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40270`](#insn-00b40270)

~~~json
{
  "source": "00b40270",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40274`](#insn-00b40274)

~~~json
{
  "source": "00b40274",
  "target": "00b40280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40278`](#insn-00b40278)

~~~json
{
  "source": "00b40278",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4027c`](#insn-00b4027c)

~~~json
{
  "source": "00b4027c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40280`](#insn-00b40280)

~~~json
{
  "source": "00b40280",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4028c`](#insn-00b4028c)

~~~json
{
  "source": "00b4028c",
  "target": "00b40128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40290`](#insn-00b40290)

~~~json
{
  "source": "00b40290",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40294`](#insn-00b40294)

~~~json
{
  "source": "00b40294",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40298`](#insn-00b40298)

~~~json
{
  "source": "00b40298",
  "target": "00b40128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b402a8`](#insn-00b402a8)

~~~json
{
  "source": "00b402a8",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b402b4`](#insn-00b402b4)

~~~json
{
  "source": "00b402b4",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b402b8`](#insn-00b402b8)

~~~json
{
  "source": "00b402b8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b402c8`](#insn-00b402c8)

~~~json
{
  "source": "00b402c8",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b402d0`](#insn-00b402d0)

~~~json
{
  "source": "00b402d0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b402e0`](#insn-00b402e0)

~~~json
{
  "source": "00b402e0",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b402e4`](#insn-00b402e4)

~~~json
{
  "source": "00b402e4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b402e8`](#insn-00b402e8)

~~~json
{
  "source": "00b402e8",
  "target": "00be00b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b402ec`](#insn-00b402ec)

~~~json
{
  "source": "00b402ec",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b402f0`](#insn-00b402f0)

~~~json
{
  "source": "00b402f0",
  "target": "00b402fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b402f4`](#insn-00b402f4)

~~~json
{
  "source": "00b402f4",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b402f8`](#insn-00b402f8)

~~~json
{
  "source": "00b402f8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4030c`](#insn-00b4030c)

~~~json
{
  "source": "00b4030c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40310`](#insn-00b40310)

~~~json
{
  "source": "00b40310",
  "target": "00b4031c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40314`](#insn-00b40314)

~~~json
{
  "source": "00b40314",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40318`](#insn-00b40318)

~~~json
{
  "source": "00b40318",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4031c`](#insn-00b4031c)

~~~json
{
  "source": "00b4031c",
  "target": "00b40324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40328`](#insn-00b40328)

~~~json
{
  "source": "00b40328",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40330`](#insn-00b40330)

~~~json
{
  "source": "00b40330",
  "target": "00b40364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40334`](#insn-00b40334)

~~~json
{
  "source": "00b40334",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40338`](#insn-00b40338)

~~~json
{
  "source": "00b40338",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4033c`](#insn-00b4033c)

~~~json
{
  "source": "00b4033c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40340`](#insn-00b40340)

~~~json
{
  "source": "00b40340",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40344`](#insn-00b40344)

~~~json
{
  "source": "00b40344",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40348`](#insn-00b40348)

~~~json
{
  "source": "00b40348",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4035c`](#insn-00b4035c)

~~~json
{
  "source": "00b4035c",
  "target": "00bdf970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40360`](#insn-00b40360)

~~~json
{
  "source": "00b40360",
  "target": "00b3fe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b40364`](#insn-00b40364)

~~~json
{
  "source": "00b40364",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b40368`](#insn-00b40368)

~~~json
{
  "source": "00b40368",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
