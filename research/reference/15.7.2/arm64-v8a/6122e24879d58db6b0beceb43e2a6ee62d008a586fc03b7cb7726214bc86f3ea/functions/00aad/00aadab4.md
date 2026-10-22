# 00aadab4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aadab4.md)

## 関数情報

~~~json
{
  "address": "00aadab4",
  "name": "FUN_00aadab4",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ec2adf5e83ec102b776eb3675bea97c100ee35a976e4ca15fad9ed20c4fdc92a",
  "source_text_sha256": "ec2adf5e83ec102b776eb3675bea97c100ee35a976e4ca15fad9ed20c4fdc92a"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 303 bytes

~~~c

long FUN_00aadab4(long param_1,long param_2)

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
