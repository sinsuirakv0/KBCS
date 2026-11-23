# 00acaff8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acadfc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acadfc.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/high-0007.md#compare-06e74ba9e3d2d11635162168c2322b03)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/high-0009.md#compare-f6cfdade836a0d46c5fb97434c27a032)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acaff8",
  "name": "FUN_00acaff8",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "36d92829ea4bca1d4583f3b7a4436cce2ece5843f5b82ee612df3fa2b882b77c",
  "source_text_sha256": "36d92829ea4bca1d4583f3b7a4436cce2ece5843f5b82ee612df3fa2b882b77c"
}
~~~

## 呼び出し元

- [00789de0](../00789/00789de0.md)
- [0082fb6c](../0082f/0082fb6c.md)
- [008ff040](../008ff/008ff040.md)
- [00a3e524](../00a3e/00a3e524.md)
- [00ac0a9c](../00ac0/00ac0a9c.md)

## 呼び出し先

- [00759114](../00759/00759114.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 444 bytes

~~~c

void FUN_00acaff8(long param_1)

{
  int iVar1;
  undefined8 uVar2;
  undefined4 uVar3;
  
  iVar1 = *(int *)(param_1 + 0x9c);
  if (iVar1 == 0) {
    uVar2 = FUN_008514f8();
    uVar3 = 0;
  }
  else {
    if ((iVar1 != 1) && (iVar1 != 2)) {
      return;
    }
    uVar2 = FUN_008514f8();
    FUN_008514f8();
    uVar3 = *(undefined4 *)(PTR_DAT_00c9b508 + (long)*(int *)(param_1 + 0x98) * 4);
  }
  FUN_00759114(uVar2,uVar3,0);
  return;
}

~~~
