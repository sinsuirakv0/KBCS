# 00bfb1ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfb1ec",
  "name": "_ZNSt6__ndk15mutex8try_lockEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28c84b37fcdb121278cca28c03496ef0e38461d2bd1f4c6f61aca3bffb58de6a",
  "source_text_sha256": "28c84b37fcdb121278cca28c03496ef0e38461d2bd1f4c6f61aca3bffb58de6a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5f310](../00c5f/00c5f310.md)

## 疑似コード / UTF-8 147 bytes

~~~c

bool _ZNSt6__ndk15mutex8try_lockEv(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_trylock(param_1);
  return iVar1 == 0;
}

~~~
