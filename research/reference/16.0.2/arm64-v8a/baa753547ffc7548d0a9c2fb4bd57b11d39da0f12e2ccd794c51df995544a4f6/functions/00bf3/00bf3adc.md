# 00bf3adc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bf3adc",
  "name": "_ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKw",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dcf6df050c2fae4bed68da48a7eb029d70e6d9c8936d387acc153f5a900e90db",
  "source_text_sha256": "dcf6df050c2fae4bed68da48a7eb029d70e6d9c8936d387acc153f5a900e90db"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e0d0](../00c5e/00c5e0d0.md)
- [00c5e0f0](../00c5e/00c5e0f0.md)

## 疑似コード / UTF-8 346 bytes

~~~c

void _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKw
               (undefined8 param_1,undefined8 param_2,wchar_t *param_3)

{
  size_t sVar1;
  
  sVar1 = wcslen(param_3);
  _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKwm
            (param_1,param_2,param_3,sVar1);
  return;
}

~~~
