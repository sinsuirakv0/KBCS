# 00bfa4ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa084`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa084.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0086.md#compare-c4c3b00d1a64783b63ec22ca2e65d206)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0096.md#compare-161f0749c7a110a4d2dd1b06742a0cc0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa4ac",
  "name": "_ZNSt6__ndk121recursive_timed_mutexD1Ev",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f146dda18efd3a4c6f248475ebc93775163bb9847d8a0969c4aff79a05d2a02",
  "source_text_sha256": "0f146dda18efd3a4c6f248475ebc93775163bb9847d8a0969c4aff79a05d2a02"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e60](../00c57/00c57e60.md)
- [00c580d0](../00c58/00c580d0.md)
- [00c58120](../00c58/00c58120.md)
- [00c5b6a0](../00c5b/00c5b6a0.md)
- [00c5b6b0](../00c5b/00c5b6b0.md)

## 関連文字列（未確認候補）

~~~text
"mutex lock failed"
~~~

## 疑似コード / UTF-8 428 bytes

~~~c

void _ZNSt6__ndk121recursive_timed_mutexD1Ev(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_lock(param_1);
  if (iVar1 == 0) {
    pthread_mutex_unlock(param_1);
    _ZNSt6__ndk118condition_variableD2Ev(param_1 + 1);
    _ZNSt6__ndk15mutexD1Ev(param_1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"mutex lock failed");
}

~~~
