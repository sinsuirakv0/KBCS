# 00afaf9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00afaf9c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISF_PvEE",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "580519bd9d2f6d49930136fd939123f0c5abddd15bc844ce3cd616787037cbb6",
  "source_text_sha256": "580519bd9d2f6d49930136fd939123f0c5abddd15bc844ce3cd616787037cbb6"
}
~~~

## 呼び出し元

- [00bde9b0](../00bde/00bde9b0.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdddd0](../00bdd/00bdddd0.md)
- [00bde2e0](../00bde/00bde2e0.md)
- [00bde9b0](../00bde/00bde9b0.md)

## 疑似コード / UTF-8 1652 bytes

~~~c

void _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISF_PvEE
               (undefined8 param_1,undefined8 *param_2)

{
  void *__ptr;
  
  if (param_2 != (undefined8 *)0x0) {
                    /* try { // try from 00afafb0 to 00bfafc3 has its CatchHandler @ 00aff51c */
    _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISF_PvEE
              (param_1,*param_2);
                    /* try { // try from 00afafc4 to 00bfaff3 has its CatchHandler @ 00af5650 */
    _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISF_PvEE
              (param_1,param_2[1]);
    __ptr = (void *)param_2[7];
    param_2[7] = 0;
    if (__ptr != (void *)0x0) {
      _ZN8firebase6LoggerD2Ev((long)__ptr + 0x68);
      _ZN8firebase15CleanupNotifierD2Ev((long)__ptr + 8);
      _ZdlPv(__ptr);
    }
    if ((*(byte *)(param_2 + 4) & 1) != 0) {
                    /* try { // try from 00afaff4 to 00bfb017 has its CatchHandler @ 00b003c0 */
      _ZdlPv((void *)param_2[6]);
    }
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~
