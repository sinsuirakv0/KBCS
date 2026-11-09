# 00bb8fdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bb8fdc",
  "name": "_ZN8firebase9messaging26illegal_argument_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90f248f19b20b70e1d29361fb1fd9b7f3113da3b1f7b36329b0f8a868d9c8682",
  "source_text_sha256": "90f248f19b20b70e1d29361fb1fd9b7f3113da3b1f7b36329b0f8a868d9c8682"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab60](../00c5a/00c5ab60.md)

## 疑似コード / UTF-8 701 bytes

~~~c

bool _ZN8firebase9messaging26illegal_argument_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01125f40 == '\0') {
                    /* try { // try from 00bb9010 to 00cb9017 has its CatchHandler @ 00bb9060 */
                    /* try { // try from 00bb9018 to 00cb9057 has its CatchHandler @ 00bb8fbc */
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01125f38,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01125f40 = iVar2 == 0;
    bVar1 = (bool)DAT_01125f40;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
