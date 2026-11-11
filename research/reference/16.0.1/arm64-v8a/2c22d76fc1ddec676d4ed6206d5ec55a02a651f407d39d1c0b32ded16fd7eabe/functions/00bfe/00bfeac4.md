# 00bfeac4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfeac4",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_8ios_baseES5_E",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc8eb55fba3f41207ec8771d702d7be7198b8a83b1f5b44d6fcdd1ba6dc04e70",
  "source_text_sha256": "fc8eb55fba3f41207ec8771d702d7be7198b8a83b1f5b44d6fcdd1ba6dc04e70"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 212 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_8ios_baseES5_E
                 (long *param_1,code *param_2)

{
  (*param_2)((long)param_1 + *(long *)(*param_1 + -0x18));
  return param_1;
}

~~~
