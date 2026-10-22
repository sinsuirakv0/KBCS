# 00bdbee0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbee0.md)

## 関数情報

~~~json
{
  "address": "00bdbee0",
  "name": "Botan::Entropy_Sources::add_source",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "73bcac4b545018b80e7c59852be04395e483144fe696a98efe96279e5c5d2898",
  "source_text_sha256": "73bcac4b545018b80e7c59852be04395e483144fe696a98efe96279e5c5d2898"
}
~~~
## 呼び出し元

- [004a0a28](../004a0/004a0a28.md)

## 呼び出し先

- [004a0414](../004a0/004a0414.md)

## 疑似コード 1/1 / UTF-8 122 bytes

~~~c

void __thiscall Botan::Entropy_Sources::add_source(void)

{
  (*(code *)PTR_add_source_00c1c7a8)();
  return;
}

~~~
