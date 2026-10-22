# 00bdcdf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcdf0.md)

## 関数情報

~~~json
{
  "address": "00bdcdf0",
  "name": "Botan::Cert_Extension::Subject_Key_ID::Subject_Key_ID",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b7a171219ddabfe4c6b783e3bee21698d147bd977d370a49594e6d2c87d48f7d",
  "source_text_sha256": "b7a171219ddabfe4c6b783e3bee21698d147bd977d370a49594e6d2c87d48f7d"
}
~~~
## 呼び出し元

- [004ede80](../004ed/004ede80.md)
- [0050a638](../0050a/0050a638.md)

## 呼び出し先

- [004f61e8](../004f6/004f61e8.md)

## 疑似コード 1/1 / UTF-8 212 bytes

~~~c

void __thiscall
Botan::Cert_Extension::Subject_Key_ID::Subject_Key_ID
          (Subject_Key_ID *this,vector *param_1,basic_string *param_2)

{
  (*(code *)PTR_Subject_Key_ID_00c1cf30)();
  return;
}

~~~
