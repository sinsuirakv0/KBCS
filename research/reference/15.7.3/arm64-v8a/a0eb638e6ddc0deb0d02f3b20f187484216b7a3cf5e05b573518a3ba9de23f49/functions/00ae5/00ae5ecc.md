# 00ae5ecc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ae5ecc",
  "name": "_ZN8firebase4util3log11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8ba03516ad9d6dbcdc977be0b8b9ffae727d0368ed20af6d13dcaad057d7695f",
  "source_text_sha256": "8ba03516ad9d6dbcdc977be0b8b9ffae727d0368ed20af6d13dcaad057d7695f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 910 bytes

~~~c

undefined8 _ZN8firebase4util3log11GetMethodIdENS1_6MethodE(uint param_1)

{
                    /* try { // try from 00ae5edc to 00be5ee3 has its CatchHandler @ 00ae5ee4 */
  if (0 < (int)param_1) {
                    /* catch() { ... } // from try @ 00ae5de4 with catch @ 00ae5ee4
                       catch() { ... } // from try @ 00ae5edc with catch @ 00ae5ee4
                       try { // try from 00ae5ee4 to 00be5f1f has its CatchHandler @ 00ae596c */
                    /* catch() { ... } // from try @ 00ae5cfc with catch @ 00ae5ee8
                       catch() { ... } // from try @ 00ae5e58 with catch @ 00ae5ee8 */
                    /* catch() { ... } // from try @ 00ae5c64 with catch @ 00ae5eec */
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
                    /* catch() { ... } // from try @ 00ae5bfc with catch @ 00ae5ef0 */
  return (&DAT_010a03e8)[param_1];
}

~~~
