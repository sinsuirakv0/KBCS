# 00afca1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afc9d8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc9d8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0008.md#compare-1330c214fac95c849f80a84c85e4bd5c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afca1c",
  "name": "_ZN8firebase15CleanupNotifier15UnregisterOwnerEPS0_Pv",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b620b0fceecefbdced7de3aa7d59bc9c69701e1a4cf19b763a35a7108d72f10d",
  "source_text_sha256": "b620b0fceecefbdced7de3aa7d59bc9c69701e1a4cf19b763a35a7108d72f10d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)
- [00bdece0](../00bde/00bdece0.md)

## 疑似コード / UTF-8 1309 bytes

~~~c

void _ZN8firebase15CleanupNotifier15UnregisterOwnerEPS0_Pv(undefined8 param_1,ulong param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  undefined8 uVar4;
  
  uVar4 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b998;
  _ZN8firebase5Mutex7AcquireEv(uVar4);
                    /* try { // try from 00afca40 to 00bfca47 has its CatchHandler @ 00aff42c */
  plVar2 = (long *)(*(long *)
                     PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b990 + 8);
  plVar3 = (long *)*plVar2;
  plVar1 = plVar2;
  if (plVar3 != (long *)0x0) {
    do {
      if ((ulong)plVar3[4] >= param_2) {
        plVar1 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < param_2];
    } while (plVar3 != (long *)0x0);
                    /* try { // try from 00afca70 to 00bfca87 has its CatchHandler @ 00aff428 */
    if ((plVar1 != plVar2) && ((ulong)plVar1[4] <= param_2)) {
      _ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nodeIS7_S5_EElEEEE
                ();
    }
  }
                    /* try { // try from 00afca88 to 00bfcb2b has its CatchHandler @ 00af5650 */
  _ZN8firebase5Mutex7ReleaseEv(uVar4);
  return;
}

~~~
