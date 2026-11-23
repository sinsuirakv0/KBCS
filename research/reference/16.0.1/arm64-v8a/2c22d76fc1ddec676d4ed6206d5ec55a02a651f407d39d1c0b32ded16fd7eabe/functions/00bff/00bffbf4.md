# 00bffbf4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bff7cc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff7cc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/reference_unresolved-0001.md#compare-04c873b9f923ad7b0513d83c3c4127b7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/reference_unresolved-0001.md#compare-e9aade3dbe41b626e18230b04359e92a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffbf4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6sbumpcEv",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35f5f9e55973879c4032ee37e40c14e211d96f74aad3aece7104e7ce179e6f4f",
  "source_text_sha256": "35f5f9e55973879c4032ee37e40c14e211d96f74aad3aece7104e7ce179e6f4f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 523 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6sbumpcEv(long *param_1)

{
  uint *puVar1;
  uint uVar2;
  ulong uVar3;
  
  puVar1 = (uint *)param_1[3];
  if (puVar1 != (uint *)param_1[4]) {
    uVar2 = *puVar1;
    param_1[3] = (long)(puVar1 + 1);
    return (ulong)uVar2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffc20. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar3 = (**(code **)(*param_1 + 0x50))(param_1);
  return uVar3;
}

~~~
