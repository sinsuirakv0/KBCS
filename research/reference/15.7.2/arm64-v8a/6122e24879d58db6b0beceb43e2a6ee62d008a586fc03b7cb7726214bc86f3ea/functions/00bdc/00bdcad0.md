# 00bdcad0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcad0.md)

## 関数情報

~~~json
{
  "address": "00bdcad0",
  "name": "Botan::X509_DN::get_attributes",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "82698432c1fc204d412ab65ea8cfbada72a73079d1f161b0bcdb2f8e0de89164",
  "source_text_sha256": "82698432c1fc204d412ab65ea8cfbada72a73079d1f161b0bcdb2f8e0de89164"
}
~~~
## 呼び出し元

- [004deb5c](../004de/004deb5c.md)
- [004e50d0](../004e5/004e50d0.md)
- [004f1c30](../004f1/004f1c30.md)
- [004f1ecc](../004f1/004f1ecc.md)
- [00503af8](../00503/00503af8.md)

## 呼び出し先

- [004e5c34](../004e5/004e5c34.md)

## 疑似コード 1/1 / UTF-8 111 bytes

~~~c

void Botan::X509_DN::get_attributes(void)

{
  (*(code *)PTR_get_attributes_00c1cda0)();
  return;
}

~~~
