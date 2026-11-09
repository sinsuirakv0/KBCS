# 00bc1dac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bc1dac",
  "name": "_ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9465a188a9c9471b9f5a024b11e0c56084910f32958cccc8d0c81c15d2b2ffd9",
  "source_text_sha256": "9465a188a9c9471b9f5a024b11e0c56084910f32958cccc8d0c81c15d2b2ffd9"
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

## 疑似コード / UTF-8 574 bytes

~~~c

long _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01126168 == 0) {
    DAT_01126168 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
                    /* try { // try from 00bc1dd8 to 00cc1ddb has its CatchHandler @ 00bc1fe0 */
  }
  return DAT_01126168;
}

~~~
