# 00ac8dfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ac8c00`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8c00.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0064.md#compare-b70366f51c64078721b514a38384d998)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/no_difference_in_scope-0013.md#compare-0ebf2766199ccc59ce98d5df439082c1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac8dfc",
  "name": "FUN_00ac8dfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56791046ae044d613b5ffc4e9046c995fdc495a36cf26e120260b1157c747b21",
  "source_text_sha256": "56791046ae044d613b5ffc4e9046c995fdc495a36cf26e120260b1157c747b21"
}
~~~

## 呼び出し元

- [00693458](../00693/00693458.md)
- [00788cac](../00788/00788cac.md)
- [0082cd18](../0082c/0082cd18.md)
- [008c385c](../008c3/008c385c.md)
- [008c5208](../008c5/008c5208.md)
- [00a6fd88](../00a6f/00a6fd88.md)
- [00a72594](../00a72/00a72594.md)
- [00a73530](../00a73/00a73530.md)
- [00a7c224](../00a7c/00a7c224.md)
- [00a7e564](../00a7e/00a7e564.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 236 bytes

~~~c

void FUN_00ac8dfc(long param_1,int param_2)

{
  int iVar1;
  
  *(int *)(param_1 + 0x60) = param_2;
  iVar1 = -(*(int *)(param_1 + 0x68) * param_2);
  *(int *)(param_1 + 0x4c) = iVar1;
  *(int *)(param_1 + 0x50) = iVar1;
  return;
}

~~~
