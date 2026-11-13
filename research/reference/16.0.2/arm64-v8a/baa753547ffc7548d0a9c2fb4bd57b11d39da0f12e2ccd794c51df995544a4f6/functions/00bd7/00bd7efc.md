# 00bd7efc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bd7efc",
  "name": "_ZN8firebase4auth8user_idp14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5732cdf6db028b8788506c593a25af6108ced58ba12838d7c1cf0f95695311f4",
  "source_text_sha256": "5732cdf6db028b8788506c593a25af6108ced58ba12838d7c1cf0f95695311f4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)
- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUser"
~~~

## 疑似コード / UTF-8 689 bytes

~~~c

void _ZN8firebase4auth8user_idp14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126d88 == 0) {
    DAT_01126d88 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUser",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126d88,&PTR_s_startActivityForLinkWithProvider_00c92528,2,&DAT_01126d98,
             "com/google/firebase/auth/FirebaseUser");
  return;
}

~~~
