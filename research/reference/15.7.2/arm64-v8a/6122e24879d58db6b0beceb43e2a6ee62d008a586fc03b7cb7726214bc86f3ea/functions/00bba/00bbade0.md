# 00bbade0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bbade0",
  "name": "_ZNSt14overflow_errorD1Ev",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b816449440e6d5f68d7d7e458f207e49df2f1504666abb562feeaa7d3bd16150",
  "source_text_sha256": "b816449440e6d5f68d7d7e458f207e49df2f1504666abb562feeaa7d3bd16150"
}
~~~

## 呼び出し元

- [00bdd970](../00bdd/00bdd970.md)
- [00be0e70](../00be0/00be0e70.md)
- [00be0ed0](../00be0/00be0ed0.md)
- [00be10a0](../00be1/00be10a0.md)
- [00be1d80](../00be1/00be1d80.md)

## 呼び出し先

- [00bd6d30](../00bd6/00bd6d30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb390](../00bdb/00bdb390.md)

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt14overflow_errorD1Ev(long *param_1)

{
  int iVar1;
  long lVar2;
  
  lVar2 = param_1[1];
  *param_1 = (long)(PTR__ZTVSt13runtime_error_00c1bb68 + 0x10);
  iVar1 = FUN_00bd6d30(0xffffffff,lVar2 + -8);
  if (iVar1 + -1 < 0) {
    _ZdlPv((void *)(lVar2 + -0x18));
  }
  _ZNSt20bad_array_new_lengthD1Ev(param_1);
  return;
}

~~~
