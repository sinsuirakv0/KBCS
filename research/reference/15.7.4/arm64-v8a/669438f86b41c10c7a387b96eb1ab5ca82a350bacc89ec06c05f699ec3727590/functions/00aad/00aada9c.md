# 00aada9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00aada9c",
  "name": "FUN_00aada9c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6ed2702a891e3127ef5a0f8155df7741cf29519810e14d79234ed6b33c9f2ce",
  "source_text_sha256": "d6ed2702a891e3127ef5a0f8155df7741cf29519810e14d79234ed6b33c9f2ce"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 290 bytes

~~~c

long FUN_00aada9c(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZN19UraStageTeamManager14showResetPopupEP21CachingTextureContextPNSt6__ndk15arrayINS2_10shared_ptrI8aTextureEELm10EEEiE3$_3"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
