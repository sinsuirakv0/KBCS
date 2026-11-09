# 00bc1dec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bc1dec",
  "name": "_ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6a8694e41214d2a7265ccae3f3222f91a9d08c839c0fbebf1e17cf4ba6fa6c9",
  "source_text_sha256": "d6a8694e41214d2a7265ccae3f3222f91a9d08c839c0fbebf1e17cf4ba6fa6c9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo"
~~~

## 疑似コード / UTF-8 644 bytes

~~~c

long _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEE
               (void)

{
                    /* try { // try from 00bc1df4 to 00cc1e0f has its CatchHandler @ 00bc1f70 */
  if (DAT_01126168 == 0) {
                    /* try { // try from 00bc1e10 to 00cc1eb7 has its CatchHandler @ 00bc1b44 */
    DAT_01126168 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126168;
}

~~~
