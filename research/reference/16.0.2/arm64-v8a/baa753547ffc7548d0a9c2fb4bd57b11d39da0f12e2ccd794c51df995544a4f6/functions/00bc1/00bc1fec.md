# 00bc1fec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc1f50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0080.md#compare-2c5dc7a0710cb50d1989cfe078d4d5a7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0092.md#compare-4624976cfac00af7c829474d5a0efaf7)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc1fec",
  "name": "_ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "55fcac3e8b2a9914a42096a091da98be5623082a6b0b300b639778f5587bb62b",
  "source_text_sha256": "55fcac3e8b2a9914a42096a091da98be5623082a6b0b300b639778f5587bb62b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigValue"
~~~

## 疑似コード / UTF-8 711 bytes

~~~c

long _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bc1ff4 to 00cc1ffb has its CatchHandler @ 00bc2214 */
                    /* try { // try from 00bc1ffc to 00cc200f has its CatchHandler @ 00bc21a8 */
  if (DAT_01126620 == 0) {
    DAT_01126620 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/remoteconfig/FirebaseRemoteConfigValue",0);
  }
  return DAT_01126620;
}

~~~
