# 00bcbeb0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c9b0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9b0.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/inspection-0019.md#compare-43ade96bd95729efa387ef77804cd81d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbeb0",
  "name": "_ZNK8firebase4auth4UserneERKS1_",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2913831d54303c2433eff895af8bc88f8fb5d1ca167486668c33f8c0ee299d7a",
  "source_text_sha256": "2913831d54303c2433eff895af8bc88f8fb5d1ca167486668c33f8c0ee299d7a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a660](../00c5a/00c5a660.md)

## 疑似コード / UTF-8 247 bytes

~~~c

uint _ZNK8firebase4auth4UserneERKS1_(undefined8 param_1,undefined8 param_2)

{
  uint uVar1;
  uint uVar2;
  
  uVar1 = _ZNK8firebase4auth4User8is_validEv();
  uVar2 = _ZNK8firebase4auth4User8is_validEv(param_2);
  return (uVar1 ^ uVar2) & 1;
}

~~~
