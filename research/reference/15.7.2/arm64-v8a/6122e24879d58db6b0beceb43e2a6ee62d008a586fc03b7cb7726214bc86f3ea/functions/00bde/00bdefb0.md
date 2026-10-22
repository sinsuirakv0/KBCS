# 00bdefb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdefb0.md)

## 関数情報

~~~json
{
  "address": "00bdefb0",
  "name": "reflection::CreateField",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f64405b3deb26ac7e1fb2040e52fc5629f8a88756d2fd3015c37dabac44c6912",
  "source_text_sha256": "f64405b3deb26ac7e1fb2040e52fc5629f8a88756d2fd3015c37dabac44c6912"
}
~~~
## 呼び出し元

- [00b2995c](../00b29/00b2995c.md)

## 呼び出し先

- [00b2afe0](../00b2a/00b2afe0.md)

## 疑似コード 1/1 / UTF-8 101 bytes

~~~c

void reflection::CreateField(void)

{
  (*(code *)PTR_CreateField_00c1e010)();
  return;
}

~~~
