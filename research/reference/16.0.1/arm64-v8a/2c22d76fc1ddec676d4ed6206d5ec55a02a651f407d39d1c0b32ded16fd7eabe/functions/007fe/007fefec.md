# 007fefec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `007fefac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefac.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0041.md#compare-35d2dfc2504ad784719f9ffecb3943cf)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0044.md#compare-c1cac87803692184acae1d704fcb583b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fefec",
  "name": "FUN_007fefec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c1f60cc41966e8ce690e8dff879c3e869f8d88faa36e94497380e3ca3eb320b",
  "source_text_sha256": "7c1f60cc41966e8ce690e8dff879c3e869f8d88faa36e94497380e3ca3eb320b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)

## 疑似コード / UTF-8 232 bytes

~~~c

void FUN_007fefec(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)param_1[2];
  *param_1 = &PTR_FUN_00c7e030;
  if (__ptr != (void *)0x0) {
    param_1[3] = __ptr;
    _ZdlPv(__ptr);
  }
  _ZdlPv(param_1);
  return;
}

~~~
