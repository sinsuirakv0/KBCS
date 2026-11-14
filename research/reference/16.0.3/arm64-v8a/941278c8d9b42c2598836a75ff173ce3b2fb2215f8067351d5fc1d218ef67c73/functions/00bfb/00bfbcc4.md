# 00bfbcc4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfbcc4",
  "name": "_ZNSt6__ndk115__thread_struct25notify_all_at_thread_exitEPNS_18condition_variableEPNS_5mutexE",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e690eed842a357ae2f0cf6645072567bfc2b43b9d69a1dd92d713e6afa71d2b",
  "source_text_sha256": "5e690eed842a357ae2f0cf6645072567bfc2b43b9d69a1dd92d713e6afa71d2b"
}
~~~

## 呼び出し元

- [00c5f2a0](../00c5f/00c5f2a0.md)

## 呼び出し先

- [00bfba58](../00bfb/00bfba58.md)

## 疑似コード / UTF-8 179 bytes

~~~c

void _ZNSt6__ndk115__thread_struct25notify_all_at_thread_exitEPNS_18condition_variableEPNS_5mutexE
               (undefined8 *param_1)

{
  FUN_00bfba58(*param_1);
  return;
}

~~~
