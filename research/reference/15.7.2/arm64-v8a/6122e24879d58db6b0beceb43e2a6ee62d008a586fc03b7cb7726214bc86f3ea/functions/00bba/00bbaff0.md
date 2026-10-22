# 00bbaff0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbaff0.md)

## 関数情報

~~~json
{
  "address": "00bbaff0",
  "name": "std::bad_cast::~bad_cast",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ada845cd6d7b838da364a0f7b4415dd559824dea4e9efd94f033bcf592f298ef",
  "source_text_sha256": "ada845cd6d7b838da364a0f7b4415dd559824dea4e9efd94f033bcf592f298ef"
}
~~~
## 呼び出し元

- [00be1390](../00be1/00be1390.md)

## 呼び出し先

- [00bdb390](../00bdb/00bdb390.md)

## 疑似コード 1/1 / UTF-8 195 bytes

~~~c

/* std::bad_cast::~bad_cast() */

void __thiscall std::bad_cast::~bad_cast(bad_cast *this)

{
  bad_array_new_length::~bad_array_new_length((bad_array_new_length *)this);
  return;
}

~~~
