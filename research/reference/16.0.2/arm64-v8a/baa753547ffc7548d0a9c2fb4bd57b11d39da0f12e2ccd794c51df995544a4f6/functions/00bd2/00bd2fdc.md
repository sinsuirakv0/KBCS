# 00bd2fdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bd2fdc",
  "name": "_ZN8firebase4auth26firebase_network_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d80b7c224b0ab5161f7996b41271e1df56a72781815525e0222a447029b1bfa",
  "source_text_sha256": "1d80b7c224b0ab5161f7996b41271e1df56a72781815525e0222a447029b1bfa"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

## 疑似コード / UTF-8 502 bytes

~~~c

bool _ZN8firebase4auth26firebase_network_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126af0 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126ae8,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126af0 = iVar2 == 0;
    bVar1 = (bool)DAT_01126af0;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
