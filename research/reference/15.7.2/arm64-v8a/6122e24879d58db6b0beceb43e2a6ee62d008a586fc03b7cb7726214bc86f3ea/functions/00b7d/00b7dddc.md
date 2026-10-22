# 00b7dddc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b7dddc.md)

## 関数情報

~~~json
{
  "address": "00b7dddc",
  "name": "std::__ndk1::random_device::~random_device",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d027b2defeab67df393ee32b96836604c9c99cfac0fb039f933433f149f8400a",
  "source_text_sha256": "d027b2defeab67df393ee32b96836604c9c99cfac0fb039f933433f149f8400a"
}
~~~
## 呼び出し元

- [00bdb480](../00bdb/00bdb480.md)

## 呼び出し先

- [00bdc880](../00bdc/00bdc880.md)

## 疑似コード 1/1 / UTF-8 213 bytes

~~~c

/* std::__ndk1::random_device::~random_device() */

int __thiscall std::__ndk1::random_device::~random_device(random_device *this)

{
  int iVar1;
  
  iVar1 = close(*(int *)this);
  return iVar1;
}

~~~
