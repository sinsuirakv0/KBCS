# 00bddba0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bddba0.md)

## 関数情報

~~~json
{
  "address": "00bddba0",
  "name": "firebase::Variant::AsInt64",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b0f120abaa30a7b4b54319983829ef78522611b19f7d9ee905138725a13af08",
  "source_text_sha256": "7b0f120abaa30a7b4b54319983829ef78522611b19f7d9ee905138725a13af08"
}
~~~
## 呼び出し元

- [0084a918](../0084a/0084a918.md)

## 呼び出し先

- [00b04800](../00b04/00b04800.md)

## 疑似コード 1/1 / UTF-8 100 bytes

~~~c

void firebase::Variant::AsInt64(void)

{
  (*(code *)PTR_AsInt64_00c1d608)();
  return;
}

~~~
