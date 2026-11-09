# 00bd7fec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bd7fec",
  "name": "_ZN8firebase4auth15phonecredential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae01b625eb14b93ea6e2881227be1a537f19a53a626b7efeed06d121db07d9f7",
  "source_text_sha256": "ae01b625eb14b93ea6e2881227be1a537f19a53a626b7efeed06d121db07d9f7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab60](../00c5a/00c5ab60.md)

## 疑似コード / UTF-8 588 bytes

~~~c

bool _ZN8firebase4auth15phonecredential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_011268e0 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_011268d8,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_011268e0 = iVar2 == 0;
    bVar1 = (bool)DAT_011268e0;
  }
  else {
    bVar1 = false;
  }
                    /* try { // try from 00bd8054 to 00cd806f has its CatchHandler @ 00bdee40 */
  return bVar1;
}

~~~
