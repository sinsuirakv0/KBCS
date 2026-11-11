# 00bc3abc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bc3abc",
  "name": "_ZN8firebase13remote_config8internal35config_update_listener_registration14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4dab0648d48a4e9c9ada7ba5a9196b36c0574bca530ebee72745f8547b2219b0",
  "source_text_sha256": "4dab0648d48a4e9c9ada7ba5a9196b36c0574bca530ebee72745f8547b2219b0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af10](../00c5a/00c5af10.md)
- [00c5af30](../00c5a/00c5af30.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration"
~~~

## 疑似コード / UTF-8 899 bytes

~~~c

void _ZN8firebase13remote_config8internal35config_update_listener_registration14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bc3acc to 00cc3c7f has its CatchHandler @ 00bc38f0 */
  if (DAT_01126698 == 0) {
    DAT_01126698 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration",0)
    ;
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126698,&PTR_s_remove_00c917d0,1,&DAT_011266a8,
             "com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration");
  return;
}

~~~
