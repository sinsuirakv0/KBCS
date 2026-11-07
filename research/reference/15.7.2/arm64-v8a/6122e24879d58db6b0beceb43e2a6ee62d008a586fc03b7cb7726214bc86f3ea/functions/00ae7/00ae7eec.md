# 00ae7eec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00ae7ff8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00ae7eec",
  "name": "_ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23a6603c785c41e1b684fe1e4b364388603a87eedf689257b3e7d1b430f698c1",
  "source_text_sha256": "23a6603c785c41e1b684fe1e4b364388603a87eedf689257b3e7d1b430f698c1"
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

## 疑似コード / UTF-8 408 bytes

~~~c

undefined8 _ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
                    /* try { // try from 00ae7f0c to 00be7f17 has its CatchHandler @ 00ae8974 */
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
                    /* try { // try from 00ae7f18 to 00be7f2b has its CatchHandler @ 00ae896c */
  return (&DAT_010a04d0)[param_1];
}

~~~
