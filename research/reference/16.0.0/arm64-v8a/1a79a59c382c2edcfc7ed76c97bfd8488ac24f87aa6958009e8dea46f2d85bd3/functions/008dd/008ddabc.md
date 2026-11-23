# 008ddabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `008a9c24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a9c24.md) · 移動量 `+0x33e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0010.md#compare-f88279078c47f363be2a65ec09fc6d3d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008ddabc",
  "name": "FUN_008ddabc",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e710bd00e72cca244ed2a96407fa0790520c01418db34b061195ad45c7708c7",
  "source_text_sha256": "2e710bd00e72cca244ed2a96407fa0790520c01418db34b061195ad45c7708c7"
}
~~~

## 呼び出し元

- [008dde04](../008dd/008dde04.md)

## 呼び出し先

- [008dbf84](../008db/008dbf84.md)

## 疑似コード / UTF-8 367 bytes

~~~c

void FUN_008ddabc(long param_1)

{
  int *piVar1;
  undefined8 *puVar2;
  int *piVar3;
  
  puVar2 = (undefined8 *)(*(long *)(param_1 + 0x38) + (long)*(int *)(param_1 + 4) * 0x18);
  piVar1 = (int *)puVar2[1];
  for (piVar3 = (int *)*puVar2; piVar3 != piVar1; piVar3 = piVar3 + 1) {
    FUN_008dbf84(*(long *)(param_1 + 8) + (long)*piVar3 * 0x100);
  }
  return;
}

~~~
