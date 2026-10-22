# 00bddcd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bddcd0.md)

## 関数情報

~~~json
{
  "address": "00bddcd0",
  "name": "firebase::CleanupNotifier::~CleanupNotifier",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "291133f6aa9d722b75c9304bdfe5c818c10982ea4738466221b47a506e618aa3",
  "source_text_sha256": "291133f6aa9d722b75c9304bdfe5c818c10982ea4738466221b47a506e618aa3"
}
~~~
## 呼び出し元

- [00af8d88](../00af8/00af8d88.md)
- [00afadc0](../00afa/00afadc0.md)
- [00afae90](../00afa/00afae90.md)
- [00afea18](../00afe/00afea18.md)
- [00b5572c](../00b55/00b5572c.md)

## 呼び出し先

- [00afc4e4](../00afc/00afc4e4.md)

## 疑似コード 1/1 / UTF-8 154 bytes

~~~c

void __thiscall firebase::CleanupNotifier::~CleanupNotifier(CleanupNotifier *this)

{
  (*(code *)PTR__CleanupNotifier_00c1d6a0)();
  return;
}

~~~
