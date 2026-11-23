# 00bfaccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e284`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0072.md#compare-204325b95b34b13da586ad880ea0f9bc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaccc",
  "name": "_ZNSt6__ndk18ios_base6xallocEv",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be611626be869c2d9b56120ac6ee844106da033895d85ea4e00bbcdfb7461ee7",
  "source_text_sha256": "be611626be869c2d9b56120ac6ee844106da033895d85ea4e00bbcdfb7461ee7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53880](../00c53/00c53880.md)

## 疑似コード / UTF-8 124 bytes

~~~c

void _ZNSt6__ndk18ios_base6xallocEv(void)

{
  FUN_00c53880(1,PTR__ZNSt6__ndk18ios_base9__xindex_E_00c9b6f8);
  return;
}

~~~
