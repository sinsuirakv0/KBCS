# 00c2cefc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00c2cefc",
  "name": "_ZNSt6__ndk18numpunctIcEC2Em",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "587f2c0bf98683396df8bbf0ee4d6722768cabdf3f2b3aa22a8bfd6647efa85b",
  "source_text_sha256": "587f2c0bf98683396df8bbf0ee4d6722768cabdf3f2b3aa22a8bfd6647efa85b"
}
~~~

## 呼び出し元

- [00c5f8a0](../00c5f/00c5f8a0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 316 bytes

~~~c

void _ZNSt6__ndk18numpunctIcEC2Em(long *param_1,long param_2)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVNSt6__ndk18numpunctIcEE_00c9ce88;
  *(undefined2 *)(param_1 + 2) = 0x2c2e;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[3] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  param_1[1] = param_2 + -1;
  return;
}

~~~
