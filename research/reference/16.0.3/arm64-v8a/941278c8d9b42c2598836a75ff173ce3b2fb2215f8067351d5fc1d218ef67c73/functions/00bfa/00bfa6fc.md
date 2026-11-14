# 00bfa6fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfa6fc",
  "name": "_ZNSt6__ndk117__assoc_sub_state16__on_zero_sharedEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2428ea3abe0f3721ce74c28789b3230cee557b7c727a4f0f86178eb4746906b9",
  "source_text_sha256": "2428ea3abe0f3721ce74c28789b3230cee557b7c727a4f0f86178eb4746906b9"
}
~~~

## 呼び出し元

- [00c595e0](../00c59/00c595e0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 284 bytes

~~~c

void _ZNSt6__ndk117__assoc_sub_state16__on_zero_sharedEv(long *param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bfa708. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 8))();
  return;
}

~~~
