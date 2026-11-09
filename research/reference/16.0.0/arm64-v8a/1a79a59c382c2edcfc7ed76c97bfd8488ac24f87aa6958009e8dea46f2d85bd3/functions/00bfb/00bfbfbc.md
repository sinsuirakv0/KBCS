# 00bfbfbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfbfbc",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_8ios_baseES5_E",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ecbe1dea5eb8de6af0436c9acb4371d708290c99a6eaa374026183f20d6f5e8",
  "source_text_sha256": "7ecbe1dea5eb8de6af0436c9acb4371d708290c99a6eaa374026183f20d6f5e8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 212 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPFRNS_8ios_baseES5_E
                 (long *param_1,code *param_2)

{
  (*param_2)((long)param_1 + *(long *)(*param_1 + -0x18));
  return param_1;
}

~~~
