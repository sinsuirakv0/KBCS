# 00aadba4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aadadc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aadadc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/inspection-0001.md#compare-887fcd8fc55585724330c43ed19c6195)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadba4",
  "name": "FUN_00aadba4",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04c9925987a712cc17d08fb1a44789bcd8a741cb1a1d23efdd1474a9e73cbea5",
  "source_text_sha256": "04c9925987a712cc17d08fb1a44789bcd8a741cb1a1d23efdd1474a9e73cbea5"
}
~~~

## 呼び出し元

- [00aac358](../00aac/00aac358.md)

## 呼び出し先

- [00471738](../00471/00471738.md)
- [00bdb010](../00bdb/00bdb010.md)

## 疑似コード / UTF-8 1251 bytes

~~~c

undefined8 * FUN_00aadba4(undefined8 *param_1,undefined8 *param_2)

{
  bool bVar1;
  void *__ptr;
  undefined8 *puVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  
  puVar5 = param_2;
  puVar2 = (undefined8 *)param_2[1];
  if ((undefined8 *)param_2[1] == (undefined8 *)0x0) {
    do {
      puVar4 = (undefined8 *)puVar5[2];
      bVar1 = (undefined8 *)*puVar4 != puVar5;
      puVar5 = puVar4;
    } while (bVar1);
  }
  else {
    do {
      puVar4 = puVar2;
      puVar2 = (undefined8 *)*puVar4;
    } while ((undefined8 *)*puVar4 != (undefined8 *)0x0);
  }
  if ((void *)*param_1 == param_2) {
    *param_1 = puVar4;
  }
  param_1[2] = param_1[2] + -1;
  FUN_00471738(param_1[1],param_2);
  puVar5 = (undefined8 *)param_2[5];
  if (puVar5 != (undefined8 *)0x0) {
    puVar3 = (undefined8 *)param_2[6];
    puVar2 = puVar5;
    if (puVar3 != puVar5) {
      do {
        puVar2 = puVar3 + -3;
        __ptr = (void *)*puVar2;
        if (__ptr != (void *)0x0) {
          puVar3[-2] = __ptr;
          _ZdlPv(__ptr);
        }
        puVar3 = puVar2;
      } while (puVar2 != puVar5);
      puVar2 = (undefined8 *)param_2[5];
    }
    param_2[6] = puVar5;
    _ZdlPv(puVar2);
  }
  _ZdlPv(param_2);
  return puVar4;
}

~~~
