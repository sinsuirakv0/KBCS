# 00ae8aac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ae8aac",
  "name": "_ZN8firebase4util15character_class11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc824f59f2133c781e728e1ec8531d1d2e82007ebb40524591ee1f4553040800",
  "source_text_sha256": "dc824f59f2133c781e728e1ec8531d1d2e82007ebb40524591ee1f4553040800"
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

## 疑似コード / UTF-8 417 bytes

~~~c

undefined8 _ZN8firebase4util15character_class11GetMethodIdENS1_6MethodE(uint param_1)

{
                    /* catch() { ... } // from try @ 00ae63f4 with catch @ 00ae8ab0 */
                    /* catch() { ... } // from try @ 00ae6bbc with catch @ 00ae8ab4 */
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_010a0640 + (ulong)param_1 * 8);
}

~~~
