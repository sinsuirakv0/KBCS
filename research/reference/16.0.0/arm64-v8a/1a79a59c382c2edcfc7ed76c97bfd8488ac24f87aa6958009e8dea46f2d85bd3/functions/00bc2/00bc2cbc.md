# 00bc2cbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bc2cbc",
  "name": "_ZN8firebase13remote_config8internal19throttled_exception14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ec068a24b5446fa88ec61216871c37703b9fa293f2fd5d4d40f459bfc9cfab4",
  "source_text_sha256": "9ec068a24b5446fa88ec61216871c37703b9fa293f2fd5d4d40f459bfc9cfab4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)
- [00c5ab30](../00c5a/00c5ab30.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException"
~~~

## 疑似コード / UTF-8 1113 bytes

~~~c

void _ZN8firebase13remote_config8internal19throttled_exception14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126238 == 0) {
    DAT_01126238 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException"
                              ,0);
  }
                    /* catch() { ... } // from try @ 00bc299c with catch @ 00bc2d20 */
                    /* catch() { ... } // from try @ 00bc2890 with catch @ 00bc2d24 */
                    /* catch() { ... } // from try @ 00bc275c with catch @ 00bc2d28 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126238,&PTR_s_getThrottleEndTimeMillis_00c91388,1,&DAT_01126248,
             "com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException");
  return;
}

~~~
