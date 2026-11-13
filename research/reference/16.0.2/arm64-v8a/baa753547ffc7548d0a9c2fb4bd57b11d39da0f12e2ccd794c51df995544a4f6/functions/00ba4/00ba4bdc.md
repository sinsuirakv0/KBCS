# 00ba4bdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00ba4bdc",
  "name": "_ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl",
  "size": 1228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b2326e1c30c2a46ab609e209b74a6bc1caa3be273311aec186d2dbae627b4c8",
  "source_text_sha256": "7b2326e1c30c2a46ab609e209b74a6bc1caa3be273311aec186d2dbae627b4c8"
}
~~~

## 呼び出し元

- [00c5cbd0](../00c5c/00c5cbd0.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)
- [00c5cbd0](../00c5c/00c5cbd0.md)
- [00c5cc60](../00c5c/00c5cc60.md)
- [00c5cd00](../00c5c/00c5cd00.md)

## 疑似コード / UTF-8 11740 bytes

~~~c

void _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl
               (uint *param_1,uint *param_2,long *param_3,ulong param_4,uint *param_5,long param_6)

{
  long lVar1;
  uint *puVar2;
  uint *puVar3;
  uint *puVar4;
  uint *puVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  uint uVar8;
  uint uVar9;
  uint uVar10;
  uint uVar11;
  uint uVar12;
  bool bVar13;
  int iVar14;
  int *piVar15;
  ulong uVar16;
  uint *puVar17;
  uint *puVar18;
  int *piVar19;
  ulong uVar20;
  long lVar21;
  ulong uVar22;
  long lVar23;
  long lVar24;
  undefined8 uVar25;
  undefined8 uVar26;
  undefined8 uVar27;
  
  if (1 < param_4) {
    if (param_4 == 2) {
      uVar10 = param_2[-1];
      uVar8 = *param_1;
      lVar21 = *(long *)(*param_3 + 0x38) + *(long *)(*param_3 + 0x28);
      piVar19 = (int *)(lVar21 - (ulong)uVar10);
      piVar15 = (int *)(lVar21 - (ulong)uVar8);
      puVar18 = (uint *)((long)piVar19 + (ulong)*(ushort *)((long)piVar19 + (4 - (long)*piVar19)));
                    /* try { // try from 00ba4c54 to 00ca4c6f has its CatchHandler @ 00ba562c */
      puVar17 = (uint *)((long)piVar15 + (ulong)*(ushort *)((long)piVar15 + (4 - (long)*piVar15)));
      puVar18 = (uint *)((long)puVar18 + (ulong)*puVar18);
      puVar17 = (uint *)((long)puVar17 + (ulong)*puVar17);
      uVar11 = *puVar18;
      uVar12 = *puVar17;
      uVar9 = uVar12;
                    /* try { // try from 00ba4c74 to 00ca4c7f has its CatchHandler @ 00ba55d0 */
      if (uVar11 <= uVar12) {
        uVar9 = uVar11;
      }
      iVar14 = memcmp(puVar18 + 1,puVar17 + 1,(ulong)uVar9);
                    /* try { // try from 00ba4c80 to 00ca4c8b has its CatchHandler @ 00ba5578 */
      bVar13 = uVar11 < uVar12;
                    /* try { // try from 00ba4c8c to 00ca4cbf has its CatchHandler @ 00ba57c4 */
      if (iVar14 != 0) {
        bVar13 = iVar14 < 0;
      }
      if (bVar13) {
        *param_1 = uVar10;
        param_2[-1] = uVar8;
      }
    }
    else if ((long)param_4 < 0x81) {
      if ((param_1 != param_2) && (puVar18 = param_1 + 1, puVar18 != param_2)) {
                    /* try { // try from 00ba4cc4 to 00ca4ccf has its CatchHandler @ 00ba552c */
        lVar21 = 0;
        do {
          uVar9 = *puVar18;
          puVar17 = param_1;
          if (puVar18 != param_1) {
            lVar1 = *(long *)(*param_3 + 0x38) + *(long *)(*param_3 + 0x28);
            piVar15 = (int *)(lVar1 - (ulong)uVar9);
            lVar23 = lVar21;
            do {
              uVar12 = *(uint *)((long)param_1 + lVar23);
                    /* try { // try from 00ba4d20 to 00ca4d3f has its CatchHandler @ 00ba56ec */
              piVar19 = (int *)(lVar1 - (ulong)uVar12);
              puVar2 = (uint *)((long)piVar15 +
                               (ulong)*(ushort *)((long)piVar15 + (4 - (long)*piVar15)));
                    /* try { // try from 00ba4d40 to 00ca4d73 has its CatchHandler @ 00ba595c */
              puVar3 = (uint *)((long)piVar19 +
                               (ulong)*(ushort *)((long)piVar19 + (4 - (long)*piVar19)));
              puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
              uVar10 = *puVar2;
              puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
              uVar11 = *puVar3;
              uVar8 = uVar11;
              if (uVar10 <= uVar11) {
                uVar8 = uVar10;
              }
              iVar14 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar8);
              bVar13 = uVar10 < uVar11;
                    /* try { // try from 00ba4d78 to 00ca4d93 has its CatchHandler @ 00ba5628 */
              if (iVar14 != 0) {
                bVar13 = iVar14 < 0;
              }
              if (!bVar13) {
                    /* try { // try from 00ba4cd0 to 00ca4cdb has its CatchHandler @ 00ba54d8 */
                puVar17 = (uint *)((long)param_1 + lVar23 + 4);
                break;
              }
              lVar24 = lVar23 + -4;
              *(uint *)((long)param_1 + lVar23 + 4) = uVar12;
              lVar23 = lVar24;
            } while (lVar24 != -4);
          }
                    /* try { // try from 00ba4cdc to 00ca4cef has its CatchHandler @ 00ba5470 */
          puVar18 = puVar18 + 1;
          lVar21 = lVar21 + 4;
          *puVar17 = uVar9;
        } while (puVar18 != param_2);
      }
    }
    else {
      uVar22 = param_4 >> 1;
      puVar18 = param_1 + uVar22;
                    /* try { // try from 00ba4da4 to 00ca4daf has its CatchHandler @ 00ba5570 */
                    /* try { // try from 00ba4db0 to 00ca4de3 has its CatchHandler @ 00ba578c */
      if (param_6 < (long)param_4) {
        _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl
                  (param_1,puVar18,param_3,uVar22,param_5,param_6);
                    /* try { // try from 00ba4de8 to 00ca4df3 has its CatchHandler @ 00ba5528 */
        _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl
                  (puVar18,param_2,param_3,param_4 - uVar22,param_5,param_6);
                    /* try { // try from 00ba4df4 to 00ca4dff has its CatchHandler @ 00ba54c0 */
                    /* try { // try from 00ba4e00 to 00ca4e13 has its CatchHandler @ 00ba5460 */
        _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
                  (param_1,puVar18,param_2,param_3,uVar22,param_4 - uVar22,param_5,param_6);
        return;
      }
      _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeE
                (param_1,puVar18,param_3,uVar22,param_5);
                    /* try { // try from 00ba4e44 to 00ca4e63 has its CatchHandler @ 00ba56e8 */
      puVar2 = param_5 + uVar22;
      _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeE
                (puVar18,param_2,param_3,param_4 - uVar22,puVar2);
                    /* try { // try from 00ba4e64 to 00ca4e97 has its CatchHandler @ 00ba5958 */
      puVar3 = param_5 + param_4;
      puVar17 = puVar2;
      puVar18 = param_5;
      do {
        if (puVar17 == puVar3) {
          if (puVar18 == puVar2) {
            return;
          }
          uVar16 = (long)param_5 + (uVar22 * 4 - (long)puVar18) + -4;
          uVar22 = (uVar16 >> 2) + 1;
                    /* try { // try from 00ba4fc0 to 00ca4fcb has its CatchHandler @ 00ba5558 */
          if ((7 < uVar22) &&
             ((uVar16 = uVar16 & 0xfffffffffffffffc, (uint *)((long)puVar18 + uVar16 + 4) <= param_1
              || ((uint *)((long)param_1 + uVar16 + 4) <= puVar18)))) {
            uVar20 = uVar22 & 0x7ffffffffffffff8;
            lVar21 = 0;
            uVar16 = uVar20;
            do {
              puVar6 = (undefined8 *)((long)puVar18 + lVar21);
                    /* try { // try from 00ba5054 to 00ca5063 has its CatchHandler @ 00ba544c */
              uVar25 = *puVar6;
              uVar27 = puVar6[3];
              uVar26 = puVar6[2];
              puVar7 = (undefined8 *)((long)param_1 + lVar21);
              uVar16 = uVar16 - 8;
              lVar21 = lVar21 + 0x20;
                    /* try { // try from 00ba5064 to 00ca5077 has its CatchHandler @ 00ba5424 */
              puVar7[1] = puVar6[1];
              *puVar7 = uVar25;
              puVar7[3] = uVar27;
              puVar7[2] = uVar26;
            } while (uVar16 != 0);
            puVar18 = puVar18 + uVar20;
            param_1 = param_1 + (uVar22 & 0x3ffffffffffffff8);
            if (uVar22 == uVar20) {
              return;
            }
          }
          do {
            puVar17 = puVar18 + 1;
            *param_1 = *puVar18;
            puVar18 = puVar17;
            param_1 = param_1 + 1;
          } while (puVar2 != puVar17);
          return;
        }
                    /* try { // try from 00ba4e98 to 00ca4f9b has its CatchHandler @ 00ba3e94 */
        uVar8 = *puVar17;
        uVar10 = *puVar18;
        lVar21 = *(long *)(*param_3 + 0x38) + *(long *)(*param_3 + 0x28);
        piVar19 = (int *)(lVar21 - (ulong)uVar8);
        piVar15 = (int *)(lVar21 - (ulong)uVar10);
        puVar4 = (uint *)((long)piVar19 + (ulong)*(ushort *)((long)piVar19 + (4 - (long)*piVar19)));
        puVar5 = (uint *)((long)piVar15 + (ulong)*(ushort *)((long)piVar15 + (4 - (long)*piVar15)));
        puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4);
        puVar5 = (uint *)((long)puVar5 + (ulong)*puVar5);
        uVar11 = *puVar4;
        uVar12 = *puVar5;
        uVar9 = uVar12;
        if (uVar11 <= uVar12) {
          uVar9 = uVar11;
        }
        iVar14 = memcmp(puVar4 + 1,puVar5 + 1,(ulong)uVar9);
        bVar13 = uVar11 < uVar12;
        if (iVar14 != 0) {
          bVar13 = iVar14 < 0;
        }
        if (bVar13) {
          *param_1 = uVar8;
          puVar17 = puVar17 + 1;
        }
        else {
          puVar18 = puVar18 + 1;
          *param_1 = uVar10;
        }
        param_1 = param_1 + 1;
      } while (puVar18 != puVar2);
      if (puVar17 == puVar3) {
        return;
      }
      uVar16 = (long)param_5 + (param_4 * 4 - (long)puVar17) + -4;
      uVar22 = (uVar16 >> 2) + 1;
                    /* try { // try from 00ba4f9c to 00ca4fab has its CatchHandler @ 00ba5610 */
      if ((7 < uVar22) &&
         ((uVar16 = uVar16 & 0xfffffffffffffffc, (uint *)((long)puVar17 + uVar16 + 4) <= param_1 ||
          ((uint *)((long)param_1 + uVar16 + 4) <= puVar17)))) {
                    /* try { // try from 00ba4fec to 00ca4fff has its CatchHandler @ 00ba553c */
        uVar20 = uVar22 & 0x7ffffffffffffff8;
        lVar21 = 0;
                    /* try { // try from 00ba5000 to 00ca500f has its CatchHandler @ 00ba5538 */
        uVar16 = uVar20;
        do {
          puVar6 = (undefined8 *)((long)puVar17 + lVar21);
          uVar25 = *puVar6;
          uVar27 = puVar6[3];
          uVar26 = puVar6[2];
                    /* try { // try from 00ba5010 to 00ca5023 has its CatchHandler @ 00ba5514 */
          puVar7 = (undefined8 *)((long)param_1 + lVar21);
          uVar16 = uVar16 - 8;
          lVar21 = lVar21 + 0x20;
          puVar7[1] = puVar6[1];
          *puVar7 = uVar25;
          puVar7[3] = uVar27;
          puVar7[2] = uVar26;
        } while (uVar16 != 0);
                    /* try { // try from 00ba5024 to 00ca5033 has its CatchHandler @ 00ba54a8 */
        puVar17 = puVar17 + uVar20;
        param_1 = param_1 + (uVar22 & 0x3ffffffffffffff8);
        if (uVar22 == uVar20) {
          return;
        }
      }
      do {
        puVar18 = puVar17 + 1;
                    /* try { // try from 00ba4fac to 00ca4fbf has its CatchHandler @ 00ba55b0 */
        *param_1 = *puVar17;
        puVar17 = puVar18;
        param_1 = param_1 + 1;
      } while (puVar3 != puVar18);
    }
  }
                    /* try { // try from 00ba5088 to 00ca5093 has its CatchHandler @ 00ba540c */
                    /* try { // try from 00ba5094 to 00ca50d3 has its CatchHandler @ 00ba3e94 */
  return;
}

~~~
