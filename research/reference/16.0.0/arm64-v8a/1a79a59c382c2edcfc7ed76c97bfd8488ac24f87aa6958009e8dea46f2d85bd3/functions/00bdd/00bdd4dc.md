# 00bdd4dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bdd4dc",
  "name": "_ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6911f5cadc3071c1559ccedb4c755df82aeda7b2e850ec864036afd768ac1d34",
  "source_text_sha256": "6911f5cadc3071c1559ccedb4c755df82aeda7b2e850ec864036afd768ac1d34"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab60](../00c5a/00c5ab60.md)

## 疑似コード / UTF-8 774 bytes

~~~c

bool _ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
                    /* try { // try from 00bdd4f4 to 00cdd4ff has its CatchHandler @ 00bde990 */
  if (DAT_01126a08 == '\0') {
                    /* try { // try from 00bdd514 to 00cdd53f has its CatchHandler @ 00bde9b0 */
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126a00,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126a08 = iVar2 == 0;
    bVar1 = (bool)DAT_01126a08;
  }
  else {
    bVar1 = false;
  }
                    /* try { // try from 00bdd540 to 00cdd723 has its CatchHandler @ 00bd6d50 */
  return bVar1;
}

~~~
