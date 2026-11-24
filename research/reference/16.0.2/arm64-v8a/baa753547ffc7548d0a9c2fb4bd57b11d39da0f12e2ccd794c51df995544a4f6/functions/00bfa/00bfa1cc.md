# 00bfa1cc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfa130`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa130.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0086.md#compare-38d2c9aed29a2645225a4d4c44489264)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0098.md#compare-8b8f4d65a4a1442df25a6e8efc7186c1)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa1cc",
  "name": "_ZNSt6__ndk15mutex4lockEv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6a09bf60f6e907cbf77359d35e00face011e0c1ea964fdc0b39b44725fd3203",
  "source_text_sha256": "d6a09bf60f6e907cbf77359d35e00face011e0c1ea964fdc0b39b44725fd3203"
}
~~~

## 呼び出し元

- [00c581b0](../00c58/00c581b0.md)

## 呼び出し先

- [00c581f0](../00c58/00c581f0.md)
- [00c5b770](../00c5b/00c5b770.md)

## 関連文字列（未確認候補）

~~~text
"mutex lock failed"
~~~

## 疑似コード / UTF-8 287 bytes

~~~c

void _ZNSt6__ndk15mutex4lockEv(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_lock(param_1);
  if (iVar1 == 0) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"mutex lock failed");
}

~~~
