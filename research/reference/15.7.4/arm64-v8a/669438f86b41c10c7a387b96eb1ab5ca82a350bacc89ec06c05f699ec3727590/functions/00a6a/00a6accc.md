# 00a6accc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a6ac88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6ac88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0002.md#compare-26ee11d5154deb64abde03f304d7a7e0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6accc",
  "name": "FUN_00a6accc",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b213e49280e4a176fbdcecba4dbbe50cd0a91b36bb520ccb58d1adf037769904",
  "source_text_sha256": "b213e49280e4a176fbdcecba4dbbe50cd0a91b36bb520ccb58d1adf037769904"
}
~~~

## 呼び出し元

- [00632468](../00632/00632468.md)
- [00664710](../00664/00664710.md)
- [006aad48](../006aa/006aad48.md)
- [006d6364](../006d6/006d6364.md)
- [0073fa38](../0073f/0073fa38.md)
- [00803d90](../00803/00803d90.md)
- [0088d060](../0088d/0088d060.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)
- [00827b94](../00827/00827b94.md)
- [008292ec](../00829/008292ec.md)
- [008292f4](../00829/008292f4.md)
- [00829328](../00829/00829328.md)
- [00a6adf0](../00a6a/00a6adf0.md)

## 疑似コード / UTF-8 1520 bytes

~~~c

undefined8 FUN_00a6accc(long param_1)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  float fVar4;
  float fVar5;
  float fVar6;
  
  if (*(char *)(param_1 + 0x1d4) == '\0') {
    return 0;
  }
  FUN_0081f580();
  uVar2 = FUN_00827b94();
  if ((uVar2 & 1) == 0) {
    FUN_0081f580();
    uVar2 = FUN_00829328();
    if (((uVar2 & 1) == 0) && (lVar3 = FUN_0081f580(), *(char *)(lVar3 + 0x347d) == '\0'))
    goto LAB_00a6ad8c;
  }
  FUN_0081f580();
  uVar2 = FUN_00829328();
  if ((uVar2 & 1) != 0) {
    *(undefined4 *)(param_1 + 500) = *(undefined4 *)(param_1 + 0x1f0);
    return 1;
  }
  uVar2 = FUN_00a6adf0(param_1);
  if ((uVar2 & 1) != 0) {
    fVar4 = *(float *)(param_1 + 0x1d8);
    iVar1 = *(int *)(param_1 + 0x284);
    fVar5 = (fVar4 * *(float *)(param_1 + 0x1e0)) / *(float *)(param_1 + 0x1dc);
    if (fVar5 <= 14.0) {
      fVar5 = 14.0;
    }
    FUN_0081f580();
    if (iVar1 == 0) {
      iVar1 = FUN_008292ec();
      fVar6 = *(float *)(param_1 + 0x1e4);
    }
    else {
      iVar1 = FUN_008292f4();
      fVar6 = *(float *)(param_1 + 0x1e8);
    }
    fVar4 = (float)NEON_fminnm((((float)iVar1 - fVar6) + -fVar5 * 0.5) / (float)(int)(fVar4 - fVar5)
                               ,0x3f800000);
    if (fVar4 <= 0.0) {
      fVar4 = 0.0;
    }
    *(float *)(param_1 + 0x1f0) = fVar4;
    return 1;
  }
LAB_00a6ad8c:
  *(undefined4 *)(param_1 + 500) = *(undefined4 *)(param_1 + 0x1f0);
                    /* try { // try from 00a6addc to 00b6ae0b has its CatchHandler @ 00a6b6a4 */
  return 0;
}

~~~
