# 00b5cedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00b5cedc",
  "name": "_ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nodeIS7_S5_EElEEEE",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc87efcc994811e8fea46e0758069651d6d7c8cf937451f30e5f10e94a309ca8",
  "source_text_sha256": "cc87efcc994811e8fea46e0758069651d6d7c8cf937451f30e5f10e94a309ca8"
}
~~~

## 呼び出し元

- [00c5bc70](../00c5b/00c5bc70.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c58010](../00c58/00c58010.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5b6a0](../00c5b/00c5b6a0.md)

## 疑似コード / UTF-8 6277 bytes

~~~c

void _ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nodeIS7_S5_EElEEEE
               (void *param_1)

{
  long *plVar1;
  long lVar2;
  long lVar3;
  size_t __n;
  undefined8 *puVar4;
  long *plVar5;
  long *plVar6;
  long lVar7;
  undefined8 uVar8;
  long *plVar9;
  
                    /* catch() { ... } // from try @ 00b572a8 with catch @ 00b5cedc */
                    /* catch() { ... } // from try @ 00b57248 with catch @ 00b5cee0 */
                    /* catch() { ... } // from try @ 00b5723c with catch @ 00b5cee4 */
                    /* catch() { ... } // from try @ 00b571b8 with catch @ 00b5cee8 */
                    /* catch() { ... } // from try @ 00b571ac with catch @ 00b5ceec */
                    /* catch() { ... } // from try @ 00b57138 with catch @ 00b5cef0 */
                    /* catch() { ... } // from try @ 00b5712c with catch @ 00b5cef4 */
                    /* catch() { ... } // from try @ 00b5711c with catch @ 00b5cef8 */
  uVar8 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c9b868;
                    /* catch() { ... } // from try @ 00b570f4 with catch @ 00b5cf00 */
  _ZN8firebase5Mutex7AcquireEv(uVar8);
                    /* catch() { ... } // from try @ 00b57090 with catch @ 00b5cf04 */
                    /* catch() { ... } // from try @ 00b57084 with catch @ 00b5cf08 */
  lVar2 = *(long *)((long)param_1 + 0x20);
  lVar3 = *(long *)((long)param_1 + 0x28);
                    /* catch() { ... } // from try @ 00b57074 with catch @ 00b5cf0c */
                    /* catch() { ... } // from try @ 00b5704c with catch @ 00b5cf14 */
  puVar4 = *(undefined8 **)PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c9b860;
                    /* catch() { ... } // from try @ 00b57010 with catch @ 00b5cf18 */
  plVar6 = *(long **)((long)param_1 + 8);
  if (*(long **)((long)param_1 + 8) == (long *)0x0) {
                    /* catch() { ... } // from try @ 00b57004 with catch @ 00b5cf30 */
    plVar6 = (long *)((long)param_1 + 0x10);
    plVar5 = (long *)*plVar6;
    if ((void *)*plVar5 != param_1) {
      do {
        lVar7 = *plVar6;
        plVar6 = (long *)(lVar7 + 0x10);
        plVar5 = (long *)*plVar6;
                    /* catch() { ... } // from try @ 00b56ff4 with catch @ 00b5cf50 */
      } while (*plVar5 != lVar7);
    }
  }
  else {
    do {
      plVar5 = plVar6;
      plVar6 = (long *)*plVar5;
    } while ((long *)*plVar5 != (long *)0x0);
  }
                    /* catch() { ... } // from try @ 00b56fcc with catch @ 00b5cf58 */
                    /* catch() { ... } // from try @ 00b56f70 with catch @ 00b5cf5c */
                    /* catch() { ... } // from try @ 00b56f64 with catch @ 00b5cf60 */
  if ((void *)*puVar4 == param_1) {
                    /* catch() { ... } // from try @ 00b56f04 with catch @ 00b5cf64 */
    *puVar4 = plVar5;
  }
                    /* catch() { ... } // from try @ 00b56ef8 with catch @ 00b5cf68 */
                    /* catch() { ... } // from try @ 00b56e74 with catch @ 00b5cf6c */
                    /* catch() { ... } // from try @ 00b56e68 with catch @ 00b5cf70 */
                    /* catch() { ... } // from try @ 00b56e0c with catch @ 00b5cf74 */
  puVar4[2] = puVar4[2] + -1;
                    /* catch() { ... } // from try @ 00b56e00 with catch @ 00b5cf78 */
  _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_(puVar4[1],param_1);
                    /* catch() { ... } // from try @ 00b56d7c with catch @ 00b5cf7c */
                    /* catch() { ... } // from try @ 00b56d70 with catch @ 00b5cf80 */
  _ZdlPv(param_1);
                    /* catch() { ... } // from try @ 00b56d10 with catch @ 00b5cf84 */
  plVar6 = *(long **)(lVar3 + 0x48);
  plVar5 = *(long **)(lVar3 + 0x50);
                    /* catch() { ... } // from try @ 00b56d04 with catch @ 00b5cf88 */
                    /* catch() { ... } // from try @ 00b56c80 with catch @ 00b5cf8c */
                    /* catch() { ... } // from try @ 00b56c74 with catch @ 00b5cf90 */
                    /* catch() { ... } // from try @ 00b56c14 with catch @ 00b5cf94 */
                    /* catch() { ... } // from try @ 00b56c08 with catch @ 00b5cf98 */
  if ((plVar6 != plVar5) && (*plVar6 != lVar2)) {
                    /* catch() { ... } // from try @ 00b56b7c with catch @ 00b5cf9c */
    plVar9 = plVar6;
    do {
                    /* catch() { ... } // from try @ 00b56b70 with catch @ 00b5cfa0 */
      plVar6 = plVar5;
                    /* catch() { ... } // from try @ 00b56b00 with catch @ 00b5cfa4 */
      if (plVar5 + -1 == plVar9) break;
      plVar1 = plVar9 + 1;
                    /* catch() { ... } // from try @ 00b56af4 with catch @ 00b5cfa8 */
                    /* catch() { ... } // from try @ 00b56860 with catch @ 00b5cfac */
      plVar6 = plVar9 + 1;
                    /* catch() { ... } // from try @ 00b56830 with catch @ 00b5cfb0 */
                    /* catch() { ... } // from try @ 00b5680c with catch @ 00b5cfb4 */
      plVar9 = plVar6;
                    /* catch() { ... } // from try @ 00b567dc with catch @ 00b5cfb8 */
    } while (*plVar1 != lVar2);
  }
  __n = (long)plVar5 - (long)(plVar6 + 1);
                    /* catch() { ... } // from try @ 00b5670c with catch @ 00b5cfd4 */
  if (__n != 0) {
                    /* catch() { ... } // from try @ 00b5668c with catch @ 00b5cfd8 */
                    /* catch() { ... } // from try @ 00b56654 with catch @ 00b5cfdc */
    memmove(plVar6,plVar6 + 1,__n);
  }
                    /* catch() { ... } // from try @ 00b5661c with catch @ 00b5cfe4 */
  *(long **)(lVar3 + 0x50) = plVar6 + ((long)__n >> 3);
                    /* catch() { ... } // from try @ 00b565a4 with catch @ 00b5cfe8 */
                    /* catch() { ... } // from try @ 00b56598 with catch @ 00b5cfec */
                    /* catch() { ... } // from try @ 00b56540 with catch @ 00b5cff0 */
                    /* catch() { ... } // from try @ 00b56534 with catch @ 00b5cff4 */
                    /* catch() { ... } // from try @ 00b564d4 with catch @ 00b5cff8 */
  _ZN8firebase5Mutex7ReleaseEv(uVar8);
  return;
}

~~~
