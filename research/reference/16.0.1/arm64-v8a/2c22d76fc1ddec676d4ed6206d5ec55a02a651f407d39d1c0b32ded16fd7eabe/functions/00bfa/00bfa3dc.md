# 00bfa3dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf9fb4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9fb4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0040.md#compare-44953720bce21203ce0fe5763186c76b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0042.md#compare-9e0af1983df2d00984fad1b4f06122e6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa3dc",
  "name": "_ZNSt6__ndk111timed_mutex8try_lockEv",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41d5e36ba8584ba38fd4f465786283fa3349aa905ab9390120ff767dab81c772",
  "source_text_sha256": "41d5e36ba8584ba38fd4f465786283fa3349aa905ab9390120ff767dab81c772"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b6b0](../00c5b/00c5b6b0.md)
- [00c5e270](../00c5e/00c5e270.md)

## 疑似コード / UTF-8 413 bytes

~~~c

bool _ZNSt6__ndk111timed_mutex8try_lockEv(pthread_mutex_t *param_1)

{
  bool bVar1;
  int iVar2;
  
  iVar2 = pthread_mutex_trylock(param_1);
  if (iVar2 == 0) {
    bVar1 = *(byte *)((long)param_1 + 0x58) == 0;
    if ((*(byte *)((long)param_1 + 0x58) & 1) == 0) {
      *(undefined1 *)((long)param_1 + 0x58) = 1;
    }
    pthread_mutex_unlock(param_1);
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
