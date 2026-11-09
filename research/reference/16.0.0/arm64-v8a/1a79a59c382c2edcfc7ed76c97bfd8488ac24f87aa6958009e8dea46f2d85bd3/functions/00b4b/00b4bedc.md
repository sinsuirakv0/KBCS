# 00b4bedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b4bedc",
  "name": "_ZN8firebase4util4list14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6530cd43ebe874895d0c0608c92eaf0d60aae4f0def602b254beb1060f3adcc2",
  "source_text_sha256": "6530cd43ebe874895d0c0608c92eaf0d60aae4f0def602b254beb1060f3adcc2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)
- [00c5ab30](../00c5a/00c5ab30.md)

## 関連文字列（未確認候補）

~~~text
"java/util/List"
~~~

## 疑似コード / UTF-8 594 bytes

~~~c

void _ZN8firebase4util4list14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011257e0 == 0) {
    DAT_011257e0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/List",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_011257e0,&PTR_DAT_00c8fbe0,3,&DAT_011257f0,"java/util/List");
  return;
}

~~~
