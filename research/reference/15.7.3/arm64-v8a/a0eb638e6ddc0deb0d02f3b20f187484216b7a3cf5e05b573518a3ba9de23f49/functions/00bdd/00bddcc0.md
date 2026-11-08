# 00bddcc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bddcc0",
  "name": "<EXTERNAL>::__umask_chk",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "84428188beee9535ce525bc0af16da85cdee8389e36a7238b37b14b0a335540d",
  "source_text_sha256": "84428188beee9535ce525bc0af16da85cdee8389e36a7238b37b14b0a335540d"
}
~~~

## 呼び出し元

- [00acc304](../00acc/00acc304.md)
- [00b4b4dc](../00b4b/00b4b4dc.md)

## 呼び出し先

- [010a5570](../010a5/010a5570.md)

## 疑似コード / UTF-8 81 bytes

~~~c

void __umask_chk(void)

{
  (*(code *)PTR___umask_chk_00c1d6f0)();
  return;
}

~~~
