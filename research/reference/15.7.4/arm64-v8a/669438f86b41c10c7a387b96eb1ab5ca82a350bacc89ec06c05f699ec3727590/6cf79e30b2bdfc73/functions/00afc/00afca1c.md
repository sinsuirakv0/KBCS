# 00afca1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00afca1c.md)

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

## 疑似コード 1/1 / UTF-8 1309 bytes

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
