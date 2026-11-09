# 00bcb9bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcb9bc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a16434114214babe0d0ae237d786a4716f90b2e7ea07bbe16fe7d6677f00195",
  "source_text_sha256": "7a16434114214babe0d0ae237d786a4716f90b2e7ea07bbe16fe7d6677f00195"
}
~~~

## 呼び出し元

- [00c5d6c0](../00c5d/00c5d6c0.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c5d6c0](../00c5d/00c5d6c0.md)

## 疑似コード / UTF-8 959 bytes

~~~c

void _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
               (undefined8 param_1,undefined8 *param_2)

{
  if (param_2 != (undefined8 *)0x0) {
                    /* try { // try from 00bcb9cc to 00ccb9d7 has its CatchHandler @ 00bcba30 */
                    /* try { // try from 00bcb9d8 to 00ccba57 has its CatchHandler @ 00bcb960 */
    _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
              (param_1,*param_2);
    _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
              (param_1,param_2[1]);
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~
