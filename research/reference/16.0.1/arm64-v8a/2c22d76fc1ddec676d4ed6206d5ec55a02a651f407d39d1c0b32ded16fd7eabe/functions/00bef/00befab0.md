# 00befab0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00befab0",
  "name": "_ZNSt13exception_ptraSERKS_",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6a4f2b6986ae6b3efb7483c629be87c5306bc0480dbf480a3c7b17005fe96bd8",
  "source_text_sha256": "6a4f2b6986ae6b3efb7483c629be87c5306bc0480dbf480a3c7b17005fe96bd8"
}
~~~

## 呼び出し元

- [00c5df30](../00c5d/00c5df30.md)

## 呼び出し先

- [00c5df10](../00c5d/00c5df10.md)
- [00c5df20](../00c5d/00c5df20.md)

## 疑似コード / UTF-8 240 bytes

~~~c

long * _ZNSt13exception_ptraSERKS_(long *param_1,long *param_2)

{
  if (*param_1 != *param_2) {
    __cxa_increment_exception_refcount();
    __cxa_decrement_exception_refcount(*param_1);
    *param_1 = *param_2;
  }
  return param_1;
}

~~~
