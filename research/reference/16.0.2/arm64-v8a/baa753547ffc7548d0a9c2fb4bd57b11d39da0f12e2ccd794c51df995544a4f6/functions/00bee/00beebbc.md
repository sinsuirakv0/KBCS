# 00beebbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00beeb20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beeb20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/no_difference_in_scope-0014.md#compare-6f7b1b123a1b3d1d9c294e07c4e0af70)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/no_difference_in_scope-0014.md#compare-f8a55aa711d3806403fb8480de3e5191)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beebbc",
  "name": "FUN_00beebbc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "89d7d7b673f5c4ec03773ce4de799b86546055e615f2290bd3bd2ce20989c66a",
  "source_text_sha256": "89d7d7b673f5c4ec03773ce4de799b86546055e615f2290bd3bd2ce20989c66a"
}
~~~

## 呼び出し元

- [00be7fdc](../00be7/00be7fdc.md)
- [00bee91c](../00bee/00bee91c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1529 bytes

~~~c

void FUN_00beebbc(double *param_1,double *param_2,double *param_3,double *param_4,double *param_5)

{
  double dVar1;
  double dVar2;
  double dVar3;
  
  dVar1 = *param_2;
  dVar2 = *param_1;
  dVar3 = *param_3;
  if (dVar2 <= dVar1) {
    if (dVar3 < dVar1) {
      *param_2 = dVar3;
      *param_3 = dVar1;
      dVar2 = *param_1;
      dVar3 = dVar1;
      if (*param_2 < dVar2) {
        *param_1 = *param_2;
        *param_2 = dVar2;
        dVar3 = *param_3;
      }
    }
  }
  else {
    if (dVar1 <= dVar3) {
      *param_1 = dVar1;
      *param_2 = dVar2;
      dVar3 = *param_3;
      if (dVar2 <= dVar3) goto LAB_00beec3c;
      *param_2 = dVar3;
    }
    else {
      *param_1 = dVar3;
    }
    *param_3 = dVar2;
    dVar3 = dVar2;
  }
LAB_00beec3c:
  if (*param_4 < dVar3) {
    *param_3 = *param_4;
    *param_4 = dVar3;
    dVar3 = *param_2;
    if (*param_3 < dVar3) {
      *param_2 = *param_3;
      *param_3 = dVar3;
      dVar3 = *param_1;
      if (*param_2 < dVar3) {
        *param_1 = *param_2;
        *param_2 = dVar3;
      }
    }
  }
  dVar3 = *param_4;
  if (*param_5 < dVar3) {
    *param_4 = *param_5;
    *param_5 = dVar3;
    dVar3 = *param_3;
    if (*param_4 < dVar3) {
      *param_3 = *param_4;
      *param_4 = dVar3;
      dVar3 = *param_2;
      if (*param_3 < dVar3) {
        *param_2 = *param_3;
        *param_3 = dVar3;
        dVar3 = *param_1;
        if (*param_2 < dVar3) {
          *param_1 = *param_2;
          *param_2 = dVar3;
        }
      }
    }
  }
  return;
}

~~~
