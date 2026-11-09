# 005dbcac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "005dbcac",
  "name": "FUN_005dbcac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4ea86570f86046cf188b04d3f8f892da41379bacaeef8ee0a8bbe4e9c4bf566f",
  "source_text_sha256": "4ea86570f86046cf188b04d3f8f892da41379bacaeef8ee0a8bbe4e9c4bf566f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 567 bytes

~~~c

long FUN_005dbcac(long param_1,long param_2)

{
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dbc78 with catch @ 005dbcb0
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dbc4c with catch @ 005dbcb4
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dbc20 with catch @ 005dbcb8
                        */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN12AwakenWindow4openEiE3$_4") {
    param_1 = 0;
  }
  return param_1;
}

~~~
