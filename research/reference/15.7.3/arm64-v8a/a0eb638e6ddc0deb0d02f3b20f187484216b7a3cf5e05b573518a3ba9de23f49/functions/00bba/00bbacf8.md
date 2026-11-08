# 00bbacf8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbacf8",
  "name": "_ZNSt9exceptionD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "91ebc617da88d03cd05fa623b4417b5d8a5fbeb1a1f78db9997d5a879008e22a",
  "source_text_sha256": "91ebc617da88d03cd05fa623b4417b5d8a5fbeb1a1f78db9997d5a879008e22a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00be1df0](../00be1/00be1df0.md)

## 疑似コード / UTF-8 1487 bytes

~~~c

void _ZNSt9exceptionD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bb39c4 with catch @ 00bbacfc */
                    /* catch() { ... } // from try @ 00bb41c0 with catch @ 00bbad00 */
                    /* catch() { ... } // from try @ 00bb3dd4 with catch @ 00bbad04 */
                    /* catch() { ... } // from try @ 00bb39b4 with catch @ 00bbad08 */
                    /* catch() { ... } // from try @ 00bba298 with catch @ 00bbad0c
                       catch() { ... } // from try @ 00bba3e8 with catch @ 00bbad0c */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bba280 with catch @ 00bbad10
                       catch() { ... } // from try @ 00bba3d0 with catch @ 00bbad10 */
                    /* catch() { ... } // from try @ 00bba268 with catch @ 00bbad14
                       catch() { ... } // from try @ 00bba3b8 with catch @ 00bbad14 */
                    /* catch() { ... } // from try @ 00bba250 with catch @ 00bbad18
                       catch() { ... } // from try @ 00bba3a0 with catch @ 00bbad18 */
                    /* catch() { ... } // from try @ 00bba238 with catch @ 00bbad1c
                       catch() { ... } // from try @ 00bba388 with catch @ 00bbad1c */
                    /* catch() { ... } // from try @ 00bba220 with catch @ 00bbad20
                       catch() { ... } // from try @ 00bba370 with catch @ 00bbad20 */
  _ZdlPv(param_1);
  return;
}

~~~
