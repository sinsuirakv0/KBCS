# 00a6acac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a6ac3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6ac3c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0034.md#compare-078e701a844d7ab81da7ca312636cb69)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0028.md#compare-988227c55cc2ada6df5d661d7b50bc90)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6acac",
  "name": "FUN_00a6acac",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c43e35222444f9898d40f3c5777f9985a8c0f5d1a9a92430044818e368ee3929",
  "source_text_sha256": "c43e35222444f9898d40f3c5777f9985a8c0f5d1a9a92430044818e368ee3929"
}
~~~

## 呼び出し元

- [007ccf44](../007cc/007ccf44.md)
- [009d7bd0](../009d7/009d7bd0.md)
- [00a47f54](../00a47/00a47f54.md)

## 呼び出し先

- [005e08f0](../005e0/005e08f0.md)

## 疑似コード / UTF-8 230 bytes

~~~c

void FUN_00a6acac(long param_1,undefined4 param_2)

{
  uint uVar1;
  
  *(undefined4 *)(param_1 + 0x7c) = param_2;
  uVar1 = FUN_005e08f0();
  *(uint *)(param_1 + 0x84) = uVar1 & ((int)uVar1 >> 0x1f ^ 0xffffffffU);
  return;
}

~~~
