# 005bcdec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "005bcdec",
  "name": "FUN_005bcdec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d5aaa47432c3d651ab9917043ad384985d81d7dca96828ca01ecc03b7379758",
  "source_text_sha256": "9d5aaa47432c3d651ab9917043ad384985d81d7dca96828ca01ecc03b7379758"
}
~~~

## 呼び出し元

- [006ee6c8](../006ee/006ee6c8.md)
- [009f4a74](../009f4/009f4a74.md)
- [009f560c](../009f5/009f560c.md)

## 呼び出し先

- [005bc280](../005bc/005bc280.md)

## 疑似コード / UTF-8 95 bytes

~~~c

bool FUN_005bcdec(void)

{
  int iVar1;
  
  iVar1 = FUN_005bc280();
  return iVar1 != -1;
}

~~~
