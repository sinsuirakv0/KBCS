# 00aadbc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aadbc0.md)

## 関数情報

~~~json
{
  "address": "00aadbc0",
  "name": "FUN_00aadbc0",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a292c753d9fb45ae3ea2e2326926dc51444d36d59a9e5a426423d111836158e4",
  "source_text_sha256": "a292c753d9fb45ae3ea2e2326926dc51444d36d59a9e5a426423d111836158e4"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 290 bytes

~~~c

long FUN_00aadbc0(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZN19UraStageTeamManager14showResetPopupEP21CachingTextureContextPNSt6__ndk15arrayINS2_10shared_ptrI8aTextureEELm10EEEiE3$_4"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
