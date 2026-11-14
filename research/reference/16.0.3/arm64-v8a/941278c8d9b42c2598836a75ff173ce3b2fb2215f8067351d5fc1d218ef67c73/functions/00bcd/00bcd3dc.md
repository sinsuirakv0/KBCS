# 00bcd3dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcd3dc",
  "name": "_ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "379df259bfdad57585f1cc82b93d6755bb661210d82bd880718e800c96eaaadd",
  "source_text_sha256": "379df259bfdad57585f1cc82b93d6755bb661210d82bd880718e800c96eaaadd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuth"
~~~

## 疑似コード / UTF-8 520 bytes

~~~c

long _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_011277e8 == 0) {
                    /* try { // try from 00bcd3f8 to 00ccd47f has its CatchHandler @ 00bcd564 */
    DAT_011277e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_011277e8;
}

~~~
