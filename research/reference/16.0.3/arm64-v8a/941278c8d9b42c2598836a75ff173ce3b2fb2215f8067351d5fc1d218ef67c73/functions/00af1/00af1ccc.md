# 00af1ccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af1ccc",
  "name": "FUN_00af1ccc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "62066d4b0ea66d568342c2c93b1e7d12819b24e7528588787a950bf695ac144a",
  "source_text_sha256": "62066d4b0ea66d568342c2c93b1e7d12819b24e7528588787a950bf695ac144a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 521 bytes

~~~c

long FUN_00af1ccc(long param_1,long param_2)

{
                    /* catch() { ... } // from try @ 00af18a0 with catch @ 00af1ccc
                       catch() { ... } // from try @ 00af19d8 with catch @ 00af1ccc */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication18UnitAdoptionUpdateEvENK3$_1clEP9NewDialog20NewDialogChangeStateiEUlS2_S3_iE_"
     ) {
    param_1 = 0;
  }
                    /* catch() { ... } // from try @ 00af170c with catch @ 00af1ce4 */
  return param_1;
}

~~~
