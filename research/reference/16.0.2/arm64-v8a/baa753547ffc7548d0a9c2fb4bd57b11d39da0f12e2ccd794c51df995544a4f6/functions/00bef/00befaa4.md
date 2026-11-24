# 00befaa4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befa08`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa08.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0086.md#compare-629e6170cc24c4cd8c8c04c3fbdbf6e2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0098.md#compare-4f84bc13e870928a66d909437b869ffc)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befaa4",
  "name": "_ZNSt6__ndk16chrono12steady_clock3nowEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f786a19d96d4d6bd97bfbe16c71d2c3731ce5e31e9fd9f46d8152ba90213d511",
  "source_text_sha256": "f786a19d96d4d6bd97bfbe16c71d2c3731ce5e31e9fd9f46d8152ba90213d511"
}
~~~

## 呼び出し元

- [00c57f90](../00c57/00c57f90.md)

## 呼び出し先

- [00c58190](../00c58/00c58190.md)
- [00c581f0](../00c58/00c581f0.md)
- [00c597d0](../00c59/00c597d0.md)

## 関連文字列（未確認候補）

~~~text
"clock_gettime(CLOCK_MONOTONIC) failed"
~~~

## 疑似コード / UTF-8 429 bytes

~~~c

long _ZNSt6__ndk16chrono12steady_clock3nowEv(void)

{
  int iVar1;
  undefined4 *puVar2;
  timespec local_20;
  
  iVar1 = clock_gettime(1,&local_20);
  if (iVar1 == 0) {
    return local_20.tv_nsec + local_20.tv_sec * 1000000000;
  }
  puVar2 = (undefined4 *)__errno();
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(*puVar2,"clock_gettime(CLOCK_MONOTONIC) failed");
}

~~~
