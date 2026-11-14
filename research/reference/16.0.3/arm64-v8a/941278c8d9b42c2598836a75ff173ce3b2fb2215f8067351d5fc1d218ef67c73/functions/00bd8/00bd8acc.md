# 00bd8acc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bd8acc",
  "name": "_ZN8firebase4auth8auth_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cda1ef5c59ba9594ebeb7b1a504f10e0084dc6427945281d6b7e048261d64692",
  "source_text_sha256": "cda1ef5c59ba9594ebeb7b1a504f10e0084dc6427945281d6b7e048261d64692"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

## 疑似コード / UTF-8 483 bytes

~~~c

bool _ZN8firebase4auth8auth_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01127d30 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01127d28,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01127d30 = iVar2 == 0;
    bVar1 = (bool)DAT_01127d30;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
