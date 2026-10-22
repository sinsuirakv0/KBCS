# 00bdafb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdafb0.md)

## 関数情報

~~~json
{
  "address": "00bdafb0",
  "name": "std::logic_error::~logic_error",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2b0372fa8c99ff58781b9d6062518a083ee39ef51a949244273da7639eceb35",
  "source_text_sha256": "d2b0372fa8c99ff58781b9d6062518a083ee39ef51a949244273da7639eceb35"
}
~~~
## 呼び出し元

- [00bbaec8](../00bba/00bbaec8.md)

## 呼び出し先

- [00bbad50](../00bba/00bbad50.md)

## 疑似コード 1/1 / UTF-8 133 bytes

~~~c

void __thiscall std::logic_error::~logic_error(logic_error *this)

{
  (*(code *)PTR__logic_error_00c1c010)();
  return;
}

~~~
