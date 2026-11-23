# 00bc1ecc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bc1aa4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1aa4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0080.md#compare-d3729b161c8bbad70fe4fc14cd7a3825)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0089.md#compare-e5298ca89f1ed2609c9531b80876c872)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc1ecc",
  "name": "_ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "11b7ddbcf2a2b335a21efe06f14caedb68f1a3a75a293ff35c429c1f51060555",
  "source_text_sha256": "11b7ddbcf2a2b335a21efe06f14caedb68f1a3a75a293ff35c429c1f51060555"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigValue"
~~~

## 疑似コード / UTF-8 548 bytes

~~~c

long _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEE
               (void)

{
                    /* try { // try from 00bc1ed4 to 00cc1ed7 has its CatchHandler @ 00bc21dc */
  if (DAT_01126520 == 0) {
    DAT_01126520 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126520;
}

~~~
