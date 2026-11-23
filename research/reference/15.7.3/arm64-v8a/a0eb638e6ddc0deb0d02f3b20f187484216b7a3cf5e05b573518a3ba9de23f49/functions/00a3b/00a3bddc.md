# 00a3bddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a3bddc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a3b/00a3bddc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/machine_only_observed-0040.md#compare-5313d271479e581393ca6ee577a7c0c2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3bddc",
  "name": "FUN_00a3bddc",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4f63d3d92b2d7da3765b5aa8405437a901c5e308177673d2e77e15faae6f5db",
  "source_text_sha256": "e4f63d3d92b2d7da3765b5aa8405437a901c5e308177673d2e77e15faae6f5db"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

## 疑似コード / UTF-8 1044 bytes

~~~c

void FUN_00a3bddc(long param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  
  puVar2 = *(undefined8 **)(param_1 + 0x28);
  if (puVar2 != (undefined8 *)0x0) {
    puVar3 = *(undefined8 **)(param_1 + 0x30);
    puVar1 = puVar2;
    if (puVar3 != puVar2) {
      do {
        puVar3 = puVar3 + -3;
        if ((void *)*puVar3 != (void *)0x0) {
          _ZdlPv((void *)*puVar3);
        }
      } while (puVar3 != puVar2);
      puVar1 = *(undefined8 **)(param_1 + 0x28);
    }
    *(undefined8 **)(param_1 + 0x30) = puVar2;
    _ZdlPv(puVar1);
  }
  puVar2 = *(undefined8 **)(param_1 + 0x10);
  if (puVar2 == (undefined8 *)0x0) {
    return;
  }
  puVar3 = *(undefined8 **)(param_1 + 0x18);
  puVar1 = puVar2;
  if (puVar3 != puVar2) {
    do {
      puVar3 = puVar3 + -3;
      if ((void *)*puVar3 != (void *)0x0) {
        _ZdlPv((void *)*puVar3);
      }
    } while (puVar3 != puVar2);
    puVar1 = *(undefined8 **)(param_1 + 0x10);
  }
  *(undefined8 **)(param_1 + 0x18) = puVar2;
  _ZdlPv(puVar1);
  return;
}

~~~
