# 00bf9fbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf9b94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b94.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0040.md#compare-7c597bd207b13c31695014b925c9a73a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0042.md#compare-476512cc8ae28dbc012005cd71c6bd81)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf9fbc",
  "name": "_ZNSt6__ndk113shared_futureIvED1Ev",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1286c3c0a28d9d4a378feeb86b3a3cec3a05ace460e31f1e0d0039ecb60a3e4c",
  "source_text_sha256": "1286c3c0a28d9d4a378feeb86b3a3cec3a05ace460e31f1e0d0039ecb60a3e4c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53d00](../00c53/00c53d00.md)

## 疑似コード / UTF-8 465 bytes

~~~c

void _ZNSt6__ndk113shared_futureIvED1Ev(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)*param_1;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53d00(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
                    /* WARNING: Could not recover jumptable at 0x00bfa00c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*plVar2 + 0x10))(plVar2);
    return;
  }
  return;
}

~~~
