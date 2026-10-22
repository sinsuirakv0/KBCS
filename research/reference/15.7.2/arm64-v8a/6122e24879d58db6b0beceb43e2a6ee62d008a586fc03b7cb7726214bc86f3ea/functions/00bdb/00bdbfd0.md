# 00bdbfd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbfd0.md)

## 関数情報

~~~json
{
  "address": "00bdbfd0",
  "name": "std::__ndk1::basic_filebuf<char,std::__ndk1::char_traits<char>>::~basic_filebuf",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a8ebf1fe09320d826450a1721e6a3ac4c0c9c5c948dbb0d667418b353bf58d60",
  "source_text_sha256": "a8ebf1fe09320d826450a1721e6a3ac4c0c9c5c948dbb0d667418b353bf58d60"
}
~~~
## 呼び出し元

- [00b88b28](../00b88/00b88b28.md)

## 呼び出し先

- [00b889c8](../00b88/00b889c8.md)

## 疑似コード 1/1 / UTF-8 236 bytes

~~~c

void __thiscall
std::__ndk1::basic_filebuf<char,std::__ndk1::char_traits<char>>::~basic_filebuf
          (basic_filebuf<char,std::__ndk1::char_traits<char>> *this)

{
  (*(code *)PTR__basic_filebuf_00c1c820)();
  return;
}

~~~
