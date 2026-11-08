# 00bbadc4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbadc4",
  "name": "_ZNSt20bad_array_new_lengthC1Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2bac531cebebd1cf0e356b9e453096abcd1b39821155444c9ba12c69b4ba796",
  "source_text_sha256": "b2bac531cebebd1cf0e356b9e453096abcd1b39821155444c9ba12c69b4ba796"
}
~~~

## 呼び出し元

- [00bdb190](../00bdb/00bdb190.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 575 bytes

~~~c

void _ZNSt20bad_array_new_lengthC1Ev(long *param_1)

{
                    /* catch() { ... } // from try @ 00bb4d50 with catch @ 00bbadc8 */
                    /* catch() { ... } // from try @ 00bb4d68 with catch @ 00bbadcc */
                    /* catch() { ... } // from try @ 00bb4988 with catch @ 00bbadd0 */
                    /* catch() { ... } // from try @ 00bb4970 with catch @ 00bbadd4 */
  *param_1 = (long)(PTR__ZTVSt20bad_array_new_length_00c1bfd0 + 0x10);
                    /* catch() { ... } // from try @ 00bb45c8 with catch @ 00bbadd8 */
  return;
}

~~~
