# 00bdeff0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdeff0.md)

## 関数情報

~~~json
{
  "address": "00bdeff0",
  "name": "reflection::CreateObject",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "13f27aafe28cf44947d0a37ef12bcffb85e79938691659f1767b8cf3938215d4",
  "source_text_sha256": "13f27aafe28cf44947d0a37ef12bcffb85e79938691659f1767b8cf3938215d4"
}
~~~
## 呼び出し元

- [00b290f4](../00b29/00b290f4.md)

## 呼び出し先

- [00b29f9c](../00b29/00b29f9c.md)

## 疑似コード 1/1 / UTF-8 103 bytes

~~~c

void reflection::CreateObject(void)

{
  (*(code *)PTR_CreateObject_00c1e030)();
  return;
}

~~~
