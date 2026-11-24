# 00af6cac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af6c10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6c10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0006.md#compare-aa04cac73e2b0c7b98fc74518d5fc106)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0029.md#compare-93144971fc0f11b9756e1819d8222f71)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af6cac",
  "name": "FUN_00af6cac",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4181316bf6c179a6649767a700ae5a4965d8bc92967f10d5d3e66ec1ac8d30e5",
  "source_text_sha256": "4181316bf6c179a6649767a700ae5a4965d8bc92967f10d5d3e66ec1ac8d30e5"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 400 bytes

~~~c

void FUN_00af6cac(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  long lVar3;
  
  lVar1 = FUN_00851550();
  uVar2 = FUN_005e7460(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  lVar3 = FUN_00851550();
  lVar1 = 0x44;
  if ((uVar2 & 1) != 0) {
    lVar1 = 0x40;
  }
  *(uint *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + lVar1 + 0x848c8) = param_3 & 1;
  return;
}

~~~
