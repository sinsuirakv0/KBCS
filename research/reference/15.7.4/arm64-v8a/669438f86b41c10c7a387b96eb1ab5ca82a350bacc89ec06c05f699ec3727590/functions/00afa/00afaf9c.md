# 00afaf9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afaf58`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0008.md#compare-d0d7f894153241467ce7a4ba7c7ca043)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
