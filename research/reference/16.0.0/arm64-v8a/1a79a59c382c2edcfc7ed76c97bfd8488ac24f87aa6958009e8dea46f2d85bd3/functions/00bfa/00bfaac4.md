# 00bfaac4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e07c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e07c.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0018.md#compare-442c24666e42997e0bb3aaa845c088e9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaac4",
  "name": "_ZNSt6__ndk117iostream_categoryEv",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc47307183cf9b19063f199a722ee44630cd2e50b5f3a46f3abd52fe6ac612e2",
  "source_text_sha256": "cc47307183cf9b19063f199a722ee44630cd2e50b5f3a46f3abd52fe6ac612e2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)

## 疑似コード / UTF-8 243 bytes

~~~c

undefined ** _ZNSt6__ndk117iostream_categoryEv(void)

{
  int iVar1;
  
  if (((DAT_01126f90 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01126f90), iVar1 != 0)) {
    __cxa_guard_release(&DAT_01126f90);
  }
  return &PTR_PTR_00ca4400;
}

~~~
