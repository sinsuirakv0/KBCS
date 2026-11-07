# 00a3abdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00a3ab98`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a3a/00a3ab98.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00a3abdc",
  "name": "FUN_00a3abdc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acbd49b3ecd1e55ea0cd89624ee4aa6982e74f7033c202c6aadf03ec8f3dca1b",
  "source_text_sha256": "acbd49b3ecd1e55ea0cd89624ee4aa6982e74f7033c202c6aadf03ec8f3dca1b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 270 bytes

~~~c

long FUN_00a3abdc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication9TitleinitEvENK3$_0clEP9NewButton20NewButtonChangeStateEUlN13aGameServices6StatusEE0_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
