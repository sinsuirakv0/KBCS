# 00aca5ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6c658`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6c658.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0053.md#compare-78dee9fdbcd15a4bda36d3ffc8bc33cb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aca5ec",
  "name": "FUN_00aca5ec",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b4ca553e52312c8304e84a7039b242732cd95da5214a33d2ba3a0feefdb30d1",
  "source_text_sha256": "1b4ca553e52312c8304e84a7039b242732cd95da5214a33d2ba3a0feefdb30d1"
}
~~~

## 呼び出し元

- [00789da0](../00789/00789da0.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008cb4a8](../008cb/008cb4a8.md)
- [008feea4](../008fe/008feea4.md)
- [00a3e32c](../00a3e/00a3e32c.md)
- [00ac08a0](../00ac0/00ac08a0.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)
- [008b6d58](../008b6/008b6d58.md)
- [008b7984](../008b7/008b7984.md)

## 疑似コード / UTF-8 308 bytes

~~~c

void FUN_00aca5ec(long param_1)

{
  long lVar1;
  undefined8 uVar2;
  
  if ((*(int *)(param_1 + 4) != -1) && (*(char *)(param_1 + 0x14) == '\0')) {
    lVar1 = FUN_008514b8();
    uVar2 = FUN_008b7984(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 4));
    FUN_008b6d58(uVar2,0,0);
    return;
  }
  return;
}

~~~
