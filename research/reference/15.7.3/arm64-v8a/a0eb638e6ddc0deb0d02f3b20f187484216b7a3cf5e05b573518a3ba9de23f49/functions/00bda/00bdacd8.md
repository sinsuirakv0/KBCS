# 00bdacd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 要確認
  - [v15.7.2 → v15.7.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/review-0042.md#review-7cd726866e80200c4c5d96aed6cbf1c5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdacd8",
  "name": "FUN_00bdacd8",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c895b00262d6911d0d5a31a0ec7a2a7d69af6efb6c92338267a1c278f7db5e8b",
  "source_text_sha256": "c895b00262d6911d0d5a31a0ec7a2a7d69af6efb6c92338267a1c278f7db5e8b"
}
~~~

## 呼び出し元

- [00bd7ff4](../00bd7/00bd7ff4.md)

## 呼び出し先

解決済みの記録なし。

## 関連文字列（未確認候補）

~~~text
"unknown register"
~~~

## 疑似コード / UTF-8 279 bytes

~~~c

char * FUN_00bdacd8(int param_1)

{
  if (param_1 + 2U < 0x62) {
                    /* try { // try from 00bdacf0 to 00cdad27 has its CatchHandler @ 00bdad58 */
    return &DAT_002fe11c + *(int *)(&DAT_002fe11c + (ulong)(param_1 + 2U) * 4);
  }
  return "unknown register";
}

~~~
