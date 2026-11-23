# 00bef5cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b729c4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b729c4.md) · 移動量 `+0x7cc08`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/detail_skipped-0004.md#compare-f35bf88f4a946344a13fc23dd4d05d14)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bef5cc",
  "name": "_ZNSt6__ndk16chrono12system_clock11from_time_tEl",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17102783bbf409c14dd0b0ae30c6c86da41e6894896b01ce67ab80a856e72733",
  "source_text_sha256": "17102783bbf409c14dd0b0ae30c6c86da41e6894896b01ce67ab80a856e72733"
}
~~~

## 呼び出し元

- [00c58610](../00c58/00c58610.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 103 bytes

~~~c

long _ZNSt6__ndk16chrono12system_clock11from_time_tEl(long param_1)

{
  return param_1 * 1000000;
}

~~~
