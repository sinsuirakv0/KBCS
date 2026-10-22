# 00bdecc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdecc0.md)

## 関数情報

~~~json
{
  "address": "00bdecc0",
  "name": "firebase::FutureBackingData::ClearExistingCallbacks",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09ef7990d89eb301f1a39ef6823f052c3fd22e04b2b0e5e035e7ed7106a45422",
  "source_text_sha256": "09ef7990d89eb301f1a39ef6823f052c3fd22e04b2b0e5e035e7ed7106a45422"
}
~~~
## 呼び出し元

- [00afe698](../00afe/00afe698.md)

## 呼び出し先

- [00afe91c](../00afe/00afe91c.md)

## 疑似コード 1/1 / UTF-8 170 bytes

~~~c

void __thiscall firebase::FutureBackingData::ClearExistingCallbacks(FutureBackingData *this)

{
  (*(code *)PTR_ClearExistingCallbacks_00c1de98)();
  return;
}

~~~
