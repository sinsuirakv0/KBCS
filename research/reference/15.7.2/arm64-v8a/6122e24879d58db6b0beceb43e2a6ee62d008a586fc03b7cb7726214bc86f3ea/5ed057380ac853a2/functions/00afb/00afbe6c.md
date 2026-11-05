# 00afbe6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afbe6c.md)

## 関数情報

~~~json
{
  "address": "00afbe6c",
  "name": "_ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3d206ec3bdaedb96924588e5ab21d61f73577f4552f14b94e02494f013991868",
  "source_text_sha256": "3d206ec3bdaedb96924588e5ab21d61f73577f4552f14b94e02494f013991868"
}
~~~
## 呼び出し元

- [00bdeb70](../00bde/00bdeb70.md)

## 呼び出し先

- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bdeb40](../00bde/00bdeb40.md)

## 疑似コード 1/1 / UTF-8 3232 bytes

~~~c

int _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv(long param_1)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  long lVar4;
  long *plVar5;
  char cVar6;
  bool bVar7;
  long lVar8;
  int iVar9;
  long *plVar10;
  long *plVar11;
  
  lVar1 = param_1 + 0x18;
                    /* try { // try from 00afbe88 to 00bfbe93 has its CatchHandler @ 00b0044c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  lVar8 = *(long *)(param_1 + 0x10);
                    /* try { // try from 00afbe98 to 00bfbea3 has its CatchHandler @ 00b00444 */
  if (lVar8 == 0) {
    iVar9 = 0;
  }
  else {
    iVar9 = 0;
    do {
      plVar10 = *(long **)(param_1 + 8);
      lVar3 = plVar10[2];
      plVar5 = (long *)plVar10[3];
                    /* try { // try from 00afbeb4 to 00bfbec7 has its CatchHandler @ 00b00448 */
      if (plVar5 != (long *)0x0) {
        plVar10 = plVar5 + 1;
        do {
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar10,0x10);
          if (bVar7) {
            *plVar10 = *plVar10 + 1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        plVar10 = *(long **)(param_1 + 8);
        lVar8 = *(long *)(param_1 + 0x10);
      }
      lVar4 = *plVar10;
      *(long *)(lVar4 + 8) = plVar10[1];
      *(long *)plVar10[1] = lVar4;
      *(long *)(param_1 + 0x10) = lVar8 + -1;
      plVar11 = (long *)plVar10[3];
      if (plVar11 != (long *)0x0) {
        plVar2 = plVar11 + 1;
        do {
          lVar8 = *plVar2;
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar2,0x10);
          if (bVar7) {
            *plVar2 = lVar8 + -1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        if (lVar8 == 0) {
          (**(code **)(*plVar11 + 0x10))(plVar11);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
        }
      }
      _ZdlPv(plVar10);
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* try { // try from 00afbf34 to 00bfbf47 has its CatchHandler @ 00b0040c */
      _ZN8firebase8callback13CallbackEntry7ExecuteEv(lVar3);
      iVar9 = iVar9 + 1;
      _ZN8firebase5Mutex7AcquireEv(lVar1);
      if (plVar5 != (long *)0x0) {
                    /* try { // try from 00afbf48 to 00bfbf4f has its CatchHandler @ 00b003f4 */
        plVar10 = plVar5 + 1;
        do {
          lVar8 = *plVar10;
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar10,0x10);
          if (bVar7) {
            *plVar10 = lVar8 + -1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        if (lVar8 == 0) {
          (**(code **)(*plVar5 + 0x10))(plVar5);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
                    /* try { // try from 00afbf78 to 00bfbf8b has its CatchHandler @ 00b003d0 */
        }
      }
                    /* try { // try from 00afbea4 to 00bfbeb3 has its CatchHandler @ 00b00440 */
      lVar8 = *(long *)(param_1 + 0x10);
    } while (lVar8 != 0);
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* try { // try from 00afbf8c to 00bfbfa7 has its CatchHandler @ 00b003b0 */
  return iVar9;
}

~~~
