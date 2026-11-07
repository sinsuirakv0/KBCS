# 00bdffe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00be00e0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00e0.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00bdffe0",
  "name": "_ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS8_E9referenceEEE5valueENS_11__wrap_iterIPhEEE4typeENSC_IS6_EES8_S8_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20501929394b73fa82431a0ca36381b81e32a21ef26fa8fc4e2aeed34e384062",
  "source_text_sha256": "20501929394b73fa82431a0ca36381b81e32a21ef26fa8fc4e2aeed34e384062"
}
~~~

## 呼び出し元

- [00b261c4](../00b26/00b261c4.md)
- [00b3203c](../00b32/00b3203c.md)
- [00b331b0](../00b33/00b331b0.md)
- [00b33b54](../00b33/00b33b54.md)
- [00b44200](../00b44/00b44200.md)

## 呼び出し先

- [00b33600](../00b33/00b33600.md)

## 疑似コード / UTF-8 709 bytes

~~~c

void _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS8_E9referenceEEE5valueENS_11__wrap_iterIPhEEE4typeENSC_IS6_EES8_S8_
               (void)

{
                    /* try { // try from 00bdffe4 to 00cdffeb has its CatchHandler @ 00be0008 */
                    /* try { // try from 00bdffec to 00ce001b has its CatchHandler @ 00bdffcc */
  (*(code *)
    PTR__ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS8_E9referenceEEE5valueENS_11__wrap_iterIPhEEE4typeENSC_IS6_EES8_S8__00c1e828
  )();
  return;
}

~~~
