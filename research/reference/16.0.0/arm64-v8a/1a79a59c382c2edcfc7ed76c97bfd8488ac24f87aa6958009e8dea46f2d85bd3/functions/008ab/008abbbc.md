# 008abbbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "008abbbc",
  "name": "FUN_008abbbc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fff10a3c9e61a8d532172239213c079cc2119c1df35aa03e1ce5a7846abad954",
  "source_text_sha256": "fff10a3c9e61a8d532172239213c079cc2119c1df35aa03e1ce5a7846abad954"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 461 bytes

~~~c

long FUN_008abbbc(long param_1,long param_2)

{
                    /* catch() { ... } // from try @ 008ab770 with catch @ 008abbc4 */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZN17MyUtilityListener22miniBrowserLinkClickedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEE3$_2"
     ) {
    param_1 = 0;
  }
                    /* catch() { ... } // from try @ 008ab758 with catch @ 008abbd4 */
  return param_1;
}

~~~
