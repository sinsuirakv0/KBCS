# 00bc0eec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b52588`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52588.md) · 移動量 `+0x6e964`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0065.md#compare-909668c482a5af66ba4b7b30e404ba0b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc0eec",
  "name": "_INIT_287",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aaa99cbe98d3db842b74fee27c340d156e2491a7111eab2812850f24732a6350",
  "source_text_sha256": "aaa99cbe98d3db842b74fee27c340d156e2491a7111eab2812850f24732a6350"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a7c0](../00c5a/00c5a7c0.md)

## 関連文字列（未確認候補）

~~~text
"remote_config"
~~~

## 疑似コード / UTF-8 203 bytes

~~~c

void _INIT_287(void)

{
  DAT_01126010 = "remote_config";
  DAT_01126018 = FUN_00bc0e44;
  DAT_01126020 = FUN_00bc0e4c;
  DAT_01126028 = 0;
  _ZN8firebase11AppCallback11AddCallbackEPS0_();
  return;
}

~~~
