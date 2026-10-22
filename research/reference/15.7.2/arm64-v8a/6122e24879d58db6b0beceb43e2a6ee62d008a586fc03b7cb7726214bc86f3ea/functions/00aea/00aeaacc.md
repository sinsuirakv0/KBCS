# 00aeaacc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeaacc.md)

## 関数情報

~~~json
{
  "address": "00aeaacc",
  "name": "firebase::util::float_class::GetMethodId",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bfdab53a1c3415388c1b0630e2fb6d99688fa9fa391dac803d85d01bd17b1e11",
  "source_text_sha256": "bfdab53a1c3415388c1b0630e2fb6d99688fa9fa391dac803d85d01bd17b1e11"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~
## 疑似コード 1/1 / UTF-8 302 bytes

~~~c

/* firebase::util::float_class::GetMethodId(firebase::util::float_class::Method) */

undefined8 firebase::util::float_class::GetMethodId(uint param_1)

{
  if (1 < (int)param_1) {
    LogAssert("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_010a0738 + (ulong)param_1 * 8);
}

~~~
