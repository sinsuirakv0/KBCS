# 00afc5ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afc5ac",
  "name": "_ZN8firebase15CleanupNotifierD2Ev",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f201b12abb428f434dd0150311560e22a5d990dfa2227484dc6bc45e9602aa2d",
  "source_text_sha256": "f201b12abb428f434dd0150311560e22a5d990dfa2227484dc6bc45e9602aa2d"
}
~~~

## 呼び出し元

- [00bddd80](../00bdd/00bddd80.md)

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bddc00](../00bdd/00bddc00.md)
- [00bddd60](../00bdd/00bddd60.md)
- [00bdeca0](../00bde/00bdeca0.md)
- [00bdecb0](../00bde/00bdecb0.md)
- [00bdecc0](../00bde/00bdecc0.md)

## 疑似コード / UTF-8 2275 bytes

~~~c

void _ZN8firebase15CleanupNotifierD2Ev(long param_1)

{
  undefined *puVar1;
  long lVar2;
  undefined8 uVar3;
  void *pvVar4;
  
  _ZN8firebase5Mutex7AcquireEv();
                    /* try { // try from 00afc5c8 to 00bfc5d3 has its CatchHandler @ 00b003a0 */
  if (*(char *)(param_1 + 0x40) == '\0') {
    lVar2 = *(long *)(param_1 + 0x28);
    while (lVar2 != param_1 + 0x30) {
      uVar3 = *(undefined8 *)(lVar2 + 0x20);
      (**(code **)(lVar2 + 0x28))(uVar3);
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(param_1,uVar3);
      lVar2 = *(long *)(param_1 + 0x28);
                    /* try { // try from 00afc5fc to 00bfc60f has its CatchHandler @ 00b00398 */
    }
    *(undefined1 *)(param_1 + 0x40) = 1;
  }
  _ZN8firebase5Mutex7ReleaseEv(param_1);
                    /* try { // try from 00afc610 to 00bfc61b has its CatchHandler @ 00b00418 */
  _ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv(param_1);
  uVar3 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b948;
  _ZN8firebase5Mutex7AcquireEv(uVar3);
  puVar1 = PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b940;
  pvVar4 = *(void **)PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b940;
  if ((pvVar4 != (void *)0x0) && (*(long *)((long)pvVar4 + 0x10) == 0)) {
                    /* try { // try from 00afc644 to 00bfc667 has its CatchHandler @ 00b00454 */
    _ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_S2_EE
              (pvVar4,*(undefined8 *)((long)pvVar4 + 8));
    _ZdlPv(pvVar4);
    *(undefined8 *)puVar1 = 0;
  }
  _ZN8firebase5Mutex7ReleaseEv(uVar3);
  pvVar4 = *(void **)(param_1 + 0x48);
                    /* try { // try from 00afc668 to 00bfc673 has its CatchHandler @ 00b00408 */
  if (pvVar4 != (void *)0x0) {
    *(void **)(param_1 + 0x50) = pvVar4;
    _ZdlPv(pvVar4);
  }
  _ZNSt6__ndk16__treeINS_12__value_typeIPvPFvS2_EEENS_19__map_value_compareIS2_S5_NS_4lessIS2_EELb1EEENS_9allocatorIS5_EEE7destroyEPNS_11__tree_nodeIS5_S2_EE
            (param_1 + 0x28,*(undefined8 *)(param_1 + 0x30));
  _ZN8firebase5MutexD1Ev(param_1);
  return;
}

~~~
