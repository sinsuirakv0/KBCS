# 00ae7eec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae7eec.md)

## 関数情報

~~~json
{
  "address": "00ae7eec",
  "name": "firebase::util::boolean_class::GetMethodId",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29847dfd037a892c8f90e45df32baeb293036a6d4225494552779ac9190b624f",
  "source_text_sha256": "29847dfd037a892c8f90e45df32baeb293036a6d4225494552779ac9190b624f"
}
~~~
## 呼び出し元

- [00bde340](../00bde/00bde340.md)

## 呼び出し先

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~
## 疑似コード 1/1 / UTF-8 477 bytes

~~~c

/* firebase::util::boolean_class::GetMethodId(firebase::util::boolean_class::Method) */

undefined8 firebase::util::boolean_class::GetMethodId(uint param_1)

{
  if (1 < (int)param_1) {
                    /* try { // try from 00ae7f0c to 00be7f17 has its CatchHandler @ 00ae8974 */
    LogAssert("method < kMethodCount");
  }
                    /* try { // try from 00ae7f18 to 00be7f2b has its CatchHandler @ 00ae896c */
  return (&DAT_010a04d0)[param_1];
}

~~~
