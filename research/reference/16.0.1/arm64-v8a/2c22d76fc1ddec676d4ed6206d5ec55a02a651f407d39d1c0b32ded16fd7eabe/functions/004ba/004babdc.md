# 004babdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `004bab9c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004bab9c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0006.md#compare-c10fbb60458d02671026e6cbf8a8eaaa)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0006.md#compare-6caa57ce40d8a7b0bf89ad39f7784613)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004babdc",
  "name": "_ZN5Botan6BigIntC1Em",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a3843c37d2054e7e4b5a5594349ca285909d1c3c07092c844ab9e9eedf49b7c",
  "source_text_sha256": "4a3843c37d2054e7e4b5a5594349ca285909d1c3c07092c844ab9e9eedf49b7c"
}
~~~

## 呼び出し元

- [00c58920](../00c58/00c58920.md)

## 呼び出し先

- [00540920](../00540/00540920.md)

## 疑似コード / UTF-8 253 bytes

~~~c

void _ZN5Botan6BigIntC1Em(undefined8 *param_1,long param_2)

{
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  *(undefined4 *)(param_1 + 3) = 1;
  if (param_2 != 0) {
    FUN_00540920(param_1,8);
    *(long *)*param_1 = param_2;
  }
  return;
}

~~~
