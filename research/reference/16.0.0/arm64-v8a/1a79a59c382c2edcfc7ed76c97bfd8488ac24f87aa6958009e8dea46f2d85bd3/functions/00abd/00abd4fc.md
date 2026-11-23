# 00abd4fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a5f544`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f544.md) · 移動量 `+0x5dfb8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0052.md#compare-a5534df28c64d78ba3efeb30e33d9faf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abd4fc",
  "name": "FUN_00abd4fc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b36ccadad6d773697ceeae7865419329ef493c7b26d99c553b3273f43b53d115",
  "source_text_sha256": "b36ccadad6d773697ceeae7865419329ef493c7b26d99c553b3273f43b53d115"
}
~~~

## 呼び出し元

- [0083f844](../0083f/0083f844.md)

## 呼び出し先

- [0046e784](../0046e/0046e784.md)
- [0046eeb8](../0046e/0046eeb8.md)
- [005c175c](../005c1/005c175c.md)

## 疑似コード / UTF-8 955 bytes

~~~c

void FUN_00abd4fc(undefined8 *param_1)

{
  undefined8 *puVar1;
  
  param_1[0xb] = 0;
  puVar1 = param_1 + 10;
  *puVar1 = 0;
  param_1[9] = puVar1;
  param_1[1] = 0;
  *param_1 = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[8] = 0;
  param_1[0x10] = 0;
  param_1[0xf] = 0;
  param_1[0x12] = 0;
  param_1[0x11] = 0;
  param_1[0x14] = 0;
  param_1[0x13] = 0;
  FUN_0046eeb8(param_1 + 0x15);
  FUN_0046e784(param_1 + 0x2a);
                    /* try { // try from 00abd55c to 00bbd64f has its CatchHandler @ 00abd2c0 */
  *(undefined4 *)(param_1 + 0xd) = 0;
  param_1[0xc] = 0;
  param_1[7] = param_1[6];
  FUN_005c175c(param_1 + 9,param_1[10]);
  param_1[10] = 0;
  param_1[0xb] = 0;
  *(undefined4 *)(param_1 + 0xe) = 0xffffffff;
  param_1[9] = puVar1;
  *(undefined1 *)((long)param_1 + 0x6c) = 0;
  param_1[0x10] = param_1[0xf];
  param_1[0x13] = param_1[0x12];
  return;
}

~~~
