# 00bfabf0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfabf0",
  "name": "_ZNSt6__ndk115__thread_structD1Ev",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1514a8542a25f4aa387c17e64e04c04f510f9eb235192d5b2ba74cc3dc3421e",
  "source_text_sha256": "e1514a8542a25f4aa387c17e64e04c04f510f9eb235192d5b2ba74cc3dc3421e"
}
~~~

## 呼び出し元

- [00c58150](../00c58/00c58150.md)

## 呼び出し先

- [00bfa8fc](../00bfa/00bfa8fc.md)
- [00c57eb0](../00c57/00c57eb0.md)

## 疑似コード / UTF-8 213 bytes

~~~c

void _ZNSt6__ndk115__thread_structD1Ev(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)*param_1;
  if (__ptr != (void *)0x0) {
    FUN_00bfa8fc(__ptr);
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
