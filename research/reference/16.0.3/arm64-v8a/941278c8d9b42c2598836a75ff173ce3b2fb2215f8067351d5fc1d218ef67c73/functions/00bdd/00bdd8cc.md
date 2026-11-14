# 00bdd8cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdd8cc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emplace_hint_unique_key_argsIS3_JRKNS_4pairIKS3_S3_EEEEENS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEENS_21__tree_const_iteratorIS4_SM_lEERKT_DpOT0_",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "66c809bf6e807cb480335da329a5326261cfdb01fd794550322ebdb5251b7f30",
  "source_text_sha256": "66c809bf6e807cb480335da329a5326261cfdb01fd794550322ebdb5251b7f30"
}
~~~

## 呼び出し元

- [00c5ef10](../00c5e/00c5ef10.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5b990](../00c5b/00c5b990.md)
- [00c5c680](../00c5c/00c5c680.md)
- [00c5ef00](../00c5e/00c5ef00.md)

## 疑似コード / UTF-8 2185 bytes

~~~c

undefined8 *
_ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emplace_hint_unique_key_argsIS3_JRKNS_4pairIKS3_S3_EEEEENS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEENS_21__tree_const_iteratorIS4_SM_lEERKT_DpOT0_
          (long *param_1,undefined8 param_2,undefined8 param_3,long param_4)

{
  long lVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined1 auStack_58 [8];
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00bdd904 to 00cdd90f has its CatchHandler @ 00bdfd38 */
  puVar2 = (undefined8 *)
           _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__find_equalIS3_EERPNS_16__tree_node_baseIPvEENS_21__tree_const_iteratorIS4_PNS_11__tree_nodeIS4_SE_EElEERPNS_15__tree_end_nodeISG_EESH_RKT_
                     (param_1,param_2,&local_50,auStack_58,param_3);
  puVar4 = (undefined8 *)*puVar2;
  if (puVar4 == (undefined8 *)0x0) {
                    /* try { // try from 00bdd910 to 00cdd927 has its CatchHandler @ 00bdfd28 */
    puVar4 = (undefined8 *)_Znwm(0x50);
    *(undefined4 *)(puVar4 + 4) = 0;
                    /* try { // try from 00bdd928 to 00cdd98b has its CatchHandler @ 00bd7fb0 */
    _ZN8firebase7VariantaSERKS0_(puVar4 + 4,param_4);
    *(undefined4 *)(puVar4 + 7) = 0;
    _ZN8firebase7VariantaSERKS0_(puVar4 + 7,param_4 + 0x18);
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = local_50;
    *puVar2 = puVar4;
    puVar3 = puVar4;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar3 = (undefined8 *)*puVar2;
    }
    _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[1],puVar3)
    ;
    param_1[2] = param_1[2] + 1;
  }
                    /* try { // try from 00bdd98c to 00cdd9db has its CatchHandler @ 00bdfe54 */
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return puVar4;
}

~~~
