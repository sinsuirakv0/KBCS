# 00befba8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00befba8",
  "name": "_ZNSt16nested_exceptionC2Ev",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "762871103ed4cbad8766aba52887d09315247ab583332febff26de4595e0cce4",
  "source_text_sha256": "762871103ed4cbad8766aba52887d09315247ab583332febff26de4595e0cce4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e010](../00c5e/00c5e010.md)

## 疑似コード / UTF-8 216 bytes

~~~c

void _ZNSt16nested_exceptionC2Ev(long *param_1)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVSt16nested_exception_00c9bb40 + 0x10);
  lVar1 = __cxa_current_primary_exception();
  param_1[1] = lVar1;
  return;
}

~~~
