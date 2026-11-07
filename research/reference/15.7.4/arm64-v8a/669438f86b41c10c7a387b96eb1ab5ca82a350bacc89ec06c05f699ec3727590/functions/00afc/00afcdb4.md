# 00afcdb4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00afcca8`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcca8.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00afcdb4",
  "name": "_ZN8firebase15CleanupNotifier11FindByOwnerEPv",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95f82c14743897158d2e38d6baf3674df35470d5ab1ca161513d8e0f2380a231",
  "source_text_sha256": "95f82c14743897158d2e38d6baf3674df35470d5ab1ca161513d8e0f2380a231"
}
~~~

## 呼び出し元

- [00bddd90](../00bdd/00bddd90.md)

## 呼び出し先

- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)

## 疑似コード / UTF-8 1334 bytes

~~~c

long _ZN8firebase15CleanupNotifier11FindByOwnerEPv(ulong param_1)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  undefined8 uVar4;
  long lVar5;
  
  uVar4 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b998;
  _ZN8firebase5Mutex7AcquireEv(uVar4);
                    /* try { // try from 00afcddc to 00bfcde3 has its CatchHandler @ 00aff400 */
  if (*(long *)PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b990 != 0) {
    plVar1 = (long *)(*(long *)
                       PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b990 + 8)
    ;
    plVar3 = (long *)*plVar1;
    plVar2 = plVar1;
    if (plVar3 != (long *)0x0) {
      do {
        if ((ulong)plVar3[4] >= param_1) {
          plVar2 = plVar3;
        }
        plVar3 = (long *)plVar3[(ulong)plVar3[4] < param_1];
      } while (plVar3 != (long *)0x0);
                    /* try { // try from 00afce0c to 00bfce23 has its CatchHandler @ 00aff3fc */
      if ((plVar2 != plVar1) && ((ulong)plVar2[4] <= param_1)) {
        lVar5 = plVar2[5];
        goto LAB_00afce24;
      }
    }
  }
  lVar5 = 0;
LAB_00afce24:
                    /* try { // try from 00afce24 to 00bfcebf has its CatchHandler @ 00af5650 */
  _ZN8firebase5Mutex7ReleaseEv(uVar4);
  return lVar5;
}

~~~
