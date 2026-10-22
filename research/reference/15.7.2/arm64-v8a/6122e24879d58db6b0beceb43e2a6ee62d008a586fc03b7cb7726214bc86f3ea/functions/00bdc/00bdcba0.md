# 00bdcba0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcba0.md)

## 関数情報

~~~json
{
  "address": "00bdcba0",
  "name": "Botan::Data_Store::add",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f7ccf3f947287db5eac05e8fb4681a59671c64ad5d767ce30f3d957b9609430",
  "source_text_sha256": "6f7ccf3f947287db5eac05e8fb4681a59671c64ad5d767ce30f3d957b9609430"
}
~~~
## 呼び出し元

- [004f6118](../004f6/004f6118.md)
- [004f6690](../004f6/004f6690.md)

## 呼び出し先

- [004e1d28](../004e1/004e1d28.md)

## 疑似コード 1/1 / UTF-8 153 bytes

~~~c

void __thiscall Botan::Data_Store::add(Data_Store *this,basic_string *param_1,vector *param_2)

{
  (*(code *)PTR_add_00c1ce08)();
  return;
}

~~~
