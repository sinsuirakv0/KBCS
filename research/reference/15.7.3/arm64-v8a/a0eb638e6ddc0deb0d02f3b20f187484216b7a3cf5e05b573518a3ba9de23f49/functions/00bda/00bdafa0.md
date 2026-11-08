# 00bdafa0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bdafa0",
  "name": "<EXTERNAL>::__register_atfork",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1973a956e5ab21db6d8309a7ac966dc79665ee5da574a895ab429a5c1b5dc115",
  "source_text_sha256": "1973a956e5ab21db6d8309a7ac966dc79665ee5da574a895ab429a5c1b5dc115"
}
~~~

## 呼び出し元

- [00418320](../00418/00418320.md)

## 呼び出し先

- [010a5010](../010a5/010a5010.md)

## 疑似コード / UTF-8 93 bytes

~~~c

void __register_atfork(void)

{
  (*(code *)PTR___register_atfork_00c1c060)();
  return;
}

~~~
