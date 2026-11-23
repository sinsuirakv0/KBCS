# 00af9dbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af9994`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af9994.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0066.md#compare-1486310c2e5d699e99c4ce84c554c6df)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0072.md#compare-fb210808d2349c14e7b76809ece7dc8e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af9dbc",
  "name": "FUN_00af9dbc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae139c01be89e972701b9f8ffb5502be4e256503a01f077cc882c4bf35b5739f",
  "source_text_sha256": "ae139c01be89e972701b9f8ffb5502be4e256503a01f077cc882c4bf35b5739f"
}
~~~

## 呼び出し元

- [0070ea5c](../0070e/0070ea5c.md)
- [007119f0](../00711/007119f0.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 385 bytes

~~~c

bool FUN_00af9dbc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_008514f8();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b0c) != 0;
  }
  return bVar1;
}

~~~
