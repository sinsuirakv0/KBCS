# 00b2bffc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acc56c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc56c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0054.md#compare-021580ec0a2937dfb1c94c6e61cf85c5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2bffc",
  "name": "FUN_00b2bffc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0b3bda01d92781a8ce4f070c697c64b6484d112e668ed2f6307af88f11cdcb64",
  "source_text_sha256": "0b3bda01d92781a8ce4f070c697c64b6484d112e668ed2f6307af88f11cdcb64"
}
~~~

## 呼び出し元

- [0043b618](../0043b/0043b618.md)

## 呼び出し先

- [0043e90c](../0043e/0043e90c.md)
- [0043f4f4](../0043f/0043f4f4.md)
- [0047acb4](../0047a/0047acb4.md)
- [0047b78c](../0047b/0047b78c.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 202 bytes

~~~c

void FUN_00b2bffc(void)

{
  long *plVar1;
  
  plVar1 = (long *)FUN_008514b8();
  (**(code **)(*plVar1 + 0x28))();
  FUN_0047acb4();
  FUN_0047b78c();
  FUN_0043e90c();
  FUN_0043f4f4();
  return;
}

~~~
