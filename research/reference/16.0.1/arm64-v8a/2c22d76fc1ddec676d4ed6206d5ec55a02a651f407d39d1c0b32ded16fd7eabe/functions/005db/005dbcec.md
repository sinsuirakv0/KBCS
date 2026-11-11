# 005dbcec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "005dbcec",
  "name": "FUN_005dbcec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "194dc71369456fa3dbbfab68809a1a4e4f3b1ab6df6e09558d5b1df13f8736ab",
  "source_text_sha256": "194dc71369456fa3dbbfab68809a1a4e4f3b1ab6df6e09558d5b1df13f8736ab"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 567 bytes

~~~c

long FUN_005dbcec(long param_1,long param_2)

{
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dbcb8 with catch @ 005dbcf0
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dbc8c with catch @ 005dbcf4
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dbc60 with catch @ 005dbcf8
                        */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN12AwakenWindow4openEiE3$_4") {
    param_1 = 0;
  }
  return param_1;
}

~~~
