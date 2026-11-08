# 00bdeec0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bdeec0",
  "name": "<EXTERNAL>::__vsnprintf_chk",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2bd377ec31dd0d3aedf013b0fdc14d7a1350e841fb90b3ae3c41fea1dc8b8a17",
  "source_text_sha256": "2bd377ec31dd0d3aedf013b0fdc14d7a1350e841fb90b3ae3c41fea1dc8b8a17"
}
~~~

## 呼び出し元

- [00b027b0](../00b02/00b027b0.md)

## 呼び出し先

- [010a5600](../010a5/010a5600.md)

## 疑似コード / UTF-8 89 bytes

~~~c

void __vsnprintf_chk(void)

{
  (*(code *)PTR___vsnprintf_chk_00c1dff0)();
  return;
}

~~~
