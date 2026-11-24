# 005cefbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `005cef7c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cef7c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0024.md#compare-0e8ef845fc09d4e33246fb7f86a0180f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0025.md#compare-bc0d3c4c6716d26e7b71c463860c1b17)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cefbc",
  "name": "FUN_005cefbc",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f56aa53d419c36d27df3396e09301b5a8cb414b4dc7603570eeda33e181888a1",
  "source_text_sha256": "f56aa53d419c36d27df3396e09301b5a8cb414b4dc7603570eeda33e181888a1"
}
~~~

## 呼び出し元

- [005ce640](../005ce/005ce640.md)

## 呼び出し先

- [00c58350](../00c58/00c58350.md)
- [00c5a870](../00c5a/00c5a870.md)

## 疑似コード / UTF-8 584 bytes

~~~c

void FUN_005cefbc(long param_1)

{
  undefined8 uVar1;
  
  _ZNSt6__ndk16localeC2Ev();
  uVar1 = _ZNKSt6__ndk16locale9use_facetERNS0_2idE(param_1,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ad00);
  *(undefined8 *)(param_1 + 8) = uVar1;
  uVar1 = _ZNKSt6__ndk16locale9use_facetERNS0_2idE(param_1,PTR__ZNSt6__ndk17collateIcE2idE_00c9b448)
  ;
  *(undefined8 *)(param_1 + 0x10) = uVar1;
  *(undefined8 *)(param_1 + 0x20) = 0;
  *(undefined8 *)(param_1 + 0x18) = 0;
  *(undefined8 *)(param_1 + 0x30) = 0;
  *(undefined8 *)(param_1 + 0x28) = 0;
  *(undefined8 *)(param_1 + 0x38) = 0;
  return;
}

~~~
