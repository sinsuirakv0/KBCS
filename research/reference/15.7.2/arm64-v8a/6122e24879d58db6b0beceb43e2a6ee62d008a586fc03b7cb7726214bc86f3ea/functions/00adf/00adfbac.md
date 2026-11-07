# 00adfbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00adfcb8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfcb8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00adfbac",
  "name": "FUN_00adfbac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23cdef6424e143af69b1e2a4b86df7bc3ae4aeb962b033213dedaa2abfe5dd14",
  "source_text_sha256": "23cdef6424e143af69b1e2a4b86df7bc3ae4aeb962b033213dedaa2abfe5dd14"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 294 bytes

~~~c

long FUN_00adfbac(long param_1,long param_2)

{
  param_1 = param_1 + 8;
                    /* try { // try from 00adfbc0 to 00bdfbdf has its CatchHandler @ 00adfbfc */
  if (*(char **)(param_2 + 8) != "ZN18unlockPopupManager11createPopupEvE3$_1") {
    param_1 = 0;
  }
  return param_1;
}

~~~
