# 00bb8efc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bb8efc",
  "name": "_ZN8firebase9messaging18firebase_messaging13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c14bc2e1e6cf56065e229b72954431c98005b5b3ae1aa1ec2d0a36262e0d88d3",
  "source_text_sha256": "c14bc2e1e6cf56065e229b72954431c98005b5b3ae1aa1ec2d0a36262e0d88d3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aef0](../00c5a/00c5aef0.md)
- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/FirebaseMessaging"
~~~

## 疑似コード / UTF-8 881 bytes

~~~c

void _ZN8firebase9messaging18firebase_messaging13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011262a8 == 0) {
                    /* try { // try from 00bb8f2c to 00cb8f3b has its CatchHandler @ 00bb909c */
    DAT_011262a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/messaging/FirebaseMessaging",0)
    ;
                    /* try { // try from 00bb8f3c to 00cb8f4f has its CatchHandler @ 00bb9084 */
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_011262a8,&DAT_0030e730,1,&DAT_01126310,
             "com/google/firebase/messaging/FirebaseMessaging");
  return;
}

~~~
