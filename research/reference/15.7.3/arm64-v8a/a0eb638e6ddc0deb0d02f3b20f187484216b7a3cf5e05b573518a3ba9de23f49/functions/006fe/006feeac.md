# 006feeac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `006feeac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fe/006feeac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/no_difference_in_scope-0009.md#compare-a6f4b60c99369c132a258cc20215de6b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

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
