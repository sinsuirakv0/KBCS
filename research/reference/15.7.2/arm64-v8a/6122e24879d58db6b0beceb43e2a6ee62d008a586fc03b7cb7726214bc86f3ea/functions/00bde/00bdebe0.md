# 00bdebe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdebe0.md)

## 関数情報

~~~json
{
  "address": "00bdebe0",
  "name": "firebase::CleanupNotifier::UnregisterOwner",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2fc9cb3d6941857a2aeba6dacb12f6360d1c5262e80689751c19119a41aac51f",
  "source_text_sha256": "2fc9cb3d6941857a2aeba6dacb12f6360d1c5262e80689751c19119a41aac51f"
}
~~~
## 呼び出し元

- [00afc63c](../00afc/00afc63c.md)
- [00afc910](../00afc/00afc910.md)
- [00afc98c](../00afc/00afc98c.md)

## 呼び出し先

- [00afcb88](../00afc/00afcb88.md)

## 疑似コード 1/1 / UTF-8 124 bytes

~~~c

void firebase::CleanupNotifier::UnregisterOwner(void)

{
  (*(code *)PTR_UnregisterOwner_00c1de28)();
  return;
}

~~~
