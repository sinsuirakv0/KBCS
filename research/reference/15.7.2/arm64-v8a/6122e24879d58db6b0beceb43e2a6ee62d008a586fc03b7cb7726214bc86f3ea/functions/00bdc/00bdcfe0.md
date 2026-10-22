# 00bdcfe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcfe0.md)

## 関数情報

~~~json
{
  "address": "00bdcfe0",
  "name": "Botan::PKIX::overall_status",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0cb026d9f1d661a7eefacedb84ad5546baccfb6c31810e2c8bbeec7659d2db1a",
  "source_text_sha256": "0cb026d9f1d661a7eefacedb84ad5546baccfb6c31810e2c8bbeec7659d2db1a"
}
~~~
## 呼び出し元

- [00509f18](../00509/00509f18.md)

## 呼び出し先

- [005086fc](../00508/005086fc.md)

## 疑似コード 1/1 / UTF-8 119 bytes

~~~c

void Botan::PKIX::overall_status(vector *param_1)

{
  (*(code *)PTR_overall_status_00c1d028)();
  return;
}

~~~
