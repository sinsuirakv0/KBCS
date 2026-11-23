# 00b0cfcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b0cf88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cf88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0009.md#compare-62736d35255178387459280806d19c58)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0cfcc",
  "name": "_ZN11flatbuffers11SymbolTableINS_10ServiceDefEED2Ev",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c27ed1249d4d905fedae3fc2e41b63a7fd8b108184eeb399359b984c0490946f",
  "source_text_sha256": "c27ed1249d4d905fedae3fc2e41b63a7fd8b108184eeb399359b984c0490946f"
}
~~~

## 呼び出し元

- [00bdea20](../00bde/00bdea20.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bde9f0](../00bde/00bde9f0.md)
- [00bdeb80](../00bde/00bdeb80.md)
- [00bdebd0](../00bde/00bdebd0.md)

## 疑似コード / UTF-8 2549 bytes

~~~c

void _ZN11flatbuffers11SymbolTableINS_10ServiceDefEED2Ev(long param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 *__ptr;
  void *__ptr_00;
  void *__ptr_01;
  
                    /* try { // try from 00b0cfe0 to 00c0cfe7 has its CatchHandler @ 00b0cffc */
  __ptr = *(undefined8 **)(param_1 + 0x18);
  puVar1 = *(undefined8 **)(param_1 + 0x20);
                    /* catch() { ... } // from try @ 00b0cf70 with catch @ 00b0cfe8
                       try { // try from 00b0cfe8 to 00c0d02f has its CatchHandler @ 00b0ce38 */
                    /* catch() { ... } // from try @ 00b0cf1c with catch @ 00b0cfec */
  if (__ptr != puVar1) {
    do {
      __ptr_00 = (void *)*__ptr;
      if (__ptr_00 != (void *)0x0) {
        puVar1 = *(undefined8 **)((long)__ptr_00 + 0xb0);
        puVar2 = *(undefined8 **)((long)__ptr_00 + 0xb8);
        if (puVar1 != puVar2) {
          do {
            __ptr_01 = (void *)*puVar1;
            if (__ptr_01 != (void *)0x0) {
              _ZN11flatbuffers10DefinitionD2Ev(__ptr_01);
              _ZdlPv(__ptr_01);
              puVar2 = *(undefined8 **)((long)__ptr_00 + 0xb8);
            }
            puVar1 = puVar1 + 1;
          } while (puVar1 != puVar2);
          puVar1 = *(undefined8 **)((long)__ptr_00 + 0xb0);
        }
        if (puVar1 != (undefined8 *)0x0) {
          *(undefined8 **)((long)__ptr_00 + 0xb8) = puVar1;
          _ZdlPv(puVar1);
        }
        _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
                  ((long)__ptr_00 + 0x98,*(undefined8 *)((long)__ptr_00 + 0xa0));
        _ZN11flatbuffers10DefinitionD2Ev(__ptr_00);
        _ZdlPv(__ptr_00);
        puVar1 = *(undefined8 **)(param_1 + 0x20);
      }
      __ptr = __ptr + 1;
    } while (__ptr != puVar1);
    __ptr = *(undefined8 **)(param_1 + 0x18);
  }
  if (__ptr != (undefined8 *)0x0) {
    *(undefined8 **)(param_1 + 0x20) = __ptr;
                    /* catch() { ... } // from try @ 00b0cea4 with catch @ 00b0cffc
                       catch() { ... } // from try @ 00b0cfe0 with catch @ 00b0cffc */
    _ZdlPv(__ptr);
  }
  _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
            (param_1,*(undefined8 *)(param_1 + 8));
  return;
}

~~~
