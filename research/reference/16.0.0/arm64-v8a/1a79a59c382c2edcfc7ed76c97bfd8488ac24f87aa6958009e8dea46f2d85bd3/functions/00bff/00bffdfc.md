# 00bffdfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b833b4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b833b4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/machine_only_observed-0018.md#compare-1fd0ce393278e4d6a11631b36b1d6b18)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffdfc",
  "name": "_ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED1Ev",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fae5a536c38840cfa53e7df8160598f4c8072c4445c980b66165e51d69c93aae",
  "source_text_sha256": "fae5a536c38840cfa53e7df8160598f4c8072c4445c980b66165e51d69c93aae"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5cce0](../00c5c/00c5cce0.md)

## 疑似コード / UTF-8 136 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED1Ev(long param_1)

{
  _ZNSt6__ndk18ios_baseD1Ev(param_1 + 0x10);
  return;
}

~~~
