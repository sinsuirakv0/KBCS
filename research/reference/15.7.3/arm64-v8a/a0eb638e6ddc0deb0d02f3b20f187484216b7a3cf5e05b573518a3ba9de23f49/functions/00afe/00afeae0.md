# 00afeae0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afeae0",
  "name": "_ZN8firebase26ReferenceCountedFutureImplD1Ev",
  "size": 504,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3c683f8f1fb4d7e6fdee4783b080d152c8f1f89f98e2334e3fe685316f86e09d",
  "source_text_sha256": "3c683f8f1fb4d7e6fdee4783b080d152c8f1f89f98e2334e3fe685316f86e09d"
}
~~~

## 呼び出し元

- [00bddda0](../00bdd/00bddda0.md)
- [00bdedd0](../00bde/00bdedd0.md)

## 呼び出し先

- [00b0129c](../00b01/00b0129c.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bddc00](../00bdd/00bddc00.md)
- [00bddd80](../00bdd/00bddd80.md)
- [00bdde80](../00bdd/00bdde80.md)
- [00bddf10](../00bdd/00bddf10.md)
- [00bde700](../00bde/00bde700.md)
- [00bde8c0](../00bde/00bde8c0.md)
- [00bded80](../00bde/00bded80.md)

## 関連文字列（未確認候補）

~~~text
"Future with handle %d still exists though its backing API 0x%X is being deleted. Please call Future::Release() before deleting the backing API."
~~~

## 疑似コード / UTF-8 4313 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplD1Ev(long *param_1)

{
  long *plVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  long lVar5;
  void *pvVar6;
  ulong uVar7;
  void *pvVar8;
  void *pvVar9;
  
  lVar2 = param_1[10];
  *param_1 = (long)(PTR__ZTVN8firebase26ReferenceCountedFutureImplE_00c1b860 + 0x10);
  if (param_1[0xb] != lVar2) {
    lVar5 = 0;
    uVar7 = 0;
    do {
      lVar2 = lVar2 + lVar5;
      _ZN8firebase5Mutex7AcquireEv(lVar2);
      plVar1 = *(long **)(lVar2 + 0x28);
      if (plVar1 != (long *)0x0) {
        (**(code **)(*plVar1 + 0x60))(plVar1,lVar2);
        (**(code **)(**(long **)(lVar2 + 0x28) + 0x18))(*(long **)(lVar2 + 0x28),lVar2 + 0x30);
        *(undefined8 *)(lVar2 + 0x28) = 0;
      }
      _ZN8firebase5Mutex7ReleaseEv(lVar2);
      lVar2 = param_1[10];
      uVar7 = uVar7 + 1;
      lVar5 = lVar5 + 0x40;
    } while (uVar7 < (ulong)(param_1[0xb] - lVar2 >> 6));
  }
                    /* catch() { ... } // from try @ 00afdd08 with catch @ 00afeb88 */
  _ZN8firebase15CleanupNotifier10CleanupAllEv(param_1 + 0xd);
  _ZN8firebase15CleanupNotifier10CleanupAllEv(param_1 + 0x19);
  plVar1 = param_1 + 6;
  lVar2 = param_1[8];
  while (lVar2 != 0) {
    pvVar9 = (void *)*plVar1;
    _ZN8firebase10LogWarningEPKcz
              ("Future with handle %d still exists though its backing API 0x%X is being deleted. Please call Future::Release() before deleting the backing API."
               ,*(undefined8 *)((long)pvVar9 + 0x20),(ulong)param_1 & 0xffffffff);
    pvVar8 = *(void **)((long)pvVar9 + 0x28);
    plVar4 = *(long **)((long)pvVar9 + 8);
    if (*(long **)((long)pvVar9 + 8) == (long *)0x0) {
      plVar4 = (long *)((long)pvVar9 + 0x10);
      plVar3 = (long *)*plVar4;
      if ((void *)*plVar3 != pvVar9) {
        do {
          lVar2 = *plVar4;
                    /* catch() { ... } // from try @ 00afdce8 with catch @ 00afec04 */
          plVar4 = (long *)(lVar2 + 0x10);
          plVar3 = (long *)*plVar4;
        } while (*plVar3 != lVar2);
      }
    }
    else {
      do {
        plVar3 = plVar4;
                    /* catch() { ... } // from try @ 00afdcfc with catch @ 00afebe4 */
        plVar4 = (long *)*plVar3;
      } while ((long *)*plVar3 != (long *)0x0);
    }
    if ((void *)*plVar1 == pvVar9) {
      *plVar1 = (long)plVar3;
    }
    param_1[8] = param_1[8] + -1;
    _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[7],pvVar9);
    _ZdlPv(pvVar9);
    if (pvVar8 != (void *)0x0) {
      _ZN8firebase17FutureBackingDataD1Ev(pvVar8);
      _ZdlPv(pvVar8);
    }
    lVar2 = param_1[8];
  }
  _ZN8firebase15CleanupNotifierD2Ev(param_1 + 0x19);
                    /* catch() { ... } // from try @ 00afdcdc with catch @ 00afec64 */
  _ZN8firebase15CleanupNotifierD2Ev(param_1 + 0xd);
  pvVar8 = (void *)param_1[10];
  if (pvVar8 != (void *)0x0) {
                    /* catch() { ... } // from try @ 00afdccc with catch @ 00afec74 */
    pvVar6 = (void *)param_1[0xb];
    pvVar9 = pvVar8;
    if (pvVar6 != pvVar8) {
      do {
                    /* catch() { ... } // from try @ 00afdcb8 with catch @ 00afec84 */
        pvVar6 = (void *)((long)pvVar6 + -0x40);
        FUN_00b0129c(param_1 + 0xc,pvVar6);
                    /* catch() { ... } // from try @ 00afdcac with catch @ 00afec94 */
      } while (pvVar8 != pvVar6);
      pvVar9 = (void *)param_1[10];
    }
    param_1[0xb] = (long)pvVar8;
    _ZdlPv(pvVar9);
  }
                    /* catch() { ... } // from try @ 00afdc8c with catch @ 00afecb8 */
  _ZNSt6__ndk16__treeINS_12__value_typeImPN8firebase17FutureBackingDataEEENS_19__map_value_compareImS5_NS_4lessImEELb1EEENS_9allocatorIS5_EEE7destroyEPNS_11__tree_nodeIS5_PvEE
            (plVar1,param_1[7]);
                    /* catch() { ... } // from try @ 00afdc7c with catch @ 00afecbc */
                    /* catch() { ... } // from try @ 00afdc64 with catch @ 00afecc4 */
                    /* catch() { ... } // from try @ 00afdc60 with catch @ 00afecc8 */
                    /* catch() { ... } // from try @ 00afdbc0 with catch @ 00afeccc */
                    /* catch() { ... } // from try @ 00afdbb0 with catch @ 00afecd0 */
                    /* catch() { ... } // from try @ 00afdb40 with catch @ 00afecd4 */
  _ZN8firebase5MutexD1Ev(param_1 + 1);
  return;
}

~~~
