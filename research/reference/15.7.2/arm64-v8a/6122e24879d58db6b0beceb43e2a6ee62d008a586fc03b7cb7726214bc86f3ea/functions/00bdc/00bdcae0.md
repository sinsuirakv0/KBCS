# 00bdcae0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcae0.md)

## 関数情報

~~~json
{
  "address": "00bdcae0",
  "name": "Botan::Certificate_Store_In_Memory::find_all_certs",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d36eca8a831b5c7cbbde31fd13987ae1237cb9bb7ee7ef8ca6720953f540006",
  "source_text_sha256": "2d36eca8a831b5c7cbbde31fd13987ae1237cb9bb7ee7ef8ca6720953f540006"
}
~~~
## 呼び出し元

- [00506ee0](../00506/00506ee0.md)

## 呼び出し先

- [004ded14](../004de/004ded14.md)

## 疑似コード 1/1 / UTF-8 159 bytes

~~~c

void Botan::Certificate_Store_In_Memory::find_all_certs(X509_DN *param_1,vector *param_2)

{
  (*(code *)PTR_find_all_certs_00c1cda8)();
  return;
}

~~~
