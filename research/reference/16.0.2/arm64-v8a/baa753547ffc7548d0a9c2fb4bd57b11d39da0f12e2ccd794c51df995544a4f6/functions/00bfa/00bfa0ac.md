# 00bfa0ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfa0ac",
  "name": "_ZNSt6__ndk113shared_futureIvEaSERKS1_",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "025e8e772dc6c446a390998dfe43922d41068911f837d42517d5acc7c4759a05",
  "source_text_sha256": "025e8e772dc6c446a390998dfe43922d41068911f837d42517d5acc7c4759a05"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)

## 疑似コード / UTF-8 397 bytes

~~~c

long * _ZNSt6__ndk113shared_futureIvEaSERKS1_(long *param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  
  if (*param_2 != 0) {
    FUN_00c53d70(1,*param_2 + 8);
  }
  plVar2 = (long *)*param_1;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
  }
  *param_1 = *param_2;
  return param_1;
}

~~~
