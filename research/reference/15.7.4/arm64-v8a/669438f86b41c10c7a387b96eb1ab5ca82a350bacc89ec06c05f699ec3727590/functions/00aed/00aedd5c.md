# 00aedd5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00aedd5c",
  "name": "_ZN8firebase4util3uri15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "764123b9d7436e6f8292e1f369d2ea3c482ea8747a1995e727d901313a9b4316",
  "source_text_sha256": "764123b9d7436e6f8292e1f369d2ea3c482ea8747a1995e727d901313a9b4316"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 601 bytes

~~~c

bool _ZN8firebase4util3uri15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a0a68 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0a60,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a0a68 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0a68;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~
