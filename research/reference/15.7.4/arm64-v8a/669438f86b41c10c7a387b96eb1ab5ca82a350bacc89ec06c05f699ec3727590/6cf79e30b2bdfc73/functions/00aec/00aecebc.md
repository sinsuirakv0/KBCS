# 00aecebc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aecebc.md)

## 関数情報

~~~json
{
  "address": "00aecebc",
  "name": "_ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cb9ff65685b002cdab8e26cce7fcd5907d475536eeee6efbb95b98d1a69c4b93",
  "source_text_sha256": "cb9ff65685b002cdab8e26cce7fcd5907d475536eeee6efbb95b98d1a69c4b93"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 601 bytes

~~~c

bool _ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a09d0 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a09c8,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a09d0 = iVar3 == 0;
    bVar2 = (bool)DAT_010a09d0;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~
