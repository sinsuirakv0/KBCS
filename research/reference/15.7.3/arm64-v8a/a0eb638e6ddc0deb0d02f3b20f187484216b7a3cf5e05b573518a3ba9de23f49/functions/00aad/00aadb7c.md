# 00aadb7c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aadb7c",
  "name": "FUN_00aadb7c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "14c91a5ef8417b8564d627cec5f7b46ee51c574b3dd151d7c07760f7be6cf4d6",
  "source_text_sha256": "14c91a5ef8417b8564d627cec5f7b46ee51c574b3dd151d7c07760f7be6cf4d6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 290 bytes

~~~c

long FUN_00aadb7c(long param_1,long param_2)

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
