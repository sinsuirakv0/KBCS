# 00bfe9ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfe910`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe910.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0041.md#compare-f5a3f60cfd1c6df2b5fd151844b46626)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0039.md#compare-3aad40a159f1fdf987951255e39f4d67)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfe9ac",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3edf5b601679214f4dddc088638730a102550e7244bff11003a452390bb6685a",
  "source_text_sha256": "3edf5b601679214f4dddc088638730a102550e7244bff11003a452390bb6685a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e3f0](../00c5e/00c5e3f0.md)

## 疑似コード / UTF-8 672 bytes

~~~c

void _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_(long *param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  undefined4 uVar3;
  undefined4 uVar4;
  undefined8 uVar5;
  
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  lVar2 = (long)param_2 + *(long *)(*param_2 + -0x18);
  _ZNSt6__ndk18ios_base4swapERS0_(lVar1,lVar2);
  uVar5 = *(undefined8 *)(lVar1 + 0x88);
  uVar3 = *(undefined4 *)(lVar2 + 0x90);
  *(undefined8 *)(lVar1 + 0x88) = *(undefined8 *)(lVar2 + 0x88);
  uVar4 = *(undefined4 *)(lVar1 + 0x90);
  *(undefined8 *)(lVar2 + 0x88) = uVar5;
  *(undefined4 *)(lVar1 + 0x90) = uVar3;
  *(undefined4 *)(lVar2 + 0x90) = uVar4;
  return;
}

~~~
