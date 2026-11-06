# 00ae6fdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00ae6fdc",
  "name": "_ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cf0b71d6b167d4403c1ab6efd90586c8ae60185281a3b6fb61665b4c60d52cbf",
  "source_text_sha256": "cf0b71d6b167d4403c1ab6efd90586c8ae60185281a3b6fb61665b4c60d52cbf"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"android/content/res/Resources"
~~~

## 疑似コード / UTF-8 849 bytes

~~~c

void _ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00ae6fdc to 00be6fdf has its CatchHandler @ 00ae8d24 */
                    /* try { // try from 00ae6fe0 to 00be7083 has its CatchHandler @ 00ae6000 */
  if (DAT_010a03e8 == 0) {
    DAT_010a03e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/content/res/Resources",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a03e8,&PTR_s_getIdentifier_00c0fd48,1,&DAT_010a03f8,
             "android/content/res/Resources");
  return;
}

~~~
