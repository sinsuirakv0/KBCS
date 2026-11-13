# 00bfac8c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfac8c",
  "name": "_ZNSt6__ndk115__thread_structD1Ev",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b69f8706f940382549accd3f35211101e0da2bd0cf445941d90e5c26982fa114",
  "source_text_sha256": "b69f8706f940382549accd3f35211101e0da2bd0cf445941d90e5c26982fa114"
}
~~~

## 呼び出し元

- [00c58220](../00c58/00c58220.md)

## 呼び出し先

- [00bfa998](../00bfa/00bfa998.md)
- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 213 bytes

~~~c

void _ZNSt6__ndk115__thread_structD1Ev(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)*param_1;
  if (__ptr != (void *)0x0) {
    FUN_00bfa998(__ptr);
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
