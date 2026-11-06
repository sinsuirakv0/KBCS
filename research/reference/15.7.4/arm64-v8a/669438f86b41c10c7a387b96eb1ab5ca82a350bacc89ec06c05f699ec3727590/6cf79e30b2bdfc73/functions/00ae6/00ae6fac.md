# 00ae6fac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00ae6fac.md)

## 関数情報

~~~json
{
  "address": "00ae6fac",
  "name": "_ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "942644bd3e96fa64710246de7fc5f309463c2e47af2b52f43fe2a1950af7e8ac",
  "source_text_sha256": "942644bd3e96fa64710246de7fc5f309463c2e47af2b52f43fe2a1950af7e8ac"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 801 bytes

~~~c

bool _ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a04f0 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a04e8,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
                    /* try { // try from 00ae7020 to 00be7023 has its CatchHandler @ 00ae8d68 */
                    /* try { // try from 00ae7024 to 00be70c7 has its CatchHandler @ 00ae6044 */
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a04f0 = iVar3 == 0;
    bVar2 = (bool)DAT_010a04f0;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~
