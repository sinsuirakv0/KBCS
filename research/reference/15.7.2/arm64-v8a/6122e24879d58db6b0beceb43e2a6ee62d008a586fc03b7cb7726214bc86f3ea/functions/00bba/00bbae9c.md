# 00bbae9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbae9c.md)

## 関数情報

~~~json
{
  "address": "00bbae9c",
  "name": "std::invalid_argument::~invalid_argument",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8d0627d59fd4bf8c9954dd0b887332b053d5da9f0f35c8e5f8b995ec15124aad",
  "source_text_sha256": "8d0627d59fd4bf8c9954dd0b887332b053d5da9f0f35c8e5f8b995ec15124aad"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1030](../00be1/00be1030.md)

## 疑似コード 1/1 / UTF-8 234 bytes

~~~c

/* std::invalid_argument::~invalid_argument() */

void __thiscall std::invalid_argument::~invalid_argument(invalid_argument *this)

{
  logic_error::~logic_error((logic_error *)this);
  operator_delete(this);
  return;
}

~~~
