# 00a6adac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a6adac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6a/00a6adac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/no_difference_in_scope-0019.md#compare-afd826624b9c23e42217133c5c8ac925)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6adac",
  "name": "FUN_00a6adac",
  "size": 316,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab53e3631c6f62ab3eb46d0a8c5da5df417734eed1149703094c7e5fd2e98f4c",
  "source_text_sha256": "ab53e3631c6f62ab3eb46d0a8c5da5df417734eed1149703094c7e5fd2e98f4c"
}
~~~

## 呼び出し元

- [00a6ac88](../00a6a/00a6ac88.md)
- [00a6af0c](../00a6a/00a6af0c.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)
- [00827b94](../00827/00827b94.md)
- [008292fc](../00829/008292fc.md)
- [00829304](../00829/00829304.md)
- [0082931c](../00829/0082931c.md)
- [00829328](../00829/00829328.md)

## 疑似コード / UTF-8 1821 bytes

~~~c

undefined8 FUN_00a6adac(long param_1)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  float fVar4;
  
  FUN_0081f580();
  uVar2 = FUN_00827b94();
  if ((uVar2 & 1) == 0) {
    FUN_0081f580();
    uVar2 = FUN_0082931c();
    if ((uVar2 & 1) == 0) {
      FUN_0081f580();
      uVar2 = FUN_00829328();
                    /* try { // try from 00a6addc to 00b6ae0b has its CatchHandler @ 00a6b6a4 */
      if (((uVar2 & 1) == 0) && (lVar3 = FUN_0081f580(), *(char *)(lVar3 + 0x347d) == '\0')) {
        return 0;
      }
    }
  }
  if (*(int *)(param_1 + 0x284) == 1) {
    FUN_0081f580();
    iVar1 = FUN_008292fc();
    if ((float)iVar1 < *(float *)(param_1 + 0x1e4)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_008292fc();
    if (*(float *)(param_1 + 0x1e4) + *(float *)(param_1 + 0x1ec) < (float)iVar1) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    if ((float)iVar1 < *(float *)(param_1 + 0x1e8)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    fVar4 = *(float *)(param_1 + 0x1e8);
  }
  else {
    if (*(int *)(param_1 + 0x284) != 0) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    if ((float)iVar1 < *(float *)(param_1 + 0x1e8)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    if (*(float *)(param_1 + 0x1e8) + *(float *)(param_1 + 0x1ec) < (float)iVar1) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_008292fc();
                    /* try { // try from 00a6ae40 to 00b6b077 has its CatchHandler @ 00a6b6c0 */
    if ((float)iVar1 < *(float *)(param_1 + 0x1e4)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_008292fc();
    fVar4 = *(float *)(param_1 + 0x1e4);
  }
  if (fVar4 + *(float *)(param_1 + 0x1d8) < (float)iVar1) {
    return 0;
  }
  return 1;
}

~~~
