# 005cdafc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `005cdabc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdabc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0024.md#compare-4234c4562d07c7c0e35facd15f9ce3eb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0024.md#compare-4ca71246ba95219292d4b1fe553e6877)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cdafc",
  "name": "FUN_005cdafc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e2230905d70f21febf609a8a17d50bc088d4a682ec81c95fdee0ac8ffafbc73",
  "source_text_sha256": "9e2230905d70f21febf609a8a17d50bc088d4a682ec81c95fdee0ac8ffafbc73"
}
~~~

## 呼び出し元

- [005cd660](../005cd/005cd660.md)

## 呼び出し先

- [00c57ef0](../00c57/00c57ef0.md)
- [00c57f10](../00c57/00c57f10.md)
- [00c5a7b0](../00c5a/00c5a7b0.md)

## 疑似コード / UTF-8 357 bytes

~~~c

void FUN_005cdafc(void)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_allocate_exception(0x18);
  _ZNSt6__ndk111regex_errorC1ENS_15regex_constants10error_typeE(uVar1,0x11);
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar1,PTR__ZTINSt6__ndk111regex_errorE_00c9b3b0,
              PTR__ZNSt6__ndk111regex_errorD1Ev_00c9b3b8);
}

~~~
