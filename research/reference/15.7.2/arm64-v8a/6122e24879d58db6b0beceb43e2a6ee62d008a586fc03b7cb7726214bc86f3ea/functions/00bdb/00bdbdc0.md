# 00bdbdc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbdc0.md)

## 関数情報

~~~json
{
  "address": "00bdbdc0",
  "name": "Botan::BigInt::get_substring",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "14c7a58f5a5eb2eb044ca7f9d2b6109622a8d15d7f013cf3af749130ff303f7e",
  "source_text_sha256": "14c7a58f5a5eb2eb044ca7f9d2b6109622a8d15d7f013cf3af749130ff303f7e"
}
~~~
## 呼び出し元

- [004bc440](../004bc/004bc440.md)
- [004bd550](../004bd/004bd550.md)

## 呼び出し先

- [00498254](../00498/00498254.md)

## 疑似コード 1/1 / UTF-8 155 bytes

~~~c

void __thiscall Botan::BigInt::get_substring(BigInt *this,ulong param_1,ulong param_2)

{
  (*(code *)PTR_get_substring_00c1c718)();
  return;
}

~~~
