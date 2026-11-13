# 00bfa1ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfa1ac",
  "name": "_ZNSt6__ndk15mutexD1Ev",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a2b9013c09a966ea36207ba466a9119a371d55235d5a815814c0461f2f827cd",
  "source_text_sha256": "3a2b9013c09a966ea36207ba466a9119a371d55235d5a815814c0461f2f827cd"
}
~~~

## 呼び出し元

- [00c57f30](../00c57/00c57f30.md)

## 呼び出し先

- [00c5b760](../00c5b/00c5b760.md)

## 疑似コード / UTF-8 134 bytes

~~~c

int _ZNSt6__ndk15mutexD1Ev(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_destroy(param_1);
  return iVar1;
}

~~~
