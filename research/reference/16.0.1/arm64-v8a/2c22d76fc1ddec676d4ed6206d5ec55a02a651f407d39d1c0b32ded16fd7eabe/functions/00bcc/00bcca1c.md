# 00bcca1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc5f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0081.md#compare-384d015984c70cb56358b95c49d2c7b1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0090.md#compare-ddcc870def1bf538414c8f5b2a32f01d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcca1c",
  "name": "_ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d124abc80a44f48a0b0284c1d7424db0c93e16a3c4b5159b936081e75adda0d",
  "source_text_sha256": "7d124abc80a44f48a0b0284c1d7424db0c93e16a3c4b5159b936081e75adda0d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
~~~

## 疑似コード / UTF-8 743 bytes

~~~c

long _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* try { // try from 00bcca24 to 00ccca3b has its CatchHandler @ 00bce90c */
  if (DAT_011267f0 == 0) {
                    /* try { // try from 00bcca3c to 00cccaef has its CatchHandler @ 00bcc5d0 */
    DAT_011267f0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",param_3);
  }
  return DAT_011267f0;
}

~~~
