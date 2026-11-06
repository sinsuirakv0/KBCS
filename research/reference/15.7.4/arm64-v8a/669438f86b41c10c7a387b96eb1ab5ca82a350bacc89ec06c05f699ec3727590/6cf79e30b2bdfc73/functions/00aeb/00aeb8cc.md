# 00aeb8cc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aeb8cc.md)

## 関数情報

~~~json
{
  "address": "00aeb8cc",
  "name": "_ZN8firebase4util8iterable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dd3014b2534baed86d377b1f12d344e98597ba94d41b84e021772871e82af117",
  "source_text_sha256": "dd3014b2534baed86d377b1f12d344e98597ba94d41b84e021772871e82af117"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 800 bytes

~~~c

bool _ZN8firebase4util8iterable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a08e0 == '\0') {
                    /* try { // try from 00aeb90c to 00beb913 has its CatchHandler @ 00af1928 */
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a08d8,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a08e0 = iVar3 == 0;
    bVar2 = (bool)DAT_010a08e0;
  }
  else {
    bVar2 = false;
  }
                    /* try { // try from 00aeb958 to 00beb96f has its CatchHandler @ 00af1924 */
  return bVar2;
}

~~~
