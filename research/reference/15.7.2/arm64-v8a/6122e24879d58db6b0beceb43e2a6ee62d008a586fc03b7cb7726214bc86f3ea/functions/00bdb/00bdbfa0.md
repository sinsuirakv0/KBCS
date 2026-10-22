# 00bdbfa0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbfa0.md)

## 関数情報

~~~json
{
  "address": "00bdbfa0",
  "name": "std::__ndk1::basic_ostream<char,std::__ndk1::char_traits<char>>::flush",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a6c8fa397d924880fd5174294cf9eece97f6566486f0db38d0a2409b2337f050",
  "source_text_sha256": "a6c8fa397d924880fd5174294cf9eece97f6566486f0db38d0a2409b2337f050"
}
~~~
## 呼び出し元

- [004a33f8](../004a3/004a33f8.md)
- [00b31d40](../00b31/00b31d40.md)
- [00b382ec](../00b38/00b382ec.md)
- [00b384c0](../00b38/00b384c0.md)
- [00b38674](../00b38/00b38674.md)
- [00b38828](../00b38/00b38828.md)
- [00b3f8f8](../00b3f/00b3f8f8.md)
- [00b4127c](../00b41/00b4127c.md)
- [00b41450](../00b41/00b41450.md)
- [00b46650](../00b46/00b46650.md)
- [00b46a88](../00b46/00b46a88.md)
- [00b46b54](../00b46/00b46b54.md)
- [00b46c00](../00b46/00b46c00.md)
- [00b46f84](../00b46/00b46f84.md)
- [00b7f24c](../00b7f/00b7f24c.md)
- [00b819f8](../00b81/00b819f8.md)
- [00b897b0](../00b89/00b897b0.md)

## 呼び出し先

- [00b31d40](../00b31/00b31d40.md)

## 疑似コード 1/1 / UTF-8 218 bytes

~~~c

void __thiscall
std::__ndk1::basic_ostream<char,std::__ndk1::char_traits<char>>::flush
          (basic_ostream<char,std::__ndk1::char_traits<char>> *this)

{
  (*(code *)PTR_flush_00c1c808)();
  return;
}

~~~
