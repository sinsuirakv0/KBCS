# 00ba6dcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00ba6dcc",
  "name": "_ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeE",
  "size": 732,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a24903bdc1405163a1d78b3c10a4fd1dee92dfa296f13a7c8bc312bd1ee2d89b",
  "source_text_sha256": "a24903bdc1405163a1d78b3c10a4fd1dee92dfa296f13a7c8bc312bd1ee2d89b"
}
~~~

## 呼び出し元

- [00c5cd80](../00c5c/00c5cd80.md)

## 呼び出し先

- [00c57ee0](../00c57/00c57ee0.md)
- [00c58050](../00c58/00c58050.md)
- [00c5ccc0](../00c5c/00c5ccc0.md)

## 疑似コード / UTF-8 7968 bytes

~~~c

void _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeE
               (uint *param_1,uint *param_2,uint *param_3,long *param_4,long param_5,long param_6,
               uint *param_7)

{
  ulong uVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  long lVar7;
  bool bVar8;
  int iVar9;
  uint *puVar10;
  uint *puVar11;
  uint *puVar12;
  int *piVar13;
  uint *puVar14;
  long lVar15;
  int *piVar16;
  ulong uVar17;
  ulong uVar18;
  undefined8 uVar19;
  undefined8 uVar20;
  undefined8 uVar21;
  long local_70;
  long local_68;
  
                    /* try { // try from 00ba6dd4 to 00ca6def has its CatchHandler @ 00ba6f48 */
  lVar7 = tpidr_el0;
  local_68 = *(long *)(lVar7 + 0x28);
                    /* try { // try from 00ba6e08 to 00ca6e13 has its CatchHandler @ 00ba6ec4 */
                    /* try { // try from 00ba6e14 to 00ca6e1f has its CatchHandler @ 00ba6ec0 */
  if (param_5 <= param_6) {
    puVar11 = param_7;
    if (param_1 != param_2) {
      uVar17 = (long)param_2 + (-4 - (long)param_1);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6e5c with catch @ 00ba6fa0
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba7098 with catch @ 00ba6fa4
                        */
      uVar1 = (uVar17 >> 2) + 1;
      puVar10 = param_7;
      puVar14 = param_1;
      if ((7 < uVar1) &&
         ((lVar15 = (uVar17 & 0xfffffffffffffffc) + 4, (uint *)((long)param_1 + lVar15) <= param_7
          || ((uint *)((long)param_7 + lVar15) <= param_1)))) {
        uVar18 = uVar1 & 0x7ffffffffffffff8;
                    /* try { // try from 00ba6fe4 to 00ca6fef has its CatchHandler @ 00ba70d4 */
        puVar10 = param_7 + 4;
        puVar11 = param_7 + uVar18;
        puVar14 = param_1 + 4;
        uVar17 = uVar18;
        do {
          puVar12 = puVar14 + -2;
          uVar19 = *(undefined8 *)(puVar14 + -4);
          uVar21 = *(undefined8 *)(puVar14 + 2);
          uVar20 = *(undefined8 *)puVar14;
          uVar17 = uVar17 - 8;
          puVar14 = puVar14 + 8;
                    /* try { // try from 00ba7008 to 00ca7013 has its CatchHandler @ 00ba70d0 */
          *(undefined8 *)(puVar10 + -2) = *(undefined8 *)puVar12;
          *(undefined8 *)(puVar10 + -4) = uVar19;
          *(undefined8 *)(puVar10 + 2) = uVar21;
          *(undefined8 *)puVar10 = uVar20;
          puVar10 = puVar10 + 8;
        } while (uVar17 != 0);
        puVar10 = puVar11;
        puVar14 = param_1 + uVar18;
        if (uVar1 == uVar18) goto LAB_00ba702c;
      }
      do {
        puVar12 = puVar14 + 1;
        puVar11 = puVar10 + 1;
        *puVar10 = *puVar14;
        puVar10 = puVar11;
        puVar14 = puVar12;
      } while (param_2 != puVar12);
    }
LAB_00ba702c:
                    /* try { // try from 00ba7030 to 00ca703b has its CatchHandler @ 00ba70c0 */
    local_70 = *param_4;
    _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_EESA_SA_EEvT0_SB_T1_SC_T2_T_
              (param_7,puVar11,param_2,param_3,param_1,&local_70);
    goto LAB_00ba704c;
  }
  if (param_2 == param_3) goto LAB_00ba704c;
                    /* try { // try from 00ba6e20 to 00ca6e2b has its CatchHandler @ 00ba6ebc */
  uVar17 = (long)param_3 + (-4 - (long)param_2);
  uVar1 = (uVar17 >> 2) + 1;
                    /* try { // try from 00ba6e3c to 00ca6e5b has its CatchHandler @ 00ba6f1c */
  puVar11 = param_2;
  puVar10 = param_7;
                    /* try { // try from 00ba6e5c to 00ca6e93 has its CatchHandler @ 00ba6fa0 */
  if ((uVar1 < 8) ||
     ((lVar15 = (uVar17 & 0xfffffffffffffffc) + 4, param_7 < (uint *)((long)param_2 + lVar15) &&
      (param_2 < (uint *)((long)param_7 + lVar15))))) {
LAB_00ba6ea4:
    do {
      puVar12 = puVar11 + 1;
      puVar14 = puVar10 + 1;
      *puVar10 = *puVar11;
      puVar11 = puVar12;
      puVar10 = puVar14;
    } while (param_3 != puVar12);
  }
  else {
    uVar18 = uVar1 & 0x7ffffffffffffff8;
    puVar11 = param_7 + 4;
    puVar10 = param_2 + 4;
    uVar17 = uVar18;
    do {
      puVar14 = puVar10 + -2;
      uVar19 = *(undefined8 *)(puVar10 + -4);
      uVar21 = *(undefined8 *)(puVar10 + 2);
      uVar20 = *(undefined8 *)puVar10;
      uVar17 = uVar17 - 8;
      puVar10 = puVar10 + 8;
      *(undefined8 *)(puVar11 + -2) = *(undefined8 *)puVar14;
      *(undefined8 *)(puVar11 + -4) = uVar19;
      *(undefined8 *)(puVar11 + 2) = uVar21;
      *(undefined8 *)puVar11 = uVar20;
                    /* try { // try from 00ba6e94 to 00ca6fa3 has its CatchHandler @ 00ba6cb8 */
      puVar11 = puVar11 + 8;
    } while (uVar17 != 0);
    puVar11 = param_2 + uVar18;
    puVar10 = param_7 + uVar18;
    puVar14 = param_7 + uVar18;
    if (uVar1 != uVar18) goto LAB_00ba6ea4;
  }
  while (puVar14 != param_7) {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6e08 with catch @ 00ba6ec4
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6e20 with catch @ 00ba6ebc
                        */
    param_3 = param_3 + -1;
    if (param_2 == param_1) {
      lVar15 = 0;
      do {
        *(undefined4 *)((long)param_3 + lVar15) = *(undefined4 *)((long)puVar14 + lVar15 + -4);
        lVar15 = lVar15 + -4;
                    /* try { // try from 00ba7098 to 00ca711b has its CatchHandler @ 00ba6fa4 */
      } while ((long)param_7 - (long)puVar14 != lVar15);
      break;
    }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6d74 with catch @ 00ba6ef0
                        */
    uVar3 = param_2[-1];
    uVar4 = puVar14[-1];
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6d50 with catch @ 00ba6f00
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6d24 with catch @ 00ba6f08
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6d00 with catch @ 00ba6f0c
                        */
    lVar15 = *(long *)(*param_4 + 0x38) + *(long *)(*param_4 + 0x28);
    piVar16 = (int *)(lVar15 - (ulong)uVar4);
    piVar13 = (int *)(lVar15 - (ulong)uVar3);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6e3c with catch @ 00ba6f1c
                        */
    puVar11 = (uint *)((long)piVar16 + (ulong)*(ushort *)((long)piVar16 + (4 - (long)*piVar16)));
    puVar10 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
    puVar11 = (uint *)((long)puVar11 + (ulong)*puVar11);
    puVar10 = (uint *)((long)puVar10 + (ulong)*puVar10);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6dd4 with catch @ 00ba6f48
                        */
    uVar5 = *puVar11;
    uVar6 = *puVar10;
    uVar2 = uVar6;
    if (uVar5 <= uVar6) {
      uVar2 = uVar5;
    }
    iVar9 = memcmp(puVar11 + 1,puVar10 + 1,(ulong)uVar2);
    bVar8 = uVar5 < uVar6;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6d38 with catch @ 00ba6f68
                        */
    if (iVar9 != 0) {
      bVar8 = iVar9 < 0;
    }
    if (bVar8) {
      *param_3 = uVar3;
      param_2 = param_2 + -1;
    }
    else {
      *param_3 = uVar4;
      puVar14 = puVar14 + -1;
    }
  }
LAB_00ba704c:
                    /* try { // try from 00ba7050 to 00ca705b has its CatchHandler @ 00ba70bc */
                    /* try { // try from 00ba705c to 00ca707b has its CatchHandler @ 00ba70e8 */
  if (*(long *)(lVar7 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 00ba707c to 00ca7097 has its CatchHandler @ 00ba70e4 */
  return;
}

~~~
