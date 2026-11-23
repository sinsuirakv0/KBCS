# 00afccf4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afc8cc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc8cc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0007.md#compare-8e28121241c599fda57140b7cf20b127)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0037.md#compare-9743d769ccda63f30ff7d802941f27ef)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afccf4",
  "name": "FUN_00afccf4",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "78134e2a6de93ec2fa04230f43b8fd84f6f8e7804f8d7cba71c2580fada5fe1f",
  "source_text_sha256": "78134e2a6de93ec2fa04230f43b8fd84f6f8e7804f8d7cba71c2580fada5fe1f"
}
~~~

## 呼び出し元

- [00700af8](../00700/00700af8.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 183 bytes

~~~c

bool FUN_00afccf4(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c34) != 0;
}

~~~
