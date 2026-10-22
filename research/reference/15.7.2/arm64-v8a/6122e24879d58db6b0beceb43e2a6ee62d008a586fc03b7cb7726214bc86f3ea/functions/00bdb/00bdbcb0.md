# 00bdbcb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbcb0.md)

## 関数情報

~~~json
{
  "address": "00bdbcb0",
  "name": "Botan::base64_decode",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2bcc685d80fb23f0e9713a1e93a28934118cf9ad543aa62182c64cdc2710c421",
  "source_text_sha256": "2bcc685d80fb23f0e9713a1e93a28934118cf9ad543aa62182c64cdc2710c421"
}
~~~
## 呼び出し元

- [0055dc58](../0055d/0055dc58.md)

## 呼び出し先

- [00493354](../00493/00493354.md)

## 疑似コード 1/1 / UTF-8 173 bytes

~~~c

void __thiscall Botan::base64_decode(Botan *this,basic_string *param_1,bool param_2)

{
  (*(code *)PTR_base64_decode_00c1c690)(this,param_1,param_2);
  return;
}

~~~
