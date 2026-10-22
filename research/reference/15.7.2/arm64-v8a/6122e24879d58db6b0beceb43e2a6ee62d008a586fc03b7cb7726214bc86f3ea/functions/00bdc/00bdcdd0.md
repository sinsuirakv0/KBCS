# 00bdcdd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcdd0.md)

## 関数情報

~~~json
{
  "address": "00bdcdd0",
  "name": "Botan::Cert_Extension::Basic_Constraints::get_path_limit",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "886814439ef76413806e9a24e48153d7330943cd9ae648528ff01ea16ba02bd6",
  "source_text_sha256": "886814439ef76413806e9a24e48153d7330943cd9ae648528ff01ea16ba02bd6"
}
~~~
## 呼び出し元

- [004ec8c8](../004ec/004ec8c8.md)
- [004fdfd8](../004fd/004fdfd8.md)

## 呼び出し先

- [004eca70](../004ec/004eca70.md)

## 疑似コード 1/1 / UTF-8 167 bytes

~~~c

void __thiscall Botan::Cert_Extension::Basic_Constraints::get_path_limit(Basic_Constraints *this)

{
  (*(code *)PTR_get_path_limit_00c1cf20)();
  return;
}

~~~
