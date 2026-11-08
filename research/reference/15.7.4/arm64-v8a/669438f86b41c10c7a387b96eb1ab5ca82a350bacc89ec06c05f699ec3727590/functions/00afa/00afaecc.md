# 00afaecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00afaecc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE5eraseENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9eb6a43b2e56057b97ba9ef64898150f4281a04abc5bb3a74f5dde2faaa213b2",
  "source_text_sha256": "9eb6a43b2e56057b97ba9ef64898150f4281a04abc5bb3a74f5dde2faaa213b2"
}
~~~

## 呼び出し元

- [00bde9a0](../00bde/00bde9a0.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdddd0](../00bdd/00bdddd0.md)
- [00bde2e0](../00bde/00bde2e0.md)
- [00bde750](../00bde/00bde750.md)

## 疑似コード / UTF-8 1777 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE5eraseENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEE
                 (undefined8 *param_1,void *param_2)

{
  long *plVar1;
  long lVar2;
  long *plVar3;
  void *__ptr;
  
                    /* try { // try from 00afaed8 to 00bfaedf has its CatchHandler @ 00aff530 */
  plVar1 = *(long **)((long)param_2 + 8);
  if (*(long **)((long)param_2 + 8) == (long *)0x0) {
    plVar1 = (long *)((long)param_2 + 0x10);
    plVar3 = (long *)*plVar1;
                    /* try { // try from 00afaf08 to 00bfaf27 has its CatchHandler @ 00aff52c */
    if ((void *)*plVar3 != param_2) {
      do {
        lVar2 = *plVar1;
        plVar1 = (long *)(lVar2 + 0x10);
        plVar3 = (long *)*plVar1;
      } while (*plVar3 != lVar2);
    }
  }
  else {
    do {
      plVar3 = plVar1;
      plVar1 = (long *)*plVar3;
    } while ((long *)*plVar3 != (long *)0x0);
  }
                    /* try { // try from 00afaf28 to 00bfafaf has its CatchHandler @ 00af5650 */
  if ((void *)*param_1 == param_2) {
    *param_1 = plVar3;
  }
  param_1[2] = param_1[2] + -1;
  _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[1],param_2);
  __ptr = *(void **)((long)param_2 + 0x38);
  *(undefined8 *)((long)param_2 + 0x38) = 0;
  if (__ptr != (void *)0x0) {
    _ZN8firebase6LoggerD2Ev((long)__ptr + 0x68);
    _ZN8firebase15CleanupNotifierD2Ev((long)__ptr + 8);
    _ZdlPv(__ptr);
  }
  if ((*(byte *)((long)param_2 + 0x20) & 1) != 0) {
    _ZdlPv(*(void **)((long)param_2 + 0x30));
  }
  _ZdlPv(param_2);
  return plVar3;
}

~~~
