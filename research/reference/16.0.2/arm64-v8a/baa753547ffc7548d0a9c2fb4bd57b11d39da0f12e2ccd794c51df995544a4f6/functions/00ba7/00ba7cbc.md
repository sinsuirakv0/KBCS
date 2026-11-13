# 00ba7cbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00ba7cbc",
  "name": "_ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl",
  "size": 1064,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e30ef4e2cbfd5685746e0eba2e7b0459913034516d26dadc07462ba18cb9691b",
  "source_text_sha256": "e30ef4e2cbfd5685746e0eba2e7b0459913034516d26dadc07462ba18cb9691b"
}
~~~

## 呼び出し元

- [00c5cc50](../00c5c/00c5cc50.md)

## 呼び出し先

- [00ba86b0](../00ba8/00ba86b0.md)
- [00c58120](../00c58/00c58120.md)
- [00c5cc50](../00c5c/00c5cc50.md)
- [00c5ce10](../00c5c/00c5ce10.md)

## 疑似コード / UTF-8 7925 bytes

~~~c

void _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
               (uint *param_1,uint *param_2,uint *param_3,long *param_4,long param_5,long param_6,
               undefined8 param_7,long param_8)

{
  uint *puVar1;
  ulong uVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  bool bVar8;
  int iVar9;
  int *piVar10;
  long lVar11;
  uint *puVar12;
  uint *puVar13;
  long lVar14;
  ulong uVar15;
  long lVar16;
  ulong uVar17;
  long lVar18;
  uint *puVar19;
  uint *puVar20;
  
  while( true ) {
    if (param_6 == 0) {
                    /* try { // try from 00ba80c8 to 00ca80fb has its CatchHandler @ 00ba8250 */
      return;
    }
    if ((param_6 <= param_8) || (param_5 <= param_8)) break;
    if (param_5 == 0) {
      return;
    }
    lVar14 = 0;
    lVar16 = 0;
    uVar3 = *param_2;
    lVar18 = *(long *)(*param_4 + 0x38) + *(long *)(*param_4 + 0x28);
    piVar10 = (int *)(lVar18 - (ulong)uVar3);
    puVar19 = (uint *)((long)piVar10 + (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
    puVar19 = (uint *)((long)puVar19 + (ulong)*puVar19);
    uVar4 = *puVar19;
    while( true ) {
      uVar7 = param_1[lVar16];
      piVar10 = (int *)(lVar18 - (ulong)uVar7);
                    /* try { // try from 00ba7d6c to 00ca7d77 has its CatchHandler @ 00ba8324 */
      puVar13 = (uint *)((long)piVar10 + (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
      puVar13 = (uint *)((long)puVar13 + (ulong)*puVar13);
      uVar5 = *puVar13;
      uVar6 = uVar5;
      if (uVar4 <= uVar5) {
        uVar6 = uVar4;
      }
      iVar9 = memcmp(puVar19 + 1,puVar13 + 1,(ulong)uVar6);
      bVar8 = uVar4 < uVar5;
      if (iVar9 != 0) {
        bVar8 = iVar9 < 0;
      }
      if (bVar8) break;
      lVar16 = lVar16 + 1;
      lVar14 = lVar14 + -4;
      if (param_5 == lVar16) {
        return;
      }
    }
    lVar11 = param_5 - lVar16;
    puVar19 = (uint *)((long)param_1 - lVar14);
    if (lVar11 < param_6) {
                    /* try { // try from 00ba7dd8 to 00ca7ddf has its CatchHandler @ 00ba8328 */
      lVar14 = param_6;
                    /* try { // try from 00ba7de0 to 00ca7e4f has its CatchHandler @ 00ba7950 */
      if (param_6 < 0) {
        lVar14 = param_6 + 1;
      }
      lVar14 = lVar14 >> 1;
      puVar13 = param_2 + lVar14;
      puVar20 = puVar19;
      if ((long)param_2 - (long)puVar19 != 0) {
        uVar15 = (long)param_2 - (long)puVar19 >> 2;
        piVar10 = (int *)(lVar18 - (ulong)*puVar13);
        puVar1 = (uint *)((long)piVar10 + (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
        puVar1 = (uint *)((long)puVar1 + (ulong)*puVar1);
        uVar3 = *puVar1;
        do {
          uVar17 = uVar15 >> 1;
          piVar10 = (int *)(lVar18 - (ulong)puVar20[uVar17]);
          puVar12 = (uint *)((long)piVar10 +
                            (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
          puVar12 = (uint *)((long)puVar12 + (ulong)*puVar12);
                    /* try { // try from 00ba7e50 to 00ca7e63 has its CatchHandler @ 00ba818c */
          uVar6 = *puVar12;
          uVar4 = uVar6;
          if (uVar3 <= uVar6) {
            uVar4 = uVar3;
          }
          iVar9 = memcmp(puVar1 + 1,puVar12 + 1,(ulong)uVar4);
          bVar8 = uVar3 < uVar6;
          if (iVar9 != 0) {
            bVar8 = iVar9 < 0;
          }
          uVar2 = uVar15 + ~uVar17;
          uVar15 = uVar17;
          if (!bVar8) {
            puVar20 = puVar20 + uVar17 + 1;
            uVar15 = uVar2;
          }
        } while (uVar15 != 0);
      }
      lVar11 = (long)puVar20 - (long)puVar19 >> 2;
                    /* try { // try from 00ba7fac to 00ca7fb7 has its CatchHandler @ 00ba81f0 */
    }
    else {
      if (param_5 + -1 == lVar16) {
        param_1[lVar16] = uVar3;
        *param_2 = uVar7;
        return;
      }
      if (lVar11 < 0) {
        lVar11 = lVar11 + 1;
      }
      lVar11 = lVar11 >> 1;
      puVar20 = (uint *)((long)param_1 + (lVar11 * 4 - lVar14));
      puVar13 = param_2;
      if ((long)param_3 - (long)param_2 != 0) {
        uVar15 = (long)param_3 - (long)param_2 >> 2;
        piVar10 = (int *)(lVar18 - (ulong)param_1[lVar11 + lVar16]);
        puVar1 = (uint *)((long)piVar10 + (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
        puVar1 = (uint *)((long)puVar1 + (ulong)*puVar1);
        uVar3 = *puVar1;
                    /* try { // try from 00ba7f10 to 00ca7f23 has its CatchHandler @ 00ba8188 */
        puVar12 = param_2;
        do {
          uVar17 = uVar15 >> 1;
          piVar10 = (int *)(lVar18 - (ulong)puVar12[uVar17]);
          puVar13 = (uint *)((long)piVar10 +
                            (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
          puVar13 = (uint *)((long)puVar13 + (ulong)*puVar13);
          uVar6 = *puVar13;
          uVar4 = uVar3;
          if (uVar6 <= uVar3) {
            uVar4 = uVar6;
          }
          iVar9 = memcmp(puVar13 + 1,puVar1 + 1,(ulong)uVar4);
          bVar8 = uVar6 < uVar3;
          if (iVar9 != 0) {
            bVar8 = iVar9 < 0;
          }
          puVar13 = puVar12 + uVar17 + 1;
          uVar15 = uVar15 + ~uVar17;
                    /* try { // try from 00ba7f74 to 00ca7f7f has its CatchHandler @ 00ba8214 */
          if (!bVar8) {
            puVar13 = puVar12;
            uVar15 = uVar17;
          }
          puVar12 = puVar13;
        } while (uVar15 != 0);
      }
      lVar14 = (long)puVar13 - (long)param_2 >> 2;
    }
                    /* try { // try from 00ba7fcc to 00ca7fd7 has its CatchHandler @ 00ba81d8 */
    lVar18 = (param_5 - lVar11) - lVar16;
    param_1 = puVar13;
    if ((puVar20 != param_2) && (param_1 = puVar20, param_2 != puVar13)) {
                    /* try { // try from 00ba7ff8 to 00ca8003 has its CatchHandler @ 00ba81cc */
      param_1 = (uint *)FUN_00ba86b0(puVar20,param_2,puVar13);
    }
                    /* try { // try from 00ba801c to 00ca8027 has its CatchHandler @ 00ba81c8 */
    if (lVar14 + lVar11 < ((param_6 + param_5) - (lVar14 + lVar11)) - lVar16) {
                    /* try { // try from 00ba8030 to 00ca803b has its CatchHandler @ 00ba81c0 */
      _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
                (puVar19,puVar20,param_1,param_4,lVar11,lVar14,param_7,param_8);
      param_2 = puVar13;
      param_6 = param_6 - lVar14;
      param_5 = lVar18;
    }
    else {
                    /* try { // try from 00ba8050 to 00ca805b has its CatchHandler @ 00ba81ac */
                    /* try { // try from 00ba805c to 00ca8067 has its CatchHandler @ 00ba81a8 */
      _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
                (param_1,puVar13,param_3,param_4,lVar18,param_6 - lVar14,param_7,param_8);
                    /* try { // try from 00ba8068 to 00ca8073 has its CatchHandler @ 00ba81a4 */
      param_3 = param_1;
      param_2 = puVar20;
      param_6 = lVar14;
      param_5 = lVar11;
      param_1 = puVar19;
    }
  }
                    /* try { // try from 00ba8088 to 00ca80c3 has its CatchHandler @ 00ba8224 */
  _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeE
            (param_1,param_2,param_3,param_4,param_5,param_6,param_7);
  return;
}

~~~
