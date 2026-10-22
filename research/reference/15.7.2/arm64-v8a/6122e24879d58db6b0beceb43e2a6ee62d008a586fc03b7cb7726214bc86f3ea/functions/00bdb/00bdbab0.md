# 00bdbab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbab0.md)

## 関数情報

~~~json
{
  "address": "00bdbab0",
  "name": "Botan::calendar_point::to_std_timepoint",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6bd03f9cba24f7ed35cf5edf5172da864d3faf2e5f03c1ce654c6a043fd8ad27",
  "source_text_sha256": "6bd03f9cba24f7ed35cf5edf5172da864d3faf2e5f03c1ce654c6a043fd8ad27"
}
~~~
## 呼び出し元

- [0048c288](../0048c/0048c288.md)

## 呼び出し先

- [0048c2e0](../0048c/0048c2e0.md)

## 疑似コード 1/1 / UTF-8 149 bytes

~~~c

void __thiscall Botan::calendar_point::to_std_timepoint(calendar_point *this)

{
  (*(code *)PTR_to_std_timepoint_00c1c590)();
  return;
}

~~~
