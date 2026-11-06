# 00b2eafc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00b2eafc.md)

## 関数情報

~~~json
{
  "address": "00b2eafc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE15__emplace_multiIJRKNS_4pairIKS7_SA_EEEEENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEEDpOT_",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb969f3f73bece37a74bd71567e41be6cbd4f3c6fb1f7ab0f52048107312dbaf",
  "source_text_sha256": "eb969f3f73bece37a74bd71567e41be6cbd4f3c6fb1f7ab0f52048107312dbaf"
}
~~~
## 呼び出し元

- [00bdff70](../00bdf/00bdff70.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb200](../00bdb/00bdb200.md)
- [00bde730](../00bde/00bde730.md)
- [00bde760](../00bde/00bde760.md)

## 疑似コード 1/1 / UTF-8 2738 bytes

~~~c

undefined8 *
_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE15__emplace_multiIJRKNS_4pairIKS7_SA_EEEEENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEEDpOT_
          (long *param_1,long param_2)

{
  void *__s1;
  ulong uVar1;
  size_t __n;
  byte bVar2;
  ulong uVar3;
  int iVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  long *plVar7;
  void *__s2;
  long *plVar8;
  long *plVar9;
  
                    /* try { // try from 00b2eb00 to 00c2eb0b has its CatchHandler @ 00b2f8ec */
                    /* try { // try from 00b2eb0c to 00c2eb33 has its CatchHandler @ 00b2f8e8 */
  puVar5 = (undefined8 *)_Znwm(0x40);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_(puVar5 + 4,param_2);
                    /* try { // try from 00b2eb34 to 00c2ec07 has its CatchHandler @ 00b2c3b0 */
  puVar5[7] = *(undefined8 *)(param_2 + 0x18);
  plVar7 = param_1 + 1;
  plVar8 = (long *)*plVar7;
  plVar9 = plVar7;
  if (plVar8 != (long *)0x0) {
    uVar3 = (ulong)(*(byte *)(puVar5 + 4) >> 1);
    __s1 = (void *)((long)puVar5 + 0x21);
    if ((*(byte *)(puVar5 + 4) & 1) != 0) {
      uVar3 = puVar5[5];
      __s1 = (void *)puVar5[6];
    }
    do {
      while( true ) {
        plVar9 = plVar8;
        bVar2 = *(byte *)(plVar9 + 4);
        uVar1 = (ulong)(bVar2 >> 1);
        if ((bVar2 & 1) != 0) {
          uVar1 = plVar9[5];
        }
        __n = uVar1;
        if (uVar3 <= uVar1) {
          __n = uVar3;
        }
        if (__n == 0) break;
        __s2 = (void *)plVar9[6];
        if ((bVar2 & 1) == 0) {
          __s2 = (void *)((long)plVar9 + 0x21);
        }
        iVar4 = memcmp(__s1,__s2,__n);
        if (iVar4 == 0) break;
        if (-1 < iVar4) goto LAB_00b2eb64;
LAB_00b2ebb0:
        plVar7 = plVar9;
        plVar8 = (long *)*plVar9;
        if ((long *)*plVar9 == (long *)0x0) goto LAB_00b2ebdc;
      }
      if (uVar3 < uVar1) goto LAB_00b2ebb0;
LAB_00b2eb64:
      plVar8 = (long *)plVar9[1];
    } while ((long *)plVar9[1] != (long *)0x0);
    plVar7 = plVar9 + 1;
  }
LAB_00b2ebdc:
  *puVar5 = 0;
  puVar5[1] = 0;
  puVar5[2] = plVar9;
  *plVar7 = (long)puVar5;
  puVar6 = puVar5;
  if (*(long *)*param_1 != 0) {
    *param_1 = *(long *)*param_1;
    puVar6 = (undefined8 *)*plVar7;
  }
                    /* try { // try from 00b2ec08 to 00c2ec13 has its CatchHandler @ 00b2f8e0 */
  _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[1],puVar6);
                    /* try { // try from 00b2ec14 to 00c2ec3b has its CatchHandler @ 00b2f8dc */
  param_1[2] = param_1[2] + 1;
  return puVar5;
}

~~~
