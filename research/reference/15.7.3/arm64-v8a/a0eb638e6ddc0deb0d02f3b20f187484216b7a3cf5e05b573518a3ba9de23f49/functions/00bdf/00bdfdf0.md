# 00bdfdf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdfd40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0021.md#compare-626dfd975f80af16976fbc58e9093082)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfdf0",
  "name": "_ZNSt6__ndk127__insertion_sort_incompleteIRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEbT0_S9_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41eb036c171868abec7ffa930c270b2f19a1fa2caca81d93e7d33ba69203e5c3",
  "source_text_sha256": "41eb036c171868abec7ffa930c270b2f19a1fa2caca81d93e7d33ba69203e5c3"
}
~~~

## 呼び出し元

- [00b32634](../00b32/00b32634.md)

## 呼び出し先

- [00b3303c](../00b33/00b3303c.md)

## 疑似コード / UTF-8 428 bytes

~~~c

void _ZNSt6__ndk127__insertion_sort_incompleteIRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEbT0_S9_T_
               (void)

{
                    /* try { // try from 00bdfdf0 to 00cdfe77 has its CatchHandler @ 00bdff5c */
  (*(code *)
    PTR__ZNSt6__ndk127__insertion_sort_incompleteIRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEbT0_S9_T__00c1e788
  )();
  return;
}

~~~
