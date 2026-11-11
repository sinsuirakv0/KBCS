# 00bcc4fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bcc4fc",
  "name": "_ZN8firebase4auth4auth14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4fae8c1e5e1801db08dc45383f23bed12faeec42f2d7dd68f35ec916acea1b5f",
  "source_text_sha256": "4fae8c1e5e1801db08dc45383f23bed12faeec42f2d7dd68f35ec916acea1b5f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af10](../00c5a/00c5af10.md)
- [00c5af30](../00c5a/00c5af30.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuth"
~~~

## 疑似コード / UTF-8 754 bytes

~~~c

void _ZN8firebase4auth4auth14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* catch() { ... } // from try @ 00bcc394 with catch @ 00bcc500 */
  if (DAT_01126728 == 0) {
    DAT_01126728 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseAuth",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126728,&PTR_s_getInstance_00c91988,0x12,&DAT_01126738,
             "com/google/firebase/auth/FirebaseAuth");
  return;
}

~~~
