# 00b6fcbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00b6fcbc",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo11provider_idEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bf903f4b9183506ada4d07c99f7710de6de8606709ac6038bac385575aabd7d8",
  "source_text_sha256": "bf903f4b9183506ada4d07c99f7710de6de8606709ac6038bac385575aabd7d8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bde0e0](../00bde/00bde0e0.md)
- [00bde200](../00bde/00bde200.md)
- [00bde510](../00bde/00bde510.md)

## 疑似コード / UTF-8 942 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo11provider_idEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
                    /* try { // try from 00b6fcd8 to 00c6fcf7 has its CatchHandler @ 00b70738 */
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_0047495c(uVar2,lVar1,DAT_010a1ac0);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
                    /* try { // try from 00b6fd04 to 00c6fd23 has its CatchHandler @ 00b70728 */
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
                    /* try { // try from 00b6fd24 to 00c6fdb7 has its CatchHandler @ 00b6e440 */
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~
