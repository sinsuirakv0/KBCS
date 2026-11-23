# 00a3eccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `009e1dd0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1dd0.md) · 移動量 `+0x5cefc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0050.md#compare-fbc54dfd1bcdd519d50c6f2b1c6bdb07)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3eccc",
  "name": "FUN_00a3eccc",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c3a949852d9d09b5fb8101efa48d200fafe5bffbdaaeb1a8db622b1352048e9",
  "source_text_sha256": "9c3a949852d9d09b5fb8101efa48d200fafe5bffbdaaeb1a8db622b1352048e9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [006917c0](../00691/006917c0.md)

## 疑似コード / UTF-8 483 bytes

~~~c

void FUN_00a3eccc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  param_2[3] = 0;
  param_2[2] = param_2 + 3;
  param_2[1] = uVar1;
  param_2[4] = 0;
  uVar1 = *(undefined8 *)(param_1 + 0x10);
  *param_2 = &PTR_FUN_00c8b0a8;
  FUN_006917c0(param_2 + 2,uVar1,param_1 + 0x18);
  param_2[6] = 0;
  param_2[5] = param_2 + 6;
  param_2[7] = 0;
  FUN_006917c0(param_2 + 5,*(undefined8 *)(param_1 + 0x28),param_1 + 0x30);
  return;
}

~~~
