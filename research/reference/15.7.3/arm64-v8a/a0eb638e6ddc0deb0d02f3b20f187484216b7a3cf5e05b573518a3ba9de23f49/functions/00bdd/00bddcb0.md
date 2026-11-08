# 00bddcb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bddcb0",
  "name": "<EXTERNAL>::atan2",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5727e89c50c7d863d5de3f52de6e7268294db7a53acdeca34ac82841257e4bc8",
  "source_text_sha256": "5727e89c50c7d863d5de3f52de6e7268294db7a53acdeca34ac82841257e4bc8"
}
~~~

## 呼び出し元

- [00a17ce0](../00a17/00a17ce0.md)

## 呼び出し先

- [010a5568](../010a5/010a5568.md)

## 疑似コード / UTF-8 207 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

double atan2(double __y,double __x)

{
  double dVar1;
  
  dVar1 = (double)(*(code *)PTR_atan2_00c1d6e8)();
  return dVar1;
}

~~~
