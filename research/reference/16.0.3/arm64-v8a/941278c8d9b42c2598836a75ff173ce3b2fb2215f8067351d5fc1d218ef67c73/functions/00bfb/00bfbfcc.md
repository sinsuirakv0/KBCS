# 00bfbfcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfbfcc",
  "name": "_ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bdda3bb9d57b4bc8891875a8cfcf761f3764879e4c70b83fb75043c761da9009",
  "source_text_sha256": "bdda3bb9d57b4bc8891875a8cfcf761f3764879e4c70b83fb75043c761da9009"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5f1f0](../00c5f/00c5f1f0.md)

## 疑似コード / UTF-8 437 bytes

~~~c

void _ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE
               (long *param_1,undefined8 param_2,undefined8 *param_3)

{
  _ZNSt6__ndk112system_errorC2ENS_10error_codeERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
            (param_1,*param_3,param_3[1],param_2);
  *param_1 = (long)(PTR__ZTVNSt6__ndk18ios_base7failureE_00c9cb88 + 0x10);
  return;
}

~~~
