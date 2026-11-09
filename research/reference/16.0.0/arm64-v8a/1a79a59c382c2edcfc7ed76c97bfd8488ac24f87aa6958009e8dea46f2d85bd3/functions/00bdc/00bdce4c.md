# 00bdce4c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bdce4c",
  "name": "_ZN8firebase4auth4user15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5a78789154684e0098376f9657a5bb05d44fc0ff39534db2ea56051dfcbb46e5",
  "source_text_sha256": "5a78789154684e0098376f9657a5bb05d44fc0ff39534db2ea56051dfcbb46e5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab60](../00c5a/00c5ab60.md)

## 疑似コード / UTF-8 479 bytes

~~~c

bool _ZN8firebase4auth4user15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126928 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126920,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126928 = iVar2 == 0;
    bVar1 = (bool)DAT_01126928;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
