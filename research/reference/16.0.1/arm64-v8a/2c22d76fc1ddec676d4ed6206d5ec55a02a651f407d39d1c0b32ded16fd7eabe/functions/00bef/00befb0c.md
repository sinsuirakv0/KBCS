# 00befb0c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00befb0c",
  "name": "_ZNSt16nested_exceptionC2Ev",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a83acee3a1d12a3c199bb2987b2e0ae2f296cabb3dc6e06dd77650a9794d5fee",
  "source_text_sha256": "a83acee3a1d12a3c199bb2987b2e0ae2f296cabb3dc6e06dd77650a9794d5fee"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5df40](../00c5d/00c5df40.md)

## 疑似コード / UTF-8 216 bytes

~~~c

void _ZNSt16nested_exceptionC2Ev(long *param_1)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVSt16nested_exception_00c9ba70 + 0x10);
  lVar1 = __cxa_current_primary_exception();
  param_1[1] = lVar1;
  return;
}

~~~
