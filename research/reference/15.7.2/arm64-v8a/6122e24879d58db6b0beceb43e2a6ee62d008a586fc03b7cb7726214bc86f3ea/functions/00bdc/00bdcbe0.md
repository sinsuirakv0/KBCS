# 00bdcbe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcbe0.md)

## 関数情報

~~~json
{
  "address": "00bdcbe0",
  "name": "Botan::verify_cert_constraints_valid_for_key_type",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db690bd890fe95de43236aef126557a058f52eff8a0f1c62d92082c109e0c7ff",
  "source_text_sha256": "db690bd890fe95de43236aef126557a058f52eff8a0f1c62d92082c109e0c7ff"
}
~~~
## 呼び出し元

- [004ede80](../004ed/004ede80.md)
- [0050a638](../0050a/0050a638.md)
- [0050b45c](../0050b/0050b45c.md)

## 呼び出し先

- [004e3024](../004e3/004e3024.md)

## 疑似コード 1/1 / UTF-8 169 bytes

~~~c

void __thiscall Botan::verify_cert_constraints_valid_for_key_type(void)

{
  (*(code *)PTR_verify_cert_constraints_valid_for_key_type_00c1ce28)();
  return;
}

~~~
