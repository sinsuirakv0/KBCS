# 00bebbe8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00beb7c0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb7c0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/no_difference_in_scope-0013.md#compare-cc77b624dbbe958f35a4f29d5a7fb280)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/no_difference_in_scope-0014.md#compare-32aab5204d03a2a31f683578066c4bd6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bebbe8",
  "name": "FUN_00bebbe8",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "59b0fc1e84d11440dd12a50dadd1a0c752499829c9f1d05bad1e0ba26bc45f53",
  "source_text_sha256": "59b0fc1e84d11440dd12a50dadd1a0c752499829c9f1d05bad1e0ba26bc45f53"
}
~~~

## 呼び出し元

- [00be4d98](../00be4/00be4d98.md)
- [00beb948](../00beb/00beb948.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1473 bytes

~~~c

void FUN_00bebbe8(int *param_1,int *param_2,int *param_3,int *param_4,int *param_5)

{
  int iVar1;
  int iVar2;
  int iVar3;
  
  iVar1 = *param_2;
  iVar2 = *param_1;
  iVar3 = *param_3;
  if (iVar1 < iVar2) {
    if (iVar3 < iVar1) {
      *param_1 = iVar3;
    }
    else {
      *param_1 = iVar1;
      *param_2 = iVar2;
      iVar3 = *param_3;
      if (iVar2 <= iVar3) goto LAB_00bebc68;
      *param_2 = iVar3;
    }
    *param_3 = iVar2;
    iVar3 = iVar2;
  }
  else if (iVar3 < iVar1) {
    *param_2 = iVar3;
    *param_3 = iVar1;
    iVar2 = *param_1;
    iVar3 = iVar1;
    if (*param_2 < iVar2) {
      *param_1 = *param_2;
      *param_2 = iVar2;
      iVar3 = *param_3;
    }
  }
LAB_00bebc68:
  if (*param_4 < iVar3) {
    *param_3 = *param_4;
    *param_4 = iVar3;
    iVar1 = *param_2;
    if (*param_3 < iVar1) {
      *param_2 = *param_3;
      *param_3 = iVar1;
      iVar1 = *param_1;
      if (*param_2 < iVar1) {
        *param_1 = *param_2;
        *param_2 = iVar1;
      }
    }
  }
  iVar1 = *param_4;
  if (*param_5 < iVar1) {
    *param_4 = *param_5;
    *param_5 = iVar1;
    iVar1 = *param_3;
    if (*param_4 < iVar1) {
      *param_3 = *param_4;
      *param_4 = iVar1;
      iVar1 = *param_2;
      if (*param_3 < iVar1) {
        *param_2 = *param_3;
        *param_3 = iVar1;
        iVar1 = *param_1;
        if (*param_2 < iVar1) {
          *param_1 = *param_2;
          *param_2 = iVar1;
        }
      }
    }
  }
  return;
}

~~~
