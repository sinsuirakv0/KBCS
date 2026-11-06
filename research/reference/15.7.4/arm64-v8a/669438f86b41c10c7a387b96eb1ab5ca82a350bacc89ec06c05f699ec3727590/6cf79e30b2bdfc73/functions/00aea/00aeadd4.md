# 00aeadd4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aeadd4.md)

## 関数情報

~~~json
{
  "address": "00aeadd4",
  "name": "_ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1af9bcab096413634acc8f5ead41b0ddd62ca47a8c4e6383acbcba6ac97f7d1",
  "source_text_sha256": "e1af9bcab096413634acc8f5ead41b0ddd62ca47a8c4e6383acbcba6ac97f7d1"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 2215 bytes

~~~c

bool _ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a0858 == '\0') {
                    /* try { // try from 00aeae0c to 00beb20f has its CatchHandler @ 00aeae0c
                       catch() { ... } // from try @ 00aeae0c with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeb3e8 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeb554 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aebac8 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aec180 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aec4d8 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeca18 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeca9c with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aecd6c with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aedb34 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeed74 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aef3fc with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aef710 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aef7e0 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1090 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1410 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1510 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1644 with catch @ 00aeae0c */
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0850,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a0858 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0858;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~
