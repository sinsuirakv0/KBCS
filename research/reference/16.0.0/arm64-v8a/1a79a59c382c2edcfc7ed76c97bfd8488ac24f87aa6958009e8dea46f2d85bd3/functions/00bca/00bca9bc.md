# 00bca9bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5b4bc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b4bc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/inspection-0019.md#compare-43ceeeb225a333ea47f309a6cfe430fe)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bca9bc",
  "name": "_ZN8firebase4auth4AuthD1Ev",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "24ea105ea03fed0548be79cb4a5abe623bea50a6c8ec0f767ed972224ff698b6",
  "source_text_sha256": "24ea105ea03fed0548be79cb4a5abe623bea50a6c8ec0f767ed972224ff698b6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5d630](../00c5d/00c5d630.md)

## 疑似コード / UTF-8 101 bytes

~~~c

void _ZN8firebase4auth4AuthD1Ev(void)

{
  _ZN8firebase4auth4Auth14DeleteInternalEv();
  return;
}

~~~
