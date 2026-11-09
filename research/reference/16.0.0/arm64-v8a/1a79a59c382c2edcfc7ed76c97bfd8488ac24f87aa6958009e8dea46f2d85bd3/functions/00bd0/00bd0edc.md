# 00bd0edc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bd0edc",
  "name": "_ZN8firebase4auth21action_code_exception11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "adb32034c646a00fa3042de0d8c1c00403c42f98c8198c1edd011e5b23c571ab",
  "source_text_sha256": "adb32034c646a00fa3042de0d8c1c00403c42f98c8198c1edd011e5b23c571ab"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ac00](../00c5a/00c5ac00.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 443 bytes

~~~c

undefined8 _ZN8firebase4auth21action_code_exception11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
                    /* try { // try from 00bd0f08 to 00cd0f0f has its CatchHandler @ 00bd6544 */
                    /* try { // try from 00bd0f14 to 00cd0f2b has its CatchHandler @ 00bd653c */
  return *(undefined8 *)(&DAT_011264d8 + (ulong)param_1 * 8);
}

~~~
