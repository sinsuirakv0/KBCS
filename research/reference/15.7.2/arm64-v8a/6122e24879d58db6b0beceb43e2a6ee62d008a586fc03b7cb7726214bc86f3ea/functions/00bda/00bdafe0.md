# 00bdafe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdafe0.md)

## 関数情報

~~~json
{
  "address": "00bdafe0",
  "name": "std::logic_error::logic_error",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "93ced2edd4646f0a217a01664be8c6a18d273874bdf5415514c7b90ec8b7fc9b",
  "source_text_sha256": "93ced2edd4646f0a217a01664be8c6a18d273874bdf5415514c7b90ec8b7fc9b"
}
~~~
## 呼び出し元

- [00418c88](../00418/00418c88.md)
- [0041fe40](../0041f/0041fe40.md)
- [00ae0404](../00ae0/00ae0404.md)
- [00b7b2a4](../00b7b/00b7b2a4.md)

## 呼び出し先

- [00b736a8](../00b73/00b736a8.md)

## 疑似コード 1/1 / UTF-8 145 bytes

~~~c

void __thiscall std::logic_error::logic_error(logic_error *this,char *param_1)

{
  (*(code *)PTR_logic_error_00c1c028)();
  return;
}

~~~
