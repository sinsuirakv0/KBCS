# 00b7ebcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b7ebcc.md)

## 関数情報

~~~json
{
  "address": "00b7ebcc",
  "name": "std::__ndk1::basic_ios<char,std::__ndk1::char_traits<char>>::~basic_ios",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2af47fa7ac09e73f370c5d056edd3270c38175d3a2a57da650855b0d1561681c",
  "source_text_sha256": "2af47fa7ac09e73f370c5d056edd3270c38175d3a2a57da650855b0d1561681c"
}
~~~
## 呼び出し元

- [00bdb070](../00bdb/00bdb070.md)
- [00be1240](../00be1/00be1240.md)

## 呼び出し先

- [00be00e0](../00be0/00be00e0.md)

## 疑似コード 1/1 / UTF-8 306 bytes

~~~c

/* std::__ndk1::basic_ios<char, std::__ndk1::char_traits<char> >::~basic_ios() */

void __thiscall
std::__ndk1::basic_ios<char,std::__ndk1::char_traits<char>>::~basic_ios
          (basic_ios<char,std::__ndk1::char_traits<char>> *this)

{
  ios_base::~ios_base((ios_base *)this);
  return;
}

~~~
