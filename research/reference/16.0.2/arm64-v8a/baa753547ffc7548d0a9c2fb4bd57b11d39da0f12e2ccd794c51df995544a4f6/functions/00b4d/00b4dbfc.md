# 00b4dbfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00b4dbfc",
  "name": "_ZN8firebase4util9throwable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cd1c26f13a137cf35f6cc4f554757dc258c11bd53d07aa42d589d32e2129dd00",
  "source_text_sha256": "cd1c26f13a137cf35f6cc4f554757dc258c11bd53d07aa42d589d32e2129dd00"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 607 bytes

~~~c

bool _ZN8firebase4util9throwable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_01125df8 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01125df0,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_01125df8 = iVar3 == 0;
    bVar2 = (bool)DAT_01125df8;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~
