# 00bcdbe0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcdb44`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb44.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0081.md#compare-0aac71bafda61eade9dcac944fbea93f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0037.md#compare-ba6b4d5dbd17d99ecc66e7d4ad32adeb)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdbe0",
  "name": "_ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d64db83b8c79c9db5c7abee8fe01970f654e1d4a20cd54a361ba6bb0470c8293",
  "source_text_sha256": "d64db83b8c79c9db5c7abee8fe01970f654e1d4a20cd54a361ba6bb0470c8293"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5dae0](../00c5d/00c5dae0.md)
- [00c5dd00](../00c5d/00c5dd00.md)

## 疑似コード / UTF-8 319 bytes

~~~c

void _ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE(param_3);
  _ZN8firebase4auth24NotifyAuthStateListenersEPNS0_8AuthDataE(param_3);
  return;
}

~~~
