# 005badcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `005bad8c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad8c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0016.md#compare-fa535daf5b7d44a45d3d715d9f240410)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0016.md#compare-6d512faeba20462fbc7988191fc7282e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005badcc",
  "name": "FUN_005badcc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3927f9875075bf785219f1a4e1220474854815864f78628d56406ed918b6ec2",
  "source_text_sha256": "e3927f9875075bf785219f1a4e1220474854815864f78628d56406ed918b6ec2"
}
~~~

## 呼び出し元

- [005ba958](../005ba/005ba958.md)

## 呼び出し先

- [00c58530](../00c58/00c58530.md)
- [00c58540](../00c58/00c58540.md)

## 疑似コード / UTF-8 260 bytes

~~~c

void FUN_005badcc(undefined8 param_1)

{
                    /* try { // try from 005badd4 to 006bade3 has its CatchHandler @ 005baec8 */
  _ZNSt6__ndk117__assoc_sub_state4waitEv();
  _ZNSt6__ndk117__assoc_sub_state16__on_zero_sharedEv(param_1);
  return;
}

~~~
