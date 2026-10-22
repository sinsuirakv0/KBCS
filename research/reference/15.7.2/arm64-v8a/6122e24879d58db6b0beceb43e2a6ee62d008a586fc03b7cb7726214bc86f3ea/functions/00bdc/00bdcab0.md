# 00bdcab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcab0.md)

## 関数情報

~~~json
{
  "address": "00bdcab0",
  "name": "Botan::Certificate_Store_In_Memory::find_cert",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d6dd993fe880d32d5cf8005a9d4ab8672003ac4914e3a487ee0644759e4f2da",
  "source_text_sha256": "7d6dd993fe880d32d5cf8005a9d4ab8672003ac4914e3a487ee0644759e4f2da"
}
~~~
## 呼び出し元

- [0050645c](../00506/0050645c.md)

## 呼び出し先

- [004de9a8](../004de/004de9a8.md)

## 疑似コード 1/1 / UTF-8 149 bytes

~~~c

void Botan::Certificate_Store_In_Memory::find_cert(X509_DN *param_1,vector *param_2)

{
  (*(code *)PTR_find_cert_00c1cd90)();
  return;
}

~~~
