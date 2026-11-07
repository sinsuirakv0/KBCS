# 00aedff8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00aee104`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee104.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00aedff8",
  "name": "_ZN8firebase4util6object15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96cfc0c2bcb8230e463b5528a61d87a77282c32e2030e125537f1d46ce872f03",
  "source_text_sha256": "96cfc0c2bcb8230e463b5528a61d87a77282c32e2030e125537f1d46ce872f03"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 604 bytes

~~~c

bool _ZN8firebase4util6object15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a0990 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0988,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a0990 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0990;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~
