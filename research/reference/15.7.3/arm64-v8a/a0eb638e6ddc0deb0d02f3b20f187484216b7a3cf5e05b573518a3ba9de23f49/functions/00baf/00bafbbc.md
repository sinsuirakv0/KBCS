# 00bafbbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bafaf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafaf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0078.md#compare-3443b2096fbdb04f33987723463bd0bb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafbbc",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0a70d9c0e8d33346251f1a55172e67db7ae130e612c7f1d5a1fef0c5f8093ef",
  "source_text_sha256": "b0a70d9c0e8d33346251f1a55172e67db7ae130e612c7f1d5a1fef0c5f8093ef"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bafc28](../00baf/00bafc28.md)
- [00bdafb0](../00bda/00bdafb0.md)
- [00bdafd0](../00bda/00bdafd0.md)

## 疑似コード / UTF-8 404 bytes

~~~c

undefined1 * _ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv(void)

{
  int iVar1;
  
  if (((DAT_010a2b68 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_010a2b68), iVar1 != 0)) {
    FUN_00bafc28();
    DAT_010a2b60 = &DAT_010a2c60;
    __cxa_guard_release(&DAT_010a2b68);
                    /* try { // try from 00bafc24 to 00cafc73 has its CatchHandler @ 00bb0dc8 */
  }
  return DAT_010a2b60;
}

~~~
