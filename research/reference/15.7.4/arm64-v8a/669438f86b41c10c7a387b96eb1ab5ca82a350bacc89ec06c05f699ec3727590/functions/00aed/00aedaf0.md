# 00aedaf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00aedaf0",
  "name": "_ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "67122c64638a5a3f5c6424c9d82bee4bf089939e8491e4ad36773d7eb62bad83",
  "source_text_sha256": "67122c64638a5a3f5c6424c9d82bee4bf089939e8491e4ad36773d7eb62bad83"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)
- [00bde0b0](../00bde/00bde0b0.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Throwable"
~~~

## 疑似コード / UTF-8 835 bytes

~~~c

void _ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aedaf8 to 00bedb33 has its CatchHandler @ 00af1b1c */
  if (DAT_010a0a30 == 0) {
    DAT_010a0a30 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Throwable",0);
  }
                    /* try { // try from 00aedb34 to 00beed6b has its CatchHandler @ 00aeae0c */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0a30,&PTR_s_getLocalizedMessage_00c105f8,3,&DAT_010a0a40,
             "java/lang/Throwable");
  return;
}

~~~
