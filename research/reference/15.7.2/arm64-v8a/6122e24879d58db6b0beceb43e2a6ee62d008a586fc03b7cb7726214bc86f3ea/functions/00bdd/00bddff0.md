# 00bddff0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bddff0.md)

## 関数情報

~~~json
{
  "address": "00bddff0",
  "name": "firebase::util::GetAndClearExceptionMessage",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "908c43b07a156e922b1596d0faa49686d2489515d49a13735be7222596681343",
  "source_text_sha256": "908c43b07a156e922b1596d0faa49686d2489515d49a13735be7222596681343"
}
~~~
## 呼び出し元

- [00ae2b00](../00ae2/00ae2b00.md)
- [00ae2ec8](../00ae2/00ae2ec8.md)
- [00b4dd3c](../00b4d/00b4dd3c.md)
- [00b4e378](../00b4e/00b4e378.md)

## 呼び出し先

- [00af710c](../00af7/00af710c.md)

## 疑似コード 1/1 / UTF-8 149 bytes

~~~c

void firebase::util::GetAndClearExceptionMessage(_JNIEnv *param_1)

{
  (*(code *)PTR_GetAndClearExceptionMessage_00c1d830)();
  return;
}

~~~
