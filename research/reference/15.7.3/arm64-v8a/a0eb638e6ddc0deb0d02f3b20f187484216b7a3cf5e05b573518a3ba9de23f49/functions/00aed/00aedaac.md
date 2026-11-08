# 00aedaac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aedaac",
  "name": "_ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9dc6dba353c9f347ac5eb28ad9dbb14c76acf2241b8a658251c7799d756b1738",
  "source_text_sha256": "9dc6dba353c9f347ac5eb28ad9dbb14c76acf2241b8a658251c7799d756b1738"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)
- [00bde060](../00bde/00bde060.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Throwable"
~~~

## 疑似コード / UTF-8 835 bytes

~~~c

void _ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aedab4 to 00bedaef has its CatchHandler @ 00af1ad8 */
  if (DAT_010a09f0 == 0) {
    DAT_010a09f0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Throwable",0);
  }
                    /* try { // try from 00aedaf0 to 00beed27 has its CatchHandler @ 00aeadc8 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a09f0,&PTR_s_getLocalizedMessage_00c105a8,3,&DAT_010a0a00,
             "java/lang/Throwable");
  return;
}

~~~
