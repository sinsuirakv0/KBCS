# 00bb6ebc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bb6ebc",
  "name": "_ZN8firebase9messaging16PollableListenerD0Ev",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b087bd9efc7b807144014561e42b1f86b10abb513c673ad91ab6d0ba26efc3a8",
  "source_text_sha256": "b087bd9efc7b807144014561e42b1f86b10abb513c673ad91ab6d0ba26efc3a8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5aac0](../00c5a/00c5aac0.md)
- [00c5d380](../00c5d/00c5d380.md)

## 疑似コード / UTF-8 397 bytes

~~~c

void _ZN8firebase9messaging16PollableListenerD0Ev(long *param_1)

{
  void *__ptr;
  
  __ptr = (void *)param_1[1];
  *param_1 = (long)(PTR__ZTVN8firebase9messaging16PollableListenerE_00c9b900 + 0x10);
  if (__ptr != (void *)0x0) {
    _ZN8firebase9messaging20PollableListenerImplD2Ev(__ptr);
    _ZdlPv(__ptr);
  }
  _ZN8firebase9messaging8ListenerD2Ev(param_1);
  _ZdlPv(param_1);
  return;
}

~~~
