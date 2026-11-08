# 00b4addc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b4addc",
  "name": "_ZN8firebase9messaging18firebase_messaging10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "617e11ee129ef3cbe019445429ef8eab1a2b38cfa52df31df2faf5ed64f98a89",
  "source_text_sha256": "617e11ee129ef3cbe019445429ef8eab1a2b38cfa52df31df2faf5ed64f98a89"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

## 疑似コード / UTF-8 538 bytes

~~~c

undefined8 _ZN8firebase9messaging18firebase_messaging10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
                    /* try { // try from 00b4adf8 to 00c4ae03 has its CatchHandler @ 00b4ae98 */
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
                    /* try { // try from 00b4ae04 to 00c4ae0f has its CatchHandler @ 00b4ae94 */
                    /* try { // try from 00b4ae10 to 00c4ae3f has its CatchHandler @ 00b4aed8 */
  return *(undefined8 *)(&DAT_010a1010 + (ulong)param_1 * 8);
}

~~~
