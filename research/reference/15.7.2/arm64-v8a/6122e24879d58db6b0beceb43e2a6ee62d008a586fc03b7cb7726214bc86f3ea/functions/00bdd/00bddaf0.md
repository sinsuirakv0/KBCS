# 00bddaf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bddaf0.md)

## 関数情報

~~~json
{
  "address": "00bddaf0",
  "name": "firebase::auth::User::is_valid",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "515d0c2da8dc0f6b9d6f637e5f1da28e45a9d35b142e5d9df8ffcddf3e54a0ff",
  "source_text_sha256": "515d0c2da8dc0f6b9d6f637e5f1da28e45a9d35b142e5d9df8ffcddf3e54a0ff"
}
~~~
## 呼び出し元

- [00848250](../00848/00848250.md)
- [0084859c](../00848/0084859c.md)
- [00ad4f2c](../00ad4/00ad4f2c.md)
- [00b5c870](../00b5c/00b5c870.md)
- [00b5c8a4](../00b5c/00b5c8a4.md)

## 呼び出し先

- [00b6e878](../00b6e/00b6e878.md)

## 疑似コード 1/1 / UTF-8 122 bytes

~~~c

void __thiscall firebase::auth::User::is_valid(User *this)

{
  (*(code *)PTR_is_valid_00c1d5b0)();
  return;
}

~~~
