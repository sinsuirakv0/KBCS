# 00ae8cec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00ae8cec",
  "name": "_ZN8firebase4util11class_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42bf2ab47f908db1f4662a80212e5e865e0516931f5788c3868db17a1533c17d",
  "source_text_sha256": "42bf2ab47f908db1f4662a80212e5e865e0516931f5788c3868db17a1533c17d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1477 bytes

~~~c

bool _ZN8firebase4util11class_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
                    /* catch() { ... } // from try @ 00ae7568 with catch @ 00ae8cec */
                    /* catch() { ... } // from try @ 00ae753c with catch @ 00ae8d04 */
  if (DAT_010a06a0 == '\0') {
                    /* catch() { ... } // from try @ 00ae7528 with catch @ 00ae8d1c */
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0698,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
                    /* catch() { ... } // from try @ 00ae7518 with catch @ 00ae8d4c */
      (**(code **)(*param_1 + 0x80))(param_1);
                    /* catch() { ... } // from try @ 00ae74e0 with catch @ 00ae8d60 */
                    /* catch() { ... } // from try @ 00ae7944 with catch @ 00ae8d64 */
                    /* catch() { ... } // from try @ 00ae7020 with catch @ 00ae8d68 */
      (**(code **)(*param_1 + 0x88))(param_1);
    }
                    /* catch() { ... } // from try @ 00ae6084 with catch @ 00ae8d6c */
    DAT_010a06a0 = iVar3 == 0;
                    /* catch() { ... } // from try @ 00ae8148 with catch @ 00ae8d70
                       catch() { ... } // from try @ 00ae86ac with catch @ 00ae8d70 */
    bVar2 = (bool)DAT_010a06a0;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~
