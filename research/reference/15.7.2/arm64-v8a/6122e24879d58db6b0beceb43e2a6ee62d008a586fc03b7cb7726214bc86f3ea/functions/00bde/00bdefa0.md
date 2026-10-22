# 00bdefa0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdefa0.md)

## 関数情報

~~~json
{
  "address": "00bdefa0",
  "name": "reflection::CreateType",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7345d61dd17e7fde4c893af8124511d3fe25125b5dbc93526cdc57da6eb3ddd7",
  "source_text_sha256": "7345d61dd17e7fde4c893af8124511d3fe25125b5dbc93526cdc57da6eb3ddd7"
}
~~~
## 呼び出し元

- [00b29390](../00b29/00b29390.md)
- [00b2995c](../00b29/00b2995c.md)
- [00b2af9c](../00b2a/00b2af9c.md)
- [00b2bd18](../00b2b/00b2bd18.md)

## 呼び出し先

- [00b2c5c0](../00b2c/00b2c5c0.md)

## 疑似コード 1/1 / UTF-8 99 bytes

~~~c

void reflection::CreateType(void)

{
  (*(code *)PTR_CreateType_00c1e008)();
  return;
}

~~~
