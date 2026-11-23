# 006feeac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `006feeac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fe/006feeac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/no_difference_in_scope-0009.md#compare-f1f9e45d1def406090f1d3756a7f9688)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006feeac",
  "name": "FUN_006feeac",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b5f2d284329b7dc26293869f955ea6a7af6b745822d1782dba3fbfb9296be827",
  "source_text_sha256": "b5f2d284329b7dc26293869f955ea6a7af6b745822d1782dba3fbfb9296be827"
}
~~~

## 呼び出し元

- [00734830](../00734/00734830.md)
- [0073496c](../00734/0073496c.md)
- [0073fa38](../0073f/0073fa38.md)
- [00749514](../00749/00749514.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 175 bytes

~~~c

undefined4 FUN_006feeac(int param_1)

{
  if (param_1 + 0x1aU < 0x1f) {
    return *(undefined4 *)(&DAT_002d02d8 + (ulong)(param_1 + 0x1aU) * 4);
  }
  return 0xffffffff;
}

~~~
