# 00b5cdfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b5cdfc",
  "name": "_ZN8firebase4auth17signinmethodquery15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bfa374a5f8e394be7344b3f1f59b721425b88cbf1f702ddc062c9cd9bbcb27cc",
  "source_text_sha256": "bfa374a5f8e394be7344b3f1f59b721425b88cbf1f702ddc062c9cd9bbcb27cc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 疑似コード / UTF-8 493 bytes

~~~c

bool _ZN8firebase4auth17signinmethodquery15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_010a1490 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a1488,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_010a1490 = iVar2 == 0;
    bVar1 = (bool)DAT_010a1490;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
