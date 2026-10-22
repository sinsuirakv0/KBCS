# 00bdbac0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbac0.md)

## 関数情報

~~~json
{
  "address": "00bdbac0",
  "name": "std::__ndk1::chrono::system_clock::from_time_t",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee6204611048b158610a83f0625c11b2b73832f46e264b70ca00f4ce49e2ee77",
  "source_text_sha256": "ee6204611048b158610a83f0625c11b2b73832f46e264b70ca00f4ce49e2ee77"
}
~~~
## 呼び出し元

- [0048c2e0](../0048c/0048c2e0.md)

## 呼び出し先

- [00b728b8](../00b72/00b728b8.md)

## 疑似コード 1/1 / UTF-8 132 bytes

~~~c

void std::__ndk1::chrono::system_clock::from_time_t(long param_1)

{
  (*(code *)PTR_from_time_t_00c1c598)();
  return;
}

~~~
