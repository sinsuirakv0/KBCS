# 00befbb8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bef790`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef790.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0039.md#compare-f4bb7e0acae5931d948ec6149bccc45c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0040.md#compare-2f8cc74a56811c539f79cf0da0a33b18)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befbb8",
  "name": "_ZNKSt16nested_exception14rethrow_nestedEv",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae78c5395c275261242cb3a96b766f35a0ee62dea1d5fbdd1d73fc1f1c79f502",
  "source_text_sha256": "ae78c5395c275261242cb3a96b766f35a0ee62dea1d5fbdd1d73fc1f1c79f502"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53f5c](../00c53/00c53f5c.md)
- [00c58020](../00c58/00c58020.md)
- [00c582f0](../00c58/00c582f0.md)
- [00c584b0](../00c58/00c584b0.md)
- [00c584c0](../00c58/00c584c0.md)

## 疑似コード / UTF-8 610 bytes

~~~c

void _ZNKSt16nested_exception14rethrow_nestedEv(long param_1)

{
  undefined8 uVar1;
  long lVar2;
  undefined1 auStack_30 [8];
  undefined8 local_28;
  
  local_28 = 0;
  lVar2 = *(long *)(param_1 + 8);
  _ZNSt13exception_ptrD1Ev(&local_28);
  if (lVar2 == 0) {
                    /* WARNING: Subroutine does not return */
    _ZSt9terminatev();
  }
  _ZNSt13exception_ptrC1ERKS_(auStack_30,(long *)(param_1 + 8));
  uVar1 = _ZSt17rethrow_exceptionSt13exception_ptr(auStack_30);
  _ZNSt13exception_ptrD1Ev(auStack_30);
                    /* WARNING: Subroutine does not return */
  FUN_00c53f5c(uVar1);
}

~~~
