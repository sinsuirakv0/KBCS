# 005afdec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `005afdac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdac.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0015.md#compare-8feedc73867189f350c82bc29c9f3956)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0015.md#compare-0ea259739ac147b244095895a3e20915)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005afdec",
  "name": "FUN_005afdec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb90ce07b03258c02c1003fd5fb0d3e8f527eda4e069f18f284966c44101f007",
  "source_text_sha256": "bb90ce07b03258c02c1003fd5fb0d3e8f527eda4e069f18f284966c44101f007"
}
~~~

## 呼び出し元

- [00a47f00](../00a47/00a47f00.md)

## 呼び出し先

- [005afc78](../005af/005afc78.md)

## 疑似コード / UTF-8 190 bytes

~~~c

int FUN_005afdec(void)

{
  int iVar1;
  
  iVar1 = FUN_005afc78(2);
                    /* try { // try from 005afe00 to 006afe0f has its CatchHandler @ 005b02cc */
  return iVar1 + 3;
}

~~~
