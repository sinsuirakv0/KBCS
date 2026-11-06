# 00bdffc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bdffc0",
  "name": "_ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b9906df238029384b81843c4cd3a7ef9647dd28492d09159c4b9f7367b18e705",
  "source_text_sha256": "b9906df238029384b81843c4cd3a7ef9647dd28492d09159c4b9f7367b18e705"
}
~~~

## 呼び出し元

- [00b1cedc](../00b1c/00b1cedc.md)

## 呼び出し先

- [00b2eb24](../00b2e/00b2eb24.md)

## 疑似コード / UTF-8 776 bytes

~~~c

void _ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA_
               (void)

{
                    /* try { // try from 00bdffcc to 00cdffe3 has its CatchHandler @ 00bdffcc
                       catch() { ... } // from try @ 00bdffcc with catch @ 00bdffcc
                       catch() { ... } // from try @ 00bdffec with catch @ 00bdffcc */
  (*(code *)
    PTR__ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA__00c1e818
  )();
  return;
}

~~~
