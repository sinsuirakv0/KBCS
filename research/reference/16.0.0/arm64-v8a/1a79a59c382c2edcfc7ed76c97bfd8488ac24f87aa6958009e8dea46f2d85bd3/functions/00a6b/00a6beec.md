# 00a6beec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a0e0d4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e0d4.md) · 移動量 `+0x5de18`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/machine_only_observed-0015.md#compare-a91ec7fa1955f3060d32f975c9904499)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6beec",
  "name": "FUN_00a6beec",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ecd41032274546acef0255d0390cce71921150d0da6e21c420d9701b5696d81e",
  "source_text_sha256": "ecd41032274546acef0255d0390cce71921150d0da6e21c420d9701b5696d81e"
}
~~~

## 呼び出し元

- [00a6a8d4](../00a6a/00a6a8d4.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)

## 疑似コード / UTF-8 443 bytes

~~~c

void FUN_00a6beec(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*(byte *)(param_2 + 8) & 1) == 0) {
    uVar2 = *(undefined8 *)(param_2 + 8);
    uVar1 = *(undefined8 *)(param_2 + 0x18);
    param_1[1] = *(undefined8 *)(param_2 + 0x10);
    *param_1 = uVar2;
    param_1[2] = uVar1;
    return;
  }
  FUN_0043bae0(param_1,*(undefined8 *)(param_2 + 0x18),*(undefined8 *)(param_2 + 0x10));
  return;
}

~~~
