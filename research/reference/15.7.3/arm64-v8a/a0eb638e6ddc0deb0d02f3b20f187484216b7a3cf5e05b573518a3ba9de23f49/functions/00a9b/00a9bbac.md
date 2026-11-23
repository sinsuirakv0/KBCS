# 00a9bbac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a9bbac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a9b/00a9bbac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/no_difference_in_scope-0024.md#compare-45fa88b6bef61b827ce97f98ad6294f3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9bbac",
  "name": "FUN_00a9bbac",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2112b0f97cea77fd2af031dbd24a3e8b06eefd668ebfb36fb1841078ed8e2fbb",
  "source_text_sha256": "2112b0f97cea77fd2af031dbd24a3e8b06eefd668ebfb36fb1841078ed8e2fbb"
}
~~~

## 呼び出し元

- [005ced48](../005ce/005ced48.md)
- [005d6c3c](../005d6/005d6c3c.md)
- [006d6d04](../006d6/006d6d04.md)
- [006e4aec](../006e4/006e4aec.md)
- [006e79bc](../006e7/006e79bc.md)
- [006eccf4](../006ec/006eccf4.md)

## 呼び出し先

- [005bb5f0](../005bb/005bb5f0.md)
- [005bbbc8](../005bb/005bbbc8.md)
- [005bbc10](../005bb/005bbc10.md)
- [005bbc90](../005bb/005bbc90.md)
- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 1418 bytes

~~~c

void FUN_00a9bbac(int param_1,int param_2,int param_3)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  
  if (param_1 == 1) {
    uVar2 = FUN_005bbbc8();
    if ((uVar2 & 1) == 0) {
      if (param_2 != 0) goto LAB_00a9bc28;
    }
    else {
      iVar1 = FUN_005bbc10();
      if (iVar1 != param_2) goto LAB_00a9bc28;
    }
    uVar2 = FUN_005bbc90();
    if ((uVar2 & 1) != 0) {
      lVar3 = FUN_0081f580();
      FUN_005bb5f0(lVar3 + 0x898,1);
      return;
    }
  }
LAB_00a9bc28:
  lVar3 = FUN_0081f580();
  lVar3 = lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar3 + 0x840cc) = *(int *)(lVar3 + 0x840cc) + param_3;
  lVar3 = FUN_0081f580();
  lVar3 = lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar3 + 0x84240) = *(int *)(lVar3 + 0x84240) + param_3;
  lVar3 = FUN_0081f580();
  if (((0 < *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84288)) &&
      (lVar3 = FUN_0081f580(),
      *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84288) < param_3)) &&
     (lVar3 = FUN_0081f580(),
     *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8428c) == 0)) {
    lVar3 = FUN_0081f580();
    *(undefined4 *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8428c) = 1;
  }
  lVar3 = FUN_0081f580();
  *(undefined4 *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84308) = 1;
  return;
}

~~~
