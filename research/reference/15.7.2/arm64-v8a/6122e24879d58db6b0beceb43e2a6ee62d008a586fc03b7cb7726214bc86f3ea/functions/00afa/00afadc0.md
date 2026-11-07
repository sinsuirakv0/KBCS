# 00afadc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00afaecc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaecc.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00afadc0",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE5eraseENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc5033779428ff5df26e41a3413f792872432dbea8e6894f91a4400bced04436",
  "source_text_sha256": "bc5033779428ff5df26e41a3413f792872432dbea8e6894f91a4400bced04436"
}
~~~

## 呼び出し元

- [00bde8a0](../00bde/00bde8a0.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bddcd0](../00bdd/00bddcd0.md)
- [00bde1e0](../00bde/00bde1e0.md)
- [00bde650](../00bde/00bde650.md)

## 疑似コード / UTF-8 1874 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE5eraseENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEE
                 (undefined8 *param_1,void *param_2)

{
  long *plVar1;
  long lVar2;
  long *plVar3;
  void *__ptr;
  
  plVar1 = *(long **)((long)param_2 + 8);
  if (*(long **)((long)param_2 + 8) == (long *)0x0) {
    plVar1 = (long *)((long)param_2 + 0x10);
    plVar3 = (long *)*plVar1;
    if ((void *)*plVar3 != param_2) {
      do {
                    /* try { // try from 00afae00 to 00bfae07 has its CatchHandler @ 00aff4fc */
        lVar2 = *plVar1;
        plVar1 = (long *)(lVar2 + 0x10);
        plVar3 = (long *)*plVar1;
      } while (*plVar3 != lVar2);
    }
  }
  else {
    do {
                    /* try { // try from 00afaddc to 00bfadef has its CatchHandler @ 00aff500 */
      plVar3 = plVar1;
      plVar1 = (long *)*plVar3;
    } while ((long *)*plVar3 != (long *)0x0);
  }
  if ((void *)*param_1 == param_2) {
    *param_1 = plVar3;
  }
                    /* try { // try from 00afae30 to 00bfae43 has its CatchHandler @ 00aff4f8 */
  param_1[2] = param_1[2] + -1;
  _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[1],param_2);
  __ptr = *(void **)((long)param_2 + 0x38);
  *(undefined8 *)((long)param_2 + 0x38) = 0;
  if (__ptr != (void *)0x0) {
    _ZN8firebase6LoggerD2Ev((long)__ptr + 0x68);
    _ZN8firebase15CleanupNotifierD2Ev((long)__ptr + 8);
    _ZdlPv(__ptr);
  }
                    /* try { // try from 00afae64 to 00bfae6b has its CatchHandler @ 00aff4f4 */
  if ((*(byte *)((long)param_2 + 0x20) & 1) != 0) {
    _ZdlPv(*(void **)((long)param_2 + 0x30));
  }
  _ZdlPv(param_2);
  return plVar3;
}

~~~
