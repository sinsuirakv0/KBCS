# 00bccb4c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bccb4c",
  "name": "_ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "89c1f15a3bc5327998a91403afd28a235f499703c10957f0b9804dda01181a65",
  "source_text_sha256": "89c1f15a3bc5327998a91403afd28a235f499703c10957f0b9804dda01181a65"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

## 疑似コード / UTF-8 681 bytes

~~~c

bool _ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
                    /* try { // try from 00bccb60 to 00cccb77 has its CatchHandler @ 00bce978 */
  if (DAT_011268f8 == '\0') {
                    /* try { // try from 00bccb78 to 00cccc2b has its CatchHandler @ 00bcc640 */
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_011268f0,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_011268f8 = iVar2 == 0;
    bVar1 = (bool)DAT_011268f8;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
