# 00af7bac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af7784`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7784.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0005.md#compare-b8c68eefbd1780c4d9ac3979be054255)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0071.md#compare-08b6f0cf0e65616f8d65b44727747ca7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af7bac",
  "name": "FUN_00af7bac",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45f699ed85237997805ef40c4a926ce8e530f4e391fd4dabdf402a23c79f8daa",
  "source_text_sha256": "45f699ed85237997805ef40c4a926ce8e530f4e391fd4dabdf402a23c79f8daa"
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 278 bytes

~~~c

void FUN_00af7bac(int param_1,int param_2,int param_3,undefined4 param_4)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  *(undefined4 *)
   (lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + (long)(int)(&DAT_0030a398)[param_3] * 4
   + 0x848c8) = param_4;
  return;
}

~~~
