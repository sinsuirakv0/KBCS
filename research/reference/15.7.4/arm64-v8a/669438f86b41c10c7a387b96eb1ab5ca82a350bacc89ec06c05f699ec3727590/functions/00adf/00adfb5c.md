# 00adfb5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00adfb5c",
  "name": "FUN_00adfb5c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "835a7f8edb69d015993de506e4cbcb19719c3e02df64499a14abaaeebcb52e2b",
  "source_text_sha256": "835a7f8edb69d015993de506e4cbcb19719c3e02df64499a14abaaeebcb52e2b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 294 bytes

~~~c

long FUN_00adfb5c(long param_1,long param_2)

{
                    /* try { // try from 00adfb64 to 00bdfb67 has its CatchHandler @ 00adfc74 */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN18unlockPopupManager11createPopupEvE3$_0") {
    param_1 = 0;
  }
  return param_1;
}

~~~
