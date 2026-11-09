# 00bcbff8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcbff8",
  "name": "_ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09fc2edf170cb9ebfe3d4bbeab9a0dc740f8b6044d7fbe427f59bf64f050789b",
  "source_text_sha256": "09fc2edf170cb9ebfe3d4bbeab9a0dc740f8b6044d7fbe427f59bf64f050789b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab60](../00c5a/00c5ab60.md)

## 疑似コード / UTF-8 566 bytes

~~~c

bool _ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126330 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126328,param_2,param_3);
                    /* catch() { ... } // from try @ 00bcc220 with catch @ 00bcc044 */
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126330 = iVar2 == 0;
    bVar1 = (bool)DAT_01126330;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
