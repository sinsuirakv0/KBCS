# 00bdaed0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdaed0.md)

## 関数情報

~~~json
{
  "address": "00bdaed0",
  "name": "<EXTERNAL>::__cxa_finalize",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e20da2767b06b1e33bbd3499c9eab09d3fa5a30f02dfcbbe9735e44593340270",
  "source_text_sha256": "e20da2767b06b1e33bbd3499c9eab09d3fa5a30f02dfcbbe9735e44593340270"
}
~~~
## 呼び出し元

- [004182d0](../00418/004182d0.md)

## 呼び出し先

- [010a5000](../010a5/010a5000.md)

## 疑似コード 1/1 / UTF-8 95 bytes

~~~c

void __cxa_finalize(void)

{
  (*(code *)PTR___cxa_finalize_00c1bfa0)();
  return;
}

~~~
