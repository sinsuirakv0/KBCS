# 00c0acdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c0a8b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0087.md#compare-a762632cce91dee999dd08bd4a58dc8b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0097.md#compare-cc2775c739acd7939118a7cdded39230)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c0acdc",
  "name": "_ZNSt6__ndk16__clocEv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "371bc99a0cbee51e8c73f468ef7d91c7add292481e190391bfa3018dd1caca01",
  "source_text_sha256": "371bc99a0cbee51e8c73f468ef7d91c7add292481e190391bfa3018dd1caca01"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c5d220](../00c5d/00c5d220.md)

## 疑似コード / UTF-8 282 bytes

~~~c

__locale_t _ZNSt6__ndk16__clocEv(void)

{
  int iVar1;
  
  if (((DAT_01127ca0 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01127ca0), iVar1 != 0)) {
    DAT_01127c98 = newlocale(0x1fbf,"C",(__locale_t)0x0);
    __cxa_guard_release(&DAT_01127ca0);
  }
  return DAT_01127c98;
}

~~~
