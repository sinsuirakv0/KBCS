# 00bdbeb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbeb0.md)

## 関数情報

~~~json
{
  "address": "00bdbeb0",
  "name": "Botan::mgf1_mask",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4df5ad547ace87e73032d9c9ccb63e3c11dddbcdcf85a0b08694adeceec7e6e",
  "source_text_sha256": "f4df5ad547ace87e73032d9c9ccb63e3c11dddbcdcf85a0b08694adeceec7e6e"
}
~~~
## 呼び出し元

- [0049eb38](../0049e/0049eb38.md)
- [0049ef6c](../0049e/0049ef6c.md)

## 呼び出し先

- [004acad0](../004ac/004acad0.md)

## 疑似コード 1/1 / UTF-8 190 bytes

~~~c

void Botan::mgf1_mask(HashFunction *param_1,uchar *param_2,ulong param_3,uchar *param_4,
                     ulong param_5)

{
  (*(code *)PTR_mgf1_mask_00c1c790)();
  return;
}

~~~
